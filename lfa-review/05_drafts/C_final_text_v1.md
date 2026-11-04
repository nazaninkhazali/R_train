# Part C (working text v1): catalytic and enzymatic amplification

Working text, 2026-11-05. Text focuses on the technologies and how they connect; numerical detail is in the tables. † = read in full; all other rows abstract only (NR = not reported in the abstract). Every DOI cited in the text appears in a table and in the evidence table. Section c covers 51 included records after the E10 exclusion of seven marketed-kit evaluations.

# 3.3 Catalytic and enzymatic amplification: adding signal after capture

## 3.3.0 Why amplify, and how this section is organised

The colour of a conventional strip is limited by what the label itself absorbs, and by how many labels the antibodies manage to capture (DOI: 10.1021/acsnano.7b06229). Amplification adds a second source of signal: after the sandwich has formed, something at the test line produces or deposits more colour. Enzyme-catalysed amplification is standard in laboratory immunoassays, but conventional implementations need technical skill and equipment that suit field use poorly (DOI: 10.1021/acsnano.7b06229). The studies in this section try to bring catalytic amplification into the strip while keeping it simple enough for the point of need.

The approaches can be read as a progression in how much of the amplifier is built into the strip. The first group deposits metal on particles that are already captured (3.3.1). The second uses natural enzymes such as horseradish peroxidase and alkaline phosphatase as labels (3.3.2). The third replaces enzymes with inorganic nanozymes, particles that mimic enzyme activity and are described by their authors as more stable and easier to scale up (3.3.3 and 3.3.4; DOI: 10.1016/j.snb.2021.130718; DOI: 10.3390/plants15040656). The fourth tries to make the amplification step automatic (3.3.5). The last group combines catalytic colour with a second readout, and only the colorimetric channel counts here (3.3.6). Section 3.3.7 states what the evidence supports.

Details (LOD with units, matrix, comparator, diagnostic data, readout) are in Tables C1a-C1f. Papers read in full are marked † in the tables; all other statements rest on abstracts. The section covers 51 included records, 47 of them from 2015-2026. Seven evaluations of marketed amplification kits were excluded under the rule agreed for commercial-kit evaluations (E10); they are listed in the supplement.

## 3.3.1 Depositing more metal on captured particles

The simplest amplifier uses the particles themselves as seeds for further metal deposition. Silver enhancement was used for tobacco mosaic virus and H5 influenza before 2015, and in later work for equine influenza and foot-and-mouth disease virus (DOI: 10.1134/s0006297909090065; DOI: 10.1016/j.jviromet.2011.08.017; DOI: 10.1292/jvms.17-0105; DOI: 10.1016/j.jviromet.2019.113736). Gold enlargement was used for avian influenza and Newcastle disease virus and, more recently, for a fish iridovirus (DOI: 10.1016/j.aca.2013.04.022; DOI: 10.1016/j.talanta.2026.130562), and copper deposition on gold seeds extended the approach to HIV p24 and to SARS-CoV-2 nucleocapsid protein (DOI: 10.1016/j.bios.2020.112753; DOI: 10.3390/bios12010013). A three-dimensional device combines gold and silver enhancement in one step for SARS-CoV-2 (DOI: 10.1021/acs.analchem.5c03575). These designs follow the logic described in section 3.1.2: the gain is large, but each needs an extra reagent step and carries a risk of background. One related approach amplifies by thermal contrast, which changes the readout from colour to heat and so lies at the edge of this review (DOI: 10.1021/acsanm.1c03217).

## 3.3.2 Natural enzymes as labels

Horseradish peroxidase (HRP) and alkaline phosphatase (ALP) produce a coloured precipitate from a substrate. On a strip they have been used as the sole label, together with gold, or on magnetic carriers. An early enzyme-based strip detected SARS coronavirus nucleocapsid antigen (DOI: 10.1002/jcla.20070). ALP combined with gold nanoparticles was used for potato virus X (DOI: 10.1007/s00604-017-2595-3). An HRP-labelled strip differentiated influenza A and B in nasopharyngeal samples (DOI: 10.1002/jmv.25322), and HRP added to a colloidal-gold strip for bovine parvovirus raised the signal on faecal samples (DOI: 10.3389/fmicb.2023.1174737). Magnetic enzyme labels were used for dengue NS1, and a capture-layer design with an enzyme label allowed quantitative dengue NS1 detection (DOI: 10.7717/peerj.7779; DOI: 10.1021/acsomega.0c00367). A hepatitis B e-antigen strip used a signal amplification system, with a mechanism not stated in the abstract (DOI: 10.1002/jmv.25452). Enzyme-induced tyramide deposition produced a dual-colour amplification for SARS-CoV-2 and influenza (DOI: 10.1016/j.bios.2024.116262), and HRP tracers have been applied to nucleic acid detection in a vertical-flow format (DOI: 10.1007/s00216-022-03988-7).

The main weakness of natural enzymes is stability. In one direct test, freeze-dried antibody-HRP conjugates lost most of their signal within two weeks of dry storage at room temperature, whereas a platinum nanocatalyst kept its signal for weeks, even at 44 C (DOI: 10.1021/acsnano.7b06229). That observation is the main reason given for nanozymes in the studies that follow.

## 3.3.3 Noble-metal nanozymes

Nanozymes are particles with peroxidase-like activity; supplied with hydrogen peroxide and a chromogenic substrate, they oxidise it and deposit colour at the test line. Platinum-based particles dominate the evidence.

A porous platinum core-shell nanocatalyst for HIV p24 is the most thoroughly characterised example (DOI: 10.1021/acsnano.7b06229). Its activity depends on particle size, on the polymer capping used in synthesis and on the porous platinum shell, which stays accessible to hydrogen peroxide even when serum proteins coat the surface; the best size range was 120-200 nm, and larger particles performed worse (DOI: 10.1021/acsnano.7b06229). The same strip works in two regimes: at high antigen the intrinsic dark colour of the particle is visible, and at low antigen the catalytic step takes over, which widens the dynamic range over several orders of magnitude (DOI: 10.1021/acsnano.7b06229). The authors tested serial plasma from an HIV seroconversion panel and detected antigen during the acute phase, and lyophilised reagents survived weeks of accelerated ageing (DOI: 10.1021/acsnano.7b06229). The assay needs a wash step and a 5-min development step, so it is not a one-step strip.

Gold-platinum particles follow the same principle. A nanoenzyme-linked sensor with Au@Pt particles for SARS-CoV-2 nucleocapsid protein reads the developed substrate by transmitted light in a small 3D-printed holder with a laser, a photometer and a smartphone, so the result is colorimetric but not equipment-free (DOI: 10.1016/j.snb.2021.130718). The reported LOD was similar to a laboratory ELISA and lower than that of a conventional strip with the same antibodies, and the Au@Pt particles kept their activity over days while HRP lost it (DOI: 10.1016/j.snb.2021.130718). Related noble-metal nanozymes include peroxide-tolerant Au@Pt for plant virus (DOI: 10.1016/j.talanta.2020.121961), Au@Pt nanorods for HBV DNA (DOI: 10.1039/d1an02084f), trimetallic Au@Pd@Pt (DOI: 10.1039/d2ay01530g), an AuPt nanoalloy for HPV16 DNA (DOI: 10.1039/d3ra00757j), Au@Pt for SARS-CoV-2 nucleocapsid protein and respiratory syncytial virus (DOI: 10.1007/s00604-024-06697-3; DOI: 10.1016/j.talanta.2026.130820), Au@Pt@Pd (DOI: 10.1007/s00604-024-06819-x), a platinum nanozyme with a mesoporous silica shell for enrichment (DOI: 10.1016/j.aca.2024.343474), Pt-Pd particles for foot-and-mouth disease virus (DOI: 10.1016/j.jchromb.2024.124043), PdRu nanocages for HPV16 and HPV18 (DOI: 10.1016/j.jcis.2024.06.002), polydopamine-platinum particles (DOI: 10.1186/s12951-025-03903-z) and platinum nanoparticles for influenza A, one of the few with a stated clinical sensitivity and specificity against RT-PCR (DOI: 10.1021/acsinfecdis.5c00731). A platinum-polymer nanoparticle strip evaluated on 200 clinical specimens had a sensitivity of 74% and a specificity of 100% (DOI: 10.3390/biomedicines13122993), a reminder that amplification does not remove the limits that antibody pairs and sample type set (Table C1c).

## 3.3.4 Other nanozymes and structured catalysts

Iron-oxide nanozymes were among the earliest: a Fe3O4 nanozyme strip for Ebola virus glycoprotein lowered the LOD 100-fold compared with a standard strip (DOI: 10.1016/j.bios.2015.05.025). A study on potato viruses shows how differently nanozymes can be used (DOI: 10.3390/plants15040656). Fe3O4 particles were applied as a plain colorimetric label read by eye within 10 minutes, with no substrate step, to build monovalent and bivalent strips for potato viruses X and Y; the authors note that substrate-based amplification could raise sensitivity further, but did not test it (DOI: 10.3390/plants15040656). All 12 tissue-culture plantlets matched RT-PCR, and the authors state that storage stability and batch consistency were not evaluated, even though the abstract mentions storage at ambient temperature (DOI: 10.3390/plants15040656).

Further designs vary the chemistry. A PDA@MnO2 oxidase-like mimic was combined with a peptide binder (DOI: 10.1021/acs.analchem.3c02821). Bimetallic Fe-Co particles were used for porcine rotavirus on faecal samples (DOI: 10.1016/j.ab.2026.116259), a nanozyme strip was developed for avian leukosis virus (DOI: 10.1016/j.tvjl.2025.106508), magnetic multi-metallic nanozymes for influenza A (DOI: 10.1002/exp.20240425), and a three-dimensional film-like nanozyme for respiratory viruses (DOI: 10.1021/acsnano.4c09513) (Table C1d).

## 3.3.5 Building the amplification into the strip

The weak point of most amplified strips is the extra step. Three designs try to make it automatic or user-friendly. A nanozyme strip with a push-button signal enhancement worked in undiluted serum (DOI: 10.1039/d1an01350e). A strip with delayed substrate release lets the substrate reach the test line after the sample, so amplification happens without a user step (DOI: 10.1016/j.talanta.2025.127557). An aptamer-based design changes how the chemical signal is transformed to raise signal quality (DOI: 10.1039/d4nr04130e). These approaches aim to keep the strip one-step, which is the main reason many simple gold strips remain in use (Table C1e).

## 3.3.6 Dual-mode strips and mixed-target assays

Some nanozyme strips add a second readout, such as photothermal, fluorescent or Raman signals, or combine viral and bacterial targets. A Fe3O4@MoS2@Pt nanotag gave colorimetric and photothermal readouts, and the photothermal LODs are not colorimetric and are kept apart in the table (DOI: 10.1021/acsami.3c15851). Others combine nanozymes with fluorescence or SERS for SARS-CoV-2, norovirus and adenovirus (DOI: 10.1021/acs.analchem.5c02780; DOI: 10.1021/acs.analchem.5c03047; DOI: 10.1021/acsami.6c07352), and three strips detect viruses together with bacteria or without naming the viral targets in the abstract (DOI: 10.1002/advs.202502574; DOI: 10.1021/acs.analchem.5c03762; DOI: 10.1021/acs.analchem.6c03394). Only the colorimetric channel and the viral target are counted for this review (Table C1f).

## 3.3.7 What the evidence supports

Catalytic amplification gives the largest gains reported in this review, often one to three orders of magnitude within a paper, and nanozymes are consistently described as more stable than natural enzymes (Table C2). Three cautions run through the evidence. First, amplification is paid for with steps: substrate, hydrogen peroxide, washing or a reading device; the clearest example of this is the smartphone nanoenzyme sensor, whose result depends on an optical reader. Second, the comparator differs, such as an unamplified strip, a commercial gold strip or an ELISA, so fold-improvements cannot be ranked. Third, clinical evidence is thin: where patient samples were tested, sensitivity ranged widely, from 74% for a platinum-polymer strip to high values with small panels. The potato-virus Fe3O4 strip shows that a nanozyme can also serve as a simple label without any amplification step, which makes the term "nanozyme strip" ambiguous in the literature.



### Table C1a. Metal deposition on captured particles

| Rec | Year | Target | Label / amplifier | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R00778 | 2009 | tobacco mosaic virus | AuNP + Ag enhancement | leaf extract | 2-4 ng/mL; 0.1 ng/mL with silver (>10x) | >10x with silver | comparable to ELISA | visual | Abstract | 10.1134/s0006297909090065 |
| R01053 | 2011 | H5 influenza HA | AuNP + Ag amplification | not reported | 500x sensitivity gain; >10x vs NP-based RIDTs | 500x gain (abstract); >10x vs NP-based tests | not reported | visual | Abstract | 10.1016/j.jviromet.2011.08.017 |
| R01321 | 2013 | avian influenza, Newcastle disease virus | AuNP + HAuCl4/NH2OH enlargement | not reported | not reported | NR | not reported | visual | Abstract | 10.1016/j.aca.2013.04.022 |
| R02120 | 2017 | equine influenza virus | silver amplification (gold) | nasal swabs | 5-fold lower than conventional RAD tests | 5-fold lower than conventional rapid tests | NR | visual | Abstract | 10.1292/jvms.17-0105 |
| R02817 | 2020 | FMDV (7 serotypes) | silver amplification | 132 clinical samples | 10-100x more sensitive than Svanodip (serotypes O, A, Asia1, C, SAT1) | 10-100x more sensitive than Svanodip | less saliva inhibition than Svanodip | visual | Abstract | 10.1016/j.jviromet.2019.113736 |
| R03340 | 2021 | HIV-1 p24 (and E. coli O157:H7) | gold nanoparticles + Cu nanoshell growth (PEI-assisted) | NR | 50 fg/mL (HIV-1 p24); 6 CFU/mL (E. coli) | NR | NR | visual | Abstract | 10.1016/j.bios.2020.112753 |
| R04697 | 2021 | SARS-CoV-2 N protein | AuNP + Cu deposition | certified reference materials | 0.01 ug/mL to 10 pg/mL (3 orders) | 3 orders of magnitude | not reported | visual | Abstract | 10.3390/bios12010013 |
| R08742 | 2027 | ISKNV | AuNP | sea bass mucus | 0.25 ug/mL; 0.050 ug/mL after gold enhancement (5x) | 5x (gold enhancement) | aligned with PCR | visual | Abstract | 10.1016/j.talanta.2026.130562 |
| R08163 | 2025 | SARS-CoV-2 | AuNP + Au/Ag enhancement | Omicron BA.1 viral samples | not reported | NR | not reported | visual | Abstract | 10.1021/acs.analchem.5c03575 |
| R04627 | 2021 | SARS-CoV-2 antigen | AuNP | not reported | fM-aM; comparable to PCR (aM-zM) | NR | not reported | visual | Abstract | 10.1021/acsanm.1c03217 |

### Table C1b. Natural enzymes as labels

| Rec | Year | Target | Label / amplifier | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R00437 | 2005 | SARS-CoV N antigen | enzyme | 150 sera; 50 NP aspirates | 31 pg/mL recombinant N; 1.99e2 TCID50/mL | NR | spec 100% | visual | Abstract | 10.1002/jcla.20070 |
| R02353 | 2017 | potato virus X | gold NPs + ALP enzyme | buffer, leaf extracts | 0.3 ng/mL (27-fold below conventional LFIA) | 27-fold below conventional LFIA | NR | visual | Abstract | 10.1007/s00604-017-2595-3 |
| R02484 | 2019 | influenza A and B | HRP enzyme (TMB colour) | nasopharyngeal samples | >10-fold more sensitive than gold-colloidal strips (13 isolates) | >10-fold more sensitive than gold-colloidal strips | sens 90.2% (55/61) and 82.6% (71/86) | visual | Abstract | 10.1002/jmv.25322 |
| R02792 | 2019 | dengue NS1 (DENV1-4) | magnetic enzyme label (catalytic) | clinical samples | 0.25 ng/mL (DENV-1/3), 0.1 (DENV-2), 1.0 (DENV-4) | NR | sens 100%, spec 100% clinical | visual | Abstract | 10.7717/peerj.7779 |
| R03014 | 2020 | dengue NS1 | enzyme label (no nanobeads) | spiked buffer and serum | 5-fold more sensitive than gold-standard ELISA | 5-fold more sensitive than ELISA | NR | visual/quantitative | Abstract | 10.1021/acsomega.0c00367 |
| R04947 | 2022 | HBV DNA | HRP enzymatic tracer | 45 HBV plasma samples | 1.7 nM (8.5 fmol in 12 uL) | NR | 100% consistent with real-time PCR | visual | Abstract | 10.1007/s00216-022-03988-7 |
| R06219 | 2023 | bovine parvovirus | colloidal gold + HRP enhancement | 280 clinical faecal samples | 10^2 TCID50 (10x traditional strip) | 10x traditional strip | no cross-reaction with BRV, BVDV, BRSV | visual | Abstract | 10.3389/fmicb.2023.1174737 |
| R06975 | 2024 | SARS-CoV-2 nucleoprotein, influenza A/B | enzyme-induced tyramide amplification (dual-colour) | inactivated virus | 3.9 pg/mL; naked-eye cut-off 7.8 pg/mL; 0.018 TCID50/mL | NR | NR | visual/automated | Abstract | 10.1016/j.bios.2024.116262 |

### Table C1c. Noble-metal nanozymes

| Rec | Year | Target | Label / amplifier | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R02272 | 2018 | HIV-1 p24 | porous Pt core-shell nanocatalyst (~120 nm) + nanobody-biotin; streptavidin line; CN/DAB + H2O2 development | spiked fetal bovine serum and plasma; HIV seroconversion panel plasma (one donor) | 0.8 pg/mL (32.5 fM) after catalysis; pre-catalysis visible 100-10,000 pg/mL | catalysis lowers LOD by about 2 orders of magnitude; authors state up to 20x better than published sensitivity of leading commercial p24 tests (cross-study) | panel samples 7-14 of one donor detected (p24 10.8 and 4.6 pg/mL in samples 13, 14); cutoff blank + 3 SD; no sensitivity/specificity | phone camera + ImageJ; wash and 5-min development; < 20 min | Full text † | 10.1021/acsnano.7b06229 |
| R03648 | 2021 | potato virus X | Au@Pt core-shell nanozyme | leaf and tuber extracts | 4 pg/mL (tuber), 8 pg/mL (leaf) | NR | NR | visual (catalytic) | Abstract | 10.1016/j.talanta.2020.121961 |
| R04340 | 2021 | SARS-CoV-2 nucleocapsid protein | Au@PtNP-mAb (13 nm Au core, Pt shell) + TMB; U-shaped strip device | buffer standards; 21 COVID-19 sera; 80 healthy donor plasma | 0.026 ng/mL (mean + 3 SD of 40 negatives); range 0.05-1.6 ng/mL | commercial ELISA LOD 0.025 ng/mL; conventional ICA visible only above 0.1 ng/mL | 21 NAT-confirmed sera: 16 positive (76.2%) vs 10 by ELISA (47.6%), p = 0.057; 80 donors all negative (spec 100%); accuracy 95.1% vs 89.1%; r = 0.990 vs ELISA | 450 nm laser + photometer + smartphone (transmitted light); 25 min | Full text † | 10.1016/j.snb.2021.130718 |
| R04683 | 2022 | HBV DNA | Au@Pt nanorods (nanozyme) | NR | 8.5 pM (range 0.1-50 nM) | NR | NR | visual (catalytic) | Abstract | 10.1039/d1an02084f |
| R05783 | 2022 | SARS-CoV-2 nucleocapsid | Au@Pd@Pt core-shell nanozyme | spiked samples | 0.037 ng/mL (17-fold lower than unenhanced LFIA); range 0.05-100 ng/mL | 17-fold lower than unenhanced LFIA | recoveries 92.5-107.9% | visual (catalytic) | Abstract | 10.1039/d2ay01530g |
| R06192 | 2023 | HPV16 DNA | AuPt nanoalloy | NR | excellent sensitivity (value NR) | NR | NR | visual | Abstract | 10.1039/d3ra00757j |
| R07345 | 2024 | SARS-CoV-2 N protein | Au@Pt | not reported | 40 pg/mL naked eye (>1000x vs without amplification) | >1000x vs without amplification | not reported | visual | Abstract | 10.1007/s00604-024-06697-3 |
| R07397 | 2024 | SARS-CoV-2 N protein | Au@Pt@Pd | nasal swab | 0.06 ng/mL; 16x and 8x vs Au-LFIA and AF-LFIA | 16x vs Au-LFIA; 8x vs AF-LFIA | sens 84.09%, spec 100%, accuracy 92.55% | visual/reader | Abstract | 10.1007/s00604-024-06819-x |
| R07452 | 2025 | influenza A | Pt nanozyme | not reported | 33 copies/mL; ~100x vs AuNP strips | about 100x vs AuNP strips | not reported | visual | Abstract | 10.1016/j.aca.2024.343474 |
| R08120 | 2025 | influenza A NP | Pt nanoparticles | clinical trials | 11.6 pg/mL; 1000x vs traditional LFIA | 1000x vs traditional LFIA | sens 96.8%, spec 98.4% vs RT-PCR | visual | Abstract | 10.1021/acsinfecdis.5c00731 |
| R08245 | 2025 | SARS-CoV-2 | Pt-P2VP | 200 clinical specimens | not reported | NR | sens 74%, spec 100% | visual | Abstract | 10.3390/biomedicines13122993 |
| R08831 | 2026 | RSV F protein | Au@Pt | preliminary clinical | 0.25, 0.04, 0.78 ng/mL (ELISA, CLIA, Au@Pt-LFIA); Au@Pt ~4x vs colloidal gold | about 4x vs colloidal gold | PPA 90.0%, 93.3%, 83.3%; NPA 100% | visual | Abstract | 10.1016/j.talanta.2026.130820 |
| R06816 | 2024 | FMDV serotype O | Pt-Pd bimetallic nanoparticles (TMB catalytic colour) | NR | 1:2^8/test (range 1:2^6-1:2^9) | NR | 96.7% sensitivity on positive serum | visual and quantitative | Abstract | 10.1016/j.jchromb.2024.124043 |
| R07119 | 2024 | HPV16, HPV18 | PdRu nanocages (catalytic colour) | NR | 0.93 nM and 0.19 nM | NR | NR | visual | Abstract | 10.1016/j.jcis.2024.06.002 |
| R08213 | 2025 | influenza A | PDA@Pt | not reported | 0.5 ng/mL colorimetric; 0.005 ng/mL catalytic (2x, 200x vs AuNP LFIA) | 2x (colorimetric) and 200x (catalytic) vs AuNP LFIA | not reported | visual | Abstract | 10.1186/s12951-025-03903-z |

### Table C1d. Other nanozymes and structured catalysts

| Rec | Year | Target | Label / amplifier | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R01705 | 2015 | Ebola virus (GP) | Fe3O4 MNP nanozyme, catalytic colour | clinical samples (EBOV, bunyavirus) | 1 ng/mL (100-fold more sensitive than standard strip) | 100-fold more sensitive than standard strip | comparable with ELISA for clinical samples (values NR) | visual | Abstract | 10.1016/j.bios.2015.05.025 |
| R06404 | 2023 | SARS-CoV-2 spike | PDA@MnO2 oxidase mimic (catalytic colour) | pseudovirus in saliva (150 TU/mL) | 8.01 pg/mL (18.7x lower than gold nanoparticle pLFIA) | 18.7x vs gold nanoparticle LFIA | NR | visual (catalytic) | Abstract | 10.1021/acs.analchem.3c02821 |
| R08764 | 2027 | porcine rotavirus | Fe-Co nanozyme | 72 faecal samples | 100 TCID50/mL (2x vs commercial gold strips) | 2x vs commercial gold strips | sens 95.45%, spec 100%, kappa 0.97 | visual | Abstract | 10.1016/j.ab.2026.116259 |
| R08369 | 2026 | PVX and PVY coat proteins | Fe3O4 nanozyme used as plain colour label (no substrate); monovalent and bivalent strips | extracts of potato plantlets in vitro (RT-PCR confirmed) | visible T line up to a dilution of 10^n (exponents lost in retrieved text; chart: 1e3 PVX, 1e4 PVY); LOD = highest dilution with a visible line in 3/3 replicates | no gold strip or ELISA comparator in the study | 12 plantlets (1 PVX+, 6 PVY+) fully concordant with RT-PCR | naked eye, 10 min | Full text † | 10.3390/plants15040656 |
| R08184 | 2026 | ALV | nanozyme | not reported | 12.5 TCID50/mL; 0.20 ng/mL proteins | NR | no cross-reaction with six avian viruses | visual | Abstract | 10.1016/j.tvjl.2025.106508 |
| R08612 | 2026 | influenza A | multi-metal nanozyme | 20 clinical samples | 0.8 pg/mL (125x vs commercial colloidal gold); 140 copies/mL inactivated virus | 125x vs commercial colloidal gold | accuracy 100% | visual | Abstract | 10.1002/exp.20240425 |
| R07275 | 2024 | respiratory viruses (two) | nanozyme (GO-Pt30-AuPt5) | not reported | 1 pg/mL | about 100x vs no amplification | not reported | visual | Abstract | 10.1021/acsnano.4c09513 |

### Table C1e. Built-in or automatic amplification

| Rec | Year | Target | Label / amplifier | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R04542 | 2021 | SARS-CoV-2 nucleocapsid | nanozyme (catalytic colour) | undiluted serum | 0.1 ng/mL | NR | NR | visual | Abstract | 10.1039/d1an01350e |
| R07515 | 2025 | H1N1 nucleic acid | nanozyme | serum recovery | 0.02 nM; 25x lower than nanozyme-LFA before catalysis | 25x lower than nanozyme-LFA before catalysis | recovery 96-102.7% | visual | Abstract | 10.1016/j.talanta.2025.127557 |
| R07513 | 2025 | SARS-CoV-2 spike | AuNP nanozyme | 25 clinical samples | 168 pg/mL; >20x signal quality | >20x signal quality | semi-quantitative efficiency >90% | visual | Abstract | 10.1039/d4nr04130e |
| R02642 | 2019 | HBeAg | gold nanoparticles + amplification | 420 blood samples | 9 ng/mL (27-fold more sensitive than conventional LFIA) | 27-fold more sensitive than conventional LFIA | fully in accordance with ELISA | visual | Abstract | 10.1002/jmv.25452 |

### Table C1f. Dual-mode and mixed-target strips (colorimetric channel only)

| Rec | Year | Target | Label / amplifier | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R06844 | 2024 | SARS-CoV-2 NP, H1N1 | Fe3O4@MoS2@Pt nanozyme | simulated nose swabs | catalytic colorimetric 80 and 20 ng/mL (~100x vs commercial); photothermal 10 and 8 ng/mL (not colorimetric) | about 100x vs commercial (catalytic colorimetric) | recovery 95.2-103.8% | visual + photothermal | Abstract | 10.1021/acsami.3c15851 |
| R07938 | 2025 | SARS-CoV-2 N protein | nanozyme + fluorophore | clinical | 0.0302 ng/mL colorimetric | NR | superior to colloidal gold LFIA (no values) | visual + fluorescence | Abstract | 10.1021/acs.analchem.5c02780 |
| R08000 | 2025 | norovirus, adenovirus | nanozyme | 92 stool samples | 0.001 ng/mL NoV; 1e2 PFU/mL AdV (visual); SERS 0.00014 ng/mL, 11 PFU/mL (not colorimetric) | NR | not reported | visual + SERS | Abstract | 10.1021/acs.analchem.5c03047 |
| R08737 | 2026 | norovirus + E. coli O157 | magnetic nanozyme | 116 stool samples | vLOD 0.05 ng/mL norovirus; SERS 0.11 pg/mL (not colorimetric) | NR | consistent with qPCR | visual + SERS | Abstract | 10.1021/acsami.6c07352 |
| R08826 | 2026 | emerging viruses (two targets) | magnetic nanozyme | not reported | 19.4 and 22.5 pg/mL direct; >=92.65x sensitivity after 2 min catalysis | >=92.65x after catalysis | not reported | visual | Abstract | 10.1021/acs.analchem.6c03394 |
| R07744 | 2025 | SARS-CoV-2 + two bacteria | FeAu@AuIr nanozyme | 170 positive respiratory samples | not reported | NR | not reported | visual | Abstract | 10.1002/advs.202502574 |
| R08107 | 2025 | SARS-CoV-2 + bacteria | Au@Ir nanozyme | not reported | >=555x vs AuNP LFA; ~116x vs ELISA | >=555x vs AuNP LFA | not reported | visual | Abstract | 10.1021/acs.analchem.5c03762 |

### Table C2. Strategy overview for catalytic and enzymatic amplification

| Strategy | What it adds | Examples | Costs and limits seen | Table |
|---|---|---|---|---|
| Metal deposition (silver, gold, copper) | larger particles at the line | plant, avian, equine and foot-and-mouth viruses; HIV p24; SARS-CoV-2 | extra reagent step, background | C1a |
| Natural enzymes (HRP, ALP, tyramide) | catalytic colour from a substrate | influenza A/B, dengue NS1, bovine parvovirus, PVX | enzyme stability on dry storage | C1b |
| Noble-metal nanozymes (Pt, Au@Pt, Pd-based) | peroxidase-like catalysis, stable | HIV p24, SARS-CoV-2, influenza A, HPV, HBV | substrate and peroxide steps; reader in some designs; clinical data thin | C1c |
| Other nanozymes (iron oxide, oxidase mimics, composites) | alternative catalysts or plain labels | Ebola, potato viruses, rotavirus, avian leukosis virus | term used also for plain labels without amplification | C1d |
| Built-in or automatic amplification | removes a user step | push-button, delayed substrate release | few clinical data | C1e |
| Dual-mode with a second readout | extra sensitivity channel | SARS-CoV-2, norovirus, adenovirus | non-colorimetric channels excluded; mixed viral and bacterial targets | C1f |

### Table C3. Reporting checklist for papers read in full (descriptive, not scored)

Items: (a) real samples; (b) n stated; (c) reference method; (d) LOD definition; (e) cross-reactivity tested by the authors; (f) replicates or reproducibility; (g) comparator run in the same study; (h) stability tested. Y = yes, N = no, P = partly, NR = not reported. The other 48 papers in Tables C1a-f have not been assessed (abstract only).

| Rec | DOI | (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) |
|---|---|---|---|---|---|---|---|---|---|
| R02272 | 10.1021/acsnano.7b06229 | P (commercial seroconversion panel, one donor) | P (panel samples; counts not given) | P (manufacturer p24 ELISA and RNA assays) | P (cutoff blank + 3 SD for panel) | N (no panel in the text seen) | Y (five batches, CV 2.4%; triplicates) | Y (before vs after catalysis; HRP conjugate) | Y (6 weeks, 44 C and room temperature) |
| R04340 | 10.1016/j.snb.2021.130718 | Y (21 sera, 80 donors) | Y | P (NAT-confirmed patients; ELISA comparator) | Y (mean + 3 SD of 40 negatives) | Y (S, RBD, H1N1 HA and NA, HBsAg, HCV core) | Y (intra-assay 6 replicates; inter-assay 8 tests) | Y (ELISA and conventional ICA on same standards) | P (catalyst activity 15 days; strip shelf life NR) |
| R08369 | 10.3390/plants15040656 | P (tissue-culture plantlets, not field) | Y (12) | Y (RT-PCR) | Y (highest dilution with a visible line in 3/3 replicates) | Y (PVA, PVM, PVS, PLRV, healthy) | P (n = 3 per dilution; batch consistency not assessed) | N | N (stated as not evaluated) |

## Items still to verify before this section is final
1. R08369 (DOI: 10.3390/plants15040656): the dilution exponents are lost in the retrieved text (chart values 1e3 and 1e4).
2. R08742 (DOI: 10.1016/j.talanta.2026.130562) and R08764 (DOI: 10.1016/j.ab.2026.116259): records show a 2027 year; check the publication dates.
3. R04627 (DOI: 10.1021/acsanm.1c03217): read-out by thermal contrast, not colour; boundary case, may be moved to the supplement.
4. R02642 (DOI: 10.1002/jmv.25452): the amplification mechanism is not stated in the abstract.
5. R07744, R08107, R08737 combine viral and bacterial targets and R08826 does not name its viruses in the abstract; viral target retained, flagged.
6. Seven marketed-kit evaluations were excluded (E10) by default; reversible.
7. Record IDs in the tables will be replaced by numbered citations when the reference list is built.
