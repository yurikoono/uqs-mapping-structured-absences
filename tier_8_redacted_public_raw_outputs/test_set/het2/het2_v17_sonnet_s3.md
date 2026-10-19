```
prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Newton, Takle, Richardson, Hellgardt, Hii 2024（ACS Catalysis, full_paper）

### §1 Claim Architecture

**コア主張：**
本論文の中心的主張は二本柱からなる。**Novelty柱**：タンデム型連続フロー反応器（PBR→PFR）を改良し、F2インレットを持つコンフィギュレーション2によって、反応混合物の各成分（溶媒・基質・塩基）が個別に引き起こすPd溶出量を独立に評価できる実験プラットフォームを確立した。**Utility柱**：3種の市販不均一系Pd触媒（PdEnCat 30、FC-1001、Pd/Al₂O₃）に対して、NEt₃が高分子担持Pd(II)触媒からの溶出の主要因（30°Cでも182 ppm）であり、Pd/Al₂O₃は90°CのPhIのみによって溶出する「最も安定な触媒」であると同定した。これらの知見が「将来の触媒設計」を指針するという実用的訴求も含む。

**Layered structure（三層構造）：**
論文の主張は独立性が異なる三層で構成されている。
- **Layer 1（観察層）**：三種触媒の溶出量がICP-MS値として定量され、支持体タイプによって大きく異なる。反証はICP測定の改訂を要するが、「PdEnCat/FC-1001 > Pd/Al₂O₃」という定性的ランキングは単独で成立しうる。
- **Layer 2（方法論層）**：コンフィギュレーション2による成分ごとの溶出帰属。反証は成分実験の独立性（新鮮触媒床の確認、SRG-1）またはICP正規化の等価性（U-3、SRG-2）に依存する。Layer 1の崩壊なしにLayer 2が崩れる構造。
- **Layer 3（機構推測層）**：溶出Pd種の化学的実体（クラスターvs分子種）の推測、Scheme 2のPdEnCat/FC-1001への適用。著者自身が"speculate"と明記（A-1）。Layer 2を崩さずにLayer 3のみ崩せる。

Layer 2の中枢的弱点は「成分実験の相互独立性の未確認（U-1）」であり、これが未解消のままであれば、Layer 2全体が崩壊し、論文の主要定量的結論（"NEt₃は最大の犯人"）の信頼性は独立に評価できない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [成分帰属実験の独立性]**（B-3, U-1, B-2, B-7）

* **Primary RI**: RI-04 Unreplicated discriminator — 4成分実験の相互独立性（新鮮触媒床、温度ランプ非交絡、DMFバックグラウンド非減算）が未確認のまま、各実験の単一データ点が論文の中心的帰属結論を決定している。
* **Secondary RI**: RI-01 Reporting integrity — 実験独立性の確認情報（触媒床交換の有無、B-7のDMF背景値の扱い）が報告フレームから完全に欠落している。
* **ER**: コンフィギュレーション2の各成分実験（A: DMF、B: acrylate、C: PhI、D: NEt₃）が独立した新鮮触媒床で実施されたことの明示、DMFバックグラウンド（30 ppm）の他成分値からの減算、温度ランプ（30→90°C）の触媒状態変化に対する独立90°C実験での確認。
* **EP**: EP-04a Discrimination / replication pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: PdEnCat 30・FC-1001・Pd/Al₂O₃それぞれについて、4成分実験を独立充填触媒床で実施することを方法の節に明示する。コンフィギュレーション2実験D（NEt₃）の前に、触媒床を新規充填した対照実験を追加する。DMF単独（実験A）のICP値をB・C・Dの値から減算し、補正済みppm値で帰属結論を再導出する。
* **注記**: U-1（critical, V1+V3収束, gap=none）がhigh_convergence_low_gapの筆頭項目。B-3はU-1とlinked（同一不在事項の報告側・U側）。B-2（V1=high, V2=medium, 2/3収束, gap=low）は温度ランプ交絡として同SRG。

---

**SRG-2 [定量的Pd溶出データの有効性]**（B-5, B-6, B-17, B-21, U-3）

* **Primary RI**: RI-08 Unquantified reliability — ICP-MS値は全実験で単一ランのみ（no replicates）、検出限界・測定不確かさ・採取体積の正規化基準がすべて未開示のまま定量的比較の根拠として使用されている。
* **Secondary RI**: RI-01 Reporting integrity — コンフィギュレーション1（Figure 4B: 194 ppm）とコンフィギュレーション2（Figure 7D: 182 ppm）の直接数値比較が異なるリアクター構成・総流量・採取体積の下で行われており（U-3）、比較フレームが整合していない。
* **ER**: 各定量的結論（特にNEt₃ 182 ppm vs. 全成分混合 194 ppmの比較）に対して、採取体積・採取時間・総流量の一致確認または正規化補正を提示する。少なくとも鍵実験（PdEnCat 30 + NEt₃）についてn=2を提示し、6 ppm（Pd/Al₂O₃ + NEt₃）に対してICP-MSの検出下限を記載する。
* **EP**: EP-08a Replication / uncertainty pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: ICP-MSの測定不確かさをPd標準溶液の直線範囲内で±ppmとして主テキストに記載する。コンフィギュレーション1と2の採取体積・流量を揃えるか、体積補正係数を明示してppm値を等価基準に換算する（U-3の解消）。反応を3回繰り返す完全な複製は過重負担であれば、PdEnCat 30 + NEt₃実験（主要結論の根拠）のみ重複実験として優先する。
* **注記**: U-3（V3=high, 単一エージェント, low_convergence_high_gap）は論文の最強定量的結論を支える比較の正規化問題。B-5（Pd/Al₂O₃の「完全安定」主張と6 ppmの検出下限問題）はRI-08 + RI-04の複合。B-6（Pd質量収支不在）はRI-08の実装例。B-17（再現実験なし）はRI-08の直接事例（V3=high, 単一エージェント）。

---

**SRG-3 [反応器特性パラメータの主テキスト不在]**（B-18, B-19, B-20, B-4）

* **Primary RI**: RI-01 Reporting integrity — 流量・PBR体積・PFR体積・滞留時間・F2混合効率はS1/S2変換率比較の解釈の前提だが、主テキストから完全に欠落している（ESIに存在するが主テキスト非議論）。
* **ER**: 主テキストにF1・F2各流量、PBR・PFR容積、代表的滞留時間を記載する。F2混合接続部の混合特性（混合時間とリアクター内滞留時間の比較）を定性的に記述する。
* **EP**: EP-01a Reporting-coherence pack
* **Case-specific実装**: Experimental sectionの反応器記述箇所に流量（mL/min）・PBR充填量・PFR管容積・30°CおよびΔT後の滞留時間（min）を各コンフィギュレーションについて1表にまとめて記載する。ブレークスルー曲線を主テキストFigure 2（または等価な位置）に移動し、プラグフロー的挙動と定常状態確認の根拠として議論する。
* **注記**: B-4（コンポーネント濃度, V1=high, V3=high, 2/3収束）はコンフィギュレーション2で実際の反応濃度と同等かを確認するための前提。全4項目がhigh_convergence_low_gap候補（SRG-3全体）。

---

**SRG-4 [溶出Pd種の同定——機構対証拠]**（A-1, B-11, B-13, B-15, U-2）

* **Primary RI**: RI-03 Unobserved explanatory — 論文の最も野心的な主張（支持体タイプによって異なるPd種が溶出する）は、溶出種の酸化状態・配位環境・粒径分布の直接観測なしに変換率プロファイルの形状のみから導出されている。
* **Secondary RI**: RI-06 Imported model — PdO表面Pd/Al₂O₃にArI酸化的付加（Pd(0)前提）を仮定するScheme 2適用（U-2）は、Pd(0)ナノ粒子モデルを表面PdO系に検証なしに輸入している。
* **ER**: 溶出収集画分に対してESI-MS（分子種同定）またはDLS/TEM（ナノ粒子・クラスター確認）、あるいはoperando EXAFS（酸化状態確認）を行い、"クラスターvs分子種"という区別を直接的証拠で示す必要がある。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific実装**: 収集画分（特にPd/Al₂O₃ + PhI @ 90°C画分）のナノフィルトレーション（>1 kDa膜）または限外ろ過によって粒子性Pdと分子性Pdを分離し、各画分のHPLC変換率を比較する（Rothenberg 2006/2007の手法, refs 18/19の直接的引用に値する実装）。PdO表面Pd/Al₂O₃については、XPS（バッチ使用後の触媒再回収）またはoperando XANES（流通下）でPdO → Pd(0)還元の有無を確認する。FC-1001の異なるPd種推測（B-13）については、両画分を同一初期Pd濃度に希釈した上で同一時間軸で活性プロファイルを取り直す。
* **注記**: U-2（V2=high, 単一エージェント, low_convergence_high_gap）はPdO/Pd(0)機構矛盾。B-13はRI-04の複合（初期濃度非正規化の運動論的差異が「異なる種」の証拠として使用）。B-11（バッチ固有のPd/Al₂O₃表面特性未確認）はRI-02に該当。A-1（V1=medium, V2=high, 2/3収束, gap=low）がhigh_convergence_low_gapに位置。

---

**SRG-5 [α-ヒドリド脱離機構——適用可能性と温度パラドックス]**（A-2, B-12, U-4）

* **Primary RI**: RI-06 Imported model — Scheme 2（100°C、トリブチルアミン、裸のPd(OAc)₂条件で文献確立）を30°C・トリエチルアミン・ポリウレア封入Pd(OAc)₂（PdEnCat）およびphosphine配位Pd(OAc)₂（FC-1001）へ検証なしに輸入している。
* **Secondary RI**: RI-03 Unobserved explanatory — 低温でScheme 2が作動するとした場合に生じるべき中間体（Pd(0)錯体、エナミン副生物）が観測されていない。
* **ER**: 30°C条件でScheme 2の副生物（エナミン/イミニウムイオン、AcOH、またはPd(0)形成の分光学的証拠）を定量的に確認するか、あるいは別機構（不均化、直接配位子還元）の可能性を実験的に検討する。FC-1001については、ホスフィン配位がScheme 2の速度に及ぼす影響を記述する。
* **EP**: EP-06a Analogy-validation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: PdEnCat 30をNEt₃/DMFと30°Cで反応させた後の液相をNMRまたはGCで分析し、エナミン副生物またはAcOHの存在を確認する。同時に反応液相のUV-visまたはin situ XANES（Pd(0)のLSPR / 還元状態確認）を追加する。FC-1001については、ホスフィン解離なし・あり条件でNEt₃との反応速度を比較するか、³¹P NMRで溶出画分中のリン種を同定する。
* **注記**: A-2（suppressed, 三要件チェックリスト充足）がA-2↔U-4 linkedでlow_convergence_high_gap。U-4（V2=high, 単一エージェント）は論文が機構と観察の矛盾を"rather unexpected"と記録しながら解決しない構造的不整合。B-12はSRG-5の第三のサブ問いとして位置づけ（FC-1001のScheme 2適用の構造的問題）。

---

**SRG外：CLA**

**CLA-1: 個別成分効果の非加算性と協同効果の定量化**

D-4候補5由来（grounded_in: A-3, B-14, C-2）

* **Primary RI**: RI-05 Qualitative overread — 「協同効果が働いている」という結論（T1）が、個別成分和（DMF 30 + acrylate 36 + PhI 65 + NEt₃ 182 = 313 ppm）と全成分混合（455 ppm @ 90°C Figure 4B）との140 ppm差という数値的非加算性を定量的に分析することなく提示されている。
* **ER**: どの成分ペアが相乗的な溶出増加をもたらすかを特定するための多成分実験（2成分/3成分の組み合わせ）、または313→455 ppmの超過分に対する統計的モデル（加算モデルとの有意差検定）の提示。
* **EP**: EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: コンフィギュレーション2でNEt₃+PhI同時供給実験を追加し、個別和（65+182=247 ppm）と比較する。もし247 ppm < 実測値であれば、相乗的溶出の実験的実証として機能する。
* **注記**: D-1のNovelty claim 2（「反応成分間の協同効果」）に直結。B-14（DMF stabilizer論、mixed分類）とC-2（DMF安定化文献、4件一括引用）がgrounded_inで共参照している。

---

**CLA-2: 触媒設計への実用的経路の実証根拠**

D-4候補6由来（grounded_in: A-4, B-8, B-1）

* **Primary RI**: RI-07 Unsupported boundary — 「これらの知見は将来の触媒設計と反応条件の最適化を導く」という実用的主張（A-4）が、表面Pdサイト数の非正規化（B-1: 4 mg等量比較）および多成分モデルの2触媒への未展開（B-8: ref 28の多尺度モデルがFC-1001とPd/Al₂O₃に未適用）という基盤的不足の上に成立している。
* **ER**: 触媒設計指針として機能するためには、少なくともPd分散度（または表面Pdサイト数）を基準とした正規化溶出量（ppm/exposed Pd atom）と、各触媒に対する多成分的TOF分割（hetero/homogeneous）が必要。
* **EP**: EP-07a Boundary-test pack
* **Case-specific実装**: CO chemisorptionまたはTEM-EDX（各触媒のPd分散度測定）を追加し、4 mg正規化から表面原子数正規化へ換算したリーチング量を再計算する。ref 28の多尺度モデルをFC-1001とPd/Al₂O₃のS1/S2変換率データに適用し、各触媒のhetero/homogeneous TOF分割を定量的に示す。
* **注記**: D-1の実用性主張（Utility柱）の直接的根拠。B-1（V1=high, 1/3）が主要grounded_in項目。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

---

**VQ-1 [Observation] — 通る（条件付き）**

必須解消項目RI-02（Object identification）について：三種の触媒はすべて市販品として名称・製造元が明示されており（PdEnCat 30, FibreCat FC-1001, Pd/Al₂O₃）、触媒としての定性的同一性は確立されている。バッチ固有のPd表面特性（XPS、TEM、BET）が未取得である点はRI-02の非致命的残存に留まる——商業品の品番・ロットを同定することで「通常品質」を担保するのは当該分野の規範内である（Era-norm: communication-era tolerated）。「Pdが溶出する」という観察事実自体はICP-MSの検出という客観的測定で成立しており、VQ-1を通す。**RI-02は非致命的**として処理。

---

**VQ-2 [Method] — 未達**

VQ-2にはRI-02（VQ-1継承：非致命的通過）に加え、RI-01（Reporting integrity）とRI-07（Unsupported boundary）の解消が必要。

- **RI-01：未解消・致命的（Layer 2）**。コンフィギュレーション1（194 ppm）とコンフィギュレーション2（182 ppm）の直接数値比較（U-3、論文の最強定量的結論"NEt₃が最大の犯人"の根拠）が異なる反応器構成・採取体積基準で行われており、比較の測定フレームが整合していない。SRG-1（成分実験の独立性）もRI-04/RI-01違反として未解消であり、コンフィギュレーション2の成分帰属クレームを方法論水準で成立させるには独立性の確認が必須である。これらは論文の方法論的中核（Component-isolation design）の信頼性を原理的に問うものであり、致命的。
- **RI-07：非致命的**。"guide future catalyst design"という主張はUtility claimとして誇張があるが、論文の方法論的結論（成分帰属の測定）を直接崩すものではない。

**VQ-2は未達。** RI-01の致命的残存により、Layer 2（成分帰属）の方法論的有効性は現状では独立に評価できない。VQ-2はRI-02が非致命的であることを前提に論じているが、RI-01が致命的に残存するため通過しない。

---

**VQ-3 [Mechanism] — 未達（VQ-2未達により継承失敗）**

VQ-2が未達であるため継承原則によりVQ-3も未達。独立に評価するとすれば、RI-03（SRG-4: 溶出Pd種の未観測）、RI-04（SRG-1: 単一データ点への高位解釈）、RI-06（SRG-5: Scheme 2の輸入）がいずれも未解消。RI-05（CLA-1: 協同効果の定性的過読）が残存するため、VQ-3は仮に到達できても"Qualified"扱いとなる。著者自身が"speculate"と位置付けるLayer 3はそもそもVQ-3水準の主張を目標としていない。

---

**VQ-4 [Benchmark] — 未達**

VQ-3未達により継承失敗。RI-08（SRG-2: 再現実験・不確かさ不在）、RI-09（Dropped Quantitative Benchmark: ref 12との直接FC-1001比較なし、C-4）も未解消。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-18（ブレークスルー曲線のESI委任）**: 2024年のACS Catalysis full paperにおいて、反応器特性データをESIに委任するのはflow chemistry論文の標準的慣行であり、当時の査読基準内。
- **B-19（流量・滞留時間の主テキスト不在）**: 反応器操作パラメータをExperimental sectionに記載しESI参照とする形式はACS Catalysisの慣行であり、当時は許容される省略。
- **B-8（ref 28多尺度モデルのFC-1001/Pd/Al₂O₃未展開）**: 先行モデルを新触媒に拡張しないことは「今後の課題」として許容される通常の絞り込みであり、D-3のjournal_constraintとも整合。
- **B-9（ブーメラン触媒主張の実験的未確認）**: 論理的推論（短滞留時間 → 再析出不可）を根拠にブーメランを除外するのは、flow chemistry文献において受け入れられる推論形式（2024年の慣行）。
- **B-10（FC-1001非極性溶媒挙動の未追跡）**: Full paperのスコープをDMFに絞ることは、比較の等価性を重視する実験設計の判断として許容範囲内。

**modern-era deficient:**

- **B-17（全実験で複製なし）**: 2024年のACS Catalysis full paperにおいて、定量的比較を中心的結論とする論文が複製データなしで掲載されることは現代の再認定基準で致命的欠落。ICP-MS値の絶対比較（455 ppm vs. 96 ppm vs. 6 ppm）に統計的信頼性がなければVQ-4水準の主張は成立しない。両タグ適用：2024年掲載実績があることは査読基準が移行途上にあることを示すが、再認定においてはmodern-era deficientと判定。
- **B-5（ICP-MS検出限界・測定不確かさ不記載）**: Pd/Al₂O₃の「完全安定性」という強い主張（"only 6 ppm"）に対して、6 ppmが検出下限以下の可能性を排除しないことは現代の分析化学標準では不可（IUPAC定量下限の開示義務）。
- **U-1/B-3（新鮮触媒床の独立性未記述）**: コンフィギュレーション2による成分帰属が本論文の中核技術革新である以上、その有効性の前提条件（触媒床の独立性）を記述しないことは、2024年の方法論報告基準を満たさない。era-norm依存ではなく普遍的要件として判定。
- **U-3（異構成間ICP値の直接比較）**: 異なるリアクター構成から得られたppm値を正規化なしに「182 vs. 194 ppm → NEt₃最大」と結論するのは、現代の定量分析報告規範（共通参照基準の明示）に照らして不充分。

---

### §5 最短補強ルート

**目的関数：VQ-2（Method）への到達**
（現在VQ-1 → 第一目的関数 VQ-2; 第二目的関数 VQ-3）

---

**VQ-2 への最短ルート：**

1. **EP-04a Discrimination / replication pack** — PdEnCat 30に対してコンフィギュレーション2実験D（NEt₃）を独立した新鮮触媒床でデュプリケート実施し、床独立性の確認とrun-to-run再現性（RSD%）を提示する（U-1・B-3をRI-04+RI-01の両面で前進させる最高情報利得ステップ）。RI-04を前進。

2. **EP-01a Reporting-coherence pack（クロス構成ICP正規化）** — コンフィギュレーション1（Figure 4B, 194 ppm）とコンフィギュレーション2（Figure 7D, 182 ppm）の採取体積・流量・採取時間窓を揃えるか補正係数を明示し、同一基準のppm値で"NEt₃最大"結論を再導出する（U-3をRI-01として解消）。RI-01を前進。

3. **EP-01a Reporting-coherence pack（ICP下限・不確かさ記載）** — ICP-MSの検出下限（3σ基準、ppm）と測定不確かさ（±ppm, k=2）を方法の節またはFigure legendに記載し、6 ppm（Pd/Al₂O₃ + NEt₃）が定量可能であることを確認する（B-5の解消）。RI-08の一部を前進（VQ-4への布石）。

4. **EP-01a Reporting-coherence pack（反応器パラメータ主テキスト記載）** — 流量（F1, F2 mL/min）・PBR充填量・PFR管容積・滞留時間をExperimental sectionに一表化する（SRG-3の解消、RI-01を完全前進）。RI-01を前進。

**認定ゲート順注記：** 実験投入順は情報利得順（1→2→3→4）だが、VQ-2認定は「RI-01が致命的に解消されたこと」の確認を要する。特にステップ1と2の両方が完了した時点でVQ-2への再評価が可能。ゲート順は継承原則に従い VQ-1 → VQ-2 で確定する。

---

**VQ-3 への追加ルート：**（VQ-2 通過が前提）

5. **EP-03a Direct-observation / state-assignment pack** — 溶出収集画分（PdEnCat + NEt₃ @ 30°C; Pd/Al₂O₃ + PhI @ 90°C）に対してナノフィルトレーション（Rothenberg 手法, refs 18/19）またはESI-MSを行い、クラスターvs分子種の直接判別を提示する（SRG-4のRI-03を前進）。RI-03を前進。

6. **EP-06a Analogy-validation pack** — PdEnCat 30 + NEt₃ @ 30°C 反応後の液相に対してNMR（エナミン副生物確認）またはin situ XANESでPd(0)形成を確認し、Scheme 2の低温適用可能性を実験内で直接評価する（SRG-5のRI-06を前進）。RI-06を前進。

**VQ-3 認定ゲート順注記：** VQ-2通過後、RI-03（ステップ5）とRI-06（ステップ6）の両方を解消することでVQ-3への道が開く。RI-04（SRG-1の成分実験複製）はステップ1で既に前進。RI-05（CLA-1の協同効果）が重大に残存する場合、VQ-3は"Qualified"。ゲート順は継承原則に従い VQ-2 → VQ-3 で確定する。

---

### §6 制度設計への寄与

**既存RIコードの新代表事例：**

- **RI-01（Reporting integrity）のflow reactor版代表事例**: 本論文のU-3（コンフィギュレーション1 vs. 2のICP ppm直接比較）は、"measurement frame incoherence"がflow chemistry論文に特有の形で現れる事例を追加する。従来のRI-01事例（有機合成のGC vs. 単離収率混在等）とは異なり、物理的に異なるリアクター構成からのデータを「同じ化学系」として比較する問題であり、flow reactor論文のRI-01チェック項目として新たに記録価値がある。

- **RI-04（Unreplicated discriminator）の実験独立性版代表事例**: SRG-1（U-1）が示す問題——複数の逐次実験が「同一触媒床の使い回し」か「独立新鮮床」かが未記述のまま比較が成立しているという問題——は、RI-04の適用範囲を従来の"単一高識別力データへの過解釈"から"実験設計の独立性の未確認"へと広げる代表事例として機能する。

**新PRI候補の提案：**

現在のRIコードでカバーされない以下のパターンを**PRI-11候補**として提案する：

> *PRI-11（暫定）: Sequential experiment cross-contamination — 同一触媒床・同一反応器システムで連続的に条件変化させる実験デザインにおいて、先行実験相（触媒状態・生成物・残留試薬）が後続実験相の観察値に混入するが、その混入の影響が定量化も言及もされていない場合。*

本論文ではB-2（温度ランプ内の前半フェーズ→後半フェーズへの触媒状態変化）とB-3/U-1（成分実験A→B→C→Dの累積溶出可能性）が同型のパターンを異なるスケールで示している。UQS open_issues OI-011（逐次昇温フロー実験の混交問題）でもhot-callout記録があり、Entry 009（v16.1 het2）・Entry 016（v17 het2）の両比較にまたがって継続的に検出されている。v17の B-2 として独立B項目化されたことでプロトコル内での捕捉は達成されたが、RIコードへの昇格は「独立2報での同型確認」要件に照らして下記判断とする：

昇格判断：本論文（het2, B-2/B-3/U-1）が1報目。scr1またはhet1の別論文でflow reactor内の逐次条件変更問題が独立に検出された場合、PRI-11として昇格可能。現時点では候補段階。

**VQ判定境界条件の新知見：**

- **VQ-1 → VQ-2 の新ブロック条件**：「論文の中心的定量的結論が2種類の異なる実験構成からのデータの等置に依存するとき、その等置の正当性（RI-01）はVQ-2の致命的要件となる」という判定事例が確立された。従来このパターンはRI-08（不確かさ）と混同されやすいが、本論文のU-3は「測定フレームの整合性（RI-01）」問題であり、RI-08（複製）の追加なしにもVQ-2を阻む。

- **Era-norm × VQ-4の移行領域**：B-17（全実験単一ラン）は2024年ACS Catalysisでの掲載実績があることから、現時点での査読基準がRI-08（VQ-4要件）についてまだ移行途上にあることを示す。VQ-4要件（RI-08）の致命性判定をera-normに依存させることの不安定性を示すケーススタディとして記録。

**EP辞書への追記：**

EP-01a（Reporting-coherence pack）のflow reactor版case-specific実装例として、「異なるリアクター構成（config 1 vs. config 2）から得られたppm値を比較する場合、採取体積・流量・時間窓を共通基準に換算するか、補正係数を明示すること」を EP 辞書の注記に追記することを推奨。これはRI-01のflow reactor特有の現れ方として、有機合成論文のGC/単離収率混在事例とは独立した新実装例となる。

inference_time_sec: not available — inject externally
```
