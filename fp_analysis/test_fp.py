"""Self-checks: python3 -I test_fp.py  (uses the synthetic plate; no pytest needed)."""
import json, sys, tempfile
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fp_analysis as fp
from make_synthetic import build

here = Path(__file__).parent
d = Path(tempfile.mkdtemp())
build(d / "p.xlsx", g=1.056, kd=3.0)
hdr, tabs = fp.parse_export(d / "p.xlsx")
assert fp.header_g(hdr) == 1.056, hdr
layout = json.loads((here / "example_layout.json").read_text())
res = {x["name"]: x for x in fp.analyse(tabs, layout, 1.056)}

# G on the parallel channel: equal channels after G scaling -> 0 mP; 3:1 -> 500 mP
mp, r, tot = fp.mp_r(np.array([1 / 1.056]), np.array([1.0]), 1.056)
assert abs(mp[0]) < 1e-9 and abs(tot[0] - 3) < 1e-9
assert abs(fp.mp_r(np.array([3 / 1.056]), np.array([1.0]), 1.056)[0][0] - 500) < 1e-9
assert abs(fp._r_to_mp(2 * 0.5 / 2.5) - 500) < 1e-9          # P=0.5 <-> r=0.4

# blank subtraction recovers the true free-aptamer polarisation (not the inflated raw one)
assert abs(res["aptamer_alone"]["mp"] - 60) < 5, res["aptamer_alone"]["mp"]
assert abs(res["fluorescein"]["mp"] - 20) < 5
# the contaminated well is flagged and dropped
assert res["V4"]["flagged"] == [(3, 1)] and res["V4"]["n"] == 2

# fit recovers K_d
fit = fp.fit_series([x for x in res.values() if x["series"] == "bufA"], res["aptamer_alone"]["r"])
assert abs(fit["kd"] - 3.0) < 1.0, fit

# overlapping wells are rejected
bad = json.loads(json.dumps(layout)); bad["groups"][1]["wells"] = "A1-A5"
try:
    fp.analyse(tabs, bad, 1.056); raise SystemExit("overlap not detected")
except ValueError as e:
    assert "both" in str(e)
print("all checks passed")
