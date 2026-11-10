# fp_analysis

Analysis of Tecan Spark (SparkControl V3.2) fluorescence-polarization exports for the FAM-aptamer / norovirus-VLP assay.

```bash
pip install numpy scipy openpyxl matplotlib
python3 fp_analysis.py RESULT.xlsx layout.json --out results/      # G read from the file header, or --g 1.056
python3 -I test_fp.py                                              # self-checks on a synthetic plate
```

What it does: parses the `Rawdata (parallel/perpendicular)` tables, applies G to the **parallel** channel (Spark convention, G ≈ 1.05–1.10),
subtracts the blank **per channel** (never on mP), reports mP / anisotropy / net total intensity per group, flags wells whose total
intensity is >25% off their group median (dropped by default), fits a 1:1 hyperbola on anisotropy, and reports assay window and Z′.
Outputs `fp_results.json` and `fp_plot.png`.

The fit warns instead of silently reporting a K_d when the top concentration is <90% saturated, the range is <30-fold, K_d is not
constrained, or net total intensity changes >20% along the titration (bound/free brightness differ). `plateau_profile` shows how K_d
moves with an assumed plateau: if it moves a lot, K_d is not identifiable from that plate.

**Layout** (`example_layout.json`): groups of wells (`"A1-A3"`), with `role` (`sample`, `free`, `blank`, `reference`), `series`, `conc` (µg/mL),
`blank` (the group whose per-channel mean is subtracted, e.g. a buffer blank or VLP-only wells), and optional `exclude`. A well in two groups is an error.
The real 9 Nov well map is unresolved (handoff §11/§12), so the example layout describes the synthetic plate, not the real one.
Concentration is also given as VP1 nM using 5.6 µg/mL ≈ 96 nM VP1.
