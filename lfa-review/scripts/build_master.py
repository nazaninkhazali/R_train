"""Build the master record table, duplicate flags, screening tags and the pilot sample
from PubMed-format exports (MEDLINE .txt).

Usage:
    python3 -I build_master.py OUT_DIR EXPORT1.txt [EXPORT2.txt ...]

Tags are aids for screening only; they never decide inclusion.
"""
import collections
import random
import re
import sys

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

PILOT_SEED = 20261028
PILOT_N = 50

# --- parsing -----------------------------------------------------------------

def parse_records(path):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    for block in text.split("\n\n"):
        if not block.strip().startswith("PMID-"):
            continue
        fields = collections.defaultdict(list)
        tag = None
        for line in block.split("\n"):
            if len(line) >= 6 and line[4] == "-" and line[:4].strip():
                tag = line[:4].strip()
                fields[tag].append(line[6:].strip())
            elif tag and line.startswith("      "):
                fields[tag][-1] += " " + line.strip()
        yield fields


def first(f, tag):
    return f[tag][0] if f.get(tag) else ""


def get_doi(f):
    for v in f.get("AID", []) + f.get("LID", []):
        if v.endswith("[doi]"):
            return v[:-5].strip().lower()
    return ""


def record_row(f, source):
    dp = first(f, "DP")
    m = re.match(r"(\d{4})", dp)
    return {
        "pmid": first(f, "PMID"),
        "doi": get_doi(f),
        "pmcid": first(f, "PMC"),
        "year": m.group(1) if m else "",
        "first_author": first(f, "AU"),
        "n_authors": len(f.get("AU", [])),
        "title": first(f, "TI") or first(f, "BTI"),
        "abstract": " ".join(f.get("AB", [])),
        "journal": first(f, "TA") or first(f, "JT"),
        "source_citation": first(f, "SO"),
        "language": ";".join(f.get("LA", [])),
        "pub_types": ";".join(f.get("PT", [])),
        "mesh": ";".join(f.get("MH", [])),
        "keywords": ";".join(f.get("OT", [])),
        "comments_corrections": ";".join(
            f.get("EIN", []) + f.get("RIN", []) + f.get("UIN", []) + f.get("ROF", []) + f.get("EFR", [])
        ),
        "export_file": source,
    }

# --- tagging -----------------------------------------------------------------

def rx(*terms):
    return re.compile("|".join(terms), re.I)

LFA_TEXT = rx(r"lateral[\s-]?flow", r"immuno-?chromatograph", r"\bLFIAs?\b", r"test strips?",
              r"strip tests?", r"dipsticks?", r"immunostrips?")
RDT_TEXT = rx(r"rapid antigen tests?", r"antigen rapid diagnostic", r"\bAg-?RDTs?\b", r"rapid diagnostic tests?")
COLOR_CLUE = rx(r"gold", r"\bAuNPs?\b", r"latex", r"colou?rimetric", r"naked[\s-]eye", r"visual",
                r"silver", r"nanozyme", r"peroxidase", r"Prussian blue", r"\bTMB\b", r"carbon (?:black|nano)",
                r"cellulose nano", r"liposome", r"smartphone", r"cell ?phone", r"mobile phone")
OTHER_SIGNAL = rx(r"fluoresc", r"quantum dot", r"europium", r"lanthanide", r"upconver", r"\bSERS\b",
                  r"raman", r"chemilumin", r"electrochem", r"photothermal", r"magnetic", r"time-resolved")
NAAT = rx(r"\bLAMP\b", r"loop-mediated", r"\bRPA\b", r"recombinase", r"CRISPR", r"Cas1[23]", r"\bPCR\b",
          r"isothermal", r"nucleic acid")
COVID = rx(r"SARS-CoV-2", r"COVID", r"coronavirus disease 2019")
EVAL = rx(r"commercial", r"\bkits?\b", r"diagnostic accuracy", r"clinical performance", r"sensitivity",
          r"specificity", r"real-world", r"evaluation", r"Ag-?RDT", r"rapid antigen", r"self-test")
DEVELOP = rx(r"we (?:developed|designed|fabricated|propose|present|report)", r"novel", r"was developed",
             r"were synthesi", r"conjugat", r"limit of detection|detection limit|\bLOD\b")
HOST_PLANT = rx(r"\bplants?\b", r"\bcrops?\b", r"leaf|leaves", r"potyvir", r"begomovir", r"geminivir",
                r"tospovir", r"tobamovir", r"luteovir", r"closterovir", r"mosaic virus", r"\bTMV\b", r"\bTSWV\b",
                r"\bPVY\b", r"ToBRFV", r"\bBBTV\b", r"tristeza", r"plum pox", r"maize", r"potato", r"tomato",
                r"citrus", r"grapevine", r"banana", r"pepper")
HOST_AQUA = rx(r"shrimp", r"prawn", r"crustacea", r"\bfish", r"salmon", r"\bkoi\b", r"carp", r"tilapia",
               r"oyster", r"shellfish", r"mollus", r"aquacultur", r"white spot syndrome", r"\bWSSV\b", r"IHHNV",
               r"nodavir", r"nervous necrosis")
HOST_ANIMAL = rx(r"swine", r"porcine", r"\bpigs?\b", r"poultry", r"chicken", r"\bduck", r"avian", r"bovine",
                 r"cattle", r"\bcows?\b", r"sheep", r"\bgoats?\b", r"ovine", r"caprine", r"canine", r"\bdogs?\b",
                 r"feline", r"\bcats?\b", r"equine", r"horse", r"veterinar", r"livestock", r"wildlife", r"\bbats?\b",
                 r"foot-and-mouth|foot and mouth", r"Newcastle", r"African swine fever", r"PRRS", r"PEDV",
                 r"parvovirus", r"distemper", r"rabies", r"bluetongue", r"lumpy skin", r"petits ruminants",
                 r"pseudorabies", r"circovirus", r"bursal", r"Marek")

REVIEW_PT = {"Review", "Systematic Review", "Meta-Analysis", "Scoping Review"}
NONPRIMARY_PT = {"Editorial", "Comment", "News", "Newspaper Article", "Interview", "Biography",
                 "Historical Article", "Portrait", "Guideline", "Practice Guideline", "Consensus Development Conference"}
NOTICE_PT = {"Published Erratum", "Retraction of Publication", "Expression of Concern"}


def tags_for(row):
    tiab = row["title"] + " " + row["abstract"]
    text_all = tiab + " " + row["keywords"]
    pts = set(row["pub_types"].split(";")) if row["pub_types"] else set()
    mesh = row["mesh"]
    t = {}
    t["tag_non_english"] = "yes" if "eng" not in row["language"].split(";") else ""
    t["tag_no_abstract"] = "yes" if not row["abstract"].strip() else ""
    t["tag_review"] = "yes" if pts & REVIEW_PT else ""
    t["tag_nonprimary_type"] = ";".join(sorted(pts & NONPRIMARY_PT))
    t["tag_notice"] = ";".join(sorted(pts & NOTICE_PT))
    t["tag_retracted"] = "yes" if "Retracted Publication" in pts else ""
    t["tag_preprint"] = "yes" if "Preprint" in pts else ""
    t["tag_letter"] = "yes" if "Letter" in pts else ""
    has_lfa = bool(LFA_TEXT.search(text_all))
    has_rdt = bool(RDT_TEXT.search(text_all))
    has_rs = "Reagent Strips" in mesh
    if has_lfa:
        t["tag_lfa_term"] = "LFA text term"
    elif has_rdt:
        t["tag_lfa_term"] = "RDT term only"
    elif has_rs:
        t["tag_lfa_term"] = "Reagent Strips MeSH only"
    else:
        t["tag_lfa_term"] = "none found in title/abstract/keywords"
    t["tag_colorimetric_clue"] = "yes" if COLOR_CLUE.search(text_all) else ""
    t["tag_other_signal_clue"] = "yes" if OTHER_SIGNAL.search(text_all) else ""
    t["tag_nucleic_acid_clue"] = "yes" if NAAT.search(text_all) else ""
    t["tag_covid_commercial_eval"] = (
        "probable" if COVID.search(text_all) and EVAL.search(text_all) and not DEVELOP.search(tiab) else ""
    )
    hosts = []
    if "Humans" in mesh.split(";") or re.search(r"\bpatients?\b|\bhuman", tiab, re.I):
        hosts.append("human")
    if HOST_ANIMAL.search(text_all) or re.search(r"(^|;)Animals(;|$)", mesh):
        hosts.append("animal")
    if HOST_AQUA.search(text_all):
        hosts.append("aquaculture")
    if HOST_PLANT.search(text_all):
        hosts.append("plant")
    t["tag_host_clue"] = ";".join(hosts)
    return t


def norm_title(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

# --- output ------------------------------------------------------------------

def write_sheet(ws, rows, cols, widths=None, wrap=()):
    ws.append(cols)
    for c in ws[1]:
        c.font = Font(bold=True)
        c.fill = PatternFill("solid", fgColor="DDDDDD")
    for r in rows:
        ws.append([r.get(c, "") for c in cols])
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = ws.dimensions
    for i, c in enumerate(cols, start=1):
        letter = openpyxl.utils.get_column_letter(i)
        ws.column_dimensions[letter].width = (widths or {}).get(c, 14)
        if c in wrap:
            for cell in ws[letter][1:]:
                cell.alignment = Alignment(wrap_text=True, vertical="top")


def main():
    out_dir, exports = sys.argv[1], sys.argv[2:]
    rows, seen = [], {}
    raw_count = collections.Counter()
    for path in exports:
        name = path.rsplit("/", 1)[-1]
        for f in parse_records(path):
            raw_count[name] += 1
            row = record_row(f, name)
            if row["pmid"] in seen:
                seen[row["pmid"]]["export_file"] += ";" + name
                continue
            seen[row["pmid"]] = row
            rows.append(row)

    by_doi, by_title = collections.defaultdict(list), collections.defaultdict(list)
    for r in rows:
        if r["doi"]:
            by_doi[r["doi"]].append(r["pmid"])
        nt = norm_title(r["title"])
        if len(nt) > 30:
            by_title[nt].append(r["pmid"])
    for r in rows:
        r.update(tags_for(r))
        same = set(by_doi.get(r["doi"], [])) | set(by_title.get(norm_title(r["title"]), []))
        same.discard(r["pmid"])
        r["possible_duplicate_of"] = ";".join(sorted(same))

    rows.sort(key=lambda r: int(r["pmid"]))
    for i, r in enumerate(rows, start=1):
        r["rec_id"] = f"R{i:05d}"

    rng = random.Random(PILOT_SEED)
    pilot = rng.sample(rows, PILOT_N)

    base_cols = ["rec_id", "pmid", "doi", "year", "first_author", "title", "abstract", "journal",
                 "language", "pub_types", "keywords", "mesh", "pmcid", "source_citation",
                 "comments_corrections", "export_file"]
    tag_cols = ["possible_duplicate_of", "tag_non_english", "tag_no_abstract", "tag_review",
                "tag_nonprimary_type", "tag_notice", "tag_retracted", "tag_preprint", "tag_letter",
                "tag_lfa_term", "tag_colorimetric_clue", "tag_other_signal_clue", "tag_nucleic_acid_clue",
                "tag_covid_commercial_eval", "tag_host_clue"]
    widths = {"title": 60, "abstract": 90, "mesh": 30, "keywords": 30}

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "master"
    write_sheet(ws, rows, base_cols + tag_cols, widths)
    wb.save(f"{out_dir}/master_records.xlsx")

    # Screening workbook: tags are NOT shown in the author's pilot sheet (blinding).
    decision_cols = ["decision_claude", "reason_claude", "note_claude",
                     "decision_author", "reason_author", "note_author", "final_decision", "final_reason"]
    pilot_cols = ["rec_id", "pmid", "doi", "year", "title", "abstract", "journal", "language", "pub_types",
                  "decision_author", "reason_author", "note_author"]
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "pilot_author"
    write_sheet(ws, pilot, pilot_cols, {"title": 50, "abstract": 100, "note_author": 30},
                wrap=("title", "abstract"))
    ws2 = wb.create_sheet("screening_all")
    write_sheet(ws2, rows, ["rec_id", "pmid", "doi", "year", "title", "journal", "language", "pub_types"]
                + tag_cols + decision_cols, {"title": 60})
    ws3 = wb.create_sheet("codes")
    codes = [
        ("Decision", "INCLUDE = may meet all criteria (go to full text)"),
        ("Decision", "EXCLUDE = clearly fails at least one criterion"),
        ("Decision", "UNSURE = cannot tell from title/abstract (go to full text)"),
        ("E1", "Target is not a virus (bacteria, fungi, parasites, prions, viroids, phages, or non-infectious)"),
        ("E2", "Not a lateral flow assay (e.g. ELISA, PCR only, Western blot, vertical flow, urine/glucose strip, µPAD without lateral flow)"),
        ("E3", "Lateral flow assay but not colorimetric (fluorescent, SERS, chemiluminescent, electrochemical, magnetic, photothermal only)"),
        ("E4", "Publication type out of scope: review, editorial, comment, news, erratum, retraction notice, preprint, conference abstract, thesis, patent"),
        ("E5", "Not in English"),
        ("E6", "No original assay data (e.g. guideline, opinion, policy, modelling or cost study only)"),
        ("E7", "Duplicate record of an included record"),
        ("E8", "Other (write the reason in the note)"),
        ("Rule", "When in doubt, choose UNSURE, not EXCLUDE. A missing label name in the abstract is NOT a reason to exclude."),
        ("Rule", "Commercial test evaluations (e.g. SARS-CoV-2 antigen tests) are INCLUDED if the device is a lateral flow test read visually or by reader."),
    ]
    write_sheet(ws3, [{"code": a, "meaning": b} for a, b in codes], ["code", "meaning"], {"meaning": 120})
    wb.save(f"{out_dir}/03_screening.xlsx")

    # Summary
    def cnt(col, val=None):
        return sum(1 for r in rows if (r[col] == val if val is not None else r[col]))
    print("raw records per file:", dict(raw_count), "sum", sum(raw_count.values()))
    print("unique PMIDs:", len(rows))
    print("records with possible DOI/title duplicate:", cnt("possible_duplicate_of"))
    for c in tag_cols[1:]:
        vals = collections.Counter(r[c] for r in rows if r[c])
        print(c, dict(vals.most_common(6)))
    print("pilot rec_ids:", " ".join(r["rec_id"] for r in pilot))


if __name__ == "__main__":
    main()
