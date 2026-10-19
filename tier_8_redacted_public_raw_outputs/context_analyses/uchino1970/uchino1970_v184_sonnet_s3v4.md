```
prompt_version: stage3-v4-20260427
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Uchino, Yamamoto & Ikeda 1970（Journal of Organometallic Chemistry, Preliminary communication）

---

### §1 Claim Architecture

**コア主張の要約:**
本論文は二つの独立した主張層から構成される。

**Layer 1（合成ニュース）— Novelty 柱:** diethyl(dipyridyl)nickel（compound I）を
クロロベンゼン中で室温処理することで、dipyridyl 二座配位子によって安定化された
Ni–C(フェニル) 結合を持つ結晶性錯体 phenyl(dipyridyl)nickel chloride（compound II,
C₆H₅(dipy)NiCl · ½C₆H₅Cl）を単離できる。これは先行する Chatt–Shaw (1960) および
Miller (1970) が「equivocal」と評価した無置換フェニルニッケル錯体の初めての結晶性
単離として位置づけられる。証拠基盤: 元素分析（C, H, N, Cl; Fajans 法による無機 Cl）
＋ 3 種の診断的化学反応（プロトン分解→ PhH; MeI 反応→トルエン; エタノール分解→ PhH）。

**Layer 2（触媒的意義）— Utility 柱:** Compound II は alkylaluminium halide 共存下で
α-オレフィン二量化触媒として「highly active」であると主張する。ただし全定量データが
脚注「Details of the dimerization catalyst will be published separately」で別報告に
外置きされており、本論文内には触媒性能の数値証拠が一切存在しない。

**Layered structure 判定: 二層構造・非対称依存（Layer 1 → Layer 2 の一方向前提）**

Layer 2（触媒的意義）が将来否定されても（例: compound II が真の触媒前駆体でないと
示されても）、Layer 1（compound II の合成・単離の事実）は崩れない。逆に、Layer 1 に
反論（化合物同定が誤りである）があれば Layer 2 も自動崩壊する。Layer 1 が Layer 2 の
前提条件であり、逆は成立しない非対称依存構造。「Preliminary communication」形式は、
Layer 2 の定量的検証が完了する前に Layer 1 を独立成果として発表するための構造的
装置として機能している。単一の反証で全主張が崩れるわけではなく、層の独立性は高い。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1: Mechanistic evidence absent**（B-2, B-3, U-1, U-2）

* **Primary RI**: RI-03 Unobserved explanatory
  　論文の中心合成反応（I + PhCl → compound II）において、Ni の酸化状態軌跡（U-2 critical）
  　および反応機構（B-3）が一切観測されていない。気体生成比（U-1）も未定量であり、
  　反応の「指紋」となる実験量がすべて未観測状態で残っている。
* **Secondary RI**: RI-04 Unreplicated discriminator
  　「緑色溶液が赤色に変化し、n-ブタン等が発生する」という観察（色変化＋気体発生）が
  　compound II 形成の証拠として提示されているが、この単一観察で oxidative addition /
  　radical / σ-bond metathesis の三つの競合機構を弁別する実験（kinetics, EPR, isotope
  　effect）は実施されていない。
* **ER**: C–Cl 活性化の機構を確立するためには、(1) 反応の反応次数（I 濃度、PhCl 濃度
  　依存性）、(2) ラジカル中間体の直接検出（EPR または TEMPO 捕捉）、(3) 気体組成の
  　定量 GC 分析（n-ブタン/エタン/エチレンのモル比）が最低限必要。
* **EP**: EP-03a Direct-observation / state-assignment pack ; EP-10a Kinetic verification pack
* **Case-specific 実装**:
  　EP-03a — 反応混合物の EPR 測定（Ni(I) または Ni(III) ラジカル中間体の検出）;
  　UV-Vis 時間分解スペクトル（I → II 転換の進行追跡）; 反応中の磁気感受率測定。
  　EP-10a — 変数温度下での I + PhCl の初期速度論（ΔH‡, ΔS‡ 決定）; ハメット
  　関係（置換クロロベンゼンで σ 定数 vs 速度定数）; ラジカルクロック実験（シクロプロピル
  　含有 aryl Cl 使用）; H/D 同位体効果（deuterated aryl chloride）。
* **注記**: B-2 (V1=high, V2=high, gap=none, convergence 2/3; high_convergence_low_gap);
  　B-3 (V1=high, gap=none); U-1 (high, self-contradictory absence);
  　U-2 (V2-only, critical, low_convergence_high_gap: フォールバック規則 (a) 最優先項目)。
  　SRG-1 は本論文の構造的核心課題。

---

**SRG-2: Analytical integrity of compound II formula**（B-4, B-11, B-10）

* **Primary RI**: RI-08 Unquantified reliability
  　元素分析が単一点（replicate なし）であり、B-4 の ½ 溶媒和物組成は EA 計算値への
  　最良フィットのみで決定。EA 典型精度（±0.3%/元素）の範囲内で ½ vs 1.0 vs 0 溶媒和物
  　を弁別できる保証がなく、再結晶時の溶媒蒸散（B-11）による組成変化も未考慮。
* **Secondary RI**: RI-01 Reporting integrity
  　反応診断（B-7）の「stoichiometric quantities」という記述に数値なし;
  　Fajans 法の校正データ（B-10）未提示。
* **ER**: ½ 溶媒和物組成を確認するには TGA（溶媒和クロロベンゼンの段階的脱溶媒和
  　プロファイル）または単結晶 X 線回折が必要。EA は triplicate + 標準偏差の提示が現代要件。
  　Fajans 法は認定参照物質での校正検証が必要。
* **EP**: EP-08a Replication / uncertainty pack ; EP-02a Identity / purity substantiation pack
* **Case-specific 実装**:
  　EP-08a — Triplicate EA（各元素 ±0.3% 以内）; TGA（50→200°C 加熱での重量減少
  　プロファイルで ClBenzene 脱離温度・量を確認）; Fajans 法を AgNO₃ 一次標準液で
  　校正（CaCl₂ 参照試料で独立確認）。
  　EP-02a — 単結晶 X 線回折（格子定数から溶媒和分子数を直接決定）。
* **注記**: B-4 (V1=medium(2), V3=high(3), gap=low, convergence 2/3; high_convergence_low_gap);
  　B-11 (V1+V3 収束 2/3); B-10 (SRG-4 とも共有: 化学的証明 vs 分析法信頼性の
  　両側面を持つブリッジ項目)。

---

**SRG-3: Catalytic activity claims without supporting data**（A-1, B-9, U-3）

* **Primary RI**: RI-05 Qualitative overread
  　"highly active dimerization catalyst" という評価語が数値根拠（TON, TOF, 反応速度）
  　なしに主張されている（A-1）。「高活性」の定量基準が存在せず、構造的に非反証可能
  　な主張となっている（V2-OV3 critical 指摘）。
* **Secondary RI**: RI-04 Unreplicated discriminator
  　U-3: クロロベンゼンによる活性向上（striking enhancement）という単一観察から
  　「compound II が触媒活性の原因」という因果帰属が行われているが、代替仮説
  　（Cl⁻ 単独効果、Ni(0) 酸化的付加経路）を排除する対照実験が一切ない。
* **ER**: (1) compound II + AlR₂X の TON/TOF（少なくとも 1 基質で）; (2) compound I +
  　AlR₂X との直接速度比較（同一条件下）; (3) Cl⁻ 塩（[Me₄N]Cl 等）を compound I に
  　添加した対照実験（compound II 形成を介さない Cl⁻ 効果の分離）。
* **EP**: EP-05a Quantitative-ranking substantiation pack ; EP-09a Internal benchmark pack
* **Case-specific 実装**:
  　EP-05a — エチレン二量化の TON（1 時間、室温、compound II 0.1 mol% + Et₂AlCl 1 eq.);
  　プロピレン二量化での選択性（2-methyl-1-pentene vs 線状 hexene 比）;
  　compound II vs compound I の速度比較（同一 Al/Ni 比・温度・圧力・溶媒）。
  　EP-09a — compound I と compound II を同一実験条件で並行測定し、
  　活性差の倍率と統計的有意性を報告。
* **注記**: A-1 (V1=high(3), V2=critical(4), gap=low, convergence 2/3; high_convergence_low_gap);
  　B-9 (electronic basis for I vs II activity difference: 未説明);
  　U-3 (high, self-contradictory absence; SRG-3 核心)。
  　Layer 2 全体がこの SRG の未解消状態にある。

---

**SRG-4: Chemical proof-of-structure and spectroscopic characterization**（B-1, B-7, [B-10 shared with SRG-2]）

* **Primary RI**: RI-02 Object identification
  　Compound II の構造証明は EA + 3 種の定性的化学反応のみ（B-1: スペクトル全不在）。
  　IR（ν(Ni–C), ν(C=N), ν(Ni–Cl)）も ¹H NMR も質量スペクトルも X 線回折も報告
  　されない。「未置換フェニル基が Ni に直接結合している」という核心主張を、代替構造
  　（ηˡ-配位 PhCl、π-フェニル、二量体 Ni₂ 錯体）に対して排除できる粒度の同定証拠がない。
* **Secondary RI**: RI-04 Unreplicated discriminator
  　診断的化学反応（B-7）が「stoichiometric quantities」と記述されるが数値なし; 三種の
  　反応のうちいずれも独立した定量的確認がなく、すべてが同一の合成バッチに由来する。
* **ER**: ¹H NMR（配位フェニル基の芳香族シフトと ½ 溶媒和クロロベンゼンの独立確認）
  　および IR（ν(Ni–C(aryl)) 450–550 cm⁻¹ 領域の帰属）が最低限必要。単結晶 X 線回折が
  　あれば結合様式（単核 vs 二核、Ni 配位数、溶媒和構造）を一義的に確定できる。
* **EP**: EP-02a Identity / purity substantiation pack ; EP-04a Discrimination / replication pack
* **Case-specific 実装**:
  　EP-02a — 単結晶 X 線（monoclinic/orthorhombic 結晶系; Ni–C(Ph) 結合距離；
  　dipy chelate 配座; ½ ClBenzene の格子中位置）; ¹H NMR in CDCl₂ (低温)。
  　EP-04a — 診断的反応の定量化（PhH 収率 GC; 各バッチ n ≥ 3 の繰り返し測定）;
  　別合成バッチで独立確認。
* **注記**: B-1 (V1=high(3), V3=critical(4), gap=low, convergence 2/3; high_convergence_low_gap);
  　B-7 (diagnostic reactions quantified なし); B-10 は SRG-2 とブリッジ。
  　1970 年に IR 分光が利用可能であった（Chatt–Shaw 1960 が Pd–aryl 錯体で IR 帰属
  　を行っている）ことを考えると、IR 不在は「時代的に unavailable」ではなく
  　「communication 形式慣行により不提示」に分類される必要がある（§4 で詳述）。

---

**SRG-5: Analogy references severed without comparative data**（C-2, C-3）

* **Primary RI**: RI-06 Imported model
  　Compound II の構造的意義の主張が、Chatt–Shaw (1960) および Miller (1970) の
  　NiX(aryl)·2PR₃ 化合物との「analogy」に依存しているが、モノデンテート PR₃ vs
  　二座 dipyridyl の電子的差異（π 逆供与能、キレート効果の大きさ）が compound II の
  　安定性や反応性に与える影響は分析されていない。先行化合物のモデルを対象系への
  　同型性実証なしに輸入している。
* **Secondary RI**: RI-05 Qualitative overread
  　先行合成の「equivocal」という評価（定性的な安定性・再現性上の問題）から、
  　compound II が「初めての isolable 無置換フェニルニッケル錯体」であるという
  　構造的含意が定量的比較なしに導出されている。
* **ER**: Compound II と Chatt–Shaw / Miller の類縁化合物の安定性を同一条件下で直接
  　比較（例：クロロベンゼン中の分解半減期; 元素分析純度の比較）。配位子電子的特性
  　（IR ν(M–C) 比較）による Ni–C 結合強度の比較。
* **EP**: EP-06a Analogy-validation pack
* **Case-specific 実装**:
  　EP-06a — Compound II と Ph(Et₃P)₂NiCl（Miller 類縁体合成）の CDCl₂ 中 ¹H NMR
  　比較; 同一条件（25°C, PhCl 溶媒）での分解速度（UV-Vis 時間経過）の比較;
  　IR ν(Ni–C(Ph)) バンドの wavenumber 比較による Ni–C 結合分極性の評価。
* **注記**: C-2 (Chatt & Shaw 1960, Ref 6); C-3 (Miller 1970, Ref 7);
  　SRG-5 は本論文の Novelty 主張の外部根拠の弱点を示す。

---

**SRG 外: CLA（Claim-level Adjunct）**

---

**CLA: Selective solvent stability mechanism**（D-4-7: B-6, B-13）

Stage 2 での分類: SRG-1（機構的不在）と SRG-2（分析的整合性）の交差領域。
いずれの SRG の member_items にも含まれないため CLA として記録。
D-1 の Layer 1 主張（compound II の安定性・貯蔵条件の定義）に直結する。

* **Primary RI**: RI-03 Unobserved explanatory
  　"Stable only in chlorobenzene" という選択的安定性の機構的根拠が全く観測されていない。
  　クロロベンゼン中では化合物が安定なのに、通常より弱い配位子と見なされる
  　トルエン（非極性芳香族）や供与性の高い THF・アセトン中で不安定となる逆説が
  　説明されていない。
* **Secondary RI**: RI-07 Unsupported boundary
  　「stable only in chlorobenzene」という否定的境界主張（RI-07 拡張適用）が速度論的
  　データ（分解半減期、活性化パラメータ）なしに提示されている。
* **ER**: 各溶媒中での compound II の分解速度（UV-Vis で Ni–Ph 吸収バンドの減衰追跡）;
  　分解生成物の同定（元素分析、MS 等）; クロロベンゼンの特異的安定化効果の機構
  　（配位子置換競合 vs π-acid 安定化 vs ラジカル経路 vs Ni–C 均一開裂）の特定。
* **EP**: EP-03a Direct-observation / state-assignment pack ; EP-07a Boundary-test pack
* **Case-specific 実装**:
  　EP-03a — 各溶媒（PhCl, THF, アセトン, トルエン）中での compound II の UV-Vis
  　スペクトル時間変化（ν(Ni–C(Ph)) 特性吸収の減衰定数 k_obs 決定, 25°C）。
  　EP-07a — 溶媒スクリーニング（PhF, PhBr, PhI, CH₂Cl₂, Et₂O, pyridine）で
  　「安定溶媒」の構造要件を体系的に決定; 分解中間体・生成物のキャラクタリゼーション。
* **注記**: B-6 (V1=medium(2), V2=medium(2), gap=none, convergence 2/3;
  　high_convergence_low_gap); B-13 (機構的説明なし)。
  　この CLA が解明されれば compound II の実用的貯蔵条件設計が可能になると同時に、
  　D-4-1 の機構問い（C–Cl 活性化後の Ni の電子状態）に間接的制約を与える。

---

**Self-referential validation チェック（PRI-12 cluster A）:**
本論文は合成・キャラクタリゼーション communication であり、計算量・指標・スコア関数の
提案を含まない。PRI-12 cluster A（自己参照的検証）の適用条件（a)–(d)はいずれも成立
しない。適用なし。

**Deductive-retrospective structure チェック（PRI-12 cluster B）:**
本論文は演繹的な理論提案論文ではなく、観察・合成報告である。PRI-12 cluster B
（演繹的遡及構造）の適用条件（a)–(d)はいずれも成立しない。適用なし。

---

### §3 現在のVQ判定

**Step 3a: Modern reassessment baseline（era-norm tolerance 非適用）**

**VQ-1 (Observation, RI-02 required):**
RI-02 Fatal。Compound II の同定は EA + 3 種の診断的化学反応のみ。
モノマー構造、Ni 配位数、½ 溶媒和物組成いずれも単独特定に至らない。
→ **VQ-1 not achieved（modern baseline）**

**VQ-2 (Method, RI-01 + RI-07 required, VQ-1 inherited):**
RI-01 Fatal（気体生成比未定量、EA 単一点、診断反応未定量）。
RI-07 Non-fatal だが未解消（"stable only in chlorobenzene" 無根拠境界）。
→ VQ-2 not reached

**VQ-3 (Mechanism, RI-03 + RI-04 + RI-06 required, VQ-2 inherited):**
RI-03 Fatal（C–Cl 活性化機構が完全未観測）; RI-04 Fatal（色変化 + 気体発生が
唯一の弁別証拠）; RI-06 Fatal（Chatt–Shaw/Miller 類推に同型性実証なし）。
→ VQ-3 not reached

**Step 3b: Era-norm annotation での補正**

**Layer 1（合成・キャラクタリゼーション）:**
- RI-02: 1970 年 J. Organomet. Chem. preliminary communication 形式において、
  EA + 診断的化学反応は新規有機金属錯体の「minimum viable characterization」として
  認定されていた。→ **era-norm tolerated → VQ-1 通過**
- RI-01: 単一点 EA・定性的気体報告・診断反応の未定量は 1970 年 communication
  の慣行内。→ **era-norm tolerated → VQ-2 通過**
- RI-07: "stable only in chlorobenzene" の定性的安定性報告は communication 形式での
  観察記録として 1970 年代慣行内。→ **era-norm tolerated → VQ-2 通過**
- RI-03: C–Cl 活性化機構の論議欠如は 2 頁 communication として era-norm tolerated
  （機構主張は本論文のスコープ外として明示的に延期）。→ **era-norm tolerated**
- RI-06: 類縁化合物との構造的比較欠如は communication 形式慣行内。→ era-norm tolerated

→ **Layer 1: VQ-2 (era-norm qualified)**

**Layer 2（触媒的意義）:**
本論文内に触媒性能の観察証拠が皆無（A-1: 全数値データを別論文に委譲）。
RI-09 拡張（split-presentation 変形）を適用:「Paper II が予告のみ・未刊の場合 →
Paper I 単独で VQ-2 (Method) 上限」との規定に基づき、Layer 2 は VQ-1 も達成せず。
→ **Layer 2: VQ-1 not reached**（split-presentation; RI-09 注記: "数値ベンチマーク委譲"）

**Step 3c: Final VQ judgment**

```
現在判定: VQ-2 (era-norm qualified) [Layer 1 合成・キャラクタリゼーション]
```

- **VQ-1 (Observation):** era-norm qualified — RI-02 は 1970 年 communication 慣行で
  era-norm tolerated（EA + 診断反応が当時の最小同定セット）。現代基準では未達。
- **VQ-2 (Method):** era-norm qualified（VQ-1 era-norm inheritance を前提）— RI-01 および
  RI-07 はいずれも communication 形式慣行内で era-norm tolerated。
  ただし modern baseline では VQ-1 が未達であるため VQ-2 も未達。
- **VQ-3 (Mechanism):** not reached — RI-03（C–Cl 活性化機構の完全未観測）が
  communication 形式で延期されたとしても、致命的欠落として残存。
- **VQ-4 (Benchmark):** not reached

**Layer 別 VQ 非対称性（§1 Layered structure との対応）:**
- Layer 1（合成・同定）単独では: **VQ-2 (era-norm qualified)**
- Layer 2（触媒的意義）単独では: **VQ-1 not reached**
  Layer 2 は split-presentation 構造（Paper II = 脚注予告の別報告に依存）のため、
  この論文単体での VQ 評価は VQ-1 に達しない。

---

### §4 Era-Norm Annotation

**communication-era tolerated（1970年、J. Organomet. Chem.、Preliminary communication）:**

- **B-1（IR/NMR/UV-Vis 不在）:** 1970 年の JOC 2 頁 communication において有機金属錯体に
  スペクトルデータを要求するのは標準慣行ではなく、EA + 化学反応が characterization
  として受理されていた（ただし IR はすでに利用可能であった点を modern-era deficient
  に記録する）。
- **B-2（気体生成比 未定量）:** GC 定量的気体分析は 1970 年に emerging であり、
  "gas evolved" の定性記述が preliminary communication では許容されていた。
- **B-5（質量収支の不記載）:** 60% 収率の報告のみで残余の帰属を論じないことは、
  synthesis communication のスタイルとして 1970 年代には慣行内。
- **B-7（診断的反応の未定量）:** "stoichiometric quantities" という叙述で化学反応の
  結果を定性的に記述することは、Ni–C 結合の診断証明として当時の communication に
  おいて認められていた形式。
- **B-10（Fajans 法の検証なし）:** 無機 Cl 分析の標準法として Fajans 法は受入れられており、
  独立校正なしに報告することは 1970 年代 communication 慣行内。
- **B-11（再結晶時の熱安定性チェックなし）:** 合成条件の熱的妥当性を DSC/TGA で
  確認することは 1970 年 communication では要求されていなかった。
- **A-1（触媒データ全体の別報告外置き）:** Preliminary communication が詳細データを
  Full Paper に委譲する構造は 1970 年代 JOC で広く認められた慣行であり、Layer 2
  全体の数値省略は format に起因する正当な延期。

**modern-era deficient（現代の再認定では許容できない欠落）:**

- **B-1 → RI-02（スペクトル不在）[**致命的**]:** 現代の有機金属化学では¹H NMR + ¹³C NMR +
  IR（少なくとも ν(Ni–C) 領域）が新規 Ni 錯体の最小同定要件。単結晶 X 線回折が
  「strong recommendation」水準。IR は 1960 年に Chatt–Shaw が類縁 Pd 錯体に適用
  しており（Chatt & Shaw 1960 = Ref 6）、1970 年時点で利用可能であったにもかかわらず
  communication 形式として省略されたことは、「技術的未整備」ではなく「形式的慣行による
  省略」と評価すべき点で重要（era-norm tolerated と modern-era deficient の**両方**に
  該当する境界事例）。
- **U-2 → RI-03（C–Cl 活性化機構の完全不在）[致命的]:** 現代では、C–Cl 酸化的付加
  かラジカル連鎖かを区別する kinetics / EPR / DFT 計算のいずれかが
  mechanism 論文の最低要件。この種の問いを完全未処理のまま発表することは
  現代基準では VQ-3 達成不可。
- **A-1 + B-9 → RI-05（"highly active" 無根拠）[致命的]:** 現代の触媒 communication では
  少なくとも 1 基質での TON か反応速度定数の初期推定値が必須。完全数値不在での
  "highly active" 主張は non-falsifiable qualitative claim として許容されない。
- **B-10 → RI-08（Fajans 法未校正）:** 現代の分析化学基準では無機 Cl 分析に
  認定参照物質での校正 + 繰り返し測定（n ≥ 3）+ 不確かさ表記が必要。
- **B-8 + SRG-5 → RI-06（配位子選択の比較なし）:** 現代の配位化学論文では
  配位子効果を議論する際に少なくとも 1 種の比較化合物（異なる N ドナー配位子）
  との電子的・安定性比較が期待される。

**両タグ重複（era-norm tolerated かつ modern-era deficient）:**
- **B-1（IR 不在）:** 上述のとおり、1960 年以降 IR は利用可能であったが
  communication 慣行として省略された。当時は tolerated、現代では deficient。
  Era-norm annotation の重要境界事例として記録する。

---

### §5 最短補強ルート

**目的関数 1: VQ-2 (achieved) — 現代 baseline での方法論水準確立**

現在: VQ-2 (era-norm qualified) → 目標: VQ-2 (achieved, modern baseline)

VQ-2 達成のためには VQ-1 継承（RI-02 現代解消）+ RI-01 + RI-07 解消が必要。

1. **EP-02a Identity / purity substantiation pack** —
   単結晶 X 線回折で compound II の結合様式（Ni–C(Ph) 距離, dipy キレート角,
   ½ ClBenzene 格子位置）を確定; ¹H NMR・IR を追加。
   → **RI-02 前進（VQ-1 確立）**。情報利得最大。

2. **EP-08a Replication / uncertainty pack** —
   Triplicate EA + TGA による ½ 溶媒和物組成確認; Fajans 法の参照校正。
   → **RI-08 + RI-01 前進**（EA 信頼性と analytcial 一貫性確立）。

3. **EP-01a Reporting-coherence pack** —
   GC による n-ブタン/エタン/エチレン定量（モル比 + 質量収支）;
   診断的反応の定量的収率報告（PhH, トルエン, PhH の GC 定量）。
   → **RI-01 前進**（reporting integrity 確立）。

4. **EP-07a Boundary-test pack** —
   各溶媒中での分解速度定数（UV-Vis）; "stable only in chlorobenzene" 境界を
   定量化; 安定溶媒の構造要件特定。
   → **RI-07 前進**（unsupported boundary 解消）。

**目的関数 2: VQ-3 (achieved) — 機構水準への昇格**

目標: VQ-3。VQ-2 が前提（目的関数 1 達成後）。

5. **EP-10a Kinetic verification pack** —
   I + PhCl の初期速度論（[I] および [PhCl] 各依存性）; 置換 PhCl での
   Hammett 相関（σ 定数 vs log k）; TEMPO 捕捉によるラジカル中間体検証;
   H/D 同位体効果（ArCl vs d₅-PhCl）。
   → **RI-03 + RI-04 同時前進**（EP-10a の高情報利得）。PRI-11 候補排除にも有効。

6. **EP-03a Direct-observation / state-assignment pack** —
   反応混合物の EPR 測定（Ni(I)・Ni(III) 中間体の g 値・超微細構造）;
   低温 UV-Vis 時間分解スペクトル（中間体検出）; 磁気感受率。
   → **RI-03 前進**（Ni 酸化状態軌跡の直接観測）。

7. **EP-06a Analogy-validation pack** —
   Compound II vs Ph(Et₃P)₂NiCl の安定性・分解速度・IR バンドの直接比較。
   → **RI-06 前進**（SRG-5 の Chatt–Shaw/Miller 類推の同型性実証）。

**目的関数 3: VQ-4 (achieved) — ベンチマーク水準 + Layer 2 確立**

目標: VQ-4。VQ-3 が前提。

8. **EP-05a Quantitative-ranking substantiation pack** —
   Compound II + AlR₂X の TON/TOF（複数基質、複数条件）; selectivity プロファイル;
   Compound I + AlR₂X との直接比較（同一 Al/Ni 比・T・P）。
   → **RI-05 + RI-09 前進**（Layer 2 の観察基盤確立）。

9. **EP-09a Internal benchmark pack** —
   I vs II の活性差を定量的に比較 + Cl⁻ 塩（[Me₄N]Cl）添加対照実験。
   → **RI-09 前進**（内部ベンチマークの確立）; U-3（因果連鎖）の検証。

```
認定ゲート順注記: 実験投入の情報利得順（EP-02a → EP-08a → EP-01a → EP-07a →
EP-10a → EP-03a → EP-06a → EP-05a → EP-09a）と最終 VQ 認定の継承ゲート順
（VQ-1 → VQ-2 → VQ-3 → VQ-4）は別個である。EP-10a（機構: VQ-3）を投入しても
VQ-2 が現代 baseline で確立されていなければ VQ-3 認定はなされない。
```

---

### §6 制度設計への寄与

**1. Split-presentation 構造の典型事例登録（RI-09 拡張適用）**

本論文は「RI-09 split-presentation 変形」（VQ 非対称性パターン）の典型事例を
提供する。Layer 1（合成・同定）が VQ-2 (era-norm qualified) を達成する一方で、
Layer 2（触媒的意義）が VQ-1 not reached のまま "highly active" と主張される構造は、
「Paper I の定式化 + Paper II に実証委譲」という split-presentation の
有機金属合成 communication 版として記録できる。
→ **EP 辞書 EP-09a Case-specific 実装の拡張事例**:
「catalytic activity comparison を companion paper に委譲した case」として
EP-09a の実装例に追加する。

**2. 通信→Full Paper 遷移の自動解消パターンの確認**

B-1（IR/NMR）、B-2（気体定量）、B-5（質量収支）、B-7（診断反応定量）、
B-10（Fajans 校正）はすべて、予告された companion paper（"Details…will be
published separately"）で自動解消される形式的欠落として分類できる。
この「形式的・一時的欠落」群と「構造的・本質的欠落」群（U-2: 機構不在 / U-3: 因果連鎖
未検証）の峻別が Stage 3 分析の重要機能として再確認された。
→ **既存制度設計の確認**（新規 PRI 提案なし）。

**3. 標識不整合（Labeling mismatch）の検出**

「which generates a highly active dimerization catalyst for α-olefins」という
事実的叙述語（generates = 現在形、確定的）がタイトルおよび本文の中心主張に
使用されているが、その根拠は脚注で完全に別報告へ委譲されている。Layer 2 の
主張が仮説的・予告的性格を持つにもかかわらず、事実的記述語でタイトルレベルに
格上げされている。脚注（末尾注）という位置への仮説標識集約パターンとして記録。
この仮説標識位置化は RI-05 と連動する: 事実的言語が定性評価（"highly active"）
の非反証可能性を強化している。
→ **Labeling mismatch pattern の新事例**（タイトルレベルの factual 語 + 脚注委譲型）。

**4. Era-norm inflection point: "技術的利用可能性" vs "形式的慣行省略" の弁別**

IR 分光は 1960 年時点で Chatt–Shaw が類縁 Pd–aryl 錯体に適用済み（Ref 6）であり、
1970 年の本論文では技術的に「利用可能」であった。にもかかわらず IR データが不在な
のは「技術が未整備だから」ではなく「2 頁 communication 形式の慣行として省略が
normとなっていたから」である。この区別は Era-norm annotation の精度に影響する:
- タイプ A（技術的未整備）: 当時は era-norm tolerated かつ現代基準では非適用
- タイプ B（形式的慣行省略）: 当時は era-norm tolerated だが技術的には実施可能
  → modern-era deficient と **両タグ付け** すべき境界事例
本論文の B-1（IR 不在）は タイプ B として初めて明示的に記録される代表事例となる。
→ **Era-norm annotation codebook への新ガイドライン候補**: era-norm tolerated の
分類に「技術的未整備 vs 形式的慣行省略」の sub-tag を追加することを §4 運用への
拡張として提案する。

**5. EP-10a 適用範囲の確認的拡張**

EP-10a（Kinetic verification pack）は Kumada 1972 / Breitenfeld 2014 / Mazet 2021 /
Pengfei 2024 等の「触媒サイクルを持つ論文」で確立されてきたが、本論文では
「触媒サイクルを提案しない単一ステップ C–Cl 活性化反応」（D-4-1: SRG-1）に
適用されている。C–Cl 結合の activating agent が Ni(0) でも Ni(I)/Ni(III) でも
ラジカルでも σ-bond metathesis でも、各メカニズムから異なる速度式が導出可能
であり、EP-10a の速度論的検証セット（反応次数、同位体効果、ラジカル捕捉等）が
直接適用できる。
→ **EP-10a の Case-specific 実装例に「触媒サイクルなし・単一ステップ C–X 活性化」
を追加**。適用条件の注記: "C–X 活性化の提案を含む合成 communication にも EP-10a
は適用可能。触媒サイクルの存在は前提条件ではない。"

**6. RI-02 ↔ RI-03 共起パターン（SRG-4 × SRG-1）の複合不確かさ構造**

Compound II の構造同定が未確定（RI-02, SRG-4）のまま C–Cl 活性化機構
（RI-03, SRG-1）が問われるとき、複合的認識論的不確かさが生まれる:
「機構が解明されても、それは未確定構造の compound II に帰属されうる」という
先順序問題。EP 投入順序が重要で、EP-02a（構造確定）が EP-10a（機構解明）に
論理的に先行する必要がある（§5 の投入順序設計はこれを反映している）。
→ **既存制度設計の確認（RI 共起パターン）**。SRG 間にまたがる共起では
EP 投入の論理的先後関係を §5 で明示することが有効と再確認。

**総括:**
本論文の分析は制度設計に対して: (1) split-presentation pattern の有機金属 synthesis
communication 事例を提供し、(2) era-norm annotation の "タイプ B（形式的慣行省略）"
境界ガイドラインを提案し、(3) EP-10a の適用範囲を触媒サイクルなし C–X 活性化反応へ
拡張し、(4) Labeling mismatch のタイトルレベル版を記録した。新規 PRI 候補は検出
されなかった。

inference_time_sec: not available — inject externally
```
