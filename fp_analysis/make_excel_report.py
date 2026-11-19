#!/usr/bin/env python3
"""Excel report for one FP titration plate: raw data, every calculation as a live formula, K_d fit, line chart.

  python3 -I make_excel_report.py RESULT.xlsx layout.json OUT.xlsx --label "Buf-2" --apt-nM 5 [--g 1.05] [--exclude B7,C2]

Sheets: Summary (settings, results, checks, chart) | Raw data | Blank | Wells | Groups | Fit | Curve.
All numbers after the raw data are Excel formulas, so changing G, the blank, or the fit parameters updates everything.
The best-fit parameters on the Fit sheet are values; to re-fit in Excel use Data > Solver (minimise the SSE cell by
changing the three or four parameter cells).  The confidence intervals on the Summary sheet are static values
computed by this script (nonlinear least squares and a bootstrap over wells).
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import xlsxwriter
from scipy.optimize import curve_fit
from scipy import stats
from xlsxwriter.utility import xl_rowcol_to_cell as rc, xl_col_to_name

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fp_analysis as fp

NM_PER_UG = 17.14
LET = "ABCDEFGH"


def wname(w):
    return f"{LET[w[0]]}{w[1] + 1}"


def hyp(c, a, b, k):
    return a + (b - a) * c / (k + c)


def hill(c, a, b, k, n):
    return a + (b - a) * c ** n / (k ** n + c ** n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("xlsx"); ap.add_argument("layout"); ap.add_argument("out")
    ap.add_argument("--label", default="Buf-2"); ap.add_argument("--apt-nM", type=float, default=5)
    ap.add_argument("--g", type=float, default=1.05); ap.add_argument("--exclude", default="")
    ap.add_argument("--no-cache", action="store_true", help="write formulas without cached values (used to test them)")
    a = ap.parse_args()

    lay = json.loads(Path(a.layout).read_text())
    hdr, tabs = fp.parse_export(a.xlsx)
    par, perp = tabs["raw_par"], tabs["raw_perp"]
    G, TOL = a.g, 0.25
    excl = set(fp.expand_wells(a.exclude)) if a.exclude else set()
    g_file = fp.header_g(hdr)

    # ---------------- groups (ascending VLP, aptamer alone first) ----------------
    groups = [dict(name="aptamer alone", conc=0.0, wells=fp.expand_wells(lay["free"]))]
    for g in sorted(lay["titration"], key=lambda x: x["conc"]):
        groups.append(dict(name=f"VLP {g['conc']:g}", conc=float(g["conc"]), wells=fp.expand_wells(g["wells"])))
    blank_wells = [w for g in sorted(lay["titration"], key=lambda x: x["conc"], reverse=True) for w in fp.expand_wells(g["blank_wells"])]
    blank_conc = {w: g["conc"] for g in lay["titration"] for w in fp.expand_wells(g["blank_wells"])}

    # ---------------- numbers (cached values + fits) ----------------
    bp = float(np.median([par[w] for w in blank_wells])); bs = float(np.median([perp[w] for w in blank_wells]))
    rows = []
    for g in groups:
        gross = [G * par[w] + 2 * perp[w] for w in g["wells"]]
        med = float(np.median(gross))
        for w, gt in zip(g["wells"], gross):
            netp, nets = par[w] - bp, perp[w] - bs
            gp = G * netp
            rows.append(dict(well=w, group=g["name"], conc=g["conc"], par=par[w], perp=perp[w], netp=netp, nets=nets, gp=gp,
                             mp=1000 * (gp - nets) / (gp + nets), nettot=gp + 2 * nets, gross=gt, med=med,
                             flag=("flag" if (abs(gt - med) > TOL * med or w in excl) else "ok")))
    ok = [r for r in rows if r["flag"] == "ok"]
    c_all = np.array([r["conc"] for r in ok]); y_all = np.array([r["mp"] for r in ok])
    lo, hi = [0, 0, 0.01], [300, 800, 500]
    p1, c1 = curve_fit(hyp, c_all, y_all, p0=[45, 250, 3], bounds=(lo, hi), maxfev=20000)
    p2, c2 = curve_fit(hill, c_all, y_all, p0=[45, 250, 3, 1], bounds=(lo + [0.5], hi + [8]), maxfev=20000)
    dof1, dof2 = len(y_all) - 3, len(y_all) - 4
    se1, se2 = np.sqrt(np.diag(c1)), np.sqrt(np.diag(c2))
    ci1 = (max(p1[2] - stats.t.ppf(.975, dof1) * se1[2], 0), p1[2] + stats.t.ppf(.975, dof1) * se1[2])
    ci2 = (max(p2[2] - stats.t.ppf(.975, dof2) * se2[2], 0), p2[2] + stats.t.ppf(.975, dof2) * se2[2])
    rng = np.random.default_rng(1); by = {}
    for r in ok: by.setdefault(r["conc"], []).append(r["mp"])
    boot = []
    for _ in range(2000):
        cc, yy = [], []
        for k, v in by.items():
            s = rng.choice(v, len(v)); cc += [k] * len(v); yy += list(s)
        try:
            pb, _ = curve_fit(hyp, np.array(cc), np.array(yy), p0=[45, 250, 3], bounds=(lo, hi), maxfev=5000); boot.append(pb[2])
        except Exception:
            pass
    bq = np.percentile(boot, [2.5, 50, 97.5])

    # ---------------- workbook ----------------
    wb = xlsxwriter.Workbook(a.out)
    F = lambda **k: wb.add_format({"font_name": "Arial", "font_size": 10, **k})
    f_txt, f_b = F(), F(bold=True)
    f_h = F(bold=True, bg_color="#1F4E79", font_color="white", border=1, text_wrap=True, valign="vcenter")
    f_t = F(bold=True, font_size=14)
    f_in = F(bg_color="#FFF2CC", border=1, num_format="0.000")  # editable input
    f_n0, f_n1, f_n2, f_n3 = F(num_format="0"), F(num_format="0.0"), F(num_format="0.00"), F(num_format="0.000")
    f_note = F(italic=True, font_color="#555555", text_wrap=True, valign="top")
    f_wrap = F(text_wrap=True, valign="top")
    f_good = F(bold=True, font_color="#1F4E79", num_format="0.00")

    def fx(ws, cell, formula, fmt, value):
        ws.write_formula(cell, formula, fmt, 0 if a.no_cache else value)

    S = wb.add_worksheet("Summary"); RD = wb.add_worksheet("Raw data"); BL = wb.add_worksheet("Blank")
    WL = wb.add_worksheet("Wells"); GR = wb.add_worksheet("Groups"); FT = wb.add_worksheet("Fit"); CV = wb.add_worksheet("Curve")

    # ---- Summary: settings block (named inputs) ----
    S.set_column("A:A", 60); S.set_column("B:B", 17); S.set_column("C:G", 15)
    def note(row, text):
        S.merge_range(row - 1, 2, row - 1, 6, text, f_note); S.set_row(row - 1, 30)
    S.write("A1", f"{a.label} aptamer ({a.apt_nM:g} nM) binding norovirus VLPs: K_d from FP", f_t)
    S.write("A2", f"Source file: {Path(a.xlsx).name}", f_note)
    S.write_row("A4", ["Setting", "Value", "Note", "", "", "", ""], f_h)
    S.write("A5", "G factor used (multiplies the parallel channel)", f_txt); S.write_number("B5", G, f_in)
    note(5, f"Yellow cells are inputs. Calibrated G in the file: {g_file}. K_d does not depend on G, absolute mP does.")
    S.write("A6", "nM VP1 per ug/mL VLP", f_txt); S.write_number("B6", NM_PER_UG, f_in); note(6, "VP1 = 58 kDa")
    S.write("A7", "Outlier flag tolerance (total intensity vs replicate median)", f_txt); S.write_number("B7", TOL, f_in)
    wb.define_name("G_FACTOR", "=Summary!$B$5"); wb.define_name("NM_PER_UG", "=Summary!$B$6"); wb.define_name("FLAG_TOL", "=Summary!$B$7")
    info = [("Gain (Optimal, from file)", hdr.get("gain optimal", hdr.get("gain manual", ""))),
            ("Z-position (um)", next((v for k, v in hdr.items() if k.startswith("z-position [")), "")),
            ("Lid lifter", hdr.get("lid lifter", "")), ("Excitation / emission (nm)", f"{float(hdr.get('excitation wavelength [nm]', 0)):g} / {float(hdr.get('emission wavelength [nm]', 0)):g}"),
            ("Temperature (C)", hdr.get("temperature [°c]", "")), ("Read start", hdr.get("start time", ""))]
    for i, (k, v) in enumerate(info):
        S.write(8 + i, 0, k, f_txt); S.write(8 + i, 1, v if not isinstance(v, float) else round(v, 1), f_txt)

    # ---- Raw data ----
    RD.set_column("A:A", 8); RD.set_column("B:M", 9)
    RD.write("A1", "Raw counts from the Spark export (not blank-subtracted, G not applied)", f_b)
    for title, tab, r0 in (("Parallel (raw)", par, 2), ("Perpendicular (raw)", perp, 14)):
        RD.write(r0, 0, title, f_b)
        RD.write(r0 + 1, 0, "", f_h)
        for c in range(12): RD.write_number(r0 + 1, 1 + c, c + 1, f_h)
        for r in range(8):
            RD.write(r0 + 2 + r, 0, LET[r], f_h)
            for c in range(12):
                if not np.isnan(tab[r, c]): RD.write_number(r0 + 2 + r, 1 + c, float(tab[r, c]), f_n0)
    pcell = lambda w: "'Raw data'!" + rc(4 + w[0], 1 + w[1], True, True)      # parallel table data starts at Excel row 5
    scell = lambda w: "'Raw data'!" + rc(16 + w[0], 1 + w[1], True, True)     # perpendicular table data starts at Excel row 17

    # ---- Blank ----
    BL.set_column("A:D", 14); BL.set_column("F:F", 36); BL.set_column("G:G", 14)
    BL.write_row("A1", ["VLP-only well", "VLP (ug/mL)", "raw parallel", "raw perp."], f_h)
    for i, w in enumerate(blank_wells):
        BL.write(1 + i, 0, wname(w), f_txt); BL.write_number(1 + i, 1, blank_conc[w], f_n2)
        fx(BL, rc(1 + i, 2), "=" + pcell(w), f_n0, par[w]); fx(BL, rc(1 + i, 3), "=" + scell(w), f_n0, perp[w])
    last = 1 + len(blank_wells)
    BL.write("F1", "Pooled blank (median of all VLP-only wells, per channel)", f_b)
    BL.write("F2", "parallel", f_txt); fx(BL, "G2", f"=MEDIAN(C2:C{last})", f_n0, bp)
    BL.write("F3", "perpendicular", f_txt); fx(BL, "G3", f"=MEDIAN(D2:D{last})", f_n0, bs)
    BL.write("F4", "total (G*par + 2*perp)", f_txt); fx(BL, "G4", "=G_FACTOR*G2+2*G3", f_n0, G * bp + 2 * bs)
    BL.write("F6", "The VLP-only wells show no trend with VLP concentration, so one pooled blank is used.", f_note)
    wb.define_name("BLANK_PAR", "=Blank!$G$2"); wb.define_name("BLANK_PERP", "=Blank!$G$3")

    # ---- Wells ----
    WL.set_column("A:A", 7); WL.set_column("B:B", 14); WL.set_column("C:N", 12); WL.set_row(0, 42)
    heads = ["Well", "Group", "VLP (ug/mL)", "VLP (nM VP1)", "raw parallel", "raw perp.", "net parallel (raw - blank)", "net perp. (raw - blank)",
             "G x net parallel", "mP", "net total (G*par + 2*perp)", "gross total (before blank)", "replicate median of gross total", "flag (>25% from median)"]
    WL.write_row("A1", heads, f_h)
    r = 1; first_row = {}
    for g in groups:
        first_row[g["name"]] = r; n = len(g["wells"])
        for j, w in enumerate(g["wells"]):
            R = [x for x in rows if x["well"] == w][0]; e = r + 1  # excel row
            WL.write(r, 0, wname(w), f_txt); WL.write(r, 1, g["name"], f_txt); WL.write_number(r, 2, g["conc"], f_n2)
            fx(WL, rc(r, 3), f"=C{e}*NM_PER_UG", f_n1, g["conc"] * NM_PER_UG)
            fx(WL, rc(r, 4), "=" + pcell(w), f_n0, R["par"]); fx(WL, rc(r, 5), "=" + scell(w), f_n0, R["perp"])
            fx(WL, rc(r, 6), f"=E{e}-BLANK_PAR", f_n0, R["netp"]); fx(WL, rc(r, 7), f"=F{e}-BLANK_PERP", f_n0, R["nets"])
            fx(WL, rc(r, 8), f"=G_FACTOR*G{e}", f_n0, R["gp"])
            fx(WL, rc(r, 9), f"=1000*(I{e}-H{e})/(I{e}+H{e})", f_n1, R["mp"])
            fx(WL, rc(r, 10), f"=I{e}+2*H{e}", f_n0, R["nettot"])
            fx(WL, rc(r, 11), f"=G_FACTOR*E{e}+2*F{e}", f_n0, R["gross"])
            a0, a1 = first_row[g["name"]] + 1, first_row[g["name"]] + n
            fx(WL, rc(r, 12), f"=MEDIAN(L{a0}:L{a1})", f_n0, R["med"])
            fx(WL, rc(r, 13), f'=IF(ABS(L{e}-M{e})>FLAG_TOL*M{e},"flag","ok")', f_txt, R["flag"])
            r += 1
    n_rows = r  # last data row index (0-based) + 1
    LAST = n_rows  # excel last row
    WL.write(n_rows + 1, 0, "mP = 1000*(G*net parallel - net perp.)/(G*net parallel + net perp.). A well flagged by the rule is excluded from the group statistics (type 'flag' manually in column N to exclude another).", f_note)
    WL.freeze_panes(1, 2)

    # ---- Groups ----
    GR.set_column("A:A", 14); GR.set_column("B:H", 13); GR.set_row(0, 42)
    GR.write_row("A1", ["Group", "VLP (ug/mL)", "VLP (nM VP1)", "n wells used", "mean mP", "SD mP", "mean net total", "net total / aptamer alone"], f_h)
    rngC, rngJ, rngK, rngN = (f"Wells!${c}$2:${c}${LAST}" for c in "CJKN")
    gstats = []
    for i, g in enumerate(groups):
        e = i + 2; okr = [x for x in ok if x["conc"] == g["conc"]]
        mps = np.array([x["mp"] for x in okr]); nts = np.array([x["nettot"] for x in okr])
        sdv = float(np.std(mps, ddof=1)) if len(mps) > 1 else 0.0
        gstats.append((g["conc"], len(mps), float(mps.mean()), sdv, float(nts.mean())))
        GR.write(i + 1, 0, g["name"], f_txt); GR.write_number(i + 1, 1, g["conc"], f_n2)
        fx(GR, rc(i + 1, 2), f"=B{e}*NM_PER_UG", f_n1, g["conc"] * NM_PER_UG)
        fx(GR, rc(i + 1, 3), f'=COUNTIFS({rngC},B{e},{rngN},"ok")', f_n0, len(mps))
        fx(GR, rc(i + 1, 4), f'=AVERAGEIFS({rngJ},{rngC},B{e},{rngN},"ok")', f_n1, mps.mean())
        GR.write_array_formula(i + 1, 5, i + 1, 5, f'{{=STDEV(IF(({rngC}=B{e})*({rngN}="ok"),{rngJ}))}}', f_n1, 0 if a.no_cache else sdv)
        fx(GR, rc(i + 1, 6), f'=AVERAGEIFS({rngK},{rngC},B{e},{rngN},"ok")', f_n0, nts.mean())
        fx(GR, rc(i + 1, 7), f"=G{e}/$G$2", f_n2, nts.mean() / gstats[0][4])
    NG = len(groups)  # groups rows 2..NG+1 ; row 2 = aptamer alone

    # ---- Fit ----
    FT.set_column("A:A", 30); FT.set_column("B:I", 14)
    FT.write("A1", "Curve fit (least squares on single wells; aptamer alone = concentration 0)", f_t)
    FT.write("A2", "Parameters are values from the script's fit. To re-fit in Excel: Data > Solver, minimise the SSE cell by changing the parameter cells.", f_note)
    FT.write("A4", "1:1 model", f_b); FT.write("D4", "Hill model", f_b)
    for i, (k, v) in enumerate((("free mP (baseline)", p1[0]), ("bound mP (plateau)", p1[1]), ("K_d (ug/mL)", p1[2]))):
        FT.write(4 + i, 0, k, f_txt); FT.write_number(4 + i, 1, float(v), f_in)
    for i, (k, v) in enumerate((("free mP", p2[0]), ("bound mP", p2[1]), ("K (ug/mL)", p2[2]), ("Hill n", p2[3]))):
        FT.write(4 + i, 3, k, f_txt); FT.write_number(4 + i, 4, float(v), f_in)
    D0 = 15  # first observation excel row
    D1 = D0 + len(rows) - 1
    FT.write("A8", "K_d (nM VP1)", f_txt); fx(FT, "B8", "=B7*NM_PER_UG", f_n1, p1[2] * NM_PER_UG)
    res1 = y_all - hyp(c_all, *p1); res2 = y_all - hill(c_all, *p2)
    FT.write("A9", "SSE (sum of squared residuals)", f_txt); fx(FT, "B9", f"=SUM(F{D0}:F{D1})", f_n0, float(np.sum(res1 ** 2)))
    FT.write("A10", "residual SD (mP)", f_txt); fx(FT, "B10", f"=SQRT(B9/(B11-3))", f_n1, float(np.sqrt(np.sum(res1 ** 2) / dof1)))
    FT.write("A11", "wells used", f_txt); fx(FT, "B11", f"=SUM(C{D0}:C{D1})", f_n0, len(y_all))
    FT.write("D9", "K (nM VP1)", f_txt); fx(FT, "E9", "=E7*NM_PER_UG", f_n1, p2[2] * NM_PER_UG)
    FT.write("D10", "SSE", f_txt); fx(FT, "E10", f"=SUM(I{D0}:I{D1})", f_n0, float(np.sum(res2 ** 2)))
    FT.write("D11", "residual SD (mP)", f_txt); fx(FT, "E11", "=SQRT(E10/(B11-4))", f_n1, float(np.sqrt(np.sum(res2 ** 2) / dof2)))
    FT.set_row(D0 - 2, 30)
    FT.write_row(D0 - 2, 0, ["VLP (ug/mL)", "observed mP", "used (1/0)", "1:1 predicted", "1:1 residual", "1:1 squared residual", "Hill predicted", "Hill residual", "Hill squared residual"], f_h)
    for i, R in enumerate(rows):
        e = D0 + i; we = 2 + i  # Wells excel row
        fx(FT, f"A{e}", f"=Wells!C{we}", f_n2, R["conc"]); fx(FT, f"B{e}", f"=Wells!J{we}", f_n1, R["mp"])
        fx(FT, f"C{e}", f'=IF(Wells!N{we}="ok",1,0)', f_n0, 1 if R["flag"] == "ok" else 0)
        pr1 = float(hyp(R["conc"], *p1)); pr2 = float(hill(R["conc"], *p2))
        fx(FT, f"D{e}", f"=$B$5+($B$6-$B$5)*A{e}/($B$7+A{e})", f_n1, pr1)
        fx(FT, f"E{e}", f"=B{e}-D{e}", f_n1, R["mp"] - pr1)
        fx(FT, f"F{e}", f"=C{e}*E{e}^2", f_n1, (R["mp"] - pr1) ** 2 * (1 if R["flag"] == "ok" else 0))
        fx(FT, f"G{e}", f"=$E$5+($E$6-$E$5)*A{e}^$E$8/($E$7^$E$8+A{e}^$E$8)", f_n1, pr2)
        fx(FT, f"H{e}", f"=B{e}-G{e}", f_n1, R["mp"] - pr2)
        fx(FT, f"I{e}", f"=C{e}*H{e}^2", f_n1, (R["mp"] - pr2) ** 2 * (1 if R["flag"] == "ok" else 0))

    # ---- Curve (for the chart) ----
    CV.set_column("A:I", 14)
    CV.write_row("A1", ["VLP (ug/mL)", "1:1 fit", "Hill fit", "", "K_d line x", "K_d line y", "", "alone line x", "alone line y"], f_h)
    xs = np.geomspace(0.14, 40, 61)
    for i, x in enumerate(xs):
        e = i + 2
        CV.write_number(i + 1, 0, float(x), f_n3)
        fx(CV, f"B{e}", f"=Fit!$B$5+(Fit!$B$6-Fit!$B$5)*A{e}/(Fit!$B$7+A{e})", f_n1, float(hyp(x, *p1)))
        fx(CV, f"C{e}", f"=Fit!$E$5+(Fit!$E$6-Fit!$E$5)*A{e}^Fit!$E$8/(Fit!$E$7^Fit!$E$8+A{e}^Fit!$E$8)", f_n1, float(hill(x, *p2)))
    for i, y in enumerate((0, 300)):
        fx(CV, f"E{i + 2}", "=Fit!$B$7", f_n2, p1[2]); CV.write_number(i + 1, 5, y, f_n0)
    for i, x in enumerate((0.14, 40)):
        CV.write_number(i + 1, 7, x, f_n2); fx(CV, f"I{i + 2}", "=Groups!$E$2", f_n1, gstats[0][2])

    # ---- Summary: results, checks, notes ----
    top_i = NG - 1; sec_i = NG - 2  # index in groups (last = highest conc)
    S.write_row("A16", ["Result", "Value", "Note", "", "", "", ""], f_h)
    S.write("A17", "K_d, 1:1 fit (ug/mL VLP)", f_b); fx(S, "B17", "=Fit!B7", f_good, p1[2]); note(17, f"95% CI {ci1[0]:.2f} - {ci1[1]:.2f} ug/mL (static, from the script)")
    S.write("A18", "K_d, 1:1 fit (nM VP1)", f_b); fx(S, "B18", "=Fit!B8", f_good, p1[2] * NM_PER_UG); note(18, f"95% CI {ci1[0] * NM_PER_UG:.0f} - {ci1[1] * NM_PER_UG:.0f} nM VP1")
    S.write("A19", "Bootstrap over wells (2000 resamples)", f_txt); S.write("B19", f"{bq[0]:.2f} - {bq[2]:.2f}", f_txt); note(19, f"ug/mL, 95% range ({bq[0] * NM_PER_UG:.0f} - {bq[2] * NM_PER_UG:.0f} nM VP1), median {bq[1]:.2f}")
    S.write("A20", "K, Hill fit (ug/mL)", f_txt); fx(S, "B20", "=Fit!E7", f_n2, p2[2]); note(20, f"Hill n = {p2[3]:.2f} +/- {se2[3]:.2f}; 95% CI {ci2[0]:.2f} - {ci2[1]:.2f} ug/mL. n near 1 means 1:1-type binding.")
    S.write("A21", "Free baseline / plateau of the 1:1 fit (mP)", f_txt); S.write("B21", f"{p1[0]:.0f} / {p1[1]:.0f}", f_txt)
    S.write("A22", "Residual SD of the 1:1 fit (mP)", f_txt); fx(S, "B22", "=Fit!B10", f_n1, float(np.sqrt(np.sum(res1 ** 2) / dof1)))
    S.write_row("A24", ["Quality check", "Value", "Meaning", "", "", "", ""], f_h)
    gtop, g2 = gstats[top_i], gstats[sec_i]
    ge, g_top_row, g_2_row = 2, NG + 1, NG   # Groups excel rows: alone = 2, top = NG+1, second = NG
    S.write("A25", "Plateau test: mP change from 2nd-highest to highest VLP (%)", f_txt)
    fx(S, "B25", f"=(Groups!E{g_top_row}-Groups!E{g_2_row})/Groups!E{g_top_row}*100", f_n1, (gtop[2] - g2[2]) / gtop[2] * 100)
    note(25, "Aim for < 5 %. Above that the curve is still rising at the top.")
    S.write("A26", "Saturation at the highest VLP (% of fitted curve)", f_txt)
    fx(S, "B26", f"=Groups!B{g_top_row}/(Fit!B7+Groups!B{g_top_row})*100", f_n0, gtop[0] / (p1[2] + gtop[0]) * 100)
    note(26, "Aim for 90 % or more for a well-defined plateau.")
    S.write("A27", "Signal over blank (mean net total / blank total)", f_txt)
    fx(S, "B27", f'=AVERAGEIFS(Wells!$K$2:$K${LAST},Wells!$C$2:$C${LAST},">0",Wells!$N$2:$N${LAST},"ok")/Blank!G4', f_n1,
       float(np.mean([x["nettot"] for x in ok if x["conc"] > 0])) / (G * bp + 2 * bs))
    note(27, "Low values (< 3) mean noisy single wells. Reading without the lid roughly doubles it.")
    S.write("A28", "Bound/free brightness ratio Q (highest VLP / aptamer alone)", f_txt)
    fx(S, "B28", f"=Groups!H{g_top_row}", f_n2, gtop[4] / gstats[0][4])
    note(28, "Q well below 1: the bound aptamer is dimmer, which biases the plain K_d upward (part of the drop may be a general VLP effect).")
    S.write("A29", "Wells flagged / excluded", f_txt); fx(S, "B29", f'=COUNTIF(Wells!$N$2:$N${LAST},"flag")', f_n0, sum(1 for x in rows if x["flag"] == "flag"))
    # fluorescein check
    fw = fp.expand_wells(lay["reference"]["fluorescein"]); bw = fp.expand_wells(lay["reference"]["fl_buffer"])
    S.write("A31", "Fluorescein reference wells (G check)", f_b)
    S.write_row("A32", ["Well", "net parallel", "net perp.", "mP at the G used", "G giving 20 mP"], f_h)
    bufp = float(np.mean([par[w] for w in bw])); bufs = float(np.mean([perp[w] for w in bw]))
    bufP_f = "AVERAGE(" + ",".join(pcell(w) for w in bw) + ")"; bufS_f = "AVERAGE(" + ",".join(scell(w) for w in bw) + ")"
    for i, w in enumerate(fw):
        e = 33 + i; npp, nss = par[w] - bufp, perp[w] - bufs
        S.write(32 + i, 0, wname(w), f_txt)
        fx(S, f"B{e}", f"={pcell(w)}-{bufP_f}", f_n0, npp); fx(S, f"C{e}", f"={scell(w)}-{bufS_f}", f_n0, nss)
        fx(S, f"D{e}", f"=1000*(G_FACTOR*B{e}-C{e})/(G_FACTOR*B{e}+C{e})", f_n1, 1000 * (G * npp - nss) / (G * npp + nss))
        fx(S, f"E{e}", f"=1.0408*C{e}/B{e}", f_n3, 1.0408 * nss / npp)
    notes = ["How to read this workbook",
             "1. Raw data: counts from the Spark file. 2. Blank: median of the VLP-only wells, per channel. 3. Wells: net counts, mP and flags for every well.",
             "4. Groups: mean and SD per VLP concentration (the plotted points). 5. Fit: model, parameters, residuals. 6. Curve: points of the fitted line.",
             "K_d is the VLP concentration at half-maximal polarization. It is an apparent K_d (one VLP carries many sites). nM VP1 = ug/mL x 17.14.",
             "Limits: single plate; no specificity controls (scrambled aptamer, competitor, off-target VLP) on it; lid on, so single wells scatter by 5-25 mP."]
    for i, t in enumerate(notes): S.write(36 + i, 0, t, f_b if i == 0 else f_txt)

    # ---- chart ----
    ch = wb.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
    n0 = 5  # Wells rows with conc > 0 start at excel row 5 (after 3 aptamer-alone rows)
    ch.add_series({"name": "single wells", "categories": f"=Wells!$C$5:$C${LAST}", "values": f"=Wells!$J$5:$J${LAST}",
                   "line": {"none": True}, "marker": {"type": "circle", "size": 5, "fill": {"color": "#B0B0B0"}, "border": {"color": "#808080"}}})
    ch.add_series({"name": "mean +/- SD", "categories": f"=Groups!$B$3:$B${NG + 1}", "values": f"=Groups!$E$3:$E${NG + 1}",
                   "line": {"color": "#1F4E79", "width": 2.0}, "marker": {"type": "circle", "size": 7, "fill": {"color": "#1F4E79"}, "border": {"color": "#1F4E79"}},
                   "y_error_bars": {"type": "custom", "plus_values": f"=Groups!$F$3:$F${NG + 1}", "minus_values": f"=Groups!$F$3:$F${NG + 1}", "line": {"color": "#1F4E79"}}})
    ch.add_series({"name": "1:1 fit", "categories": "=Curve!$A$2:$A$62", "values": "=Curve!$B$2:$B$62",
                   "line": {"color": "#B22222", "width": 2.0, "dash_type": "dash"}, "marker": {"type": "none"}})
    ch.add_series({"name": "K_d", "categories": "=Curve!$E$2:$E$3", "values": "=Curve!$F$2:$F$3",
                   "line": {"color": "#B22222", "width": 1.0, "dash_type": "round_dot"}, "marker": {"type": "none"}})
    ch.add_series({"name": "aptamer alone", "categories": "=Curve!$H$2:$H$3", "values": "=Curve!$I$2:$I$3",
                   "line": {"color": "#505050", "width": 1.0, "dash_type": "square_dot"}, "marker": {"type": "none"}})
    ch.set_title({"name": f"{a.label} aptamer ({a.apt_nM:g} nM) with norovirus VLP: polarization vs VLP", "name_font": {"size": 12}})
    ch.set_x_axis({"name": "VLP (µg/mL)", "log_base": 10, "min": 0.1, "max": 50, "major_gridlines": {"visible": True, "line": {"color": "#E5E5E5"}}})
    ch.set_y_axis({"name": "Polarization (mP)", "min": 0, "max": 300, "major_gridlines": {"visible": True, "line": {"color": "#E5E5E5"}}})
    ch.set_legend({"position": "bottom"}); ch.set_size({"width": 860, "height": 500})
    S.insert_chart("I3", ch)
    S.set_landscape(); S.fit_to_pages(1, 1)   # Summary prints on one page
    wb.close()
    print(f"K_d (1:1) = {p1[2]:.3f} ug/mL = {p1[2] * NM_PER_UG:.1f} nM VP1; CI {ci1[0]:.2f}-{ci1[1]:.2f}; Hill K {p2[2]:.3f}, n {p2[3]:.2f}; bootstrap {bq[0]:.2f}-{bq[2]:.2f}; wells used {len(y_all)}")
    print("wrote", a.out)


if __name__ == "__main__":
    main()
