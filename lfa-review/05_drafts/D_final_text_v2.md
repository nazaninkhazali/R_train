# Part D (working text v2): assay and flow engineering and the colorimetric signal

Working text, 2026-11-10. Reframed around the question of this review: how do changes to the strip, the flow, the sample and the binders change the colour signal, by how much, and at what cost? Each subsection follows four questions: what limits the signal at this point, which design addresses it, what the papers report against their own baseline, and what it costs. The target virus is named for every method. Numbers are in the tables; Table D4 gathers the within-paper changes. † = read in full; all other rows abstract only (NR = not reported in the abstract). Every DOI cited in the text appears in a table and in the evidence table. The section covers 99 included records, all from 2015-2026, after the E9 exclusion of six papers in which the strip was used only to screen antibodies or peptides; three records were read in full.

# 3.4 Assay and flow engineering: how the strip, the sample and the binder change the colour

## 3.4.0 What limits the signal outside the label, and how this section is organised

The sections so far changed what is on the strip: the particle, the colour carrier and the amplifier. This section looks at everything else that decides whether the label gets a chance to colour the line. A sample has to enter the strip in a usable form, flow past the capture line for long enough, meet binders that recognise the target, and be read in a defined format. Any of these can limit the signal, independent of the label. The label is usually colloidal gold and often not changed at all, so the gains reported here describe the strip around the label.

The studies are organised along that path. They start with the flow inside the strip (3.4.1), then concentrating the target before it enters (3.4.2), collecting and pre-treating the sample (3.4.3), the binders and antigens that give the strip its specificity (3.4.4), and the assay formats built around them, including DNA structures that add signal (3.4.5). The strips that combine these elements for a new virus are summarised in 3.4.6, and 3.4.7 states what the evidence supports.

## 3.4.1 Controlling the flow inside the strip

Limit addressed: the time the sample is in contact with the capture line. Slowing or shaping the flow gives labelled complexes longer to bind. For the SARS-CoV-2 spike receptor-binding domain, a delayed lateral flow design with a hydrophobic barrier gave a 9.1-fold lower LOD and 2.6-fold higher sensitivity than a conventional strip (DOI: 10.1007/s00604-022-05467-3). Dissolvable sugar barriers on the membrane of a SARS-CoV-2 nucleic acid strip lowered the LOD from 2.5 to 0.5 nM, a 5-fold gain (DOI: 10.1016/j.carbpol.2021.118259). A tapered strip for dengue virus NS1 reached 4.9 ng/mL, about 11-fold better than previously reported (DOI: 10.1063/1.5035113). Other geometries: a sponge shunt for hepatitis B virus nucleic acid with improved analytical sensitivity (value not given) (DOI: 10.1038/s41598-017-01558-x), a two-dimensional paper network for influenza haemagglutinin (4.45 x 10^2 TCID50/mL in spiked paediatric nasal swabs) (DOI: 10.1039/c8lc00691a), a paper-hydrogel hybrid for dengue virus RNA tested on clinical samples (DOI: 10.1002/adhm.201600920), and femtosecond-laser micromachined channels in nitrocellulose for respiratory viruses and SARS-CoV-2, with no values in the abstract (DOI: 10.1038/s41598-024-74407-3). Cost-efficient changes of strip design also raised the sensitivity of SARS-CoV-2 nucleocapsid tests: a cotton intermembrane with higher test-line antibody gave a 4-fold improvement (2.0 ng/mL) (DOI: 10.1038/s41598-023-31641-5), and a water-soluble polymer wall gave 50 pg/mL, 5- to 20-fold better than market kits (DOI: 10.3390/bios14060305).

A second family moves the sample through the paper in another direction. Vertical-flow cellulose assays were used for SARS-CoV-2 antibodies and antigen (DOI: 10.1021/acssensors.1c00235; DOI: 10.1039/d2lc00073c), for Rift Valley fever virus (RVFV), where the vertical-flow format reached 0.78 ng/mL, 2.5-fold better than a lateral-flow prototype (DOI: 10.1128/spectrum.00341-25), and for influenza A (H1N1), where a vertical-flow paper immunosensor with a different pore sample pad reached 1.34 PFU/mL in buffer and 2.27 PFU/mL in saliva (DOI: 10.1016/j.bios.2018.10.008). A thermochromic strip for dengue virus serotype 2 NS1 reached a 4-fold lower LOD than a typical visual readout, which changes the readout and not the colour (DOI: 10.1039/d3nr01858j), and a centrifugal microfluidic chip analysed Ebola virus-like particles by imaging (DOI: 10.1039/d3ay00073g). Low-cost fabrication addresses manufacturing rather than sensitivity: manually developed SARS-CoV-2 IgM/IgG strips (sensitivity 93.3% and 96.6%) (DOI: 10.1021/acsomega.2c07014), 3D-printed and foil-based nanoimprinted chips for SARS-CoV-2 serology (DOI: 10.18063/ijb.v7i4.399; DOI: 10.3390/bios15040229), and a cellulose-based test strip for SARS-CoV-2 anti-S antibodies, run on 500-fold diluted serum over a range of 10 ng/mL to 1 ug/mL (DOI: 10.1007/s10570-022-04808-y).

Cost: these designs trade the one-step simplicity of a conventional strip for sensitivity or manufacturability, and gains are measured against the authors' own or earlier strips.

## 3.4.2 Concentrating the target before the strip

Limit addressed: the number of target molecules reaching the line. The target can be enriched before it enters the strip, and the simplest approach for the user is a front-end device used with an unmodified commercial strip.

A nanoelectrokinetic preconcentrator coupled to a commercial SARS-CoV-2 IgG/IgM strip concentrated antibodies more than 30-fold on rolled paper discs under an electric field of about 70 V/cm and gave a 32-fold lower LOD (the signal appeared at 1/6,400 instead of 1/200 dilution of a vaccinated serum), with 95.7% extraction efficiency when the right paper was used (DOI: 10.1016/j.bios.2022.114385). In a pilot with sera from vaccinated people, four samples that the commercial strip did not detect became detectable (Table D1b). Another group enriched SARS-CoV-2 virus, nucleocapsid protein and IgG on a red-blood-cell-membrane-coated nanoporous aluminium oxide membrane under 3 bar of pressure in 3 minutes, again in front of a commercial strip (DOI: 10.1038/s41467-023-37018-6). The LOD improved up to 20-fold, and in 62 individuals the strip's sensitivity rose from 14.29% to 88.1% with 100% specificity (DOI: 10.1038/s41467-023-37018-6). The low-viral-load samples were partly produced by diluting positive swabs, and the device needs a pressure source and 3 mL of sample, which the authors recognise as limits for fingerstick serology (DOI: 10.1038/s41467-023-37018-6).

Related approaches for SARS-CoV-2 use an osmotic processor that concentrates urine (nucleocapsid protein and hCG as model analytes) (DOI: 10.3389/fbioe.2022.884271), a non-powered preconcentrator tested on clinical samples (DOI: 10.1016/j.bios.2022.114965), electrokinetic focusing by ion concentration polarization for the spike protein (DOI: 10.1039/d3ay00990d), an agglutination system for large sample volumes that reached 10 pg/mL with a 10-fold enhancement (DOI: 10.1016/j.aca.2023.341674), and a nanoelectrokinetic strip with a Nafion-cellulose gel for the nucleocapsid protein, which gave 32.5-fold enhancement and sensitivity 100% and specificity 100% against 66.7% sensitivity for the conventional strip in a clinical evaluation (DOI: 10.1016/j.bios.2025.117357). An electrophoresis-driven assembly of antibody-antigen complexes (a serological model) lowered the LOD 1000-fold against a conventional strip (DOI: 10.1021/acssensors.3c00130). For HIV nucleic acid, a dialysis-based concentrator gave a 10-fold signal gain (DOI: 10.1016/j.talanta.2016.02.017). For potato virus X, magnetic enrichment gave a 32-fold lower LOD in a double-enhanced strip with magnetic and gold nanoparticles (0.25 ng/mL against 8 ng/mL), and a barcode strip with magnetic nanoparticles set cut-offs at 3, 30 and 150 ng/mL with a first cut-off of 0.5 ng/mL (DOI: 10.1016/j.aca.2017.12.023; DOI: 10.1016/j.talanta.2016.11.025). For SARS-CoV-2, a magnetic-focus-enhanced strip detected 400 PFU/mL in buffer and 1200 PFU/mL in saliva, with sensitivity 66.7% and specificity 100% on nasal swabs (DOI: 10.3390/bios11120488), and for the hepatitis B virus preS2 antigen a secondary-antibody magnetic nanoprobe gave sensitivity 93.3% and specificity 90% on 25 clinical sera (DOI: 10.3390/bios10110161).

Cost: enrichment shows the largest gains in this section without changing the label or the commercial strip, but it is paid for with hardware (electrodes, pressure, magnets) and larger sample volumes. Most studies show the enrichment effect with spiked or reference samples; only a few include patient samples (Table D1b).

## 3.4.3 Collecting and treating the sample

Limit addressed: whether the sample reaches the strip in a usable form. A pretreatment with TCEP and bovine serum albumin made sputum usable for lateral flow detection of porcine epidemic diarrhea virus and MERS coronavirus (DOI: 10.4110/in.2021.21.e11). A gargle with a bean extract (Beanguard) replaced swab collection for SARS-CoV-2 antigen tests: sensitivity 97.8% and specificity 100% in 45 patients tested within six days of onset, in a study of 102 patients (DOI: 10.1128/spectrum.01614-21). A porous microneedle patch collected sample for an IgM/IgG test for SARS-CoV-2 (IgM 3 ng/mL, IgG 7 ng/mL) (DOI: 10.1038/s41598-022-14725-6). A new diluent improved a SARS-CoV-2 IgG test (sensitivity 91%, specificity 100% on 25 positive and 25 negative samples) (DOI: 10.1007/s13337-021-00669-4). Together these show that sample handling is itself a design variable (Table D1c). Cost: extra reagents or devices, and evidence at the level of one study each.

## 3.4.4 Binders and antigens designed for the strip

Limit addressed: what the strip is able to recognise, and with what affinity. This is the most numerous group.

**Antibody pairs and fragments.** Many studies develop monoclonal antibody pairs or scFv fragments for a new target: SARS-CoV-2 nucleocapsid protein (DOI: 10.1002/jmv.27520; DOI: 10.1371/journal.pntd.0010311; DOI: 10.3390/microorganisms11102422; DOI: 10.1093/jaoacint/qsaf105), the hepatitis C virus core antigen (10 ng/strip and 0.3125 ng/mL, with sensitivity 92.0% and specificity 100% in the second study) (DOI: 10.3390/ph17081022; DOI: 10.1038/s41598-026-54470-8), the feline leukaemia virus p27 antigen (DOI: 10.1016/j.ab.2025.116013), the Lassa virus nucleoprotein, with lineage-dependent detection and specificity 100% on 60 human samples (DOI: 10.1128/jcm.00071-26), the orthoebolavirus glycoprotein, which detected Ebola virus in non-human primates at day 4 (DOI: 10.1038/s44298-026-00209-1), the Nipah and Hendra viruses (diagnostic specificity 94.4%) (DOI: 10.3390/v17071021), and mpox and other orthopoxviruses with four monoclonal antibodies to the A27 protein (3 x 10^5 pfu/mL) (DOI: 10.1128/spectrum.02456-24). Affimers were used for the Crimean-Congo haemorrhagic fever virus nucleoprotein (DOI: 10.1371/journal.pntd.0008364).

**Non-antibody binders.** Six aptamer-aptamer pairs for the SARS-CoV-2 spike receptor-binding domain were compared, with the best reaching sensitivity 100% and specificity 93.3% on swabs (DOI: 10.1093/jaoacint/qsae004); a competitive aptamer device for the SARS-CoV-2 spike protein reached 51.81 ng/mL (DOI: 10.1016/j.talanta.2024.126825), an aptamer lateral flow biosensor for the nucleocapsid protein 500 ng/mL (DOI: 10.1016/j.virol.2025.110688), and aptamer cocktails in three models reached sensitivity of 96.6% to 100% with specificity 100% (DOI: 10.1186/s12879-025-11751-3). For dengue virus serotype 2 NS1, an aptamer-antibody strip reached 5.2 ng/mL in buffer and 6.1 ng/mL in spiked serum (DOI: 10.1038/s41598-025-29869-4). Nanobodies were used in a SARS-CoV-2 spike S1 strip improved by streptavidin-biotin capture (sensitivity 95.21% and specificity 99.29% against 91.66% and 98.57% for the earlier strip) (DOI: 10.1038/s41598-024-57230-8), for SARS-CoV-2 and MERS-CoV (DOI: 10.1021/acssynbio.4c00592), and for Zika virus NS1 (25 ng/mL in buffer, 1 ng/mL in urine) (DOI: 10.1021/acssynbio.4c00819). A competitive strip with an affinity-engineered receptor-binding domain/ACE2 pair detected betacoronavirus S1 at 1.66 ug/mL (DOI: 10.1016/j.bios.2026.118909). Helical affibodies replaced the antibody in a SARS-CoV-2 spike strip (DOI: 10.1021/jacs.4c17452). The human ACE2 receptor served as capture for the SARS-CoV-2 spike S1 antigen (1.86 x 10^5 copies/mL) on clinical specimens (DOI: 10.1016/j.bios.2020.112715). Glycan recognition was used for SARS-CoV-2 in a flow-through device and in a glycopolymer-capture system for SARS-CoV-2 and other betacoronaviruses (DOI: 10.1021/acssensors.1c01470; DOI: 10.1021/acscentsci.1c01080). High-affinity haemagglutinin-binding proteins detected intact influenza virus particles (3.54 x 10^7 and 1.34 x 10^7 CEID50/mL) (DOI: 10.1021/acs.analchem.7b00769).

**Orientation, antigen design and special targets.** Orienting the antibody on the particle improved a SARS-CoV-2 strip, which detected 5 x 10^4 copies/mL and gave 100% accuracy on 19 clinical samples (DOI: 10.1016/j.snb.2022.133245). Engineered nucleocapsid antigens were designed to improve the stability of SARS-CoV-2 strips (DOI: 10.3390/biom13101524). An antibody against a drug-resistance-associated neuraminidase mutant allowed detection of oseltamivir-resistant influenza virus (DOI: 10.1038/s41467-020-17246-w), and genotype-specific antibodies were developed for human bocavirus 1 and 2 (DOI: 10.1007/s12519-023-00697-8). An extracellular-vesicle capture design links HIV to vesicle markers in blood (DOI: 10.1016/j.vesic.2025.100084).

**Kits for variants.** Antigen detection kits with recombinant or monoclonal nucleocapsid antibodies detected SARS-CoV-2 Omicron (62.5 TCID50/mL on simulated positive samples) and Omicron sublineages, Wuhan and Delta strains (DOI: 10.3390/vaccines11020303; DOI: 10.1016/j.heliyon.2023.e20913).

These papers establish what a strip can recognise; whether the strip then works depends on the assay format and the samples, which many of them do not report in the abstract (Table D1d). Cost: a new binder needs development, and the abstracts rarely give a within-paper comparison with a conventional antibody.

## 3.4.5 Assay formats, functional assays and DNA structures that add signal

Limit addressed: how the reaction is arranged and read. A half-strip format uses open reagents for the SARS-CoV-2 nucleocapsid protein (0.65 ng/mL) and for Rift Valley fever virus antibodies (DOI: 10.1021/acs.analchem.0c01975; DOI: 10.3390/diagnostics12112664). A pipetting-based format runs the immunoreaction outside the strip for influenza A nucleoprotein and gave a 100-fold better LOD when used for capture (DOI: 10.1038/s41598-019-53083-8). A comparison of three SARS-CoV-2 antibody-detection formats, run with the same receptor-binding domain antigen and 30 nm gold particles, found that the format with immobilised protein A in the line and labelled antigen in the conjugate gave a 15- and 255-fold lower detection limit than the other two on pooled positive serum, while still detecting 22 of 22 patient sera correctly (DOI: 10.3390/bios13070750). A two-stage label incorporation into immune complexes (a serodiagnosis model) raised sensitivity from 62.5% to 100% at specificity 100% (DOI: 10.3390/bios12070434). For potato virus Y, pre-incubation in a sandwich strip gave a 60-fold lower LOD (5.4 ng/mL against 330 ng/mL) (DOI: 10.3390/s18113975).

Functional formats measure neutralizing antibodies against SARS-CoV-2: a competitive strip from a finger prick (DOI: 10.1016/j.jcv.2021.105024), a strip capturing neutralized receptor-binding domain (DOI: 10.1016/j.crmeth.2022.100273), and a strip with a LOD of 2 ug/mL, sensitivity 97.80% and specificity 100% on 684 uninfected and clinical samples (DOI: 10.2147/ijn.s408921). Serological and multiplex tests include a four-serotype dengue panel with serotype-specific NS1 detection (333 to 22,500 TCID50/mL in plasma and serum) (DOI: 10.1128/spectrum.02796-22), a species-independent double-antigen test for Rift Valley fever virus antibodies (DOI: 10.3390/v18030316), a semi-quantitative multi-line SARS-CoV-2 antibody test that classifies high and low titres (DOI: 10.1039/d3tb02895j), a strip with HPV16 virus-like particle capture to determine HPV16 vaccination status (DOI: 10.1016/j.vaccine.2016.09.021), and a dengue NS1 capture assay with serotype specificity of 100% (DOI: 10.3390/bios15120802).

Nucleic-acid targets were read on strips by hybridisation with signal-amplifying DNA structures. For SARS-CoV-2, a triplex enhanced assay reached 0.01 nM without amplification (DOI: 10.3390/ijms232315258), a hybridisation chain reaction strip 200 copies/uL against 500 to 2000 for commercial unamplified strips (DOI: 10.1021/acsinfecdis.2c00472), a net-shaped DNA nanostructure strip covered 10^3 to 10^8 copies/mL (DOI: 10.1021/acs.analchem.3c03698), and protein-based probe anchoring reached about 0.2 nM (DOI: 10.3390/mi14101936). For influenza A (H1N1), an M13 nanoscaffold gave an amplification-free strip with 1 pM (DOI: 10.1016/j.ijbiomac.2024.136945), and for porcine epidemic diarrhea virus a DNA nanostructure with multivalent binding gave accuracy 97.06% on 102 clinical samples (DOI: 10.1002/adhm.202504037). A probe-gated silica nanoparticle strip detected SARS-CoV-2 at 0.73 pg/mL in unprocessed swabs (sensitivity 100%, specificity 83% against RT-qPCR) (DOI: 10.1002/open.202300120) (Table D1e). A caution applies to the functional and serological formats: their reference standards differ (neutralization tests, ELISA), so agreement figures cannot be compared with antigen strips.

## 3.4.6 Strips that combine these elements for one virus

A large share of the records are strips developed for one virus without a deliberate change to the label, many of them evaluated on patient samples. They matter as baseline: they show what the combination of binder, format and sample achieves without signal engineering. Their abstracts rarely give a within-paper change in the colour signal, so they are summarised here by target, with values in Table D1f.

For SARS-CoV-2, antigen prototypes include a saliva strip tested on 111 hospitalised patients (DOI: 10.48101/ujms.v127.8207), a prototype compared with BinaxNOW (DOI: 10.3390/v14122609), a spike LFIA with specificity 98% (25 ng/test) (DOI: 10.3389/fimmu.2023.1111644), a nucleocapsid antigen test that meets the WHO target product profile at 4 TCID50/swab (DOI: 10.1371/journal.pone.0258819), a visual platform whose reading correlated with a reader (R2 0.9571; sensitivity 98%, specificity 100% on 170 swabs) (DOI: 10.1039/d3ay02075d), and an in-house antibody kit tested on 300 samples (DOI: 10.1186/s13568-023-01620-0). For manually developed IgM/IgG strips see 3.4.1. For other viruses: an influenza A and B strip with new monoclonal antibodies, 4- to 8-fold more sensitive than commercial tests, with sensitivity 89% (A) and 83% (B) and specificity 100% on 101 swabs (DOI: 10.1039/d1ra01361k); a paper-based dengue NS1 device on 219 sera (sensitivity 88.89%, specificity 86.67%, kappa 0.7522 against nested PCR) (DOI: 10.1016/j.ijid.2021.05.007); and standard and rapid antigen assays for human metapneumovirus (DOI: 10.1002/jmv.70374).

## 3.4.7 What the evidence supports

For the question of this review, the gains in the colour signal in this section come from the strip and sample, not from the label. Within-paper changes range from about 2-fold to 1000-fold (Table D4). The largest come from enrichment and electrokinetic or electrophoretic concentration (32-fold and 32.5-fold for SARS-CoV-2 strips, 1000-fold for a serological model) and from format and pre-incubation changes (60-fold for potato virus Y, 255-fold between antibody-detection formats for SARS-CoV-2), while flow control and design changes give gains of roughly 4- to 20-fold. Front-end enrichment shows the largest gains without changing the label or the commercial strip, but its cost is hardware (electrodes, pressure, magnets) and larger sample volumes. The three papers read in full show the pattern: both enrichment studies used a commercial strip as the downstream test, measured gains against that strip, and cannot be called equipment-free (Table D2).

Three limitations recur. First, many studies use reference or spiked samples; clinical samples are the exception among engineering papers. Second, several studies give only a fold-improvement and not the strip's accuracy on patients. Third, the antibody and binder papers rarely report the matrix, number of samples or reference method in their abstracts. For the three papers read in full, Table D3 lists the reporting items.

### Table D4. Reported change in the colour signal against the paper's own baseline

Only studies with a baseline in the same paper are listed. Fold-changes are the authors' figures; baselines differ and the rows cannot be ranked against each other. † = read in full.

| Rec | Virus (target) | Design | Baseline in the same paper | Reported change | Matrix tested | DOI |
|---|---|---|---|---|---|---|
| R05533 | SARS-CoV-2 (spike RBD) | delayed flow, hydrophobic barrier | conventional strip | 9.1-fold lower LOD; 2.6-fold higher sensitivity | NR | 10.1007/s00604-022-05467-3 |
| R04042 | SARS-CoV-2 (nucleic acid) | dissolvable sugar barriers | strip without barriers | 5-fold (0.5 vs 2.5 nM) | NR | 10.1016/j.carbpol.2021.118259 |
| R06060 | SARS-CoV-2 (nucleocapsid) | cotton intermembrane, more test-line antibody | conventional strip | 4-fold (2.0 ng/mL) | NR | 10.1038/s41598-023-31641-5 |
| R07133 | SARS-CoV-2 | water-soluble polymer wall | market kits | 5- to 20-fold (50 pg/mL) | NR | 10.3390/bios14060305 |
| R07816 | Rift Valley fever virus | vertical flow | lateral-flow prototype | 2.5-fold (0.78 ng/mL) | NR | 10.1128/spectrum.00341-25 |
| R06336 | dengue virus 2 (NS1) | thermochromic readout | typical visual readout | 4-fold lower LOD | NR | 10.1039/d3nr01858j |
| R05150 † | SARS-CoV-2 (IgG/IgM) | nanoelectrokinetic preconcentrator | commercial strip alone | 32-fold lower LOD (1/6,400 vs 1/200); 4 more vaccinated sera detected | serum | 10.1016/j.bios.2022.114385 |
| R06050 † | SARS-CoV-2 | membrane nanotrap enrichment | commercial strip alone | up to 20-fold; sensitivity 14.29% to 88.1% in 62 individuals | swabs | 10.1038/s41467-023-37018-6 |
| R07636 | SARS-CoV-2 (nucleocapsid) | nanoelectrokinetic gel | conventional strip | 32.5-fold; sensitivity 100% vs 66.7% | clinical | 10.1016/j.bios.2025.117357 |
| R06432 | SARS-CoV-2 (model antigen) | agglutination for large volume | strip without agglutination | 10-fold enhancement | spiked saliva | 10.1016/j.aca.2023.341674 |
| R06089 | serological model | electrophoretic assembly | conventional LFIA | 1000-fold lower LOD | NR | 10.1021/acssensors.3c00130 |
| R01867 | HIV (nucleic acid) | dialysis concentration | strip without concentrator | 10-fold signal gain | NR | 10.1016/j.talanta.2016.02.017 |
| R02324 | potato virus X | magnetic + gold double enhancement | non-enhanced LFIA | 32-fold (0.25 vs 8 ng/mL) | leaf extract | 10.1016/j.aca.2017.12.023 |
| R02519 | potato virus Y | pre-incubation | conventional LFIA | 60-fold (5.4 vs 330 ng/mL) | NR | 10.3390/s18113975 |
| R02830 | influenza A (nucleoprotein) | pipetting-based capture | strip without capture step | 100-fold | NR | 10.1038/s41598-019-53083-8 |
| R06372 † | SARS-CoV-2 (antibodies) | protein A line + labelled antigen (format C) | formats A and B, same antigen | 15- and 255-fold lower LOD; 22/22 sera correct | pooled and 22 sera | 10.3390/bios13070750 |
| R05342 | serodiagnosis model | two-stage label incorporation | common LFIA | sensitivity 62.5% to 100% | NR | 10.3390/bios12070434 |
| R05932 | SARS-CoV-2 (RNA) | hybridisation chain reaction | commercial unamplified LFAs | 200 vs 500 to 2000 copies/uL | gamma-irradiated virions in saliva | 10.1021/acsinfecdis.2c00472 |
| R05044 | influenza A and B | new monoclonal antibodies | commercial tests | 4- to 8-fold | 101 NP swabs | 10.1039/d1ra01361k |

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
| R03041 | 2020 | CCHFV nucleoprotein | NR | NR | NR | NR | NR | visual | Abstract | 10.1371/journal.pntd.0008364 |
| R08211 | 2026 | SARS-CoV-2 | not reported | NP/OP swabs | not reported | NR | not reported | visual | Abstract | 10.1093/jaoacint/qsaf105 |
| R06754 | 2024 | SARS-CoV-2 sRBD | not reported | swabs | not reported | NR | best: sens 100%, spec 93.3% | visual | Abstract | 10.1093/jaoacint/qsae004 |
| R07292 | 2025 | SARS-CoV-2 S protein | not reported | not reported | 51.81 ng/mL (linear 0.1-1 ug/mL) | NR | not reported | visual/reader | Abstract | 10.1016/j.talanta.2024.126825 |
| R08036 | 2025 | SARS-CoV-2 N protein | not reported | not reported | 500 ng/mL | NR | not reported | visual | Abstract | 10.1016/j.virol.2025.110688 |
| R08072 | 2025 | SARS-CoV-2 | not reported | clinical | not reported | NR | spec 100%; sens 96.6% (model 1), 100% (models 2, 3) | visual | Abstract | 10.1186/s12879-025-11751-3 |
| R08198 | 2025 | DENV2 NS1 | not reported | buffer, spiked serum | 5.2 ng/mL buffer; 6.1 ng/mL serum | NR | not reported | visual | Abstract | 10.1038/s41598-025-29869-4 |
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
| R06372 | 2023 | SARS-CoV-2 RBD antibodies (serology) | three formats with 30 nm gold particles: A protein A label, B labelled antigen with antigen line, C labelled antigen with protein A line | pooled positive serum; humanized monoclonal antibody; 22 human sera | Scheme C 10 ng/mL monoclonal antibody (blank + 3 SD) | Scheme C 15x lower than B and 255x lower than A (pooled positive serum) | 22 sera (confirmed by PCR and clinical observation; ELISA): Scheme C sens 100%, spec 100% | visual; 60 uL sample, 10 min | Full text † | 10.3390/bios13070750 |
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

### Table D1f. Prototype and development strips (by year)

| Rec | Year | Target | Label / device | Matrix | LOD (as stated) | Within-paper comparison | Diagnostic data (as stated) | Readout | Evidence | DOI |
|---|---|---|---|---|---|---|---|---|---|---|
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
| R06372 | 10.3390/bios13070750 | Y (22 human sera) | P (22; split into positives and negatives not stated in the text read) | P (PCR and clinical observation; ELISA on sera) | Y (blank mean + 3 SD) | NR | NR | Y (three formats run under optimised conditions) | P (conjugates stable 3 months; strip stability NR) |

## Items still to verify before this section is final
1. Many abstract-level rows give matrix or reference method as NR; they stay NR until full text is read.
2. R05150 (DOI: 10.1016/j.bios.2022.114385): the 32-fold figure is the shift from 1/200 to 1/6,400 dilution of a vaccinated serum with a commercial strip; no patient accuracy is reported.
3. R06050 (DOI: 10.1038/s41467-023-37018-6): low-viral-load samples were partly prepared by diluting positive swabs.
4. Six antibody-screening papers were excluded (E9) by default; reversible.
5. Records flagged scope-check (R03041, R03119, R04535, R05963, R06590, R05822, R07722, R00584) are kept; check them if section length matters.
6. Record IDs in the tables will be replaced by numbered citations when the reference list is built.
