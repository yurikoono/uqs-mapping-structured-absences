prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Li et al. 2024（Nature Catalysis, full_paper）

### §1 Claim Architecture

**コア主張の要約：**
本論文は、活性化基（ボリル・シリル・π系）を一切必要とせずに、非活性化アルキルハライド間のクロスカップリング（eXEC）を電気化学的Ni触媒によって達成した最初の一般的手法を報告する。Novelty柱は「非活性化アルキルハライド（1°–1°, 1°–2°, 1°–3°, 2°–2°の全組み合わせ）のクロス選択的eXEC」であり、Utility柱は「生物活性化合物の後期修飾・グラムスケール合成・合成ステップ削減への応用」である。電気化学を用いることで、化学量論的還元剤（Zn/Mg）もHAT試薬も不要とし、持続可能性を主張する。

**Layered structureの判定：**
構造は4層に分離している：
（1）電気化学的活性化による非活性化ハライドカップリングの実現（実験的観察層）；
（2）基質スコープの広汎性（合成有用性層）；
（3）Ni(I/II/III)ラジカル機構の提案（機構層）；
（4）医薬化学・製造への実用可能性（応用層）。

各層は部分的に独立しており、単一の反証が全層を崩すことはない。ただし（3）機構層は（1）（2）の信頼性根拠を提供しているため、機構的誤りが判明しても（1）（2）の観察的・方法論的主張は別途成立し得る。主張間の依存関係：機構層(3)が選択性の説明を提供するが、その選択性機構の定量的根拠が主テキストに不在（B-3, SRG-3）であるため、(1)(2)の選択性主張が(3)に依存している部分が証明できない状態になっている。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [定量的反応収支の体系的不在]**

* **Primary RI**: RI-01 Reporting integrity — 基質スコープ90例以上を通じて単離収率のみが報告され、GC収率・転化率・ホモカップリング副生成物量が不在であることで、選択性と効率の横比較が不能。
* **Secondary RI**: RI-08 Unquantified reliability — 再現性データ（繰り返し実験、標準偏差）が全実験にわたって不在。
* **ER**: クロス/ホモ選択性をスコープ全体にわたって主張するためには、モデル反応と同様のGC収率・副生成物量の報告が代表的基質（5–10例）で必要。また主要結果（モデル反応）の繰り返し実験（n≥3）と標準偏差が必要。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication/uncertainty pack
* **Case-specific実装**: Fe板/Ni foamセル・DMF・5 mA・12 hの標準条件下で、主要基質（化合物3, 30, 57, 62）について内部標準（1,3,5-トリメトキシベンゼン等）を用いたGC収率測定と、n=3の繰り返し実験（単離収率の平均と標準偏差）を実施する。TEMPO捕捉実験の全生成物をGCで定量し59%収支を解明する。
* **注記**: B-1（3/3 convergence, high/high/high）、B-9（2/3, medium/high）、B-11（2/3, medium/high）、B-12（1/3, medium）、B-14（1/3, high）、B-15（1/3, medium）。TEMPERATURE_SUMMARY: high_convergence_low_gap筆頭（B-1は3/3全エージェントhigh）。

---

**SRG-2 [電気化学的稼働条件の未測定]**

* **Primary RI**: RI-03 Unobserved explanatory — 提案されたNi(0)/Ni(I)/Ni(II)の電気化学的生成は電解中のカソード電位が未測定であり、各Ni酸化還元ステップが稼働条件下でアクセス可能かが実証されていない。
* **Secondary RI**: RI-05 Qualitative overread — Fe/Zn/Mgアノード間の収率差（85%/30%/17%）から「Feアノードが重要」という定量的結論を引き出しているが、アノード酸化生成物も定電位も報告されておらず、さらにentries 5–6はアノードとカソード材料を同時変更するため非matched-pair control（D4-7）。
* **ER**: 5 mA定電流電解中のカソード電位をAg/AgNO3基準の同一スケールでモニタリングし（B-2の参照電極統一を含む）、ファラデー効率を算出することで、どのNi酸化還元プロセスが稼働条件でアクセス可能かを実証する。アノード酸化生成物（Fe溶出量）を定量する。
* **EP**: EP-03a Direct-observation/state-assignment pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: 定電位電解（ポテンシオスタット）条件でSWVと同一参照電極（Ag/AgNO3）を用いてカソード電位を経時記録する。Feアノード対Ptアノードの対照実験（真のmatched-pair control）を実施してアノード効果を孤立させる。OHM法でiRドロップを測定する。
* **注記**: B-6（2/3, high/medium, gap=low）、B-7（2/3, medium/medium）、B-8（2/3, medium/medium）、B-17（2/3, medium/medium）、B-18（1/3, medium）。TEMPERATURE_SUMMARY: high_convergence_low_gap: B-6(gap=low)。

---

**SRG-3 [選択性機構が主テキストに不在]**

* **Primary RI**: RI-04 Unreplicated discriminator — クロス選択性はモデル反応1例（Table 1）で確認されているが、それを説明する機構（速度論的vs熱力学的制御、Path I vs II）は主テキストに不在でSIに委ねられており、独立した機構的検証実験がない。
* **Secondary RI**: RI-06 Imported model — Ni(I/II/III)サイクルは先行報告（refs. 30, 65）から輸入されており、このeXEC系での同型性を実証する独立した中間体捕捉実験がない。
* **ER**: クロス選択性機構を主張するためには、少なくとも（a）速度論的制御を示す競合速度実験（二種のハライドを混合した速度定数比）または（b）Path I/IIを判別する電位依存的産物分布実験（電位を変化させてクロス/ホモ比がどう変わるか）が必要。
* **EP**: EP-04a Discrimination/replication pack; EP-06a Analogy-validation pack
* **Case-specific実装**: 異なる印加電位（−1.5 V, −2.0 V, −2.5 V vs Ag/AgNO3、定電位モード）でのクロス/ホモ収率比を測定し、電位依存性からPath IとIIの相対寄与を推定する。また1°/2°ハライドの個別還元速度定数を測定し、選択性の定量的モデルを構築する。
* **注記**: A-1（suppressed, V2=high）、B-3（intentional_narrowing, V2=high）、U-1（V2=high）。TEMPERATURE_SUMMARY: low_convergence_high_gap（B-3 V2=high、1/3）。SRG-3はピボット構造の核：A-1 ↔ B-3（ピボット）。

---

**SRG-4 [DFT計算の方法論的記述不在と実験値との不整合]**

* **Primary RI**: RI-06 Imported model — DFT計算（ΔG‡ = 13.4 vs 16.2 kcal/mol, E°計算値）が機構的支持として使用されているが、SWV測定値（−2.74 V）とDFT計算値（−2.38 V）の360 mVの不一致が議論されておらず、汎関数・基底関数・溶媒和モデル・分散補正が主テキストに不在。
* **Secondary RI**: RI-01 Reporting integrity — CVはAg/AgCl基準、SWV/DFTはAg/AgNO3基準で、参照電極スケールの不統一が定量比較を妨げている（B-2）。
* **ER**: DFT計算ポテンシャルを機構的証拠として使用するためには、（a）使用汎関数・基底関数・分散補正・溶媒和モデルの完全記述、（b）SWV測定値との一致または360 mVずれの系統的説明（参照電極変換係数の測定を含む）が必要。
* **EP**: EP-06a Analogy-validation pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: Ag/AgClとAg/AgNO3間のフェロセン基準を用いた電位変換係数を実験的に測定し、全電気化学データを同一スケールに統一する。SMD(DMF)溶媒和・D3BJ分散補正を用いたDFT再計算でNi(I)/Ni(0)電位を再予測し、SWV値と比較する。
* **注記**: B-2（1/3, high）、B-4（1/3, high）、B-5（1/3, medium）、B-13（1/3, medium）、U-2（self-contradictory absence）。TEMPERATURE_SUMMARY: low_convergence_high_gap（B-2 V3=high、B-4 V2=high）。

---

**SRG-5 [一次アルキルハライドのラジカル中間体への直接証拠の不在]**

* **Primary RI**: RI-04 Unreplicated discriminator — ラジカル機構の実験証拠（ラセミ化・TEMPO・シクロプロピルメチル開環）がいずれも二次ハライドを基軸とした実験であり、一次ハライドへの一般化が実験的に未検証。
* **Secondary RI**: RI-03 Unobserved explanatory — 一次アルキルラジカル中間体は直接観測されておらず、TEMPO捕捉（41%収率、59%未説明）とシクロプロピルメチル開環（53%開環体、非開環体の収率不明）が不完全。
* **ER**: 一次ハライドのラジカル経路を実証するためには、光学活性一次ハライドのラセミ化実験、または一次ハライドに特異的なラジカルクロックを用いた速度論的プローブが必要。
* **EP**: EP-04a Discrimination/replication pack; EP-03a Direct-observation/state-assignment pack
* **Case-specific実装**: α位に立体中心を持つキラル一次ハライド（例：(R)-2-メチル-3-フェニルプロピルブロミド、>95% ee）を標準条件で反応させ、クロスカップリング生成物のeeをHPLCで測定する。ラセミ化観測で一次ハライドのラジカル中間体を実証。
* **注記**: B-10（2/3, medium/high, gap=low）、B-11（2/3, medium/high, gap=low）、B-12（1/3, medium）。TEMPERATURE_SUMMARY: high_convergence_low_gap（B-10, B-11, 2/3）。

---

**SRG-6 [非標準基質クラスへの条件変更の原理的根拠の不在]**

* **Primary RI**: RI-07 Unsupported boundary — 2°–2°（L6配位子）と1°–3°（L11/DMA）で異なる条件が必要であるにもかかわらず、なぜL2/DMFが機能しないのか、どの基質クラスでどの条件が機能するかの系統的境界テストが不在。「一般戦略」主張と暗黙の基質クラス限定が矛盾している。
* **Secondary RI**: RI-05 Qualitative overread — L6がL2より2°–2°に有効という観察から「配位子効果」という一般原理を定量的根拠なしに導出している。
* **ER**: 「一般的eXEC」を主張するためには、標準条件（L2/DMF）での全4基質クラスの試験と失敗例の記録、および各条件変更の配位子特性との相関が必要。
* **EP**: EP-07a Boundary-test pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: L2/DMF標準条件で2°–2°カップリングを試験し失敗を確認；L1〜L9の全配位子を2°–2°カップリングでスクリーニングし、L6選択の理由をSWVで得られるNi錯体電位と相関させる。三級ブロミド収率改善を試みて最低限の「一般的条件」を定義する。
* **注記**: A-2（deferred, medium）、B-16（mixed, medium）。フォールバック規則(c)でSRG-6をD4-6として特定。

---

**SRG外：CLA**

**CLA: スケールアップ時の条件変更と収率低下** (D4-8, B-17)

* **Primary RI**: RI-01 Reporting integrity — グラムスケール（50 mA, 24 h）と小スケール（5 mA, 12 h）で条件が不連続に変更されており、収率変化（3: 85%→69%等）の原因が特定できない。
* **ER**: スケールアップ主張には、電流密度一定でのスケール実験が必要；もし条件変更が必須ならその理由（電流密度上限、質量移動）の説明が必要。
* **EP**: EP-01a Reporting-coherence pack
* **Case-specific実装**: 5 mA/cm²の電流密度一定（電極面積比例拡大）でのグラムスケール実験を実施し、条件変更なしのスケールアップ可能性を確認する。
* **注記**: B-17（2/3 convergence, V1=V3=medium, gap=none）。

---

### §3 現在のVQ判定

**現在判定: VQ-2 qualified (Method)**

---

**VQ-1 Observation — 通過（Non-fatal残存あり）**

RI-02（Object identification）は実質的に解消されている：>90の全生成物がSIで完全キャラクタリゼーション（NMR, MS）を受けており、CCDC 2285024に結晶構造が寄託されている。SIへの全面委任はEra-norm toleratedの範囲内。RI-02はNon-fatalとして扱い、VQ-1通過とする。

**VQ-2 Method — 通過 qualified（RI-01, RI-07残存）**

VQ-1継承を前提として、RI-01とRI-07を検討する。

RI-01（Reporting integrity）：スコープ全体で孤立収率のみの報告（B-1）は2024年の合成化学full paperのEra-normの範囲内であり単独ではNon-fatal。ただし参照電極スケールの不統一（B-2, SRG-4）は電気化学的データの定量比較に影響し、Non-fatalだが未解消。

RI-07（Unsupported boundary）：失敗例が不在だが（SRG-6）、2°–2°と1°–3°で条件変更が必要という暗黙の境界は部分的に開示されている。三級基質の「低収率」（A-2）も認識されている。完全には解消されていないがEra-norm toleratedの範囲で部分的成立。

→ VQ-2は「qualified（限定的）」で通過。限定事由：スコープ全体のGC収率・マスバランス不在（RI-01残存）、および系統的失敗例テストの不在（RI-07残存）。

**VQ-3 Mechanism — 未達**

VQ-2を前提として、RI-03, RI-04, RI-06を検討する。

- RI-03（Unobserved explanatory）：稼働条件下のカソード電位未測定（SRG-2）、Ni中間体の直接観測なし（SRG-3）。未解消。
- RI-04（Unreplicated discriminator）：クロス選択性のモデル反応1例のみ（Table 1）；Path I/II未判別（A-1/U-1）；一次ハライドのラジカル機構未直接検証（SRG-5）。未解消。
- RI-06（Imported model）：DFT計算ポテンシャルとSWV実測値の360 mV不一致が未議論（SRG-4/U-2）；Ni(I/II/III)サイクルの直接中間体捕捉なし。未解消。

→ VQ-3は未達。RI-03, RI-04, RI-06が全て未解消。

**VQ-4 Benchmark — 未達**

- RI-08（Unquantified reliability）：繰り返し実験・標準偏差不在（B-14）。未解消。
- RI-09（External superiority）：Lin group (ref. 60)・Gong group (refs. 29–30)との直接数値比較なし（C-1, C-2）。未解消。

→ VQ-4未達。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- B-1（孤立収率のみ、GC・転化率不在）：2024年Nature Catalysis合成methodology論文として標準的報告形式。Era-norm内。
- B-3（選択性機構のSI委任）：Nature CatalysisのArticle形式では、定量的機構議論のSI委任は標準的慣行。
- B-4, B-5（DFT方法論詳細のSI委任）：合成化学論文でのDFT計算詳細のSI委任は2024年標準。
- B-14（繰り返し実験・標準偏差不在）：合成化学論文で単一実験値報告は2024年のEra-norm範囲内（特に>90例スコープの場合）。
- B-9（速度論グラフの定量的解析不在）：合成化学論文の機構実験として速度論グラフの定性的解釈は許容される。

**modern-era deficient:**

- B-2（参照電極スケール不統一：Ag/AgCl vs Ag/AgNO3）：2024年の電気化学メカニズム論文として同一論文内での参照電極スケール統一は最低限の要件。重大な不統一。
- U-2/B-13（SWV−DFT 360 mV不一致の未議論）：DFT計算ポテンシャルを機構的証拠として使用する論文では実験値との定量的整合確認が現代基準で必須。VQ-3到達の阻害要因。
- A-1/U-1（Path I/IIの未判別）：2024年の電気化学機構論文として二つの経路を同時に提案し判別実験なしに終わることは現代では不十分。VQ-3到達の阻害要因。
- B-11（TEMPO実験の59%収支未解明）：電気化学系ではTEMPO自体が電気化学的に還元される可能性があり、その確認を含む完全な質量収支が現代基準で必要。
- B-6（稼働電解条件下のカソード電位未測定）：電気化学反応機構論文として実際の電解中の電位モニタリングは現代基準の必須要件。

（B-1は合成スコープ報告としてはcommunication-era tolerated、機構的選択性主張との整合においてはmodern-era deficientの両方に該当する。）

---

### §5 最短補強ルート

**目的関数1：VQ-3 (Mechanism) への最短ルート**

1. **EP-01a Reporting-coherence pack** — Ag/AgClとAg/AgNO3の電位変換係数をフェロセン基準で実験的に決定し、論文内全電気化学データを同一スケールに統一する。RI-01（SRG-4）を解消。

2. **EP-03a Direct-observation/state-assignment pack** — 定電位モードで稼働電解中のカソード電位を記録し、ファラデー効率を算出する（RI-03, SRG-2を前進）。Feアノード対Ptアノードのmatched-pair対照実験でアノード効果を孤立（RI-05, B-7）。

3. **EP-04a Discrimination/replication pack** — 印加電位を変化させた定電位eXECでクロス/ホモ比の電位依存性を測定し、Path I/IIの相対寄与を推定（RI-04, A-1/U-1を前進）。キラル一次ハライドのラセミ化実験で一次ハライドのラジカル機構を直接検証（RI-04, SRG-5を解消）。

4. **EP-06a Analogy-validation pack** — SMD(DMF)溶媒和・D3BJ分散補正つきDFT再計算でNi(I)/Ni(0)ポテンシャルを再予測し、SWV実測値との整合を確認（RI-06, SRG-4/U-2を解消）。

上記1–4の投入によりRI-01（部分）, RI-03, RI-04, RI-06が前進または解消され、VQ-3到達が可能となる。

**目的関数2：VQ-4 (Benchmark) への追加ルート**（VQ-3前提）

5. **EP-09a Internal benchmark pack** — Lin group (ref. 60) の活性化アルキルハライド基質3–5例を本手法標準条件で試験し、収率・選択性を直接比較（RI-09, C-1を解消）。

6. **EP-08a Replication/uncertainty pack** — モデル基質（化合物3）のn≥3繰り返し実験で単離収率の平均・標準偏差を報告；代表的10基質でGC収率と孤立収率を比較（RI-08, B-1/B-14のRI-08成分を解消）。

**認定ゲート順注記：** 実験投入順は情報利得順（EP-01a → EP-03a → EP-04a → EP-06a → EP-09a → EP-08a）だが、最終的な認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承順で確定する。VQ-3認定にはVQ-2の完全通過（RI-01, RI-07の解消）が前提となる。

---

### §6 制度設計への寄与

**新PRI候補の提案：**

**PRI-11候補：Analytical-to-operating conditions extrapolation**
定義：分析スケールの電気化学データ（CV、SWV）を用いて、稼働スケールの電解条件（カソード電位、ファラデー効率、電流密度効果）を実証なしに推定すること。
代表事例：本論文SRG-2（B-6, B-7, B-8）—CVの還元ピーク電位から「電解中にNi(0)が生成し得る」と結論しているが実際の定電流電解中のカソード電位は未測定。
昇格要件：電気化学合成を扱う独立2報でこの構造が確認されれば正式昇格とする。

**既存RIコードの新代表事例：**
- SRG-2（電気化学的稼働条件の未測定）はRI-03の新しい代表事例を提供する：「analytical-to-operating substitution」パターンは2020–2024年の電気化学合成論文群で繰り返される構造的欠落の可能性がある。
- U-1とU-2の「self-contradictory absence」パターン（DFT計算値と電気化学実験値が同じ機構を支持するために並置されているが互いに矛盾する）は、RI-04とRI-06が連動して作動するケースの代表事例として記録できる。

**VQ判定境界条件の新知見：**
本ケースは「基質スコープの広汎性」（暗黙の条件変更が事実上の失敗例開示として機能）がRI-07の部分的代替となり得ることを示す、VQ-2/VQ-3境界のケーススタディ。

**EP辞書への追加実装例：**
EP-03a（Direct-observation/state-assignment pack）のNi電気化学系特化実装として、「フェロセン基準での参照電極統一 + 定電位電解でのカソード電位モニタリング + Feアノード対不活性アノードmatched-pair対照」という組合せを本ケースで確立した。
