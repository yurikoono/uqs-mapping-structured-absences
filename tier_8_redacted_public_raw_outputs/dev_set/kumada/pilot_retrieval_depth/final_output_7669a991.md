以下を Codex セッションにそのまま投入してください。Claude Code の「`dev/kumadaをv18.4で解析`」短縮記法を Codex 用にフル展開したものです。

---

## Codex 投入プロンプト（kumada × v18.4 × GPT-5.5 Thinking）

````
あなたは UQS (Unasked Question Structuring) プロトコル v18.4 を Kumada 1972 論文に
適用するアナリストです。Claude Code 環境で確立された手順を GPT-5.5 Thinking で
再現し、ファイル出力までを完結させてください。

## 作業ディレクトリ

<project-root>/

以下、全パスはこのリポジトリルートからの相対パスで示します。

## 入力ファイル

- 論文 PDF:    papers/dev/kumada/Kumada_1972.pdf
  （PDF を直接読めない場合のフォールバック: papers/dev/kumada/Kumada_1972.txt）
- v18.4 プロンプト:
  - prompts/v184/prompt_stage0_v184.md
  - prompts/v184/prompt_stage1_turn1_v184.md
  - prompts/v184/prompt_stage1_turn2_v184.md
  - prompts/v184/prompt_stage1_turn3_v184.md
  - prompts/v184/prompt_stage1_turn4_v184.md
  - prompts/v184/prompt_stage2_v184.md

## 出力ファイル（papers/dev/kumada/ 配下、UTF-8）

| Step | ファイル名 |
|------|-----------|
| S0 | kumada_v184_gpt55thinking_s0.md |
| S1 Turn 1 | kumada_v184_gpt55thinking_s1_turn1.md |
| S1 Turn 2 | kumada_v184_gpt55thinking_s1_turn2.md |
| S1 Turn 3 | kumada_v184_gpt55thinking_s1_turn3.md |
| S1 Turn 4 (synthesis) | kumada_v184_gpt55thinking_s1.md |
| S2 | kumada_v184_gpt55thinking_s2.md |

既存の `kumada_v184_sonnet_s*.md` は **絶対に上書きしない**。
GPT-5.5 用は `_gpt55thinking_` サフィックスで別ファイル化します。

## 実行原則（厳守）

1. **単一セッションで逐次実行**。Stage 2 の品質は Turn 1–3 の引用と推論の
   フルコンテキストに依存するため、セッション分割は禁止。
2. 各ステップで読み込むもの:
   - Step S0: PDF + prompt_stage0_v184.md
   - Step S1T1: PDF + S0 出力(コンテキスト保持) + prompt_stage1_turn1_v184.md
   - Step S1T2: 上記 + Turn1 出力 + prompt_stage1_turn2_v184.md
   - Step S1T3: 上記 + Turn2 出力 + prompt_stage1_turn3_v184.md
   - Step S1T4: 上記 + Turn3 出力 + prompt_stage1_turn4_v184.md
                → 出力は `_s1.md`（Turn 4 = 統合版）
   - Step S2:   上記すべて + prompt_stage2_v184.md
3. **プロンプト本文の解釈は Sonnet 実行と同じく日本語/英語混在のまま**。
   v18.4 プロンプトで指定された出力言語規定（D-4/E 節以降は日本語、それ以前は
   プロンプトの指示通り）に厳密に従う。GPT-5.5 が独自に言語を切り替えない。
4. 各ステップ完了後、対応ファイルを保存し、保存パスを 1 行で報告してから
   次のステップに進む。
5. PDF は可能ならマルチモーダルで直接読む（figure/scheme/table を含めるため）。
   テキスト抽出に頼らないこと。直接読みが不可な場合のみ `.txt` を補助に使い、
   その旨を S0 出力の冒頭メタ行に明記する。
6. プロンプト v18.4 で要求される出力フォーマット（A/B/C/U 分類、SRG、
   D-4 候補、E 節 T1/T2/T3 アンカー、scope_type 等）の構造を欠落させない。
   GPT-5.5 が「説明的散文」で置換するのは v18.4 の output-discipline 違反。

## 完了報告

全 6 ファイルを書き出した後、以下を 1 ブロックで返してください:

- 各出力ファイルの絶対パスとバイト数
- D-4 候補の通し番号一覧（タイトルのみ、本文は不要）
- v18.4 プロンプトで要求される構造要素のうち、欠落させた・縮約した
  項目があれば明示（無ければ「欠落なし」と記載）

## 比較メモ（任意、最後に）

`papers/dev/kumada/kumada_v184_sonnet_s2.md` が同フォルダに存在します。
これは Claude Sonnet 4.6 による v18.4 ベースラインです。今回の GPT-5.5
出力との 1 行比較（D-4 個数、SRG 個数、E 節項目数のみ）を完了報告の末尾に
付記してください。**詳細比較やスコアカード作成は行わない**（別タスク）。

それでは Step S0 から開始してください。
````

---

ポイント:
- 命名規則は CLAUDE.md の `_gpt55thinking_` 形式（gpt54thinking 先例に倣う）。`v184` で固定。
- 既存 `kumada_v184_sonnet_*` を温存して別ファイル化。
- PDF 直読み優先（v18.4 の Stage 0 は scheme/構造式参照を要求）。
- セッション分割禁止を明示（Codex はステップごとに context を切りがち）。
- 1 行比較のみ末尾に付け、詳細比較は別途 `dev/kumadaのsonnet, gpt55thinkingを比較` 等で Claude Code 側に戻す前提。