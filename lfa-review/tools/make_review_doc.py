import re, subprocess, docx
from docx.enum.text import WD_COLOR_INDEX
SRC='/home/user/R_train/lfa-review/05_drafts/article_body_sections1-4_2026-11-21.md'
OUT_MD='/home/user/R_train/lfa-review/05_drafts/article_commercial_review_2026-11-24.md'
OUT='/home/user/R_train/lfa-review/05_drafts/article_commercial_review_2026-11-24.docx'
t=open(SRC).read().split('\n---\n')[0]
NAMED={
1:("the Humasis HBsAg rapid test (manufacturer: Humasis, as named in the paper)","Jargalsaikhan et al., PLoS One 2020, doi:10.1371/journal.pone.0235036 (tests 19 hepatitis B and C rapid kits, Humasis among them; confirm it is the same product)"),
2:("the Alere HIV-1/2 Ag/Ab Combo rapid test (as named in the paper)","none found in PubMed by my search"),
3:("the Alere HIV-1/2 Ag/Ab Combo strip","same as above"),
15:("three SARS-CoV-2 antigen tests from Anbio Biotech, Boson Biotech and Sejoy (manufacturers as named in the paper)","none found in PubMed by my combined search; not searched one by one"),
16:("the three antigen tests (Anbio, Boson, Sejoy)","as above"),
24:("an ELISA from Ingenasa (as named in the paper)","none found in PubMed by my search"),
29:("the Svanodip FMDV-Ag lateral flow kit (as named in the paper)","no dedicated evaluation found; PLoS One 2015, doi:10.1371/journal.pone.0134931, matched on the name (development of a different FMDV strip, to be checked)"),
30:("a colloidal gold SARS-CoV-2 antibody strip from Jiangxi YeLi Medical Device Co., Ltd (Nanchang, China)","none found in PubMed by my search"),
33:("the BD Veritor and Quidel Sofia SARS antigen tests (values quoted by the paper from the literature, source given there as Pollock et al. 2021, not checked by me)","BD Veritor: Hardick et al., Microbiol Spectr 2022, doi:10.1128/spectrum.01025-22. Sofia: Pray et al., MMWR 2021, doi:10.15585/mmwr.mm695152a3; Lippi et al., EJIFCC 2023 (meta-analysis, PMID 37455844)"),
38:("three influenza A antigen strips from Biodragon, Easy Quarter and Runbo Fude (manufacturers as named in the paper)","not searched"),
47:("a SARS-CoV-2 antigen rapid kit from Calth Inc. (Republic of Korea, as named in the paper)","none found in PubMed by my search"),
48:("the QuickVue SARS-CoV-2 antigen test (Quidel, as named in the paper)","Hardick et al., Microbiol Spectr 2022, doi:10.1128/spectrum.01025-22; Bourassa et al., J Clin Virol 2021, doi:10.1016/j.jcv.2021.104900"),
}
PURCH={4:("gold nanoparticles purchased from Cytodiagnostics (a reagent, not a test)","10.5599/admet.2079"),19:("gold nanoparticle conjugates bought from a supplier (name the supplier; a reagent, not a test)","10.3390/ijms23147957")}
GENERAL={6,9,21,28,32,39,41,42,53}
UNNAMED={5:'10.3892/ijmm.2015.2333',7:'10.1007/s00604-023-06013-5',8:'10.1007/s00604-026-08241-x',10:'10.1021/acs.analchem.2c01286',11:'10.1007/s00604-025-07587-y',12:'10.1007/s00604-020-04670-4',13:'10.1007/s00604-020-04670-4',14:'10.1007/s00604-025-07179-w',17:'10.1016/j.nano.2025.102853',18:'10.1016/j.bios.2015.11.099',20:'10.1038/s41467-025-58663-z',22:'10.1155/tbed/5512419',23:'10.1155/tbed/5512419',25:'10.3390/bios13030352',26:'10.1016/j.bbrc.2024.149821',27:'10.3390/bios13030352',31:'10.1021/acsanm.1c03217',34:'10.1016/j.aca.2024.343474',35:'10.1016/j.aca.2024.343474',36:'10.1021/acsami.3c15851',37:'10.1021/acsami.3c15851',40:'10.1016/j.ab.2026.116259',43:'10.3390/bios14060305',44:'10.1016/j.bios.2022.114385',45:'10.1016/j.bios.2022.114385',46:'10.1038/s41467-023-37018-6',49:'10.1016/j.talanta.2016.11.025',50:'10.1038/s41598-019-53083-8',51:'10.1021/acsinfecdis.2c00472',52:'10.1039/d1ra01361k'}
# extra named products without the word "commercial"
EXTRA=[("BD gold strips","BD Directigen EZ Flu A+B (Becton Dickinson), as named in the paper","Weinberg & Walker, Clin Diagn Lab Immunol 2005, doi:10.1128/CDLI.12.3.367-370.2005; DiMaio et al., J Virol Methods 2012, doi:10.1016/j.jviromet.2012.07.023"),
("BinaxNOW","BinaxNOW COVID-19 Antigen CARD (Abbott); the abstract calls it commercially available","Hardick et al., Microbiol Spectr 2022, doi:10.1128/spectrum.01025-22; Bourassa et al., J Clin Virol 2021, doi:10.1016/j.jcv.2021.104900"),
("CoV-SCAN","CoV-SCAN: this is the authors' own development (BioMedomics), not a commercial comparator, and the abstract does not state its label; MOVE out of the gold section or confirm the label from the full text","Liu et al., J Clin Virol Plus 2022, doi:10.1016/j.jcvp.2022.100080 (the paper itself)")]
ms=list(re.finditer(r'[Cc]ommercial\w*(?:[ -][\w/+.-]+){0,3}',t))
assert len(ms)>=53,len(ms)
# trim match to not run past punctuation
spans=[]
for m in re.finditer(r'[Cc]ommerc\w+',t):
    end=m.end()
    tail=re.match(r'(?:\s[\w/+-]+){0,3}',t[end:])
    ext=end+len(tail.group(0)) if tail else end
    seg=t[m.start():ext]
    cut=re.search(r'[,;.()]',seg)
    if cut: ext=m.start()+cut.start()
    spans.append((m.start(),ext))
assert len(spans)==53,len(spans)
def heading_before(pos):
    hs=[h for h in re.finditer(r'(?m)^### (.*)$',t[:pos])]
    return hs[-1].group(1) if hs else ''
rows=[]; out=[]; last=0
for i,(s,e) in enumerate(spans,1):
    out.append(t[last:s]); cur=t[s:e]
    if i in NAMED: prop,pub=NAMED[i]; note=f"CHANGE TO: {prop}. PUBLICATION: {pub}"; kind='named'
    elif i in PURCH: prop,doi=PURCH[i]; note=f"CHANGE TO: {prop}. No test publication applies"; pub='not applicable'; kind='purchased reagent'
    elif i in GENERAL: note="GENERAL STATEMENT: replace 'commercial' by 'marketed' or 'reference' and refer to the individual studies"; prop="reword (general)"; pub='not applicable'; kind='general'
    else: doi=UNNAMED[i]; prop=f"NAME THE TEST (product and manufacturer) from the Methods of DOI {doi}; if the paper gives none, write 'a marketed test, not named in the paper'"; note="CHANGE TO: "+prop+". PUBLICATION: search once the test is named"; pub='search once named'; kind='unnamed'
    out.append("«HL»"+cur+"«/HL»«HL» ["+note+"]«/HL»")
    rows.append((i,heading_before(s)[:40],cur,prop,pub,kind)); last=e
out.append(t[last:]); t2=''.join(out)
for key,prop,pub in EXTRA:
    c=t2.count(key)
    t2=t2.replace(key,"«HL»"+key+"«/HL»«HL» [CHANGE TO: "+prop+". PUBLICATION: "+pub+"]«/HL»")
    rows.append(('+',key,key,prop,pub,'named' if key!='CoV-SCAN' else 'misplaced'))
    print(key,c)
tab="\n\n---\n\n## Change list\n\nEach highlighted phrase in the text is listed here. 'named' = the product is named in the paper; 'unnamed' = the paper (or my record of it) gives no product name and you need to look it up in the Methods; 'general' = a summary statement; 'purchased reagent' = nanoparticles bought from a supplier. Publications are only those found in PubMed by me; 'none found' means my search returned nothing, not that none exists.\n\n| No. | Section | Current wording | Proposed change | Publication on the test | Type |\n|---|---|---|---|---|---|\n"
for r in rows: tab+="| "+" | ".join(str(x).replace('|','/') for x in r)+" |\n"
open(OUT_MD,'w').write(t2+tab)
subprocess.run(['pandoc',OUT_MD,'-f','gfm','-o',OUT],check=True)
d=docx.Document(OUT)
def process(par):
    txt=par.text
    if '«HL»' not in txt: return
    parts=re.split(r'(«HL»|«/HL»)',txt); hl=False; style=par.style
    for r in list(par.runs): r._element.getparent().remove(r._element)
    for p in parts:
        if p=='«HL»': hl=True; continue
        if p=='«/HL»': hl=False; continue
        if not p: continue
        run=par.add_run(p)
        if hl: run.font.highlight_color=WD_COLOR_INDEX.YELLOW
for p in d.paragraphs: process(p)
for tb in d.tables:
    for row in tb.rows:
        for c in row.cells:
            for p in c.paragraphs: process(p)
d.save(OUT)
print(len(rows),'rows; highlighted paragraphs ok')
