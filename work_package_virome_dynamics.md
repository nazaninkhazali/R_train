# Work package: how the gut virome changes over time in healthy adults

**Draft for supervisor review — v3, 2026-11-08**

One MSc student, 6 months. Metagenomic sequencing is the primary method; a small qPCR panel runs alongside it. Sequencing and bioinformatic analysis are outsourced.

> **How to read this document.** Section 3 holds the scientific questions. Section 4 holds the questions about the samples that must be answered before anything else. Section 7 explains qPCR from the beginning for a reader who has not used it. Items marked **[confirm]** are assumptions I could not verify and that must be checked before this plan is final. Items marked **[verify]** are statements taken from general knowledge that need a literature or supplier source before they appear in a proposal or paper.

---

## 1. Summary

The gut contains a large population of viruses, mostly bacteriophages, together with a smaller number of viruses that infect human cells. How much of this population stays constant in one person over weeks, and how much comes and goes, is not well described.

This project takes repeat stool samples from the same healthy adults and asks how far the viral community in one person changes between samples. The main method is shotgun metagenomic sequencing of DNA and RNA, carried out and analysed outside our laboratory. Alongside it, the student measures a small number of specific viruses by qPCR and RT-qPCR in our own laboratory, which gives absolute quantities, provides a sensitive check on the sequencing, and forms the practical and defendable core of the thesis.

The results speak to a practical problem in faecal microbiota transplantation (FMT): donors are screened at intervals rather than per donation, which assumes that what is found in one sample still holds weeks later.

**Scale.** Approximately 30–40 stool samples, from roughly 8–12 people with at least 3 and preferably 4 samples each.

---

## 2. Background and rationale

### 2.1 Why temporal change matters

Most descriptions of the gut virome are built from one sample per person. Such a study cannot distinguish a virus that is a permanent resident from one that was passing through on the day of collection. Repeat sampling of the same person separates the two, and it is the design used here.

### 2.2 Why this is relevant to FMT

In FMT, stool from a healthy donor is transferred to a patient, often someone who is already unwell or whose immune system is suppressed. Donors donate repeatedly. Testing every donation with a full viral panel is not economically viable, so donor screening is performed at intervals and donations in between are released on the strength of the surrounding screens. **[verify against current FMT guidelines and, if possible, a stool bank's written procedure; intervals of roughly 4–12 weeks are general practice rather than a sourced figure]**

This practice rests on an assumption that has not been measured directly: that viral carriage is a stable property of a person over the interval between two screens. The present project does not test donors, and does not claim to. It measures how far the virome of a healthy adult moves over weeks, which is the quantity that assumption depends on.

### 2.3 Why norovirus is included

Norovirus is a frequent cause of acute gastroenteritis and transmits efficiently. Two properties make it relevant here:

- People can carry and shed norovirus in stool without having symptoms, and shedding can continue for a period after symptoms resolve. In people whose immune system is suppressed, shedding can be prolonged. **[verify; find a reference giving asymptomatic prevalence in healthy adults and typical viral loads]**
- Donor screening in FMT includes a questionnaire about symptoms. A person who feels entirely well but is shedding norovirus is not identified by a symptom question, only by a test.

How often healthy adults without symptoms shed norovirus, and whether that status changes from week to week in the same person, is not well established. Norovirus is therefore kept in the panel.

**A warning that must be understood before the project starts.** Asymptomatic carriage is expected to be uncommon, so the most likely result for norovirus is that no sample is positive. Section 6.3 explains what that result means and why the thesis does not depend on it.

---

## 3. Scientific questions and hypotheses

The overarching question:

> **How much does the gut viral community of a healthy adult change over a period of weeks, and how much of it stays the same?**

Hypotheses and acceptance thresholds are to be fixed in writing, with the supervisor, before any data are examined. Thresholds must not be changed after results are seen.

### 3.1 Primary questions — metagenomic sequencing

| ID | Question | Hypothesis (H1) | Null hypothesis (H0) | Analysis |
|---|---|---|---|---|
| **Q1** | Are two samples from the same person more similar to each other than samples from two different people? | Within-person similarity is higher than between-person similarity | Similarity does not depend on whether samples come from the same person | Similarity between viral profiles for all sample pairs, grouped as within-person or between-person; test on the resulting distributions |
| **Q2** | Does a person's viral community become less similar to itself as the gap between samples grows? | Similarity falls as the interval increases | Similarity does not depend on the interval | Similarity against time between samples, within person |
| **Q3** | What proportion of the viruses detected in a person is present at every time point, as opposed to appearing at only some? | A persistent group is accompanied by a larger group that appears intermittently | Essentially all detected viruses are present at all time points | Classify each virus found in a person as present at all, some, or one time point; report proportions per person |

Q1 and Q2 may already have partial answers in the published literature. **A literature check in the first weeks is required**, both to position the project and to make sure the hypotheses are stated in the direction the field expects.

### 3.2 Secondary questions — qPCR panel

| ID | Question | Hypothesis (H1) | Null hypothesis (H0) | Analysis |
|---|---|---|---|---|
| **Q4** | Can each assay in the panel reliably quantify its target in these stool samples? | Each assay meets criteria agreed in advance: amplification efficiency 90–110%, R² above 0.99, at least 5 orders of magnitude of linear range, and a stated limit of detection | At least one assay does not meet them | Standard curves, replicate testing near the limit of detection, inhibition testing, recovery of a spiked control |
| **Q5** | Does the measured quantity of the common markers (TTV, crAssphage, PMMoV) change within a person between time points by more than the measurement error of the method? | Within-person variation exceeds technical variation | Within-person variation is no greater than technical variation | Variation components estimated from duplicate extractions and repeat samples; within-person coefficient of variation compared against the technical figure |
| **Q6** | How much of the total variation in these markers lies between people rather than within a person? | Between-person variation dominates, so one sample from a person carries information about that person (intraclass correlation above a threshold set in advance) | Intraclass correlation below that threshold | Mixed-effects model with person as a random effect |
| **Q7** | Does detection status (detected or not detected) change within a person between time points, for any target in the panel? | At least some people change status for at least one target | Status does not change within a person | Count of changes, restricted to changes confirmed on repeat testing |

**Q7 requires care.** A result close to the limit of detection can switch between detected and not detected purely through measurement noise. Only a change confirmed by repeat testing is counted as a real change. This rule is written into the analysis plan before any results are seen.

### 3.3 Linking question

| ID | Question | Hypothesis (H1) | Null hypothesis (H0) |
|---|---|---|---|
| **Q8** | Do sequencing and qPCR agree on the same samples? | They agree for abundant targets such as crAssphage and disagree for scarce targets, where qPCR detects what sequencing misses | Agreement does not depend on how abundant the target is |

Q8 is a genuine methodological result in its own right, and it is one of the strongest reasons to run both methods on the same material.

### 3.4 Descriptive observation, not a hypothesis

Norovirus detection is **reported descriptively**: how many people, if any, were positive at any time point, with the viral load and an interval of uncertainty around the proportion. No hypothesis in this project depends on a norovirus-positive sample existing. See section 6.3.

### 3.5 What the answers would mean

- **Within-person similarity high and little change with interval:** a single sample describes a person well over the period studied, which supports the assumption behind interval screening.
- **Clear change with interval, or a substantial intermittent fraction in Q3:** a single sample describes the person on that day rather than over the following weeks, which is the harder case for interval screening and the more interesting finding.
- **Either outcome is publishable**, provided the methods are sound and the measurement error is known. This is why Q4 and Q5 matter: without the technical figure, a stability result cannot be distinguished from an insensitive method.

---

## 4. The samples

**This section contains the most important open questions in the document.** The samples determine what can be asked, and several necessary facts about them are not yet known to me.

### 4.1 What is assumed here

You have told me the samples you will receive **have already been collected and have been frozen for some time**. The plan is therefore written around existing, frozen, repeat stool samples from healthy adults, received from an existing collection. **[confirm]**

### 4.2 Questions that must be answered before this plan is final

Put these in writing to whoever holds the samples. The answer to each one changes the design.

| # | Question | Why it decides something |
|---|---|---|
| 1 | How many separate people are there, and how many samples are there from each? | Repeat samples per person are the whole design. Fewer than 3 time points per person leaves Q2 and Q3 unanswerable. |
| 2 | What are the exact collection dates for each sample? | Q2 is a comparison against the interval between samples. Without dates there is no Q2. |
| 3 | What were the samples collected into? A preservative buffer, such as DNA/RNA Shield, or nothing? | Determines whether RNA is usable, which extraction chemistry applies, and whether RNA sequencing is possible at all. |
| 4 | If a buffer was used: what volume of buffer, and is the mass of stool recorded for each sample? | Without stool mass and buffer volume, results cannot be expressed per gram of stool. Quantities then exist only as presence or absence and as comparisons within one sample set, which weakens Q5 and Q6 considerably. |
| 5 | How was each sample stored, at what temperature, and for how long? Has anything thawed and been refrozen? | Repeated freezing and thawing degrades RNA in particular. A sample that has thawed is a different measurement from one that has not. |
| 6 | How much material remains in each tube? | Sequencing of DNA and RNA plus a qPCR panel plus repeat testing must all come out of one tube. |
| 7 | Were samples processed, homogenised, diluted or pooled before freezing? | A pooled or diluted sample cannot be quantified per gram, and a non-homogenised sample varies from one part of the tube to another. |
| 8 | What is recorded about each donor at each time point: symptoms, gastrointestinal illness in the preceding days, medication (particularly antibiotics), travel, diet changes? | These explain outlying results. Without them, an unusual sample cannot be interpreted. |
| 9 | Does the consent under which these samples were collected cover viral sequencing, removal of human sequences, sending material or data to an external provider, and deposition of sequence data? | This is the one item that cannot be corrected later. |
| 10 | What is written about returning unused material and about authorship or acknowledgement? | Agree before work starts, not after. |

### 4.3 Consequences of the likely answers

- **If RNA was not preserved** — for example, samples frozen without a preservative, or thawed at some point — then RNA sequencing and RT-qPCR for RNA viruses, including norovirus, become unreliable. In that case the project narrows to DNA viruses, and the RNA part must be dropped or replaced by a small, separately collected sample set. **This is the single largest technical risk in the project and should be checked first.**
- **If stool mass is not recorded**, results are reported as relative quantities and as presence or absence, not per gram. Say so explicitly in the thesis rather than quietly reporting a figure that cannot be supported.
- **If fewer than 3 time points per person exist**, Q2 and Q3 fall away, and the project becomes a within-person comparison between two time points, which is a smaller but still valid study.

### 4.4 Study size

Working with 30–40 samples in total:

| Arrangement | People | Samples per person | Total | Comment |
|---|---|---|---|---|
| Preferred | 10 | 4 | 40 | Supports Q1, Q2 and Q3 |
| Acceptable | 12 | 3 | 36 | Q2 rests on fewer intervals |
| Minimum useful | 8 | 4 | 32 | Small, but the design holds |
| Not advised | 20 | 2 | 40 | Q2 and Q3 not answerable |

**The number of samples per person matters more here than the number of people.** A study of this size is descriptive. It is not a prevalence estimate for a population, and the thesis should say so plainly.

### 4.5 Handling in our laboratory

- Keep every sample at −80 °C. We have a −80 °C freezer. **[confirm space for the full set plus aliquots]**
- **Thaw each tube as few times as possible.** On the first thaw, split the material into separate aliquots: one for DNA, one for RNA, one for qPCR, and at least one spare that is never touched. Record every thaw.
- Give every aliquot a label that identifies the person, the time point and the aliquot, and keep a single inventory file that is the only authoritative record.
- Treat the material as potentially infectious and follow local biosafety rules for human stool. **[confirm requirements with the biosafety officer]**

### 4.6 How much material is needed, and what for

The figures below are typical input amounts for commercial stool extraction kits and typical sequencing input requirements. **They must be checked against the specific kit you buy and against the sequencing provider's written requirements before any material is requested. [verify]** They are given so that you can ask for the right amount rather than discover a shortfall halfway through.

#### The principle

Each sample needs **two extractions**, one for DNA and one for RNA, because the two require different chemistry. Each extraction produces a small volume of purified material, called the eluate, and **that eluate is then shared between qPCR and sequencing**. You do not need separate stool for the two methods. What you do need is enough stool that the extraction can be repeated if it fails, and enough left untouched that the sample is not consumed.

#### Per study sample

| Use | If the sample is in preservative buffer at about 1 part stool to 9 parts buffer | If the sample is neat frozen stool |
|---|---|---|
| DNA extraction | about 250 µl of the mixed slurry | about 200 mg |
| RNA extraction | about 700 µl of the mixed slurry | about 200 mg |
| Reserve for one repeat of each, which will be needed for some samples | about 950 µl | about 400 mg |
| Duplicate extractions, on roughly a quarter of samples, to measure technical variation | about 950 µl on those samples | about 400 mg on those samples |
| Untouched archive, never opened | at least 500 µl | at least 500 mg |
| **Comfortable total to request** | **at least 2 ml of slurry** | **at least 1 g** |
| **Absolute minimum that still allows one DNA and one RNA extraction with no margin** | about 1 ml | about 500 mg |

RNA extraction takes more material than DNA because RNA is present in smaller amounts and is more easily lost.

If the samples were collected into a tube of roughly 10 ml, as is common, then **volume is not a constraint** and the question becomes only how much is left after any previous use. If they are neat frozen stool, ask for the mass of each.

#### One detail worth settling early

A single extraction is eluted into a small volume, commonly 50 to 100 µl. Out of that volume you need:

- **For qPCR:** three or four assays, each in duplicate, at roughly 5 µl per reaction, plus a dilution check and allowance for repeats. Realistically 60 to 80 µl of eluate per sample per nucleic acid.
- **For sequencing:** a quantity of material set by the provider, commonly in the range of 100 ng to 1 µg. **[verify]**

Those two demands can exceed one elution. There are two ways round it, and the choice should be made once the provider's requirements are known:

1. **Elute into a larger volume, say 100 µl, and split it.** Simpler, fewer extractions. The cost is that a larger elution is more dilute, which slightly worsens the detection limit.
2. **Two separate extractions per sample per nucleic acid, one for qPCR and one for sequencing.** Cleaner, and the better option if the provider needs a lot of material. The cost is twice the extraction work and twice the stool, which the budget above already allows for.

**Ask the sequencing provider for their input requirements before buying the extraction kit.** This single question determines both the kit and the amount of stool you must request.

#### Total material to request

| Material | Amount | Purpose |
|---|---|---|
| Study samples, 30 to 40 | at least 2 ml of slurry, or 1 g, each | The study itself |
| Positive samples: norovirus, astrovirus, adenovirus | at least 1 ml of slurry, or 500 mg, of each | Validation and detection limit in stool (section 6.4) |
| Stool known to be negative for the panel targets | 15 to 20 g, or the equivalent in slurry | The background for the dilution series, and practice material during training |

The last line is the one usually forgotten and it is the largest amount. (In this table, "the last line" is the negative stool.) Training on this method consumes a great deal of material: a first-time user will perform dozens of practice extractions before the competency sign-off in section 10.2, and every dilution series needs negative stool as its background. For practice material, a commercially sold pooled human stool matrix intended for method development avoids the need for ethical approval altogether and is worth pricing against stool from consenting volunteers. **[verify what products are available]**

### 4.7 Specification: what makes a stool sample usable here

This is the standard against which to judge the samples you are offered. **[verify the specific figures against the extraction kit and preservative manufacturer's documentation before adopting them as acceptance criteria]**

#### The short answer on storage and buffer

There are two acceptable histories for a sample, and they are alternatives rather than both being required:

1. **Mixed into a nucleic-acid stabilising buffer at the moment of collection**, then frozen. Such buffers hold both DNA and RNA stable at room temperature for days to weeks, which is what makes collection at home possible. **[verify the stated stability period for the particular buffer]**
2. **Collected neat, with no buffer, and frozen quickly** — within about two hours — then held at −80 °C and never thawed.

Both work. What does not work is neat stool that sat at room temperature for hours before freezing, or stool held at −20 °C for a long period, or stool that has been thawed and refrozen more than once. In each of those cases DNA may survive well enough while **RNA is likely to be degraded**, and with it norovirus, astrovirus, PMMoV and the RNA sequencing.

So: a buffer is not strictly necessary if the sample was frozen fast and kept at −80 °C. Storage at −80 °C is necessary in nearly all circumstances, and is what I would insist on for anything held long term.

#### Requirements

| Property | What is required | Why it matters |
|---|---|---|
| **Storage temperature** | −80 °C for long-term storage. −20 °C is tolerable for DNA over short periods but not for RNA, and a frost-free freezer is worse than a conventional one because it cycles its temperature deliberately | RNA degrades at higher temperatures, and the RNA viruses are half the panel |
| **Time from passage to preservation** | Into buffer immediately, or into a freezer within about two hours. The actual figure should be recorded | This is the single most important variable for RNA quality, and it is the one most often not recorded |
| **Freeze–thaw history** | Ideally never thawed. Any thaw recorded, with how many | Each cycle degrades nucleic acids, RNA most of all, and changes the measured quantity |
| **Homogenisation** | Mixed thoroughly before being divided into aliquots, and this recorded | Viruses are not spread evenly through a stool. Two portions taken from an unmixed sample can differ substantially, and that difference would appear in the results as change over time when it is nothing of the kind. For Q5 and Q6 this is not a minor point |
| **Mass and volume** | The mass of stool, and the volume of any buffer, recorded for each sample | Without both, nothing can be expressed per gram, and quantities exist only as comparisons |
| **Aliquots** | Already divided into single-use portions, if possible | Avoids thawing the whole sample each time something is measured |
| **Identification** | A unique label on each tube, linked without ambiguity to the person, the time point and the collection date | A sample that cannot be assigned to a person and a date is of no use whatever |
| **Consistency across the set** | **Every sample collected, preserved and stored the same way** | See below. This matters as much as the absolute quality |
| **Remaining material** | At least 2 ml of slurry, or 1 g of neat stool (section 4.6) | Two extractions, a repeat, a duplicate and an untouched archive |

#### Requirements concerning the donors

| Property | What is required | Why |
|---|---|---|
| Health status | Adults without gastrointestinal symptoms at collection. Where symptoms did occur, recorded rather than the sample discarded | The project is about healthy adults; a symptomatic time point is informative if it is known about |
| Antibiotics | No antibiotics in the period before collection, and the period stated. Studies of this kind commonly exclude use within three months **[verify]** | Antibiotics disturb the gut community profoundly and would dominate any change observed over time |
| Repeat sampling | At least 3, preferably 4, samples from each person, with collection dates known | Without repeat samples from the same person there is no study |
| Recorded about each person | Age, sex, and for each time point: symptoms, medication, travel, notable diet change | These are what explain an outlying result |
| Consent | Covering viral sequencing, removal of human sequences, transfer to an external provider, and deposition of sequence data | The one item that cannot be put right later |

#### Why consistency across the set matters so much

If some samples were collected into buffer and others neat, or some frozen within the hour and others the next day, then those samples differ from each other systematically before any biology is involved. Such a difference can appear in the results as a difference between people, or between time points, and there is afterwards no way to separate it from a real one. **A uniform set of slightly imperfect samples is more useful here than a mixed set of individually better ones.** If the set is mixed, record which sample is which, and treat the grouping as something to be accounted for in the analysis.

#### What would disqualify a sample

- The collection date is unknown, which removes Q2.
- It cannot be linked to a person, or it is not known which other samples came from the same person.
- It has been thawed and refrozen repeatedly, or the history is unknown.
- It was pooled from more than one donation, or from more than one person.
- It was stored without buffer at above freezing for an extended period, in which case it may still serve for DNA work but not for RNA.
- Too little material remains (section 4.6).

#### Handling once in our possession

Treat all of it as potentially infectious and follow local rules for human stool. **[confirm with the biosafety officer]** On the first thaw, mix thoroughly, divide into separate aliquots for DNA, RNA, qPCR and an untouched spare, and record the date of every thaw in the inventory.

---

## 5. Sequencing: outsourced, DNA and RNA

### 5.1 What is being asked of the provider

Shotgun metagenomic sequencing of both DNA and RNA from each sample, with bioinformatic analysis. Our laboratory does not build the analysis pipeline, and the student is not expected to.

### 5.2 Our own instrument

The laboratory has an **Illumina MiSeq**. It is not large enough for the main run here. By my arithmetic, 30–40 samples with both DNA and RNA is roughly 60–80 sequencing libraries, and useful depth per library is well beyond what a MiSeq produces in a reasonable number of runs. **[verify the output figures for the specific reagent kits your MiSeq uses]**

A sensible division is therefore:

| Step | Where | Who |
|---|---|---|
| Nucleic acid extraction | Our laboratory | Student, supervised |
| Quality and quantity check of extracts | Our laboratory | Student with facility staff |
| Optional small test run to check library quality before committing to the main run | Our MiSeq | Facility staff |
| Library preparation and main sequencing run | External provider or a partner facility with a larger instrument | Provider |
| Bioinformatic analysis | External provider or a bioinformatics partner | Provider |

The optional MiSeq test run is worth discussing with whoever runs the instrument. It is a way to catch a failed library before paying for the full run, and it keeps the instrument involved in the project.

### 5.3 What to request in writing from the provider

Ask for a quotation and a written specification covering:

1. Input requirements: how much DNA and RNA per sample, at what concentration and purity, and whether extracts from your buffer are acceptable. **Ask this before choosing the extraction kit.**
2. Library preparation method, and confirmation that no whole-genome amplification step is used, since it distorts the relative quantities we want to measure.
3. For RNA: removal of ribosomal RNA, and the method used.
4. Sequencing instrument, read length and the depth delivered per sample.
5. How samples are divided across preparation batches and sequencing runs, and whether our randomisation can be followed.
6. Removal of human sequences, and the method used.
7. Deliverables: raw sequence data, a quality report, the set of viral sequences found per sample, a table of quantities per sample, classification where possible, and the proportion that could not be classified.
8. Identification of likely contaminants using the blank controls we supply.
9. Software names, versions and settings, so that the analysis can be repeated.
10. Data ownership, where data will be deposited, authorship or acknowledgement, and what happens to leftover material.

Obtain at least two quotations. I have not estimated the cost; it depends mainly on sample number, depth and whether RNA is included, and RNA roughly doubles the library count.

### 5.4 Controls that must go to the provider with the samples

These are not optional, and a sequencing run without them is difficult to interpret.

- **At least one blank** per extraction batch: the extraction performed with no stool added. Without blanks, contaminating sequences from kits and reagents cannot be separated from real findings, and low-abundance viruses are exactly where this matters.
- **Two or three duplicate extractions** from the same stool, sequenced as if they were separate samples. These give the technical variation, which is what Q2 and Q3 are measured against.
- **A spiked control organism**, if the provider supports one.

### 5.5 Randomisation

Samples must be assigned to extraction batches, library preparation batches and sequencing runs in a shuffled order, so that one person's samples and one time point do not sit together in one batch. Otherwise a batch effect is indistinguishable from real change over time, which is precisely the thing being measured. Write the scheme down, keep the file, and give it to the provider.

### 5.6 Limitations to state in the thesis

- Sequencing of whole stool under-represents free virus particles compared with methods that concentrate them first. Concentrating particles from already-frozen, preserved stool is difficult. **[verify; ask the provider whether they offer it]**
- Sequencing gives the proportion each virus makes up of the total, not an absolute quantity. A virus can appear to increase because something else decreased. This is a principal reason for running qPCR alongside.
- Many sequences in a gut virome cannot be classified. The unclassified proportion is reported as a result rather than discarded.
- A detected sequence is not evidence of an infectious virus.

---

## 6. The qPCR panel

### 6.1 Why qPCR is run as well as sequencing

This question came up repeatedly, so the reasons are set out plainly:

1. **It gives absolute quantities.** qPCR measures copies per gram of stool, provided the stool mass is known. Sequencing gives proportions. Q5 and Q6 ask whether an amount changed, which proportions cannot answer on their own.
2. **It is more sensitive for scarce targets.** A virus present at a low level can fall below what a sequencing run detects, and asymptomatic norovirus shedding is expected to be low. **[verify typical loads]**
3. **It is the method that screening actually uses.** The practical question behind this project concerns screening tests, which are PCR-based.
4. **It is the student's own work.** Sequencing and its analysis are performed outside, and the results may well arrive late. A thesis must rest on work the student performed and can defend in detail.
5. **It provides the comparison in Q8**, which needs both methods on the same samples.

### 6.2 The panel

Six targets and one control. Validation proceeds in the order given, so that the student learns on abundant targets that give a clear signal before meeting scarce ones that are hard to troubleshoot.

| Order | Target | Nucleic acid | Method | Role |
|---|---|---|---|---|
| 1 | crAssphage | DNA | qPCR | Abundant in most people; confirms the method worked on a sample |
| 2 | Torque teno virus (TTV) | DNA | qPCR | Present in nearly everyone; a marker for change in quantity |
| 3 | PMMoV, a plant virus from diet | RNA | RT-qPCR | Abundant; adjusts for diet and stool consistency |
| 4 | Adenovirus | DNA | qPCR | Shed persistently by some people |
| 5 | **Norovirus GII** | RNA | RT-qPCR | The pathogen of interest; see 6.3. Positive control material available |
| 6 | Astrovirus | RNA | RT-qPCR | Pathogen. Positive control material available |
| — | Mengovirus or equivalent, added to each sample before extraction | RNA | RT-qPCR | Measures how much was recovered from each individual sample |

Adenovirus, norovirus and astrovirus are the three targets for which characterised positive material is expected to be available (section 6.4), which is why astrovirus is now in the panel and **rotavirus has been removed**. Rotavirus would have had to be validated on synthetic standards alone. Norovirus GI, sapovirus and rotavirus are left out to keep the workload achievable, and can be added later.

**Published assays are used; we do not design primers.** For each target, the student finds the original publication describing the primers and probe, checks that the sequences still match viruses in current sequence databases, records the reference in the protocol, and only then orders. Norovirus and rotavirus are the two most likely to need a newer published version, because the circulating strains change. **The candidate assay references I gave in earlier drafts came from memory and are not reliable; finding and confirming them is a first-week task for the student, with help from an experienced colleague.** **[verify]**

**Standards.** Each assay needs a synthetic standard of known concentration to convert the instrument's reading into a number of copies. RNA targets need an RNA standard, not DNA, so that the reverse transcription step is included in the measurement.

### 6.3 Norovirus: what if no sample is positive?

This is the likely outcome and the plan must account for it in advance.

**How likely.** If, say, 5% of healthy people were carrying norovirus at a given time, then with 10 people the chance of finding nobody positive is around 60%. At 3% it is about 74%. These percentages are illustrations, not estimates for your population, and repeat samples from one person count as one person for this purpose. With 8–12 people, finding no positive sample is more likely than finding one.

**What a negative result means.** With no positives among 10 people, the upper limit of what the data can exclude is roughly 26% — in other words, the study would be consistent with carriage anywhere from 0% up to about a quarter of people. That is a weak statement, and it must be reported as such rather than as evidence that carriage does not occur.

**Therefore:**

1. No hypothesis in this project depends on a norovirus-positive sample.
2. The assay's performance is demonstrated regardless. With the positive control material described in section 6.4, this demonstration becomes considerably stronger: the lowest quantity the assay can reliably detect is established **in stool**, not only in clean synthetic template, and can be compared against published asymptomatic loads. A validated assay with a detection limit stated in copies per gram, shown on real stool, is a legitimate and defendable result on its own.
3. The common markers, crAssphage, TTV and PMMoV, supply data from every sample and carry Q5, Q6 and Q7.
4. Norovirus is reported descriptively with its uncertainty, in the terms above.
5. If a positive does appear, confirm it by repeat testing before reporting it, and check against the donor's recorded symptoms for that time point.

Agree this framing with the student and with their examiners at the start, so that nobody expects a positive finding that the study is not designed to produce.

### 6.4 Positive control material: norovirus, astrovirus and adenovirus

Positive samples for these three viruses are expected to be available. This is a significant addition to the plan and changes what the project can claim.

#### What positive material is used for

| Use | What it adds |
|---|---|
| **Validating the whole procedure, not just the reaction** | A synthetic standard shows that the chemistry works on clean template. A real positive stool sample shows that the entire sequence of steps works: breaking the sample open, purifying, converting RNA to DNA, and detecting. These are different claims, and the second is the one that matters. |
| **Establishing the detection limit in stool** | Dilute a positive sample step by step into stool known to be negative, and find the lowest quantity still reliably detected. This gives a detection limit in copies per gram of stool rather than copies per reaction, which was listed as a limitation in section 7.5. It is the most valuable single use of this material. |
| **Showing the assay would catch asymptomatic-level shedding** | This directly addresses the weakness in section 6.3. If the detection limit in stool sits below published asymptomatic loads, a negative result in the study carries real weight instead of being uninformative. **[verify those published loads]** |
| **A positive control on every plate** | At present the plan uses the standards for this. A characterised positive extract is better, because it passes through the same procedure as the samples. |
| **Checking that the published primers match local strains** | If a published assay fails on a confirmed positive sample, either the primers no longer match the circulating strain or something in the procedure is wrong. Either way it must be found during validation, not afterwards. |
| **Partial cover for the RNA risk** | If the study samples turn out to have degraded RNA (section 4.3, the largest technical risk), positive material still allows the RNA assays to be validated and reported. The thesis keeps a chapter. |

#### Rules for using them

1. **They are validation material, not study samples.** They come from people with an infection, not from healthy adults with repeat samples over time. They cannot contribute to Q1 to Q7, and they must not appear in any count of how many people were positive. Keep them in a separate part of the records so that the two are never mixed.
2. **Handle them apart from the study samples.** This is the one real hazard they introduce. A positive stool sample can contain very large quantities of virus, and the study is searching for very small ones. Extract them in a separate session, never in the same batch as study samples, ideally on different days, with a blank run afterwards to show nothing was carried over. Treat them with the same caution as the concentrated standards.
3. **Aliquot on the first thaw.** There will not be much material, and each freeze and thaw costs some of it, RNA most of all.
4. **Find out what is actually in them.** See the questions below.

#### Questions to settle before relying on them

| # | Question | Why |
|---|---|---|
| 1 | Where do they come from, and does their consent or ethical approval permit use as validation material in this project? | Residual diagnostic material from patients usually needs its own approval or a defined anonymisation route. **This must be resolved before the material is used. [confirm]** |
| 2 | Are they quantified, or only recorded as positive? Are diagnostic Cq values available? | A quantified sample can anchor the dilution series directly. An unquantified one can still be diluted, but the series is relative until your own standards place it. |
| 3 | How many samples per virus, and how much material in each? | One sample per virus is enough for a dilution series. Two or three are better, because they show the assay works on more than a single strain. |
| 4 | What are they in: neat stool, a preservative buffer, a transport medium? | If their matrix differs from that of the study samples, dilute them into negative stool of the same type as the study samples, so that the detection limit you report applies to the material you are actually testing. |
| 5 | Is the genotype known, particularly for norovirus? | Useful for interpreting a failed assay as a primer mismatch rather than a procedural error. |

#### Does adenovirus change?

Adenovirus is a DNA virus and is already in the panel, so positive material adds a matrix-based detection limit and a proper positive control, but no new target. Norovirus and astrovirus are the two where it makes the real difference, because RNA targets are the harder ones and the positive material covers the reverse transcription step as well.

#### Also worth asking

If **negative** stool from the same source is available — stool tested for these viruses and found negative — it is exactly what the dilution series needs as a background, and it is also useful practice material during training. Ask for it at the same time.

---

## 7. qPCR explained from the beginning

You said you have not used qPCR and want to know the steps, what is needed, and the limitations. This section is written for that.

### 7.1 What it does

qPCR counts how many copies of one specific stretch of DNA are present in a sample. It works by copying that stretch repeatedly, roughly doubling it each cycle, while an instrument watches a fluorescent signal rise. The more copies there were at the start, the fewer cycles it takes before the signal becomes visible. The cycle number at which that happens, usually written **Cq**, is the raw measurement. A sample with many copies gives a low Cq; a sample with few copies gives a high one.

To convert a Cq into an actual number of copies, you run alongside it a set of standards: samples containing a known number of copies, at a series of concentrations. These produce a straight line relating Cq to copy number, called a **standard curve**, which is then used to read off the unknown samples.

**RT-qPCR** is the same process with one step added at the front. Some viruses, including norovirus, rotavirus and PMMoV, carry their genetic information as RNA rather than DNA. PCR only copies DNA, so the RNA is first converted into DNA by an enzyme called reverse transcriptase. The "RT" refers to that step. It is the same instrument and a similar reagent mix; the difference is that RNA is fragile and more easily lost, so RNA targets are consistently more demanding than DNA targets.

**What makes it specific.** Each assay includes two short pieces of synthetic DNA, the **primers**, which match the two ends of the target stretch, and usually a third, the **probe**, which sits between them and carries the fluorescent dye. Only the intended virus is copied and detected. This is also the method's main restriction: it answers only about the targets you chose in advance.

### 7.2 The steps, in order, for one batch of samples

1. **Thaw and weigh.** Thaw the aliquot. The mass of stool, and the volume of any buffer, must be recorded, or results cannot be expressed per gram.
2. **Add the control organism.** A measured amount of a virus that does not occur in human stool is added to each sample before anything else. Whatever fraction of it is recovered at the end tells you how much of the real target was likely lost along the way, sample by sample.
3. **Break the sample open and purify the nucleic acid.** Stool is shaken violently with small beads to break cells apart — a **bead-beater** — and the DNA and RNA are then purified with a commercial kit. **We do not know yet whether the laboratory has a bead-beater. [confirm]** This step also includes the blank: the same procedure with no stool added, which reveals contamination from the kit itself.
4. **Check what you obtained.** Measure the concentration of the purified material, and for sequencing also its quality.
5. **Set up the reaction.** In a plate of small wells, combine the purified sample with the reagent mix, the primers and the probe. On the same plate go the standards, a well with no sample added at all, and the samples that are being tested in duplicate.
6. **Run the instrument.** Typically one and a half to two hours.
7. **Read and check.** Confirm that the standard curve meets the agreed criteria, that the blank and the no-sample well are clean, and that the duplicates agree. If not, the run is repeated. Early on, this will happen often.
8. **Calculate.** Convert Cq to copies using the standard curve, correct for the recovery measured in step 2 and for the dilution, and express the result per gram of stool.

### 7.3 What is needed

**Equipment**

| Item | Status |
|---|---|
| Real-time PCR instrument capable of RT-qPCR | **[confirm]** |
| Bead-beater | **[confirm — not known]** |
| −80 °C freezer | Available |
| Refrigerated centrifuge | **[confirm]** |
| Instrument for measuring nucleic acid concentration | **[confirm]** |
| Analytical balance reading to 0.01 g | **[confirm]** |
| Calibrated pipettes, including a set used only for standards | **[confirm]** |
| Biosafety cabinet, per local rules for human stool | **[confirm]** |
| Separate working areas, or at minimum separate benches, for reagent preparation and for handling the concentrated standards | **[confirm]** |

**Consumables**: extraction kits for DNA and RNA, enough for the samples plus blanks plus duplicates plus all the practice runs; reaction mixes, including one with reverse transcriptase; primers and probes for six assays; synthetic standards, DNA for DNA targets and RNA for RNA targets; the spiked control organism; plates, seals, tubes and pipette tips.

**People**: this is the item I would raise first with your supervisor. **A student who has never run qPCR needs an experienced colleague available in the laboratory, roughly four hours a week for the first two months and an hour a week thereafter.** The method is not conceptually difficult, but it is unforgiving of small technique errors, and the failures are silent: a contaminated reagent or a mis-set pipette produces plausible-looking numbers that are wrong. Without that person, I would not recommend this plan.

### 7.4 The controls, and what each one is for

| Control | What it catches |
|---|---|
| Standard curve, on every plate | Whether the reaction is working properly, and the conversion from Cq to copies |
| Well with no sample added | Contamination of the reagents |
| Extraction blank, in every batch | Contamination introduced during extraction |
| Spiked control organism, in every sample | How much was lost during extraction, for that individual sample |
| The same sample run at two dilutions | Substances in stool that suppress the reaction |
| Duplicate reactions | The precision of the measurement |
| Duplicate extractions of some samples | The real technical variation, which is what Q5 is compared against |
| A characterised positive sample, on every plate | Whether the assay would in fact have detected a true positive on that run |
| One shared reference sample on every plate | Differences between plates |

### 7.5 Limitations you should know before committing to the method

1. **It detects genetic material, not infectious virus.** A positive result does not establish that a virus could infect anyone.
2. **It only finds what you asked for.** A virus not in the panel is invisible. This is why sequencing is the primary method here.
3. **There is a floor below which it cannot see.** That floor is set by how much stool goes into the reaction. If the stool was collected into a preservative at roughly one part in ten, the material is diluted tenfold before anything begins, and the floor rises accordingly. A negative result means "below that floor", never "absent", and the floor must be stated in copies per gram. The positive control material in section 6.4 is how that floor is measured in stool rather than estimated.
4. **Stool suppresses the reaction.** It contains substances that interfere, which is why the spiked control and the dilution check exist. A suppressed sample can read as negative when it is not.
5. **Viruses change, and primers can stop matching.** A published assay may miss a strain circulating now. Checking the sequences against current databases is a necessary step, most of all for norovirus and rotavirus.
6. **Contamination is the characteristic failure.** The standards contain very large numbers of copies; a trace carried into a sample produces a convincing false positive. Hence the separate benches, the separate pipettes and the blanks.
7. **Results near the floor are unstable.** The same sample can read positive once and negative the next time. This is a measurement property, not biology, and it is exactly why Q7 only counts changes that repeat.
8. **It is slower to learn than it appears.** For a first-time user, a standard curve that meets the criteria for all six assays commonly takes several weeks of repeated attempts. The plan allows for that.

---

## 8. Work plan

**WP-A — Governance and preparation (supervisor and PI; begins before the student arrives)**

- A1 Put the ten questions in section 4.2 in writing to the holder of the samples. **This is the first action and nothing else should precede it.**
- A2 Resolve the ethical and consent position, including whether the existing consent covers sequencing, external providers and data deposition.
- A3 Written plan for what happens if a clinically significant virus is found in material traceable to an identifiable person. Required before the first result exists.
- A4 Confirm the equipment in 7.3, in particular the bead-beater, and arrange the experienced colleague described in 7.3.
- A5 Obtain sequencing quotations, using section 5.3. Do this early: the provider's input requirements determine which extraction kit is bought.
- A6 Agree with the student's programme that the thesis structure in section 11 is acceptable.

**WP-B — Training and assay validation (student, weeks 1–10)**

- B1 Weeks 1–2: biosafety; pipetting checked against a balance; the principles in section 7; find and verify the published assays; read the sample documentation.
- B2 Weeks 3–6: extraction established on practice material; first standard curves; expect repeats.
- B3 Weeks 7–10: all six assays validated; inhibition testing; randomisation scheme written and the random seed stored.
- B4 Weeks 7–10: dilution series of the positive control material in negative stool, giving a detection limit in copies per gram for norovirus, astrovirus and adenovirus (section 6.4). Performed in sessions kept separate from any study material.
- Deliverable: a table of assay performance, including the detection limit in stool for the three targets with positive material; competency sign-off per section 10.2.

**WP-C — Sample handling and extraction (weeks 10–16)**

- C1 Receive and inventory the samples; verify them against the documentation; record any discrepancy.
- C2 First thaw, split into aliquots, including untouched spares.
- C3 Extraction in randomised batches, with blanks, duplicates and the spiked control.
- C4 Quality and quantity checks on extracts; set aside the portions destined for sequencing.
- Deliverable: inventory, extracts, quality records.

**WP-D — Sequencing and qPCR (weeks 14–22)**

- D1 Send extracts, blanks and duplicates to the provider, with the randomisation scheme. **[timing depends on quotation and contract]**
- D2 Optional quality test run on the MiSeq before despatch, with facility staff.
- D3 qPCR for all six targets across all samples, in randomised plate layouts, in duplicate, with the full control set.
- D4 Written rule, agreed in advance, for when a run is repeated and how many repeats are permitted.
- Deliverable: the qPCR dataset with its quality records.

**WP-E — Analysis and writing (weeks 18–26)**

- E1 Analysis plan written out before results are examined; it can be tested on simulated data beforehand.
- E2 Q5 and Q6: variation components and the mixed-effects model, with statistical support.
- E3 Q7: changes in detection status, counting only those confirmed on repeat.
- E4 Q1, Q2, Q3 and Q8 when the sequencing analysis arrives. **If it has not arrived, the thesis is completed without it.**
- E5 Thesis; a manuscript outline for later.

---

## 9. Timeline and decision points

| Weeks | Student | Supervisor and PI |
|---|---|---|
| Before start | — | Section 4.2 questions sent; quotations requested; equipment and mentor confirmed |
| 1–2 | Induction, biosafety, pipetting, assay references | Sample documentation reviewed |
| 3–6 | Extraction established; first standard curves | Sequencing contract; extraction kit chosen to match provider requirements |
| 7–10 | Six assays validated; randomisation written | **Decision 1 (week 8)** |
| 10–16 | Samples received, aliquoted, extracted | Oversee despatch to provider |
| 14–22 | qPCR across all samples; extracts despatched | Weekly review of quality data |
| 18–26 | Analysis; thesis written in parallel | **Decision 2 (week 18)**; thesis supervision |

**Decision 1, week 8 — are the samples usable, and do the assays work?**
If the samples turn out to lack preserved RNA, or lack dates, or lack repeat time points, the design is reduced at this point rather than at the end. Possible reductions: DNA only; two time points instead of four; qPCR and sequencing on fewer samples. If the assays are not yet passing, allow two further weeks, and no more.

**Decision 2, week 18 — has the sequencing analysis arrived?**
If not, the thesis is completed on the qPCR work alone, and the sequencing becomes a later paper. This must be stated to the student at the start, so that the outcome is planned rather than a disappointment.

**Realistic expectations.** For a first-time user, validating six assays in ten weeks is achievable but not comfortable. Roughly a third of bench time should be assumed to go on repeated runs. Externally produced sequencing analysis arriving later than hoped is the normal case, not the exception.

---

## 10. Training, quality and supervision

### 10.1 Order of training

Biosafety and waste handling; pipetting verified by weighing; keeping reagent preparation separate from the handling of concentrated standards; the principles in section 7; extraction on practice material with blanks; then the six assays one at a time.

### 10.2 Competency sign-off before the study samples are touched

The study samples cannot be replaced, so the student works on practice material until all of the following are demonstrated, with the numerical thresholds agreed in advance:

- Three consecutive extraction batches with clean blanks.
- A standard curve for every assay meeting efficiency 90–110% and R² above 0.99 across at least five orders of magnitude.
- Recovery of the spiked control within the agreed range.
- Agreement between duplicate reactions within the agreed limit.
- The student can explain each control in section 7.4 and what it means when that control fails.

### 10.3 Supervision pattern

- First month: ten minutes daily. A student who is stuck for two days without saying so is the most common way this kind of project fails.
- Thereafter: twice-weekly short check-ins; one hour weekly with one decision on the agenda; a half-page written update each Friday with the data attached.
- One protocol document, under version control, with every deviation written down the same day.
- Each task handed over in writing: the goal, the deliverable, how both of you will know it is right, the deadline and a mid-point check, who to ask, and what not to do.

### 10.4 Who does what

| Task | Does it | Answerable for it |
|---|---|---|
| Sample access, consent, ethics | Supervisor and PI | Supervisor |
| Equipment and ordering | PI or laboratory manager | PI |
| Sequencing contract and liaison | Supervisor | Supervisor |
| Finding and verifying published assays | Student | Supervisor |
| Extraction, qPCR, validation | Student | Supervisor, with the experienced colleague |
| Inventory and randomisation | Student, reviewed before use | Supervisor |
| Statistical analysis | Student with statistical support | Supervisor |
| Thesis | Student | Academic supervisor |

With one student there is no cover for illness or absence, so name a deputy for the inventory and freezer records, and keep the documentation good enough that someone else could continue.

---

## 11. Thesis structure

1. Introduction: the gut virome; what repeat sampling adds; the FMT screening context; asymptomatic norovirus shedding.
2. Aims and hypotheses: section 3, as fixed at the start.
3. Methods: samples; extraction; the six assays and their validation; the sequencing arrangement; the analysis plan.
4. Results I: assay performance — Q4. **Available in every scenario.**
5. Results II: quantities and their variation within and between people — Q5, Q6, Q7; norovirus reported descriptively. **Available provided the samples are usable.**
6. Results III: the metagenomic results — Q1, Q2, Q3, Q8. **Conditional on the analysis arriving in time.**
7. Discussion: what it means for interval screening; the limitations of a study this size; what to do next.

Chapters 4 and 5 constitute a complete thesis. Chapter 6 raises it.

---

## 12. Risks

| Risk | Likelihood | What is done about it |
|---|---|---|
| RNA in the stored samples is degraded, so RNA viruses including norovirus cannot be measured | **High, and unresolved** | Establish at Decision 1; the project narrows to DNA viruses. The RNA assays can still be validated and reported using the positive control material |
| Carry-over from the positive control material produces false positives in study samples | Medium | Extracted in separate sessions, never in the same batch; blanks run afterwards; handled like the concentrated standards (section 6.4) |
| Positive control material cannot be used for want of ethical approval | Unknown | Resolve before validation begins; otherwise validation falls back to synthetic standards and the detection limit is reported per reaction, not per gram |
| Stool mass or buffer volume not recorded, so results cannot be given per gram | Medium | Report relative quantities and state the limitation |
| Too few time points per person | Medium | Section 4.2 question 1, answered before the plan is fixed |
| Sequencing analysis arrives after the thesis deadline | High | Thesis rests on chapters 4 and 5 |
| Assay validation overruns | High | Easiest targets first; a third of bench time allowed for repeats; rotavirus droppable |
| No norovirus-positive sample | High, and expected | Section 6.3; no hypothesis depends on it |
| Contamination from standards | Medium | Separate benches and pipettes; blanks in every batch |
| Batch effects mistaken for change over time | Medium | Randomisation written down before any sample is thawed |
| No experienced colleague available | Unknown | **If this is the case, reconsider the plan; see 7.3** |
| Student absent or leaves | Medium | Deputy for records; samples remain frozen; protocol documented |

---

## 13. What I need from you to finalise this

1. **The answers to section 4.2.** Everything else follows from them. The RNA question is the most urgent.
2. **Whether there is a bead-beater**, and the other equipment in 7.3.
3. **Whether an experienced colleague can support the student** as described in 7.3.
4. **Sequencing quotations**, DNA only and DNA with RNA, from at least two providers.
5. **The ethical and consent position**, including external providers and data deposition, **and separately for the positive control material** (section 6.4).
6. **The five questions in section 6.4** about the positive samples, and whether negative stool from the same source can be had as well.
6. **Confirmation that the thesis structure in section 11 is acceptable** to the student's programme, given that chapter 6 is conditional.

---

### A note on what is and is not verified in this document

Statements about FMT screening practice, asymptomatic norovirus shedding, typical viral loads, sequencing depth, MiSeq output, and the suitability of particular kits and methods are drawn from general knowledge and are marked **[verify]**. They need a literature or supplier source before they appear in a proposal, an application or a paper. The assay references given in earlier drafts of this work package were from memory and should not be relied on; locating and confirming them is a first-week task.

Items marked **[confirm]** are facts about your laboratory and your samples that I do not have.
