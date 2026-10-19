```
prompt_version: stage3-v4-20260427
model_info: claude-sonnet-4-6
```

---

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

---

### §1 Claim Architecture

**コア主張の要約:**

本論文のコア主張は「ニッケル-ジホスフィン錯体を触媒とするグリニャール試薬と sp2 ハライドの選択的クロスカップリングという新規かつ実用的な合成法の確立」である。Novelty 柱は五重構造：(1) β-水素含有アルキルグリニャール試薬での高収率達成、(2) sp2 塩化物の高反応性（過去はほぼ臭化物・ヨウ化物使用）、(3) 二座ジホスフィン配位子の必要性とその序列、(4) ビニルハライドカップリングの非立体特異的・異常 cis 富化、(5) ジエチルエーテル溶媒の優位性。Utility 柱は「従来法では不利な選択性しか得られなかったグリニャール-ハライドカップリングを触媒的かつ高収率・高選択的に実現する」合成手法としての価値であり、具体的達成目標として11基質ペアで76〜98%の単離収率が示される。機構的「working hypothesis」（eqs 2–4）は主張の説明枠組みとして提示されるが、主たる主張の成否には直接関与しないと著者自身が留保している。

**Layered structure の判定:**

多層独立構造（yes）。D-1 layered_structure 判定と一致。主な独立層は以下の通り：

- **Layer 1（合成実用性層）**: Table I の 11 エントリー・76〜98% 収率・two detailed procedures。論文の primary claim であり、機構的解釈の正誤に左右されない。JACS communication 体裁での検証の中核。
- **Layer 2（機構仮説層）**: eqs 2–4 の Ni(0)/Ni(II) 触媒サイクル。著者自身が "working hypothesis" と明示し、[REDACTED: substantial verbatim quotation; see Tier 9] と断言しており、別層として明確に分離されている。Layer 1 の主張に論理的に独立。
- **Layer 3（配位子構造-活性相関層）**: 六錯体の活性序列と cis-幾何要件の推論（Feature 3）。単一基質ペアのデータから構築されており、Layer 1 の収率実証とも Layer 2 の機構仮説とも部分的に独立。

**「単一の反証で全主張が崩れるか」:** No。Layer 2（機構仮説）の反証—たとえば活性種が分子的 Ni 錯体でなく Ni ナノ粒子だと判明したとしても—Layer 1（合成実用性）は崩れない。Layer 1 は Table I データの実証性に立脚するため、機構的誤りとは原理的に独立に成立する。これが Kumada 1972 の構造的強靭性の根源である。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [GLPC収率定量基盤の検証不能性]**

* **Primary RI**: RI-01 [Reporting integrity] — 5件の GLPC 収率エントリー（98%, 95%, 89%, 95%, 80%）について、内部標準の同定・応答係数・校正方法が全く記述されず、横比較に必要な測定フレームが不統一である。
* **Secondary RI**: RI-08 [Unquantified reliability] — 反復測定データも不確かさ記述もなく、特に最高収率エントリー（EtMgBr/PhCl, 98%）の信頼性を独立評価できない。
* **ER**: GLPC 定量収率を主張するには、内部標準の同定・応答係数（校正値）・測定反復数・不確かさ範囲の記述が必要である。収率基準（限定試薬）の明示も要件。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: EtMgBr/PhCl（98%, GLPC）エントリーでの独立単離収率取得 + ドデカン等内部標準を用いた応答係数校正実験（FID 検出器）。GLPC 収率と単離収率の相関を 3 反応以上で確認し、相対標準偏差を報告。
* **注記**: B-2（reporting_omission: GLPC 内部標準不在）を直接反映。TEMPERATURE_SUMMARY high_convergence_low_gap（V1-Q1=high, V3-Q2=high; convergence=2/3）。v19 triggers C20/C21/C22/C25 は不発火（D-4 v19_trigger_status 参照）。

---

**SRG-2 [ビニルハライドカップリングの立体化学的異常と機構的説明責任]**

* **Primary RI**: RI-03 [Unobserved explanatory] — cis 富化の起源（vinyl-Ni 中間体の幾何、速度論的 vs. 熱力学的制御、ラジカル連鎖関与）が直接観測も速度論的拘束もされていない。"Anomalously" という語が暗示する参照予測すら論文内で導出されない。
* **Secondary RI**: RI-06 [Imported model] — eqs 2–4 の Ni(0)/Ni(II) サイクルは (dipy)Ni 系の文献類推から輸入されたモデルであり、dpe-Ni 系での立体化学的予測を生成できていない（同型性実証なし）。RI-05 [Qualitative overread] — 異常 cis 富化を "may offer a facile route to cis-stilbene" と利用可能性に転換する定性的解釈も残存。
* **ER**: ビニルハライドカップリングの非立体特異的・cis 富化を主張するには、cis/trans 比の測定方法（GLPC における異性体分離確認）・実験誤差・反復性の開示が要件。さらに提案機構から予測される立体化学的帰結の導出と、観測との突き合わせが必要。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-10a [Kinetic verification pack]
* **Case-specific実装**: cis- / trans-ClCH=CHCl それぞれについて (a) vinyl-Ni(dpe) 中間体の独立合成と立体化学的キャラクタリゼーション（NMR, X線）、(b) 反応温度を変えた速度論的制御 vs. 熱力学的制御の区別実験、(c) TEMPO 捕捉によるラジカル連鎖関与チェック、(d) 重水素標識 Grignard 試薬を用いたクロスオーバー実験。
* **注記**: A-2（deferred, convergence=3/3）, U-2（self-contradictory absence: high）, U-3（exotherm: high）を包含するSRG-2 全体を反映。

---

**SRG-3 [触媒サイクルの実験的検証基盤の全不在]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 提案 Ni(0)/Ni(II) サイクルの三つの中間体（1, 2, 3）は触媒条件下で直接観測も速度論的拘束もされていない。eq 3 が化学量論的副生物として予測する R-R（ホモカップリング生成物）は Table I の全エントリーで報告されない。
* **Secondary RI**: RI-06 [Imported model] — サイクル全体が (dipy)Ni 系文献類推から大規模に輸入されており、dpe-Ni 触媒条件下での同型性検証なし（RI-06 スコープ注記: サイクルレベル輸入に該当）。RI-02 [Object identification] — 「black mixture」（Example 1）の組成が未同定であり、活性種が均一系分子錯体か Ni ナノ粒子かが区別されていない（U-5）。
* **ER**: 触媒サイクルを提案するには、(a) 少なくとも一段階の中間体の独立合成・検出または速度論的拘束、(b) 主要副生物（R-R ホモカップリング）の定量または検出限界の明示、(c) 触媒活性種の同定（均一系か不均一系か）が要件である。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-10a [Kinetic verification pack]; EP-02a [Identity / purity substantiation pack]
* **Case-specific実装**: (a) [NiCl₂(dpe)] と過剰 RMgX の反応から中間体 1（L₂NiR₂）の独立合成と NMR キャラクタリゼーション（Ni(II) ジアルキル錯体）、(b) 触媒量条件下での R-R（ビフェニル、ジエチル、ジ-n-ブチル等）の GLPC 定量（各 Table I エントリーのマスバランス確認）、(c) Example 1 の黒色沈殿物のTEM/EDX 分析による Ni(0) vs. NiCl₂/MgCl₂ の識別。
* **注記**: A-3（deferred, convergence=2/3）, U-1（critical: R-R 自己予測矛盾）, U-5（high: 黒色混合物と分子機構の矛盾）を包含。TEMPERATURE_SUMMARY high_convergence_low_gap（A-3: V2-Q1/V2-Q9=critical）。

---

**SRG-4 [bidentate 配位子要件と β-H 許容の機構的根拠の不在]**

* **Primary RI**: RI-03 [Unobserved explanatory] — β-H 含有アルキルグリニャール試薬で β-脱離が抑制されるメカニズム（dpe 配位子の bite angle によるシン-ペリプラナー配座回避等）が、中間体観測も速度論的拘束もなく説明されない。配位子活性序列から cis-幾何要件を推論する論理の中核となる中間体 3 の構造も未同定。
* **Secondary RI**: RI-05 [Qualitative overread] — 一基質ペア（n-BuMgBr/PhCl）のみで確立された配位子活性序列から、全基質系に適用される「cis 幾何が第一要件」という構造的含意を定性的に導出（数値データなし）。RI-07 [Unsupported boundary] — "Only Csp2 halides can be used" という sp3 ハライド排除の境界を失敗実験エントリーなしに宣言（B-4）。
* **ER**: bidentate 配位子の β-H 脱離抑制効果を主張するには、β-H 脱離と還元的脱離の速度論的競合データ（速度定数比または活性化パラメータ差）と、dpe 配位子の bite angle が競合比に与える影響の定量化が要件。sp3 ハライドの排除には失敗実験の記述が要件。
* **EP**: EP-10a [Kinetic verification pack]; EP-07a [Boundary-test pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: (a) β-H 脱離速度 vs. 還元的脱離速度の競合実験（L₂Ni(n-Bu)(X) の加熱分解と Arrhenius 解析）、(b) bite angle の異なる dphosphine 系（dpe/dpp/dmpe/DPPP/BINAP）での二次・三次アルキルグリニャール試薬（i-PrMgBr, sec-BuMgBr）との反応性マトリクス、(c) sp3 ハライド（1-ブチルクロリド、シクロヘキシルクロリド）との失敗実験記録。
* **注記**: A-4（high_convergence_high_gap 最優先: V1=medium(2), V2=critical(4), V3=high(3); gap=2）、A-5（convergence=3/3）、B-4（sp2 scope 境界）を包含するSRG-4全体を反映。

---

**SRG-5 [収率基準の内部矛盾]**

* **Primary RI**: RI-01 [Reporting integrity] — Table I 脚注 d は単離収率をデフォルトと定めるが、Example 1（ハライド基準: 94%）と Example 2（グリニャール試薬基準: 80%）が異なる分母で収率を報告し、この逸脱が明示されない（U-4）。同一方法の比較評価を阻害する報告フレーム不整合。
* **Secondary RI**: RI-08 [Unquantified reliability] — 収率基準の非一貫性により、単離収率間の定量比較が不可能。
* **ER**: 収率はどのエントリーも同一の限定試薬を分母とした単一基準で報告し、基準を変える場合は明示的な注釈が要件。
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific実装**: Table I 11 エントリーの全収率を有機ハライド基準の単離収率に統一して再報告（または基準変更の明示的注釈付き再表示）。特に Example 2 の α-NpMgBr/CH₂=CHCl について、塩化ビニル基準での単離収率を取得・記録。
* **注記**: B-1（reporting_omission）, U-4（self-contradictory absence: high）を包含するSRG-5を反映。

---

**SRG-8 [先行技術との数値的比較の完全不在]**

* **Primary RI**: RI-09 [External superiority] — Kharasch-Reinmuth 型反応・Tamura-Kochi 鉄触媒系・(dipy)Ni 系モデル反応との収率・選択性の数値的対比を一件も提示せず、「seldom employed in synthetic practice due to homo coupling」「only for alkenyl halides」という比較を定性的先行技術批判として行う。
* **Secondary RI**: RI-07 [Unsupported boundary] — "definitely superior to tetrahydrofuran" という溶媒優位性の断定（Feature 5）は Table I 中に THF 条件エントリーを含まずに宣言（B-5）。
* **ER**: 先行技術系に対する改善主張には、同一基質ペアでの parallel comparison（収率・ホモカップリング比率の対比データ）が要件。溶媒比較主張には、同一基質での ether vs. THF の収率・選択性比較実験が要件。
* **EP**: EP-09a [Internal benchmark pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: (a) EtMgBr/PhCl または n-BuMgBr/PhCl で Tamura-Kochi 鉄触媒条件（THF, 0°C）と [NiCl₂(dpe)] 条件（ether）を並行実験し、収率・Ph-Ph ホモカップリング比を対比、(b) PhMgBr/PhCl または EtMgBr/PhCl で ether vs. THF の [NiCl₂(dpe)] 条件下収率比較。
* **注記**: C-1, C-2, C-5（先行技術引用群）とB-5（溶媒比較データ不在）を包含するSRG-8を反映。

---

**SRG外：CLA**

---

**CLA-1 [D-4-1: ホモカップリング生成物 R-R の自己予測矛盾]**

（SRG-3 に部分的に含まれるが、「自己矛盾的不在のCLAチェック」の典型事例として独立記録）

* **Primary RI**: RI-03 [Unobserved explanatory] — eq 3（L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R-R）は各触媒回転で R-R を化学量論的に副生すると予測するが、Table I 11エントリー・Examples 1/2 のいずれにも R-R の検出・定量記述がない。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — R-R 不在の観察が「選択性」主張の唯一の根拠として機能しているが、検出感度以下なのか実際にゼロなのかを区別する実験が未実施。
* **ER**: 「高選択性」という主要主張の実証には、ホモカップリング副生物の定量（または検出限界の明示）と、eq 3 の化学量論的含意との整合性説明が要件。
* **EP**: EP-04a [Discrimination / replication pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: 各 Table I エントリーの反応混合物からビフェニル（ArMgBr 系）、ジエチル（EtMgBr 系）、ジブチル（n-BuMgBr 系）等の R-R ホモカップリング生成物を GLPC で定量し、マスバランスを閉じる。特に PhMgBr/PhCl エントリーでは R-R = ビフェニルが検出容易。
* **注記**: U-1（critical severity）直接対応。SRG-3 の A-3/U-1/U-5 三元群のうち、eq 3 自己矛盾に特化した独立 CLA として記録。grounded_in: U-1, A-3, B-3。

---

**CLA-2 [D-4-5: 活性触媒種の同一性——均一系 vs. 不均一系]**

* **Primary RI**: RI-02 [Object identification] — "black mixture"（Example 1）の組成が未同定であり、活性触媒種が分子的 Ni(0)/Ni(II) 錯体か Ni ナノ粒子か区別されていない。「黒色」観察が提案された molecular mechanism と直接矛盾し得る。
* **Secondary RI**: RI-03 [Unobserved explanatory] — Ni ナノ粒子が真の活性種であれば配位子の役割は根本的に変わり、Feature (3) の配位子序列の機構的解釈が基盤を失う。
* **ER**: 均一系触媒反応として mechanism を提案するには、活性種の speciation（分子的か不均一系か）を最低限の特性評価（TEM、EDX または元素分析）で確認することが要件。
* **EP**: EP-02a [Identity / purity substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: Example 1 の黒色混合物のフィルタリング + TEM 観察（Ni ナノ粒子の存在・粒子径）+ EDX または ICP-OES による Ni 量定量。水銀ポイゾニング試験による不均一系触媒関与の評価（均一系なら水銀添加で活性変化なし）。
* **注記**: U-5（high severity）、B-6（reporting_omission）直接対応。grounded_in: U-5, B-6, A-3。SRG-3/SRG-7 と共通根。

---

**Self-referential validation チェック（v18 C8）:**

PRI-12 クラスター A への該当なし。本論文は計算量・記述子・スコア関数の提案論文ではなく、実験的な合成化学報告である。検証構造が自己参照的循環（検証指標と被検証対象の同一数学的依存）を持つ構造は見られない。

**Deductive-retrospective structure チェック（v18 C4）:**

PRI-12 クラスター B への部分的該当が検討されるが、適用閾値には達しない。提案された触媒サイクル（eqs 2–4）は演繹的導出ではなく文献類推（inductively grounded working hypothesis）として明示され、B2（Retrospective Confirmation Bias）の候補として挙げられる可能性があるが、著者自身が検証を明示的に将来に委ねており、「事後的文献一致を確認として提示する」構造は本論文の一次主張（Table I の合成実用性）を支持するものとしては機能していない。クラスター B の閾値（演繹的中心主張 + 遡及的事例一致による検証）には達しないと判断する。

---

### §3 現在のVQ判定

**Step 3a: Modern reassessment baseline**

**VQ-1（Observation）— RI-02 要件:**

RI-02 の充足を評価する。活性種の構造・純度の代替候補排除については、「black mixture」問題（CLA-2）が非致命的ではあるが残存する。Table I 11 エントリーの生成物は "glpc, nmr, ir, and/or mass spectra" で特性評価されており、生成物同定は少なくとも一次的には充足。RI-02 は Non-fatal として通過。

**→ VQ-1 通過（RI-02 Non-fatal）**

**VQ-2（Method）— RI-01, RI-07 要件（VQ-1 継承）:**

- RI-01: SRG-1（GLPC 収率の内部標準不在）、SRG-5（収率基準の内部矛盾）により、測定フレーム不統一が重大に残存。5件の GLPC 収率エントリーを独立評価不能。**Fatal に近い Non-fatal**（GLPC エントリーが 5/11 を占め、方法論的完全性を損なうが、単離収率エントリー（6件）を主たる実証の基盤とすれば VQ-2 は原理的に成立可能）。
- RI-07: Feature (5)「definitely superior to THF」（B-5, SRG-8 RI-07 secondary）と Feature (2)「Only Csp2 halides can be used」（B-4）の両境界主張が失敗実験・比較データなしに宣言。**Era-norm 依存（後述 Step 3b で補正）**。

Modern baseline（era-norm 適用なし）では RI-01 非致命的残存 + RI-07 Fatal: **VQ-2 未達（modern baseline）**

**VQ-3（Mechanism）— RI-03, RI-04, RI-06 要件（VQ-2 継承）:**

- RI-03: SRG-3（触媒サイクルの中間体未観測）、SRG-2（vinyl-Ni 中間体の立体化学未観測）、SRG-4（β-H 脱離抑制機構の中核種未観測）において複数の Fatal 残存。
- RI-04: CLA-1（R-R ホモカップリング不在の識別力欠如）で Fatal 残存。
- RI-06: SRG-3 の触媒サイクルは (dipy)Ni 系からの大規模モデル輸入で同型性実証なし。Fatal 残存。

**VQ-3 未達（modern baseline）**

**VQ-4（Benchmark）— RI-08, RI-09 要件（VQ-3 継承）:**

- RI-09: SRG-8（先行技術との数値比較全不在）でFatal 残存。
- RI-08: SRG-1 で反復測定・不確かさ記述ともに不在。

**VQ-4 未達（modern baseline）**

---

**Step 3b: Era-norm annotation での補正**

本論文は 1972 JACS communication（approximately 2 pages including Table I and two detailed procedures）。この communication genre の当時の慣行を考慮する（§4 で詳細化）：

- RI-07（境界主張）は communication 体裁での page 制約から構造的に来ており、era-norm tolerated として分類可能（失敗実験エントリーの省略は 1972 年 JACS communication では典型的）。
- RI-01（GLPC 収率基準 + 内部標準不在）は 1972 年当時の JACS では既に内部標準開示が推奨されており、**完全な era-norm tolerance とは言えない**が、communication の紙面制約下では部分的 tolerance が成立。
- RI-09（外部優位性の数値根拠なし）は 1972 年当時の communication 体裁では許容される範囲内（先行技術との並行実験を同一 communication に収めることは期待されていなかった）。

Era-norm adjustment: RI-07 と RI-09 の Fatal 判定を era-norm tolerated に格下げ可能。RI-01 は部分的 tolerance（GLPC 内部標準不在は era-norm で tolerated、収率基準矛盾は era-norm でも partially deficient）。

**Step 3c: Final VQ judgment**

```
VQ-1: VQ-1 achieved
      RI-02 Non-fatal（black mixture は CLA-2 として記録されるが単離生成物の
      同定は最低限充足）

VQ-2: VQ-2 (era-norm qualified)
      Modern baseline では RI-01（GLPC 内部標準）が残存するが era-norm で
      partially tolerated。RI-07（境界主張）は era-norm tolerated。
      VQ-2 成立は「単離収率 6 エントリーを主要エビデンスとして読む」
      解釈に依存する。

VQ-3: VQ-3 not reached
      RI-03（中間体未観測: SRG-3/SRG-4/SRG-2）、RI-04（R-R識別不在: CLA-1）、
      RI-06（サイクルレベルモデル輸入: SRG-3）がいずれも Fatal で残存。
      Era-norm では 1972 年 communication として mechanistic 実証の欠如は
      communication-era tolerated だが、VQ-3 の主張成立には原理的に不十分。
      著者自身が "working hypothesis" と留保しており、VQ-3 を主張していない
      という意味では、VQ-3 not reached は著者の意図とも整合する。

VQ-4: VQ-4 not reached
      RI-08（定量信頼性）、RI-09（外部優位性）が残存。RI-09 は era-norm
      tolerated だが VQ-3 未達により VQ-4 も自動的に未達。
```

**現在判定: VQ-2 (era-norm qualified)（Method）**

継承原則の明示: VQ-2 は RI-02 が非致命的であることを前提に成立している（VQ-1 継承）。VQ-2 の era-norm qualified 判定は、GLPC 収率 5 件を communication 体裁での紙面制約による部分的省略として読み、単離収率 6 件が主要実証基盤として機能することを前提とする。

**層別 VQ 非対称性:**

本論文は単一 paradigm（溶液相有機金属触媒合成化学）であり、§1 Claim Architecture の Layer 1（合成実用性）・Layer 2（機構仮説）の独立性から、層別 VQ 非対称性を評価する：

- **Layer 1（合成実用性）単独**: VQ-2 (era-norm qualified) を安定的に達成。収率・生成物キャラクタリゼーション・detailed procedures の組み合わせで合成方法論主張は成立。
- **Layer 2（機構仮説）単独**: VQ-1 止まり（VQ-2 は RI-07 Fatal で未達: eqs 2–4 の各ステップの速度論的境界が未定義）。著者が "working hypothesis" と明示しており、VQ-2 以上を主張していない。

**Single-paradigm 確定（no Layer asymmetry detected）**: Stage 2 の v19_trigger_status で C22_layer_asymmetry = not applicable（single-paradigm paper）と判定されており、異種 paradigm 混在による Layer asymmetry は存在しない。Layer 1/Layer 2 の VQ 非対称性は claim 構造の独立層に由来するものであり、paradigm asymmetry（C22 の対象）ではない。これは Stage 2 C22 not-applicable と完全に整合する。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-4（sp3 ハライドの失敗実験なし）**: 1972 年 JACS communication の 2 ページ体裁では、成功例 11 件の表示が優先され、スコープ境界の制御実験は Full Paper に委ねられるのが通常の genre convention だった。"Only Csp2 halides can be used" という宣言は community に対する実用的指針として通用し、反証実験の記述は全論文の当時の慣行ではなかった。
- **B-5（溶媒比較データ不在）**: "Definitely superior to THF" という比較主張についても、当時の JACS communication では定性的特性評価の報告が許容されており、並行実験データの同一通信への収録は義務ではなかった。Tamura-Kochi 系との逆転という観察事実を先行技術差別化のフックとして使う構造は当時の実験化学 communication では通例。
- **A-3（触媒サイクルの "working hypothesis" 留保）**: 機構的詳細を "working hypothesis" として明示しつつ将来研究に委ねる形式は、1972 年の experimental communication では完全に許容されていた。当時は機構と合成が同一 communication に収録されることへの期待がなく、合成的有用性の実証が priority だった。
- **B-3（触媒量のエントリーごとの非開示）**: 10⁻²〜10⁻³ の範囲指定のみで per-entry 開示なしは、当時の短報様式で許容された condensation。Full Paper では開示が期待される事項。
- **B-7（条件 A/B の基質割当根拠不開示）**: 同上。
- **C-1, C-2（先行技術との数値比較なし）**: Era-norm tolerated（RI-09 が era-norm tolerated に分類される根拠）。1972 年の JACS communication では、定性的先行技術差別化が standard practice であり、parallel control experiment の同一論文への収録は通例ではなかった。

**modern-era deficient:**

- **B-2（GLPC 内部標準・応答係数の不開示）**: 現代の ACS Journals では GLPC / GC 定量収率には内部標準の同定と応答係数（または校正方法）の開示が投稿規定上求められる。5 件の GLPC 収率（98%, 95%, 89%, 95%, 80%）は現代基準では独立評価不能な値として扱われる。
- **U-1（R-R 予測副生物の未報告）**: 現代の触媒系論文では、提案機構から予測されるすべての副生物の定量または検出限界の明示が要件。"高選択性"という主張を裏付けるマスバランスの閉鎖は現代標準。
- **U-5（黒色混合物の未同定）**: 現代の均一系触媒研究では、触媒の speciation（均一系か不均一系か）の確認（水銀毒化試験、TEM、動的光散乱等）が要件。
- **B-1/U-4（収率基準の内部矛盾）**: 現代の synthetic communication では収率の分母統一と明示が基本的報告要件。
- **C-3（Corriu-Masse との比較不在）**: 現代では concurrent disclosure に対する scope 比較が reviewers に要求される。Note Added in Proof のみによる「承認」は不十分と見なされる。

**両方に該当する項目（当時許容・現代不足）:**

- **B-5（溶媒比較データ）**: 当時は communication として era-norm tolerated だが、現代の synthetic methods paper では "definitely superior" という strong assertion には比較実験が必須。
- **B-3（per-entry 触媒量）**: 当時は communication として tolerated だが、現代では reproducibility の観点から must-report 事項。

---

### §5 最短補強ルート

現在の VQ 判定は VQ-2 (era-norm qualified)。

**第一目的関数: VQ-3（Mechanism）への到達**

必須解消項目: RI-03（Unobserved explanatory）、RI-04（Unreplicated discriminator）、RI-06（Imported model）。

VQ-2 継承前提: RI-01 非致命的残存 + era-norm qualified の成立は前提として継承する。

```
**VQ-3 への最短ルート：**

1. EP-10a [Kinetic verification pack] — SRG-3/SRG-4/CLA-1 を同時前進させる効率最高 EP。
   [NiCl₂(dpe)] 触媒量条件下でのリン酸エステル系 initial-rate kinetics（基質次数・触媒次数
   決定）+ 重水素化 Grignard 試薬（EtMgBr-d₅ vs. n-BuMgBr-d₉）による KIE 測定 +
   TEMPO 捕捉によるラジカル連鎖排除。各 Table I エントリーの R-R ホモカップリング副生物
   GLPC 定量（マスバランス閉鎖）を同時実施。
   RI-03（速度論的拘束による中間体制約）、RI-04（R-R 定量による識別力確立）、
   PRI-11（速度式と機構サイクルの整合性検証）を前進。

2. EP-03a [Direct-observation / state-assignment pack] — 中間体 1（L₂NiR₂）および 2
   （L₂Ni(R')(X'')）の独立合成と NMR/X 線キャラクタリゼーション。dpe-Ni(0) の
   独立生成と酸化的付加（sp2 C-Cl）の単独ステップ実証（eq 2 型）。黒色混合物の
   TEM/EDX 分析による均一系 vs. 不均一系確認（CLA-2 解消）。
   RI-06（サイクルレベルモデル輸入を dpe-Ni 系での stoichiometric 検証で代替）、
   RI-02（活性種同定）、RI-03（中間体直接検出）を前進。

3. EP-04a [Discrimination / replication pack] — ビニルハライド立体化学の識別実験
   （SRG-2 CLA 解消）。cis- / trans-ClCH=CHCl それぞれについて反応温度を 0°C / RT /
   reflux と変え、生成物 cis/trans 比の温度依存性を測定。TEMPO 存在下での実験と
   対比（ラジカル連鎖の排除または特定）。cis/trans 比の反復測定（n=3）で再現性確立。
   RI-03（vinyl-Ni 中間体の速度論的制御 vs. 熱力学的制御の区別）、RI-04
   （ステレオ選択性測定の再現性確立）を前進。

認定ゲート順注記: 実験投入順は情報利得順（EP-10a → EP-03a → EP-04a）だが、
最終 VQ-3 認定は VQ-1 → VQ-2 → VQ-3 の継承ゲート順で確定する。VQ-2 (era-norm
qualified) の成立（RI-01/RI-07 の era-norm tolerance 前提）を継承した上で、
RI-03/RI-04/RI-06 の解消によって VQ-3 が開く。
```

**第二目的関数: VQ-4（Benchmark）への到達**（VQ-3 達成後）

```
**VQ-4 への最短ルート（VQ-3 前提）：**

4. EP-08a [Replication / uncertainty pack] — SRG-1 解消。GLPC 収率 5 件について
   内部標準（ドデカン等）の応答係数校正 + 反復測定（n=3）で不確かさを記述。
   単離収率での検証も実施。RI-08 を前進。

5. EP-09a [Internal benchmark pack] — SRG-8 解消。Tamura-Kochi 鉄触媒
   （THF 条件）vs. [NiCl₂(dpe)]（ether 条件）の parallel comparison を
   EtMgBr/PhCl + n-BuMgBr/PhCl で実施し、収率・Ph-Ph ホモカップリング比を
   数値対比。溶媒比較（ether vs. THF）実験も同時実施（Feature 5 の実証）。
   RI-09 を前進。

認定ゲート順注記: VQ-4 認定も VQ-1 → VQ-2 → VQ-3 → VQ-4 の継承ゲート順で
確定する。
```

---

### §6 制度設計への寄与

**1. EP-10a の正式登録の追加確認事例（SRG-3/SRG-4/CLA-1）:**

Kumada 1972 は EP-10a（Kinetic verification pack）の 7 独立観察源の一つとして既に登録されている（prompts 内 EP-10a 運用注記参照）。本 Stage 3 v4 実行（Sonnet, v19）はその確認を更新する。SRG-3（触媒サイクルの動力学的検証不在）、SRG-4（β-H 脱離抑制の速度論的拘束不在）、CLA-1（R-R 予測副生物の定量不在）の三つの独立な欠落が、いずれも EP-10a によって同時に前進可能であることを確認。これは EP-10a の「複数の RI を単一の EP で同時前進させる高効率性」という登録根拠を実例で裏付ける。

**2. PRI-11（Mechanism-kinetics decoupling）の第三確認事例候補:**

SRG-3 および SRG-4 において、提案触媒サイクル（eqs 2–4）から速度式を代数的に導出せずに、機構的支持を文献類推（C-5）のみで行っている。これは PRI-11 の定義（「提案触媒サイクルまたは反応機構から速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」）に該当するが、本論文では速度次数データすら取得されていない点で PRI-11 の「軽度」事例よりも重篤である。Breitenfeld 2014（提案）・Pengfei 2024（同型確認）・本 Kumada 1972 で三例となり、PRI-11 の昇格要件（独立 2 報確認）はすでに Breitenfeld + Pengfei で充足されている。Kumada 1972 は PRI-11 の第三確認事例として追記可能（Murai 1993 との類似性も含め cross-model meta に記録）。

**3. PRI-12 系の適用境界明示（Heck-style / Kumada 1972 への非適用）:**

PRI-12 Cluster A（Self-referential validation）は現代計算化学・方法論論文に特有であり、本論文（実験的合成化学 communication）には適用されない。Self-referential validation チェックの結果、PRI-12 Cluster A の発火条件（「検証指標と被検証対象が同一の数学的構成物に依存する」等）は成立しないことを確認した。

PRI-12 Cluster B（Deductive-retrospective circularity）については、eqs 2–4 の working hypothesis が文献類推に基づく惰性的な「理論先行」構造ではなく、著者が明示的に "working hypothesis" として限定していること、また演繹的中心主張として機構的 VQ を要求する形式ではないことから、Cluster B の閾値にも達しないと判断する。

**Kumada 1972 における PRI-12 適用判断**: 非適用（PRI-12 Cluster A / B いずれも不発火）。これは Murai 1993（同型 Heck-style 実験的合成 communication）と同一の適用境界を示す。"PRI-12 非適用 + PRI-11 第三確認事例候補" というパターンが Kumada 1972 / Murai 1993 の共通プロファイルとなる。

**4. 通信→Full Paper遷移の自動解消パターン（§6 の記録が求めるパターン）:**

SRG-6（B-3 per-entry 触媒量・B-7 条件 A/B 根拠）、B-4（sp3 ハライド失敗実験）、B-5（溶媒比較）は communication から Full Paper への展開で自動解消される典型的パターンである。著者の「investigations are continuing」宣言（A-1 series_signal）はこのパターンの明示的な制度的宣言であり、ERA-NORM ANNOTATION の communication-era tolerated 分類と完全に整合する。Kumada 1972 はこのパターンの模範事例として §4 に記録する。

**5. RI共起パターンの確認:**

SRG-3 では RI-03（中間体未観測）+ RI-06（モデル輸入）が共起し、どちらか一方の解消だけでは不十分である。RI-06 の解消（stoichiometric 実験で dpe-Ni サイクルを実証）だけでは、触媒量条件下での中間体の速度論的拘束（RI-03）は解消されない。両方の同時解消が VQ-3 達成の要件。SRG-4 では RI-03（β-H 脱離抑制の中心的説明者未観測）+ RI-05（定性的序列から構造的含意への overread）が共起し、同様に両方の解消が必要。

**6. 本ケースの既存制度設計への寄与まとめ:**

本 Kumada 1972 v19 Sonnet Stage 3 v4 分析は、新規の制度設計知見を生成するというより、既存の制度設計を高精度で追加確認するケースである：(a) EP-10a の高効率性（複数 RI 同時前進）を 3 独立欠落で再確認、(b) PRI-11 第三確認事例候補の記録、(c) PRI-12 の Heck-style 実験論文への非適用境界の安定確認、(d) 通信→Full Paper 自動解消パターンの模範事例記録、(e) RI-03/RI-06 共起パターンの追加実例。「本ケースは既存の制度設計を高精度で追加確認した」と総括する。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
