# Work package 1, single-student version: within-person stability of gut viral markers in healthy adults

Draft v2.1, 2026-11-08. Scaled-down version of `work_package_1.md` for **one MSc student, 6 months, no prior experience**. The stool specification (section 3 of `work_package_1.md`: tube, weighing, dilution, storage, controls, normalisation) applies **unchanged** and is not repeated. Items marked **[verify]** come from general knowledge and must be checked against a source.

---

## 1. What is cut, and why

| Cut from the 2-student plan | Why | Consequence |
|---|---|---|
| Panel reduced from ~10 to **6 assays + 1 spike control** | Each assay costs ~3-4 weeks of a novice's time to validate. | See section 3. |
| Volunteers 16 -> **10** (target 8 completing) | Less to recruit, track and process. | Wider confidence intervals; stated openly. |
| Preservation experiment (M2) reduced to **3 donors, 3 conditions** | Keeps the question, cuts the workload. | Smaller but still publishable comparison. |
| Separate DNA and RNA extractions -> **one co-extraction kit** (DNA and RNA from the same aliquot, e.g. ZymoBIOMICS DNA/RNA Miniprep **[verify suitability for Shield-preserved stool]**) | Halves extractions (~80 instead of ~160 plus blanks). | RNA targets are RNA viruses, so co-purified DNA does not produce signal; run a **no-RT control** on RNA assays to confirm. |
| Miss-rate modelling (C1) becomes **descriptive only** | Too few transitions at n = 10 to model. | Report transition counts and an honest "not estimable at this n". |
| No stretch goals in the core plan | No slack. | The metagenomics follow-up your supervisor suggested is added as a separate, outsourced extension that is **not on the thesis critical path** (section 11). |

## 2. Questions (thesis is defendable whatever the biology does)

| ID | Question | Always answerable? |
|---|---|---|
| **M1** | Can each of the 6 targets be quantified reliably in Shield-preserved stool? Efficiency, linearity, LoD/LoQ in copies per gram, inhibition, extraction recovery. | Yes |
| **M2** | How much does preservation change recovery (Shield 1:10 vs neat frozen; Shield stored 7 days at room temperature)? | Yes |
| **M3** | How much does load of TTV, crAssphage, PMMoV (and adenovirus if prevalent) vary within a person over 8 weeks versus between people versus technical noise (ICC, within-person CV)? | Yes, if samples are collected |
| **M4** | How often are norovirus GII and rotavirus detected in healthy volunteers? A zero is reported with the rule of three (95% upper bound about 3/n). | Yes |
| **Descriptive** | Do detection states change between weeks for any target? Report counts of transitions; no model unless there are enough. | Reported either way |

Same limits as the 2-student plan apply: volunteers are a surrogate for donors; weekly sampling supports intervals up to about 4 weeks, not 8-12; TTV, crAssphage and PMMoV are model markers, not pathogens; PCR detects nucleic acid, not infectious virus.

## 3. Panel

| # | Target | Type | Role |
|---|---|---|---|
| 1 | TTV (anellovirus) | DNA | Near-universal; load stability |
| 2 | crAssphage | DNA | Abundant; process positive; model marker |
| 3 | Adenovirus (pan-adenovirus) | DNA | Persistent shedder in some people |
| 4 | PMMoV | RNA | Diet-derived; normaliser; model marker |
| 5 | Norovirus GII | RNA | Pathogen |
| 6 | Rotavirus | RNA | Pathogen |
| spike | Mengovirus (extraction control, as in ISO 15216 **[verify]**) | RNA | Per-sample recovery and inhibition |

Order of validation: crAssphage -> TTV -> PMMoV (high-abundance targets first so the student learns on assays that give signal) -> adenovirus -> norovirus GII -> rotavirus. Low-abundance pathogens last, because they are the hardest to troubleshoot without positive material.

Dropped to a "later" list: norovirus GI, sapovirus, astrovirus, adenovirus F40/41 typing, SARS-CoV-2.

## 4. Do we need to design primers for each virus?

**No, and a novice should not.** Use published, already-validated primer/probe sets. That is the single biggest time saver in this project.

How it works:
1. **Find the published assay** for each target (the original methods paper, or a standard such as ISO 15216 for norovirus/Mengovirus). The paper gives primer and probe sequences, cycling conditions and the amplicon.
2. **Check it still matches current virus sequences.** Viruses drift. For each assay, align the primers/probe against recent sequences from GenBank (the bioinformatics check takes an afternoon and can be done with a colleague). Norovirus GII and rotavirus are the most likely to need this because of changing circulating genotypes. If there are mismatches at the 3' end of a primer, look for a newer published assay or a minor variant of the original.
3. **Order the oligos** (a TaqMan-style probe assay is the usual format) and **order synthetic standards** built from the published amplicon sequence (synthetic RNA for RNA targets so reverse transcription is controlled).
4. **Validate it yourself in your matrix anyway.** A published assay working in someone else's hands does not guarantee it works in yours, on Shield-preserved stool, on your instrument. This is exactly what M1 is.

When design from scratch is justified: only if no published assay exists for the target, or if in-silico checking shows the published set misses current strains and no updated version exists. In that case ask a bioinformatician or an experienced colleague to help, and budget an extra 3-4 weeks. This plan is built so that **no target requires it**.

I wrote candidate sources for each assay in section 4 of `work_package_1.md` from memory; they are unverified. Week 1 task for the student (with the bench buddy): find each original paper, confirm the sequences, record the reference in the protocol. I can search PubMed to help with that.

## 5. Work plan (single student)

**WP-A, coordinator (you), before and during weeks 1-10**
- Ethics application for volunteer stool collection, submitted before the student starts. Clarify whether stool from consenting lab staff for method development needs approval.
- Written incidental-findings plan.
- Orders: oligos, standards, kits, tubes, spike virus, balance, labels. Allow 2-4 weeks.
- Do not recruit your own team as volunteers. The student is not a volunteer.
- **Write the consent form and ethics application so they already cover metagenomic sequencing** (human DNA in stool, removal of human reads, deposition of data, sending samples to an outside company). Adding this later may need an amendment, and volunteers cannot be re-consented retroactively for stored samples. See section 11.

**WP-B, student, weeks 1-10: training and validation**
- Weeks 1-2: biosafety, pipetting qualification, qPCR theory, contamination control, read the protocol and each assay paper.
- Weeks 3-6: extraction on surrogate stool; first standard curves (expect repeats).
- Weeks 7-10: validation of all 6 assays (efficiency, R², LoD, inhibition); M2 experiment on 3 donors; randomisation scheme written.
- Deliverable: validated assay table + competency sign-off.

**WP-C, weeks 11-18: collection**
- Recruit ~10 volunteers; issue pre-weighed kits; weekly logging; freezer storage; metadata sheet.
- If the start slips, **cut to 6 weekly samples** rather than extend (decide at Gate 2).

**WP-D, weeks 15-21: production**
- Randomised extraction batches of ~24 (including blanks, spike, duplicates); qPCR in 2 technical replicates; fixed rerun policy.
- About 80 samples + duplicates + validation material is roughly 4 extraction batches and a few plate runs per assay; the limit is learning speed, not throughput.

**WP-E, weeks 19-26: analysis and thesis**
- Pre-specified analysis plan (written before the data are in; test it on simulated data).
- Mixed-effects model for M3 (person as random effect), ICC per target, prevalence with exact confidence intervals for M4.
- Write results chapters as data arrive; thesis draft by week 24.

## 6. Timeline and gates

| Weeks | Student | You |
|---|---|---|
| 1-2 | Onboarding, biosafety, pipetting, read assay papers | Ethics submitted; orders; bench buddy booked |
| 3-6 | Extraction set-up; first curves | Consent forms; recruitment plan; kit preparation |
| 7-10 | Validation; M2 experiment; randomisation plan | **Gate 1 (week 8):** ethics approved? |
| 10 | Competency gate | **Gate 2 (week 10):** start sampling or reduce to 6 weeks |
| 11-18 | Weekly sample logging; continued assay work | Volunteer logistics (shared with student) |
| 15-21 | Randomised extractions; qPCR | Weekly QC review |
| 19-26 | Analysis; thesis | **Gate 3 (week 18):** collection stops; analyse what exists |

**If ethics is not approved by week 8:** no volunteer sampling. The thesis becomes M1 + M2 on surrogate stool (assay validation and the preservation comparison). That is defendable but smaller; this is the main risk in the whole plan, so start the application now.

## 7. Training and competency gate

Same sequence as the 2-student plan. Before touching volunteer samples the student must show (acceptance numbers agreed in advance with the bench buddy):
- Three consecutive extraction batches with clean blanks.
- Standard curves for all 6 assays: efficiency 90-110%, R² > 0.99, ≥ 5 logs.
- Spike recovery within the agreed range.
- Replicate Cq spread within agreed limits.
- Ability to explain each control and what its failure means.

Randomisation of people and weeks across extraction batches and plates is written down and the seed saved before the first volunteer sample is thawed. A pooled reference sample goes on every plate as an inter-plate calibrator.

## 8. Delegation for one student

| Task | Responsible | Accountable | Support |
|---|---|---|---|
| Ethics, consent, incidental findings | You | You | Ethics office |
| Ordering | You or lab manager | You | Student checks specs |
| Finding and confirming published assays | Student | You | Bench buddy (sequence check) |
| Extraction, qPCR, validation | Student | You | Bench buddy (heavy early, light later) |
| Volunteer kits and weekly logging | Student, with lab manager backup | You | Lab manager |
| Analysis plan and statistics | Student | You | Statistician or biostatistics service |
| Thesis | Student | Academic supervisor | You |

With one student there is no backup for illness or a bad month, so:
- Name a **deputy** who can do the weekly kit logistics and freezer logging.
- Keep one written, versioned protocol; every deviation noted the same day.
- Rhythm: daily 10-minute check-in in month 1, then twice a week; one-hour weekly meeting with one decision on the agenda; Friday half-page written update; the student flags any problem within a day.
- Use the six-line hand-over template from `work_package_1.md` section 10.2 for every task.

## 9. Risks specific to one student

| Risk | Likelihood | Mitigation |
|---|---|---|
| Ethics late | High | Submit before week 1; fallback is M1 + M2 only |
| Assay validation takes longer | High | Order of validation easiest-first; 30% rerun allowance; 6-week fallback sampling |
| Student ill or leaves | Medium | Deputy for logistics; frozen samples stable; documented protocol |
| All pathogen targets negative | High (expected) | Framed as M4 with upper bounds; thesis does not depend on positives |
| Volunteers drop out | Medium | Recruit 10 for 8 completers; per-person analysis uses available weeks |
| Contamination from standards | Medium | Separate rooms/benches; dilute standards away from sample prep; blanks every batch |

## 10. Open items

1. Is a qPCR-experienced bench buddy available (about 4 h/week early, 1 h/week later)? If not, risk is high.
2. Ethics office and its usual timing.
3. Instruments: RT-qPCR-capable machine, bead-beater, balance, -80 °C space.
4. Does the co-extraction kit work on Shield-preserved stool? Check the manufacturer's information and run a small test in weeks 3-4.
5. All assay sources, the ISO method reference and acceptance criteria need verification against the original papers and current standards.
6. Whether the MSc programme allows an experimental thesis of this kind with a sampling window.

## 11. Extension: metagenomics by a third party (suggested by your supervisor)

**Status:** this was not in the core plan above. It is added here as an optional extension. It answers a different question from the qPCR work: **how does the whole viral community (diversity), not just six targets, change over time within a person?** The qPCR data tell you how much of six known viruses is there. Metagenomics tells you which viruses are there, without choosing in advance.

**The thesis does not depend on it.** Sequencing results come back after the student has finished, so the thesis must be defendable on sections 2-9 alone. Treat metagenomics as the follow-up paper or a second project.

### 11.1 What must be decided *now*, before any volunteer is recruited
1. **Consent and ethics.** The consent form must say that stool DNA/RNA may be sequenced by an external company, that human sequences will be removed before analysis or deposition, and how data are stored and shared. This is the one part that cannot be fixed later.
2. **Which samples will be sequenced.** Keep a **spare, unthawed extraction or tube** for each sequenced sample so qPCR does not use up the material.
3. **Extraction suitable for sequencing.** The co-extraction kit in section 1 may or may not meet the sequencing company's DNA and RNA quality and quantity needs. Ask the company for its input requirements in writing (amount, purity, fragment size, what buffer is acceptable) before choosing the kit. **[verify]**

### 11.2 Which samples to sequence
Sequencing every sample is probably unaffordable. Suggested choice, to be decided after the qPCR data are in: **3-4 volunteers, all 8 weekly samples each (24-32 samples)**, chosen to include volunteers with large qPCR changes and volunteers with stable qPCR profiles. Always include:
- **Extraction blanks** (at least one per extraction batch of sequenced samples). Without them, contaminant DNA cannot be separated from real viruses.
- **A mock or spike-in control** if the company offers it.
- A few **duplicate extractions** from the same stool to estimate technical variation.

### 11.3 What kind of sequencing
- **DNA metagenome (shotgun)** covers DNA viruses and phages, which are most of the gut virome.
- **RNA** viruses need an RNA-based method (metatranscriptome or total RNA-seq) and a further extraction and cost. Ask the supervisor whether the RNA part is wanted.
- Bulk stool metagenomes under-represent free virus particles compared with virus-particle-enriched libraries. That enrichment is difficult on stool already in DNA/RNA Shield. Ask the company whether they can do it, and expect the answer may be no. **[verify]**
- Sequencing depth: set with the company. For orientation, a published study on Luxembourg stool used about 6 Gbp per DNA sample, and far more for RNA (this comes from the earlier project notes, not re-checked). **[verify]**

### 11.4 What the third party should deliver
Write this into the order or collaboration agreement:
1. Raw reads and a sequencing quality report.
2. Human reads removed, with the method stated.
3. A table of viral sequences per sample (assembled viral contigs or species-like units), with completeness estimates.
4. An abundance table per sample, taxonomy where possible, and the share of sequences that cannot be classified.
5. Contaminants flagged using the sequenced blanks.
6. The software, versions and settings used, so the analysis can be repeated.
7. Agreement on who owns the data, where it is deposited, and authorship if the company contributes analysis.

The student does **not** build the analysis pipeline. The student's role is choosing samples, shipping them, checking the report, and comparing the results with their qPCR data.

### 11.5 What this adds scientifically
- **Concordance:** does metagenomics detect the same targets (crAssphage, TTV, adenovirus, PMMoV) at the same time points as qPCR, and where does it disagree? Expect qPCR to be more sensitive for low-abundance viruses.
- **Within-person diversity over time:** how much of a person's viral community stays and how much comes and goes week to week, compared between volunteers. This directly addresses the supervisor's idea.
- **Targets for future screening panels:** viruses that appear in many people but are not in the current six.

### 11.6 Limits to state
Only 3-4 volunteers means this is descriptive, not a population estimate. Contamination and low-input samples are the main technical risk. A metagenome shows viral sequences, not infectious virus.

### 11.7 Timing and cost
- Ask the company for a quote and lead time **in weeks 1-4**, so that the extraction method and consent are right.
- Send samples around **weeks 20-22**, once qPCR has shown which volunteers to choose. Results may arrive after week 26.
- Cost depends heavily on the number of samples, depth, and whether RNA is included. I have not estimated it. Get at least two quotes.
