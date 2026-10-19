prompt_version: stage3-v4-20260427
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, Articles）

---

### §1 Claim Architecture

**コア主張の要約：**

Novelty 柱：RuH₂(CO)(P(C₆H₅)₃)₃ が触媒として芳香族ケトンの ortho C–H 結合とオレフィンの C–C 結合形成を実現した。成功の鍵はキレーション補助（低原子価 Ru が芳香族カルボニル基に配位し、隣接 ortho C–H 結合の切断を誘導する）にある。

Utility 柱：この反応は効率（両出発物質基準でほぼ定量的収率）・選択性（「virtually 100%」位置選択性）・汎用性（アシルベンゼン系＋アシルヘテロ芳香族、複数のモノ/ジ置換ターミナルオレフィン）の三つを同時に達成し、「practical organic synthesis に要求される水準」に達すると主張している。

**Layered structure 判定：**

論文の主張は独立した三層から構成される。

- **Layer 1（効率）**：NC-1（定量的収率の先例なき達成）——GC 収率データ（Table 1）に基礎を置く。
- **Layer 2（選択性）**：NC-2（virtually 100% regioselectivity）——同じ Table 1 データに基礎を置くが、効率層とは独立に評価可能。
- **Layer 3（汎用性）**：NC-3（アシルベンゼン + ヘテロ芳香族 × 複数オレフィン）——実験 13 run の基質多様性による主張。

さらに NC-4（「キレーション補助コンセプトはより広範に適用できる」）は実験データから独立した展望として付加されており、NC-1〜NC-3 が反論されても取り下げ不要な構造になっている。

**単一の反証で全崩れするか：** しない。Layer 1（GC 収率の信頼性）が問われても、Layer 2（選択性主張）および Layer 3（基質多様性）は独立して成立しうる。ただし、**全三層は共通して「キレーション補助が機構的に成立すること」を暗黙の前提とする。** この前提が否定されると、効率・選択性・汎用性がいずれも chelation assistance によって説明される主張の機構的基盤が崩れる。すなわち、機構的基盤（SRG-2: 中間体未検出問題）は三層にまたがる共通の脆弱点である。

**Layer asymmetry annotation：**

本論文は有機金属触媒合成という**単一 paradigm**で構成されている。Stage 2 v19 D-4 の C22 trigger 判定（"single-paradigm: not applicable"）と整合する。構造解析 Layer と機能 Layer の非対称性は本論文では発火しない。

**結論：single-paradigm: no Layer asymmetry detected。**

すべての主張は触媒反応の観測量（収率・選択性・基質多様性）という単一の実験パラダイムに属する。ただし、機構的基盤（SRG-2）という横断的な共通前提の未検証が三層全体を構造的に脆弱にしている点は注記する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [GC収率定量的根拠の三重不在]**

* **Primary RI**: RI-01 [Reporting integrity] — GC 収率の内部標準・応答因子 calibration が未記載であり、13 run 中 10 run で単離収率が与えられず、run 1 で 17% が未帰属のまま mass balance が閉じていない。定量的主張の横比較可能性が根本的に欠如している。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 「almost quantitative yields」（NC-1）の主張が GC 収率という単一の測定値のみに依拠し、反復測定・不確かさ記述が存在しない。
* **ER**: GC 収率は内部標準または個別応答因子による calibration を実施し、その方法を明記すること。全 13 run について単離収率または GC/単離収率の対応関係を提示し、run 1 の 17% 未帰属成分を明示すること。
* **EP**: EP-01a [Reporting-coherence pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: Ru 触媒 C–H 官能基化において — (a) 全ランに対して同一の GC 内部標準（例：デカン、ドデカン）または外部標準と calibration 曲線を設定して収率を再測定、(b) 10 run について bulb-to-bulb distillation 後の単離収率を記録、(c) run 1 のクロマトグラム全ピークを帰属（1:1 coupling 75% + 1:2 coupling 8% + 残 17% の正体を明示）、(d) 「100%」報告のある run（4、8、9、10、12）について GC ピーク面積対内部標準の絶対収率値を記述。
* **注記**: D-4-5 (grounded_in: B-1, U-3)、SRG-1 [B-1, U-3]。TEMPERATURE_SUMMARY: high_convergence_low_gap（convergence=2/3、V1+V3 一致、temperature_gap=none）。

---

**SRG-2 [触媒サイクル中間体の未検出・触媒的有能性未確認]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 論文が Fig. 1 で提案した cyclometallated Ru 中間体（ortho-metalated ルテナサイクル）は触媒反応条件下で直接観測・単離・独立合成されておらず、この中間体が on-cycle 種であることは実証されていない。
* **Secondary RI**: RI-06 [Imported model] — 中間体の証拠として Mn 系（ref 14、Knobler et al. 1975）および異なる Ru 前触媒系（ref 15、McGuiggan & Pignolet 1982）の化学量論的シクロメタル化反応を引用しているが、それらの中間体が現行触媒条件（RuH₂(CO)(PPh₃)₃、toluene reflux、2 mol% Ru）で同型に成立することは検証されていない。
* **ER**: 提案された cyclometallated Ru 中間体を以下のいずれかにより実証すること：(1) 化学量論量以下のオレフィン条件での in situ 中間体トラップ、(2) 中間体独立合成と触媒的有能性確認、または (3) 低温 ³¹P NMR / ¹H NMR による直接観測。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-10a [Kinetic verification pack]
* **Case-specific実装**: (a) ortho-deuterated acetophenone（[d₁]-acetophenone, ortho 位 D 標識）を用いた KIE 測定——C–H 酸化的付加が律速か否かの判定；(b) trapping 実験：RuH₂(CO)(PPh₃)₃ と acetophenone を olefin 非存在下 toluene reflux し、³¹P NMR / ¹H NMR で cyclometallated Ru species を検出；(c) 独立に合成した Ru(ortho-metalated acetophenone) 錯体に olefin を加えて catalytic competence を確認（化学量論的反応でよい）；(d) EP-10a: initial-rate kinetics を run 1 条件下（acetophenone + vinyl-Si(OEt)₃、[ketone] および [olefin] を独立変化）で実施し、反応次数から律速ステップを拘束。
* **注記**: D-4-1 (grounded_in: U-1, A-1, C4, C5)、SRG-2 [A-1, U-1, C4, C5]。TEMPERATURE_SUMMARY: high_convergence_low_gap（convergence=3/3、V1+V2+V3 一致、temperature_gap=none）— 最高収束、最高優先度。recurring_root: 「触媒サイクル中間体の直接証拠欠如」は EP-10a の7独立観察源（Breitenfeld 2014、Mazet 2021、Pengfei 2024、Kumada 1972 × 3 モデル、Murai 1993）のうち GPT-5.5 on Murai 1993 が既に確認済み（EP-10a 正式登録根拠の一部）。cross-case confirmed。

---

**SRG-3 [位置選択性の定量的根拠と機構的起源の双重不在]**

* **Primary RI**: RI-04 [Unreplicated discriminator] — 「virtually 100% regioselectivity」という主張が GC による端点収率分布のみに基礎を置き、minor regioisomers の検出下限が未記載であり、選択性が kinetic 制御か thermodynamic 制御かを判定するデータが存在しない。
* **Secondary RI**: RI-05 [Qualitative overread] — GC で検出されなかった（≒ 検出下限以下）という操作的観察から、「提案サイクルの特定ステップで選択性が決定される」という構造的・機構的含意への飛躍がある。
* **ER**: 位置選択性の定量的下限を以下の方法で確立すること：(1) 代替 regioisomers の GC/HPLC 検出下限を明示、(2) runs 8 および 13（aromatic regioselectivity）について NOE または X 線構造解析による regiochemical assignment の独立確認、(3) 変換率 10–30% での早期時点サンプリングによる kinetic vs thermodynamic 制御の検定。
* **EP**: EP-04a [Discrimination / replication pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: (a) ¹H NMR NOESY により ortho-アルキル化生成物の regiochemistry を確認（特に run 8: 1-naphthyl 系と run 13: thienyl 系）；(b) 代替 Markovnikov 付加体（branch-selective）の GC 保持時間を合成標準品または文献値と対照し、1% 未満での検出下限を明示；(c) acetophenone + vinyl-Si(OEt)₃ を run 1 条件で conversion 10%、30%、50%、100% で sampling し、1:1 / 1:2 比率の時間依存性を確認。
* **注記**: D-4-2 (grounded_in: U-2, B-2)、SRG-3 [B-2, U-2]。TEMPERATURE_SUMMARY: high_convergence_low_gap（convergence=3/3、temperature_gap=low）。RI-05 が残存するため現状では VQ-3 は qualified。

---

**SRG-4 [リング歪み論拠の定量的速度データ欠如]**

* **Primary RI**: RI-04 [Unreplicated discriminator] — run 10（1-acetonaphthone、0.5 h、100%）と run 11（tetralone、20 h、88%）の速度差、および 1-indanone の非反応は chelation assistance の最も具体的な内部動力学的プローブであるが、これら3点の定量的 TOF 比・活性化エネルギー差・side-by-side 実験が一切報告されず、1-indanone 実験条件も未記載である。
* **Secondary RI**: RI-05 [Qualitative overread] — 「slower」（run 11 vs run 10）および「did not react at all」（1-indanone）という定性的比較から「angle strain controls reactivity via chelation-assisted cyclometallation」という構造的・機構的含意を導出している。
* **ER**: run 10、run 11、1-indanone の比較を以下の条件で定量化すること：同一触媒量・基質量・オレフィン量・温度で side-by-side 実験を実施し、初期速度（TOF initial）を比較する。1-indanone については実験条件（触媒量、時間、オレフィン）を明記すること。
* **EP**: EP-04a [Discrimination / replication pack]; EP-10a [Kinetic verification pack]（リング歪み vs 電子効果を区別するための速度論的拘束）
* **Case-specific実装**: (a) run 9 条件（isopropyl vinyl ketone + vinyl-Si(OEt)₃）で run 10 / run 11 / 1-indanone を同一バッチで並行実験し、GC による時間分解収率測定；(b) Ea を Arrhenius plot（100–135°C 範囲で 4 点以上）で決定し、six-membered vs seven-membered vs five-membered cyclometallated ring の ring-strain 文献値と比較；(c) 環サイズの影響と電子効果を分離するために、同一リングサイズで電子的性質のみ異なる基質対（例：6-methoxy-tetralone vs 6-nitro-tetralone）を導入。
* **注記**: D-4-6 (grounded_in: B-3)、SRG-4 [B-3]。TEMPERATURE_SUMMARY: high_convergence_low_gap（convergence=3/3、temperature_gap=none）。

---

**SRG-5 [活性触媒種の同一性未確認]**

* **Primary RI**: RI-02 [Object identification] — 5 種の Ru 前触媒の定性的活性ランキング（equally effective / modestly effective / not effective）が提示されているが、数値的活性データ（収率、TON、時間）も比較した基質/オレフィン組み合わせも明示されていない。活性種の構造（低原子価 Ru(0) が in situ 生成されるのか、各前触媒固有の活性種があるのか）は未確認である。
* **Secondary RI**: RI-03 [Unobserved explanatory] — 提案サイクルでは Ru(0) が共通の活性種として暗黙的に想定されているが、前触媒から Ru(0) への変換（還元的脱配位）は観測されていない。
* **ER**: 少なくとも最効触媒（RuH₂(CO)(PPh₃)₃）と「equally effective」な前触媒（Ru(CO)₂(PPh₃)₂）について同一基質・条件下での定量的収率/TON 比較を提示し、活性種の ³¹P NMR / ¹H NMR による特徴付けを試みること。
* **EP**: EP-02a [Identity / purity substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: (a) run 9 条件（最良条件）で RuH₂(CO)(PPh₃)₃ / Ru(CO)₂(PPh₃)₂ / RuH₂(PPh₃)₄ について GC 収率を時間分解（0.25 h 間隔）で測定し TOF_initial を比較；(b) 各前触媒を toluene 中 135°C で加熱し、sub-stoichiometric ketone 添加後の ³¹P NMR で共通 Ru 種が生成するか確認；(c) Ru(CO)₂(PPh₃)₂ の活性確認が同じ chelation-assisted 機構によるものかを、KIE または regioselectivity の比較で評価。
* **注記**: D-4-7 (grounded_in: B-4, A-1)、SRG-5 [B-4, A-1]。TEMPERATURE_SUMMARY: high_convergence_low_gap（convergence=2/3、V1+V2 一致、temperature_gap=low）。

---

**SRG-6 [TOFベンチマーク：数値不在と比較基準未同定]**

* **Primary RI**: RI-09 [External superiority] — 「[REDACTED: verbatim source text; see the source paper via its DOI]」という比較優位性主張が、Table 1 から原理的に計算可能な数値 TOF を提示せず、比較対象の先行文献値（refs 11、12、16 の TOF）も明示していない。
* **Secondary RI**: RI-01 [Reporting integrity] — TOF の計算基準（initial rate vs final yield at endpoint / どの時点の yield か）が未記述であり、runs 9 と 10 については 0.5 h 時点の endpoint yield 100% のみが報告されているため、TOF の上限しか計算できない（より高い TOF が実際には存在する可能性を排除できない）。
* **ER**: runs 1、9、10 について TOF 値を数値として明記し（計算式：mmol product / mmol Ru / h、初期速度または endpoint yield 時の明示）、refs 11（Jordan & Taylor 1989）および 12（Moore et al. 1992）の公表 TOF/TON 値と数値で比較すること。
* **EP**: EP-09a [Internal benchmark pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: (a) Table 1 の既存データから runs 1（75% × 2 mmol / 0.04 mmol / 0.2 h ≈ 188 h⁻¹）、9（100% × 2 mmol / 0.04 mmol / 0.5 h = 100 h⁻¹）、10（100% × 2 mmol / 0.04 mmol / 0.5 h = 100 h⁻¹）の endpoint-based TOF を計算して明記；(b) Jordan & Taylor 1989 と Moore et al. 1992 の公表 TOF/TON 値を抽出し、同一スケールで比較表を作成；(c) runs 9/10 について 0.1 h、0.3 h、0.5 h の time-course を追加し、initial-rate TOF を決定。
* **注記**: D-4-3 (grounded_in: U-3, A-3, C2, C8)、SRG-6 [A-3, U-3]。TEMPERATURE_SUMMARY: high_convergence_low_gap（convergence=2/3、V1+V3 一致、temperature_gap=low）。

---

**SRG-7 [キレーション補助の射程と合成標的との接続]**

* **Primary RI**: RI-07 [Unsupported boundary] — 「[REDACTED: verbatim source text; see the source paper via its DOI]」という境界拡張主張が、全 13 run で C=O 基を配位基とする芳香族ケトンのみを基質とし、非カルボニル配位基（アミド、エステル、イミン、オキサゾリン等）の例がゼロの状態でなされている。さらに「a new range of alkylated aromatic compounds」という合成的価値主張に対して、得られた生成物のいずれかが具体的合成標的（天然物・医薬品中間体）の前駆体であることが示されていない。
* **Secondary RI**: RI-05 [Qualitative overread] — 「[REDACTED: verbatim source text; see the source paper via its DOI]」という汎用性記述が、全オレフィンが Si 置換または分岐アルキル末端であるという暗黙の制限を含みながら、純炭化水素ターミナルオレフィンを対象外としている事実を言及しない。
* **ER**: 「applicable more widely」という主張を実験的に検証するために、少なくとも1例の非カルボニル配位基（例：N,N-dimethylamide, imine, oxazoline）を用いた Ru 触媒 C–H 官能基化を試み、その結果（成功または失敗）を報告すること。さらに純炭化水素ターミナルオレフィン（例：1-hexene、1-octene）との反応性を run 1 条件と対照比較すること。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: (a) N,N-dimethylbenzamide（アミド配位基）と vinyl-Si(OEt)₃ を run 9 条件で実施し、Ru 触媒 C–H/olefin coupling が発現するか確認；(b) 1-hexene または 1-octene（純炭化水素ターミナルオレフィン）を acetophenone に対して run 1 条件で試験し、Si 置換オレフィンとの活性比較；(c) 標的合成：トリエトキシシリルアルキル化芳香族ケトン（例：run 12 生成物）の Si を酸化してアルコールとし、既知天然物または医薬品への変換ルートを例示。
* **注記**: D-4-4 (grounded_in: A-2, B-5) および D-4-10 (grounded_in: A-2, B-5)、SRG-7 [A-2, B-5]。TEMPERATURE_SUMMARY: high_convergence_high_gap（convergence=2/3、V1=low、V2=high、gap=medium）— 唯一の high_gap 項目。

---

**SRG-8 [生成物キャラクタリゼーションの特定不在]**

* **Primary RI**: RI-01 [Reporting integrity] — 「[REDACTED: verbatim source text; see the source paper via its DOI]」が、いずれの spectroscopic 技術（¹H NMR、¹³C NMR、IR、MS、X 線）を使用したかを特定していない。特に regiochemical assignment（runs 8、13：位置選択性の主張証拠として機能）に必要な技術（NOE、X 線）が明示されていない。
* **Secondary RI**: RI-08 [Unquantified reliability] — 「analytically pure sample」という記述に対して純度基準（例：GC 純度 ≥95%）が付記されていない。
* **ER**: 少なくとも代表的な生成物（runs 1、8、9、13 の各 1 例）について ¹H / ¹³C NMR データを報告し、regiochemical assignment に用いた根拠（NOE 相関または X 線）を明示すること。純度基準を GC ピーク面積比または元素分析で定量的に記述すること。
* **EP**: EP-02a [Identity / purity substantiation pack]
* **Case-specific実装**: (a) ¹H NMR スペクトルの ortho-アルキル化生成物シグナルが aromatic region に特徴的なパターンを示すことを NOE 差スペクトルで確認（特に run 13：チエニル系の regiochemistry）；(b) run 8（1-naphthyl 系）は X 線構造解析で regiochemistry を決定；(c) 全生成物について Kugelrohr 蒸留後の GC 純度 ≥95% を記録。
* **注記**: D-4-5（部分）と B-1 から派生。SRG-8 [B-1, B-6]。TEMPERATURE_SUMMARY: high_convergence_low_gap（convergence=2/3、V1+V3 一致、temperature_gap=none）。

---

**SRG外：CLA**

**CLA-1: 触媒サイクルの自己矛盾的予測未検証（U-1 由来）**

* **Primary RI**: RI-03 [Unobserved explanatory]（RI-06 との共起）
* **Secondary RI**: RI-06 [Imported model] — 提案された Fig. 1 触媒サイクル（chelation-assisted oxidative addition → olefin insertion → reductive elimination）は自身で複数の実験可能な予測を生成している：(1) ortho C–D 基質の KIE、(2) 化学量論量以下のオレフィンでの中間体トラップ、(3) H 転移の化学量論バランス。いずれも未検証のまま「not yet clear」で閉じられている。これは既存 SRG-2 と重複するが、**自己矛盾的不在の独立性**（v18.1 規則）により CLA として独立記録する（SRG-2 は「中間体の直接検出」に焦点、CLA-1 は「提案サイクルが予測する量の未検証」に焦点）。
* **ER**: 触媒サイクルの自己整合性を検証するために、サイクルが予測する観測量（KIE、中間体、H バランス）の少なくとも1つを実験的に確認すること。
* **EP**: EP-10a [Kinetic verification pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: ortho-C–D-acetophenone vs 無標識 acetophenone の parallel run（run 9 条件）で KIE（kH/kD）を GC 収率比から推定；ideal kH/kD > 2 なら C–H 活性化律速と整合する。
* **注記**: U-1 (self-contradictory absence, critical) から派生。SRG-2 [A-1, U-1, C4, C5] との部分連結。

**CLA-2: 「未活性化 C–H 結合」フレームとキレーション補助の内的矛盾（B-8 + D-4-8 由来）**

* **Primary RI**: RI-05 [Qualitative overread] — 論文は「catalytic functionalization of unactivated C–H bonds」という優先性フレームを用いながら、機構の核心は「キレーション補助（C=O 基による金属誘導）によって活性化された C–H 結合」の切断であり、「unactivated」の定義が操作的に未定義のまま使用されている。
* **Secondary RI**: RI-07 [Unsupported boundary] — 「never been attained before」という境界主張が、先行 30 年の文献（refs 1–10）との数値比較なしになされている。
* **ER**: 「unactivated C–H bonds」の操作的定義を明示すること（例：外部酸化剤・事前官能基化なしに切断される C–H 結合を指す）。先行 refs 11、12、16 の yield/TON を数値で比較して「never been attained before」の定量的根拠を示すこと。
* **EP**: EP-01a [Reporting-coherence pack]; EP-09a [Internal benchmark pack]
* **Case-specific実装**: 先行 2 例（Jordan & Taylor 1989: α-picoline + propene / Moore et al. 1992: pyridine + CO + 1-hexene）の TON・収率値を文献から抽出し、本論文の best run（run 9 または 10）の同指標と side-by-side で記述。
* **注記**: D-4-8 (grounded_in: B-8, A-1)。low_convergence_high_gap（convergence=1/3）だが内的矛盾の性質が重要。SRG-2 との間接連結（A-1）。

**Self-referential validation チェック（v18 規則）：**

論文は新規計算量・指標・スコア関数を提案しておらず、クラスター A（Self-referential validation）の定義条件——(a) 検証指標と被検証対象が同一の数学的構成物に依存、(b) 検証成功基準が提案理論の前提と循環、(c) 外部基準の欠如、(d) 多層近似の累積——のいずれにも直接該当しない。

**Deductive-retrospective structure チェック（v18 規則）：**

本論文は実験論文（新規触媒反応の実証）であり、演繹的導出による原理・選択則・形式的予測の提案論文ではない。クラスター B の条件 (a)〜(d) は本論文では発火しない。

**PRI-12 適用判定：** PRI-12 クラスター A・B ともに本論文には非適用。

---

### §3 現在のVQ判定

**Step 3a: Modern reassessment baseline（2025年基準）**

**VQ-1 (Observation) — RI-02 の評価：**

生成物の構造は「standard methods」で「unequivocally」確立されたと述べられているが、具体的な spectroscopic 方法が未記載である（SRG-8、CLA-2 関連）。ただし 13 run の生成物の存在と化学的実体（ortho-アルキル化芳香族ケトン）は Table 1 のデータから同定可能であり、RI-02 違反は観察記述を根本から否定するほどの致命性はない（GC 収率 + 単離品の記述は存在する）。

**RI-02: Non-fatal（構造確認の詳細が未記載だが生成物の実体は観察されている）**

→ **VQ-1 (Observation): achieved**

**VQ-2 (Method) — RI-01 および RI-07 の評価：**

- **RI-01**: GC calibration 未記載、単離収率 10/13 run 欠如、mass balance 未閉鎖（run 1: 17% 未帰属）。定量的収率報告の方法的完全性が欠如している。**Fatal（現代基準では許容不可）**。
- **RI-07**: 「applicable more widely」という境界拡張主張が非カルボニル基質で未検証のまま（SRG-7）。また「not effective」（RuHCl(CO)(PPh₃)₃、Ru₃(CO)₁₂）という境界が実験条件なしに主張されている。**Non-fatal（境界主張は将来の系統的研究への invitation として許容できる側面がある）**。

RI-01 が Fatal 残存のため：

→ **VQ-2 (Method): not reached（Modern reassessment baseline）**

VQ-2 の RI-01 (Fatal) が未解消。VQ-1 達成を前提とした段階的評価ではあるが、定量的収率報告の方法的欠如が致命的である。

**Step 3b: Era-norm annotation での補正**

1993 年 Nature Articles（3 ページ）の format 制約については §4 で詳述する。

- **RI-01（GC calibration 欠如）**: Nature 3 ページ制約下では補助データ記載が困難であり、GC 定量法の詳細省略は当時の高インパクトジャーナル通信・論文の慣行内に収まる。→ **communication-era tolerated**。
- **RI-07（境界未検証）**: 探索的な一報目の論文として、全配位基変種の系統的検討を要求しないことは当時の Field convention 内。→ **communication-era tolerated**（ただし "more widely" という言語は現代基準では overstatement と評価される）。

Era-norm 補正後：VQ-2 の RI-01 が communication-era tolerated に分類される。

→ **VQ-2 (Method): VQ-2 (era-norm qualified)**

*注記：VQ-2 は VQ-1 達成を前提に成立している。*

**VQ-3 (Mechanism) — RI-03, RI-04, RI-06 の評価（VQ-2 継承）：**

- **RI-03**: cyclometallated Ru 中間体が catalytic 条件下で未観測。**Fatal（機構的主張の核心）**。
- **RI-04**: ring-size 系列（run 10/11/1-indanone）による chelation 証拠が定量的速度データ不在のまま機構論拠として使用されている（SRG-4）。また regioselectivity（SRG-3）の定量的検出下限が不明確。**Fatal（機構論拠として機能する唯一の内部動力学プローブが定性的）**。
- **RI-06**: Fig. 1 の触媒サイクルが Mn 系・異種 Ru 複合体の化学量論的シクロメタル化反応から類推されており、現行触媒条件での同型性が未実証。**Fatal（触媒サイクルのモデル輸入）**。
- **RI-05**: regioselectivity 主張が操作的（GC 端点）と機構的（どのステップが selectivity-determining か）を区別しないまま使用されており、**VQ-3 を limited/qualified 化する根拠**となる（*注1 適用）。

RI-03、RI-04、RI-06 いずれも Fatal 残存。RI-05 も残存。

→ **VQ-3 (Mechanism): not reached**（era-norm 補正後も、中間体未検出および動力学データ不在は 1993 年 Nature の形式上の慣行で説明できないため、VQ-3 は era-norm qualified にも分類されない）

**VQ-4 (Benchmark) — RI-08, RI-09 の評価（到達不可）：**

VQ-3 未達のため到達不可。

- **RI-09**: TOF が「among the highest reported」と主張されているが数値比較なし（SRG-6）。**Fatal**。
- **RI-08**: 収率の反復測定・不確かさ記述が全 run で欠如。**Fatal**。

→ **VQ-4 (Benchmark): not reached**

**Step 3c: Final VQ judgment**

```
現在判定: VQ-2 (era-norm qualified) / Method
- VQ-1 (Observation): achieved
- VQ-2 (Method): VQ-2 (era-norm qualified)
  RI-01 は modern 基準では Fatal だが 1993年 Nature 3-page format で communication-era tolerated
  RI-07 は Non-fatal かつ communication-era tolerated
- VQ-3 (Mechanism): not reached
  RI-03 (Fatal): 中間体未検出
  RI-04 (Fatal): 速度論的プローブが定性的
  RI-06 (Fatal): モデル輸入（類推のみ）
  RI-05 残存 → qualified 化要因
- VQ-4 (Benchmark): not reached
  VQ-3 前提未達成 + RI-08/RI-09 Fatal 残存
```

**Layer 別 VQ 非対称性：**

単一 paradigm 論文のため Layer 非対称性の正式適用は行わない（§1 Layer asymmetry annotation: single-paradigm 確定）。ただし非公式の観察として：NC-2（regioselectivity: virtually 100%）は観察記述としては Table 1 データで VQ-1 は確実に達成しているが、機構的帰属（どのステップが selectivity-determining か）は VQ-3 未達の一因となっている。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1（GC calibration 未記載、単離収率 10/13 run 欠如）**: 1993 年の Nature Articles（3 ページ）では補助データの詳細記載は構造上困難であり、主要収率データのみを Table 形式で提示する慣行は当時の高インパクトジャーナルにおいて許容されていた。GC 定量の response factor 省略は同時代の有機金属触媒論文でも一般的であった。
- **B-6（反応雰囲気・キャラクタリゼーションスペクトル未記載）**: Nature 3 ページ制限下で実験条件詳細の省略は通常慣行；追加データは著者宛て問い合わせで取得することが当時のノームであった。
- **B-3（1-indanone の実験条件未記載）**: 陰性結果の詳細条件を全て記載する義務は 1993 年の Nature Articles では確立されていなかった；脚注または methods 節への簡略記述で許容された。
- **B-5（olefin scope の implicit 制限）**: 方法論論文の初発報で全olefin クラスを網羅する系統的スクリーニングを要求しないことは当時の field convention 内であり、探索的範囲として「a variety of」という表現が許容された。
- **C-1〜C-8（文献の定性的引用、数値比較なし）**: 1993 年の短報・Articles 形式では benchmark comparison table の要求は確立されておらず、先行文献の定性的評価（"exceptionally high yields" / "limited to pyridine derivatives"）は当時の通常スタイルの範囲内。

**modern-era deficient:**

- **B-1（GC calibration 欠如・mass balance 未閉鎖）**: 現代の合成有機化学論文では、新規触媒反応の初発報においても GC 収率の response factor calibration または isolated yield の全 run 提示が標準要件となっており、「100%」収率の信頼性は現代基準では独立確認なしに受け入れられない。
- **A-1 / SRG-2（中間体未検出・KIE なし）**: 現代の触媒 C–H 活性化論文では、機構提案に対して少なくとも KIE（kH/kD）または KINETIC isotope effect の言及が標準要件であり、intermediate の直接証拠なしに完全な触媒サイクルを提案することは現代では不十分とされる。
- **SRG-3 / B-2（regioselectivity の検出下限未記載）**: 現代では「virtually 100%」という claim に対して、GC/HPLC 検出下限（≤1%）の明示が求められる。
- **SRG-6 / U-3（TOF 数値不記載）**: 現代では数値として計算可能な量を「among the highest」と記述するだけで数値を省略することは、再現性・比較可能性の観点から許容されない。

---

### §5 最短補強ルート

**目的関数 1: VQ-3 (Mechanism) への到達**

現在: VQ-2 (era-norm qualified)
VQ-3 未達の主因: RI-03 (Fatal: 中間体未観測)、RI-04 (Fatal: 速度論プローブ定性的)、RI-06 (Fatal: モデル輸入)、RI-05 残存

**VQ-3 への最短ルート：**

1. **EP-10a [Kinetic verification pack]** — ortho-C–D-acetophenone を用いた KIE 測定（kH/kD）と初期速度測定（[ketone]・[olefin]・[Ru] を独立変化させた速度次数決定）を実施する。RI-03（律速ステップの間接拘束）・RI-04（速度論的プローブの定量化）・RI-06（モデル輸入の代替：現行系での速度論証拠）を同時に前進させる最高情報利得 EP。

2. **EP-03a [Direct-observation / state-assignment pack]** — RuH₂(CO)(PPh₃)₃ + aromatic ketone を olefin 非存在下で toluene reflux し、³¹P NMR / ¹H NMR による cyclometallated intermediate の直接観測を試みる；または独立合成した Ru(ortho-metalated ketone) の触媒的有能性確認。RI-03 を直接前進させる。

3. **EP-04a [Discrimination / replication pack]** — runs 10、11、1-indanone を同一バッチで side-by-side 実験し初期速度 TOF ratio を定量化；run 9/10 の time-course により regioselectivity の endpoint vs early-time 分布を確認。RI-04 を前進させ、RI-05 を低減する。

認定ゲート順注記：実験投入順は情報利得順（EP-10a → EP-03a → EP-04a）だが、最終的な VQ-3 認定は継承原則に従い VQ-1 → VQ-2 → VQ-3 のゲート順で確定する（VQ-2 での RI-01 完全解消が VQ-3 認定の前提となる）。

---

**目的関数 2: VQ-4 (Benchmark) への到達**（VQ-3 達成が前提）

**VQ-4 への最短ルート：**

1. **EP-09a [Internal benchmark pack]** — runs 1、9、10 の数値 TOF を明記し、refs 11（Jordan & Taylor）・12（Moore et al.）・16（Hong & Yamazaki）の公表 TON/TOF と数値比較表を作成する。RI-09 を前進させる。

2. **EP-08a [Replication / uncertainty pack]** — 代表的な run（例：run 9）について 3 回以上の独立反復実験を実施し、収率の標準偏差を報告する。RI-08 を前進させる。

3. **EP-01a [Reporting-coherence pack]** — 全 13 run の GC 収率を response-factor calibrated 値に置き換え、10 run について単離収率を追加記録する。RI-01 を完全解消する（VQ-2 → VQ-3 ゲートの prerequisites）。

認定ゲート順注記：VQ-4 認定は VQ-3 達成を前提とするため、EP-10a + EP-03a + EP-04a（VQ-3 ルート）を先行させた後に EP-09a + EP-08a + EP-01a を投入する順序が適切。

---

### §6 制度設計への寄与

**1. 既存 RI コードの代表事例確認**

本ケースは既存 RI コードのいくつかに明確な代表事例を提供した：

- **RI-09 (External superiority) の典型例**: 「among the highest reported TOF」という外部比較優位性主張を数値なしに行い、比較 benchmark 文献の具体値も示さない構造。SRG-6 / D-4-3 として記録。本 RI は Kumada 1972 等の先行ケースでも観察されており、触媒合成論文での共通パターンとして確認が累積している。
- **RI-05 (Qualitative overread) のダブル発動**: SRG-3（regioselectivity: 操作的主張→機構的主張への飛躍）と SRG-4（ring-strain: 定性的速度差→mechanistic assignment）の2箇所で独立に RI-05 が発動した。同一論文で RI-05 が複数の独立した箇所に共起することは、方法論論文よりも実験的発見論文でより多く観察される可能性があり、今後の比較データとして記録に値する。

**2. EP-10a (Kinetic verification pack) の Murai 1993 代表事例確認**

EP-10a の正式登録（2026-04-27、v18.3）の根拠の一つは「GPT-5.5 on Murai 1993」による確認であり、本 Stage 3 v4 分析はその Sonnet 4.6 版対応確認として機能する。SRG-2（RI-03 + RI-06 同時前進）と CLA-1（触媒サイクル予測の未検証）に対して EP-10a が最高情報利得 EP として同定されたことは、EP-10a の case-specific 実装のバリエーション（Ru 触媒 C–H 活性化、1993 年報）として記録する。

**3. PRI-11 (Mechanism-kinetics decoupling) 確認**

D-4-1 および SRG-2 / CLA-1 の分析は、「提案触媒サイクルから速度式を代数的に導出せずに、機構を支持している」という PRI-11 パターンの Murai 1993 における発現を確認した。PRI-11 の昇格候補状態（2報の独立確認：Breitenfeld 2014 + Pengfei 2024）に本ケースが第3の独立確認として加わり得る。しかし PRI-11 はすでに 2 報確認済みで昇格候補状態にあり、Murai 1993 はその追加事例に過ぎない（新規 PRI 提案には至らない）。§6 注記として「PRI-11 の Ru 系触媒 C–H 活性化への適用事例」として記録する。

**4. PRI-12 非適用の確認（単一 paradigm 実験論文）**

PRI-12 クラスター A（Self-referential validation）および クラスター B（Deductive-retrospective circularity）はともに本論文には非適用であることが確認された。本論文は新規実験結果を報告する実験的方法論論文（新触媒反応の実証）であり、計算量・指標・形式理論の提案論文ではない。この確認は、PRI-12 の適用境界（実験論文 vs 計算/理論/方法論論文）の明示化に貢献する。

**5. 標識不整合（Labeling mismatch）パターンの記録**

D-4-8（CLA-2）で記録した「unactivated C–H bonds」フレームと「chelation-assisted activation」の内的矛盾は、§6 の標識不整合パターンとして記録する。著者は機構提案節でキレーション補助を核心原理として述べているが（「[REDACTED: verbatim source text; see the source paper via its DOI]」）、efficiency 節の優位性フレームでは「unactivated C–H bonds」を使用している。この仮説標識の位置的分離——本文冒頭と efficiency 節では事実的記述語、mechanistic 節では明示的仮説 ("The reaction may begin with…", "not yet clear")——は RI-06 との連動が弱く、むしろ RI-05（操作的-機構的飛躍）と連動している点が Kumada 1972 とは異なるパターンを示す。

**6. PRI-12 候補の不在確認（新規 PRI 提案なし）**

本ケースでは新規 PRI 候補を提案すべきパターンは検出されなかった。本ケースは既存の制度設計（RI-01〜RI-09、PRI-10〜PRI-12、EP-01a〜EP-10a）を追加確認する結果となった。

**7. 通信→Full Paper 遷移の自動解消パターン（予測）**

B-1、B-6、SRG-8 に記録された「standard methods」の未特定と GC calibration 欠如は、Nature Articles 3 ページ形式の format-imposed compression に起因する（§4 communication-era tolerated）。もし本論文が Full Paper 形式（例：JACS、Organometallics）で発表されていたならば、これらの RI-01 関連問題は自動解消されていた可能性が高い（「通信→Full Paper 遷移の自動解消パターン」）。実際、Murai グループは 1993 年以降に複数の Full Paper を発表し（Chatani/Kakiuchi らによる follow-up series）、本論文の A-2（scope extension）と B-5（olefin scope 制限）も段階的に解消されている（retrospective: series_signal 実現）。これは §6 の「通信→Full Paper 遷移の自動解消パターン」として記録する。

---

*End of Assessment Sheet*
