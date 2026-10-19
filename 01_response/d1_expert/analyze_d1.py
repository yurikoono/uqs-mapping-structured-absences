#!/usr/bin/env python3
"""D1 analysis, as fixed in preregistration_D1_itemwise.md (Analysis items 1-4; Amendments 1-2).
Primary: R1 and R2. Secondary: all pairs and Fleiss' kappa over the raters who returned forms.
Reads ratings/ratings.csv only. Prints Markdown."""
import csv, itertools, math, collections
CATS = ["i", "ii", "iii", "iv", "v", "vi"]
COLL = {"i": "worth", "ii": "worth", "iii": "worth", "iv": "not", "v": "not", "vi": "unable"}
rows = list(csv.DictReader(open("ratings/ratings.csv")))
raters = sorted({r["rater"] for r in rows if r["category"]})
R = {r: {int(x["form_no"]): x for x in rows if x["rater"] == r} for r in raters}
items = sorted(R[raters[0]])
typ = {i: R[raters[0]][i]["type"] for i in items}

def kappa(a, b, labels):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[l] * cb[l] for l in labels) / n / n
    return po, (po - pe) / (1 - pe) if pe < 1 else float("nan")
def fleiss(table, labels):  # table: list of per-item rating lists
    N, n = len(table), len(table[0])
    P = [(sum(c * c for c in collections.Counter(t).values()) - n) / (n * (n - 1)) for t in table]
    Pbar = sum(P) / N
    p = [sum(t.count(l) for t in table) / (N * n) for l in labels]
    Pe = sum(x * x for x in p)
    return (Pbar - Pe) / (1 - Pe)
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
cat = lambda r: [R[r][i]["category"] for i in items]
col = lambda r: [COLL[c] for c in cat(r)]

print("## 1. Category distribution per rater\n")
print("| rater | " + " | ".join(f"({c})" for c in CATS) + " | high / medium / low confidence |")
print("|---|" + "---|" * (len(CATS) + 1))
for r in raters:
    cc = collections.Counter(cat(r)); cf = collections.Counter(R[r][i]["confidence"] for i in items)
    print(f"| {r} | " + " | ".join(str(cc[c]) for c in CATS) + f" | {cf['high']} / {cf['medium']} / {cf['low']} |")
print("\n### Per item type (Stage 1 items n = %d, D-4 candidates n = %d)\n" % (sum(t == "S1" for t in typ.values()), sum(t == "D4" for t in typ.values())))
print("| rater | type | " + " | ".join(f"({c})" for c in CATS) + " |")
print("|---|---|" + "---|" * len(CATS))
for r in raters:
    for t in ("S1", "D4"):
        cc = collections.Counter(R[r][i]["category"] for i in items if typ[i] == t)
        print(f"| {r} | {t} | " + " | ".join(str(cc[c]) for c in CATS) + " |")

print("\n## 2. Inter-rater agreement\n")
print("| pair | role | raw agreement, 6 categories | Cohen's κ, 6 categories | raw agreement, collapsed | Cohen's κ, collapsed |")
print("|---|---|---|---|---|---|")
for a, b in itertools.combinations(raters, 2):
    p6, k6 = kappa(cat(a), cat(b), CATS); pc, kc = kappa(col(a), col(b), ["worth", "not", "unable"])
    role = "**primary**" if (a, b) == ("R1", "R2") else "secondary"
    print(f"| {a}–{b} | {role} | {round(p6*10)}/10 | {k6:.2f} | {round(pc*10)}/10 | {kc:.2f} |")
if len(raters) > 2:
    print(f"\nFleiss' κ over {len(raters)} raters (secondary): 6 categories {fleiss([[R[r][i]['category'] for r in raters] for i in items], CATS):.2f}; "
          f"collapsed {fleiss([[COLL[R[r][i]['category']] for r in raters] for i in items], ['worth','not','unable']):.2f}.")

print("\n## 3. Proportion judged worth raising, (i)–(iii), per rater (95% Wilson interval)\n")
print("| rater | worth raising | 95% CI | not worth raising, (iv)–(v) | unable, (vi) |")
print("|---|---|---|---|---|")
for r in raters:
    cc = collections.Counter(col(r)); lo, hi = wilson(cc["worth"], len(items))
    print(f"| {r} | {cc['worth']}/{len(items)} | {lo:.2f}–{hi:.2f} | {cc['not']}/{len(items)} | {cc['unable']}/{len(items)} |")

print("\n## Per item (all raters)\n")
print("| item | type | " + " | ".join(raters) + " | worth raising |")
print("|---|---|" + "---|" * (len(raters) + 1))
for i in items:
    cs = [R[r][i]["category"] for r in raters]
    print(f"| {i} | {typ[i]} | " + " | ".join(f"({c})" for c in cs) + f" | {sum(COLL[c]=='worth' for c in cs)}/{len(raters)} |")
