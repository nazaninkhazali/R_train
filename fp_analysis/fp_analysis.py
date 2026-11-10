#!/usr/bin/env python3
"""Analysis of Tecan Spark (SparkControl V3.2) fluorescence-polarization exports.

Conventions (verified against the Spark result files, see README):
  * "Rawdata (parallel/perpendicular)" are the unscaled counts.
  * G multiplies the PARALLEL channel (Spark convention, G ~ 1.05-1.10 for
    fluorescein at a 20 mP reference).  mP = 1000*(G*Ipar - Iperp)/(G*Ipar + Iperp).
  * Blank subtraction is done per channel (parallel and perpendicular
    separately), never on mP.
  * Total intensity = G*Ipar + 2*Iperp; anisotropy r = (G*Ipar - Iperp)/Total.

Usage:
  python fp_analysis.py RESULT.xlsx LAYOUT.json [--g 1.056] [--out DIR]
"""
import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
from openpyxl import load_workbook
from scipy.optimize import curve_fit

ROWS = "ABCDEFGH"
TITLES = {
    "raw_par": "rawdata (parallel)",
    "raw_perp": "rawdata (perpendicular)",
}
VP1_NM_PER_UG_ML = 96.0 / 5.6  # 5.6 ug/mL ~ 96 nM VP1 (handoff section 1)


# ----------------------------------------------------------------- parsing
def _norm(v):
    return str(v).strip().lower() if v is not None else ""


def parse_export(path, sheet=None):
    """Return (header dict, {'raw_par': 8x12, 'raw_perp': 8x12})."""
    wb = load_workbook(path, data_only=True)
    ws = wb[sheet] if sheet else (wb["Result sheet"] if "Result sheet" in wb.sheetnames else wb.worksheets[0])
    rows = [[c for c in r] for r in ws.iter_rows(values_only=True)]

    header, tables = {}, {}
    title_rows = {}
    for i, r in enumerate(rows):
        for c in r:
            for key, title in TITLES.items():
                if _norm(c) == title:
                    title_rows[key] = i
    if len(title_rows) < 2:
        sys.exit("Could not find 'Rawdata (parallel)'/'Rawdata (perpendicular)' tables in the sheet.")

    first_title = min(title_rows.values())
    # header rows are everywhere before the first 8x12 table block; keep all
    # rows (the first two non-empty cells are label/value)
    for r in rows:
        cells = [c for c in r if c not in (None, "")]
        if len(cells) >= 2 and isinstance(cells[0], str):
            header.setdefault(cells[0].strip().lower(), cells[1])

    for key, t in title_rows.items():
        block = np.full((8, 12), np.nan)
        got = 0
        for r in rows[t + 1 : t + 14]:
            if got == 8:
                break
            cells = list(r)
            for j, c in enumerate(cells):
                if isinstance(c, str) and c.strip().upper() in tuple(ROWS) and j + 12 < len(cells) + 1:
                    vals = cells[j + 1 : j + 13]
                    if len(vals) == 12:
                        ri = ROWS.index(c.strip().upper())
                        block[ri] = [float(v) if isinstance(v, (int, float)) else np.nan for v in vals]
                        got += 1
                        break
        if got != 8:
            sys.exit(f"Table '{TITLES[key]}': expected 8 rows A-H, found {got}.")
        tables[key] = block
    return header, tables


def header_g(header):
    """Find the G factor used by SparkControl in the header, or None."""
    for k, v in header.items():
        if re.search(r"\bg[- ]?factor\b", k) and isinstance(v, (int, float)):
            return float(v)
    return None


# ---------------------------------------------------------------- layout
def expand_wells(spec):
    """'A1-A3, B1' or ['A1-A3'] -> [(row, col), ...] zero-based."""
    if isinstance(spec, str):
        spec = [s for s in re.split(r"[,\s]+", spec) if s]
    out = []
    for s in spec:
        m = re.fullmatch(r"([A-H])(\d{1,2})(?:-([A-H])?(\d{1,2}))?", s.upper())
        if not m:
            raise ValueError(f"Bad well spec: {s}")
        r1, c1, r2, c2 = m.group(1), int(m.group(2)), m.group(3) or m.group(1), m.group(4)
        c2 = int(c2) if c2 else c1
        for r in range(ROWS.index(r1), ROWS.index(r2) + 1):
            for c in range(c1, c2 + 1):
                out.append((r, c - 1))
    return out


# --------------------------------------------------------------- analysis
def mp_r(par, perp, g):
    """par/perp raw counts; returns mP, anisotropy, total (G on parallel)."""
    gp = g * par
    tot = gp + 2 * perp
    with np.errstate(divide="ignore", invalid="ignore"):
        mp = 1000 * (gp - perp) / (gp + perp)
        r = (gp - perp) / tot
    return mp, r, tot


def analyse(tables, layout, g, flag_tol=0.25):
    par, perp = tables["raw_par"], tables["raw_perp"]
    groups = {}
    seen = {}
    for gr in layout["groups"]:  # a well can have only one role
        for w in expand_wells(gr["wells"]):
            if w in seen:
                raise ValueError(f"Well {ROWS[w[0]]}{w[1] + 1} is in both '{seen[w]}' and '{gr['name']}'")
            seen[w] = gr["name"]
    for gr in layout["groups"]:
        wells = expand_wells(gr["wells"])
        excl = set(expand_wells(gr.get("exclude", [])))
        used = [w for w in wells if w not in excl]
        p = np.array([par[w] for w in used])
        s = np.array([perp[w] for w in used])
        tot_w = g * p + 2 * s
        keep = np.ones(len(used), bool)
        if len(used) >= 3 and flag_tol:  # flag wells deviating from group median
            med = np.median(tot_w)
            keep = np.abs(tot_w - med) <= flag_tol * med
        groups[gr["name"]] = dict(gr, wells=used, excluded=sorted(excl), par=p, perp=s,
                                  flagged=[used[i] for i in np.where(~keep)[0]], keep=keep)

    results = []
    for name, gr in groups.items():
        if gr.get("role") in ("blank",):
            continue
        keep = gr["keep"] if layout.get("drop_flagged", True) else np.ones(len(gr["par"]), bool)
        p, s = gr["par"][keep], gr["perp"][keep]
        bname = gr.get("blank")
        if bname:
            b = groups[bname]
            bk = b["keep"] if layout.get("drop_flagged", True) else np.ones(len(b["par"]), bool)
            bp, bs = b["par"][bk].mean(), b["perp"][bk].mean()
        else:
            bp = bs = 0.0
        pn, sn = p - bp, s - bs  # per-channel blank subtraction
        mp_w, r_w, tot_w = mp_r(pn, sn, g)
        results.append(dict(
            name=name, role=gr.get("role", "sample"), series=gr.get("series"), conc=gr.get("conc"),
            blank=bname, n=len(p), flagged=gr["flagged"], excluded=gr["excluded"],
            mp=float(np.nanmean(mp_w)), mp_sd=float(np.nanstd(mp_w, ddof=1)) if len(p) > 1 else np.nan,
            r=float(np.nanmean(r_w)), r_sd=float(np.nanstd(r_w, ddof=1)) if len(p) > 1 else np.nan,
            total=float(np.mean(tot_w)),
            total_over_blank=float(np.mean(g * p + 2 * s) / (g * bp + 2 * bs)) if bname and (bp or bs) else np.nan,
        ))
    return results


def hyperbola(c, r_free, r_bound, kd):
    return r_free + (r_bound - r_free) * c / (kd + c)


def fit_series(series_res, r_free_fixed=None):
    """Fit anisotropy vs conc.  r_bound floats only if the data justify it."""
    pts = sorted([x for x in series_res if x["conc"] is not None and x["role"] == "sample"], key=lambda x: x["conc"])
    c = np.array([x["conc"] for x in pts], float)
    r = np.array([x["r"] for x in pts], float)
    sd = np.array([x["r_sd"] if np.isfinite(x["r_sd"]) and x["r_sd"] > 0 else np.nan for x in pts])
    out = dict(n_points=len(c), conc_range_fold=float(c.max() / c.min()) if len(c) > 1 else 1.0, warnings=[])
    if len(c) < 4:
        out["warnings"].append("fewer than 4 concentrations: no fit")
        return out
    if out["conc_range_fold"] < 30:
        out["warnings"].append(f"concentration range only {out['conc_range_fold']:.0f}-fold (aim for >= 100-fold)")
    rf = r_free_fixed if r_free_fixed is not None else r.min()
    sigma = np.where(np.isfinite(sd), sd, np.nanmedian(sd) if np.isfinite(sd).any() else None)
    use_sigma = sigma is not None and np.all(np.isfinite(sigma))
    kw = dict(sigma=sigma, absolute_sigma=False) if use_sigma else {}
    try:
        popt, pcov = curve_fit(lambda cc, rb, kd: hyperbola(cc, rf, rb, kd), c, r,
                               p0=[r.max() * 1.2, np.median(c)], bounds=([r.min(), c.min() / 100], [0.5, c.max() * 1e3]), **kw)
        se = np.sqrt(np.diag(pcov))
        kd, kd_se = popt[1], se[1]
        out.update(r_free=float(rf), r_bound=float(popt[0]), kd=float(kd), kd_se=float(kd_se),
                   kd_vp1_nM=float(kd * VP1_NM_PER_UG_ML))
        sat = c.max() / (kd + c.max())
        out["top_saturation"] = float(sat)
        if sat < 0.90:
            out["warnings"].append(
                f"top concentration reaches only {sat:.0%} of saturation (fitted): K_d and r_bound are confounded; "
                "extend VLP range upward (aim >= 90%) before reporting K_d")
        if not np.isfinite(kd_se) or kd_se > kd or kd > 3 * c.max():
            out["warnings"].append("K_d poorly constrained (SE > value or K_d beyond top concentration)")
        # degeneracy check: fix plateau at several windows above free and compare K_d
        prof = {}
        for add in (0.05, 0.10, 0.15, 0.20):
            try:
                q, _ = curve_fit(lambda cc, kd_: hyperbola(cc, rf, rf + add, kd_), c, r, p0=[np.median(c)],
                                 bounds=(c.min() / 100, c.max() * 1e3))
                res = float(np.sqrt(np.mean((hyperbola(c, rf, rf + add, q[0]) - r) ** 2)))
                prof[f"plateau=+{add:.2f}"] = dict(kd=float(q[0]), rmse=res)
            except Exception:
                pass
        out["plateau_profile"] = prof
    except Exception as e:  # noqa
        out["warnings"].append(f"fit failed: {e}")
    return out


def assay_quality(res_free, res_top):
    """Assay window (mP) and Z' on anisotropy."""
    win = res_top["mp"] - res_free["mp"]
    d = abs(res_top["r"] - res_free["r"])
    z = 1 - 3 * (res_free["r_sd"] + res_top["r_sd"]) / d if d and np.isfinite(res_free["r_sd"]) else np.nan
    return dict(window_mP=float(win), z_prime=float(z))


# ------------------------------------------------------------------- main
def plot(results, fits, out, title):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    series = sorted({x["series"] for x in results if x["series"]})
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    for s in series:
        pts = sorted([x for x in results if x["series"] == s and x["role"] == "sample" and x["conc"]], key=lambda x: x["conc"])
        c = np.array([x["conc"] for x in pts])
        ax[0].errorbar(c, [x["mp"] for x in pts], [x["mp_sd"] for x in pts], marker="o", capsize=3, label=s)
        ax[1].plot(c, [x["total"] for x in pts], marker="o", label=s)
        f = fits.get(s, {})
        if "kd" in f:
            cc = np.geomspace(c.min(), c.max(), 100)
            r = hyperbola(cc, f["r_free"], f["r_bound"], f["kd"])
            ax[0].plot(cc, _r_to_mp(r), "--", color="grey", lw=1)
    for x in results:
        if x["role"] == "free":
            ax[0].axhline(x["mp"], ls=":", color="k", lw=1)
    ax[0].set_xscale("log"); ax[1].set_xscale("log")
    ax[0].set(xlabel="VLP (µg/mL)", ylabel="mP (blank-subtracted)", title=title)
    ax[1].set(xlabel="VLP (µg/mL)", ylabel="net total intensity", title="Total intensity (check quenching/scatter)")
    ax[0].legend(); fig.tight_layout(); fig.savefig(out, dpi=150)


def _r_to_mp(r):
    """anisotropy -> mP via r = 2P/(3-P)  =>  P = 3r/(2+r)."""
    return 1000 * 3 * r / (2 + r)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx"); ap.add_argument("layout")
    ap.add_argument("--g", type=float, help="G factor (overrides header and layout)")
    ap.add_argument("--out", default=".")
    ap.add_argument("--sheet")
    a = ap.parse_args(argv)

    layout = json.loads(Path(a.layout).read_text())
    header, tables = parse_export(a.xlsx, a.sheet)
    g = a.g or layout.get("g") or header_g(header)
    if g is None:
        sys.exit("G factor not found in header; pass --g")
    if g < 1.0 and not a.g:
        print(f"WARNING: G={g} < 1 looks like the textbook convention; Spark G is ~1.05-1.10", file=sys.stderr)
    print(f"G = {g} (G multiplies the parallel channel)  |  gain/Z from header: "
          f"{ {k: v for k, v in header.items() if k.startswith(('gain', 'z-position', 'z position'))} }")

    results = analyse(tables, layout, g)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    free = {x["series"]: x for x in results if x["role"] == "free"}

    print(f"\n{'group':<18}{'series':<10}{'conc':>8}{'n':>3}{'mP':>8}{'±SD':>7}{'net total':>11}{'tot/blank':>10}  flags")
    for x in results:
        fl = (f"flagged:{[ROWS[r]+str(c+1) for r,c in x['flagged']]} " if x["flagged"] else "") + \
             (f"excluded:{[ROWS[r]+str(c+1) for r,c in x['excluded']]}" if x["excluded"] else "")
        print(f"{x['name']:<18}{str(x['series'] or ''):<10}{x['conc'] if x['conc'] is not None else '':>8}{x['n']:>3}"
              f"{x['mp']:>8.1f}{x['mp_sd']:>7.1f}{x['total']:>11.0f}{x['total_over_blank']:>10.1f}  {fl}")

    fits = {}
    for s in sorted({x["series"] for x in results if x["series"] and x["role"] == "sample"}):
        ser = [x for x in results if x["series"] == s]
        rf = free[s]["r"] if s in free else None
        f = fit_series(ser, rf)
        top = max((x for x in ser if x["role"] == "sample"), key=lambda x: x["conc"])
        if s in free:
            f["quality"] = assay_quality(free[s], top)
            tot_free = free[s]["total"]
            ratio = [x["total"] / tot_free for x in ser if x["role"] == "sample"]
            if max(abs(np.array(ratio) - 1)) > 0.2:
                f["warnings"].append("net total intensity changes >20% along titration: bound/free brightness differ; "
                                     "weight the fit by brightness ratio Q before trusting K_d")
        fits[s] = f
        print(f"\n[{s}] {json.dumps(f, indent=2)}")

    (out / "fp_results.json").write_text(json.dumps(dict(g=g, results=results, fits=fits), indent=2, default=str))
    plot(results, fits, out / "fp_plot.png", Path(a.xlsx).stem)
    print(f"\nWrote {out/'fp_results.json'} and {out/'fp_plot.png'}")


if __name__ == "__main__":
    main()
