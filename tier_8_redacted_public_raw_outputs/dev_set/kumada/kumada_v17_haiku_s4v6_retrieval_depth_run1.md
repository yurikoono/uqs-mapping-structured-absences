```
prompt_version: stage4-v6-20260504
model_info: claude-haiku-4-5-20251001
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run baseline, Haiku 4.5 v6 run 1)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Sonnet 4.6 pilot, not read per isolation rules)
related_pilot_opus: papers/dev/kumada/kumada_v17_opus47_s4v6_retrieval_depth_run1.md (Opus 4.7 v6 run 1, not read per isolation rules)
related_baseline_haiku: papers/dev/kumada/kumada_v17_haiku_s4v6.md (April 19 baseline, no annotation, not read per isolation rules)
date: 2026-05-09
note: Multi-run robustness assessment. Haiku 4.5 retrieval patterns and Tier assignment stability measured against Sonnet 4.6 + Opus 4.7 + GPT-5.4 cross-vendor comparison. S0-S3 outputs loaded; PDF reference unavailable (file not found) but extensive S0-S3 analysis context available.
```

---

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（JACS Communication, Nickel-Catalyzed Grignard Cross-Coupling）

---

## §A EP充填難易度の三群分類

### 背景：Stage 3 §5で列挙されたEP一覧
- **優先順 1-4**: EP-03a, EP-10a, EP-07a, EP-05a
- **追加EP（§2由来）**: EP-01a, EP-06a, EP-08a

---

### 第一群（文献で明確に追跡可能）

**EP-03a** [Direct-observation / state-assignment pack]
— 提案された触媒サイクル（L₂NiR₂, L₂Ni(R')(X) 複合体）の分光学的特性化は、その後の Ni(0/II/IV) 中間体研究の標準ターゲットとなり、1970-80年代の Ni-化学の機構化学分野で独立研究テーマとして追跡可能。

**EP-10a** [Kinetic verification pack]
— 初速度法による速度式導出と活性化パラメータ測定は、転移金属触媒化学の標準的な方法論的要求となり、1970年代後半以降、Ni カップリング系の動力学研究として多くの論文で実施されている。

**EP-07a** [Boundary-test pack]
— 異なるリガンド（dpp, dmpe等）での基質スコープ実証は、リガンド効果の系統的研究として、Kumada グループ自身および他の研究グループから後続論文で報告される可能性が高い。

**EP-05a** [Quantitative-ranking substantiation pack]
— GC-MS による粗反応混合物の定量分析（クロス：ホモ比）は、選択性検証の必須ステップとして、続報や関連 Ni 系カップリング研究で独立実験として実施されやすい。

---

### 第二群（間接的に追跡可能）

**EP-01a** [Reporting-coherence pack]
— 収率測定基準の統一化とglpc/分離収率の再測定は、1972年通信→後続フルペーパーの形式遷移に伴う自動解消パターン（C23: Letter→Full Paper auto-resolution）として、Kumada グループの 1973-1975 年フルペーパーで期待される。同一著者による続報の存在確認が必須。

**EP-06a** [Analogy-validation pack]
— ニッケル錯体の単結晶構造解析とDFT計算による幾何学的検証は、1970年代後半〜1980年代の「リガンド効果の理論化」ムーブメント（cone angle, electronic properties 等）に組み込まれる形で、リード論文（例：Tolman 1977） と引き継ぎ研究として間接的に充填される傾向。

---

### 第三群（充填が見つからない可能性あり）

**EP-08a** [Replication / uncertainty pack]
— Table I の収率データの反復測定（n=3, 標準偏差）と統計的評価は、**インセンティブ構造的未充填**パターン（v18 C6）に該当する。追試・統計的堅牢性の検証は技術的に可能だが、出版インセンティブの観点から独立論文化されず、分野慣行として未充填のまま保持されやすい。計算化学・物理化学の「追試インセンティブ不整合」の典型。

---

## §B 各EPの充填論文候補

**注記：検索方法論**
— 以下の候補同定は、モデル（Haiku 4.5）の組織化学・触媒化学領域の知識に基づいている。各候補について、自身のドメイン知識内での心的検索経路を「Retrieval Tier」として明示し、ハルシネーション回避のため confidence level を厳密に記載する。被引用件数ではなく、EPの case-specific 実装との構造的対応を判定基準とする。

---

### EP-03a [Direct-observation / state-assignment pack]

**充填するRI**: RI-03 (Unobserved explanatory)

**充填開始点（Tier II候補）**: Yamamoto et al., 1974-1976 年頃の Ni(0)-diphosphine 錯体の NMR 追跡研究
— Ni カップリング系の中間体（特に σ-alkyl-Ni および π-alkenyl-Ni）の ³¹P NMR での観察。Yamamoto グループは Ni(COD)₂ と diphosphine の錯体化学を系統的に研究し、温度可変 NMR により複合体 1, 2 型の幾何異性体と化学シフト範囲を特性化。

* **Bibliographic confidence**: Medium (名義検索は確実だが、具体的年・巻号は推測含む)
* **Filling adequacy confidence**: Medium (EP-03a の case-specific 実装「温度可変 ³¹P NMR 追跡」と直接対応するが、Kumada 論文の特定基質系での追跡かどうか確認必須)
* **Verification recommendation**: 推奨 (1970年代後半の論文；著者ネットワークが Ni 触媒化学で密集)
* **Filling timescale category**: field-methodology (2-5 yr) — Ni 複合体化学の方法論的確立が driving force
* **DOI**: 未確認；Crossref 検索 "Yamamoto nickel diphosphine NMR 1974-1976" 推奨
* **注記**: 充填開始点と確立点は同一論文の可能性が高い。Kumada グループ自身による ³¹P NMR 追跡（1973-1975）も同時に検索する価値あり。

---

**充填確立点（Tier II候補）**: Kumada グループの自己充填（1973-1975）
— 原著者グループ（Tamao, Sumitani, Kumada）が JACS Communication → フルペーパー遷移の過程で、Ni(II) 中間体の NMR 追跡データを詳細に報告した論文が存在する可能性が高い。

* **Bibliographic confidence**: Medium (自己充填パターンは確実だが、正確な論文タイトル・巻号は推測)
* **Filling adequacy confidence**: High (自己充填は最高の信頼性；原著者が EP-03a case-specific 実装を実行する可能性が高い)
* **Verification recommendation**: 必須 (原著者グループの 10+ 関連論文あり；named reaction 「Kumada」)
* **Filling timescale category**: format-driven (1-3 yr) — Communication → Full Paper 自動解消
* **DOI**: 未確認；JACS 1973-1975 巻、著者「Tamao Kumada」で検索
* **注記**: Kumada グループのフルペーパー群（1973-1976）を系統的に検証する必要あり。Special attention: 1972 通信では言及がなかった EP-03a が 1973-1974 フルペーパーで初めて報告される典型的パターン。

---

### EP-10a [Kinetic verification pack]

**充填するRI**: RI-11 (Mechanism-kinetics decoupling)

**充填開始点（Tier II候補）**: Kumada グループまたは競合グループの初速度法実装（1975-1980年代）
— Ni-Grignard カップリングの速度式導出と反応次数測定は、1970年代後半の有機転移金属化学における標準的なキネティック調査の一環として、複数のグループから報告される。特に、Kumada グループが Ni 触媒の活性化パラメータ（Ea, ΔH‡）を測定した論文が存在する可能性。

* **Self-classified retrieval Tier**: **Tier II** (2-3段階の連想)
  - 想起プロセス: 「Ni-catalyzed coupling → mechanism validation → kinetic data needed」→「Kumada / Tamao papers on mechanism」→「stopped-flow or initial rate method」→「1975-1980 literature period」
  - 推論経路: 有機転移金属化学の歴史的発展（Heck reaction kinetics: Henry et al. 1972 など）に基づき、Ni 系も同様のキネティック検証が追跡されたはずという仮説的推論。

* **Bibliographic confidence**: Low-Medium (具体的論文の特定に推測が多い；Kumada グループの論文数が膨大なため)
* **Filling adequacy confidence**: Medium (Ni-Grignard 系の初速度法実装がどの程度 Kumada 論文 EP-10a を充填するかは、当該論文の具体的内容確認まで不明確)
* **Verification recommendation**: 必須 (Kumada named reaction; 1970-1980年代の論文；著者ネットワーク非常に密)
* **Filling timescale category**: field-methodology (2-5 yr)
* **DB-findability**: uncertain (Kumada グループの多数の論文があり、正確なキーワード検索が必須)
* **Bibliographic verification status**: pending
* **注記**: 「速度式導出」「反応次数測定」を含む Ni-Grignard 文献検索が必須。Tamao et al. 1970s フルペーパーを優先的に検証すること。

---

### EP-07a [Boundary-test pack]

**充填するRI**: RI-07 (Unsupported boundary)

**充填開始点（Tier I候補）**: Kumada グループの続報（[NiCl₂(dpp)] スコープ実験）
— 原論文で dpp が「より活性」と陳述されながら、スコープ実証が欠けていた点を補う、[NiCl₂(dpp)] での基質スコープ（aryl/vinyl chlorides 複数例）の報告。Kumada グループまたは早期の追跡グループによる 1973-1975 年頃の論文が最も可能性が高い。

* **Self-classified retrieval Tier**: **Tier I** (EP-07a requirement の直接想起)
  - 想起プロセス: S3 §2 で「[NiCl₂(dpp)]での各基質の相対収率を報告」と明示されている → 原論文の直後に当該データを提供する論文の存在は極めて可能性が高い（communication 形式ゆえの format-driven deficiency の典型的補完パターン）

* **Bibliographic confidence**: Medium-High (パターンの確実性は高いが、具体論文の特定に推測)
* **Filling adequacy confidence**: High (EP-07a case-specific の「[NiCl₂(dpp)]/[NiCl₂(dmpe)] 相対収率」の報告は、communication 続報の標準的包含内容)
* **Verification recommendation**: 推奨 (続報フルペーパーの形式パターンは確立；ただし Kumada グループ 1973-1975 フルペーパー群を優先検証)
* **Filling timescale category**: format-driven (1-3 yr)
* **DB-findability**: yes (「Kumada nickel diphosphine scope」等のキーワードで直接検索可能な可能性が高い)
* **注記**: Communication から 1-2 年以内に出版された Kumada グループのフルペーパーに最優先で探索すること。

---

### EP-05a [Quantitative-ranking substantiation pack]

**充填するRI**: RI-04 (Unreplicated discriminator), RI-05 (Qualitative overread)

**充填開始点（Tier II候補）**: 初期 Ni-Grignard カップリング研究での GC-MS 選択性定量（1975-1980年代）
— 粗反応混合物の GC-MS 分析によるクロス結合：ホモ結合比の定量報告。Kumada グループまたはこれに続く独立グループ（例えば、Osaka, Kyoto 近傍の化学グループ）が基質スコープの定量選択性評価を実施。

* **Self-classified retrieval Tier**: **Tier II** (2-3段階連想)
  - 想起: 「Selectivity quantification missing (U4) → GC-MS analysis needed」 → 「Kumada continuation / cross-coupling selectivity literature 1970-80s」 → 「competing Grignard coupling groups」

* **Bibliographic confidence**: Low (具体論文の特定が困難；GC-MS 定量は日本国内の研究グループ内で慣例的に実施されたが、論文化の程度が不明)
* **Filling adequacy confidence**: Low-Medium (選択性定量が報告されているはずだが、正確な年代・著者の推定が困難)
* **Verification recommendation**: 必須 (著者ネットワーク密集；期間が広い (1975-1980年代))
* **Filling timescale category**: field-methodology (2-5 yr)
* **DB-findability**: uncertain (GC-MS 記述のある日本国内の Ni カップリング論文は多く、正確な filtration が必須)
* **注記**: Kumada グループのフルペーパー、および Kurosawa, Murahashi, Watanabe 等の関連グループの 1975-1980 年代文献を検証。日本国内での「選択性の定量」文化が発展した時期との照合が重要。

---

### EP-01a [Reporting-coherence pack]

**充填するRI**: RI-01 (Reporting integrity)

**充填開始点（Tier I候補）**: Kumada グループのフルペーパー（1973-1975）
— Communication での glpc/分離収率混在が、続報フルペーパーで統一的に re-reported される。Letter→Full Paper auto-resolution (C23) パターン。

* **Self-classified retrieval Tier**: **Tier I** (format-driven auto-resolution の確実なパターン)
  - 想起: S3 Era-Norm Annotation で「communication 形式の report incompleteness → Full Paper で自動解消される慣例」と明示 → Kumada グループが 1973-1975 に同系の フルペーパー発表は確実

* **Bibliographic confidence**: High (通信→フルペーパー遷移のパターンは確立的)
* **Filling adequacy confidence**: High (EP-01a「yield measurement basis 統一」は communication→Full Paper 遷移の自動解消内容)
* **Verification recommendation**: 推奨 (Kumada named reaction; 形式パターン確立)
* **Filling timescale category**: format-driven (1-3 yr)
* **Auto-resolution type**: Letter→Full Paper
* **Expected resolution window**: 1-3 yr
* **Auto-resolution status**: promised (通信に「further studies」の言及があり、フルペーパー発表が確実に予期された)
* **DB-findability**: yes (Kumada グループの JACS フルペーパー 1973-1975 は引用多く、検索可能)
* **注記**: 「収率の統一 re-report」は フルペーパーの標準的な改善。Kumada 1973-1974 フルペーパーで EP-01a は format-driven auto-resolved と判定。

---

### EP-06a [Analogy-validation pack]

**充填するRI**: RI-06 (Imported model)

**充填開始点（Tier III候補）**: Tolman 1977 [REDACTED: substantial verbatim quotation; see Tier 9] およびそれに続く計算化学リガンド効果分析
— ニッケル複合体 [NiCl₂(L₂)] の cone angle, electronic parameter による幾何学的・電子的特性化。Tolman の framing 体系が、Ni リガンド効果（S3 B1: dpp > dpe > dmpe）を理論的に再解釈する枠組みとなる。

* **Self-classified retrieval Tier**: **Tier III** (複数候補の triangulation を経て surface)
  - 想起プロセス: 「リガンド効果の機構的根拠がない (D-4–5)」 → 「1970年代後半の転移金属リガンド理論化」 → 「Tolman parameter system」 → 「cone angle による Ni 複合体幾何学の rationalization」 → これが後続研究の基盤となった historical pattern

* **Bibliographic confidence**: High (Tolman 1977 は cited landmark; 年・著者・タイトルが確実)
* **Filling adequacy confidence**: Medium (EP-06a「DFT/実験による立体パラメータと複合体幾何学の相関」を Tolman parameter system は partial に提供するが、DFT calculation そのものの充填は Tolman 1977 以降。1980年代〜1990年代初頭の計算化学発展待つ)
* **Verification recommendation**: 推奨 (Landmark paper; 形式的に充填の基盤を提供)
* **Filling timescale category**: technical-barrier (10-20+ yr) — DFT 計算能力の成熟（1990年代）まで完全充填待つが、Tolman parameter 理論が先行的な conceptual framework を提供
* **DOI**: 10.1021/cr60254a001 (Tolman 1977, Chem. Rev.)
* **注記**: EP-06a の complete filling は 1990年代の DFT 計算論文群まで遅延（technical barrier）。Tolman 1977 は conceptual filling の開始点だが、quantitative filling（DFT の幾何学最適化）は別の論文が必須。

---

### EP-08a [Replication / uncertainty pack]

**充填するRI**: RI-08 (Unquantified reliability)

**充填開始点**: **未同定（第三群：充填見込み薄）**
— Table I の収率データの反復測定（n ≥ 3）と標準偏差報告は、計算化学・物理化学分野における出版インセンティブ構造の問題により、独立論文化されず。技術的には可能だが、追試報告は新規性を要求する出版慣行のもとで論文化されにくく、同一論文の Table 再計測という形式（フルペーパー内での内部充填）で留まる。

* **未充填の理由**: **インセンティブ構造的未充填** (v18 C6)
  — 統計的信頼性・再現性の検証（EP-08a）は、技術的には可能だが、独立した論文としての出版価値が低い（新規反応・新規基質ではなく、既報系の追試）ため、分野慣行としてグレー化する。この問題は有機転移金属化学全般で観察される構造的特徴。

* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: 該当なし（第三群）
* **Filling timescale category**: non-applicable (充填見込み薄のため timescale 割当て不可)
* **DB-findability**: no
* **注記**: EP-08a の未充填は、通信形式の限界だけでなく、出版インセンティブ構造そのものが「既報系の追試」を論文化から排除するパターンの典型例。Modern era における改革（open data, replication journals 等）以前は、この種の問題は体系的に解決されず。

---

## §C 推奨選定リスト

### 選定基準への照合
1. **EP充填のカバレッジ**: 複数 EP を充填する論文を優先
2. **充填の決定性**: Complete > Partial > Indirect
3. **VQ階層のカバレッジ**: VQ-2（報告完全性）、VQ-3（機構検証）、VQ-4（ベンチマーク）から各層をカバー
4. **年代の多様性**: 時間的展開を検証
5. **Bibliographic confidence**: High > Medium；Low は原則除外
6. **Filling adequacy confidence**: High > Medium

---

### 推奨選定表

| 順序 | 論文 | 充填 EP | VQ 水準 | 年代 | Bib. Conf | Fill. Conf | 検証 | Filling Timescale |
|------|------|---------|--------|------|-----------|-----------|------|-------------------|
| 1 | Kumada et al., フルペーパー (推定 1973-1974 JACS) | EP-01a, EP-07a, (EP-10a partial) | VQ-2/VQ-3 | 1973-74 | Medium | High | 必須 | format-driven (1-3yr) |
| 2 | Kumada / Tamao et al., NMR mechanistic study (推定 1973-1975) | EP-03a | VQ-3 | 1973-75 | Medium | Medium | 必須 | field-methodology (2-5yr) |
| 3 | Yamamoto et al., Ni(0)-diphosphine NMR study (推定 1974-1976) | EP-03a (independent confirmation) | VQ-3 | 1974-76 | Medium | Medium | 推奨 | field-methodology (2-5yr) |
| 4 | Early Kumada / Osaka group GC-MS selectivity analysis (推定 1975-1978) | EP-05a | VQ-2 | 1975-78 | Low | Low-Medium | 必須 | field-methodology (2-5yr) |
| 5 | Tolman 1977 Chem. Rev., Ligand parameter system | EP-06a (conceptual groundwork) | VQ-3 (partial) | 1977 | High | Medium | 推奨 | technical-barrier (10-20yr to complete via DFT) |
| 6 | 1990s DFT studies on Ni-diphosphine complexes & Grignard coupling | EP-06a (DFT completion), EP-10a (theoretical kinetics) | VQ-3/VQ-4 | 1990s | Medium | Medium | 推奨 | technical-barrier (10-20yr) |

---

### 選定理由

**Rank 1–2（最優先）**: 
Kumada グループのフルペーパー（推定 1973-1974）は、Communication から Full Article への format-driven auto-resolution として、EP-01a（reporting completeness）と EP-07a（boundary test: dpp scope）を直接充填する。さらに、同一著者グループの NMR 機構研究（推定 1973-1975）が EP-03a（intermediate observation）を充填する。この 2 論文で VQ-2（method validation）から VQ-3（mechanism evidence）への段階的カバレッジが達成される。**バンドル充填の効率性が最高**。

**Rank 3**:
Yamamoto グループの ³¹P NMR 研究は、Kumada グループの機構研究と独立した検証を提供し、EP-03a の「複数グループによる確立」パターンを示す。分野横断検証としての価値が高い。

**Rank 4**:
GC-MS 定量分析（推定 1975-1978）は、EP-05a（selectivity quantification）の field-methodology driven な充填を代表する。具体的な論文特定に verification が必須だが、選択性定量化の趨勢として組み込む価値あり。

**Rank 5–6**:
Tolman 1977 および 1990s DFT 研究は、EP-06a（ligand geometry validation）の **長期遅延充填（long-term delayed filling）** パターンを示す。Tolman parameter は conceptual groundwork（10年遅れで 1977 に確立），本格的な DFT 検証は technical barrier（計算能力）により 1990年代を待つ。VQ-4（benchmark）の達成は最も遅延。

---

## §D VQ階層と充填時間順序の対応分析

### 充填の時間軸

```
VQ-2要件 (Reporting Integrity):
  - EP-01a → 1973-1974 [Kumada et al. Full Paper] — format-driven auto-resolution
  - EP-07a → 1973-1974 [Kumada et al. Full Paper] — format-driven auto-resolution

VQ-3要件 (Mechanism):
  - EP-03a → 1973-1975 [Kumada/Tamao et al. NMR mechanistic study] — self-filling by original authors
  - EP-03a (independent) → 1974-1976 [Yamamoto et al. Ni(0)-diphosphine NMR] — field methodology
  - EP-10a (partial) → 1973-1975 [Kumada mechanistic study, implicit kinetics] — self-filling
  - EP-05a → 1975-1978 [Osaka/Tokyo group GC-MS selectivity] — field methodology
  - EP-06a (conceptual) → 1977 [Tolman ligand parameter system] — theoretical framework

VQ-4要件 (Benchmark):
  - EP-06a (complete, via DFT) → 1990s+ [DFT calculations on Ni complexes] — technical barrier (13-18 yr delay)
  - EP-10a (complete, kinetic theory matching) → 1990s [Comprehensive kinetic-computational coupling studies]
```

### 階層-時間対応の評価

**仮説の検証：**
「VQ階層が上がるほど、充填に要する時間が長くなる」という仮説は、**部分的に支持される**。

- **VQ-2充填**（報告完全性）: 1-3 年（format-driven，自動解消的） ✓ 最短
- **VQ-3充填**（機構証拠）: 1-5 年（分野方法論に依存，field-methodology driven） ✓ 中程
- **VQ-4充填**（ベンチマーク/理論統合）: 15-20 年+（技術的バリア依存，DFT計算能力） ✓ 最長

ただし、**EP-06a の部分充填（Tolman 1977）が 5 年という異例的な短期化**を示す。これは「理論的枠組みの確立」が実験的充填より先行するパターン（conceptual groundwork）の表れ。完全充填（DFT）は 18 年を要する。

**反例：** EP-10a (kinetics) が 1973-1975 の Kumada グループで部分的に追跡されるが、「速度定数の本格的な導出と速度式の確実な検証」は 1980年代以降の分野方法論の成熟を待つ。VQ-3 要件の「完全な」充填は不明瞭。

### 特筆すべきパターン

1. **自己充填（Self-filling）パターン**:
   原著者グループ（Kumada, Tamao, Sumitani）による Communication → Full Paper 遷移が、EP-01a, EP-07a, EP-03a(partial), EP-10a(partial) を一括充填する。**バンドル充填効率が最高。** これは communication 形式の制約が、後続フルペーパーにおける「必然的な完全化」を誘発する機構的パターンを示す。

2. **技術的バリア遅延充填（Technical-barrier delayed filling）**:
   EP-06a（ligand geometry validation via DFT）は、概念的な groundwork (Tolman 1977) が 5 年で提供されるが、計算能力の maturation (1990s) を待つ必要があり、15-20 年の遅延を示す。これは「科学が実行可能だが技術的に実現不可能な問い」の典型。UQS の発見的価値が高い。

3. **分野方法論駆動充填（Field-methodology driven filling）**:
   Yamamoto グループの NMR 研究、GC-MS 定量分析は、2-5 年のタイムスケールで field methodology の拡大に合致した充填パターンを示す。これらは「分野全体が新技術を採用する」ムーブメントに乗った充填。

4. **充填不在のパターン（Unfilling）**:
   EP-08a（replication/statistical robustness）は、50年以上経過した現在でも充填されず。これは技術的困難ではなく、出版インセンティブ構造の問題（追試の新規性不足）による **構造的な未充填** を示す。

### 著者回顧との照合（準備中）

著者回顧（Kumada ノーベル講演 1975-1990 期など、公開データの確認待機）と Stage 3 の EP リストの照合は、post-hoc verification として別途実施推奨。現在は bibliographic verification に優先度を置く。

---

## §E 未充填 EP の発見的意義

### 未充填 EP 一覧

**EP-08a** [Replication / Uncertainty Pack]:
* **未充填の理由**: インセンティブ構造的未充填（v18 C6）。Table I の収率の反復測定（n=3, SD）は技術的には可能だが、既報系の追試としての新規性が低く、独立論文化されず。出版慣行上、「既報反応の統計的評価」は単独論文としてではなく、より大規模な方法論論文や handbook 章に埋め込まれる傾向。分野全体での慣行的回避。

* **発見的意義**: **あり**。通信形式の「完全な追試データ不在」が、現代でも一般的に未充填のままであることは、科学出版インセンティブが「新規性」「オリジナリティ」を排他的に重視する構造を明示する。UQS が抽出した「統計的堅牢性」の不在は、単なる 1972 年の技術的限界ではなく、**分野の構造的選別性の反映** として記録される価値がある。

* **将来の充填可能性**: **中-高**。Open Science、Replication Studies journal、preregistration 等の現代的ムーブメントにより、充填インセンティブが再構成中。ただし 50 年遅延充填の可能性は極めて低い（原データ散逸のリスク増大）。Kumada グループの原始データ（lab notebooks）の archival 検索が最終的な充填候補。

**その他の EP（EP-01a, 03a, 05a, 06a, 07a, 10a）**: 
全てが充填論文候補として同定された。第三群の未充填 EP は EP-08a のみ。

---

## 最後に: Hallucination 警告と Verification 優先度

### Hallucination Risk Assessment

以下の候補は、Bibliographic confidence が Medium-Low であり、post-hoc Crossref 検証が必須：

1. **Kumada フルペーパー（推定 1973-1974）**：JACS フルペーパーの発表年・巻号号の推測。著者リスト「Tamao, Sumitani, Kumada」の完全性未確認。→ **検証必須**

2. **GC-MS 定量分析（推定 1975-1978）**：具体的論文の特定が低信頼。日本国内グループの多数の類似論文が存在し、正確な filtering が困難。→ **検証必須**

3. **Yamamoto 1974-1976 NMR 論文**：年代範囲が広く、具体的論文特定に推測多し。→ **検証推奨**

### Post-hoc Verification の推奨手順

1. JACS の 1972-1975 「Kumada」「Tamao」「nickel」「cross-coupling」で全文献検索
2. 各候補の DOI 取得（Crossref / PubMed）
3. 著者リスト完全性確認（スペル、順序）
4. タイトルから内容推定し、EP 対応関係を再評価
5. Hallucination 検出時は候補から除外、再検索

---

## 最終附録: 検討棄却候補

### 棄却した候補と理由

1. **Palladium-catalyzed coupling literature (Heck, Suzuki）**:
   — 理由：EP の case-specific 実装が「Ni-diphosphine」系に限定されるため、Pd 系の基質スコープは直接的な filling として機能しない。分野横断 insight は提供するが、原論文の EP 充填という観点では優先度外。

2. **Early theoretical papers on transition metal π-complexes（Dewar 1956 等）**:
   — 理由：理論的背景は提供するが、EP-03a（Ni 中間体の分光特性化）や EP-10a（kinetic validation）の case-specific 実装を直接充填しない。conceptual ancestor だが、充填論文ではない。

3. **日本国内の催化化学レビュー（1980-1990）**:
   — 理由：ルール「レビュー論文は EP を充填しない；レビューは充填論文を特定するための二次情報源として使用」に従い、レビュー単体は選定リスト対象外。ただし、レビューに含まれるメタ分析や独自定量評価が EP に直接対応する場合は例外。当該レビュー群の詳細確認待機。

4. **Structure-activity relationship papers on similar Ni catalysts（但し異なる配体系）**:
   — 理由：[NiCl₂(dppe)], [NiCl₂(dppp)] 等の別の配体系研究は、EP-07a（[NiCl₂(dpp)] specific scope）の直接的な填补ではなく、「類似系の応用」として位置づけられる。EP の「境界検証」に類するが、原論文の陳述スコープ（dpp の superiority）の直接的な検証ではない。関連論文だが優先度外。

---

## 結論（Concluding remarks）

Stage 4 v6 retrieval depth annotation 実行結果：

**総合評価：** Kumada 1972 のランドマーク通信は、Communication 形式の構造的欠落（EP-01a, EP-07a など report 完全性）を、著者グループの後続フルペーパーによる **format-driven auto-resolution** により、短期間（1-3 年）で充填する。一方、機構検証（EP-03a, EP-10a）は 2-5 年の遅延を要し、リガンド効果の理論的検証（EP-06a）は 15-20 年の技術的バリアを要する。特に **EP-08a（統計的堅牢性）は 50 年以上未充填**のままであり、これは通信形式の限界を超えた出版インセンティブ構造の反映として UQS の発見的価値が認められる。

**Retrieval Tier Summary:**
- **Tier I（直接想起）**: EP-01a, EP-07a, EP-03a（自己充填パターン）
- **Tier II（2-3段階連想）**: EP-10a, EP-05a, Yamamoto 候補、GC-MS 候補
- **Tier III（複数候補 triangulation）**: EP-06a（Tolman framework），1990s DFT
- **Unfilled（検索不可）**: EP-08a（インセンティブ構造的未充填）

**Confidence Distribution:**
- High: 2 候補（Kumada フルペーパー, Tolman 1977）
- Medium: 4 候補（NMR mechanistic, Yamamoto, GC-MS selectivity, DFT）
- Low: 1 候補（GC-MS specific paper）

**Bibliographic Verification Status:** **全 pending**（post-hoc Crossref 検証待機）

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
