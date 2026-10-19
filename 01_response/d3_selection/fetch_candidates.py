#!/usr/bin/env python3
"""D3 candidate pool per prereg §2.1 (commit 88e7cc3). Crossref query + corpus CSV."""
import csv, json, urllib.request, urllib.parse, time, pathlib
OUT = pathlib.Path("manuscript_A/DigitalDiscovery_R1/01_response/d3_selection")
UA = {"User-Agent": "UQS-PaperA-R1/1.0 (mailto:yono@sci.hokudai.ac.jp)"}
def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
def date_of(m):
    for k in ("published-online", "published-print", "issued"):
        p = m.get(k, {}).get("date-parts", [[None]])[0]
        if p and p[0]: return k, "-".join(f"{x:02d}" if i else str(x) for i, x in enumerate(p))
    return None, None
pool = {}
cursor = "*"
while True:
    q = urllib.parse.urlencode({"query.bibliographic": "Heck", "filter": "from-online-pub-date:2026-02-01,type:journal-article",
                                "rows": 1000, "cursor": cursor, "select": "DOI,title,abstract,published-online,published-print,issued,container-title,type"})
    d = get("https://api.crossref.org/works?" + q)["message"]
    for m in d["items"]:
        t = " ".join(m.get("title", [])); a = m.get("abstract", "") or ""
        if "heck" in (t + a).lower():
            pool[m["DOI"].lower()] = {"doi": m["DOI"].lower(), "title": t, "journal": " ".join(m.get("container-title", [])),
                                      "src": "crossref", "has_abstract": bool(a)}
    if not d["items"] or len(d["items"]) < 1000: break
    cursor = d["next-cursor"]; time.sleep(1)
for x in csv.DictReader(open("corpus/corpus_paper_list.csv", encoding="utf-8-sig")):
    if "heck" in (x["Title"] + x["Abstract"]).lower() and x["DOI"]:
        pool.setdefault(x["DOI"].lower(), {"doi": x["DOI"].lower(), "title": x["Title"], "journal": x["Journal"], "src": "corpus"})["src_corpus"] = True
rows = []
for doi, r in sorted(pool.items()):
    try:
        m = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
    except Exception as e:
        r["date_key"], r["date"] = "error", str(e)[:40]; rows.append(r); continue
    r["date_key"], r["date"] = date_of(m); r["type"] = m.get("type"); rows.append(r); time.sleep(0.2)
with open(OUT / "candidate_pool.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["doi", "date", "date_key", "type", "journal", "title", "src", "src_corpus", "has_abstract"], extrasaction="ignore")
    w.writeheader(); w.writerows(rows)
print(len(rows), "candidates;", sum(1 for r in rows if (r.get("date") or "") >= "2026-02-01"), "dated >= 2026-02-01")
