# PRISMA-ScR flow counts (title/abstract stage), PubMed search v1.0, run 2026-10-28

| Stage | n |
|---|---|
| Unique records identified (PubMed only) | 8,836 |
| Duplicates / preprint or republication of an included study (E7) | 13 |
| Records screened on title/abstract | 8,836 (13 of them removed as duplicates) |
| Excluded at title/abstract | 5,760 (including the 13 duplicates) |
| Additionally excluded at chart-based scope-check review (2026-11-04) | 439 |
| Total excluded after scope-check review | 6,199 |
| Retained for charting (before scope-check) | 3,076 (2,595 published 2015-2026; 481 before 2015) |
| Included after scope-check review | 2,637 (2,227 published 2015-2026; 410 before 2015) |
| Excluded by scope amendment E10 (commercial/finished-kit evaluations, 2026-11-05) | 1,322 |
| Included after E10 | 1,315 (1,150 published 2015-2026; 165 before 2015) |
| Section-z records (21) reviewed and excluded (19 E10, 2 E9) | 21 |
| Section-b review: R07568 excluded (E2, not a conventional LFA) | 1 |
| Section-c review: 7 evaluations of marketed silver-amplification or rapid-test kits excluded (E10) | 7 |
| Section-d review: 6 antibody-screening papers excluded (E9) | 6 |
| Section-g review: 15 evaluations of marketed multiplex rapid antigen tests excluded (E10) | 15 |
| **Final included** | **1,265 (1,102 published 2015-2026; 163 before 2015)** |

Exclusion reasons (final, 6,199): E1 not a virus or non-viral analyte 1,120; E2 not an LFA 896; E3 LFA but not colorimetric 377; E4 publication type 1,182; E5 non-English 271; E6 no original assay data 637; E7 duplicate 13; E8 other/retracted 9; E9 LFA/RDT used only as a tool 1,694.

Scope-check review: 640 charted records were flagged during abstract charting; 439 were excluded by rule (script `scripts/apply_scope_rules.py`, reason and chart flag recorded in `note_claude`), 201 retained and flagged (no abstract 42, incomplete abstract 12, arthropod-vector pools 7, reader formats with coloured label 7, non-viral co-target 11, small n 4, interference 3, other flag-only 115). These decisions use charting-level abstract reading and remain single-screener.

Method notes
- Single screener (Claude), per author delegation; no second screener. Author's rule decisions of 2026-10-30 applied (see protocol); UNSURE category fully resolved by excluding.
- Self-check: 65 random exclusions (E2 20, E3 15, E6 12, E9 18; year >= 2015) re-read; 0 should have been included, 2 reason codes corrected (E2 to E3). Sample is small; the true miss rate is not estimated.
- Possible-duplicate flags (103) reviewed: 13 excluded as E7; remaining flags are pairs of excluded records or errata, no action.
- Limitations: PubMed only; no seed-set recall check; veterinary, aquaculture and plant literature likely under-captured; abstract-level decisions.

E10 amendment: 1,322 section-h records (commercial or finished-kit evaluations, accuracy/epidemiology use of marketed tests) excluded; 65 development/prototype records in section h retained. Rule applied by title and chart tags (`scripts/apply_e10.py`); borderline cases need author check.
