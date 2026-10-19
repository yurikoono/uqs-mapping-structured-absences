```
prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Wang et al. 2020（Chemical Science, Edge Article）

---

### §1 Claim Architecture

**コア主張（要約）:**

本論文は、Pd(II)触媒インドール酸化的Heck C–Hアルケニル化反応において、
スルホキシド・2-ヒドロキシピリジン（SOHP）リガンドが「位置選択性決定ステップを
C–Hパラジウム化からアルケン挿入にスイッチする」ことでC2選択性を実現したと主張する。

**Novelty柱**: (1) 合成事実柱 — 配位子制御による初のC2選択的酸化的Heck C–Hアルケニル化
（Table 2、18種超の基質スコープ）；(2) 配位子設計柱 — κ²-S,N配位型SOHPリガンドの
新設計クラス；(3) 機構概念柱 — 「後続官能基化ステップを配位子設計のターゲットにする」
という反応設計原理。

**Utility柱**: インドール骨格のC2位官能化は医薬・天然物合成に有用であり、
好気的（O₂終酸化剤）条件での実現は合成的有用性を持つ。

**Layered structure判定: あり（三層、独立的）**

第一層（合成的成果）はTable 2のC2選択的スコープ実証として独立して検証可能。
第二層（SOHP配位子設計）は第一層の事実が成立すれば第三層の機構が否定されても成立する。
第三層（挿入ステップスイッチ機構）はDFT + 実験証拠の両方を必要とし、第一・第二層とは
独立して反証可能。この三層構造により、機構（第三層）が疑問視されても合成的事実
（第一層）と配位子設計コンセプト（第二層）は残存する。ただし、三層のうち最も強い
Novelty柱は第三層（挿入ステップスイッチ概念）に存在するため、機構主張の検証密度が
最も重要な再認定対象となる。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [KIE/kinetic data package]**（B-5, B-12）

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-01 Reporting integrity
* **ER**: KIE値は測定プロトコル（競争実験 vs 独立速度測定）の明示、個別初速度値と
  不確かさの報告、および[Pd]/[indole]/[Cu(II)]/[O₂]依存性を含む完全な速度則の
  確立とともに初めて「C–Hパラジウム化が速度決定段階」の主張を支持できる。
* **EP**: EP-04a Discrimination / replication pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: N-メチルインドール + tBu-アクリレート / Pd(II)/L17 系で
  KIEを競争実験（同一フラスコ）と独立2-run測定の両法で独立測定し、三重複の
  初速度値（M s⁻¹）と標準偏差を報告する；同系で[Pd]₀、[indole]₀、[Cu(OTf)₂]₀、
  p(O₂)の各一点変化実験を行い全速度則次数を決定する。
* **注記**: TEMPERATURE_SUMMARYでhigh_convergence_low_gap（B-5: V1=medium, V2=medium,
  V3=high, convergence=3/3, gap=low）。B-12はV3単独（convergence=1/3）。
  B-5とB-12は「同じ速度論的証拠パッケージの前処理と後段の問い」として連鎖している。

---

**SRG-2 [DFT methodology quality]**（B-1, B-2, B-3, B-14）

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-01 Reporting integrity
* **ER**: 分散補正（D3BJまたは同等）の適用と非適用の影響評価、熱力学補正の
  計算レベル明示（B3LYP振動数 vs M06振動数）、主要4遷移状態（TS-1a/1b/2a/2b）の
  系統的コンフォメーション探索、および最適配位子L17での感度解析のうち少なくとも
  前三者が揃ってはじめてΔΔG‡≈5.9 kcal mol⁻¹を選択性証拠として評価できる。
* **EP**: EP-04a Discrimination / replication pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: B3LYP-D3BJ/6-31G(d) で再最適化し、M06//B3LYP-D3BJ
  単点計算との差異を報告する；各TSについてメタダイナミクスまたは系統的
  ダイヘドラル走査でコンフォメーション探索し最安定TS幾何を確認する；
  L17（SOHP本体）で主要TSを再計算しL13との差を報告する。
* **注記**: B-1は低収束高重大度（V2-Q2=high, convergence=1/3）；
  B-3はlow_convergence_high_gap（V2-Q6=high）；B-2はhigh_convergence_low_gap
  （V2=high, V3=medium, convergence=2/3, gap=low）。4項目の合計がSRG中最大。

---

**SRG-3 [Quasi-reversibility mechanistic evidence]**（B-6, U-1）

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-03 Unobserved explanatory
* **ER**: 「C2-パラジウム化の準可逆性」という機構主張を採るためには、
  Scheme 5右パネルの各時点でのD%値と測定誤差（NMR積分精度）、ならびに
  前進（k_f）・逆反応（k_r）速度定数をfitした速度論モデルが必要であり、
  少なくとも定性的時間経過の定量化が最低限の要件となる。
* **EP**: EP-04a Discrimination / replication pack; EP-03a Direct-observation /
  state-assignment pack
* **Case-specific実装**: Pd(II)/L17存在下で重水素標識N-メチルインドール（2-D）を
  用い、各時点（0–6 h）でのC2位およびC3位のD%を定量NMR（d₁≧60 s,外部標準）で
  三重複測定し、準可逆性モデルおよびC3プロトン化の一方向モデルの両方をfitして
  AICで比較する。
* **注記**: SRG-3はhigh_convergence_low_gap最上位（B-6: V1=high, V2=high, V3=high,
  convergence=3/3, gap=none）。U-1は「自己矛盾的不在」として記録されており、
  本SRGの項目は論文の機構主張が直接予測する実験データが報告されていないという
  最も深刻なRI-03例。

---

**SRG-4 [Table 2 scope data completeness]**（B-4, B-11）

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: C2-アルケニル化条件のスコープデータを「メソッド水準」で評価するためには、
  全エントリーに基質変換率・C3副生物収率・質量収支が必要であり、またNMR収率計算の
  内部標準と緩和時間パラメータが明記されることが必要。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: Table 2の全エントリーを再実験し、変換率（GC/内部標準）、
  単離C2収率、NMR C3収率、残査NMR収率を同一フォーマットで報告する；Table 1と
  同一の報告様式（変換率・収率同時記載）に統一する。
* **注記**: B-4はhigh_convergence_low_gap（V1=medium, V3=high, convergence=2/3,
  gap=low）。B-11はV3単独（convergence=1/3）。

---

**SRG-5 [Scope failure attribution and deferral]**（B-7, A-1, A-2）

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-07 Unsupported boundary
* **ER**: 「C2-パラジウム化困難」という失敗帰属を採るためには、対象基質での
  C–H活性化速度の定量的評価（KIE、化学量論実験、またはDFT）が必要であり、
  現状の「帰属なし提示」あるいは「C–Hパラジウム化困難」という定性的帰属は
  等価な挿入ステップ側の失敗説明を排除しない。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-07a Boundary-test pack
* **Case-specific実装**: アクリロニトリルでの化学量論実験（ノルボルネントラップ
  対照と比較）でC2-Pd-H中間体の生成をチェックし、挿入困難 vs パラジウム化困難を
  診断する；N-Ts-インドールの不反応理由をDFT（Nの配位モード変化）で調査する。
* **注記**: B-7はV1単独（convergence=1/3）。A-2はT2解釈水準のdeferral（内部不整合）。
  ピボット項目1（A-2 ↔ B-7）に該当：失敗の機構帰属がパラジウム化側に置かれることで
  「挿入ステップスイッチ」概念の成功基質限定適用というフレームが維持されている。

---

**SRG-6 [Catalytic cycle experimental grounding]**（B-10）

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-04 Unreplicated discriminator
* **ER**: 触媒サイクルにおけるCu(II)のHCl捕捉剤役割、β-水素化物脱離の
  選択性中立性、およびPd(0)→Pd(II)再酸化経路は、DFTのみによる割り当てでは
  説明変数として「使用不可」であり、少なくとも1つの対照実験（非酸化性塩基への
  Cu(II)代替実験）が必要。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a
  Analogy-validation pack
* **Case-specific実装**: Cu(OTf)₂を等モルのK₂CO₃またはEt₃Nに代替した反応を実施し、
  収率・選択性への影響を定量比較することでHCl捕捉説を実験的に検証する；
  Pd(0)→Pd(II)再酸化のターンオーバー頻度を酸化剤対照実験（O₂なし、Cu(II)なし）
  から切り分ける。
* **注記**: B-10はV1+V2収束（convergence=2/3, gap=none）。

---

**SRG-7 [Anomalous observation unaddressed]**（B-13, U-3）

* **Primary RI**: RI-08 Unquantified reliability
* **Secondary RI**: RI-04 Unreplicated discriminator
* **ER**: Table 1 entry 1（配位子なし）での10% C2生成が測定誤差範囲内かどうかを
  判定するためには、GC定量のS/N比と測定精度が必要であり、仮に有意であれば
  DFT（ΔΔG‡≈5.9 kcal mol⁻¹）との不整合を説明する必要がある。
* **EP**: EP-08a Replication / uncertainty pack; EP-04a Discrimination /
  replication pack
* **Case-specific実装**: 配位子なし条件のentry 1を三重複で実施し、C2生成物の
  有意性を統計的に検定する；有意であればDFTで配位子なし系の低バリア経路を探索する。
* **注記**: B-13はV1単独（convergence=1/3）；U-3は自己矛盾的不在として記録。

---

**SRG外：CLA**

**CLA-1: 速度論的制御 vs 熱力学的制御**（D-4候補3; grounded_in: U-2, B-6, B-5）

* **Primary RI**: RI-05 Qualitative overread
* **ER**: 「挿入ステップ制御によりC2選択性が生じる」という速度論的解釈を採るためには、
  C2-アルケニル化インドールとC3-アルケニル化インドールの相対的熱力学的安定性
  （ΔG°）を計算または実測し、速度論的制御と熱力学的制御の寄与を区別する必要がある。
* **EP**: EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: DFTでC2-アルケニル化生成物3bとC3-アルケニル化生成物3aの
  ΔG°を計算し、速度論的産物（より高エネルギー）vs熱力学的産物（より安定）の
  どちらがC2生成物かを明示する；必要であれば平衡条件（酸触媒、高温）での
  異性化実験でΔG°を実測する。
* **注記**: D-1の第三層（機構）の主張の完全性に直結；いずれのSRGにも属さない独立候補。
  U-2はV2-Q10に由来（medium）；B-6はhigh_convergence_low_gap（convergence=3/3）。

---

### §3 現在のVQ判定

**現在判定: VQ-2 Qualified（Method, 限定的）**

---

**VQ-1 Observation は通る（Non-fatal残存あり）:**
主要生成物（C2-アルケニル化インドール3b群、C3-アルケニル化インドール3a群）は
単離・NMR/MS/X線結晶構造で同定されており、RI-02の核心（生成物・触媒の構造同定）は
充足されている。非致命的残存：B-15（N-HインドールのN-Pdボンド形成可能性が排除
されていない）は主要生成物の同定精度に影響せず非致命的。

**VQ-2 Method は通る（Qualified）:**
VQ-1継承を前提に、RI-01（Reporting integrity）はTable 2の変換率・C3副生物収率・
質量収支の欠落（B-4, B-11）により部分的未解消だが、C2選択性の方向的主張（C2優先）
を覆さないため非致命的。RI-07（Unsupported boundary）は「C2-パラジウム化困難」
という帰属なし失敗提示（B-7, A-2）として残存するが、スコープの枠組み主張を
根底から否定しないため非致命的。ただし「限定的（Qualified）」とする：両未解消項が
スコープ評価の定量的精度を著しく制限している。

**VQ-3 Mechanism は未達（RI-03 Fatal）:**
VQ-2継承を前提に評価する。RI-03（Unobserved explanatory）は致命的：
本論文の機構的中心主張「C2-パラジウム化の準可逆性」は前進・逆反応速度定数の
導出を自己予測するが、それを可能にする定量的時間経過データが主本文にも
ESIにも報告されていない（B-6, U-1; SRG-3）。Cu(II)のHCl捕捉役割・Pd(0)/Pd(II)
再酸化経路も直接観測なし（B-10; SRG-6）。RI-04（Unreplicated discriminator）も
非致命的残存：KIE=3.3は単独値で誤差なし（B-5）、DFT PESは単一コンフォマー
（B-2）だが、証拠群の複合性がこれを非致命的に留めている。RI-05（CLA-1: 熱力学
制御非排除）が残存するため、仮にRI-03が解消されてもRI-05が残れば「VQ-3 Qualified」。

**VQ-4 Benchmark は未達（VQ-3未達のため継承不成立）:**
VQ-3が未達のためVQ-4の審査は成立しない。追記：RI-08（B-11, B-13 — 全Table 2
エントリーに反復なし）およびRI-09（C-2, C-3 — 先行基準値との数値比較なし）も
未解消であり、VQ-4への経路は複数のブロックを持つ。

---

### §4 Era-Norm Annotation

**communication-era tolerated（2020年・Chemical Science・Edge Article）:**

- **B-11**（GC/NMR定量条件・反復データ不在）: 2020年の合成化学ジャーナルでは
  スコープ表の全エントリーに誤差を付けない単一実験報告が広く受容されており、
  リガンド最適化テーブルの有意差判定基準の未記載は当時の標準的形式であった。

- **B-9**（ノルボルネン化学量論プローブの基質ミスマッチ）: 2020年のC–H
  官能化論文では、ノルボルネンをC–Cカップリング中間体のトラップ剤として
  使用する慣行が確立されており、基質ミスマッチへの指摘は現在より低頻度であった。

- **B-14**（DFT参照状態・Cu種の簡略化モデル）: 2020年時点でCu種の正確な
  溶液化学種モデリングは計算コスト的に希少であり、単純化されたCuモデルは
  許容された実践であった。

- **C-2, C-3**（先行文献の数値比較なし引用）: 背景先行技術の集合引用と
  数値非比較は2020年の合成化学論文の標準的な導入スタイルであった。

**modern-era deficient（現代再認定で不足）:**

- **B-6, U-1**（準可逆性の定量的速度論的検証不在）: 現代の機構論的有機化学の
  標準では、速度論的モデル（微分方程式fit）を添付しない定性的時間経過プロットは
  機構同定の証拠として不十分とされ、VQ-3の致命的未充足項目となる。

- **B-5**（KIEプロトコル・不確かさ未記載）: 現代では競争法 vs 独立測定法の
  区別は必須記載事項とみなされており、測定値のみの報告は再評価不可能として
  受理されない。

- **B-1**（分散補正の不適用）: 2022年以降のPd/π系DFTでD3BJまたは同等の
  補正なしの計算は現代審査で即指摘の対象となり、era-normとして報告当時（2020年）
  は移行期的に許容されたが現代再認定では不足とみなす。

- **B-2**（TS系統的コンフォメーション探索の記述なし）: 現代の計算化学報告
  基準では主要TS探索戦略の明示が必須であり、B-1とともにSRG-2の現代不足項目。

**両方に該当（当時許容・現代不足）:**

- **B-4**（Table 2変換率・C3副生物収率不在）: 当時はhighlight-style Edge Article
  として許容されたが（journal_constraint参照）、現代の方法論論文再認定では
  選択性主張に必要な最低限のデータとして分類される。両タグに記載。

---

### §5 最短補強ルート

**目的関数 第一: VQ-3（Mechanism）への最短ルート**

現在VQ-2 Qualified → 次目標VQ-3（RI-03, RI-04, RI-05の解消が必要）

1. **EP-03a** Direct-observation / state-assignment pack —
   定量NMRによる各時点D%測定（三重複）と速度論モデルfit（準可逆vs一方向を
   AICで比較）、およびCu(OTf)₂→K₂CO₃代替対照実験による Cu HCl捕捉役割の
   検証を実施する。RI-03（最致命項目）を前進させる。

2. **EP-04a** Discrimination / replication pack —
   KIEを競争法・独立2-run法の両方で三重複測定し個別速度値と標準偏差を報告する；
   TS-1a/1b/2a/2bの系統的コンフォメーション探索（メタダイナミクスまたは
   ダイヘドラル走査）を実施し最安定TSを確認する。RI-04を前進させる。

3. **EP-05a** Quantitative-ranking substantiation pack —
   DFTでC2生成物（3b）とC3生成物（3a）のΔG°を計算し速度論的制御の確認または
   熱力学的制御への関与を定量化する。RI-05（CLA-1）を前進させる。

→ EP-03a投入後にRI-03が解消され、EP-04aでRI-04が非致命的水準に軽減、
  EP-05aでRI-05（RI-05重大残存）が排除されれば VQ-3 到達（RI-05残存時はVQ-3 Qualified）。

**目的関数 第二: VQ-4（Benchmark）への最短ルート（VQ-3達成後）**

4. **EP-08a** Replication / uncertainty pack —
   Table 2全エントリーを三重複で追加実験し、変換率・C3副生物収率・標準偏差を
   報告する；異常値（entry 1の10% C2）を統計検定する。RI-08を前進させる。

5. **EP-09a** Internal benchmark pack —
   ref 13e（C3選択的基準値75%収率）および ref 18（DMSO系）と同一基質セットで
   直接数値比較実験を実施し、収率・選択性の両軸で対比表を作成する。RI-09を前進させる。

**前提: VQ-2 Qualified → VQ-2（脱qualified）**

EP-03a実施前の準備段階：
- **EP-01a** Reporting-coherence pack — Table 2に変換率・C3副生物収率・質量収支
  を追記し、GC内部標準と応答係数算出法、NMR定量条件（遅延時間・標準物質）を
  明示する。RI-01を前進させる。
- **EP-07a** Boundary-test pack — アクリロニトリルおよびN-Ts-インドールの
  失敗原因を化学量論実験・DFTで診断し「C2-パラジウム化困難」帰属の正否を
  確認する。RI-07を前進させる。

**認定ゲート順注記**: 実験投入順は情報利得の大きさ順（EP-03a > EP-04a > EP-05aを優先）
だが、最終認定は継承原則に従いVQ-1 → VQ-2 → VQ-3 → VQ-4のゲート順で確定する。
現在VQ-2 Qualifiedが起点であるため、EP-01a/EP-07aによるRI-01/RI-07の解消で
VQ-2（脱qualified）を確定した上でVQ-3審査に進むことが正式ルートとなる。

---

### §6 制度設計への寄与

**1. RI-04の典型事例提供（Unreplicated discriminator）:**
本ケースは、単一のKIE値（KIE=3.3）と単一のDFT PESという「識別力の高い単一データ」
が複数のhigh-severity B項目として現れ、VQ-3未達の主因を構成するRI-04の
代表的実例を提供する。特に「KIEの誤差なし・プロトコル未明示」と
「DFTのコンフォメーション探索なし」は、Pd(II)触媒C–H官能化論文において
繰り返し出現すると予想されるRI-04の具体的現れ方であり、このケースはCodebook
の事例集に収録すべき標準例となる。

**2. RI-03の「自己矛盾的不在」サブタイプの明確化:**
U-1（自己矛盾的不在）は、論文の機構提案が直接予測する実験データ（準可逆性
→ 速度定数）が報告されていないという特殊なRI-03例であり、「説明変数の
直接観測なし」という通常のRI-03より論理的重大性が高い。本ケースは
「提案機構が予測する定量値を論文自身が報告しないとき、RI-03は致命的になる」
という致命性判定の境界条件を具体化する。この境界条件をVQ判定基準マトリクスの
注釈として追加することを提案する：
「RI-03 Fatal条件の明示：論文の提案機構が特定の定量値を予測しており、
かつその値の報告も未報告の承認もない場合、RI-03は致命的とみなす」。

**3. 三層主張構造とVQ水準の層別対応:**
本論文の三層Novelty構造（合成事実 / 配位子設計 / 機構概念）において、
合成的第一層はVQ-2（限定的）水準に対応し、機構的第三層はVQ-3未達に対応する。
現状のVQ判定基準は「論文全体」への単一VQ付与を前提としているが、
主張が独立した複数層を持つ場合、層別VQ認定（例：VQ-2@Layer1, VQ-1@Layer3）
が情報量として豊かである。本ケースを起点に「Layered VQ notation」の
導入可能性を検討することを提案する。

**4. 新PRI候補の不要確認:**
本ケースで検出された全パターン（RI-01: Table 2報告不統一、RI-03: 準可逆性
速度論不在、RI-04: KIE/DFT単一データ、RI-05: 熱力学制御非排除、
RI-08: 反復なし）は既存RIコードの範囲内に収まる。PRI-10（Kinetic overclaim）は
B-12（速度則不完全）に適用できないことはないが、B-12はRI-04 + RI-01の
複合としてより正確に記述できるため、新PRI提案は不要。

**5. EP-03aのCase-specific実装例の追加:**
本ケースで設計したEP-03aの具体的実装（定量NMR時間経過 + 速度論モデルfitting）は、
Pd触媒C–Hパラジウム化準可逆性の再認定に汎用的に適用できるEP-03a実装例として、
EP辞書のcase-specific実装リポジトリに収録する価値がある。

```
