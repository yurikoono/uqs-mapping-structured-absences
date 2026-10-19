---
title: changelog v184
created: 2026-05-28
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# Changelog: v18.3 → v18.4

**作成日:** 2026-05-02
**作成モデル:** Opus 4.7（1M context）
**性格:** **実行モデル整合性パッチ**。UQS プロンプトは Opus 4.6 で最適化されたが
実行は Sonnet 4.6（コスト要因）であるため、Anthropic 公式の "Prompting best
practices for Claude's latest models"（platform.claude.com、2026 年版）に
照らした Sonnet 4.6 整合性チェックの結果を反映。Stage 2 D-4 セクションのみ
substantive 改訂（C17, C18, C19 + 5 件の tone 修正）、Stage 0/1 は版番号のみ更新。

---

## 📌 Status (2026-05-02 確定)

v18.4 は v18.3 確定（2026-04-27）後、Anthropic 公式 prompt engineering best
practices と UQS 実装の突合せ評価を経て策定された **実行モデル整合性パッチ**。

v18.3 までの改訂は分析的内容（anchoring rule / D-4 候補生成基盤）に集中していた。
v18.4 は **prompt-side compatibility tuning for Sonnet 4.6 cost-aware
deployment** を性格とし、内容的な分析能力には影響しない。

**実装ステータス：** 確定（2026-05-02）。n=2 検証（dev/kumada Entry 056 +
dev/murai Entry 057）で 4 シグナルすべて確認、OI-055 が解消、新規退行は
低 severity のみ。**v18.4 を Phase 2 advisor pilot の公式版に昇格** し、
CLAUDE.md の現行版表記を v18.3 → v18.4 に更新済み。

実装ファイル：
- `prompts/v184/prompt_stage0_v184.md`（版番号のみ更新）
- `prompts/v184/prompt_stage1_turn1-4_v184.md`（版番号のみ更新）
- `prompts/v184/prompt_stage2_v184.md`（C17, C18, C19 + tone 修正、73 行追加）
- `prompts/v184/prompt_stage2_v184_en.md`（C17, C18, C19 + tone 修正、88 行追加、
  2026-05-02 に JP 並行更新完了）

---

## 動機：Sonnet 4.6 と Opus 4.6 の prompt-side mismatch

### 出発点となった観察

Anthropic 公式 best practices（2026 年版）には Sonnet 4.6 / Opus 4.6 / Opus 4.7 の
**モデル別固有の挙動**が文書化されている。UQS が実行モデルとして使用する
Sonnet 4.6 について、以下が UQS プロンプトとの mismatch 候補として浮上した：

1. **Verbosity の自動 calibration**：「Less verbose: may skip detailed summaries
   for efficiency unless prompted otherwise」— Sonnet 4.6 は出力を圧縮的に
   調整する傾向が Opus 4.6 より強い。
2. **強調語への過敏**：「more responsive to system prompt」— 4.5/4.6/4.7 系は
   "CRITICAL: You MUST" 型の強調で overtrigger（保守化）する。公式は
   「dial back any aggressive language」を推奨。
3. **Multi-step reasoning 負荷**：Sonnet 4.6 は推論能力が Opus より低いため、
   多段ルールの並列適用で取りこぼしが起きやすい。Adaptive thinking が
   無効な場合は内部 reasoning が浅くなる failure mode が想定される。
4. **Long-context retrieval 精度**：Stage 2 は PDF + S0 + S1 4ターン（50k〜100k
   トークン規模）の入力を持ち、Sonnet では Opus より retrieval が脆弱。

### UQS 実装との突合せ結果

D-4 セクションが最も影響を受ける分析単位として特定された：
- anchoring 8 ルール / cross_field_temperature 利用 / same_root_groups 活用 /
  候補数上限（v18.1 改訂）/ フォールバック規則 / C9〜C16 / 追加チェック
  (a)(b)(c) — 単一パスで並列適用される制約数が突出して多い。
- 候補本文の長さ・深さ指定が「確定させる必要はありません」程度で、Sonnet が
  圧縮的に出した場合の歯止めが効かない。
- 「**禁止**」「**必ず**」「**Do not**」が出力形式（パース対象の機械的構造）と
  分析的判断（候補展開の徹底）の両方に混在している。

### 過去の失敗モードとの整合

OI-028（v18 nakanishi2025 の U-4/U-5 消失パターン）は v18.1 C11 で
「多重 critical/high U項目の独立記録保護」として補修されたが、その背景は
「Stage 1 で記録された critical U項目が D-4 候補生成段階で既存候補に
吸収されて消える」だった。これは Sonnet 4.6 の multi-step reasoning 負荷
と verbosity 圧縮が複合した failure mode と整合的に解釈できる。
v18.4 の C17 / C19 はこのクラスの取りこぼしを構造的に予防する。

---

## 変更一覧

### C17: D-4 生成前の整理ステップ（CoT scaffolding）追加 — 必須

**対象ファイル:** `prompts/v184/prompt_stage2_v184.md`
**コメントタグ:** `<!-- v18.4 C17: D-4 generation preparation step (CoT scaffolding) -->`
**挿入位置:** D-4 セクション冒頭（cross_field_temperature 活用節の直前）

**追加内容（要点）:**
候補生成に入る前に `<thinking>` タグ内で以下を順に確認させる：
1. high_convergence_high_gap 項目の列挙（空ならフォールバック規則特定）
2. METAのsame_root_groups の列挙
3. critical/high U項目の id 列挙
4. 候補数上限（デフォルト8 / 拡張10）の確定 + 拡張根拠

**Why:** Sonnet 4.6 は adaptive thinking が無効な場合に内部 reasoning が浅く
なる failure mode が想定される。明示的な準備ステップにより TEMPERATURE_SUMMARY
と U項目の体系的活用を保証する。ベストプラクティス "Manual CoT as a fallback ...
Use structured tags like `<thinking>` and `<answer>`" を直接適用。

### C18: D-4 候補本文の構造仕様（4要素）追加 — 必須

**対象ファイル:** `prompts/v184/prompt_stage2_v184.md`
**コメントタグ:** `<!-- v18.4 C18: D-4 candidate body structure specification -->`
**挿入位置:** 「独立項目として記載する対象」節の直前

**追加内容（要点）:**
各候補本文に以下4要素を順に含めることを陽に規定：
1. 問いの記述（その候補が何を尋ねているか）
2. 論文の処理様態（沈黙 / 言及のみ / 今後の課題への外置き / 否認的処理 / 結論への利用 等）
3. 答えられた場合の帰結（または欠落の含意）
4. Stage 1 観察との関係（grounded_in 項目との関係）

合計 6〜12 文程度の analytical depth を要求。

**Why:** Sonnet 4.6 の "less verbose" 傾向に対する直接的なカウンター。
候補本文が「key_quote + 一文要約のみ」に縮約する failure mode を予防し、
上限8〜10候補が "topic 列挙" に退化するのを防ぐ。

### C19: D-4 出力確定前のセルフチェックリスト追加 — 必須

**対象ファイル:** `prompts/v184/prompt_stage2_v184.md`
**コメントタグ:** `<!-- v18.4 C19: D-4 pre-output self-check list -->`
**挿入位置:** D-4 セクション末尾（priority_structure 記述の直後、--- delimiter の直前）

**追加内容（要点）:**
9 項目のチェックリストを `<thinking>` タグ内で順に確認させる：
- 候補数上限の遵守と拡張根拠の明記
- 4 メタフィールドの行単位独立性
- grounded_in の id 種別（A/B/C/U のみ、ターンレベル ID 不在）
- key_quote の出典（メインテキスト、SI/ESI 排除）
- multi-critical U項目の独立記録
- 重複候補の統合
- 「問い得ない問い」の分離
- pivot 項目の形式
- 候補本文の C18 構造遵守

**Why:** 多段ルール（C17準備 / anchoring 8 / temperature / SRG / 上限 /
フォールバック / C9〜C16 / 追加チェック / C18 構造）の並列適用負荷を
出力直前のチェックリスト適用で軽減し、特定ルールの取りこぼしを構造的に
予防する。ベストプラクティス "Ask Claude to self-check ... Before you
finish, verify your answer against [test criteria]" を直接適用。

### Tone 修正（5 件）— 必須

**対象ファイル:** `prompts/v184/prompt_stage2_v184.md`
**コメントタグ:** なし（散発的な置換のため）

| 旧（v18.3）| 新（v18.4）| 場所 | 種別 |
|---|---|---|---|
| **テキスト根拠の要件：** 各候補には**必ず**以下を付記してください | 各候補には以下4フィールドを付記する | テキスト根拠の要件節 | 出力形式の正当化追加 |
| V1-Qx, V2-Qx等のターンレベルIDは使用**禁止** | V1-Qx, V2-Qx 等のターンレベルIDは使用しない（中間ラベル...） | grounded_in 仕様 | Why 補足 |
| **出力形式の厳守：** 4フィールドは**必ず**改行で区切ること...**禁止** | **出力形式（行単位の独立性）：** 各々独立した行に記載する。downstream のパース処理が... | 出力形式節 | positive + Why |
| **必ず独立した項目として記載すること：** | **独立項目として記載する対象：** | 問い得ない問い節 | 命令語除去 |
| **悪い例（生成禁止）：** | **悪い例（避けるべきパターン）：** | propositional 制約 | 命令語除去 |

**全体効果:** 「禁止 / 必ず」の出現が 11 → 5 に削減。残存 5 件はすべて
「分析的判断の徹底」を求める文脈（C14 規則・追加チェック項目）であり、
出力形式の機械的制約ではない。

**Why:** ベストプラクティス引用：「dial back any aggressive language. Where
you might have said 'CRITICAL: You MUST use this tool when...', you can use
more normal prompting like 'Use this tool when...'」。Sonnet 4.6 は強調語に
overtrigger し、保守的な出力（候補数の縮小、analytical depth の圧縮）に
傾く可能性がある。出力形式の機械的制約は positive + Why に転換し、分析的
判断の徹底を求める emphasis のみ残した。

---

## v18.3 との互換性

### 出力スキーマ

C17 / C19 のチェックは `<thinking>` タグ内に閉じ、出力本文には現れない。
C18 は候補本文の構造仕様であり、`Output format` セクションのフィールド構成は
変更なし。**既存の downstream パース処理（regression 比較スクリプト等）は
v18.3 と v18.4 の出力で同じパーサが動作する**。

### 命名規則

新規ファイルは `{論文ID}_v184_sonnet_s2.md` のように `v184` を含む。
v18.3 出力との比較は版番号で識別可能（例: `kumada_v183_sonnet_s2.md` vs
`kumada_v184_sonnet_s2.md`）。

### Stage 3 / Stage 4 / Stage 2F

v18.4 では変更なし。これらは独立版管理であり、`prompts/stage2f3/` 配下の
最新版（Stage 3 v4 / Stage 4 v4 / Stage 2F v7.1）をそのまま参照する。

---

## 検証プロトコル（推奨）

### Step 1: dev/kumada または dev/murai の n=1 比較

```
dev/kumada または dev/murai を v18.4 で再解析（Sonnet 4.6）
→ 既存 v18.3 出力との比較（バージョン比較プロトコル適用）
→ regression_log.md に新エントリ追記
```

### Step 2: 期待されるシグナル

C17 / C18 / C19 が機能していれば、以下のいずれか（理想は複数）が観測される：

1. **D-4 候補本文の analytical depth 増加**：v18.3 で「key_quote + 1-2文」だった
   候補が、v18.4 で 4 要素を含む 6〜12 文に展開される（C18 効果）
2. **候補数の上限到達への接近**：v18.3 で 6-7 候補で終わっていた解析が、
   v18.4 で上限 8 に到達する（C17 + C19 効果）
3. **multi-critical U項目の独立化安定**：critical/high U項目が複数ある場合に、
   それぞれが独立候補として展開される率の向上（C19 効果）
4. **TEMPERATURE_SUMMARY 利用の体系性向上**：high_convergence_high_gap 項目が
   D-4 候補に明示的に紐付けられる比率の向上（C17 効果）

### Step 3: シグナル不在時の対応

n=1 で明確なシグナルが出ない場合：
- 別の論文（papers/test/ 配下）で n=2 検証
- それでもシグナル不在なら、v18.3 がすでに sufficient であった可能性を
  記録し、v18.4 を draft 状態のまま保留（v18.3 を継続使用）

### Step 4: シグナル確認後の措置

シグナル確認後：
- v18.4 を Phase 2 advisor pilot の公式版に昇格
- `prompts/v184/prompt_stage2_v184_en.md` を並行更新（同様の修正を英語版に適用）
- CLAUDE.md の「v18.3 が現行版」記述を v18.4 に更新

---

## 未実装項目（v18.5 以降の候補）

### Quote-first scaffolding（W5、優先度 P3）

ベストプラクティス "Ground responses in quotes ... ask Claude to quote
relevant parts of the documents first before carrying out its task" を
D-4 に適用すると、現状の構造を以下に再編する案：

```
1. <relevant_passages> Stage 1 観察に対応する論文の引用を先に抽出
2. <D4_candidates> 抽出した引用から候補を導出
```

これは long-context retrieval 弱点への直接対応だが、D-4 セクションの
構造的再編が必要なため v18.4 では見送り。v18.5 で運用データに基づき
判断する。

### Stage 2F / Stage 3 / Stage 4 への同種パッチ適用

v18.4 は Stage 2 のみが対象。Stage 2F は Opus 4.7 で実行されるため
別の最適化軸（前回評価ノート参照）。Stage 3 / Stage 4 は Sonnet 実行
だが、本パッチで指摘された failure mode の D-4 ほどの集中は確認されて
いない。runtime 観測で必要性が確認された段階で対応する。

### 英語版 (prompt_stage2_v184_en.md) への mirror — 完了（2026-05-02）

JP 版での n=2 検証（Entry 056 / 057）完了を受けて並行適用。C17/C18/C19 の
3 改変と tone 修正 5 件を英語に直訳ではなく構造的に対応する形で適用。
v18.3 EN → v18.4 EN: 518 行 → 606 行（+88 行、JP の +73 行に対応）。

---

## 参考資料

- Anthropic Prompting best practices（2026 年版）：
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- v18.3 changelog: `improvements/_prompts/changelog_v183.md`
- 過去の D-4 取りこぼし事例: OI-028（nakanishi2025 U-4/U-5 消失）、
  v18.1 C11 で構造的補修済み
- 関連する failure mode 観察:
  `improvements/cross_model_kumada_vs_murai_meta.md`（n=2 メタ観察）
