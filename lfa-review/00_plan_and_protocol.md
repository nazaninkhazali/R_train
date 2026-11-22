# Protocol (DRAFT v0.1) — Colorimetric lateral flow assays for virus detection in human, animal and plant hosts: a scoping review

Status: **draft v0.2 — not final, not registered**
Date of draft: 2026-10-17; updated 2026-10-18 (see decision log, §12)

Note on v0.2: on 2026-10-18 the author approved the plan in general terms ("I agree with the plan"). I have
therefore recorded each [PROPOSED] item and each [DECISION NEEDED] item that had a stated default as
**accepted provisionally** (§12). Any of them can still be changed. Items with no default remain open.
Items marked **[DECISION NEEDED]** must be settled before the protocol is frozen.
Items marked **[PROPOSED]** are my suggestions and need your approval.

---

## 1. Review type and reporting standards

- Review type: **scoping review** (decided 2026-10-17).
- Methodological guidance: JBI scoping review methodology (DOI: 10.11124/JBIES-20-00167).
- Reporting: PRISMA-ScR checklist (DOI: 10.7326/M18-0850).
- Search reporting: PRISMA-S (DOI: 10.1186/s13643-020-01542-z).
- Registration **[PROPOSED]**: register this protocol on OSF (Open Science Framework) before screening
  starts. Reason: scoping reviews cannot be registered in PROSPERO, and a time-stamped protocol shows the
  eligibility criteria were set before the results were seen.

Wording rule: the article will be called a "scoping review". It will not be called "systematic" or
"comprehensive" unless the final methods justify that, for example multiple databases searched and dual
screening done.

## 2. Rationale (to be written with evidence in Stage 7)

Placeholder only; no literature claims are made here. The introduction will need to establish, with
citations:
- why colorimetric (instrument-free) readout matters for point-of-care and field testing;
- why combining human, veterinary and plant viruses is useful (shared technologies; One Health);
- what existing reviews cover and what they leave out, so the novelty of this review is shown with
  evidence and not just asserted. This is mapped in Stage 2.

## 3. Review question and objectives

**Main question.** What is known about the design, targets, readout and validation of lateral flow assays
with colorimetric detection for viruses of human, animal and plant hosts?

**Sub-questions** **[PROPOSED]**:
- RQ1 — Labels and signal generation: which colorimetric labels and colour-generating or enhancement
  strategies have been used, and how has their use changed over time?
- RQ2 — Targets and hosts: which viruses, host species, analyte types (antigen, antibody, nucleic acid)
  and sample matrices have been addressed?
- RQ3 — Assay architecture: which formats (sandwich, competitive, nucleic-acid amplification with strip
  readout, multiplex, dual-mode) have been used?
- RQ4 — Readout: how is the result read (naked eye, smartphone, scanner/reader), and is it qualitative,
  semi-quantitative or quantitative?
- RQ5 — Performance reporting: how are analytical performance (detection limit, cross-reactivity) and
  diagnostic performance (sensitivity, specificity against a reference method) reported, in which
  settings and with what sample sizes?
- RQ6 — Translation: what evidence exists on validation with real samples, field or clinical
  evaluation, and commercial availability?
- RQ7 — Gaps: where is evidence missing or of limited reporting quality, by technology, host and virus?

## 4. Eligibility criteria (PCC framework)

### Population (targets)
- **Included:** viruses of any host: human; animals (livestock, poultry, companion animals, wildlife);
  aquaculture species (fish, crustaceans, molluscs); plants.
- Viruses detected in any sample type, including environmental or food samples **[DECISION NEEDED: include
  food/environmental samples such as norovirus in shellfish or wastewater? I propose to include them]**.
- **Excluded:** bacteria, fungi, parasites and prions. Studies of several pathogen types are kept only for
  their virus results.
- **[DECISION NEEDED]** Viroids, bacteriophages and satellite viruses. I propose to exclude them unless you
  want them; they are rare and add definitional problems.

### Concept (the assay)
A study is included if it reports a **lateral flow assay** (immunochromatographic strip, lateral flow
dipstick, or a cassette with a lateral flow strip) in which **the test result is produced as a visible
colour signal**.

Colorimetric signal categories included (agreed 2026-10-17):
1. Plasmonic metal nanoparticles: gold nanoparticles (colloidal gold), shape-engineered gold
   (nanostars, nanoflowers), silver, bimetallic or core–shell particles (e.g., Au@Ag, Au@Pt).
2. Coloured carriers: coloured latex or polystyrene beads, cellulose nanobeads, carbon black or
   carbon nanoparticles, dye-loaded liposomes.
3. Colour-generating amplification: nanozymes (e.g., Pt, Prussian blue, Fe₃O₄ with peroxidase-like
   activity), enzyme–substrate systems (e.g., HRP/TMB), silver or gold enhancement.
4. Nucleic-acid amplification (e.g., PCR, LAMP, RPA) or CRISPR-Cas reactions **when the final readout is
   a colorimetric lateral flow strip**.
5. Instrument-assisted measurement (smartphone, scanner, reader) of a colorimetric signal.
6. Multiplex assays (several viruses or targets on one strip or device).
7. Dual-mode assays: included, but only the colorimetric channel is charted and analysed.

Decision rules for borderline cases **[PROPOSED; please confirm or change each]**:

| Case | Proposed decision | Reason |
|---|---|---|
| Fluorescent, SERS, chemiluminescent, electrochemical or magnetic LFA without a colorimetric channel | Exclude | Not colorimetric |
| AuNP strip read only by photothermal or SERS signal | Exclude | Colour is not the reported result |
| Colorimetric assay in solution or on paper without lateral flow (e.g., AuNP aggregation in a tube, LAMP colour change in a tube, µPADs without lateral flow) | Exclude | Not a lateral flow assay |
| Vertical flow / flow-through devices | **[DECISION NEEDED]**: exclude, or chart separately as "related formats" | Similar labels but a different device principle |
| Commercial LFA evaluated without describing its label | Include if the device is a colorimetric LFA (e.g., visual line read); record label as "not reported" | Most clinical evaluations use commercial colloidal-gold or latex devices |
| Same assay reported in several papers | Include all; link as one study with multiple reports | Avoids double-counting |

### Context
- Any setting (laboratory, clinical, point of care, farm, field), any country.
- Publication dates: **all years searched; detailed charting and synthesis focused on 2015–2026**
  (decided 2026-10-17). **[DECISION NEEDED]** How will pre-2015 studies be handled? I propose to screen
  and chart them at a basic level (year, virus, host, label, format) so the trend analysis (RQ1) covers
  all years. Full detail (performance, validation) would be extracted only for 2015–2026.

### Types of sources **[DECISION NEEDED; my proposal below]**
- Include: primary research articles that develop and/or evaluate an assay with experimental results,
  including analytical-only laboratory studies and evaluations of commercial tests.
- Include as a charted category: clinical, field and diagnostic-accuracy studies.
- Exclude from charting: reviews, editorials and commentaries. These will be used for citation chasing
  and to map overlap with existing reviews.
- **[DECISION NEEDED]** Preprints, conference abstracts, theses and patents. I propose to exclude them,
  because they have limited or unreviewed methods detail. A scoping review may include them, though.
- **[DECISION NEEDED]** Minimum evidence requirement: should a study have to test real samples
  (clinical, field or spiked real matrix) to be included? I propose **no**: include all, and chart
  "tested on real samples: yes/no" as a variable, because this gap is itself a key finding (RQ6/RQ7).

### Language **[DECISION NEEDED]**
I propose English only, stated as a limitation. Note that a large share of veterinary and plant LFA work
may be published in Chinese-language journals. Excluding them is a known bias that must be reported.

## 5. Information sources

| Source | Who searches | Status |
|---|---|---|
| PubMed/MEDLINE | Me (PubMed connector) | Available. Max 20 Boolean operators per query, so strategies are split and merged |
| Scopus | You (export RIS/CSV) | **[DECISION NEEDED]** do you have access? |
| Web of Science Core Collection | You | **[DECISION NEEDED]** |
| CAB Abstracts / AGRICOLA (veterinary and plant) | You | **[DECISION NEEDED]** Strongly recommended now that plants are in scope |
| Embase | You | Optional (mostly human clinical) |
| Reference lists of included reviews; forward citation of key papers | Me (PubMed related-article tools) + you (Scopus/Google Scholar "cited by") | Planned |

Access limits found while drafting (2026-10-17): from this environment, direct connections to NCBI
E-utilities, Crossref and doi.org are **blocked** by the network policy. DOI verification will use the
PubMed connector's metadata. DOIs of papers not in PubMed (common for chemistry and plant journals) will
need your help or a later check.

Exploratory sizing searches were run in PubMed on 2026-10-17 only to estimate volume. They are **not**
part of the formal search, which will be built, tested and logged in Stage 2.

## 6. Search strategy (developed in Stage 2)
- Three concept blocks: (lateral flow terms) AND (colorimetric/label terms) AND (virus terms, including
  named human, animal, aquaculture and plant viruses).
- Validation: a seed set of 10–20 known relevant papers must all be retrieved. Missed papers lead to
  strategy revision.
- Every executed string, database, platform, date and hit count is recorded in `01_search_log.md`.
- Finding from strategy testing (2026-10-18): adding a colorimetric term block lowered seed-set recall from
  8/9 to 5/9, because abstracts often do not name the label. **[DECISION NEEDED]** whether to keep the
  block (see `01_search_log.md` §C).

## 7. Selection of sources
- Stage A: title/abstract screening. Stage B: full-text screening, with the exclusion reason recorded for
  each excluded full text.
- **[PROPOSED]** Pilot: both screeners screen the same 50 records, then refine the criteria.
- **[DECISION NEEDED]** Second screener: I do the first pass on all records; you (or a co-author) screen
  a random ≥20% sample independently. Agreement is reported (Cohen's κ) and disagreements are resolved by
  discussion. Without a human second screener, this limitation must be stated in the paper.
- Results reported in a PRISMA-ScR flow diagram.

## 8. Data charting (evidence table)
Fields (agreed): full citation; DOI; access status (**full text assessed / abstract only**); virus;
virus family; host species; host category (human / animal / aquaculture / plant); assay format; target
analyte; recognition element (antibody, aptamer, nucleic-acid probe, other); colorimetric label;
enhancement strategy; amplification/CRISPR (if any); multiplex (yes/no, number of targets); dual-mode
(yes/no, other mode); readout (eye / smartphone / reader); qualitative or quantitative; sample type;
real samples tested (yes/no, n); study design; analytical detection limit (value, units, matrix, how
determined); diagnostic sensitivity/specificity (reference method, n positives/negatives, setting);
time-to-result; cross-reactivity tested (yes/no); commercial status; reported limitations; my notes.

Rules: missing values are recorded as "not reported" (absent from the paper) or "not assessed" (not
checked, e.g., abstract-only). Details that need the full text are never filled in from an abstract. The
charting form is piloted on ~10 papers and revised before full extraction.

## 9. Critical appraisal **[PROPOSED]**
Formal appraisal is optional in scoping reviews (DOI: 10.11124/JBIES-20-00167). I propose two light layers:
- For all studies: reporting-completeness indicators (real samples tested; LOD method stated;
  cross-reactivity tested; reference method stated; replicates reported).
- For clinical/field diagnostic-accuracy studies only: QUADAS-2 domains (DOI:
  10.7326/0003-4819-155-8-201110180-00009), used descriptively, not to exclude studies.

## 10. Synthesis
- Descriptive: counts and evidence maps (e.g., label type × host category × year; virus family ×
  analyte type), tables and narrative summary for each RQ.
- No meta-analysis. Detection limits are compared only within the same units and matrix, and always with
  stated caveats. Analytical detection limits are never compared with diagnostic sensitivity.
- Reported results are kept separate from our interpretation in the text.

## 11. Preliminary article structure (finalized in Stage 6)
1. Introduction and rationale
2. Methods (scoping review)
3. Results overview (PRISMA flow, evidence map)
4. Principles of colorimetric LFA (background, cited)
5. Colorimetric labels: plasmonic NPs; coloured carriers
6. Colour-generating amplification and enhancement
7. Nucleic-acid amplification and CRISPR with strip readout
8. Readout and quantification (eye, smartphone, reader)
9. Multiplex and dual-mode assays
10. Applications by host: human; animal (incl. aquaculture); plant
11. Performance reporting and validation evidence
12. Gaps, limitations and future directions
13. Conclusions

## 12. Decision log
| Date | Decision | By |
|---|---|---|
| 2026-10-17 | Focus on colorimetric detection | Author |
| 2026-10-17 | Include veterinary viruses | Author |
| 2026-10-17 | Review type: scoping review | Author |
| 2026-10-17 | Dates: all years, focus 2015–2026 | Author |
| 2026-10-17 | Hosts: human, animal, aquaculture, plant | Author |
| 2026-10-17 | Include NAAT/CRISPR + strip, instrument colour reading, multiplex, dual-mode | Author |
| 2026-10-18 | Provisionally accepted defaults (general approval): sub-questions RQ1–RQ7; borderline-case rules table; include food/environmental samples; exclude viroids, phages, satellites; pre-2015 studies charted at basic level only; include analytical-only and commercial-test studies; no real-sample requirement (charted as variable); exclude preprints, conference abstracts, theses, patents; English only (bias to be reported); pilot screening of 50 records; light appraisal (reporting indicators + QUADAS-2 for accuracy studies); OSF registration recommended | Author (general approval), recorded by Claude |
| 2026-10-28 | Screening approach: title/abstract screening of all records by Claude alone (single AI-assisted reviewer). The author checks records at the full-text and synthesis stage. Safeguards: UNSURE when in doubt; a reason code for every exclusion; a second-pass self-check of a random sample of exclusions; a known-paper recall check; limitation reported in the methods. An optional author check of 50 random exclusions was offered. | Author |
| 2026-10-28 | Pilot rule changes adopted: new code E9 (LFA/RDT used only as a tool, not evaluated) → exclude; implementation/feasibility studies without test-performance data → exclude (E9); component-only studies (e.g. antibody epitope mapping without strip testing) → exclude (E6); commercial devices with unclear label/readout → UNSURE; English only kept (bias reported; e.g. pilot record R02553, Chinese carbon-NP Ebola LFA). Deterministic rules: non-English → E5; published erratum, preprint, review/systematic review/meta-analysis, editorial, news, guideline, historical article → E4 (reviews kept on a separate list for overlap mapping); retracted publication → E8. Comments and letters are screened by hand, because letters can contain data. | Author approved continuing with Claude's decisions |
| 2026-10-18 | Still open: target journal/audience; human/animal/plant weighting; vertical-flow devices; databases available to the author; second screener; colorimetric block in search (see 01_search_log.md §C) | — |

## 13. Methodology references used in this protocol (verified via PubMed metadata, 2026-10-17)
- Tricco AC, et al. PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation.
  Ann Intern Med. 2018;169(7):467–473. DOI: 10.7326/M18-0850
- Peters MDJ, et al. Updated methodological guidance for the conduct of scoping reviews.
  JBI Evid Synth. 2020;18(10):2119–2126. DOI: 10.11124/JBIES-20-00167
- Rethlefsen ML, et al. PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches
  in Systematic Reviews. Syst Rev. 2021;10(1):39. DOI: 10.1186/s13643-020-01542-z
- Whiting PF, et al. QUADAS-2: a revised tool for the quality assessment of diagnostic accuracy studies.
  Ann Intern Med. 2011;155(8):529–536. DOI: 10.7326/0003-4819-155-8-201110180-00009

## Screening rule decisions (author, 2026-10-30)
Applied to all title/abstract decisions; UNSURE category removed (0 remaining).
- Insect viruses (BmNPV, DWV, BmBDV): out of scope (E1). Aquaculture nodaviruses (fish, shrimp) retained.
- Viroids: out of scope (E1).
- Used/spent strips as sample source for PCR, sequencing or shipment: excluded (E9).
- Reader or label-engineering papers with no stated viral target: excluded (E6).
- Dual-mode assays reporting only a fluorescent channel: excluded (E3).
- Plant-virus "First Report" immunostrip papers: excluded (E9).
- CRISPR/isothermal papers whose abstract does not state a lateral-flow readout: excluded (E2).
- LFA used only to validate another new platform; method papers using a commercial LFA with no new accuracy data: excluded.
- LFAs for non-viral targets and host-biomarker assays (CRP, IL-6, CD4, CXCL10): excluded (E1).

## Review structure decisions (author, 2026-11-01)
- PubMed only; no seed-set recall check (state as limitation).
- Organised by technology section (AuNP engineering; other coloured labels; catalytic amplification; assay/flow engineering; nucleic-acid amplification + strip; smartphone/reader/AI; multiplex/dual-mode; clinical/commercial evaluation; veterinary/aquaculture/plant).
- Studies discussed individually (innovation, approach, analytical LOD with units/matrix); repeated approaches grouped at section end.
- Ordering within sections by contribution type, then fold-improvement over each paper's own comparator; no cross-study LOD ranking.
- Main-text table must contain every test discussed in the text (script-checked); full abstract-level charting in supplement.

## Scope-check review decisions (2026-11-04)
- Flags raised during charting (640 records) were converted to recorded exclusions by explicit rules (`scripts/apply_scope_rules.py`); 439 excluded, 201 retained and flagged.
- Author agreed: Sofia, LumiraDx and fluorescence FIA formats are not colorimetric (E3). BD Veritor and other reflectance-reader strips kept only when the label is a coloured particle.
- Epidemiology, seroprevalence and surveillance papers using an LFA only as a tool (E9); strip not stated or not an LFA (E2); modelling, EQA/QA, protocol, case report (E6).
- Retained and flagged: arthropod-vector pools, viral assays with a non-viral co-target, records without or with incomplete abstracts, small-n and interference studies.
- Included total: 2,637 (2,227 from 2015-2026; 410 pre-2015).

## Scope amendment (author, 2026-11-05)
Commercial/finished-kit evaluations are out of scope (new code E10). Section h retained only for development or prototype papers (65). Post-hoc change, to be stated in the manuscript. Included total: 1,315.

Section-z review (2026-11-05): 21 unclassified records excluded (19 E10, 2 E9). Final included: 1,294.

## Boundary-case decision (author, 2026-11-05)
R07685 (plasmonic scattering LFIA, DOI: 10.1038/s41467-025-58663-z) is kept in section a as a flagged boundary case; its LOD is reported separately from absorption-based strips. LOD and clinical values are to be reported with the readout (naked eye, scanner/imager, smartphone, reader) beside each.

Section-b review (2026-11-05): R07568 excluded (E2) by default decision; R02149 kept as dual-mode note. Final included: 1,293.

Section-c review (2026-11-05): 7 kit evaluations excluded (E10; R00647, R01362, R02575, R02638, R04171, R05720, R08189), by default, reversible. Final included: 1,286.

Section-d review (2026-11-05): 6 records where the LFA only screens antibodies/peptides excluded (E9; R04099, R04230, R04396, R04446, R05367, R05737), default, reversible. Final included: 1,280.

Section-g review (2026-11-05): 15 evaluations of marketed multiplex rapid antigen tests excluded (E10), default, reversible. Final included: 1,265.

Scope amendment (author, 2026-11-05): records published before 2015 are excluded from the analysis (E11, 163 records); the search covered all years, a short paragraph on the origin of the lateral flow assay replaces them. Final included: 1,102.

## Amendment 2026-11-10: article framing (author decision)
The article describes methodologies, substances and technologies and how each changes the colorimetric signal. Only colorimetric detection is in scope. Sections are rewritten one at a time around four questions (what limits the signal; which technology addresses it; what the paper reports against its own baseline; what it costs), starting with section 3.1 (A). Sections 3.5-3.9 (E-I) will be shortened and their records re-sorted by mechanism; record counts will be updated when that is done. Text-assessment field corrected: 31 records read in full (a 13, b 7, c 6, d 3, e 1, f 1).

## Amendment 2026-11-10 (b): nucleic-acid strips (section E)
Author rule: keep nucleic-acid papers only where the final reading is also colorimetric, and state how the signal is read in each paper. Check of the 382 section-E records against their PubMed abstracts: all are built around a lateral flow strip readout, so none was excluded; 64 also report a second readout (marked in the tables, figures from the second readout are not counted as colorimetric). Reading mode as stated in the abstract: eye 191, device 10, not stated 180, no abstract 1.

## Amendment 2026-11-10 (c): colorimetric-reading check for sections A-D
The same check as for section E was applied to the 272 records of sections A-D against their PubMed abstracts. None was excluded: all describe a strip with a coloured result. Reading mode as stated: eye 93, device 3, eye or device 17, not stated 158, no abstract 1; 16 records with a second readout or a non-colour comparator are marked in the tables, and their non-colour figures are not counted. Corrections made: R02149 (colorimetric LOD 1 ng/mL; 0.1 ng/mL is fluorescent), R04627 (visual figures counted, thermal-contrast reading not counted).

## Amendment 2026-11-10 (d): gold-engineering records moved from section G to A
Author's Au-engineering summary showed that gold-based labels with a second signal (dual-mode) belong with gold engineering when their colorimetric channel is reported. 26 records moved from G to A (R02263, R03396, R04879, R05183, R05756, R05960, R06118, R06367, R06484, R06634, R06797, R06802, R06886, R06972, R07118, R07227, R07366, R07456, R07462, R07583, R07634, R07770, R07942, R08134, R08145, R08616) and R08222 (self-enhancing triplex strip) from G to C. Only the colorimetric channel is counted. Counts now: a 119, c 48, g 76. Pending author decisions: re-screening of 54 records excluded as E3 whose abstracts mention naked-eye or colorimetric reading (03_e3_recheck_candidates.csv); re-inclusion of R07841, R08256 and R02731.

## Amendment 2026-11-10 (e): full texts received for five gold-engineering papers
Full texts read: R05183, R05756, R03396, R08134, R06367 (supporting information not seen). Findings: in each paper the abstract's headline sensitivity belongs to the second channel (SERS or fluorescence); the colour channel gains were 2- to 5-fold (R08134, R06367) or none (R03396, R05756 has no colour comparator; R05183 colour identified 26 vs 11 positives for commercial colloidal gold strips). R05183: abstract states four orders of magnitude between visual and SERS limits; full-text values give about 2.7-3.3 orders. Full-text records in the evidence table: 36 (a 18, b 7, c 6, d 3, e 1, f 1). R06118 full text then received and read: naked-eye limit 160 ng/mL; 20 ng/mL is photothermal and SERS. Full-text records: 37 (a 19, b 7, c 6, d 3, e 1, f 1).

## Amendment 2026-11-10 (f): second group of full texts and two re-inclusions
Full texts read: R06886 (gold nanocrowns), R07634 (gold nanocages), R02731 (RPA70A-conjugated AuNPs, influenza A nucleoprotein) and R08256 (hydrogel-delayed substrate release, SARS-CoV-2 E gene nucleic acid). R02731 (to section a) and R08256 (to section c) were re-included after reading, because the full text names a viral target and gives a colour result; this is a default and is reversible. R07841 (gold nanoantennas, PEDV) and R06797 (Au@Pt nanostars) have not been received. Counts: a 120, c 49, g 76. Full-text records: 41 (a 22, b 7, c 7, d 3, e 1, f 1). Findings: nanocrowns gave about 65-fold (LOD) to 100-fold (visible end-point) colour gain against gold nanospheres in the same study; nanocages 7-fold (1.8 vs 12.5 ng/mL); RPA70A-AuNPs 1000-fold against a streptavidin-AuNP two-step comparator; hydrogel delayed release 25-fold, equal to manual DAB addition.

## Amendment 2026-11-11: third group of full texts
Full texts read: R07841, R06797, R06317 (re-read with tables), R05311 (re-read), R08340. R07841 re-included to section a (naked-eye LOD 1.0 x 10^2 TCID50/mL for PEDV, about 59-fold below a quoted traditional gold LFIA). R06317 discrepancy resolved (mAb sensitivity 90.04% at Ct <= 30 in Table 3, 83.33% across all positives in Table 2; LOD 0.4 vs 1.6 x 10^4 copies/mL). R05311 discrepancy remains (nanoshells in the legend, nanoparticles in the text). R06797 colour LOD 1 ng/mL about 100-fold below colloidal gold strips in the same study. R08340 kept as a development study (not E10). Counts: a 121, c 49, g 76. Full-text records: 44 (a 25, b 7, c 7, d 3, e 1, f 1).

## Amendment 2026-11-11 (b): fourth group of full texts (engineering papers with unstated reading mode)
Full texts read: R03985 (hydrazide oriented coupling, HBsAg), R03607 (EDTA-K2 plasma, SARS-CoV-2 IgM/IgG), R02055 (Zika NS1 protein corona, gold nanostars), R05768 (dengue NS1 preformed coronas), R03110 (probe aggregation, model pairs). Reading modes now stated for these records. Full-text records: 49 (a 30, b 7, c 7, d 3, e 1, f 1).

Fifth group (2026-11-11): R07303 (hollow gold nanoparticles, HIV p24) read in full: about 2-fold higher sensitivity than the commercial Alere HIV-1/2 Ag/Ab Combo (LOD 0.02 ng/mL), read by eye and optical density. Full-text records: 50 (a 31). R02505, R01743, R04920, R05924 and R06939 could not be obtained by the author.

## Amendment 2026-11-11 (c): sixth group of full texts (E3 re-check, first ten, part 1)
Full texts read: R08261, R07970, R07743, R04615, R03509 (all Raman-tagged gold strips for virus targets). All five re-included to section a under the rule used for R07841: include when the full text reports a naked-eye or colour result, counting only the colour channel; the SERS channel is not counted. This reverses, for these papers, the scope-check rule of 2026-11-04 that excluded SERS formats (reversible). Findings: none of the five reports a colour gain against a gold baseline run in the same study; naked-eye limits R08261 1.02 x 10^3 copies/uL, R03509 80 pg/mL, R07743 0.1 ng/reaction, R04615 colour 1.2 ng/mL; R07970 gives no visual value (SERS about 100-fold lower; calculated). Counts: a 126, c 49, g 76. Full-text records: 55 (a 36). Remaining from the first ten: R03979, R01811, R04296, R02597, R05349.

## Amendment 2026-11-12: seventh group of full texts (E3 re-check, first ten, part 2)
Full texts read: R05349, R02597, R04296, R01811, R03979. Re-included to section a (colour channel only): R05349 (cysteamine gold-europium, H5N1; naked eye 10 vs 20 HAU/mL for commercial AuNP, 2-fold), R04296 (SARS-CoV-2 IgM/IgG; line visible at serum 1:100), R01811 (HIV-1 DNA hybridisation; naked eye 80 pg/mL), R03979 (West Nile virus NS1; visual 10 ng/mL). R02597 (H7N9 SERS strip) stays excluded: no naked-eye limit reported, only brown lines shown (reversible). Counts: a 130, c 49, g 76. Full-text records: 59 (a 40). Of the first ten, all received. Remaining gold-related records of the 54 (about seven) to be requested.

Eighth group (2026-11-12): R02071 (KSHV DNA, SERS-LFA) and R07690 (digital SERS, SARS-CoV-2) read in full and re-included to section a; R08470 (E-SERS-LFA, HIV/HBV) read and kept excluded (own strip SERS only; visual limits belong to commercial control kits). Counts: a 132, c 49, g 76. Full-text records: 61 (a 42).

Ninth group (2026-11-12): R06248 (yeast nanofragment nanobody reagent, colorimetric LFA among four platforms) read in full and re-included to section a (binders). R06269 (commercial Wondfo kits, E10) and R05780 (96-well plate multimodal immunoassay, E2) read in full and stay excluded. Counts: a 133, c 49, g 76. Full-text records: 62 (a 43).

Tenth group (2026-11-12): R06172, R02038, R05088, R02458, R06484 (all already in section a, abstract-only) read in full; evidence table text_assessed changed to full text. Findings: gold-enhancement pad 10-fold (naked eye 5.0 to 0.5 ng/mL); 42.7 nm AuNP best of 34-138 nm (no LOD stated); Au/Fe3O4 10-fold over gold (10^4.5 to 10^3.5 EID50); OHT-gold LOD 5 x 10^2-10^3 PFU/test; MagAu(shell) enrichment 100-fold on colour (1 vs 100 ng/mL), 40-fold vs self-made gold strip. Counts unchanged (a 133). Full-text records: 67 (a 48).

Eleventh group (2026-11-12): R02747 (dextrin-capped gold, dengue-1 RNA, NASBA for virus RNA), R08254 (abiotic antibody-mimic hydrogel on gold, SARS-CoV-2 spike) and R06935 (laser-ablated gold, spike: same as commercial gold, 10 ng) read in full and kept in section a. R08549 (gold nanoprism thermoplasmonic LFA) read in full and removed from section a: the viral RNA readout is thermal only, visual limits are for cancer markers (E3). Counts: a 132, c 49, g 76; included 1,116. Full-text records: 70 (a 51).

Narrative rewrite (2026-11-12): Section 3.1 rewritten as a continuous narrative (05_drafts/A_narrative_text_v1.md; with tables A_narrative_v1_with_tables.md/.docx). All 133 DOIs of v16 checked present in text and tables; numbers audited against v16 (only the nanoprism figure removed with the record).

Section B full texts, first group (2026-11-14): R08235 (cellulose nanobeads vs 40 nm AuNP, SARS-CoV-2 N antigen), R03444 (cellulose nanobeads with scFv-Fc, SARS-CoV-2 N), R05828 (latex vs europium fluorescent beads, NAb), R06514 (carbon black vertical flow, IgG vs spike), R08674 (gold vs carbon, PDCoV) read in full; evidence table updated (section b: 12 of 33 read in full). Findings: CNB visual cut-off 0.41 vs 3.28 ng/mL for AuNP in buffer (about 8-fold), and in swabs the highest-Ct positive detected was Ct 26.10 for CNB vs 21.31 for AuNP; latex LoD 7.11 vs fluorescent 1.13 ng/mL with similar sensitivity/specificity vs cVNT; carbon black strip less sensitive than gold for PDCoV (sens 73.2% vs 83.9% vs RT-PCR); carbon black VFIA had no gold comparator in the same study.

Section B full texts, second group (2026-11-14): R02984 (AuNP-polystyrene latex, influenza H3), R07595 (red-dyed latex, SARS-CoV-2 NP), R06924 (polylevodopa, SARS-CoV-2 and influenza A), R07390 (PEG-selenium, SARS-CoV-2 N), R08686 (dual-colour cellulose nanobeads, Nipah NP) read in full. Section b: 17 of 33 read in full. Findings: AuNP-polystyrene latex 64-fold and 16-fold lower visual limit than 10 nm and 30 nm gold strips in the same study (1/16 vs 4 and 1 HAU); red-dyed latex LFIA 10 ng/mL vs ELISA 15 pg/mL with same antibodies; polylevodopa 5 pg/mL, gold comparator in supplementary figures only; selenium 10 pg/mL, 192 clinical samples (overall coincidence 95.83% vs RT-PCR), no gold comparator for LOD; cellulose nanobead Nipah 1 ng/mL, no gold comparator.

Section B full text (2026-11-14): R02468 (Au and Pt nanoparticles on poly(2-vinylpyridine) latex, influenza A antigen) read in full. Naked-eye lowest detectable antigen 6.25 x 10^-3 HAU/mL (Au-P2VP), 2.5 x 10^-2 HAU/mL (Pt-P2VP) against 4.0 x 10^-1 HAU/mL for 30 nm AuNP (more than 64- and 16-fold); extinction per particle about 200x and 100x. Section b: 18 of 33 read in full.

Section B narrative (2026-11-14): 05_drafts/B_narrative_text_v1.md written as publication draft; tables updated for the 11 newly read papers (B_narrative_v1_with_tables.md/.docx). 18 of 33 read in full.

Section C full texts, first group (2026-11-18): R07345 (Au@Pt, SARS-CoV-2 N), R07452 (Fe3O4@MSiO2@Pt, influenza A), R06844 (Fe3O4@MoS2@Pt, SARS-CoV-2 N and H1N1), R08612 (MoS2@Fe3O4/Ag@AP, influenza A), R08107 (rambutan-like Fe-DAu@Ir magnetic nanozyme, SARS-CoV-2 spike) read in full; section c: 12 of 49 read in full. Findings: catalytic step adds 10- to 200-fold on the visual limit within the same strip (10-fold R06844, R08612; 50-fold R08107; 100-fold R07452; 1250-fold R07345); gains against commercial gold are mixed (visual vs calculated LOD): R07452 abstract says 100-fold, text visual values give 1000-fold; R08612 125-fold is calculated LOD vs visual commercial (20-fold on visual); R06844 abstract prints 80 ng/mL where the text gives 80 pg/mL; R08107 555-fold is catalytic LOD vs AuNP-LFA LOD of about 1 ng/mL. Magnetic enrichment adds 10-fold (R08107).

Section C full texts, second group (2026-11-18): R03340 (copper in situ growth, HIV-1 p24), R07397 (Au@Pt@Pd, SARS-CoV-2 N), R06404 (PDA@MnO2 with peptide binder, SARS-CoV-2 spike), R08826 (core-satellite magnetic nanozyme, SARS-CoV-2 and mpox) read in full; section c: 16 of 49 read in full. Findings: Cu deposition over four orders on the visual limit of the same strip (2 ng/mL to 50 fg/mL) and rescued 7 of 7 false negatives of a commercial antibody strip (69 positive, 63 negative blood samples); Au@Pt@Pd catalysis added only 4-fold within the strip, the rest of the 16-fold over gold comes from the probe; PDA@MnO2 catalytic visual limit 10-fold below gold (the 18.7-fold LOD figure in the abstract is not reproduced by the printed LODs); magnetic nanozyme: catalysis 100-fold, enrichment 10-fold more, swabs 89.04% direct and 100% after enrichment.

Section C full texts, third group (2026-11-21): R04697 (copper deposition, SARS-CoV-2 N), R02353 (gold + alkaline phosphatase, potato virus X), R06975 (tyramide colour enhancement, SARS-CoV-2 N), R02484 (HRP/TMB, influenza A and B), R02817 (silver amplification, foot-and-mouth disease virus) read in full; section c: 21 of 49 read in full. Findings: copper deposition 3 orders on certified reference NP only (no real samples); ALP 27-fold (8 to 0.3 ng/mL) with a red-to-violet colour change; tyramide dual-colour 14-fold on LOD and 16-fold on the naked-eye cut-off; HRP/TMB more than 10-fold over gold strips on isolates but clinical sensitivity 58-90% depending on swab type; silver amplification 10-fold on virus titre, 85.4% sensitivity on vesicular epithelium but 46.7% on lesion swabs and 36.8% on saliva (saliva inhibited the untreated test in 51.3%).

Section C full text (2026-11-21): R08222 (self-enhancing triplex strip, in situ gold growth by Au3+/hydroxylamine pads, influenza A, influenza B, SARS-CoV-2) read in full; section c: 22 of 49. Visual LOD 2 vs 10 ng/mL (influenza A), 2 vs 20 ng/mL (influenza B), 0.2 vs 10 ng/mL (SARS-CoV-2) against the conventional strip (5- to 50-fold by the visual figures; the abstract's 5-25-fold refers to calculated LODs); 24 positive swabs; stable 21 days at 45 C. This is gold enhancement in situ, not a nanozyme: it is kept in 3.3 as the single-step counterpart of the Section 3.1 enhancer pad.

Section C narrative (2026-11-21): 05_drafts/C_narrative_text_v1.md written as publication draft; tables updated for the 15 full-text papers read since the last draft (22 of 49 in full). Combined manuscript 3.1-3.3.

Section D full texts, first group (2026-11-21): R02519 (pre-incubation, potato virus Y), R02830 (pipetting-based capture before a commercial strip, influenza A), R06432 (agglutination for large sample volumes, SARS-CoV-2 N), R02324 (magnetic + gold double enhancement, potato virus X), R06089 (electrophoretic LFIA, anti-HBs and anti-HCV serology) read in full; section d: 8 of 99 read in full. Findings: pre-incubation 60-fold as stated (330 to 5.4 ng/mL) but 27.5-fold visual to visual (330 to 12); pipetting capture 100-fold on virus titre, clinical gain partial (6/11 to five additional positives, one false negative, one false positive); agglutination 10-fold for 40-fold volume; magnetic concentration and aggregation 2-fold each, 32-fold together; electrophoretic assembly 1000-fold in serum (625 to 0.6 ng/mL) of which the electrophoretic step itself accounts for 8-fold and removal of background IgG for the rest; diagnostic sensitivity 75% to 98% and 65% to 96%.

Section D full texts, second group (2026-11-21): R05533 (delayed LFIA, hydrophobic barrier), R04042 (dissolvable sugar barriers, nucleic acid), R07133 (water-soluble polymer wall), R06060 (cotton intermembrane), R07816 (vertical flow, Rift Valley fever virus) read in full; section d: 13 of 99 read in full. Findings: flow-delay designs give 2.5- to 9-fold on the LOD (hydrophobic barrier 9.1-fold, sugar barriers 5-fold, cotton intermembrane 2-fold per step, 4-fold in total, polymer wall 5-20-fold vs commercial kits); vertical flow 100-fold in buffer but 2.5-fold in serum (the abstract figure) because the serum background rises.

Section D full texts, third group (2026-11-21): R02057 (magnetic barcode strip, potato virus X), R05235 (osmotic processor, SARS-CoV-2 N and hCG in urine), R05785 (non-powered preconcentrator, SARS-CoV-2) read in full; section d: 16 of 99 read in full. Findings: magnetic concentration lowers cut-offs 3.3- to 6-fold; osmotic processor concentrates about 100-fold from 10 mL, no numeric LOD in text read; non-powered preconcentrator more than 10-fold, tested on one diluted patient sample.

Section D narrative (2026-11-21): 05_drafts/D_narrative_text_v1.md written as publication draft; tables updated for the 13 full-text papers read since the last draft (16 of 99 in full). Combined manuscript 3.1-3.4.

Article body (2026-11-21): Sections 3.1-3.4 assembled as Sections 1-4 of one article body (no introduction, abstract or conclusion), cross-references renumbered, openers unified, closing bridges added; Tables A1a-D4 as supplementary tables. Files: 05_drafts/article_body_sections1-4_2026-11-21.md/.docx and article_sections1-4_with_supplementary_tables_2026-11-21.md/.docx.

## Amendment 2026-11-22: exclusion of nucleic-acid amplification strips (E12)
Author decision: nucleic-acid amplification assays read on a strip (RPA, RAA, MIRA, ERA, LAMP, MCDA, CPA, NASBA, PCR, CRISPR-Cas with target amplification and related) are excluded, because in these assays the improvement in the test comes from amplification and the strip is only the read-out, not from colorimetric detection, although the final reading is colorimetric. New exclusion code E12. Applied to section e (382 records) and to the 107 records in sections g and i whose format names an amplification method (g 21, i 86): 489 records in total, moved to the sheet excluded_E12 of 04_evidence_table.xlsx and marked EXCLUDE (E12) in 03_screening.xlsx; reversible. Kept: hybridisation strips without target amplification in which the colour or flow engineering is the contribution (for example R04042 sugar barriers, R04683 Au@Pt nanorods, R06192 AuPt nanoalloy, R07515 and R08256 delayed substrate release, R05786 nucleic acid sandwich strip, R05788 triplex enhanced detection, R05932 hybridisation chain reaction, R06795 net-shaped DNA nanostructure, R07400 M13 scaffold, R08593 DNA nanostructure, R01811 and R02071 SERS-tagged DNA strips, R08441 bicolour latex duplex LAMP strip), because the evaluated gain is in the colour signal; borderline records to confirm: R02747 (dextrin-capped gold; NASBA used for the virus RNA), R08441, R08748, R07808, R08293, R06049 (antigen LFIA and RPA). The planned Section 3.5 (nucleic-acid amplification) is dropped and the reader/smartphone/AI section becomes Section 5.
