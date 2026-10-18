# Search log

Database: PubMed (MEDLINE + PubMed-only records), searched through the PubMed connector available in this
session. Connector limits: max 20 Boolean operators per query; no `*` truncation; max 200 records per
page. Field tag `[tiab]` = title/abstract; `[MeSH]` = MeSH heading (exploded by default); `[uid]` = PMID.

Status: **strategy development (Stage 2). None of these runs is the final search.**

---

## A. Exploratory sizing searches (2026-10-17, before protocol; not reproducible as reported)
Run only to estimate volume; strings were not fully recorded at the time. Reported in chat as
~900 hits (basic colorimetric × LFA × virus) and ~35 reviews. **Not used for any analysis.**

## B. Strategy development runs (2026-10-18)

Concept blocks:
- **A (LFA):** `"lateral flow"[tiab] OR immunochromatographic[tiab] OR immunochromatography[tiab] OR LFIA[tiab] OR "test strip"[tiab] OR "strip test"[tiab] OR dipstick[tiab]`
- **C (virus, generic):** `virus[tiab] OR viruses[tiab] OR viral[tiab] OR "Viruses"[MeSH] OR "Virus Diseases"[MeSH]`
- **B1 (plasmonic):** `"gold nanoparticle"[tiab] OR "gold nanoparticles"[tiab] OR "colloidal gold"[tiab] OR AuNPs[tiab] OR AuNP[tiab] OR nanostars[tiab] OR nanoflowers[tiab] OR "silver nanoparticles"[tiab] OR "core-shell"[tiab]`
- **B2 (carriers):** `latex[tiab] OR polystyrene[tiab] OR "cellulose nanobeads"[tiab] OR "carbon nanoparticles"[tiab] OR "carbon black"[tiab] OR liposomes[tiab] OR microspheres[tiab]`
- **B3 (colour amplification):** `nanozyme[tiab] OR nanozymes[tiab] OR "Prussian blue"[tiab] OR "peroxidase-like"[tiab] OR TMB[tiab] OR "silver enhancement"[tiab] OR "gold enhancement"[tiab] OR "signal amplification"[tiab] OR "signal enhancement"[tiab]`
- **B4 (nucleic acid):** `RPA[tiab] OR "recombinase polymerase"[tiab] OR LAMP[tiab] OR "loop-mediated"[tiab] OR CRISPR[tiab] OR Cas12a[tiab] OR Cas13a[tiab] OR "isothermal amplification"[tiab] OR "nucleic acid"[tiab]`
- **B5 (readout words):** `colorimetric[tiab] OR colourimetric[tiab] OR "naked eye"[tiab] OR "naked-eye"[tiab] OR "visual detection"[tiab] OR "visual readout"[tiab] OR visually[tiab] OR smartphone[tiab] OR "mobile phone"[tiab]`

| # | Query | Hits (2026-10-18) |
|---|---|---|
| 1 | A AND C | 4,697 |
| 2 | A AND (coronavirus OR SARS-CoV-2 OR COVID-19 OR HIV OR influenza OR hepatitis OR HBsAg OR norovirus OR rotavirus OR dengue OR mpox OR monkeypox) [all tiab] | 3,842 |
| 3 | A AND (coronavirus OR SARS-CoV-2 OR COVID-19 OR HIV OR influenza OR hepatitis) NOT C | 544 |
| 4 | A AND (HBsAg OR norovirus OR rotavirus OR dengue OR mpox OR monkeypox OR PRRSV) NOT C | 61 |
| 5 | A AND C AND (plant OR plants OR crop OR leaf OR leaves OR "Plant Diseases"[MeSH]) | 131 |
| 6 | (A′) AND (SARS-CoV-2 OR COVID-19) AND (sensitivity OR "diagnostic accuracy" OR "clinical performance"), where A′ = A minus test strip/strip test/dipstick plus "rapid antigen test", "antigen rapid diagnostic test", "Ag-RDT" | 1,202 |
| 7 | A AND C AND B1 | 590 |
| 8 | A AND C AND B2 | 134 |
| 9 | A AND C AND B3 | 132 |
| 10 | A AND C AND B4 | 1,012 |
| 11 | A AND C AND B5 | 592 |

Estimates (overlaps between rows 1, 3 and 4 are zero by construction):
- **A AND (C OR named viruses) ≈ 5,300 records** (rows 1 + 3 + 4 = 5,302; other named viruses not yet tested).
- A AND C AND (B1 OR … OR B5): ≤ 2,460 (sum of rows 7–11; overlap not removed; true union not yet measured).

## C. Recall test with a seed set (2026-10-18)

Seed set v0.1: 9 papers selected by me from prior knowledge, then verified in PubMed (PMID, DOI, title,
abstract, MeSH). Their **eligibility is provisional**. It is based on abstracts only, and for several the
colorimetric label is not stated in the abstract, so full text is needed to confirm. Retrieval was tested
by running each block AND the seed PMIDs (`[uid]`).

| Seed | PMID | DOI | A AND C | Any B block | Notes |
|---|---|---|---|---|---|
| Broughton 2020, Nat Biotechnol — CRISPR-Cas12 LFA, SARS-CoV-2 | 32300245 | 10.1038/s41587-020-0513-4 | ✔ | ✔ (B4) | |
| Gootenberg 2018, Science — SHERLOCKv2 with lateral-flow readout | 29449508 | 10.1126/science.aaq0179 | ✔ | ✔ (B4) | |
| Myhrvold 2018, Science — HUDSON + SHERLOCK, Zika/dengue | 29700266 | 10.1126/science.aas8836 | ✘ | ✘ | No LFA term in title/abstract/MeSH; LFA use not confirmable from abstract |
| Loynachan 2018, ACS Nano — Pt nanocatalyst LFIA, HIV p24 | 29215864 | 10.1021/acsnano.7b06229 | ✔ | ✔ (B1, B5) | |
| Grant 2020, Anal Chem — SARS-CoV-2 N antigen half-strip LFA | 32605363 | 10.1021/acs.analchem.0c01975 | ✔ | **✘** | Label not named in abstract |
| Li 2020, J Med Virol — IgM-IgG LFIA, SARS-CoV-2 | 32104917 | 10.1002/jmv.25727 | ✔ | ✔ (B4, incidental: "nucleic acid" refers to PCR comparator) | Label not named in abstract |
| Duan 2015, Biosens Bioelectron — Fe₃O₄ nanozyme strip, Ebola | 26134291 | 10.1016/j.bios.2015.05.025 | ✔ | ✔ (B3) | |
| Bosch 2017, Sci Transl Med — NS1 rapid tests, dengue/Zika, image analysis | 28954927 | 10.1126/scitranslmed.aan1589 | ✔ | **✘** | "visual test analysis", "image processing" not matched |
| Mudanyali 2012, Lab Chip — cellphone RDT reader (incl. HIV RDT) | 22596243 | 10.1039/c2lc40235a | ✔ | **✘** | "cellphone" not matched |

Result:
- **A AND C: 8/9 retrieved (89%)**. The miss is not a lateral-flow paper by title/abstract.
- **A AND C AND (any B): 5/9 (56%)**; one of the 5 was retrieved only by coincidence.
- Limitations of this test: small set; human viruses only; chosen from high-profile papers; no veterinary,
  aquaculture or plant seeds yet. **Veterinary and plant seed papers are needed from the author.**

Interpretation (mine): abstracts often do not name the label or use a colour term, so a colorimetric
block in the search loses many eligible studies. Colorimetric status is better judged at screening.

## D. Access notes
- Direct HTTPS to NCBI E-utilities, Crossref (api.crossref.org) and doi.org: blocked by this environment's
  network policy (tested 2026-10-17). PubMed connector works.
- The PubMed website (pubmed.gov) has no 20-operator limit and can export up to 10,000 records with
  abstracts. This makes it the better tool for the final reproducible run (see protocol §6).
