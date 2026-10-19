prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Zhang et al. 2017（Chemical Science, Edge Article）

### §1 Claim Architecture

**コア主張の要約：**

Novelty柱は四層からなる独立構造を持つ。(1) 三置換アリルアルケノールを基質とした初の不斉 redox-relay Heck アルケニル化反応の開発——先行する Sigman 自身の研究（refs 2a–f）は単一ステレオセンターしか設定できず、syn-carbopalladation の潜在力が未実現だった。(2) 高 er（≥90:10）・高 dr（>20:1）での隣接ステレオセンターの同時構築という合成的達成。(3) 塩基性条件下でのエピ化なし——enolizable α-カルボニル位ステレオセンターの保持が独立した売り文句として Abstract と Conclusions の両方に記載されている。(4) E-/Z-アルケノール間の選択性差の計算化学的機構解明——選択性の起源が既報基質と質的に異なることを DFT で示した。Utility 柱は 25 種以上の基質スコープと天然物誘導体トリフラート（nootkatone, estrone, cholesterol）への適用。

**Layered structure：**

四層の主張は論理的に独立している。合成的達成（er・dr・収率）の層は実験測定値のみに依存し、計算機構層の反証では崩れない。エピ化抵抗性の層は合成的達成層と独立だが、時間推移データが存在せず確認できていない（U-3）。計算機構層は DFT 方法論の妥当性に依存し、合成的主張とは切り離して反証可能。スコープ層は個別の基質実験に依存する。「単一の反証で全主張が崩れる」構造ではない。最も堅牢な層は合成的達成（er・dr・収率は直接測定値）、最も脆弱な層は計算機構（RI-03 + RI-06 双方に抵触）とエピ化抵抗性（RI-03 + RI-04）である。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [触媒サイクルの実験的根拠の不在]**

* **Primary RI**: RI-03 [Unobserved explanatory] — β-水素化物脱離/再挿入リレーの中核を担う中間体 5, 6, 7（特に PdとOHが同一炭素に結合する「ユニーク」な中間体 7）が直接観測・トラッピングされておらず、速度論的適格性も未検証。
* **Secondary RI**: PRI-11 [Mechanism-kinetics decoupling] — 提案触媒サイクルから速度式を代数的に導出せずに、生成物構造と er のみで機構を支持している。
* **ER**: β-HE/再挿入リレーの存在を支持するためには、化学量論的 Pd–PyrOx 反応での中間体観測（低温 NMR またはX線結晶構造）、もしくは KIE を用いた β-HE と E2 型脱離の速度論的弁別が必要。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific 実装**: (a) Pd₂dba₃/2-t-BuPyrOx と 1 当量のアルケノール 2a およびアルケニルトリフラート 1a を低温（−40 ℃, CD₂Cl₂）で混合し、¹H/³¹P NMR で中間体種を観測・帰属する。(b) d₁-アルケノール（OD 標識）を用いた KIE 実験で β-HE（KIE 非依存）と E2 型（KIE 依存）を区別する。(c) Table 1 entries 7–8 の NEt₃/Li₂CO₃ ベース効果を機構的弁別に再活用——強塩基阻害が E2 経路の選択的阻害に相当するか速度論的に確認する。
* **注記**: B-14（V2=high, 1/3 収束）, B-15（V2=high, 1/3 収束）, U-2（self-contradictory absence, severity=high）, B-10（V1=medium, V2=high; 2/3 収束, gap=low）, U-4（self-contradictory absence, severity=medium）。TEMPERATURE_SUMMARY では B-10 が high_convergence_low_gap。本 SRG は最多の A/B/U 項目を包括し、機構的主張の根幹に関わる。PRI-11 の追加確認事例（→§6 参照）。

---

**SRG-2 [DFT 計算方法論の不完全な報告]**

* **Primary RI**: RI-06 [Imported model] — 気相計算（溶媒和モデルなし）をカチオン性 Pd 中間体の溶液相不斉選択性に直接適用しており、気相モデルと溶液相との同型性が実証されていない。カチオン性 Pd 錯体の遷移状態では溶媒配位および静電安定化が ΔΔG‡ に有意に寄与しうる。
* **Secondary RI**: RI-01 [Reporting integrity] — コンフォーマー探索プロトコルが完全に省略されており（全 3 エージェント収束: B-16 3/3）、使用した熱化学補正の種類（ZPE+thermal+TΔS か否か）が明記されていない（B-17: V3=high）。
* **ER**: カチオン性 Pd–PyrOx 錯体の溶液相選択性を計算化学的に支持するためには、暗黙的溶媒和モデル（SMD または CPCM、ethyl pivalate 相当の誘電率）の適用、分散補正（D3BJ）の追加、および系統的コンフォーマー探索（CREST 等）による TS 同定の再現可能な記述が必要。
* **EP**: EP-06a [Analogy-validation pack]（RI-06）; EP-01a [Reporting-coherence pack]（RI-01）
* **Case-specific 実装**: M06-L/def2-TZVP-D3(BJ)/SMD（溶媒 = ethyl pivalate 近似, ε ≈ 4.2）で TSA^S, TSA^R, TSB^S, TSB^R を再計算; CREST/xTB によるコンフォーマーサンプリングを明示; 補正後 ΔΔG‡ と実験値（E-体: 1.74 kcal/mol、Z-体: 0.17 kcal/mol）との再比較。
* **注記**: B-16（3/3 収束, gap=low）, B-17（V2=medium, V3=high; 2/3 収束, gap=low）。TEMPERATURE_SUMMARY で B-16, B-17 ともに high_convergence_low_gap。RI-06 と RI-03（SRG-1）が異なる SRG で共起しており、気相モデル補正のみでは VQ-3 は達成されない（→§6 参照）。

---

**SRG-3 [スコープエントリの定量的実験検証の不在]**

* **Primary RI**: RI-08 [Unquantified reliability] — 25 種以上の基質について反復実験データ・標準偏差が一切報告されておらず、特に低収率基質（3k: 19%, 3p: 22%, 3y: 26%）では run-to-run 変動が収率値に匹敵する可能性がある。
* **Secondary RI**: RI-05 [Qualitative overread] — 19%, 22%, 26% の低収率結果が「官能基許容性の証明」として定量的根拠なしに肯定的にフレーミングされている（B-5）。
* **ER**: スコープテーブルの信頼性を確立するためには、少なくとも代表的な高収率基質（3a, 3d）および低収率基質（3k, 3p, 3y）での 3 連実験と平均±標準偏差の報告、および低収率基質での質量収支（回収基質・副生成物）の記述が必要。
* **EP**: EP-08a [Replication / uncertainty pack]; EP-05a [Quantitative-ranking substantiation pack]（RI-05 補助）
* **Case-specific 実装**: 3k（TMS 基, 19%）、3p（2-Br-トリフラート, 22%）、3y（コレステロール誘導体, 26%）について各 3 回の独立した反応を実施し、回収基質・副生成物・触媒を定量化してマスバランスを閉じる; 低収率の原因（基質消費か触媒失活か副生成物生成か）をGC/HPLC で特定する。
* **注記**: B-3（V1=medium, V3=medium; 2/3 収束, gap=none）, B-4（V1=medium, 1/3 収束）, B-22（V3=medium, 1/3 収束）。RI-08 は Era-norm 依存性が高く（§4 参照）、VQ-4 要件に属する。

---

**SRG-4 [E/Z 反応性の機構的解釈の実験的根拠の不在]**

* **Primary RI**: RI-04 [Unreplicated discriminator] — (E)-トリフラート 1t からの混合 E/Z 生成物とそれぞれの er（97:3, 91:9）という単一の実験的観測から、トリフラート異性化という機構的結論を引き出している。代替説明（生成物アルケンの触媒的 E/Z 異性化、または競合的配位子交換による二経路の同時進行）が排除されていない。
* **Secondary RI**: RI-03 [Unobserved explanatory] — Z-トリフラートが反応中に実際に生成されているという直接証拠（NMR モニタリング）がなく、the proposed isomerization は er 一致のみに依拠する。
* **ER**: トリフラート異性化仮説を支持するためには、(E)-トリフラート 1t の反応混合物を ¹⁹F NMR で時間追跡し Z-体トリフラートの蓄積を直接確認する実験、または触媒なし条件での 1t の異性化速度測定が必要。
* **EP**: EP-04a [Discrimination / replication pack]
* **Case-specific 実装**: (E)-トリフラート 1t を触媒量の Pd₂dba₃/Li₂CO₃/ethyl pivalate に曝露し、基質転化率が 10% 以下の時点でアリコートを取り ¹⁹F NMR（またはLC-MS）で Z-体の直接検出を試みる; 別途、触媒・塩基・溶媒のみ（アルケノール不在）での 1t の安定性確認実験を実施する。
* **注記**: B-9（V1=high, V2=high; 2/3 収束, gap=none）, U-1（self-contradictory absence, severity=high）, B-19（V2=medium, 1/3 収束）。TEMPERATURE_SUMMARY で B-9 は high_convergence_low_gap。U-1 の self-contradictory absence が優先度を高めている。

---

**SRG-5 [NBO 電荷–er 相関のモデル転用]**

* **Primary RI**: RI-06 [Imported model] — 酵素触媒の溶媒依存性研究（MacManus/Vulfson 1997）と溶媒極性指標の総説（Reichardt 1979）を支持文献として使用しており、Pd 触媒の不斉反応への適用可能性が実証されていない。気相 NBO 電荷と溶液相での Pd–溶媒相互作用の関係は非自明である。
* **Secondary RI**: RI-01 [Reporting integrity] — NBO 相関の定量的パラメータ（R², slope, 溶媒数, 溶媒リスト）が主文から完全に省略され ESI に委譲されており、主文中で相関の統計的品質を評価できない。
* **ER**: NBO 電荷–er 相関を物理化学的に有意義とするためには、相関の R² と統計的有意性（p 値）、使用溶媒の完全リスト、溶媒が Pd 配位圏に与える効果（DFT での溶媒–Pd 相互作用エネルギー、または ¹H NMR 化学シフトへの影響）の記述が必要。
* **EP**: EP-06a [Analogy-validation pack]（RI-06）; EP-01a [Reporting-coherence pack]（RI-01）
* **Case-specific 実装**: 気相 NBO 電荷ではなく DFT 計算での溶媒–Pd 相互作用エネルギー（M06-L/def2-TZVP, BSSE 補正、選択的配位構造を探索）を計算し、経験的 NBO 相関が配位性の代理指標として機能するかを検証する; 非エステル溶媒（ニトリル系、エーテル系）での er 測定値を追加して相関式の外挿適用範囲を確認する。
* **注記**: B-7（3/3 収束, gap=none; TEMPERATURE_SUMMARY で high_convergence_low_gap 最優先候補の一つ）, C-4（非類似引用, severed）。SRG-5 は B-7 の 3/3 収束により D-4 選定で最初に到達した high_convergence_low_gap 項目の一つ。

---

**SRG-6 [選択性制御の動力学的・熱力学的根拠の不在]**

* **Primary RI**: RI-04 [Unreplicated discriminator] — 「エピ化なし」の主張が最終単離生成物の er 値のみに依拠しており、反応進行中の er 安定性（時間推移）は未検証。Abstract と Conclusions 双方への記載にもかかわらず直接的な動力学的証拠がない。
* **Secondary RI**: RI-03 [Unobserved explanatory] — er 時間推移データが存在せず、Li₂CO₃/EtPiv 条件下での α-カルボニル位立体中心の熱力学的安定性も未評価。
* **ER**: 「エピ化なし」の主張を確立するためには、反応時間の 2 倍以上の撹拌後（または反応完了後の追加撹拌）での er と初期 er の比較、または単離生成物の反応条件下でのラセミ化速度測定（半減期の推定）が必要。
* **EP**: EP-04a [Discrimination / replication pack]
* **Case-specific 実装**: 最適化条件（Pd₂dba₃/2-t-BuPyrOx/Li₂CO₃/ethyl pivalate, rt）下で基質 3a を反応させ、30 分・2 時間・24 時間・48 時間の各時点でアリコートを取り SFC 分析して er を追跡する; 別途、単離した 3a を同一塩基・溶媒中（触媒なし）で 24 時間撹拌後の er を測定してエピ化の「熱力学的上限」を確認する。
* **注記**: U-3（self-contradictory absence, severity=medium）, B-18（V2=medium, 1/3 収束）。U-3 は Abstract と Conclusions 双方に登場する中心的主張に直接関係し、影響範囲が大きい。

---

**SRG 外：CLA**

全 U 項目（U-1, U-2, U-3, U-4）は既存 SRG に包摂済み。D-4 候補 8（合成的文脈の不在: B-12, A-1）はいずれのSRG の member_items にも属さないが、D-1 の四つの主要主張（方法論・エピ化・スコープ・計算）の成否に直接関わらないため CLA 登録しない。自己矛盾的不在で未収載のものはない。

---

### §3 現在の VQ 判定

**現在判定: VQ-2 (Method)**

**VQ-1 [Observation] は通る。**
RI-02（Object identification）: 生成物の構造は NMR/HRMS（ESI 参照）で同定されており、代替候補構造を排除できる粒度が確保されている。絶対配置については 3d の ECD（(2S,3S) 確定）+ 類推割り当て（B-23）が存在し、3d については要件を充足。他の 25 化合物については構造的類似性による類推（B-23）が完全な独立検証ではないが、主要合成産物の同定水準では Non-fatal と判断する。VQ-1 は通過（B-23 を Non-fatal として記録）。

**VQ-2 [Method] は通る（VQ-1 継承を前提）。**
RI-01（Reporting integrity）: スコープテーブル（Tables 1–4）の収率・dr・er は統一された形式で全エントリに一貫して報告されており、主要な合成的主張の横比較は可能。B-7（NBO 相関パラメータのESI委譲）と B-17（熱化学補正種類未明）は RI-01 に該当するが、いずれも主たる合成的主張の横比較を妨げない——Non-fatal。
RI-07（Unsupported boundary）: 「エピ化なし」は U-3 により time-course データが欠如しているが、RI-07 の「失敗例なしに限界を主張」という定義には直接該当しない（エピ化の「失敗例」ではなく「不在の動的証拠」の問題）。低収率基質（3k, 3p, 3y）は実際に試験されており、RI-07 の肯定的境界主張は部分的に根拠を持つ。Non-fatal として通過。
VQ-2 は通過（RI-01, RI-07 を非致命的として記録）。

**VQ-3 [Mechanism] は未達。**
RI-03（Unobserved explanatory）: SRG-1（中間体 5/6/7 の非観測——β-HE/再挿入リレーの直接証拠なし）、SRG-4（Z-トリフラートの非観測）、SRG-6（er 時間推移なし）の三箇所で残存。特に SRG-1 は論文の中心的機構主張（β-HE/再挿入リレー）を支える種が直接観測されていない点で **Fatal**。
RI-06（Imported model）: SRG-2（気相 DFT の溶液相転用）、SRG-5（酵素/溶媒極性モデルの Pd 触媒転用）の二箇所で残存。SRG-2 は計算による選択性説明の根拠を直接損なうため **Fatal**。
RI-04（Unreplicated discriminator）: SRG-4（トリフラート異性化の er 一致のみ）、SRG-6（エピ化なしの最終 er のみ）で残存——機構の各個別主張を限定するが合成的達成層を根底から覆さないため **Non-fatal**（合成主張の観点で）。
RI-05（Qualitative overread）: SRG-3（低収率基質の「許容性の証拠」フレーミング）——Non-fatal（定性的フレーミングの問題）。
VQ-3 は未達（RI-03 と RI-06 が Fatal）。

**VQ-4 [Benchmark] は継承原則により VQ-3 未達のため未評価。**
RI-08（SRG-3: 反復測定なし）、RI-09（C-1/C-2: 定量的直接比較なし）が残存しており、VQ-3 達成後に評価される。

**層別 VQ 非対称性：**
ただし**合成的達成層**（er・dr・収率の実測値そのもの）単独では：各測定値は直接の実験観測値であり、RI-03/RI-04/RI-06 が扱う「機構の説明」は er・dr・yield の数値自体の成立を覆さない。この層は VQ-2 水準に到達している（RI-01 非致命的）。すなわち「この反応が機能する」という合成的事実は VQ-2 水準で成立しているが、「なぜ/どのように機能するか」という機構的説明は VQ-1 水準に留まる。

---

### §4 Era-Norm Annotation

**communication-era tolerated（2017 年, Chem. Sci., Edge Article 形式）：**

- B-3, B-4（低収率基質のマスバランス省略）— 合成コミュニケーション形式では収率と選択性が主要報告事項であり、マスバランス詳細は ESI またはフォローアップFull Paperへの委譲が 2017 年当時の標準慣行だった。
- B-22（反復実験データ・標準偏差なし）— 通信形式の単代表値報告は 2017 年当時許容範囲であり、全スコープへの 3 連実験は Edge Article の紙幅慣行ではなかった。
- B-23（ECD 絶対配置の類推による割り当て）— 2017 年当時の合成論文では 1 標品 + 類推による絶対配置割り当ては Chem. Sci. を含む主要誌で許容されていた。
- B-16, B-17（DFT 方法論の詳細の ESI 委譲）— 合成論文の計算セクションでは方法論詳細の ESI 委譲が 2017 年当時の標準であり、TS 座標は ESI 掲載が通例だった。
- B-21（SFC/HPLC 条件の省略）— 分析条件の詳細は 2017 年当時の合成通信では主文に必須とされていなかった。

**modern-era deficient（現代の再認定では許容できない欠落）：**

- B-7（NBO 電荷–er 相関の定量パラメータの主文からの完全省略）— 現代では統計的相関を主張するには主文中での R²、p 値、使用溶媒数の開示が必要であり、ESI 委譲のみでは統計的品質の評価が不可能。
- B-16（コンフォーマー探索プロトコルの完全な欠如）— 現代の計算化学では再現性のために CREST や MD+minimization によるコンフォーマーサンプリングの記述が再現性要件として必須となっており、最低エネルギー TS のみの報告は不十分。
- B-17（熱化学補正種類の未明示）— 現代では計算された「free energy」が ΔE/ΔH/ΔG のいずれかを明示し、ZPE+thermal の適用有無を記述することが再現性要件として求められる。特に 0.7 kcal/mol という境界値では補正の種類が結論を左右しうる。
- U-3（「エピ化なし」主張の時間推移データなし）— 現代の再認定水準では Abstract と Conclusions の両方に登場する中心的主張への「観察されなかった」記述に er 時間安定性の直接確認なしには不十分——少なくとも代表基質での er 時間追跡実験が期待される。
- C-1, C-2（定量的ベンチマーク比較の欠如）— 現代の Nat. Chem.・JACS・ACS Cent. Sci. 水準では先行類似反応との数値比較が明示的に求められており、引用のみの定性的位置づけは不十分。

**両タグ（当時は許容されたが現代では不足）：**

- B-14, B-15, U-2（触媒サイクル中間体の非観測）— 2017 年当時の合成方法論通信として許容されたが、現代の Nat. Chem.・JACS 水準では少なくとも化学量論的実験または速度論データによる機構支持が期待される。ERA の変化としてVQ-3 達成の必要性が高まっている。

---

### §5 最短補強ルート

**VQ-3 への最短ルート：**

現在 VQ-2 → 第一目的関数: VQ-3。Fatal 要件: RI-03（SRG-1, SRG-4, SRG-6）と RI-06（SRG-2, SRG-5）の解消。

1. **EP-03a [Direct-observation / state-assignment pack]** — Pd₂dba₃/2-t-BuPyrOx 系でのアルケノール 2a とトリフラート 1a の化学量論的反応（−40 ℃, CD₂Cl₂）を NMR でモニタリングし、中間体 5/6/7 に相当する Pd–アルキル種を観測・帰属する; d₁-アルケノールでの KIE を用いて β-HE vs E2 を速度論的に弁別する。**RI-03 (SRG-1) を前進。SRG-1 が最多の A/B/U 項目（5 項目）を含み Fatal 判定のため最優先。**

2. **EP-04a [Discrimination / replication pack]** — (E)-トリフラート 1t の反応中に ¹⁹F NMR で Z-体トリフラートを直接検出（SRG-4）; er 時間推移実験（0.5, 2, 24, 48 h 時点で SFC サンプリング）により「エピ化なし」の動的安定性を実証（SRG-6）。**RI-03 (SRG-4, SRG-6) と RI-04 (SRG-4, SRG-6) を前進。2 つの SRG を同時に前進させる情報利得が高い。**

3. **EP-06a [Analogy-validation pack]** — M06-L/def2-TZVP-D3(BJ)/SMD（ε ≈ ethyl pivalate）で TS^{AS}, TS^{AR}, TS^{BS}, TS^{BR} を再計算; CREST によるコンフォーマー探索を明示; 補正後 ΔΔG‡ と実験値（E-体 1.74 kcal/mol、Z-体 0.17 kcal/mol）との再比較（SRG-2）。NBO 電荷と Pd–溶媒相互作用エネルギーの DFT 計算で SRG-5 の RI-06 を検証（SRG-5）。**RI-06 (SRG-2, SRG-5) と RI-01 (B-16, B-17) を前進。**

**VQ-4 への追加ルート（VQ-3 達成後、第二目的関数）：**

4. **EP-08a [Replication / uncertainty pack]** — 低収率代表基質（3k: 19%, 3p: 22%, 3y: 26%）各 3 連実験、yield 平均±SD 報告、質量収支（回収基質・副生成物）の定量。**RI-08 (SRG-3) を前進。**

5. **EP-09a [Internal benchmark pack]** — refs 3c–f（Yoo et al., J. Org. Chem. 2010, 75, 95; Org. Lett. 2007, 9, 3933）の er/yield 値を今回と同基質クラスに最も近い条件で抽出し数値比較表を作成; refs 8e–g（Trost JACS 2007; Liu-Stoltz JACS 2013）との隣接ステレオセンター合成の er 比較。**RI-09 (C-1, C-2) を前進。**

**認定ゲート順注記：** 実験投入は情報利得順（EP-03a → EP-04a → EP-06a → EP-08a → EP-09a）で設計されているが、最終的な VQ 認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 の継承原則に従い、下位水準の全要件を充足したことを確認した上で上位を認定する。

---

### §6 制度設計への寄与

**1. RI-03 サブタイプ「Available-but-unutilized characterization」の典型事例（SRG-1/U-4）：**

Table 1 entries 7–8（NEt₃ → trace, Li₂CO₃ → 74%）は機構弁別に活用可能なデータとして取得済みだが、β-HE vs E2 の弁別に一切使用されていない（U-4）。これは RI-03 の「取得済み実験データが機構的主張の検証に活用可能であるにもかかわらず未活用」サブタイプ（v0.2a 運用注記）の代表例として記録する。EP-03a の case-specific 実装においても、このデータの速度論的再解析が最も実行可能性の高い最初のステップとなる点で、このサブタイプの実用的価値を確認した。

**2. RI-06 × RI-03 共起パターンの構造的記述（SRG-2 × SRG-1）：**

DFT 計算（RI-06: 気相モデルの溶液相転用、SRG-2）と触媒サイクル中間体の非観測（RI-03: 提案サイクルの実験的未根拠、SRG-1）が異なる SRG で共起しており、いずれか一方の解消だけでは VQ-3 達成には不十分である。具体的には: SRG-2 の RI-06 を解消して溶媒和込み DFT を実施しても（計算の信頼性向上）、選択性決定ステップが実際に提案通りの migratory insertion step であることは実験的に確認されない（SRG-1 の RI-03 未解消）。この RI-06 × RI-03 共起は「計算化学的合理化」と「実験的機構検証」が独立した必要条件であることを示す制度的示唆を持ち、Codebook の「RI 共起パターン」として記録する。

**3. PRI-11（Mechanism-kinetics decoupling）の正式昇格を推奨する追加確認事例：**

SRG-1 は提案触媒サイクル（intermediates 4→5→6→7→3）から速度式を代数的に導出せずに、最終生成物の er・dr・収率のみで機構を支持するパターンを示す（B-14, B-15 との対応）。Breitenfeld 2014 での提案、Pengfei 2024 での確認に続く独立 2 報目以上の確認事例として機能し、**PRI-11 の Codebook 正式昇格に必要な条件を満たしていると判断する**。定義「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持している」は本ケースにも適用可能（速度次数データそのものが存在せず、よりラジカルな形の decoupling が起きている）。

**4. 標識不整合（Labeling mismatch）の記録（B-11 / Scheme 2）：**

[REDACTED: substantial verbatim quotation; see Tier 9]（Scheme 2）において、"confirms" という強い事実的記述語が使用されているが、証拠は単離生成物 3l の構造（α,β-不飽和ケトン）のみであり、中間体 8, 9, 10 は観測・トラッピングされていない（RI-04 との連動）。"is consistent with" または "supports the proposal that" が適切な仮説標識である。仮説標識は Main Text 冒頭（"Mechanistically, we propose the reaction initiates with..."）に形式的に集約されているが、Scheme 2 の直接記述では事実的語法が局所的に復活するパターンとして記録する。このパターンは RI-06 と連動する場合が多いという Codebook 注記と一致しており（本ケースでは RI-04 との連動）、適用範囲の拡張として記録する。

**5. 通信→Full Paper 遷移の自動解消パターンが機能しない事例（B-16, B-17）：**

B-16（DFT コンフォーマー探索プロトコルの欠如）と B-17（熱化学補正種類の未明示）は Full Paper 展開で自動解消されやすい RI-01/RI-06 項目だが、この communication に対応する Full Paper は発表されていない（series_signal=yes だが A-1 のフォローアップがホモアリル基質に向かっており、同一基質クラスの Full Paper 展開は未確認）。通信→Full Paper 遷移が起きない場合、これらの項目は永続的に未解消となる典型例として記録する。この「Full Paper 遷移なし」パターンは、§4 の communication-era tolerated 項目が Era-norm 変化後も未解消のまま残る経路の一つとして Codebook に追記すべきである。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
