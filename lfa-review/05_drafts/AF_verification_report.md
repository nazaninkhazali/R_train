# Verification report for sections 3.1-3.6 (A-F), 2026-11-10

## Checks run on the current drafts (A v4, B v3, C v3, D v3, E v5, F v2)
1. Coverage. Every one of the 609 records of sections A-F (93, 33, 47, 99, 382, 55) is cited in the narrative with its DOI (or PMID if no DOI) and appears in a table of its section: passed.
2. DOI integrity. Every DOI cited in the narrative exists in the evidence table, and none is cited from a record of another section: passed.
3. Numbers. For every narrative sentence that cites abstract-level records, each number was searched for in the abstract (PubMed export) and the chart fields of the cited records. No unexplained mismatch remained. The few sentences flagged contained derived values (for example 80-fold computed from 675.69 and 8.384 copies/uL, or 5.1 x 10^1 written as 51) or a number from a full-text record. Sentences that cite full-text records (31 records) were not checked this way and rest on the full-text reading.
4. Virus named. Every sentence that cites a record names the virus, or follows a sentence in the same paragraph that names it.
5. Reading of the signal. A "How the signal is read (from abstract)" column was added to all tables of A-F; second readouts are marked and their figures are not counted.

## Errors found and corrected during the check
- R02149 (section B): the colorimetric LOD (1 ng/mL by naked eye) had been recorded as not reported; the 0.1 ng/mL figure is fluorescent.
- R04627 (section C): visual figures (3.6 aM buffer, 28.6 aM nasopharyngeal wash) are now counted; the thermal-contrast reading is not.
- R05678 (section F): the time-to-signal paragraph cited the wrong record for the "routine samples" result; now cites 10.1515/cclm-2022-0873. R05854 has no DOI and is cited by PMID 36605302.
- Full-text counts in the evidence table: 31 records read in full (a 13, b 7, c 6, d 3, e 1, f 1); nine had been left as abstract-only.

## What the checks cannot show
- 1,071 of the 1,102 records, and 578 of the 609 records in A-F, rest on abstracts only. Claims about methods, matrices, controls and stability need the full text.
- 338 records (158 in A-D, 180 in E) do not say in the abstract how the strip is read. Full texts are needed (reminder in 07_open_questions.md).
- Reference methods and units differ between papers, so no ranking across studies is made.

## Decisions taken by default and still reversible
- Nine non-colour readers in section F (R03295, R03638, R03788, R04362, R04816, R04887, R05112, R05244, R05731) are described but not counted as colorimetric results.
- R08549 (thermoplasmonic nanoprisms, section A) and R06336 (thermochromic dengue strip, section D) stay in as flagged boundary cases.
- Commercial-kit evaluations (E10) and records before 2015 (E11) were excluded earlier.

## Open items per section
- A: R06317 (LOD exponent; comparator sensitivity 90.04% vs 83.33%), R05311 (150 nm nanoshells vs nanoparticles); two animal-virus strips known from abstract only.
- B: R05403 and R04517 (lost LOD exponents); carbon black (R06199) and selenium (R03310) PDFs not available; R02878 (abstract vs main-text comparator).
- C: R08369 (lost dilution exponents); R08742 and R08764 (2027 year in metadata); viral plus bacterial strips R07744, R08107, R08737; R08826 does not name its viruses.
- D: scope-check records R03041, R03119, R04535, R05963, R06590, R05822, R07722; six E9 exclusions reversible.
- E: R08160 abstract (100%) vs results (95.47%); commercial pregnancy-test strips R04269, R04707, R06175, R07905 flagged for scope; R07388 abstract incomplete; R03364 has no abstract.
- F: R06820 (abstract incomplete), R07836 (viruses not named).
- All sections: Au-engineering summary supplied by the author needs its article numbering before it can be used; record IDs must be replaced by numbered citations.
