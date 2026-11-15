# WP1: Dynamics and diversity of enteric viruses in stools of healthy adults

*Proposal section, draft v1. Background is written separately. Items marked **[confirm]** are facts about your laboratory, samples or contract that I do not have. Items marked **[verify]** come from general knowledge and need a source before submission.*

## 1. Objective and hypothesis

The first work package establishes, in stool from healthy adults, which enteric viruses are present, in what quantity, and how stable this picture is across repeated samples from the same person. It supplies the quantitative baseline for the real viral risk in FMT donor screening, and it characterises and archives naturally positive stool for the later work packages (WP2 and WP3).

Two methods are combined. Targeted PCR gives absolute quantities of selected viruses and is carried out in our laboratory. Shotgun metagenomic sequencing gives the whole viral community, including viruses that no screening panel targets, and is carried out and analysed externally.

> **HYPOTHESIS:**
> The viral content of stool from a healthy adult changes over a period of weeks by more than the technical variation of the methods, so that a single sample describes a person less well than interval-based donor screening assumes.

The hypothesis is tested through the following specific questions. Thresholds are fixed in writing before any result is examined and are not changed afterwards.

| ID | Question | H1 | H0 |
|---|---|---|---|
| H1.1 | Are samples from the same person more similar than samples from different people? (sequencing) | Within-person similarity is higher | No difference |
| H1.2 | Does a person's viral profile become less similar to itself as the gap between samples grows? (sequencing) | Similarity falls with the interval | Similarity is independent of the interval |
| H1.3 | Does the quantity of common markers (TTV, crAssphage, PMMoV) vary within a person by more than measurement error, and how much variation lies between rather than within people? (PCR) | Within-person variation exceeds technical variation; between-person variation dominates (intraclass correlation above a threshold set in advance) | Within-person variation equals technical noise |
| H1.4 | Does detection status of any target change within a person? (PCR) | Some people change status, confirmed on repeat testing | Status never changes |
| H1.5 | Does sequencing find viruses that the PCR panel does not? | Yes, in a fraction of samples | No |
| — | Norovirus, astrovirus, adenovirus | Reported descriptively (number of people positive, load, uncertainty). No hypothesis depends on a positive sample. | |

## 2. Methodology

### 2.1 Samples

The work uses **existing frozen stool from healthy adults, with repeat samples from the same people**: about 30 to 40 samples, from roughly 8 to 12 people, with at least 3 and preferably 4 samples each. **[confirm source, numbers and dates]** Samples per person matter more than the number of people, because the question concerns change within a person. The study is descriptive and is not a population prevalence estimate.

A sample is usable if the following are known. Most of them must be asked of whoever holds the samples, in writing, before the design is fixed. **[confirm]**

1. Collection date of every sample, and which samples belong to the same person.
2. What each sample was collected into (a nucleic-acid preservative or nothing), the volume of any buffer, and the mass of stool. Without the mass and volume, quantities cannot be expressed per gram of stool.
3. Time between collection and freezing, storage temperature, and the number of times the sample has thawed. **RNA does not survive slow freezing or repeated thawing**, and norovirus and astrovirus are RNA viruses. This is the largest technical risk in the work package.
4. Whether each sample was mixed thoroughly before it was divided, and whether any sample was pooled.
5. How much material remains. A comfortable amount is at least 2 ml of preserved slurry or 1 g of neat stool per sample.
6. Health and medication information for each time point, in particular antibiotics and gastrointestinal symptoms.
7. Whether the consent under which the samples were collected covers viral sequencing, removal of human sequences, transfer to an external provider and deposition of sequence data.

Every sample should have been handled in the same way. A uniform set of slightly imperfect samples is more useful than a mixed set of individually better ones, because differences in handling cannot afterwards be separated from real differences between people or time points.

**Positive control material.** Stool positive for norovirus, astrovirus and adenovirus is expected to be available. It is used only for validation: it is not a study sample and does not enter any count of people. It is handled in separate sessions from study samples, to prevent carry-over. Its origin, quantification, volume, matrix, genotype and the permission to use it are confirmed before use. **[confirm]** Stool known to be negative for the targets (15 to 20 g, or the equivalent) is requested at the same time, as the background for dilution series and as practice material.

### 2.2 Sample handling and nucleic acid extraction

On the first thaw, each sample is mixed, divided into single-use aliquots for DNA, RNA and PCR, and a spare that is never opened. Every thaw is recorded in one inventory file, which is the only authoritative record. Human stool is treated as potentially infectious according to local biosafety rules. **[confirm]**

DNA and RNA are extracted from separate aliquots of the same sample, with mechanical lysis by bead-beating **[confirm that a bead-beater is available]**. The extraction kit is chosen only after the sequencing provider has stated its input requirements in writing, since the provider's requirements decide how much material each extraction must yield. Each sample receives a known amount of a non-human virus (for example Mengovirus, as in ISO 15216 **[verify]**) before lysis, to measure recovery sample by sample.

Controls: an extraction blank in every batch, duplicate extractions of about a quarter of the samples to measure technical variation, and a pooled reference sample on every PCR plate. Samples are assigned to extraction batches and plates in a shuffled order, so that one person or one time point never sits together in one batch. The scheme and its random seed are written down and stored before any study sample is thawed. Otherwise a batch effect cannot be told apart from change over time, which is what the work package measures.

### 2.3 Targeted detection by PCR

The target viruses are listed below. Published, validated primer and probe sets are used and no primers are designed. The recruited person finds the original publication for each target, checks the sequences against current sequence databases, and records the reference in the protocol before anything is ordered.

| Order | Target | Nucleic acid | Role |
|---|---|---|---|
| 1 | crAssphage | DNA | Abundant; confirms the method worked on a sample |
| 2 | Torque teno virus (TTV) | DNA | Present in nearly everyone; marker of change in quantity |
| 3 | PMMoV | RNA | Dietary marker; adjusts for diet and stool consistency |
| 4 | Adenovirus | DNA | Persistent shedding in some people; positive material available |
| 5 | Norovirus GII | RNA | Pathogen; positive material available |
| 6 | Astrovirus | RNA | Pathogen; positive material available |
| — | Mengovirus (added before extraction) | RNA | Recovery control |

Norovirus GI, enterovirus and rotavirus belong to the full target list of the project and are added in this order if time allows, or in a later phase. **[confirm with your supervisor]**

**Platform.** The project plan prefers droplet digital PCR for its absolute quantification without a standard curve. If a droplet digital PCR instrument is available, it is used. If only real-time PCR is available, every assay needs a synthetic standard (RNA for RNA targets) and a standard curve on every plate. **[confirm which instrument is available]** Either way, results are expressed in copies per gram of stool, corrected for the dilution in any preservative and for the recovery of the spiked control.

**Validation.** Each assay is validated before study samples are handled: efficiency, linear range and detection limit, inhibition by stool, and recovery. For norovirus, astrovirus and adenovirus, the positive material is diluted step by step into negative stool to find the lowest quantity still reliably detected **in stool**, in copies per gram. This is the most valuable single validation step, because it shows what a negative result in this study can and cannot exclude.

**Limits to state.** PCR detects nucleic acid, not infectious virus. It only finds the targets chosen in advance. Stool contains substances that suppress the reaction, which the recovery control and a dilution check are designed to reveal. Results near the detection limit can switch between positive and negative through noise alone, so only changes of status that are confirmed on repeat testing are counted.

### 2.4 Viral metagenomics (external)

Shotgun metagenomic sequencing of both DNA and RNA is carried out by an external provider **[confirm]**. The laboratory's MiSeq is too small for the main run (it produces far less per run than the roughly 6 Gbp per sample that this kind of study uses **[verify]**), so it is used at most for a small quality test of the libraries before the main run, if the facility agrees.

Before samples are sent, a written specification is agreed with the provider covering input requirements, the library method (without whole-genome amplification), ribosomal RNA removal for RNA, read depth, removal of human sequences, how samples are divided across batches and runs, the deliverables, data ownership and deposition. At least two quotations are obtained. The following controls accompany the samples: an extraction blank for every extraction batch, two or three duplicate extractions, and a spiked control if the provider offers one. The blanks allow contaminating sequences to be separated from real ones, which matters most for low-abundance viruses.

### 2.5 Data analysis

**Bioinformatics.** Analysis of the sequence data is carried out by an external bioinformatician **[confirm who]**, and the recruited person does not build the pipeline. The bioinformatician delivers: the quality report; human sequences removed; the viral sequences found in each sample with completeness estimates; an abundance table per sample; taxonomic assignment with the proportion that could not be classified; contaminants flagged using the blanks; and the software, versions and settings used. The recruited person checks the report against the controls, and compares the sequencing results with the PCR results for the same samples.

**Statistics (PCR data).** Variation within and between people is estimated with a mixed-effects model (person as a random effect), with the intraclass correlation for each target. Technical variation comes from the duplicate extractions. Changes of detection status are counted only when confirmed. For targets with no positive sample, the 95% upper bound on prevalence is about 3 divided by the number of people. With about 10 people this is roughly 26%, which is a weak statement, and it is reported as such. A statistician advises on the analysis plan, and the plan is written before the data are examined.

## 3. Task allocation and supervision

**People.** You are the supervisor. A person is recruited to carry out the laboratory work. **[confirm the position, the length of the contract, and whether the person is an intern or a master student]** The plan assumes six months and no prior experience of PCR or of working with stool.

| Task | Does it | Approves | Deliverable | When |
|---|---|---|---|---|
| Ask the sample holder the questions in 2.1; decide sample set and its size | You | You | Written answers and a decision on the design | Before the person starts |
| Ethics and consent position; incidental-findings plan | You | Ethics office | Written position | Before the person starts |
| Quotations and specification from the sequencing provider; contract with the external bioinformatician | You | You | Signed agreements | Weeks 1 to 8 |
| Equipment check (bead-beater, PCR instrument, balance, −80 °C space) and a named experienced colleague | You | You | Checklist; colleague available | Before the person starts |
| Order assays, standards, kits, spike-in, consumables | You or a laboratory manager | You | Orders placed | Weeks 1 to 4 |
| Training: biosafety, pipetting, PCR principles | Recruited person | Experienced colleague | Sign-off record | Weeks 1 to 2 |
| Find, check and record the published assays | Recruited person | You, with the colleague | Assay reference table | Weeks 1 to 3 |
| Establish extraction on practice material | Recruited person | Experienced colleague | Clean blanks in three batches | Weeks 3 to 6 |
| Validate the assays; detection limit in stool with positive material | Recruited person | You and the colleague | Validation table | Weeks 5 to 10 |
| Randomisation scheme and plate layouts | Recruited person | You, before use | Written scheme, saved seed | Weeks 8 to 10 |
| Inventory, thaw, aliquot study samples | Recruited person | You | Inventory file | Weeks 10 to 12 |
| Extraction and PCR of study samples | Recruited person | You | Raw and quality-checked dataset | Weeks 11 to 20 |
| Dispatch samples and controls to the sequencing provider | Recruited person | You | Dispatch record | After the extraction; set by the provider's schedule |
| Analysis of sequence data | External bioinformatician | You | Deliverables in 2.5 | Set by contract; may fall after week 26 |
| Statistical analysis of PCR data | Recruited person, with a statistician | You | Analysis plan and results | Weeks 18 to 24 |
| Final report | Recruited person | You | Written report | Weeks 22 to 26 |

**Competency gate.** Study samples cannot be replaced, so the recruited person works on practice material until the following are shown, with numerical thresholds agreed in advance: three consecutive extraction batches with clean blanks; every assay meeting the agreed efficiency and linearity (or, for droplet digital PCR, the agreed droplet and replicate criteria); recovery of the spiked control within the agreed range; duplicates agreeing within the agreed limit; and the ability to explain every control and what its failure means.

**Supervision.** A person who has never used PCR needs an experienced colleague nearby, about four hours a week for the first two months and about an hour a week afterwards. Without that colleague, this work package is high risk. In the first month, a daily check of ten minutes; afterwards, twice a week, with one hour weekly and a half-page written update on Fridays with the data attached. A single protocol document is kept under version control, and every deviation is written down the same day. A deputy is named for the inventory and freezer records, since a single recruit leaves no cover for illness. Each task is handed over in writing with the goal, the deliverable, how you will both know it is right, the deadline and a mid-point check, who to ask, and what not to do.

## 4. Timeline

| Weeks | Recruited person | You |
|---|---|---|
| Before start | | Sample questions answered; ethics position; equipment and colleague confirmed |
| 1 to 2 | Training; assay literature | Orders; quotations requested |
| 3 to 6 | Extraction on practice material; first assays | Sequencing specification agreed; bioinformatician contracted |
| 7 to 10 | Assay validation; detection limit in stool; randomisation | **Decision 1 (week 8):** are the samples usable, and do the assays work? |
| 10 to 12 | Inventory, thaw, aliquot | |
| 11 to 20 | Extraction and PCR of study samples; dispatch to provider | Weekly review of quality data |
| 18 to 26 | Statistics; final report | **Decision 2 (week 18):** has the sequencing analysis arrived? If not, the report is completed on the PCR results alone |

At Decision 1 the design is reduced if the samples turn out to lack preserved RNA, dates or repeat samples. The options are DNA targets only, two time points instead of four, or fewer samples. The sequencing analysis may arrive after the person has left, which is the usual case and not an exception. About a third of bench time is allowed for repeated runs.

## 5. Expected outputs and milestone

- A validated set of PCR assays, with detection limits in copies per gram of stool for the three viruses that have positive material.
- A quantitative dataset for healthy adults: viral load, its variation within and between people, and changes of detection status.
- Metagenomic profiles and their comparison with the PCR data (conditional on the external analysis).
- **Milestone D0** (aligned with the project plan): prevalence and load data complete, and an inventory of positive samples characterised and archived for WP2 and WP3. The number of positive samples archived depends on the sample set. **[confirm against the target of 5 to 10 per virus in the project plan]**
- A contribution to the epidemiological article of the project plan.

## 6. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| RNA in the stored samples is degraded | High, unresolved | Check at Decision 1; narrow to DNA viruses; RNA assays still validated on the positive material |
| Stool mass or buffer volume not recorded | Medium | Report relative quantities and state the limitation |
| Too few time points per person | Medium | Ask the sample holder first; reduce to two time points |
| Sequencing analysis arrives late | High | Report does not depend on it |
| No norovirus-positive study sample | High, expected | No hypothesis depends on it; detection limit in stool shows what a negative excludes |
| Carry-over from positive material | Medium | Separate sessions; blanks afterwards |
| Contamination from standards | Medium | Separate benches and pipettes; blanks in every batch |
| Batch effects mistaken for change | Medium | Randomisation written before any sample is thawed |
| No experienced colleague | Unknown | Reconsider the work package |
| Recruited person absent or leaves | Medium | Named deputy; samples remain frozen; documented protocol |

## 7. To confirm before this section is final

1. The ten facts in 2.1 about the samples, in particular whether RNA was preserved.
2. Whether a droplet digital PCR or a real-time PCR instrument is available, and whether there is a bead-beater.
3. Who the experienced colleague is.
4. The recruited person's position, contract length and level of experience.
5. Who the external bioinformatician is, and whether the sequencing provider is the same organisation.
6. Which viruses from the project plan's full list (norovirus GI, enterovirus, rotavirus) your supervisor wants kept in WP1.
7. Ethics and consent, including for the positive control material.
