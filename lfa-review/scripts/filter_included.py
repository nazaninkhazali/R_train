import openpyxl,collections
S=openpyxl.load_workbook('03_screening.xlsx',read_only=True)['screening_all']
sr=list(S.iter_rows(values_only=True));h=sr[0]
inc={r[h.index('rec_id')] for r in sr[1:] if r[h.index('decision_claude')]=='INCLUDE'}
wb=openpyxl.load_workbook('04_evidence_table.xlsx')
ws=wb['abstract_chart_all3076'];rows=list(ws.iter_rows(values_only=True))
H=rows[0]
if 'included' in wb.sheetnames: del wb['included']
n=wb.create_sheet('included',0); n.append(H)
k=[r for r in rows[1:] if r[0] in inc]
for r in k:n.append(r)
wb.save('04_evidence_table.xlsx')
print(len(k),len(inc))
si=H.index('section');yi=H.index('year')
print(sorted(collections.Counter(r[si] for r in k).items(),key=lambda x:-x[1]))
print('2015+ by section',sorted(collections.Counter(r[si] for r in k if r[yi] and int(r[yi])>=2015).items(),key=lambda x:-x[1]))
