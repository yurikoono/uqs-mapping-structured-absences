---
title: regression log
created: 2026-05-28
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# UQS Regression Log
<!-- バージョン比較のたびに追記する。各エントリは比較対象・評価論文・スコアカードを含む。 -->

> **R1 version (2026-10-16).** Entries 025, 051 and 058–066 are not in this copy. They concern other manuscripts (Entries 025 and 051 an unpublished manuscript draft by other authors; Entries 058–066 the later v19 prompt and another paper of the project) and are not used by Paper A. Entry numbers are not re-numbered.

---

## Entry 001: v15 vs v16 vs v16.1 — Kumada (devset)

**比較日:** 2026-04-14
**評価論文:** Kumada (Tamao, Sumitani, Kumada, JACS 1972) — devset
**モデル:** claude-sonnet-4-6
**評価者:** Opus セッション

### 背景

v16はv15からの構造的改善（rhetorical_function、ピボット構造、reporting_omission、
DFTチェックリスト等）を導入したが、devset Kumada論文での比較で5つの退行が検出された。
v16.1はv16に対して修復1（self-contradictory absence rule）と修復2（C項目exhaustive
extraction rule）を追加した修正版。

### スコアカード

| ID | 退行ポイント | v15 | v16 | v16.1 | 判定 |
|----|---|---|---|---|---|
| R1 | U項目（自己矛盾的不在）の生成 | U-1〜U-5 (5項目) | 0項目（B-14に吸収） | U-1〜U-4 (4項目) | ✅ 回復 |
| R2 | C項目の分析密度 | C-1〜C-4 (4項目) | C-1のみ (1項目) | C-1〜C-3 (3項目) | ✅ 回復 |
| R3 | D4-3（触媒同一性問題）のD-4候補化 | 独立候補 | 対応なし | D-4候補1(c)に統合 | ✅ 回復 |
| R4 | D4-7（β-水素消去の競合）のD-4候補化 | 独立候補 | 対応なし | 未回復 | ⚠️ 部分回復 |
| R5 | E節の射程の広さ | メタ科学的抽象化 | 化学的に限定 | 化学的、やや一般化 | 🔄 変化 |

### 総合判定

**v16.1 > v15 > v16**

- v16.1はv15の分析的捕捉力（U項目、C項目密度、D-4候補の幅）を回復した上で、
  v16の構造的改善を保持。
- R4（β-水素消去）はself-contradictory absence ruleの射程外。→ open_issues OI-001
- R5（E節）はv16.1がT2範囲内に収まり、anchoring disciplineとの整合性はv16.1が優位。
  v15のメタ科学的抽象化はT3に近く再現性に疑問。

### v16.1で確認された正の副次効果

- B ↔ U の二重記帳（B-4 ↔ U-2、B-8 ↔ U-3）がlinked_itemsに明示化
- D-4候補1がSRG-1全体を統合した大型候補として構造化（v15の分散候補3つ分に相当）
- C-2（dipy-Ni analogy）が C-2 ↔ U-2 のlinked_itemsでD-4に直接接続

### v16.1で確認された未回復項目

- v15 U-2（1,1-ジクロロエチレン二重置換）— medium severity、単一エージェント。影響小
- v15 U-5 / D4-7（β-水素消去）— → open_issues OI-001

---

## Entry 002: v15 vs v16.1 — Murai (devset)

**比較日:** 2026-04-15
**評価論文:** Murai (Murai, Kakiuchi, Sekine, Tanaka, Chatani, Nature 1993) — devset
**モデル:** claude-sonnet-4-6
**評価者:** Opus セッション（HET-1節目 Step 1）

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 3 | 2 |
| B | 8 | 14 |
| C | 3 | 8 |
| U | 1 | 2 |
| 合計 | 15 | 26 |

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | B-8 bilateral yield claim（両原料ベース収率の矛盾） | 独立B項目として詳細分析 | D-4 cand.7に吸収、specific contradictionが拡散 | ⚠️ medium impact |
| R2 | B-6 steric説明のcircular argument批判 | 独立B項目 | 対応項目なし。D-4 cand.3で間接的にのみ | ⚠️ low-medium |
| R3 | D4-4 触媒消費・回収・再利用 | 独立D-4候補 | 消失 | ⚠️ low |
| R4 | U-1 run 5の触媒量3倍異常 | 独立U項目 | 言及なし | ⚠️ low |
| R5 | D4-2 bilateral yieldの内部矛盾 | grounded_in B-1,B-2,B-8で完全展開 | cand.7がGC信頼性に焦点移行、bilateral矛盾は鈍化 | ⚠️ medium |

### 総合判定

**v16.1 > v15**

v16.1は項目数が大幅に増加（15→26）し、特に以下が顕著な改善:
- U-1（Ru(CO)₂自己矛盾）: self-contradictory absence ruleが正確に作動。v15ではB-5の注記に埋没していた
- U-2（hydride mass balance）: 完全に新規。触媒サイクルの化学量論的矛盾を捕捉
- C項目密度（3→8）: exhaustive extraction ruleが作動
- D-4にピボット構造（A-1↔B-10, A-1↔B-12, A-2↔B-7）が明示化

退行5件はいずれもlow〜medium impact。R1/R5の「bilateral yield矛盾」の拡散が最も惜しい
点だが、v16.1のU-1/U-2が提供する分析的深度がそれを上回る。

### v16.1で確認された正の副次効果

- self-contradictory absence ruleがKumadaに続きMuraiでも有効に作動（U-1, U-2）
- exhaustive extraction ruleによりC-4〜C-8が網羅的に抽出
- SRGの再編成で機構的問題と分析的問題の分離が改善

### 確認された未回復項目・新規懸案

- R1/R5: bilateral yield矛盾の拡散 → open_issues OI-004
- R4: run 5の触媒量3倍異常が消失 → open_issues OI-005

---

## Entry 003: v15 vs v16.1 — hom1 (test, 凍結評価)

**比較日:** 2026-04-15（v15解析完了により更新）
**評価論文:** hom1 (Wang et al., Chem. Sci. 2020, 11, 11042–11054)
**モデル:** claude-sonnet-4-6

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 1 | 3 (A-1, A-2, A-3) |
| B | 12 | 10 |
| C | 2 | 6 |
| U | 10 | 3 |
| SRG | 5 | 5 |
| D-4候補 | 8 | 8 |
| 合計(A+B+C+U) | 25 | 22 |

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | A-3（挿入ステップ役割の先送り）の捕捉 | U-4（速度論的対熱力学的制御）として分類、明示的A項目なし | A-3として明示的先送り分類（"further studies"の引用）| ⚠️ medium |
| R2 | ノルボルネン代理妥当性のD-4候補化 | U-3にとどまり、D-4に昇格せず | D-4候補3として独立展開 | ⚠️ medium |
| R3 | C2-生成物3bのC3位重水素化の独立候補化 | A-1との連動でU-4に包含 | D-4候補6として独立展開（"significant deuterium incorporation … C3-position of product 3b"） | ⚠️ low |
| R4 | 触媒回転数・寿命の問い | 対応なし | D-4候補8として展開 | ⚠️ low |
| R5 | high_convergence_high_gap の検出 | 空（フォールバック適用） | B-3 (V1=medium, V3=critical; gap=medium) が最優先候補 | ⚠️ medium |
| R6 | E節 scope_type 判定 | framework_question（設計原理への問い） | tool_question（より論文の実際の問いに近い） | ⚠️ low |

### 総合判定

**v15 < v16.1**

v16.1の優位点:
- A-3として挿入ステップ役割の先送りを明示捕捉（R1）
- high_convergence_high_gap の検出によりフォールバック不要（R5）
- D-4候補3（ノルボルネン代理妥当性）・候補6（C3位重水素化）・候補8（触媒寿命）が固有

退行6件はいずれもlow〜medium impact。v15のU項目数（10個）はv16.1より多いが、
v16.1の方が重要項目（D-4候補）への変換精度が高い。

### v15固有の正の寄与

- C項目の明示的構造化（C-1: refs 9a,9b 未継続引用分析; C-2: ref 25 類比引用分析）が
  v16.1のS2では明示されていない
- D-4-C7（合成標的との接続の不在）: v16.1候補に対応なし。「このツールが何に使われるか」
  という問いが固有に展開されている
- D-4-C6（N-Tsインドール異常）: v16.1では候補4の中で言及のみ。v15では独立候補として展開
- SRG-5（Cu(II)の機構的役割）が独立SRGとして明示化

### 確認された未回復項目

- R1（A-3 分類精度）、R2（ノルボルネン代理妥当性のD-4化）は v15プロンプトの
  A分類判定の保守性（"further studies" 型の先送りへの感度）に起因する可能性。
  → OI-006 resolved

---

## Entry 004: v15 vs v16.1 — hom2 (test, 凍結評価)

**比較日:** 2026-04-15（v15解析完了により更新）
**評価論文:** hom2 (Shirai et al., J. Org. Chem. 2024, 89, 2787–2793)
**モデル:** claude-sonnet-4-6

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 10 | 2 |
| B | 18 | 7 |
| C | 4 | 6 |
| U | 1 | 4 |
| SRG | 6 | 3 |
| D-4候補 | 8 | 6 |
| 合計(A+B+C+U) | 33 | 19 |

v15は各機構的問いを個別A項目（A1–A10）として列挙したため項目数が多い。
v16.1は同一の機構的問いをA-1一項目に統合したが、U-2〜U-4を別途独立化している。

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | 再現性の独立B項目 | B15（NMR精度）で部分カバーのみ | B-4（V1=medium, V3=high; convergence 2/3; gap=low）として独立 | ⚠️ medium |
| R2 | AQ除去問題の分類精度 | B12（intentional_narrowing）として分類 | A-2（suppressed、三要件明示）として精度高く分類 | ⚠️ high |
| R3 | U項目の質と数 | U1のみ（T3 Hammett外部推論） | U-2（同位体パターン整合性）、U-3（Pd(0)種同定 critical）、U-4（ラジカル経路）が独立 | ⚠️ high |
| R4 | SRG-3（AQ合成的実用性）の統合 | B12単独、製薬フレーミングC項目と未接続 | SRG-3 (A-2, B-6, C-3, C-4) として構造化・linked_items明示 | ⚠️ medium |
| R5 | D4-5「室温が不可欠であることの未証明」 | 対応なし | 独立D-4候補として展開 | ⚠️ medium |

### 総合判定

**v16.1 > v15**

v16.1の優位点:
- A-2（suppressed: AQ除去問題）が製薬フレームとの内的緊張を精確に捕捉
- U-3（Pd(0)活性種同定）のcritical評価がsingle-agentながら最重要構造的ギャップを指摘
- SRG-3がAQ指向基問題を凍結評価用凝集群として構造化
- D4-5（室温が不可欠である証明の不在）がv15に存在しない固有の洞察

### v15固有の正の寄与

- D4-7（Table 1 ASAP誤りの影響）: v15のみ独立D-4候補として展開。v16.1では
  questions_that_cannot_be_askedの文脈でのみ言及。
- D4-6（緩慢添加戦略の論理的根拠vs実際機構）: v15でより明示的に展開。
- E節scope_type: v15 = framework_question（より広い設計原理を問う形式）;
  v16.1 = tool_question（ヒドロシランの供給速度という具体的ツールに着目）。
  scope_typeの判定はv15の方が設問の抽象度に合致している可能性がある。

### 未回復項目

- R2（AQ suppressed分類）、R3（U項目独立化）、R4（SRG-3統合）、R5（D4-5）は
  v15プロンプトの構造的制約に起因する可能性が高い。
  → OI-006更新: hom2のv15ベースラインが作成されたため、OI-006はhom1のみに限定して更新。

---

## Entry 007: v15 vs v16.1 — app1 (test)

**比較日:** 2026-04-15
**評価論文:** app1 (Zhang, Tutkowski, DeLuca, Joyce, Wiest, Sigman — Chem. Sci. 2017, 8, 2277–2282)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

app1は非対称Pd触媒redox-relay Heck反応によるビシナル立体中心構築を報告するスコープ論文（EDGE ARTICLE, 6 pages）。DFT計算を含む合成論文。v15の_contaminated/ディレクトリに存在するS1/S2出力と比較。

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 1 | 1 |
| B | 23 | 17 |
| C | 4 | 8 |
| U | 0 | 4 |
| SRG | 5 | 3 |
| D-4候補 | 7 | 7 |

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | 触媒サイクルの機構論的問いの消失（SRG-1喪失） | SRG-1に6項目（B-4 V2=critical, B-16可逆性, B-17速度決定ステップ, B-18中間体無検出, B-5環開環, B-6E/Z異性化）。D4-1「触媒サイクルが類推的」として最強D-4候補 | SRG-3はU-1, U-2の2項目のみ。B-16〜B-18相当の独立B項目なし。DFT checklist集中によりV2の機構論的B項目カバレッジが低下 | ⚠️ medium |
| R2 | D4-3（立体化学帰属の空洞）の消失 | D4-3として「単一ECD → 25以上の生成物の立体化学帰属」を独立候補展開 | B-5（reporting_omission）として記録のみ。D-4候補化されず | ⚠️ medium |
| R3 | D4-4（エナンチオ選択性制御機構の物理的説明の不在）の消失 | D4-4としてNBO電荷相関（B-7）とC-H···O相互作用（B-15）を統合して独立展開 | B-3（mixed）とU-3（幾何的根拠）に分散。統合D-4候補なし | ⚠️ medium |
| R4 | B-10（アキラル配位子対照実験の不在）の消失 | B-10として V2=high, convergence 2/3で独立記録 | 対応なし | ⚠️ low |
| R5 | series_signal判定の相違 | series_signal: yes（「This information will be utilized...」をT1解釈） | series_signal: no | ⚠️ low |

### 総合判定

**v16.1 > v15**

v16.1の優位点:
- U項目（0→4）: self-contradictory absence ruleが初作動（v15にU項目ゼロ）。特にU-1（シクロプロピル「確認」の過剰主張）、U-2（er速度論/熱力学的制御の未検討）が価値高い
- C項目（4→8）: exhaustive extraction ruleが作動
- DFT checklistがB-12に系統的適用（dispersionとsolvationを一括記録）
- ピボット構造（A-1 ↔ B-11）がitem_id形式で明示化

退行5件はいずれもlow〜medium impact。R1が最大の損失だが、v16.1のU-2が部分的にカバー。

### v16.1で確認された正の副次効果

- U-1（シクロプロピル環開環の「確認」過剰主張）: self-contradictory absence ruleが作動。v15では対応なし
- U-2（erの速度論/熱力学的制御）: selectivity triggerが正確に機能。v15のB-23と類似だがU分類での明示はv16.1固有
- C-7（ref 11 NBO correlation引用）、C-8（ref 13 cyclopropyl引用）がexhaustive extractionで新規抽出

### 確認された未回復項目

- R1（触媒サイクル機構論的問い群の消失）: DFT checklist作動時のV2焦点変化に起因 → OI-010（新規）
- R2（D4-3立体化学帰属のD-4候補化）: B-5として記録されているが引き上げが起きていない

---

## Entry 005: v15 vs v16.1 — comp2 (test)

**比較日:** 2026-04-15
**評価論文:** comp2 (Palladino et al., ACS Catal. 2023, 13, 12048–12061)
**モデル:** claude-sonnet-4-6

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 1 | 3 |
| B | 6 (推定) | 18 |
| C | 4 | 5 |
| U | 1 | 5 |
| D-4候補 | 6 | 7 (+問い得ない問い) |

※v15はS2のみ参照（S1出力未確認のため項目数はS2記載内容から推定）

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | D4-4: 否定的証拠（M「非検出」、ホモダイマー「観察されず」）の検出下限不在 | 独立D-4候補として詳細展開 | B-2に吸収されD-4候補化なし | ⚠️ medium |
| R2 | D4-6: 20 mol%触媒負荷量と実用条件（1–5 mol%）の外挿可能性 | 独立D-4候補として展開 | 完全に不在 | ⚠️ medium |
| R3 | D4-5: 4-OMe基質観察（Table 4 entry 10）とDFT計算対象の具体的乖離 | 独立D-4候補として「少量塩基でもR錯体形成」という観察を核心に展開 | B-9/候補5に一般化され、4-OMe観察の具体性が弱化 | ⚠️ low |

### 総合判定

**v16.1 > v15**

v16.1の優位点:
- U-1, U-2（self-contradictory absence ruleが機能）: DFTバリア値（TEA 32.0 kcal/mol、TS0OTf 24.0 kcal/mol）と実験観測の不整合を明示化。v15 D4-2では「バリアの絶対精度」という一般論に留まっていた
- U-3: Ra/Rbエネルギー差がDFT誤差内という機構的自己矛盾——v16.1固有
- U-4: RDS内的矛盾（TS1Iを律速と断言しながら「OAとアルキン配位が類似バリア」と記述する矛盾）——v16.1固有
- B-3の統合: ECP、立体配座サンプリング、溶媒モデル、IRC検証、スピン状態の6パラメータを一括捕捉（V2 DFT checklist運用）
- A-2（BCl/TMG異常forgotten）、A-3（Buchwald配位子系mixed）——v16.1固有のA項目
- D-4候補6（Mårtensson条件境界）——C-2からの引き出しがv16.1固有

退行3件はいずれもmedium以下。機構論文においてDFT自己矛盾（U項目）の明示化はD-4候補への直接的貢献度が高く、v16.1の総合的分析価値はv15を上回る。

### v16.1で確認された正の副次効果

- self-contradictory absence ruleがcomp2（機構論文）でも有効に作動（U-1〜U-4）
- V2 DFT checklistが系統的に機能し、ECP・IRC・solvation modelの欠如を一括捕捉
- D-4ピボット構造（A-1↔B-3、A-1↔B-4）がDFT方法論の不透明性と将来課題の構造的依存関係を明示

### 確認された未回復項目

- R1（否定的証拠の検出下限）、R2（触媒負荷量の外挿可能性）→ open_issues OI-007

---

## Entry 006: v15 vs v16.1 — comp1 (test)

**比較日:** 2026-04-15
**評価論文:** comp1 (Race, Faulkner, Shaw, Bower — Chem. Sci. 2016, 7, 1508–1513)
**モデル:** claude-sonnet-4-6

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 1 | 2 |
| B | （不明、S2参照） | 20 |
| C | （不明） | 8 |
| U | （不明） | 5 |
| SRG | 不明 | 7 |
| D-4候補 | 7 | 8 |

※v15はS2のみ参照（S1出力未確認のため項目数はS2 D-4参照内容から推定）

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | Schemes 3A/3B異なる基質設計の実験設計問題 | v15 D4-7として独立D-4候補（V3=high, single agent）。「O-ピバロイル(3A) vs O-ペンタフルオロベンゾイル(3B)という異なる活性化基を使用しており、対照実験として不完全」 | 消失。B-6（13a/b特性評価問題）は残るが、設計上の非対称性問題はD-4候補化されず | ⚠️ medium |
| R2 | refs 10-13への波及の未検証 | v15 D4-6として「電子豊富配位子が他の方法論（アジリジン化、ベンジンアミノ化等）でもラジカル経路を促進するか」という具体的問い | v16.1 D-4-8「合成標的・目的論的文脈の不在」に一般化。「refs 10-13への波及」という具体的問いが薄れている | ⚠️ partial recovery |

### 総合判定

**v16.1 > v15**

v16.1の優位点:
- U-1（p-シメン自己矛盾的不在）: self-contradictory absence ruleが作動。v15に対応なし。D-4-3として候補化
- U-2（Pd(I)不均化）: v15になし。触媒サイクルの機構的内部矛盾を新規捕捉
- U-3（TEMPO/Pd(0)酸化）: v15 D4-5と等価だがU分類として明示、D-4-5と連動
- A-2（スコープ「予備的」先送り）: v15になし。v16.1で独立A項目として明示
- B-item consolidation ruleの系統的適用により同一引用を参照する複数B項目が整理
- SRG-7（定量的報告の省略群）による構造的問題の可視化が向上
- E節のconfirmed_english_propositionalがscope anchor ruleに忠実（v15はmechanism clauseを含む）

退行2件のうちR1（medium）は分析的損失。R2は部分的回復の範囲。

### v16.1で確認された正の副次効果

- self-contradictory absence rule（p-シメン: U-1/B-7）がmechanism paperでも有効に作動
- A-1 ↔ B-20 および A-1 ↔ B-14 のピボット構造が「現段階留保→定量的根拠不在」の依存関係を明示
- SRG-3が4項目（A-1, B-14, B-20, U-2）を統合し、SET機構問題の複合的不在を構造化

### 確認された未回復項目

- R1（Schemes 3A/3B対照実験の設計上の非対称性）→ open_issues OI-008（新規）

---

---

## Entry 008: v15 vs v16.1 — app2 (test)

**比較日:** 2026-04-15
**評価論文:** app2 (Meck et al., J. Am. Chem. Soc. 2025, 147, 44692–44698) — testset
**モデル:** claude-sonnet-4-6

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 6 | 1 |
| B | 13 | 17 |
| C | 5 | 4 |
| U | 0 | 2 |
| SRG | 6 | 5 |
| D-4候補 | 7 | 5 |
| 合計(A+B+C+U) | 24 | 24 |

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | N-Ph基質の不活性化に対する「電子的」帰属（無証拠）の高温度項目 | B-2（3/3収束、high_convergence_HIGH_gap）/ D-4候補1 | 完全に不在 | ⚠️ high impact |
| R2 | 「塩基がee誘起に必要」という抑圧された観察 | A-2（suppressed、V2=critical）/ D-4候補2 | 不在（B-14/B-4に部分的に分散） | ⚠️ medium impact |
| R3 | メフェニトイン最終生成物(30)のee直接測定不在・水素化条件未記載 | B-6（詳細分析あり） | B-11で部分カバーのみ | ⚠️ medium impact |

### 総合判定

**v16.1 ≥ v15（R1により部分的退行）**

v16.1の優位点:
- U-1（PhOH自己矛盾的不在）: self-contradictory absence ruleが正確に作動
- U-2（aza-Wacker論理の空白）: ラセミ26の排除論理の空白を新規捕捉（v15のA-4/A-5を超える）
- B-3（絶対配置帰属）: 3/3収束（v15 B-4は2/3収束）に向上
- B-7（スコープ主張の非対称提示）: "unprotected nitrogen" vs footnote 23 乖離を正式B分類
- スケールアップ収率の正確な引用: "31%, 94% ee"（v15は"similar"と不正確）

退行3件のうちR1がhigh impact。v15の唯一のhigh_convergence_HIGH_gap項目
（N-Ph電子的帰属、3/3収束）がv16.1で完全消失したことはD-4分析の深度において実質的損失。

### v16.1で確認された正の副次効果

- self-contradictory absence ruleがorganic synthesis論文（非機構論文）でも有効に作動（U-1）
- U-2がaza-Heck vs aza-Wacker の論理的差異を精確に区別（B-5の補完）
- A項目を6→1に整理し分類精度向上（機構的問いの多くをB/Uへ適切に再分類）

### 確認された未回復項目

- R1（N-Ph電子的帰属の3/3 high_convergence_HIGH_gap）→ open_issues OI-009（新規）
- R2（塩基/ee suppressed観察）→ OI-009に統合

---

## Entry 009: v15 vs v16.1 — het2 (test)

**比較日:** 2026-04-15
**評価論文:** het2 (Newton, Takle, Richardson, Hellgardt, Hii — ACS Catal. 2024, 14, 9678–9686)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

het2はタンデム型連続フロー反応器（PBR→PFR）を用いた in situ Pd溶出・失活研究論文。
3触媒（PdEnCat 30, FibreCat FC-1001, Pd/Al2O3）×3溶媒×個別反応成分を系統的に解析し、
ICP-MSによるPd定量とHPLCによる変換率監視を組み合わせている。

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 8 | 4 |
| B | 15 | 13 |
| C | 5 | 8 |
| U | 1 | 3 |
| SRG | 6 | 7 |
| D-4候補 | 7 | 8 |
| 合計(A+B+C+U) | 29 | 28 |

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | B-9: 逐次昇温プロトコルの混交問題（30°C→90°C同一ランで実施） | 対応なし | B-9（medium）「30°Cフェーズで既に微量溶出が始まるため、90°Cフェーズの変換率が前フェーズの状態変化に汚染されている」として独立B項目 | ⚠️ medium-high impact |
| R2 | U-2: α-水素化物消去によるN-脱アルキル化副生成物の自己矛盾的不在 | 対応なし | U-2（self-contradictory absence ruleが作動）「Scheme 2がN-脱アルキル化副生成物を予測するが、その検出・定量が報告されていない」 | ⚠️ medium impact |
| R3 | U-3: Pd(0)前提とPdEnCatの実際の含有種の不整合 | 対応なし | U-3（medium-high）「PdEnCatはPd(OAc)₂（Pd(II)）を含有するが、論文はPd(0)表面への酸化的付加を仮定。Pd(II)→Pd(0)還元の証拠が不在」 | ⚠️ medium-high impact |
| R4 | C-5（Muzart ref 52）・C-6（Clark ref 53）の文献分析 | C項目5件（ref 23, 24, 28, 56, + 1件） | C-5（Muzart 1992: DMF vs. ketoneのPd安定化比較）、C-6（Clark 2002: tributylamine + Pd(OAc)₂の反応条件）として独立C項目 | ⚠️ low-medium impact |
| R5 | C-8: PdEnCatのSuzuki反応への相反報告（refs 41,42） | 対応なし | C-8（refs 41,42が競合するPdEnCat安定性評価を含む）として独立記録 | ⚠️ low impact |
| R6 | 確定的命題の論文固定度 | "Leaching and catalytic activity of Pd species from heterogeneous catalysts depend on support type and individual reaction components."（機構的節が混入） | [REDACTED: verbatim source quotation; see the source paper via its DOI]（scope anchor ruleに忠実） | ⚠️ low impact |

### 総合判定

**v16.1 > v15**

v16.1の優位点:
- U-2（α-水素化物消去副生成物の自己矛盾的不在）: self-contradictory absence ruleが化学機構論文でも有効に作動
- U-3（Pd(II)前提とPd(0)仮定の不整合）: 単一エージェント（V2）ながらcritical評価、D-4候補6に直接接続
- B-9（逐次昇温の混交問題）: flow reactor特有の変数が独立B項目として捕捉された
- C-8（Suzuki相反報告）: exhaustive extraction ruleが作動
- confirmed_english_propositionalがscope anchor ruleに忠実（v15は機構的節が混入）

退行6件のうちR1（medium-high）とR3（medium-high）が最大の損失。

### v15固有の正の寄与

- B-5（ICP-MSフラクション統合問題）: 90分の全収集液を単一画分にプールした場合、時間分解溶出プロファイルが得られないという分析設計問題を独立B項目として捕捉。v16.1では対応なし。
- B-14（F2希釈係数の不明）: 配置2でF1流（溶出Pd含有）がF2でF2成分と混合する際の希釈係数が未記述という問題。v16.1では対応なし。
- A-2（suppressedの精確な分類）: 30°C NEt3溶出が"rather unexpected"と記述されているにもかかわらず機構的説明が回避されている点を三要件チェックリストに基づきsuppressedとして分類。v16.1では一般的先送り分類に留まる。
- D-4候補の粒度: D-4-5（配置2の設計的盲点）、D-4-6（4mg等量比較の未検証基盤）がv15固有の候補として独立展開。

### 確認された未回復項目

- R1（逐次昇温プロトコルの混交問題）: flow reactor特有の問題で、既存OIのカバレッジなし → OI-011（新規）
- R2（U-2 α-水素化物消去副生成物の不在）: self-contradictory absence ruleがv15で未作動
- R3（U-3 Pd(0)前提との不整合）: V2の機構論的エージェントとしての精度差に起因

---

## Entry 010: v15 vs v16.1 — het1 (test)

**比較日:** 2026-04-15
**評価論文:** het1 (Yuan et al., J. Am. Chem. Soc. 2018, 140, 8206–8217)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 3 | 3 |
| B | 28 | ~22（S2 D-4参照から推定） |
| C | 3 | ~4 |
| U | 0 | 5 |
| SRG | 7 | ~6 |
| D-4候補 | 8 | 8 |

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | U項目（自己矛盾的不在）の不在 | 0項目（全てB/A分類） | U-1〜U-5（Pd(0)非検出矛盾、60℃活性帰属矛盾、Cl⁻起源矛盾など） | ⚠️ medium |
| R2 | 不均一性テスト回避のD-4候補化 | B-6としてmethodological_limitationに留まる | D-4-2としてcritical評価（V2）、B-5↔C-1ピボット構造で展開 | ⚠️ medium |
| R3 | Wacker副反応のオレフィン質量収支 | 対応なし（B-8はWacker証拠の不十分性のみ） | D-4-5として独立候補（18 mol% Pd × Wacker化学量論） | ⚠️ low |
| R4 | 否定的証拠の検出下限問題 | 対応なし | D-4-8として独立候補 | ⚠️ low |
| R5 | E節 scope_type 判定 | framework_question | tool_question（論文の実際の問いに近い） | ⚠️ low |

### 総合判定

**v15 < v16.1**

v16.1の優位点:
- U-2（Pd(0)非検出と活性種主張の矛盾）: self-contradictory absence ruleが正確に作動
- U-4（60℃活性帰属矛盾）: 「Wacker型Pd(0)が既に存在する」という論文自身の記述と「60℃活性は単核Pd(II)リンカー錯体のもの」という帰属の矛盾を独立捕捉
- D-4-2（不均一性テスト回避）: B-5の引用回避パターンをC-1と組み合わせてpivot構造化。D-4内の最重要候補として展開
- D-4-5（Wacker化学量論）: 18 mol% Pd × Wacker消費によるオレフィン質量収支問題はv15に完全に不在
- D-4-8（否定的証拠の検出下限）: 「Pd–I距離が観測されない」等の否定的証拠への検出下限問いはv15に不在
- scope_type = tool_questionがより論文の実際の問いに忠実

退行5件はいずれもlow〜medium impact。

### v15固有の正の寄与

- D-4候補2（EXAFSフィット統計的決定性）: k範囲・R範囲・R因子・Nyquist基準・S₀²の不在をSRG-1として4B項目に体系的展開。v16.1のD-4-4（クラスターサイズパイプライン）より網羅的
- D-4候補1（熱効果と化学変化の未分離）: 温度ランプ下でのXANES/EXAFS変化に対するブランク実験不在を3/3収束項目として展開。v16.1のD-4-6（非等温加熱ランプ）より広い問い
- D-4候補8（単一基質での汎用性主張）: 「widely applicable」主張と単一基質系との乖離をB-14↔A-2として展開。v16.1には明示的対応なし

### 確認された未回復項目

- R1（U項目生成）: v15プロンプトのself-contradictory absence rule不在に起因。OI-009で追跡中のパターンと一致
- R3（Wacker質量収支）、R4（否定的証拠）: OI-007の「否定的証拠検出下限」問題との連続性あり

---

## Entry 011: v15 vs v16.1 — scr2 (test)

**比較日:** 2026-04-15
**評価論文:** scr2 (Templ, Hwang, Schwemin, Baltaci, Borchardt — RSC Mechanochem. 2025, 2, 598–602)
**モデル:** claude-sonnet-4-6

### 背景

scr2はPdミリングボールによる直接メカノ触媒的Mizoroki–Heck反応を報告するフルペーパー（5ページ）。
v15で新規解析（S0〜S2）を実施し、既存のv16.1出力と比較。

### 項目数の変化

| カテゴリ | v15 | v16.1 |
|----------|-----|-------|
| A | 5 | 10 |
| B | 15 | 5 |
| C | 2 | 5 |
| U | 1 | 5 |
| SRG | 7 | 4 |
| D-4候補 | 8 | 6 |
| 合計(A+B+C+U) | 23 | 25 |

※v15はA→B分散（methodological limitationをAではなくBに多く配置）のためA/B比率が大きく異なる。

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | 浸出実験（ESI）の過小評価・誤記述 | B-3で「Pd浸出未定量、データなし」と記述。ESI参照の定性的結論（"not mainly"）を完全不在として扱った | A-5として「"not mainly"修飾語付きでESIに委任」と正確に分類し、均一系の部分寄与が否定されていない点を指摘 | ⚠️ high |
| R2 | ArF結合の過剰主張の不検出 | 該当項目なし | B-3（"C(sp²)–X bonds (X = F, Cl, Br) intact"でArF実験なしにもかかわらずFを列挙）として独立記録 | ⚠️ medium |
| R3 | ミリング無条件下での対照実験の不検出 | B-2で「内部温度未測定」に焦点。「ミリングなし・室温での生成物非検出」という対照実験の存在自体を未認識 | B-4として「120°Cミリングなし・室温30 Hzで生成物なし」の二値対照のみという限界を記録 | ⚠️ medium |
| R4 | series_signal判定の誤り | series_signal: no | series_signal: yes [T2]（Suzuki→Sonogashira→Heckの系列を検出） | ⚠️ low |
| R5 | C項目の密度 | C-1, C-2の2項目（広域グループ分類） | C-1〜C-5の5項目（PFA jar ref、浸出方法ref、Wittig先行論文含む） | ⚠️ low |

### 総合判定

**v16.1 > v15**

v16.1の優位点:
- R1: 浸出実験の"not mainly"修飾語の分析（均一系の部分寄与が否定されていない点）がA-5として精確に記録
- R2: ArF実験なしにもかかわらずConclusionsにX=Fを含む過剰主張をB-3として独立記録
- R3: ミリングなし対照実験の存在を認識した上でB-4として「二値対照のみ」という限界を記録
- U項目（5 vs 1）: U-2（空気/O₂役割）、U-3（C(sp²)–Br残存の誘導体化未実施）、U-4（3t出発物質の具体的同定）、U-5（TEA塩基性効果の解釈）が独立記録

### v15固有の正の寄与

- K₂CO₃「沸点119°C」という見かけ上の事実誤謬の検出（U-1）: v16.1では未指摘
- D-4候補6（合成標的との接続の不在）: v16.1対応なし
- B項目の網羅性（15 vs 5）: No blank control（B-5）、Pd ball surface area/TON未報告（B-6）等を個別に明示
- E節のconfirmed_english_question: 「表面触媒か浸出ナノ粒子か」という機構的区別を明示（v16.1の"chemoselective"追加に対して scope anchor ruleにより忠実）

### 確認された未回復項目

- R1（浸出実験の誤記述）: v15がESI参照データを「実験不在」と扱う傾向 → OI-012（新規）
- R2（ArF過剰主張の不検出）: Conclusions中の実験未実施基質の過剰主張をv15が見落とす傾向

---

## Entry 012: v15 vs v16.1 — scr1 (test)

**比較日:** 2026-04-15
**評価論文:** Fodor, Kégl, Takacs, Horváth, Mika — "Homogeneous Pd-Catalyzed Heck Coupling in γ-Valerolactone as a Green Reaction Medium" (ACS Sustainable Chem. Eng. 2020, 8, 9926–9936) — testset
**モデル:** claude-sonnet-4-6
**評価者:** Sonnet セッション

### 背景

GVL溶媒中のPd触媒Heckカップリングの速度論・DFT・グリーン化学研究。
v15出力: A=2, B=27, C=4, U=0, SRG=7
v16.1出力: A=1, B=17, C=5, U=5, SRG=5

### スコアカード

| ID | 退行ポイント | v15 | v16.1 | 判定 |
|----|---|---|---|---|
| R1 | U項目（自己矛盾的不在）の生成 | 0項目 | U-1〜U-5（5項目）: U-4「DFTが均一系触媒を前提とするが均一系が未確認」(critical)、U-5「GVL vs DMF速度差がないとの主張の統計的根拠不在」(critical)含む | ⚠️ high |
| R2 | 導入部の速度論ベンチマーク引用の展開不在 | C-1: GVL先行論文（refs 55-58）、定性的。Amatore/Dupont論文の数値的ΔS‡値(+7, −43 J/K/mol)と本論文ΔS‡_app(+103.7〜+138.1)の劇的乖離を未捕捉 | C-1（Amatore, ΔS‡=+7 J/K/mol）、C-2（Dupont, ΔS‡=−43 J/K/mol）として独立記録。導入部に数値付き引用で登場しながら結果部で比較されない「中断引用」を明示 | ⚠️ high |
| R3 | Et₃N対照実験の定性的限界 | 対応項目なし（A-2はEt₃Nの化学量論的役割の不在） | B-9「Et₃N量がcis/trans比に影響するかの対照実験なし」として独立記録 | ⚠️ medium |
| R4 | フィッティング誤差の定量的超過 | B-10「フィッティング偏差の統計的評価なし」（汎用的記述） | B-14「GVL実験のDMFフィッティングで5.3%偏差が論文自身の5%基準を超過」（数値的・具体的）として記録 | ⚠️ medium |

### 総合判定

**v16.1 > v15**

- R1: U項目の完全欠如は最大の差異。特にU-4（DFT前提の自己矛盾）とU-5（溶媒効果なしの主張の根拠不在）は本論文の中核的弱点を捉えており、v15では完全に見落とされた
- R2: Amatore/Dupont論文のΔS‡値（+7, −43 J/K/mol）は本論文のΔS‡_app（+103.7〜+138.1 J/K/mol）と1〜2桁異なる。この乖離が導入部で「先行研究」として引用され結果部で比較されない構造が、v16.1では「速度論ベンチマーク引用の中断」として記録された（→ OI-013）
- R4: v16.1はB-14で論文自身の5%基準との定量的比較を行った。v15のB-10は一般的な統計評価の欠如に留まる

### v15固有の正の寄与

- B-27（エンタルピー・エントロピー補償の等速度的関係の未検定）: v16.1に対応項目なし。ΔH‡とΔS‡が共変する等温パターンがアイソキネティックプロットで検証されなかった点を明示
- B-17（ラジカル vs イオン機構識別の不在）: v16.1に対応項目なし。Heck反応のラジカル経路検討なしの問題
- B-26（固定時間TOFがinitial rateに等しくないハメット相関の限界）: v16.1対応なし。30分時点のTOFと速度定数比の非等価性を指摘

### 確認された未回復項目

- R1（U項目0 vs 5）: v15はself-contradictory absence ruleを適用しなかった → OI-013で別途追記（pattern: DFTの前提未検証がU項目として浮かび上がる条件の捕捉不全）
- R2（Amatore/Dupont C項目の欠如）: 速度論的数値ベンチマークが導入部に登場しながら結果部で比較されないパターンがv15では捕捉されない → OI-013に追記

---

---

## Entry 013: v16.1 vs v17 — Kumada (devset)

**比較日:** 2026-04-15
**評価論文:** Kumada (Tamao, Sumitani, Kumada, JACS 1972) — devset
**モデル:** claude-sonnet-4-6
**比較対象:** v16.1 → v17（新版）

### 背景

v17はv16.1からの改善として、OI-004（yield basis mixing exception）、OI-007/008
（否定的証拠の検出下限・実用条件外挿）、OI-013（速度論的ベンチマーク引用）等の
修復を導入した版。Kumada devsetで初のv17評価。

### 項目数の変化

| カテゴリ | v16.1 | v17 |
|----------|-------|-----|
| A | 2 | 2 |
| B | 約9 | 14 |
| C | 3 | 4 |
| U | 4 | 4 |
| D-4候補 | 5 | 8 |
| SRG | 3 | 6 |

### スコアカード

| ID | 退行ポイント | v16.1 | v17 | 判定 |
|----|---|---|---|---|
| R-1 | 発熱性エントリー（Cl₂C=CH₂/PhMgBr, Table I footnote f）の自己矛盾的不在記録 | U-1(b)として D4-1に統合 | 消失（U-1がR–R不在に変更） | ⚠️ 部分後退 |
| R-2 | D4-1の統合的記述（4下位要素の凝集） | 高凝集（1候補に「ラジカル・発熱性・黒色混合物・ホモカップリング予測」を統合） | D4-2+D4-6に分散、発熱性欠落 | ⚠️ 部分後退 |

### 正の変化（v17の改善点）

1. **B-12（yield basis mixing exception）が実装・作動**: Example 1（有機ハライド基準）vs
   Example 2（Grignard試薬基準）の収率計算基準不一致が独立B項目として記録。
   OI-004対応の直接的成果。
2. **D4-3（Table I収率データの信頼性）が体系化**: SRG-3（B-4, B-8, B-9, B-12, B-13の5項目）
   として統合された新候補。v16.1では散在していた分析的品質問題を一候補に凝集。
3. **D4-5（選択性の速度論的vs熱力学的性格）が独立候補化**: A-1・B-11・U-3から独立した
   第5候補として明示化。v16.1のD4-2のサブ要素だったものが独立。
4. **confirmed_english_questionのfeature削除**: v16.1の "over competing homo-coupling"
   という結果節がスコープアンカールールに従い削除。
5. **B-14（dipy-Ni類推の問題）が独立B項目化**: v16.1では D4-1の注記に埋もれていたが、
   B-14として独立し D4-2のgrounded_inに明示的に入力。
6. **SRGが6グループに細分化**: SRG-1〜6として各問題群の根拠が明示化され、
   D4候補との対応が追跡しやすくなった。

### 総合判定

**v17 > v16.1**

B項目の大幅充実（9→14）、D4候補数の増加（5→8）、B-12（yield basis exception）の
実装、D4-3・D4-5の新規体系化が v17 の優位を確立する。退行2件（R-1/R-2）はいずれも
発熱性エントリー（footnote f）の処理に起因し、severity=lowだが継続して注視が必要。

### v17で確認された未回復項目

- R-1/R-2: 発熱性エントリー（"Reaction proceeded exothermally"）の自己矛盾的不在記録
  が消失。→ open_issues OI-014

## Entry 014: v16.1 vs v17 — Murai (devset)

**比較日:** 2026-04-15
**評価論文:** Murai (Murai, Kakiuchi, Sekine, Tanaka, Chatani, Nature 1993) — devset
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

v17はv16.1からの改善として OI-007/008（否定的証拠検出下限・実用条件外挿）、
OI-013（Dropped Quantitative Benchmark）、OI-012（ESI委任 vs 実験不在の区別）等を
組み込んだ版。Murai devsetで初のv17評価。

### 項目数の変化

| カテゴリ | v16.1 | v17 |
|----------|-------|-----|
| A | 2 | 1 |
| B | 14 | 20 |
| C | 8 | 5 |
| U | 2 | 2 |
| SRG | ~4 | 5 |
| D-4候補 | 7 | 8 |
| 合計(A+B+C+U) | 26 | 28 |

### スコアカード

| ID | 退行ポイント | v16.1 | v17 | 判定 |
|----|---|---|---|---|
| R1 | D-4候補2（シリル基が「隠れた要件」の可能性）の消失 | D-4候補2として独立展開。Table 1の大多数がシリル化オレフィンである事実を「汎用性」主張との矛盾として展開 | B-13（olefin scope, intentional_narrowing）で記録あり。「シリル基が本質的要件である可能性」という角度のD-4候補なし | ⚠️ medium |
| R2 | D-4候補4（キレーション補助の必要性：引き算の実験不在）の消失 | [REDACTED: verbatim source quotation; see the source paper via its DOI]に対し、非キレート基質（アルキルベンゼン、フェニルエーテル等）での対照実験不在をD-4候補として独立展開（B-12 grounded_in） | B-12（"unactivated" C-H claim）、B-17（chelation tether length）はあるが「非キレート基質のnegative control」という核心角度がD-4候補化されていない | ⚠️ medium |
| R3 | D-4候補5＋high_convergence_HIGH_gap（シクロメタル化中間体の単離・同定の不在）の消失 | B-10（V2=critical, V3=medium; gap=medium）がhigh_convergence_HIGH_gap最優先項目。D-4候補5として中間体単離の不在を独立展開 | B-3（機構全般absent）+ SRG-1で機構的問題群として広くカバーするが、中間体単離に特化した項目なし。high_convergence_high_gap=[] | ⚠️ medium |
| R4 | v16.1 U-1（Ru(CO)₂(PPh₃)₃が"equally effective"と提案機構の矛盾）の消失 | U-1として"equally effective"=M-H挿入不要という自己矛盾的不在を独立記録 | B-10注記に「V2-Q9: ligand effects mechanistically significant」として言及のみ。U項目・D-4候補化なし。v17 U-1はRu(II)→Ru(0)活性化（別角度） | ⚠️ low |

### 総合判定

**v17 ≥ v16.1（R1〜R4 により部分的退行）**

v17の優位点:
- **U-1（Ru(II)→Ru(0)活性化の自己矛盾的不在）**: v16.1はRu(CO)₂の矛盾を捕捉したが、
  前駆体活性化ステップ（H₂還元脱離等）の未記述という根本的矛盾はv17が初捕捉
- **U-2（β-水素脱離抑制の自己矛盾的不在）**: v16.1のU-2「ヒドリドマスバランス」と異なる
  角度。M-アルキル中間体がβ-H脱離すべきにもかかわらず異性化副生成物が報告されない矛盾
- **B-5（runs 1+2 マスバランス欠損の数値的特定）**: 75+8=83%で17%欠損という具体的計算。v16.1では一般的質問に留まる
- **B-11（run 2 excess olefin使用の内部矛盾）**: 「一方を過剰使用」という批判に対して
  run 2自身が3:1比を使うという矛盾を独立B項目化
- **B-17（キレーション支援の構造的境界：tether length）**: D-4候補7として展開。v16.1にはない角度
- **D-4候補4（1-インダノン否定的証拠の検出下限）**: OI-007/008対応が実際に作動
- **D-4候補5（実用条件への外挿根拠の不在）**: OI-007/008対応として新規捕捉
- **B項目の網羅性向上（14→20）**: GC収率信頼性・再現性・雰囲気条件等を独立B項目として体系化

退行4件中R3が構造的影響最大（high_convergence_HIGH_gap消失はD-4選択基盤の弱体化）。
R1（シリル基隠れた要件）は化学的ドメイン知識を要する角度であり、プロンプト的対応が難しい。

### C項目の変化について

v16.1の8件→v17の5件への減少は、v17が参照文献を広域グループに統合した結果。
C-5（refs 16-18、機構サポート引用）は複数文献を一グループとして処理。
個別の文献分析密度はv16.1がやや優位だが、v17の統合はMETAへの接続が明確。

### 正の副次効果

- OI-007/008（否定的証拠の検出下限・実用条件外挿）がMurai論文で初作動確認
- OI-013（Dropped Quantitative Benchmark）が C-2（refs 11-12）として正確に生成
- SRGが5グループに体系化され、D-4候補との対応が明示化
- self-contradictory absence ruleがB-14↔U-1、B-3↔U-2 の二重記帳で機能

### 確認された未回復項目

- R1（シリル基隠れた要件のD-4化）: 基質分布バイアスへの感度が低い → OI-015（新規）
- R3（high_convergence_HIGH_gap消失パターン）: OI-014（Kumada発熱性エントリー）と
  同種の問題。高温度項目の再配置・統合によりD-4選択の最優先候補が消失する傾向継続

---

## Entry 015: v161 vs v17 — app2 (test)

**比較日:** 2026-04-15
**評価論文:** app2 (Meck, Omer, Edwards, Idowu, Murray, Korch, Watson — JACS 2025, 147, 44692–44698)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

app2はPd(OAc)₂/キラルホスホロアミダイト(L1)触媒によるaza-Heck環化で四置換ヒダントインを不斉合成するJACS Communication（7ページ）。v161で初回解析済み。v17は新規解析として本セッションで実施。

### 項目数の変化

| カテゴリ | v161 | v17 |
|----------|------|-----|
| A | 1 | 1 |
| B | 約17 | 17 |
| C | 0 | 3 |
| U | 2 | 1 |
| SRG | 約5 | 6 |
| D-4候補 | 5 | 8 |
| 合計(A+B+C+U) | 約20 | 22 |

### スコアカード

| ID | 退行ポイント | v161 | v17 | 判定 |
|----|---|---|---|---|
| R1 | N–O酸化的付加機構が予測するPhOH化学量論的副生物の問い | U-1 + D-4候補1（N–O OAによりPhOH等モル副生という具体的化学的予測として独立展開） | U-01（機構全般の自己矛盾的不在として広くカバーするが、PhOH具体的化学予測への言及なし） | ⚠️ medium impact |
| R2 | aza-Wacker並行経路によるeeの上限問題（87–99% eeの欠損原因） | U-2 + D-4候補2（26がラセミ排除 ≠ 並行ラセミ経路の排除。O₂添加実験の定量データ欠如と組み合わせて独立展開） | D-4-2はaba-Wacker副生物26の検出下限に焦点。「並行ラセミ経路→ee欠損」という定量的問いの独立展開なし | ⚠️ medium impact |
| R3 | "unprotected nitrogen"（abstract graphic）vs footnote 23の修辞的緊張 | B-7 + D-4候補5として独立展開（"excellent, unprotected nitrogen"主張とN,N-ジアルキル基質の完全不反応の乖離） | B-04がN,N-ジアルキル基質の失敗を methodological_limitationとして記録するが、abstract graphicの主張との修辞的緊張としてD-4候補化されず | ⚠️ low impact |

### 総合判定

**v17 > v161（R1〜R3により部分的退行）**

v17の優位点:
- **C項目の初出（C-01〜C-03）**: app2で初のC項目。C-01（Archambeau Dropped Quantitative Benchmark: "good to modest ee"が数値なし）、C-02（先行aza-Heck技術refs [11-14]の数値比較欠如）、C-03（Atkinson合成との定量比較欠如）が独立記録。OI-013対応が初作動。
- **B-03（yield basis mixing exception）**: OI-004対応。Scheme 3のNMR収率と単離収率の混在を脚注から正確に検出し独立B項目化。
- **B-16（基底状態エネルギーのTS代理問題）**: v161にない新規角度。ground-state conformer energy（0.6 kcal/mol）をTS活性化エネルギーの代理として使う論理的問題を独立B項目として捕捉。
- **D-4候補の充実（5→8）**: D-4-6（グラムスケール収率31% vs 78%の急落）、D-4-7（L9一般性未評価）、D-4-8（nBu₂N塩基の触媒サイクル上の役割不明）が新規。
- **SRG体系化（6グループ）**: SRG-1〜6として各問題群の根拠が明示化。
- **B-08（ee決定法未開示）、B-12（塩基の役割）、B-13（N-O結合同定不在）、B-14（再現性データなし）**: v161で未記録の報告省略が独立B項目化。

退行3件のうちR1（PhOH予測）が最も重要。v161が捕捉した「N–O酸化的付加機構が化学量論的に予測するPhOH副生物」という具体的化学的予測が、v17では機構全般の「中間体不在」問いに吸収されて希薄化した。

### 正の副次効果

- C項目exhaustive extraction rule（OI-013由来のDropped Quantitative Benchmark）がaza-Heck organic synthesis論文で初作動確認（C-01: Archambeau ee値の数値引用なし比較）
- B-16の「基底状態エネルギー ≠ TS活性化エネルギー」という論理的誤りの捕捉は、DFTなし論文における計算化学的主張の品質評価として新規パターン

### 確認された未回復項目

- R1（N–O OA機構のPhOH化学量論的予測）: v17のU-01の一般化により具体的化学予測が吸収・希薄化 → OI-016（新規）
- R3（"unprotected nitrogen" vs footnote 23の修辞的緊張）: OI-009で部分的に追跡中だが、v17でも未解決 → OI-009の備考に追記

---

## Entry 016: v16.1 vs v17 — het2 (test)

**比較日:** 2026-04-15
**評価論文:** het2 (Newton, Takle, Richardson, Hellgardt, Hii — ACS Catal. 2024, 14, 9678–9686)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

het2はタンデム型連続フロー反応器（PBR→PFR）を用いたin situPd溶出・失活研究論文。
v16.1はEntry 009（v15 vs v16.1比較）で既評価済み。
v17はOI-011（逐次昇温プロトコル混交問題）を含む複数改善を組み込んだ新版。
本比較はv16.1（最近版）とv17の直接比較。

### 項目数の変化

| カテゴリ | v16.1 | v17 |
|----------|-------|-----|
| A | 4 | 4 |
| B | 13 | 22 |
| C | 8 | 5 |
| U | 3 | 4 |
| SRG | 7 | 5 |
| D-4候補 | 8 | 8 |
| 合計(A+B+C+U) | 28 | 35 |

### スコアカード

| ID | 退行ポイント | v16.1 | v17 | 判定 |
|----|---|---|---|---|
| R1 | D-4候補7（pseudosteady state機構の未解明）の消失 | D-4候補7として独立展開「Pd/Al₂O₃の疑似定常状態（60–90分でca. 30%変換率維持）の機構が一切説明されていない」（A-3 = forgotten由来） | A-3は依然A項目として存在するが、D-4候補として独立展開されず。D-4候補群のいずれにも擬似定常状態機構の問いが含まれない | ⚠️ medium impact |
| R2 | U-2（α-ヒドリド脱離副生物の自己矛盾的不在）の消失 | U-2として独立記録「Scheme 2が正しければNEt₃の酸化副生物（エナミン、イミニウムイオン）とPd(OAc)₂還元由来の酢酸が化学量論的に生成するはずだが一切測定・報告されていない」→ D-4候補3の核心構成要素として展開 | D-4候補4（α-ヒドリド低温パラドックス）にU-4として吸収されているが、具体的副生物（エナミン/イミニウムイオン/AcOH）の化学量論的予測への言及なし。一般的「温度パラドックス」問いに吸収 | ⚠️ medium impact |
| R3 | U-3（PdEnCat Pd(OAc)₂ vs Pd(0)前提の矛盾）の一部希薄化 | U-3として「PdEnCatはPd(OAc)₂（Pd(II)）を含有するが、論文はPd(0)表面への酸化的付加を仮定。Pd(II)→Pd(0)還元の証拠が不在」として独立記録。D-4候補2の構成要素として展開 | v17 U-2はPd/Al₂O₃表面PdO層に関する矛盾（ArI誘起リーチングがPd(0)OAを仮定するがPdO表面と矛盾）に変更。PdEnCat固有のPd(OAc)₂問題はD-4候補1テキスト内（Pd(II)→Pd(0)還元言及あり）に部分的に存在するが、独立U項目・D-4候補としての展開なし | ⚠️ low impact |

### 総合判定

**v17 > v16.1**

v17の優位点:
- **U-1（新鮮触媒床の独立性問いが初出、critical）**: 「コンフィギュレーション2の成分A/B/C/D実験が同一触媒床vs独立触媒床のどちらで実施されたか」という問いがv16.1で完全に不在だったのに対し、v17でcritical評価の独立U項目として新出。D-4候補1の核心
- **B-2（逐次昇温プロトコル混交を独立B項目として明示化）**: v16.1ではD-4候補6のテキスト内に埋め込まれていたが、v17では独立B項目として抽出される。OI-011が解決された
- **U-4（A-2の suppressed 再分類 + 温度パラドックスU項目化）**: v16.1のA-1/A-2の統合的処理に対し、v17はsuppressed三要件チェックリストに基づきA-2（30°C NEt₃漏出）をsuppressedと精確に分類し、U-4（温度パラドックスの自己矛盾的不在）として独立記録
- **D-4候補5（個別成分非加算性の発見）**: 313 ppm（個別和）vs 455 ppm（全成分）の140 ppm超過という定量的非加算性を独立候補として展開。v16.1では候補8（協調効果）として類似問いが存在したが、数値的非加算性の明示的計算はv17が初
- **C-4（ref 12 Dropped Quantitative Benchmark）**: OI-013対応。Greco/Kappeのref 12がFC-1001で量的リーチングデータを含む可能性を指摘し、未比較として記録
- **B項目の大幅充実（13→22）**: ICP-MS検出限界・再現性・流量・滞留時間・F2希釈係数等の報告省略を体系的にB項目化

退行3件（R1 medium, R2 medium, R3 low）のうちR2は OI-016（app2 PhOH問題）と同一パターン（一般化されたU項目が具体的化学量論的副生物予測を吸収）。

### 正の副次効果

- OI-011（逐次昇温フロー実験の混交問題）がv17 B-2として解決 → OI-011 status: resolved
- U-1「同一/独立触媒床問い」はflow catalyst評価論文の新規チェック項目として機能
- D-4候補の数的維持（8→8）に加え質的変化：候補5（非加算性）が純粋に定量的論理から展開された独立候補として新出

### 確認された未回復項目

- R1（pseudosteady state D-4候補の消失）: het2固有の観察（Figure 5C）がv17ではA-3に留まりD-4展開なし。独立追跡の必要はlow
- R2（α-ヒドリド副生物の具体的化学量論的予測）: OI-016（app2）と同一パターン → OI-016の備考に追記

---

## Entry 017: v161 vs v17 — app1 (test)

**比較日:** 2026-04-15
**評価論文:** app1 (Zhang, Tutkowski, DeLuca, Joyce, Wiest, Sigman — Chem. Sci. 2017, 8, 2277–2282)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

app1はPd触媒エナンチオ選択的redox-relay Heckアルケニル化によりビシナルステレオセンターを構築する論文。
v161はEntry 007（v15 vs v161比較）で既評価済み。
本比較はv161（最近版）とv17の直接比較。

### 項目数の変化（v161 → v17）

| カテゴリ | v161 | v17 |
|----------|------|-----|
| A | 1 | 1 |
| B | ~16 | 23 |
| C | 0 | 5 |
| U | 2 | 4 |
| SRG | ~4 | 6 |
| D-4候補 | 6 | 8 |
| 合計(A+B+C+U) | ~19 | 33 |

### スコアカード

| ID | 退行ポイント | v161 | v17 | 判定 |
|----|---|---|---|---|
| R1 | シクロプロピル実験「"confirms"過剰主張」という修辞的問いのD-4候補化 | D4-4として独立展開（"Ultimately, this confirms"という断言に対する問い） | B-11（methodological_limitation）に吸収・D-4候補として独立せず | ⚠️ medium impact |
| R2 | 実験データ全体の定量的信頼性という統合的問い | D4-2として「GC収率不在・dr実値・標準偏差・2当量使用根拠」を統合展開 | B-1, B-22等に分散記録、統合的D-4候補としての展開が弱化 | ⚠️ low impact |

### 総合判定

**v17 > v161（R1〜R2により部分的退行）**

v17の優位点:
- **C項目の初出（app1では初めて5C項目を体系的に抽出）**: C-1〜C-5（うちDropped Quantitative Benchmark 2件: C-1 refs 3c-f先行asymmetric Heck er値比較不在、C-2 refs 8e-g隣接立体中心合成先行例との比較不在）。OI-013対応が本論文で初作動。
- **U項目の精緻化（U-3, U-4が新規）**: U-3「エピ化なし主張の自己矛盾的不在（時間推移データなし）」、U-4「Table 1塩基スクリーンデータが機構弁別に未使用」はv161にない洞察。
- **D-4候補の増加・多様化（6→8）**: D-4候補1（触媒サイクル中間体実在性）、D-4候補4（塩基の役割）、D-4候補5（溶媒NBO相関の機構的意味）が新規角度として追加。
- **SRG構成の精緻化（4→6グループ）**: SRG-4（E/Z機構解釈）、SRG-5（NBO相関）、SRG-6（選択性制御）が独立グループとして明示化。
- **triflate異性化問いの独立記録**: B-9 + U-1のペアとして、B（方法論的限界）とU（自己矛盾的不在）の両面で記録。

退行2件：R1がより重要。「"Ultimately, this confirms"という断言の修辞的過剰主張」という角度は特定の実験が何を確立できないかを問う重要な視点であり、v17ではB-11に方法論的限界として記録されているが、D-4候補としての独立展開がない。

### 正の副次効果

- U-4（Table 1塩基スクリーンデータの機構弁別未使用）は「論文自身の最適化データが自己の機構仮説を検証するために使われていない」というself-contradictory absence検出の新パターン
- C項目exhaustive extraction（Dropped Quantitative Benchmark, OI-013由来）がPd触媒不斉合成論文で初確認（C-1: refs 3c-f, C-2: refs 8e-g）

### 確認された未回復項目

- R1（シクロプロピル実験「"confirms"過剰主張」のD-4候補化）: v17のB-11（methodological_limitation）に記録されているが、D-4候補としての独立展開は未回復 → OI-020（新規追記）

---

## Entry 018: v161 vs v17 — comp2 (test)

**比較日:** 2026-04-15
**評価論文:** comp2 (Palladino, Fantoni, Ferrazzano, Muzzi, Ricci, Tolomelli, Cabri — ACS Catal. 2023, 13, 12048–12061)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

comp2は銅フリーHeck–Cassar–Sonogashira（HCS）カップリングの機構解明を目的とするフルペーパー（14ページ）。
¹H/³¹P NMR、HPLC、GC、DFT（PBE/def2-TZVP）を駆使してアルキン直接配位経路と、
中性（ハライド）/カチオン性（トリフラート）の二経路を提案。
v161はEntry 005（v15 vs v161比較）で既評価済み。本比較はv161（最近版）とv17の直接比較。

### 項目数の変化

| カテゴリ | v161 | v17 |
|----------|------|-----|
| A | 3 | 2 |
| B | 18 | 20 |
| C | 5 | 3 |
| U | 5 | 2 |
| SRG | 6 | 5 |
| D-4候補 | 7 | 8 |
| 合計(A+B+C+U) | 31 | 27 |

### スコアカード

| ID | 退行ポイント | v161 | v17 | 判定 |
|----|---|---|---|---|
| R1 | D-4候補3（速度論的vs熱力学的選択性）の独立展開消失 | D-4候補3として「ハライド経路が速度論的制御、トリフラート経路が熱力学的制御という選択性原理」を独立展開。k_halide vs k_triflate の温度依存性測定の不在が核心 | D-4候補6（二経路選択制御原理 [B-14,A-1]）で部分的にカバーするが、速度論的vs熱力学的制御の実験的検証という角度が独立候補として浮上せず | ⚠️ medium |
| R2 | v161 U-4（RDS帰属の曖昧性：OA vs carbopalladation）の消失 | U-4として「酸化的付加 vs カルボパラデーション：どちらが律速段階かを論文内の実験データで区別できない」（V2=high）を記録。D-4候補7の核心 | B-17（TS障壁 vs RT、2/3収束）がDFT数値信頼性を問うが、OA vs carbopalladation の帰属曖昧性がU項目・D-4候補として独立記録されず | ⚠️ medium |
| R3 | v161 U-3（Ra/Rb順序）のD-4候補化消失 | D-4候補2として「DFT計算のRa>Rbエネルギー順序が実験的選択性と整合するか」を独立展開 | B-1（DFT方法論統合、3/3収束）のnote内に吸収。Ra/Rb順序に特化したD-4候補として独立展開なし | ⚠️ low |

### 総合判定

**v17 > v161**

v17の優位点:
- **U-1（脱プロトン化TS3の自己矛盾的不在）**: v161にない角度。論文が提案する脱プロトン化段階（TS3）に対し、塩基種・収率・pKa依存性等の実験的証拠が一切ないという自己矛盾的不在を初捕捉。D-4候補4の核心
- **U-2（M非検出の自己矛盾的不在）**: M錯体の速度論的競合（B:M競合）を論文が主張しながら、Mの不在が「not detected」のみで定量的根拠なく裏付けられている自己矛盾を捕捉。D-4候補3の直接根拠
- **D-4候補3（M非検出の検出下限）**: OI-007 R1に対応。「Complex M was never detected」という否定的証拠の検出下限値不在と機構的含意を独立候補として展開。初作動確認
- **B-1（DFT方法論、3/3収束、high_convergence_low_gap）**: V1/V2/V3全エージェントが分散指摘した7つのDFT方法論問題（分散補正・溶媒モデル・熱化学補正・コンフォメーション・ECP・基底関数・参照状態）を単一B項目に統合。v161の個別B項目より構造的かつ優先度が明確
- **C-1（Mårtensson — Dropped Quantitative Benchmark）**: OI-013対応。Mårtensson論文のΔH‡/ΔS‡値が導入部で数値引用されながら結果部での比較が行われない「中断引用」として記録
- **B-13/B-14/B-16/B-18/B-19/B-20（新規B項目群）**: 二分子エントロピーペナルティ参照状態・Br/Cl基質DFT不在・SI溶媒スクリーン未提示・TEA失敗未説明・M検出下限未記載・PPh₃触媒効果のB項目化（v161対応なし）
- **D-4候補数の増加（7→8）**: 候補2（定量的NMR基盤[SRG-2]）・候補7（製品定量整合性）が独立候補として体系化

退行3件のうちR1（速度論的vs熱力学的選択性の独立展開）が最も重要。U項目数の減少（5→2）は
R2（RDS帰属曖昧性のU項目化）に起因するが、v17のU-1/U-2は機構論的問いのより深いレイヤーを
捕捉しており、質的には進歩。

### 正の副次効果

- OI-007 R1（「M not detected」の検出下限問題）がv17 D-4候補3として初作動確認 → OI-007のR1 resolved（comp2）
- OI-013（Dropped Quantitative Benchmark）がcomp2 C-1として作動確認（機構論論文での初出）
- DFT方法論7問題のB-item consolidation（convergence 3/3）がD-4選択基盤を強化
- self-contradictory absence rule が複合証拠型HCS論文（DFT+NMR+HPLC）で有効作動

### 確認された未回復項目

- R1（速度論的vs熱力学的選択性の独立D-4展開）: v17 D-4候補6に吸収。継続注視
- R2（U-4 RDS帰属の曖昧性）: v17 B-17の部分カバーに留まる
- OI-007 R2（20 mol%非実用的触媒負荷量の外挿可能性）: v17でも未作動。引き続きopen

---

---
## Entry 020: v16.1 vs v17 — scr1 (test)

**比較日:** 2026-04-15
**評価論文:** scr1 (Fodor et al., ACS Sustainable Chem. Eng. 2020, 8, 9926–9936) — testset
**モデル:** claude-sonnet-4-6
**評価者:** Sonnet セッション

### 背景

v17はv16.1に対してOI-013（Dropped Quantitative Benchmark C項目明示化）、
C7（OI-004 yield basis mixing例外）、C8（PDF直接読み込み）等を追加した版。
scr1論文（GVL溶媒中のPd触媒Heckカップリング — 触媒・速度論・計算研究）での
v17適用結果。v16.1 scr1出力（Entry 012）との対比。

### 項目数比較

| カテゴリ | v16.1 | v17 |
|----------|-------|-----|
| A | 1 | 0 |
| B | 13 | 23 |
| C | 4 | 4 |
| U | 5 | 5 |

### スコアカード

| ID | 退行ポイント | v16.1 | v17 | 判定 |
|----|---|---|---|---|
| R1 | A-1（塩基補助HI脱離のDFT計算先送り）の捕捉 | A-1として「Future DFT calculations will examine the role of base-assisted H–I elimination」を明示捕捉 | 対応するA項目なし（B-7/B-14に関連内容あるが先送り分類されず） | ⚠️ 部分回復 |
| R2 | D-4候補2（均一触媒前提のD-4化）の捕捉 | D-4候補2「Is the reaction truly homogeneous Pd catalysis?」として独立候補 | 独立D-4候補なし（B-19に言及のみ） | ❌ 未回復 |
| R3 | scope_type判定 | framework_question（均一触媒性の前提問い） | tool_question（GVLがDMA/DMFの代替として機能するか） | 🔄 変化（どちらも論文から支持可能） |

### 総合判定

**v17 ≥ v16.1**

- C-1/C-2（Dropped Quantitative Benchmark: Czernecki ρ値・Amatore/Jutand活性化パラメータ）の
  新規抽出はv16.1に欠落。v17の明確な改善（OI-013対応確認）。
- B-10/U-3の3/3 convergence（sub-unity kinetic orders vs first-order rate law前提）はv17の新規捕捉。
- U-1（GVL-Et₃N速度論汚染のself-contradictory absence）はv17の新規捕捉。
- B-21（Eyringプロット非提示）の独立B項目化はv17の改善。
- SRG-3（DFT環境不整合群）・SRG-6（実験再現性欠如群）はv17の新規グループ。
- R1（A-1塩基補助HI脱離先送り）は中程度の退行。→ OI-022に記録。
- R2（均一触媒前提のD-4候補消失）は中程度の退行。→ OI-010パターン継続。

### v17で確認された正の副次効果

- C-1 Dropped Quantitative Benchmark（Czernecki σ/ρ相関、ref 48）の新規抽出
- C-2 Dropped Quantitative Benchmark（Amatore/Jutandの活性化パラメータ、ref 17）の新規抽出
- B-10/U-3のself-contradictory absence二重分類（sub-unity orders vs rate law前提）
- U-1（GVL-Et₃N副反応の速度論汚染）の新規U項目化
- SRG-2（動速学モデル自己検証体系の不在）として6項目大型グループ化
- ピボット構造の明示化（U-3 ↔ B-10、U-1 ↔ B-5）

### 確認された未回復項目

- R1（A-1 塩基補助HI脱離先送り、⚠️ 部分回復）→ OI-022
- R2（均一触媒前提D-4候補消失、❌ 未回復）→ OI-010（継続中）

## Entry 023: v16.1 vs v17 — hom1 (test)

**比較日:** 2026-04-15
**評価論文:** Wang et al., Chem. Sci. 2020, 11, 11042 (hom1) — testset
**モデル:** claude-sonnet-4-6
**評価者:** Claude Sonnet 4.6 セッション（HOM-1 凍結評価）

### 背景

v17はv16.1に対してC8（PDF直接読み込み）・C1〜C7の各改善を導入した新版。
hom1は凍結評価セットの1本目であり、v17の実質的な最初のtestset評価。

### 項目数の変化（v16.1 → v17）

| カテゴリ | v16.1 | v17 |
|----------|-------|-----|
| A | 3 | 3 |
| B | 10前後 | 17 |
| C | 0 | 3 |
| U | 3 | 3 |

### スコアカード

| ID | 退行ポイント | v16.1 | v17 | 判定 |
|----|---|---|---|---|
| R1 | KIE-準可逆性自己矛盾の明示的テキスト引用 | D-4候補2で"Normally, such a remarkable isotope effect...However, it seemed contradictory..."を直接引用し矛盾を特定 | D-4候補1/4で概念的に捕捉するが当該引用なし | ⚠️ 部分回復 |
| R2 | C2生成物3bのC3位重水素化（Scheme 5a）のD-4候補化 | D-4候補6として独立候補「C2-生成物3bのC3位への重水素取り込み」 | 対応するD-4候補なし（B-6に部分的に含まれるが独立しない） | ❌ 未回復 |
| R3 | critical評価項目の検出（high_convergence_high_gap） | B-3でV3=critical評価あり（temperature_gap=medium） | critical評価ゼロ、high_convergence_high_gap空 | ⚠️ 変化（深刻度スケールの差による可能性） |
| R4 | scope_type判定 | tool_question（リガンドが特定の機構を可能にするか） | framework_question（設計原理）| 🔄 変化（どちらも論文から支持可能） |
| R5 | パラジウムブラック生成の観察との接続 | D-4候補8の key_quote に"palladium black formation was observed"を使用 | B-17に一般言及のみ、D-4候補として接続なし | ⚠️ 部分回復 |

### 総合判定

**v17 ≥ v16.1**

- C項目（C-1 Dropped Quantitative Benchmark, C-2, C-3）の新規抽出はv16.1に完全欠落。v17の明確な改善。
- D-4候補5（スコープ失敗例の機構的帰属問題）・D-4候補8（配位子なし条件での10% C2）はv16.1に存在しない新規候補で質が高い。
- B項目の系統化（17項目、バンドル・統合・ESI delegation check）はv17が大幅優位。
- ピボット構造の明示化（A-2 ↔ B-7、A-3 ↔ B-3）はv17の新機能。
- R2（C2-生成物3bのC3-D）は分析的に重要な退行。→ OI-017に記録。
- R1（KIE-矛盾の引用精度）は部分的退行。D-4候補1/4で概念は到達しているが引用品質が落ちる。

### v17で確認された正の副次効果

- C-1 Dropped Quantitative Benchmark（Scheme 1a, 75% yield, ref 13e）の新規抽出
- C-2/C-3のsymmetric_citations記録（先行文献群の集団的引用退出パターン）
- B-8（最適化条件の3変数同時変化）、B-9（ノルボルネン代理基質）の独立B項目化
- D-4候補8（U-3 self-contradictory absence: 配位子なし10% C2）が論文モデルとの定量的矛盾を新規に記録

### 確認された未回復項目

- R2（C2-生成物3bのC3-D、⚠️ 未回復）→ OI-017

---

## Entry 022: v16.1 vs v17 — het1 (test)

**比較日:** 2026-04-15
**評価論文:** het1 (Yuan et al., J. Am. Chem. Soc. 2018, 140, 8206–8217)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

het1はPd@MOF触媒によるHeckカップリングのオペランドXAS研究。Entry 010（v15 vs v16.1）では
v16.1が大幅改善と評価された。本エントリはv16.1 → v17の変化を評価する。

### 項目数の変化

| カテゴリ | v16.1 | v17 |
|----------|-------|-----|
| A | 3 | 2 |
| B | ~22（推定） | 17 |
| C | ~4 | 3 |
| U | 5 | 4 |
| SRG | ~6 | 6 |
| D-4候補 | 8 | 8 |
| 合計(A+B+C+U) | ~34 | 26 |

### スコアカード

| ID | 退行ポイント | v16.1 | v17 | 判定 |
|----|---|---|---|---|
| R1 | Pd(0)活性種の直接観測不在がD-4候補として独立展開されない | D-4-1「適応的機構の実証的空洞」——「Pd(0)は全時間帯でXAS未検出にもかかわらずPd(0)が活性種と提案される」矛盾を核心展開 | U-1「XASで機構の素反応を限定できるか」という広い問いに吸収。Pd(0)未検出の具体的矛盾が明示されない | ⚠️ medium impact |
| R2 | 不均一性テスト不在（均一系vs不均一系問題）がD-4候補化されない | D-4-2「ホットフィルトレーション・水銀毒化試験の不在」——B-5（参照引用回避）↔C-1のpivot構造で展開、V2=criticalの評価あり | 完全不在（B-16はアニリンモデルの代替性を問うが不均一性の根本問いに至らない） | ⚠️ medium impact |
| R3 | Cl⁻の化学的起源の未特定 | D-4-3「Cl⁻の起源三候補（前触媒由来、ArI酸化的付加由来、不純物）」として独立候補 | D-4候補3「Cl⁻毒化の因果未検証」で部分カバー。起源の特定問いは含まれない | ⚠️ low impact |
| R4 | scope_type判定 | tool_question（XASというツールでPdスペシエーションを追跡できるか） | framework_question（触媒活性種と失活機構の一般原理） | ⚠️ low impact（どちらも論文から支持可能） |

### 総合判定

**v16.1 ≈ v17（R1, R2は実質的損失、v17の新規強化により相殺）**

v17の優位点:
- B-1+B-2（SRG-1、2/3収束・high）: EXAFS系統誤差の除外（B-1）とLCFフィット品質指標の不在（B-2）が独立B項目として記録（v16.1のD-4-4よりEXAFS解析品質問題を体系的にカバー）
- B-3: 単一実験の再現性欠如を独立B項目として捕捉（v16.1対応なし）
- B-7: 逐次昇温プロトコルの混交問題（OI-011で追跡してきたsquential protocol confounding checkが作動確認）
- D-4候補4（SRG-5）: ブランク実験・H₂O閾値・昇温カーブの統合展開（v16.1のD-4-6「非等温加熱ランプ」より広い枠組み）
- A-1 ↔ B-1+B-2ピボット: 定量的根拠の確認不能性と将来課題の連動構造が明示
- D-4候補5（SRG-6）: 定量的性能指標の体系的不在（TON/TOF・表面Pd当たりTOF・単一基質での汎用性主張）の統合展開

### v17で確認された正の副次効果

- OI-011（逐次昇温混交問題）: het2に続きhet1でも作動確認。バッチ/オペランド系でも sequential protocol confounding checkが有効
- self-contradictory absence rule: U-2（ブランク実験）、U-3（Cl⁻因果実験）、U-4（Wacker化学量論）が独立U項目として記録

### 確認された未回復項目

- R1（Pd(0)直接観測不在の独立D-4候補化）→ OI-018（新規）
- R2（不均一性テスト不在のD-4候補化）→ OI-019（新規）

---

## Entry 019: v161 vs v17 — comp1 (test)

**比較日:** 2026-04-15
**評価論文:** comp1 (Race, Faulkner, Shaw, Bower — Chem. Sci. 2016, 7, 1508–1513) — testset
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

comp1はPd触媒によるNarasaka–Heck環化における機構二分岐（電子豊富Pd→イミニルラジカル経路 vs 電子欠乏Pd→aza-Heck経路）を報告するChem. Sci. Edge Article（6ページ）。v161で初回解析済み（Entry 006参照）。v17はOI-007（否定的証拠の検出下限）、OI-008（対照実験の設計上の非対称性）、OI-013（Dropped Quantitative Benchmark）等の改善を組み込んだ版として本セッションで再解析。

### 項目数の変化

| カテゴリ | v161 | v17 |
|----------|------|-----|
| A | 2 | 7 |
| B | 20 | 18 |
| C | 8 | 5 |
| U | 5 | 3 |
| SRG | 7 | 6 |
| D-4候補 | 8 | 8 |
| 合計(A+B+C+U) | 35 | 33 |

### D-4候補の対応関係

| v161候補 | v17候補 | 対応状況 |
|----------|---------|---------|
| D-4-1（SET熱力学的・速度論的根拠の不在） | D-4-2（SET実行可能性の自己矛盾的不在） | ✅ 対応（U-1との二重記帳で構造深化） |
| D-4-2（ラジカルクロック三重問題） | D-4-1（マスバランス体系的不在）+ D-4-8（検出下限） | ⚠️ 部分対応（速度定数較正・NMR帰属角度消失） |
| D-4-3（p-シメン自己矛盾的不在） | D-4-5（p-シメン触媒サイクル副生成物） | ✅ 対応 |
| D-4-4（重水素標識の分析的根拠の不在） | D-4-8（否定的証拠の検出下限） | ✅ 対応（射程が拡大） |
| D-4-5（TEMPOがPd(0)を酸化する代替解釈） | 対応なし | ❌ 欠落 |
| D-4-6（配位子電子性の定量的境界不在） | D-4-6（電子豊富クラス内収率不均一性） | ✅ 対応 |
| D-4-7（エストロン実験の多重的信頼性問題） | 対応なし（B-5・A-3等に分散） | ❌ 欠落 |
| D-4-8（合成標的・目的論的文脈の不在） | D-4-7（既存イミニルラジカル法との定量比較不在） | ✅ 対応 |
| ——— | D-4-3（Pd不要条件対照実験の欠如）【新規】 | ✅ 新規（OI-008対応） |
| ——— | D-4-4（配位子制御主張のマッチドペア問題）【新規】 | ✅ 新規（OI-008対応） |

### スコアカード

| ID | 退行ポイント | v161 | v17 | 判定 |
|----|---|---|---|---|
| R1 | ラジカルクロック実験の三重問題特異性の消失 | D-4-2: (a)速度定数較正未実施（B-12）、(b)25%収率マスバランス欠損（B-4）、(c)NMR帰属詳細欠如（B-18）を三問題統合の高特異性候補として展開 | D-4-1はマスバランス体系的不在（B-3,B-4,B-5,SRG-1）として統合するが、速度定数較正角度（C-5参照）とNMR帰属問題が独立D-4候補として浮上しない | ⚠️ medium impact |
| R2 | TEMPO対照実験の代替解釈（TEMPOがPd(0)を酸化する）の欠落 | D-4-5（grounded_in: B-3, U-3, C-6）として「TEMPO自体がPd(0)を酸化する代替説明が論じられていない」観察が独立候補。U-3がself-contradictory absenceとして寄与 | B-2（TEMPO limitation, methodological_limitation）として記録されているが、D-4候補化されず。v17のU-2はPd-free controlに変更されており、TEMPO-Pd酸化代替解釈がU項目から消失 | ⚠️ medium impact |
| R3 | エストロン実験の多重的信頼性問題の統合的展開欠落 | D-4-7（grounded_in: B-5, B-13, U-5）として「(1)ストイキオメトリックPd、(2)β-開裂と水素引き抜きの速度論的競合未分析、(3)後処理エピメリ化の未排除」の三問題統合候補 | B-5（エストロン反応のPd負荷量）、A-3（後処理エピメリ化の先送り）として部分的に記録されているが、統合されたD-4候補として展開されず | ⚠️ low-medium impact |

### 総合判定

**v17 > v161**

v17の優位点:
- **D-4-3（Pd不要条件対照実験の欠如）**: v161では U-3（TEMPO-Pd酸化）が類似問題を扱っていたが、Pd触媒必須性を直接試験する実験の欠如というD-4候補はv161に不在。OI-008の問いに部分対応。
- **D-4-4（マッチドペアコントロール問題）**: 「solely by choice of phosphine ligand」という主張と実際の多変数差異（温度・Pd源・基質・溶媒添加剤の同時変化）の矛盾を独立D-4候補として展開。OI-008に直接対応。v161にはB-6として部分的記録があったが、D-4候補化されていなかった。
- **D-4-8（否定的証拠の検出下限）**: 「観測されなかった」という否定的証拠（β-ヒドリド脱離生成物不在、TEMPO付加体不在、重水素取り込み<10%）の証拠価値問題がD-4候補として独立。OI-007対応。
- **A項目の体系化（2→7）**: A-3（後処理エピメリ化）、A-4（Scheme 5未検証ステップ）、A-5（環化vs再結合速度論）、A-6（LFER/Hammett）、A-7（N-Pd BDE）が先送り分類として新規捕捉。timing_pressure分析の精度向上。
- **D-4-2（SET自己矛盾的不在）**: v161 D-4-1の「SET熱力学的根拠不在」からU-1（自己矛盾的不在）との二重記帳に昇格し、論証構造が深化。

退行3件のうちR1（ラジカルクロック三重問題の特異性）とR2（TEMPO代替解釈）がmedium impact。いずれもv161が持つ特定の化学的角度をv17が体系的カテゴリに吸収した結果として生じた退行。

### 正の副次効果

- OI-007（否定的証拠の検出下限）がcomp1のD-4-8として作動確認（Murai devsetに続き2例目。comp2発端論文での確認は初）
- OI-008（対照実験の設計上の非対称性）がcomp1のD-4-4として直接展開。v17で同一論文（OI-008の発端論文）において解決確認
- self-contradictory absence ruleがB-10↔U-1（酸化還元電位）・U-2（Pd-free control）・U-3（p-シメン）で有効作動
- A項目の体系化（2→7）によりdeferral typeの多様性（deferred/forgotten/mixed）が明示化され、timing_pressureおよびpriority_structure分析の精度が向上

### 確認された未回復項目

- R1（ラジカルクロック速度定数較正角度）: C-5として文献記録があるがD-4候補化なし → OI-007の備考に追記（検出下限問題の亜種）
- R2（TEMPO-Pd酸化代替解釈）: comp1特有の問題として未追跡。low impact単一論文のため新規OI不要


---

## Entry 021: v16.1 vs v17 — scr2 (test)

**比較日:** 2026-04-15
**評価論文:** scr2 (Templ, Hwang, Schwemin, Baltaci, Borchardt — RSC Mechanochem. 2025, 2, 598–602)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

scr2はPdミリングボールを触媒源とする直接メカノ触媒Heck反応を報告する5ページのRSC
Mechanochem短報（2025年）。無溶媒・不活性雰囲気不要・ケモ選択性（C(sp²)–I優先）・
one-pot Wittig/Heck連続反応を特徴とする。v16.1では初回解析済み（Entry 011: v15 vs v16.1
比較で v16.1 > v15 と評価）。本エントリはv16.1 → v17の変化を評価する。

### 項目数の変化

| カテゴリ | v16.1 | v17 |
|----------|-------|-----|
| A | 10 | 1 |
| B | 5 | 27 |
| C | 5 | 3 |
| U | 5 | 4 |
| SRG | 4 | 6 |
| D-4候補 | 6 | 8 |
| 合計(A+B+C+U) | 25 | 35 |

### スコアカード

| ID | 退行ポイント | v16.1 | v17 | 判定 |
|----|---|---|---|---|
| R1 | ArF過剰主張の不検出 | B-3「Conclusionsに "C(sp²)–X bonds (X=F, Cl, Br) intact" と記述されるが、ArF基質の純粋実験なし。F付加体の不在が検証されていない」として独立B項目（V1=medium） | 対応する項目なし。C(sp²)–F非反応性は複数B項目（B-4等）で周辺的に触れられるが、Conclusions記述と実験事実の乖離という修辞的緊張がD-4候補化されず | ⚠️ medium |
| R2 | series_signal検出 | yes [T2]: Suzuki→Sonogashira→Heck の直接メカノ触媒論文群の計画シリーズ検出 | no。将来展開の言語的指示なしと判定 | ⚠️ low |
| R3 | v16.1固有U項目（ArBr残存誘導体化・TEA塩基効果）の未回復 | U-3（ArBr残存の誘導体化未実施）、U-5（TEA塩基の量的効果・K₂CO₃との等価性未検証）として独立記録 | 対応項目なし（周辺的な問いとして他B項目内に分散または欠落） | ⚠️ low |

### 総合判定

**v17 > v16.1**

v17の優位点:
- **A/B境界ルールの適正化（A: 10→1, B: 5→27）**: v16.1はA-1〜A-10（10項目）を生成し、
  この論文の実験的限界の大部分を「将来課題への委任」として分類していた。v17はA vs B
  境界ルールを厳密に適用し、論文が明示的に先送りした唯一の問い（A-1: "further mechanistic
  studies are needed"）のみをA分類。残り全てをB項目（この実験内の痕跡）として正確に分類。
  この変換はUQSプロトコルの意図に忠実であり、明確な改善。
- **self-contradictory absence ruleの多重作動（U-1, U-2, U-4）**: U-1（浸出実験の
  閾値不在）、U-2（hot filtration/mercury test未実施：表面触媒主張の標準的検証不在）、
  U-4（リサイクル可能性の主張にデータなし）の3件で自己矛盾的不在が独立記録。
  各U項目は対応するB項目（B-1, B-9, B-8）と二重記帳。
- **B-23（1h vs 2h反応時間の内部矛盾）**: 最適化TableとスコープTable間の時間条件不一致を
  v16.1が完全に見落としていたのに対し、v17で独立B項目として新規捕捉。
- **C-1 Dropped Quantitative Benchmark（refs 7-10）**: OI-013対応として、先行メカノ化学的
  Heckプロトコル（refs 7-10）が導入部に収率数値付きで引用されながら結果部で直接比較され
  ないパターンを正確に記録。OI-013の解決をscr2で実証。
- **OI-012の確認**: B-1が "not mainly" 修飾語を正確に捕捉し、ESI委任と実験不在を混同
  しない。v16.1はA-5（deferred_to_ESI）という別経路で捕捉していたが、v17はB+U二重記帳
  （B-1 + U-1）として構造的に整理。OI-012の解決を実証。
- **SRG体系化（4→6グループ）**: 各グループとD-4候補の対応が追跡しやすくなった。
- **D-4候補の充実（6→8）**: D-4-1（表面触媒検証可能性、3/3収束最優先）、D-4-3
  （リサイクル主張 vs 証拠ギャップ）、D-4-5（one-pot Wittig/Heck黒箱問題）等が新規。

退行3件のうちR1（medium）のみ実質的な分析損失。R2・R3はlowかつv17の全体的改善に
対して限定的影響。

### v17で確認された正の副次効果

- **A/B境界ルール**: 5ページの短報でも「将来課題型」と「この実験内の限界型」の
  厳密な区別が機能し、9項目分の分類が適正化された（v16.1のA-10項目中9項目がB再分類）。
- **yield basis mixing exception（B-7）**: NMR収率（dibromomethane内標準）vs 単離収率の
  混在を独立B項目として正確に保持（統合ルール例外として明示）。
- **ピボット構造（A-1 ↔ B-1, A-1 ↔ B-16）**: 機構研究の先送りが表面触媒主張の
  定量的根拠不在を隠蔽する構造的依存関係を明示。
- OI-012（ESI委任 vs 実験不在の区別）・OI-013（Dropped Quantitative Benchmark）の
  両者がscr2 v17で実証的に確認（ステータス → resolved）。

### 確認された未回復項目

- R1（ArF過剰主張: Conclusions記述と実験事実の乖離がB項目化・D-4候補化されない）→ OI-023（新規）
- R2（series_signal no判定）: 低影響。継続追跡。

---

## Entry 024: v161 vs v17 — hom2 (test)

**比較日:** 2026-04-15
**評価論文:** hom2 (Shirai, Sugino, Nakao — J. Org. Chem. 2024, 89, 3840–3847, Note) — testset（凍結評価セット2本目）
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

hom2はPd(OAc)₂/CsF/PMHSを用いたAQ配向型還元的Heckヒドロアリール化の室温条件確立を報告するJ. Org. Chem. Note（7ページ）。v161で初回解析済み（hom2_v161_sonnet_s2.md）。v17はOI-013（Dropped Quantitative Benchmark）、OI-004（yield basis mixing）等を組み込んだ改善版として本セッションで再解析。なお、Table 1にASAP掲載時の事後訂正（2024年2月6日）があり、v17はこれをB-6として独立記録した。

### 項目数の変化（v161 → v17）

| カテゴリ | v161 | v17 |
|----------|------|-----|
| A | 2 | 4 |
| B | 7 | 14 |
| C | 4 | 4 |
| U | 4 | 3 |
| SRG | 3 | 8 |
| D-4候補 | 6 | 7 |
| 合計(A+B+C+U) | 17 | 25 |

### スコアカード

| ID | 退行ポイント | v161 | v17 | 判定 |
|----|---|---|---|---|
| R1 | AQ配向基の「無コスト化」——医薬品合成への応用で必要なAQ導入・除去ステップが問われていない | D-4候補4として独立展開「全基質がAQ二座配位型アミドであり、FDA医薬品（サクビトリル、ベナゼプリル等）への応用にはAQ導入・除去ステップが加算される。この合成的コストが問われていない」（grounded_in: A-2, B-6, C-3, C-4） | A-2（AQ除去言及の抑圧）、B-11（AQ基質コスト）でカバーするが、「製薬合成の実質的ステップ数」という統合的D-4候補として独立しない | ⚠️ medium impact |
| R2 | 「室温」が不可欠であることの未証明——「室温でも反応する」と「室温でなければならない」は別の命題 | D-4候補5として独立展開「50〜80 °Cでの同条件試験が一点もなく、室温という条件の化学選択性への役割が実験的に未検証」（grounded_in: B-4, B-5, C-2） | B-5（比較主張の根拠欠如）、B-10（ArI限定の未言及）でカバーするが、「温度を独立変数として扱う実験の欠如」というD-4候補として独立しない | ⚠️ low impact |

### 総合判定

**v17 > v161**

v17の優位点:
- **D-4候補1（双触媒サイクルの自己矛盾的不在）**: v161では U-2/U-3/U-4 に分散していた問題を統合し、「遅い添加条件でのみ重水素実験を実施し、速い添加条件（副サイクル優勢）でのγ/δ取り込み比変化が存在しない」という具体的かつ内部一貫した自己矛盾的不在としてD-4候補1を構成。grounded_in: A-1, U-1, U-2, B-8。v161候補2（触媒サイクルの「演じられた確実性」）より実験的に検証可能な形で定式化。
- **D-4候補3（NMR内部標準の信頼性）**: ジベンジルエーテルがPd(OAc)₂/PMHS存在下で安定かを示す対照実験の欠如を独立D-4候補として記録。v161に完全不在だった新規角度。B-3（単回NMR収率への全依存）、B-6（Table 1事後訂正）と組み合わせるとデータ信頼性の三重問題として展開可能。
- **D-4候補7（触媒ターンオーバーとPd失活の未検討）**: 遅い添加（Si-H供給制限）がPd(II)→Pd(0)還元速度をも制限するため生産的ターンオーバーが損なわれている可能性。10 mol% Pd使用にもかかわらずTON未報告という問いを独立候補化。v161では言及なし。
- **B項目の大幅充実（7→14）**: B-8（PMHS増量条件での副生成物収率欠如）、B-9（基質選択バイアス）、B-10（ArI限定の未言及）、B-11（AQ基質コスト）、B-12（スコープ失敗例未開示）、B-13（PMHS遅い添加の機構的根拠欠如）、B-14（添加時間データ未報告）が新規独立B項目として体系化。
- **SRG粒度の向上（3→8）**: SRG-1〜SRG-8として各問題群の共有根拠が明示化され、D-4候補選択の構造的根拠が追跡可能になった。
- **C-2/C-3（Dropped Quantitative Benchmark）**: Wu/Loh 2018（ref 16）の収率範囲引用が結果部での直接比較につながらないパターンをOI-013対応として記録。v161のC-1〜C-4は存在したが「数値ベンチマーク中断」の明示的記録は弱かった。
- **A-1↔B-7主ピボット**: 双触媒サイクルモデルの根拠とされる重水素実験（B-7）の方法論的脆弱性が、機構解明の先送り（A-1）によって保護される構造として明示化。priority_structureで三つのピボット関係（A-1↔B-7、A-4↔B-7、B-3↔B-6）を記述。

退行2件のうちR1（AQ合成コスト角度）がより重要。AQを用いた製薬合成における配向基導入・除去のステップコストは論文の「laboratory-scale and industrial synthesis」主張の核心に関わり、v17はA-2・B-11で断片的に触れるのみでD-4候補として統合されていない。

### 正の副次効果

- self-contradictory absence rule（U-1, U-2）が還元的Heck論文で有効に作動し、「遅い添加条件でのみ機構証拠を提示し、速い添加（副サイクル優勢）での検証が存在しない」という内部矛盾を明示化
- B-3↔B-6のデータ基盤ピボット（単回NMR収率 × Table 1事後訂正）がD-4候補3に接続し、定量的信頼性問題を多層的に記録

### 確認された未回復項目

- R1（AQ配向基コストのD-4候補独立化）: AQ二座配位型アミド基質の導入・除去コストを「industrial synthesis utility主張」と接続した統合的問いがv17では未形成 → OI-021（新規）
- R2（室温の必要性検証の欠如）: severity=low、B-5・B-10との重複が大きく、独立追跡の実益は限定的のため新規OI不要

---

## Entry 026: v17 vs v18 — Kumada (devset)

**比較日:** 2026-04-25
**評価論文:** Kumada (Tamao, Sumitani, Kumada, JACS 1972) — devset
**モデル:** claude-sonnet-4-6

### スコアカード

| ID | 退行ポイント | v17 | v18 | 判定 |
|----|---|---|---|---|
| R1 | Table I収率データの解釈可能性候補（D4-3相当） | 独立D-4候補（「方法は機能する証明 vs 合成計画用途」の区別） | SRG-3に分散、統合洞察なし | ⚠️ 部分回復 |
| R2 | 目的論的接続候補（D4-7相当） | 独立D-4候補（「何のための手段か」） | 対応候補なし | ⚠️ 未回復 |
| R3 | institutional visibility（同号Kiso論文との協調掲載指摘） | D-2に明示 | 一般的記述のみ | minor |

### 総合判定

**v18 > v17**

主要改善（v18の優位点）:
1. **high_convergence_high_gap検出**: v18でB-10がhigh_convergence_high_gap（V1=medium, V2=critical → temperature_gap=medium）として検出。v17ではフォールバック規則を適用（high_convergence_high_gap: none）。これによりD-4の最優先候補がNi酸化状態問題（触媒の実体）に正しく設定された。
2. **scope_type修正**: v17 tool_question → v18 framework_question。"Can a nickel-diphosphine complex enable..."（特定ツールへの問い）から"What structural features enable..."（設計原理への問い）へ。
3. **U-4の独立分類**: 速度論/熱力学の区別が中心主張（「selective」）に直接紐付けられた独立U項目として抽出。v17ではD4-5としてA-1（立体化学）に紐付けられており、primary selectivity claimとの接続が弱かった。
4. **選択性候補の統合**: v17 D4-1 + D4-5の2エントリがv18 Candidate 2（SRG-1ベース）に統合され、「定量的空洞」と「機構的根拠の不在」が同一候補内で記述された。

### v18で確認された正の副次効果

- TEMPERATURE_SUMMARY の high_convergence_high_gap が初めて有効活用され、D-4選択アルゴリズムが改善を実証
- B-10の B↔U 二重記帳（B-10 ↔ U-2）がlinked_itemsに明示化
- SRG-2（触媒サイクル根拠不在）が候補1・5・U-3をカバーし、機構的問題の構造が整理された

### 確認された未回復項目・新規懸案

- R1: Table I収率データの解釈可能性（「方法の存在証明 vs 合成計画用途」の区別）→ open_issues OI-024
- R2: 目的論的接続の不在候補 → open_issues OI-025

---

## Entry 027: v17 vs v18 — binkley1979 (nakanishi/19, test)

**比較日:** 2026-04-25
**評価論文:** Binkley et al. (Pople, Krishnan, Schlegel, Binkley, Int. J. Quantum Chem. Symp. 13, 225–241, 1979) — nakanishi/19
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

binkley1979はHF+MP2解析エネルギー微分の定式化・実装・エチレン応用を報告する計算量子化学方法論論文。v17で初回解析済み（s3v2まで実施）。v18ではs3v3まで実施（Stage 3プロンプトも更新）。v18の主要変更点：PRI-12正式昇格・二階層定義追加（v18 C2）、RI-06判定注記追加、RI-09分割提示構造対応（v18 C5）、Self-referential validationチェック追加（v18 C8）。

### 項目数の変化

| カテゴリ | v17 | v18 |
|----------|-----|-----|
| A | 2 | 2 |
| B | 8 | 8 |
| C | 4 | 4 |
| U | 3 | 2 |
| SRG | 5 | 4 |
| D-4候補 | 7 | 5 |
| 合計(A+B+C+U) | 17 | 16 |

### スコアカード

| ID | 退行ポイント | v17 | v18 | 判定 |
|----|---|---|---|---|
| R1 | D4-1（幾何効果 vs 電子相関効果の未分離）の消失 | D-4候補1として独立展開。r_CC差（1.317 vs 1.335 Å）に対する「クロス幾何計算の不在」として grounded_in B-1, B-2 で展開 | V2-Q4として記録（B-5関連）、D-4候補に昇格せず | ⚠️ medium |
| R2 | D4-5（スケーリングHFとの定量精度比較の欠落）の独立候補化 | 独立D-4候補5として「Pulay-Meyer 10%/20%スケーリングをTable Iに適用した場合の振動数が示されない」として展開 | 候補4（有限差分法との非較量比較）に一部吸収されたが、「スケーリングHFとの精度比較」という固有の問いは残らず | ⚠️ low-medium |
| R3 | D4-7（IR強度・ラマン活性の不在）の消失 | 解析微分の枠組みから双極子微分が同一コストで得られる点を独立D-4候補7として展開 | 対応なし | ⚠️ low |

### 総合判定

**v17 ≈ v18（実質同等、分析焦点が異なる）**

v18の優位点:
- **候補2（非調和補正の操作的不透明性）**: v17ではD4-2の「70%要約」の文脈で言及されたが、v18では「実験比較の根拠が検証不可能」として独立候補化し、C-4（Duncan et al.の手法不記述）との連動も明示化。
- **候補5（Ref [28] 未公刊による再現性障壁）**: v17のD4-4（実装正当性の独立検証不在）より「再現性の構造的障壁」として焦点が明確化。SRG-2として独立グループ化。
- **Stage 3 PRI-12チェック**: v18ではSelf-referential validationチェック（v18 C8）とDeductive-retrospective structureチェック（v18 C4）の両方を実施。Mild A5（Multi-layer approximation stacking）として記録。v17 s3v2では相当するチェックなし。
- **VQ判定の明確化**: v17は現在のVQ水準の判断記述が不明確（当時プロンプト未整備）。v18ではVQ-2(Method)条件付き通過・VQ-3未達（RI-04 Fatal）の根拠が明示化。

退行3件中R1（幾何効果分離）がmedium impactで最も注目。R2（スケーリング比較）はv18候補4に部分吸収。R3（IR強度）はlow影響。

### 正の副次効果

- Self-referential validation チェックがbinkley1979（計算化学方法論論文）に適用され、PRI-12-A5（Mild）として判定される基準点が確立した
- RI-04 + RI-09の共起パターン（§6）が制度設計知見として記録された
- VQ-2条件付き通過・VQ-3 Fatal（RI-04）の判定が計算化学方法論論文の典型VQプロファイルとして確立した

### 確認された未回復項目・新規懸案

- R1: 幾何効果分離問題（HF/MP2の異なる平衡幾何からの周波数比較）がv18でD-4候補に昇格しない → open_issues OI-026

---

## Entry 028: v17 vs v18 — woodward1965 (nakanishi/13, test)

**比較日:** 2026-04-25
**評価論文:** Woodward & Hoffmann (JACS, 87, 395–397, 1965) — nakanishi/13
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

woodward1965は電子環状反応の立体化学則（Woodward–Hoffmann則の原型）を報告する2ページの
JACS Communication。v17で初回解析済み（S2まで）。v18ではS2+S3v3を実施。
v18の主要変更点：PRI-12正式昇格・二階層定義追加（Cluster A自己言及的検証、Cluster B演繹遡及的構造）、
B項目分類の精緻化、U項目（falsifiability）の優先昇格。

### 項目数の変化

| カテゴリ | v17 | v18 |
|----------|-----|-----|
| A | 2 | 2 |
| B | 5 | 9 |
| C | 6 | 3 |
| U | 3 | 4 |
| SRG | 5 | 6 |
| D-4候補 | 7+1(cannot-ask) | 6+1(cannot-ask) |
| GAP | 5 | 5 |
| 合計(A+B+C+U) | 16 | 18 |

### スコアカード

| ID | 退行ポイント | v17 | v18 | 判定 |
|----|---|---|---|---|
| R1 | C項目の粒度（6→3）：C-4/C-5/C-6の消失 | C-4（Havinga光化学引用群）、C-5（Oosterhoff独立項目）、C-6（Criegee & Furrer XVI活性化データ）を独立C項目として分析 | C-3項目に削減。XVI活性化エネルギーデータ（C-6）・Oosteroffとの概念的差異（C-5）・光化学実験的支持の粒度（C-4）が独立分析されない | ⚠️ medium |
| R2 | D-4-6（奇電子系・荷電系の独立理論的根拠の不在）の消失 | 独立D-4候補6として「シクロプロピルカチオン・ラジカル・アニオンのTable I予測が電子計数類推のみに基づき独立MO解析なし」として展開（SRG-5） | 対応する独立D-4候補なし（一部Candidate 2に吸収されるが展開なし） | ⚠️ medium |
| R3 | D-4-4（EHT幾何学サンプリング不透明性）の独立性低下 | 独立D-4候補4として「α角の範囲・ステップサイズ未記載、α=117°逆転点の再現性不明」として具体的に展開（B-2, B-4, SRG-2） | Candidate 2（EH定量性・循環性）に吸収。幾何サンプリング固有の問い（α角範囲・逆転点のロバスト性）が独立候補として示されない | ⚠️ low-medium |

### 総合判定

**v18 > v17**

v18の優位点:
- **B項目の拡充（5→9）**: B-6（XVI協奏性未確立）、B-7（HOMOが末端原子のみ記述）、
  B-8（非対称基質の二モード）、B-9（カルシフェロール系の複雑性）が独立B項目として捕捉された。
  特にB-6（XVI concertedness）はV2で重要指摘されながらv17では独立B項目化されていなかった。
- **U-1（反証可能性の構造的欠如）の優先昇格**: v18ではlow_convergence_high_gap（V3=critical）
  として最優先D-4候補1に接続。v17のU-1相当（遡及確認の認識論的問い）より明確にfalsifiability
  の枠組みで整理された。
- **D-4 Candidate 5（非対称基質・二モード問題）**: v18で新規。SRG-6として独立グループ化。
  HOMO-対称性則の操作的適用範囲における重要な欠落を初めて独立候補化。
- **D-4 Candidate 6（Lewis & Steiner識別実験不在）**: v18で新規。競合的仮説との識別テストが
  一度も行われていないことをD-4として明示的に問題化（U-2のD-4接続を確立）。
- **D-2 format_exploitationの精緻化**: B-1・B-5・B-3をJACS通信フォーマットの圧縮と
  明示的に連動させた分析がv18で追加。
- **D-4 pivot構造の明確化**: A-2↔B-1、U-3↔B-1、A-1↔B-9の三つのピボット関係を
  明示化し、「定量証拠の後回し」という構造読解がより精密化。

退行3件中R1（C項目粒度）がmedium impactで最も注目。
R2（奇電子系理論根拠）はmedium・単一候補消失。R3（幾何サンプリング）はlow-medium。

### 正の副次効果

- Stage 3 v3でPRI-12 Cluster A（A1, A3）とCluster B（B2, B3, B5）の両クラスターが
  初の歴史的創始論文（1965年JACS Communication）に対して適用され、
  典型例として確立した
- VQ-2未達（RI-07 Fatal dual + RI-05 Fatal）のVQプロファイルが
  「実験的証拠が遡及的で全て既知事例の場合」の典型として記録された
- 脚注脱出条項（footnote-escape clause structure）とfield-delegation構造が
  新パターンとしてS3で識別された

### 確認された未回復項目・新規懸案

- R1: C-5（Oosterhoff）のD-4-7固有展開（「概念的差異の未明確化」）がv18でcannot-ask
  カテゴリに移動し分析深度が低下 → 再評価トリガー: 次の歴史的理論論文への適用時
- R2: 奇電子系・荷電系Table I予測の独立MO解析不在がv18でD-4候補に昇格しない → open_issues OI-027

---

## Entry 029: v17 vs v18 — nakanishi2025 (nakanishi/7, test)

**比較日:** 2026-04-25
**評価論文:** Nakanishi, Tsutsumi, Ono, Sada, Taketsugu — J. Comput. Chem. 2025, 46:e70101 (nakanishi/7)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

nakanishi2025はNRO（Natural Reaction Orbital）法を反応経路分岐に初めて適用し、
ベックマン転位の10置換基について分岐点でのλ_R/λ_Fを計算・ユカワ-ツノ相関と照合した論文。
v17で初回解析済み（S0〜S2）。v18でS0〜S3v3を再実施。
v18の主要変更点：PRI-12正式昇格（Cluster A自己言及的検証、Cluster B演繹遡及的構造）、
Stage 3 v3プロンプト（Self-referential validationチェック追加）、
S1 Turn 4のA/B/U境界ルール精緻化。

### 項目数の変化

| カテゴリ | v17 | v18 |
|----------|-----|-----|
| A | 2 | 1 |
| B | 6 | 11 |
| C | 7 | 3 |
| U | 5 | 3 |
| SRG | 6 | 5 |
| D-4候補 | 8 | 8 |
| 合計(A+B+C+U) | 20 | 18 |

### D-4候補の対応関係

| v17候補 | v18候補 | 対応状況 |
|---------|---------|---------|
| D4-1（λ_R/λ_F: 予測子か記述子か） | 候補2（軌道混合の大きさは分岐確率と何の関係があるか） | ✅ 対応（形式変更） |
| D4-2（LFER統計的不完全性） | 候補4（ユカワ-ツノ相関の統計的根拠） | ✅ 対応 |
| D4-3（NRO再現性とIOp非公開オプション） | 対応なし | ⚠️ 消失 |
| D4-4（気相計算と溶液相の乖離） | 候補6（計算モデルと実験的Beckmann転位の乖離） | ✅ 対応 |
| D4-5（λ_R/λ_F = 1.0閾値の信頼性） | 候補3（p-Me外れ値が示す記述子の適用限界） | ✅ 対応 |
| D4-6（ROET/IBO/NPOとの比較なき競合主張） | 候補7（NROはROET・IBOと同一事象を同定するか） | ✅ 対応 |
| D4-7（一般化の根拠不在） | 候補8（記述子の汎化） | ✅ 対応 |
| D4-8（計算レベル依存性） | 対応なし | ⚠️ 消失 |
| ——— | 候補1（λ_R/λ_Fは「生成物分布の予測」を実現しているか）【新規・核心】 | ✅ 新規 |
| ——— | 候補5（p-OMe のVRT不在と概念的不整合）【新規】 | ✅ 新規 |

### スコアカード

| ID | 退行ポイント | v17 | v18 | 判定 |
|----|---|---|---|---|
| R1 | A-2（酵素・有機反応への一般化, forgotten）の消失 | A-2として独立記録（linked_to: U-3, C-2; convergence=2/3） | 対応するA項目なし。内容はB-4（no validation against product distributions）とC-3（refs 13–15 symmetric）に部分分散 | ⚠️ medium |
| R2 | U-4（λ_R/λ_F = 1.0閾値の数値的信頼性）およびU-5（λ値の分子間比較可能性）の消失 | U-4（p-Meとm,m′-Me₂の境界事例からの閾値不確実性, high）、U-5（λ値の無次元性・規格化問題, high）として独立記録 | 両者ともU項目として記録されず。U-4相当内容はB-5（regression statistics）に、U-5相当はB-5/B-9（selection bias）に部分的に吸収 | ⚠️ medium |
| R3 | D4-3（NRO法のIOp非公開オプションと再現性障壁）の独立D-4候補化 | 独立D-4候補3「IOp(10/21=1)は非公開オプション、ゲージ不変性未証明」として grounded_in U-1, B-3 で展開 | 対応するD-4候補なし。IOp問題はB-3（IRC parameters reporting_omission）に部分的に記録されるが、NRO再現性・ゲージ不変性という問いとして独立展開されない | ⚠️ low-medium |

### 総合判定

**v18 > v17**

v18の優位点:
1. **U-1（自己矛盾的不在, critical）の確立**: v18ではλ_R/λ_Fが「生成物分布を予測する」と
   主張しながら生成物分布（転位:断片化比率）を検証標的として一度も使用していないという
   self-contradictory absenceがU-1として明示的に記録（v17にはこの種の明示的U項目なし）。
   これがSRG-1 {B-4, U-1, C-1}を形成し、D-4候補1の核心となった。
2. **C-1のDropped Quantitative Benchmark化**: v17のC-1はrefs 4–7（分岐理論基礎引用）だったが、
   v18のC-1はrefs 23–24（AIMD動的分岐統計を含む可能性が高い先行文献）のDropped Quantitative
   Benchmarkとして診断的に記録。これにより不在データの種類と所在が明確化した。
3. **B項目の系統化（6→11）**: B-7（E/Z立体化学不特定）、B-8（分岐点定義の二重基準）、
   B-9（後付け選択バイアス）、B-10（気相モデル）、B-11（ROET/IBO比較, intentional_narrowing）
   が新規B項目として独立記録。
4. **A-1収束率向上**: p-Meの抑圧（A-1）がconvergence=2/3（v17）→3/3（v18）に上昇。
5. **D-4候補1の構造的明示**: v17では D-4として「気相計算と溶液相の乖離」「LFER統計的不完全性」
   が並列だったが、v18では「λ_R/λ_Fは生成物分布を予測すると主張しながら生成物分布で
   検証していない」という一点が第一候補として核心化し、他の候補がこれを補強する形に整理された。
6. **Stage 3 PRI-12適用（v18 s3v3）**: Self-referential validationチェックが機能し、
   PRI-12/A1（Descriptor-Causality overclaim）・A2（Post-hoc surrogate validation）を正確に
   分類。VQ-2条件付き通過・VQ-3未達（RI-03/RI-04 Fatal + PRI-12/A1·A2 Fatal）の判定が
   NRO型計算化学新手法論文の典型VQプロファイルとして確立した。

退行3件中R1・R2がmedium impact。R3はlow-medium。
R2（U-4/U-5の消失）は「数値的指標の比較可能性問題」として独立したU項目記録の価値があり、
プロンプトレベルの対応を要する可能性がある（→ OI-028）。

### 正の副次効果

- PRI-12/A1（Descriptor-Causality overclaim）がNRO型論文の代表ケースとして確立した
- SRG-1 {B-4, U-1, C-1}が「記述子の検証標的不在」パターンの構造テンプレートとなった
- C-1 Dropped Quantitative Benchmark（refs 23–24の動的分岐統計）がcomputational chemistry
  論文でのパターンとして確認された
- U-1 ↔ B-4のピボット構造（「予測主張」と「予測標的への比較不在」）が明示化された

### 確認された未回復項目・新規懸案

- R1（A-2: 酵素/一般化への言及の forgotten分類消失）→ 再評価トリガー: 「序論で動機として
  挙げながら本文で一度も戻らない」型の forgotten検出条件をプロンプトで確認
- R2（U-4/U-5: 数値指標の閾値信頼性・比較可能性のU項目消失）→ open_issues OI-028
- R3（D4-3: NRO/IOp再現性候補の消失）→ 再評価トリガー: IOp等の非公開オプションを
  用いた計算化学新手法論文への次回適用時

---

## Entry 030: v17 vs v18 — gerrat1968 (nakanishi/18, test)

**比較日:** 2026-04-25
**評価論文:** Gerratt, Mills — J. Chem. Phys. 1968, 49, 1719–1729 (gerrat1968)
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

gerrat1968はPerturbed Hartree-Fock（PHF）法による力定数・双極子モーメント微分の
解析的計算を定式化した理論論文（Paper I）。Paper II（J.Chem.Phys. 48, 1730, 1968）に
全数値結果を委譲する分割提示構造を持つ。v17で初回解析済み（S0〜S2）。
v18でS0〜S3v3を再実施。v18の主要変更点：RI-09分割提示拡張（C5）、PRI-12正式昇格
（Cluster B演繹遡及的構造, B2/B4）、Stage 3 v3（PRI-12正式昇格 + Layer VQ非対称性
パターン + series-presentation resolvedパターン）。

### 項目数の変化

| カテゴリ | v17 | v18 |
|----------|-----|-----|
| A | 2 | 2 |
| B | 6 | 6 |
| C | 4 | 4 |
| U | 2 | 2 |
| SRG | 3 | 3 |
| D-4候補 | 7 | 5 |
| 合計(A+B+C+U) | 14 | 14 |

### D-4候補の対応関係

| v17候補 | v18候補 | 対応状況 |
|---------|---------|---------|
| D4-1（分割提示構造が精度主張を実証から隔離） | 候補1（同） | ✅ 対応 |
| D4-2（εの未定量化による精度主張の操作的空虚性） | 候補2（同, 緩和項問題含む） | ✅ 対応（強化） |
| D4-3（PHF線形方程式の収束保証欠如） | 候補3（同） | ✅ 対応 |
| D4-4（PHFと状態和法の計算量対比の未定量化） | 対応なし | ⚠️ 消失 |
| D4-5（Mills 1957との比較省略） | 対応なし | ⚠️ 消失（低priority） |
| D4-6（閉殻制限と開殻系への拡張未言及） | 対応なし | ⚠️ 消失（低priority） |
| ——— | 候補4（Stanton定理の移動基底問題）【新規・CLA-1から昇格】 | ✅ 新規 |
| ——— | 候補5（BOP誤差と電子相関誤差の未分離）【新規】 | ✅ 新規 |

### スコアカード

| ID | 退行ポイント | v17 | v18 | 判定 |
|----|---|---|---|---|
| R1 | D4-4（PHFと状態和法Eq.13の計算量対比）の独立D-4候補化の消失 | D4-4「状態和法の明示的N乗スケーリングとPHFの線形スケーリングの対比が定量化されない」としてB-6（continuum, convergence 2/3）と接続してD-4候補として記録 | 対応するD-4候補なし。B-6（continuum contribution to infinite sum）はSRG-3に吸収されているが、「PHF vs 状態和法の計算量優位の未定量化」という問いとして独立展開されない | ⚠️ medium |
| R2 | D4-5（Mills 1957との比較省略）の消失 | D4-5「Mills(1957)のcurve-fitting精度がTable IIのHF vs 実験比較と照合された場合、PHFの優位性は自明か」として記録 | 対応なし。v18ではGoodisman/McLeanとの比較はD-2で言及されるが、Mills 1957固有の問いとして独立展開されない | ⚠️ low |
| R3 | D4-6（閉殻制限と開殻系への拡張未言及）の消失 | D4-6「PHF理論は閉殻SCF-MO関数を前提としているが（Section IV冒頭）、Table II–IVのH₂・LiH・HF・HClはすべて閉殻系。開殻系（ラジカル、励起状態）へのPHF適用可能性が未言及」として記録 | 対応なし。v18のA-1（polyatomic extensionの先送り）は軽く言及するが、開殻系の制限として独立記録されない | ⚠️ low |

### 総合判定

**v18 > v17**

v18の優位点:
1. **CLA-1（Stanton定理）の新規D-4候補化**: v17ではC-1（引用切断）として記録のみだったが、
   v18ではB-4（reporting_omission）→D-4候補4（Stanton定理の移動基底問題）として独立展開。
   移動基底条件下でのHellmann–Feynman定理の成立条件という問いが明示化された。
2. **PRI-12 Cluster B（B2/B4）の量子化学方法論論文への適用確立**: v18 Stage 3 v3で
   PRI-12/B4（Retroductive-foundation mismatch: Table I一電子性質類推→力定数精度の推論）
   とPRI-12/B2（Retrospective Confirmation Bias: LiF 39%エラーを方法の支持証拠として
   引用）が量子化学理論論文の典型パターンとして初めて明示記録された。
3. **Layer VQ非対称性パターンの確立**: Layer 1（PHF形式論）= VQ-2相当、論文全体 = VQ-1
   という層別VQ評価が方法論論文の標準パターンとして記録された（Stage 3 §6）。
4. **series-presentation resolved patternの確立**: Paper I/II同時発表という分割提示が
   RI-09 case(a)（同時発表・相互参照）として記録され、単一論文の communication→Full Paper
   遷移とは異なる構造的類型として確立した。
5. **SRG-2の深化**: v18でB-2（一電子性質類推）・B-3（ε未定量化）・U-2（limited basis
   矛盾）の三者が緩和項問題を共有根として統合され、v17のSRG-2より問いの構造が明確化。
6. **BOP候補（候補5）の新規生成**: v17に存在しなかったBorn–Oppenheimer誤差と電子相関
   誤差の未分離問題がD-4候補5として新規展開。

退行3件中R1がmedium impact。R2・R3はlow impact。
R1（PHF vs 状態和法の計算量対比）は「計算量優位の未定量化」として独立した問いの価値があり、
プロンプトレベルでの対応を要する可能性がある（→ OI-029）。

### 正の副次効果

- PRI-12/B4（Retroductive-foundation mismatch）が1968年量子化学理論論文の代表ケースとして確立
- Layer VQ非対称性が「方法論論文の典型VQプロファイル」として§6に記録された
- series-presentation resolved patternが新構造的類型として登録された（woodward1965とは異なる）
- CLA-1（Stanton定理）のD-4候補昇格が「引用切断→独立問いへの昇格」パターンを例示した

### 確認された未回復項目・新規懸案

- R1（D4-4: PHFと状態和法の計算量優位の未定量化）→ open_issues OI-029
- R2（D4-5: Mills 1957比較省略）→ 再評価トリガー: 同世代の競合手法との比較論文への適用時
- R3（D4-6: 閉殻制限・開殻系拡張未言及）→ 再評価トリガー: 閉殻前提の計算化学理論論文

---

## Entry 031: v18 vs v181 — Kumada (devset)

**比較日:** 2026-04-25
**評価論文:** Kumada (Tamao, Sumitani, Kumada, JACS 1972) — devset
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v18 vs v181; Stage 3 = v3（両版同一）

### 背景

v181はv18に対して以下の主要変更を含む:
- Turn 4に「Multi-critical U-item independent recording rule (v18.1)」を追加（C11）
- D-4候補数上限の条件付き拡張（デフォルト8→条件付き10）（C9）
- 予測テーブル独立 grounding チェック（C10）
- D-4ガイダンスに「新手法の動機付け回避コスト チェック」を追加

### スコアカード

| ID | 退行ポイント | v18 | v181 | 判定 |
|----|---|---|---|---|
| R1 | Ni(0)種同定問題（黒色混合物）の独立U項目化 | U-2「黒色混合物 = Ni(0)析出の可能性、high_convergence_high_gapの候補」として独立記録、D-4候補1として最優先展開 | U項目に現れず、SRG-1（Mechanistic validation absent）に一般的吸収。D-4候補から消失 | ⚠️ 後退（medium） |
| R2 | U-4（速度論的 vs 熱力学的制御）の独立記録 | U-4として独立記録、D-4候補2の中心課題 | D-4候補2の注記に言及のみ。独立U項目として記録されない | ⚠️ 後退（low） |
| R3 | Cl₂C=CH₂二重置換機構（D-4候補5） | U-3として独立記録、D-4候補5として展開 | S1・S2・S3のいずれにも現れない | ⚠️ 後退（low） |
| — | D-4候補の総数 | 6候補 | 7候補 | ✅ v181増加 |
| — | Corriu–Masse系との区別 | D-4候補6（比較的優位性）として混在 | CLA-2（独立CLAとして明示化） | ✅ v181改善 |
| — | β水素排除（CLA） | D-4候補で言及なし（D4-7相当項目はOI-001として保留のみ） | CLA-1として独立展開、S3にも反映 | ✅ v181改善 |
| — | Stage 3実行 | 未実行（比較対象外） | v3初回実行（VQ-2 Qualified, §5最短補強ルート生成） | ✅ v181新規 |
| — | scope_type | framework_question | tool_question | 🔄 変化（要確認） |

### 総合判定

**v181 > v18（3退行、ただし全てmedium/low impact）**

v181の優位点:
1. **D-4候補数の増加（6→7）**: β水素排除（候補5）とCorriu–Masse区別（候補7）が独立候補として生成
2. **CLA設計の改善**: β水素排除がCLA-1として、Corriu–Masse比較がCLA-2として明示化され、S3 §2に直接反映
3. **Stage 3 v3の初回実行**: VQ-2 (Qualified)判定、SRG→RI/ER/EPのcrosswalk、§5最短補強ルートが生成された
4. **v18.1 Turn 4ルールの適用確認**: Multi-critical U-item independent recording ruleが有効に動作

退行3件：R1（黒色混合物/Ni(0)種）がmedium impact。黒色混合物の観察はv18のTurn 4でB-10として独立記録されていたが、v181ではB-7（reporting_omission for R–R）のconsolidationにより消失した可能性がある。R2・R3はlow impact。

### 正の副次効果

- VQ-2 (Qualified)判定が有機金属合成通信論文の典型VQプロファイルとして確立
- RI-09「Note Added in Proof後の非比較パターン」がCodebook注記候補として同定
- RI-03の「純粋観測欠如サブタイプ（Prediction-not-tested）」の追加が提案された
- 層別VQ非対称性（機構層VQ-3未達 / 合成実証層VQ-2到達）が明示的に記録された

### 確認された未回復項目・新規懸案

- R1（Ni(0)種同定問題: 黒色混合物の独立U項目化消失）→ open_issues OI-030
- R3（Cl₂C=CH₂二重置換機構の消失）→ 再評価トリガー: 同条件での次版実行時

---

## Entry 032: v18 vs v181 — gerrat1968（nakanishi/18, testset）

**比較日:** 2026-04-25
**評価論文:** Gerratt & Mills, J. Chem. Phys. 49, 1719–1729 (1968) — PHF力定数理論 Paper I
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v18 vs v181; Stage 3 = v3（v181で初回実行）

### 背景

v18ではgerrat1968（v17→v18比較 Entry 030）で候補4（Stanton定理の移動基底問題）と候補5（BO誤差 vs 電子相関誤差の未分離）が新規展開された。v18.1はv181候補数拡張上限（C9）・multi-critical U-item独立記録保護（C11）・新手法動機付けコストチェックを導入。

### v18 D-4候補（5件）vs v181 D-4候補（10件）対応表

| v18候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| 候補1（分割提示構造が精度主張を実証から隔離） | D4-1（PHF計算値ゼロ問題）| ✅ 対応（明確化） |
| 候補2（εの未定量化、緩和項問題含む）| D4-4（数値実装不透明性）+ D4-6（二電子精度延長）| ✅ 分解・精緻化 |
| 候補3（PHF線形方程式の収束保証欠如）| D4-4（一部）+ D4-5（基底収束）| ✅ 再分類 |
| 候補4（Stanton定理の移動基底問題）| **対応なし** | ⚠️ 消失 |
| 候補5（BO誤差 vs 電子相関誤差の未分離）| **対応なし** | ⚠️ 消失 |
| ——— | D4-2（性能比較の非対称性）| ✅ 新規（独立展開） |
| ——— | D4-3（Δ項の不使用）| ✅ 新規（独立展開、v18では候補2の下位要素） |
| ——— | D4-7（Mills 1957比較回避）| ✅ 回復（v17→v18退行R2が解消） |
| ——— | D4-8（Stevens-Lipscomb精度ブリッジ不在）| ✅ 新規 |
| ——— | D4-9（動機付けコスト比較なし）| ✅ 新規（v18.1チェック適用） |
| ——— | D4-10（Table I分子選択バイアス）| ✅ 新規 |

### スコアカード

| ID | 退行ポイント | v18 | v181 | 判定 |
|----|---|---|---|---|
| R1 | Stanton定理の有限移動基底への拡張問題（v18候補4）の消失 | 候補4として独立展開: key_quote "The proof of (22) has been given by Stanton." 移動基底条件（∂χ_p/∂R_J^α ≠ 0）でHellmann-Feynman定理が厳密に成立するかという問い | v181では独立D-4候補として現れない。B-4が別用途（コスト比較D4-9）、C-1がC項目として分類済みだが「Stanton定理の移動基底適用域」という固有の問いが展開されない | ⚠️ 後退（medium） |
| R2 | Born-Oppenheimer誤差 vs 電子相関誤差の未分離（v18候補5）の消失 | 候補5として独立展開: key_quote "We assume the Born–Oppenheimer approximation." BO補正と電子相関誤差の重複が未分離という問い | v181ではC-4（Born & Huang）がD4-8（Stevens-Lipscomb精度ブリッジ）に使われるが、BO誤差分離問題は展開されない | ⚠️ 後退（low） |

### 総合判定

**v181 > v18**

v181の優位点:
1. **D-4候補数の大幅増加（5→10）**: multi-critical U-item保護（C11）と拡張上限（C9）の適用により、D4-3（Δ項不使用）・D4-7（Mills比較回避）が独立候補として展開された。
2. **D4-3（Δ項の不使用）の独立記録**: v18では候補2「εの未定量化」の下位要素的位置づけだったが、v181ではU-3として独立記録され、D4-3として展開。multi-critical U-item独立記録保護（C11）の効果。
3. **D4-7（Mills 1957比較）の回復**: v17→v18比較（Entry 030）のR2として記録されていた退行が、v181で回復（OI-029の部分解消）。
4. **D4-9（動機付けコスト比較）の新規生成**: v18.1新規チェック「新手法の動機付け回避コストチェック」が有効に機能。PHFと状態和法の計算量対比未定量化（OI-029のR1）に直接対応。
5. **CLA-2（PRI-12 A4）の独立化**: 二電子緩和項へのO(ε²)精度延長問題がCLA-2として、かつPRI-12 A4（Theorem-domain overclaim）新サブタイプ候補として記録された。
6. **Stage 3 v3の初回実行**: §3でVQ-2判定（Paper I単独）/ VQ-3 Qualified候補（Paper I+II結合）の層別非対称性が記録。§6でRI-03新サブタイプ「Self-proposed-but-unused diagnostic」が提案された。

退行2件：R1がmedium impact（Stanton定理の移動基底問題は理論的に固有の問いであり独立展開の価値がある）。R2はlow impact（BO誤差は当時の慣行内で許容される）。

### 正の副次効果

- Entry 030のR2（Mills 1957比較省略、OI-029暫定対象）がv181で回復
- PRI-12 A4新サブタイプ「Theorem-domain overclaim」が gerrat1968 CLA-2として提案
- RI-03新サブタイプ「Self-proposed-but-unused diagnostic」が §6 で提案（§6記録）
- 「逆時系列split-presentation」（Paper II先行刊行）が新構造的類型として§6に記録
- OI-029（PHFと状態和法の計算量対比未定量化）が D4-9 として部分的に対処

### 確認された未回復項目・新規懸案

- R1（Stanton定理の移動基底問題）→ open_issues OI-031

---

## Entry 033: v18 vs v181 — binkley1979（nakanishi/19, testset）

**比較日:** 2026-04-25
**評価論文:** Pople, Krishnan, Schlegel, Binkley (1979) — "Derivative Studies in Hartree–Fock and Møller–Plesset Theories", Int. J. Quantum Chem. Symp. 13, 225–241
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v18 vs v181; Stage 3 = v3（v181で初回実行）

### 背景

v18.1は候補数拡張上限（C9、SRG≥7で9件まで）・multi-critical U-item独立記録保護（C11）・新手法動機付けコストチェックを導入。binkley1979はSRG-1〜SRG-7の7件を生成したため拡張上限が適用され、v18.1でD-4候補数が5→9に増加した。

### v18 D-4候補（5件）vs v181 D-4候補（9件）対応表

| v18候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| 候補1（力定数行列の不在、U-2扱い） | **対応なし**（B-2がCPHF収束基準として再定義） | ⚠️ 消失 |
| 候補2（非調和補正の操作的不透明性） | D4-2（非調和補正の不確かさがベンチマークを汚染） | ✅ 強化・対応 |
| 候補3（単一分子検証） | D4-3（残差誤差3要因の分離なし）に一部吸収 | ✅ 再定義・対応 |
| 候補4（有限差分法との非較量比較） | D4-7（先行有限差分計算との数値比較の体系的欠如） | ✅ 対応 |
| 候補5（再現性の構造的障壁、Ref [28]未発表） | D4-6（効率主張の再現可能性の欠如）に吸収 | ✅ 対応 |
| ——— | D4-1（解析的MP2勾配式の実装正確性の未検証、B-1+U-1） | ✅ 新規・独立展開 |
| ——— | D4-4（CPHFソルバーの収束基準と数値安定性） | ✅ 新規 |
| ——— | D4-5（調和振動数比較の統計的根拠の欠如） | ✅ 新規 |
| ——— | D4-8（平衡幾何学の報告と最適化収束の不在） | ✅ 新規 |
| ——— | D4-9（スピン軌道定式化（UHF）の未検証） | ✅ 新規 |

### スコアカード

| ID | 退行ポイント | v18 | v181 | 判定 |
|----|---|---|---|---|
| R1 | 力定数行列の不在（U-2）が独立候補から消失 | 候補1として独立展開: "The derivative programs at the HF and the MP2 level have been used to calculate the harmonic vibrational frequencies" — アルゴリズムの直接産物（力定数行列）が報告されない自己矛盾的不在をU-2+D-4候補1として特定 | v181ではB-2がCPHF収束基準として再定義され、力定数行列不在は独立D-4候補として現れない。SRG-4がCPHF収束に割り当てられており、「力場そのものの不在」という問いが展開されない | ⚠️ 後退（medium） |

### 総合判定

**v181 > v18**

v181の優位点:
1. **D-4候補数の大幅増加（5→9）**: SRG7件による拡張上限適用（C9）により、CPHFソルバー収束（D4-4）・統計的根拠欠如（D4-5）・幾何学報告（D4-8）・UHF未検証（D4-9）が新規展開された。
2. **D4-1（解析的MP2勾配の実装正確性）の独立記録**: B-1とU-1の組み合わせを論文の核心的未検証事項として明確に位置づけ、v18の候補3「単一分子検証」より焦点を絞った形で展開。
3. **scope_typeの精緻化**: v18の "tool_question"（計算ツールの効率比較）からv18.1の "framework_question"（汎用計算フレームワークの問い）に変化し、論文の主張の本質（新たな計算フレームワークの確立）をより正確に反映。
4. **E節の競合分析精度向上**: Pulay [5,6]のみからIshida-Morokuma [14]・Thomsen-Swanstrom [7]を含む4者の競合分析に拡充。
5. **temperature_note全候補付記**: v18では部分的だったtemperature_noteがv181では全9候補に付記され、優先順位根拠が透明化。

退行1件：R1（medium impact）。力定数行列の不在は「このアルゴリズムの直接産物が論文に掲載されていない」という独自の問いであり、v181での独立展開が望ましい。

### 正の副次効果

- SRG-1〜SRG-7の7件構造がD-4候補9件と§2 SRG/CLAクロスウォークに一貫して接続された（S3v3 §2でSRG-1→PRI-12/A5対応が記録された）
- Stage 3 v3初回実行: VQ-2（qualified）判定、VQ-3未達はPRI-12/A5 Fatal（SRG-1→RI-03直結）が主因

### 確認された未回復項目・新規懸案

- R1（力定数行列の不在をU-2＋D-4独立候補として展開する問題）→ open_issues OI-032
- R2（BO誤差 vs 電子相関誤差の未分離）→ 再評価トリガー: BO補正を明示的に議論する計算化学論文への適用時

---

## Entry 034: v18 vs v181 — nakanishi2025（nakanishi/7, testset）

**比較日:** 2026-04-25
**評価論文:** Nakanishi, Tsutsumi, Ono, Sada, Taketsugu — J. Comput. Chem. 2025, 46:e70101 (nakanishi/7)
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v18 vs v181; Stage 3 = v3（両版共に実行済み）

### 背景

nakanishi2025はNRO（Natural Reaction Orbital）法を反応経路分岐に初めて適用し、ベックマン転位の10置換基について分岐点でのλ_R/λ_F比を計算してユカワ-ツノ相関（R = 0.9512）と照合した論文。Entry 029（v17 vs v18）でOI-028（数値指標の閾値信頼性・比較可能性に関するU項目がv18で消失）が記録された。v18.1のC11ルール（multi-critical U-item独立記録保護）がOI-028への直接対応として設計されており、本比較はその効果検証を主目的とする。

### 項目数の変化

| カテゴリ | v18 | v181 |
|----------|-----|------|
| A | 1 | 0 |
| B | 11 | 18 |
| C | 3 | 3 |
| U | 3 | 5 |
| SRG | 5 | 7 |
| D-4候補 | 8 | 10 |
| 合計(A+B+C+U) | 18 | 26 |

### D-4候補の対応関係

| v18候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| 候補1（生成物分布の予測、grounded U-1/B-4/C-1）| D-4-5（予測フレームワーク外部検証不在、U-5/C-1/C-2/B-7） | ✅ 対応（U番号変更・内容強化） |
| 候補2（動的解釈の欠如、grounded U-2/B-4）| D-4-4（静的IRC vs 動的分岐の自己矛盾、U-4/B-7） | ✅ 対応（形式変更） |
| 候補3（p-Me外れ値、grounded A-1/B-5）| D-4-2（閾値信頼性、U-2/B-16） | ✅ 対応（A-1→U-2に昇格、強化） |
| 候補4（ユカワ-ツノ統計、grounded B-5/B-6/B-9）| D-4-9（ハメット相関統計的厳密性、B-11/B-16/U-2） | ✅ 対応 |
| 候補5（p-OMe VRT不在概念的不整合、grounded U-3/B-8）| D-4-3（分岐点定義非等価性、U-3/B-14） | ✅ 対応（フレーミング変化: 現象クラス問い→比較可能性問い） |
| 候補6（気相モデル、grounded B-7/B-10）| D-4-8（気相中性基質モデル、B-12/B-4） | ✅ 対応 |
| 候補7（ROET/IBO比較不在、grounded B-11/C-2）| D-4-7（代替軌道追跡手法との定量比較不在、B-9/C-3） | ✅ 対応 |
| 候補8（記述子の汎化、grounded B-4/C-3）| **対応なし**（D-4-5に部分吸収） | ⚠️ 消失 |
| ——— | D-4-1（正規化問題、U-1 critical）【新規 critical】 | ✅ 新規 |
| ——— | D-4-6（速度論vs熱力学的制御、B-7/U-4）【新規】 | ✅ 新規 |
| ——— | D-4-10（計算レベル依存性、B-13/C-1/C-2）【v17 D4-8の回復】 | ✅ 回復 |

### スコアカード

| ID | 退行ポイント | v18 | v181 | 判定 |
|----|---|---|---|---|
| R1 | 候補8（クロス反応系での汎化問い）の独立D-4候補化の消失 | 候補8として独立展開: "NROはDiels-Alder後TS分岐など既知の別の分岐反応に適用したとき同様の相関を示すか？" — 同一基質クラス10置換基への限定とフレームワーク主張の間の張力として展開。grounded_in B-4/C-3 | v181ではD-4-5（予測フレームワーク外部検証不在）が"訓練セットに含まれない置換基での予測検証"を含むが、「別の反応系（Diels-Alder等）への適用」という固有の問いが独立候補として展開されない | ⚠️ 後退（low） |

### 総合判定

**v181 > v18**

v181の優位点:
1. **OI-028の解消（U項目回復）**: v18でB-5/B-9に吸収されていた閾値信頼性・比較可能性のU項目が、C11ルールにより独立U項目として復活。U-1（正規化/比較可能性, critical）・U-2（p-Me閾値/threshold-reliability, high-critical）・U-3（分岐点定義非等価性/comparability, high-critical）が記録され、v17のU-4・U-5に対応する内容が両者ともvoll回復した上でU-1（normalization）が新たなcritical项目として追加された。
2. **A-1（p-Me抑圧）→ U-2への昇格**: v18では p-Me異常をA項目（著者の deferred item）として分類していたが、v181ではU-2（self-contradictory absence, threshold-reliability）として再分類。p-Me の説明は論文内で完結を主張しており、真にdeferredではない。この昇格はより正確な分類である。
3. **D-4-1（正規化問題、critical）の新規記録**: λ_R とλ_F の比較に際して変位ベクトルの正規化規約が記載されないという問いがcritical severity U-1として確立し、D-4筆頭候補として展開された。v17・v18いずれにも存在しなかった新規かつ最高severity候補である。
4. **D-4-10（計算レベル依存性）の回復**: Entry 029の対応表で⚠️消失として記録されていたv17 D4-8（計算レベル依存性）が、v181ではD-4-10として復活。
5. **SRG数の増加（5→7）**: SRG-6（静的IRC vs 動的分岐）・SRG-7（代替手法比較不在）が新規追加され、priority_structureの「前提層・検証層・機構層」3層構造が明確化した。
6. **confirmed_english_propositionalの精度向上**: v18の"along IRC pathways"（一般的）がv181では"at reaction path bifurcation points"（論文の固有貢献点）に修正された。

退行1件：R1（low impact）。クロス反応系汎化の問いは V3-Q9（medium severity）に対応し、D-4-5の"訓練セットに含まれない置換基"の記述で部分的に対処されている。

### 正の副次効果

- OI-028（数値指標の閾値信頼性・比較可能性のU項目消失）が解消（→ status: resolved）
- Entry 029対応表で⚠️消失だったv17 D4-8（計算レベル依存性）がD-4-10として回復
- 前提層/検証層/機構層の3層priority_structure分類が新規確立。D-4-1（前提層）・D-4-5（検証層）・D-4-4（機構層）の独立性が明示化された
- U-5 ↔ B-7の準ピボット構造が記録され、相対生成物エネルギー不在がpredictive claim検証不能性を支える構造が可視化された

### 確認された未回復項目・新規懸案

- R1（汎化クロス反応系問い: "別の分岐反応系でのNRO相関"が独立候補として現れない）→ 再評価トリガー: 明示的に「他の反応系への一般化」を述べる計算化学新手法論文での次回適用時に確認

---

## Entry 035: v18 vs v181 — woodward1965 (nakanishi/13)

**比較日:** 2026-04-25
**評価論文:** Woodward & Hoffmann, JACS 1965 (nakanishi/13) — "Stereochemistry of Electrocyclic Reactions"
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v18 vs v181; Stage 3 = v3（v181で初回実行）

### 背景

v18.1はD-4候補上限条件拡張（C9）・multi-critical U-item独立記録保護（C11）・予測テーブル独立groundingチェック（C10）・新手法動機付けコストチェックを導入。woodward1965はW-H 1965 communication（2頁）であり、v18ではD-4候補が6件、v181では8件生成された。

### v18 D-4候補（6件）vs v181 D-4候補（8件）対応表

| v18候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| 候補1（HOMO反証可能性 / U-1）| 候補1（反証可能性の操作的不在 / U-1, B-6） | ✅ 継続・強化 |
| 候補2（EH計算定量性 / B-1）| 候補5（EH計算HOMO寄与率と幾何学的感度 / B-1, B-2） | ✅ 継続・強化（B-2統合） |
| 候補3（全既知事例の脆弱性 / B-4v18）| 候補2（verified vs asserted / B-3, C-3） | ✅ 継続 |
| 候補4（光化学逆転則の反証不能修飾 / A-1）| 候補3（光化学励起状態同定 / U-2）| ✅ 再分類・強化（A→U）|
| 候補5（操作的適用範囲・二経路選択 / B-8v18）| 候補8（二つの許容経路選択原理 / T2:B-4）| ⚠️ grounding後退（medium） |
| 候補6（競合モデルとの識別実験不在 / C-1v18 Lewis&Steiner）| 候補6（Oosterhoff提案差異 / C-1） | △ 対象変更（Lewis&Steiner→Oosterhoff） |
| ——— | 候補4（Table I独立grounding / A-1, U-3, B-4）| ✅ 新規・独立展開（C10適用） |
| ——— | 候補7（熱的許容/禁止エネルギーコスト / B-6）| ✅ 新規・候補1から分離展開 |

### スコアカード

| ID | 退行ポイント | v18 | v181 | 判定 |
|----|---|---|---|---|
| R1 | 二経路選択問いの grounding 強度 | 候補5が明示的B項目（B-8v18: 「special stereoelectronic factors may be definitive」直接引用）で展開 | 候補8がT2:B-4と表記され明示的Bアンカーなし | ⚠️ 後退（medium） |

### 総合判定

**v181 > v18**（R1 1件: medium）

v181の優位点:
1. **D-4候補数の増加（6→8）**: C9拡張上限適用（critical U-1 + high U-2, U-3の3件）により候補7・候補8が追加展開された。
2. **光化学問題の再分類（A→U）**: v18では「光化学逆転則の suppressed deferral」として A-1 に分類していたが、v181では「励起状態同定という prerequisite-absence」として U-2 に再分類。これは v18 より論理的に正確。
3. **Table I独立grounding問題の独立展開（候補4）**: C10（予測テーブル独立groundingチェック）が v18.1 で追加されたことにより、奇電子系・荷電系の独立計算不在が v18 で見落とされていた独立 D-4 候補として展開された。
4. **候補1と候補7の分離**: v18では「反証可能性」として一括していた問いが v181 では U-1（脱出条項の操作的未定義）と B-6（活性化エネルギーの不在）として分離され、それぞれの問いの独立性が明確化された。
5. **Lewis & Steiner の正確な再分類**: v18 では C 項目（引用中断）として扱っていた可能性がある Lewis & Steiner が、v181 では「全面的に接触した反論対象」として正確に排除され、C-1 が Oosterhoff（真の novelty 競合）に割り当てられた。

### 正の副次効果

- Stage 3 v3（nakanishi/13 初回）: VQ-2 qualified 判定、PRI-12 Cluster B（B2+B3）の歴史的基礎理論論文への最重要事例として記録。
- Layer 別 VQ 非対称性（Layer A VQ-3 qualified / Layer C VQ-1）を標準事例として制度登録。
- RI-07 致命性の Era-norm 依存の具体事例として Codebook 注記追加を提案。

### 確認された未回復項目・新規懸案

- R1（二経路選択問いの grounding 後退）→ open_issues OI-033 として追記。再評価トリガー: 非対称基質の立体電子選択問題を扱う論文への適用時。

---

## Entry 036: v18 vs v181 横断メタ観察 — SRG 拡張による細粒度候補吸収パターン

**比較日:** 2026-04-25
**性格:** メタエントリ（個別論文ではなく Entry 031〜035 の横断観察）
**作成モデル:** Opus 4.7（v18.1 確定判断時）

### 背景

v18.1（C9: D-4 候補上限の条件付き拡張、C10: 予測テーブル独立 grounding チェック、C11: 多重 critical/high U項目独立記録保護）は v18 退行確認で検出された OI-024〜029（D-4 候補上限制約による中位候補消失）への対応として策定された。退行確認 5 論文（Kumada, gerrat1968, binkley1979, nakanishi2025, woodward1965）すべてで **v181 > v18** が確認されたが、6 件の OI のうち 3 件が解消、1 件部分対応、2 件未解消の一方で、**4 件の新規退行（OI-030〜033）が観察された**。本メタエントリは新規退行の構造的原因を記録する。

### 個別エントリの集計

| Entry | 論文 | D-4 候補数 | 解消した v18 OI | 新規退行 |
|-------|------|---------|---------------|---------|
| 031 | Kumada | 6 → 7 | （直接対応なし）| OI-030 |
| 032 | gerrat1968 | 5 → 10 | OI-029 | OI-031 |
| 033 | binkley1979 | 5 → 9 | OI-026（部分）| OI-032 |
| 034 | nakanishi2025 | 8 → 10 | **OI-028 完全解消** | （なし）|
| 035 | woodward1965 | 6 → 8 | **OI-027 解消** | OI-033 |

**集計:** D-4 候補総数 30 → 44（+47%）。OI 解消 3 件（OI-027/028/029）+ 部分 1 件（OI-026）/ 新規退行 4 件（OI-030/031/032/033）。

### 共通パターン: SRG 再編による細粒度候補吸収

C9 拡張上限（8→10）により D-4 候補数は増加したが、**v18 で独立 D-4 候補化されていた細粒度の問いが v181 の SRG 再編で大粒度 SRG に吸収される逆現象が発生した**。

| OI | 論文 | v18 で独立化されていた候補 | v181 での吸収先 |
|----|------|--------------------------|-----------------|
| OI-030 | Kumada | B-10「黒色混合物 = Ni(0) 析出」（U-2 として独立 U項目化） | SRG-1（Mechanistic validation absent）に統合的吸収 |
| OI-031 | gerrat1968 | 候補 4「Stanton 定理の有限移動基底拡張」 | B-4/C-1 が D4-9（動機付けコスト比較）に再割当て |
| OI-032 | binkley1979 | 候補 1「力定数行列の不在」（U-2 + D-4 候補） | B-2 が「CPHF 収束基準」として再定義 |
| OI-033 | woodward1965 | 候補 5「二経路選択問い」（B-8v18 直接引用付き） | T2:B-4 grounding に後退（明示的 B-anchor 弱化） |

### 構造的解釈

C9 + C10 + C11 が D-4 候補生成の **総量** を増やす一方で、Stage 1 Turn 4 の SRG 形成段階では同じプロンプトロジックが動作するため、**SRG 自体の境界が拡大・再編** されることがある。新しい SRG は v18 では別 SRG/CLA に属していた B/U項目を統合的に取り込み、結果として：

1. **候補スロットの再配分:** v18 で独立スロットを占めていた中粒度候補が、v181 では拡張 SRG の一部要素として note 内記述に格下げ
2. **B-anchor の希釈:** v18 で明示的な B 項目アンカーを持っていた候補が、v181 では SRG 統合候補の T2 grounding に後退
3. **U項目の B 項目への吸収:** v18 で self-contradictory absence U として独立記録されていた問いが、SRG 再編後は B 項目（reporting_omission）として吸収

これは v18.1 の C11（multi-critical U-item 独立記録保護）が **「論文内に複数の critical/high U項目が並存する場合」のみ発動** する仕様の限界を示す。U項目が単独・medium severity の場合は保護対象外であり、SRG 拡張による吸収を防げない。

### v19 候補としての対応設計

新規退行 OI-030〜033 の構造的原因（SRG 再編による細粒度候補吸収）への対応として、以下の v19 候補を記録する：

**(a) v18→v18.1 候補保持チェック（v19 candidate）:**
v18.1 D-4 候補生成後、もし v18 出力が利用可能であれば、v18 で独立 D-4 候補だった項目が v181 で SRG 統合候補の note 内に明示記述されているかを確認する保護ルールを追加。明示記述なく吸収されている場合、独立候補として再展開する。

**(b) U-as-D-4-anchor 保護（v19 candidate）:**
v18 で U項目として独立記録されていた問いが、v181 で B項目に格下げされている場合、それを Turn 4 で検出し U項目への昇格を維持する。multi-critical 条件に依存しない単独 U項目保護ルール。

**(c) D-4 候補の granularity diff 検出（v19 candidate）:**
v18 と v181 の同一論文 D-4 候補を機械的に diff し、v18 で B-anchor 付きだった候補が v181 で T2 grounding に後退している場合を自動検出。Stage 2 出力の構造的退行を可視化。

これらは v19 設計時に検討する。v18.1 確定時点では新規退行を構造的観察として記録のみとし、追加プロンプト改訂は行わない。

### v18.1 確定判断

v18.1 はネット評価で v18 を上回るため確定する：
- **プラス:** D-4 候補総数 +47%、OI-027/028/029 解消（3 件）、OI-026 部分対応、PRI-12 A4 新サブタイプ提案、normalization critical U項目の新規記録
- **マイナス:** OI-030〜033（4 件 medium）の新規退行、OI-024/025（Kumada）の継続未解消

OI-024〜025 の継続未解消は Kumada（devset、有機合成論文）特有の「合成計画用途の二層性」「目的論的接続」パターンであり、C10（予測テーブル）や C11（U項目）には捕捉されない。これらは v19 で別の D-4 出発点視点（例: 「方法の存在証明 vs 計画用途」「目的論的接続の不在」）として明示化する候補。

OI-030〜033 は本メタエントリで構造的原因を記録した上で、v19 で対応する。

### 正の副次効果（メタ的観察）

- **PRI-12 A4「Theorem-domain overclaim」新サブタイプ提案** — gerrat1968 (Entry 032) で初検出。Codebook 拡張候補として §6 に記録された。
- **normalization critical U項目の新規記録** — nakanishi2025 (Entry 034) で D-4-1 として確立。数値記述子論文での前提層問いの典型として登録。
- **Layer別 VQ 非対称性の標準事例化** — woodward1965 (Entry 035) で Layer A VQ-3 qualified / Layer C VQ-1 が制度登録。
- **逆時系列 split-presentation パターン** — gerrat1968 (Entry 032) で Paper II 先行刊行という新類型が §6 に記録。

### 確認された未回復項目・新規懸案

- 構造的観察として v19 で対応：(a) v18→v181 候補保持チェック、(b) U-as-D-4-anchor 保護、(c) D-4 candidate granularity diff 検出

---

## Entry 037: v17 vs v181 — arcoco2004（NobleGas/References, full paper）

**比較日:** 2026-04-25
**評価論文:** Ono & Taketsugu, J. Phys. Chem. A 2004, 108, 5464–5467「Theoretical Study of Ar-CoCO」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション

### 背景

arcoco2004 は NobleGas/References フォルダに格納された著者グループ自身の論文（自己解析）であり、v17 プロンプトで既解析済み。今回 v18.1（+s3v3+s4v3）で再解析し、v17 S2 出力と比較した。固体アルゴン行列単離条件下での Ar-CoCO 形成を CASPT2/RCCSD(T)/UMPWPW91 三手法で計算し、既報実験スペクトルを Ar-CoCO に再帰属する論文。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| A | 2（A-1: Ar-Co 結合詳細, A-2: M-CO 系一般化 suppressed）| 0 |
| B | ~10（概算） | 18 |
| C | 5 | 4 |
| U | 2（U-1: Ar-CoCO 固有指紋の実験的不確認, U-2: 方法信頼性）| 5（U1: critical, U2-U3: high, U4-U5: medium） |
| SRG | 3（SRG-1, 2, 5）| 5（SRG-1〜5）|
| D-4 候補 | 5 | 9（拡張上限適用）|

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | A-2「他の M-CO 系への一般化が suppressed」という修辞分析 | A-2 として独立分類；D-4-4（Sc-Cu 系統適用問い）の grounding に使用 | D-4-9/B18 で「"in some cases" の適用範囲未定義」として部分的に触れるが、suppressed deferral の修辞的性格は消失 | ⚠️ 部分回復 |
| R2 | D-4-5「Zhou-Andrews（refs 16/17）と Tremblay（ref 18）の ν(CoCO) 実験値の整合性」問い | D-4-5 として独立候補（C-1, B-6 grounded）— 二実験グループの報告値が一致するかを問う | v181 D-4 に対応なし | ⚠️ 未回復 |

### 総合判定

**v17 < v181**

v181 の優位点:
1. **U 項目の新規導入（U1 critical, U2–U3 high, U4–U5 medium）**: v17 では U-1（Ar 指紋の実験不確認）のみだったが、v181 では U1（ν(CoCO) 非調和性不在、critical）・U2（ν(CO) カウンタートレンド、high）・U3（1:1 Ar-CoCO モデル前提、high）が critical/high severity で独立化された。これらは帰属主張の核心的脆弱性を初めて明示した新規発見。
2. **D-4 候補数の拡張（5→9）**: C9 拡張上限（3 critical/high U 項目により上限 10）が適用され、D-4-2（ν(CO) カウンタートレンド）・D-4-3（1:1 モデル前提）・D-4-8（指紋モード）・D-4-9（マトリックスシフト検証可能性）の 4 候補が新規追加された。
3. **D-4-2（ν(CO) カウンタートレンド）の発見**: 「帰属モデルなら全モードで Ar-CoCO が実験値に近いはず」に反して ν(CO) では CoCO の方が近いという内部矛盾を初めて D-4 候補として展開。v17 ではこの矛盾が議論されていなかった。
4. **SRG の細分化（3→5）**: SRG-3（スペクトル帰属証拠）・SRG-4（活性空間）が新規追加され、RI/ER/EP のクロスウォークがより精緻化。
5. **B 項目の詳細化（~10→18）**: B13（CASPT2 IPEA/level-shift 未記載）・B14（50 Å 参照の妥当性）・B15（Co-C 結合長順序逆転）・B18（マトリックスシフト主張の気相参照なし）等、v17 で見落とされていた細粒度問題を捕捉。

### 正の副次効果

- Stage 3 v3（arcoco2004 初回）: VQ-2 判定、RI-04 Fatal（SRG-3: 選択的モード前景化）+ RI-03 Fatal（CLA-1: 1:1 Ar-CoCO 前提未確立）によって VQ-3 未達が構造的に記録された。
- **RI-04 サブパターン「選択的モード前景化（Selective mode highlighting）」の発見**: 複数モードのうち帰属モデルと一致するモードのみ前景化するパターンを初検出し、Codebook §6 への追記候補として登録。
- **PRI-12 A5（Multi-layer approximation stacking）の新代表事例**: CASPT2 幾何学 × UMPWPW91 ZPE × UMPWPW91 BSSE × UMPWPW91 周波数の四層異種転用という、「著者が明示的に開示した方法間転用」の新類型として登録。
- **Era-transitional edge case（CASPT2 IPEA シフト）**: Ghigo et al. 2004 と同年投稿であることを Stage 3 が記録し、Stage 4 が外部文献確認で裏付けた。

### 確認された未回復項目

- **R1（A-2 suppressed generalization の修辞分析）**: ⚠️ 部分回復。内容は D-4-9 で部分的に触れるが、「著者が意識的に Sc-Cu 系の一般化を抑制した」という修辞分析の独立性は v181 で消失。v18.1 では A 分類を使用しない仕様のため構造的。
- **R2（D-4-5: 実験値の実験グループ間整合性）**: ⚠️ 未回復。Zhou-Andrews（refs 16/17）と Tremblay（ref 18）の ν(CoCO) 実験値が一致するかという問いは、スペクトル帰属論証の一次的根拠の安定性に関わり、独立 D-4 候補として価値を持つ。**OI-034 として追記。**

---

## Entry 038: v17 vs v181 — ngpt2005（NobleGas/References, full paper）

**比較日:** 2026-04-25
**評価論文:** Ono, Taketsugu, Noro (J. Chem. Phys. 2005, 123, 204321) — CCSD(T)/DK による Pt–Ng および Ng–Pt–Ng (Ng=Ar,Kr,Xe) 理論研究
**モデル:** claude-sonnet-4-6
**評価者:** Sonnet 4.6 セッション（v181 解析完了後に自動比較）

### 背景

ngpt2005 は本プロジェクト全体の著者（Taketsugu グループ）の原論文であり、NobleGas/References フォルダに配置された。v17 は先行版として解析済みであり、v181 は S0–S2–S3v3–S4v3 を同一セッションで完走した。比較対象は S2 出力（D-4 候補・U 項目・SRG・E節）。

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | 質量非依存性振動数のD-4候補化（PtAr/PtKr/PtXeのωeがほぼ等しいことの機構的説明欠如） | D-4候補3（v17 U-2: medium severity、U観測として記録） | 未収録（v181のU-2はAr-Pt-Ar閾値信頼性として別問題に置換） | ⚠️ 退行 |
| R2 | 先行実験系との数値比較不在のD-4候補化（Evans & Gerry との数値対比欠如） | D-4候補7（C-1/C-2/C-3 grounded、medium severity） | C項目で記録のみ。D-4候補に昇格せず | ⚠️ 部分退行 |
| R3 | IR強度不在の独立D-4候補化 | D-4候補5（B-7/A-1、独立候補） | D-4候補4（「実験検出可能性の技術的根拠不在」）に吸収。B-7の独立性消失 | ⚠️ 部分回復（吸収） |

### 総合判定

**v181 > v17**

v181 の優位点:
1. **T1診断/単参照妥当性（U-1: high severity）の新規発見**: v17 に完全欠如。Pt(¹S)状態に対する CCSD(T) の単参照妥当性という最も根本的な方法論的前提欠如を初めて U 項目として独立記録した。全報告数値（結合エネルギー・分光定数・安定性主張）の信頼性基盤の問いであり、最重要の新規捕捉。
2. **U-2架構精緻化（Ar-Pt-Ar閾値信頼性）**: v17 では B-1/D4-1/D4-6 に分散していた「2.2 kcal/mol マージンが不確かさ範囲内」問題を U-2 として構造化し、二値判定の論理的矛盾を明示した。
3. **CBS外挿懸念 (B-14) の新規記録**: v17 未記録。
4. **相対論的寄与定量化（D-4候補3）の独立昇格**: v17 では C-5 に留まっていた Pyykkö ref 13 の Dropped Quantitative Benchmark が独立候補に昇格。
5. **5s/5p相関の三原子系未適用（D-4候補7）**: v17 完全欠如。論文自身の感度試験が二原子系のみに限定された点を独立候補化。
6. **DFT境界の第三Ng不付加未検証（D-4候補8）**: v17 完全欠如。A-1と B-6 の連動で DFT-only 境界の信頼性問題を候補化。
7. **SRG構造の精緻化（7個、RI/EP対応付き）**: v17 の SRG 構造に対して RI/EP クロスウォークが追加されてより機能的。
8. **TEMPERATURE_SUMMARY の明示化**: high_convergence_high_gap（空）/ high_convergence_low_gap / low_convergence_high_gap の3区分が明示された。

### 正の副次効果

- Stage 3 v3（ngpt2005 初回）: VQ-2（Qualified）判定、RI-04 Fatal for Ar–Pt–Ar（安定性マージン~2.2 kcal/molが不確かさ範囲内）を構造的に記録。層別VQ非対称性（Kr/Xe→VQ-3閾値近接、Ar→VQ-2止まり）を初記録。
- **PRI-12/A8（Boundary-adjacent application without diagnostic）の相対論的量子化学論文代表例**: 遷移金属CCSD(T)論文のT1省略パターンを Era-Norm とRI-08 サブタイプ「uncombined uncertainty threshold crossing」候補とともに記録。
- **RI-01新サブタイプ候補「参照状態非対称性（Reference-state asymmetry）」の発見**: 二原子系は一重項解離限、三原子系は三重項解離限を参照状態として使用する非対称性を RI-01 新サブタイプ候補として提案（§6）。
- **Stage 4 v3**: EP-08a・EP-01a・EP-03a の長期未充填（インセンティブ構造的未充填、~20年）と VQ 階層逆転パターン（高VQ EP が同年または先行充填; 低VQ EP が未充填）を記録。

### 確認された未回復項目

- **R1（質量非依存性振動数）**: ⚠️ 退行。PtAr/PtKr/PtXe の ωe がほぼ等しいという反直観的観察（論文自身が "similar to one another in spite of the difference in atomic mass" と明記）が v181 では U 項目・D-4 候補として収録されなかった。**OI-035 として追記。**
- **R2（先行実験系との数値比較不在）**: ⚠️ 部分退行。Evans & Gerry 実験値との数値比較欠如が D-4 候補に昇格しない。中程度の影響。OI として登録しない（既存 OI-007 の射程内の可能性あり）。

---

## Entry 039: v17 vs v181 — ngnico2004（NobleGas/References, letter）

**比較日:** 2026-04-25
**評価論文:** Ono & Taketsugu, Chem. Phys. Lett. 385 (2004) 85–91「Theoretical study of Ng–NiCO (Ng = Ar, Ne, He)」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181 S0–S1–S2–S3v3–S4v3 解析完了後に自動比較）

### 背景

ngnico2004 は本プロジェクト著者グループの CPL 通信論文。v17 は先行版として解析済み。今回 v181（+s3v3+s4v3）で解析し、v17 S2 出力と比較した。Ar/Ne/He–NiCO の結合エネルギー・振動数・行列単離スペクトル帰属（NiCO vs. Ar–NiCO）を CASSCF/MR-SDCI(+Q)/CCSD(T)/DFT で理論的に特徴付けた論文。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| A | — | 0（v181 は A 分類を使用しない仕様） |
| B | ~12 | 17 |
| C | ~6 | 5 |
| U | 4（U-1〜U-4、診断ピーク/He>Ne/1:1モデル/Ne-ECP）| 4（U1〜U4、循環検証/診断バンド/矛盾証拠/調和-基本互換）|
| SRG | 7（SRG-1,3,4,5,6,7,8） | 5 + 2 CLA |
| D-4 候補 | 8 | 10（拡張上限適用：U1,U2,U3 が high）|

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | D-4-4「He > Ne 結合エネルギー異常が BSSE アーティファクトである可能性」 | D-4-4（SRG-6, B-8, U-2, U-4 grounded）として独立候補；「計算アーティファクトである場合、論文の物理的結論は根底から覆される可能性がある」を明記 | D-4-7（SRG-5）が「結合エネルギー順序の物理的起源」として RI-05 qualitative overread 問いを提起；BSSE による Ha > Ne 逆転の artifact シナリオは記述なし | ⚠️ 部分回復（RI-05 framing に後退） |
| R2 | D-4-7「イソトープシフト計算の方法論的一貫性」（B-5: CCSD(T) レベルの同位体シフト不在） | D-4-7 として独立候補；MPWPW91 の誤差相殺が同位体シフトに対して安定かどうかを問う | SRG-4（U1,U3,B7 grounded）で同位体シフト問題を詳しく展開するが、CCSD(T) vs. MPWPW91 の方法論的不一貫性という独立問いは D-4 候補として立てられず | ⚠️ 部分回復（SRG-4 に吸収） |
| R3 | D-4-8「行列単離データベースへの影響範囲の定量化不在」（A-2, C-6 grounded） | D-4-8（"reinvestigated more carefully" の対象範囲・閾値基準不在）として独立候補 | D-4-8（多 Ar 行列環境モデル）および CLA-1 で部分的に触れるが、「どの結合エネルギー閾値以上で再検討が必要か」という定量基準問いは独立候補に昇格しない | ⚠️ 部分回復 |

### 総合判定

**v17 < v181**

v181 の優位点:
1. **PRI-12 A2（Circular validation design）の初検出**: v17 は循環的検証設計を U-1（診断ピーク不在）として間接的に捕捉していたが、「帰属仮説の検証に帰属先が問われている同一データを使用する」という PRI-12 A2 パターンを明示的に同定した。分光学的文脈での PRI-12 A2 初事例として制度設計に寄与。
2. **SRG-4 の三候補化（D-4-1, D-4-2, D-4-3）**: v17 は D-4-3「診断ピーク未確認」として一つの候補に圧縮していたが、v181 は循環的検証（D-4-1）・矛盾証拠の重み付け（D-4-2）・診断バンド探索（D-4-3）の三つを構造的に独立させた。これにより SRG-4 問いの多面性が明示された。
3. **SRG-2（多参照電子構造処理の妥当性文書化）の新規追加**: v17 には V3 エージェント的視点が反映されておらず、T1 診断・Davidson 補正・CASSCF 活性空間の欠如問いが完全に欠如していた。v181 では D-4-4 として独立候補化。
4. **D-4 拡張上限の適用（8→10）**: U1,U2,U3 の high severity 収束により拡張上限が適用され、D-4-9（Ne 行列調和/基本振動数非互換、U4）・D-4-10（先行定量ベンチマーク落下）が新規追加。
5. **U3（矛盾する証拠線の未調停）の独立 U 項目化**: v17 では証拠の矛盾がテキスト中で認識されながらも D-4 候補の一部に溶け込んでいたが、v181 では U3（high severity）として独立記録し、証拠統合失敗のパターンを明示した。

### 正の副次効果

- **Stage 3 v3（ngnico2004 初回）**: VQ-2（era-norm 2004）判定、RI-03 + RI-04 双方 Fatal として VQ-3 未達を構造的に記録。Layer 1（安定性）と Layer 2（スペクトル帰属）の VQ 非対称性（前者 VQ-2 到達、後者 VQ-3 未達）を初記録。
- **PRI-12 A2（Circular validation design）の分光学的代表事例**: 合成・触媒化学で頻出の PRI-12 A2 が物理化学・行列単離分光領域にも適用可能なことを確認した最初の事例として制度設計（§6）に記録。
- **RI-04 + RI-05 共起パターン（SRG-4）の新事例**: SRG-4 内で循環識別根拠（RI-04）と定性的過読（RI-05）が共起し、いずれか一方の解消のみでは証拠完全性が成立しないパターンを記録。RI-04 解消（独立診断バンド観測）が RI-05 解消（定量 RMS 評価）の前提になるという依存関係を明示。
- **Stage 4 v3**: EP-04a（診断バンド探索）の長期遅延または未充填候補として記録；VQ 階層逆転パターン（RI-03/RI-04 Fatal EP が 20+ 年未充填、VQ-3 補強 EP が技術駆動先行充填）を記録。

### 確認された未回復項目

- **R1（He > Ne BE 異常の BSSE アーティファクトシナリオ）**: ⚠️ 部分回復。v17 D-4-4 で明示された「Ne–NiCO(3.71 kcal/mol) が BSSE 補正後に実質的に消滅し物理的結論が覆る可能性」が v181 D-4-7 の RI-05 問いに後退。catastrophic-scenario framing は消失。**OI-036 として追記。**
- **R2（イソトープシフト方法論的一貫性）**: ⚠️ 部分回復。CCSD(T) vs. MPWPW91 の誤差相殺安定性問いが SRG-4 に吸収されて独立候補化されず。OI 不要（SRG-4 で部分的にカバー）。
- **R3（行列単離データベース影響範囲の定量化）**: ⚠️ 部分回復。D-4-8 と CLA-1 で部分的にカバーされているが、「何 kcal/mol 以上で再検討が必要か」という閾値基準問いは独立候補化されず。OI 不要（部分回復で許容範囲）。

---

## Entry 040: v17 vs v181 — ngnico2008（NobleGas/References, full paper）

**比較日:** 2026-04-25
**評価論文:** Y. Taketsugu, T. Noro, T. Taketsugu, J. Phys. Chem. A 2008, 112, 1018–1023「Identification of the Matrix Shift: A Fingerprint for Neutral Neon Complex?」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

ngnico2008 は Taketsugu グループが 2004 年論文の帰属問題を再論した 2008 年の full paper。Tremblay & Manceron（ref 20）が実験的に反論した Ar-NiCO 帰属を、改良 CCSD(T)/seg-QZP + cc-VSCF 計算で再反論する。v17 で先行解析済みで、今回 v181+s3v3+s4v3 で解析した。

### 項目数の変化

| カテゴリ | v17 S2（D-4参照から推算） | v181 |
|----------|------|------|
| A | 2 | 2 |
| B | ~7 | 8 |
| C | ~3 | 5 |
| U | ~4（U-1〜U-4）| 2（U-1: critical, U-2: high）|
| SRG | — | 4（SRG-1〜4）|
| D-4 候補 | 7 | 8（ヘッダー誤記: "9"）|

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | D-1 layered_structure | yes（3層: 計算改善・帰属・一般化原理が独立層） | no（単一基準串刺し構造）| ⚠️ 判断差（軽微）|
| R2 | confirmed_english_propositional の計算修飾欠如 | "CCSD(T) calculations predict Ar-NiCO and Ne-NiCO as stable..." (計算予測の旨明示) | "Noble gas atoms...bind to NiCO to form stable..." (計算/実験の区別なし) | ⚠️ 退行 |
| R3 | E 節の scope_type と問いの問題特定精度 | framework_question; 問い文に "without computed isotopic shift patterns" を明示（D-4候補1の核心を問いに組込み） | tool_question; NiCO系固有の振動指紋の十分性を問う（汎用性低下）| ⚠️ 部分退行 |

### 総合判定

**v181 ≥ v17**（僅差；v18.1 の構造的優位が R2・R3 回帰を上回る）

v181 の優位点：
1. **U-1 critical / U-2 high + C11 独立記録保護**: v17 では U-1〜U-4（severity 不明確）だったが、v181 では U-1（isotopic shifts 未計算: critical）と U-2（Ne cluster 発散: high）が C11 規則で独立保護され、SRG-2 の grounding として D-4 拡張上限（8候補）適用の根拠となった。
2. **D-4 新規追加候補**: 候補6（charge-transfer 分類の操作的定義欠如; q(Ne)=+0.029 e⁻ で「charge-transfer」と称する根拠不在）と候補8（NiN₂・CoCO の高精度化省略と一般化主張の非対称）が v17 に存在しない新規候補。
3. **SRG-2「Tremblay-Manceron rebuttal absence」の明示的 Codebook 化**: B-1（isotopic shifts 未計算）・B-7（T&M 実験的反論スコープ外）・U-1（critical）が SRG-2 として統合され、RI-03+RI-04 双方 Fatal という Stage 3 VQ-1 未達の主因として構造的に展開された。
4. **Stage 3 v3 新知見（計算予測層 vs. 実験帰属主張層の VQ 非対称性）**: VQ-1 の層別判定（計算予測層のみ通過、実験帰属主張層は RI-02 Fatal）を canonical 事例として§6に登録した。「計算が予測し実験が帰属する」二段構造種同定論文の VQ 非対称パターンとして初記録。
5. **Stage 4 v3 新知見（先行充填の逆向き証拠パターン）**: T&M 2006 が EP-03a・EP-04a の「実験側先行充填」を提供するが、充填方向が bare NiCO 解釈を支持するという逆向き先行充填パターンを記録。EP-03a 計算側（isotopic shift 計算）が 16年以上未充填という UQS 発見的意義を明示。

### 正の副次効果

- **RI-03 新サブタイプ「model-predictable-but-uncomputed」提案**: SRG-2（U-1）が「計算可能な予測量が競合仮説識別に必要だが未計算」という RI-03 の新パターンを例示し、Codebook v0.4 追記候補として登録。
- **PRI-12/A5（Multi-layer approximation stacking）の計算分光・種同定論文への適用事例**: CCSD(T) 調和 × PW91PW91 cc-VSCF × MPWPW91 クラスター × 調和/基本振動混合比較という 4 層スタッキングを新適用ドメインとして登録。
- **RI-02+RI-04 共起パターン（種同定論文の構造的共起）の命名と記録**: §6 での RI-02+RI-04 共起が EP-03a 単一投入で同時解消される構造的パターンを初記録。
- **VQ 階層逆転（出版インセンティブ vs. 科学的論理）**: EP-08a・EP-09a（VQ-2要件）の間接充填が EP-03a（VQ-1完全達成要件）より先行するという充填逆転パターンを Stage 4 で記録。
- **D-4 候補数ヘッダー誤記（minor bug）**: S2 ヘッダー "D-4 候補数: 9" は実際の候補数 8 と不整合。v18.2 以降で候補数の自動集計または記述後確認を推奨。

### 確認された未回復項目

- **R1（D-1 layered_structure の判断差）**: ⚠️ 軽微。v17「3層独立」と v181「単一串刺し」はいずれも一定の根拠がある境界判定。計算改善層（CCSD(T)/seg-QZP > SK+aug-cc-pVTZ for NiCO benchmark）は帰属主張から独立し得る。OI 登録しない（単一論文の境界判定差であり系統的パターン未確認）。
- **R2（confirmed_english_propositional の計算修飾欠如）**: ⚠️ 退行。v17 は "CCSD(T) calculations predict..." と明記し計算予測であることを担保していたが、v181 は "Noble gas atoms bind to NiCO..." という事実的記述語を使用。計算物理化学論文で predicted/calculated を propositional に明記することは引用精度に影響する。**OI-037 として追記。**
- **R3（E 節の framework_question → tool_question 縮退）**: ⚠️ 部分退行。v17 の問いは "without computed isotopic shift patterns" を明示して D-4 候補1と直接接続しており、E 節が分析の総括として機能していた。v181 の tool_question は NiCO 固有に限定され転用性が低下。OI-037 と同根として統合。

---

## Entry 041: v17 vs v181 — ngninn2004（NobleGas/References, full paper）

**比較日:** 2026-04-25
**評価論文:** Y. Ono, T. Taketsugu, J. Chem. Phys. 120, 6035–6040 (2004)「Theoretical study of Ng–NiN2 (Ng=Ar,Ne,He)」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

ngninn2004 は Ono & Taketsugu が同年の Ng–NiCO 論文（Ref. 10 = CPL 385, 2004）に続いて NiN2 系を対象とし、Manceron et al. 1998 の実験スペクトル帰属を計算的に挑戦した full paper。v17 で先行解析済み。今回 v181+s3v3+s4v3 で解析した。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|------|------|
| A | 2 | 2 |
| B | ~8（推算）| 14 |
| C | ~5（推算）| 5 |
| U | 3（U-1: critical, U-2: critical, U-3: high）| 3（同 severity）|
| SRG | 7（推算）| 5 + CLA 1 |
| D-4 候補 | 8 | 8 |

### D-4 候補の対応関係

| v17 | v181 | 対応状況 |
|-----|------|---------|
| 候補1（CCSD(T)信頼性診断が複合体に延長されない）| D-4-4（BE信頼性区間不在）| ✅ 統合 |
| 候補2（CASPT2にCP補正なし）| D-4-4（BE信頼性区間不在）| ✅ 統合 |
| 候補3（NiN2曲げ振動数の気相未検証）| D-4-1（非調和性自己矛盾）+ D-4-8（気相参照値不在）| ✅ 分割収録・拡充 |
| 候補4（非調和性補正の非対称性）| D-4-1（U-2 grounded）| ✅ 同一 |
| 候補5（同位体シフト定量基準なし）| D-4-3（全モードRMSD不在）| ✅ 拡充 |
| 候補6（He–NiN2曲げシフトに力定数分析なし）| **v181 D-4 に明示なし**| ⚠️ 部分退行 |
| 候補7（He > Ne異常順序の機構的説明不完全）| D-4-5（He > Ne anomaly）| ✅ 同一 |
| 候補8（TM再検討提案の設計原理不在）| D-4-6（実験的検証経路不在）| ✅ 再定式化 |

v181 新規追加（v17 に対応なし）:
- **D-4-2**（Ar 3p相関の前提条件的不在、grounded_in: U-1 critical）— CASPT2活性空間にAr 3pが含まれるかが未記述なのに、NPA証拠がAr 3p関与を示すという前提条件問題
- **D-4-7**（Ng–NiCO系との定量的比較不在 = Dropped Quantitative Benchmark、grounded_in: C-1）— 等電子性類推の定量的検証が欠落
- **D-4-8**（気相周波数参照値不在・0.5%シフト指針の未検証適用、grounded_in: B-10, B-4, A-1）— 前提的指針の適用可能性が問われない

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | He–NiN2曲げシフトの力定数分析不在 | 候補6として独立D-4候補（grounded_in: B-3; force constant Table Vがarのみ提供）| D-4 に明示なし（D-4-3・D-4-5が周辺領域を部分カバー）| ⚠️ 部分退行 |
| R2 | E節の問い文スコープ | framework_question; 問い文は「TM行列単離スペクトル全般」に汎用化（"Do noble gas matrices perturb..." ）| framework_question; 問い文はngninn2004固有（"Does the noble gas isolation medium form stable Ng–NiN2 compounds..."）| ⚠️ scope縮退（OI-037と同パターン）|

### 総合判定

**v181 > v17**

v181 の優位点：
1. **D-4-2（Ar 3p前提条件問題）の独立候補化**: v17 で B-1 止まりだったAr 3p活性空間問題が、NPA証拠との構造的矛盾（U-1 critical）として D-4-2 に昇格。これはスペクトル再帰属論証の計算基盤に直接触れる最重要追加。
2. **D-4-7（Dropped Quantitative Benchmark）**: Ng–NiCO（Ref. 10）との全Ng系列定量比較不在が CLA として明示的に追跡された。等電子性類推の有効性が3種Ng原子全体にわたって未検証である点を明示。
3. **D-4-8（気相参照値・0.5%指針の前提問題）**: 論文の全体的前提（0.5%以下のマトリクスシフト）の適用可能性が問われていない点を独立候補化。B-10 の reporting_omission を D-4 に昇格させた構造的貢献。
4. **SRG統合の精緻化**: v17推算7 SRG から v181 5 SRG + CLA への統合により、「CASPT2 BE信頼性」「CCSD(T)信頼性」「スペクトル帰属証拠」「実験的検証」「He>Ne異常」という主題的に一貫した5群が形成された。
5. **D-4-3（全モードRMSD不在）の構成**: v17 候補5（同位体シフトのみ）を B-5・B-9・B-11 の三項統合として拡充し、ν(NiN)の17 cm⁻¹改善が本文言及なしという選択的提示構造を明示。

### 正の副次効果

- **Stage 3 v3 §6（PRI-12/A5 + RI-04 共起パターン）**: 「認識済み近似の未補正適用」（著者自身が調和/基準振動数非同等を認識しながら補正なしに主張を閉じる）という RI-04 の「自己認識的サブタイプ」を §6 に提案。制度設計への新記録。
- **Stage 3 VQ 層別非対称性**: Layer A（計算的存在, VQ-2 qualified）と Layer B（スペクトル再帰属, VQ-1）の非対称性が同一論文に共存するパターンを canonical 事例として記録。
- **Stage 4 v3 「知識限界型未同定」パターン**: 第一群 EP（EP-03a, EP-07a）の充填論文が存在する可能性が高いにもかかわらず本モデルの知識で同定できない「知識限界型」未同定を明示記録。Ng–NiN2という niche 系での文献的孤立性の証拠として記録。

### 確認された未回復項目

- **R1（He–NiN2曲げシフト力定数分析の不在）**: ⚠️ 部分退行。v17 候補6が明示的に指摘したTable Vの非対称性（Ar–NiN2のみ力定数記載、He/Ne–NiN2は未記載）は、He–NiN2の358→361 cm⁻¹大幅増加という主張の力学的根拠に直接関わる。D-4-3（全モードRMSD）とD-4-5（He>Ne）が周辺をカバーするが、力定数の非対称性自体は D-4 に明示なし。→ **OI-038 として追記。**
- **R2（E節の問い文スコープ縮退）**: ⚠️ scope縮退。v17 の問い文（"Do noble gas matrices perturb..."）は遷移金属マトリクス単離分光全体への汎用的問いとして framework_question を体現していたが、v181 はこの論文固有に特化。OI-037 と同パターンのため新規 OI は作成せず OI-037 参照。

---

## Entry 042: v17 vs v181 — koukounas2008（NobleGas/References, full paper）

**比較日:** 2026-04-25
**評価論文:** C. Koukounas, A. Mavridis, J. Phys. Chem. A 2008, 112, 11235–11250「Ab initio Study of the Diatomic Fluorides FeF, CoF, NiF, and CuF」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

koukounas2008 は Athens グループ（Mavridis）が ScF–MnF 先行シリーズを完結させる形で FeF, CoF, NiF, CuF の 35 電子状態を MRCI + RCCSD(T) で体系計算した full paper。v17 で先行解析済みで、今回 v181+s3v3+s4v3 で再解析した。CoF 基底状態問題（A-1）と NiF MRCI 失敗（A-2）という2つの未解決 A 項目を持つ。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|------|------|
| A | 3（A-1, A-2, A-3）| 2（A-1, A-2）|
| B | ~8（推算）| 12 |
| C | ~3（推算）| 4 |
| U | 2（U-1, U-2）| 2（U-1: high, U-2: high）|
| SRG | 5（SRG-1〜5）| 4 + CLA 2 |
| D-4 候補 | 7 | 7（拡張上限適用、U-1/U-2 high × 2）|

### D-4 候補の対応関係

| v17 | v181 | 対応状況 |
|-----|------|---------|
| D4-1（CoF ground-state と LIF 実験の矛盾の非調停）| D-4-2（CoF基底状態の方法依存不確かさ定量的未提示）| ✅ 対応・C-2内的矛盾を v181 で追加 |
| D4-2（NiF MRCI 失敗の診断的分析の不在）| v181 D-4 に明示なし（A-2 として存在）| ⚠️ 退行 |
| D4-3（SOC 系統的不在と Ω 分解実験比較の非整合性）| D-4-1（SOC 省略と「よい一致」主張の有効性問題）| ✅ 対応（A-2 も統合） |
| D4-4（推薦値プロトコルと不確かさ区間の不在）| D-4-4（推奨値選択基準と Te→T₀補正の非明示）| ✅ 対応 |
| D4-5（Sc〜Cu シリーズ全体の MAE メタ分析の不在）| D-4-7（MF 系列横断補正効果の非体系的提示）| ✅ 部分対応（MAE/RMSD 定量指標の観点は弱化）|
| D4-6（高イオン性統一原理と eccentric d 電子の相克問い）| v181 D-4 に対応なし | ⚠️ 退行 |
| D4-7（FeF De 高温質量分析との熱力学的循環問い）| v181 D-4 に対応なし | ⚠️ 退行 |
| （v17 にない）| D-4-3（ベンチマーク精度根拠4要素の組織的欠如、SRG-3）| ✅ v181 新規 |
| （v17 にない）| D-4-5（NiF 基底状態割り当て前提欠如、U-2 独立記録）| ✅ v181 新規 |
| （v17 にない）| D-4-6（Mulliken 電荷のイオン性主張の方法論的脆弱性）| ✅ v181 新規 |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | NiF MRCI 失敗診断の D-4 候補化 | D4-2 として独立（A-2, B-4, C-3 grounded；「なぜ MRCI が失敗するか」という問いを D-4 として記録）| A-2 として存在するが D-4 候補化なし | ⚠️ 退行 |
| R2 | 高イオン性統一原理と eccentric d 電子の相克問い | D4-6 として独立（A-1, A-2, B-1 grounded；複数 SRG を横断する統合的解釈問い）| v181 D-4 に対応なし | ⚠️ 退行 |
| R3 | FeF De 熱力学的循環問い | D4-7 として独立（C-6 grounded；計算値で算出した実験 De で計算値を検証する循環）| v181 D-4 に対応なし | ⚠️ 退行（low severity）|
| R4 | confirmed_english_question の鋭さ | 「MRCI vs CC で定性差が生じるとき診断基準は何か」（手法間矛盾解決への具体的問い）| 「SOC/CBS/不確かさ省略時の精度限界とは」（構造的・広い問い）| 🔄 変化（鋭さ vs 構造的広さのトレードオフ）|

### 総合判定

**v181 > v17**（3 退行があるが、v181 の新規追加と新機能適用が上回る）

v181 の優位点：
1. **D-4-5（U-2 独立記録保護）**: NiF X²Π/A²Σ⁺ の 101 cm⁻¹ 差 vs SOC 安定化 251.26 cm⁻¹ という具体的数値的矛盾を U-2 として独立保護し D-4-5 に昇格。v18.1 multi-critical U-item protection rule の機能確認。
2. **D-4-3（SRG-3 の精度根拠4要素組織化）**: BSSE・CBS 外挿・Davidson+Q 検証・不確かさ区間という4欠如を SRG-3 として束ね、ベンチマーク論文の精度根拠不在パターンとして系統的に記述。v17 D4-4 で一部のみ扱われていた問いを拡充。
3. **CLA-2（内的矛盾型 RI-09 変形の検出）**: 「先行理論研究なし」主張と同段落の ref 29（Freindorf & Marian 1993）引用という内的矛盾が CLA-2 として独立検出。v17 には存在しない新規検出。Stage 3 で RI-09 の新サブタイプ「Internal-citation inconsistency」として制度化。
4. **D-4-6（Mulliken 電荷の独立化）**: v17 D4-6 が「高イオン性統一原理の限界」という広い問いの一部として電荷問題を内包していたのに対し、v181 は方法論的脆弱性（Mulliken vs NPA/QTAIM）に特化した独立 D-4 候補として精密化。
5. **SRG 構造の精緻化**: v17 の 5 SRG から v181 の 4 SRG + CLA 2 への整理により、SOC 不在・CoF 基底状態・ベンチマーク完全性・比較基準という主題的に一貫した4群が形成された。

### 正の副次効果

- **PRI-12 A5 新代表事例の登録**（Stage 3 §6）: ic-MRCI × Davidson(+Q) × DKH2 × BSSE × コア相関という5層近似スタックが PRI-12 A5 の計算化学 benchmark 論文への新適用事例として登録された。
- **RI-04「精度錯視」変形の検出**（Stage 3 §6）: 最高レベル計算値（−57 cm⁻¹）をその不確かさ（同論文の低レベル計算との 520 cm⁻¹ 乖離）から切り離して報告するパターンを「precision illusion」として Codebook 追記候補に登録。
- **VQ 逆転パターンの新事例**（Stage 4 §D/E）: 低 VQ 要件 EP（EP-08a、RI-08）が第三群（インセンティブ構造的未充填）で、高 VQ 要件 EP（EP-04a、RI-04）が第一群（追跡可能）という出版インセンティブ vs. 科学的論理の逆転を計算化学 benchmark 論文で初記録。

### 確認された未回復項目

- **R1（NiF MRCI 失敗診断の D-4 候補消失）**: ⚠️ 退行。v17 D4-2 は「なぜ MRCI が失敗するのか（活性空間飽和 vs. 参照空間不足 vs. ic truncation）という診断的問い」を D-4 として記録していたが、v181 では A-2 の「制限として認識」止まりで D-4 候補化されていない。計算手法の失敗機構を問う D-4 候補は計算化学ベンチマーク論文での UQS 分析において系統的に重要。→ **OI-039 として追記。**
- **R2（高イオン性統一原理と eccentric d 電子の相克問いの消失）**: ⚠️ 退行。v17 D4-6 は複数 SRG を横断する「統一原理の説明力の限界」という統合的解釈問いとして価値があった。v181 では Mulliken 電荷問題（D-4-6）に置換されており、この統合的問いは消失。他の計算化学ベンチマーク論文での再現確認後に OI 登録を判断する（現時点では新規 OI 登録しない）。
- **R3（FeF De 熱力学的循環問い）**: low severity、単一エージェント（V2-Q2）由来。OI 登録しない。
- **R4（confirmed_english_question の変化）**: 🔄 どちらが優位とは言えない変化。OI 登録しない。

---

## Entry 053: v17 vs v181 — arptco2018（NobleGas/References, full paper）

**比較日:** 2026-04-25
**評価論文:** Y. Ono, K. Yagi, T. Takayanagi, T. Taketsugu, Phys. Chem. Chem. Phys. 2018, 20, 3296–3302「Fundamental peak disappears upon binding of a noble gas」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

arptco2018 は直接 VCI 法を Ar–PtCO に初めて適用し、Ar 行列実験における 917 cm⁻¹
バンドを Pt–C–O 曲げ倍音への誤帰属と同定した full paper。v17 で先行解析済みであり、
今回 v181+s3v3+s4v3 で再解析した。本論文は著者グループ（Taketsugu 教授ら）が自ら
発表した論文である。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| A | 2 | 0 |
| B | 8 | 14 |
| C | 8 | 5 |
| U | 5 | 6 |
| SRG | 6 | 5 + CLA 4 |
| D-4 候補 | 7 | 8 |

### D-4 候補の対応関係

| v17 | v181 | 対応状況 |
|-----|------|---------|
| D4-1（VCI計算の定量的信頼性未検証, B-1/B-3/B-5）| D-4-3（VCI数値収束未検証, B1/B2/B3/B9）| ✅ 拡充（B9追加、SRG-1+SRG-2統合） |
| D4-2（実験的検証の体系的不在, U-1/U-2/B-6/C-6）| D-4-1（「解決宣言」の実験的根拠不在, U5/U4/U6/B12）| ✅ 再定式化・強化（3/3収束に昇格） |
| D4-3（Ar–PtCO以外への射程, U-4/A-1/C-4）| D-4-4（Ar-NiCO類推の非対称性, U1/C2）| ✅ 部分対応（NiCO側カバー; PdCO forgotten deferral は消失） |
| D4-4（双極子面の定量的分解, B-7/U-3/B-2）| D-4-6（双極子モーメント微分の数値不在, B8）| ✅ 対応（U-3の倍音機構問題は縮小） |
| D4-5（単一Arモデルの正当化, A-2/B-4/C-5）| D-4-2（孤立複合体モデルと行列環境の乖離, U2/C1）| ✅ 対応（A-2→U2 self-contradictory absence昇格） |
| D4-6（三倍音成分と実験1バンドの不整合, U-2/B-6）| **v181 D-4 に明示なし**| ⚠️ 退行（R1） |
| D4-7（Ar–Pt結合の化学的性格 "strong van der Waals", U-5/C-3）| **v181 D-4 に明示なし**| ⚠️ 退行（R2） |

v181 新規追加（v17 に対応なし）:
- **D-4-5**（CCSD(T)単参照妥当性前提不在、grounded_in: B4/U3, PRI-12 A8）— T1 診断が未報告という genuine new item
- **D-4-7**（VPT2/cc-VSCF比較不在、grounded_in: C3）— 方法論的優位性の定量的未検証
- **D-4-8**（ref.25との計算レベル非対称性、grounded_in: B5/B10/C4）— QCISD(T)/DK と CCSD(T)/ECP の系統差未評価

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | 三倍音成分（905, 909, 905 cm⁻¹）対一実験バンド（917 cm⁻¹）の内部整合性問題 | U-2（medium）+ D4-6として独立 D-4 候補 | B6 が spectrum comparison 定量性として部分カバーするが、「なぜ3成分が1バンドに対応するか」という specific question は D-4 から消失 | ⚠️ 退行 |
| R2 | Ar–Pt結合の化学的性格（"strong van der Waals" ラベルの根拠問い）| U-5（medium, 1/3収束）+ D4-7として独立 D-4 候補 | v181 U・D-4 に明示なし（低収束・低severity のため D-4 昇格優先度外と推定） | ⚠️ 退行（低impact） |

### 総合判定

**v181 > v17**

v181 の優位点：
1. **D-4-1（「解決宣言」の実験的根拠不在）の精密化**: v17 D4-2 では U-1/U-2/B-6/C-6 の混在した4項目に分散していた実験検証不在問題が、v181 では B12/U5（3/3 agent 収束）を最高優先ピボットとして U4・U5・U6・B12 の4要素に構造化され、RI-07 Fatal 判定（Stage 3）に直接接続する。
2. **D-4-5（T1 診断の前提条件的不在, PRI-12 A8）の新規追加**: v17 には全く対応がなかった。Pt の近縮退 5d 軌道と単参照 CCSD(T) の妥当性検証の欠如は、PES 信頼性問題として Stage 3 の CLA に直接昇格した。
3. **A-2（Monte Carlo省略）→ U2（self-contradictory absence）への概念的格上げ**: v17 では "deferral" 項目 A-2 として低優先だったが、v181 では同一著者グループが確立した手法を採用しなかったという自己矛盾的不在として D-4-2 の核に昇格。
4. **SRG 構造の精緻化（6→5+CLA4）**: v17 SRG-3（実験検証）と SRG-5（スペクトル比較）の重複解消。CLA 4件の導入により、SRG から外れた個別論点が明示的に追跡される。
5. **VCI収束クラスターの包括化**: v17 SRG-1（B-1/B-3）に対し、v181 SRG-1+SRG-2（B1/B2/B3/B9）として PES/DMS レベル不整合が独立 SRG-2 に分離されつつ D-4-3 に統合。

### 正の副次効果

- **Stage 3 v3（PRI-12 A5代表事例の確立）**: CCSD(T) PES × CCSD DMS × 3次カップリング × SoQN<6 VCI という4層近似積み重ねが、「計算-実験一致を全層の収束証拠として機能させる（self-convergence by agreement）」PRI-12 A5 の教科書的事例として §6 に記録された。
- **Stage 3 v3（RI-06後退型モデル輸入変種の提案）**: 「参照済み精緻化手法を用いずに単純化モデルを採用」という RI-06 の新変種が §6 で提案された。
- **Stage 3 v3（"closed claim without experimental closure" パターン）**: A 項目ゼロ + "solved" 宣言の共起が RI-07 Fatal の強シグナルとなるパターンが §6 に記録された。
- **Stage 4 v3（自己充填可能性の高い第一群EP）**: EP-07a（同位体シフト計算）と EP-06a(NiCO)（Ar-NiCO VCI）が著者グループによる自己充填候補として明示され、「niche 分野での著者自己充填動態」が S4 の知見として記録された。

### 確認された未回復項目

- **R1（三倍音成分対一実験バンドの内部整合性）**: ⚠️ 退行。Table 2 の三倍音成分（905 cm⁻¹ × 2, 909 cm⁻¹; intensities 0.15, 0.11, 3.14 km/mol）と実験一バンド（917 cm⁻¹）の対応が論文本文で議論されないという内部整合性問題が D-4 から消失した。→ **OI-039 として追記。**
- **R2（Ar–Pt結合の "strong van der Waals" ラベル問題）**: ⚠️ 退行（低impact）。低収束（1/3）・中 severity であり、v181 の D-4 優先順位内に収まらなかったと推定される。新規 OI は不要（D-4 候補数上限 8 での自然な排除）。

---

## Entry 043: v17 vs v181 — frenking2021（NobleGas/References, full paper）

**比較日:** 2026-04-25
**評価論文:** G. Frenking, I. Fernández, N. Holzmann, S. Pan, I. Krossing, M. Zhou, JACS Au 2021, 1, 623–645「Metal−CO Bonding in Mononuclear Transition Metal Carbonyl Complexes」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3+s4v3 解析完了後に自動比較）

### 背景

frenking2021 は DFT/EDA-NOCV を群2〜10の単核カルボニル錯体に系統的に適用し、
DCDモデルの有効性を定量的に主張した JACS Au フルペーパー（23頁）。アルカリ土類
M(CO)₈（Ca/Sr/Ba）のDCD検証とCa/Sr/Baの遷移金属再分類提案が論争的中心。
v17 で先行解析済みであり、今回 v181+s3v3+s4v3 で再解析した。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| B | （記録なし） | 15 |
| C | （記録なし） | 4 |
| U | （記録なし）| 8 |
| SRG | （記録なし） | 7 |
| D-4 候補 | 8 | 9（拡張上限） |
| high_convergence_high_gap | なし（フォールバック） | B-10（D-4-6最優先） |

### D-4 候補の対応関係

| v17 候補 | v181 D-4 | 対応状況 |
|---|---|---|
| 候補1: EDA-NOCV相関の説明力非対称性（「相関≠説明」を自身に不適用） | **不在**（U-1背景に後退） | ⚠️ 退行 R1 |
| 候補2: EDA-NOCV断片選択の基準不在 | D-4-1（断片選択非中立性） | ✅ 対応 |
| 候補3: 計算プロトコル多層不整合・感度分析不在 | D-4-4（ΔEmetahybrid除外） | ✅ 部分対応（B-4特化→精緻化） |
| 候補4: 周期表再分類のカルボニル限定性 | D-4-9（操作的境界の不在） | ✅ 対応（U-7/B-14活用で精緻化） |
| 候補5: 実験検証の単一指標依存 | D-4-6（最優先、B-10 high_convergence_high_gap） | ✅ 改善（B-10最優先化） |
| 候補6: 「イオン結合は分子に存在しない」定義的主張 | **不在** | ⚠️ 退行 R2 |
| 候補7: BaのECPとd軌道整合性 | B-3に吸収、D-4不在 | ⚠️ 退行 R3（軽微） |
| 候補8: refs 128–131の不統合 | **不在** | ⚠️ 退行 R3 |
| — | D-4-2（DCD反証不可能性） | ✅ 新規 |
| — | D-4-3（AIM電荷循環的検証） | ✅ 新規 |
| — | D-4-5（M(CO)₈直接CO–CO検証不在） | ✅ 新規（v181 U-3 活用） |
| — | D-4-7（ν(M–C)未検証） | ✅ 新規（v181 U-5 活用） |
| — | D-4-8（配位数間比較可能性） | ✅ 新規（v181 U-8 活用） |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|---|---|---|---|
| R1 | 「相関は説明でない」の論理的非対称性問い（v17候補1） | 独立 D-4 候補（最優先、U-1 grounded） | D-4 不在（U-1 背景説明に後退） | ⚠️ 退行（medium） |
| R2 | 「イオン結合は分子に存在しない」定義的主張の問い（v17候補6） | 独立 D-4 候補（U-2 grounded） | D-4 不在（U-2 は D-4-3 の grounded_in に含まれるが焦点消失） | ⚠️ 退行（medium） |
| R3 | refs 128–131の不統合（v17候補8）+ BaのECP問題（v17候補7） | 2つの独立 D-4 候補 | D-4 不在（C-1, B-3 に残存するが D-4 未昇格） | ⚠️ 退行（low × 2） |

### 総合判定

**v181 > v17**

v181の優位点：
1. **B-10の high_convergence_high_gap 特定と D-4-6 最優先化**: v17 では high_convergence_high_gap 候補なし（フォールバック適用）だったが、v181 では V2（実験系エージェント）が B-10（気相vs行列単離Δν比較の問題）を high severity で独立指摘し、温度差 medium（V1=low, V2=high）を生成。D-4 の優先順位付けが根本的に改善した。
2. **v18.1 新規U項目ルールによる5新規 D-4 候補**: D-4-2（DCD反証不可能性/U-4）、D-4-3（AIM循環性/U-2）、D-4-5（M(CO)₈直接検証/U-3）、D-4-7（ν(M–C)/U-5）、D-4-8（配位数間比較/U-8）は v18.1 の inter-system comparability U 規則と multi-critical U 独立記録ルールによって生成された質の高い候補群。
3. **confirmed_english_question の精緻化**: v17「複数手法のどれが物理的に有効か」という広い方法論問いから、v181「EDA-NOCVはDCDのmodel-neutral validationを提供するか、それとも断片選択の循環性が独立検証を妨げるか」という論文固有の核心的問いへ絞り込み成功。

退行（未回復）：
- **R1（medium）**: v17候補1「相関は説明でない」を自身のEDA-NOCV相関に適用しない論理的非対称性の問いが消失。→ **OI-040 として追記**
- **R2（medium）**: v17候補6「イオン結合は分子に存在しない」という定義的主張問いが消失。→ OI-040 に包含
- **R3（low × 2）**: refs 128–131不統合・Ba ECP問題が D-4 未昇格。影響は軽微。

### 正の副次効果

- **Stage 3 v3（PRI-12/A3代表事例の確立）**: EDA-NOCVがDCDのσ/π二項を操作的に定義するよう設計されており、EDA-NOCVによる「DCD検証」がconstruct-validity circular（A3）となるという指摘は §6 でCodebook登録提案として記録。
- **Stage 3 v3（RI-01クロスフェーズ比較サブタイプの提案）**: 「気相DFT計算と行列単離/溶液/結晶IR実験の無補正混在比較」がRI-01の新サブタイプとして§6に記録された。計算化学分野で広汎なパターン。
- **Stage 4 v3（VQ階層逆転パターンの確認）**: 低VQ要件（RI-01: 相補正）が技術的容易にもかかわらず出版インセンティブ欠如で未充填、高VQ要件（RI-03/06: 直接観測・独立検証）が活発に充填されるというVQ逆転パターンを確認。

### 確認された未回復項目

- **R1/R2（論理的非対称性問い・定義的主張問い）**: ⚠️ 退行（medium）。v17候補1「相関≠説明の非対称的適用」は論文の知的自己矛盾を最も鋭く捉えた問いであり、v181では U-1 の背景説明に後退した。v17候補6（イオン結合定義問題）も論争の前提衝突として独自の価値があった。→ **OI-040 として追記**。
- **R3**: 低impact。D-4 候補数が9（上限拡張）であることを考慮すると、refs 128–131問いの D-4 不採用は優先順位の合理的帰結とも読める。新規 OI は不要。

---

## Entry 044: v17 vs v181 — gerry2000b（NobleGas/References, full paper）

**比較日:** 2026-04-26
**評価論文:** C.J. Evans & M.C.L. Gerry, J. Chem. Phys. 112, 1321–1329 (2000)「The microwave spectra and structures of Ar–AgX (X=F,Cl,Br)」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

gerry2000b は FTMW 回転分光によって Ar–AgF, Ar–AgCl, Ar–AgBr を初めて観測・構造決定した
フルペーパー。中心的主張は Ar–Ag 結合が「van der Waals 結合と化学結合の境界線付近」にある
という解釈的結論。v17 で先行解析済みであり、今回 v181+s3v3+s4v3 で再解析した。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| D-4 候補 | 5 | 8（拡張上限: high severity U項目 2件） |
| high_convergence_high_gap | なし（フォールバック） | なし（フォールバック） |

### D-4 候補の対応関係

| v17 候補 | v181 D-4 | 対応状況 |
|---|---|---|
| 候補1: van der Waals/化学結合の指標体系で決定不能か | D-4-1（Ag NQCC自己矛盾）+ D-4-2（EDA不在）に分解 | ✅ 分解・精緻化 |
| 候補2: BSSE未補正のDeは境界議論に影響するか | D-4-3（BSSE不在） | ✅ 対応 |
| 候補3: 典型的van der Waals参照クラスの代表性 | **D-4 不在**（D-2 competitive_positioning に吸収） | ⚠️ 退行 R1 |
| 候補4: Ag核四重極モーメント不在の構造的バイアス | D-4-1（Ag NQCC自己矛盾）として精緻化 | ✅ 対応・改善 |
| 候補5: Ab initio 計算が Ar–AgBr を含まない理由 | D-4-4（Ar–AgBr ab initio 不在） | ✅ 対応 |
| — | D-4-5（同位体種帰属の未検証） | ✅ 新規 |
| — | D-4-6（Ar–Ag距離ハライド依存性・遮蔽モデル軌道的根拠不在） | ✅ 新規 |
| — | D-4-7（[Cl–Ag–Cl]⁻参照計算の未検証性） | ✅ 新規（v17 では B 項目止まり） |
| — | D-4-8（Cu/Au延期と境界線主張の自立性） | ✅ 新規（A1↔U2ピボット明示化） |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|---|---|---|---|
| R1 | 「典型的 van der Waals 参照クラス」の代表性問いの D-4 候補化 | 独立 D-4 候補（cand-3, grounded_in: B-3, C-2） | D-4 不在（D-2 competitive_positioning に吸収） | ⚠️ 退行（low） |

### 総合判定

**v181 > v17**

v181 の優位点：
1. **D-4 候補数 5→8（+3）**: 同位体種帰属の統計的未検証（B4/B14/B15）、Ar–Ag 距離のハライド依存性とその軌道的根拠不在（B13/B18/B23）、Cu/Au 延期と境界線主張の自立性（A1/U2/U1）が新規候補として生成。
2. **[Cl–Ag–Cl]⁻参照計算を独立 D-4 候補に昇格**: v17 では B 項目（B-7）止まりだった未検証 MP2 参照計算が、v181 では D-4-7 として独立化。
3. **A1↔U2 ピボット分析の明示化**: Cu/Au 実験延期（A1）が「論文が『はるかに敏感な尺度』と自認する金属核 NQCC の先送り」として U2 と接続され、「主張を先行させ検証を後続論文に委ねる」構造として明示化。
4. **D-2 timing pressure の根拠化**: A1（Cu/Au 延期宣言）と B1（Ar–AgBr 計算不在）を連動させ、投稿時点での実験・計算プログラムの未完性として記述。
5. **D-3 field_competition_state の直接引用化**: 論文テキスト "very sparse" を明示引用し、外部推論への依存を低減。

退行（未回復）：
- **R1（low）**: v17 cand-3「Ar–NaCl 一報のみによる『typical van der Waals complex』定義の循環性」が D-4 に不在。内容は D-2 競合分析に残存するが独立した問いとして昇格していない。→ **OI-041 として追記**。

### 確認された未回復項目

- **R1（参照クラス代表性問い）**: ⚠️ 退行（low）。v17 候補3「典型的 van der Waals 複合体の参照クラスが Ar–NaCl 一報のみで定義されており、比較の代表性が循環的」という問いが D-4 に不在。→ **OI-041 として追記**。

---

## Entry 045: v17 vs v181 — zhou2001（NobleGas/References, Chemical Reviews review）

**比較日:** 2026-04-26
**評価論文:** M. Zhou, N. Moody, Jr., D. A. Andrews, C. W. Bauschlicher, Jr. — Chem. Rev. 2001, 101, 1931–1961「Vibrational Spectra of Transition Metal Carbonyls in Noble Gas Matrices」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

zhou2001 は第一〜第三遷移系列全金属のカルボニル中性体・カチオン・アニオンのC–O伸縮振動数を体系的にまとめた31ページのChemical Reviews総説。v17 で先行解析済み。今回 v181（+s3+s4v3）で再解析した。先行解析論文との主要差異：v181 では4エージェント展開（V1: マトリクス単離IR分光、V2: 計算量子化学、V3: 系統的レビュー方法論、V4: 物理無機化学）を適用。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| A | 3（A-1: 遠赤外M-C振動数, A-2: 気相EA測定, A-3: 触媒電荷プローブ）| 3（A1: 遠赤外M-C, A2: 気相EA, A3: 触媒電荷プローブ）|
| B | 9（推算）| 15 |
| C | 5（C-1〜C-5）| 5（C1〜C5）|
| U | 2（U-1: FeCO行列依存スピン状態, U-4: 分子間比較可能性前提）| 4（U1: FeCO行列スピン, U2: RhCO三点校正閾値, U3: IPモデル矛盾, U4: 分子間比較可能性）|
| SRG | 5（SRG-1〜SRG-5）| 6（SRG-1〜SRG-6）|
| D-4 候補 | 7 | 8（拡張上限適用、high severity U項目4件）|

### D-4 候補の対応関係

| v17候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| 候補1（行列誘起電子状態逆転の体系的調査不在, U-1/U-2/A-4/B-7/B-8）| PRI-1（FeCO行列スピン状態逆転の自己矛盾, U1/B1）| ✅ 対応（スコープ縮小・焦点精緻化）|
| 候補2（電荷プローブ外挿の不確かさ, A-3/B-6/U-4）| PRI-4（触媒局所電荷プローブの閾値信頼性+比較可能性, A3/B3/U2/U4）| ✅ 対応・強化（U2+U4 C11保護）|
| 候補3（DFT方法論の報告不完全性, B-3/B-4/B-5/B-9）| PRI-3（DFT ±1%精度主張の体系的検証不在, B5/B6/B7/B10）| ✅ 対応・4要素統合化|
| 候補4（M⁺–CO GIBMS結合解離エネルギー–振動数相関の不在, C-1/C-2/A-1）| **v181 D-4 に対応なし** | ⚠️ 退行 R1 |
| 候補5（スピン禁制CO付加の体系的マッピング不在, B-1/U-3）| **v181 D-4 に対応なし** | ⚠️ 退行 R2（B1として存在） |
| 候補6（電子親和力DFT計算の実験的検証不十分, A-2/C-3/B-5）| PRI-7（アクチニドカルボニル割り当ての不確実性, B4/B8）として部分対応| ⚠️ 部分対応（EAの角度は後退）|
| 候補7（アブレーションプルーム内イオン分子反応識別, B-2/U-3）| PRI-5（割り当て信頼性の階層化基準の不在, B2/B9/B11/B15）に吸収| ✅ 吸収（射程は広く、機構的特定は弱化）|
| （v17になし）| PRI-2（IPモデル vs Figure 18双峰型非単調パターンの矛盾, U3/B12）| ✅ 新規（U3 self-contradictory absence）|
| （v17になし）| PRI-6（σ/π定量的分解と先行文献の非関与, B12/C5）| ✅ 新規 |
| （v17になし）| PRI-8（先行DFTベンチマーク文献の定量的非関与, C1/C5/B5）| ✅ 新規 |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | M⁺–CO GIBMS 結合解離エネルギーと振動数の定量的相関の不在（候補4）| C-1（GIBMS BDE 文献）・C-2（refs 13-14 Weitz）・A-1（遠赤外M-C）を統合して「π逆供与解釈の熱力学的検証が放棄されている」という独立D-4候補として展開。key_quote: [REDACTED: verbatim source quotation; see `loc:`] | C1 が PRI-8（先行DFTベンチマーク非関与）のgrounded_inに含まれるが、実験的D₀(M⁺–CO)値と振動数の定量的対照という角度は D-4 に存在しない | ⚠️ 退行（medium）|
| R2 | スピン禁制CO付加反応の体系的マッピング（候補5）| B-1・U-3 grounded として「Fe(CO)₄→Fe(CO)₅のスピン禁制速度定数2桁低下が示されるが、全TM系のスピン多重度横断マッピングは行われていない」という D-4 候補として展開 | B1（FeCOスピン状態, convergence 3/4）として S1 に存在するが、D-4 候補として展開されず | ⚠️ 退行（low）|

### 総合判定

**v181 > v17**

v181 の優位点:
1. **PRI-2（IPモデルvsFigure 18, U3 self-contradictory absence）の新規展開**: Section IIIの結合フレームワークが単調なIP–振動数相関を予測するが、Figure 18 の実測値が双峰型を示すという内部矛盾を U3（self-contradictory absence, high severity）として捕捉し、D-4 最優先候補に昇格。v17 には存在しない新規かつ高価値な候補。
2. **4つのU項目の独立D-4記録（C11保護）**: v17では U-1（FeCO行列依存）と U-4（比較可能性前提）の2件だったが、v181では U1-U4（FeCOスピン逆転/RhCO三点校正/IPモデル矛盾/比較可能性）の4件全てが C11 ルールで独立 D-4 候補として保護された。
3. **PRI-6（σ/π定量的分解）の新規展開**: EDAやNBO解析による σ/π 寄与の定量的分解が引用されながら利用されていないという問いを独立 D-4 候補として展開。v17 には対応なし。
4. **PRI-4の強化（U2+U4同時保護）**: v17 候補2は電荷プローブ外挿の不確かさを単一候補として記述していたが、v181 PRI-4 は三点校正の閾値信頼性（U2）と分子間比較可能性前提（U4）を両方明示的に統合し、「どの配位環境まで有効か」という二層の問いとして精緻化。
5. **confirmed_english_propositional の精度向上**: v17は触媒電荷プローブ側面を前面に出した ("frequency scale for estimating local charge") のに対し、v181は論文の実際の一次貢献（全電荷状態・全TM行にわたる振動数測定とデータベース構築）を正確に記述した。

退行（R1 medium, R2 low）はいずれも S1 B/C 項目には記録されており、D-4 昇格が起きなかった構造的問題（R1: GIBMS 実験的角度は SRG なし・single-agent C 項目のため優先度低；R2: B1 として収束しているが D-4 昇格基準を満たすほど温度が高くない）に帰因する。

### 正の副次効果

- U3（IPモデル自己矛盾）のself-contradictory absence ruleが総説論文（31頁）に適用され機能確認——「レビュー論文自身の結合モデルと掲載データの矛盾」型の新規パターン
- SRG-6（先行ベンチマーク非関与）が PRI-8 を通じて化学計算論文の典型的パターンとして確立
- 4エージェント展開（V1-V4）が大型総説論文（31頁）で適切に機能し、V4（物理無機化学）が σ/π 定量化（PRI-6）という独自候補を生成したことを確認

### 確認された未回復項目

- **R1（M⁺–CO GIBMS BDE-振動数定量相関の不在）**: ⚠️ 退行（medium）。v17 が捉えた「気相実験で測定されたD₀(M⁺–CO)とTable 4の振動数を定量的に対照させる分析の欠如」という問いが v181 D-4 に存在しない。C1/C2 の grounded_in は PRI-8 に配分されており、実験熱力学角度の D-4 化パスが消失。→ **OI-041 として追記**
- **R2（スピン禁制CO付加マッピング）**: low impact。B1 には存在する。独立 OI は不要。

---

## Entry 046: v17 vs v181 — zhou1999（NobleGas/References, J. Phys. Chem. A 1999）

**比較日:** 2026-04-26
**評価論文:** Mingfei Zhou, Lester Andrews — J. Phys. Chem. A 1999, 103, 7773–7784「Reactions of Laser-Ablated Co, Rh, and Ir with CO: Infrared Spectra and Density Functional Calculations of the Metal Carbonyl Molecules, Cations and Anions in Solid Neon」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

zhou1999 は第9族遷移金属（Co/Rh/Ir）のカルボニル中性体・カチオン・アニオンをネオン行列中で初めて分光した12頁のJ. Phys. Chem. A原著論文。v17 で先行解析済み。今回 v181（+s3v3+s4v3）で再解析した。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| A | 3（A-1: 気相周波数, A-2: 電子親和力, A-3: 触媒電荷プローブ）| 2（A-1: 電子親和力, A-2: 気相周波数）|
| B | 9（B-1: ΔE/ΔH₀未明示, B-2: S/N未報告, B-3: バンド強度不在, B-4: 光分解線量未記録, B-5: CCl₄閾値未定量, B-6: Rh(CO)₃乖離, B-7: 溶媒補正不在, B-8: スケールファクター変動, B-9: Rh(CO)₄混合同位体不在）| 7（B-1〜B-7）|
| C | 2実質（C-1: GIBMS BDE refs, C-7: 溶媒系refs）| 4（C-1〜C-4: refs 17-21/9-10/52-53を含む明示的追加）|
| U | 3（U-1: Rh(CO)₄混合同位体自己矛盾, U-2: ²Σ⁺周波数未報告, U-3: カチオン混合同位体不可能）| 2（U-1: 電荷-周波数自己一致テスト不在, U-2: ²Σ⁺周波数未報告）|
| SRG | 5（SRG-1〜SRG-5）| 4（SRG-1〜SRG-4）|
| D-4 候補 | 8 | 8（同数、内容は再構成）|
| E scope_type | framework_question | tool_question |

### D-4 候補の対応関係

| v17候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| D-4-1（DFTエネルギー型未明示+スピン状態帰属, grounded: B-1/B-6/U-2）| D-4-x（²Σ⁺/²Δ循環的根拠; SRG-3）| ✅ 部分対応（エネルギー型ΔE/ΔH₀の問いは消失）|
| D-4-2（実験バンド強度の体系的不在; SRG-2, grounded: B-2/B-3）| **v181 D-4 に対応なし** | ⚠️ 退行 R2 |
| D-4-3（CCl₄診断の定量的根拠欠如, grounded: B-5/B-6）| v181 D-4（CCl₄質量収支+光分解機構; SRG-4）| ✅ 部分対応（角度は再構成）|
| D-4-4（Rh(CO)₃ 39 cm⁻¹ DFT乖離, grounded: B-6/B-8）| **v181 D-4 に対応なし** | ⚠️ 退行 R3 |
| D-4-5（スケールファクター変動パターン, grounded: B-8/A-1）| v181 B-2（カチオン2–3%系統過大評価）として B 項目に吸収 | ⚠️ D-4 未昇格（low impact）|
| D-4-6（ネオン行列→触媒系外挿可能性, grounded: A-3/B-7/C-1/C-7）| v181 D-4-1（電荷-周波数自己一致テスト; U-1/B-5）| ✅ 焦点精緻化（触媒外挿→内部一貫性）|
| D-4-7（Rh(CO)₄中性+カチオン証拠非対称, grounded: B-9/U-1/U-3）| v181 B-3+SRG-2として収録; U-3 消失 | ⚠️ 退行 R4（U-3=カチオン証拠非対称が独立記録から消失）|
| D-4-8（気相周波数不在+検出感度下限未示; grounded: A-1/B-2）| v181 A-2（気相周波数未確定; deferred）として A 項目に収録 | ✅ 部分対応（感度下限の問いは消失）|
| （v17になし）| v181 D-4-3（4K行列でのアニオン分布の熱力学vs速度論）| ✅ 新規 |
| （v17になし）| v181 D-4-4（光分解によるアニオン種間変換機構の不在）| ✅ 新規 |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | DFT相対エネルギーの型（ΔE vs ΔH₀）未明示（v17 B-1）| B-1として独立記録し、D-4-1（スピン状態帰属可検証性）の中核根拠として機能。key_quote: [REDACTED: verbatim source quotation; see `loc:`] — この主張が ΔE か ΔH₀ かが不明で検証不能 | v181 B 項目に対応なし。スピン状態問いは SRG-3/U-2 で記録されるが ΔE/ΔH₀ の問いは消失 | ⚠️ 退行（medium）|
| R2 | 実験バンド強度の体系的不在（v17 B-3 + SRG-2 + D-4-2）| SRG-2「Band intensity reporting absent from experimental tables」として独立SRGを構成し、D-4-2（証拠構造の一方向性）へ展開。「DFT計算強度と観測強度の非対称な開示が構造帰属を一方向証拠にする」という問いを完全展開 | v181 B/SRG/D-4 のいずれにも対応なし | ⚠️ 退行（medium）|
| R3 | Rh(CO)₃ DFT周波数乖離 39 cm⁻¹の独立記録（v17 D-4-4）| D-4-4として「C₂ᵥ構造帰属の根拠・他構造異性体との比較不在・虚振動数確認なし」を含む完全展開。key_quote: [REDACTED: verbatim source quotation; see `loc:`] | B-3/B-6 として記録あるが D-4 候補として展開なし | ⚠️ 退行（medium）|
| R4 | Rh(CO)x⁺カチオンの混合同位体観測不能・証拠非対称（v17 U-3）| U-3「band congestion precludes observation of mixed isotopic counterparts」として U 項目に独立記録。D-4-7 でカチオン証拠非対称として展開 | U-3 消失。カチオン証拠非対称は明示的に展開されず | ⚠️ 退行（low）|
| R5 | E scope_type の質的変化 | framework_question: "Can carbonyl stretching frequency agreement between DFT calculations and matrix infrared observations reliably determine ground electronic states when the same DFT calculations give a conflicting energy ordering?" — DFT使用の認識論的自己矛盾を直接捉えた高価値問い | tool_question: "What is the infrared spectroscopic signature of Group 9 metal carbonyl cations and anions in a neon matrix, and how accurately do DFT/BP86 calculations reproduce their carbonyl stretching frequencies?" — 論文の表面的な測定問いに後退 | ⚠️ 退行（medium）|

### 総合判定

**v181 > v17**（ただし R1–R5 計5件の退行あり）

v181 の優位点:
1. **C 項目の体系的拡充（2→4件）**: C-2（refs 17-21 RhCO ground state計算群）、C-3（refs 9-10 表面CO monolayer）、C-4（refs 52-53 Cu/silica電荷-振動数相関）が新規追加。特に C-4 は「Rh/neonスケールとCu/silicaスロープの数値比較が行われていない」という非対称引用パターンを記録（D-4-9相当の根拠提供）。
2. **U-1 の内容高度化**: v17 U-1（Rh(CO)₄混合同位体の自己矛盾的不在）は B-3 として適切に再分類され、v181 U-1 は「論文が同一論文内のMulliken電荷（+0.12）に対してスケール予測を適用していない」という内部一貫性検証の欠如という、より高価値な自己矛盾として確立。
3. **SRG-4（光分解機構）の新設**: 「光誘起アニオン間変換機構が記述されるが機構解析がない」という独立SRGが新たに構成され、D-4-4として展開。v17 にはこの問いが独立候補として存在しなかった。
4. **新規 D-4-3（アニオン分布の熱力学vs速度論）**: 4K行列中での多配位アニオン系列の分布が速度論的産物か熱力学的産物かという問いが新規に展開。v17 にはなし。
5. **A-3 の内部化**: v17 A-3（触媒電荷プローブへの外挿）は宣言済み継続課題として先送りされていたが、v181 では D-4-1 の中核問いとして内部化され、スケール内部一貫性の問いとして深化。

### 正の副次効果

- **Stage 3 v3（PRI-12/A4の新規事例確立）**: RhCOのBP86スピン状態帰属循環性（「BP86が²Σ⁺を予測するがBP86振動数で²Δを選択する」という認識論的閉鎖）をPRI-12/A4（Epistemological closure claim）の代表事例として§6に記録。Codebook A4サブタイプの具体的事例確立。
- **Stage 4 v3（先行充填パターンの確認）**: EP-09a（CO周波数-電荷相関）について Kazansky 1997 が原論文 1999 より2年先行して充填されていた「先行充填パターン」を記録。VQ逆転パターン（VQ-3要件EP-03aより VQ-4要件EP-09aが先に充填）も記録。

### 確認された未回復項目

- **R2（実験バンド強度体系的不在のSRG・D-4消失）**: ⚠️ 退行（medium）。v17 SRG-2「Band intensity reporting absent」と D-4-2（計算強度は開示・観測強度は非開示という一方向証拠構造の問い）は matrix isolation 分光論文の分野慣行に由来する高価値問いであり、v181 では消失。この問いは zhou2001（NobleGas総説）でも表面化しなかった場合は分野パターンとして確定できる。→ **OI-042 として追記**。
- **R5（E scope framework_question → tool_question）**: ⚠️ 退行（medium）。v17 の confirmed_english_question は「DFTが自身の計算した振動数で自身が予測したエネルギー順序を覆す」という認識論的自己矛盾を直接言語化した問いであり、Stage 2 E 節としての価値は v17 > v181。→ **OI-043 として追記**。
- **R1（ΔE/ΔH₀未明示）**: low-medium impact。スピン状態問いの文脈で関連するが独立OI化には至らない。B 項目消失は構造的退行であるが、v181 全体のB/C/U の質的向上を考慮すると優先度低。

---

## Entry 047: v17 vs v181 — gerry2004a（NobleGas/References, Inorg. Chem. 2004 full paper）

**比較日:** 2026-04-26
**評価論文:** Michaud, J.M.; Cooke, S.A.; Gerry, M.C.L. — Inorg. Chem. 2004, 43, 3871–3881
「Rotational Spectra, Structures, Hyperfine Constants, and the Nature of the Bonding of KrCuF and KrCuCl」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

gerry2004a は KrCuF と KrCuCl の初回 FTMW 分光論文。貴ガス–貴金属ハロゲン化物（NgMX）系列の
化学結合性を多指標で評価する11頁の full paper。v17 で先行解析済み（Stage 2まで）。
今回 v181（+s3v3+s4v3）で全ステージを実行した。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| A | 3（A-1: 代替メカニズム, A-2: 結合基準不在, A-3: XeCuX後回し）| 2（A1: 将来測定, A2: 結合基準 suppressed）|
| B | 9（B-1〜B-9）| 18（B1〜B18）|
| C | 4（C-1〜C-4）| 3（C1〜C3）|
| U | 3（U-1: eQq(⁸³Kr) 3倍過小評価, U-2: 境界判定不能, U-3: 定義不在）| 3（U1: self-contradictory bonding claim, U2: comparability prerequisite, U3: ELF demonstrates without population）|
| SRG | 7（SRG-1〜SRG-7; 部分的紐付け）| 5（SRG-1〜SRG-5; 完全D-4紐付き）|
| D-4 候補 | 7 | 10（C11規則: 3高severity U項目により拡張上限適用）|
| E scope_type | framework_question | framework_question |

### D-4 候補の対応関係

| v17候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| D-4-1（電子密度記述子数値省略; B-1/B-2/B-4/B-8）| 候補2（SRG-2: 電子密度解析手法多様性+裁定プロトコル不在）| ✅ 拡張・SRG体系化 |
| D-4-2（静電モデル破綻と代替説明不在; A-1/B-3/U-1）| 候補4（SRG-1: MP2信頼性）+ 候補7（E_ind/D_e較正問い）| ✅ 分化展開（MP2問いと誘起エネルギー問いが分離） |
| D-4-3（化学結合定義欠如; A-2/U-2/U-3/C-4）| 候補1（SRG-3: 操作的判定基準不在）| ✅ 第一位に昇格・精緻化 |
| D-4-4（Mulliken依存性と独立検証不在; B-4/B-5）| 候補9（三法電荷移動整合性不在; B2/B3/B10）| ✅ 拡張（三法比較という新視点） |
| D-4-5（擬二原子近似不確かさ; B-7/B-3）| 候補8（擬二原子近似系統誤差; B4）| ✅ 実質対応 |
| D-4-6（XeCuX後回し; A-1/A-3/U-2）| **v181 D-4 に独立候補なし** | ⚠️ 退行 R1 |
| D-4-7（Frenking-Gillespie未適用; A-2/C-4/U-3）| 候補10（Frenking-Gillespie適用不在; C2/A2）| ✅ 実質対応 |
| （v17になし）| 候補3（SRG-4: KrCuCl証拠非対称性）| ✅ 新規昇格 |
| （v17になし）| 候補5（多次元指標圧縮の正当性; U2/B11/B13/C1）| ✅ 新規 |
| （v17になし）| 候補6（35–40% NQCC比率のKrCuX未検証; C1/B12）| ✅ 新規（C1昇格） |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | XeCuX後回しの独立D-4候補化（v17候補6）| D-4-6として「NgCuX系列完結前の部分公表」「Xeなしに〈borderに最も近い〉とする循環性」を完全展開。key_quote: [REDACTED: verbatim source quotation; see `loc:`] | v181 A1として deferred記録あり（linked_to: B15/B16/C3）だがD-4独立候補に非昇格 | ⚠️ 退行（low）|
| R2 | eQq(⁸³Kr)の3倍過小評価の独立U項目記録（v17 U-1）| U-1「静電モデルがeQq(⁸³Kr)を43 MHz（計算）vs 128.8 MHz（実験）と約3倍過小評価し代替機構が必要」として独立U項目記録。D-4-2の中核証拠として機能。key_quote: [REDACTED: verbatim source quotation; see `loc:`] | B10（Sternheimer自由原子パラメータの分子環境転用; 感度解析不在）として非致命的B項目に格下げ。「定量モデルが主要観測量を3倍外す」量的予測失敗の独立U項目記録が消失 | ⚠️ 退行（medium）|

### 総合判定

**v181 > v17**（R1: low, R2: medium の退行2件あり）

v181 の優位点:
1. **D-4候補数の拡張（7→10）**: C11規則により拡張上限適用。KrCuCl証拠非対称性（候補3: SRG-4新設）、
   NQCC比率未検証（候補6: C1昇格）、E_ind/D_e較正問い（候補7: 新規）、
   三法電荷移動整合性（候補9: 新規）が追加。
2. **SRG完全紐付け（SRG-1〜SRG-5）**: 全D-4候補がSRGへの明示的対応付きで記録。
3. **Layer A/Layer B分離VQ判定（S3v3）**: 実験記録層VQ-2確実; 結合解釈層VQ-1止まり（RI-07 Fatal）。
4. **ピボット主軸精緻化**: A2↔B7（「定義不在」↔「計算信頼性不在」の相互依存回避構造）。
5. **PRI-12/A3 anchor事例の確立（S3v3 §6）**: NgMX化学結合主張のconstruct-validity
   circularityをCodebook代表事例として記録。

### 正の副次効果

- **S3v3 §6: cross-compound RI-04サブタイプ提案** — ELF識別解析がKrCuFのみに適用され
  KrCuClへ拡張されないパターンをCodebook v0.3候補として記録。
- **S4v3 §B EP-05a注記: C1の内部算出確認** — KrCuFで37.1%、KrCuClで37.2%と算出可能であり、
  「自己確認可能な未確認クレーム」パターンを実証。
- **S4v3 §D VQ階層逆転記録** — VQ-2境界論（EP-07a, 2008年Belpassi et al.）が
  VQ-3/VQ-4定量検証より先に間接充填されるという逆転パターンを初めて記録。

### 確認された未回復項目

- **R2（eQq(⁸³Kr) 3倍過小評価の独立U項目記録消失）**: ⚠️ 退行（medium）。
  NgMX系列でSternheimer模型が実験値を3倍外す事象が反復する可能性があり、
  「定量モデルの量的失敗が支持証拠として機能する矛盾」のU項目記録vs B項目格下げの
  系統的判定基準が問われる。→ **OI-044 として追記**。
- **R1（XeCuX後回しのD-4非昇格）**: low impact。A1として残存するが独立OI化は不要。

## Entry 054: v17 vs v181 — koukounas2004（NobleGas/References, full paper）

**比較日:** 2026-04-26
**評価論文:** Koukounas, Kardahakis, Mavridis — J. Chem. Phys. 120, 11500–11521 (2004)「Ab initio investigation of the ground and low-lying states of the diatomic fluorides TiF, VF, CrF, and MnF」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

koukounas2004 は第一列遷移金属フッ化物二原子分子（TiF, VF, CrF, MnF）の 34 電子状態について大規模 MRCI + RCCSD(T) 計算を行った 22 頁の J. Chem. Phys. Full Paper。MnF については初の理論計算。v17 で先行解析済み。今回 v181（+s3v3+s4v3）で再解析した。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| A | 3 (A-1: c⁵Π deferred, A-2: a⁵Σ⁺–X gap, A-3: VF/truncated PEC) | 3 (A-1: c⁵Π, A-2: PEC truncation, A-3: VF ground state mixed) |
| B | 8 (B-1〜B-8, SOCを含む) | 6 (B-1〜B-6, 統合・再分類) |
| C | 3 (C-1: Harrison, C-2: Boldyrev/Dement'ev, C-3: Simard) | 3 (C-1〜C-3; 同一対象) |
| U | 3 (U-1: c⁵Π self-contradictory, U-2: a⁵Σ⁺ gap, U-3: active space) | 3 (U-1: c⁵Π, U-2: VF ground state, U-3: active space inconsistency) |
| SRG | 6 (SRG-1〜SRG-6) | 4 (SRG-1〜SRG-4、統合) |
| D-4 候補 | 7（問い得ない問い欄を除く） | 8 |
| E scope_type | framework_question | framework_question |

### D-4 候補の対応関係

| v17候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| D-4-1（c⁵Π誤同定の自己矛盾, SRG-1）| D-4-1（c⁵Π状態同定失敗, SRG-1）| ✅ 直接対応 |
| D-4-2（De不確実性定量化欠如, SRG-3）| D-4-5（不完全PECによるDₑ信頼性）+ D-4-6（size nonextensivity）| ✅ 分割対応 |
| D-4-3（SOC体系的不在, SRG-4）| D-4-4（SOC全面省略, SRG-4）| ✅ 直接対応 |
| D-4-4（M⁺F⁻イオンモデル検証の循環性）| D-4-7（イオン性モデル循環検証）| ✅ 直接対応 |
| D-4-5（a⁵Σ⁺–X ギャップ帰因の自己矛盾, A-2/U-2）| **v181 D-4 に対応なし** | ⚠️ 退行 R1 |
| D-4-6（Harrison CrF比較回避, C-2/B-1）| D-4-8（Harrison CrF比較回避, C-1/B-2）| ✅ 直接対応 |
| D-4-7（b⁵Δ・d⁵Σ⁺・f⁵Γ PEC未完成, A-3/B-4）| D-4-5（不完全PECによるDₑ信頼性, A-2/B-4）に吸収 | ✅ 部分対応 |
| （v17になし）| D-4-2（VF基底状態検証不能性, U-2/A-3）| ✅ **新規（genuine improvement）** |
| （v17になし）| D-4-3（活性空間妥当性検証不在, B-4/U-3）| ✅ **新規（genuine improvement）** |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | MnF a⁵Σ⁺–X gap 帰因分析の独立 D-4 消失 | D-4-5として独立展開：「A⁷Πでは活性空間拡張が成功したが同じ試みがa⁵Σ⁺に適用された痕跡がない」という方法論的自己矛盾の問いを独立記録。grounded_in: A-2, U-2。key_quote: [REDACTED: verbatim source quotation; see `loc:`] — なぜA⁷Πと同等の処置を試みないのかという問い | D-4-4（SOC全面省略）がギャップ乖離の一部を説明する文脈として言及されるが、「活性空間拡張の非対称な適用」という問いは独立D-4として展開されず | ⚠️ 退行（medium） |

### 総合判定

**v181 ≥ v17**（R1 1件の退行あり）

v181 の優位点:
1. **D-4-2 新規（VF 基底状態の検証不能性）**: v17 では U-2 が a⁵Σ⁺–X gap に紐付いており、VF 基底状態の epistemological gap（「疑いの余地がない」主張の反証条件未定義）が D-4 として独立展開されなかった。v181 では CLA-1 として構造化され、独立 D-4 として昇格。UQS が高価値と判定すべき項目（検証不可能な確定的主張）が適切に捕捉された。
2. **D-4-3 新規（活性空間妥当性の系統的不在）**: v17 では B-4 として報告省略に分類されていた活性空間診断の欠如が、v181 では U-3（self-contradictory absence）と組み合わせて独立 D-4 として昇格。SRG-2 との接続も明示化。
3. **SRG 統合の簡潔化**: v17 の 6 SRG から v181 の 4 SRG への統合により、SRG 間の階層関係（SRG-2 が SRG-1 の上流問題）が§3で明確に記述された。
4. **U 項目の再編成**: v17 U-2（a⁵Σ⁺ gap）が v181 では VF 基底状態問い（U-2）に置き換えられ、より高価値な self-contradictory absence として再設定された。

### 正の副次効果

- **Stage 3 v3（PRI-12 A3 の計算化学事例確立）**: M⁺F⁻ イオン性モデルの循環的検証を PRI-12 A3（Construct-validity circularity）の代表事例として §6 に記録。Mulliken 「信頼できない」自己批判と Mulliken 使用の共存という構造の記録。
- **Stage 3 v3（RI-02B：Root-following failure サブタイプ候補）**: MnF c⁵Π 根追跡失敗を RI-02 の計算化学固有サブタイプ候補として記録。独立 2 報での再確認要件も明示。
- **Stage 3 v3（VQ 内部非対称性パターン）**: 単一論文内で NC-1（TiF）が VQ-3 相当、NC-3（MnF c⁵Π）が VQ-1 留保という最高水準と最低水準の共存を multi-molecule full paper 固有パターンとして記録。
- **Stage 4 v3（VQ 逆転パターン）**: EP-03a（SOC、VQ-3 要件）が技術駆動で充填される一方、EP-08a/EP-09a（誤差棒定量、VQ-4 要件）がインセンティブ構造的未充填として残るという VQ 逆転パターンを記録。

### 確認された未回復項目

- **R1（a⁵Σ⁺–X gap 帰因分析の独立 D-4 消失）**: ⚠️ 退行（medium）。v17 D-4-5 は「A⁷Π では活性空間拡張が成功したにもかかわらず同一処置が a⁵Σ⁺ に適用されなかった」という方法論的非一貫性を問い、v181 では D-4-4（SOC）に part 的に吸収されるが独立問いとしての精度を失っている。計算化学 full paper で特定の状態への手法非適用の問いが D-4 として捕捉されるべきかについては、v18 で C 規則の拡張として検討する価値がある。独立 OI 化は不要（impact 限定的）。
- **R3（Rh(CO)₃ 39 cm⁻¹乖離の独立D-4消失）**: low-medium impact。具体的DFT精度問いの消失だが、v181 SRG-3/EP-06a でRhCO電子状態問いとして吸収されており、完全消失ではない。独立OIは不要。

---

## Entry 048: v17 vs v181 — gerry2006a（NobleGas/References, JACS full paper）

**比較日:** 2026-04-26
**評価論文:** Michaud & Gerry — J. Am. Chem. Soc. 2006, 128, 7613–7621「XeCu Covalent Bonding in XeCuF and XeCuCl」
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6 セッション（v181+s3v3+s4v3 解析完了後に自動比較）

### 背景

gerry2006a は XeCuF・XeCuClを超音速ジェット中で初検出し、FTMW分光 +
MP2/ECP計算の4収束証拠（結合長・NQCC・De > Eind・H(r) < 0）でXeCu共有結合を
主張した JACS full paper（9頁）。v17 で先行解析済み。今回 v181（+s3v3+s4v3）で再解析。

### 項目数の変化（S1/S2から読み取り可能な範囲）

| カテゴリ | v17（S2記述から推定） | v181 |
|----------|------|------|
| A | 2 (A-1: future synthesis, A-2: "rare" boundary claim) | 1 (A-1 only; A-2相当はU-3/B-6に吸収) |
| B | ≥6 (B-1〜B-6+) | 13 (B-1〜B-13) |
| C | ≥1 (C-1: Bellert ref 44) | 3 (C-1〜C-3) |
| U | 3 (U-1: QTAIM high, U-2: spectral assignment, U-3: De-k) | 3 (U-1: ECP前提 critical, U-2: 閾値信頼性, U-3: 反証条件) |
| SRG | ≥4 | 6 (SRG-1〜SRG-6) |
| D-4 候補 | 7 | 8 |
| E scope_type | framework_question | framework_question |

### D-4 候補の対応関係

| v17候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| D-4候補1（QTAIM completeness, B-1/U-1）| D-4-1（H(r) ECP前提不在, U-1/B-11）| ✅ 保持・深化（ECP applicabilityまで追跡、critical昇格）|
| D-4候補2（De/BSSE/静電排除, B-3/C-1/U-1）| D-4-2（静電排除, B-3/C-1）+ D-4-5（De信頼性, B-1/B-9/B-10）| ✅ 分割精緻化 |
| D-4候補3（XeCuClデータ非対称性, B-2/B-1）| **対応なし** | ⚠️ 退行 R1 |
| D-4候補4（De–k線形関係の統計未検証, B-5/U-3）| **対応なし**（D-4-3/D-4-6に間接要素のみ）| ⚠️ 退行 R2 |
| D-4候補5（超音速ジェット/熱力学, A-2/B-3）| D-4-8（超音速ジェット, A-1/B-1）| ✅ 保持 |
| D-4候補6（スペクトル帰属ブランク実験, U-2）| **対応なし**（U-2 slotが閾値信頼性問題に置き換わり消失）| ⚠️ 退行 R3 |
| D-4候補7（XeCuBr/NgMX「完結」境界, A-1/B-6）| **対応なし** | ⚠️ 退行 R4 |
| （v17になし）| D-4-3（収束証拠反証条件+閾値信頼性, U-2/U-3/B-6）| ✅ 新規（U-item保護の恩恵）|
| （v17になし）| D-4-4（電子移動量三重不確定性, B-4/B-12/B-7）| ✅ 新規 |
| （v17になし）| D-4-6（NgMX連続変化vs離散カテゴリー, B-6/B-8/B-11）| ✅ 新規 |
| （v17になし）| D-4-7（分光フィット品質の不報告, B-2/B-5/B-13）| ✅ 新規 |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | XeCuClデータ非対称性の独立D-4消失 | D-4候補3として独立展開：「XeCuFのNBO/Mulliken集団は詳細報告、XeCuClは"quite similar"で省略」という2化合物論文の証拠非対称性を批判。grounded_in: B-2/B-1 | D-4-7が分光フィット品質（B-2含む）を扱うが「XeCuCl独自の電子構造証拠の欠如」という論点は独立D-4に昇格せず消失 | ⚠️ medium |
| R2 | De–k線形関係の統計未検証 | D-4候補4として独立展開：Figure 5回帰統計なし・二原子近似の系統誤差・「間接的近似測定」の量的根拠。grounded_in: B-5/U-3 | D-4-3/D-4-6に間接的要素はあるが「Figure 5のR²・不確かさ」という具体的統計論点が消失 | ⚠️ low-medium |
| R3 | スペクトル帰属ブランク実験論点の消失 | v17 U-2として独立記録：「陰性対照実験（Cuのみ+Ar等）が示されていない—レーザー蒸着FTMWの標準確認手続きの不在」をD-4候補6として展開 | v181 U-2 slotが「XeAuF例外による閾値信頼性問題」に置き換わり、実験設計批判が完全消失 | ⚠️ medium |
| R4 | NgMX「完結」主張のXeCuBr次元問題 | D-4候補7として独立展開：「Ng×M次元完結≠X次元完結」 | 対応なし | ⚠️ low |

### 総合判定

**v181 > v17**（R1・R3 medium退行あり、正の変化多数）

v181の優位点:
1. **U-1 critical保護 → D-4-1最優先昇格**: ECP系H(r)前提欠如をcritical U項目として独立記録。v17のU-1（high）より高位。
2. **B-3の3/3収束 → D-4-2独立明確化**: 全エージェント一致最大収束のB-3がD-4-2として焦点化。
3. **U-2（閾値信頼性）→ D-4-3統合**: XeAuF例外が示す内部矛盾をより高価値なU項目として捕捉。
4. **SRG-6（操作的定義）新出**: 共有結合の定量的閾値・反証条件問題のグループ化。
5. **D-4-4（電子移動量三重不確定性）・D-4-6（連続体vs離散）新出**: v17になかった視点。

### 正の副次効果

- **S3v3 §6（PRI-12-A5事例）**: MP2レベル×ECP近似×Cremer-Kraka H(r)の3層近似積み重ねをPRI-12-A5代表事例として記録。重元素-貴ガス結合論文全体に適用可能。
- **S3v3 §6（RI-03 Available-but-uncalculated サブタイプ候補）**: SAPT分解が「技術的可能だが未計算」という新サブタイプをCodebook v0.3候補として提案。
- **S3v3（層別VQ非対称性）**: Layer 1+2（検出）がVQ-2 full、Layer 3（共有結合分類）がVQ-2 qualified、という層別非対称性を記録。
- **S4v3（先行充填パターン）**: Lovallo & Klobukowski 2002が4年先行してDe・構造を独立計算。EP-04aの残余未充填（H(r)/NBO）を明確化。
- **S4v3（VQ逆転パターン）**: RI-01（VQ-2要件）がインセンティブ構造的未充填（第三群）、RI-06/RI-03（VQ-3要件）が技術駆動充填第一群という逆転を記録。

### 確認された未回復項目

- **R1（XeCuClデータ非対称性の独立D-4消失）**: ⚠️ medium。「2化合物論文で1化合物の電子構造証拠が"quite similar"で省略される」パターンは分光+計算複合論文に汎用的。→ **OI-045（新規）**
- **R3（スペクトル帰属ブランク実験消失）**: ⚠️ medium。レーザー蒸載FTMW論文でのブランク実験不在論点がU-2 slot変更で消失。v18.1のU slot数（3スロット）が容量制約かを確認要。→ **OI-046（新規）**

---

## Entry 049: v17 vs v181 — gerry2000a（NobleGas/References, J. Chem. Phys. 2000 full paper）

**比較日:** 2026-04-26
**評価論文:** Evans & Gerry 2000 — Ar–CuF, Ar–CuCl, Ar–CuBr FTMW spectra / 初回観測 + 「弱い共有結合」命題
**モデル:** claude-sonnet-4-6
**評価者:** Sonnet セッション

### 背景

v17: S1 A項目3件（A-1: Cu NQCC先送り; A-2: D_e Cl/Br不算出; A-3: 代替電荷解析不実施）+複数B/C/U項目。D-4候補7件、high_convergence_high_gap: none（フォールバック規則適用）。

v181: S1 A-1のみ（A-2/A-3をB/C項目に再分類）+ B-1〜B-12 + C-1〜C-3 + U-1（NBO/QTAIM不在, high）+ U-2（Mulliken電荷方向不整合, high）+ U-3（Mulliken基底アーティファクト, critical）。D-4候補8件（展開規則適用: ≥2 critical/high U項目）、high_convergence_high_gap: B-3, U-3。

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | Ar–Cu距離変化機構の内部矛盾のD-4独立消失 | D4-5として独立展開：「Mulliken電荷q^Cuが F→Cl→Brで増大（+0.23→+0.45）しており、Cu-X共有結合増大によるCu⁺遮蔽増大という説明機構と逆向き」という論文内部矛盾を批判。grounded_in: B-4/U-3 | U-2（Mulliken電荷方向不整合, high）としてS1に保護されているが、D-4候補としての独立展開がなく「遮蔽説明との因果的矛盾」という論点が消失 | ⚠️ low-medium |
| R2 | 三機構非分離（SAPT/EDA）のD-4独立消失 | D4-7として独立展開：「Ar–Cu結合エネルギーへの静電/誘起/分散/交換の各寄与がSAPT/EDA的に非分離のまま『共有結合性』を主張」。grounded_in: C-2/B-3/U-2 | D-4候補1（弱い共有結合根拠の多重欠落）またはU-1（NBO/QTAIM不在）に部分統合。「SAPT分解による機構分離」という具体的実験提案が独立候補として消失 | ⚠️ medium |

### 総合判定

**v181 > v17**（R2 medium退行1件、R1 low-medium退行1件あり。正の変化5点で全体的に改善）

v181の優位点:
1. **high_convergence_high_gap検出（B-3, U-3）**: v17ではフォールバック規則を適用するほど収束なし。v181ではU-3 critical + B-3が 2/3以上の収束で正しく検出され、D-4展開規則（≥2 critical/high U項目）が正当に発動。
2. **D-4候補3「Ar–Cu結合長精度」（SRG-1）の独立候補化**: r₀系統誤差（B-2: 2.216〜2.274 Åの幅をランダム誤差として平均報告）とr_d誤差伝播不在（B-8）が独立SRG-1として記録。v17には対応する独立候補なし。
3. **D-4候補6「ωₑ不確かさと剛直主張」の独立候補化**: B-4（D_J不確かさのωₑ伝播なし）とB-5（励起状態不検出感度なし）を統合した独立展開。v17では D4-5の周辺に埋没。
4. **D-4候補8「Group 11周期律的完成/Ar–AuX」の追加**: 後続研究方向性（T3）として提示。v17には対応なし。
5. **D-4候補5「OC–CuXとのDropped Quantitative Benchmark」の分離**: v17のD4-6（van der Waalsベースライン不在）から分離し、CLA-2/C-2（Antes et al. Ref.9との定量比較なし）を独立候補として明確化。

### 正の副次効果

- **S3v3 §6（RI-03+RI-05共起パターン）**: 「Cu NQCC合理化失敗（RI-03: Fatal）を認めながらNQCC変化をRI-05的にutility pilllarの証拠として流用する」という証拠の循環構造を代表事例として記録。分光法論文特有の構造として Codebook 登録推奨。
- **S3v3 §6（PRI-12 Cluster A5の物理化学拡張）**: MP2+ECP+不均一基底+Mulliken+Townes–Daileyの多層近似累積を物理化学・分光論文でのPRI-12 A5事例として記録。従来の計算化学代表例から適用ドメイン拡充。
- **S3v3 §6（計算品質許容閾値は用途依存）**: BSSE未補正D_eが「ベンチマーク値」として許容されても「分類命題の一次的定量根拠」として使う場合は現代基準で致命的——という判定原則をEra-Norm Codebook注記候補として提示。
- **S3v3 §3（Layer別VQ非対称性）**: 「Layer 1（初回観測）はVQ-3相当、Layer 3（結合解釈）はVQ-2止まり」という層別VQ非対称性の典型例を登録。物理化学・分光論文に汎用。
- **S4v3（VQ階層逆転パターン）**: EP-09a（VQ-4前提）が最短時間で自己充填、EP-08a（VQ-2: 統計精密化）がインセンティブ構造的未充填——という「科学論理と出版インセンティブの逆転」パターンをFTMW分光論文の典型例として記録。
- **S4v3（EP-03a 25年超潜在的未充填）**: A-1先送り宣言のある最重要問い（Cu EFG直接計算）が25年超にわたって充填論文未同定の可能性。「宣言された最重要問いが最長未充填になる逆説」候補。

### 確認された未回復項目

- **R2（SAPT/EDA三機構非分離のD-4独立候補消失）**: ⚠️ medium。「希ガス-金属結合の静電/誘起/分散/交換寄与が未分離のまま共有結合性を主張する」という問いがD-4候補として独立展開されない。Ng-MX系論文に汎用的パターン。→ **OI-047（新規）**
- **R1（Mulliken電荷方向矛盾のD-4独立消失）**: ⚠️ low-medium。U-2として保護されているため実質的影響は限定的。独立OI化不要。
- **R2・R4**: low impact。独立OI化は不要。

---

## Entry 050: v17 vs v181 — gerry2004b（NobleGas/References, J. Am. Chem. Soc. 2004 full paper）

**比較日:** 2026-04-26
**評価論文:** Cooke & Gerry 2004 — XeAuF / FTMW検出・構造決定・XeAu共有結合主張
**モデル:** claude-sonnet-4-6
**評価者:** claude-sonnet-4-6セッション

### 背景

本論文はNgMX系列の最終ピース（XeAuFとXeAu(I)中性分子の初検出）を提供するJACS論文。
v17での解析では12個のB項目、8個のSRGを持つ詳細な分類体系が生成された。
v181の主要変更：Turn 4のMulti-critical U-item independent recording rule（C11）、
D-4候補数上限の条件付き拡張（C9）、D-4候補grounding check（C10）。

### 項目数の変化

| カテゴリ | v17 | v181 |
|----------|-----|------|
| A | 3 | 1 |
| B | 12 | 6 |
| C | 4 | 5 |
| U | 4 | 2 |
| SRG | 8 | 5 |
| D-4候補 | 8 | 8 |
| 合計(A+B+C+U) | 23 | 14 |

### D-4候補の対応関係

| v17候補 | v181候補 | 対応状況 |
|---------|---------|---------|
| D4-1（EDA不在: 消去的議論が肯定的EDA候補に転換されない）[U-4] | 対応なし | ⚠️ 消失（OI-047確認ケース2例目）|
| D4-2（Sternheimer自己矛盾: 閉殻前提崩壊の論理的循環）[U-1] | 候補6（NQCC独立証拠性欠如）| ⚠️ 視点変化（論理的循環性の精度喪失）|
| D4-3（中性XeAuF De異常値: XeAu⁺より低い）[U-2] | 候補3（Dₑ/ke矛盾）+ 候補8（イオン性比較不在）| ✅ 対応（分割精緻化）|
| D4-4（NgMX全体への一般化の定量的閾値不在）[A-1] | 候補5（NgMX外挿: CLA-1）| ✅ 対応（A→D-4への適切な昇格）|
| D4-5（AIM選択的提示: ρ/∇²ρ欠如のD-4候補化）[B-7] | 対応なし（SRG-4記録のみ）| ⚠️ 部分回復 |
| D4-6（三手法不一致: Townes-Dailey/Mulliken/NBO）[U-3] | 候補2（閾値信頼性）の一部 | ⚠️ 部分回復 |
| D4-7（MP2/ECP水準不十分性の横断的波及）[B-8, B-12] | 候補4（MP2精度保証なし）| ✅ 対応 |
| D4-8（ガスジェット生成条件の選択性・副生成物不在証明）[A-2] | 対応なし | ⚠️ 消失（low impact）|
| ——— | 候補1（AuF双極子未測定: convergence=3/3最高収束項のD-4最優先化）【新規・重要】 | ✅ 新規 |
| ——— | 候補7（幾何学的構造決定過信: 固定r(AuF)+単一同位体置換）【新規】 | ✅ 新規 |

### スコアカード

| ID | 退行ポイント | v17 | v181 | 判定 |
|----|-------------|-----|------|------|
| R1 | EDA不在（v17 U-4・D-4-1）のD-4独立候補化の消失 | U-4として独立記録（MOLDEN/population analysisはcircumstantial、EDA不在では定量的分離不可）かつD-4-1（最優先候補）として展開 | D-4候補として非候補化。候補2（閾値信頼性）の背景的要素に統合されるが「エネルギー寄与の定量的分離手段の欠如」として独立展開されない | ⚠️ medium（OI-047確認ケース2例目）|
| R2 | Sternheimer自己矛盾の論理的精度喪失（v17 U-1・D-4-2） | U-1として独立記録・D-4-2として展開：「Sternheimerモデルは閉殻Xe原子を前提とする。XeAu共有結合が存在するならXe 5pσが結合性MOに参加し閉殻前提が崩壊する。モデル前提を否定する結論の証拠としてそのモデル出力を使う論理的循環が認識されていない」 | 候補6（NQCC独立証拠性欠如）として部分対応：「Sternheimerモデルの限界（点電荷近似、γXe不確かさ）とAb initio NQCCの乖離を区別できない」— 閉殻前提崩壊による論理的循環は記述されず「独立計算の不在」に変換 | ⚠️ medium（新OI-048）|
| R3 | AIM選択的提示（ρ/∇²ρ欠如）のD-4独立候補化の消失（v17 D-4-5） | D4-5として独立展開：「∇²ρ(r)はAIM一次的共有結合判定指標であり不在ではHb(r)解釈が非一意。ρ(r)もAIM標準出力として未報告」 | SRG-4（定量的結合次数指標の不在）に記録されるがD-4独立候補として展開されない。SRG-4は候補2・EP-05aに反映されているが「∇²ρが一次的判定指標として欠如」という論点が明示されない | ⚠️ low-medium |
| R4 | ガスジェット生成条件の選択性・副生成物問題（v17 A-2・D-4-8）の消失 | A-2（forgotten: 探索過程の経緯不透明）+ D-4-8「XeAuXe, AuXe₂F等の副生成物が探索・排除されたかを示す証拠がない」として独立展開 | A-1（XeCuX deferral）のみが記録され、v17 A-2相当の「ガスジェット生成条件の探索選択性・副生成物同定」は非記録。D-4候補としても展開されない | ⚠️ low |

### 総合判定

**v181 > v17**（R1・R2 medium退行、R3 low-medium退行、R4 low退行。正の変化5点で全体的改善）

v181の優位点:
1. **AuF双極子（候補1）の最優先候補化**: v17ではB-4相当として記録されていたがD-4候補に昇格しなかった。v181ではconvergence=3/3（全エージェント一致）のhigh_convergence_low_gapフォールバック規則によりD-4最優先候補として適切に展開。SRG-1の根本問題が最も顕著なD-4項目として記録された。
2. **v17 A-1（NgMX外挿）のD-4適切昇格**: v17ではA-1（deferred: NgMX bonding generalization）として分類されていたが、CLA-1・候補5として適切にD-4に昇格。将来公表待ちではなく「問われていない問い」として正しく再分類。
3. **Dₑ/ke矛盾の分割精緻化**: v17 U-2（De異常値）がv181候補3（力定数比例則との内的矛盾）+ 候補8（イオン性比較不在）として分割展開され、両側面が明示化された。
4. **幾何学的過信（候補7）の新規候補化**: 固定r(AuF)+単一同位体置換によるrm(1)信頼性限界がv17 SRG-6から独立D-4候補として昇格。
5. **B項目の整理統合（12→6）**: v17の細分化された12項目がSRG構造によって5グループに整理統合され、問いの根本構造が明確化。

退行R1（EDA消失: medium）はgerry2000aに続くOI-047の2例目。R2（Sternheimer論理精度: medium）は新OI-048として記録。R3はSRG-4での部分カバーにより実質的影響が限定される。

### 正の副次効果

- S3 v3でPRI-12見送り判定（Hb(r) < 0基準は2004年分野標準慣行の範囲内）が適切に記録された
- Stage 3の「CLA-2（NQCC独立証拠性）→RI-03 Fatal」判定が気相分光論文でのRI-03典型事例として確立
- S4 v3でVQ階層逆転パターン（EP-01a/EP-08aがインセンティブ構造的未充填、EP-03a/04a/05aが技術駆動充填）がNgMX論文の典型として記録された
- S4 v3でAuF双極子「先行充填の可能性」（2004年以前に計算済みの可能性）が記録され、著者による意図的情報選択の証拠候補として記録された

### 確認された未回復項目

- **R1（EDA不在のD-4独立候補消失）**: gerry2000a（Entry 049）に続く2例目の確認。OI-047のtriger conditionを充足 → **OI-047の発生論文欄に追記**
- **R2（Sternheimer自己矛盾の論理的精度喪失）**: 「原子モデルの閉殻前提を崩す結合の証拠としてそのモデルを使う論理的循環」というD-4検出パターンの消失。NgMX系以外の分光論文にも汎用性がある可能性。→ **OI-048（新規）**
- **R3（ρ/∇²ρ欠如のD-4独立候補化消失）**: SRG-4に記録されているため実質的影響は限定的。独立OI化は不要。再評価トリガー: 次のQTAIM提示論文との比較時。

---

## Entry 052: v181 vs v182 — kumada（dev/kumada, JACS communication 1972）

**比較日:** 2026-04-27
**評価論文:** Tamao, Sumitani, Kumada 1972 — Ni-ホスフィン錯体触媒によるGrignard試薬×有機ハライドの選択的クロスカップリング
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v181 vs v182

### 比較対象バージョン

| 版 | ファイル |
|---|---|
| 旧版（v181） | kumada_v181_sonnet_s2.md |
| 新版（v182） | kumada_v182_sonnet_s2.md |

### D-4候補対応表

| v181候補 | v182候補 | 対応状況 |
|---------|---------|---------|
| 候補1（触媒サイクルの自己検証不在: R–R ホモカップリング予測の検証なし）| D-4-1（「選択的クロスカップリング」主張と触媒サイクルの自己矛盾的不在）| ✅ 対応（U-1がD-4-1の核として独立展開、より明確な自己矛盾構造を提示）|
| 候補2（触媒サイクルの素反応的根拠の不在）| D-4-2（触媒サイクルの全素反応ステップの機構的証拠の体系的欠如）| ✅ 対応（ラジカル経路排除という問いが明示的に追加）|
| 候補3（「選択性」の定量的根拠の不在）| D-4-1に統合（B-2, U-1, SRG-2）| ✅ 対応（D-4-1に吸収、mass balanceと自己矛盾が統一）|
| 候補4（cis中間体3の構造的根拠の不在）| **対応なし**（D-4-2内に部分吸収）| ⚠️ 消失（medium）|
| 候補5（β水素排除回避の原理的根拠の不在）| **対応なし**（D-4-2内に部分吸収）| ⚠️ 消失（medium）|
| 候補6（cis:trans比の立体化学的含意の不問）| D-4-3（立体選択性の速度論的帰属と測定信頼性の同時的不在）| ✅ 対応（B-5との統合により精緻化）|
| 候補7（先行Ni触媒系との実験的区別の不在）| D-4-5（Corriu-Masse同時投稿との化学的差別化の不在）| ✅ 対応 |
| ——— | D-4-4（基質スコープ境界の実験的根拠の体系的不在）| ✅ 新規（B-3+B-4+A-4のSRG-3統合候補化）|
| ——— | D-4-6（触媒のTON・失活・化学的状態の未定量）| ✅ 新規（A-3+B-8の黒色化問題を均一/不均一系問いとして昇格）|

### スコアカード

| ID | 退行ポイント | v181 | v182 | 判定 |
|----|---|---|---|---|
| R1 | cis中間体3の構造的根拠（v181候補4）の消失 | 「[REDACTED: verbatim source text; see the source paper via its DOI]」を独立D-4候補4として展開: 配位子活性順位から推論されるcis幾何の実験的根拠（X線・NMR・UV）の不在 | v182ではD-4-2（機構的証拠の体系的欠如）に部分吸収。V2-Q6として元々記録されていたがU-2として独立U分類されず、D-4候補として前景化しない | ⚠️ 後退（medium）|
| R2 | β水素排除回避の原理的根拠（v181候補5）の消失 | 「[REDACTED: verbatim source text; see the source paper via its DOI]」のβ-H脱離抑制機構の不在を独立D-4候補として展開 | v182ではD-4-2に吸収されうるが、「β-H排除を回避するための分子的要件」という化学的に具体的な問いが独立D-4候補として現れない | ⚠️ 後退（medium）|

### 総合判定

**v182 > v181**

v182の優位点:
1. **D-4-6（TON・均一系/不均一系問いの新規浮上）**: v181にはなかったA-3+B-8の統合候補。黒色混合物（B-8）を「均一系か不均一系か」という実用的に重要な問いとして昇格した初事例。
2. **D-4-3の精緻化**: v181候補6（cis:trans比の含意）がB-5（GLC測定信頼性）との統合によって「測定の信頼性が速度論的帰属の前提」という構造が明示された。
3. **D-4-4（基質スコープ境界のSRG統合）の新規候補化**: v181では独立D-4候補になっていなかったB-3・B-4・A-4がSRG-3として整理され、「スコープ境界の実験的根拠不在」として統合候補化された。
4. **E節confirmed_english_questionの精度向上**: v181の「What ligand structural features...」（論文が答えていない問い）から v182の「Can a nickel-phosphine complex selectively couple...」（論文が実際に問うた問い）へ修正。scope_typeをtool_questionとして一貫させた。

退行2件: R1（cis中間体構造、medium）・R2（β-H排除回避、medium）。両者ともD-4-2に部分吸収されており完全消失ではない。

### 正の副次効果

- 1972年JACS通信への初回v182適用事例として、C12（multi-measurement reporting symmetry）のチェックが非対称データ報告問題（B-4: 配位子活性順の定量なし）の検出に貢献した（V1-Q4, V3-Q3のconsolidation）
- SRG設計の精細化（3→5 SRG）が prior versions と比較してより焦点化されたD-4候補化を実現

### 確認された未回復項目・新規懸案

- R1（cis中間体3の構造的根拠の独立D-4候補化消失）→ open_issues OI-053
- R2（β水素排除回避の原理的根拠の独立D-4候補化消失）→ open_issues OI-054

---

## Entry 055: v17 vs v182 — murai（dev/murai, Nature communication 1993）

**比較日:** 2026-04-27
**評価論文:** Murai et al. 1993 — Ru触媒によるアロマティックC–H/オレフィンカップリング
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v17 vs v182

### 比較対象バージョン

| 版 | ファイル |
|---|---|
| 旧版（v17） | murai_v17_sonnet_s2.md |
| 新版（v182） | murai_v182_sonnet_s2.md |

### D-4候補対応表

| v17候補 | v182候補 | 対応状況 |
|---------|---------|---------|
| 候補1（触媒サイクルの自己矛盾的不在）| D-4-1（キレーション補助の正の証拠の不在）| ✅ 対応（U-1の自己矛盾的不在として維持）|
| 候補2（GC収率の信頼性・定量的実証）| D-4-3（GC収率の絶対値信頼性）| ✅ 対応（キャリブレーション問いに焦点化）|
| 候補3（選択性の速度論/熱力学的起源）| D-4-4（選択性の制御起源）+ D-4-2（選択性の分析的根拠）| ✅ 改善（U-2がD-4-2として独立展開）|
| 候補4（1-インダノンの検出下限）| D-4-7（キレーション基の必要性の定量的実証）| ✅ 対応（合成化学的要件として再フレーミング）|
| 候補5（実用条件への外挿根拠）| D-4-6（触媒失活・回収）+ D-4-7の境界問い | ⚠️ 部分回復（「雰囲気条件不記載」B-16相当は消失）|
| 候補6（先行文献との数値比較不在）| D-4-5（先行文献との定量的比較の不在）| ✅ 対応|
| 候補7（キレーション支援の構造的境界）| D-4-7に吸収（部分）| ⚠️ 部分回復（芳香環-カルボニル間の原子数境界問いが後退）|
| 候補8（合成標的との接続の不在）| D-4-8（合成標的との接続の不在）| ✅ 対応|

### スコアカード

| 評価項目 | v17 | v182 | 判定 |
|---------|-----|------|------|
| D-4候補数 | 8 | 8 | ≡ |
| U項目数 | 2 | 2 | ≡ |
| SRG構造 | SRG×5 | SRG×5 + CLA-1 | ✅ v182改善 |
| U-2のD-4独立昇格 | 部分的（候補3内） | D-4-2として独立 | ✅ v182改善 |
| propositional精緻化 | "catalyze addition of aromatic C–H bonds to olefins" | "ortho-selective C–H/olefin coupling of aromatic ketones or acylheteroaromatics" | ✅ v182改善 |
| scope_type | framework_question | tool_question | △（両解釈可; v182がより正確）|
| 実用条件外挿候補の維持 | D-4候補5として明示 | D-4-6/D-4-7に分散 | ⚠️ R1 |
| キレーション構造的境界の維持 | D-4候補7として明示 | D-4-7に吸収（部分） | ⚠️ R2 |

### 総合判定: **v182 > v17**

U-2の独立D-4昇格、propositionalのスコープアンカー改善、CLA-1の明示的分離が重要な前進。実用条件外挿とキレーション境界問いの独立性が後退しているが、これらは既存候補に吸収されており消失ではない。

### 正の副次効果

- Multi-measurement reporting symmetry check (v18.2 C12) が合成論文では既存のB-1/B-8に収束する形で機能した（計算論文向けチェックとの共存確認）
- PRI-11適用候補として§6に記録（Murai 1993が3報目候補）

### 確認された未回復項目・新規懸案

- R1（「実用条件への外挿根拠の不在」が独立D-4候補として消失）→ open_issues OI-055
- R2（「キレーション支援の構造的境界条件（芳香環-カルボニル間原子数）」の独立D-4候補化消失）→ 既存OI-001/OI-007の同型パターン、新規OI不要

---

## Entry 056: v182 vs v184 — kumada（dev/kumada, JACS communication 1972）

**比較日:** 2026-05-02
**評価論文:** Kumada (Tamao, Sumitani, Kumada, JACS 1972) — devset
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v182 vs v184（Sonnet 4.6 整合性パッチ: C17 CoT scaffolding + C18 候補本文4要素構造 + C19 セルフチェック + tone修正5件）
**注意:** dev/kumada に v183 出力が存在しないため、比較は v182 vs v184。v183（中間版）との直接比較は省略。

### 背景

v18.4 は v18.3 確定後に実施した Sonnet 4.6 実行モデル整合性パッチ（changelog_v184.md）。
Stage 2 D-4 セクションへの 3 改変が中心：
- C17: D-4 生成前に CoT scaffolding（thinking ステップで high_convergence_high_gap / SRG / U項目 / 上限数を順に整理）
- C18: 各 D-4 候補本文に「問い/処理様態/帰結/Stage 1 関係」の 4 要素構造を義務付け（6〜12文）
- C19: D-4 出力確定前のセルフチェックリスト

Stage 0/1 は版番号のみ更新（分析的内容変更なし）。

### D-4候補対応表

| v182候補 | v184候補 | 対応状況 |
|---------|---------|---------|
| D-4-1（ホモカップリング自己矛盾的不在） | D-4-2（ホモカップリング自己矛盾的不在） | ✅ 対応・維持 |
| D-4-2（触媒サイクル機構証拠欠如） | D-4-1（触媒サイクル素反応未検証） | ✅ 対応・深化 |
| D-4-3（立体選択性速度論帰属＋測定信頼性） | D-4-4（立体化学速度論/熱力学的起源） | ✅ 対応・維持 |
| D-4-4（基質スコープ境界の実験的根拠欠如） | D-4-3（sp²制限否定的証拠不在）+ D-4-7（配位子活性序列） | ✅ 改善（分離独立化）|
| D-4-5（Corriu-Masse差別化不在） | D-4-6（先行研究定量比較欠如） | ✅ 対応・拡張（SRG-6統合）|
| D-4-6（触媒失活・Ni⁰不均一系問題） | D-4-1内U-2サブ要素として吸収 | ⚠️ R1（独立性後退、severity=mediumのため許容範囲）|
| — | D-4-5（収率データ分析的信頼性）【新規】 | ✅ 新規独立候補（SRG-5）|
| — | D-4-7（配位子活性序列の物理化学的根拠）【新規分離】 | ✅ v182 D-4-4から分離 |
| — | D-4-8（実用条件外挿可能性）【新規】 | ✅ 新規独立候補 |

### スコアカード

| 評価項目 | v182 | v184 | 判定 |
|---------|------|------|------|
| D-4候補数 | 6 | 8（上限到達） | ✅✅ v184改善（+2、上限到達） |
| D-4候補本文の平均文数 | ≈4〜6文（単段落） | ≈8〜12文（4要素構造） | ✅✅ v184改善（C18効果） |
| D-4候補本文の4要素構造 | なし（単段落） | 全8候補で問い/処理様態/帰結/Stage 1関係を明示 | ✅ v184改善（C18直接効果） |
| C17 CoT scaffolding 実行証跡 | なし | 「フォールバック規則適用」冒頭明示 + temperature_note全候補明記 | ✅ v184改善 |
| high_convergence_high_gap対応 | フォールバック記述あり | フォールバック記述あり（形式一致） | ≡ |
| U-1（high）独立D-4昇格 | ✅（D-4-1として独立） | ✅（D-4-2として独立） | ≡ |
| SRG-5（収率データ品質）の独立D-4化 | 未実現（B項目群として記録のみ） | D-4-5として独立 | ✅ v184改善 |
| 配位子序列問いの独立D-4化 | D-4-4に吸収 | D-4-7として独立 | ✅ v184改善 |
| 実用条件外挿問いの独立D-4化 | 未実現 | D-4-8として独立 | ✅ v184改善（cf. OI-055 同型パターン解消）|
| Ni⁰不均一系問いの独立D-4化 | D-4-6として独立 | D-4-1内U-2サブ要素 | ⚠️ R1 |
| priority_structure ピボット記述 | A-1↔B-3, A-1↔U-1, A-3↔B-8（3件） | A-2↔B-6, A-1↔B-11（2件、より具体的） | △（件数減だが焦点化） |
| propositional | 同一 | 同一 | ≡ |
| scope_type | tool_question | tool_question | ≡ |

### 4シグナル評価（ユーザー指定）

| シグナル | 評価 | 根拠 |
|---------|------|------|
| 1. D-4候補本文 analytical depth 増加（C18の4要素構造、6〜12文） | **✅ 確認** | v182: 平均4〜6文の単段落; v184: 全候補が4要素×段落構造、10〜12文 |
| 2. D-4候補数が上限8に到達 | **✅ 確認** | v182: 6候補; v184: 8候補（デフォルト上限に到達） |
| 3. critical/high U項目の独立展開 | **≈同等** | 両版ともU-1（high）は独立D-4昇格。本論文はcritical U項目なし、high U項目=1件のため多重U独立展開のテスト条件なし |
| 4. high_convergence_high_gap → D-4明示的紐付け | **≡同等** | 両版ともgap=空; フォールバック規則の適用とtemperature_noteの記載はv184でより系統的 |

### 総合判定: **v184 > v182**

シグナル1（analytical depth）とシグナル2（候補数上限到達）の両方が明確に確認された。
C17（CoT scaffolding）とC18（4要素構造指定）の複合効果により、候補数と候補深度が同時に改善。
C19（セルフチェック）の効果はD-4-1〜8の構造的整合性に反映されている（grounded_in全件がA/B/C/U item_idのみ）。

### 正の副次効果

- SRG-5（収率データ品質）が初めて独立D-4候補（D-4-5）として浮上。v182では記録のみ。
- OI-055同型（実用条件外挿問い）が v184 では D-4-8 として独立化。murai v182での消失パターンが Kumada v184で回避された。
- Tone修正5件により「禁止/必ず」の出力形式強制語が除去されたことは、D-4本文の自然な記述スタイル（断定回避の「〜として読める」形式）と整合していると推定される（直接観測不可）。

### 確認された退行・懸案

- **R1**: v182 D-4-6（触媒失活・Ni⁰不均一系問題）が v184 では D-4-1 の U-2 サブ要素として吸収され、独立D-4候補としての地位を失った。U-2 は medium severity のため multi-critical U-item 独立記録保護規則の適用外であり、許容範囲内の後退。open_issues への新規 OI は不要（既存の SRG-1 リンクで追跡可能）。
- **懸案**: シグナル3（multi-critical U独立展開）のテスト機会がなかった。high U×2以上の論文（例: 計算化学論文）での検証が別途必要。
  → **2026-05-02 解消**: Entry 057（murai v18.4）で U-1(critical)+U-2(high)+U-3(high) の3件独立展開（D-4-1, D-4-2, D-4-4）を確認。シグナル3の検証完了。

---

## Entry 057: v182 vs v184 — murai（dev/murai, Nature communication 1993）

**比較日:** 2026-05-02
**評価論文:** Murai et al. 1993 — Ru触媒によるアロマティックC–H/オレフィンカップリング
**モデル:** claude-sonnet-4-6
**プロンプト比較:** S0–S2 = v182 vs v184（Sonnet 4.6 整合性パッチ: C17 CoT scaffolding + C18 候補本文4要素構造 + C19 セルフチェック + tone修正5件）
**注意:** dev/murai に v183 出力が存在しないため、比較は v182 vs v184。v183（中間版）との直接比較は省略。Entry 056（kumada）と同一の比較軸。

### 背景

本エントリは Entry 056（kumada v182→v184）の murai 対称版。v18.4 の4シグナル（C18 4要素構造・候補数上限・multi-critical U独立展開・TEMPERATURE_SUMMARY紐付け）を kumada に続いて合成論文（Murai 1993）で検証する。なお Entry 055（v17→v182 murai）で発見された OI-055（実用条件外挿問いの独立D-4化消失）が本バージョンで解消されるか否かも確認対象。

v18.4 D-4 セクション変更点（Stage 0/1 は版番号のみ更新）：
- C17: D-4 生成前の CoT scaffolding（thinking ステップで high_convergence_high_gap / SRG / U項目 / 上限数を順に整理）
- C18: 各 D-4 候補本文に「問い/処理様態/帰結/Stage 1 関係」の 4 要素構造を義務付け（6〜12文）
- C19: D-4 出力確定前のセルフチェックリスト

### Stage 1 分類比較

| 分類 | v182 | v184 | 差分 |
|------|------|------|------|
| A 項目数 | 2（A-1, A-2） | 1（A-1のみ） | -1（A-2は D-4-8 として実体化）|
| B 項目数 | 9（B-1〜B-9） | 11（B-1〜B-11） | +2 |
| C 項目数 | （参照のみ: C-2, C-4 等）| 8（C-1〜C-8 明示）| 明示化 |
| U 項目数 | 2（U-1, U-2） | 4（U-1 critical, U-2 high, U-3 high, U-4 medium） | +2 |
| SRG 数 | 6（SRG-1〜SRG-6） | 5（SRG-1〜SRG-5） | -1（SRG-6 が SRG-1/SRG-5 に統合）|

### D-4候補対応表

| v182候補 | v184候補 | 対応状況 |
|---------|---------|---------|
| D-4-1（キレーション補助の正の証拠の不在）[A-1, B-3, B-4, B-7, U-1] | D-4-1（環状メタレート中間体の実在証拠）[U-1, A-1, C-2, B-11] | ✅ 対応・再フレーミング（C-2連動追加）|
| D-4-2（選択性の分析的根拠: GCは位置異性体を区別できない）[B-2, B-8, U-2] | D-4-5（位置選択性と速度差の速度論/熱力学的根拠）[B-8, B-9, B-10, U-4] | ⚠️ 変形（U-2の意味が別候補に移行; D-4-5に吸収）|
| D-4-3（GC収率の絶対値信頼性）[B-1, B-5] | D-4-3（定量的性能主張の分析的根拠）[B-1, B-2, B-3, B-4, C-1] | ✅ 対応・拡大統合（B-2, B-3, B-4, C-1を取り込み）|
| D-4-4（選択性の制御起源: 速度論 vs 熱力学）[B-9, A-1] | D-4-5（位置選択性と速度差の根拠）[B-8, B-9, B-10, U-4] | ✅ 吸収統合（SRG-3に基づく適切な統合）|
| D-4-5（先行文献との定量的比較の不在）[B-5, C-2] | D-4-6（先行研究との定量的比較の欠如 DQB）[C-1, B-2] | ✅ 対応・維持（DQBラベル付与で明確化）|
| D-4-6（触媒の失活・回収・再利用）[B-1, B-6] | D-4-8（実用条件外挿可能性）[B-6, B-7, B-1] | ✅ 拡張対応（OI-055 同型解消）|
| D-4-7（キレーション基の必要性の定量的実証）[B-7, A-1] | （独立候補なし; D-4-5/D-4-9に部分吸収） | ⚠️ R1（独立性後退）|
| D-4-8（合成標的との接続の不在）[A-2] | （独立候補なし; A-2が消失し D-4-8 は別テーマ）| ⚠️ R2（消失）|
| — | D-4-2（Ru(0)活性種の実在証拠）[U-2, A-1, B-3]【新規】 | ✅ 新規独立候補（multi-critical U-item 独立記録 v18.1）|
| — | D-4-4（基質スコープの乖離）[U-3, B-5]【新規】 | ✅ 新規独立候補（U-3 high severity、v18.1規則）|
| — | D-4-7（先例引用における酸化状態マニホールドの不整合）[C-2, C-4, B-11, A-1]【新規】 | ✅ 新規独立候補（C項目起点の候補が初めて独立化）|
| — | D-4-9（C-H結合開裂機構とKIE不在）[A-1, U-1, C-2]【新規; fallback rule (a)】 | ✅ 新規独立候補（フォールバック規則明示的適用）|

### スコアカード

| 評価項目 | v182 | v184 | 判定 |
|---------|------|------|------|
| D-4候補数 | 8（デフォルト上限） | 9（拡張上限適用: critical/high U×3件） | ✅ v184改善（拡張上限を初めて発動）|
| D-4候補本文の平均文数 | ≈4〜6文（単段落または2段落）| ≈9〜11文（4要素構造）| ✅✅ v184改善（C18直接効果）|
| D-4候補本文の4要素構造 | なし | 全9候補で問い/処理様態/帰結/Stage 1関係を明示 | ✅ v184改善（C18直接効果）|
| U 項目数 | 2 | 4（+U-2 Ru(0), +U-3 scope） | ✅ v184改善 |
| multi-critical U 独立展開 | U-1のみ独立 | U-1→D-4-1, U-2→D-4-2, U-3→D-4-4（3件独立） | ✅✅ v184改善（シグナル3 検出）|
| フォールバック規則の明示的候補紐付け | 記述あり（漠然） | (a)→D-4-9, (b)→D-4-3 明示的マッピング | ✅ v184改善（シグナル4 検出）|
| C項目起点の独立D-4候補 | なし | D-4-7（C-2, C-4起点）として初出現 | ✅ v184新規 |
| priority_structure ピボット | A-1↔B-7, B-8↔B-2（2件） | A-1↔B-2, A-1↔B-1（2件）| △（機構留保↔定量省略の連鎖として読み替え）|
| OI-055（実用条件外挿問い）の解消 | 未解消（消失）| D-4-8として独立化（OI-055 解消）| ✅ v184解消 |
| propositional | "Ruthenium complexes catalyze ortho-selective C–H/olefin coupling of aromatic ketones or acylheteroaromatics." | "Ruthenium complexes catalyze addition of aromatic carbon–hydrogen bonds to olefins." | ⚠️ R3（v184がやや後退。v182のほうがortho-selective・acylheteroaromatics を明示）|
| scope_type | tool_question | tool_question | ≡ |

### 4シグナル評価（ユーザー指定）

| シグナル | 評価 | 根拠 |
|---------|------|------|
| 1. D-4候補本文 analytical depth 増加（C18 の4要素構造、6〜12文） | **✅ 確認** | v182: 平均4〜6文の単段落または2段落構造; v184: 全9候補で4パラグラフ×4要素、平均9〜11文。C18の直接効果が明確。|
| 2. D-4候補数が上限8に到達または上限超え | **✅ 確認（上限超え）** | v182: 8候補（デフォルト上限ちょうど）; v184: 9候補（拡張上限発動）。v18.4 の C17 CoT scaffolding が critical/high U×3件を正確に集計し、拡張閾値を自律的に発動した。Kumada v184（8候補）と合わせ、上限到達・超えの両パターンを確認。|
| 3. critical/high U項目が複数ある場合、それぞれが独立D-4候補として展開されているか | **✅ 確認（murai で初検証）** | U-1(critical)→D-4-1, U-2(high)→D-4-2, U-3(high)→D-4-4 の3件独立展開。各候補本文でmulti-critical U-item独立記録規則（v18.1）への明示的言及あり。Kumada v184ではhigh U×1件のためテスト不可だったが、murai v184で初めて検証完了。|
| 4. high_convergence_high_gap 項目が D-4 候補に明示的に紐付いているか | **✅ 確認（フォールバック経由）** | 両版ともhigh_convergence_high_gap=空（通常ケース）。v184ではフォールバック規則の明示的マッピングが顕著に改善: (a)→D-4-9「フォールバック規則(a)最優先」, (b)→D-4-3「フォールバック規則(b): B-3 convergence 3/3」, 各temperature_noteに規則番号が記載。v182のフォールバック記述は候補名と項目IDが曖昧だった。|

### 総合判定: **v184 > v182**

4シグナルすべてが確認された。Entry 056（kumada）で確認できなかったシグナル3（multi-critical U独立展開）が murai で初めて実証された。C18（4要素構造）とC17（CoT scaffolding）の複合効果が候補深度・候補数・U独立展開の同時改善として表れている。また C項目起点のD-4候補（D-4-7）が初めて生成されたことは、C18の4要素構造が Stage 1 の全分類を D-4 に接続する回路を拡大することを示唆する。

### 正の副次効果

- **OI-055 解消**: v182 で消失していた「実用条件外挿問いの独立D-4化」が v184 では D-4-8 として明示的に独立化した。Entry 055 R1 の直接解消であり、open_issues OI-055 をクローズする。
- **シグナル3初検証完了**: Kumada v184 で検証できなかった multi-critical U 独立展開（U×3独立）が Murai v184 で確認された。Entry 056 の懸案が本エントリで解消。
- **C項目起点のD-4候補の初出現**: D-4-7（先例引用の酸化状態マニホールドの不整合, C-2 + C-4）は C-item が D-4 の primary source となった初例。C18 の4要素構造が「引用の機構的適切性」という分析ベクターを D-4 に接続した。
- **DQBラベルの適切な適用**: D-4-6 が「Dropped Quantitative Benchmark」と明示的にラベル付けされており、分類語彙の一貫した使用が確認された。

### 確認された退行・懸案

- **R1**: v182 D-4-7（キレーション基の必要性の定量的実証 [B-7, A-1]）が v184 では独立候補として存在せず、D-4-5（B-9経由）と D-4-9 に部分吸収。B-7 は D-4-8 の grounded_in（B-6, B-7, B-1）には含まれるが、「ケトン以外の指向基での非反応性の検出下限」という固有の問いが消えている。ただし9候補中での吸収であり、severity=medium のB-7問い（V1-Q5）として許容範囲内。open_issues 新規追記は不要。
- **R2**: v182 D-4-8（合成標的との接続の不在 [A-2]）が v184 では独立候補として存在しない。A-2 が v184 では Stage 1 の独立 A 項目として記録されておらず、D-4-8 のテーマは全く異なる（実用条件外挿）。合成標的接続問いは severity=low（v182では最後の候補として配置）であり、実用条件外挿問い（OI-055 内容）の独立化と比較して優先度が逆転した結果として許容範囲内。open_issues 新規追記は不要。
- **R3**: v184 の confirmed_english_propositional が v182 より後退（ortho-selective・acylheteroaromatics の明示が失われた）。v182: "Ruthenium complexes catalyze ortho-selective C–H/olefin coupling of aromatic ketones or acylheteroaromatics." vs v184: "Ruthenium complexes catalyze addition of aromatic carbon–hydrogen bonds to olefins." 本論文の最小主張は "addition of C–H bonds to olefins" でありどちらも正確だが、v182 の表現がより情報量が高い。Stage 0/1 には変更がないため、propositional の差異は D-4 生成の CoT が E 節推論に影響した可能性がある。新規 OI 追記。→ OI-056

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
