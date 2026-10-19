"""
Render Tables 1-4 to Markdown.

Table 1: test set papers.
Table 2: ground truth from papers/ep/kumada1972/kumada1972_v17_sonnet_s3.md §2
         (SRG/CLA to RI/ER/EP crosswalk).
Table 3: ground truth from papers/ep/kumada1972/kumada1972_all_v17_opus_s2fv71.md
         §"Cross-reference with Stage 3 EP filling landscape".
Table 4: EP-to-ChemOntology-AFIR parameter mapping, summarized from
         chemontology_pilot/layer_A_parameter_mapping/ep_to_chemontology_mapping.md.
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
# Repository: data in ROOT/data, output to ROOT/output. Deposit copy (Tier 7): ROOT is the deposit root, the data are in
# tier_4_classification_tables/figures_data/ and the output goes to rerun_output/ at the deposit root.
DATA_DIR = next(d for d in (ROOT / "data", ROOT / "tier_4_classification_tables" / "figures_data") if d.is_dir())
OUT = ROOT / "output" if (ROOT / "data").is_dir() else ROOT / "rerun_output"
DATA = DATA_DIR
OUT.mkdir(exist_ok=True)

# Table 1
t1 = pd.read_csv(DATA / "table1_test_set.csv")
# Shorten category for compact display
t1_md = t1.to_markdown(index=False)
(OUT / "table1_test_set.md").write_text(t1_md + "\n")
print(f"wrote {OUT / 'table1_test_set.md'}")

# Table 2
t2 = pd.read_csv(DATA / "table2_kumada_eps.csv")
t2_md = t2.to_markdown(index=False)
(OUT / "table2_kumada_eps.md").write_text(t2_md + "\n")
print(f"wrote {OUT / 'table2_kumada_eps.md'}")

# Table 3
t3 = pd.read_csv(DATA / "table3_case_studies.csv")
t3_md = t3.to_markdown(index=False)
(OUT / "table3_case_studies.md").write_text(t3_md + "\n")
print(f"wrote {OUT / 'table3_case_studies.md'}")

# Table 4
t4 = pd.read_csv(DATA / "table4_ep_chemontology_mapping.csv")
t4_md = t4.to_markdown(index=False)
(OUT / "table4_ep_chemontology_mapping.md").write_text(t4_md + "\n")
print(f"wrote {OUT / 'table4_ep_chemontology_mapping.md'}")
