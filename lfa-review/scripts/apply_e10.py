import openpyxl,re,sys,collections,json
mode=sys.argv[1]
ev=openpyxl.load_workbook('04_evidence_table.xlsx',read_only=True)['included']
rows=list(ev.iter_rows(values_only=True));H=rows[0]
h=[dict(zip(H,r)) for r in rows[1:] if r[H.index('section')]=='h']
DEV=re.compile(r'(\bdevelopment\b|\bdeveloped\b|prototype|in-house|homemade|self-developed|\bnovel\b|\bengineered\b|\bfacile\b|\bnew(ly)?\b.{0,30}(test|assay|strip|kit)|\bsimple (point|antigen|test|and quick)|low-cost|smart polymer|nanoparticle-enhanced)',re.I)
EXTRA=re.compile(r'(prevalence|pooling|proficiency|panel quality|manufacturing|perspectives|comparative evaluation|independent (evaluation|testing)|self-testing|screening strateg|absence of|prescreening|assessment of the accuracy|point-of-care evaluation|validation of a rapid antigen test|limited sensitivity|prospective evaluation|field evaluation)',re.I)
EVAL=re.compile(r'^(evaluation|comparison|performance|clinical (performance|evaluation)|diagnostic (accuracy|performance|value|efficacy)|accuracy|field|real-life|sensitivity)',re.I)
keep=[];exc=[]
for d in h:
    tg=(d['tags'] or '').lower();ti=d['title'] or ''
    new='new assay' in tg
    dev=bool(DEV.search(ti)) and not EVAL.match(ti) and not EXTRA.search(ti)
    if d['rec_id'] in {'R01677','R05401','R06408'}: new=dev=False
    (keep if new or dev else exc).append(d)
print('section h',len(h),'keep (development/prototype)',len(keep),'E10',len(exc))
json.dump([d['rec_id'] for d in exc],open('/tmp/claude-0/-home-user-R-train/2a209992-7073-59bb-ae76-d6f52e35dbc7/scratchpad/e10.json','w'))
if mode=='list':
    for d in keep:print(d['rec_id'],d['year'],d['title'][:110],'|',d['label'])
if mode=='apply':
    wb=openpyxl.load_workbook('03_screening.xlsx');ws=wb['screening_all']
    hh=[c.value for c in ws[1]];ix={k:i for i,k in enumerate(hh)}
    ids={d['rec_id'] for d in exc};n=0
    for r in ws.iter_rows(min_row=2):
        if r[ix['rec_id']].value in ids:
            r[ix['decision_claude']].value='EXCLUDE';r[ix['reason_claude']].value='E10'
            old=r[ix['note_claude']].value or ''
            r[ix['note_claude']].value=(old+'; ' if old else '')+'author scope amendment 2026-11-05: commercial/finished-kit evaluation, no new strip development'
            n+=1
    wb.save('03_screening.xlsx');print('applied',n)
