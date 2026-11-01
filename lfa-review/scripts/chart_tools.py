"""Abstract-level charting helpers.

  python3 -I chart_tools.py batch  SIZE OUT [brief]   dump next uncharted INCLUDE records (year>=2015 first; 'brief' = pre-2015)
  python3 -I chart_tools.py merge                    write charting/*.tsv into 04_evidence_table.xlsx
  python3 -I chart_tools.py status

Chart files: charting/*.tsv, 12 tab-separated fields:
rec_id, virus, host, analyte, format, label, readout, sample, lod, clinical, section, tags
Missing values are written NR (not reported in the abstract). All rows are 'abstract only'.
Sections: a AuNP engineering; b other coloured labels; c catalytic/enzymatic amplification;
d assay/flow engineering; e nucleic-acid amplification + strip; f smartphone/reader/AI;
g multiplex/dual-mode; h clinical/commercial test evaluation; i vet/aquaculture/plant application;
z none of these / unclear.
"""
import glob
import re
import os
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CH_DIR = os.path.join(ROOT, "charting")
SCREEN = os.path.join(ROOT, "03_screening.xlsx")
OUT = os.path.join(ROOT, "04_evidence_table.xlsx")
MASTER = os.path.join(ROOT, "02_records", "work", "master_records.xlsx")
SNIP = re.compile(r"limit of detection|detection limit|\\bLOD\\b|sensitivity|specificity|copies|TCID|PFU|ng/mL|pg/mL|ng/ml|agreement|kappa|samples", re.I)
EVAL = {}
FIELDS = ["rec_id", "virus", "host", "analyte", "format", "label", "readout", "sample", "lod", "clinical", "section", "tags"]


def load_chart():
    d = {}
    for p in sorted(glob.glob(os.path.join(CH_DIR, "*.tsv"))):
        for line in open(p, encoding="utf-8"):
            if not line.strip() or line.startswith("#"):
                continue
            f = line.rstrip("\n").split("\t")
            assert len(f) == 12, (p, line[:60], len(f))
            d[f[0]] = f
    return d


def included():
    ws = openpyxl.load_workbook(SCREEN, read_only=True)["screening_all"]
    it = ws.iter_rows(values_only=True)
    h = next(it)
    ci = {k: i for i, k in enumerate(h)}
    out = []
    for r in it:
        if r[ci["decision_claude"]] == "INCLUDE":
            out.append(r[ci["rec_id"]])
            EVAL[r[ci["rec_id"]]] = r[ci["tag_covid_commercial_eval"]] == "probable"
    return out


def master():
    ws = openpyxl.load_workbook(MASTER, read_only=True)["master"]
    it = ws.iter_rows(values_only=True)
    h = next(it)
    return {r[0]: dict(zip(h, r)) for r in it}


def batch(size, out, mode="dev"):
    size = int(size)
    done = load_chart()
    m = master()
    ids = [i for i in included() if i not in done]
    ids = [i for i in ids if (int(m[i]["year"] or 0) >= 2015) == (mode != "brief")]
    if mode in ("dev", "eval"):
        ids = [i for i in ids if EVAL.get(i) == (mode == "eval")]
    chunk = ids[:size]
    with open(out, "w", encoding="utf-8") as f:
        for i in chunk:
            r = m[i]
            ab = (r["abstract"] or "(no abstract)").replace("\n", " ")
            lim = {"dev": 420, "eval": 200}.get(mode, 350)
            head, tail = ab[:lim], ab[lim:]
            sn = [t.strip()[:240] for t in re.split(r"(?<=[.;])\s+", tail) if SNIP.search(t)][:3]
            f.write(f"{i} | {r['year']} | {r['pub_types'][:60] if r['pub_types'] else ''}\nT: {r['title']}\nA: {head}{' …' if tail else ''}\n")
            for t in sn:
                f.write(f"S: {t}\n")
            f.write("\n")
    print(f"uncharted in this mode: {len(ids)}; wrote {len(chunk)}; range {chunk[0] if chunk else '-'}..{chunk[-1] if chunk else '-'}")


def merge():
    done = load_chart()
    m = master()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "abstract_chart"
    ws.append(["rec_id", "pmid", "doi", "year", "title", "journal", "text_assessed", "virus", "host", "analyte", "format",
               "label", "readout", "sample", "lod_as_stated", "clinical_as_stated", "section", "tags"])
    for i in included():
        if i in done:
            f = done[i]
            r = m[i]
            ws.append([i, r["pmid"], r["doi"], r["year"], r["title"], r["journal"], "abstract only"] + f[1:])
    wb.save(OUT)
    status()


def status():
    done = load_chart()
    inc = included()
    m = master()
    left = [i for i in inc if i not in done]
    new = sum(1 for i in left if int(m[i]["year"] or 0) >= 2015)
    print(f"included {len(inc)}; charted {len([i for i in inc if i in done])}; left {len(left)} (2015+: {new}, pre-2015: {len(left)-new})")


if __name__ == "__main__":
    c, a = sys.argv[1], sys.argv[2:]
    {"batch": batch, "merge": merge, "status": status}[c](*a)
