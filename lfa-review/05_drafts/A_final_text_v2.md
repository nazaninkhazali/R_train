# Part A (working text v2): gold-nanoparticle engineering

Working text, 2026-11-05. Text focuses on the technologies and how they connect; all numerical detail is in the tables. † = read in full; all other rows are abstract only (NR = not reported in the abstract). Every DOI cited in the text appears in a table and in the evidence table. Wording and length will be adjusted when the whole review is assembled.

# 3.1 Gold nanoparticle engineering: making the standard colorimetric label easier to see

## 3.1.0 Why the label limits sensitivity, and how this section is organised

In a colorimetric lateral flow immunoassay (LFIA) the result is the colour that builds up at the test line. How sensitive the strip is therefore depends on two things: how much label the sandwich captures, and how strongly each captured particle changes the white membrane. Gold nanoparticles (AuNPs) became the default label because they absorb visible light strongly, are easy to make, and are easy to couple to antibodies (DOI: 10.1016/j.bios.2022.114094). Their weakness is the high limit of detection (LOD) that results when only a few particles reach the line (DOI: 10.3390/bios11070229).

The engineering work reviewed here can be read as a sequence of increasingly deep changes to the standard strip. The first group of studies keeps the particle and tunes its size and surface (section 3.1.1). The second leaves the particle unchanged and makes the captured gold more visible after the immunoreaction (3.1.2). The third replaces the sphere with a structure that has a larger optical effect per particle (3.1.3). The fourth changes what the particle carries, replacing the antibody with another binder (3.1.4). The fifth changes the way the signal is read, using scattering instead of absorption (3.1.5). Each step addresses a different bottleneck: antibody activity, signal size, particle optics, binder quality and background. Section 3.1.6 deals with conventional strips that apply none of these steps, and 3.1.7 summarises what the evidence allows us to say.

Numerical details (LOD with units, matrix, comparator, diagnostic accuracy, readout) are given in Tables A1a-A1e, not in the text. The text concentrates on how each approach works, what it changes and what it costs. Papers read in full are marked † in the tables; every other statement rests on an abstract. The section covers 97 included records, 93 of them from 2015-2026.

## 3.1.1 Getting the standard particle right: size and surface

The first design question is the particle itself. Large AuNPs carry more colour, but they also move more slowly through the membrane and may not reach the test line in useful numbers (DOI: 10.3390/bios11070229; DOI: 10.1038/s41467-025-58663-z). Studies that vary particle diameter treat this trade-off directly. In an early plant-virus study the LOD depended clearly on particle size (DOI: 10.1007/s00216-012-5985-8). Later work built HBsAg and dengue NS1 strips around size-controlled or large (80 nm) particles (DOI: 10.3390/s16122154; DOI: 10.3390/diagnostics16030395).

What sits on the gold matters as much as the gold itself. Oriented conjugation lets an antibody bind through a defined site and reduces the amount of antibody needed (DOI: 10.1016/j.aca.2021.338623). An additive that chelates the gold surface (EDTA-K2) improved a SARS-CoV-2 antibody test without raising false positives (DOI: 10.2147/ijn.s281594). Studies of the protein corona and of the aggregation state of the probe show that the layer of adsorbed protein changes how the probe binds in NS1 sandwich assays (DOI: 10.1021/acs.bioconjchem.6b00523; DOI: 10.3390/pharmaceutics14112439; DOI: 10.1021/acsami.0c08628).

These studies are valuable because they explain why nominally identical strips perform differently. Most of them, however, are mechanistic, and their abstracts report few diagnostic data (Table A1a). Even a well-tuned conventional strip reaches a limit, which leads to the next approach: making more of the gold that has already been captured.

## 3.1.2 Making more of the captured gold: enlargement and amplification

After the sandwich has formed, the particles at the test line can act as seeds. Depositing more metal on them enlarges them, and larger or more irregular particles colour the line more strongly (DOI: 10.3390/bios11070229). Panferov and colleagues compared silver enhancement, a new gold-after-silver step based on galvanic replacement, and gold enhancement on one strip format with the same antibodies and the same AuNPs. Gold enhancement gave the lowest LOD, by more than two orders of magnitude over the unenhanced strip, and used stable reagents, but it brought nonspecific colouring and needed an optical instrument to reach the lowest value (DOI: 10.3390/bios11070229). The pattern repeats in other studies: growing 20 nm particles into much larger ones after the assay, which in potato leaf extracts turned most of the conventional strip's false negatives into positives (DOI: 10.1007/s00604-018-3052-7), a self-enhancement design (DOI: 10.1016/j.snb.2023.133898), and gold nanoflowers combined with gold staining, which were tested in buffer and artificial saliva only (DOI: 10.1007/s00604-024-06502-1). Each lowers the LOD within its own strip format. Each also adds a step beyond the conventional run, and the lowest values often rely on calibration or a reader.

A different route is to build up the label at the line instead of growing it. Layer-by-layer assembly of AuNPs through biotin-streptavidin binding, driven by electrophoresis, lowered the LOD of an HBsAg strip by more than 60-fold (DOI: 10.1002/anie.202215548). The design is a two-stage workflow: the conventional strip is read first, and enhancement is applied only to samples that look negative or weakly positive. On 118 clinical samples this raised diagnostic sensitivity against a laboratory chemiluminescent assay without changing specificity, but it needs a small power supply, a holder and an extra reagent step (DOI: 10.1002/anie.202215548). In antibody (serology) strips, a complex of antibody-gold and antigen-gold conjugates increased the test-line signal over antigen-gold alone, and brought the visual limit to the cut-off of the reference ELISA (DOI: 10.1002/gch2.202200008).

The trade-off in this group is consistent. The gains are real and often large, but they are paid for with extra reagents, extra time, more background or dependence on instrument reading (Table A1b). That limits their use where the strip must work with no equipment. The alternative is to design a better particle in advance.

## 3.1.3 Better particles: clusters, dimers, shells and composites

The optical response of a particle depends on its size, shape, composition and the distance to its neighbours. Several groups exploit this to give each captured particle more effect on the line.

Clusters add absorption by putting several particles at each binding event. The difficulty is plasmon coupling: when particles sit closer than about 10 nm the absorption shifts towards the near-infrared and the visible colour fades (DOI: 10.1016/j.bios.2022.114094). Streptavidin-core clusters held about 15 nm apart by biotinylated antibodies avoid this and keep the red colour, and the 40-40 cluster outperformed single particles, whereas the 40-15 cluster did not (DOI: 10.1016/j.bios.2022.114094). Gold dendrimer nanochains with a red-to-blue shift have also been tested (DOI: 10.1039/c7tb01394a). Core-satellite SiO2@Au particles, in which a silica core carries many small gold satellites, lowered the LOD by two orders of magnitude against 40 nm gold colloids with the same assay, although only recombinant protein and inactivated culture virus were tested and the visual limit was much higher than the calculated LOD (DOI: 10.1021/acsami.2c13303).

Dimers use the opposite logic. Two particles joined with a sub-nanometre gap couple strongly and show two plasmon peaks, giving a stronger signal than single spheres, and they gave a clearly lower naked-eye LOD than a commercial strip for porcine epidemic diarrhea virus, with full agreement with RT-PCR on faecal samples (DOI: 10.1007/s00604-023-06013-5). The authors note that dimers are hard to prepare at scale and that their long-term stability has not been tested (DOI: 10.1007/s00604-023-06013-5).

Hollow alloy shells widen the absorption band. Silver-rich Ag-Au nanoshells have two plasmon peaks and a larger integrated absorbance than same-size AuNPs. Used as label in a bovine viral diarrhea virus strip, they gave a lower visual LOD than the authors' own AuNP strip with the same antibodies, and good agreement with a commercial ELISA on field samples (DOI: 10.1007/s00604-026-08241-x).

Composite particles combine gold with a second material, for example a magnetic Fe3O4 core used as a performance enhancer (DOI: 10.1039/c8ra00185e) or magnetic-gold nanostars, which add magnetic pre-concentration to a spiked plasmonic shell and gave a very large gain over the authors' own gold-sphere strip in buffer and spiked serum, but require a magnet and a pre-incubation step and were not tested on patient samples (DOI: 10.1021/acsami.5c21544). One study used two-wavelength imaging of composite particles, which gives a large gain but depends on an imager rather than the eye (DOI: 10.1016/j.bios.2022.114133).

The strongest evidence in this group comes from papers that compare their particle with a conventional strip made with the same antibodies (clusters, shells). Others compare with commercial strips, which mixes label and antibody effects (dimers), or have been tested only in buffer (nanostars) (Table A1c). All of these designs still read absorbed colour against a white membrane. One study changes that.

## 3.1.4 Replacing the antibody on the particle

A brighter label cannot help if the binder is weak. A parallel line of work therefore replaces the conventional antibody with a binder that is smaller, more stable or easier to produce.

Nanobodies are small single-domain fragments. In a SARS-CoV-2 spike S1 strip, a nanobody-gold detector with an ACE2-gold capture probe lowered the LOD compared with a monoclonal-antibody version of the same strip, and gave higher sensitivity at low viral loads in saliva (DOI: 10.1038/s41598-023-37347-y). The abstract and the results text disagree on the comparator's sensitivity, so this comparison needs checking against the source tables (DOI: 10.1038/s41598-023-37347-y). Other nanobody designs, including multivalent and Y-shaped assemblies, have been reported for SARS-CoV-2 and chikungunya virus, and a nanobody strip has been used on human norovirus outbreak specimens (DOI: 10.1021/acs.analchem.4c00509; DOI: 10.1039/d4nr02762k; DOI: 10.1039/d5nr02568k; DOI: 10.3390/bios16020132; DOI: 10.3389/fimmu.2025.1707358; DOI: 10.1128/msphere.00219-16).

Aptamers are chemically synthesised and can be produced more reproducibly and cheaply than antibodies (DOI: 10.3390/molecules29081776). They can be used in sandwich or competitive formats. A competitive aptamer strip for SARS-CoV-2 spike protein on food packaging used an aptamer chosen for broad binding to variant spike proteins, but its sensitivity was lower than other methods and it was tested only with recombinant protein (DOI: 10.3390/molecules29081776). Other aptamer strips were evaluated with inactivated virus or spiked samples (DOI: 10.1002/anie.202107730; DOI: 10.1021/acs.analchem.2c00554; DOI: 10.1186/s12951-023-02191-9).

Further binders include sialic-acid glyconanoparticles that recognise spike through glycans, a lectin for severe dengue, and a miniprotein binder aimed at variants of concern (DOI: 10.1021/acscentsci.0c00855; DOI: 10.1080/15321819.2023.2260480; DOI: 10.1007/s00604-023-06113-2). Their abstracts give no accuracy data (Table A1d).

In principle, binder replacement is promising for supply independence and for coping with sequence variation. The evidence so far is mostly analytical, and the clearest like-for-like comparison is the nanobody strip.

## 3.1.5 Changing the optics: plasmonic scattering as a boundary case

All the strategies above increase absorbed colour. One study instead removes the white background that hides a different optical signal. When the nitrocellulose membrane is made transparent by refractive-index matching and placed over a black backing card, large AuNPs appear as orange lines by scattering rather than absorption, and the background almost disappears (DOI: 10.1038/s41467-025-58663-z). The authors report a very large gain against their own conventional strip and against commercial strips, a higher sensitivity on a small set of clinical swabs, and a naked-eye or smartphone readout (DOI: 10.1038/s41467-025-58663-z). The approach needs an extra reagent step and sufficient light, and the authors place it beyond absorbance-based colorimetric detection. We therefore keep it as a flagged boundary case and report its figures separately from absorption-based strips (Table A1c).

## 3.1.6 Conventional gold strips without engineering

Many included records describe new colloidal-gold strips that apply none of the steps above. They matter for two reasons: they are the baseline against which the engineering studies compare themselves, and they show how widely the format has been adapted to new viruses and hosts, from SARS-CoV-2 antibody and antigen tests to animal-virus strips (DOI: 10.1002/jcla.23619; DOI: 10.1002/ctm2.90; DOI: 10.1002/jmv.28416; DOI: 10.1007/s00705-018-3846-2; DOI: 10.1039/d4an00180j; DOI: 10.1039/d2an02043b). Several report clinical comparisons, and Table A1e lists examples. The line between a new assay and an engineering study is blurry: a strip is listed in this group when its abstract describes no deliberate change to the label, binder or readout.

## 3.1.7 What the evidence supports

The studies reviewed here form a coherent picture. Most of the sensitivity gains come from making the captured gold more visible, either after capture or through a better particle, and the best-supported comparisons are those against the authors' own conventional strip (Table A2). Binder replacement addresses a different problem, namely the quality and supply of the binding molecule, and has fewer clinical data. In one study, scattering shows that a change of optics can give a much larger gain, at the price of an extra step and a departure from pure absorbance.

Three limitations apply across the section. First, many reported LODs come from scanners, imagers or readers rather than the naked eye, so they describe instrument-assisted rather than equipment-free performance. Second, clinical evaluation is the exception among engineering papers, several papers tested only spiked buffer, saliva or recombinant protein, and the reference method varies (ELISA, RT-PCR, gel-read RT-PCR). Third, comparators differ between papers (own conventional strip, same-size particles, commercial strip), so fold-improvements cannot be ranked against each other. Reporting quality for the papers read in full is summarised in Table A3. Two animal-virus strips (DOI: 10.1039/d4an00180j; DOI: 10.1039/d2an02043b) are still known from abstracts only. Thirteen of the papers in Tables A1a-e have now been read in full, in some cases in the main text only (supporting information not seen).



### Table A1a. Particle size and conjugation chemistry

| Rec | Year | Target | Label / engineering | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R01131 | 2012 | potato virus X | AuNP (6.4-52 nm) | leaf extract | 80 to 3 ng/mL with 6.4-33.4 nm; 9 ng/mL at 52 nm | LOD vs diameter: 80 ng/mL (6.4 nm) to 3 ng/mL (33.4 nm); 9 at 52 nm | not reported | visual | Abstract | 10.1007/s00216-012-5985-8 |
| R02038 | 2016 | HBsAg | AuNP, sizes 34.2-137.8 nm | NR | NR | NR | NR | visual | Abstract | 10.3390/s16122154 |
| R08340 | 2026 | DENV NS1 | 80 nm AuNP | 185 archived plasma | 2.9 (DENV-1), 0.5 (DENV-2), 25.2 (DENV-3), 4.5 ng/mL (DENV-4) | NR | vs NS1 ELISA (values not in abstract) | visual | Abstract | 10.3390/diagnostics16030395 |
| R03985 | 2021 | HBsAg | gold nanoparticles | NR | less labelled antibody (0.2 mg/pmol AuNPs); LOD NR | NR | NR | visual | Abstract | 10.1016/j.aca.2021.338623 |
| R03607 | 2021 | SARS-CoV-2 IgM/IgG | AuNP | serum | not reported | NR | improved sensitivity without false positives (no values) | visual | Abstract | 10.2147/ijn.s281594 |
| R02055 | 2017 | Zika virus NS1 | gold nanoparticles | NR | NR | NR | protein corona improves specificity/sensitivity | visual | Abstract | 10.1021/acs.bioconjchem.6b00523 |
| R05768 | 2022 | dengue NS1 | gold nanoparticles | NR | preformed coronas altered LOD and KD | NR | NR | visual | Abstract | 10.3390/pharmaceutics14112439 |
| R03110 | 2020 | dengue (model) | gold nanoparticles | NR | NR | NR | NR | visual | Abstract | 10.1021/acsami.0c08628 |

### Table A1b. On-strip enlargement and signal amplification

| Rec | Year | Target | Label / engineering | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R04212 | 2021 | SARS-CoV-2 RBD | 22.8 nm AuNP; Ag, galvanic-Au or Au enhancement on strip | saliva spiked (1 healthy volunteer); inactivated virus | 488 / 61 / 8 / 1 pg/mL (conventional / Ag / galvanic / Au) | Same strip, same antibodies: 488-fold from conventional to gold enhancement (calculated); inactivated virus detected at 500-fold higher dilution | none (no patient samples) | flatbed scanner, grayscale | Full text † | 10.3390/bios11070229 |
| R02496 | 2018 | Potato virus X | 20 nm AuNP enlarged to ~350 nm on strip (HAuCl4 + H2O2, 1 min) | potato leaf extracts | conventional 4.11 ng/mL; enhanced 17 pg/mL (blank mean + 3 SD) | 240-fold lower than conventional LFIA | 170 infected and 49 healthy extracts (20 and 16 plants): conventional detected 117/170; enhanced 170/170; no false positives in 49 healthy; infected status of plants checked with commercial ELISA | visual; flatbed scanner (Canon 9000F) for quantification | Full text † | 10.1007/s00604-018-3052-7 |
| R06172 | 2023 | SARS-CoV-2 nucleocapsid | gold nanoparticles + gold enhancement | saliva | 0.50 ng/mL (naked eye), 0.10 ng/mL (calibration); 10x conventional | about 10x vs conventional LFIA | NR | visual | Abstract | 10.1016/j.snb.2023.133898 |
| R07142 | 2024 | SARS-CoV-2 N protein | 135 nm gold nanoflowers (Au NFs) +/- gold staining; Au NF-600 vs 94 nm AuNP of similar size | sample dilution buffer; artificial saliva (matrix test); no real samples | naked eye 0.025 ng/mL (3 sigma/slope 0.01 ng/mL); with gold staining naked eye 0.005 ng/mL (3 sigma/slope 0.0035 ng/mL) | nanoflower 5-fold (naked eye 0.05 vs 0.25 ng/mL) vs spherical AuNP of similar size, same antibodies; gold staining 5-fold further | none; artificial saliva up to 40% v/v no effect, 50% weakened signal | naked eye; smartphone (Oppo Reno 8 Pro+) + ImageJ | Full text † | 10.1007/s00604-024-06502-1 |
| R05719 | 2023 | HBsAg | 22.7 nm AuNP; post-assay electrophoretic layer-by-layer assembly (biotin/streptavidin AuNP) | human serum spiked with HBsAg; 118 clinical samples (99 serum, 19 plasma) | conventional 7.8 ng/mL; enhanced 0.12 ng/mL (blank + 3 SD, n = 3); linear range 0.12-62.5 ng/mL | more than 60-fold (authors; 65-fold calculated); capillary-flow addition of the same conjugates gave only 6.0 vs 7.8 ng/mL | vs Abbott Alinity i chemiluminescent assay (80 positive, 38 negative): conventional sens 58/80 (72.5%), spec 36/38 (94.7%); enhanced sens 78/80 (97.5%), spec 36/38 (94.7%); enhancement applied only to samples with no or weak coloration (< 4 RU) | visual and colorimetric intensity (RU); imaging device not stated in main text | Full text † | 10.1002/anie.202215548 |
| R05311 | 2022 | SARS-CoV-2 N-protein IgM/IgG (serology) | N-protein-gold + anti-N IgG-gold amplifier complex (150 nm nanoshells per text) | serum, 2 uL | visual at ELISA OD 0.55 (IgM), 0.4 (IgG); no concentration LOD | more than 2-fold signal vs N-protein-gold alone | 112 RT-PCR+ and 52 pre-pandemic sera vs in-house ELISA: IgM sens 94% (103/109), spec 93% (51/55); IgG sens 96% (107/112), spec 98% (51/52) | smartphone + ImageJ | Full text † | 10.1002/gch2.202200008 |

### Table A1c. Structured plasmonic particles and the scattering boundary case

| Rec | Year | Target | Label / engineering | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R04815 | 2022 | SARS-CoV-2 nucleocapsid | PLASCOP AuNP clusters (streptavidin core, ~15 nm gaps) | buffer; virus-spiked saliva | 0.910 (15 nm AuNP), 0.226 (40 nm), 0.551 (40-15 cluster), 0.038 ng/mL (40-40 cluster); 54 TCID50/mL virus in saliva | 40-40 cluster: 5.9x vs 40 nm, 23.8x vs 15 nm; 40-15 cluster worse than 40 nm | none (spiked saliva only) | ChemiDoc imager, S/N = 5 | Full text † | 10.1016/j.bios.2022.114094 |
| R02948 | 2017 | HIV p24 | gold dendrimer nanochains (red-to-blue shift) | pseudo-serum | 5 ng/mL (pseudo-serum) | NR | NR | visual | Abstract | 10.1039/c7tb01394a |
| R05579 | 2022 | SARS-CoV-2 nucleocapsid protein | SiO2@Au core-satellite particles vs 40 nm gold colloid | assay buffer; heat-inactivated cultured virus | 0.24 pg/mL N protein (blank + 3 SD); visual limit 10 pg/mL; cultured virus 4.9 TCID50/mL (naked eye 3.8 x 10^2 TCID50/mL) | 2 orders of magnitude lower than conventional strip with 40 nm gold colloids (100-fold in dilution test) | none (no patient samples); no cross-reactivity with influenza A, influenza B, MERS-CoV, Ebola and HCoV-229E NPs; strips stable 15 days (RSD 4.31%) | naked eye and colorimetric intensity (imaging reader) | Full text † | 10.1021/acsami.2c13303 |
| R06544 | 2023 | PEDV antigen | AuNP dimers (30 nm, Ag-ion soldering) | pig faeces; cultured virus dilutions | 2.0 x 10^2 TCID50/mL | 50-fold vs commercial AuNP strip (1.0 x 10^4); different antibodies | 109 faeces vs gel-read RT-PCR: 90+/19-, 100% agreement | naked eye | Full text † | 10.1007/s00604-023-06013-5 |
| R08618 | 2026 | BVDV NS3 antigen | hollow Ag-rich Ag-Au nanoshells (~40 nm) | bovine serum and ear tissue | 1.95 x 10^3 TCID50/mL | 4-fold vs own AuNP strip (7.81 x 10^3), same antibodies | 215 samples vs commercial NS3 ELISA: TP 45, FN 3, FP 1, TN 166; PPA 93.75%, NPA 99.40%, OA 98.14% | visual (ImageJ for optimisation) | Full text † | 10.1007/s00604-026-08241-x |
| R05088 | 2018 | avian influenza H7 | Au/Fe3O4 core-shell nanoparticles | 200 clinical samples | 10^3.5 EID50 | NR | 7 positives in 200 clinical samples | visual | Abstract | 10.1039/c8ra00185e |
| R08385 | 2026 | RVFV nucleoprotein (recombinant) | magnetic-gold nanostars (mpGNS-3, Fe3O4 core, sharp gold spikes); magnetic pre-concentration | PBS; blood serum spiked; saliva, urine, whole blood from one healthy volunteer (1 ng/mL spike) | 2.24 pg/mL in PBS; 1.17 pg/mL in spiked blood serum (3 sigma/slope) | about 1000-fold vs own gold nanosphere strip (2 ng/mL); non-magnetic control run | none (spiked samples only); specificity panel not tested; whole blood caused aggregation | smartphone grayscale; colorimetric | Full text † | 10.1021/acsami.5c21544 |
| R04920 | 2022 | HIV capsid protein | composite plasmonic nanoparticles | NR | 170 fM (58-fold improvement over 50 nm AuNP single wavelength) | 58-fold vs single-wavelength imaging of 50 nm AuNP | NR | optical two-wavelength imaging | Abstract | 10.1016/j.bios.2022.114133 |
| R07685 | 2025 | Influenza A (H1N1 particles, NP) | 100 nm AuNP, plasmonic scattering on black backing (boundary case) | buffer; swabs in transport medium (diluted to 10%) | 2.09 pfu/mL (NP 1.17 pg/mL) | 361-fold vs own 40 nm AuNP strip (755.47 pfu/mL; NP 234.69 pg/mL); 2600-4400-fold vs three commercial strips (5,417-9,219 pfu/mL) | 30 qRT-PCR+ and 12 healthy: sens 90% (27/30), spec 100%; commercial strips 23-30%; own conventional 40% | gel imager; smartphone gave same positive rate | Full text † | 10.1038/s41467-025-58663-z |

### Table A1d. Alternative recognition elements

| Rec | Year | Target | Label / engineering | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R06317 | 2023 | SARS-CoV-2 S1 | AuNP-nanobody detector + AuNP-ACE2 capture (40 nm) | gamma-irradiated virus; saliva | nanobody 0.4 vs mAb 1.6 (x 10^n copies/mL; exponent unverified) | 4-fold lower LOD than mAb version of same strip | 320 saliva (180 RT-PCR+, 140 -): Ct<=30 sens 97.14%, spec 98.57% (nanobody); mAb sens 90.04% (abstract) vs 83.33% (text) | gel documentation imager | Full text † | 10.1038/s41598-023-37347-y |
| R07006 | 2024 | SARS-CoV-2 N protein | NR | NR | 500 pg/mL | NR | NR | visual | Abstract | 10.1021/acs.analchem.4c00509 |
| R07343 | 2024 | SARS-CoV-2 S1 | AuNP | not reported | picomolar sensitivity | NR | not reported | visual | Abstract | 10.1039/d4nr02762k |
| R08024 | 2025 | SARS-CoV-2 N protein | AuNP | not reported | 10^3.15 PFU/mL; R2 0.9874 | NR | not reported | visual | Abstract | 10.1039/d5nr02568k |
| R08366 | 2026 | SARS-CoV-2 N protein | AuNP | not reported | 40 ng/mL | NR | not reported | visual | Abstract | 10.3390/bios16020132 |
| R08202 | 2025 | CHIKV E protein | AuNP | serum | 1.56 ng/mL (ICTS); 49 pg/mL (ELISA) | nanobody ELISA 49 pg/mL for comparison | not reported | visual | Abstract | 10.3389/fimmu.2025.1707358 |
| R01994 | 2016 | human norovirus | NR | outbreak specimens | NR | NR | sens 80%, spec 86% | visual | Abstract | 10.1128/msphere.00219-16 |
| R07002 | 2024 | SARS-CoV-2 spike protein | AuNP-aptamer, competitive format | thawed cold-chain package ice, spiked with recombinant S protein | 91.2 ng/mL (0.68 nM), 3 sigma/slope | NR | none; recovery 83.3-108.8% (RSD 2.3-6.2%) | Hamamatsu reader; visual range 0.1-1 ug/mL | Full text † | 10.3390/molecules29081776 |
| R04192 | 2021 | SARS-CoV-2 spike | NR | UV-inactivated virus | 5 x 10^5 copies/mL | NR | NR | visual | Abstract | 10.1002/anie.202107730 |
| R05081 | 2022 | SARS-CoV-2 | NR | UV-inactivated virus | 10^6 copies/mL | NR | NR | visual | Abstract | 10.1021/acs.analchem.2c00554 |
| R06728 | 2024 | SARS-CoV-2 N | NR | 10 spiked NP samples | 0.1 ng/mL (ELAAA); 0.1-0.5 ng/mL range (hybrid-LFS) | NR | ELAAA recovery 92% | visual | Abstract | 10.1186/s12951-023-02191-9 |
| R03437 | 2020 | SARS-CoV-2 spike | glyconanoparticles (gold) | NR | NR | NR | NR | visual | Abstract | 10.1021/acscentsci.0c00855 |
| R06535 | 2023 | dengue (severe) | gold nanoparticles (lectin) | patient samples | 5 ug/uL | NR | NR | visual | Abstract | 10.1080/15321819.2023.2260480 |
| R06699 | 2023 | SARS-CoV-2 variants of concern | gold nanoparticles | NR | NR | NR | NR | visual | Abstract | 10.1007/s00604-023-06113-2 |

### Table A1e. Conventional gold strips (examples with data)

| Rec | Year | Target | Label / engineering | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R03311 | 2021 | SARS-CoV-2 IgG/IgM | colloidal gold | 170 patients, 300 controls | NR | NR | 158/170 positive, 296/300 negative; AUC 0.958, kappa 0.926 | visual | Abstract | 10.1002/jcla.23619 |
| R03052 | 2020 | SARS-CoV-2 IgM/IgG | colloidal gold | 75 cases, 139 controls | NR | NR | IgM sens 90.67%, spec 97.84%, accuracy 95.33% | visual | Abstract | 10.1002/ctm2.90 |
| R05807 | 2023 | SARS-CoV-2 RBD | gold nanoparticles | 100 clinical samples | 1 ng/mL | NR | sens 94.3%, spec 90.9% vs RT-PCR | smartphone | Abstract | 10.1002/jmv.28416 |
| R02384 | 2018 | canine parvovirus | gold nanoparticles | faecal samples | 6.6 x 10^5 TCID50/mL | NR | sens/spec 71%/92% vs HA; 71%/100% vs commercial IC | visual | Abstract | 10.1007/s00705-018-3846-2 |
| R06939 | 2024 | avian leukosis virus p27 | gold nanoparticles | 35 egg samples | 1.53 ng/mL (ICS); 0.2 ng/mL (ELISA) | ELISA 0.2 ng/mL for comparison | 5 positive, 30 negative | visual | Abstract | 10.1039/d4an00180j |
| R05924 | 2023 | monkeypox virus A29 | colloidal gold | NR | 50 pg/mL purified A29 | NR | no cross-reaction with vaccinia or cowpox | visual | Abstract | 10.1039/d2an02043b |

### Table A2. Strategy overview for gold-nanoparticle engineering

| Strategy | Bottleneck addressed | Approaches in the included studies | Reported within-paper gains (see tables for values) | Costs and limits seen in the evidence | Table |
|---|---|---|---|---|---|
| Size and surface tuning | antibody activity, particle mobility | size series, oriented conjugation, additives, corona and aggregation studies | LOD varies with diameter in one plant-virus study; less antibody needed with oriented conjugation | mostly mechanistic; few diagnostic data | A1a |
| Enlargement and amplification | size of the captured signal | silver, gold and galvanic enhancement, self-enhancement, layer assembly, amplifier complex | LOD lowered within the same strip format, by up to more than two orders of magnitude | extra steps, background, lowest values often need calibration or a reader | A1b |
| Structured particles | optical effect per particle | clusters, dimers, nanoshells, composites, nanostars | about 4- to 24-fold against the authors' own strips; 50-fold against a commercial strip (dimers) | scale-up (dimers), buffer-only tests (nanostars), instrument imaging (two-wavelength) | A1c |
| Binder replacement | binder quality, supply, variants | nanobodies, aptamers, glycans, lectins, miniproteins | nanobody: lower LOD than mAb in the same strip | aptamer strips less sensitive; mostly spiked or inactivated-virus samples | A1d |
| Optical readout change | background of the white membrane | plasmonic scattering on a black backing | one study: 361-fold against its own strip, sensitivity 90% on 30 positive swabs | extra reagent step, light source, boundary to colorimetric | A1c |


### Table A3. Reporting checklist for papers read in full (13 papers; the supporting information was not available for R05719) (descriptive, not scored)

Items: (a) real samples; (b) n stated; (c) reference method; (d) LOD definition; (e) cross-reactivity tested by the authors; (f) replicates or reproducibility; (g) comparator run in the same study; (h) stability tested. Y = yes, N = no, P = partly, NR = not reported. The other 30 papers in Tables A1a-e have not been assessed (abstract only); they will be added as summaries arrive.

| Rec | DOI | (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) |
|---|---|---|---|---|---|---|---|---|---|
| R04212 | 10.3390/bios11070229 | N (spiked saliva, inactivated virus) | NR | not applicable | Y (blank mean + 3 SD) | N (supplier claim only) | P (blank n = 5; assay replicates unclear) | Y (same strip, same antibodies) | N |
| R04815 | 10.1016/j.bios.2022.114094 | N (spiked saliva) | NR | not applicable | Y (S/N = 5 formula) | Y (influenza A/B, MERS-CoV, HCoV-229E N proteins) | NR | Y (single AuNPs; two commercial kits compared) | N |
| R07685 | 10.1038/s41467-025-58663-z | Y (30 flu A, 12 healthy) | Y | Y (qRT-PCR) | Y (blank mean + 3 SD) | Y (SARS-CoV-2, RSV, flu B) | P (six repeats in stability test) | Y (own strip and three commercial strips) | Y (one year) |
| R07002 | 10.3390/molecules29081776 | N (spiked package ice, recombinant protein) | NR | not applicable | Y (3 sigma/slope) | Y (HCoV-229E, OC43, RSV-F, IgG, BSA) | Y (intra- and inter-batch, CV < 15%) | N | Y (16 days) |
| R05311 | 10.1002/gch2.202200008 | Y (112 RT-PCR+, 52 pre-pandemic sera) | Y | P (in-house ELISA, not PCR) | Y (visual OD cut-off; regression formula) | P (reagent specificity by ELISA only) | P (triplicate strips) | Y (N-protein-gold alone) | N |
| R06317 | 10.1038/s41598-023-37347-y | Y (320 saliva) | Y | Y (RT-PCR) | P (serial dilution; statistical definition NR) | Y (SARS-CoV, MERS-CoV S1) | P (small stability set; batch testing NR) | Y (mAb version) | Y (2 months) |
| R08618 | 10.1007/s00604-026-08241-x | Y (215 serum and ear tissue) | Y | P (commercial ELISA; RT-PCR only for sequencing) | Y (visual cut-off: no purple band) | Y (CSFV, IBRV, BPIV-3, M. bovis, BVDV subtypes) | NR | Y (own AuNP strip) | Y (accelerated, 37 C, 21 d) |
| R06544 | 10.1007/s00604-023-06013-5 | Y (109 pig faeces) | Y | Y (gel-read RT-PCR) | Y (lowest dilution with visible T line) | Y (TGEV, RV, PRV, PCV2, 4 bacteria) | Y (intra- and inter-batch, 3 batches) | P (commercial strip, different antibodies) | N (stated limitation) |
| R05719 | 10.1002/anie.202215548 | Y (118 clinical, 99 serum and 19 plasma) | Y (80 pos, 38 neg) | Y (Abbott Alinity i chemiluminescent assay) | Y (blank + 3 SD) | NR (main text only) | P (n = 3 for calibration) | Y (same strips before and after enhancement) | P (one-week storage of strips before enhancement tested; shelf stability NR) |
| R02496 | 10.1007/s00604-018-3052-7 | Y (170 infected and 49 healthy leaf extracts) | Y | P (infected status from commercial ELISA of source plants) | Y (blank mean + 3 SD) | NR | P (n = 4 and n = 5 per calibration point) | Y (conventional vs enhanced) | N |
| R07142 | 10.1007/s00604-024-06502-1 | N (artificial saliva only) | not applicable | not applicable | Y (3 sigma/slope; naked-eye limit) | NR (main text) | Y (intra- and inter-batch RSD, Table S1, S2) | Y (spherical AuNP of similar size) | Y (8 weeks, 4 C, RT and 40 C) |
| R05579 | 10.1021/acsami.2c13303 | N (cultured inactivated virus) | NR | P (RT-qPCR on culture fluid) | Y (IUPAC blank + 3 SD) | Y (influenza A and B, MERS-CoV, Ebola, HCoV-229E NPs) | Y (three independent experiments; five for membrane optimisation) | Y (40 nm gold colloid) | Y (15 days) |
| R08385 | 10.1021/acsami.5c21544 | N (spiked serum, saliva, urine, blood) | not applicable | not applicable | Y (IUPAC 3 sigma/slope) | N (stated as needed) | Y (four batches, RSD 7.5%) | Y (own gold nanosphere strip; non-magnetic control) | P (probe stable 6 months at 2-8 C; not at 40 C or room temperature) |

## Items still to verify before this section is final
1. R06317 (DOI: 10.1038/s41598-023-37347-y): exponent of the LOD, and the mAb comparator sensitivity (90.04% in the abstract, 83.33% in the results text).
2. R05311 (DOI: 10.1002/gch2.202200008): label is 150 nm gold nanoshells in the text, gold nanoparticles in the abstract.
3. R05924 (DOI: 10.1039/d2an02043b) and R06939 (DOI: 10.1039/d4an00180j): abstract only.
4. R07685 (DOI: 10.1038/s41467-025-58663-z): boundary case; LOD reported separately from absorption-based strips.
5. Record IDs in the tables will be replaced by numbered citations when the reference list is built.
