#!/usr/bin/env python3
"""Compare set-up plates (blank diagnosis / aptamer concentration / lid / volume).

Each plate is given as LABEL:FIRSTROW:PATH, where FIRSTROW is the row of the first group
(A for the 100 uL plate, D for the 50 uL plate).  Well map of the 12 Nov 2026 set-up plates
(rows relative to FIRSTROW, 3 wells each):
  row+0: water | buffer B | buffer C | empty  (cols 1-3, 4-6, 7-9, 10-12)
  row+1: fluorescein 1 nM | fluorescein diluent | aptamer 2 nM | aptamer 5 nM
  row+2: aptamer 10 nM (cols 1-3)

  python3 -I compare_setup_plates.py "100 uL, lid:A:file1.xlsx" "50 uL, no lid:D:file3.xlsx"

All four blank groups are pooled when they agree; per-channel subtraction, G from the file header.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fp_analysis as fp

KEYS = ["lid lifter", "plate area", "gain manual", "gain optimal", "z-position [μm]", "z-position mode",
        "g factor manual", "g factor calibrated", "temperature [°c]", "start time",
        "excitation wavelength [nm]", "excitation bandwidth [nm]", "emission wavelength [nm]", "emission bandwidth [nm]"]


def wellmap(first):
    i = "ABCDEFGH".index(first)
    R = lambda k: "ABCDEFGH"[i + k]
    return {
        "water": f"{R(0)}1-{R(0)}3", "buffer B": f"{R(0)}4-{R(0)}6", "buffer C": f"{R(0)}7-{R(0)}9",
        "empty": f"{R(0)}10-{R(0)}12", "fluorescein 1nM": f"{R(1)}1-{R(1)}3", "fl. diluent": f"{R(1)}4-{R(1)}6",
        "apt 2 nM": f"{R(1)}7-{R(1)}9", "apt 5 nM": f"{R(1)}10-{R(1)}12", "apt 10 nM": f"{R(2)}1-{R(2)}3",
    }


def main(args):
    for a in args:
        label, first, path = a.split(":", 2)
        hdr, tabs = fp.parse_export(path)
        g = fp.header_g(hdr)
        print("=====", label, "|", {k: hdr[k] for k in KEYS if k in hdr})
        par, perp = tabs["raw_par"], tabs["raw_perp"]
        st = {}
        print(f"{'group':<18}{'∥ raw':>8}{'⊥ raw':>8}{'total':>8}{'CV%':>6}{'mP raw':>9}{'SD':>6}")
        for name, spec in wellmap(first).items():
            w = fp.expand_wells(spec)
            p = np.array([par[x] for x in w]); s = np.array([perp[x] for x in w])
            tot = g * p + 2 * s; mp = fp.mp_r(p, s, g)[0]
            st[name] = (p, s, tot)
            print(f"{name:<18}{p.mean():>8.1f}{s.mean():>8.1f}{tot.mean():>8.1f}"
                  f"{tot.std(ddof=1) / tot.mean() * 100:>6.1f}{mp.mean():>9.1f}{mp.std(ddof=1):>6.1f}")
        bl = [st[k] for k in ("water", "buffer B", "buffer C", "empty")]
        bp = np.mean([b[0].mean() for b in bl]); bs = np.mean([b[1].mean() for b in bl]); bt = g * bp + 2 * bs
        rng = (min(b[2].mean() for b in bl), max(b[2].mean() for b in bl))
        print(f"pooled blank total {bt:.0f} (groups {rng[0]:.0f}-{rng[1]:.0f}), mP {fp.mp_r(np.array([bp]), np.array([bs]), g)[0][0]:.0f}")
        print(f"{'net (pooled blank off)':<24}{'net total':>10}{'net/blank':>10}{'mP':>8}{'SD':>6}")
        for name in ("fluorescein 1nM", "apt 2 nM", "apt 5 nM", "apt 10 nM"):
            mp, r, tot = fp.mp_r(st[name][0] - bp, st[name][1] - bs, g)
            print(f"{name:<24}{tot.mean():>10.0f}{tot.mean() / bt:>10.2f}{mp.mean():>8.1f}{mp.std(ddof=1):>6.1f}")
        print()


if __name__ == "__main__":
    main(sys.argv[1:]) if len(sys.argv) > 1 else sys.exit(__doc__)
