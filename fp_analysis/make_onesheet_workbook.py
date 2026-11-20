#!/usr/bin/env python3
"""ONE-SHEET, step-by-step K_d workbook for a Tecan FP titration plate (every calculation is a live formula).

  python3 -I make_onesheet_workbook.py TECAN.xlsx layout.json OUT.xlsx [--label Buf-2] [--g 1.062]

Then run the xlsx skill's scripts/recalc.py TWICE (first pass can leave dependent cells at 0 in LibreOffice).
Everything is on the sheet "FP_Kd": read it top to bottom. Blue = typed-in / copied data, black = formula.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np, xlsxwriter
from openpyxl import load_workbook
from scipy.optimize import curve_fit
from xlsxwriter.utility import xl_col_to_name as cn

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fp_analysis as fp

LET = "ABCDEFGH"
SH = "FP_Kd"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("xlsx"); ap.add_argument("layout"); ap.add_argument("out")
    ap.add_argument("--label", default="Buf-2"); ap.add_argument("--g", type=float, default=None)
    ap.add_argument("--apt-nM", type=float, default=5.0)
    a = ap.parse_args()
    lay = json.loads(Path(a.layout).read_text())
    hdr, _ = fp.parse_export(a.xlsx)
    G0 = a.g or fp.header_g(hdr) or 1.05

    rows = [list(r) for r in load_workbook(a.xlsx, data_only=True).worksheets[0].iter_rows(values_only=True)]

    def table(name):
        for i, r in enumerate(rows):
            if r and r[0] == name:
                t = {}
                for rr in rows[i + 2:i + 10]:
                    for j in range(12):
                        if isinstance(rr[1 + j], (int, float)): t[(LET.index(rr[0]), j)] = rr[1 + j]
                return t
    PAR, PERP, MPT = table("Rawdata (parallel)"), table("Rawdata (perpendicular)"), table("Label 1 [mP]")

    wells = fp.expand_wells
    wname = lambda w: f"{LET[w[0]]}{w[1] + 1}"
    groups = sorted(lay["titration"], key=lambda g: g["conc"])
    blank_wells = sorted([w for g in groups for w in wells(g["blank_wells"])], key=lambda w: (w[0], w[1]))
    free_w = wells(lay["free"]); FL = wells(lay["reference"]["fluorescein"]); FLB = wells(lay["reference"]["fl_buffer"])
    apt_buf = wells("F7-F9"); vlp_buf = wells("G1-G3")
    conc_of_blank = {w: g["conc"] for g in groups for w in wells(g["blank_wells"])}

    # ---------- offline reference numbers (for the static Hill / bootstrap block and a cross-check) ----------
    bp0 = float(np.median([PAR[w] for w in blank_wells])); bs0 = float(np.median([PERP[w] for w in blank_wells]))
    def mp_of(w):
        gp = G0 * (PAR[w] - bp0); s = PERP[w] - bs0
        return 1000 * (gp - s) / (gp + s)
    cc, yy = [], []
    for g in groups:
        for w in wells(g["wells"]): cc.append(g["conc"]); yy.append(mp_of(w))
    for w in free_w: cc.append(0.0); yy.append(mp_of(w))
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
            x_ += [k] * len(v); y_ += list(rng.choice(v, len(v)))
        try:
            pb, _ = curve_fit(hyp, np.array(x_), np.array(y_), p0=[45, 250, 3], bounds=([0, 0, .01], [300, 800, 500]), maxfev=5000); boot.append(pb[2])
        except Exception: pass
    bq = np.percentile(boot, [2.5, 50, 97.5])

    # ---------- workbook & formats ----------
    wb = xlsxwriter.Workbook(a.out, {"default_format_properties": {"font_name": "Arial", "font_size": 10}})
    F = lambda **k: wb.add_format({"font_name": "Arial", "font_size": 10, **k})
    DARK = "#1F4E79"
    f_title = F(bold=True, font_size=16, font_color=DARK)
    f_band = F(bold=True, font_size=12, font_color="white", bg_color=DARK, valign="vcenter")
    f_h = F(bold=True, font_color="white", bg_color="#2E75B6", text_wrap=True, valign="vcenter", align="center", border=1)
    f_why = F(text_wrap=True, valign="top", bg_color="#EAF1FB", border=1)
    f_how = F(text_wrap=True, valign="top", bg_color="#FFF9E5", border=1, font_color="#5A4A00")
    f_lab = F(); f_labw = F(text_wrap=True, valign="top"); f_bold = F(bold=True)
    f_note = F(italic=True, font_color="#555555", text_wrap=True, valign="top")
    f_in = F(font_color="#0000FF", bg_color="#FFF2CC", border=1)
    f_in3 = F(font_color="#0000FF", bg_color="#FFF2CC", border=1, num_format="0.000")
    f_d0 = F(font_color="#0000FF", num_format="#,##0"); f_dtxt = F(font_color="#0000FF"); f_d2 = F(font_color="#0000FF", num_format="0.0##")
    n0, n1, n2, n3, n4 = (F(num_format=x) for x in ("#,##0", "0.0", "0.00", "0.000", "0.0000"))
    key2 = F(bold=True, font_color=DARK, num_format="0.00", bg_color="#DDEBF7", border=1)
    key1 = F(bold=True, font_color=DARK, num_format="0.0", bg_color="#DDEBF7", border=1)
    f_pass = F(bold=True, font_color="#006100", bg_color="#C6EFCE"); f_warn = F(bold=True, font_color="#9C5700", bg_color="#FFEB9C")
    f_fail = F(bold=True, font_color="#9C0006", bg_color="#FFC7CE")
    rolef = {k: F(bg_color=c, align="center", valign="vcenter", border=1, font_size=8, text_wrap=True) for k, c in
             {"S": "#DDEBF7", "B": "#FCE4D6", "A": "#E2EFDA", "F": "#FFF2CC", "FB": "#FFF9E5", "X": "#EDEDED", "U": "#FFFFFF"}.items()}

    ws = wb.add_worksheet(SH)
    ws.hide_gridlines(2); ws.print_area(0, 0, 700, 18); ws.set_landscape(); ws.set_paper(9); ws.fit_to_pages(1, 0)
    ws.set_column("A:A", 15); ws.set_column("B:S", 12.5); ws.set_column("T:T", 110)

    def put(cell, v, fmt=None):
        if isinstance(v, str):
            (ws.write_formula if v.startswith("=") else ws.write_string)(cell, v, fmt)
        elif v is None: ws.write_blank(cell, None, fmt)
        else: ws.write_number(cell, v, fmt)

    def band(r, text):
        ws.set_row(r - 1, 22); ws.merge_range(f"A{r}:S{r}", text, f_band)

    def box(r, text, fmt, h):
        ws.merge_range(f"A{r}:S{r}", text, fmt); ws.set_row(r - 1, h)

    def kv(r, label, val, fmt, note=None):   # label A:D, value E, note F:S
        ws.merge_range(f"A{r}:D{r}", label, f_labw); put(f"E{r}", val, fmt)
        if note: ws.merge_range(f"F{r}:S{r}", note, f_note)

    names = {}
    def name(nm, cell):
        col = "".join(ch for ch in cell if ch.isalpha()); row = "".join(ch for ch in cell if ch.isdigit())
        wb.define_name(nm, f"={SH}!${col}${row}"); names[nm] = cell

    # =====================================================================================
    r = 1
    ws.write(f"A{r}", f"{a.label} aptamer + norovirus VLP: K_d from fluorescence polarization, step by step (one sheet)", f_title)
    r = 2
    box(r, "How to read this sheet: go from top to bottom. Each step has a blue box (WHAT and WHY), a yellow box (the FORMULA used), then the numbers. "
           "Blue text = data typed in or copied from the Tecan file. Yellow cells = settings you may change. Black = formulas (click any cell to see it). "
           "Every number after the raw data is a live formula, so changing a setting or excluding a well recalculates everything, including the chart.", f_why, 44)
    r = 4
    ws.merge_range(f"A{r}:D{r}", "HEADLINE RESULT", f_bold)
    HEAD = r  # filled in later (needs result cell addresses)

    # ---------------- SETTINGS ----------------
    r = 8
    band(r, "SETTINGS (change the yellow cells; the whole sheet recalculates)")
    S0 = r + 1
    kv(S0, "G factor (multiplies the parallel channel)", G0, f_in3, "From the Tecan file header (fluorescein calibration, 20 mP). It shifts absolute mP by ~10 mP per 0.02 but does not move the K_d.")
    name("G_FACTOR", f"E{S0}")
    kv(S0 + 1, "Outlier tolerance (fraction)", 0.25, f_in, "A well is flagged if its gross total intensity differs from its replicates' median by more than this fraction. Flagged wells get weight 0.")
    name("FLAG_TOL", f"E{S0 + 1}")
    kv(S0 + 2, "Aptamer concentration (nM)", a.apt_nM, f_in, "Fixed in every well; used only for the depletion note.")
    name("APT_NM", f"E{S0 + 2}")
    kv(S0 + 3, "nM VP1 per ug/mL of VLP", 17.14, f_in, "1 ug/mL of VLP protein = 17.14 nM VP1 (VP1 ~58 kDa).")
    name("NM_PER_UG", f"E{S0 + 3}")
    kv(S0 + 4, "VP1 copies per VLP particle", 180, f_in, "T=3 norovirus capsid: 180 VP1 (90 dimers), ~10.4 MDa.")
    name("VP1_PER_VLP", f"E{S0 + 4}")
    inst = (f"Instrument settings in the file header: lid lifter = {hdr.get('lid lifter', '?')}, ex/em = {float(hdr.get('excitation wavelength [nm]', 0)):g}/{float(hdr.get('emission wavelength [nm]', 0)):g} nm, "
            f"mirror = {hdr.get('mirror', '?')}, gain = {hdr.get('gain optimal', hdr.get('gain manual', '?'))}, G in file = {fp.header_g(hdr)}, "
            f"'Measurement Blank' = {hdr.get('measurement blank', '?')} (= the instrument removed NO blank; we do it ourselves in Step 1). Source file: {Path(a.xlsx).name}.")
    ws.merge_range(f"A{S0 + 5}:S{S0 + 5}", inst, f_note); ws.set_row(S0 + 4, 28)

    # ---------------- STEP 0: PLATE MAP + RAW DATA ----------------
    r = S0 + 7
    band(r, "STEP 0 - THE DATA: plate map and the two measured tables from the Tecan file")
    box(r + 1, "WHAT: the plate holds (a) aptamer + VLP at 12 VLP concentrations (3 wells each, blue), (b) VLP only, no aptamer, at the same 12 concentrations (2 wells each, orange; these measure the background), "
               "(c) aptamer alone (green; the 'free' baseline), (d) fluorescein and its buffer (yellow; an instrument/G check), and buffers. "
               "WHY: the Tecan measures light polarized PARALLEL and PERPENDICULAR to the excitation light. Those two raw counts are the only real measurements; everything else is calculated from them.", f_why, 58)
    mp = r + 3; ws.write(f"A{mp - 1}", "Plate map", f_bold)
    ws.write_blank(f"A{mp}", None, f_h)
    for j in range(12): ws.write_number(mp - 1, 1 + j, j + 1, f_h)
    role = {}
    for g in groups:
        for w in wells(g["wells"]): role[w] = ("S", f"apt+VLP {g['conc']:g}")
        for w in wells(g["blank_wells"]): role[w] = ("B", f"VLP only {g['conc']:g}")
    for w in free_w: role[w] = ("A", "aptamer alone")
    for w in FL: role[w] = ("F", "fluorescein 1 nM")
    for w in FLB: role[w] = ("FB", "fluor. buffer")
    for w in apt_buf: role[w] = ("X", "buffer (F7-F9)")
    for w in vlp_buf: role[w] = ("X", "VLP buffer (G1-G3)")
    for w in wells("G4-G6"): role[w] = ("U", "not specified")
    for i in range(7):
        ws.write(mp + i, 0, LET[i], f_h); ws.set_row(mp + i, 30)
        for j in range(12):
            if (i, j) in role: ws.write(mp + i, 1 + j, role[(i, j)][1], rolef[role[(i, j)][0]])
    ws.merge_range(f"N{mp + 1}:S{mp + 4}", "Note: the plate description lists B10-B12 as 2.1 ug/mL and its blank E3-E4 as 2.3; 2.3 (the planned value) is used for both. G4-G6 are not specified and not used.", f_note)
    pr = mp + 9   # parallel grid label row (1-based)
    def grid(r0, title, T):
        ws.write(f"A{r0}", title, f_bold)
        ws.write_blank(f"A{r0 + 1}", None, f_h)
        for j in range(12): ws.write_number(r0, 1 + j, j + 1, f_h)
        for i in range(8):
            ws.write(r0 + 1 + i, 0, LET[i], f_h)
            for j in range(12):
                if (i, j) in T: ws.write_number(r0 + 1 + i, 1 + j, T[(i, j)], f_d0)
        return r0 + 2   # Excel row number of grid row "A"
    PR0 = grid(pr, "Raw counts, PARALLEL (Rawdata (parallel) table of the Tecan file)", PAR)
    QR0 = grid(pr + 11, "Raw counts, PERPENDICULAR (Rawdata (perpendicular) table)", PERP)
    MR0 = grid(pr + 22, "For comparison only: the instrument's own mP table (Label 1 [mP]); NO blank removed, so it is inflated", MPT)
    cell_par = lambda w: f"${cn(1 + w[1])}${PR0 + w[0]}"
    cell_perp = lambda w: f"${cn(1 + w[1])}${QR0 + w[0]}"
    cell_imp = lambda w: f"${cn(1 + w[1])}${MR0 + w[0]}"

    # ---------------- STEP 1: BLANK ----------------
    r = MR0 + 9
    band(r, "STEP 1 - THE BACKGROUND (BLANK): remove it from the COUNTS, in each channel separately")
    box(r + 1, "WHAT: every well also gives light that is not from the aptamer (buffer, plastic, scattered light). That light is strongly polarized and pulls every mP value upward. "
               "The 24 VLP-only wells contain everything except the aptamer, so they measure it. We take the MEDIAN of those 24 wells (ignores a contaminated well) for each channel, and use that one pooled blank for EVERY well, including the aptamer-alone wells. "
               "WHY pooled: if the VLP itself scattered or fluoresced, the blank would rise with VLP concentration. The trend test below shows it does not, so all 24 wells are the same background and a larger n gives a more precise blank. "
               "WHY counts, not mP: counts add, polarization values do not, so the blank is subtracted from counts, never from mP.", f_why, 86)
    box(r + 2, "FORMULA: Blank_parallel = MEDIAN(raw parallel of the 24 VLP-only wells); Blank_perpendicular = MEDIAN(raw perpendicular of the same wells). "
               "Trend test: SLOPE(counts, log10 VLP) as % of the median, and R squared; |slope| < 5 % per decade = no VLP scatter.", f_how, 32)
    b0 = r + 4
    ws.write_row(b0 - 2, 0, ["Well", "VLP ug/mL", "log10 VLP", "Raw parallel", "Raw perpendicular", "Total (G x par + 2 x perp)", "Blank-well mP"], f_h); ws.set_row(b0 - 2, 42)
    for i, w in enumerate(blank_wells):
        e = b0 + i
        ws.write(f"A{e}", wname(w), f_bold); put(f"B{e}", conc_of_blank[w], f_d2); put(f"C{e}", f"=LOG10(B{e})", n3)
        put(f"D{e}", f"={cell_par(w)}", n0); put(f"E{e}", f"={cell_perp(w)}", n0)
        put(f"F{e}", f"=G_FACTOR*D{e}+2*E{e}", n0); put(f"G{e}", f"=1000*(G_FACTOR*D{e}-E{e})/(G_FACTOR*D{e}+E{e})", n0)
    b1 = b0 + len(blank_wells) - 1
    D_, E_, C_ = f"$D${b0}:$D${b1}", f"$E${b0}:$E${b1}", f"$C${b0}:$C${b1}"
    ws.write("I" + str(b0 - 1), "Statistic", f_h); ws.merge_range(f"I{b0 - 1}:K{b0 - 1}", "Statistic", f_h); put(f"L{b0 - 1}", "Parallel", f_h); put(f"M{b0 - 1}", "Perpendicular", f_h)
    stats = [("MEDIAN = pooled blank (USED)", "MEDIAN"), ("Mean", "AVERAGE"), ("Standard deviation", "STDEV"), ("Minimum", "MIN"), ("Maximum", "MAX")]
    for i, (lab, fn) in enumerate(stats):
        e = b0 + i; ws.merge_range(f"I{e}:K{e}", lab, f_bold if i == 0 else f_lab)
        put(f"L{e}", f"={fn}({D_})", n0); put(f"M{e}", f"={fn}({E_})", n0)
    BP, BS = f"L{b0}", f"M{b0}"
    name("BLANK_PAR", BP); name("BLANK_PERP", BS)
    e = b0 + 5; ws.merge_range(f"I{e}:K{e}", "Coefficient of variation (%)", f_lab); put(f"L{e}", f"=L{b0 + 2}/L{b0 + 1}*100", n1); put(f"M{e}", f"=M{b0 + 2}/M{b0 + 1}*100", n1)
    e = b0 + 6; ws.merge_range(f"I{e}:K{e}", "Blank total (G x par + 2 x perp)", f_lab); put(f"L{e}", f"=G_FACTOR*{BP}+2*{BS}", n0); name("BLANK_TOTAL", f"L{e}")
    e = b0 + 7; ws.merge_range(f"I{e}:K{e}", "Blank polarization (mP)", f_lab); put(f"L{e}", f"=1000*(G_FACTOR*{BP}-{BS})/(G_FACTOR*{BP}+{BS})", n0)
    e = b0 + 9; ws.merge_range(f"I{e}:K{e}", "Trend with VLP: slope per decade (counts)", f_lab); put(f"L{e}", f"=SLOPE({D_},{C_})", n0); put(f"M{e}", f"=SLOPE({E_},{C_})", n0)
    e = b0 + 10; ws.merge_range(f"I{e}:K{e}", "Slope as % of the median", f_lab); put(f"L{e}", f"=L{b0 + 9}/{BP}*100", n1); put(f"M{e}", f"=M{b0 + 9}/{BS}*100", n1); TREND = f"L{e}"
    e = b0 + 11; ws.merge_range(f"I{e}:K{e}", "R squared of the trend", f_lab); put(f"L{e}", f"=RSQ({D_},{C_})", n3); put(f"M{e}", f"=RSQ({E_},{C_})", n3)
    e = b0 + 12; ws.merge_range(f"I{e}:K{e}", "Verdict", f_bold); ws.merge_range(f"L{e}:S{e}", "", f_bold)
    put(f"L{e}", f'=IF(AND(ABS(L{b0 + 10})<5,ABS(M{b0 + 10})<5),"No trend with VLP: one pooled blank is valid","Trend with VLP: do not pool")', f_bold)
    # comparison of blanks
    cb = b1 + 3
    ws.write(f"A{cb - 1}", "Why the blank choice matters: the free-aptamer baseline (wells F10-F12) under three possible blanks", f_bold)
    ws.write_row(cb - 1 + 0, 0, [], None)
    ws.write_row(cb, 0, ["Blank used", "", "Parallel", "Perpendicular", "F10 mP", "F11 mP", "F12 mP", "Mean free mP"], f_h); ws.set_row(cb, 30)
    avg = lambda ws_, f_: "AVERAGE(" + ",".join(f_(w) for w in ws_) + ")"
    comp = [("Pooled VLP-only wells (USED)", f"={BP}", f"={BS}"), ("'Aptamer buffer' F7-F9 (buffer only)", "=" + avg(apt_buf, cell_par), "=" + avg(apt_buf, cell_perp)),
            ("'VLP buffer' G1-G3", "=" + avg(vlp_buf, cell_par), "=" + avg(vlp_buf, cell_perp))]
    for i, (lab, fpar, fperp) in enumerate(comp):
        e = cb + 2 + i
        ws.merge_range(f"A{e}:B{e}", lab, f_labw); put(f"C{e}", fpar, n0); put(f"D{e}", fperp, n0)
        for j, w in enumerate(free_w):
            put(f"{cn(4 + j)}{e}", f"=1000*(G_FACTOR*({cell_par(w)}-$C{e})-({cell_perp(w)}-$D{e}))/(G_FACTOR*({cell_par(w)}-$C{e})+({cell_perp(w)}-$D{e}))", n1)
        put(f"H{e}", f"=AVERAGE(E{e}:G{e})", n1)
    ws.merge_range(f"I{cb + 2}:S{cb + 4}", "Reading it: the aptamer-alone wells contain the same buffer fractions as all other wells, so their correct blank is the VLP-only background. A buffer-only blank under-removes the background and "
                   "raises the free baseline by ~12 mP, which makes the lowest VLP points look as if they fall BELOW the free baseline. That is an artefact of the blank choice, not of the data.", f_note)

    # ---------------- STEP 2: PER-WELL ----------------
    r = cb + 7
    band(r, "STEP 2 - EACH WELL: net counts, polarization (mP), anisotropy, outlier flag")
    box(r + 1, "WHAT: for every aptamer well, subtract the blank from each channel (net counts), multiply the parallel channel by G (the instrument's two detection paths are not equally sensitive; G corrects that), then compute polarization. "
               "The weight column (1 = used, 0 = excluded) is set automatically by the outlier rule; type x in 'manual exclude' to drop a well yourself. "
               "WHY: mP is a ratio of the two net channels; it is high when most of the emitted light is parallel (slow-tumbling = bound aptamer) and low when the light is scrambled (fast-tumbling = free aptamer).", f_why, 62)
    box(r + 2, "FORMULAS: net = raw - blank (per channel)  |  mP = 1000 x (G x net_par - net_perp) / (G x net_par + net_perp)  |  anisotropy r = (G x net_par - net_perp) / (G x net_par + 2 x net_perp)  |  "
               "net total = G x net_par + 2 x net_perp (brightness)  |  flag if |gross total - replicate median| > tolerance x median.", f_how, 32)
    w0 = r + 4
    heads = ["Well", "Group", "VLP ug/mL", "VLP nM VP1", "Raw parallel", "Raw perpendicular", "Blank parallel", "Blank perpendicular", "Net parallel", "Net perpendicular",
             "G x net parallel", "mP", "Anisotropy r", "Net total (brightness)", "Gross total (before blank)", "Replicate median, gross total", "Auto flag", "Manual exclude (x)", "Weight (1 = used)", "The arithmetic in words"]
    ws.write_row(w0 - 2, 0, heads, f_h); ws.set_row(w0 - 2, 54)
    sgroups = [dict(name="aptamer alone", conc=0.0, wells=free_w)] + [dict(name=f"VLP {g['conc']:g}", conc=float(g["conc"]), wells=wells(g["wells"])) for g in groups]
    e = w0; gr = {}
    for g in sgroups:
        g0 = e; gr[g["name"]] = (g0, g0 + len(g["wells"]) - 1)
        for w in g["wells"]:
            ws.write(f"A{e}", wname(w), f_bold); ws.write(f"B{e}", g["name"], f_lab); put(f"C{e}", g["conc"], f_d2); put(f"D{e}", f"=C{e}*NM_PER_UG", n1)
            put(f"E{e}", f"={cell_par(w)}", n0); put(f"F{e}", f"={cell_perp(w)}", n0)
            put(f"G{e}", "=BLANK_PAR", n0); put(f"H{e}", "=BLANK_PERP", n0)
            put(f"I{e}", f"=E{e}-G{e}", n0); put(f"J{e}", f"=F{e}-H{e}", n0); put(f"K{e}", f"=G_FACTOR*I{e}", n0)
            put(f"L{e}", f"=1000*(K{e}-J{e})/(K{e}+J{e})", n1); put(f"M{e}", f"=(K{e}-J{e})/(K{e}+2*J{e})", n3)
            put(f"N{e}", f"=K{e}+2*J{e}", n0); put(f"O{e}", f"=G_FACTOR*E{e}+2*F{e}", n0)
            put(f"P{e}", f"=MEDIAN($O${g0}:$O${g0 + len(g['wells']) - 1})", n0)
            put(f"Q{e}", f'=IF(ABS(O{e}-P{e})>FLAG_TOL*P{e},"flag","ok")', f_lab); ws.write_blank(f"R{e}", None, f_in)
            put(f"S{e}", f'=IF(AND(Q{e}="ok",R{e}=""),1,0)', n0)
            put(f"T{e}", f'="net par "&TEXT(E{e},"#,##0")&" - "&TEXT(G{e},"#,##0")&" = "&TEXT(I{e},"#,##0")&";  net perp "&TEXT(F{e},"#,##0")&" - "&TEXT(H{e},"#,##0")&" = "&TEXT(J{e},"#,##0")&";  mP = 1000 x ("&TEXT(K{e},"#,##0")&" - "&TEXT(J{e},"#,##0")&") / ("&TEXT(K{e},"#,##0")&" + "&TEXT(J{e},"#,##0")&") = "&TEXT(L{e},"0.0")', f_lab)
            e += 1
    w1 = e - 1
    col = lambda c: f"${c}${w0}:${c}${w1}"

    # ---------------- STEP 3: GROUPS ----------------
    r = w1 + 3
    band(r, "STEP 3 - AVERAGE THE REPLICATES: mean, SD and brightness at each VLP concentration")
    box(r + 1, "WHAT: for each VLP concentration, average the mP of the wells that are used (weight 1) and compute the sample SD and the SEM. The brightness ratio compares each group's net total intensity with the aptamer alone: "
               "if it falls, bound aptamer is dimmer than free aptamer (this can bias a plain fit). WHY: the means (with SD bars) are what you see on the chart; the fit below uses every single well, not just the means.", f_why, 46)
    box(r + 2, "FORMULAS: mean = SUMPRODUCT(weight x mP)/n  |  SD = sqrt( (sum w mP^2 - n mean^2) / (n - 1) )  |  SEM = SD / sqrt(n)  |  CV = SD / mean  |  fraction bound = (fitted mP - baseline) / amplitude (from the fit in Step 4).", f_how, 32)
    g0r = r + 4
    ws.write_row(g0r - 2, 0, ["Group", "VLP ug/mL", "VLP nM VP1", "n used", "Mean mP", "SD (mP)", "SEM (mP)", "CV (%)", "Mean net total", "Brightness vs aptamer alone", "Fitted mP (Step 4)", "Fraction bound"], f_h); ws.set_row(g0r - 2, 54)
    for i, g in enumerate(sgroups):
        e = g0r + i
        ws.write(f"A{e}", g["name"], f_bold); put(f"B{e}", g["conc"], f_d2); put(f"C{e}", f"=B{e}*NM_PER_UG", n1)
        put(f"D{e}", f"=SUMIFS({col('S')},{col('C')},B{e})", n0)
        put(f"E{e}", f"=SUMPRODUCT(({col('C')}=B{e})*{col('S')}*{col('L')})/D{e}", n1)
        put(f"F{e}", f"=SQRT((SUMPRODUCT(({col('C')}=B{e})*{col('S')}*{col('L')}^2)-D{e}*E{e}^2)/(D{e}-1))", n1)
        put(f"G{e}", f"=F{e}/SQRT(D{e})", n1); put(f"H{e}", f"=F{e}/E{e}*100", n1)
        put(f"I{e}", f"=SUMPRODUCT(({col('C')}=B{e})*{col('S')}*{col('N')})/D{e}", n0); put(f"J{e}", f"=I{e}/$I${g0r}", n2)
        put(f"K{e}", f"=A_BASE+B_AMP*B{e}/(K_BEST+B{e})", n1)
        if i > 0: put(f"L{e}", f"=(K{e}-A_BASE)/B_AMP", n2)
    g1r = g0r + len(sgroups) - 1
    top1, top2 = g1r, g1r - 1

    # ---------------- STEP 4: FIT ----------------
    r = g1r + 3
    band(r, "STEP 4 - FIND THE K_d: the VLP concentration at which half of the aptamer is bound")
    box(r + 1, "WHAT: the binding curve is mP = baseline + amplitude x c / (K_d + c). The K_d is the VLP concentration c at which the signal is halfway between the free baseline and the plateau. "
               "Two ways: (A) BY HAND, find where the curve of the group means crosses the halfway line and interpolate on a log scale; (B) LEAST SQUARES, find the K_d whose curve is closest (smallest sum of squared residuals, SSE) to ALL 39 wells. "
               "WHY two: if they agree, the number does not depend on the method. For (B), for each trial K_d the best baseline and amplitude have a closed form (a straight-line fit of mP against c/(K_d + c)), so no Solver is needed: "
               "the table at the bottom of this sheet tries 241 K_d values and the smallest SSE wins. The 95 % interval is every K_d whose SSE is below SSE_min x (1 + F/df).", f_why, 98)
    box(r + 2, "FORMULAS: halfway = (baseline + plateau)/2  |  log10 K_d = log10 c1 + (halfway - mP1)/(mP2 - mP1) x (log10 c2 - log10 c1)  |  for each trial K_d: f = c/(K_d+c); amplitude = (Sfy - Sf Sy/n)/(Sff - Sf^2/n); "
               "baseline = (Sy - amplitude Sf)/n; SSE = (Syy - Sy^2/n) - amplitude (Sfy - Sf Sy/n)  |  95 % threshold: SSE_min x (1 + FINV(0.05,1,n-3)/(n-3)).", f_how, 46)
    a0 = r + 4
    ws.write(f"A{a0 - 1}", "A. By hand (interpolation)", f_bold)
    kv(a0, "Free baseline = mean mP of the aptamer-alone wells", f"=E{g0r}", n1)
    kv(a0 + 1, "Plateau (observed) = mean of the two highest VLP groups", f"=AVERAGE(E{top2}:E{top1})", n1)
    kv(a0 + 2, "Halfway signal = (baseline + plateau) / 2", f"=(E{a0}+E{a0 + 1})/2", n1)
    HALF = f"$E${a0 + 2}"
    pr0 = a0 + 7
    ws.write_row(pr0 - 2, 0, ["Neighbouring groups", "", "VLP lower", "VLP upper", "mP lower", "mP upper", "log10 K_d if crossed here"], f_h); ws.set_row(pr0 - 2, 30)
    npairs = len(sgroups) - 2
    for i in range(npairs):
        e = pr0 + i; s = g0r + 1 + i
        ws.merge_range(f"A{e}:B{e}", "", f_lab); put(f"A{e}", f'=A{s}&" to "&A{s + 1}', f_lab)
        put(f"C{e}", f"=B{s}", n2); put(f"D{e}", f"=B{s + 1}", n2); put(f"E{e}", f"=E{s}", n1); put(f"F{e}", f"=E{s + 1}", n1)
        put(f"G{e}", f'=IF(AND(E{e}<={HALF},F{e}>{HALF}),LOG10(C{e})+({HALF}-E{e})/(F{e}-E{e})*(LOG10(D{e})-LOG10(C{e})),"")', n4)
    pr1 = pr0 + npairs - 1
    kv(a0 + 3, "K_d by hand (ug/mL) = 10^(crossing)", f"=10^MIN(G{pr0}:G{pr1})", key2, "the first interval where the means cross the halfway line (table below)")
    HAND = f"E{a0 + 3}"
    kv(a0 + 4, "K_d by hand (nM VP1)", f"={HAND}*NM_PER_UG", n1)
    # least squares
    l0 = pr1 + 3
    ws.write(f"A{l0 - 1}", "B. Least squares on every well (scan table is at the bottom of the sheet)", f_bold)
    kv(l0, "Wells used (n)", f"=SUM({col('S')})", n0); name("FIT_N", f"E{l0}")
    kv(l0 + 1, "Sy = sum of mP", f"=SUMPRODUCT({col('S')},{col('L')})", n1); name("FIT_SY", f"E{l0 + 1}")
    kv(l0 + 2, "Syy = sum of mP squared", f"=SUMPRODUCT({col('S')},{col('L')},{col('L')})", n0); name("FIT_SYY", f"E{l0 + 2}")
    kv(l0 + 3, "Scan: first log10 K_d (ug/mL)", -0.55, f_in, "scan covers 0.28 to 10 ug/mL; the check below tells you if you must widen it"); name("LOGK_START", f"E{l0 + 3}")
    kv(l0 + 4, "Scan: step in log10 units", 0.0065, F(font_color="#0000FF", bg_color="#FFF2CC", border=1, num_format="0.0000")); name("LOGK_STEP", f"E{l0 + 4}")
    SC0_PLACE = l0 + 5   # rows for results below, filled after scan location is known
    # chart + quality sections are placed after; compute positions first
    res0 = l0 + 5
    # ---------------- results rows (fit) ----------------
    r_fit = res0
    # scan position: put after everything else; compute later -> use placeholders through names
    # We lay out remaining sections now (results, checks, chart, worked example, notes), then scan.
    # fit-result cells (refer to scan via formulas filled after scan rows are known)
    labels = ["Best K_d (ug/mL) = the scanned K_d with the smallest SSE", "Baseline (mP) at the best K_d", "Amplitude = plateau - baseline (mP)", "Plateau (mP)",
              "Smallest SSE (sum of squared residuals)", "Degrees of freedom (n - 3)", "Residual SD = sqrt(SSE/df) (mP)", "SSE threshold for the 95% interval", "95% interval, lower (ug/mL)", "95% interval, upper (ug/mL)", "Scan range check"]
    for i, lab in enumerate(labels): ws.merge_range(f"A{res0 + i}:D{res0 + i}", lab, f_labw)
    R = {nm: f"E{res0 + i}" for i, nm in enumerate(["K", "BASE", "AMP", "PLAT", "SSE", "DF", "SD", "THR", "LO", "HI", "CHK"])}
    name("K_BEST", R["K"]); name("A_BASE", R["BASE"]); name("B_AMP", R["AMP"])
    # static block
    st0 = res0 + len(labels) + 1
    ws.write(f"A{st0 - 0}", "C. Hill model and bootstrap (STATIC values computed offline in Python; they do not update when you change a setting)", f_bold)
    stat = [("Hill model: K (ug/mL)", float(p2[2]), n2, "four-parameter fit"), ("Hill coefficient n", float(p2[3]), n2, f"+/- {se2[3]:.2f}; near 1 = one-to-one-type binding"),
            ("Bootstrap median K_d (ug/mL)", float(bq[1]), n2, "2,000 resamples of the wells within each concentration"), ("Bootstrap 95% range, low (ug/mL)", float(bq[0]), n2, None), ("Bootstrap 95% range, high (ug/mL)", float(bq[2]), n2, None)]
    for i, (lab, v, fm, nt) in enumerate(stat): kv(st0 + 1 + i, lab, v, fm, nt)

    # ---------------- STEP 5: RESULTS ----------------
    r = st0 + 8
    band(r, "STEP 5 - THE RESULT, in every unit, and quality checks")
    box(r + 1, "WHAT: the K_d in ug/mL of VLP protein (what you pipetted), nM of VP1 (a protein-based unit), nM of dimers, and nM of whole particles (~10.4 MDa each). It is an APPARENT K_d: one VLP carries many binding sites (avidity), "
               "and the number depends on the aptamer concentration and buffer. WHY the checks: a K_d is only trustworthy if the curve flattens at the top, the signal is well above background, replicates agree, and the baseline and background are sane.", f_why, 46)
    k0 = r + 3
    ws.write_row(k0 - 2, 0, ["Quantity", "", "", "", "Value", "95% low", "95% high"], f_h)
    unit = [("K_d (ug/mL of VLP protein)", f"={R['K']}", f"={R['LO']}", f"={R['HI']}", key2), ("K_d (nM VP1 monomer) = ug/mL x nM per ug/mL", f"={R['K']}*NM_PER_UG", f"={R['LO']}*NM_PER_UG", f"={R['HI']}*NM_PER_UG", key1),
            ("K_d (nM VP1 dimers) = VP1 / 2", f"={R['K']}*NM_PER_UG/2", f"={R['LO']}*NM_PER_UG/2", f"={R['HI']}*NM_PER_UG/2", n1),
            ("K_d (nM whole particles) = VP1 / VP1 per VLP", f"={R['K']}*NM_PER_UG/VP1_PER_VLP", f"={R['LO']}*NM_PER_UG/VP1_PER_VLP", f"={R['HI']}*NM_PER_UG/VP1_PER_VLP", n3)]
    for i, (lab, v, lo, hi, fm) in enumerate(unit):
        e = k0 + i; ws.merge_range(f"A{e}:D{e}", lab, f_labw); put(f"E{e}", v, fm); put(f"F{e}", lo, n2 if i < 1 else n1 if i < 3 else n3); put(f"G{e}", hi, n2 if i < 1 else n1 if i < 3 else n3)
    KD_UG, KD_NM = f"E{k0}", f"E{k0 + 1}"
    kv(k0 + 4, "K_d by hand (ug/mL), for comparison", f"={HAND}", n2, "should agree with the fit within the interval")
    kv(k0 + 5, "Depletion note: K_d - aptamer/2 (nM VP1)", f"={KD_NM}-APT_NM/2", n1, "bound aptamer uses up VLP, so the half-point is K_d + [aptamer]/2; small here because K_d >> aptamer")
    kv(k0 + 6, "Baseline / plateau of the fit (mP)", f"={R['BASE']}", n1); put(f"F{k0 + 6}", f"={R['PLAT']}", n1)
    c0 = k0 + 9
    ws.write(f"A{c0 - 1}", "Quality checks (criteria in column G; verdict in column F)", f_bold)
    ws.write_row(c0 - 1, 0, ["Check", "", "", "", "Value", "Verdict", "Criterion"], f_h)
    sig = f"SUMPRODUCT(({col('C')}>0)*{col('S')}*{col('N')})/SUMPRODUCT(({col('C')}>0)*{col('S')})/BLANK_TOTAL"
    flb = lambda f_: "AVERAGE(" + ",".join(f_(w) for w in FLB) + ")"
    checks = [("Plateau test: change from 2nd-highest to highest VLP (%)", f"=(E{top1}-E{top2})/E{top1}*100", "0.0", 'IF(E{r}<5,"Pass",IF(E{r}<10,"Caution","Fail"))', "< 5 % = curve flat at the top"),
              ("Saturation at the highest VLP (% of the fitted curve)", f"=B{top1}/({R['K']}+B{top1})*100", "0", 'IF(E{r}>=90,"Pass",IF(E{r}>=80,"Caution","Fail"))', ">= 90 %"),
              ("Points on the rising part (fraction bound 0.2-0.8)", f'=COUNTIFS(L{g0r + 1}:L{g1r},">=0.2",L{g0r + 1}:L{g1r},"<=0.8")', "0", 'IF(E{r}>=4,"Pass",IF(E{r}>=3,"Caution","Fail"))', ">= 4 concentrations"),
              ("Signal over blank (mean net total / blank total)", f"={sig}", "0.0", 'IF(E{r}>=3,"Pass",IF(E{r}>=2,"Caution","Fail"))', ">= 3; low values scatter more (lid on)"),
              ("SD of the aptamer-alone wells (mP)", f"=F{g0r}", "0.0", 'IF(E{r}<=8,"Pass",IF(E{r}<=12,"Caution","Fail"))', "<= 8 mP"),
              ("Typical SD of replicates (median of group SDs, mP)", f"=MEDIAN(F{g0r + 1}:F{g1r})", "0.0", 'IF(E{r}<=10,"Pass",IF(E{r}<=15,"Caution","Fail"))', "<= 10 mP"),
              ("Brightness ratio, highest VLP / aptamer alone (Q)", f"=J{top1}", "0.00", 'IF(E{r}>=0.8,"Pass",IF(E{r}>=0.6,"Caution","Fail"))', ">= 0.8; lower = plain K_d may be high"),
              ("Wells flagged or excluded", f'=COUNTIF({col("Q")},"flag")+COUNTIF({col("R")},"x")', "0", 'IF(E{r}=0,"Pass","Caution")', "list every one in the report"),
              ("Blank trend with VLP (slope, % of median per decade)", f"={TREND}", "0.0", 'IF(ABS(E{r})<5,"Pass","Fail")', "< 5 %"),
              ("Hand estimate / least-squares K_d", f"={HAND}/{R['K']}", "0.00", 'IF(AND(E{r}>0.8,E{r}<1.25),"Pass","Caution")', "between 0.8 and 1.25")]
    for i, (lab, fml, nf, ver, crit) in enumerate(checks):
        e = c0 + 1 + i
        ws.merge_range(f"A{e}:D{e}", lab, f_labw); put(f"E{e}", fml, F(num_format=nf)); put(f"F{e}", "=" + ver.format(r=e), f_bold); ws.merge_range(f"G{e}:L{e}", crit, f_note)
    ce = c0 + 1 + len(checks)
    ws.conditional_format(f"F{c0 + 1}:F{ce - 1}", {"type": "cell", "criteria": "==", "value": '"Pass"', "format": f_pass})
    ws.conditional_format(f"F{c0 + 1}:F{ce - 1}", {"type": "cell", "criteria": "==", "value": '"Caution"', "format": f_warn})
    ws.conditional_format(f"F{c0 + 1}:F{ce - 1}", {"type": "cell", "criteria": "==", "value": '"Fail"', "format": f_fail})
    CHK0 = c0 + 1
    # fluorescein
    fq = ce + 2
    ws.write(f"A{fq - 1}", "Instrument check with fluorescein (1 nM in NaOH should read ~20 mP at the right G)", f_bold)
    ws.write_row(fq - 1, 0, ["Well", "", "mP at the G used", "Net parallel", "Net perpendicular", "G that gives 20 mP"], f_h); ws.set_row(fq - 1, 30)
    for i, w in enumerate(FL):
        e = fq + 1 + i
        ws.write(f"A{e}", wname(w), f_bold)
        put(f"D{e}", f"={cell_par(w)}-{flb(cell_par)}", n0); put(f"E{e}", f"={cell_perp(w)}-{flb(cell_perp)}", n0)
        put(f"C{e}", f"=1000*(G_FACTOR*D{e}-E{e})/(G_FACTOR*D{e}+E{e})", n1); put(f"F{e}", f"=1.0408*E{e}/D{e}", n3)
    e = fq + 1 + len(FL)
    ws.merge_range(f"A{e}:E{e}", "Mean G that would give 20 mP (net = raw minus the fluorescein-buffer wells F4-F6; 1.0408 = 1.02/0.98)", f_labw); put(f"F{e}", f"=AVERAGE(F{fq + 1}:F{e - 1})", n3)
    FLG = e
    # what it shows
    wn = e + 2
    ws.merge_range(f"A{wn}:S{wn + 1}", "WHAT THIS SHOWS / DOES NOT SHOW: a smooth, one-to-one-type binding curve (Hill n near 1) with a ~200 mP window and an apparent K_d near 2 ug/mL. It does NOT yet show that the binding is specific "
                   "(no scrambled-aptamer, 50x unlabeled-competitor or off-target-VLP wells on this plate), that equilibrium was reached (no second read time), or that a second plate agrees. "
                   "Bound aptamer is dimmer than free (Q well below 1), so the plain K_d may be slightly high; with the lid on, the signal is only ~1.6x the blank, so single wells scatter by 5-25 mP.", f_note)
    ws.set_row(wn - 1, 30); ws.set_row(wn, 30)

    # ---------------- CHART ----------------
    r = wn + 3
    band(r, "CHART - polarization against VLP concentration (grey = single wells, blue = mean +/- SD, red dashed = fitted curve)")
    chart_row = r + 2
    # ---------------- WORKED EXAMPLE ----------------
    we = chart_row + 22
    band(we, "WORKED EXAMPLE - follow any one well through every step (type a well name in the yellow cell)")
    kv(we + 1, "Choose a well (any titration well such as A1 or C10, or F10-F12)", "A1", f_in)
    WELL = f"$E${we + 1}"
    kv(we + 2, "Row of that well in the Step 2 table", f"=MATCH({WELL},$A${w0}:$A${w1},0)", n0)
    ix = lambda c: f"INDEX(${c}${w0}:${c}${w1},$E${we + 2})"
    wsteps = [("Group ; VLP ug/mL", f'={ix("B")}&" ; "&TEXT({ix("C")},"0.0")', None), ("1. Raw parallel counts", f"={ix('E')}", n0), ("2. Raw perpendicular counts", f"={ix('F')}", n0),
              ("3. Blank parallel (pooled median)", f"={ix('G')}", n0), ("4. Blank perpendicular (pooled median)", f"={ix('H')}", n0),
              ("5. Net parallel = 1 - 3", f"={ix('I')}", n0), ("6. Net perpendicular = 2 - 4", f"={ix('J')}", n0), ("7. G x net parallel", f"={ix('K')}", n0),
              ("8. Numerator = 7 - 6", f"={ix('K')}-{ix('J')}", n0), ("9. Denominator = 7 + 6", f"={ix('K')}+{ix('J')}", n0),
              ("10. mP = 1000 x 8 / 9", f"={ix('L')}", n1), ("11. Anisotropy r", f"={ix('M')}", n4),
              ("12. The instrument's own mP for this well (no blank removed)", f"=INDEX($B${MR0}:$M${MR0 + 7},CODE(UPPER(LEFT({WELL},1)))-64,VALUE(MID({WELL},2,2)))", n0),
              ("13. How much the background inflated the instrument's mP = 12 - 10", None, n1)]
    for i, (lab, fml, fm) in enumerate(wsteps):
        e = we + 3 + i
        if fml is None: fml = f"=E{e - 1}-E{e - 3}"
        ws.merge_range(f"A{e}:D{e}", lab, f_labw); put(f"E{e}", fml, fm or f_lab)
    wend = we + 3 + len(wsteps)

    # ---------------- NOTES ----------------
    nt = wend + 1
    band(nt, "ASSUMPTIONS AND CAUTIONS")
    notes = ["Blank: the median of all 24 VLP-only wells is used for every well, including aptamer-alone wells (Step 1 shows no trend with VLP; the median ignores a contaminated well).",
             "G: the calibrated G from the file header; the export's 'Intensity (parallel)' table is already multiplied by G, but here G is applied once to the RAW counts.",
             "Replicates: B10-B12 (2.3 ug/mL) are used with their planned concentration; the plate description lists 2.1. G4-G6 are unspecified and unused. F7-F9 and G1-G3 are used only for the blank comparison.",
             "The K_d is APPARENT (avidity: one VLP has many binding sites; VLP concentration is by protein mass, VP1 ~58 kDa). Hill and bootstrap results are static values from Python.",
             "Missing controls: scrambled aptamer, 50x unlabeled competitor, off-target VLP, a second read time (30 vs 60 min) and a second plate."]
    for i, t in enumerate(notes): ws.merge_range(f"A{nt + 1 + i}:S{nt + 1 + i}", f"{i + 1}. {t}", f_labw)
    nend = nt + 1 + len(notes)

    # ---------------- SCAN TABLE ----------------
    sc = nend + 2
    band(sc, "STEP 4b - THE LEAST-SQUARES SCAN (241 trial K_d values; supports Step 4B)")
    box(sc + 1, "For each trial K_d (column B): f = c/(K_d + c) for every well; Sf, Sff, Sfy are weighted sums over the wells; amplitude and baseline follow from straight-line algebra; SSE is the leftover squared error. "
                "The smallest SSE (column H) is the best K_d. Column I keeps the K_d values whose SSE is below the 95 % threshold; the smallest and largest of those are the interval. Columns L-O hold the chart data.", f_how, 46)
    ws.write(f"J{sc + 3}", "Smallest SSE", f_lab); put(f"K{sc + 3}", f"=MIN(H{sc + 6}:H{sc + 246})", n1)
    ws.write(f"J{sc + 4}", "SSE threshold (95%)", f_lab); put(f"K{sc + 4}", f"=K{sc + 3}*(1+FINV(0.05,1,FIT_N-3)/(FIT_N-3))", n1)
    THR = f"$K${sc + 4}"
    ws.write_row(sc + 4, 0, ["log10 K_d", "K_d (ug/mL)", "Sf = sum w f", "Sff = sum w f^2", "Sfy = sum w f mP", "Amplitude", "Baseline", "SSE", "K_d inside 95% interval"], f_h); ws.set_row(sc + 4, 42)
    s0 = sc + 6; NS = 241; s1 = s0 + NS - 1
    cR, yR, wR = col("C"), col("L"), col("S")
    for i in range(NS):
        e = s0 + i
        put(f"A{e}", "=LOGK_START" if i == 0 else f"=A{e - 1}+LOGK_STEP", n3); put(f"B{e}", f"=10^A{e}", n4)
        put(f"C{e}", f"=SUMPRODUCT({wR},{cR}/(B{e}+{cR}))", n4); put(f"D{e}", f"=SUMPRODUCT({wR},{cR}/(B{e}+{cR}),{cR}/(B{e}+{cR}))", n4)
        put(f"E{e}", f"=SUMPRODUCT({wR},{cR}/(B{e}+{cR}),{yR})", n2)
        put(f"F{e}", f"=(E{e}-C{e}*FIT_SY/FIT_N)/(D{e}-C{e}^2/FIT_N)", n2); put(f"G{e}", f"=(FIT_SY-F{e}*C{e})/FIT_N", n2)
        put(f"H{e}", f"=(FIT_SYY-FIT_SY^2/FIT_N)-F{e}*(E{e}-C{e}*FIT_SY/FIT_N)", n1)
        put(f"I{e}", f'=IF(H{e}<={THR},B{e},"")', n4)
    # fit result formulas
    SCB, SCH, SCG, SCF, SCI = (f"$B${s0}:$B${s1}", f"$H${s0}:$H${s1}", f"$G${s0}:$G${s1}", f"$F${s0}:$F${s1}", f"$I${s0}:$I${s1}")
    put(R["SSE"], f"=MIN({SCH})", n0); put(R["K"], f"=INDEX({SCB},MATCH({R['SSE']},{SCH},0))", key2)
    put(R["BASE"], f"=INDEX({SCG},MATCH({R['SSE']},{SCH},0))", n1); put(R["AMP"], f"=INDEX({SCF},MATCH({R['SSE']},{SCH},0))", n1)
    put(R["PLAT"], f"={R['BASE']}+{R['AMP']}", n1); put(R["DF"], "=FIT_N-3", n0); put(R["SD"], f"=SQRT({R['SSE']}/{R['DF']})", n1)
    put(R["THR"], f"={THR}", n0); put(R["LO"], f"=MIN({SCI})", n2); put(R["HI"], f"=MAX({SCI})", n2)
    put(R["CHK"], f'=IF(AND({R["LO"]}>MIN({SCB})*1.05,{R["HI"]}<MAX({SCB})/1.05),"OK: interval inside the scan","Widen the scan")', f_bold)
    # chart data (L:O) next to the scan
    ws.write_row(sc + 4, 11, ["Curve grid VLP", "Fitted mP", "K_d line x", "K_d line y"], f_h)
    xs = np.geomspace(0.14, 40, 61)
    for i, x in enumerate(xs):
        e = s0 + i; ws.write_number(f"L{e}", float(x), n3); put(f"M{e}", f"=A_BASE+B_AMP*L{e}/(K_BEST+L{e})", n1)
    put(f"N{s0}", "=K_BEST", n2); ws.write_number(f"O{s0}", 0, n0); put(f"N{s0 + 1}", "=K_BEST", n2); ws.write_number(f"O{s0 + 1}", 320, n0)
    ws.write_row(sc + 4, 16, ["Baseline x", "Baseline y"], f_h)
    ws.write_number(f"Q{s0}", 0.14, n2); put(f"R{s0}", f"=E{g0r}", n1); ws.write_number(f"Q{s0 + 1}", 40, n2); put(f"R{s0 + 1}", f"=E{g0r}", n1)

    def make_chart(log):
        ch = wb.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
        ch.add_series({"name": "single wells", "categories": f"={SH}!$C${w0 + 3}:$C${w1}", "values": f"={SH}!$L${w0 + 3}:$L${w1}", "line": {"none": True},
                       "marker": {"type": "circle", "size": 5, "fill": {"color": "#BFBFBF"}, "border": {"color": "#7F7F7F"}}})
        ch.add_series({"name": "mean +/- SD", "categories": f"={SH}!$B${g0r + 1}:$B${g1r}", "values": f"={SH}!$E${g0r + 1}:$E${g1r}", "line": {"color": DARK, "width": 2.0},
                       "marker": {"type": "circle", "size": 7, "fill": {"color": DARK}, "border": {"color": DARK}},
                       "y_error_bars": {"type": "custom", "plus_values": f"={SH}!$F${g0r + 1}:$F${g1r}", "minus_values": f"={SH}!$F${g0r + 1}:$F${g1r}", "line": {"color": DARK}}})
        ch.add_series({"name": "fitted curve", "categories": f"={SH}!$L${s0}:$L${s0 + 60}", "values": f"={SH}!$M${s0}:$M${s0 + 60}", "line": {"color": "#C00000", "width": 2.0, "dash_type": "dash"}, "marker": {"type": "none"}})
        ch.add_series({"name": "K_d", "categories": f"={SH}!$N${s0}:$N${s0 + 1}", "values": f"={SH}!$O${s0}:$O${s0 + 1}", "line": {"color": "#C00000", "width": 1.0, "dash_type": "round_dot"}, "marker": {"type": "none"}})
        ch.add_series({"name": "aptamer alone", "categories": f"={SH}!$Q${s0}:$Q${s0 + 1}", "values": f"={SH}!$R${s0}:$R${s0 + 1}", "line": {"color": "#595959", "width": 1.0, "dash_type": "square_dot"}, "marker": {"type": "none"}})
        xa = {"name": "VLP concentration (ug/mL)", "min": 0.14 if log else 0, "max": 40 if log else 30, "major_gridlines": {"visible": True, "line": {"color": "#E7E6E6"}}}
        if log: xa["log_base"] = 10
        ch.set_x_axis(xa); ch.set_y_axis({"name": "Polarization (mP)", "min": 0, "max": 320, "major_gridlines": {"visible": True, "line": {"color": "#E7E6E6"}}})
        ch.set_title({"name": f"{a.label} + VLP ({'log' if log else 'linear'} x axis)", "name_font": {"size": 11}}); ch.set_legend({"position": "bottom"}); ch.set_size({"width": 640, "height": 400})
        return ch
    ws.insert_chart(f"A{chart_row}", make_chart(True), {"x_offset": 5, "y_offset": 5}); ws.insert_chart(f"H{chart_row}", make_chart(False), {"x_offset": 40, "y_offset": 5})

    # ---------------- HEADLINE (top) ----------------
    kv(HEAD + 1, "K_d (ug/mL VLP protein)", f"={KD_UG}", key2, None)
    ws.merge_range(f"F{HEAD + 1}:S{HEAD + 1}", "", f_note); put(f"F{HEAD + 1}", f'="95% interval "&TEXT({R["LO"]},"0.00")&" to "&TEXT({R["HI"]},"0.00")&" ug/mL (least squares on all "&TEXT(FIT_N,"0")&" wells; hand estimate "&TEXT({HAND},"0.00")&")"', f_note)
    kv(HEAD + 2, "K_d (nM VP1)", f"={KD_NM}", key1, None)
    ws.merge_range(f"F{HEAD + 2}:S{HEAD + 2}", "", f_note); put(f"F{HEAD + 2}", f'="interval "&TEXT(F{k0 + 1},"0")&" to "&TEXT(G{k0 + 1},"0")&" nM VP1;  "&TEXT(E{k0 + 3},"0.00")&" nM whole particles;  free baseline "&TEXT(E{g0r},"0")&" mP, plateau "&TEXT({R["PLAT"]},"0")&" mP"', f_note)
    ws.merge_range(f"A{HEAD + 3}:D{HEAD + 3}", "Checks passed / caution / failed", f_labw)
    put(f"E{HEAD + 3}", f'=COUNTIF(F{CHK0}:F{CHK0 + len(checks) - 1},"Pass")&" / "&COUNTIF(F{CHK0}:F{CHK0 + len(checks) - 1},"Caution")&" / "&COUNTIF(F{CHK0}:F{CHK0 + len(checks) - 1},"Fail")', f_bold)
    ws.merge_range(f"F{HEAD + 3}:S{HEAD + 3}", "see Step 5; the weak points are low signal over blank (lid on) and a dimmer bound aptamer; no specificity controls yet", f_note)
    ws.freeze_panes(2, 0)
    wb.close()
    print("written", a.out)
    print(f"python reference: 1:1 K_d {p1[2]:.4f} ug/mL; Hill K {p2[2]:.3f} n {p2[3]:.2f}; bootstrap {bq[0]:.2f}-{bq[2]:.2f}")


if __name__ == "__main__":
    main()
