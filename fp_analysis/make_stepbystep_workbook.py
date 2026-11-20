#!/usr/bin/env python3
"""Step-by-step Excel workbook for one FP titration plate (every calculation is a live formula).

  python3 -I make_stepbystep_workbook.py TECAN.xlsx layout.json OUT.xlsx [--label Buf-2] [--g 1.062]

Then run the xlsx skill's scripts/recalc.py TWICE (the first pass can leave a few dependent cells at 0 in LibreOffice; the second settles them) so formula values are stored in the file.

Design
  README, Inputs, Plate_Map : what was measured and the settings that drive everything
  Raw_Tables                : the seven tables of the Tecan file, as exported
  Step1_Blank               : the background (VLP-only wells) and why one pooled blank is used
  Step2_Wells               : per-well net counts, mP, anisotropy, outlier flag
  Step3_Groups              : mean, SD, n per VLP concentration
  Step4_Fit / Step4b_Scan   : K_d by a hand estimate and by a least-squares scan done with formulas
  Step5_Results             : K_d in all units, quality checks with pass/caution/fail
  Chart, Worked_Example, Report_Text
Colour code: blue text = number typed in or copied from the Tecan file (inputs); black text = formula.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import xlsxwriter
from openpyxl import load_workbook
from scipy.optimize import curve_fit
from xlsxwriter.utility import xl_col_to_name as colname

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fp_analysis as fp

LET = "ABCDEFGH"
TABLES = ["Rawdata (parallel)", "Rawdata (perpendicular)", "Intensity (parallel)", "Intensity (perpendicular)",
          "Total Intensity", "Label 1 [mP]", "Anisotropy"]
T_PAR, T_PERP, T_IPAR, T_IPERP, T_TOT, T_MP, T_ANI = range(7)
FIRST_ROW = 6   # first data row (Excel numbering) of Step2/Step3 tables


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("xlsx"); ap.add_argument("layout"); ap.add_argument("out")
    ap.add_argument("--label", default="Buf-2"); ap.add_argument("--g", type=float, default=None)
    ap.add_argument("--apt-nM", type=float, default=5.0)
    a = ap.parse_args()
    lay = json.loads(Path(a.layout).read_text())
    hdr, tabs_raw = fp.parse_export(a.xlsx)
    G0 = a.g or fp.header_g(hdr) or 1.05

    # ---------- read all seven tables (numbers and text) ----------
    ws_in = load_workbook(a.xlsx, data_only=True).worksheets[0]
    rows = [list(r) for r in ws_in.iter_rows(values_only=True)]
    tables = {}
    for k in TABLES:
        for i, r in enumerate(rows):
            if r and r[0] == k:
                t = {}
                for rr in rows[i + 2:i + 10]:
                    for j in range(12):
                        if rr[1 + j] is not None:
                            t[(LET.index(rr[0]), j)] = rr[1 + j]
                tables[k] = t
                break
    raw_par = {(r, c): v for (r, c), v in tables["Rawdata (parallel)"].items() if isinstance(v, (int, float))}
    raw_perp = {(r, c): v for (r, c), v in tables["Rawdata (perpendicular)"].items() if isinstance(v, (int, float))}

    # ---------- plate map ----------
    def wells(spec): return fp.expand_wells(spec)
    wname = lambda w: f"{LET[w[0]]}{w[1] + 1}"
    plate = {}   # well name -> dict
    groups_titr = sorted(lay["titration"], key=lambda g: g["conc"])
    for g in groups_titr:
        for w in wells(g["wells"]):
            plate[wname(w)] = dict(role="Sample", text=f"Aptamer {a.apt_nM:g} nM + VLP {g['conc']:g} ug/mL", conc=g["conc"], apt=a.apt_nM, used="Yes")
        for w in wells(g["blank_wells"]):
            plate[wname(w)] = dict(role="VLP-only blank", text=f"VLP only {g['conc']:g} ug/mL (no aptamer)", conc=g["conc"], apt=0, used="Yes (blank)")
    for w in wells(lay["free"]): plate[wname(w)] = dict(role="Aptamer alone", text=f"Aptamer alone {a.apt_nM:g} nM", conc=0, apt=a.apt_nM, used="Yes")
    for w in wells(lay["reference"]["fluorescein"]): plate[wname(w)] = dict(role="Fluorescein", text="Fluorescein 1 nM", conc=None, apt=None, used="Yes (G check)")
    for w in wells(lay["reference"]["fl_buffer"]): plate[wname(w)] = dict(role="Fluorescein buffer", text="Fluorescein buffer (BF1)", conc=None, apt=None, used="Yes (G check)")
    for w in wells("F7-F9"): plate[wname(w)] = dict(role="Aptamer buffer", text="Aptamer buffer (no VLP)", conc=0, apt=0, used="Comparison only")
    for w in wells("G1-G3"): plate[wname(w)] = dict(role="VLP buffer", text="VLP buffer (no aptamer)", conc=0, apt=0, used="Comparison only")
    for w in wells("G4-G6"): plate[wname(w)] = dict(role="Unspecified", text="Contents not specified", conc=None, apt=None, used="No")
    note_21 = "The plate description lists B10-B12 as 2.1 ug/mL and its blank E3-E4 as 2.3; 2.3 (the planned value) is used for both."

    # ---------- independent numbers for the static extras (Hill, bootstrap) ----------
    allb = [w for g in lay["titration"] for w in wells(g["blank_wells"])]
    bp0 = float(np.median([raw_par[w] for w in allb])); bs0 = float(np.median([raw_perp[w] for w in allb]))
    def mp_of(w):
        gp = G0 * (raw_par[w] - bp0); s = raw_perp[w] - bs0
        return 1000 * (gp - s) / (gp + s)
    cc, yy, grp = [], [], []
    for g in groups_titr:
        for w in wells(g["wells"]): cc.append(g["conc"]); yy.append(mp_of(w)); grp.append(g["conc"])
    for w in wells(lay["free"]): cc.append(0.0); yy.append(mp_of(w)); grp.append(0.0)
    cc, yy = np.array(cc), np.array(yy)
    hyp = lambda c, a_, b_, k: a_ + (b_ - a_) * c / (k + c)
    hill = lambda c, a_, b_, k, n: a_ + (b_ - a_) * c ** n / (k ** n + c ** n)
    p1, _ = curve_fit(hyp, cc, yy, p0=[45, 250, 3], bounds=([0, 0, .01], [300, 800, 500]), maxfev=20000)
    p2, c2 = curve_fit(hill, cc, yy, p0=[45, 250, 3, 1], bounds=([0, 0, .01, .5], [300, 800, 500, 8]), maxfev=20000)
    se2 = np.sqrt(np.diag(c2))
    rng = np.random.default_rng(1); byg = {}
    for c_, y_ in zip(cc, yy): byg.setdefault(c_, []).append(y_)
    boot = []
    for _ in range(2000):
        x_, y_ = [], []
        for k, v in byg.items():
            s = rng.choice(v, len(v)); x_ += [k] * len(v); y_ += list(s)
        try:
            pb, _ = curve_fit(hyp, np.array(x_), np.array(y_), p0=[45, 250, 3], bounds=([0, 0, .01], [300, 800, 500]), maxfev=5000); boot.append(pb[2])
        except Exception: pass
    bq = np.percentile(boot, [2.5, 50, 97.5])

    # ---------- workbook, formats ----------
    wb = xlsxwriter.Workbook(a.out, {"default_format_properties": {"font_name": "Arial", "font_size": 10}})
    F = lambda **k: wb.add_format({"font_name": "Arial", "font_size": 10, **k})
    DARK = "#1F4E79"
    f_title = F(bold=True, font_size=16, font_color=DARK)
    f_h = F(bold=True, font_color="white", bg_color=DARK, text_wrap=True, valign="vcenter", border=1)
    f_sub = F(bold=True, font_color=DARK, font_size=11)
    f_txt = F(text_wrap=True, valign="top")
    f_note = F(italic=True, font_color="#555555", text_wrap=True, valign="top")
    f_in = F(font_color="#0000FF", bg_color="#FFF2CC", border=1)
    f_in3 = F(font_color="#0000FF", bg_color="#FFF2CC", border=1, num_format="0.000")
    f_data = F(font_color="#0000FF"); f_data0 = F(font_color="#0000FF", num_format="#,##0")
    f_data1 = F(font_color="#0000FF", num_format="0.0")
    f_n0, f_n1, f_n2, f_n3, f_n4 = (F(num_format=x) for x in ("#,##0", "0.0", "0.00", "0.000", "0.0000"))
    f_pct = F(num_format="0.0"); f_bold = F(bold=True)
    f_key = F(bold=True, font_color=DARK, num_format="0.00", bg_color="#DDEBF7", border=1)
    f_key1 = F(bold=True, font_color=DARK, num_format="0.0", bg_color="#DDEBF7", border=1)
    f_pass = F(bold=True, font_color="#006100", bg_color="#C6EFCE"); f_warn = F(bold=True, font_color="#9C5700", bg_color="#FFEB9C")
    f_fail = F(bold=True, font_color="#9C0006", bg_color="#FFC7CE")
    role_fmt = {"Sample": F(bg_color="#DDEBF7", text_wrap=True, align="center", valign="vcenter", border=1, font_size=8),
                "VLP-only blank": F(bg_color="#FCE4D6", text_wrap=True, align="center", valign="vcenter", border=1, font_size=8),
                "Aptamer alone": F(bg_color="#E2EFDA", text_wrap=True, align="center", valign="vcenter", border=1, font_size=8),
                "Fluorescein": F(bg_color="#FFF2CC", text_wrap=True, align="center", valign="vcenter", border=1, font_size=8),
                "Fluorescein buffer": F(bg_color="#FFF9E5", text_wrap=True, align="center", valign="vcenter", border=1, font_size=8),
                "Aptamer buffer": F(bg_color="#EDEDED", text_wrap=True, align="center", valign="vcenter", border=1, font_size=8),
                "VLP buffer": F(bg_color="#EDEDED", text_wrap=True, align="center", valign="vcenter", border=1, font_size=8),
                "Unspecified": F(bg_color="#FFFFFF", text_wrap=True, align="center", valign="vcenter", border=1, font_size=8, font_color="#9C0006")}

    names = ["README", "Inputs", "Plate_Map", "Raw_Tables", "Step1_Blank", "Step2_Wells", "Step3_Groups",
             "Step4_Fit", "Step4b_Scan", "Step5_Results", "Chart", "Worked_Example", "Report_Text"]
    S = {n: wb.add_worksheet(n) for n in names}
    for n, w in S.items():
        w.hide_gridlines(2); w.set_landscape(); w.fit_to_pages(1, 0); w.set_paper(9)
    S["README"].set_tab_color("#1F4E79"); S["Step5_Results"].set_tab_color("#00B050")

    # ================= Inputs =================
    I = S["Inputs"]; I.set_column("A:A", 4); I.set_column("B:B", 44); I.set_column("C:C", 16); I.set_column("D:D", 90)
    I.write("B1", "Inputs and settings (yellow cells can be changed; everything recalculates)", f_title)
    I.write_row("B3", ["Setting", "Value", "Meaning / source"], f_h)
    inputs = [
        ("G factor (multiplies the parallel channel)", G0, "G_FACTOR", f_in3, "Calibrated G stored in the Tecan file header (fluorescein reference, 20 mP). Earlier analyses used 1.05; changing G shifts absolute mP by about 10 mP per 0.02 but does not change the K_d."),
        ("Blank method (1 or 2)", 1, "BLANK_METHOD", f_in, "1 = one pooled blank: the median of all 24 VLP-only wells, per channel (recommended: those wells show no trend with VLP). 2 = the two VLP-only wells at the matching concentration."),
        ("Outlier tolerance (fraction)", 0.25, "FLAG_TOL", f_in, "A well is flagged when its total intensity (G x parallel + 2 x perpendicular, before the blank) is more than this fraction from the median of its replicates."),
        ("Aptamer concentration (nM)", a.apt_nM, "APT_NM", f_in, "Fixed aptamer concentration in the well; used for the depletion correction."),
        ("nM VP1 per ug/mL of VLP", 17.14, "NM_PER_UG", f_in, "1 ug/mL VLP protein = 17.14 nM VP1 (VP1 about 58 kDa; the lab notes give 5.6 ug/mL = 96 nM VP1)."),
        ("VP1 copies per VLP", 180, "VP1_PER_VLP", f_in, "T = 3 norovirus capsid: 180 VP1 (90 dimers), about 10.4 MDa per particle."),
    ]
    for i, (lab, val, nm, fmt, note) in enumerate(inputs):
        r = 4 + i
        I.write(r, 1, lab, f_txt); I.write_number(r, 2, val, fmt); I.write(r, 3, note, f_note); I.set_row(r, 32)
        wb.define_name(nm, f"=Inputs!$C${r + 1}")
    I.write("B12", "Instrument settings in the Tecan file header (for the record)", f_sub)
    hv = lambda k: hdr.get(k, "")
    info = [("Lid lifter", hv("lid lifter")), ("Plate area", hv("plate area")), ("Excitation / emission (nm)", f"{float(hv('excitation wavelength [nm]') or 0):g} / {float(hv('emission wavelength [nm]') or 0):g}"),
            ("Bandwidth ex / em (nm)", f"{hv('excitation bandwidth [nm]')} / {hv('emission bandwidth [nm]')}"), ("Mirror", hv("mirror")), ("Gain", hv("gain optimal") or hv("gain manual")),
            ("Z-position (um)", next((v for k, v in hdr.items() if k.startswith("z-position [")), "")), ("G factor in the file", fp.header_g(hdr)), ("Measurement blank", hv("measurement blank")),
            ("Temperature (C)", hv("temperature [°c]")), ("Read start", hv("start time")), ("Source file", Path(a.xlsx).name)]
    for i, (k, v) in enumerate(info):
        I.write(12 + i, 1, k, f_txt); I.write(12 + i, 2, v, f_data)
    I.write(25, 1, "Note: 'Measurement Blank: Not defined' means the instrument did NOT remove any blank; the exported mP and Anisotropy tables still contain the background. The blank is removed here, per channel (Step 1).", f_note)

    # ================= Raw_Tables =================
    R = S["Raw_Tables"]; R.set_column("A:A", 8); R.set_column("B:M", 10)
    R.write("A1", "The seven tables of the Tecan export (values exactly as exported; blue = data)", f_title)
    R.write("A2", "Only the first two are measurements. The others are calculated by the instrument from them (with G, and WITHOUT removing a blank).", f_note)
    T0 = 4
    expl = {"Rawdata (parallel)": "Counts for light polarized parallel to the excitation (measured).", "Rawdata (perpendicular)": "Counts for light polarized perpendicular (measured).",
            "Intensity (parallel)": "= G x Rawdata (parallel).", "Intensity (perpendicular)": "= Rawdata (perpendicular).",
            "Total Intensity": "= Intensity (parallel) + 2 x Intensity (perpendicular): overall brightness.",
            "Label 1 [mP]": "= 1000 x (I par - I perp) / (I par + I perp), no blank removed.", "Anisotropy": "= 1000 x (I par - I perp) / (I par + 2 I perp) in milli-units, no blank removed."}
    def tcell(k, w):  # absolute reference to a table cell on Raw_Tables, w = (row index, col index)
        return f"Raw_Tables!${colname(1 + w[1])}${T0 + k * 12 + 2 + w[0]}"
    def trange(k): return f"Raw_Tables!$B${T0 + k * 12 + 2}:$M${T0 + k * 12 + 9}"
    for k, title in enumerate(TABLES):
        r0 = T0 + k * 12 - 1 + 1
        R.write(r0 - 1 + 0, 0, f"{k + 1}. {title}", f_sub); R.write_string(r0 - 1, 3, expl[title], f_note)
        R.write(r0, 0, "", f_h)
        for c in range(12): R.write_number(r0, 1 + c, c + 1, f_h)
        for i in range(8):
            R.write(r0 + 1 + i, 0, LET[i], f_h)
            for j in range(12):
                v = tables[title].get((i, j))
                if v is None: continue
                if isinstance(v, (int, float)): R.write_number(r0 + 1 + i, 1 + j, v, f_data0 if title not in ("Anisotropy", "Label 1 [mP]") else f_data0)
                else: R.write(r0 + 1 + i, 1 + j, v, f_data)
    # sanity: the cell for table k, well (0,0) must be at row T0 + k*12 + 3 (Excel numbering)
    R.freeze_panes(2, 1)

    # ================= Plate_Map =================
    P = S["Plate_Map"]; P.set_column("A:A", 8); P.set_column("B:M", 12); P.set_column("N:N", 4)
    P.write("A1", "Plate map (as described by the experimenter)", f_title)
    P.write("A2", note_21, f_note)
    P.write("A4", "", f_h)
    for c in range(12): P.write_number(3, 1 + c, c + 1, f_h)
    for i in range(7):
        P.write(4 + i, 0, LET[i], f_h); P.set_row(4 + i, 40)
        for j in range(12):
            w = f"{LET[i]}{j + 1}"
            if w in plate:
                d = plate[w]; cv = d["conc"] if d["conc"] is not None else 0
                label = {"Sample": f"apt+VLP {cv:g}", "VLP-only blank": f"VLP only {cv:g}", "Aptamer alone": "aptamer alone", "Fluorescein": "fluorescein 1 nM",
                         "Fluorescein buffer": "fl. buffer", "Aptamer buffer": "aptamer buffer", "VLP buffer": "VLP buffer", "Unspecified": "unspecified"}[d["role"]]
                P.write(4 + i, 1 + j, label, role_fmt[d["role"]])
    P.write("A13", "Colour key", f_sub)
    for i, (k, fm) in enumerate(role_fmt.items()): P.write(13 + i, 1, k, fm); P.set_row(13 + i, 18)
    P.write("A23", "All 78 measured wells", f_sub)
    P.write_row("A24", ["Well", "Role", "Contents", "VLP ug/mL", "Aptamer nM", "Used for", "Raw parallel", "Raw perpendicular", "Instrument mP (no blank removed)"], f_h)
    P.set_column("B:B", 16); P.set_column("C:C", 38); P.set_column("F:F", 18); P.set_column("G:I", 18)
    P.set_row(23, 42)
    order = sorted(plate, key=lambda w: (LET.index(w[0]), int(w[1:])))
    for i, w in enumerate(order):
        d = plate[w]; r = 24 + i; rc_ = (LET.index(w[0]), int(w[1:]) - 1)
        P.write(r, 0, w, f_bold); P.write(r, 1, d["role"], f_txt); P.write(r, 2, d["text"], f_txt)
        if d["conc"] is not None: P.write_number(r, 3, d["conc"], f_data)
        if d["apt"] is not None: P.write_number(r, 4, d["apt"], f_data)
        P.write(r, 5, d["used"], f_txt)
        P.write_formula(r, 6, "=" + tcell(T_PAR, rc_), f_n0); P.write_formula(r, 7, "=" + tcell(T_PERP, rc_), f_n0)
        mpv = tables["Label 1 [mP]"].get(rc_)
        P.write_formula(r, 8, "=" + tcell(T_MP, rc_), f_n0)

    # ================= Step1_Blank =================
    B = S["Step1_Blank"]; B.set_column("A:A", 8); B.set_column("B:H", 15); B.set_column("I:I", 3); B.set_column("J:J", 40); B.set_column("K:N", 15)
    B.write("A1", "Step 1: the background (blank)", f_title)
    B.merge_range("A2:N3", "Every well also gives light that is not from the aptamer (buffer, plastic, scattered light, the VLP). That light is itself strongly polarized, so it pulls every polarization reading upward. Counts add, polarization values do not, so the background is removed from the COUNTS of each channel before anything is calculated. The VLP-only wells (no aptamer) measure it.", f_txt)
    B.set_row(1, 30); B.set_row(2, 14)
    B.write_row("A5", ["Well", "VLP ug/mL", "log10 VLP", "Raw parallel", "Raw perpendicular", "Total (G x par + 2 x perp)", "Blank polarization (mP)"], f_h); B.set_row(4, 42)
    blank_list = []
    for g in groups_titr:
        for w in wells(g["blank_wells"]): blank_list.append((wname(w), w, g["conc"]))
    blank_list.sort(key=lambda x: (LET.index(x[0][0]), int(x[0][1:])))
    b0 = 6; b1 = b0 + len(blank_list) - 1
    for i, (nm, w, conc) in enumerate(blank_list):
        r = b0 + i
        B.write(r - 1, 0, nm, f_bold); B.write_number(r - 1, 1, conc, f_data); B.write_formula(r - 1, 2, f"=LOG10(B{r})", f_n3)
        B.write_formula(r - 1, 3, "=" + tcell(T_PAR, w), f_n0); B.write_formula(r - 1, 4, "=" + tcell(T_PERP, w), f_n0)
        B.write_formula(r - 1, 5, f"=G_FACTOR*D{r}+2*E{r}", f_n0); B.write_formula(r - 1, 6, f"=1000*(G_FACTOR*D{r}-E{r})/(G_FACTOR*D{r}+E{r})", f_n0)
    rngD, rngE, rngC_, rngB_ = f"$D${b0}:$D${b1}", f"$E${b0}:$E${b1}", f"$C${b0}:$C${b1}", f"$B${b0}:$B${b1}"
    B.write("J5", "Pooled blank (used when Blank method = 1)", f_h); B.write("K5", "Parallel", f_h); B.write("L5", "Perpendicular", f_h)
    lines = [("Median of the 24 wells", "MEDIAN"), ("Mean", "AVERAGE"), ("Standard deviation", "STDEV"), ("Minimum", "MIN"), ("Maximum", "MAX")]
    for i, (lab, fn) in enumerate(lines):
        B.write(5 + i, 9, lab, f_bold if i == 0 else f_txt)
        B.write_formula(5 + i, 10, f"={fn}({rngD})", f_n0); B.write_formula(5 + i, 11, f"={fn}({rngE})", f_n0)
    B.write("J11", "Coefficient of variation (%)", f_txt); B.write_formula("K11", "=K8/K7*100", f_n1); B.write_formula("L11", "=L8/L7*100", f_n1)
    B.write("J12", "Blank total (G x par + 2 x perp)", f_txt); B.write_formula("K12", "=G_FACTOR*K6+2*L6", f_n0)
    B.write("J13", "Blank polarization (mP)", f_txt); B.write_formula("K13", "=1000*(G_FACTOR*K6-L6)/(G_FACTOR*K6+L6)", f_n0)
    B.write("J15", "Is there a trend with VLP concentration?", f_h); B.write("K15", "Parallel", f_h); B.write("L15", "Perpendicular", f_h)
    B.write("J16", "Slope per decade of VLP (counts)", f_txt); B.write_formula("K16", f"=SLOPE({rngD},{rngC_})", f_n0); B.write_formula("L16", f"=SLOPE({rngE},{rngC_})", f_n0)
    B.write("J17", "Slope as % of the median", f_txt); B.write_formula("K17", "=K16/K6*100", f_n1); B.write_formula("L17", "=L16/L6*100", f_n1)
    B.write("J18", "R squared of the trend", f_txt); B.write_formula("K18", f"=RSQ({rngD},{rngC_})", f_n3); B.write_formula("L18", f"=RSQ({rngE},{rngC_})", f_n3)
    B.write("J19", "Verdict", f_bold); B.write_formula("K19", '=IF(AND(ABS(K17)<5,ABS(L17)<5),"No trend: one pooled blank is valid","Trend: use Blank method 2")', f_bold)
    B.merge_range("J20:N22", "If the VLP itself scattered or fluoresced, the blank would rise with VLP concentration. A slope of a few percent per decade, with a small R squared, means the VLP-only wells are all the same background, so their median (robust to one contaminated well) can be used for every well, including the aptamer-alone wells.", f_note)
    # matched blanks table
    B.write("A33", "Matched blanks (used when Blank method = 2): the two VLP-only wells at each concentration", f_sub)
    B.write_row("A34", ["VLP ug/mL", "Well 1", "Well 2", "Mean parallel", "Mean perpendicular"], f_h); B.set_row(33, 30)
    mrow0 = 35
    for i, g in enumerate(groups_titr):
        r = mrow0 + i; ws_ = wells(g["blank_wells"])
        B.write_number(r - 1, 0, g["conc"], f_data); B.write(r - 1, 1, wname(ws_[0]), f_txt); B.write(r - 1, 2, wname(ws_[1]), f_txt)
        B.write_formula(r - 1, 3, f"=AVERAGE({tcell(T_PAR, ws_[0])},{tcell(T_PAR, ws_[1])})", f_n0)
        B.write_formula(r - 1, 4, f"=AVERAGE({tcell(T_PERP, ws_[0])},{tcell(T_PERP, ws_[1])})", f_n0)
    mrow1 = mrow0 + len(groups_titr) - 1
    # comparison of blanks for the free aptamer baseline
    B.write("A50", "Why the blank for the aptamer-alone wells matters: the free baseline under three different blanks", f_sub)
    B.write_row("A51", ["Blank used", "Parallel", "Perpendicular", "F10 mP", "F11 mP", "F12 mP", "Mean free mP"], f_h); B.set_row(50, 30)
    fw = wells(lay["free"]); apt_buf = wells("F7-F9"); vlp_buf = wells("G1-G3")
    cmp_rows = [("Pooled VLP-only wells (used)", "=K6", "=L6"),
                ("'Aptamer buffer' F7-F9 (buffer only)", f"=AVERAGE({','.join(tcell(T_PAR, w) for w in apt_buf)})", f"=AVERAGE({','.join(tcell(T_PERP, w) for w in apt_buf)})"),
                ("'VLP buffer' G1-G3", f"=AVERAGE({','.join(tcell(T_PAR, w) for w in vlp_buf)})", f"=AVERAGE({','.join(tcell(T_PERP, w) for w in vlp_buf)})")]
    for i, (lab, fp_, fs_) in enumerate(cmp_rows):
        r = 52 + i
        B.write(r - 1, 0, lab, f_txt); B.write_formula(r - 1, 1, fp_, f_n0); B.write_formula(r - 1, 2, fs_, f_n0)
        for j, w in enumerate(fw):
            B.write_formula(r - 1, 3 + j, f"=1000*(G_FACTOR*({tcell(T_PAR, w)}-B{r})-({tcell(T_PERP, w)}-C{r}))/(G_FACTOR*({tcell(T_PAR, w)}-B{r})+({tcell(T_PERP, w)}-C{r}))", f_n1)
        B.write_formula(r - 1, 6, f"=AVERAGE(D{r}:F{r})", f_n1)
    B.set_column("A:A", 34)
    B.merge_range("A56:N59", "Reading the comparison: the aptamer-alone wells contain aptamer plus the same VLP-free storage-buffer fraction as every other well, so their correct blank is the VLP-only background, not buffer alone. Subtracting the buffer-only blank (F7-F9) under-removes the background and raises the free baseline by about 12 mP, which makes the lowest VLP points appear to fall below the free baseline. That is an artefact of the blank choice, not of the data.", f_txt)
    wb.define_name("BLANK_PAR_POOL", "=Step1_Blank!$K$6"); wb.define_name("BLANK_PERP_POOL", "=Step1_Blank!$L$6")
    wb.define_name("BLANK_TOTAL", "=Step1_Blank!$K$12")

    # ================= Step2_Wells =================
    W = S["Step2_Wells"]
    W.write("A1", "Step 2: per-well calculation (net counts, polarization, anisotropy)", f_title)
    W.merge_range("A2:T3", "For each well: net = raw - blank, in each channel separately.  mP = 1000 x (G x net parallel - net perpendicular) / (G x net parallel + net perpendicular).  Anisotropy r = (G x net par - net perp) / (G x net par + 2 x net perp).  A well is flagged when its gross total intensity is more than the tolerance (Inputs) from the median of its three replicates; the weight column (1 = used) is what the group statistics and the fit use. Type x in 'manual exclude' to drop a well yourself.", f_txt)
    W.set_row(1, 30); W.set_row(2, 14)
    heads = ["Well", "Group", "VLP ug/mL", "VLP nM VP1", "Raw parallel", "Raw perpendicular", "Blank parallel", "Blank perpendicular", "Net parallel", "Net perpendicular",
             "G x net parallel", "mP", "Anisotropy r", "Net total", "Gross total (before blank)", "Replicate median of gross total", "Auto flag", "Manual exclude (x)", "Weight (1 = used)", "Arithmetic in words"]
    W.write_row(4, 0, heads, f_h); W.set_row(4, 54)
    widths = [7, 16, 10, 11, 11, 12, 11, 12, 11, 12, 12, 9, 11, 11, 13, 14, 9, 11, 10, 95]
    for i, wd in enumerate(widths): W.set_column(i, i, wd)
    step2_groups = [dict(name="aptamer alone", conc=0.0, wells=fw)] + [dict(name=f"VLP {g['conc']:g}", conc=float(g["conc"]), wells=wells(g["wells"])) for g in groups_titr]
    r = FIRST_ROW; grow = {}
    for g in step2_groups:
        grow[g["name"]] = (r, r + len(g["wells"]) - 1)
        for w in g["wells"]:
            e = r
            W.write(e - 1, 0, wname(w), f_bold); W.write(e - 1, 1, g["name"], f_txt); W.write_number(e - 1, 2, g["conc"], f_data)
            W.write_formula(e - 1, 3, f"=C{e}*NM_PER_UG", f_n1)
            W.write_formula(e - 1, 4, "=" + tcell(T_PAR, w), f_n0); W.write_formula(e - 1, 5, "=" + tcell(T_PERP, w), f_n0)
            W.write_formula(e - 1, 6, f"=IF(OR(C{e}=0,BLANK_METHOD=1),BLANK_PAR_POOL,INDEX(Step1_Blank!$D${mrow0}:$D${mrow1},MATCH(C{e},Step1_Blank!$A${mrow0}:$A${mrow1},0)))", f_n0)
            W.write_formula(e - 1, 7, f"=IF(OR(C{e}=0,BLANK_METHOD=1),BLANK_PERP_POOL,INDEX(Step1_Blank!$E${mrow0}:$E${mrow1},MATCH(C{e},Step1_Blank!$A${mrow0}:$A${mrow1},0)))", f_n0)
            W.write_formula(e - 1, 8, f"=E{e}-G{e}", f_n0); W.write_formula(e - 1, 9, f"=F{e}-H{e}", f_n0)
            W.write_formula(e - 1, 10, f"=G_FACTOR*I{e}", f_n0)
            W.write_formula(e - 1, 11, f"=1000*(K{e}-J{e})/(K{e}+J{e})", f_n1)
            W.write_formula(e - 1, 12, f"=(K{e}-J{e})/(K{e}+2*J{e})", f_n3)
            W.write_formula(e - 1, 13, f"=K{e}+2*J{e}", f_n0); W.write_formula(e - 1, 14, f"=G_FACTOR*E{e}+2*F{e}", f_n0)
            g0, g1 = grow[g["name"]]
            W.write_formula(e - 1, 15, f"=MEDIAN($O${g0}:$O${g0 + len(g['wells']) - 1})", f_n0)
            W.write_formula(e - 1, 16, f'=IF(ABS(O{e}-P{e})>FLAG_TOL*P{e},"flag","ok")', f_txt)
            W.write(e - 1, 17, "", f_in)
            W.write_formula(e - 1, 18, f'=IF(AND(Q{e}="ok",R{e}=""),1,0)', f_n0)
            W.write_formula(e - 1, 19, f'="Net par = "&TEXT(E{e},"#,##0")&" - "&TEXT(G{e},"#,##0")&" = "&TEXT(I{e},"#,##0")&";  net perp = "&TEXT(F{e},"#,##0")&" - "&TEXT(H{e},"#,##0")&" = "&TEXT(J{e},"#,##0")&";  G x net par = "&TEXT(K{e},"#,##0")&";  mP = 1000 x ("&TEXT(K{e},"#,##0")&" - "&TEXT(J{e},"#,##0")&") / ("&TEXT(K{e},"#,##0")&" + "&TEXT(J{e},"#,##0")&") = "&TEXT(L{e},"0.0")', f_txt)
            r += 1
    LAST = r - 1
    for col in "CLNQS": pass
    W.freeze_panes(5, 2)
    rng2 = lambda c: f"Step2_Wells!${c}${FIRST_ROW}:${c}${LAST}"

    # ================= Step3_Groups =================
    GS = S["Step3_Groups"]
    GS.write("A1", "Step 3: average the replicates", f_title)
    GS.merge_range("A2:L3", "For each VLP concentration: mean of the mP of the wells that are used (weight 1), the sample standard deviation SD = sqrt( sum (x - mean)^2 / (n - 1) ), the standard error SD / sqrt(n), and the mean net total intensity (brightness). The brightness ratio compares each group with the aptamer alone: if it falls, the bound aptamer is dimmer than the free one.", f_txt)
    GS.set_row(1, 30); GS.set_row(2, 14)
    GS.write_row(4, 0, ["Group", "VLP ug/mL", "VLP nM VP1", "n used", "Mean mP", "SD (mP)", "SEM (mP)", "CV (%)", "Mean net total", "Brightness vs aptamer alone", "Fraction bound at the fitted curve", "Fitted mP"], f_h)
    GS.set_row(4, 54)
    for i, wd in enumerate([14, 11, 11, 8, 10, 10, 10, 9, 14, 16, 16, 11]): GS.set_column(i, i, wd)
    for i, g in enumerate(step2_groups):
        e = FIRST_ROW + i
        GS.write(e - 1, 0, g["name"], f_bold); GS.write_number(e - 1, 1, g["conc"], f_data)
        GS.write_formula(e - 1, 2, f"=B{e}*NM_PER_UG", f_n1)
        GS.write_formula(e - 1, 3, f"=SUMIFS({rng2('S')},{rng2('C')},B{e})", f_n0)
        GS.write_formula(e - 1, 4, f"=SUMPRODUCT(({rng2('C')}=B{e})*{rng2('S')}*{rng2('L')})/D{e}", f_n1)
        GS.write_formula(e - 1, 5, f"=SQRT((SUMPRODUCT(({rng2('C')}=B{e})*{rng2('S')}*{rng2('L')}^2)-D{e}*E{e}^2)/(D{e}-1))", f_n1)
        GS.write_formula(e - 1, 6, f"=F{e}/SQRT(D{e})", f_n1); GS.write_formula(e - 1, 7, f"=F{e}/E{e}*100", f_n1)
        GS.write_formula(e - 1, 8, f"=SUMPRODUCT(({rng2('C')}=B{e})*{rng2('S')}*{rng2('N')})/D{e}", f_n0)
        GS.write_formula(e - 1, 9, f"=I{e}/$I${FIRST_ROW}", f_n2)
        if i > 0:
            GS.write_formula(e - 1, 10, f"=(L{e}-A_BASE)/B_AMP", f_n2)
        GS.write_formula(e - 1, 11, f"=A_BASE+B_AMP*B{e}/(K_BEST+B{e})", f_n1)
    NG = len(step2_groups); G_LAST = FIRST_ROW + NG - 1
    GS.write(G_LAST + 1, 0, "Fraction bound = (fitted mP - baseline) / (plateau - baseline) at that concentration, from the fit on Step 4.", f_note)
    # fix: fraction bound uses fitted mP column L, defined above (col index 11 = L)

    # ================= Step4_Fit =================
    FT = S["Step4_Fit"]; FT.set_column("A:A", 46); FT.set_column("B:B", 16); FT.set_column("C:C", 16); FT.set_column("D:H", 15)
    FT.write("A1", "Step 4: find the K_d", f_title)
    FT.merge_range("A2:H3", "K_d is the VLP concentration at which the signal is halfway between the free baseline and the fully bound plateau. Two ways to find it: (A) by hand, by interpolating where the curve of the means crosses the halfway line; (B) by least squares: the best curve of the form mP = baseline + amplitude x c / (K_d + c), using every single well. Part B is done with formulas on sheet Step4b_Scan: for each trial K_d the best baseline and amplitude have a closed form (a straight-line fit of mP against c/(K_d + c)), and the K_d with the smallest sum of squared residuals wins.", f_txt)
    FT.set_row(1, 40); FT.set_row(2, 40)
    FT.write("A5", "A. Estimate by hand (interpolation)", f_sub)
    FT.write("A6", "Free baseline = mean of the aptamer-alone wells", f_txt); FT.write_formula("B6", f"=Step3_Groups!E{FIRST_ROW}", f_n1)
    top1, top2 = G_LAST, G_LAST - 1
    FT.write("A7", "Plateau (observed) = mean of the two highest VLP concentrations", f_txt); FT.write_formula("B7", f"=AVERAGE(Step3_Groups!E{top2}:E{top1})", f_n1)
    FT.write("A8", "Halfway signal = (baseline + plateau) / 2", f_txt); FT.write_formula("B8", "=(B6+B7)/2", f_n1)
    FT.write("A9", "K_d by hand (ug/mL) = 10^(interpolated log10 crossing)", f_bold); FT.write_formula("B9", "=10^MIN(F13:F23)", f_key)
    FT.write("A10", "K_d by hand (nM VP1)", f_txt); FT.write_formula("B10", "=B9*NM_PER_UG", f_n1)
    FT.write_row(11, 0, ["Neighbouring groups (ascending VLP)", "VLP ug/mL (lower)", "VLP ug/mL (upper)", "Mean mP (lower)", "Mean mP (upper)", "log10 K_d if the curve crosses here"], f_h); FT.set_row(11, 42)
    for i in range(NG - 2):               # pairs among the 12 concentration groups (rows FIRST_ROW+1 ...)
        e = 13 + i; s = FIRST_ROW + 1 + i
        FT.write_formula(e - 1, 0, f'=Step3_Groups!A{s}&" to "&Step3_Groups!A{s + 1}', f_txt)
        FT.write_formula(e - 1, 1, f"=Step3_Groups!B{s}", f_n2); FT.write_formula(e - 1, 2, f"=Step3_Groups!B{s + 1}", f_n2)
        FT.write_formula(e - 1, 3, f"=Step3_Groups!E{s}", f_n1); FT.write_formula(e - 1, 4, f"=Step3_Groups!E{s + 1}", f_n1)
        FT.write_formula(e - 1, 5, f'=IF(AND(D{e}<=$B$8,E{e}>$B$8),LOG10(B{e})+($B$8-D{e})/(E{e}-D{e})*(LOG10(C{e})-LOG10(B{e})),"")', f_n4)
    FT.write("A26", "B. Least-squares fit (done with formulas; scan on sheet Step4b_Scan)", f_sub)
    FT.write("A27", "Wells used (n)", f_txt); FT.write_formula("B27", f"=SUM({rng2('S')})", f_n0)
    FT.write("A28", "Sum of mP, Sy", f_txt); FT.write_formula("B28", f"=SUMPRODUCT({rng2('S')},{rng2('L')})", f_n1)
    FT.write("A29", "Sum of mP squared, Syy", f_txt); FT.write_formula("B29", f"=SUMPRODUCT({rng2('S')},{rng2('L')},{rng2('L')})", f_n0)
    FT.write("A30", "Scan start (log10 K_d, ug/mL)", f_txt); FT.write_number("B30", -2, f_in)
    FT.write("A31", "Scan step (log10 units)", f_txt); FT.write_number("B31", 1 / 300, F(font_color="#0000FF", bg_color="#FFF2CC", border=1, num_format="0.00000"))
    FT.write("A32", "Best K_d (ug/mL): the scanned K_d with the smallest SSE", f_bold); FT.write_formula("B32", f"=INDEX(Step4b_Scan!B7:B1207,MATCH(B36,Step4b_Scan!H7:H1207,0))", f_key)
    FT.write("A33", "Baseline at the best K_d (mP)", f_txt); FT.write_formula("B33", f"=INDEX(Step4b_Scan!G7:G1207,MATCH(B36,Step4b_Scan!H7:H1207,0))", f_n1)
    FT.write("A34", "Amplitude (plateau - baseline) (mP)", f_txt); FT.write_formula("B34", f"=INDEX(Step4b_Scan!F7:F1207,MATCH(B36,Step4b_Scan!H7:H1207,0))", f_n1)
    FT.write("A35", "Plateau (mP)", f_txt); FT.write_formula("B35", "=B33+B34", f_n1)
    FT.write("A36", "Smallest sum of squared residuals, SSE", f_txt); FT.write_formula("B36", "=MIN(Step4b_Scan!H7:H1207)", f_n0)
    FT.write("A37", "Degrees of freedom (n - 3)", f_txt); FT.write_formula("B37", "=B27-3", f_n0)
    FT.write("A38", "Residual SD = sqrt(SSE / df) (mP)", f_txt); FT.write_formula("B38", "=SQRT(B36/B37)", f_n1)
    FT.write("A39", "SSE threshold for the 95% interval = SSE x (1 + F(0.05; 1, df) / df), where F = t squared", f_txt); FT.write_formula("B39", "=Step4b_Scan!K6", f_n0)
    FT.write("A40", "95% interval for K_d, lower (ug/mL)", f_txt); FT.write_formula("B40", "=MIN(Step4b_Scan!I7:I1207)", f_n2)
    FT.write("A41", "95% interval for K_d, upper (ug/mL)", f_txt); FT.write_formula("B41", "=MAX(Step4b_Scan!I7:I1207)", f_n2)
    FT.write("A42", "Scan resolution check: lowest and highest scanned K_d must not touch the interval", f_note)
    FT.write_formula("B42", '=IF(AND(B40>MIN(Step4b_Scan!B7:B1207)*1.05,B41<MAX(Step4b_Scan!B7:B1207)/1.05),"OK","Widen the scan")', f_bold)
    for nm, cell in (("K_BEST", "B32"), ("A_BASE", "B33"), ("B_AMP", "B34"), ("PLATEAU", "B35"), ("SSE_MIN", "B36"), ("FIT_N", "B27"), ("FIT_SY", "B28"), ("FIT_SYY", "B29"),
                     ("LOGK_START", "B30"), ("LOGK_STEP", "B31"), ("K_LOW", "B40"), ("K_HIGH", "B41"), ("RESID_SD", "B38"), ("FIT_THR", "B39")):
        wb.define_name(nm, f"=Step4_Fit!${cell[0]}${cell[1:]}")
    FT.write("A44", "C. Hill model and bootstrap (static values computed offline in Python; they do NOT update when you change inputs)", f_sub)
    FT.write_row(44, 0, ["Quantity", "Value", "Note"], f_h)
    static = [("Hill model: K (ug/mL)", p2[2], "four-parameter fit"), ("Hill coefficient n", p2[3], f"+/- {se2[3]:.2f}; near 1 = one-to-one-type binding"),
              ("Bootstrap median K_d (ug/mL)", bq[1], "2,000 resamples of the wells within each concentration"), ("Bootstrap 95% range, low", bq[0], ""), ("Bootstrap 95% range, high", bq[2], ""),
              ("Settings for these static values", f"G = {G0}, blank method 1", "")]
    for i, (k, v, n) in enumerate(static):
        FT.write(45 + i, 0, k, f_txt)
        (FT.write_number if isinstance(v, (float, np.floating)) else FT.write)(45 + i, 1, v if not isinstance(v, np.floating) else float(v), f_n2 if isinstance(v, (float, np.floating)) else f_txt)
        FT.write(45 + i, 2, n, f_note)
    FT.write("A53", "D. Observed against fitted, every well", f_sub)
    FT.write_row(53, 0, ["Well", "VLP ug/mL", "mP (observed)", "Fitted mP", "Residual", "Weight"], f_h)
    for i in range(LAST - FIRST_ROW + 1):
        e = 55 + i; s = FIRST_ROW + i
        FT.write_formula(e - 1, 0, f"=Step2_Wells!A{s}", f_txt); FT.write_formula(e - 1, 1, f"=Step2_Wells!C{s}", f_n2)
        FT.write_formula(e - 1, 2, f"=Step2_Wells!L{s}", f_n1); FT.write_formula(e - 1, 3, f"=A_BASE+B_AMP*B{e}/(K_BEST+B{e})", f_n1)
        FT.write_formula(e - 1, 4, f"=C{e}-D{e}", f_n1); FT.write_formula(e - 1, 5, f"=Step2_Wells!S{s}", f_n0)
    FT.freeze_panes(4, 1)

    # ================= Step4b_Scan =================
    SC = S["Step4b_Scan"]; SC.set_column("A:I", 15)
    SC.write("A1", "Step 4b: the least-squares scan (1,201 trial values of K_d)", f_title)
    SC.merge_range("A2:I4", "For a trial K_d, let f = c / (K_d + c) for each well. The best curve mP = baseline + amplitude x f is a straight-line fit: amplitude = (Sfy - Sf Sy / n) / (Sff - Sf^2 / n), baseline = (Sy - amplitude Sf) / n, and SSE = (Syy - Sy^2 / n) - amplitude (Sfy - Sf Sy / n). Weights (1 or 0) switch wells on or off. The row with the smallest SSE is the least-squares K_d. The last column keeps only the K_d values whose SSE is below the 95% threshold (Step4_Fit), which gives the confidence interval.", f_txt)
    SC.write_row(5, 0, ["log10 K_d", "K_d (ug/mL)", "Sf = sum w f", "Sff = sum w f^2", "Sfy = sum w f mP", "Amplitude", "Baseline", "SSE", "K_d inside 95% interval"], f_h); SC.set_row(5, 42)
    SC.write("J5", "Smallest SSE", f_txt); SC.write_formula("K5", "=MIN(H7:H1207)", f_n1)
    SC.write("J6", "SSE threshold (95%)", f_txt); SC.write_formula("K6", "=K5*(1+FINV(0.05,1,FIT_N-3)/(FIT_N-3))", f_n1)
    cR, yR, wR = rng2("C"), rng2("L"), rng2("S")
    for i in range(1201):
        e = 7 + i
        SC.write_formula(e - 1, 0, "=LOGK_START" if i == 0 else f"=A{e - 1}+LOGK_STEP", f_n3)
        SC.write_formula(e - 1, 1, f"=10^A{e}", f_n4)
        SC.write_formula(e - 1, 2, f"=SUMPRODUCT({wR},{cR}/(B{e}+{cR}))", f_n4)
        SC.write_formula(e - 1, 3, f"=SUMPRODUCT({wR},{cR}/(B{e}+{cR}),{cR}/(B{e}+{cR}))", f_n4)
        SC.write_formula(e - 1, 4, f"=SUMPRODUCT({wR},{cR}/(B{e}+{cR}),{yR})", f_n2)
        SC.write_formula(e - 1, 5, f"=(E{e}-C{e}*FIT_SY/FIT_N)/(D{e}-C{e}^2/FIT_N)", f_n2)
        SC.write_formula(e - 1, 6, f"=(FIT_SY-F{e}*C{e})/FIT_N", f_n2)
        SC.write_formula(e - 1, 7, f"=(FIT_SYY-FIT_SY^2/FIT_N)-F{e}*(E{e}-C{e}*FIT_SY/FIT_N)", f_n1)
        SC.write_formula(e - 1, 8, f'=IF(H{e}<=$K$6,B{e},"")', f_n4)
    SC.freeze_panes(6, 1)

    # ================= Step5_Results =================
    RS = S["Step5_Results"]; RS.set_column("A:A", 56); RS.set_column("B:B", 16); RS.set_column("C:C", 18); RS.set_column("D:D", 70)
    RS.write("A1", "Step 5: result, units and quality checks", f_title)
    RS.write("A3", "A. The K_d in every unit", f_sub); RS.write_row(3, 0, ["Quantity", "Value", "95% interval low", "95% interval high / note"], f_h)
    RS.write("A5", "K_d (ug/mL of VLP protein)", f_bold); RS.write_formula("B5", "=K_BEST", f_key); RS.write_formula("C5", "=K_LOW", f_n2); RS.write_formula("D5", "=K_HIGH", F(num_format="0.00", align="left"))
    RS.write("A6", "K_d (nM VP1 monomer) = ug/mL x nM per ug/mL", f_txt); RS.write_formula("B6", "=B5*NM_PER_UG", f_key1); RS.write_formula("C6", "=C5*NM_PER_UG", f_n1); RS.write_formula("D6", "=D5*NM_PER_UG", F(num_format="0.0", align="left"))
    RS.write("A7", "K_d (nM VP1 dimers) = VP1 / 2", f_txt); RS.write_formula("B7", "=B6/2", f_n1); RS.write_formula("C7", "=C6/2", f_n1); RS.write_formula("D7", "=D6/2", F(num_format="0.0", align="left"))
    RS.write("A8", "K_d (nM whole particles) = VP1 / VP1 per VLP", f_txt); RS.write_formula("B8", "=B6/VP1_PER_VLP", f_n3); RS.write_formula("C8", "=C6/VP1_PER_VLP", f_n3); RS.write_formula("D8", "=D6/VP1_PER_VLP", F(num_format="0.000", align="left"))
    RS.write("A9", "K_d by hand (ug/mL), for comparison", f_txt); RS.write_formula("B9", "=Step4_Fit!B9", f_n2); RS.write("D9", "should agree with the fit within the interval", f_note)
    RS.write("A10", "Depletion-corrected K_d (nM VP1) = K_d - aptamer / 2", f_txt); RS.write_formula("B10", "=B6-APT_NM/2", f_n1)
    RS.write("D10", "The half-point of the curve is K_d + [aptamer]/2 because bound aptamer uses up VLP; small when K_d is much larger than the aptamer.", f_note)
    RS.write("A11", "Baseline / plateau of the fit (mP)", f_txt); RS.write_formula("B11", "=A_BASE", f_n1); RS.write_formula("C11", "=PLATEAU", f_n1)
    RS.write("A12", "Residual SD of the fit (mP)", f_txt); RS.write_formula("B12", "=RESID_SD", f_n1)
    RS.write("A14", "B. Quality checks (formulas; thresholds in column D)", f_sub); RS.write_row(14, 0, ["Check", "Value", "Verdict", "Criterion"], f_h)
    sig_ratio = f"SUMPRODUCT(({rng2('C')}>0)*{rng2('S')}*{rng2('N')})/SUMPRODUCT(({rng2('C')}>0)*{rng2('S')})/BLANK_TOTAL"
    F1 = wells(lay["reference"]["fluorescein"]); FB = wells(lay["reference"]["fl_buffer"])
    fl_buf_par = f"AVERAGE({','.join(tcell(T_PAR, w) for w in FB)})"; fl_buf_perp = f"AVERAGE({','.join(tcell(T_PERP, w) for w in FB)})"
    checks = [
        ("Plateau test: change from the 2nd-highest to the highest VLP (%)", f"=(Step3_Groups!E{top1}-Step3_Groups!E{top2})/Step3_Groups!E{top1}*100", "0.0",
         '=IF(B{r}<5,"Pass",IF(B{r}<10,"Caution","Fail"))', "Below 5 % = the curve is flat at the top"),
        ("Saturation at the highest VLP (% of the fitted curve)", f"=Step3_Groups!B{top1}/(K_BEST+Step3_Groups!B{top1})*100", "0",
         '=IF(B{r}>=90,"Pass",IF(B{r}>=80,"Caution","Fail"))', "90 % or more = a well-defined plateau"),
        ("Points on the rise (fraction bound 0.2 to 0.8)", f'=COUNTIFS(Step3_Groups!K{FIRST_ROW + 1}:K{G_LAST},">=0.2",Step3_Groups!K{FIRST_ROW + 1}:K{G_LAST},"<=0.8")', "0",
         '=IF(B{r}>=4,"Pass",IF(B{r}>=3,"Caution","Fail"))', "At least 4 concentrations"),
        ("Signal over blank (mean net total / blank total)", f"={sig_ratio}", "0.0", '=IF(B{r}>=3,"Pass",IF(B{r}>=2,"Caution","Fail"))', "3 or more; lower values scatter more (lid on)"),
        ("SD of the aptamer-alone wells (mP)", f"=Step3_Groups!F{FIRST_ROW}", "0.0", '=IF(B{r}<=8,"Pass",IF(B{r}<=12,"Caution","Fail"))', "8 mP or less"),
        ("Typical SD of the replicates (median of the group SDs, mP)", f"=MEDIAN(Step3_Groups!F{FIRST_ROW + 1}:F{G_LAST})", "0.0", '=IF(B{r}<=10,"Pass",IF(B{r}<=15,"Caution","Fail"))', "10 mP or less"),
        ("Brightness ratio, highest VLP / aptamer alone (Q)", f"=Step3_Groups!J{top1}", "0.00", '=IF(B{r}>=0.8,"Pass",IF(B{r}>=0.6,"Caution","Fail"))', "Within 20 % of 1; lower means the plain fit may overestimate K_d"),
        ("Wells flagged or excluded", f'=COUNTIF({rng2("Q")},"flag")+COUNTIF({rng2("R")},"x")', "0", '=IF(B{r}=0,"Pass","Caution")', "List every one in the report"),
        ("Blank trend with VLP (slope, % of median per decade; parallel)", "=Step1_Blank!K17", "0.0", '=IF(ABS(B{r})<5,"Pass","Fail")', "Under 5 % = no VLP scatter"),
        ("Fluorescein check: largest distance from 20 mP", "=MAX(ABS(B34-20),ABS(B35-20),ABS(B36-20))", "0.0", '=IF(B{r}<=15,"Pass","Caution")', "Within 15 mP; G for 20 mP in the table below"),
        ("Hand estimate and fit agree (ratio)", "=Step4_Fit!B9/K_BEST", "0.00", '=IF(AND(B{r}>0.8,B{r}<1.25),"Pass","Caution")', "Between 0.8 and 1.25"),
    ]
    for i, (lab, fml, nf, verdict, crit) in enumerate(checks):
        r = 16 + i
        RS.write(r - 1, 0, lab, f_txt); RS.write_formula(r - 1, 1, fml, F(num_format=nf)); RS.write_formula(r - 1, 2, verdict.format(r=r), f_bold); RS.write(r - 1, 3, crit, f_note)
    RS.conditional_format("C16:C26", {"type": "cell", "criteria": "==", "value": '"Pass"', "format": f_pass})
    RS.conditional_format("C16:C26", {"type": "cell", "criteria": "==", "value": '"Caution"', "format": f_warn})
    RS.conditional_format("C16:C26", {"type": "cell", "criteria": "==", "value": '"Fail"', "format": f_fail})
    RS.write("A30", "C. Fluorescein reference wells (instrument and G check)", f_sub)
    RS.write_row(32, 0, ["Well", "mP at the G used", "Net parallel", "Net perpendicular", "G that would give 20 mP"], f_h)
    for i, w in enumerate(F1):
        e = 34 + i
        RS.write(e - 1, 0, wname(w), f_txt)
        RS.write_formula(e - 1, 2, f"={tcell(T_PAR, w)}-{fl_buf_par}", f_n0); RS.write_formula(e - 1, 3, f"={tcell(T_PERP, w)}-{fl_buf_perp}", f_n0)
        RS.write_formula(e - 1, 1, f"=1000*(G_FACTOR*C{e}-D{e})/(G_FACTOR*C{e}+D{e})", f_n1); RS.write_formula(e - 1, 4, f"=1.0408*D{e}/C{e}", f_n3)
    RS.write("A38", "Mean G that would give 20 mP", f_txt); RS.write_formula("E38", "=AVERAGE(E34:E36)", f_n3)
    RS.write("A39", "Net = raw - mean of the fluorescein-buffer wells (F4-F6). 1.0408 = (1 + 0.02) / (1 - 0.02), the factor for a 20 mP reference.", f_note)
    RS.write("A41", "D. What this does and does not show", f_sub)
    RS.merge_range("A42:D46", "Shows: a smooth, one-to-one-type binding curve with a window of about 200 mP and an apparent K_d near 2 ug/mL. Does not yet show: that the binding is specific (no scrambled-aptamer, competitor or off-target VLP wells on this plate), that equilibrium was reached (no second read time), or that a second plate agrees. The bound aptamer is dimmer than the free aptamer (Q well below 1), so the plain K_d may be slightly high; and with the lid on the aptamer signal is only about 1.6x the blank, so single wells scatter by 5-25 mP.", f_txt)

    # ================= Chart =================
    CH = S["Chart"]; CH.set_column("A:E", 16)
    CH.write("A1", "Binding curve: polarization against VLP concentration", f_title)
    CH.write("A55", "Chart data", f_sub)
    CH.write_row(55, 0, ["VLP ug/mL (curve grid)", "Fitted curve mP", "K_d line x", "K_d line y", "Baseline x", "Baseline y"], f_h); CH.set_row(55, 30)
    xs = np.geomspace(0.14, 40, 61)
    for i, x in enumerate(xs):
        e = 57 + i
        CH.write_number(e - 1, 0, float(x), f_n3); CH.write_formula(e - 1, 1, f"=A_BASE+B_AMP*A{e}/(K_BEST+A{e})", f_n1)
    for i, yv in enumerate((0, 320)):
        CH.write_formula(56 + i, 2, "=K_BEST", f_n2); CH.write_number(56 + i, 3, yv, f_n0)
    for i, xv in enumerate((0.14, 40)):
        CH.write_number(56 + i, 4, xv, f_n2); CH.write_formula(56 + i, 5, f"=Step3_Groups!E{FIRST_ROW}", f_n1)

    def make_chart(log):
        ch = wb.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
        ch.add_series({"name": "single wells", "categories": f"=Step2_Wells!$C${FIRST_ROW + 3}:$C${LAST}", "values": f"=Step2_Wells!$L${FIRST_ROW + 3}:$L${LAST}",
                       "line": {"none": True}, "marker": {"type": "circle", "size": 5, "fill": {"color": "#BFBFBF"}, "border": {"color": "#7F7F7F"}}})
        ch.add_series({"name": "mean +/- SD", "categories": f"=Step3_Groups!$B${FIRST_ROW + 1}:$B${G_LAST}", "values": f"=Step3_Groups!$E${FIRST_ROW + 1}:$E${G_LAST}",
                       "line": {"color": DARK, "width": 2.0}, "marker": {"type": "circle", "size": 7, "fill": {"color": DARK}, "border": {"color": DARK}},
                       "y_error_bars": {"type": "custom", "plus_values": f"=Step3_Groups!$F${FIRST_ROW + 1}:$F${G_LAST}", "minus_values": f"=Step3_Groups!$F${FIRST_ROW + 1}:$F${G_LAST}", "line": {"color": DARK}}})
        ch.add_series({"name": "fitted curve", "categories": "=Chart!$A$57:$A$117", "values": "=Chart!$B$57:$B$117", "line": {"color": "#C00000", "width": 2.0, "dash_type": "dash"}, "marker": {"type": "none"}})
        ch.add_series({"name": "K_d", "categories": "=Chart!$C$57:$C$58", "values": "=Chart!$D$57:$D$58", "line": {"color": "#C00000", "width": 1.0, "dash_type": "round_dot"}, "marker": {"type": "none"}})
        ch.add_series({"name": "aptamer alone", "categories": "=Chart!$E$57:$E$58", "values": "=Chart!$F$57:$F$58", "line": {"color": "#595959", "width": 1.0, "dash_type": "square_dot"}, "marker": {"type": "none"}})
        xa = {"name": "VLP concentration (ug/mL)", "min": 0.14 if log else 0, "max": 40 if log else 30, "major_gridlines": {"visible": True, "line": {"color": "#E7E6E6"}}}
        if log: xa["log_base"] = 10
        ch.set_x_axis(xa); ch.set_y_axis({"name": "Polarization (mP)", "min": 0, "max": 320, "major_gridlines": {"visible": True, "line": {"color": "#E7E6E6"}}})
        ch.set_title({"name": f"{a.label} + VLP: polarization vs VLP ({'log' if log else 'linear'} x axis)", "name_font": {"size": 12}})
        ch.set_legend({"position": "bottom"}); ch.set_size({"width": 900, "height": 400})
        return ch
    CH.insert_chart("A3", make_chart(True)); CH.insert_chart("A30", make_chart(False))

    # ================= Worked_Example =================
    WE = S["Worked_Example"]; WE.set_column("A:A", 6); WE.set_column("B:B", 46); WE.set_column("C:C", 52); WE.set_column("D:D", 18)
    WE.write("A1", "Worked example: follow one well through every step", f_title)
    WE.write("B3", "Choose a well (type its name, e.g. A1, B10, F11):", f_bold); WE.write("C3", "A1", f_in)
    WE.write("B4", "Row in the Step 2 table", f_txt); WE.write_formula("C4", f"=MATCH(C3,Step2_Wells!$A${FIRST_ROW}:$A${LAST},0)", f_n0)
    WE.write_row(5, 0, ["Step", "What happens", "Formula (in words)", "Value"], f_h)
    ix = lambda col: f"INDEX(Step2_Wells!${col}${FIRST_ROW}:${col}${LAST},$C$4)"
    steps = [
        ("Group and VLP concentration (ug/mL)", "from the plate map", f"={ix('B')}&\" ; \"&TEXT({ix('C')},\"0.0\")", None),
        ("1. Raw parallel counts", "Rawdata (parallel) table", f"={ix('E')}", f_n0),
        ("2. Raw perpendicular counts", "Rawdata (perpendicular) table", f"={ix('F')}", f_n0),
        ("3. Blank, parallel", "Step 1 (pooled median of the VLP-only wells)", f"={ix('G')}", f_n0),
        ("4. Blank, perpendicular", "Step 1", f"={ix('H')}", f_n0),
        ("5. Net parallel", "raw parallel - blank parallel", f"={ix('I')}", f_n0),
        ("6. Net perpendicular", "raw perpendicular - blank perpendicular", f"={ix('J')}", f_n0),
        ("7. G factor", "Inputs", "=G_FACTOR", f_n3),
        ("8. G x net parallel", "G x step 5", f"={ix('K')}", f_n0),
        ("9. Numerator", "step 8 - step 6", f"={ix('K')}-{ix('J')}", f_n0),
        ("10. Denominator", "step 8 + step 6", f"={ix('K')}+{ix('J')}", f_n0),
        ("11. Polarization mP", "1000 x numerator / denominator", f"={ix('L')}", f_n1),
        ("12. Anisotropy r", "(G x net par - net perp) / (G x net par + 2 x net perp)", f"={ix('M')}", f_n4),
        ("13. Net total intensity", "G x net par + 2 x net perp (brightness)", f"={ix('N')}", f_n0),
        ("14. Auto flag / weight", "outlier rule and manual override", f'={ix("Q")}&" / "&{ix("S")}', None),
        ("15. Instrument's own mP for this well", "Label 1 [mP] table, NO blank removed", f"=INDEX({trange(T_MP)},CODE(UPPER(LEFT($C$3,1)))-64,VALUE(MID($C$3,2,2)))", f_n0),
        ("16. Background inflation = step 15 - step 11 (mP)", "how much the background raised the instrument's value", "=D22-D18", f_n1),
        ("17. Mean mP of this well's group", "Step 3 (the number that goes on the chart)", f"=INDEX(Step3_Groups!$E${FIRST_ROW}:$E${G_LAST},MATCH({ix('B')},Step3_Groups!$A${FIRST_ROW}:$A${G_LAST},0))", f_n1),
    ]
    for i, (lab, how, fml, fmt) in enumerate(steps):
        r = 7 + i
        WE.write(r - 1, 0, i, f_txt); WE.write(r - 1, 1, lab, f_txt); WE.write(r - 1, 2, how, f_note); WE.write_formula(r - 1, 3, fml, fmt or f_txt)
    WE.write("B26", "Then: the group means (step 17) are plotted against VLP concentration, the curve is fitted (Step 4), and K_d is the concentration at half-maximal polarization.", f_note)

    # ================= Report_Text =================
    RT = S["Report_Text"]; RT.set_column("A:A", 150)
    RT.write("A1", "Text for the report (the numbers update with the workbook)", f_title)
    RT.write("A3", "Result sentence", f_sub)
    RT.write_formula("A4", f'="The apparent K_d of {a.label} for the VLP was "&TEXT(K_BEST,"0.00")&" ug/mL VLP ("&TEXT(Step5_Results!B6,"0")&" nM VP1; 95% interval "&TEXT(K_LOW,"0.00")&" to "&TEXT(K_HIGH,"0.00")&" ug/mL), measured by fluorescence polarization with "&TEXT(APT_NM,"0")&" nM aptamer, "&TEXT(FIT_N,"0")&" wells on one plate, G = "&TEXT(G_FACTOR,"0.000")&", blank method "&BLANK_METHOD&"."', f_txt)
    RT.set_row(3, 48)
    RT.write("A6", "Quality statement", f_sub)
    RT.write_formula("A7", '="Plateau test: "&TEXT(Step5_Results!B16,"0.0")&" % ("&Step5_Results!C16&"); saturation at the top: "&TEXT(Step5_Results!B17,"0")&" % ("&Step5_Results!C17&"); signal over blank "&TEXT(Step5_Results!B19,"0.0")&" ("&Step5_Results!C19&"); brightness ratio Q = "&TEXT(Step5_Results!B22,"0.00")&" ("&Step5_Results!C22&"); wells flagged: "&Step5_Results!B23&"."', f_txt)
    RT.set_row(6, 48)
    RT.write("A9", "Limitations to state", f_sub)
    lim = ["Single plate; specificity (scrambled aptamer, 50x unlabeled competitor, off-target VLP) and equilibrium (second read time) not tested.",
           "The K_d is apparent: one VLP carries many binding sites, and the VLP concentration refers to protein mass (VP1 about 58 kDa).",
           "Bound aptamer is dimmer than free aptamer, which can bias the plain K_d upward; the lid was on, so single wells scatter.",
           "G (about 1.06) was calibrated once; it shifts absolute mP but not the K_d."]
    for i, t in enumerate(lim): RT.write(9 + i, 0, f"- {t}", f_txt)

    # ================= README =================
    RD = S["README"]; RD.set_column("A:A", 3); RD.set_column("B:B", 30); RD.set_column("C:C", 22); RD.set_column("D:D", 90)
    RD.write("B1", f"{a.label} aptamer + norovirus VLP: K_d from fluorescence polarization, step by step", f_title)
    RD.write("B3", "Headline result (live)", f_sub)
    RD.write("B4", "K_d (ug/mL VLP)", f_txt); RD.write_formula("C4", "=Step5_Results!B5", f_key); RD.write_formula("D4", '="95% interval "&TEXT(K_LOW,"0.00")&" to "&TEXT(K_HIGH,"0.00")&" ug/mL (least squares on every well; interval from the SSE profile)"', f_txt)
    RD.write("B5", "K_d (nM VP1)", f_txt); RD.write_formula("C5", "=Step5_Results!B6", f_key1); RD.write_formula("D5", '="interval "&TEXT(Step5_Results!C6,"0")&" to "&TEXT(Step5_Results!D6,"0")&" nM VP1; "&TEXT(Step5_Results!B8,"0.00")&" nM whole particles"', f_txt)
    RD.write("B6", "Source file", f_txt); RD.write("C6", Path(a.xlsx).name, f_data)
    RD.write("B8", "What this workbook does", f_sub)
    RD.merge_range("B9:D12", "A FAM-labeled aptamer (fixed concentration) is mixed with increasing VLP. The small free aptamer tumbles fast (low polarization); bound to a VLP it tumbles slowly (high polarization). The polarization at each VLP concentration is calculated from the raw Tecan counts after removing the background, and the VLP concentration at half-maximal polarization is the K_d. Every number after the raw data is a formula, so you can click any cell and see exactly how it was made.", f_txt)
    RD.write("B14", "The six steps", f_sub); RD.write_row(14, 1, ["Sheet", "Step", "What it does"], f_h)
    smap = [("Inputs", "Settings", "G factor, blank method, outlier tolerance, aptamer concentration, unit conversions (yellow cells)."),
            ("Plate_Map", "Design", "What is in each of the 78 measured wells, and the raw counts and instrument mP of each."),
            ("Raw_Tables", "Data", "The seven tables of the Tecan export. Only the first two are measurements."),
            ("Step1_Blank", "1", "Remove the background: the VLP-only wells, their median per channel, and why one pooled blank is valid."),
            ("Step2_Wells", "2", "Per well: net counts, polarization (mP), anisotropy, outlier flag, with the arithmetic written out."),
            ("Step3_Groups", "3", "Mean, SD, SEM and brightness per VLP concentration."),
            ("Step4_Fit, Step4b_Scan", "4", "K_d by hand (interpolation) and by least squares done with formulas; interval from the SSE profile."),
            ("Step5_Results", "5", "K_d in all units, quality checks with pass / caution / fail, fluorescein G check."),
            ("Chart", "-", "The binding curve (log and linear axes)."),
            ("Worked_Example", "-", "Pick any well and follow it through every step."),
            ("Report_Text", "-", "Ready-made result and quality sentences with live numbers.")]
    for i, (s_, st, wh) in enumerate(smap):
        RD.write(15 + i, 1, s_, f_bold); RD.write(15 + i, 2, st, f_txt); RD.write(15 + i, 3, wh, f_txt)
    RD.write("B28", "Colour code", f_sub)
    RD.write("B29", "Blue text", F(font_color="#0000FF")); RD.write("D29", "numbers typed in or copied from the Tecan file or the plate map", f_txt)
    RD.write("B30", "Blue on yellow", f_in); RD.write("D30", "settings you can change; the whole workbook recalculates", f_txt)
    RD.write("B31", "Black text", f_txt); RD.write("D31", "formulas", f_txt)
    RD.write("B33", "Assumptions and cautions", f_sub)
    cautions = [note_21, "Background: the median of all 24 VLP-only wells is used for every well, including the aptamer-alone wells. These wells show no trend with VLP (Step 1), and the median ignores a contaminated well. A matching-concentration blank (two wells) is available as Blank method 2.",
                "G: the file's calibrated G (stored in the header) is the default. The export's 'Intensity (parallel)' is already multiplied by G; here G is applied to the raw counts, so it is applied once.",
                "G4-G6 are wells of unspecified content and are not used. F7-F9 (aptamer buffer) and G1-G3 (VLP buffer) are used only for the blank comparison in Step 1.",
                "The Hill fit and the bootstrap interval are static values computed offline; the least-squares K_d and its interval are live formulas.",
                "This is an apparent K_d from a single plate. Specificity controls, a second read time and a second plate are still needed."]
    for i, t in enumerate(cautions):
        RD.merge_range(33 + i, 1, 33 + i, 3, f"{i + 1}. {t}", f_txt); RD.set_row(33 + i, 44 if len(t) > 150 else 30)

    S["README"].activate()
    wb.close()
    print("written", a.out)
    print(f"python reference: 1:1 K_d {p1[2]:.4f} ug/mL (G={G0}); Hill K {p2[2]:.3f}, n {p2[3]:.2f}; bootstrap {bq[0]:.2f}-{bq[2]:.2f}")


if __name__ == "__main__":
    main()
