# One-page article summary prompt (for the author's use), v2 with reporting checklist

Use one article per run. Keep the heading numbers so rows map into the evidence table.

```
You are summarizing ONE scientific article for a scoping review of colorimetric
lateral flow assays (LFAs) for virus detection. I will paste or attach the full text.

STRICT RULES
- Use only what is written in the article. Never add outside knowledge, never guess.
- If a value is not stated, write "not reported". Do not infer, round, or convert units.
- Copy numbers and units exactly as written (e.g. "10^3.3 TCID50/0.1 mL", "0.25 ug/mL").
- Keep analytical LOD separate from diagnostic sensitivity/specificity.
- Distinguish what the authors measured from what they claim or speculate.
- Quote the page/section/table where each key number appears, e.g. (Table 2), (Results, p. 5).
- If the abstract and the main text disagree, report both and flag it.
- Maximum one page (about 450-500 words). Use the exact headings below.

OUTPUT FORMAT
1. CITATION: first author, year, journal, title, DOI (copy exactly; "DOI not found in text" if absent).
2. TEXT ASSESSED: full text / abstract only.
3. TARGET: virus (species/subtype), host (human / livestock / companion animal / wildlife / fish / shrimp / plant), analyte (antigen / antibody / nucleic acid).
4. ASSAY: format (sandwich / competitive / indirect / nucleic-acid strip / other), amplification step if any (LAMP, RPA, RAA, PCR, CRISPR...), time to result.
5. LABEL AND SIGNAL: material (AuNP shape/size, Ag, Au@Ag, latex, carbon, cellulose nanobeads, nanozyme, enzyme...), how colour is produced, any signal enhancement, whether other readout channels exist (fluorescent, SERS, photothermal) and which one the authors report as colorimetric.
6. READOUT: naked eye / reader / smartphone / AI; software or device used.
7. KEY INNOVATION: 2-3 sentences, what is new compared with the authors' own conventional comparator or prior work they cite.
8. ANALYTICAL PERFORMANCE: LOD value + unit + matrix + how LOD was determined (visual / instrument; replicates; blank-based or lowest detectable dilution). Fold-improvement vs their own conventional comparator, if stated. Cross-reactivity panel (what was tested).
9. CLINICAL / FIELD PERFORMANCE: sample type, setting, n (positives/negatives), reference method, sensitivity (95% CI), specificity (95% CI), agreement/kappa. "no clinical samples" if none.
10. MULTIPLEX: yes/no, targets.
11. STABILITY / USABILITY: storage stability, user training, cost, if reported.
12. LIMITATIONS: those stated by the authors, then any evident gap (small n, spiked samples only, no reference method), labelled "my observation".
13. SECTION FIT: ONE best technology section: (a) AuNP engineering, (b) other coloured labels, (c) catalytic/enzymatic amplification, (d) assay/flow engineering, (e) nucleic-acid amplification + strip, (f) smartphone/reader/AI, (g) multiplex/dual-mode, (h) clinical/commercial test evaluation, (i) veterinary/aquaculture/plant application. Secondary tags if relevant.
14. UNCERTAINTIES: anything ambiguous or that should be verified in the original.
15. REPORTING CHECKLIST (answer Yes / No / Partly / not reported, with page or table; no scoring, no opinion):
   a. Real samples: were patient, animal or field samples tested (not only spiked buffer, spiked matrix or recombinant protein)?
   b. Sample size stated: n positive and n negative given?
   c. Reference method stated (name it: RT-PCR, ELISA, virus isolation, neutralization...)?
   d. LOD definition stated: how was it set (blank + 3 SD, S/N, lowest visible dilution, endpoint)? Name it.
   e. Cross-reactivity tested by the authors on a panel of other agents (not only claimed by a reagent supplier)? List the agents.
   f. Replicates or reproducibility: number of replicates, intra-/inter-batch testing?
   g. Comparator run under the same conditions (own conventional strip or commercial strip tested in the same experiment)?
   h. Storage or stability tested?
   i. Readout: who read the result (instrument, one reader, several readers, blinded or not)?
```
