"""Apply author scope rules to rows tagged scope-check in the evidence table.
Usage: python3 -I scripts/apply_scope_rules.py [dry|apply]"""
import sys, re, collections, openpyxl
EV='04_evidence_table.xlsx'; SC='03_screening.xlsx'
# (code, label, regex on lower-cased scope-check text) in priority order
RULES=[
 ('E9','spent strips/tests used as a sample source (author rule)', r'spent|sequencing source|rna source'),
 ('E1','insect or invertebrate virus (author rule)', r'insect virus|invertebrate|baculovirus|nodavirus'),
 ('E1','non-viral or host target (author rule)', r'non-viral|host biomarker|host response|cancer biomarker(?!, strip)|phage model|m13 phage|no virus|virus not stated|target not stated|fabrication tool|heterophile|non-viral coinfection|non-viral analyte|il-6|cancer risk'),
 ('E3','not colorimetric: fluorescence/automated/chemiluminescent format (author rule)', r'sofia|lumiradx|fia fluorescence|afias|fluorescence-type|cleia|clia\b|liaison|amperometric|chemiluminescent|includes fluorescence|mixes lf and fia|rapiim|veritor analyser|sers not colorimetric|elisa-type'),
 ('E2','not a lateral flow assay or strip not stated (author rule)', r'strip not stated|strip readout not stated|virus and strip|lfa not stated|no lfa stated|not an? lfa|not lfa|format not|not a lateral flow|not clearly lateral|lamp, strip|rpa, strip|rpa is main|lamp colour|lamp focus|mostly elisa|elisa|ia?\W*not lfa|biosensor|qcm|microarray|vertical flow|paper elisa|svnt|surrogate assays|pcr|rt-pcr|rha m|rham|mlpa|molecular|nass? comparator|naat comparator|mostly automated|paper-based|pregnancy test strip(?!)x|assays not all|includes non-lfa|mixed ?(platform|method|assay)|multiple methods|assay formats not|assay types not|includes dfa|includes parasite|lamp focus|molecular-vs|only a comparator|only comparator'),
 ('E6','no original assay data (modelling, QA/EQA, protocol, method, reference material)', r'modell?ing|statistical|eqa|qa programme|qa training|quality|protocol|secondary analysis|reference material|iqc|methodology|pt scheme|specimen collection|survey of|operational|abuse|case report'),
 ('E9','LFA used only as a tool in epidemiology, surveillance or screening (author rule)', r'seroprevalence|seroepidemiology|epidemiolog|surveillance|prevalence|outbreak|incidence|screening|program|programme|perceptions|viral load|infection-control|incubation|return-to-work|vaccination antibody|pilot monitoring|monitoring study|clinical immunology|prognostic|longitudinal|infectivity|feasibility|registry|genotyping focus|observational ppv|small cohort|viral dynamics|predictor|immune-response study|immunology|molecular epidemiology|serosurvey|surveillance app|cohort(?!.*lfa)x'),
]
KEEP_REASON={'no abstract':'abstract unavailable; retained on title','abstract incomplete':'abstract incomplete; retained','arthropod':'arbovirus detection in vector pools; retained, flagged','syphilis':'viral target retained; non-viral co-target noted','bacteria':'viral target retained; bacterial co-target noted','fungal':'viral target retained; fungal co-target noted','reader':'reader format with coloured label retained','tiny':'small n retained, flagged','pilot':'small n retained, flagged','n=4':'small n retained, flagged','interference':'interference study retained','sens/spec labels':'abstract inconsistency noted'}

OVER={}
def _o(code,label,ids):
    for i in ids.split(): OVER[i]=(code,label)
_o('E2','not a lateral flow assay or strip not stated (author rule)','R01604 R01627 R01657 R01692 R01800 R02571 R02827 R03078 R03165 R03578 R03633 R04449 R04594 R04999 R05255 R05272 R05339 R05347 R05751 R05835 R05872 R05969 R05450 R06443 R07071 R07163')
_o('E9','LFA used only as a tool or comparator (author rule)','R01620 R01633 R01795 R02230 R02232 R02758 R03122 R05065 R05407 R05836 R06187')
_o('E9','spent strips/tests used as a sample source (author rule)','R06115 R06218 R06637 R07189')
_o('E1','no stated virus or non-viral target (author rule)','R02731 R03244 R03829 R04578 R04729 R04924 R04980 R05003 R05054 R05333 R05376 R05493 R05571 R05685 R05832 R05833 R06258 R06325 R06656 R06712 R06715 R06902 R06964 R07024 R07033')
_o('E1','insect virus (author rule)','R04632 R07079')
_o('E3','not colorimetric: fluorescence, SERS or chemiluminescent format (author rule)','R04036 R04615 R06248 R06269 R06958 R06960')
_o('E6','no original assay data (protocol, case report, trial design)','R01828 R03795 R05295')
AFTER={'LFA not stated':'E2','not LFA':'E2','format not stated':'E2','format NR':'E2','readout NR':'E2','LFA readout not stated':'E2','not clearly LFA':'E2','paper-based':'E2','PCR not LFA':'E2','PCR':'E2','ELISA':'E2','mixed methods':'E2','mainly molecular':'E2','non-viral':'E1','viral target NR':'E1','epidemiology':'E9','seroprevalence':'E9','surveillance':'E9','prevalence':'E9','molecular epidemiology':'E9','immunology':'E9','programme':'E9','surveillance programme':'E9','surveillance app':'E9','prevalence study':'E9','outbreak report':'E9','serosurvey':'E9','LFA comparator only':'E9','fluorescent':'E3','fluorescent readout':'E3','luminescent assay':'E3','electrochemical':'E3','proficiency test':'E6','modelling':'E6','case report':'E6'}

def classify(tag, title):
    t=tag.lower()
    for code,label,rx in RULES:
        if re.search(rx,t): return code,label
    return None,None
def main(mode):
    wb=openpyxl.load_workbook(EV,read_only=True); ws=wb['abstract_chart']
    rows=list(ws.iter_rows(values_only=True)); h=rows[0]; R=rows[1:]
    ix={k:i for i,k in enumerate(h)}
    dec={}; keep=collections.Counter(); sc=0
    for r in R:
        tag=str(r[ix['tags']] or '')
        parts=[p.strip() for p in tag.split(';')]
        sctags=[p for p in parts if p.startswith('scope-check')]
        if not sctags: continue
        sc+=1
        txt='; '.join(sctags)
        rid=r[ix['rec_id']]
        if rid in OVER: code,label=OVER[rid]
        elif any(p.startswith('scope-check:') for p in sctags): code,label=classify(txt,r[ix['title']])
        elif 'scope-check' not in parts: code,label=classify(txt,r[ix['title']])
        else:
            k=parts.index('scope-check'); aft=';'.join(parts[k+1:]); code=AFTER.get(aft)
            label={'E1':'non-viral or no stated virus (author rule)','E2':'not a lateral flow assay or strip not stated (author rule)','E3':'not colorimetric (author rule)','E6':'no original assay data','E9':'LFA used only as a tool in epidemiology, surveillance or screening (author rule)'}.get(code); txt='scope-check; '+aft
        if code: dec[r[ix['rec_id']]]=(code,label,txt)
        else:
            k=next((v for kk,v in KEEP_REASON.items() if kk in txt.lower()),'retained after review: flag only')
            keep[k]+=1
    print('scope-check rows',sc,'to exclude',len(dec))
    print(collections.Counter((c,l) for c,l,_ in dec.values()))
    print('kept:',keep)
    if mode!='apply': 
        import json; json.dump({k:v for k,v in dec.items()},open('/tmp/claude-0/-home-user-R-train/2a209992-7073-59bb-ae76-d6f52e35dbc7/scratchpad/dec_preview.json','w'))
        return
    wb=openpyxl.load_workbook(SC); ws=wb['screening_all']
    hh=[c.value for c in ws[1]]; I={k:i for i,k in enumerate(hh)}
    n=0
    for row in ws.iter_rows(min_row=2):
        rid=row[I['rec_id']].value
        if rid in dec:
            code,label,txt=dec[rid]
            row[I['decision_claude']].value='EXCLUDE'; row[I['reason_claude']].value=code
            row[I['note_claude']].value=f'author rule (scope-check review 2026-11-04): {label}; chart flag: {txt}'
            n+=1
    wb.save(SC); print('applied',n)
main(sys.argv[1] if len(sys.argv)>1 else 'dry')
