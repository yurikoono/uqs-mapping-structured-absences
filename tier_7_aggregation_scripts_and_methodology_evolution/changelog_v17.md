---
title: changelog v17
created: 2026-05-28
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# Changelog: v16.1 → v17

**作成日:** 2026-04-15
**作成モデル:** Opus
**性格:** 構造的再設計なし。全変更が追記・例外追加。v16.1の基本設計を完全保持。

---

## 📌 Status (2026-04-21)

v17 は Digital Discovery 投稿のための **提出確定版** である（`docs/version_history.md` 参照）。Kumada 1972 の EP 辞書に関する **dictionary-level の更新**（EP-10a 追加、2026-04-19）は v17 prompt を変更せずに行われた。次のプロンプト改訂（v18）は `future_work/deferred_items_registry.md §1.8` に登録されている。本 changelog は v17 確定時点の記録として凍結されている。

---

## 変更一覧

### C1: スコープ失敗例の著者帰属理由検証（Turn 1, OI-009）— 必須

**対象ファイル:** prompt_stage1_turn1_v17.md
**挿入位置:** Turn 1 Instructions セクション末尾（"Focus on:" リスト後）
**コメントタグ:** `<!-- v17 C1: OI-009 -->`

**変更内容:**
スコープ表（Scheme等）における0%収率・0% ee・失敗例基質について、著者が提示する
失敗理由（電子的、立体的、コンフォメーション的等）と、その説明を支持/反論する
実験的・計算的証拠の有無を検証する指示を追加。証拠なしの帰属はB項目候補として
記録するよう指示。

**根拠:** app2で3/3収束 HIGH_gap項目（N-Ph基質の電子的帰属）がv16.1で完全消失。
Turn 1-3でスコープ失敗例の説明根拠を問う指示がなかったことが根本原因。

---

### C2: DFT checklist後の触媒サイクル機構論的評価の分離維持（Turn 2, OI-010）— 必須

**対象ファイル:** prompt_stage1_turn2_v17.md
**挿入位置:** DFT reporting checklist の直後
**コメントタグ:** `<!-- v17 C2: OI-010 -->`

**変更内容:**
DFT checklistの適用が計算方法論の評価に限定されることを明示し、論文が提案する
触媒サイクルや反応機構に対する実験的検証（速度論、同位体効果、中間体捕捉等）の
評価を独立して実施する指示を追加。DFT方法論チェックと触媒サイクル機構論評価が
相互排他的に扱われないよう明示。

**根拠:** app1でV2がDFT方法論に集中し、触媒サイクルの機構論的B項目群が消失。

---

### C3: D-4候補選択への3項目追加（Turn 4→Stage 2 D-4, OI-007+008）— 必須

**対象ファイル:** prompt_stage2_v17.md
**挿入位置:** D-4セクション「出発点となる視点」リスト後
**コメントタグ:** `<!-- v17 C3: OI-007+008 -->`

**変更内容:**
D-4候補選択時の追加チェック項目として以下の3項目を追加：
- (a) 否定的証拠の検出下限：「not detected」等の否定的証拠を機構的主張の根拠と
  して使用する場合の検出下限情報の有無チェック
- (b) 実用条件外挿：触媒量・基質濃度・反応温度が実用条件と大きく異なる場合の
  外挿可能性チェック
- (c) matched-pair control：対照実験として提示される実験ペアで基質・試薬・条件が
  異なる場合（非対称性）のチェック

**根拠:**
- (a)(b) comp2で否定的証拠の検出下限問題・触媒負荷量の外挿可能性がD-4候補化されず
- (c) comp1で対照実験の設計上の非対称性がD-4候補化されず

---

### C4: C項目定義への「Dropped Quantitative Benchmark」追加（Turn 1 + Turn 4, OI-013）— 必須

**対象ファイル:** prompt_stage1_turn1_v17.md, prompt_stage1_turn4_v17.md
**挿入位置:**
- Turn 1: Instructions セクション末尾（C1の後）
- Turn 4: C項目定義（Exhaustive extraction rule後）
**コメントタグ:** `<!-- v17 C4: OI-013 -->`

**変更内容:**
- Turn 1: 導入部・関連研究で数値付きで引用された先行研究が結果・考察部で同じ
  数値軸での直接比較なしに終わるパターンの検出指示を追加
- Turn 4: C項目のサブタイプとして「Dropped Quantitative Benchmark」を明示的に
  定義し、reason_severed記載方法を規定

**根拠:** scr1でv15がΔS‡数値引用の未展開を捕捉できず。v16.1は既にC-1, C-2として
正確処理済みだが、プロンプトへの明示化により将来の安定的再現を保証。

---

### C5: ESI委任 vs 実験不在の区別明示（Turn 1, OI-012）— 必須

**対象ファイル:** prompt_stage1_turn1_v17.md
**挿入位置:** Instructions セクション末尾（C4の後）
**コメントタグ:** `<!-- v17 C5: OI-012 -->`

**変更内容:**
ESI/SI参照が付属する場合に実験は実施済みとして扱い、partial disclosure（ESI内
データ非開示）と実験不在を明確に区別する指示を追加。partial-negation修飾語への
注意も含む。

**根拠:** scr2でv15がESI参照データを「実験不在」として誤分類。v16.1はA-5
（deferral_to_ESI）として正確処理済みだが、明示化により将来の安定的再現を保証。

---

### C6: 逐次プロトコルの混交可能性チェック（Turn 1, OI-011）— 推奨

**対象ファイル:** prompt_stage1_turn1_v17.md
**挿入位置:** Instructions セクション末尾（C5の後）
**コメントタグ:** `<!-- v17 C6: OI-011 -->`

**変更内容:**
同一ラン内で条件を段階的に変化させる逐次プロトコルにおいて、先行フェーズが
後続フェーズに及ぼす影響（触媒状態変化、中間体蓄積、表面修飾）のチェック指示を
追加。flow reactor実験および多段one-pot反応に特に関連。

**根拠:** het2でv16.1がB-9として検出済みだが、検出理由がプロンプトに明示されて
おらず将来の安定的検出が保証されていなかった。

---

### C7: B項目consolidation ruleへの収率基準混在例外（Turn 4, OI-004）— 推奨

**対象ファイル:** prompt_stage1_turn4_v17.md
**挿入位置:** B-item consolidation rule 直後
**コメントタグ:** `<!-- v17 C7: OI-004 -->`

**変更内容:**
論文内で異なる収率計算基準（出発物質基準 vs 生成物基準、単一収率 vs 両原料ベース
収率、isolated yield vs GC yieldの不整合な混用）が使われており内部矛盾を構成する
場合は、consolidationせず独立B項目として保持する例外条件を追加。

**根拠:** Muraiでbilateral yield矛盾（B-8）がGC信頼性D-4候補に吸収された。

---

### C8: PDF直接読み込みの明示（全プロンプト）— 必須

**対象ファイル:** 全6ファイル
**挿入位置:** 各ファイル冒頭（version行の直後またはProcedure overview前）
**コメントタグ:** `<!-- v17 C8: PDF direct reading -->`

**変更内容:**
「論文PDFはReadツールで直接読み込むこと（マルチモーダル読み込み）」の指示を
全プロンプトに追加。20ページ以下は全体を1回で読み、超過時はページ範囲で分割。
pdftotext等のテキスト抽出ツール不使用を明記。figure・scheme・構造式・エネルギー
図等の視覚情報が利用可能であることを明示。

**根拠:** session_handover_v16.1.mdで決定済みの方針。v17移行時に統一。

---

## 変更マッピング（ファイル別）

| ファイル | 適用された変更 |
|---------|-------------|
| prompt_stage0_v17.md | C8 |
| prompt_stage1_turn1_v17.md | C1, C4, C5, C6, C8 |
| prompt_stage1_turn2_v17.md | C2, C8 |
| prompt_stage1_turn3_v17.md | C8 |
| prompt_stage1_turn4_v17.md | C4(C定義), C7, C8 |
| prompt_stage2_v17.md | C3, C8 |

## v16.1からの不変部分

以下のv16.1基本設計要素は全てv17で保持：
- rhetorical_function制約
- ピボット構造探索
- SRG（Same Root Groups）
- scope anchor rule
- self-contradictory absence rule
- exhaustive extraction rule
- suppressed classification checklist
- DFT reporting checklist（C2は追記のみ）
- B-item consolidation rule（C7は例外追加のみ）
- cross_field_temperature / TEMPERATURE_SUMMARY
- フォールバック規則
- Anchoring discipline（T1/T2/T3）
- Multi-paper PDF boundary rule

## 次のアクション

v17の検証計画（devsetでの退行チェック）：
1. dev/kumada を v17 で解析し、v16.1と比較（C1, C7の効果確認）
2. dev/murai を v17 で解析し、v16.1と比較（C4, C7の効果確認）
3. 退行が見られない場合、testsetの優先論文（app2, comp2, comp1）で検証
