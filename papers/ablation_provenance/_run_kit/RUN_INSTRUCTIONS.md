# Ablation run 実行手順（実行 session 用 / 1 session = 1 run）

> ⚠ 本 file は手順のみを含む（解析所見・スコア・先行結果は一切書かない/読まない —
> 汚染防止）。実行 session はこの file と該当 stub（Arm W のみ）以外の ablation 資料を開かない。

## 事前チェック（全 run 共通、HARD STOP）

1. `/model` で **Sonnet 4.6** を選択し、model id を**逐語**確認。合格 = 次の **2 形のいずれかと
   完全一致**: `claude-sonnet-4-6` または `claude-sonnet-4-6-20251001`（harness は短縮形で
   報告することがある — Amendment 2）。それ以外（`claude-sonnet-5` 系・bare `sonnet`・
   他のいかなる文字列）は即 halt。**glob・部分一致・alias 推論による自己判断は禁止**
   （Sonnet 5 との取り違え防止が目的）。出力の `model_info:` には**報告された文字列を
   そのまま**書く（日付形を自分で補完しない）。
2. 本 run の (paper_id, arm, k) を確認し、出力先 folder を作成:
   `papers/ablation_provenance/{paper_id}/arm{P|W}/run{k}/`
3. registry に upsert（status=analyzing、notes=`ablation_paperA;arm{P|W};r{k}`、
   Arm W はさらに `;noPDF`）。

## Arm P（PDF あり、k=1..3）

標準の S0–S2 実行（CLAUDE.md の実行手順どおり、ただし出力先のみ本 zone）:
1. PDF を Read で直接読む（正本の場所: kumada=`papers/dev/kumada/Kumada_1972.pdf`、
   murai=`papers/dev/murai/Murai_1993.pdf`、app1/app2/scr2/hom2 =
   `papers/test/{id}/` 内の本文 PDF。**`*_si*.pdf`・`*_bundle.pdf` は読まない**）
2. prompts/v184 を順に適用: `prompt_stage0_v184.md` → `prompt_stage1_turn1_v184.md` →
   turn2 → turn3 → `prompt_stage1_turn4_v184.md` → `prompt_stage2_v184.md`
   （セッション分割禁止、全文脈保持。S3/S4 は実行しない）
3. 出力命名: `{paper_id}_v184_sonnet46_s0_ablP_r{k}.md`、
   `..._s1_turn1_ablP_r{k}.md` … `..._s1_ablP_r{k}.md`、`..._s2_ablP_r{k}.md`
4. **papers/dev|test 内の既存解析出力（*_s*.md）は開かない**

## Arm W（書誌 stub のみ、k=1..3）

1. **PDF は開かない。papers/dev|test の既存出力も開かない。** 入力は
   `papers/ablation_provenance/_run_kit/stub_{paper_id}.txt` のみ。
2. prompts/v184 を Arm P と**逐語同一**の順で適用。各 stage で通常 PDF を参照する箇所は、
   stub の書誌情報を「入手できた全文書情報」として扱う（prompt の変更・注記の追加は禁止 —
   入力差し替えのみ）。
3. 出力命名: `..._ablW_r{k}.md`（他は Arm P と同形式）。
4. モデルが「本文がない」と述べる場合もそのまま出力として保存する（それ自体がデータ）。

## 事後（全 run 共通）

1. registry を status=analyzed で upsert（stages_completed=S0-S2）。
2. `python3 scripts/registry_helper.py audit-provenance --scan-fs papers/ablation_provenance/{paper_id} --strict`
3. `python3 scripts/claudemd_contamination_audit.py --sweep`
4. **自動 /record は発火しない**（本 run は統制実験であり通常解析ではない。insight の記録は
   全 36 run 完了後の採点 session で一括）。

## 実行順の推奨

腕・論文をインターリーブ（P と W を交互、論文もローテーション）し、日内の環境ドリフトが
片腕に偏らないようにする。36 run の順序は自由だが、同一論文の連続実行は避ける。
