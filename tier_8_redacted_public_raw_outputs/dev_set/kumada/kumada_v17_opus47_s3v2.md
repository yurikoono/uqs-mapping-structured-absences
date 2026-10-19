```
prompt_version: stage3-v2-20260416
model_info: Claude Opus 4.7 (claude-opus-4-7[1m])
```

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc., Communication）

---

### §1 Claim Architecture

**コア主張：** ジハロジホスフィンニッケル(II)錯体（代表例：[NiCl₂(dpe)]）が、Grignard 試薬と C_sp² ハロゲン化物（ビニル／アリール塩化物）との選択的クロスカップリングを触媒する。**Novelty 柱**は (a) Ni-ホスフィン触媒系の導入、(b) 二座ジホスフィン配位子の活性優位性、(c) C_sp²-Cl 基質の実用的利用、(d) β-H をもつ Grignard 試薬への寛容性、(e) 1,2-ジクロロエチレンから cis-スチルベンへの経路、(f) Et₂O > THF の溶媒効果——の六層。**Utility 柱**は「難入手化合物（例：m-ジ-n-ブチルベンゼン、α-ビニルナフタレン）を一段階で得る」合成的便益、および後続する均一系触媒化学への方法論的基盤提供。

**Layered structure：** **yes**。上記 (a)-(f) は相互に独立しており、単一の反証では全主張が崩れない。例えば Corriu-Masse Ni(acac)₂ が同変換を達成することが後に確認されても、(b) の「二座 > 単座」配位子順序と (d) の β-H 寛容性は独立に成立する。層間の依存関係：(b)-(f) は触媒サイクル（§2 SRG-2）の機構解釈を共有するが、各層の現象論的観察（収率、選択性）はサイクルの正しさから独立している。この多層構造は、機構層（SRG-2）が未解決でも方法論層（Table I の収率）は独立に通信価値を保持するという asymmetric robustness を生む。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1「マスバランスと副生成物定量の不在」**

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: 「selective cross-coupling」という中心主張を採るには、ホモカップリング（R-R, R'-R'）・還元（R-H, R'-H）・β-H 脱離（butenes）・ディスプロポーション積の定量、および GLPC 検出下限の開示による質量収支の閉鎖（≥ 95% target）が必要。
* **EP**: EP-08a [Replication / uncertainty pack]; EP-04a [Discrimination / replication pack]
* **Case-specific 実装**: Ph-n-Bu（76% エントリ）を対象に、Et₂O 中で [NiCl₂(dpe)] 仕込み量 1 mol% に固定、n-BuMgBr/PhCl = 1.2 で 20 h 還流中 30 min 毎 GLPC サンプリング（OV-17 キャピラリカラム、n-C₁₀H₂₂ 内部標準）。n-オクタン（Wurtz）、ビフェニル、1-ブテン、n-ブタン、PhCl 消失を同時追跡し、マスバランス閉鎖度を報告。U-04 が予測する「触媒活性化段階での化学量論的 R-R 生成」（初期 Ni 投入量 × 1）の検証もここで可能。
* **注記**: 下位項目 B-01, B-04, B-13, U-04。TEMPERATURE_SUMMARY 上で B-01 は high_convergence_low_gap（2/3, none）、U-04 は self-contradictory absence。

---

**SRG-2「提案触媒サイクルの直接的証拠の不在」**

* **Primary RI**: RI-03 [Unobserved explanatory]（サブタイプ適用：中間体 1, 2, 3 は未観測）
* **Secondary RI**: RI-06 [Imported model]（サイクルレベル輸入：eqs 1-4 は refs 11-12 の (dipy)Ni(Et)₂ 系から輸入、[NiCl₂(dpe)] 系での同型性は実証されていない）; **PRI-11** [Mechanism-kinetics decoupling]（暫定：提案サイクルから速度式を代数的に導出せずに、end-point 収率のみで機構を支持）
* **ER**: 触媒サイクルの機構的主張を採るには、(i) 中間体 1, 2, 3 のいずれかの分光学的直接観測または trap、(ii) [RMgX'], [RX], [Ni] に関する初期速度次数、(iii) 酸化状態割当（Ni(0)/Ni(II) vs Ni(II)/Ni(IV)）、(iv) クロスオーバー実験による R' 継代保持の検証、の最低二つが必要。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]; EP-10a [Kinetic verification pack]（暫定）
* **Case-specific 実装**: (i) [NiCl₂(dpe)] + n-BuMgBr（2 eq）を Et₂O-d₁₀ 中 -78 ℃ で混合、³¹P{¹H} NMR を -78 → 25 ℃ で温度可変測定し L₂NiR₂ の ³¹P 化学シフト変化を追跡。(ii) PhCl 添加後の in situ ³¹P / ¹H NMR で L₂Ni(R)(Cl) 中間体の検出。(iii) Cl₂Hg でのラジカル trap、または CAr-Cl の para-置換による σ Hammett 分析（n=5 p-X-C₆H₄Cl, X = OMe, H, Cl, CF₃, CN）。(iv) 時刻 0 で PhCl、時刻 t で PhCl-d₅ 添加し、生成 Ph-n-Bu の d₀/d₅ 比から R' 解離・再結合を評価。
* **注記**: 下位項目 A-01, A-02, A-05, A-07, A-13, U-01。6 項目を含む最大 SRG。U-01 は self-contradictory absence（eq 1 の先例はホモカップリングを示すのに提案サイクルはクロスカップリングを予測する矛盾）。

---

**SRG-3「1,2-ジクロロエチレンでの立体スクランブル」**

* **Primary RI**: RI-04 [Unreplicated discriminator]（単一測定による機構的診断値）
* **Secondary RI**: RI-01 [Reporting integrity]（cis:trans 測定方法未開示）
* **ER**: "rather nonstereospecifically" を機構的診断として採るには、(a) 測定方法（GLPC カラム／¹H NMR）と不確かさの開示、(b) 反応時間を変えた cis:trans 比の時間発展、(c) 生成スチルベンの反応条件下異性化試験（control）、(d) [PhMgBr] 依存性、の四軸が必要。
* **EP**: EP-04a [Discrimination / replication pack]; EP-01a [Reporting-coherence pack]
* **Case-specific 実装**: cis- および trans-ClCH=CHCl（99% 異性体純度）を PhMgBr / [NiCl₂(dpe)] / Et₂O 条件下で処理。反応を t = 0.5, 2, 5, 20 h で停止し cis:trans スチルベン比を GLPC (SE-30) + ¹H NMR (300 MHz 以上) の両方で測定。ブランク対照として純粋 cis-スチルベンと trans-スチルベンを同条件下で処理し、触媒による stilbene 異性化能を評価。ラジカル介在を probe するため、10 mol% TEMPO または galvinoxyl 存在下での比較も実施。
* **注記**: 下位項目 A-04, A-14, B-10。A-14 は convergence 3/3（high_convergence_low_gap）; A-04 は V2 critical（low_convergence_high_gap）。

---

**SRG-4「配位子活性順位の定性的記述」**

* **Primary RI**: RI-05 [Qualitative overread]（">" と "≈" の定性記述から "cis configuration is the first requisite" という構造的含意を導出）
* **Secondary RI**: RI-08 [Unquantified reliability]（単一基質ペアから一般化）
* **ER**: 配位子順位を機構的含意に接続するには、(a) 複数基質ペアでの yields/time-course データ、(b) cis-強制型単座配位子（dba + 2 PMe₃ in situ cis-constrained）などによる "chelation vs cis-geometry" の分離制御、(c) ³¹P NMR による free phosphine 濃度のモニター、の三要素が必要。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific 実装**: [NiCl₂(L)]（L = dpp, dpe, dmpe, (PPh₃)₂, (PEt₃)₂, (PPh₂Me)₂, dppp, dppb, dppf）の9配位子を、(Ph-n-Bu 生成 + Ph-Et 生成 + α-Np-vinyl 生成) の3基質ペアで測定。各ペアで 1, 5, 20 h 時点の GLPC 収率を記録し TOF を算出。cis-強制のための二価単座制御として、cis-固定されたシクロパラジフェニレン系に対応する Ni 錯体を別途合成。
* **注記**: 下位項目 A-02, A-12, B-02, B-18。

---

**SRG-5「触媒終状態への沈黙（黒色混合物・多量の塩）」**

* **Primary RI**: RI-02 [Object identification]（"black mixture" と "much salt" が同定されない）
* **Secondary RI**: RI-03 [Unobserved explanatory]（触媒終状態という機構的説明を担う状態が未観測）
* **ER**: 触媒均一性／TON／配位子比較の解釈可能性を確保するには、(a) 反応終了時の溶液相と固相への Ni 分配（AA または ICP-OES）、(b) 沈殿の XRD / SEM-EDX、(c) 均一溶液側の EPR（Ni(0)/(I)/(III) の検出）、(d) 触媒 filtering test（0.22 μm 濾過後の残余活性）の最低二つが必要。
* **EP**: EP-02a [Identity / purity substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific 実装**: Example 1 の Ph-n-Bu 反応（53.9 mmol m-Cl₂C₆H₄ + 120 mmol n-BuMgBr + 0.39 mmol [NiCl₂(dpe)]）を 20 h 還流後、反応混合物を Ar 雰囲気下で遠心分離（Schlenk 対応）。溶液相・沈殿をそれぞれ酸分解後 ICP-OES で Ni, Mg, Cl 定量。上清に対し filtering test + Hg-drop test でヘテロジニアス触媒経路の寄与を評価。
* **注記**: 下位項目 A-12, U-02, U-03。U-02, U-03 はいずれも self-contradictory absence（観察が記録されながら分析されない）。

---

**SRG-6「表エントリ単位の分析的開示欠落」**

* **Primary RI**: RI-01 [Reporting integrity]（10 エントリが "and/or" と "A/B" 条件指示の単一フットノートに集約）
* **Secondary RI**: RI-02 [Object identification]（"pure" が数値化されない）
* **ER**: エントリ単位の横比較可能性を確保するには、(a) 各エントリの GLPC カラム／温度プログラム／内部標準、(b) 各新規化合物の燃焼 EA または HR-MS、(c) 複製数と標準偏差、(d) 単離収率 vs GLPC 収率を列で分ける、(e) 蒸留後の GLPC 純度、の五要件。
* **EP**: EP-01a [Reporting-coherence pack]; EP-02a [Identity / purity substantiation pack]
* **Case-specific 実装**: Supporting Information 形式で 10 エントリを (触媒 mol%, 温度, 時間, スケール, Grignard:RX モル比, Et₂O 体積, 収率 ± SD (n=3), GLPC 純度, EA C/H %, HR-MS) の 10 列テーブルに展開。RI-01 の解消。
* **注記**: 下位項目 B-08, B-09, B-10, B-11, B-12, B-16, B-17。最大項目数の SRG（7項目）。

---

**SRG-7「溶媒効果の非裏付け」**

* **Primary RI**: RI-05 [Qualitative overread]（"definitely superior" が裏付けなし）
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: 溶媒優位性を採るには、Et₂O, THF, 1,4-dioxane, DME, toluene/Et₂O 混合を同基質ペアで yield + rate + Ni 均一性で比較。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific 実装**: n-BuMgBr + PhCl + [NiCl₂(dpe)] を上記 5 溶媒系で、-10, 0, 25, 35 ℃（還流）の 4 温度 × 5 時点の 5×4×5 matrix で測定。Schlenk 平衡の NMR 診断も併走（¹H, ²⁵Mg NMR の溶媒依存性）。
* **注記**: 下位項目 A-10, A-11, B-03。

---

**SRG-8「β-H 寛容性の機構的未解決」**

* **Primary RI**: RI-03 [Unobserved explanatory]（k_RE / k_{β-H} という "β-H 寛容性" の説明を担う量が未測定）
* **Secondary RI**: RI-06 [Imported model]（ref 17 の β-H 不安定性一般論を輸入）
* **ER**: β-H 寛容性の機構的主張を採るには、(a) β-D 標識 Grignard からの生成物での β-D 保持率、(b) 添加オレフィン（1-ヘキセン等）存在下での交換実験、(c) Eyring パラメータ（ΔH‡, ΔS‡）、の三要素。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific 実装**: n-Bu-d₁-MgBr（β-D₂ 標識）+ PhCl + [NiCl₂(dpe)] で生成 Ph-n-Bu-d_n の ²H NMR 分布を測定。β-H 挿入-脱離の可逆性がある場合は D scrambling が観測される。並行して 1-ヘキセン 10 eq 存在下で crossover を評価。
* **注記**: 下位項目 A-03, A-06, C-04。

---

**SRG-9「C_sp³ / 重ハロゲン化物の境界主張の非裏付け」**

* **Primary RI**: RI-07 [Unsupported boundary]（[REDACTED: substantial verbatim quotation; see Tier 9] は失敗試行データなしに断言）
* **Secondary RI**: RI-09 [External superiority]（"high reactivity of chlorides" は Br/I と head-to-head なし）
* **ER**: 境界主張を採るには、(a) C_sp³ 基質（n-BuBr, n-BuCl, c-HexBr）での収率・主生成物の報告、(b) 同一 Grignard/基質での Cl/Br/I 収率と速度比較、の両方。
* **EP**: EP-07a [Boundary-test pack]; EP-09a [Internal benchmark pack]
* **Case-specific 実装**: PhMgBr 固定で PhCl, PhBr, PhI との反応を 0, 0.1, 1, 5 mol% [NiCl₂(dpe)] の各仕込み量で測定。C_sp³ 側では n-BuMgBr + n-BuBr, n-BuI, c-HexBr, Me₃CCH₂Br（neopentyl: 無 β-H）を測定。Neopentyl Br で反応が起これば β-H 不安定論拠への反例、起きなければ sp²/sp³ 差の別要因を示唆。
* **注記**: 下位項目 B-05, B-06。RI-07 拡張適用：否定的境界主張にも RI-07 を適用。

---

**SRG-10「収率基準の不整合」**

* **Primary RI**: RI-01 [Reporting integrity]（isolated / GLPC 収率、per-halide / per-Grignard 基準が単一表内で混在）
* **Secondary RI**: **RI-08 サブタイプ 内部矛盾型**（Example 2 の 80% が per-Grignard なら Table I の 80% と同一なのか異なるのかが決定不能）
* **ER**: 単一テーブル内でのメトリクス統一、少なくとも列分割。
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific 実装**: Table I を「単離収率（列 A）／GLPC 収率（列 B）／per-halide 基準（列 C）／per-Grignard 基準（列 D）」の 4 列構造に分割。α-Np + vinyl は過剰 vinyl のため per-Grignard が妥当、他エントリは per-halide。
* **注記**: 下位項目 B-08, B-14。

---

**SRG 外：CLA**

**CLA-1「Corriu-Masse Ni(acac)₂ との非比較：ホスフィン配位子要件の未実証」**

* **Primary RI**: RI-09 [External superiority]（Ni-ホスフィン系の "phosphine" フレーミングが Ni(acac)₂ 対照なしに宣言）
* **Secondary RI**: RI-06 [Imported model]（phosphine の役割についての背景論拠を refs 1-3 から輸入）
* **ER**: Ni-ホスフィンのタイトル請求を採るには、同一 Grignard / 基質ペアでの Ni(acac)₂（phosphine なし）vs [NiCl₂(dpe)] の直接比較収率と時間発展が必要。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific 実装**: n-BuMgBr + m-Cl₂C₆H₄, PhMgBr + PhCl, PhMgBr + cis-ClCH=CHCl, α-NpMgBr + CH₂=CHCl の 4 基質ペアを、Ni(acac)₂（1, 5, 10 mol%）vs [NiCl₂(dpe)]（1 mol%）vs NiCl₂·6H₂O（1 mol%）vs 無触媒 の 4 条件で比較。feature 3 の配位子順位にある PPh₃, PEt₃, PPh₂Me も同比較ラインに加え、配位子「要否」vs「影響」を分離。
* **注記**: 下位項目 B-07, C-01。これはいずれの SRG にも含まれない claim-level adjunct（タイトル・NC 項目に直結）。

---

**CLA-2「"Selective" の operational 定義不在：速度論／熱力学制御の未分離」**

* **Primary RI**: RI-05 [Qualitative overread]（"selective" が操作的に定義されず、自己矛盾的不在が潜在）
* **Secondary RI**: PRI-11 [Mechanism-kinetics decoupling]
* **ER**: "selective cross-coupling" の主張を採るには、(a) selectivity を k_cross / k_homo の比として定義、(b) 熱力学的停点と速度論的停点の区別、(c) 1,1- vs 1,2-dichloroethylene の異なる挙動が速度論 vs 熱力学のどちらを診断するかの操作化、の三要素。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-10a [Kinetic verification pack]（暫定）
* **Case-specific 実装**: R-R / R-R' / R'-R' の 3 種を同時 GLPC 定量し、k_cross / k_homo 比を時間発展で追跡。reversibility を確認するため、予め単離した R-R ホモ積と [NiCl₂(dpe)] + R'MgX を共存させ、交差積への再分配を試験。
* **注記**: 下位項目 A-04, A-14, B-01, U-04（U-04 は SRG-1 に属し self-contradictory absence）。D-4 候補 D4-2, D4-8 に対応。

---

### §3 現在の VQ 判定

**現在判定（era-norm 適用下）: VQ-2 (Method)**
**現在判定（modern-era）: VQ-1 (Observation) qualified**

**VQ-1 (Observation)**: **通る**（era-norm 下で非致命）。
- 根拠: 単離化合物（m-ジ-n-ブチルベンゼン, α-ビニルナフタレン, cis-/trans-スチルベン, Ph-Et, Ph-n-Bu 等 10 種）の構造は bp + n_D + footnote c の "glpc, nmr, ir, and/or mass spectra" で同定されており、1972 年 JACS Communications 標準では十分。
- 非致命的な残存: B-11（bp 圧力非整合）, B-16（"pure" の数値化不在）, B-17（EA 欠落）は modern-era では致命的だが 1972 年では era-norm tolerated。
- Modern-era では RI-02（規制方向性の不在）により qualified。

**VQ-2 (Method)**: **通る（era-norm 下）** / **未達（modern-era）**。
- VQ-1 の era-norm 通過を前提に成立。
- Era-norm 下: Example 1, 2 の全プロトコルが開示され、condition A/B の参照が通信形式で許容される。RI-07（C_sp³ 境界）も当時は「今後の課題」扱いで非致命。
- Modern-era 下: RI-01（per-entry 条件非開示, 収率基準混在 SRG-10）+ RI-07（C_sp³ 失敗試行データ不在）が解消されないため未達。

**VQ-3 (Mechanism)**: **未達**（era-norm・modern 両方）。
- 未解消 RI: RI-03（SRG-2 中間体未観測, SRG-8 k_RE/k_{β-H} 未測定, SRG-5 触媒終状態未同定）、RI-04（SRG-3 cis:trans 単一測定）、RI-06（SRG-2 輸入モデル, SRG-8 β-H 不安定論拠輸入）、PRI-11（速度式の代数的導出なし）、RI-05 重大残存（SRG-4, SRG-7, CLA-2）。
- VQ-3 は era-norm 下でも qualified 以下。RI-05 の重大残存により qualified 判定に留まる。
- 層別 VQ 非対称性の検出: 以下の層別評価を付す。
  - **方法論層（Novelty 柱 a, c, d）単独では**: era-norm 下で VQ-2 到達。Table I の 10 エントリと 2 つの worked example が反復可能性を担保。
  - **機構層（Novelty 柱の暗黙層、eqs 2-4）単独では**: VQ-1 にも到達しない。中間体 1, 2, 3 は物質として同定されていない（RI-02 + RI-03 複合未解消）。
  - **cis-スチルベン層（Novelty 柱 e）単独では**: VQ-1 qualified。測定方法が不在（B-10）のため、観測自体の再現可能性が era-norm 下でも不安定。
  - **配位子順位層（Novelty 柱 b）単独では**: era-norm 下で VQ-2 qualified。RI-05 が重大残存。

**VQ-4 (Benchmark)**: **未達**。
- 未解消 RI: RI-08（全 Table I エントリの複製・不確かさ不在）、RI-09（Corriu-Masse Ni(acac)₂ 比較不在 CLA-1, Tamura-Kochi 数値比較不在）。
- VQ-3 が未達のため VQ-4 も継承原則上到達不能。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**
- B-08（isolated/GLPC 収率混在）— JACS Communications 1972 では単一 footnote での区別が慣例的。
- B-09（"glpc, nmr, ir, and/or mass spectra" の集約）— 10 エントリに対し 1-sentence の characterization footnote は communication 形式で標準的。
- B-11（bp 圧力非整合）— 蒸留条件の literature 比較は "approximate agreement" で許容される当時の慣習。
- B-12（エラーバー・複製数不在）— 1972 年 JACS Communications で統計的複製開示は稀。
- B-14（α-Np エントリの per-Grignard 基準）— 過剰試薬のある反応で per-limiting-reagent 基準を採る記述は当時の通例。
- B-15（condition A/B への参照）— 通信形式の紙幅制約下で典型的省略。
- B-16（"pure" の数値化不在）— "pure" が distillation 後の一般的記述として許容。
- B-17（燃焼 EA の欠落）— 実は 1972 年 JACS Communications では EA 付記が慣例だったため borderline。完全 era-norm tolerated ではなく semi-deficient。
- A-15（条件非最適化宣言）— "not necessarily optimum" は当時の communication で標準的 disclaimer。

**modern-era deficient:**
- B-01（マスバランス不在）— "selective" 主張に必須。modern での cross-coupling の再認定は副生成物定量を必要とする。
- B-02（配位子順位の定量根拠不在）— 現代では yield + time-course + TOF の開示が最低限。
- B-07 / CLA-1（Corriu-Masse 非比較）— タイトル請求の "phosphine" 要件を検証できない。
- B-13（GLPC 検出下限不在）— 副生成物の検出下限が開示されなければ mass balance 閉鎖の意味が定まらない。
- SRG-2 関連（A-01, A-02, A-05, A-07, A-13, U-01）— 現代では触媒サイクルの主張には ³¹P NMR や in situ 観測が標準。era-norm では A 項目として tolerated だが modern では deficient。
- SRG-3 関連（A-04, A-14, B-10）— 現代では機構的診断に用いる stereochem データは measurement method と複数時点測定が必須。
- U-02, U-03（黒色混合物・多量の塩の非同定）— era-norm では観察の詳細分析は求められない。modern では Ni 均一性／heterogeneity の評価が必須。

**両方に該当（当時も当時基準ぎりぎり、現代では deficient）:**
- B-17 EA 欠落 — 1972 年 JACS Communications での慣例は EA 付記だが通信形式では省略も散見。Borderline。
- B-04（Ph₂C=CH₂ aggregate vs mono）— 当時は合成結果の end-point 報告で許容。現代では monocoupled intermediate 不在の確認が標準。

---

### §5 最短補強ルート

**目的関数設定:**
- **第一目的関数**: VQ-3 (Mechanism) の era-norm 下到達。現在 VQ-2 (era-norm) から VQ-3 への引き上げ。
- **第二目的関数**: VQ-4 (Benchmark) 到達。VQ-3 を前提。

---

**VQ-3 への最短ルート:**

1. **EP-03a [Direct-observation / state-assignment pack]** — [NiCl₂(dpe)] + n-BuMgBr（2 eq）の -78 → 25 ℃ ³¹P{¹H} NMR 温度可変追跡 + PhCl 添加後の in situ NMR。中間体 1 (L₂NiR₂), 2 (L₂Ni(R)(Cl)) の存在を分光学的に確認し、SRG-2 の RI-03 を前進。Ni(0) の生成が検出されれば SRG-5 の RI-02 も同時に前進し、RI-06（サイクルレベル輸入）も輸入先から一部解放される。
2. **EP-10a [Kinetic verification pack]（暫定）** — n-BuMgBr + PhCl + [NiCl₂(dpe)] 系での初期速度 v = k[Ni]^a[RMgBr]^b[PhCl]^c の a, b, c を least-squares 決定。PRI-11（速度式代数導出の不在）を前進。観測される速度式からサイクル内の律速段階を特定。SRG-2 の RI-03 を副次的に前進。
3. **EP-04a [Discrimination / replication pack]** — SRG-3 の 1,2-ジクロロエチレン系で時間発展 cis:trans 測定、control（純粋 cis-/trans-スチルベンの条件下異性化）、TEMPO 存在下比較、α-d₁-α-chiral Grignard の retention 評価を並行実施。SRG-3 の RI-04 と SRG-2 の「radical vs 2e」選択を同時前進。
4. **EP-01a [Reporting-coherence pack]** — Table I を per-entry で (mol%, T, t, scale, 基準, SD) 開示する SI 展開。SRG-6 の RI-01 と SRG-10 を前進。era-norm では不要だが modern VQ-3 認定に必要。
5. **EP-02a [Identity / purity substantiation pack]** — 10 エントリ全製品の EA + HR-MS + GLPC 純度開示。SRG-6 の RI-02 を前進。

**VQ-4 への補強（VQ-3 後）:**
6. **EP-08a [Replication / uncertainty pack]** — Table I 全エントリの n=3 複製と SD 報告。SRG-1 の RI-08 を前進。
7. **EP-09a [Internal benchmark pack]** — CLA-1 の Ni(acac)₂ vs [NiCl₂(dpe)] 直接比較 + SRG-9 の Cl/Br/I 比較。
8. **EP-07a [Boundary-test pack]** — SRG-9 の C_sp³ 失敗エントリ（n-BuBr, c-HexBr, neopentyl-Br）の試行と主生成物同定。
9. **EP-05a [Quantitative-ranking substantiation pack]** — SRG-4 の配位子 9 種 × 基質 3 種 matrix + cis-強制制御。SRG-4 の RI-05 を前進。
10. **EP-06a [Analogy-validation pack]** — SRG-8 の β-d 標識 Grignard + Eyring + 添加オレフィン交換実験。

**認定ゲート順注記:** 実験投入順は情報利得順であり、EP-03a, EP-10a, EP-04a を先行させて機構層の可視化を優先するが、最終認定は継承原則に従い VQ-1 → VQ-2 → VQ-3 → VQ-4 のゲート順で確定する。したがって EP-01a / EP-02a（VQ-2 の modern 要件）は VQ-3 確認実験と並行して走らせ、VQ-3 認定時に両方が揃っていることが必要。

---

### §6 制度設計への寄与

本ケースが Codebook・VQ 基準・EP 辞書に対して提供する知見：

**(i) 既存 RI の新しい代表事例:**
- **RI-03 サブタイプ "Available-but-unutilized characterization" 補強例**: 論文が自らの観察（"black mixture"、"much salt"）を記述しながら、その同定に必要な分析（Ni 定量、XRD）を施していない点は、既存サブタイプ "Available-but-unutilized characterization" と並ぶ新サブタイプ候補 "Recorded-but-uninterrogated observation" の萌芽として記録しうる。Monnereau 2009 や Breitenfeld 2014 との比較で PRI 昇格を検討する余地あり。
- **RI-07 否定的境界主張への拡張適用（v0.2a サブタイプ）の代表例**: [REDACTED: substantial verbatim quotation; see Tier 9] は否定的境界主張の典型例（SRG-9）。この論文は拡張適用が必要な 1972 年起源のケースを提供する。
- **RI-08 内部矛盾型（v0.2a サブタイプ）の代表例**: SRG-10 の per-halide/per-Grignard 基準混在は、同一論文内で2つの量の計算基準が不一致となる「内部矛盾型」の典型。

**(ii) 新しい PRI 候補の提案:**
- **"Self-predicted-but-unreported-byproduct" PRI 候補**: 論文の触媒サイクル自身が（eq 1 の先例と eq 2 の初期化ステップを合わせて）化学量論的 R-R ホモカップリング生成を予測するにもかかわらず、当該 R-R が定量されない U-04 の自己矛盾的不在は、既存 RI-08 や RI-03 とは異なる独立パターンを示唆する。「モデルが予測する観測量を測らない」という pattern を、**PRI-12 candidate: Self-prediction-observation gap** として提案する。Breitenfeld 2014 や Pengfei 2024 で類似パターンが検出された場合は昇格候補。
- **PRI-11 (Mechanism-kinetics decoupling) 昇格の補強**: 本ケースの SRG-2 は PRI-11 の定義「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」を満たす。1972 年の通信形式では速度次数すら観測されていないため、より極端な形の PRI-11 サブタイプ "Kinetic-observation absence" として記録可能。PRI-11 の独立 2 報確認（Breitenfeld, Pengfei）に本ケースを追加しても 3 報目となり、昇格判断材料を補強する。

**(iii) VQ 判定境界条件の知見:**
- **層別 VQ 非対称性の典型例**: 本論文は Layered structure により、方法論層（Novelty 柱 a, c, d）単独では era-norm VQ-2 に到達し、機構層（暗黙の Novelty 柱）は VQ-1 にも届かないという層別非対称性を明瞭に示す。この asymmetric robustness は「単一反証で全主張は崩れないが、機構主張は単独で脆弱」という Communications 論文の典型構造。VQ 判定基準マトリクスの層別適用ガイドラインに本ケースを追加推奨。
- **Era-norm tolerated → modern deficient の移行例**: B-17（EA 欠落）は 1972 年 borderline だった慣行が modern で明確に deficient に分類される典型例。Era-norm 境界条件の時代区分を記録する補強例。

**(iv) EP 辞書への case-specific 追加:**
- EP-03a の "cis-強制単座配位子対照" 実装（SRG-4 Case-specific の cis-固定シクロパラジフェニレン Ni 錯体）は、既存の EP-03a の Ni 系実装に追加推奨。
- EP-04a の "radical probe + α-chiral Grignard stereochem + TEMPO" 3-way 並行評価（SRG-3 Case-specific）は Ni-Grignard 系特異的な実装として追加。
- EP-07a の "sp²/sp³ 対称境界試験" 実装（neopentyl-Br 等、無 β-H 炭素中心で β-H 論拠を探針する SRG-9）は Boundary-test pack の新エントリに値する。

**(v) 標識不整合（Labeling mismatch）の検出:**
- 本論文は明確な標識不整合を示す: eqs 2-4 の本文ナレーションが事実的記述動詞（"reacts with," "form," "is converted to," "forms," "successive reaction"）を使用するのに対し、「working hypothesis」という仮説標識は最終段落の一文（"apart from the working hypothesis described above"）に圧縮されている。この仮説標識の末尾集約は、読者がテクストの中盤で受け取る「提案サイクルは事実」という impression を弱めない構造として機能する。RI-06（Imported model）と連動する典型例として記録。

**(vi) 通信 → Full Paper 自動解消パターン:**
- B-15（per-entry 条件不在）, B-17（EA 欠落）, B-12（複製数不在）は communications の紙幅制約起因であり、Kumada グループの後続 Full Paper（Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, Bull. Chem. Soc. Jpn. 49, 1958, 1976 等）で自動解消されたと予測される。§4 の era-norm tolerated 項目のうち A 項目との対応を確認する必要があるケース。

**(vii) RI 共起パターン:**
- **SRG-2 の RI-03 + RI-06 + PRI-11 共起**: サイクルの intermediate は未観測（RI-03）、サイクル自体は他系から輸入（RI-06）、そしてサイクルから速度式が代数的に導出されていない（PRI-11）——この 3 項共起は、いずれか一つの解消では VQ-3 到達に不十分で、最低でも RI-03 と PRI-11 の両方の前進が必要。SRG-2 は「共起 RI を同時に解消する EP の設計」の test case として使える。
- **SRG-9 の RI-07 + RI-09 共起**: C_sp³ の否定的境界主張（RI-07）と Cl/Br/I の比較不在（RI-09）は実質的に同一 EP-07a + EP-09a の複合投入で解消。Boundary と external superiority が連動する典型。

**(viii) 否定的証拠の不完全性:**
- 本論文は明示的なラジカルクロック実験・TEMPO trap は未実施だが、同時に「ラジカル経路を棄却した」という肯定的主張も行っていない——RI-04 の case-specific 実装としての「否定的証拠の不完全性」は直接適用されない。ただし、1,2-dichloroethylene の cis:trans scramble を "rather nonstereospecifically" と記述しつつ原因を特定しない点は、「ラジカル経路 vs σ-vinyl-Ni 回転 vs post-coupling isomerization」の三経路のいずれを肯定的にも否定的にも主張していない状態であり、EP-04a の "exhaustive exclusion matrix" が必要なケース。

**結論**: 本ケースは、既存 Codebook v0.2a の (i) RI-03 サブタイプ拡張、(ii) RI-07 否定的境界主張、(iii) RI-08 内部矛盾型、(iv) PRI-11 Mechanism-kinetics decoupling、(v) 層別 VQ 非対称性、(vi) 通信 → Full Paper 自動解消パターンの 6 箇所で代表事例を提供する。新規パターン候補として **PRI-12 "Self-prediction-observation gap"** を提案する。

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
