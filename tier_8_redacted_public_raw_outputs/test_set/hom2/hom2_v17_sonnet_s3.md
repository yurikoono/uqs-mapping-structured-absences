```
prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Shirai, Migitera, Nakajima, Kumamoto 2024（J. Org. Chem. note）

### §1 Claim Architecture

**コア主張：**
本論文は、Pd(OAc)₂/CsF/PMHS系を用いたAQ配向型還元的Heckヒドロアリール化を室温で達成し、ヒドロシランを水素化物源とする遅い添加プロトコルにより競合するSi–Pd^II–H経路を選択的に抑制することで、従来法（>100 °C、アミン/アルコール水素化物源）の三つの欠点（高温要件・極性官能基不適合・還元感受性置換基不耐性）を克服したと主張する。**Novelty柱**は(a)室温反応性、(b)拡張された官能基許容性（アミノ、ヒドロキシ、ブロモ、OBn、ニトロ等）、(c)二重触媒サイクルモデル（重水素標識による）、(d)遅い添加プロトコルという設計原理の四層。**Utility柱**は「実験室・工業合成への有用性」と、FDA承認医薬品（サクビトリル、ベナゼプリル、クロランブシル）の脂肪酸アルキルアレーン骨格への合成的アクセス。

**Layered structure 判定：**
三層構造で相互依存性は非対称。(a)合成層（室温反応性）と(b)スコープ層（官能基許容性）は依存関係あり——(a)が崩れれば(b)の文脈も失われる。(c)機構層（二重サイクルモデル）は(a)(b)から独立——合成結果は機構モデルの正否によらず成立し得る。(d)設計層（遅い添加）は(a)(b)に実験的に紐付くが、その機構的根拠は(c)に依存しており部分的な相互依存がある。単一の証拠（例：重水素実験の否定的再評価）で(c)は崩れるが(a)(b)は残る構造であり、各層は独立に評価可能。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Mass balance incompleteness]**（B-1, B-2）

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: 収率比較・副生物抑制効果の主張には完全なマスバランスが必要；Entry 12の6%欠損・Entry 13の7%欠損は、遅い添加による「副生物の減少」という核心主張の定量的根拠を不完全にしている。
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific実装**: Entry 12/13両条件でGC-MSまたは^1H NMR（完全スペクトル積分）による全成分（3aa, 1b, 1c, 1a, PMHS由来副生物）の定量化；全成分の合算が100±5%に収まることを示す。
* **注記**: B-1, B-2ともにhigh_convergence_low_gap（V1=medium, V3=high; convergence 2/3; gap=low）。マスバランス欠損は遅い添加プロトコルの合理性を支える定量的根拠の弱点に直結。

---

**SRG-2 [Side cycle evidence inadequacy]**（A-1, U-2）

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: 二重触媒サイクルモデルの有効性は、添加速度を独立変数として変えたときにδ位重水素取り込み比率が変化することを実験的に示すことを要件とする；現状では遅い添加条件下の単一重水素実験のみ。
* **EP**: EP-04a [Discrimination / replication pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: (1) Entry 12相当の速い添加条件（Si-H一括添加）でEt₃SiD実験を実施し、δ位D取り込みが遅い添加条件（0.2D）から統計的に有意に増加することを確認；(2) ベンジル-Pd中間体IX（側鎖サイクルの提案中間体）の捕捉または速度論的証拠（クロスオーバー実験等）。
* **注記**: A-1はhigh_convergence_low_gap最重要項目（V1=high, V2=critical; convergence 2/3; gap=low）。U-2はself-contradictory absence（論文が予測するfast-addition条件での比較実験が存在しない）。このSRGがD-4候補1の核心。

---

**SRG-3 [Deuterium experiment reliability]**（A-4, B-7）

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: 機構的割り当てに用いる重水素取り込み値（0.8D, 0.2D）は、^2H NMR取得法・複数回測定・H/D交換コントロール・不確かさ範囲を伴って報告されなければならない；特に0.2Dは^1H NMR積分誤差（±5–10%）の範囲内に収まりうる値であり、追加検証なしに機構的結論の根拠とできない。
* **EP**: EP-08a [Replication / uncertainty pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: (1) ^2H NMRによるD取り込み定量化（定量^1H NMRに対する独立検証）；(2) AQ-アミドのN-D結合から反応媒体（AcOEt, CsF, PMHS）へのH/D交換の時間経過測定；(3) 同一条件での3回以上の繰り返し実験。
* **注記**: B-7はhigh_convergence_low_gap（V2=high, V3=high; convergence 2/3; gap=none）。A-4はhigh_convergence_low_gap（V1=medium, V2=high; convergence 2/3; gap=low）。KIE測定（プロトデパラジネーションとトランスメタル化の競合速度比）が論文自身のA-4デファラルに対応する最短補強経路。

---

**SRG-4 [Dropped Quantitative Benchmark / yield comparison]**（B-5, C-1）

* **Primary RI**: RI-09 [External superiority]
* **ER**: "comparable to or higher"という性能主張は、同一基質・同一収率指標での直接比較データを要件とする；Figure 1で数値付きで引用された先行研究の収率範囲（γ位58–97%、δ位41–86%等）は、結果・考察部での対照実験を必要とする。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: 先行研究（refs 16, 18, 19, 20）が報告した代表的な基質（例：1-undecene + 4-iodotoluene相当）を本条件と先行条件（高温・アミン水素化物源）の両方で実施し、単離収率・選択性・副生物比率を直接比較。
* **注記**: B-5はhigh_convergence_low_gap（V1=high, V3=medium; convergence 2/3; gap=low）。C-1はDropped Quantitative Benchmark。B-5↔C-1ピボットがpriority_structureの第三の軸。

---

**SRG-5 [Table 1 correction identity]**（B-6）

* **Primary RI**: RI-01 [Reporting integrity]
* **ER**: 定量的データ表への事後訂正は、変更された値を特定し変更前後の値を示すchangelogを要件とする；特に、Entry 12（21%）とEntry 13（82%）という機構的仮説の定量的根拠となる値が訂正対象かどうかが不明な場合、主張全体の追跡可能性が損なわれる。
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific実装**: DOI-linked correction noteに「Corrected value: Entry [N], [field], from [X%] to [Y%]」という形式で具体的に特定；JOC ASAP訂正ポリシーの文書化に従って修正版と原版の差分を明示。
* **注記**: B-6はhigh_convergence_low_gap（V1=medium, V3=high; convergence 2/3; gap=low）。Table 1 Entry 12/13の値の真正性はCLA-1（内部標準信頼性）問題と連動する複合RI-01事象。

---

**SRG-6 [Excess PMHS contradicts dual-cycle model]**（B-8, U-1）

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: 二重触媒サイクルモデルの予測（総PMHS量が多いほどSi–Pd^II–H経由の副生物1b/1cが増える）は、脚注b/c/d条件の基質全てについて副生物収率を報告することで検証される必要がある；現状では予測と矛盾しうる条件が副生物データなしに提示されている。
* **EP**: EP-04a [Discrimination / replication pack]
* **Case-specific実装**: 脚注b（3.1当量PMHS/9h）・c（4.1当量PMHS/12h）条件の基質について、標準条件（2.0当量PMHS/6h）との副生物比率（1b/1c）を直接比較；PMHS当量-副生物収率の相関プロット（モデル検証）。
* **注記**: B-8はmixed（intentional_narrowing + reporting_omission）。U-1はself-contradictory absence。SRG-2との連結が強く、両SRGが共にA-1に帰属する。

---

**SRG-7 [CsF role uncharacterized]**（B-11）

* **Primary RI**: RI-03 [Unobserved explanatory]
* **ER**: 反応において複数の役割を担いうる試薬（CsF: フッ化物活性化剤 vs ブレンステッド塩基）は、その役割を分離する実験なしに機構的記述の根拠とできない；特に、プロトデパラジネーションや配位子交換に関与する可能性のある塩基性機能の寄与が未分離。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: (1) CsFの代わりにTBAFまたはKF（フッ化物のみ）で反応を実施し、収率・副生物比率を比較；(2) CsFの代わりにK₂CO₃（塩基のみ）での実施；(3) CsF当量最適化データの詳細開示。
* **注記**: B-11はhigh_convergence_low_gap（V1=low, V2=medium; convergence 2/3; gap=low）。独立SRGとして記録するが、VQ-3到達への優先度は中。

---

**SRG-8 [Unexplained scope anomalies]**（B-4）

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: 引用した理論的予測（Thorpe-Ingold効果）と観察が逆転する場合、その観察を「スコープ注記」として通過させるためには少なくとも代替説明の提示か明示的な機構的疑問としての記録が必要である；内部アルケン＞末端アルケンという挿入速度論との矛盾も説明を要する。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: (1) 分岐鎖基質（3fa, 3ga, 3ha）と非分岐鎖基質の速度比較実験（初速度法）；(2) 内部アルケンと末端アルケンの競合実験（同一条件・同一基質アクセプターとの等モル混合）；(3) DFTによる5-/6員パラダサイクル形成のエネルギー差推算。
* **注記**: B-4はhigh_convergence_low_gap（V1=medium, V2=medium; convergence 2/3; gap=none）。D-4候補6（γ/δ選択性の速度論/熱力学フレーム）に直接接続。

---

**SRG外：CLA**

**CLA-1 [Analytical validity of NMR yields]**（B-3）

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: NMR収率の信頼性根拠として、内部標準の反応条件下での安定性確認（回収率試験）は現代の有機化学報告における基本要件である；ジベンジルエーテルがPd(OAc)₂/PMHS/CsF/AcOEt系（r.t., 24h）で定量的に回収されることを示さなければ、全収率データが系統誤差を含む可能性が排除できない。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: ジベンジルエーテル（標準量）を標準条件（PMHS 2.0当量/CsF 2.0当量/Pd(OAc)₂ 10 mol%/AcOEt/r.t./24h）に添加し、反応後の回収率を^1H NMRで定量；±5%以内の回収を確認。さらに少なくともEntry 12・13・3つの代表的スコープエントリーを3回繰り返し標準偏差を報告。
* **注記**: D-4候補3（NMR内部標準信頼性）に直接接続。Table 1のEntry 12/13という核心データ点の信頼性に関わり、VQ-2の継続課題として実質的。

---

**CLA-2 [Utility claim vs experimental scope]**（B-10, U-3）

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: 「実験室・工業合成への有用性」という主張は、実際に使用されたアリールハライド（ArIのみ）の限定性、高触媒量（10 mol% Pd）、遅い添加による長い反応時間（24–48h）、触媒再生効率の不確実性（U-3）を明示した上で成立しなければならない；ArBr/ArClを含まない適用範囲は工業的文脈において重要な制限。
* **EP**: EP-07a [Boundary-test pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: (1) ArBr基質（4-bromoanisole等）での反応試行（範囲確認または限界表明）；(2) 反応の時間経過モニタリング（in situ NMRまたは分時サンプリング）によるTON推移の可視化；(3) 遅い添加終了後（t=6h）と反応終了時（t=24h）でのPd黒析出・溶液色変化の記録。
* **注記**: D-4候補5・7の根拠項目。ArI限定（B-10）は「実用合成」主張の境界を定め、これが不記載である点がRI-07に該当。U-3はself-contradictory absence（遅い添加がPd再生を制限する可能性の未検討）。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Qualified)**

**VQ-1 [Observation] — 通る**
RI-02要件（生成物・触媒の構造同定）は有機合成ノート形式として充足している。目的アルキルアレーン生成物群（3aa等）は^1H/^13C NMR・HRMSにより同定されており、代替構造との区別が原理的に可能。重水素標識生成物（3aa-d1等）も重水素化度0.8Dの報告を含めて同定されている。Non-fatal残存：活性種Pd(0)の直接観測は未実施だが、これはRI-03問題であり、VQ-3水準で評価する。

**VQ-2 [Method] — Qualified（限定的通過）**
VQ-1通過を前提とする。RI-01（Reporting integrity）がCLA-1（ジベンジルエーテル安定性未確認）とSRG-5（Table 1訂正内容不明）の形で非致命的に残存する。RI-07（Unsupported boundary）がCLA-2（ArI限定の未記載）とB-12（失敗例未開示）の形で残存する。いずれも核心的方法論（PMHS/CsF/Pd(OAc)₂/r.t.でアルキルアレーンが生成する）の成立を根底から覆すものではないが、収率数値の定量的信頼性と適用範囲の境界の両方を制限するため「Qualified」とする。Qualified限定の理由：RI-01 CLA-1がEntry 12/13の核心数値に系統誤差を導入しうる点。

**VQ-3 [Mechanism] — 未達**
VQ-2（Qualified）を前提としても、RI-03・RI-04・RI-06がいずれも未解消。
- RI-03 [Unobserved explanatory]: Pd(0)活性種の直接観測なし（U-3）；CsF役割未区分（SRG-7）；チェーンウォーキング経由1b形成の実験的根拠なし（C-3）。
- RI-04 [Unreplicated discriminator]: 副サイクルの唯一の証拠である0.2D at δ は単一条件・単一実験由来で、添加速度を変えた場合の比較なし（SRG-2/U-2）；重水素値の不確かさ未記載（SRG-3）。
- RI-06 [Imported model]: フルオロシリカートトランスメタル化機構のPMHS/アルキル-Pd系への適用性未実証（C-4）；Thorpe-Ingold予測の逸脱が未説明（SRG-8/C-2）。
RI-05も注記：スコープ異常（SRG-8）において定性的な順位判断から機構的含意を導出しており、VQ-3はRI-05残存により完全版には至らず限定的となる。

**VQ-4 [Benchmark] — 未達**
VQ-3未達に加え、RI-08（全収率データが単一測定でありリプリケーション不在; SRG-3/CLA-1）、RI-09（先行研究との直接比較なし; SRG-4）ともに未解消。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-3（単回NMR収率）**: J. Org. Chem. Note（2024年）の形式として単回NMR収率の報告は現在も広く許容されており、全エントリーへの繰り返し測定を義務付けるガイドラインは同誌に存在しない。
- **B-12（失敗例の未開示）**: スコープノートにおいて全試行基質を開示する慣行は確立しておらず、正の結果のみ掲載することは2024年現在も多くの合成論文で標準的。
- **B-14（遅い添加の用量依存性データなし）**: 最適化データの開示範囲は著者裁量に委ねられており、最終条件のみの報告はノート形式で一般的。
- **B-13（EDG/EWG効果の定量的根拠なし）**: 置換基効果の定性的一般化はスコープ論文において慣用的な記述であり、この形式への要件はない。

**modern-era deficient:**

- **B-6（Table 1訂正内容の不特定）**: デジタル時代のDOIリンク訂正システム下では、変更値の特定なしの「corrections were made」という記述は再現性保証の観点から不十分であり、2024年現在は現代基準で不足。
- **CLA-1（内部標準安定性の未確認）**: Pd触媒と還元性シランを同時に含む反応系でのNMR内部標準（ベンジル骨格含有）の安定性確認は、現代の定量報告標準において最低限要求される検証項目として認識されつつある。
- **B-7（重水素値の不確かさ未記載）**: ^1H NMRからD取り込みを推定する場合の分析的不確かさの開示は、機構的割り当てに用いるデータとして現代基準では必須；0.2D at δというマージン値への言及がない点は現代基準で不足。
- **U-2（速い添加条件での重水素対照実験不在）**: 二重触媒サイクルモデルの中心的な定量的予測（速い添加→δ-D増加）を自己検証しないまま機構を提案することは、2024年のJ. Org. Chem. Note形式においても現代基準での機構論的主張として不足。

*両タグ該当項目：* B-3（単回NMR収率）はcommunication-era toleratedとしての慣行が2024年にも残るが、CLA-1（内部標準安定性）という派生問題は現代基準でmodern-era deficientに分類。「親行為の許容性（single-point yield）」と「その実践を成立させる前提の検証義務（internal standard stability）」が別個の評価軸を構成する事例。

---

### §5 最短補強ルート

**現在VQ: VQ-2 (Qualified)**

**第一目的関数: VQ-3 [Mechanism] への到達**

1. **EP-04a [Discrimination / replication pack]** — 速い添加条件（Si-H一括添加）でのEt₃SiD実験を実施し、δ位D取り込み比が遅い添加（0.2D）と統計的に有意に異なることを確認。同時にSRG-3の繰り返し不足も解消。 → **RI-04を前進（SRG-2, SRG-3の両SRGに作用）**

2. **EP-08a [Replication / uncertainty pack]** — ^2H NMRによる独立定量化、H/D交換速度測定（アミドN-DからAcOEtへのクロスオーバー確認）、繰り返し3回以上の誤差評価。 → **RI-08を前進（SRG-3, CLA-1に作用）**

3. **EP-03a [Direct-observation / state-assignment pack]** — CsF役割分離実験（TBAF/KF vs K₂CO₃置換試験）、チェーンウォーキング1b形成の同位体トレーサー実験（標識オレフィン使用）。 → **RI-03を前進（SRG-7, C-3に作用）**

4. **EP-06a [Analogy-validation pack]** — PMHS/アルキル-Pdでのフルオロシリカート形成の直接証明（^19F NMR, HMQC）；分岐鎖基質の初速度測定によるThorpe-Ingold境界条件検証。 → **RI-06を前進（C-4, SRG-8に作用）**

*（RI-05の抑制のため追加）:* 内部アルケン/末端アルケン競合実験により定性的スコープ記述を定量化。→ RI-05を抑制し、VQ-3の完全版到達が可能。

**第二目的関数: VQ-4 [Benchmark] への到達（VQ-3達成後）**

5. **EP-09a [Internal benchmark pack]** — 先行研究（refs 16, 18, 19, 20）が報告した代表的基質を本条件と先行条件（高温・アミン水素化物源）の両方で実施し、単離収率・副生物比率を直接比較。 → **RI-09を前進（SRG-4に作用）**

6. **EP-08a [Replication / uncertainty pack]（拡張）** — Table 1 Entry 12・13および全スコープ代表例の3回繰り返し単離収率報告；内部標準安定性試験（CLA-1）の完了。 → **RI-08を完全解消（SRG-3, CLA-1に作用）**

**VQ-2 Qualified → 完全通過のための並行補強:**
- **EP-01a [Reporting-coherence pack]** — Table 1訂正のchangelog公開（SRG-5）、マスバランス表完備（SRG-1）。 → **RI-01を解消**
- **EP-07a [Boundary-test pack]** — ArBr基質試行結果の開示（成功または失敗を明示）、失敗例のカテゴリ記述（B-12）。 → **RI-07を前進（CLA-2, B-12に作用）**

**認定ゲート順注記：** 実験投入順は情報利得順（EP-04a → EP-08a → EP-03a → EP-06a → EP-09a）だが、最終的な認定確定は継承原則に従い VQ-1 → VQ-2 (fully qualified) → VQ-3 → VQ-4 の順で行われる。EP-04aとEP-08aを完了してもRI-01（CLA-1, SRG-5）が残存する場合、VQ-2はQualifiedのままとなりVQ-3への継承が弱まるため、EP-01aによるRI-01解消を並行推進することを推奨する。

---

### §6 制度設計への寄与

**PRI候補提案 — 「単一実験二重経路割り当て」（PRI-11候補）:**
本論文は、一対の重水素実験（Et₃SiD, N-D-アミド）から「主サイクルへの割り当て（0.8D at γ）」と「副サイクルの存在証明（0.2D at δ）」という二つの独立した機構的主張を同時に導出している。この構造は (a) RI-04 [Unreplicated discriminator]（単一実験からの高位解釈）と (b) RI-03 [Unobserved explanatory]（提案中間体の未観測）が連動する複合パターンを形成しており、既存のRI-03・RI-04の組み合わせには収まるが、「一つの同位体実験で複数の競合経路を同時に主張する」という特定の形式には現行 Codebook に対応コードがない。独立2報での確認後に **PRI-11: Multi-pathway isotope overclaim** 候補として提案する（定義案：同位体標識実験1件から複数の競合経路への割り当てを同時に行う場合の過剰解釈）。

**RI-01の新事例 — デジタル訂正の追跡可能性問題:**
SRG-5（B-6: Table 1訂正内容不明）は、ASAP掲載と訂正版再掲載という現代的な電子出版ワークフローにおいて、訂正内容の特定がない場合に機構的議論の定量的根拠の追跡可能性が失われるという新パターンを示している。既存のRI-01は「報告単位・条件記述の不統一」として定義されているが、「デジタル出版訂正の不透明性」は同コードの拡張的適用事例として EP-01a [Reporting-coherence pack] のcase-specific実装に追記する価値がある。

**Era-norm境界条件の具体事例:**
B-3（単回NMR収率）はcommunication-era toleratedとして処理したが、内部標準安定性確認（CLA-1）は派生するmodern-era deficientな問題として区別した。これは「単一実践の許容性（single-point yield）」と「その実践を成立させる前提の検証義務（internal standard stability）」が別個の評価軸を構成することを示しており、Era-norm Annotation フレームワークにおける「親行為の許容性と補助検証の義務の分離」という判定技法の具体事例として記録する。

**既存RI/EP追加確認:**
- RI-09（SRG-4: "comparable to or higher"主張）は数値引用後の直接比較断絶という典型事例として Codebook の代表事例リストに追加可能。OI-013（Dropped Quantitative Benchmark）がRI-09の検出に直接対応していることを確認。
- EP-04a（速い/遅い添加の比較重水素実験）はSi-Pd系の速度論的パスウェイ制御研究における標準的case-specific実装として記録する。本ケースはSRG-2（添加速度制御による経路選択）という具体的な実験設計に対応した初事例。
```
