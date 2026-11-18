import sys, subprocess, docx
from docx.shared import Cm, Pt
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
src,out=sys.argv[1],sys.argv[2]
subprocess.run(['pandoc',src,'-f','gfm','-o',out],check=True)
d=docx.Document(out)
for s in d.sections:
    s.orientation=WD_ORIENT.LANDSCAPE; s.page_width,s.page_height=Cm(29.7),Cm(21.0); s.left_margin=s.right_margin=Cm(1.5)
for t in d.tables:
    b=OxmlElement('w:tblBorders')
    for e in('top','left','bottom','right','insideH','insideV'):
        el=OxmlElement(f'w:{e}'); el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'4'); el.set(qn('w:color'),'999999'); b.append(el)
    t._tbl.tblPr.append(b)
    for r in t.rows:
        for c in r.cells:
            for p in c.paragraphs:
                for run in p.runs: run.font.size=Pt(7.5)
d.save(out)
