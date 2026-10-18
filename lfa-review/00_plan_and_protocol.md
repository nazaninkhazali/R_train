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
