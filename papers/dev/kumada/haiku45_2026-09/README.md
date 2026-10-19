# Haiku 4.5 追加 run — 2026-09

**目的**: Claude Haiku 4.5 の retirement floor（2026-10-15、Anthropic 公式 lifecycle）までに、Haiku でしか取れない
run を取っておく。洗い出しの根拠は `improvements/uqs_model_migration_sonnet5_readiness_20260826.md` §4.1。

| ID | 条件 | run | 対応する論文記述 |
|---|---|---|---|
| H1 | v18.4（S0–S2）+ Stage 3 v4 + Stage 4 v6 | run1–3 | Paper A SI-6 の Phase 2 verification path (b)（v18.4-matched N × 4-model rerun）の Haiku arm |
| H1b | v18.4（S0–S2）のみ | **run4–5**（2026-10-01 追加） | **Referee 2 項目 3**（モデル横断の再現性統計量）に答えるため、Sonnet 4.6 repro の 5 run と**同じ 10 pair** に揃えた。floor 2026-10-15 後は二度と揃えられない。S3/S4 は作らない（run1–3 でも別 agent だったので S0–S2 の context 条件は同一） |
| H2 | v17（S0–S2）+ Stage 3 v2 + Stage 4 v2 | run2–3 | Paper A SI-6 の v17 Haiku 4.5 run の反復。run1 = 既存 `../kumada_v17_haiku_*.md`（2026-04-19、CLI main session） |

## 実行環境（harness）

- Claude Code の Agent tool で `model: haiku` を指定した subagent。2026-09-14 の probe で system prompt 上の
  model ID が `claude-haiku-4-5-20251001` であることを確認（Haiku は 4.5 以外に選択肢がない）。
- 1 agent = 1 context。各 run は互いに独立した新規 context。
- **H1 は S0–S2 と S3+S4 を別 agent に分けた**。subagent は起動時点で約 74K token（CLAUDE.md・MEMORY index・
  skill 一覧）を読み込み済みで、v18.4 の S0–S4 を 1 context に載せると見積り約 175K と Haiku の 200K 上限に近く、
  途中 compaction で「S2 は全履歴を参照」の規則が黙って崩れる恐れがあるため。S0→Turn1→2→3→4→S2 は 1 context で連続実行。
  S3+S4 は CLAUDE.md の単独ステージ実行（`s3+s4を実行`）と同じく、PDF + 同 run の S0–S2 出力を読んで実行。
- **H2 は S0–S4 を 1 context で実行**（見積り約 140K）。SI-6 の元 run（S3/S4 を同一の拡張 context で実行）に合わせた。

## 元の run との差（比較時に注意）

- H2 run1（元 run）は CLI main session、run2–3 は subagent。起動時に読み込まれている文脈（CLAUDE.md の版、
  MEMORY index、skill 一覧）が異なる。
- 表 crop（`scripts/table_crop.py`）は使っていない（Paper A の v18.4 production と SI-6 の元 run に合わせる）。

## 隔離

- 入力は `../Kumada_1972.pdf`（Read で直接）と `prompts/` の該当 prompt file のみ。
- 読まない: `papers/dev/kumada/` の既存出力とサブフォルダ（本 folder の他 run を含む）、`kumada_bundle.pdf`、
  `_table_crops/`、`analysis/`、`improvements/`（S3v4/S4v6 prompt 内で参照される memo を含む）、`manuscript_*/`、
  `submissions/`、`zenodo_deposit_*/`、`diary/`、`docs/`、memory ファイル。
- 既知の曝露: subagent には CLAUDE.md と MEMORY index が自動で読み込まれる。MEMORY index には Kumada を名指しする
  entry が 2 件あるが、hook は途中で切れていて所見本文は含まない。main session で実行しても同じ曝露になる。

## 命名

- H1: `kumada_v184_haiku45_run{k}_{s0|s1_turn1|s1_turn2|s1_turn3|s1|s2|s3v4|s4v6}.md`
- H2: `kumada_v17_haiku45_run{k}_{s0|s1_turn1|s1_turn2|s1_turn3|s1|s2|s3v2|s4v2}.md`
- 検証: `python3 scripts/registry_helper.py audit-provenance --scan-fs papers/dev/kumada/haiku45_2026-09 --strict`

## プロトコル逸脱と再実行（2026-09-14）

初回の agent には「prompt を Read → 出力 → Write → 次へ」と指示したが、tool call の順序（agent transcript から
抽出）を確認したところ、以下は**後段の prompt を先に読んでから前段の出力を書いていた**。UQS の手順では各 stage の
prompt は前段の出力を書いた後に初めて与えられるので、前段の出力が後段の指示を見て作られた可能性を排除できない。

| run | 逸脱 |
|---|---|
| H1 run1–3 S0–S2 | 6 prompt を全部読んでから S0→S2 を書いた |
| H1 run1–3 S3+S4 | S4 prompt を読んでから S3 を書いた |
| H2 run3 | S0–S2 は順守、S4 prompt を読んでから S3 を書いた |
| H2 run2 | **逸脱なし**（全 stage で Read → Write が交互）→ 本 folder に残す |

逸脱した 32 file は `_deviation_prompt_lookahead/` に移した（削除しない、解析には使わない）。
再実行は **1 turn に 1 prompt** の形にする: agent には最初に S0 prompt の path だけを渡し、出力を書いたら停止させる。
呼び出し側が SendMessage で同じ agent（context はそのまま）に次の prompt の path を渡す。
agent は次の prompt の path をその時点まで知らないので、先読みが構造的に起きない。
H1 の S0–S2 と S3+S4 を別 agent に分ける点は変えない。

## 完了状態（2026-09-14）

| run | 実行方式 | Read / Write | context 最大 | compaction | 許可外 file |
|---|---|---|---|---|---|
| H1 run1 S0–S2 / S3–S4 | 1 turn 1 prompt | 7/6 ・ 9/2 | 159K / 162K | なし | なし |
| H1 run2 S0–S2 / S3–S4 | 1 turn 1 prompt | 10/6 ・ 9/2 | 182K / 164K | なし | なし |
| H1 run3 S0–S2 / S3–S4 | 1 turn 1 prompt | 7/6 ・ 9/2 | 165K / 170K | なし | なし |
| H2 run2 | 一括指示（順序は transcript で確認済み） | 13/8 | 154K | なし | なし |
| H2 run3 | 1 turn 1 prompt | 9/8 | 187K | なし | なし |

- 各 run 8 file（計 40）。`audit-provenance --scan-fs --strict` = mismatch 0。
- registry: `(kumada, v184, haiku45)` / `(kumada, v17, haiku45)` とも `analyzed`。
- 検査方法: 各 turn 後に agent transcript から tool call 列を抽出し、(a) prompt Read → 出力 Write の順序、
  (b) 許可外 path の有無、(c) 連続 API call 間で input context が 15K 以上減る箇所（compaction の痕跡）を確認した。
- H1 run2 の Read が多いのは、S0–S2 の途中で自分の過去出力と PDF を読み直したため（同 run の入力のみ）。
- Haiku が出力を返答本文に書き Write しなかった turn が 2 回あった（run1 S0、run1 S3）。同じ agent に
  「作り直さず保存」を指示して保存させ、次の prompt はその後に渡した。
- 形式上の残差: H1 run1 / run3 の Turn 1–3 などで末尾の `inference_time_sec` 行が欠ける file がある（内容には影響しない）。


## 2026-10-01 追記 — run4/run5 と測定結果

**追加の経緯**: Paper A の査読（Digital Discovery R1）Referee 2 項目 3 が
「モデル間の VQ の食い違いを era-norm frame の差に帰しているが、それは出力の不安定さかもしれない。
**モデル横断の再現性・頑健性の統計量**を supplement せよ」と要求。Haiku を含む 4 モデル比較に関わるため、
floor（2026-10-15）前に対称なデータを確保した。

**先に既存を調べた**: run1–3 と Sonnet 4.6 repro 5 run（`../repro_2026-07/`）で**測定自体は可能**だった。
run4/5 は「測定に必要」ではなく「**pair 数を 3→10 にして Sonnet 4.6 と対称にする**」ために取った。

**実行条件**: H1 と同じ（Agent tool subagent・model haiku・S0→S2 を 1 context・表 crop なし）。
隔離の禁止リストは本 README のものをそのまま prompt に転記した。provenance 84 file 不一致 0。

**測定（kumada 1972 × v18.4）**:

| | J | pair |
|---|---|---|
| within-Haiku 4.5 | **0.263 ± 0.088** | 10 |
| within-Sonnet 4.6 | **0.297 ± 0.054** | 10 |
| cross（Haiku × Sonnet 4.6） | **0.188 ± 0.090** | 25 |

> **注（2026-10-16）**: within-Haiku の 0.263 ± 0.088 はこの時点の値。寄託した照合スクリプト（`classification_concordance.py`）での再計算値 **0.258 ± 0.090** が SI-6.10 の報告値（他の 2 値は同じ）。

**cross < within の下限** ∴ この 2 モデルの食い違いの大部分は **run 揺れの範囲内**。
era-norm frame の差として解釈する前に、この下限を示す必要がある。**査読者の疑いは正しい方向**。
計器は `scripts/classification_concordance.py`（within/cross を同時に出す設計）。

**比較時の注意（新規）**: run4/5 は **item 行の書式が run1–3 と違う**
（run1–3 `A1 | P1:Lcol:37-40* | "…"` / run4–5 `B-2 | loc: … | quote: …`）。
同じ prompt・同じモデルで書式が揺れている = **それ自体が「出力の不安定さ」の実例**。
signature 抽出はラベル付き書式に対応済みなので測定には影響しない。

**計器の修正（同日）**: `classification_concordance.py` の item 行 regex が
v18.4 の `A1 |`（ハイフンなし）を拾えず、**Haiku を 5.3 項目/run と誤読**していた（実際 17.0）。
第 2 分岐のハイフンを optional 化。**v27.1 側 30 file の項目数は 1 件も変わらないことを検証済み**。
