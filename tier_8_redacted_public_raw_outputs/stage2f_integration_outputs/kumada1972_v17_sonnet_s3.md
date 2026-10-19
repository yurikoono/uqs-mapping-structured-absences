```
prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc. communication）

### §1 Claim Architecture

**コア主張：**
本論文は、ニッケル–ジホスフィン錯体触媒によるGrignard試薬と芳香族・ビニル系ハライドのクロスカップリングを「選択的かつ実用的な新炭素–炭素結合形成法」として提示する。Novelty柱は二つある：（1）ホモカップリング副生物を生じずに高収率でクロスカップリングを達成する「選択性」（β-H含有Grignard試薬での許容を含む）、（2）NiCl₂(dpe)を代表とするbidentate diphosphine配位子の触媒活性——とりわけArCl（先行研究はBr/I主体）への適用可能性と配位子活性序列からのcis-幾何要件仮説。Utility柱は一つ：従来法では容易に得られない直鎖アルキル芳香族化合物（m-ジ-n-ブチルベンゼン等）を1段階で合成できる実用的手段としての宣言（T1: "a new and useful preparative method"）。

**Layered structure：**
D-1の通り、layered structure = yes。請求項1–2（選択性＋収率）、3（塩化物反応性）、4（配位子設計原理）、5（合成的有用性）は論理的に独立しており、単一の反証で全主張が崩れる構造ではない。ただし、主張4（cis-幾何要件仮説）が主張3（塩化物の高反応性特徴）と機構的に結びつけられているため、cis-幾何要件の否定は請求項3の「最も注目すべき特徴」という修辞を弱める——ただし請求項3の事実（塩化物が機能する）は崩れない。主張5（合成的有用性）は主張1–3の成否と原理的に独立しており、最も堅牢な層である。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Mechanistic cycle without experimental evidence in the dpe-Ni system]**

* **Primary RI**: RI-06 Imported model
* **Secondary RI**: RI-03 Unobserved explanatory
* **ER**: NiCl₂(dpe)系において提案された触媒サイクルの少なくとも1つの化学量論的ステップ（eq 2–4の個々の素反応）が、同一系内で単離・分光観測・独立合成された中間体によって実証されることが必要。dipy-Ni類似体からの類推は同型性の根拠にならない。
* **EP**: EP-06a Analogy-validation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: (i) NiCl₂(dpe)とPhMgBrの化学量論的反応（eq 2相当）を低温NMRまたはESI-MSで追跡し、中間体Ph₂Ni(dpe)（1）を観測する。(ii) 単離した中間体または類似モデル錯体（例：Me₂Ni(dpe)）がPhClと反応して式(3)に相当するカップリングを生じることを確認する。(iii) ラジカルクロック基質（シクロプロピルメチル-Grignard等）またはEPR測定でNi(I)/Ni(III)ラジカル経路を排除する。
* **注記**: B-2, B-14, U-1, U-2, U-4（5項目）。TEMPERATURE_SUMMARY: B-2はhigh_convergence_low_gap（V1=high, V2=critical）、B-14はhigh_convergence_low_gap（V1=medium, V2=high）。D4-2, D4-6はいずれもSRG-1に帰属。SRG内最多item count。

---

**SRG-2 [Selectivity claim without byproduct data]**

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-08 Unquantified reliability; RI-09 External superiority
* **ER**: 「選択的クロスカップリング」という主張を支持するためには、少なくとも1例のTable Iエントリについて、クロスカップリング生成物・ホモカップリング生成物（R–R）・プロト脱金属生成物（R–H）・β-脱離生成物の収量を定量し、マスバランスを閉じる必要がある。
* **EP**: EP-04a Discrimination / replication pack; EP-08a Replication / uncertainty pack; EP-09a Internal benchmark pack
* **Case-specific実装**: (i) グリニャール試薬（例：n-BuMgBr）とPhClの反応について、glpc内部標準法によりn-Bu–n-Bu（ホモカップリング）、n-Bu–H（プロト脱金属）、および1-ブテン（β-脱離生成物）の収量を定量し、マスバランスを構築する。(ii) eq(3)が予測するR–R（n-Bu–n-Bu）の実測収率をTable Iに併記する。(iii) 同基質でFe触媒（Tamura-Kochi ref 6）またはNi(acac)₂（Corriu-Masse）と並行実験を行い、内部ベンチマークを得る。
* **注記**: B-1, U-1, C-1（3項目）。B-1はhigh_convergence_low_gap（V1=high, V2=high, V3=high; convergence=3/3; gap=none）。D4-1はSRG-2に帰属。本SRGはD-4選択パスの最優先候補。

---

**SRG-3 [Analytical quality of Table I yield data]**

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: Table Iの収率値を独立に再現するため、glpc条件（カラム、固定相、検出器、温度プログラム、内部標準の同一性・濃度）、各エントリの反応時間、および収率算出基準（有機ハライド基準かGrignard試薬基準か）を全エントリについて統一記載する必要がある。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: (i) 全11エントリについてglpc条件を明記したTable Iの改訂版と反応時間を補足情報として提供する。(ii) Grignard試薬基準と有機ハライド基準のどちらが一般的に適用されたかを統一し、両基準で換算した値を示す。(iii) 少なくとも3エントリについて収率の反復実験値（n≥3）と標準偏差を報告する。
* **注記**: B-4, B-8, B-9, B-12, B-13（5項目）。B-4, B-8はhigh_convergence_low_gap（各V1=medium, V3=medium）。D4-3はSRG-3に帰属。RI-01の解消はVQ-2到達の必要条件。

---

**SRG-4 [Scope restriction basis]**

* **Primary RI**: RI-07 Unsupported boundary
* **Secondary RI**: RI-09 External superiority
* **ER**: 「Only Csp² halides can be used」という境界主張には、sp³ハライド（一次・二次アルキルクロリド等）を同一条件下で試みて不活性または選択性不良と確認した代表例が必要。また、「chlorides offer one of the most remarkable features」の定量的裏付けとして、同一基質でBrまたはIと直接比較した収率または速度データが必要。
* **EP**: EP-07a Boundary-test pack; EP-09a Internal benchmark pack
* **Case-specific実装**: (i) n-BuCl、sec-BuCl、PhCH₂Clを同一条件（NiCl₂(dpe)/Et₂O）でPhMgBrとカップリング試験し、不活性または選択性不良の結果を「failed scope」データとしてTable Iに追加する。(ii) PhBrおよびPhIをTable Iの基準基質（n-BuMgBr）と反応させ、PhClと同一条件で収率を直接比較する。
* **注記**: B-5, B-6, A-2（3項目）。A-2はconvergence=1/3。D4-4はSRG-4に帰属、D4-7はSRG-4に部分帰属。

---

**SRG-5 [Solvent and condition effects without quantitative or mechanistic basis]**

* **Primary RI**: RI-05 Qualitative overread
* **ER**: "Diethyl ether is definitely superior to THF" という確信的な溶媒比較は、THFを溶媒とした場合の収率（少なくとも1エントリ）の実測値によって裏付ける必要がある。"definitely" という副詞は定量的根拠を要求する。
* **EP**: EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: (i) Table IのExample 1相当系（n-BuMgBr + m-Cl₂C₆H₄）をTHF溶媒で実施し、Et₂Oとの収率・選択性を直接比較する。(ii) 溶媒効果の機構的検討として、Grignard試薬の溶媒和状態（DOSY NMR）または触媒の溶解度（UV-Vis）をEt₂OおよびTHFで比較する。
* **注記**: B-7, B-9（2項目）。B-7に"definitely"という確信的副詞が付されており、RI-05の典型例。

---

**SRG-6 [Cis/trans selectivity observation]**

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: 報告されたcis/trans比（80:20, 43:57）は、使用した分析法（glpc面積比またはNMR積分）、機器設定、繰り返し測定数、およびその標準偏差を明示することで定量的信頼性を得る。特に「43:57」という近接した比率には不確かさ評価が不可欠。
* **EP**: EP-04a Discrimination / replication pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: (i) cis-1,2-ジクロロエチレンおよびtrans体のPhMgBr反応をn=3で繰り返し、glpcまたは¹H NMR（ビニルプロトンの化学シフト差を利用）でcis/trans比を独立に定量する。(ii) 異なる反応時間（例：1 hr, 5 hr, 20 hr）で並行実験を行い、比率が時間依存性を持つかを確認することで、速度論的産物か熱力学的産物かを判別する（U-3解消）。
* **注記**: A-1, B-11, U-3（3項目）。A-1はhigh_convergence_low_gap（V1=medium, V2=high）。D4-5はSRG-6に帰属。

---

**SRG外：CLA**

**CLA-1 [D4-7: "Useful preparative method" — 合成標的との目的論的接続の不在]**

* **Primary RI**: RI-09 External superiority
* **Secondary RI**: RI-07 Unsupported boundary
* **ER**: "a new and useful preparative method" という宣言は、先行のCorey/Whitesidesストイキオメトリック試薬（C-2）との定量的比較（同一基質での収率・操作工程数）を通じて実用優位性を支持する必要がある。「hardly accessible by conventional methods」という境界主張は、代替手法を試みて困難と確認した例を必要とする。
* **EP**: EP-09a Internal benchmark pack; EP-07a Boundary-test pack
* **Case-specific実装**: (i) m-ジ-n-ブチルベンゼンをWhitesidesオルガノクプレート法（ref 10）またはCorey π-アリルNi法（refs 7–9）で合成する比較実験を行い、工程数・収率・廃棄物量を定量比較する。(ii) 1972–1975年の応用論文でこのカップリング法を使用した合成標的を後付けで記録し、"useful"の実証とする。
* **注記**: B-9, A-2, C-2が帰属項目。C-2（Corey/Whitesides）はいずれのSRGにも含まれない独立帰属項目。D-1の主張5（"hardly accessible... one step"）に直結。

---

**CLA-2 [D4-8: Corriu/Masse (Ni(acac)₂) — bidentate diphosphineの必要性の問い]**

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-06 Imported model
* **ER**: 配位子活性序列（[NiCl₂(dpp)] > [NiCl₂(dpe)] > ... > [NiCl₂(PEt₃)₂]）から「cis幾何要件」という構造的含意を引き出すには、bite angle・電子効果・立体効果を独立に変化させた配位子セットの定量的活性データと、Ni(acac)₂等のmonodentate/非chelate系との直接比較が必要。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-06a Analogy-validation pack
* **Case-specific実装**: (i) 全6配位子について同一基質（n-BuMgBr + PhCl）での収率を定量的に測定し、bite angleおよびσ-donor強度と活性の相関を作成する。(ii) Ni(acac)₂とNiCl₂(dpe)を同一基質・条件で並行実験し、収率・cis/trans比・byproduct profileを直接比較する（Corriu/Masse追試）。
* **注記**: C-3, B-3, U-4が帰属項目。B-3はいずれのSRGにも含まれない独立帰属項目（SRG-1との部分重複はU-4経由のみ）。C-3（Corriu/Masse Note Added in Proof）も独立帰属。D-1の主張4（bidentate diphosphineの配位子活性序列 + cis幾何仮説）に直結。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

**VQ-1 [Observation]：通る（RI-02 Non-fatal）**
Table Iの11エントリは、m-ジ-n-ブチルベンゼン（bp/n²⁰D比較）およびα-ビニルナフタレン（bp比較）については既知化合物の物性値との照合があり、その他エントリは「glpc, nmr, ir, and/or mass spectra」による特性確認を受けている。"and/or"構文により一部エントリがglpcリテンションタイム比較のみに基づく可能性があるが（B-13）、Table I記載の生成物はいずれも既知化合物であり、1972年の通信フォーマット慣行下では既知化合物の物性値照合は観察水準の主張を支えるのに原理的に十分である。RI-02はNon-fatal（現代基準では不足だが観察主張の成立を根底からは覆さない）として通過とする。この判断は§4でEra-Norm Annotationとして記録する。

**VQ-2 [Method]：未達（RI-01, RI-07 未解消、致命的）**
VQ-1継承を前提として、VQ-2にはRI-01（Reporting integrity）とRI-07（Unsupported boundary）の解消が必要。RI-01はSRG-3の5項目（B-4: glpc条件不記載; B-8: 反応時間不記載; B-9: 条件最適化免責; B-12: 収率算出基準の不統一; B-13: 特性評価の"and/or"）として構造的に残存し致命的——これらが未解消では収率データの独立再現が原理的に不可能である。RI-07はSRG-4（B-5: sp²制限に失敗例なし; B-6: Cl/Br/I直接比較なし）として残存し致命的——"Only Csp² halides"という境界主張は方法の適用範囲を規定するものであり、実験的根拠なしにはVQ-2方法水準の主張が成立しない。VQ-2は未達。

**VQ-3 [Mechanism]：未達（RI-01, RI-03, RI-04, RI-05, RI-06, RI-07 未解消）**
VQ-2が未達のためVQ-3も未達。仮にVQ-2が解消されたとしても、RI-03（SRG-1: 中間体1, 2, 3の未観測）、RI-04（SRG-2: 選択性の未定量; SRG-6: cis/trans比の繰り返し測定なし）、RI-06（SRG-1: dipy-Niからの機構類推）がいずれも致命的に残存する。RI-05（CLA-2: 配位子活性序列からのcis幾何推定）が重大に残存するため、仮にRI-03/04/06が解消されても VQ-3 は「VQ-3 (qualified)」にとどまる（RI-05残存：数値なき定性的順位から構造的含意を導出している）。

**VQ-4 [Benchmark]：未達（VQ-3未達を含む全要件が未解消）**
VQ-3が未達のためVQ-4も未達。加えてRI-08（SRG-2, SRG-6: 反復測定・不確かさなし）およびRI-09（SRG-2, SRG-4, CLA-1, CLA-2: 外部文献値のみによる優位性主張）が致命的に残存する。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-4**（glpc条件の不記載）: 1972年のJACS Communications形式では、glpcの詳細条件（固定相・温度プログラム・内部標準）を本文に記載することは期待されておらず、通常はFull Paperの実験部に委ねられていた。
- **B-8**（全エントリの反応時間不記載）: Communications形式では詳細な実験手順は代表例2例に限定して記述することが慣例であり、残り9エントリへの反応時間の省略は許容範囲内であった。
- **B-13**（全生成物の分光データの個別非記載）: 1972年時点では、既知化合物の同一性確認に物性値（bp, n²⁰D）＋glpcリテンションタイム比較＋簡略特性確認（"characterized by..."）で足りるとされており、Communications形式では本文に全スペクトルデータを載せることは求められていなかった。
- **B-1**（選択性のbyproduct定量なし）: 一報目の方法論的通信では、副生物マスバランスの定量なしに「選択的」と記述することが当時の形式上は許容されていた——先行研究の全不活性なGrignard反応との対比が文脈を形成しており、定性的な選択性主張として読めた。
- **B-2**（触媒サイクルの "working hypothesis" 提示）: 1972年時点の有機金属化学では、化学量論的実証なしにアナロジーに基づく「working hypothesis」機構を短報で提示することは許容されており、著者自身が最終文で "working hypothesis" と明記することで当時の適切なエビデンス標準を示していた。

**modern-era deficient:**

- **B-1**（選択性の定量的根拠の欠如）: 現代のJACS/Nature Chemistry等では「選択的」という主張はbyproduct profile（クロス/ホモ比、マスバランス）の定量データを必要とし、glpc収率のみでは不十分である——eq(3)が予測するR–Rの非存在に言及すらない点は、現代基準では自己矛盾的不在として記録される（U-1）。
- **B-4**（glpc条件・内部標準の不記載）: 現代の実験報告基準では内部標準の同一性・濃度・キャリブレーション曲線の開示が義務的であり、これなしには収率データの独立検証が原理的に不可能である。
- **B-13**（per-entry特性評価データの不記載）: 現代のJACSでは各化合物にNMR/MS等のcharacterization dataを補足情報として添付することが必須であり、"and/or" による包括的免責は受理されない。
- **B-3/U-4**（配位子活性序列 → cis幾何要件の因果的帰属）: 現代の触媒設計論文では、1種の活性序列から構造的含意を引き出す際にはDFT計算・bite angle系統変化・独立した立体電子プローブ実験による裏付けが求められる。
- **B-7**（"definitely superior" 溶媒主張の定量的根拠なし）: 現代の方法論論文では定量的比較データなしに"definitely"のような確信的副詞を使用することは編集審査で指摘される。

**両タグ（当時は許容されたが現代では不足）:**

- **B-4**: 1972年communication形式内では許容されたが、現代では独立検証に必要な最低限の情報として必須。
- **B-13**: 既知化合物の物性値確認は当時の基準を満たしていたが、現代基準では補足情報での全データ添付が必要。
- **B-1**: 通信の初報としての定性的選択性主張は当時許容されたが、現代では定量的マスバランスが必須であり、とりわけ機構提案の eq(3) が R–R を予測している点でEra-norm依存性が際立つ。

---

### §5 最短補強ルート

**VQ-2 への最短ルート（第一目的関数）：**

1. **EP-01a** Reporting-coherence pack — glpc条件（固定相・検出器・内部標準・温度プログラム）と全エントリの反応時間をTable Iに統一記載し、収率算出基準をGrignard基準または有機ハライド基準に統一する。RI-01 を前進（SRG-3の5項目を一括解消）。
2. **EP-07a** Boundary-test pack — sp³ハライド（n-BuCl, sec-BuCl, allyl Cl等）およびBr/Iとの同一基質直接比較実験を実施し、「Only sp² halides」境界に実験的根拠を与える。RI-07 を前進（SRG-4のB-5, B-6を解消）。

認定ゲート順注記：実験投入順は情報利得順（EP-01aがSRG-3の5項目をカバーする最大ゲイン）だが、最終的なVQ-2認定はVQ-1の継承を前提として VQ-1 → VQ-2 のゲート順で確定する。

---

**VQ-3 への最短ルート（第二目的関数、VQ-2達成後）：**

3. **EP-06a** Analogy-validation pack — NiCl₂(dpe)系での化学量論的ステップを低温NMRまたはESI-MSで検証し、dipy-NiアナロジーをdpeNiの実験結果に置換する（RI-06解消）。同時にNi(acac)₂との並行比較で配位子の必要性を検証し（CLA-2のRI-06に寄与）、情報利得を最大化する。RI-06 を前進（SRG-1の5項目に寄与）。
4. **EP-04a** Discrimination / replication pack — 少なくとも1エントリについてクロス/ホモ/β-脱離byproduct profileをglpcで定量し（RI-04, SRG-2解消）、cis/trans比をn=3以上で繰り返し測定する（RI-04, SRG-6解消）。RI-04 を前進（SRG-2, SRG-6の計6項目に寄与）。
5. **EP-03a** Direct-observation / state-assignment pack — EP-06aで特定した中間体候補をEPR・X線結晶解析・磁気感受率等で直接観測し、均一系/不均一系の分岐を実験的に排除する（RI-03, U-2解消）。EP-06aの後に配置することで観測標的を絞り込む。RI-03 を前進（SRG-1の残存項目を解消）。
6. **EP-05a** Quantitative-ranking substantiation pack — 配位子全6種について同一基質での定量的収率データを測定し、bite angle・電子効果との相関を分析する（RI-05解消）。これによりVQ-3がQualifiedから全解消VQ-3に到達。RI-05 を前進（CLA-2の主残存RIを解消）。

認定ゲート順注記：EP-06a/04a/03a/05aの投入順は情報利得順（EP-06aが最多のSRG-1項目をカバーし、かつCLA-2への二重寄与を持つ）だが、VQ-3の正式認定はVQ-2達成を前提として VQ-1 → VQ-2 → VQ-3 のゲート順で確定する。

---

**VQ-4 への最短ルート（VQ-3達成後）：**

7. **EP-09a** Internal benchmark pack — Tamura-Kochi（Fe触媒）・Corriu/Masse（Ni(acac)₂）・Corey/Whitesides試薬（C-2）と同一基質で並行実験し、収率・選択性・操作性の直接数値比較を得る。RI-09 を前進（SRG-2, SRG-4, CLA-1, CLA-2の外部優位性主張を全て実験値で置換）。
8. **EP-08a** Replication / uncertainty pack — 全エントリについてn≥3反復測定を実施し、標準偏差付き収率と選択性値を報告する。RI-08 を前進（SRG-2, SRG-6の信頼性要件を解消）。

認定ゲート順注記：EP-09aとEP-08aは独立して実施可能だが、VQ-4の正式認定はVQ-3達成を前提として VQ-1 → VQ-2 → VQ-3 → VQ-4 のゲート順で確定する。

---

### §6 制度設計への寄与

**RI-06の代表事例確立と「標識不整合」サブタイプの提案：**
本論文はRI-06（Imported model）の教科書的事例を提供する。dipy-NiおよびハロゲンNi結合のトランスメタル化という2つの異なる配位子系の結果を、対象系（dpe-Ni）での同型性実証なしに統合して触媒サイクルを構築している（B-2, B-14, SRG-1）。特に注目すべきは、著者自身が "working hypothesis" と最終文で明記しながら、前段の叙述が事実的記述語（"reacts with", "is subsequently converted to", "forms"）で書かれているという「標識不整合（labeling mismatch）」であり——仮説標識が末尾1文に集約され本文全体は事実として記述されている。このパターンはRI-06の新しいサブタイプ候補として記録する価値がある：「RI-06b: 仮説が末尾で明示されているにもかかわらず、本文叙述が事実的記述語を使用するもの」。

**RI-07の「制限の肯定的再フレーム」パターン：**
B-5とA-2の組み合わせは、方法論論文における「スコープ制限の肯定的再フレーム」という特有のパターンを示す。失敗例を提示せずに「〜のみ可能」という境界を設け（RI-07）、同時にその制限を方法の「最も注目すべき特徴」として再定義し、スコープ拡張を将来課題として外部化する（A-2）。このパターンはFull Paper展開時にRI-07が自動的に解消されることが多いが、通信単独ではRI-07が残存する。Codebookへの注記推奨：「RI-07：通信→Full Paper遷移での自動解消パターン——Aアイテムとの対応を確認すること。」

**CLA同定手順の実用性確認：**
D4-7（C-2が独立帰属項目）とD4-8（C-3, B-3が独立帰属項目）はSRGに収まらないD-4候補としてCLA同定手順を使用して抽出された。いずれもD-1の主張に直結し（D4-7→主張5、D4-8→主張4）、両CLAへのRI/EP割り当てが§5最短補強ルートを実質的に強化している——特にCLA-2（D4-8）はEP-06aの「二重寄与」（SRG-1のRI-06解消とCLA-2のRI-06解消を同一実験パックで達成）を可能にする。CLA同定手順が単報モードでも有効に機能することを確認。

**VQ-1 / VQ-2境界条件：Era-Norm依存の致命性判定：**
本ケースでは、RI-02（Object identification）が1972年JACS Communication形式下では既知化合物の物性値比較で事実上満たされており、VQ-1通過をNon-fatalとして支持する。しかし現代基準では同じ特性確認は不十分となる（Era-norm依存）。これはVQ判定基準マトリクスにおける「致命性はEra-Norm依存で変化しうる」という境界事例として記録する。Codebookへの継承原則への注記推奨：「RI-02の致命性は、主張対象化合物が既知か新規かによって変動する；既知化合物の物性値照合は1970年代通信形式ではVQ-1 Non-fatalとして扱う。」

**PRI昇格：該当なし（既存RIで網羅）：**
SRG-1（RI-06）、SRG-2（RI-04）、SRG-3（RI-01）、SRG-4（RI-07）、SRG-5（RI-05）、SRG-6（RI-04）、CLA-1（RI-09）、CLA-2（RI-05）のいずれも既存RIコードに収まる。新規パターンは検出されず、PRI昇格候補なし。本ケースはCodebook v0.2の既存分類体系を追加確認した。
```
