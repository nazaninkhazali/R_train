#!/usr/bin/env python3
"""Write a synthetic Spark-style export for testing (known K_d, known G, scatter blank).

Well map matches example_layout.json: 8-point 4-fold VLP series in rows A-H (cols 1-3),
aptamer alone A5-A7, buffer blank G7-G9, fluorescein H5-H7, its diluent H9-H11, and one
contaminated well (D2).
"""
import sys
import numpy as np
from openpyxl import Workbook

ROWS = "ABCDEFGH"


def mp_from(par_net, perp_net, g):
    return 1000 * (g * par_net - perp_net) / (g * par_net + perp_net)


def build(path, g=1.056, kd=3.0, mp_free=60.0, mp_bound=190.0, gain=149, seed=1):
    rng = np.random.default_rng(seed)
    par = np.zeros((8, 12)); perp = np.zeros((8, 12))

    def put(well_list, total_net, mp):
        """total_net = G*par + 2*perp (net); mp -> channels."""
        # anisotropy r = 2P/(3-P); par*g = tot*(1+2r)/3, perp = tot*(1-r)/3
        for (rw, cl) in well_list:
            t = total_net * (1 + rng.normal(0, 0.02))
            P = (mp + rng.normal(0, 3.0)) / 1000.0
            r = 2 * P / (3 - P)
            par[rw, cl] = t * (1 + 2 * r) / 3 / g
            perp[rw, cl] = t * (1 - r) / 3

    def wells(spec):
        out = []
        for chunk in spec.split(","):
            a, b = (chunk.split("-") + [chunk])[:2] if "-" in chunk else (chunk, chunk)
            r1, c1, r2, c2 = a[0], int(a[1:]), b[0], int(b[1:])
            out += [(r, c - 1) for r in range(ROWS.index(r1), ROWS.index(r2) + 1) for c in range(c1, c2 + 1)]
        return out

    # buffer blank: strongly polarised scatter, ~4.5k counts total
    bl = wells("G7-G9")
    for w in bl:
        t = 4500
        par[w] = t * (1 + 2 * 0.28) / 3 / g * (1 + rng.normal(0, .02)); perp[w] = t * (1 - 0.28) / 3 * (1 + rng.normal(0, .02))
    # everything starts at blank level (incl. empty wells)
    for rw in range(8):
        for cl in range(12):
            if par[rw, cl] == 0:
                par[rw, cl] = par[bl[0]]; perp[rw, cl] = perp[bl[0]]
    b_par = np.mean([par[w] for w in bl]); b_perp = np.mean([perp[w] for w in bl])

    def put_on_blank(ws, total_net, mp):
        put(ws, total_net, mp)
        for w in ws:
            par[w] += b_par; perp[w] += b_perp

    concs = [0.0055 * 4 ** i for i in range(8)]  # 0.0055 ... 90 ug/mL
    for i, c in enumerate(concs):
        w = wells(f"{ROWS[i]}1-{ROWS[i]}3")
        f = c / (kd + c)
        put_on_blank(w, 22000, mp_free + (mp_bound - mp_free) * f)
    put_on_blank(wells("A5-A7"), 22000, mp_free)  # aptamer alone
    # fluorescein reference H5-H7, diluent H9-H11
    put_on_blank(wells("H5-H7"), 28000, 20.0)
    put_on_blank(wells("H9-H11"), 0.0001, 20.0)
    # contaminated outlier well in a titration group
    par[3, 1] *= 4; perp[3, 1] *= 4

    wb = Workbook(); ws = wb.active; ws.title = "Result sheet"
    ws.append(["Tecan SparkControl V3.2 (synthetic test file)"])
    ws.append(["Gain", gain]); ws.append(["Z-Position", 17982]); ws.append(["G Factor", g])
    ws.append(["Mode", "Fluorescence polarisation"]); ws.append([])
    def table(title, arr):
        ws.append([title]); ws.append([""] + list(range(1, 13)))
        for i, r in enumerate(arr):
            ws.append([ROWS[i]] + [float(round(v, 2)) for v in r])
        ws.append([])
    tot = g * par + 2 * perp
    table("Label 1 [mP]", mp_from(par, perp, g)); table("Total Intensity", tot)
    table("Intensity (parallel)", par * g); table("Intensity (perpendicular)", perp)
    table("Rawdata (perpendicular)", perp); table("Rawdata (parallel)", par)
    wb.save(path)


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "synthetic_plate.xlsx")
