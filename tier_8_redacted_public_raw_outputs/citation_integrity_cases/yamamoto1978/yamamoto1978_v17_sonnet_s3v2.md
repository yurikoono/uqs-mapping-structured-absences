prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Yamamoto, Hayashi, Yamamoto 1978（Bull. Chem. Soc. Jpn. full_paper）

---

### §1 Claim Architecture

**コア主張の要約**

本論文は「遷移金属触媒C–Cカップリングを重縮合へ応用した新型ポリコンデンセーション法」の最初の実証報告である。**Novelty柱**は（1）NiCl₂(bpy)等の遷移金属錯体がMgとジハロゲン化芳香族の系において重縮合を触媒できるという方法論的発見と、（2）この反応がScheme 1に示す有機金属サイクル（旧来Kumada型カップリングと同型の機構）を経るという機構的提案の二つからなる。**Utility柱**は（1）高重合度・規則構造・低着色のポリフェニレン型ポリマーの穏和条件合成と、（2）従来の銅・アルカリ金属による脱ハロゲン化法に対する品質的優位性の主張である。

**Layered structureの判定：**

論文の主張は少なくとも3つの独立した層に分かれており、単一の反証では全主張が崩れない。

- **合成結果層（Synthetic Layer）**: Table 1（27エントリー）とTable 2（収率・物性データ）に記録された実験事実。触媒が反応を開始させるという観察自体は機構が誤りでも成立する。→ 最も堅牢。
- **高分子物性層（Property Layer）**: IRスペクトル（Fig. 1）、X線回折（Fig. 2）、DTA熱分解温度（Table 2）に基づく高規則性・高熱安定性の主張。IRプロキシによるDPの間接的評価を含む。→ 中程度の堅牢性。
- **機構仮説層（Mechanism Layer）**: Scheme 1の4ステップサイクル（中間体1・2の提案）。文言上「seems to proceed」「if the same mechanism can be applied」と条件節に置かれており、著者自身が検証として提示していない。→ 最も脆弱。

**層間の依存関係：** Property LayerはSynthetic Layerが成立していれば成立可能。Mechanism LayerはSynthetic/Property Layerを支持するためには不要（観察事実の説明として後付け可能）。しかし論文の競争的優位性主張（「従来法のラジカル経路より優れた選択性」）はMechanism Layerに依存しており、その機構が実証されない限り「構造規則性の機構的理由」という主張は成立しない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1: 絶対分子量測定の不在**（Absence of absolute molecular weight determination）

* **Primary RI**: RI-05 Qualitative overread — IRバンド強度比（A(δ(para))/A(δ(mono))）という定性的プロキシから「高重合度」「同程度のDP」という定量的主張を導出。
* **Secondary RI**: RI-08 Unquantified reliability — 反復測定なし、不確かさ記述なし。
* **ER**: poly(p-phenylene)のMn/Mw/PDIをGPCまたは粘度測定（[η] vs Mn較正）により絶対測定し、少なくとも代表的2エントリー（最高収率No.2と最高IR比No.7）で報告すること。抽出フラクションのMnが報告されれば「high degree of polymerization」の定量的根拠となる。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: poly(p-phenylene)はTHF不溶だが抽出フラクションはClHC₃可溶であり、Soxhlet抽出後フラクションのGPC（DMF/LiClまたはTCB高温GPC）を実施し、Mn/Mw/PDIを報告。IRプロキシとの相関較正曲線を作成する。
* **注記**: B-1, B-9がhigh_convergence_low_gap（V1=high, V3=high; convergence=2/3; gap=none）。SRG-1はProperty Layerの定量的堅牢性に直結。

---

**SRG-2: 触媒サイクルの実験的根拠欠如**（Absence of experimental grounding for the catalytic cycle）

* **Primary RI**: RI-06 Imported model — Tamao 1976 BCSJ（ref. 6b）の低分子クロスカップリング機構を重縮合系への同型性実証なしに輸入。「if the same mechanism can be applied」という条件節自体が輸入の自覚を示す（RI-06スコープ注記「サイクルレベル輸入」に該当）。
* **Secondary RI**: RI-03 Unobserved explanatory — 中間体1（BrNiL₂–(–C₆H₄–)ₙMgBr）および中間体2（ジアリールNiL₂型）は「鍵中間体」と命名されているが、直接観測も速度論的拘束もされていない。
* **ER**: 少なくとも（a）n=1類縁体の単離・NMR同定（単量体基質でのモノアリールNi(X)(L₂)錯体の独立合成）、（b）クロスオーバー実験または同位体標識実験による反応経路の実証、（c）ラジカル経路排除のための阻害剤（TEMPO、AIBN等）を用いた試験、のいずれかを実施すること。
* **EP**: EP-06a Analogy-validation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: n=1類縁体として BrNi(bpy)(C₆H₄MgBr)（中間体1(1)）を独立合成し、¹H/³¹P NMRで同定。あるいはFig. 3の3 °C動力学実験系にTEMPOを添加し、ラジカル経路であれば重合が完全に阻害されることを確認する。クロスオーバー実験：p-Br-C₆H₄Brとp-I-C₆H₄Iを1:1で用い、クロス生成物（p-BrC₆H₄–C₆H₄I）の割合をGCで定量する。
* **注記**: A-1, A-2, B-3, U-1, U-2, U-3を含む最大SRG（6項目）。U-2はlow_convergence_high_gap（V2=critical）。A-1, B-3はhigh_convergence_low_gap（convergence=2/3）。**標識不整合パターン**検出：Scheme 1本文の叙述には"formation of NiR₂L₂", "reaction of NiR₂L₂ with R'X to yield R-R"という事実的記述語を使用しながら、直前に「seems to proceed」という仮説標識を置く。仮説標識がScheme 1の冒頭1文に集約され、各ステップの記述は事実的語で展開されている（§6で詳述）。

---

**SRG-3: 動力学データの速度則的解析不在**（Absence of rate-law analysis from kinetic data）

* **Primary RI**: RI-04 Unreplicated discriminator — Fig. 3の時間–濃度プロファイルという単一データが機構的主張（誘導期の意味、Scheme 1の速度論的整合性）の唯一の実験的支持として使用されているが、速度定数、反応次数、マスバランス、再現性情報がない。
* **Secondary RI**: PRI-11 Mechanism-kinetics decoupling（暫定）— Scheme 1から速度式を代数的に導出せず、Fig. 3の定性的プロファイルとの一致のみで機構を支持。PRI-11の定義（提案触媒サイクルから速度式を代数的に導出せずに観測速度次数との一致のみで機構を支持）と一致。**本ケースはPRI-11の追加確認例となる**（Breitenfeld 2014、Pengfei 2024に続く第3例候補）。
* **ER**: Fig. 3の各時点での[BrC₆H₄MgBr]、[BrMg–C₆H₄–MgBr]、[p-C₆H₄Br₂]の量的データから速度定数を求め、Scheme 1から導出される速度式（少なくとも誘導期の律速段階の仮定を明示した上で）と比較すること。マスバランス（全炭素量の保存）を各時点で報告すること。
* **EP**: EP-04a Discrimination / replication pack; EP-10a Kinetic verification pack（暫定）
* **Case-specific実装**: 3 °C実験のFig. 3データに対して、誘導期の速度依存性（[Ni]₀に対する[触媒]依存性）と、誘導期後の見かけ一次または二次速度則のフィッティングを実施。独立5点以上の時点でマスバランスを検証する。
* **注記**: B-3（high_convergence_low_gap）と連動。SRG-3はSRG-2の動力学的補強に対応する。

---

**SRG-4: 従来法との直接数値比較の欠如**（Absence of direct numerical comparison with conventional methods）

* **Primary RI**: RI-09 External superiority — 従来のUllmann法、Wurtz-Fittig法に対する優位性主張が直接比較なしに外部文献値のみで行われている。
* **Secondary RI**: RI-05 Qualitative overread — 色（light yellow vs. brown/black）という定性的観察から「構造規則性の向上」という定量的・構造的含意を導出。
* **ER**: 同一モノマー（p-ジブロモベンゼン）を用いたUllmann法（Cu、高温）またはWurtz-Fittig法（Na、高温）による対照実験を実施し、本法と同一キャラクタリゼーション手順（IR比、X線回折、GPC）で直接比較すること。
* **EP**: EP-09a Internal benchmark pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: p-ジブロモベンゼンをCuBr₂存在下で高温（200°C以上）反応させたpoly(p-phenylene)の試料を作製し、本論文法産物と同一条件でIR比、X線回折パターン（アニーリング前）、DTA分解温度を測定して数値比較する。
* **注記**: B-4はhigh_convergence_low_gap（V1=high, V2=critical; convergence=2/3; gap=low）。C-2, C-3, C-4がSymmetric citationsとして同期した cite-and-drop を形成（SRG-4関連）。

---

**SRG-5: ホモカップリング副生成物とマスバランス**（Homo-coupled byproduct and mass balance）

* **Primary RI**: RI-03 Unobserved explanatory（サブタイプ：自己矛盾的不在）— Scheme 1のステップ(b)（NiR₂L₂ + R'X → R-R + NiR'(X)L₂）が触媒サイクル開始フェーズで化学量論的なホモカップリング生成物（ビフェニル型）の生成を予測するが、その検出・定量が論文内で一切実施されていない。
* **Secondary RI**: RI-01 Reporting integrity — Fig. 3の各時点でのマスバランス（モノマー炭素の行方）が報告されていない。
* **ER**: Scheme 1ステップ(b)由来のビフェニル（または対応するアリールホモカップリング生成物）の定量（GC/MS）をワークアップ段階で実施し、報告すること。Fig. 3の各時点での全炭素マスバランスを確認すること。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: 重合開始初期（0〜30分）の反応アリコートをGC/MSで分析し、ビフェニル（biphenyl）の生成量を内部標準（トルエン）に対して定量する。ステップ(b)が正しければ、触媒量（[Ni]₀）に対してほぼ化学量論的なビフェニルが初期に生成するはずである。
* **注記**: U-1（self-contradictory absence; high_convergence_low_gap相当; V2=high, V3=high; convergence=2/3）が対応。

---

**SRG-6: 立体化学・位置化学の間接証拠割り当て**（Indirect assignment of regio- and configurational chemistry）

* **Primary RI**: RI-05 Qualitative overread — poly(m-phenylene)のcis-trans/trans-trans配置比、poly(phenylenemethylene)のhead-to-tail選択性が、X線ピーク幅とIRパターン形状という定性的観察から「presumably the head-to-tail structure」として断定的に割り当てられている。
* **ER**: ¹H NMRによる化学シフト帰属、必要に応じてNOE測定またはモデル化合物比較によって位置化学（head-to-tail/head-to-head）と構成異性体（cis-trans/trans-trans）の存在比を定量化すること。
* **EP**: EP-02a Identity / purity substantiation pack
* **Case-specific実装**: CDCl₃またはd-TFAに可溶なフラクション（Soxhlet抽出フラクション）の¹H NMRを詳細帰属し、頭対尾、頭対頭、尾対尾構造単位のピーク積分比を報告する。poly(m-phenylene)については可変温度NMR（高温CDCl₃溶液）でcis-transコンホメーションの寄与を評価する。
* **注記**: B-5, B-8が対応。単独エージェント（V2=medium）であり、この SRGはSynthetic Layerではなく Property Layerの厳密性に関わる。

---

**SRG外：CLA**

**CLA-1: 触媒不活性の機構的矛盾（Pd不活性 vs. Scheme 1の論理的一貫性）**

* Stage 2 D4-4に対応。B-2がmemberだがいずれのSRGにも属さない。
* D-1のNovelyly柱（機構提案：Ni²⁺/Ni⁰サイクルが選択的重縮合を可能にする）に直結するCLAである。
* **Primary RI**: RI-06 Imported model（拡張）— Scheme 1はNiX₂L₂/NiR₂L₂/NiR'(X)L₂サイクルとして記述されているが、Pd²⁺は同等の酸化数変化（Pd²⁺→Pd⁰→Pd²⁺）が可能であるにもかかわらず無活性と報告される。この不活性がScheme 1の論理から説明されていない。
* **ER**: Pd類縁体の不活性の原因（還元消去速度の差異、Pd⁰の安定性、基質酸化的付加に対する異なる反応性等）を速度論的または計算化学的に検討すること。
* **EP**: EP-06a Analogy-validation pack
* **Case-specific実装**: PdCl₂(bpy)の非活性実験（Table 1, No. 7は活性！）を確認する注意：Table 1 No.7はPdCl₂(bpy)が95%収率を与えている。「PdCl₂は無活性」という記述は「Pd金属とPdCl₂」（担持または無配位子形態）に限定されている可能性がある。したがってこのCLAの焦点は「配位子なしのPdCl₂ vs. 配位子あり PdCl₂(bpy) の活性差の原因」に絞られる。
* **注記**: B-2はhigh_convergence_low_gap（V1=medium, V2=high; convergence=2/3; gap=low）。SRG-2の周辺に位置するが独立CLA。

**CLA-2: 負の証拠からの強い推論——端末基の同定（D₂O/CO₂プローブ）**

* B-6に対応。「D₂O、CO₂処理でD・カルボキシル基の導入なし」という否定的証拠から「–C₆H₄MgBr末端の不在」を結論する推論。
* **Primary RI**: RI-04 Unreplicated discriminator — 単一の負の試験（D₂O/CO₂クエンチ）から端末基構造について強い結論を導出しているが、検出下限が報告されていない。
* **ER**: D₂O/CO₂クエンチの検出下限（NMR または質量分析での最低定量濃度）を明示し、小割合（例えば<5%）の–C₆H₄MgBr末端が検出できない条件かどうかを確認すること。
* **EP**: EP-04a Discrimination / replication pack
* **Case-specific実装**: 末端基比率が既知のモデルオリゴマー（合成によりMgBr末端とPh末端の比が確認されたもの）を用いてD₂O/CO₂クエンチアッセイを較正し、検出感度を決定する。
* **注記**: B-6はhigh_convergence_low_gap（V1=medium, V2=high; convergence=2/3; gap=low）。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation) — 通過**

**VQ-1 [Observation]**（RI-02: Object identification の解消が必要）: **通過**。
論文はpoly(p-phenylene)のIRスペクトル（Fig. 1）、X線回折（Fig. 2）、元素分析（本文記述），ならびに主要ポリマーの融点・色・溶解性（Table 2）を提供しており、生成物の同一性確認に最低限必要な分光学的同定はなされている。RI-02は非致命的に残存する（配位子NMR帰属、高分解能MSは未実施だが、1978年の全紙面体では許容範囲）。
ただし、RI-02の部分未解消として、Soxhlet抽出フラクションの元素分析やMg/Ni残存量の確認が未実施であることは非致命的に残存する。

---

**VQ-2 [Method]**（RI-01: Reporting integrity + RI-07: Unsupported boundary の解消が必要、VQ-1継承）: **通過（qualified）**。
RI-01に関して：Table 1の収率はすべて「炭素量基準」で統一されているが、Entries 25・27のみ%表示なし（B-7）という内部不整合がある（RI-08サブタイプ「内部矛盾型」）。Table 1の主体は同一基準で報告されており、全体としてRI-01は非致命的に残存するが主張を根底から覆さない。
RI-07に関して：論文はリチウムが不成功だったことを記述しているが、失敗理由を述べない。「Mgが必要」という境界主張が証拠なしに成立している（CLA-1参照）。これも非致命的残存。
VQ-2はRI-02の非致命的残存とRI-01・RI-07の非致命的残存を前提に成立する。
Qualified理由: RI-05が軽度に残存している（色・X線パターンの定性的比較）。

---

**VQ-3 [Mechanism]**（RI-03 + RI-04 + RI-06 の解消が必要、VQ-2継承）: **未達**。
- RI-06: Scheme 1はTamao 1976 BCSJ低分子機構の重縮合系への大規模輸入（サイクルレベル）。同型性の実証なし。**致命的**：機構層の主張（「触媒サイクルを経て選択的重縮合が進行する」）はRI-06が未解消である限り原理的に成立しない。
- RI-03: 中間体1・2は「鍵中間体」と命名されているが、いかなる直接観測も速度論的拘束もない。**致命的**。
- RI-04: Fig. 3の単一時間プロファイルから機構的結論を導出しているが、速度定数・反応次数・マスバランスなし。**致命的**。
- PRI-11（暫定）: Scheme 1から速度式を代数的に導出せず、Fig. 3の定性プロファイルとの一致のみで機構を支持。**非致命的**（機構層をさらに制約する要件として重要）。

ただし**Synthetic Layer単独では：** VQ-2到達（method水準）で観察的に成立。机上での比較では、機構提案を除いた合成・物性の主張（Novel合成法、高DP、高熱安定性）はVQ-2水準で評価可能。

---

**VQ-4 [Benchmark]**（RI-08 + RI-09 の解消が必要、VQ-3継承）: **未達**（VQ-3未達のため評価不可）。
コメント: SRG-1（絶対Mn不在；RI-05/RI-08）とSRG-4（従来法直接比較不在；RI-09）が未解消のため、VQ-3が先に要求される。

---

### §4 Era-Norm Annotation

**communication-era tolerated（1978年、BCSJ全紙面）:**

- **B-3（機構の analogy import）**: 1978年時点では、Kumada-Tamao機構の重縮合への外挿を「一応の提案」として提示することは、機構有機化学の報告規範として許容された。独立した機構的検証（クロスオーバー実験、ラジカルクロック）は当時の有機合成報告では標準的でなかった。
- **B-8（cis-trans配置の間接的割り当て）**: 1978年当時、固体ポリマーの配置的均一性の¹H NMR帰属は技術的に困難であり（高温溶液NMR、¹³C CPMAS等は普及途上）、X線パターンによる間接的推論は許容されていた。
- **B-5（head-to-tail "presumably"）**: 同上。1978年当時のポリマー化学では、X線とIRに基づく位置化学の推定は許容された表現様式。
- **C-2, C-3, C-4（従来法へのcite-and-drop）**: 1970年代後半の合成報告において、背景技術を列挙して新法の優位性を主張することは、直接比較実験なしでも一般的に許容された。

**modern-era deficient（現代の再認定基準）:**

- **B-1, B-9（絶対分子量不在）**: 現代のポリマー化学では、GPCまたは粘度測定によるMn/Mw/PDIの報告は絶対的要件。IRプロキシによるDPの評価は補助的にしか許容されない。→ **RI-05/RI-08 Fatal（現代基準）**。
- **U-2（中間体1・2の不在）**: 現代の有機金属化学・触媒反応機構の報告規範では、提案された「鍵中間体」の少なくとも1つについて、独立合成または分光観測が要求される。→ **RI-03 Fatal（現代基準）**。
- **U-1（ホモカップリング副生成物の未定量）**: 現代では、提案触媒サイクルが予測する副生成物の有無をGC/MSで確認することは標準的要件。→ **RI-03（自己矛盾的不在サブタイプ）Modern-deficient**。
- **B-4, C-2（Dropped Quantitative Benchmark）**: 現代では、先行技術との優位性主張に同一測定条件下での直接比較が要求される。単なる文献値引用では不十分。→ **RI-09 Modern-deficient**。
- **V3-Q3/V3-Q4相当（GC較正・マスバランス）**: 現代の触媒化学報告では、動力学実験のマスバランス確認と検出器較正の記述は標準要件。→ **RI-01 Modern-deficient**。

**両タグ該当（当時は許容されたが現代では不足）:**
- **B-3, A-1（機構のanalogy import）**: 1978年時点では許容されたが（communication-era tolerated）、現代基準では独立検証なしの機構輸入はRI-06として致命的に扱われる（modern-era deficient）。

---

### §5 最短補強ルート

**第一目的関数：VQ-3 [Mechanism] への到達**（現在VQ-2 → 目標VQ-3）

**VQ-3への最短ルート：**

1. **EP-06a Analogy-validation pack** — SRG-2向け：n=1類縁体BrNi(bpy)(C₆H₄Br)を独立合成・NMR同定し、Scheme 1の中間体1(1)の実在を実証する（または重合系で in situ ³¹P/{¹H}NMR観測）。RI-06, RI-03 を同時前進。
   *(これが最大の情報利得：RI-06とRI-03の両方を前進させ、SRG-2のPrimary・Secondary RIを一括対処)*

2. **EP-03a Direct-observation / state-assignment pack** — SRG-5向け：Scheme 1ステップ(b)由来ビフェニルをGC/MSで初期時点（0〜30 min）に定量。SRG-5（U-1）のRI-03自己矛盾的不在を解消。RI-03 前進。

3. **EP-04a Discrimination / replication pack** — SRG-3向け：Fig. 3実験にラジカル阻害剤（TEMPO）添加対照を設定し、ラジカル経路の寄与を排除。SRG-2(U-3)のRI-03を追加前進。RI-04, RI-03 前進。

4. **EP-10a Kinetic verification pack（暫定）** — SRG-3向け：Scheme 1から速度式を代数的に導出し、Fig. 3データに対する速度定数フィッティングを実施。マスバランスを各時点で報告。PRI-11 前進（RI-04 も前進）。

認定ゲート順注記：実験投入順は情報利得順（EP-06a → EP-03a → EP-04a → EP-10a）だが、最終認定はVQ-1 → VQ-2 → VQ-3 のゲート順で確定する。VQ-2通過（現在確認済み）を前提に、RI-06・RI-03・RI-04 が同時に解消された段階でVQ-3が確定する。

---

**第二目的関数：VQ-4 [Benchmark] への到達**（VQ-3到達が前提）

**VQ-4への追加ルート（VQ-3到達後）：**

5. **EP-05a Quantitative-ranking substantiation pack** — SRG-1向け：抽出フラクションのGPC（高温クロマトグラフィー）でMn/Mw/PDIを報告。RI-05, RI-08 を前進。
   *(情報利得最大：SRG-1のPrimary・Secondary RI両方を一括対処)*

6. **EP-09a Internal benchmark pack** — SRG-4向け：同一モノマーによるUllmann法対照実験を同一キャラクタリゼーション手順で実施し、DP（IR比+GPC）・熱安定性・構造規則性を数値比較。RI-09 前進。

認定ゲート順注記：VQ-4確定にはVQ-3が先行する必要がある。EP-05a, EP-09aはVQ-3到達後に投入する。

---

### §6 制度設計への寄与

**1. 既存RIコードの新しい代表事例**

- **RI-06「サイクルレベル輸入」の明確な代表事例**: Yamamoto 1978は、個別の素反応ステップの類推ではなく、低分子クロスカップリング触媒サイクル全体（Tamao 1976 BCSJ、4ステップ機構）を重縮合系に「if the same mechanism can be applied」という条件節一文で輸入している。これはRI-06スコープ注記「サイクルレベル輸入」の典型例として記録する。同様のパターンはKumada 1972にも観察されており（小分子モデル系機構の触媒サイクルへの外挿）、cross-case recurrenceが確認される。

- **RI-05「位置化学/立体化学の間接割り当て」の代表事例**: SRG-6において、X線ピーク幅の定性的解釈から「presumably head-to-tail」という構造的割り当てを行うパターンは、RI-05 Qualitative overreadの典型。

**2. PRI-11（Mechanism-kinetics decoupling）の昇格補強**

Yamamoto 1978は、（a）Scheme 1（4ステップ触媒サイクル）を提案しながら、（b）Fig. 3の定性的な時間–濃度プロファイルを唯一の動力学的証拠とし、（c）速度式の代数的導出を行わずにプロファイルの定性的形状（誘導期後の加速）を機構の傍証として使用している。これはPRI-11の定義「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」に完全に適合する。Breitenfeld 2014（第1確認）、Pengfei 2024（第2確認）に続く第3確認例として記録する。PRI-11の昇格判断を支持する。

**3. 「標識不整合（Labeling mismatch）」パターンの代表事例**

Scheme 1の構造は以下の通り：
- 冒頭1文：「[REDACTED: verbatim source text; see the source paper via its DOI]」（仮説標識）
- 各ステップ記述：「formation of NiR₂L₂」「[REDACTED: verbatim source text; see the source paper via its DOI]」（事実的記述語）
- Scheme 1全体：ボックスと矢印による化学量論的機構式（視覚的事実性）

仮説標識が冒頭一文に集約され、Scheme全体の視覚的記述と各ステップの動詞が事実的語で展開されているため、機構の「仮説性」が論文の視覚的印象から解離している。これはRI-06と連動する「標識不整合」パターンの明確な例として記録する。

**4. 「Second-generation non-filler」観察**

本論文はKumada 1972が提案したNi/Grignard触媒サイクルを重縮合系に拡張しながら、中間体1・2（EP-03a相当）の実在証拠を自ら生成しない。すなわち：
- Kumada 1972はScheme 1（小分子版）の中間体を提案・命名したが単離せず（EP-03aギャップを継承として残した）。
- Yamamoto 1978はKumada 1972のScheme 1を重縮合系に外挿し、高分子版の中間体1・2を命名したが、やはり単離・観測していない。

この「世代間でEP-03aギャップが継承される」パターンは、EP辞書に「Second-generation EP-03a inheritance」として記録する価値がある。Kumada 1972の機構的欠落が1978年段階でも埋まっていない事実は、Stage 4での充填論文探索において重要な文脈情報となる。

**5. EP-03a Case-specific実装の精緻化**

Yamamoto 1978のSRG-2では、EP-03aの実装として「n=1類縁体（BrNi(bpy)(C₆H₄Br)相当）の独立合成」を提案した。これはKumada 1972やTamao 1976で提案された類縁体実装（PEt₃配位子系でのmonoaryl-Ni(X)(L₂)単離）と異なり、bpy配位子系での実装になる。Parshall 1974のtrans-NiAr(X)(PEt₃)₂単離事例はPR₃配位子系であり、bpy系への転用には配位子の違いを明示的に考慮する必要がある。→ EP-03a Case-specific実装例の配位子依存性を記録する。

**6. EP辞書への新規case-specific実装例**

- **EP-10a（Kinetic verification pack）に「重縮合動力学専用プロトコル」を追加**: 重縮合（step-growth）の動力学はSchulz-Flory型PDI発展式と連動するため、通常の単分子反応速度論と異なる解析が必要。Fig. 3の解析には「チェーン長分布の時間発展をScheme 1から導出し、実測GCデータと比較する」という重縮合固有のプロトコルが必要。これをEP-10a重縮合サブ実装として記録する。
