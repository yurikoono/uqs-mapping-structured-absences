prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Li et al. 2024（Nature Catalysis, Article）

### §1 Claim Architecture

**コア主張：**
Ni触媒・電気化学的クロス電子求電子剤カップリング（eXEC）によって、非活性化アルキルハライド間のC(sp³)–C(sp³)結合形成を初めて一般的に達成した。Novelty柱：活性化基（ボリル、シリル、π系）を必要とせずに、1°–1°、1°–2°、1°–3°、2°–2°の全4クラスのアルキルハライド組み合わせで高選択的クロスカップリングを実現した最初の電気化学的一般戦略。Utility柱：90以上の基質スコープ（単離収率のみ）、生物活性化合物のレイトステージ修飾（>20例）、グラムスケール合成、1ステップ既知化合物合成。Ni(I/II/III)ラジカルサイクルが提案されているが、主張の中核である「クロス選択性の機構的根拠」は主テキストに存在しない。

**Layered structure：** あり・独立4層構造。
- 層1: 電気化学的有効化（非活性化ハライドへの電位到達）― 化学量論的還元剤なしのeXEC実現として独立して成立
- 層2: 合成スコープ広さ（90+基質の単離収率）― 機構が改訂されても成立
- 層3: Ni(I/II/III)機構提案（CV, SWV, DFT, ラジカルトラッピング）― スコープが限定されても独立
- 層4: 製薬・工業応用性（レイトステージ修飾、グラムスケール）― 機構が不確定でも成立

層間の依存関係：層3は層1を前提（電気化学的Ni還元が前提）。層1–2は相互に独立。ただし主張の「新規性」核心（なぜ非活性化でも選択的クロスカップリングが起きるか）は層3にのみ存在し、層3の検証が不完全であることが論文全体の最大の空白を構成する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Quantitative reaction outcome accounting absent]**

* **Primary RI**: RI-01 [Reporting integrity] — 単離収率のみの全スコープ報告、収率計算基準混在（B-15）、反復測定不在（B-14）が横断的に共存
* **Secondary RI**: RI-08 [Unquantified reliability] — 反復測定および統計的不確かさ記述の完全不在
* **ER**: 全スコープ反応においてGC収率（内部標準法）と単離収率を併記し収率計算基準を統一する；ホモカップリング副生成物収率を系統的に報告する；少なくともモデル反応（化合物3）について独立3回の反復実験（mean ± SD）を提示すること。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**:
  - 全90+基質にGCまたはHPLC収率（内部標準：メシチレン等）を追加報告（SIへの移行可）
  - ホモカップリング副生成物の系統的報告（現状はTable 1のモデル反応のみ）
  - TEMPO実験（B-11: 59%不明）とラジカルクロック実験（B-12: 直接カップリング体未報告）の完全質量収支（SM＋クロスカップリング体＋TEMPO付加体＋その他の定量）
  - 収率計算基準のTable全体での統一（限界試薬基準）
* **注記**: B-1（convergence 3/3、全エージェント=high、gap=none; TEMPERATURE_SUMMARYでhigh_convergence_low_gap中最高優先）、B-14（V3=high、1/3、low_convergence_high_gap）、B-15（V3=medium、1/3）。B-9, B-10, B-11, B-12もSRG-1構成要素。

---

**SRG-2 [Electrochemical operating conditions unreported]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 5 mA定電流電解中の実際のカソード電位（稼働条件下の電位窓）、アノード半反応という反応の中核的「状態」が直接観測されていない
* **Secondary RI**: RI-04 [Unreplicated discriminator] — アノード材料効果対照実験（entries 5–6）がmatched-pairでなく（B-7: アノードとカソードを同時変更）、アノード vs カソード効果の分離不可
* **ER**: 5 mA定電流電解中のchronopotentiometryによるカソード電位の直接測定を実施し、CV/SWVで測定した各Ni酸化還元電位と比較する；アノード半反応を同定しファラデー効率を報告する；アノード材料のmatched-pair対照実験（カソード固定）を実施する。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**:
  - 定電流電解中の電位–時間プロファイル（chronopotentiometry）記録：カソード動作電位の直接把握
  - Fe板アノード vs. Pt, GC, Cアノード（Ni foamカソード固定のmatched-pair control）でアノード独立効果を分離
  - ファラデー効率測定（GCで定量したクロスカップリング体モル数 / 投入電荷モル数）
  - NaI 0.33 equiv.（≈20 mM in 5 mL DMF）条件でのiR測定（EIS）と補正
* **注記**: B-6（V2=high/V3=medium、convergence 2/3、gap=low）、B-7（V1=V2=medium、2/3、gap=none）、B-8（V1/V3=medium、2/3）、B-18（V3=medium、1/3）。D4-3, D4-7に対応。

---

**SRG-3 [Selectivity mechanism absent from main text]**

* **Primary RI**: RI-03 [Unobserved explanatory] — この論文の中心主張である「クロス電子求電子剤選択性」の機構的説明（速度論的 vs 熱力学的制御、Path I vs II）が主テキストに存在せず、実際に稼働しているメカニズムが観測されていない
* **Secondary RI**: RI-05 [Qualitative overread] — 「濃度差と電気化学的特性の差」という定性的記述から選択性の定量的根拠が引き出されている（B-3）
* **ER**: クロス選択性の定量的モデル（速度論的 vs 熱力学的制御の実験的判別を含む）を主テキストに提示し、Path I（Ni(0)→ラジカル）とPath II（Ni(II)→Ni(I)→Ni(III)）を識別する定電位電解実験を提供すること。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**:
  - 独立したNi(0)起点の反応（Path I: −2.74 V定電位）とNi(II)起点の電気化学的還元（Path II: −2.09 V定電位）を分離し、それぞれのクロス/ホモ選択比を測定（分割セル使用）
  - 異なる1°/2°濃度比（1:1〜1:6）での選択性の定量的依存性を速度定数として表現（kinetic simulation; GitHubコードが既存）
  - SIの選択性モデル定量分析の主テキスト統合（または主テキストへの適切なサマリー移行）
* **注記**: A-1（V2=high、1/3）、B-3（V2=high、1/3）、U-1（V2=high、1/3）。low_convergence_high_gapクラスターとして最高priority。D4-1に対応。自己矛盾的不在チェック：Ni(I/II/III)サイクルが提案するクロス/ホモ速度比がFig. 4bデータから検証可能だが未実施（→CLA-2参照）。

---

**SRG-4 [DFT methodology and validation gaps]**

* **Primary RI**: RI-04 [Unreplicated discriminator] — DFT計算値（Ni(I)/Ni(0) = −2.38 V）という単一計算値を実験SWV値との比較（360 mV乖離）を議論しないまま電気化学的アクセシビリティの証拠として使用（B-13, U-2）
* **Secondary RI**: RI-06 [Imported model] — DFT計算モデル（汎関数・溶媒和モデル・分散補正）の対象系（Ni-terpyridine/DMF系）への同型性実証が主テキストに不在（B-4, B-5）
* **ER**: DFT計算の汎関数・基底関数系・分散補正・溶媒和モデルを完全に報告し、計算ポテンシャルと参照電極を統一したSWV実験値との比較を行い、360 mVの不一致を定量的に議論すること（参照電極変換係数の算定を含む）。
* **EP**: EP-04a [Discrimination / replication pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**:
  - 参照電極をAg/AgNO3（またはFc/Fc⁺）に統一した全CVおよびSWV測定の再取得（B-2解消）
  - DFT方法論の完全記載（例：SMD溶媒モデルDMF, ε=37.219; M06-2X/def2-TZVP or similar; DFT-D3補正）
  - 360 mV不一致の考察：(1)参照電極変換係数の算定、(2)DFTの系統誤差の既報推定値との照合、(3)動的溶媒和効果の影響
  - 既報Ni-terpyridine錯体のDFT計算値と本系の比較による方法論の妥当性検証
* **注記**: B-4（V2=high、1/3、low_convergence_high_gap）、B-5（V2=medium、1/3）、B-13（V2=medium、1/3）、B-2（V3=high、1/3）、U-2（severity medium）。RI-04 + RI-06共起パターン（→§6参照）。D4-4に対応。

---

**SRG-5 [Radical mechanism validation incomplete for primary halide]**

* **Primary RI**: RI-07 [Unsupported boundary] — 一次アルキルハライドもラジカル機構を経ると主張しているが、一次ハライド固有のラジカル証拠が不在（全ラジカル実験が二次ハライドを基軸）
* **Secondary RI**: RI-04 [Unreplicated discriminator] — ラセミ化実験（単一の二次基質58bのみ）という単一データから両カップリングパートナーへのラジカル機構一般化
* **ER**: 一次アルキルハライドを基質とした独立したラジカルトラッピング実験（TEMPO捕捉）またはラジカルクロック（一次アルキルラジカル再編成）を実施し、一次ハライドのラジカル中間体を直接実証すること；質量収支を閉鎖すること。
* **EP**: EP-07a [Boundary-test pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**:
  - 一次アルキルブロミド（例：1-bromooctane）を基質とするTEMPO捕捉実験（完全質量収支：クロスカップリング体＋TEMPO付加体＋未反応SMの定量）
  - シクロプロピルメチルブロミドを一次ハライドとして使用したラジカルクロック（開環体と直接カップリング体の両収率報告）
  - 二次ハライドと一次ハライドそれぞれに対する独立したラセミ化実験（一次ハライドに適用可能なキラルプローブ基質の設計）
* **注記**: B-10（V1=medium/V2=high、convergence 2/3、gap=low）、B-11（2/3、gap=low）、B-12（V2=medium、1/3）。D4-5に対応。high_convergence_low_gap。

---

**SRG-6 [Substrate class condition variations unexplained]**

* **Primary RI**: RI-05 [Qualitative overread] — 配位子スクリーニングの定性的観察（「L6/L11が有効」）から基質クラス別の「一般戦略」成立という含意を導出
* **Secondary RI**: RI-07 [Unsupported boundary] — 「一般戦略」と主張しつつ、条件変更の原理的根拠なしに暗黙の基質クラス境界が存在
* **ER**: 各基質クラス（1°–2°、1°–1°、2°–2°、1°–3°）でL2/DMFが失敗する原因を電気化学的・速度論的根拠から説明し、配位子変更の合理的設計原理を提示すること。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-07a [Boundary-test pack]
* **Case-specific実装**:
  - L2, L6, L11それぞれのSWVによる酸化電位測定と各基質クラスでの収率–電位相関
  - 2°–2°カップリングにおけるL2/DMF条件での主副生成物プロファイル報告（なぜL2が2°–2°で機能しないかの電気化学的根拠）
  - 三級臭化物の低収率（42–47%）に対する追加最適化試験（電流密度、溶媒、配位子の変数分離）
* **注記**: A-2（V1=medium、1/3）、B-16（V1=medium、1/3）。フォールバック規則(c)適用。D4-6に対応。

---

**SRG外：CLA**

**CLA-1 [Gram-scale yield erosion mechanism]**

* **Primary RI**: RI-01 [Reporting integrity] — グラムスケール条件（50 mA, 24 h）が標準条件（5 mA, 12 h）から不連続に変更されており収率低下（3: 85%→69%、49: 72%→61%）の原因が未記載（B-17）
* **Secondary RI**: RI-03 [Unobserved explanatory] — 電流密度10倍増加が拡散層・電流分布・局所加熱に与える効果が観測・評価されていない
* **ER**: 電流密度（5, 10, 25, 50 mA）の系統的スキャンを化合物3の収率でモニターし、収率–電流密度曲線を作成する；スケールアップ設計原理（電極面積/溶液体積比一定の条件）を明示すること。
* **EP**: EP-01a [Reporting-coherence pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: 電流密度の段階的変化実験（5→10→25→50 mA）＋chronopotentiometryによる各電流密度での電位–時間プロファイル取得
* **注記**: B-17（V1=V3=medium、convergence 2/3、gap=none）。D4-8に対応。D-1の「実用的スケールアップ可能」主張に直結。

**CLA-2 [自己矛盾的不在: Ni(I/II/III)サイクルから導出可能な速度式の不在]**

* **Primary RI**: PRI-11 [Mechanism-kinetics decoupling]（暫定コード） — 提案されたNi(I/II/III)触媒サイクルから速度式を代数的に導出せず、Fig. 4bの定量的速度論データ（[1]または[2] vs [Δ3]/Δt）との照合が実施されていない
* **Secondary RI**: RI-03 [Unobserved explanatory]（Available-but-unutilized characterizationサブタイプ） — 速度論データが取得・図示されているが、サイクルの検証に利用されていない
* **ER**: 提案されたNi(I/II/III)サイクルの各素反応から全速度式を代数的に導出し、Fig. 4bの速度論データへのfitting（rate constants抽出）を実施し、サイクルの定量的整合性を示すこと。
* **EP**: EP-03a [Direct-observation / state-assignment pack]（EP-10a相当の暫定実装）
* **Case-specific実装**: Kinetic simulationコード（GitHub既存）を使用し、Ni(I)/Ni(II)/Ni(III)各状態の定常状態近似から速度式を導出 → Fig. 4bデータへのfitting → Ni(I)+1° vs Ni(I)+2° radical addition速度定数の比として選択性を定量化
* **注記**: U-1（V2=high、1/3）、B-9（V2=medium/V3=high、2/3）との連動。Breitenfeld 2014での先行確認に加えて、本論文が独立2報目として機能しPRI-11の昇格に貢献（→§6参照）。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation) 通過 / VQ-2 (Method) 未達**

**VQ-1 (Observation) は通る。**
主要クロスカップリング生成物の構造はNMR・MS・典型的合成化学的特性評価で確認されており、CCDC 2285024のX線結晶構造も取得済み（B-23）。[Ni/L2]錯体を直接使用した対照実験（83%収率）により触媒系の同定は十分。RI-02は実質的に解消されており、VQ-1通過の要件を満たす。

**VQ-2 (Method) は未達。**
必須解消項目RI-01とRI-07がいずれも重大に残存する。RI-01（SRG-1）：全スコープ単離収率のみ・収率計算基準混在（B-15）・再現性不在（B-14）が複合する。これらはNon-fatalな要素（全スコープGC収率は慣行的省略）を含むが、収率基準混在と再現性の完全不在はRI-01の構造的残存として致命的。RI-07（SRG-5, SRG-6）：一次ハライドのラジカル機構という境界主張を支持する一次ハライド固有の実験証拠が不在（SRG-5）、かつ「一般戦略」を標榜しながら基質クラス条件変更の原理的根拠が不在（SRG-6）。RI-07は合成スコープ主張の境界画定に直結しており致命性あり。

VQ-1通過を前提に、VQ-2はRI-01とRI-07の両解消が必要であり、現状では未達。

**ただし合成スコープ層（層2）単独では：**
90以上の基質で単離収率・レイトステージ修飾・グラムスケール合成が実証されており、これは合成有用性の直接的証拠として実質的にVQ-2 (qualified) に相当する。RI-01残存がNon-fatalと判断される範囲での層別VQ非対称性が存在する。

**VQ-3 (Mechanism) は未達（参考）。**
必須要件のRI-03（SRG-2: 稼働電位未測定; SRG-3: Path I/II未判別）、RI-04（SRG-4: DFT単一計算値の360 mV乖離未議論）、RI-06（SRG-4: DFT計算モデルの同型性実証なし）がすべて残存。VQ-2未達のため、VQ-3は継承原則により未達。RI-05（SRG-3のSecondary RI）が重大に残存するため、VQ-3が達成されたとしても「VQ-3 (qualified)」となる。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1**（全スコープ単離収率のみ）: Nature Catalysis 2024のArticle形式では、90+基質スコープのGC収率を全主テキストに記載することは紙面制約上非現実的であり、SI参照が当時の慣行。
- **B-4, B-5**（DFT計算詳細の主テキスト不在）: 計算化学的詳細（汎関数、基底関数系、分散補正）のSI記載は2024年においてジャーナル標準であり、主テキストへの全詳細記載は不要とされている。
- **B-14**（反復測定不在）: 合成化学系論文において、単一の代表収率を報告することは2024年においても広く許容されており、全報告化合物の三連測定は一般的な過剰要件。
- **B-9**（速度論データの非定量的解析）: 「概念実証」レベルの動力学実験でグラフを速度定数の代わりに提示することは、合成化学系Nature Catalysis論文の2024年時点の慣行として許容範囲内。

**modern-era deficient:**

- **B-3**（選択性モデルのSI委任）: 論文の中心的主張である「クロス選択性」の定量的機構説明が主テキストに存在しないことは、2024年の機構化学・Physical organic chemistry標準では致命的不足。SIの内容が主張の核心を担う場合に主テキスト省略を許容するgenre conventionは、機構化学コミュニティには適用されない。
- **B-2, B-13, U-2**（参照電極不統一・DFT vs SWV 360 mV不一致未議論）: 電気化学データの参照電極統一と計算値–実験値乖離の定量的議論は、2024年の電気有機合成論文の現代的基準では必須。2015年以前の電気有機合成論文では許容されていたが、現代ではmodernly deficient。
- **B-8**（ファラデー効率未報告）: ファラデー効率は2024年の電気有機合成論文では標準的報告事項となっており、不在は現代的に不足。

**両タグ（当時は許容されたが現代では不足）:**

- **A-1**（Path I/II判別実験の不在）: 機構の代替経路が「排除できない」状態のまま合成化学系通信論文が成立することは、2022–2024年の合成化学系Nature誌論文では慣行的に許容されてきた（合成スコープを主軸とするgenre convention）。しかし現代の機構有機化学・電気化学の再認定基準では、実際に稼働している経路の実験的判別は必須要件とみなされる。

---

### §5 最短補強ルート

**目的関数1: VQ-2達成**（必須解消: RI-01, RI-07）

**VQ-2 への最短ルート：**

1. **EP-04a [Discrimination / replication pack]** — 一次アルキルブロミドを使用したTEMPOトラッピング実験（完全質量収支付き）およびラジカルクロック実験（開環体＋直接カップリング体の両収率）を追加実施。RI-07（SRG-5）を前進。情報利得大（単一実験セットでSRG-5の複数B項目を同時に解消）。

2. **EP-07a [Boundary-test pack]** — 2°–2°カップリングにおけるL2/DMF条件での主副生成物プロファイル報告（失敗事例の明示）と、L6への切り替え根拠（SWVによる配位子酸化電位比較）を追加。RI-07（SRG-6）を前進。

3. **EP-01a [Reporting-coherence pack]** — 代表的基質10–15例についてGC収率と単離収率を併記し収率計算基準を統一（SIへの移行可）；TEMPO実験とラジカルクロック実験の完全質量収支報告。RI-01（SRG-1, CLA-1）を部分前進。

認定ゲート順注記: 実験投入はRI-07解消（EP-04a, EP-07a）→RI-01解消（EP-01a）の順が情報利得順だが、最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4のゲート順で確定する。VQ-2はRI-01とRI-07の両解消が必要であり、片方のみの解消では認定されない。

---

**目的関数2: VQ-3達成**（VQ-2達成後の必須解消: RI-03, RI-04, RI-06）

**VQ-3 への最短ルート：**

4. **EP-03a [Direct-observation / state-assignment pack]** — 定電流電解中のchronopotentiometryによるカソード電位直接測定；Fe板アノードのmatched-pair対照実験（カソード固定）。RI-03（SRG-2）を前進。情報利得最大（SRG-2全B項目を同時前進させる）。

5. **EP-03a [Direct-observation / state-assignment pack]** — Path I vs IIの判別実験：定電位電解（Ni(0)形成電位固定 vs Ni(II)還元電位固定）による経路分離実験；Ni(I/II/III)サイクルからの速度式導出とFig. 4bデータへのfitting（CLA-2解消）。RI-03（SRG-3）とPRI-11（CLA-2）を同時前進。

6. **EP-06a [Analogy-validation pack]** — DFT計算方法論の完全開示（汎関数・溶媒和モデル・分散補正）；参照電極統一後の実験値との360 mV乖離の定量的考察；既報Ni-terpyridine錯体との比較。RI-06（SRG-4）とRI-04（SRG-4）を同時前進。

認定ゲート順注記: VQ-3認定はVQ-2達成を前提とし、継承原則に従いRI-01, RI-07の解消がVQ-2水準で確定した後でなければVQ-3水準は認定されない。RI-05（SRG-3 Secondary）が残存する場合、VQ-3は「VQ-3 (qualified)」となる。

---

### §6 制度設計への寄与

**1. PRI-11（Mechanism-kinetics decoupling）昇格の第2独立確認**

本論文のCLA-2において、提案されたNi(I/II/III)触媒サイクルから速度式を代数的に導出せず、Fig. 4bの定量的速度論データ（[1]または[2] vs [Δ3]/Δt）への照合が実施されていないというPRI-11パターンが確認された。Codebook v0.2a注記が「Breitenfeld 2014で提案、Pengfei 2024で同型パターン確認」とすでに記録しており、本分析はこれを独立的に裏付けた。特筆すべきは本論文がKinetic simulationコードをGitHubで公開していること（Code availabilityに記載）であり、速度定数抽出が技術的に実施可能であったにもかかわらず未実施であるという「取得済みデータの未活用（RI-03: Available-but-unutilized characterizationサブタイプ）」の典型例を提供している。PRI-11は2報の独立確認を満たしており、RI-03の関連コードから独立した正式コードへの昇格が支持される。

**2. RI-04 + RI-06共起パターンの新事例（SRG-4）**

SRG-4において、DFT単一計算値の実験値乖離未議論（RI-04）とDFT計算モデルの対象系への未検証輸入（RI-06）が共起している。この共起では「RI-04の解消（追加計算による値の信頼性評価）」と「RI-06の解消（同型性の実証）」の両方が必要であり、どちらか一方では不十分。共起の構造：RI-06未解消ではDFT計算モデルの対象系への適用が正当化されないため、RI-04（実験値との比較）をいくら精緻化しても、計算値そのものの信頼性が担保されない。SRG-4はRI-04 + RI-06共起の典型的事例として記録する。

**3. 標識不整合（Labeling mismatch）パターンの確認**

機構記述において「reductive elimination via dialkyl–Ni(III) complexes is preferred」という事実的記述語が使用されているが、根拠はDFT計算のみであり直接的な機構実験では未確認。著者は「postulated」「based on DFT calculations...it is postulated」という仮説標識を前半文に集約するが、結論文では事実的記述語に移行している（仮説標識の前半集約パターン）。これはRI-06（Imported model）と連動する標識不整合の典型例として記録する。

**4. Era-Norm境界条件の新事例**

A-1（Path I/II判別実験の不在）が「合成化学系通信論文では慣行的に許容 / 現代機構基準では不足」の両タグ対象となったことで、VQ-3境界条件運用の有用な事例を提供する。合成スコープを主軸とするgenre conventionのもとでの機構的曖昧性の「許容」と、それが現代の機構有機化学的再認定でmodernly deficientとなる境界を示す事例として記録する。この境界条件は、同様のNi触媒電気化学的カップリング論文の評価に汎用的に適用できる。

**5. 新PRI候補**

本ケース固有の新PRI候補は特に検出されなかった。CLA-1（グラムスケール収率低下の電気化学的説明不在）はRI-01とRI-03の既存コードの組み合わせで記述可能。本ケースは制度設計における既存の複数RI/PRIパターンを追加確認・精緻化した。
