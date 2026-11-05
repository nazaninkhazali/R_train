# Part D (working text v1): assay and flow engineering

Working text, 2026-11-05. Text focuses on the technologies and how they connect; numerical detail is in the tables. † = read in full; all other rows abstract only (NR = not reported in the abstract). Every DOI cited in the text appears in a table and in the evidence table. Section d covers 122 included records after the E9 exclusion of six antibody-screening papers.

# 3.4 Assay and flow engineering: designing the strip around the sample

## 3.4.0 Why look at the strip rather than the label, and how this section is organised

The sections so far changed what is on the strip: the particle, the colour carrier and the amplifier. This section looks at everything else that decides whether the label gets a chance to work. A sample has to enter the strip in a usable form, flow past the capture line for long enough, meet binders that recognise the target, and be read in a defined format. Performance can be limited by any of these steps, not only by the label.

The studies are organised along that path. They start with the flow inside the strip (3.4.1), then with concentrating the target before it enters (3.4.2), and with collecting and pre-treating the sample (3.4.3). They continue with the binders and antigens that give the strip its specificity (3.4.4), the assay formats built around them (3.4.5), and the many prototype strips that combine these elements for a new virus (3.4.6). Section 3.4.7 states what the evidence supports. Numerical details are in Tables D1a-D1f. Papers read in full are marked † in the tables; all other statements rest on abstracts. The section covers 122 included records, 99 of them from 2015-2026. Six records in which the strip was used only to screen antibodies or peptides were excluded (E9).

## 3.4.1 Controlling the flow inside the strip

Sensitivity depends on how long the sample is in contact with the capture line, so several designs slow or shape the flow. A delayed lateral flow design for SARS-CoV-2 spike RBD lowered the LOD and raised sensitivity against a conventional strip (DOI: 10.1007/s00604-022-05467-3), and dissolvable sugar barriers placed in the membrane did the same for a nucleic acid strip (DOI: 10.1016/j.carbpol.2021.118259). Other designs change the geometry: a tapered strip for dengue NS1 (DOI: 10.1063/1.5035113), a sponge for hepatitis B nucleic acid (DOI: 10.1038/s41598-017-01558-x), a paper network for influenza haemagglutinin (DOI: 10.1039/c8lc00691a), a paper-hydrogel hybrid for dengue RNA (DOI: 10.1002/adhm.201600920) and laser micro-machined channels (DOI: 10.1038/s41598-024-74407-3). Cost-efficient changes of strip design also raised the sensitivity of SARS-CoV-2 antigen tests (DOI: 10.1038/s41598-023-31641-5; DOI: 10.3390/bios14060305).

A second family moves the sample through the paper in another direction. Vertical-flow cellulose assays were used for SARS-CoV-2 antibodies and antigen and for Rift Valley fever virus, where a vertical-flow format was 2.5-fold more sensitive than a lateral-flow prototype (DOI: 10.1021/acssensors.1c00235; DOI: 10.1039/d2lc00073c; DOI: 10.1128/spectrum.00341-25), and a vertical-flow paper sensor combined colorimetric and electrochemical readout for influenza (DOI: 10.1016/j.bios.2018.10.008). A thermochromic strip was developed for dengue NS1, and a centrifugal microfluidic chip analysed Ebola virus-like particles by digital imaging (DOI: 10.1039/d3nr01858j; DOI: 10.1039/d3ay00073g). Low-cost fabrication tools, foil-based chips and cellulose test strips address manufacturing rather than sensitivity (DOI: 10.1021/acsomega.2c07014; DOI: 10.3390/bios15040229; DOI: 10.1007/s10570-022-04808-y; DOI: 10.18063/ijb.v7i4.399). These designs trade the one-step simplicity of a conventional strip for sensitivity or manufacturability; whether the trade is worth it depends on the setting.

## 3.4.2 Concentrating the target before the strip

The target concentration at the line can also be raised by enriching the sample before it reaches the strip. The simplest approach for the user is a front-end device that works with an unmodified commercial strip.

A nanoelectrokinetic preconcentrator coupled to a commercial SARS-CoV-2 IgG/IgM strip concentrated antibodies more than 30-fold on rolled paper discs under an electric field of about 70 V/cm and gave a 32-fold lower LOD (the signal appeared at 1/6,400 instead of 1/200 dilution of a vaccinated serum), with 95.7% extraction efficiency when the right paper was used (DOI: 10.1016/j.bios.2022.114385). In a pilot with sera from vaccinated people, four samples that the commercial strip did not detect became detectable (Table D1b). Another group enriched virus, nucleocapsid protein and IgG on a red-blood-cell-membrane-coated nanoporous aluminium oxide membrane under 3 bar of pressure in 3 minutes, again in front of a commercial strip (DOI: 10.1038/s41467-023-37018-6). The LOD improved up to 20-fold, and in 62 individuals the strip's sensitivity rose from 14.29% to 88.1% with 100% specificity (DOI: 10.1038/s41467-023-37018-6). The low-viral-load samples were partly produced by diluting positive swabs, and the device needs a pressure source and 3 mL of sample, which the authors recognise as limits for fingerstick serology (DOI: 10.1038/s41467-023-37018-6).

Related approaches use an osmotic processor, a non-powered preconcentrator, electrokinetic focusing by ion concentration polarization and an agglutination system for large sample volumes (DOI: 10.3389/fbioe.2022.884271; DOI: 10.1016/j.bios.2022.114965; DOI: 10.1039/d3ay00990d; DOI: 10.1016/j.aca.2023.341674), nanoelectrokinetic enhancement of nucleocapsid-protein strips (DOI: 10.1016/j.bios.2025.117357), electrophoresis-driven assembly of antibody-antigen complexes (DOI: 10.1021/acssensors.3c00130), electrophoretic DNA concentration, aqueous two-phase concentration of virus and paper-based concentration of HIV nucleic acid (DOI: 10.3390/s140304399; DOI: 10.1002/bit.25316; DOI: 10.1016/j.talanta.2016.02.017), and magnetic enrichment for potato virus X (DOI: 10.1016/j.talanta.2016.11.025; DOI: 10.1016/j.aca.2017.12.023). Most of these show an enrichment effect with spiked or reference samples; only a few include patient samples (Table D1b).

## 3.4.3 Collecting and treating the sample

The sample itself can be the main obstacle. Pre-treatment of whole blood was developed for hepatitis B antigen strips, and a processing method makes sputum usable for lateral flow detection of PEDV and MERS coronavirus (DOI: 10.1128/cdli.8.1.9-13.2001; DOI: 10.4110/in.2021.21.e11). A gargle with a bean extract replaced swab collection for SARS-CoV-2 (102 patients; high sensitivity in the first six days) (DOI: 10.1128/spectrum.01614-21), and a porous microneedle patch served for sampling in an antibody test (DOI: 10.1038/s41598-022-14725-6). Buffer composition and sample volume were optimised for SARS-CoV-2 IgG, for mpox and orthopoxviruses, and for a dengue serotype-specific NS1 assay that needed less sample (DOI: 10.1007/s13337-021-00669-4; DOI: 10.1128/spectrum.02456-24; DOI: 10.3390/bios15120802). Together they show that sample handling is itself a design variable (Table D1c).

## 3.4.4 Binders and antigens designed for the strip

The most numerous group concerns the molecules that give the strip its specificity. Many studies develop monoclonal antibody pairs or scFv fragments for a new target: SARS-CoV-2 nucleocapsid protein, hepatitis C core antigen, FeLV p27, Lassa virus nucleoprotein, Ebola glycoprotein, CCHFV nucleoprotein and others (DOI: 10.1002/jmv.27520; DOI: 10.1371/journal.pntd.0010311; DOI: 10.3390/microorganisms11102422; DOI: 10.3390/ph17081022; DOI: 10.1016/j.ab.2025.116013; DOI: 10.1128/jcm.00071-26; DOI: 10.1038/s41598-026-54470-8; DOI: 10.1038/s44298-026-00209-1; DOI: None; DOI: 10.1371/journal.pntd.0008364; DOI: 10.1093/jaoacint/qsaf105). Non-antibody binders are also used: aptamers and aptamer pairs for SARS-CoV-2 and dengue NS1 (DOI: 10.1093/jaoacint/qsae004; DOI: 10.1016/j.talanta.2024.126825; DOI: 10.1016/j.virol.2025.110688; DOI: 10.1186/s12879-025-11751-3; DOI: 10.1038/s41598-025-29869-4; DOI: 10.1080/15257770.2013.763976), an earlier nanobody strip improved by streptavidin-biotin capture (DOI: 10.1038/s41598-024-57230-8), a competitive strip with an affinity-engineered receptor for betacoronaviruses (DOI: 10.1016/j.bios.2026.118909), nanobodies for Zika NS1 and coronaviruses (DOI: 10.1021/acssynbio.4c00819; DOI: 10.1021/acssynbio.4c00592), an affibody that replaces the antibody directly (DOI: 10.1021/jacs.4c17452), the human ACE2 receptor as capture (DOI: 10.1016/j.bios.2020.112715), glycan recognition (DOI: 10.1021/acssensors.1c01470; DOI: 10.1021/acscentsci.1c01080), and a binder that recognises intact influenza virus particles (DOI: 10.1021/acs.analchem.7b00769). Orienting the antibody on the particle improved a SARS-CoV-2 strip (DOI: 10.1016/j.snb.2022.133245), and an extracellular-vesicle capture design links HIV to EV markers (DOI: 10.1016/j.vesic.2025.100084). Three further studies concern antigen engineering, an antibody against a drug-resistance-associated neuraminidase and genotype-specific bocavirus antibodies (DOI: 10.3390/biom13101524; DOI: 10.1038/s41467-020-17246-w; DOI: 10.1007/s12519-023-00697-8).

These papers establish what a strip can recognise; whether the strip then works depends on the assay format and the samples, which many of them do not report in the abstract (Table D1d).

## 3.4.5 Assay formats and functional assays

Formats go beyond the antigen sandwich. A half-strip format uses open reagents for nucleocapsid protein and Rift Valley fever antibodies (DOI: 10.1021/acs.analchem.0c01975; DOI: 10.3390/diagnostics12112664), a pipetting-based format runs the immunoreaction outside the strip (DOI: 10.1038/s41598-019-53083-8), and a comparison of three antibody formats found that one format was 15- and 255-fold more sensitive than the others on 22 sera (DOI: 10.3390/bios13070750). Functional formats measure neutralizing antibodies from a finger prick or from sera (DOI: 10.1016/j.jcv.2021.105024; DOI: 10.1016/j.crmeth.2022.100273; DOI: 10.2147/ijn.s408921). Serological and multiplex tests include a four-serotype dengue panel, a species-independent Rift Valley fever antibody test, a semi-quantitative visual antibody test, an HPV vaccination status test and an enhancement step for "silent" antibodies (DOI: 10.1128/spectrum.02796-22; DOI: 10.3390/v18030316; DOI: 10.1039/d3tb02895j; DOI: 10.1016/j.vaccine.2016.09.021; DOI: 10.3390/bios12070434). Plant virus assay engineering lowered the PVY LOD 60-fold in one study (DOI: 10.3390/s18113975).

Nucleic-acid targets were read on strips by hybridisation, with signal-amplifying DNA structures (a triplex enhanced assay, hybridisation chain reaction, net-shaped DNA nanostructures, an M13 scaffold) or new probe-anchoring methods (DOI: 10.3390/ijms232315258; DOI: 10.1021/acsinfecdis.2c00472; DOI: 10.1021/acs.analchem.3c03698; DOI: 10.1002/adhm.202504037; DOI: 10.3390/mi14101936; DOI: 10.1016/j.ijbiomac.2024.136945) (Table D1e). A caution applies to the functional and serological formats: their reference standards are different (neutralization tests, ELISA), so agreement figures cannot be compared with antigen strips.

## 3.4.6 Prototype and development strips

A large share of the records are strips developed for one virus by combining these elements, many of them evaluated on patient samples. Early work includes rotavirus, human metapneumovirus, norovirus, hepatitis C core antigen, H5 and pandemic H1N1 influenza, cytomegalovirus, hantavirus and SFTSV (DOI: 10.1016/0166-0934(94)90130-9; DOI: 10.1089/hyb.2006.034; DOI: 10.1373/clinchem.2007.091140; DOI: 10.1016/j.jviromet.2007.10.010; DOI: 10.1016/j.jviromet.2009.02.013; DOI: 10.1089/hyb.2009.0006; DOI: 10.1128/jcm.02262-09; DOI: 10.1097/qai.0b013e3181f1afbc; DOI: 10.1128/cvi.00269-10; DOI: 10.1111/j.1472-765x.2010.03002.x; DOI: 10.1016/j.jviromet.2011.02.007; DOI: 10.1111/j.1348-0421.2012.00455.x; DOI: 10.3892/ijmm.2012.1121; DOI: 10.1016/j.jviromet.2012.09.015; DOI: 10.1016/j.phrp.2013.10.006; DOI: 10.1155/2014/530621; DOI: 10.7754/clin.lab.2013.130342; DOI: 10.1186/1743-422x-11-87). The SARS-CoV-2 era added antigen strips and prototypes for variants, Omicron-specific detection and in-house antibody kits (DOI: 10.3390/bios10110161; DOI: 10.1016/j.ijid.2021.05.007; DOI: 10.1371/journal.pone.0258819; DOI: 10.3390/bios11120488; DOI: 10.48101/ujms.v127.8207; DOI: 10.1039/d1ra01361k; DOI: 10.3390/v14122609; DOI: 10.3390/vaccines11020303; DOI: 10.3389/fimmu.2023.1111644; DOI: 10.1002/open.202300120; DOI: 10.1186/s13568-023-01620-0; DOI: 10.1016/j.heliyon.2023.e20913; DOI: 10.1039/d3ay02075d; DOI: 10.1002/jmv.70374; DOI: 10.3390/v17071021). Their clinical sensitivities are reported in Table D1f and range widely; they are reported there, not ranked.

## 3.4.7 What the evidence supports

For this section front-end enrichment shows the largest gains without changing the label or the commercial strip, but its cost is hardware: electrodes, pressure and larger sample volumes. The two enrichment studies read in full show the pattern. Both used a commercial strip as the downstream test, both measured gains against that strip, and neither can be called equipment-free (Table D2).

Three limitations recur. First, many studies use reference or spiked samples; clinical samples are the exception among engineering papers. Second, several studies give only a fold-improvement and not the strip's accuracy on patients. Third, the antibody and binder papers rarely report the matrix, number of samples or reference method in their abstracts. For the two papers read in full, Table D3 lists the reporting items.



### Table D1a. Flow control and device architecture

| Rec | Year | Target | Label / device | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R02018 | 2017 | dengue virus RNA | NR | clinical samples | NR | NR | NR | visual (semi-quantitative) | Abstract | 10.1002/adhm.201600920 |
| R02122 | 2017 | HBV nucleic acid | NR | NR | improved analytical sensitivity (value NR) | NR | NR | visual | Abstract | 10.1038/s41598-017-01558-x |
| R02398 | 2018 | dengue NS1 | NR | NR | 4.9 ng/mL (~11-fold better than previously reported) | about 11-fold better than previously reported | NR | visual | Abstract | 10.1063/1.5035113 |
| R02604 | 2019 | influenza haemagglutinin | NR | spiked pediatric nasal swab | 4.45 x 10^2 TCID50/mL | NR | NR | visual | Abstract | 10.1039/c8lc00691a |
| R04042 | 2021 | COVID-19 nucleic acid | NR | NR | 0.5 nM vs 2.5 nM (5-fold) | 5-fold (0.5 vs 2.5 nM) | NR | visual | Abstract | 10.1016/j.carbpol.2021.118259 |
| R05533 | 2022 | SARS-CoV-2 spike RBD | NR | NR | 9.1-fold lower LOD, 2.6-fold higher sensitivity than conventional LFIA | 9.1-fold lower LOD; 2.6-fold higher sensitivity | NR | visual | Abstract | 10.1007/s00604-022-05467-3 |
| R06060 | 2023 | SARS-CoV-2 nucleocapsid | NR | NR | 2.0 ng/mL (4-fold improvement) | 4-fold improvement | NR | visual | Abstract | 10.1038/s41598-023-31641-5 |
| R07133 | 2024 | SARS-CoV-2 | NR | NR | 50 pg/mL (5-20x better than market kits) | 5-20x better than market kits | high specificity | visual | Abstract | 10.3390/bios14060305 |
| R07330 | 2024 | respiratory viruses/SARS-CoV-2 | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1038/s41598-024-74407-3 |
| R03802 | 2021 | SARS-CoV-2 antibodies | NR | clinical sera | NR | NR | consistent with bead-based chemiluminescence immunoassay | visual | Abstract | 10.1021/acssensors.1c00235 |
| R04839 | 2022 | SARS-CoV-2 N protein | NR | NR | NR | NR | NR | visual | Abstract | 10.1039/d2lc00073c |
| R07816 | 2025 | RVFV | not reported | not reported | 0.78 ng/mL (2.5x vs LFI prototype) | 2.5x vs lateral-flow prototype | not reported | visual | Abstract | 10.1128/spectrum.00341-25 |
| R02509 | 2019 | influenza H1N1 | HRP (colorimetric) + electrochemical | PBS, saliva | 1.34 PFU/mL (PBS), 2.27 PFU/mL (saliva) colorimetric | NR | NR | electrochemical and colorimetric | Abstract | 10.1016/j.bios.2018.10.008 |
| R06078 | 2023 | Zaire Ebola virus-like particles | gold nanoparticles | NR | NR | NR | NR | digital image analysis | Abstract | 10.1039/d3ay00073g |
| R06336 | 2023 | dengue NS1 (DENV2) | colorimetric thermal sensing | NR | 4x lower LOD than typical visual readout | NR | NR | visual | Abstract | 10.1039/d3nr01858j |
| R07716 | 2025 | SARS-CoV-2 serology | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.3390/bios15040229 |
| R06051 | 2023 | SARS-CoV-2 IgM/IgG | not reported | serum 5 uL | not reported | NR | sens 93.3% IgM, 96.6% IgG; spec 96.6%, 100% | visual | Abstract | 10.1021/acsomega.2c07014 |
| R05559 | 2022 | SARS-CoV-2 anti-S antibodies | NR | 500-fold diluted serum | 10 ng/mL to 1 ug/mL range | NR | NR | digital image green coordinate | Abstract | 10.1007/s10570-022-04808-y |
| R04535 | 2021 | SARS-CoV-2 antibodies | NR | NR | NR | NR | NR | visual | Abstract | 10.18063/ijb.v7i4.399 |

### Table D1b. Concentrating the target before the strip

| Rec | Year | Target | Label / device | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R01434 | 2014 | avian influenza H5 sequence | not reported | model | 40 ng to 0.1 ng at 12 V | NR | not reported | visual | Abstract | 10.3390/s140304399 |
| R01489 | 2014 | virus (model) | AuNP + PEG | virus samples | not reported | NR | not reported | visual | Abstract | 10.1002/bit.25316 |
| R01867 | 2016 | HIV nucleic acid | NR | NR | 0.1 nM (10-fold signal gain) | NR | NR | visual | Abstract | 10.1016/j.talanta.2016.02.017 |
| R05150 | 2022 | SARS-CoV-2 IgG/IgM antibodies | nanoelectrokinetic paper preconcentrator in front of a commercial IgG/IgM strip | vaccinated serum (pooled and five individual samples) | signal at 1/6,400 dilution with enrichment vs 1/200 without; enrichment factor > 30; extraction efficiency 95.7% | 32-fold lower LOD; analytical sensitivity +16.4% | four individual sera below the commercial LOD gave a signal after enrichment; no sensitivity/specificity | custom imaging system; five trained observers set LOD | Full text † | 10.1016/j.bios.2022.114385 |
| R05235 | 2022 | SARS-CoV-2 nucleocapsid (and hCG) | NR | model analytes | improved LOD (value NR) | NR | NR | visual | Abstract | 10.3389/fbioe.2022.884271 |
| R05785 | 2023 | SARS-CoV-2 | NR | clinical samples | enhanced LOD (value NR) | NR | NR | visual | Abstract | 10.1016/j.bios.2022.114965 |
| R06050 | 2023 | SARS-CoV-2 virus, N protein, IgG | red-blood-cell-membrane-coated AAO nanotrap (3 bar, 3 min) in front of a commercial antigen strip | PBS, artificial saliva, NP/OP swabs, saliva; 62 individuals | LOD improved up to 20-fold | commercial strip alone vs with enrichment | 42 positive, 20 healthy: sens 88.1% vs 14.29% (strip alone); spec 100%; Delta 10/10 vs 2/10; Omicron 27/32 vs 4/32; low-viral-load samples partly prepared by dilution | colour intensity (custom optical system); five observers set LOD | Full text † | 10.1038/s41467-023-37018-6 |
| R06089 | 2023 | serological target (model) | NR | NR | 1000x lower LOD than conventional LFIA | 1000x lower LOD than conventional LFIA | NR | visual | Abstract | 10.1021/acssensors.3c00130 |
| R06432 | 2023 | SARS-CoV-2 antigen (model) | NR | saliva spiked with gamma-irradiated virus | 10 pg/mL (~250 fM); 250 genome copies/uL; 10x enhancement at 2 mL vs 50 uL | 10x enhancement at 2 mL vs 5 uL (abstract) | NR | visual | Abstract | 10.1016/j.aca.2023.341674 |
| R06685 | 2023 | SARS-CoV-2 spike | not reported | not reported | enhanced vs standard LFA | NR | not reported | visual | Abstract | 10.1039/d3ay00990d |
| R07636 | 2025 | SARS-CoV-2 N protein | not reported | clinical trial | 0.24 ng/mL; 32.5x | 32.5x; conventional strip sensitivity 66.7% | sens 100%, spec 100% vs conventional LFA sens 66.7% | visual | Abstract | 10.1016/j.bios.2025.117357 |
| R02057 | 2017 | potato virus X | magnetic nanoparticles | leaf extracts | cut-offs 3, 30, 150 ng/mL; first cut-off 0.5 ng/mL (6-fold lower with magnetic concentration) | 6-fold lower first cut-off with magnetic enrichment | NR | visual/reader | Abstract | 10.1016/j.talanta.2016.11.025 |
| R02324 | 2018 | potato virus X | magnetic NPs + gold NPs | buffer, leaf extract | 0.25 ng/mL (32-fold below non-enhanced LFIA at 8 ng/mL) | NR | NR | visual | Abstract | 10.1016/j.aca.2017.12.023 |

### Table D1c. Sample collection and pretreatment

| Rec | Year | Target | Label / device | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R00213 | 2001 | HBsAg | not reported | whole blood | not reported | NR | not reported | visual | Abstract | 10.1128/cdli.8.1.9-13.2001 |
| R03733 | 2021 | PEDV, MERS-CoV | NR | spiked sputum | NR | NR | pretreatment suitable for sputum | visual | Abstract | 10.4110/in.2021.21.e11 |
| R04785 | 2022 | SARS-CoV-2 | NR | 102 COVID-19 patients | NR | NR | sens 97.8%, spec 100% (45 patients within 6 days) | visual | Abstract | 10.1128/spectrum.01614-21 |
| R05266 | 2022 | SARS-CoV-2 IgM/IgG | NR | NR | IgM 3 ng/mL, IgG 7 ng/mL | NR | NR | visual | Abstract | 10.1038/s41598-022-14725-6 |
| R03716 | 2021 | SARS-CoV-2 IgG | NR | 25 positive, 25 negative | NR | NR | sens 91%, spec 100% | visual | Abstract | 10.1007/s13337-021-00669-4 |
| R07605 | 2025 | mpox, orthopoxviruses | not reported | buffer/clinical matrices | 3e5 pfu/mL | NR | not reported | visual | Abstract | 10.1128/spectrum.02456-24 |
| R08237 | 2025 | DENV serotypes NS1 | not reported | clinical isolates, specimens | not reported | NR | serotype specificity 100% | visual | Abstract | 10.3390/bios15120802 |

### Table D1d. Binders and antigens designed for the strip

| Rec | Year | Target | Label / device | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R04590 | 2022 | SARS-CoV-2 N protein | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1002/jmv.27520 |
| R04950 | 2022 | SARS-CoV-2 | NR | NR | NR | NR | NR | NR | Abstract | 10.1371/journal.pntd.0010311 |
| R06593 | 2023 | SARS-CoV-2 N protein | not reported | clinical | not reported | NR | best prototype sens 95.2% (Ct<=25), spec 98.3%, accuracy 85.0% | visual | Abstract | 10.3390/microorganisms11102422 |
| R07270 | 2024 | HCV core antigen | not reported | serum matrix | 10 ng/strip | NR | not reported | visual | Abstract | 10.3390/ph17081022 |
| R08171 | 2026 | FeLV p27 | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1016/j.ab.2025.116013 |
| R08432 | 2026 | Lassa virus NP | not reported | 60 human samples | lineage-dependent | NR | spec 100% | visual | Abstract | 10.1128/jcm.00071-26 |
| R08528 | 2026 | HCV core | not reported | clinical | 0.3125 ng/mL | NR | sens 92.0%, spec 100%, accuracy 95.6% | visual | Abstract | 10.1038/s41598-026-54470-8 |
| R08594 | 2026 | orthoebolavirus GP | not reported | spiked blood, NHP samples | not reported | NR | detected EBOV in NHP at day 4 | visual | Abstract | 10.1038/s44298-026-00209-1 |
| R01300 | 2013 | norovirus | not reported | stool | similar to commercial kit | NR | not reported | visual | Abstract | None |
| R03041 | 2020 | CCHFV nucleoprotein | NR | NR | NR | NR | NR | visual | Abstract | 10.1371/journal.pntd.0008364 |
| R08211 | 2026 | SARS-CoV-2 | not reported | NP/OP swabs | not reported | NR | not reported | visual | Abstract | 10.1093/jaoacint/qsaf105 |
| R06754 | 2024 | SARS-CoV-2 sRBD | not reported | swabs | not reported | NR | best: sens 100%, spec 93.3% | visual | Abstract | 10.1093/jaoacint/qsae004 |
| R07292 | 2025 | SARS-CoV-2 S protein | not reported | not reported | 51.81 ng/mL (linear 0.1-1 ug/mL) | NR | not reported | visual/reader | Abstract | 10.1016/j.talanta.2024.126825 |
| R08036 | 2025 | SARS-CoV-2 N protein | not reported | not reported | 500 ng/mL | NR | not reported | visual | Abstract | 10.1016/j.virol.2025.110688 |
| R08072 | 2025 | SARS-CoV-2 | not reported | clinical | not reported | NR | spec 100%; sens 96.6% (model 1), 100% (models 2, 3) | visual | Abstract | 10.1186/s12879-025-11751-3 |
| R08198 | 2025 | DENV2 NS1 | not reported | buffer, spiked serum | 5.2 ng/mL buffer; 6.1 ng/mL serum | NR | not reported | visual | Abstract | 10.1038/s41598-025-29869-4 |
| R01273 | 2013 | HCV core antigen | AuNP | clinical | 10 pg/mL scanner; 100 pg/mL naked eye | NR | coincidence 97.28% at >1e4 copies/mL | visual + scanner | Abstract | 10.1080/15257770.2013.763976 |
| R07619 | 2025 | Zika NS1 | not reported | buffer, urine | 25 ng/mL (buffer); 1 ng/mL (urine) | NR | not reported | visual | Abstract | 10.1021/acssynbio.4c00819 |
| R07509 | 2025 | SARS-CoV-2, MERS-CoV | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1021/acssynbio.4c00592 |
| R07644 | 2025 | SARS-CoV-2 spike | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1021/jacs.4c17452 |
| R03325 | 2021 | SARS-CoV-2 S1 antigen | NR | clinical specimens, COVID-19 patients | 1.86 x 10^5 copies/mL | NR | no cross-reactivity with nasal swabs of healthy subjects | visual | Abstract | 10.1016/j.bios.2020.112715 |
| R04412 | 2021 | SARS-CoV-2 | NR | NR | NR | NR | NR | visual | Abstract | 10.1021/acssensors.1c01470 |
| R04739 | 2022 | SARS-CoV-2 and betacoronaviruses | gold nanoparticles | NR | NR | NR | NR | visual | Abstract | 10.1021/acscentsci.1c01080 |
| R02133 | 2017 | influenza virus (intact) | NR | NR | 3.54 x 10^7 and 1.34 x 10^7 CEID50/mL | NR | NR | visual | Abstract | 10.1021/acs.analchem.7b00769 |
| R05843 | 2023 | SARS-CoV-2 | colloidal gold | 19 clinical samples | 5 x 10^4 copies/mL | NR | 100% accuracy | visual | Abstract | 10.1016/j.snb.2022.133245 |
| R08676 | 2025 | HIV | not reported | blood | not reported | NR | not reported | visual | Abstract | 10.1016/j.vesic.2025.100084 |
| R06590 | 2023 | SARS-CoV-2 nucleocapsid antigen | NR | NR | NR | NR | NR | visual | Abstract | 10.3390/biom13101524 |
| R03119 | 2020 | oseltamivir-resistant influenza (NA mutant) | NR | NR | NR | NR | NR | naked eye, SERS, etc. | Abstract | 10.1038/s41467-020-17246-w |
| R05963 | 2023 | human bocavirus 1 and 2 | NR | paediatric respiratory samples | NR | NR | NR | NR | Abstract | 10.1007/s12519-023-00697-8 |
| R08578 | 2026 | Betacoronavirus S1 | not reported | not reported | 1.66 ug/mL | NR | not reported | visual | Abstract | 10.1016/j.bios.2026.118909 |
| R06925 | 2024 | SARS-CoV-2 S1 | gold-streptavidin | saliva, NP swabs | NR | NR | sens 95.21%, spec 99.29% (vs 91.66%/98.57% earlier strip) | visual | Abstract | 10.1038/s41598-024-57230-8 |

### Table D1e. Assay formats, functional assays and nucleic-acid formats

| Rec | Year | Target | Label / device | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R03096 | 2020 | SARS-CoV-2 nucleocapsid | NR | buffer, recombinant antigen | 0.65 ng/mL (0.53-0.77) | NR | NR | optical reader (equivalent to visual) | Abstract | 10.1021/acs.analchem.0c01975 |
| R05721 | 2022 | Rift Valley fever virus antibodies | NR | NR | NR | NR | NR | visual | Abstract | 10.3390/diagnostics12112664 |
| R02830 | 2019 | influenza A (NP) | enzyme/colorimetric | NR | 100-fold better LOD when used for capture | 100-fold better LOD when used for capture | NR | visual | Abstract | 10.1038/s41598-019-53083-8 |
| R06372 | 2023 | SARS-CoV-2 antibodies | NR | pooled and 22 individual sera | 10 ng/mL (Scheme C); 15x and 255x lower than B and A | Scheme C 15x and 255x lower than B and A | Scheme C 100% sens and spec (n=22) | visual | Abstract | 10.3390/bios13070750 |
| R04519 | 2021 | SARS-CoV-2 neutralizing antibodies | NR | finger-prick blood | NR | NR | NR | visual | Abstract | 10.1016/j.jcv.2021.105024 |
| R05400 | 2022 | SARS-CoV-2 neutralizing antibodies | NR | NR | NR | NR | NR | visual | Abstract | 10.1016/j.crmeth.2022.100273 |
| R06277 | 2023 | SARS-CoV-2 neutralizing antibodies | NR | 684 uninfected, clinical samples | 2 ug/mL | NR | sens 97.80%, spec 100% | visual | Abstract | 10.2147/ijn.s408921 |
| R05892 | 2023 | dengue serotypes | not reported | spiked plasma, serum, blood | 333 to 22,500 TCID50/mL (plasma/serum); 94,000-333,000 in blood | NR | each serotype-specific, no cross-reactivity | visual | Abstract | 10.1128/spectrum.02796-22 |
| R08431 | 2026 | RVFV antibodies | not reported | not reported | not reported | NR | high sens and spec (no values) | visual | Abstract | 10.3390/v18030316 |
| R06800 | 2024 | SARS-CoV-2 antibodies | NR | NR | NR | NR | classifies high and low titres | visual | Abstract | 10.1039/d3tb02895j |
| R01986 | 2016 | HPV16 vaccination status | NR | whole blood/plasma | NR | NR | NR | visual | Abstract | 10.1016/j.vaccine.2016.09.021 |
| R05342 | 2022 | NR (serodiagnosis model) | gold nanoparticles | NR | NR | NR | sens 62.5% (common) vs 100% (enhanced); spec 100% | visual | Abstract | 10.3390/bios12070434 |
| R02519 | 2018 | potato virus Y | gold nanoparticles | NR | 5.4 ng/mL (60-fold lower than 330 ng/mL conventional) | 60-fold lower than conventional (330 ng/mL) | NR | visual | Abstract | 10.3390/s18113975 |
| R05788 | 2022 | SARS-CoV-2 | NR | NR | 0.01 nM without amplification | NR | NR | visual | Abstract | 10.3390/ijms232315258 |
| R05932 | 2023 | SARS-CoV-2 | NR | gamma-irradiated virions in saliva | 200 copies/uL (commercial unamplified LFAs: 500, 1000, 2000, 2000, 20,000) | NR | NR | visual | Abstract | 10.1021/acsinfecdis.2c00472 |
| R06795 | 2024 | SARS-CoV-2 | not reported | not reported | 1e3 to 1e8 copies/mL | NR | not reported | visual | Abstract | 10.1021/acs.analchem.3c03698 |
| R08593 | 2026 | PEDV | not reported | oral fluid, 102 clinical samples | 1.33 ng/mL N protein; 278 copies/test | NR | accuracy 97.06%, sens 96.92%, spec 97.30% | visual | Abstract | 10.1002/adhm.202504037 |
| R06592 | 2023 | SARS-CoV-2 sequence | NR | NR | ~0.2 nM | NR | NR | visual | Abstract | 10.3390/mi14101936 |
| R07400 | 2024 | influenza A H1N1 | not reported | not reported | 1 pM | NR | not reported | visual | Abstract | 10.1016/j.ijbiomac.2024.136945 |

### Table D1f. Prototype and development strips (pre-2015 first)

| Rec | Year | Target | Label / device | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| R00103 | 1994 | human rotavirus | AuNP | faeces | not reported | NR | spec 100%/sens 100% vs latex; 99%/98% vs RNA-PAGE; 100%/98% vs ELISA | visual | Abstract | 10.1016/0166-0934(94)90130-9 |
| R00522 | 2007 | human metapneumovirus | not reported | infected cells, purified N | not reported | NR | good specificity, sufficient sensitivity | visual | Abstract | 10.1089/hyb.2006.034 |
| R00584 | 2007 | West Nile virus IgM | not reported | suspected WNV patients | not reported | NR | not reported (no abstract) | visual | Abstract | 10.1373/clinchem.2007.091140 |
| R00585 | 2008 | norovirus GI, GII | not reported | stool of children | not reported | NR | agreement 84.1%, sens 69.8%, spec 93.7% | visual | Abstract | 10.1016/j.jviromet.2007.10.010 |
| R00718 | 2009 | HCV core antigen | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1016/j.jviromet.2009.02.013 |
| R00747 | 2009 | measles | not reported | recombinant proteins | 5.1e3 copies/test | NR | spec efficacy (no value) | visual | Abstract | 10.1089/hyb.2009.0006 |
| R00798 | 2010 | pandemic H1N1 (2009) | not reported | virus isolates; 5 patients | not reported | NR | 100% specificity; 5/5 positive | visual | Abstract | 10.1128/jcm.02262-09 |
| R00887 | 2010 | HIV p24 (paediatric) | not reported | 51 archived infant; 389 South African infant | 50 pg/mL recombinant; 42.5k RNA copies/mL | NR | archived 90%/100%; field 95%/99% | visual | Abstract | 10.1097/qai.0b013e3181f1afbc |
| R00940 | 2011 | pandemic H1N1 | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1128/cvi.00269-10 |
| R00942 | 2011 | human cytomegalovirus | not reported | HCMV samples | 1:5.12e4 | NR | no cross-reaction with HSV-1/2, VZV etc. | visual | Abstract | 10.1111/j.1472-765x.2010.03002.x |
| R00961 | 2011 | H5 influenza virus | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1016/j.jviromet.2011.02.007 |
| R01147 | 2012 | pandemic H1N1 (2009) | not reported | 215 patients | not reported | NR | sens 81.5% (75/92), spec 96.7% (119/123) | visual | Abstract | 10.1111/j.1348-0421.2012.00455.x |
| R01189 | 2012 | HCV antibodies | not reported | 23 positive, 8 negative sera; 300 clinical | not reported | NR | sens 100%, spec 100% | visual | Abstract | 10.3892/ijmm.2012.1121 |
| R01206 | 2013 | Toscana virus antibodies | not reported | 100 sera | not reported | NR | IgM: 64/65 ELISA positives detected | visual | Abstract | 10.1016/j.jviromet.2012.09.015 |
| R01422 | 2013 | pandemic H1N1 (pdm09) | not reported | 188 samples | 1/2^8 HAU | NR | sens 75.86% (110/145), spec 100% (43/43) | visual | Abstract | 10.1016/j.phrp.2013.10.006 |
| R01473 | 2014 | SFTSV | AuNP | 245 positive sera | not reported | NR | good selectivity | visual | Abstract | 10.1155/2014/530621 |
| R01477 | 2014 | influenza B | AuNP | 710 NP samples | not reported | NR | sens 89.76%, spec 99.56%; consistency 96.06% | visual | Abstract | 10.7754/clin.lab.2013.130342 |
| R01486 | 2014 | hantaviruses | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1186/1743-422x-11-87 |
| R03359 | 2020 | HBV preS2 antigen | magnetic nanoparticles (GAM-MNPs) | 25 clinical sera | 625 ng/mL (qualitative); 3.6 ng/mL (quantitative) | NR | sens 93.3%, spec 90% | visual and magnetic signal | Abstract | 10.3390/bios10110161 |
| R03930 | 2021 | dengue NS1 | NR | 219 sera | 0.78 (unit NR in abstract) | NR | sens 88.89%, spec 86.67%, kappa 0.7522 vs nested PCR | visual | Abstract | 10.1016/j.ijid.2021.05.007 |
| R04503 | 2021 | SARS-CoV-2 nucleocapsid | NR | gamma-irradiated virus on swabs | 4 TCID50/swab | NR | meets WHO target product profile | visual | Abstract | 10.1371/journal.pone.0258819 |
| R04614 | 2021 | SARS-CoV-2 | magnetic particles (blue dots) | PBS, saliva, nasal swabs | 400 PFU/mL (PBS); 1200 PFU/mL (saliva) | NR | sens 66.7%, spec 100% (nasal swabs) | visual | Abstract | 10.3390/bios11120488 |
| R04897 | 2022 | SARS-CoV-2 antigen | not reported | 111 hospitalised patients | not reported | NR | not reported in abstract | visual | Abstract | 10.48101/ujms.v127.8207 |
| R05044 | 2021 | influenza A and B | NR | 101 NP swabs | 4-8x more sensitive than commercial tests | NR | sens 89% (A), 83% (B); spec 100% | visual | Abstract | 10.1039/d1ra01361k |
| R05822 | 2022 | SARS-CoV-2 antigen | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.3390/v14122609 |
| R05994 | 2023 | SARS-CoV-2 Omicron | NR | simulated positive samples | 62.5 TCID50/mL | NR | no cross-reaction | visual | Abstract | 10.3390/vaccines11020303 |
| R06038 | 2023 | SARS-CoV-2 spike | NR | heat-inactivated virus, respiratory panel | 25 ng/test | NR | spec 98% | visual | Abstract | 10.3389/fimmu.2023.1111644 |
| R06556 | 2024 | SARS-CoV-2 | silica nanoparticles | unprocessed swabs (1:10^3 dilution) | 0.73 pg/mL | NR | sens 100%, spec 83%, accuracy 92% vs RT-qPCR | visual | Abstract | 10.1002/open.202300120 |
| R06568 | 2023 | SARS-CoV-2 IgG/IgM | not reported | 300 samples | not reported | NR | not reported in abstract | visual | Abstract | 10.1186/s13568-023-01620-0 |
| R06576 | 2023 | SARS-CoV-2 Omicron variants | NR | variant virus panel | NR | NR | detected Omicron sublineages, Wuhan, Delta | visual | Abstract | 10.1016/j.heliyon.2023.e20913 |
| R06981 | 2024 | SARS-CoV-2 nucleocapsid | NR | 170 NP swabs | R2 0.9571 visual vs reader | NR | sens 98% (89.35-99.95), spec 100% | visual and reader | Abstract | 10.1039/d3ay02075d |
| R07722 | 2025 | hMPV | not reported | not reported | not reported | NR | not reported | visual | Abstract | 10.1002/jmv.70374 |
| R07921 | 2025 | Nipah, Hendra viruses | not reported | not reported | not reported | NR | diagnostic spec 94.4% | visual | Abstract | 10.3390/v17071021 |

### Table D2. Strategy overview for assay and flow engineering

| Strategy | What it changes | Examples | Costs and limits seen | Table |
|---|---|---|---|---|
| Flow control and architecture | contact time, reagent delivery, geometry | delayed flow, sugar barriers, sponges, tapered strips, vertical flow | more parts or steps; format differs from a simple strip | D1a |
| Front-end enrichment | target concentration entering the strip | nanoelectrokinetic, nanotrap, osmotic and magnetic enrichment | hardware (power, pressure), larger sample volumes | D1b |
| Sample collection and pretreatment | usability of the sample | blood, sputum, gargle, microneedle, buffers | few clinical data | D1c |
| Binders and antigens | specificity and supply | mAb pairs, aptamers, nanobodies, affibody, receptor and glycan capture | matrix, n and reference often not in abstracts | D1d |
| Formats and functional assays | what is measured | half-strip, neutralization, serotyping, DNA-structure readouts | reference standards differ | D1e |
| Prototype strips | new target, new evaluation | rotavirus, influenza, dengue, SARS-CoV-2 and others | accuracy ranges widely | D1f |

### Table D3. Reporting checklist for papers read in full (descriptive, not scored)

Items: (a) real samples; (b) n stated; (c) reference method; (d) LOD definition; (e) cross-reactivity tested by the authors; (f) replicates or reproducibility; (g) comparator run in the same study; (h) stability tested. Y = yes, N = no, P = partly, NR = not reported. The other papers in Tables D1a-f have not been assessed (abstract only).

| Rec | DOI | (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) |
|---|---|---|---|---|---|---|---|---|---|
| R05150 | 10.1016/j.bios.2022.114385 | P (vaccinated sera; no infected patients) | P (five individual sera) | N (no reference method) | Y (normalised signal; observers' LOD) | Y (other antibodies, BSA, buffer after enrichment) | Y (ten repeats per commercial assay) | Y (commercial strip alone) | N |
| R06050 | 10.1038/s41467-023-37018-6 | Y (62 individuals; NP/OP and saliva) | Y (42 + 20) | Y (RT-qPCR) | P (observer-defined cut-off) | Y (RSV A/B, influenza A/B, HCoV-OC43) | P (at least three repeats per point) | Y (commercial strip alone) | P (membrane stable 15 days at room temperature) |

## Items still to verify before this section is final
1. Many abstract-level rows give matrix or reference method as NR; they stay NR until full text is read.
2. R05150 (DOI: 10.1016/j.bios.2022.114385): the 32-fold figure is the shift from 1/200 to 1/6,400 dilution of a vaccinated serum with a commercial strip; no patient accuracy is reported.
3. R06050 (DOI: 10.1038/s41467-023-37018-6): low-viral-load samples were partly prepared by diluting positive swabs.
4. Six antibody-screening papers were excluded (E9) by default; reversible.
5. Records flagged scope-check (R03041, R03119, R04535, R05963, R06590, R05822, R07722, R00584) are kept; check them if section length matters.
6. Record IDs in the tables will be replaced by numbered citations when the reference list is built.
