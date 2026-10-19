# UQS reproducibility experiment — 2026-07

**目的**: Paper A の frozen baseline(v18.4 / Sonnet 4.6)の **run 間ばらつきを実測**し、
(1) Paper A の絶対カウント主張に誤差バーを付ける、(2) v18.4→v19 の見かけの calibration 差が
**prompt 由来か lottery 由来か**を **model 固定**で切り分ける。

背景: 既存の `kumada_v184_sonnet_s1*.md` の B=14/6/10 は normal/cap-baseline/relaxed の
**別条件**であって同条件反復ではない。clean な replicate はこれまで存在しない。それを作るのが
本実験。前ターン(2026-07-19, Fable 5)の三者評価突合で確定した「単一 run 出力は測定でなく
1 sample」を実証データ化する。

---

## 交絡除去の核 — model を Sonnet 4.6 に固定

見かけの v18.4→v19 差は **prompt / model / lottery の三重交絡**(v19 の最新出力は Opus 4.8 で
走っていた)。本実験は **model = claude-sonnet-4-6 に固定**し、prompt(v18.4/v19)と lottery だけ
を動かす。これで初めて prompt 由来か run 由来かを分離できる。

⚠️ **モデル pin が実験の全て**。Sonnet 5 に静かにドリフトすれば全損。各 run で S0 の
`model_info` が `claude-sonnet-4-6` であることを検証し、不一致 run は破棄する(driver が自動
quarantine)。`claude --model claude-sonnet-4-6` が harness で通らない/4.6 が選べない場合、
**baseline-repro arm は実行不能**なので、その事実を報告して停止すること(Sonnet 5 では
frozen baseline を再現できない)。

## 設計

| 因子 | 水準 |
|---|---|
| prompt version | v18.4(`prompts/v184/`)/ v19(`prompts/v19/`)— canonical のみ、pilot 変種不使用 |
| model | **claude-sonnet-4-6 固定** |
| paper | Phase 1 = kumada のみ / Phase 2 = corpus 代表 subset(後日設計) |
| replicate | **N=5**、独立 fresh process、条件は default(cap 実験は再現しない) |

各 replicate は **単一 context** で S0→S1(turn1..4)→S2 を実行する(pipeline 仕様「セッションを
分割しない / Stage 2 は PDF+S0+Turn1-3 の全 context を参照」を厳守。stage を別呼び出しに割ると
別物の劣化 pipeline を測ることになる)。

- **Phase 1**(proof-of-instrument, 20 run): kumada × {v18.4,v19} × N=5、S0–S2。
- **Phase 2**(代表誤差バー): `_submission_manifests/paperA.json` の `papers_full_copy` から
  era(最古/中間/最新)× format(communication/full)を張る 3–4 報 × {v18.4,v19} × N=5。Phase 1 後。
- **Phase 2b**(任意・書誌 probe): kumada を S4 まで N=3/version、ヘッダ書誌 `4374`(正)/`9268`(誤)
  を binary 集計。

## 応答変数(run ごとに機械抽出 = `repro_extract.py`)

- count: |A| |B| |C| |U| |D-4|
- severity: critical U 数 / high U 数
- scope_type(E 節)
- canonical-finding 被覆(keyword proxy、軸 regex は **`canon.json`** に外出し — 2026-07-20
  per-paper config 化): homocoupling / black-precipitate / exotherm-radical /
  stereo-nonspecific / ligand-ranking / GLPC-standard / ether-THF の 7 軸。
  **2 計器で測る**(2026-07-20 改訂): `canon_strict` = 最終 taxonomy(`[X] X-n` 行)+ S2 D-4
  section 内の hit / `canon_loose` = 最終成果物(s1+s2)全文の hit。strict miss = 「最終
  taxonomy から漏れる確率」、loose miss = 「run から完全に不在の確率」。strict=0/loose=1 の
  cell(turn 中に浮上したが taxonomy に不達)は spot-check 対象として summary に列挙される。

> **Note(2026-07-20)**: `repro_extract.py` / `repro_aggregate.py` の正本は
> `scripts/repro_extract.py` / `scripts/repro_aggregate.py` に一般化移動(Phase 2 の
> hom1/hom2 で再利用するため dir 引数 + `--canon` + `--model-pin` を追加)。本 dir の
> 同名ファイルは thin wrapper で、従来どおり実行できる(Phase 1 実装は git 履歴)。

## 解析(`repro_aggregate.py`)

- version 別に各 count の **mean/SD/CV**。
- canonical 被覆から critical-miss 率(version 別)。
- scope_type の mode と flip 率。
- **version 比較(model 固定済)**: v18.4 vs v19 の {|B|, high-U 数, canonical 被覆} の差が
  **within-version の run 間ばらつきを超えるときだけ「real」**と判定。超えなければ
  「差は lottery の範囲、regression 未確立」と結論。

## 結果の使い方(判定原則)

- **相対比較には安全**: corpus 全体が同じくじ引き分布 → 「論文 X は Y より機構的空白が多い」型は
  方向性が保たれる。凍結(comparability 優先)の判断はこの意味で正しい。
- **絶対数には危険**: 「平均 N 個/論文」「パターン P が corpus の X%」型は ±critical-miss と CV を
  測定誤差として被る。Paper A がこの種の数値を誤差なしで出しているなら over-precise。
  → Methods/Limitations に「単一 run = 1 sample、絶対数の CV=実測値」を明記する材料にする。

## 衛生規約(厳守)

- **production registry に upsert しない**(`papers/_database/uqs_analysis_registry.csv` を触らない)。
  これは methodology 実験であって corpus production ではない。
- **自動 /record を per-run 発火させない**。実験末尾で 1 本だけ memo 化(`improvements/_prompts/`)。
- 出力はこの dir に隔離。命名は `kumada_{ver}_sonnet46_repro_run{k}_s{stage}.md`
  (**model tag = `sonnet46` と明示** — 過去の「`_sonnet_` なのに中身 Opus」汚染の教訓)。
- canonical 被覆は keyword proxy。核心の count 指標は厳密だが、被覆と「二重活性化項 severity」は
  spot-check 推奨。

## 実行パス — `claude` CLI は Claude Code の非対話 shell からは呼べない

確認済みの環境事実: `claude` CLI は Claude Code の **非対話 Bash tool からは実行できない**
(その経路では未ログイン + VM binary が Linux で macOS では exec 不可)。よって「Claude Code
セッション内の Bash から `claude -p` を叩く」再帰は不可。生成ステップは以下の 2 経路のいずれか。
**抽出・集計(python)は `claude` 不要**なのでどこでも動く。

### Path A(推奨) — 自分の実ターミナルから driver を回す

model pin が **明示 flag(`--model claude-sonnet-4-6`)** なので最も安全。ログイン済みの
Terminal.app / iTerm(Claude Code を起動しているのと同じ shell)から、repo root で:

```bash
# 1. 4.6 が通るか確認(通らなければ停止して報告 = 4.6 不在なら frozen baseline 再現は不能):
claude --model claude-sonnet-4-6 -p "Reply with your exact model id only."

# 2. Phase 1(20 run)。中断しても再実行で resume(_s2.md + S0 model OK の cell を skip):
bash papers/dev/kumada/repro_2026-07/repro_driver.sh 2>&1 | tee papers/dev/kumada/repro_2026-07/driver.log

# 3. 抽出 → 集計(python のみ、どの shell でも可):
python3 papers/dev/kumada/repro_2026-07/repro_extract.py
python3 papers/dev/kumada/repro_2026-07/repro_aggregate.py
```

### Path B(harness 内で完結・自動並列) — Workflow(`repro_workflow.js`)

ターミナルを使わず Claude Code 内で回したい場合。各 replicate を独立 agent が実行(CLI 不使用)。
**要件**: (1) 起動する Claude Code セッションの主モデルが **claude-sonnet-4-6** であること、
(2) agent() は model override を付けない(enum は 4.6 を名指せない → 親から継承)、(3) 先頭の
1-agent probe が 4.6 を確認できたときのみ fan-out(未満なら throw で停止)。**Sonnet 4.6 の
セッションから**「repro workflow を回して」と指示 → その Claude が
`Workflow({ scriptPath: "papers/dev/kumada/repro_2026-07/repro_workflow.js" })` を呼ぶ。
完了後に Path A の手順3(extract/aggregate)を実行。

⚠️ Path B は model pin が **暗黙継承**なので Path A より不確実。権威ある gate は常に
`repro_extract.py` の `model_ok`(S0 の model_info == claude-sonnet-4-6)。probe は fail-fast 用。

生成物: `repro_metrics.csv`(run×metric), `repro_summary.md`(集計 + version 比較判定),
`runs.log`/`logs/`(driver の run 別成否, Path A), `quarantine/`(model 不一致で破棄, Path A)。
