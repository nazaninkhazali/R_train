#!/usr/bin/env python3
"""Charts-only workbook: the Buf-2 binding curves of two plates, each dot labelled with its VLP concentration.

  python3 -I make_chart_workbook.py PLATE_A.xlsx "label A" PLATE_B.xlsx "label B" OUT.xlsx

PLATE_x.xlsx = a one-sheet workbook made by make_onesheet_workbook.py (recalculated). The numbers are copied from its
Step 2 / Step 3 tables and fit cells; the fitted curve here is a live formula of the copied fit parameters.
Run the xlsx skill's recalc.py twice afterwards so cached values are stored.
"""
import sys
import numpy as np, xlsxwriter
from openpyxl import load_workbook


def read_plate(path):
    ws = load_workbook(path, data_only=True)["FP_Kd"]
    A = {r: ws.cell(r, 1).value for r in range(1, ws.max_row + 1)}
    def find(prefix, col=1):
        for r in range(1, ws.max_row + 1):
            v = ws.cell(r, col).value
            if isinstance(v, str) and v.startswith(prefix): return r
        raise KeyError(prefix)
    g0 = find("aptamer alone") if False else None
    # Step 3 header row: "Group"; rows after it until blank
    hdr3 = next(r for r in range(1, ws.max_row + 1) if ws.cell(r, 1).value == "Group" and ws.cell(r, 5).value == "Mean mP")
    groups = []
    r = hdr3 + 1
    while ws.cell(r, 1).value:
        groups.append(dict(name=ws.cell(r, 1).value, conc=ws.cell(r, 2).value, nM=ws.cell(r, 3).value, n=ws.cell(r, 4).value,
                           mean=ws.cell(r, 5).value, sd=ws.cell(r, 6).value, fit=ws.cell(r, 11).value)); r += 1
    hdr2 = next(r for r in range(1, ws.max_row + 1) if ws.cell(r, 1).value == "Well" and ws.cell(r, 12).value == "mP")
    wells = []
    r = hdr2 + 1
    while ws.cell(r, 1).value:
        wells.append(dict(well=ws.cell(r, 1).value, conc=ws.cell(r, 3).value, mp=ws.cell(r, 12).value, w=ws.cell(r, 19).value)); r += 1
    val = lambda prefix: ws.cell(find(prefix), 5).value
    fit = dict(K=val("Best K_d (ug/mL)"), base=val("Baseline (mP) at the best K_d"), amp=val("Amplitude"),
               lo=val("95% interval, lower"), hi=val("95% interval, upper"))
    return groups, wells, fit


def main():
    pa, la, pb, lb, out = sys.argv[1:6]
    plates = [(la,) + read_plate(pa), (lb,) + read_plate(pb)]
    wb = xlsxwriter.Workbook(out, {"default_format_properties": {"font_name": "Arial", "font_size": 10}})
    F = lambda **k: wb.add_format({"font_name": "Arial", "font_size": 10, **k})
    f_title = F(bold=True, font_size=14, font_color="#1F4E79"); f_h = F(bold=True, font_color="white", bg_color="#2E75B6", border=1, text_wrap=True, align="center", valign="vcenter")
    f_in = F(font_color="#0000FF", num_format="0.00"); f_in1 = F(font_color="#0000FF", num_format="0.0"); f_t = F(font_color="#0000FF")
    f_n1 = F(num_format="0.0"); f_note = F(italic=True, font_color="#555555", text_wrap=True, valign="top"); f_b = F(bold=True)
    ch_ws = wb.add_worksheet("Charts"); d_ws = wb.add_worksheet("Data")
    ch_ws.hide_gridlines(2); ch_ws.set_landscape(); ch_ws.fit_to_pages(1, 0); ch_ws.set_column("A:A", 3)
    d_ws.set_column("A:A", 16); d_ws.set_column("B:Z", 13)
    d_ws.write("A1", "Data behind the charts (copied from the one-sheet K_d workbooks; blue = copied numbers, black = formulas)", f_title)
    cols = {}   # per plate: dict of column ranges
    xs = np.geomspace(0.1, 100, 61)
    colour = ["#1F4E79", "#C55A11"]
    c0 = 0
    for k, (label, groups, wells, fit) in enumerate(plates):
        col = c0
        cn = lambda c: xlsxwriter.utility.xl_col_to_name(c)
        d_ws.write(2, col, f"{label}", f_b)
        # fit parameters
        d_ws.write(3, col, "K_d (ug/mL)", f_t); d_ws.write_number(3, col + 1, fit["K"], f_in)
        d_ws.write(4, col, "Baseline (mP)", f_t); d_ws.write_number(4, col + 1, fit["base"], f_in1)
        d_ws.write(5, col, "Amplitude (mP)", f_t); d_ws.write_number(5, col + 1, fit["amp"], f_in1)
        d_ws.write(6, col, "K_d 95% low / high", f_t); d_ws.write_number(6, col + 1, fit["lo"], f_in); d_ws.write_number(6, col + 2, fit["hi"], f_in)
        Kc, Bc, Ac = f"${cn(col + 1)}$4", f"${cn(col + 1)}$5", f"${cn(col + 1)}$6"
        # means
        d_ws.write_row(8, col, ["VLP ug/mL", "VLP nM VP1", "n", "Mean mP", "SD (mP)"], f_h)
        gr = [g for g in groups if g["conc"] > 0]
        for i, g in enumerate(gr):
            r = 9 + i
            d_ws.write_number(r, col, g["conc"], f_in); d_ws.write_formula(r, col + 1, f"={cn(col)}{r + 1}*17.14", f_n1)
            d_ws.write_number(r, col + 2, g["n"], f_in1); d_ws.write_number(r, col + 3, g["mean"], f_in1); d_ws.write_number(r, col + 4, g["sd"], f_in1)
        m0, m1 = 10, 9 + len(gr)
        # aptamer alone baseline line
        apt = next(g for g in groups if g["conc"] == 0)
        # single wells (used wells only)
        sw = [w for w in wells if w["w"] == 1 and w["conc"] > 0]
        s0 = m1 + 3
        d_ws.write_row(s0 - 1, col, ["Well", "VLP ug/mL", "mP (used wells)"], f_h)
        for i, w in enumerate(sw):
            d_ws.write(s0 + i, col, w["well"], f_t); d_ws.write_number(s0 + i, col + 1, w["conc"], f_in); d_ws.write_number(s0 + i, col + 2, w["mp"], f_in1)
        s1 = s0 + len(sw)
        # curve grid (formula)
        g0 = s1 + 3
        d_ws.write_row(g0 - 1, col, ["Curve grid ug/mL", "Fitted mP"], f_h)
        for i, x in enumerate(xs):
            d_ws.write_number(g0 + i, col, float(x), F(num_format="0.000")); d_ws.write_formula(g0 + i, col + 1, f"={Bc}+{Ac}*{cn(col)}{g0 + i + 1}/({Kc}+{cn(col)}{g0 + i + 1})", f_n1)
        g1 = g0 + len(xs)
        # reference lines
        l0 = g1 + 2
        d_ws.write_row(l0 - 1, col, ["K_d line x", "K_d line y", "Baseline x", "Baseline y"], f_h)
        d_ws.write_formula(l0, col, f"={Kc}", f_in); d_ws.write_number(l0, col + 1, 0, f_in1); d_ws.write_formula(l0 + 1, col, f"={Kc}", f_in); d_ws.write_number(l0 + 1, col + 1, 320, f_in1)
        d_ws.write_number(l0, col + 2, 0.1, f_in); d_ws.write_number(l0 + 1, col + 2, 100, f_in)
        d_ws.write_number(l0, col + 3, apt["mean"], f_in1); d_ws.write_number(l0 + 1, col + 3, apt["mean"], f_in1)
        cols[k] = dict(col=col, m=(m0, m1), s=(s0 + 1, s1), g=(g0 + 1, g1), l=(l0 + 1, l0 + 2), n=len(gr))
        c0 += 8
    D = "Data"
    rng = lambda c, a, b: f"={D}!${xlsxwriter.utility.xl_col_to_name(c)}${a}:${xlsxwriter.utility.xl_col_to_name(c)}${b}"

    def labels(k, pos, size, colr, bold=False):
        # Excel's "X Value" data label (showCatName on a scatter series): prints each dot's VLP concentration
        return {"category": True, "value": False, "position": pos, "num_format": "General", "font": {"size": size, "bold": bold, "color": colr}}

    def xaxis(ch):
        ch.set_x_axis({"name": "VLP concentration (ug/mL VLP protein); each dot is labelled with its concentration", "min": 0.1, "max": 100, "log_base": 10, "num_format": "0.#",
                       "name_font": {"size": 11, "bold": True}, "major_gridlines": {"visible": True, "line": {"color": "#D9D9D9"}}, "minor_gridlines": {"visible": True, "line": {"color": "#F2F2F2"}}})
        ch.set_y_axis({"name": "Polarization (mP)", "min": 0, "max": 320, "major_gridlines": {"visible": True, "line": {"color": "#E7E6E6"}}})
        ch.set_legend({"position": "bottom"}); ch.set_size({"width": 900, "height": 480})

    def single(k):
        label, groups, wells, fit = plates[k]; c = cols[k]; col = c["col"]
        ch = wb.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
        ch.add_series({"name": "single wells", "categories": rng(col + 1, *c["s"]), "values": rng(col + 2, *c["s"]), "line": {"none": True},
                       "marker": {"type": "circle", "size": 5, "fill": {"color": "#BFBFBF"}, "border": {"color": "#7F7F7F"}}})
        ch.add_series({"name": "mean +/- SD", "categories": rng(col, *c["m"]), "values": rng(col + 3, *c["m"]), "line": {"color": "#1F4E79", "width": 2.25},
                       "marker": {"type": "circle", "size": 8, "fill": {"color": "#1F4E79"}, "border": {"color": "#1F4E79"}},
                       "data_labels": labels(k, "above", 9, "#1F4E79", True),
                       "y_error_bars": {"type": "custom", "plus_values": rng(col + 4, *c["m"]), "minus_values": rng(col + 4, *c["m"]), "line": {"color": "#1F4E79"}}})
        ch.add_series({"name": "1:1 fit", "categories": rng(col, *c["g"]), "values": rng(col + 1, *c["g"]), "line": {"color": "#C00000", "width": 2.0, "dash_type": "dash"}, "marker": {"type": "none"}})
        ch.add_series({"name": "K_d", "categories": rng(col, *c["l"]), "values": rng(col + 1, *c["l"]), "line": {"color": "#C00000", "width": 1.0, "dash_type": "round_dot"}, "marker": {"type": "none"}})
        ch.add_series({"name": "aptamer alone", "categories": rng(col + 2, *c["l"]), "values": rng(col + 3, *c["l"]), "line": {"color": "#595959", "width": 1.0, "dash_type": "square_dot"}, "marker": {"type": "none"}})
        ch.set_title({"name": f"{label}: Buf-2 aptamer (5 nM) with norovirus VLP", "name_font": {"size": 12}}); xaxis(ch); return ch

    def overlay():
        ch = wb.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
        for k, pos in ((0, "above"), (1, "below")):
            label = plates[k][0]; c = cols[k]; col = c["col"]
            ch.add_series({"name": f"{label} mean +/- SD", "categories": rng(col, *c["m"]), "values": rng(col + 3, *c["m"]), "line": {"color": colour[k], "width": 2.25},
                           "marker": {"type": "circle", "size": 7, "fill": {"color": colour[k]}, "border": {"color": colour[k]}},
                           "data_labels": labels(k, pos, 8, colour[k]),
                           "y_error_bars": {"type": "custom", "plus_values": rng(col + 4, *c["m"]), "minus_values": rng(col + 4, *c["m"]), "line": {"color": colour[k]}}})
            ch.add_series({"name": f"{label} fit", "categories": rng(col, *c["g"]), "values": rng(col + 1, *c["g"]), "line": {"color": colour[k], "width": 1.5, "dash_type": "dash"}, "marker": {"type": "none"}})
        ch.set_title({"name": "Buf-2 aptamer (5 nM) with norovirus VLP: both plates", "name_font": {"size": 12}}); xaxis(ch); return ch

    ch_ws.write("B1", "Buf-2 binding curves with the VLP concentration shown at every dot", f_title)
    ch_ws.write("B2", "Grey = single wells, solid line = mean +/- SD with the VLP concentration (ug/mL) printed above each dot, red dashed = 1:1 fit, dotted red = K_d, grey dotted = aptamer alone.", f_note)
    ch_ws.insert_chart("B4", single(0)); ch_ws.insert_chart("B30", single(1)); ch_ws.insert_chart("B56", overlay())
    k0, k1 = plates[0][3], plates[1][3]
    ch_ws.write("B82", f"K_d: {plates[0][0]} = {k0['K']:.2f} ug/mL ({k0['K'] * 17.14:.0f} nM VP1);  {plates[1][0]} = {k1['K']:.2f} ug/mL ({k1['K'] * 17.14:.0f} nM VP1)  (1 ug/mL = 17.14 nM VP1)", f_b)
    wb.close(); print("written", out)


if __name__ == "__main__":
    main()
