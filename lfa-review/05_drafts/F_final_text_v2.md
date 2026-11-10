# Part F (working text v2): readers, smartphones and AI and the colorimetric signal

Working text, 2026-11-10. Reframed around the question of this review. In this section the strip itself is usually unchanged; what changes is how its colour is read. Each subsection follows four questions: what limits the reading of the colour, which reader or algorithm addresses it, what the paper reports against visual reading or another reference, and what it costs. The target virus is named for every method. Numbers are in the tables, and Table F4 gathers the comparisons with visual reading. † = read in full; all other rows abstract only (NR = not reported in the abstract). Every DOI cited in the text appears in a table and in the evidence table. The section covers 55 included records, all from 2015-2026; one was read in full. Nine of them read the strip by a principle other than colour (heat, photon counting, SERS, electron microscopy); under the rule that only the colorimetric reading is counted, they are described in 3.6.2 and not used as results.

# 3.6 Reading the colour: readers, smartphones and AI

## 3.6.0 What limits the reading of the colour, and how this section is organised

A conventional strip is read by eye, which is quick but subjective. Weak lines are the main source of disagreement: in the HIV field study discussed below, visual agreement between five readers ranged from 61% to 100% depending on test type and training (DOI: 10.1038/s41591-021-01384-9). Reading technology addresses two limits: the subjectivity of a faint line, and the lack of a number. It does not make the line stronger. The improvements reported here are therefore improvements in the call (sensitivity, specificity or agreement against a reference) and in quantification, and they come at the cost of a device or software.

The section moves from the simplest to the most complex intervention. Dedicated readers and spectrometers come first (3.6.1), then readers that use another physical principle than colour (3.6.2). Smartphone-based quantification follows (3.6.3), then machine-learning interpretation of strip images (3.6.4), and finally studies that use the time of line appearance as a signal (3.6.5). Section 3.6.6 states what the evidence supports. Many studies apply readers or algorithms to commercial strips; they are retained when the reading technology itself is the contribution.

**How the signal is read.** Reading the abstracts: 36 records state that the colour is read with a device or algorithm, 2 state reading by eye, 8 describe a strip without saying how it is read, 0 has no abstract, and 9 read the strip by a principle other than colour (marked in the tables and not counted). The record read in full (R04048) gives its reading mode from the full text.

## 3.6.1 Dedicated readers and spectrometers

Limit addressed: the visual call and the absence of a number. Strategy: a portable optical reader or spectrometer measures the colour of the line.

**HIV.** The Fio Deki reader used with HIV rapid tests gave, for one test version, sensitivity 99.5% and specificity 99.4%, for another sensitivity 100% and specificity 93.1%, and in the field sensitivity 99.8% and specificity 97.7% in South Africa (DOI: 10.1186/s12879-020-4932-0). A smartphone e-reader read dual HIV and syphilis rapid tests in men who have sex with men and transgender women in Lima, with HIV sensitivity of 98% (DOI: 10.1136/sextrans-2017-053511). Two HIV antibody tests (TRUSTline HIV-1/2 and OnSite HIV 1/2 Ab Plus Combo) were compared by visual reading and with the ALTA reader, with sensitivity of 100% for both and specificity 99.6% and 100% (DOI: 10.1016/j.ijmmb.2022.05.011). A microfluidic cassette with a handheld optical reader targeted HIV in urine, with no values in the abstract (DOI: 10.1007/s10544-020-00494-4).

**SARS-CoV-2 antibodies and neutralising antibodies.** The pandemic produced the largest cluster of reader studies. A point-of-care system reading nucleocapsid and spike IgG/IgM agreed with a chemiluminescence immunoassay with a kappa of 0.804 on 108 suspicious samples (DOI: 10.1016/j.snb.2020.129415). A spectrochip-coupled quantitative strip gave a limit of 186 pg/mL for spiked recombinant IgG, and a newly designed spectrometer was built for SARS-CoV-2 immunoglobulin strips, with no values in the abstract (DOI: 10.3390/mi12030321; DOI: 10.1371/journal.pone.0254486). A commercial strip with a spectrum-based reader classified neutralising-antibody status in 30 patients and 16 vaccinees with an AUC of 0.989 (sensitivity 100%, specificity 87.5%) (DOI: 10.3390/vaccines10020271); a quantitative spectrometer readout was tested on 69 sera including AstraZeneca vaccinees (DOI: 10.12659/msm.935812); the TestNOW system with the RapiRead reader was tested on 94 samples (DOI: 10.1007/s00705-022-05422-w); the ichroma semiquantitative strip correlated with IgG (rho 0.83) and with anti-Alpha neutralising antibodies (rho 0.78) (DOI: 10.1016/j.jcv.2022.105268); a lateral flow with a spectrum reader set sRBD IgG thresholds of 60.15 to 230.20 ng/mL in maternal and cord blood (DOI: 10.3390/bios12100891); a POCT with a traceable RBD-IgG calibrator linked strip results to international units in 37 vaccinated people, with levels of 0.45 to 2.46 ug/mL in 33 of 37 (DOI: 10.1007/s00604-023-06004-6); the ichroma COVID-19 nAb surrogate strip showed high specificity in several cohorts (DOI: 10.3390/life14070791); a strip with spectrophotometric measurement gave results similar to ELISA, PPV 99.0%, on 274 plasma samples (DOI: 10.1038/s41598-025-90730-9); and a flow-based sqLFA platform reached specificity 80% and sensitivity 90% at a microneutralisation cut-off of 1:40 (DOI: 10.20411/pai.v11i1.910). The improvement across these studies is a quantitative value that can be calibrated against neutralisation assays or ELISA.

**African swine fever virus and influenza.** An ASFV antigen strip with an iaX reader gave, on serum, sensitivity 100% and specificity 91%, and on whole blood sensitivity 79% and specificity 95% against qPCR (DOI: 10.1016/j.jviromet.2026.115424). A centrifugal chip with a nanozyme ELISA-like assay for influenza read by a reader reached a 2.5-fold lower LOD than eye observation (DOI: 10.1039/d5an00237k).

Cost: a device per reader, calibration, and, for many of these studies, a commercial strip whose chemistry is unchanged, so the gain describes the reader and not the strip.

## 3.6.2 Readers that do not read the colour (not counted as colorimetric results)

Nine studies read the same gold-labelled strip with a different physical principle. Under the rule of this review that only the colorimetric reading is counted, their figures are described here but not used as results. Thermal-contrast amplification heats the gold particles with a laser and measures the temperature rise: it improved sensitivity on a commercial influenza A and B strip against PCR (value not given) and detected HIV p24 at 8 pg/mL in spiked serum (DOI: 10.3390/diagnostics11030462; DOI: 10.1038/s41378-020-0168-9). A thermometric strip with coloured latex beads detected 1 x 10^5 particles/mm2 for SARS-CoV-2, which the abstract states is ten times better than colour reading (DOI: 10.1038/s41598-022-07963-1), and two handheld thermo-photonic readers measured SARS-CoV-2 antibody titers in RBD IgG standards or in ICU patients (DOI: 10.1109/jsen.2021.3089016; DOI: 10.3390/biomedicines10061424). A photon-counting readout increased the sensitivity of a SARS-CoV-2 antibody strip (value not given) (DOI: 10.1063/5.0021842). A portable SERS reader read commercial colorimetric strips for SARS-CoV-2 and classified 54 clinical samples (49 positive, 5 negative) (DOI: 10.1021/acssensors.2c01808), and two studies used desktop scanning electron microscopy to read gold/platinum particle strips for influenza A and SARS-CoV-2, with sensitivities of 94% (29/31) and 86.7% (26/30) against visual results or qRT-PCR (DOI: 10.1016/j.jpba.2021.113924; DOI: 10.3390/biomedicines10020447). These approaches raise sensitivity but give up the colorimetric, equipment-free reading.

## 3.6.3 Smartphone-based quantification

Limit addressed: the cost of a dedicated reader. Strategy: a phone camera and software read the line, sometimes with a holder or colour calibration. A smartphone reader and app quantified Ebola virus IgG and distinguished 15 survivors from 5 controls in Uganda, with a glycoprotein assay of sensitivity 100% and specificity 98% against ELISA (DOI: 10.1021/acsnano.7b07021). A smartphone add-on and app measured nucleic-acid lateral flow assays with colour calibration, with a predicted-versus-true concentration of R2 = 0.96 (DOI: 10.1002/elps.201800449). A smartphone quantification method for SARS-CoV-2 antibody strips was applied to 800 serum samples and 100 health-care workers (values not in the abstract) (DOI: 10.1016/j.diagmicrobio.2023.116166). A paper analytical device with a smartphone app read dengue virus NS1 colorimetrically from clinical samples (DOI: 10.3791/66130). Low-cost hardware appears in a Raspberry Pi reader for SARS-CoV-2 nucleic-acid lateral flow assays with spiked-sample recoveries of 84 to 108% (DOI: 10.3390/s26020598) and an open-source fluid handler for automating strips for dengue virus and ASFV (DOI: 10.1371/journal.pgph.0002625); an image-recognition app for multianalyte strips was developed for infectious diseases without naming the viruses in the abstract (DOI: 10.1021/acs.analchem.5c01487). Cost: phone and lighting variability, which is a recurring limit and is not quantified in these abstracts.

## 3.6.4 Machine-learning interpretation of strip images

Limit addressed: the subjective call of a faint line, often by an untrained user. Strategy: an algorithm decides positive or negative from an image.

**HIV.** A field-scale example, read in full, is the deep-learning classifier for HIV rapid tests in rural South Africa (DOI: 10.1038/s41591-021-01384-9). Sixty fieldworkers took 11,374 photographs of two HIV test types with a tablet, a MobileNetV2 network was trained to classify them as positive or negative, and in a pilot with five readers (two nurses, three community health workers) on 190 tests the algorithm gave a sensitivity of 97.8% and a specificity of 100%, against 95.6% and 89% for visual reading, with 0 false positives against 11 by eye (DOI: 10.1038/s41591-021-01384-9). The authors note the limits: five participants, no invalid-result class, and processing on a server (DOI: 10.1038/s41591-021-01384-9). A nanotrap enrichment was combined with an AI smartphone reader on commercial HIV antibody strips, with about 20-fold enrichment and detection 8 days earlier (DOI: 10.1021/acsnano.6c01808).

**SARS-CoV-2.** AI interpretation was developed for serological rapid tests (DOI: 10.1073/pnas.2019893118), for home antibody tests, where the ALFA machine-learning system reached kappa 0.90 to 0.97 against experts (specificity 98.7 to 99.4%, sensitivity 90.1 to 97.1%) (DOI: 10.1038/s43856-022-00146-z), and for antigen tests: LFAIR reported sensitivity 86.2% and specificity 94.3% against same-day RT-PCR (DOI: 10.1016/j.diagmicrobio.2022.115763), and a machine-learning system for lateral flow devices reported a sensitivity of 92.08% to 97.6% in asymptomatic people, with a much lower figure (16.00% to 100%) for self-reading (DOI: 10.1016/j.xcrm.2022.100784). A smartphone AI reader of antibody rapid tests reported IgG-band sensitivity of 100% and specificity of 94.4% against visual reading (IgM 100% and 95.8%) (DOI: 10.2196/38533). Algorithmic work on SARS-CoV-2 images includes a lightweight YOLOv5 detector for rapid-test images (DOI: 10.1016/j.displa.2023.102403), a deep-learning smartphone LFA (DOI: 10.1038/s41467-023-38104-5), automated interpretation across point-of-care diagnostics (DOI: 10.1038/s43856-023-00312-x), the SCAISY smartphone AI quantification of IgG (DOI: 10.3390/bios13060623) and a CNN with StyleGAN2 classification of test images (abstract incomplete) (DOI: 10.3389/frai.2023.1235204). A comparison of AI-assisted and visual reading of at-home antigen tests reported AI accuracy of 96.97% (sensitivity 80%, specificity 100%) against 68.82% (78.57%, 67.09%) by eye (DOI: 10.1016/j.diagmicrobio.2026.117414), and a computer-vision method decoded BinaxNOW images to estimate viral load within an RMSE of 1.44 Ct (DOI: 10.1186/s44247-026-00287-4). An AI-assisted colorimetric strip with polydopamine nanoparticles read SARS-CoV-2 neutralising antibodies on 50 clinical sera and agreed with a commercial ELISA (160 ng/mL, range 625 to 10,000 ng/mL) (DOI: 10.1016/j.bios.2022.114449).

**Influenza, ASFV, HPV and multi-analyte.** A computer-vision-assisted LFA for influenza A and SARS-CoV-2 gave a 3-fold gain in analytical sensitivity (DOI: 10.1039/d3an01189e), machine learning read a CRISPR-Cas12a strip for HPV DNA on 60 validation plasma samples with 96.7% sensitivity and 100% specificity (DOI: 10.1016/j.bios.2026.118765), and a smartphone AI read ASFV strips, with accuracy metrics not given in the abstract (DOI: 10.2460/ajvr.24.10.0305).

Cost: training data from one source, few tests with naive users on other phones, and processing on a server in some designs.

## 3.6.5 Using the time of appearance as a signal

Limit addressed: a positive/negative call hides information on viral load. Strategy: record how fast the line becomes visible. For SARS-CoV-2 antigen strips, the time to visible positivity predicted viral load: for the Roche antigen test a cut-off of 32 seconds gave sensitivity 94.9% and specificity 58.2% (AUC 0.82) (DOI: 10.5937/jomb0-35482); for COVID-VIRO ALL IN the positivisation time reached accuracy 93.7% for samples above 1500 TCID50/mL (PMID: 36605302; no DOI recorded); and in routine samples the positivisation time gave 0.84 sensitivity and 0.73 specificity for Ct below 20 (DOI: 10.1515/cclm-2022-0873). The reading remains visual; the new information is the time.

## 3.6.6 What the evidence supports

For the question of this review, reading technology does not strengthen the colour; it makes the call objective and, where a calibrator exists, quantitative. The best-supported results are the HIV field study and the SARS-CoV-2 reader studies that benchmark against ELISA, neutralisation tests or a chemiluminescence immunoassay (Table F4). Where a paper compares the algorithm with visual reading, the algorithm is better: 97.8% against 95.6% sensitivity for HIV tests, and 96.97% against 68.82% accuracy for SARS-CoV-2 at-home tests. Three cautions apply. First, many studies apply readers to commercial strips, so their gains describe the reader and not the strip. Second, readers that use another physical principle (3.6.2) are not colorimetric and are not counted. Third, AI studies often train and test on images from the same source, and few report accuracy on images taken by naive users with other phones.

### Table F4. Reported comparison of the reading technology with visual reading or another reference

Only studies that state a comparison in the abstract are listed. Reference methods differ and the rows cannot be ranked. † = read in full.

| Rec | Virus (target) | Reading technology | Comparator in the same paper | Reported result | DOI |
|---|---|---|---|---|---|
| R04048 † | HIV | deep-learning classifier on tablet images | visual reading by five users; ELISA | sensitivity 97.8%, specificity 100% vs 95.6% and 89%; 0 vs 11 false positives | 10.1038/s41591-021-01384-9 |
| R08464 | SARS-CoV-2 (antigen) | AI-assisted reading, at-home test | visual reading | accuracy 96.97% (sens 80%, spec 100%) vs 68.82% (78.57%, 67.09%) | 10.1016/j.diagmicrobio.2026.117414 |
| R05633 | SARS-CoV-2 (antibodies) | smartphone AI reader | visual reading | IgG band sens 100%, spec 94.4%; IgM 100%, 95.8% | 10.2196/38533 |
| R05611 | SARS-CoV-2 (antigen) | machine learning for lateral flow devices | self-reading | sens 92.08% to 97.6% with the algorithm; self-reading 16.00% to 100% | 10.1016/j.xcrm.2022.100784 |
| R05282 | SARS-CoV-2 (antibodies) | ALFA machine learning, home tests | expert readers | kappa 0.90 to 0.97 | 10.1038/s43856-022-00146-z |
| R05492 | SARS-CoV-2 (antigen) | LFAIR, smartphone AI | same-day RT-PCR | sens 86.2%, spec 94.3% | 10.1016/j.diagmicrobio.2022.115763 |
| R06579 | influenza A and SARS-CoV-2 | computer-vision-assisted LFA | conventional LFA | 3-fold gain in analytical sensitivity | 10.1039/d3an01189e |
| R08461 | HIV (antibodies) | nanotrap + AI smartphone reader | commercial strip alone | about 20-fold enrichment; detection 8 days earlier | 10.1021/acsnano.6c01808 |
| R07826 | influenza | reader on nanozyme chip | eye observation | 2.5-fold lower LOD | 10.1039/d5an00237k |
| R05199 | HIV (antibodies) | ALTA reader | visual reading | TRUSTline sens 100%, spec 99.6%; OnSite 100%/100% | 10.1016/j.ijmmb.2022.05.011 |
| R03592 | SARS-CoV-2 (IgG/IgM) | point-of-care reader | chemiluminescence immunoassay | kappa 0.804, 108 samples | 10.1016/j.snb.2020.129415 |
| R04829 | SARS-CoV-2 (neutralising antibodies) | spectrum-based reader | neutralisation assay | AUC 0.989; sens 100%, spec 87.5% | 10.3390/vaccines10020271 |
| R05445 | SARS-CoV-2 (neutralising antibodies) | ichroma reader | IgG; anti-Alpha neutralising antibodies | rho 0.83; rho 0.78 | 10.1016/j.jcv.2022.105268 |
| R05738 | SARS-CoV-2 (antigen) | positivisation time, Roche test | RT-PCR Ct | AUC 0.82; 32 s cut-off sens 94.9%, spec 58.2% | 10.5937/jomb0-35482 |


### Table F1a. Dedicated readers and spectrometers

| Rec | Year | Target | Strip / reading technology | Matrix | LOD or analytical result (as stated) | Within-paper comparison | Diagnostic data (as stated) | How the signal is read (from abstract) | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R02989 | 2020 | HIV | Fio Deki Reader for HIV RDTs | lab and field, South Africa | NR | NR | V100 sens 99.5%, spec 99.4%; V200 sens 100%, spec 93.1%; field sens 99.8%, spec 97.7% | colour read with a device or algorithm (stated) | Abstract | 10.1186/s12879-020-4932-0 |
| R02452 | 2018 | HIV, syphilis | dual RDTs with smartphone e-reader | MSM and transgender women, Lima | NR | NR | HIV sens 98% (93-100) | colour read with a device or algorithm; eye also stated | Abstract | 10.1136/sextrans-2017-053511 |
| R05199 | 2022 | HIV | TRUSTline HIV-1/2 Ab, OnSite HIV 1/2 Ab Plus Combo, ALTA reader | NR | NR | NR | TRUSTline sens 100%, spec 99.6%; OnSite 100%/100% | colour read with a device or algorithm; eye also stated | Abstract | 10.1016/j.ijmmb.2022.05.011 |
| R03015 | 2020 | HIV (urine) | microfluidic cassette with handheld reader | NR | NR | NR | NR | colour read with a device or algorithm; eye also stated | Abstract | 10.1007/s10544-020-00494-4 |
| R03592 | 2021 | SARS-CoV-2 IgG/IgM | POC system N and S proteins | 108 suspicious samples | not reported | NR | kappa 0.804 vs CLIA | colour read with a device or algorithm (stated) | Abstract | 10.1016/j.snb.2020.129415 |
| R03791 | 2021 | SARS-CoV-2 IgG | spectrochip-coupled quantitative LFIA | spiked recombinant IgG | 186 pg/mL | NR | NR | strip read by eye (stated) | Abstract | 10.3390/mi12030321 |
| R04162 | 2021 | SARS-CoV-2 immunoglobulins | LFIA with newly designed spectrometer | NR | NR | NR | NR | colour read with a device or algorithm; eye also stated | Abstract | 10.1371/journal.pone.0254486 |
| R04829 | 2022 | SARS-CoV-2 neutralizing antibodies | commercial LFIA + spectrum-based reader | 30 patients; 16 vaccinees | NR | NR | AUC 0.989; sens 100%, PPV 95.7%, spec 87.5%, NPV 100% | colour read with a device or algorithm; eye also stated | Abstract | 10.3390/vaccines10020271 |
| R04938 | 2022 | SARS-CoV-2 neutralizing antibodies | LFIA kit + spectrometer readout, quantitative | 69 sera incl. AZ vaccinees | NR | NR | NR | colour read with a device or algorithm (stated) | Abstract | 10.12659/msm.935812 |
| R04958 | 2022 | SARS-CoV-2 neutralising Ab | TestNOW quantitative LFIA with RapiRead reader | 94 samples | not reported | NR | ROC-based sens and spec (values not in abstract) | colour read with a device or algorithm (stated) | Abstract | 10.1007/s00705-022-05422-w |
| R05445 | 2022 | SARS-CoV-2 NAbs | ichroma semiquantitative LFA | post-infection and vaccinated | not reported | NR | inhibition rate vs IgG rho 0.83; anti-Alpha NAbs rho 0.78 | strip; reading mode not stated in abstract | Abstract | 10.1016/j.jcv.2022.105268 |
| R07198 | 2024 | SARS-CoV-2 NAbs | ichroma COVID-19 nAb surrogate LFA | various cohorts | not reported | NR | high specificity | strip; reading mode not stated in abstract | Abstract | 10.3390/life14070791 |
| R07596 | 2025 | SARS-CoV-2 neutralizing Ab | LFIA + spectrophotometric measurement | 274 plasma | similar to ELISA | NR | PPV 99.0% | strip; reading mode not stated in abstract | Abstract | 10.1038/s41598-025-90730-9 |
| R05658 | 2022 | SARS-CoV-2 neutralizing antibodies | LFI with spectrum reader | maternal and cord blood, 20 mothers | NR | NR | sRBD IgG thresholds 60.15-230.20 ng/mL | colour read with a device or algorithm (stated) | Abstract | 10.3390/bios12100891 |
| R08360 | 2026 | SARS-CoV-2 neutralizing Ab | sqLFA flow-based platform | not reported | not reported | NR | spec 80%, sens 90% at MN cutoff 1:40 | strip; reading mode not stated in abstract | Abstract | 10.20411/pai.v11i1.910 |
| R06526 | 2023 | SARS-CoV-2 RBD-IgG | POCT with traceable RBD-IgG calibrator | 37 post-vaccination fingertip blood samples | 0.39 ug/mL | NR | levels 0.45-2.46 ug/mL in 33/37 | colour read with a device or algorithm (stated) | Abstract | 10.1007/s00604-023-06004-6 |
| R08556 | 2026 | ASFV | ASFV Ag LFA + iaX reader | serum, whole blood | not reported | NR | serum sens 100% (0.92-1.00), spec 91%; whole blood sens 79%, spec 95% vs qPCR | colour read with a device or algorithm (stated) | Abstract | 10.1016/j.jviromet.2026.115424 |
| R07826 | 2025 | influenza | centrifugal chip nanozyme ELISA-LFIA | not reported | 2.5x lower LOD vs eye observation | NR | not reported | colour read with a device or algorithm; eye also stated | Abstract | 10.1039/d5an00237k |

### Table F1b. Readers using a non-colour principle (thermal, photon, SERS, electron microscopy)

| Rec | Year | Target | Strip / reading technology | Matrix | LOD or analytical result (as stated) | Within-paper comparison | Diagnostic data (as stated) | How the signal is read (from abstract) | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R03788 | 2021 | influenza A/B | QuickVue + thermal contrast amplification | clinical samples | improved sensitivity (value NR) | NR | vs PCR | not colour: read by another principle (not counted) | Abstract | 10.3390/diagnostics11030462 |
| R04362 | 2020 | HIV p24 | thermal contrast amplification LFA | spiked serum | 8 pg/mL | NR | NR | not colour: read by another principle (not counted) | Abstract | 10.1038/s41378-020-0168-9 |
| R04887 | 2022 | SARS-CoV-2 | thermometric LFIA with coloured latex beads | NR | 1 x 10^5 particles/mm2 (10x better than colour reading) | NR | NR | not colour: read by another principle (not counted) | Abstract | 10.1038/s41598-022-07963-1 |
| R05112 | 2021 | SARS-CoV-2 antibodies | handheld thermo-photonic reader for commercial LFA | RBD IgG standards | clinically relevant range (value NR) | NR | NR | not colour: read by another principle (not counted) | Abstract | 10.1109/jsen.2021.3089016 |
| R05244 | 2022 | SARS-CoV-2 Ab | handheld thermo-photonic device for antibody titers | ICU patients | not reported | NR | not reported | not colour: read by another principle (not counted) | Abstract | 10.3390/biomedicines10061424 |
| R03295 | 2020 | SARS-CoV-2 antibodies | photon-counting readout of LFA | NR | enhanced sensitivity (value NR) | NR | NR | not colour: read by another principle (not counted) | Abstract | 10.1063/5.0021842 |
| R05731 | 2022 | SARS-CoV-2 | portable SERS-LFA reader on commercial colorimetric strips | 54 clinical samples | NR | NR | 49 positive, 5 negative | not colour: read by another principle (not counted) | Abstract | 10.1021/acssensors.2c01808 |
| R03638 | 2021 | influenza A | Au/Pt particle LFA read by desktop SEM | clinical samples | NR | NR | SEM sens 94% (29/31), spec 100% vs visual 14.3% | not colour: read by another principle (not counted) | Abstract | 10.1016/j.jpba.2021.113924 |
| R04816 | 2022 | SARS-CoV-2 | Au/Pt particle LFA read by desktop SEM (LFA-NanoSuit) | clinical samples | NR | NR | LNSM sens 86.7% (26/30), spec 93.3% (14/15) vs qRT-PCR | not colour: read by another principle (not counted) | Abstract | 10.3390/biomedicines10020447 |

### Table F1c. Smartphone quantification and low-cost readers

| Rec | Year | Target | Strip / reading technology | Matrix | LOD or analytical result (as stated) | Within-paper comparison | Diagnostic data (as stated) | How the signal is read (from abstract) | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R02299 | 2018 | Ebola virus IgG | immunochromatographic strip + smartphone reader | 15 survivors, 5 controls, Uganda | NR | NR | GP monoplex sens 100%, spec 98% vs ELISA | colour read with a device or algorithm (stated) | Abstract | 10.1021/acsnano.7b07021 |
| R02532 | 2019 | nucleic acids (lateral flow) | smartphone add-on and app for LF nucleic acid assays | NR | NR | NR | predicted vs true concentration R2 0.96 | colour read with a device or algorithm; eye also stated | Abstract | 10.1002/elps.201800449 |
| R06721 | 2024 | SARS-CoV-2 Ab | smartphone quantification of antibody LFAs | 800 serum samples, 100 HCPs | not reported | NR | not reported in abstract | colour read with a device or algorithm; eye also stated | Abstract | 10.1016/j.diagmicrobio.2023.116166 |
| R06817 | 2024 | dengue NS1 | DEN-NS1-PAD paper analytical device with smartphone app | clinical samples | NR | NR | NR | colour read with a device or algorithm; eye also stated | Abstract | 10.3791/66130 |
| R08297 | 2026 | SARS-CoV-2 | Raspberry Pi NALFA reader | spiked | recoveries 84-108% | NR | not reported | colour read with a device or algorithm; eye also stated | Abstract | 10.3390/s26020598 |
| R07432 | 2024 | dengue, ASFV | open-source fluid handler for LFA | not reported | not reported | NR | not reported | colour read with a device or algorithm (stated) | Abstract | 10.1371/journal.pgph.0002625 |

### Table F1d. Machine-learning interpretation and time-to-signal

| Rec | Year | Target | Strip / reading technology | Matrix | LOD or analytical result (as stated) | Within-paper comparison | Diagnostic data (as stated) | How the signal is read (from abstract) | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R04048 | 2021 | HIV antibodies (rapid tests, two types) | MobileNetV2 deep-learning classifier of tablet photographs; Android app | 11,374 field photographs (training); pilot: discarded anonymised blood samples (10 positive, 10 negative per ELISA) on two HIV test types | not applicable (reading step) | algorithm vs visual reading by five users: sens 97.8% vs 95.6%; spec 100% vs 89%; false positives 0 vs 11; accuracy 98.9% vs 92.1% | 10-fold cross-validation: type A sens 95.9% +/- 5.1, spec 99.0% +/- 0.6; type B sens 98.7% +/- 1.7, spec 99.8% +/- 0.2; pilot 190 tests, five readers | tablet camera + server-side classifier (full text) | Full text † | 10.1038/s41591-021-01384-9 |
| R03705 | 2021 | SARS-CoV-2 serology | AI interpretation of RDT results | NR | NR | NR | NR | colour read with a device or algorithm; eye also stated | Abstract | 10.1073/pnas.2019893118 |
| R05282 | 2022 | SARS-CoV-2 antibodies | ALFA machine learning for home LFIA interpretation | home self-tests | NR | NR | kappa 0.90-0.97 vs experts; spec 98.7-99.4%, sens 90.1-97.1% | colour read with a device or algorithm; eye also stated | Abstract | 10.1038/s43856-022-00146-z |
| R05492 | 2022 | SARS-CoV-2 antigen | at-home LFA with AI read (LFAIR) | same-day RT-PCR | not reported | NR | sens 86.2% (73.6-98.8), spec 94.3%; 97.8% day 1 | strip; reading mode not stated in abstract | Abstract | 10.1016/j.diagmicrobio.2022.115763 |
| R05611 | 2022 | SARS-CoV-2 antigen | ML for determining LFD results | asymptomatic populations | not reported | NR | ATS sens 92.08% to 97.6%; self-read 16.00% to 100% | colour read with a device or algorithm (stated) | Abstract | 10.1016/j.xcrm.2022.100784 |
| R05633 | 2022 | SARS-CoV-2 Ab | smartphone AI reader for RDTs | field studies | not reported | NR | IgG band sens 100%, spec 94.4%; IgM 100%, 95.8% vs visual | colour read with a device or algorithm; eye also stated | Abstract | 10.2196/38533 |
| R06053 | 2023 | SARS-CoV-2 RDT images | LightR-YOLOv5 detector for RDT result classification | RDT images | NR | NR | NR | colour read with a device or algorithm (stated) | Abstract | 10.1016/j.displa.2023.102403 |
| R06147 | 2023 | SARS-CoV-2 | deep learning smartphone LFA (SMART-AI-LFA) | clinical samples | NR | NR | NR | colour read with a device or algorithm (stated) | Abstract | 10.1038/s41467-023-38104-5 |
| R06292 | 2023 | SARS-CoV-2 RDTs | automated interpretation of POC diagnostics | NR | NR | NR | NR | colour read with a device or algorithm; eye also stated | Abstract | 10.1038/s43856-023-00312-x |
| R06303 | 2023 | SARS-CoV-2 IgG | SCAISY smartphone AI quantification of IgG LFA | NR | NR | NR | NR | colour read with a device or algorithm (stated) | Abstract | 10.3390/bios13060623 |
| R06820 | 2023 | SARS-CoV-2 LFT images | deep CNN and StyleGAN2 image classification | LFT images | not reported | NR | not reported | colour read with a device or algorithm (stated) | Abstract | 10.3389/frai.2023.1235204 |
| R08464 | 2026 | SARS-CoV-2 antigen | AI-assisted vs visual reading of at-home test | home testing | not reported | NR | AI accuracy 96.97%, sens 80%, spec 100%; visual 68.82%, 78.57%, 67.09% | strip read by eye (stated) | Abstract | 10.1016/j.diagmicrobio.2026.117414 |
| R08695 | 2026 | SARS-CoV-2 antigen | computer vision decoding BinaxNOW | user images | viral load estimate within RMSE 1.44 Ct | NR | not reported | colour read with a device or algorithm (stated) | Abstract | 10.1186/s44247-026-00287-4 |
| R06579 | 2023 | influenza A, SARS-CoV-2 | computer-vision-assisted LFA | patient samples | 3-fold gain in analytical sensitivity | NR | NR | colour read with a device or algorithm; eye also stated | Abstract | 10.1039/d3an01189e |
| R05213 | 2022 | SARS-CoV-2 neutralizing antibodies | AI-assisted colorimetric LFIA with polydopamine nanoparticles | 50 clinical sera | 160 ng/mL (range 625-10,000 ng/mL) | NR | consistent with commercial ELISA | colour read with a device or algorithm; eye also stated | Abstract | 10.1016/j.bios.2022.114449 |
| R08461 | 2026 | HIV antibodies | nanotrap + AI smartphone reader on commercial LFAs | oral-fluid equivalent | ~20x enrichment; 8 days earlier detection | NR | not reported | colour read with a device or algorithm (stated) | Abstract | 10.1021/acsnano.6c01808 |
| R08500 | 2026 | HPV DNA | ML smartphone CRISPR-Cas12a LFA | 60 validation plasma | not reported | NR | sens 96.7%, spec 100% | colour read with a device or algorithm; eye also stated | Abstract | 10.1016/j.bios.2026.118765 |
| R07608 | 2025 | ASFV | smartphone AI to read LFAs | not reported | not reported | NR | accuracy metrics (values not in abstract) | colour read with a device or algorithm; eye also stated | Abstract | 10.2460/ajvr.24.10.0305 |
| R07836 | 2025 | infectious diseases (multi-analyte) | smartphone image recognition for multianalyte LFAs | real samples | not reported | NR | not reported | colour read with a device or algorithm; eye also stated | Abstract | 10.1021/acs.analchem.5c01487 |
| R05678 | 2023 | SARS-CoV-2 antigen | RDT positivization time predicts viral load | routine samples | not reported | NR | 0.84 sens, 0.73 spec for Ct<20 | strip; reading mode not stated in abstract | Abstract | 10.1515/cclm-2022-0873 |
| R05738 | 2022 | SARS-CoV-2 antigen | positivization time of Roche RAT | NP specimens | not reported | NR | AUC 0.82; 32 s cut-off sens 94.9%, spec 58.2% | strip; reading mode not stated in abstract | Abstract | 10.5937/jomb0-35482 |
| R05854 | 2022 | SARS-CoV-2 antigen | COVID-VIRO ALL IN positivization time | paired samples | >1500 TCID50/mL (Liaison) | NR | accuracy 93.7% | strip; reading mode not stated in abstract | Abstract | PMID 36605302 (no DOI) |

### Table F2. Strategy overview for reading technologies

| Approach | What it adds | Examples | Costs and limits seen | Table |
|---|---|---|---|---|
| Dedicated readers and spectrometers | objective, quantitative reading of existing strips | HIV rapid tests, SARS-CoV-2 antibody and neutralisation strips | device cost; gains describe the reader, not the strip | F1a |
| Non-colour readers | higher sensitivity by thermal, photon, SERS or SEM readout | influenza, SARS-CoV-2, HIV p24 | not equipment-free; boundary to colorimetric reading | F1b |
| Smartphone quantification | camera and app replace a reader | Ebola IgG, dengue NS1, nucleic-acid strips | phone and lighting variability | F1c |
| Machine-learning interpretation | objective positive/negative call from an image | HIV and SARS-CoV-2 rapid tests, ASFV, CRISPR strips | training-data source; few tests with naive users | F1d |
| Time-to-signal | line appearance time as a viral-load proxy | SARS-CoV-2 antigen tests | moderate accuracy | F1d |

### Table F3. Reporting checklist for papers read in full (descriptive, not scored)

Items: (a) real samples; (b) n stated; (c) reference method; (d) LOD definition; (e) cross-reactivity tested by the authors; (f) replicates or reproducibility; (g) comparator run in the same study; (h) stability tested. Y = yes, N = no, P = partly, NR = not reported, NA = not applicable (reading step). All other papers have not been assessed (abstract only).

| Rec | DOI | (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) |
|---|---|---|---|---|---|---|---|---|---|
| R04048 | 10.1038/s41591-021-01384-9 | P (field photographs; pilot on discarded anonymised blood samples) | Y (11,374 images; 190 pilot tests) | Y (ELISA for samples; expert reading of images) | NA | NA | Y (10-fold cross-validation) | Y (visual reading by five users) | NA |

## Items still to verify before this section is final
1. Nine records (R03295, R03638, R03788, R04362, R04816, R04887, R05112, R05244, R05731) read the strip by heat, photon counting, SERS or electron microscopy; they are described in 3.6.2 and not counted as colorimetric results. The author should confirm this.
2. R06820 (abstract incomplete) and R07836 (viruses not named in the abstract) are flagged.
3. Most reader and AI studies are abstract level; accuracy figures are those stated in the abstract and were measured against different references.
4. The reading mode of 8 records is not stated in the abstract; full texts are needed (see the reminder in 07_open_questions.md).
5. Record IDs in the tables will be replaced by numbered citations when the reference list is built.
