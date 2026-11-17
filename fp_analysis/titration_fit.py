#!/usr/bin/env python3
"""Titration analysis for a Spark FP plate: per-channel blank subtraction, per-well mP, 1:1 and Hill fits.

  python3 -I titration_fit.py RESULT.xlsx layout.json [--g 1.05] [--blank pooled|matched] [--exclude B7,...] [--out DIR]

layout.json:
  {"titration":[{"conc":28,"wells":"A1-A3","blank_wells":"D1-D2"}, ...],   # conc in ug/mL
   "free":"F10-F12",                       # aptamer alone (plotted/fitted at conc 0)
   "reference":{"fluorescein":"F1-F3","fl_buffer":"F4-F6"}}
Blank: 'pooled' = median raw parallel and perpendicular of ALL blank wells (robust to a few contaminated wells,
use it when VLP-only wells show no concentration trend); 'matched' = mean of the VLP-only wells at the same concentration.
Wells whose total intensity is >25% from their group median (n>=3) are flagged and left out; add --exclude to drop others.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fp_analysis as fp

UG_TO_NM_VP1 = 17.14           # 1 ug/mL ~ 17.14 nM VP1 (58 kDa)
hyp = lambda c, a, b, k: a + (b - a) * c / (k + c)
hill = lambda c, a, b, k, n: a + (b - a) * c ** n / (k ** n + c ** n)

def fit(c, y, model, p0, lo, hi):
    popt, pcov = curve_fit(model, c, y, p0=p0, bounds=(lo, hi), maxfev=20000)
    dof = len(y) - len(popt); se = np.sqrt(np.diag(pcov)); res = y - model(c, *popt)
    return popt, se, stats.t.ppf(0.975, dof), float(np.sqrt(np.sum(res ** 2) / dof))

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx"); ap.add_argument("layout")
    ap.add_argument("--g", type=float); ap.add_argument("--blank", choices=["pooled", "matched"], default="pooled")
    ap.add_argument("--exclude", default=""); ap.add_argument("--out", default="."); ap.add_argument("--no-flag", action="store_true")
    a = ap.parse_args(argv)
    lay = json.loads(Path(a.layout).read_text()); hdr, t = fp.parse_export(a.xlsx)
    par, perp = t["raw_par"], t["raw_perp"]; G = a.g or lay.get("g") or fp.header_g(hdr)
    excl = set(fp.expand_wells(a.exclude)) if a.exclude else set()
    print(f"G = {G} (G multiplies the parallel channel); blank = {a.blank}; excluded by hand: {a.exclude or 'none'}")
    allb = [w for g in lay["titration"] for w in fp.expand_wells(g["blank_wells"])]
    bp_pool, bs_pool = np.median([par[w] for w in allb]), np.median([perp[w] for w in allb])
    print(f"pooled blank ({len(allb)} VLP-only wells): par {bp_pool:.0f}  perp {bs_pool:.0f}  total {G*bp_pool+2*bs_pool:.0f}")
    def well_mp(w, b):
        m, _, T = fp.mp_r(np.array([par[w] - b[0]]), np.array([perp[w] - b[1]]), G); return m[0], T[0]
    rows, cs, ys, tots = [], [], [], []
    for g in lay["titration"]:
        ws = [w for w in fp.expand_wells(g["wells"]) if w not in excl]
        bw = fp.expand_wells(g["blank_wells"])
        b = (np.mean([par[w] for w in bw]), np.mean([perp[w] for w in bw])) if a.blank == "matched" else (bp_pool, bs_pool)
        tw = np.array([G * par[w] + 2 * perp[w] for w in ws]); flag = []
        if len(ws) >= 3 and not a.no_flag:
            med = np.median(tw); keep = np.abs(tw - med) <= 0.25 * med
            flag = [ws[i] for i in np.where(~keep)[0]]; ws = [w for w, k in zip(ws, keep) if k]
        vals = [well_mp(w, b) for w in ws]
        for m, T in vals: cs.append(g["conc"]); ys.append(m); tots.append(T)
        mp = np.array([v[0] for v in vals]); T = np.array([v[1] for v in vals])
        rows.append((g["conc"], len(mp), mp.mean(), mp.std(ddof=1) if len(mp) > 1 else np.nan, T.mean(), flag))
    fb = (bp_pool, bs_pool)
    free_w = fp.expand_wells(lay["free"]); fv = [well_mp(w, fb) for w in free_w]
    ftot = np.array([G * par[w] + 2 * perp[w] for w in free_w]); fmed = np.median(ftot)
    free_flag = [w for w, T in zip(free_w, ftot) if abs(T - fmed) > 0.25 * fmed]
    fv = [v for w, v in zip(free_w, fv) if w not in free_flag]
    for m, T in fv: cs.append(0.0); ys.append(m); tots.append(T)
    print(f"\n{'conc':>7}{'nM VP1':>8}{'n':>3}{'mP':>8}{'SD':>7}{'net total':>11}  flags")
    for c, n, m, sd, T, fl in rows:
        print(f"{c:>7g}{c*UG_TO_NM_VP1:>8.0f}{n:>3}{m:>8.1f}{sd:>7.1f}{T:>11.0f}  {'flagged '+str([fp.ROWS[r]+str(k+1) for r,k in fl]) if fl else ''}")
    fm = np.array([v[0] for v in fv]); print(f"{'alone':>7}{'':>8}{len(fm):>3}{fm.mean():>8.1f}{fm.std(ddof=1):>7.1f}{np.mean([v[1] for v in fv]):>11.0f}  "
          f"{'flagged '+str([fp.ROWS[r]+str(k+1) for r,k in free_flag]) if free_flag else ''}")
    ref = lay.get("reference")
    if ref:
        fw, bw = fp.expand_wells(ref["fluorescein"]), fp.expand_wells(ref["fl_buffer"])
        b = (np.mean([par[w] for w in bw]), np.mean([perp[w] for w in bw]))
        fl = [well_mp(w, b)[0] for w in fw]; print(f"fluorescein reference (G={G}): {np.round(fl,1)} mP (expect ~20); suggested G for 20 mP: "
              f"{np.mean([1.0408*(perp[w]-b[1])/(par[w]-b[0]) for w in fw]):.3f}")
    c, y = np.array(cs), np.array(ys); out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    res = {}
    def report(lab, mask, model, p0, lo, hi, names):
        try:
            popt, se, tc, rmse = fit(c[mask], y[mask], model, p0, lo, hi)
        except Exception as e:
            print(f"{lab}: fit failed ({e})"); return None
        kd = popt[2]; ci = (max(kd - tc * se[2], 0), kd + tc * se[2])
        extra = f"  Hill n {popt[3]:.1f} ± {se[3]:.1f}" if len(popt) == 4 else ""
        print(f"{lab:<28} free {popt[0]:.0f}  bound {popt[1]:.0f}  K {kd:.2f} µg/mL = {kd*UG_TO_NM_VP1:.0f} nM VP1 (95% CI {ci[0]:.2f}-{ci[1]:.2f} µg/mL){extra}  residual SD {rmse:.0f} mP")
        res[lab] = dict(popt=list(map(float, popt)), kd_ug=float(kd), ci=list(map(float, ci)), rmse=rmse); return popt
    print()
    allm = np.ones_like(c, bool)
    p1 = report("1:1 hyperbola, all", allm, hyp, [45, 210, 4], [0, 0, 0.01], [200, 600, 500], None)
    p2 = report("Hill, all", allm, hill, [45, 210, 4, 2], [0, 0, 0.01, 0.5], [200, 600, 500, 8], None)
    top = c.max(); m2 = c < top
    report(f"1:1 hyperbola, without {top:g}", m2, hyp, [45, 210, 4], [0, 0, 0.01], [200, 600, 500], None)
    report(f"Hill, without {top:g}", m2, hill, [45, 210, 4, 2], [0, 0, 0.01, 0.5], [200, 600, 500, 8], None)
    (out / "titration_fit.json").write_text(json.dumps(dict(G=G, blank=a.blank, fits=res), indent=1))
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2)); pos = c > 0
    ax[0].scatter(c[pos], y[pos], c="C0", s=18, label="aptamer + VLP (wells)"); ax[0].axhline(fm.mean(), ls=":", c="k", label="aptamer alone")
    cc = np.geomspace(max(c[pos].min() * 0.7, 0.05), c.max() * 1.2, 200)
    if p1 is not None: ax[0].plot(cc, hyp(cc, *p1), "--", c="grey", label="1:1 fit")
    if p2 is not None: ax[0].plot(cc, hill(cc, *p2), "-", c="C3", lw=1, label=f"Hill fit (n={p2[3]:.1f})")
    ax[0].set_xscale("log"); ax[0].set(xlabel="VLP (µg/mL)", ylabel=f"mP (G={G}, {a.blank} blank)", title=Path(a.xlsx).stem[:40]); ax[0].legend(fontsize=7)
    ax[1].scatter(c[pos], np.array(tots)[pos], s=18); ax[1].scatter([cc[0]] * len(fv), [v[1] for v in fv], c="k", marker="s", label="aptamer alone")
    ax[1].set_xscale("log"); ax[1].set(xlabel="VLP (µg/mL)", ylabel="net total intensity", title="Net total intensity"); ax[1].legend(fontsize=7)
    fig.tight_layout(); fig.savefig(out / "titration_fit.png", dpi=130); print(f"\nWrote {out/'titration_fit.json'} and {out/'titration_fit.png'}")

if __name__ == "__main__":
    main()
