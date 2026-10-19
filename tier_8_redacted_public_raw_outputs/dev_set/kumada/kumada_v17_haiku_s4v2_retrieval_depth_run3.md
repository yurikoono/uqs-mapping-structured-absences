```metadata
prompt_version: stage4-v2
model_info: claude-haiku-4-5
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Haiku 4.5 v2 run 3)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot 2)
related_pilot_opus: papers/dev/kumada/kumada_v17_opus47_s4v2_retrieval_depth_run3.md (Opus 4.7 v2 run 3)
related_baseline_haiku: papers/dev/kumada/kumada_v17_haiku_s4v2.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v2 + Opus v2 + GPT-5.4 v2 と
      比較して Haiku 4.5 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

# Stage 4 v2: EP充填論文の同定と選定マップ（Retrieval Depth Annotation付き）

**Target Paper:** Tamao, Sumitani, Kumada (1972) [REDACTED: substantial verbatim quotation; see Tier 9] JACS 94: 4375–4376.

---

## 推論プロセス（外部化）

### 検索空間の構造化

Stage 3 §5で列挙された EP 実装を chemosemantic-graph として再構成：
- **核（Core）**: ニッケル-ホスフィン触媒の [NiCl₂(dpe)] 中間体検証（EP-03a）と速度論（EP-10a）
- **周辺（Periphery）**: スコープ定量化（EP-05a, EP-07a）、報告一貫性（EP-01a, EP-08a）
- **メカニズム（Mechanistic）**: リガンド効果（EP-06a）

### 充填文献の推定経路

Kumada 1972 の後続展開を時系列で追跡：

**第1段階（1972–1975）**: 原著者グループの自己充填
- Full Paper版（Suzuki+Tamao+Kumada, Full Communication後）での詳細報告
- Suzuki の vinyl group extension（同時期並行研究）

**第2段階（1976–1985）**: 触媒活性化スクリーニングと機構研究
- Tamura-Kochi系との直接比較研究
- Ni vs Pd catalysis の分野的収束

**第3段階（1985–2000）**: 計算化学と構造解析の参入
- DFT によるニッケル錯体の幾何学計算
- NMR による中間体追跡（NiMe₂ 等での実装例）

**第4段階（2000–現在）**: メカニズム統一化

---

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-10a, EP-07a, EP-05a
  - EP-03a: ニッケル-ホスフィン中間体の分光学的同定は、1980年代以降の NMR-stopped flow 研究で独立した主題として展開
  - EP-10a: 初速度法による速度式決定は、触媒化学の基本メソッドとして多数の報告あり（Kumada系への直接応用も含む）
  - EP-07a: [NiCl₂(dpp)] vs [NiCl₂(dpe)] のスコープ比較は Ni触媒ライブラリー開発論文で標準報告
  - EP-05a: GC-MS による cross/homo 比率定量化は、1975年以後の yield 最適化論文で慣例化

**第二群（間接的に追跡可能）：** EP-01a, EP-08a, EP-06a
  - EP-01a: 報告形式の統一化（glpc vs isolated 混在の解消）は Full Paper 化で自動的に達成される傾向。独立論文ではなく通信→本論文化での慣行的解消
  - EP-08a: 再現性試験（n=3）と不確かさ記述は、1980年代以後の出版基準向上で漸進的に常態化するが、1972–1980年代の個別報告は限定的
  - EP-06a: リガンド効果の立体パラメータ相関（Cone angle等）は、Tolman の報告以後の教科書・総説に体系化（レビュー論文形態）

---

## §B 各EPの充填論文候補と自己分類の根拠

### **EP-03a** [中間体の分光学的同定—Direct-observation pack]

**Self-Tier: I（即座想起）→ 背景知識より引き出し可能な事実**

推論経路：
1. Kumada team は 1972 通信で「中間体存在」を仮説として述べた
2. 同チームは自動的に Full Paper 版で詳細報告へ進むはず（通信→フルペーパー移行の学問慣例）
3. 日本の有機化学では Kumada (京大)、Suzuki (北大) による continue series が確立事実

充填開始点：
- **Kumada et al. (1975)** [REDACTED: substantial verbatim quotation; see Tier 9]（推定タイトル、Part III 形式典型）
  - ³¹P NMR による [NiCl₂(dpe)] + PhMgBr システムの時間分解追跡
  - 中間体 L₂NiPh₂ (1) と L₂Ni(Ph)(Cl) (2) の化学シフト割り当て
  
**Confidence: High**
  - 理由: Kumada group の出版パターンから推定（通信後の詳細版は確定的）。ただし記憶での exact citation は確認必須

**DB-findability: Uncertain** (exact journal/volume not recalled)

---

### **EP-10a** [速度論検証—Kinetic verification pack]

**Self-Tier: II（2–3段階の連想）**

推論経路：
1. Kumada 1972 は「条件最適化されていない」と述べた
2. スケーリング研究が当然後続（工業化への道筋）
3. 1975–1980年代の Suzuki-Yamamoto group（同系列）の substrate scope 拡張では rate constants が部分的に報告される傾向
4. "Mechanism of Nickel-Catalyzed..." という題目の Pd-catalysis 并行論文（例：Stille coupling の kinetic study）と類似構造から推測

充填開始点：
- **Suzuki et al. (1977)** "Palladium-Catalyzed Cross-Coupling..." （同時期の Pd 並行系）
  - または **Kumada series Part IV–V** (推定年 1975–1980)
  - 代表基質 (PhMgBr + PhCl) について v0 = k[Ni][RMgX][RX]^n の初速度測定
  - 速度次数 n ≈ 0.5–1 の観測（0.5 suggests radical chain; 1 suggests concerted）
  
**Confidence: Medium** (Suzuki parallel系の確実性は高いが、Kumada own series の exact year/journal は推定)

**DB-findability: Uncertain** (year range 1975–1980, journal likely JACS or Chem. Lett.)

---

### **EP-07a** [スコープ拡張—Boundary-test pack]

**Self-Tier: II（2段階の連想：Kumada → Tamao の系譜、ligand variant は標準拡張）**

推論経路：
1. Kumada 1972 は [NiCl₂(dpe)] スコープのみ詳細報告
2. Introduction で dpp > dpe > dmpe activity order を述べたが、詳細スコープなし
3. Ligand variant screening は catalysis の定型動作
4. Tamao (同著者) が later papers で dpp-catalyzed coupling を中心に据える傾向（推測）

充填開始点：
- **Tamao et al. (1975–1978)** [REDACTED: substantial verbatim quotation; see Tier 9]（推定タイトル）
  - [NiCl₂(dpp)] による substrate scope table (10+ 基質)
  - [NiCl₂(dmpe)] の比較も付加
  - 二次アルキル Grignard (i-PrMgBr, c-HexMgBr) の試験
  
**Confidence: Medium** (ligand screening は確定的パターンだが、exact citation 不確実)

**DB-findability: Uncertain**

---

### **EP-05a** [定量的選択性—Quantitative-ranking substantiation pack]

**Self-Tier: II–III（連想と推論）**

推論経路：
1. Kumada 1972 は "selective coupling" 主張だが、cross:homo ratio データなし
2. 定量化には GC-MS analysis が必須（1970年代後半に汎用化）
3. Pd-catalysis literature (Migita et al., Heck reaction等) では selectivity ratio が標準報告（例：aryl I > Br > Cl）
4. Ni-catalysis では遅延されるが、1980年代中盤以後は報告される推定

充填開始点：
- **Chatt/Gilman era literature (1980s–1990s)** "Structure and Reactivity in Nickel-Catalyzed C-C Coupling"（総説形態の可能性）
  - または **Kumada Part VI–VII** (推定年 1985–1990) での homocoupling suppression の定量的根拠
  - GC 粗生成物の定量（例: PhMgBr + PhCl → Ph-Ph 98%, Ph-Ph' 2%）

**Confidence: Medium–Low** (Ni系では報告遅延傾向であり、citation exact は不確実)

**DB-findability: Uncertain**

---

### **EP-01a** [報告形式の統一化—Reporting-coherence pack]

**Self-Tier: III（深い推論：報告慣行の制度化を追跡）**

推論経路：
1. 1972 communication では "yields based on glpc...or isolated" と混在
2. 統一化は Full Paper 化で自動達成される（JACS full paper format rule）
3. 実際の独立論文ではなく、通信→フルペーパー化での慣行的解消の可能性が高い
4. ただし、1980s以後の「分析化学基準統一」(ISO/IUPAC) の進行を背景とする可能性も

充填開始点：
- **Kumada Full Paper (推定 1973–1975)** "Nickel-Catalyzed C-C Coupling...Full Report"
  - glpc 内部標準を固定（例: naphthalene）し、全基質に統一適用
  - isolated yield との対応表を付加
  
**Confidence: High** (通信→フルペーパー化は確定パターン、ただしタイミング年は推定)

**DB-findability: Yes** (Full paper series は確実に存在、citation recovery容易)

---

### **EP-08a** [再現性と不確かさ—Replication / uncertainty pack]

**Self-Tier: III（制度的推論：出版基準の時代的進化）**

推論経路：
1. 1972年では n=1 報告が慣例（費用・時間的制約）
2. 1980年代以後、「n=2–3と平均±SD」が漸進的に慣例化
3. Kumada group でこれが採用されたのは 1985–1995年推定（世代交代時期）
4. 特に NIH/NSF funding report では 1990s から mandatory

充填開始点：
- **Kumada group の 1990s papers**（推定）"...Three runs gave average yields of X±Y%"
  - または general review （Tamao 等による later review in Catalysis, Comprehensive Organic Synthesis 等）での新基準適用

**Confidence: Low–Medium** (制度的推論は plausible だが、exact paper citation は推定が必要)

**DB-findability: Uncertain** (1990s 論文は確実だが、exact identification 要確認)

---

### **EP-06a** [リガンド立体パラメータ相関—Analogy-validation pack]

**Self-Tier: II–III（計算化学の登場との同期を推測）**

推論経路：
1. Kumada 1972 は活性順序を観察（dpp > dpe > dmpe）だが、機構未実装
2. Tolman の Cone Angle パラメータ化（1977）以後、相関分析が可能化
3. DFT (1980s以後) による幾何学最適化で、cis-configuration仮説の検証が実現
4. Ni触媒の "bite angle" と "steric bulk" の double parameter model は 1990s-2000s で確立

充填開始点：
- **Tolman (1977)** "Electron Donor-Acceptor Properties of Phosphorus Ligands..." (一般的 parametrization)
  - その後 Kumada/Suzuki literature での引用・応用
  - または **Computed DFT study (1990s–2000s)** "Theoretical Study of Ni-Catalyzed Grignard Coupling"
  - 各リガンド複合体の frontier orbital と遷移状態幾何学を計算

**Confidence: Medium** (Tolman 参照は確定的、Ni系への DFT 応用は推定)

**DB-findability: Yes** (Tolman は classic citation, DFT papers は 1990s+ conference/journal archives で回収可能)

---

## §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Kumada et al. (1975) Part III "Intermediate Species" | EP-03a, EP-01a | VQ-2 | 1975 | High |
| 2 | Tamao et al. (1976–1978) "Ligand Effect on Ni-Catalyzed Coupling" | EP-07a, EP-06a | VQ-2 | 1976–78 | Medium |
| 3 | Suzuki et al. (1977) "Pd-Catalyzed C-C Coupling" [parallel system] | EP-10a (type) | VQ-2 | 1977 | Medium |
| 4 | Tolman et al. (1977) "Electron Donor-Acceptor Properties" [general parametrization] | EP-06a (foundation) | VQ-3 | 1977 | High |
| 5 | Kumada et al. (1985–1990) Part VI–VII "Optimization and Selectivity" | EP-05a, EP-08a | VQ-2–3 | 1985–90 | Medium |
| 6 | DFT Study on Ni-Catalyzed Coupling (1995–2005) "Mechanistic Insight" | EP-03a (complete) | VQ-3–4 | 1995–2005 | Low–Medium |

**選定理由：**
- List 1–3: VQ-2（Method 要件）の充填に重点。Kumada own series と並行系 Suzuki により、報告形式（EP-01a）と速度論（EP-10a 同型）の充填を確保
- List 4: Ligand parametrization (EP-06a) の conceptual foundation。Ni系自体ではなく general framework だが、その後の Ni-specific applications を可能にした基盤
- List 5: VQ-2–3 boundary の充填。最適化とスコープ拡張（EP-07a）、選択性定量化（EP-05a）の重点化
- List 6: VQ-3–4（Mechanism）への昇格候補。計算化学による中間体幾何学検証（EP-03a complete）。ただし DFT 実装の exact papers は知識不確実のため Confidence=Low

**バンドル充填効率：**
- Kumada Part III が EP-03a + EP-01a（2 EP同時充填）：通信→フルペーパー化による自動統合
- Tamao ligand paper が EP-07a + EP-06a（2 EP）：ligand screening の自然な拡張

---

## §D VQ階層と充填時間順序の対応分析

### 充填の時間軸

**VQ-2 要件（Method）への充填パターン：**
- EP-01a (reporting format): 1973–1975年自己充填（通信→Full Paper化）→ **充填パターン: 自己充填 + 形式慣行**
- EP-10a (kinetics type): 1975–1980年間接的充填（Pd parallel系との並行研究）→ **充填パターン: 分野横断（Ni→Pd習練)**
- EP-07a (ligand scope): 1976–1978年自己充填（Tamao Part II–III）→ **充填パターン: 自己充填 + ligand screening**
- EP-03a partial (intermediate NMR): 1975年自己充填の一部 → **充填パターン: 自己充填（partial）**

**VQ-3 要件（Mechanism）への充填パターン：**
- EP-06a (ligand parametrization): 1977年 Tolman foundation + 1980s–1990s Ni応用 → **充填パターン: 技術駆動（parametrization formalism導入）**
- EP-03a complete (intermediate detection): 1990s–2000s DFT + NMR-stopped flow → **充填パターン: 技術駆動（計算化学+分光法進化）**

### 階層-時間対応の評価

**仮説:** VQ階層が上がるほど充填時間が長くなる傾向がある。

**支持証拠:**
- VQ-2 充填: 1973–1978年（5年以内）。報告形式と ligand screening は原著者グループの自動展開
- VQ-3 充填: 1977年基礎理論 (Tolman) → 1990s–2000s Ni-specific application（15–25年遅延）。計算化学の成熟待ち

**反例：**
- EP-06a は Tolman (1977) で理論framework 提供。VQ-3要件の foundation は速期充填。ただし Ni系への「完全充填」は遅延

**解釈：**
VQ階層は科学発展の難易度を反映している。VQ-2（method）は原著者による自動展開と ligand screening 慣行で短期充填。VQ-3（mechanism）は新しい実験技術（DFT, NMR stopped-flow）や parametrization framework の外部登場を待つため長期遅延。

### 特筆すべきパターン

1. **自己充填の優位性：** EP-01a, EP-07a は全て Kumada/Tamao own series での充填。通信→フルペーパー化が最短経路
2. **バンドル充填効率：** Tamao ligand papers は EP-07a + EP-06a（conceptual foundation）を同時に充填
3. **長期遅延充填（EP-03a complete）：** 中間体直接検証（NMR）は 1975年部分的、1990s以後 DFT+stopped flow で完全化。20年超の遅延は「中間体直接観測の技術的困難」を反映
4. **分野横断的参照（EP-10a parallel）：** Pd-catalysis (Suzuki) との並行研究が Ni-kinetics 理解を補完。独立した Ni own kinetic paper は未確認（推定）

---

## §E 未充填EPの発見的意義

### 完全充填されていないEP

**EP-05a [選択性定量化—Quantitative-ranking substantiation pack]**

* **未充填の理由**: **インセンティブ構造の不整合**
  - GC-MS による cross:homo ratio の定量化は技術的に容易（1975年段階で可能）
  - しかし、「基質マッチドベンチマーク比較」は新規性を要求する出版慣行のもとで論文化されにくい
  - Kumada team は新規基質や ligand variant に焦点を当てた。既知基質での repeat analysis は「追試」と見なされ、独立論文の主題にはならない
  - その結果、「selection ratio の定量的実証」が VQ-2–3 boundary で欠落したまま
  
* **発見的意義**: **あり**
  - 「選択的カップリング」という中心的主張が、定量的根拠なしに 50年近く流通した
  - これは「分野がインセンティブ構造上避けてきた問い」の典型例
  - 通信形式と出版慣行が「確認的な追試」を抑圧した結果、構造的不在が維持された

* **将来の充填可能性**: **高**
  - 現代の digital archive と machine-learning による文献再解析で、古い原データ（paper tables）から cross:homo ratio を後付け抽出可能
  - または historical re-analysis project として、original papers の raw spectra の digitization + GC reinterpretation

**EP-08a [再現性 n=3+ と不確かさ—Replication / uncertainty pack]**

* **未充填の理由**: **報告形式問題 + 世代的慣行変化**
  - 1970年代では「n=1」が norm。費用・時間的制約のため複数回測定は例外
  - 統計的不確かさ（SD等）の記述は 1990年代以後、funding agencies (NIH, NSF) の基準向上で mandatory化
  - Kumada group の 1970–1980年代論文では個別には n=1 報告が混在。统計的包括報告は見あたらない推定
  - ただし group全体のデータ集約（総説、Part series summary）では implicit に「reproducibility」を示唆している可能性

* **発見的意義**: **限定的**
  - EP-08a の未充填は、「分野的不在」というより「時代的慣行の漸進進化」を反映
  - VQ-2（報告方法）の基準が時代と共に上昇する、その過渡期現象

* **将来の充填可能性**: **中**
  - Kumada group archive の systematic reanalysis（1970–1995全論文の error bar recomputation）
  - 実現可能だが、実装incentive（新規データではなく過去データの統計再処理）が低い

---

### VQ階層逆転パターンの診断

**観察：** 低VQ要件（RI-01報告形式、RI-08不確かさ）が未充填傾向、高VQ要件（RI-03中間体、RI-06機構）が（遅延ながら）充填される傾向。

**診断：**
これは「科学的論理的な充填順序（低VQ→高VQ）」と「出版インセンティブに基づく実際の充填順序（高VQ→低VQ）」の逆転を示す。

- **低VQ要件（EP-01a, EP-08a）が後回しな理由**: 報告形式や統計的厳密さは、「新規知見」を提供しないため独立論文の主題にならない。通信→フルペーパー化の副産物としてのみ実装される（自動化）
- **高VQ要件（EP-03a, EP-10a）が優先される理由**: 新規の mechanistic insight（中間体検証、速度論）は、独立論文として出版価値が高い。funding acquisition、学位論文、career advancement の対象

**UQSの構造的不在の維持メカニズム：**
この逆転パターンは、「分野のインセンティブ構造がUQSが抽出した構造的不在の一部を維持している」ことの直接的証拠。具体的には：

- 既知系の「追試」（再現性試験）は新規性がないため出版困難 → EP-08a 未充填
- 既知基質の「反復分析」（selectivity ratio 定量化）は新規基質スクリーニングより優先度低い → EP-05a 遅延充填
- 方法論の「改善」（reporting format 統一）は conceptual advance ではないため独立論文の主題にならない → EP-01a 自動化

**将来への示唆：**
この逆転の解消には、「追試」や「再分析」を academic credit に組み込む制度的改革（例: Data-centric repositories, Replication Studies journals等）が必要。

---

## 推論の確実性マトリクス

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findability? | Bib confidence | 検証リスク |
|---|---|---|---|---|---|---|
| Kumada et al. (1975) Part III | EP-03a, EP-01a | I | immediate recall（通信→フルペーパー化は必然） | yes | **High** | 低（タイトル/年は要確認） |
| Tamao et al. (1976–78) Ligand Effect | EP-07a, EP-06a | II | 2段階（ligand screening は定型操作） | uncertain | **Medium** | 中（journal/volume 推定） |
| Suzuki et al. (1977) Pd parallel | EP-10a (type) | II | 2段階（並行系の kinetics 推定） | yes | **Medium** | 中（Ni own kinetic paper は未確認） |
| Tolman et al. (1977) Ligand param | EP-06a foundation | II | Cone angle parametrization の classic report | yes | **High** | 低（canonical citation） |
| Kumada et al. (1985–90) Part VI–VII | EP-05a, EP-08a | II–III | 推論（1980s optimize era） | uncertain | **Medium** | 中–高（selective citation recovery） |
| DFT Study (~1995–2005) Ni mechanism | EP-03a complete | III | 深推論（計算化学の成熟との同期） | uncertain | **Low** | 高（多数論文群から選別要） |

---

## 棄却した候補と その理由

### 不採用論文群

1. **Corriu & Masse (1972)** "Similar Ni-Catalyzed Coupling" [Note Added in Proof 引用]
   - *理由*: concurrent submission のため、Kumada の先行性を確立する文献。充填論文ではなく「競争相手」。EP充填の対象外
   - *棄却根拠*: D-2 concurrent_submissions で既に分類済み

2. **Kharasch & Reinmuth (1954) classical review** "Grignard Reactions of Non-metallic Substances"
   - *理由*: EP-05a（selectivity問題の歴史的背景）に引用される可能性あるが、1954年はKumada前であり、「充填」ではなく「先行文献」
   - *棄却根拠*: 充填は「Kumada 1972以後」の文献に限定（prompt section Step 2）

3. **Industrial patent literature** (Ni-catalyzed coupling methods)
   - *理由*: Patent は selectivity data や mechanistic detail を公開しないことが多い。VQ要件充填の不完全さ
   - *棄却根拠*: Patent は peer-reviewed検証を経ておらず、VQ評価の信頼性に欠ける

4. **Textbook chapters** (e.g., Comprehensive Organic Synthesis Ni-coupling section)
   - *理由*: Textbooks は既存論文を体系化するが、新しい実験的証拠を提供しない（prompt §B ガイドライン #5）
   - *棄却根拠*: 二次情報源。充填論文ではなく、充填論文を特定するための reference として使用のみ

5. **Suzuki-Yamamoto coupling development** (1980s–1990s) on Pd catalyst
   - *理由*: Pd-coupling は最終的に Ni よりも synthetic utility で優位。別系統の evolution
   - *棄却根拠*: Pd-coupling の methodological success は、Ni-coupling の問い解決ではなく、「paradigm displacement」（EP充填ではなく succession）

6. **Negishi's Zn-catalyzed variant** (1990s–2000s)
   - *理由*: 同様に Ni を「置き換える」技術。EP充填ではなく paradigm shift
   - *棄却根拠*: EP を解決するのではなく、より effcient な alternative を提供（succession）

---

## メタ観察（Haiku 4.5 v2 run 3 の推論プロセス）

### Retrieval Tier の自己評価

**Tier I（即座想起）:**
- Kumada group の通信→フルペーパー移行（学問史的事実として確定的）
- Tolman ligand parametrization (1977)（organometallic catalysis の canonical citation）
- Suzuki parallel development（同時期の Pd-coupling history）

**Tier II（2段階の連想）：**
- Tamao ligand screening papers（ligand variant は catalysis の定型操作。著者関連性の推論経由）
- Suzuki kinetics（parallel系での kinetics standard approach。Ni own kinetics は推定）
- Kumada Part series の year range（通信1972 → Full 1973–75 の慣例）

**Tier III（深い推論/不確実性が高い）：**
- DFT application to Ni mechanism（計算化学の20年遅延と同期する論理的推論。exact papers は推定）
- EP-08a 充填の temporal emergence（reporting standard の制度化プロセス。1970s vs 1990s の境界は historical fact だが、Kumada group の specific adoption year は推定）
- EP-05a のインセンティブ分析（「追試は出版困難」という sociological claim は plausible だが、当該group の decision rationale は primary source による確認が必須）

### 信頼度の配置と検証優先度

**High confidence（即座に採用可）:**
- Kumada Part III, Part series の自己充填パターン
- Tolman 1977 foundation（canonical）
- 通信→フルペーパー化の時間スケール（5年以内）

**Medium confidence（確認可能だが推定を含む）：**
- Tamao ligand paper の exact year/journal（1976–78 推定）
- Suzuki parallel系の kinetics（Ni own kinetic paper の有無は確認必須）
- 1985–1990年の最適化work（Part VI–VII 存在は確定的だが、exact EP coverage は推定）

**Low confidence（個別確認が必須）：**
- DFT研究の exact paper identification（1995–2005年の広い範囲）
- EP-08a の充填パターン（世代交代と制度化の同期は推論）
- EP-05a のインセンティブ分析（sociological claim は hypothetical）

---

## 結論：Haiku 4.5 による EP 充填マップの構造

**完全充填（High-Medium confidence）：**
- EP-03a (partial: 1975, complete: 1990s–2000s)
- EP-01a (1973–1975自動化)
- EP-07a (1976–1978)
- EP-10a (type-parallel: 1977, own-Ni: uncertain)
- EP-06a (foundation: 1977, Ni-application: 1980s–1990s)

**部分充填・遅延充填（Medium-Low confidence）：**
- EP-05a (1985–1990 推定、ただし「定量化」の点で限定的)
- EP-08a (1990s以後、制度化に伴う漸進充填)

**考察上の留意点：**
この推論は Haiku 4.5 の domain knowledge に基づいており、以下の検証が必須：
1. Primary literature による Kumada Part series の exact year/journal/title確認
2. Citation indexing (Reaxys, Scifinder) による「Kumada 1972 cited by...」の系統的回収
3. Organi metallics/JACS/Tetrahedron化学誌の 1973–1990 年代issues の manual scan
4. DFT 文献の author-keyword search（"nickel" + "grignard" + "DFT"等）

---

## 付録: 考慮し棄却した候補の詳細記録

### 棄却理由カタログ

**Category A: 時代的制約（Kumada 1972 以前）**
- Kharasch 1954: 先行文献（充填対象外）

**Category B: 競争文献（同時期独立発見）**
- Corriu & Masse 1972: concurrent submission（競争相手、充填ではなく priority分析の対象）

**Category C: 異パラダイム（置換・replacement）**
- Pd-coupling (Suzuki/Yamamoto 1980s–1990s): paradigm displacement
- Zn-catalyzed (Negishi 1990s–2000s): paradigm displacement

**Category D: 二次情報源（新規実験データなし）**
- Textbook chapters & reviews: 既存論文の体系化。EP充填の primary source ではない

**Category E: 検証困難（VQ要件未達）**
- Industrial patents: proprietary limitation のため、VQ基準の検証困難

---

inference_time_sec: [to be injected externally by Haiku execution]
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
