# Work package 1 (revised): Within-person stability of gut viral markers in healthy adults, and what it means for FMT donor screening

Draft v2, 2026-11-08. Supersedes the cohort-based version. Self-contained: needs no external cohort, no computational partner, and no prior student experience.

**How to read this:** sections 1-2 are the decisions and the questions. Section 3 is the stool specification. Sections 4-8 are the plan. Section 9 is the step-by-step for you. Section 10 is delegation. Anything marked **[verify]** is from general knowledge and must be checked against a source before it goes into an ethics application or a paper.

---

## 1. Decisions taken in this version

| Decision | Reason |
|---|---|
| **No archived cohort material.** We collect our own stool prospectively from consenting local volunteers. | You do not want cohort samples. Also removes access, MTA and funding-gate delays, and lets us choose the storage buffer instead of inheriting one. |
| **No computational reanalysis in this work package.** | It was only needed to choose targets for cohort samples. Targets are now fixed from published, validated assays. Sequencing is an optional stretch, outsourced (section 6, S1). |
| **Recommend 2 MSc students (one DNA track, one RNA track).** One student is possible only with reduced scope (section 5). | One novice doing validation of ~10 assays, two extraction chemistries, ~130 samples, and the analysis in 6 months is not realistic. |
| **Samples are only handled after a training competency gate is passed** (section 8). | Longitudinal samples cannot be recollected. Novice errors on irreplaceable samples are the biggest avoidable risk. |
| **Questions are split into "must answer" (always defendable) and "conditional".** | Healthy adults will mostly be negative for classic enteric pathogens. The thesis must not depend on a positive result. |

## 2. Questions

**Overarching question:** is viral carriage in a healthy adult stable enough over time that a periodic screen can certify donations between screens?

### Must answer (answerable whatever the biological outcome)

| ID | Question | Why it is safe |
|---|---|---|
| **M1** | Can each target be quantified reliably in stool preserved this way? Report efficiency, linearity, LoD/LoQ, inhibition, extraction recovery, and LoD expressed in **copies per gram of stool**. | Depends only on lab work. |
| **M2** | How much do preservation and handling (buffer vs neat frozen; delay at room temperature) change measured quantity? | Depends on 3-5 stool donors and a short experiment. Directly informs how stool should be collected for any future virome study. |
| **M3** | How much does measured load of common markers (TTV, crAssphage, PMMoV, adenovirus if prevalent) vary within a person over weeks, versus between people, and versus technical noise (ICC, within-person CV)? | These markers are detected often enough to give data in most volunteers. |
| **M4** | How often is each pathogen target (norovirus, sapovirus, rotavirus, astrovirus, adenovirus F40/41) detected in healthy volunteers? | A zero is a result: with 0 positives in n samples the 95% upper bound on prevalence is about 3/n (rule of three). Report it that way. |

### Conditional (answered only if enough variation is seen)

| ID | Question | Condition |
|---|---|---|
| **C1** | For targets whose detection status changes over time, what fraction of ever-positive people are negative at a single randomly chosen visit (single-test miss rate), and how does it rise with interval? Method: subsample the weekly series at 1, 2, 3, 4-week intervals; two-state Markov model. | At least ~10 ever-positive people for a target with at least some transitions. Otherwise report as "not estimable at this n" and show what n would be needed. |

**Honest limits to state in the thesis and paper:**
- Healthy volunteers are a surrogate for screened donors, not donors.
- Weekly sampling for 8 weeks supports intervals up to about 4 weeks. It does **not** support the 8-12 week intervals some banks use **[verify actual bank intervals]**.
- TTV, crAssphage and PMMoV are not pathogens. They are model markers for temporal dynamics. Conclusions about pathogens are inference.
- PCR detects nucleic acid, not infectious virus. Positive does not mean infectious. For donor safety this errs on the cautious side. It must still be stated.

## 3. The stool: specification

This is where most virome and qPCR studies quietly lose validity, so it is fixed in writing before recruitment.

### 3.1 What is collected, per volunteer, per week
One stool, **one tube**, plus a short form. Volunteers do home collection (weekly lab visits are too burdensome and cause drop-out).

| Item | Specification | Why |
|---|---|---|
| Container | Commercial stool collection tube with spoon and stabilising buffer (e.g. Zymo DNA/RNA Shield Fecal Collection Tube) **[verify current product and manufacturer's stated room-temperature stability]** | Preserves DNA **and** RNA at home; inactivates virus (biosafety); no cold chain. |
| Amount | Target ~1 g, but **measured**: tubes are weighed empty (with buffer) at the lab before issue and weighed again on return. Stool mass = difference. | Spoon amounts vary several-fold. Without mass, "copies per gram" is invalid and temporal variation is inflated by sampling noise. |
| Dilution | Typically ~1 g in 9 ml buffer (1:10) **[verify for the chosen tube]**. Record exact buffer volume per tube lot. | Needed for the per-gram calculation. |
| Return | Posted or dropped within 7 days of collection, kept at room temperature or 4 °C at home; logged on arrival; **stored at -80 °C** (or -20 °C if -80 unavailable, documented) until extraction. | Fixed rules avoid hidden storage-time effects. Record days from collection to freezer for every sample and put it in the analysis as a covariate. |
| Form | Date and time, Bristol stool score, diarrhoea or GI illness in last 7 days, fever, medication (antibiotics, PPIs, probiotics), travel, unusual diet, any known infection contact. | Explains outliers. A symptomatic week is a data point, not an exclusion. |

### 3.2 Two buffers, the trade-off (decide knowingly)

| | DNA/RNA Shield (1:10) | Neat stool frozen at -80 °C (no buffer) | FMT-bank style (saline ± glycerol, frozen) |
|---|---|---|---|
| DNA and RNA | Both preserved | RNA degrades if thawing/delay before freezing | Often poorly suited to RNA, unknown processing delays |
| Home collection | Easy | Requires cold chain | Not applicable |
| Sensitivity per gram | **Lower**: stool is diluted 10-fold before extraction (see 3.3) | Highest (can extract 100-250 mg directly) | Unknown dilution unless recorded |
| Biosafety | Inactivated, safer | Live stool handled | Live stool handled |
| Infectivity / culture | Impossible | Possible but not planned | Possible |

**Plan:** use Shield tubes for the longitudinal study (it is the only option that works for both nucleic acids at home), and **run M2** to quantify the sensitivity cost against neat-frozen stool on the same stool, so the limitation is measured rather than assumed.

M2 design: 3-5 consenting donors, one fresh stool each, homogenised, split into: (a) Shield 1:10; (b) neat, frozen at -80 °C within 2 h; (c) neat, 24 h at room temperature then frozen; (d) Shield, 7 days at room temperature then frozen (mimics home return). Each in extraction triplicate. Spike a known non-human virus in all (see 3.5). Compare per-gram recovery.

### 3.3 What dilution does to sensitivity (worked example, illustrative numbers)
Assume 250 µl of stool-in-Shield slurry extracted (= 25 mg stool at 1:10), eluted in 50 µl, 5 µl used per qPCR well. Template per well = 5/50 × 25 mg = **2.5 mg stool**. If the assay detects 5 copies per well reliably, LoD is about 2 copies/mg = **~2 × 10³ copies/g stool**. Low-level asymptomatic shedding may be near or below this. Therefore:
- Report LoD in copies/g for every assay, not only copies/reaction.
- Consider larger extraction input or lower elution volume during method development (this is part of M1).
- A negative means "below ~LoD copies/g", never "absent".

### 3.4 If you instead use existing FMT donor or bank stool
You mentioned access to repeat donations from FMT donors. Before relying on them, ask the bank, in writing: how stool is processed (homogenised? diluted in what? glycerol?), volume and mass per aliquot, freeze/thaw history, whether aliquots are pooled or single-donation, donation dates, and whether donor consent covers research use. Without mass or dilution data, per-gram quantification is not possible and only presence/absence plus relative comparisons within the same donor are valid. Treat these as a **bonus dataset**, not the core.

### 3.5 Extraction and controls on stool
- Extract DNA and RNA from the **same tube** in parallel (separate aliquots of the slurry). Bead-beating for lysis; DNase step in RNA extraction **[verify the chosen kits' protocols]**.
- **Extraction control spiked into every sample before lysis:** a non-human virus not found in stool (e.g. Mengovirus, as used in ISO 15216 for foodborne virus detection **[verify]**) to measure per-sample recovery and inhibition. Distinct from the qPCR internal amplification control.
- **Extraction blank in every batch** (buffer only) and a **no-template control on every plate**.
- Stool contains PCR inhibitors (bile salts, polysaccharides). Test eluate dilutions (e.g. 1:1, 1:5, 1:10) on pilot stool and choose the dilution that restores amplification without losing too much sensitivity.
- **Duplicate extractions** of 10% of samples to estimate the technical floor (needed to interpret within-person variation).

### 3.6 Normalisation
Primary result: copies per gram of wet stool. Secondary: dry-weight correction (dry a separate neat aliquot from the M2 donors, and for volunteers use PMMoV as a dietary and consistency covariate) because watery vs formed stool changes wet-weight concentration.

## 4. Target panel

Take **published, validated assays** rather than designing primers. This is the single largest time-saver for novices. Candidate sources below are from memory and **must be verified** before ordering; do not order from this list without confirming sequences in the original paper.

| Target | Type | Role | Candidate assay source **[verify]** |
|---|---|---|---|
| Norovirus GI, GII | RNA | Pathogen | ISO 15216 / Kageyama-type assays |
| Sapovirus | RNA | Pathogen | Oka et al. |
| Rotavirus | RNA | Pathogen | NSP3 assay (Zeng et al.) |
| Astrovirus | RNA | Pathogen | Le Cann et al. |
| Adenovirus (pan, then F40/41) | DNA | Pathogen / persistent shedder | Heim et al.; Jothikumar et al. |
| Torque teno virus (TTV, anellovirus) | DNA | Near-universal; load stability | Ninomiya et al. |
| crAssphage | DNA | Abundant; process positive; model marker | Stachler et al. (CPQ assays) |
| PMMoV | RNA | Diet-derived; normaliser; model marker | Zhang et al.; Haramoto et al. |
| Mengovirus (spike) | RNA | Extraction control | ISO 15216 |

About 10 assays total. **Do not add SARS-CoV-2 to the core panel**; keep it as an optional extra only if a student finishes early.

**Standards:** synthetic DNA fragments for DNA targets; synthetic or in-vitro-transcribed **RNA** standards for RNA targets (DNA standards do not control for the reverse-transcription step). Acceptance: efficiency 90-110%, R² > 0.99, ≥ 5 logs, LoD by replicate testing at low concentration.

## 5. Staffing: how many people

| | Realistic with 1 student | Recommended: 2 students |
|---|---|---|
| Targets | DNA: TTV, crAssphage, adenovirus. RNA: PMMoV + 2 pathogens max | Full panel, split by chemistry |
| Volunteers | ~10 | ~16 |
| Samples | ~80 (10 × 8 weeks) | ~128 (16 × 8 weeks) |
| Question coverage | M1, M2 (narrow), M3, M4 (limited) | M1-M4, C1 conditional |
| Risk | One bad month ends the project | Failure of one track does not end the other |

**Recommended split**
- **Student A, DNA track.** Owns DNA extraction, assays for TTV, crAssphage, adenovirus. Thesis built on M1 (DNA), M2 (DNA targets), M3 (the three DNA markers, within vs between person).
- **Student B, RNA track.** Owns RNA extraction, assays for noro/sapo/rota/astro/PMMoV. Thesis built on M1 (RNA), M2 (RNA stability under preservation, the most informative RNA result), M4 (prevalence with upper bounds), and PMMoV dynamics as the positive-data target.
- **Shared (both, co-authored):** volunteer logistics, sample intake, randomisation, and the C1 miss-rate analysis. Each student writes their own thesis chapters on their own data, so each is defendable alone.

**Risk for B:** pathogen targets in healthy volunteers will mostly be negative. B's thesis is still defensible (M1, M2, M4, PMMoV), but make sure B and their examiners understand beforehand that a well-bounded null is the expected outcome. If you can lawfully obtain pathogen-positive residual diagnostic material for assay validation, it improves M1 for B (needs ethics clearance; otherwise use spiked stool).

**Condition:** at least one person in the lab must already run qPCR and be available as a "bench buddy" for ~4 h/week in the first 8 weeks and ~1 h/week afterwards. If nobody is, the project is high risk regardless of student numbers.

## 6. Work plan

### WP-A: Governance and logistics (PI/coordinator, weeks 1-10)
- A1 Ethics application for the volunteer study (consent, information sheet, data protection, incidental findings plan). Submit in **week 1 or earlier, before students start**. Ethics lead time is the main uncontrollable. Ask your ethics office what they need, and whether method-development stool from consenting lab staff needs approval.
- A2 Decide recruitment source. **Do not recruit your own supervisees or team members** (pressure to consent). Students are not volunteers.
- A3 Written incidental-findings plan: what happens if a clinically significant virus is detected in an identifiable person. Required before the first result.
- A4 Order assays, standards, kits, tubes (lead times 1-4 weeks; see section 10).
- A5 Write the study protocol (this document, fixed) and the data management plan.

### WP-B: Training and method development (weeks 1-10, students)
- B1 Biosafety, pipetting qualification, qPCR theory, contamination control.
- B2 Extraction set-up on surrogate stool (commercial stool matrix or approved consenting donors).
- B3 Assay validation (M1): standards, efficiency, LoD/LoQ, inhibition, spike recovery.
- B4 Preservation experiment (M2) on 3-5 donors.
- B5 Randomisation scheme and plate layout written down (section 8.3).
- **Deliverable:** validated assay set with a performance table; competency sign-off.

### WP-C: Longitudinal collection (weeks 10-18)
- C1 Recruit and consent ~16 volunteers (target ~12 completing); issue pre-weighed kits.
- C2 Weekly kits, reminders, return logging, freezer storage, data entry.
- C3 Pre-specified drop-out rule: a volunteer with ≥ 3 missing weeks is excluded from C1 analysis only.
- **Deliverable:** complete biobank inventory and metadata sheet.

### WP-D: Production testing (weeks 14-22)
- D1 Extract in randomised batches (all time points and people shuffled across batches).
- D2 qPCR, ≥ 2 technical replicates, randomised plate layouts, controls per section 3.5.
- D3 Rerun policy written in advance (what triggers a rerun, how many allowed).
- **Deliverable:** raw and QC-filtered dataset in copies/g.

### WP-E: Analysis and writing (weeks 18-26)
- E1 Pre-specified analysis plan, written before data unblinding (can be tested on simulated data earlier).
- E2 M3: mixed-effects model with person as random effect, ICC per target, within-person CV vs technical floor.
- E3 M4: prevalence with exact confidence intervals; rule of three for zeros.
- E4 C1 (conditional): single-test miss rate by interval via subsampling; two-state Markov model.
- E5 Theses (each student) and a joint manuscript outline.

### Stretch (only if everything is on time; never on the critical path)
- **S1** Outsource shotgun virome sequencing for 2-3 volunteers across time (sequencing facility, no student bioinformatics). Likely needs separate funding and separate library prep consideration given buffer. Optional discussion for a future project.
- **S2** SARS-CoV-2 and extra targets.
- **S3** FMT-bank donations (section 3.4).

## 7. Timeline (26 weeks) and decision gates

| Weeks | Students | Coordinator |
|---|---|---|
| 1-2 | Onboarding, biosafety, pipetting, qPCR theory, read protocol | Ethics submitted, orders placed, bench buddy booked |
| 3-6 | Extraction set-up, first standard curves (expect repeats) | Recruitment materials, consent forms, kit preparation |
| 7-10 | Assay validation, inhibition, M2 experiment | **Gate 1 (week 8):** ethics approved? |
| 10-18 | Weekly sample logging; continue validation/extra runs; practise batch layout | Run recruitment and weekly kit logistics |
| 14-22 | Randomised extractions; qPCR production runs | Weekly QC review |
| 18-26 | Analysis; thesis writing in parallel from week 18 | Analysis plan review; thesis supervision |

**Gates**
- **Gate 1, week 8:** ethics approved and assays passing validation? If ethics is **not** approved, sampling cannot start. Fallback: the thesis proceeds on M1 and M2 only (surrogate stool). That is defendable but smaller; decide at this gate whether to ask for a project extension.
- **Gate 2, week 10:** competency gate passed (section 8.2) and core assays validated? If not, delay volunteer start by up to 2 weeks maximum; beyond that, reduce to 6 weekly samples.
- **Gate 3, week 18:** collection complete? Whatever exists is analysed. No further collection after week 18.

**Realism notes:** the first valid standard curve by novices commonly takes 4-6 weeks including reruns, and extraction optimisation takes longer than planned. About 30% of bench time is budgeted for reruns. If ethics approval arrives later than week 8, the longitudinal part shortens or drops. Do not promise it to the students as guaranteed.

## 8. Training and quality

### 8.1 Training sequence (each step signed off by the bench buddy)
1. Biosafety and waste handling for human stool (local BSL-2 rules **[verify with your biosafety officer]**).
2. Pipetting qualification (gravimetric check).
3. Clean-area discipline: separate pre-PCR (reagent prep, extraction) and post-PCR areas; standards are the main contamination source, so dilute them away from sample prep.
4. qPCR: plate setup, standards, interpreting Cq, melt/amplification curves.
5. Extraction on surrogate stool with blanks.
6. Full assay validation per target.

### 8.2 Competency gate before handling volunteer samples (pre-set acceptance)
- Three consecutive extraction batches with clean blanks (no amplification in blanks, or Cq well above LoQ).
- Triplicate standard curve with efficiency 90-110%, R² > 0.99 for every target in the core set.
- Spike-in recovery within a range agreed in advance (e.g. 50-150%; set from the surrogate runs).
- Replicate Cq spread within agreed limits (e.g. SD ≤ 0.3 Cq at mid-range; agree before measuring).
- Student can explain every control and what failure of each means.

### 8.3 Randomisation (written before any volunteer sample is thawed)
Participants and time points shuffled across extraction batches and qPCR plates, so batch cannot masquerade as time. Keep every sample from one person on the **same plate set where possible** only if the plate layout is balanced across time points. Store the random seed and layout file with the data. Run the same pooled reference sample on every plate as an inter-plate calibrator.

## 9. Step by step: what you do, in order

**Today**
1. Read this document; confirm the decisions in section 1 (especially: 2 students, own volunteers, no cohort).
2. Answer the open questions in section 12 (lab capability, ethics office, budget).

**This week**
3. Contact the ethics office; ask what is required for (a) healthy volunteer stool collection and (b) method development on stool from consenting staff. Start the application using the section 3 specification as the methods text.
4. Confirm a bench buddy and a biosafety contact.
5. Confirm the funding for consumables (section 11) and the student recruitment (1 or 2).
6. Book the -80 °C freezer space (~130 tubes plus M2 aliquots plus backups).

**Before the students arrive**
7. Verify and order assays and standards (section 4), kits, tubes, balance, labels, spike-in virus. Lead times are the hidden delay.
8. Prepare volunteer documents: information sheet, consent, collection instructions (with pictures), form, return instructions, pre-addressed packaging.
9. Prepare onboarding schedule (section 8.1) and the folder structure for data and notebooks.

**Weeks 1-26**
10. Run the weekly rhythm (section 10).
11. Hold the gates (section 7) and decide at each gate, in writing, whether to continue, cut scope, or stop.
12. Review the analysis plan before data are in.

## 10. Delegation

### 10.1 Who does what

| Task | Responsible | Accountable | Support |
|---|---|---|---|
| Ethics, consent, incidental-findings plan | You | You | Ethics office |
| Ordering and lead times | You (delegate to a lab manager if you have one) | You | Students check specs |
| Volunteer recruitment and kit logistics | Student A and B (alternate weeks), starting week 8 | You | Lab manager |
| DNA extraction and DNA assays | Student A | You | Bench buddy |
| RNA extraction and RNA assays | Student B | You | Bench buddy |
| Randomisation and plate layouts | Both, reviewed by you before use | You | Statistician |
| Sample inventory and metadata | Both, one owner per week | You | none |
| Analysis plan and statistics | Both, with an advisor | You | Statistician or biostatistics service |
| Thesis writing | Each student | Their academic supervisor | You |

### 10.2 How to hand a task to someone (use this template every time)
1. **Goal:** one sentence, including why it matters.
2. **Deliverable:** exactly what exists when it is done (a file, a plate, a table).
3. **Acceptance criteria:** how both of you will know it is good (numbers where possible, as in 8.2).
4. **Deadline and check-in date:** a check-in halfway, not only at the end.
5. **Resources and who to ask** when stuck.
6. **What not to do** (e.g. do not change the protocol; do not delete data; do not handle volunteer samples before sign-off).

### 10.3 Weekly rhythm
- Monday 15-minute stand-up: what is planned, what is blocked.
- Friday written update from each student (half page): done, problems, next week. Raw data uploaded.
- Weekly 1-hour meeting with you: one decision per meeting.
- First month: daily 10-minute check-in. A novice stuck for two days without telling anyone is the main failure mode, so ask students to flag any problem within a day.
- Keep a lab notebook and a single versioned protocol; any deviation is written down on the day.

## 11. Resources (categories, to be costed by you)
- Personnel: 2 MSc students (or 1), bench buddy time, statistician hours, freezer and qPCR instrument time.
- Consumables: extraction kits (DNA and RNA, enough for ~300 extractions plus blanks, duplicates, validation and M2), qPCR master mixes (including RT), primers/probes for ~10 assays, synthetic DNA/RNA standards, collection tubes (~150 plus spares), spike-in virus, plasticware, labels, postage.
- Equipment: bead-beater, qPCR instrument, fluorometer or equivalent, analytical balance (0.01 g), -80 °C freezer, biosafety cabinet.
- Volunteer costs: possible small compensation (check what ethics allows).

## 12. Open items I could not resolve from the files

1. **Where and under which ethics office?** Luxembourg was assumed from the earlier conversation. Confirm.
2. **Is there a bench buddy who already runs qPCR?** Determines the viability of this plan for novices.
3. **Instruments:** qPCR machine with RT-qPCR capacity, bead-beater, -80 °C space?
4. **Budget status** and how many students are actually possible.
5. **Thesis rules:** can two students share one dataset and still each be examined individually? Check with their programme.
6. **FMT donor stool:** do you want it as a bonus dataset (section 3.4)? If yes, what does the bank record about processing?
7. **Assay sources in section 4 are unverified.** A literature check by you or a student in week 1 is a necessary step, not optional.
8. Software and thresholds mentioned (kit names, ISO method, acceptance criteria) are general practice and should be rechecked against current versions and your own lab's SOPs.
