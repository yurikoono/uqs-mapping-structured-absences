prompt_version: stage4-v1-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tellis, Kelly, Primer, Jouffroy, Patel, Molander 2016（Accounts of Chemical Research, full_paper）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a, EP-04a

- **EP-03a** (Direct-observation / state-assignment pack): Stern-Volmer消光実験・EPR観測・量子収率測定はいずれも独立した論文の主題として発表される性質の実験であり、光レドックス/Ni二元触媒の分野では2014–2020年代に複数の独立機構研究が公表されている。
- **EP-06a** (Analogy-validation pack): ベンジルラジカル以外の系（二級アルキルラジカル）へのDFT適用拡張または実験的ラジカルクロック研究は、合成方法論の機構的正当化論文として発表されやすく文献検索で追跡可能。
- **EP-04a** (Discrimination / replication pack): 温度依存性er測定とHammett解析は、エナンチオ選択的光レドックス/Niカップリングを主題とする独立論文として2017年以降に複数発表されており、追跡可能。

**第二群（間接的に追跡可能）：** EP-05a, EP-09a

- **EP-05a** (Quantitative-ranking substantiation pack): 触媒サイクル閉環SETのPC⁻/PCとNiII/Ni⁰の酸化還元ポテンシャル比較はTotal Mechanism Reviewまたは光レドックス触媒設計論文の一部として扱われることが多く、独立論文の主題となる例は少ない。
- **EP-09a** (Internal benchmark pack): 光レドックス/Ni手法と先行Suzuki法（95–115°C）の直接収率比較は、総説・方法論比較論文には含まれうるが、独立した主要論文として発表される可能性は低い。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-07a, EP-08a

- **EP-01a** (Reporting-coherence pack): キラルHPLCおよびCV条件の不開示はAccount形式固有の報告形式問題であり、一次論文（Full Paper）への移行時に自動解消されるかAccounts本文では未解消のまま残る性質。
- **EP-07a** (Boundary-test pack): スコープ失敗例の体系的報告はAccounts論文のgenre convention問題であり、独立した充填論文として発表されることは稀；個別の一次論文に含まれる。
- **EP-08a** (Replication / uncertainty pack): 合成スコープの再現収率・標準偏差の不在は報告形式問題（RI-08）であり、Full Paper版では解消されているはずだが、独立した「再現性検証論文」として発表される性質ではない。

---

### §B 各EPの充填論文候補

---

**EP-03a Direct-observation / state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点（Stern-Volmer）**: Zuo, Z.; Ahneman, D.T.; Chu, L.; Terrett, J.A.; Doyle, A.G.; MacMillan, D.W.C. *Science* **2014**, *345*, 437–440 — MacMillan/Doyleの並行論文（ref 25）がシリルオキサラートα-位ラジカル系について*Irに対するStern-Volmer消光データを報告；有機ラジカル前駆体がPC*を消光する主要クエンチャーであることを示した最初の実験的証拠。
* **充填確立点（PC*消光 + 競合定量）**: Ting, S.I.; Garakyaraghi, S.; Taliaferro, C.M.; Shields, B.J.; Scholes, G.D.; Castellano, F.N.; Doyle, A.G. *J. Am. Chem. Soc.* **2020**, *142*, 5800–5810 — 光レドックス/Ni系における励起状態消光経路（PC*→Ni経路 vs PC*→有機ラジカル前駆体経路）を時間分解分光で解析し、消光の競合を定量。
* **充填の性質**: Partial — Stern-Volmer定量は前進したがNiI/NiIII EPR観測と量子収率測定はそれぞれ独立の論文で補完が必要
* **Confidence**: Medium（Zuo et al. Science 2014はHigh; Ting et al. JACSはMedium — 論文の存在は確信、EP充填との対応に推論を含む）
* **注記**:
  - Ni酸化状態のEPR観測: Diccianni, J.B.; Heitmann, L.E.; Diao, T. *J. Am. Chem. Soc.* **2019**, *141*, 1867–1878（またはDiao group類似論文）がNi触媒的クロスカップリング中のNi(I)ラジカル中間体をEPRで確認したと記憶するが、photoredox条件下での直接観測かどうかは確認が必要（Confidence: Low）
  - 量子収率測定: Arias-Rotondo, D.M.; McCusker, J.K. *Chem. Soc. Rev.* **2016**, *45*, 5803–5820 がphotoredox触媒一般の量子収率測定の方法論を整備したが、Ir/BF₃K/Ni系の特定量子収率測定については実際の文献確認が必要（Confidence: Low）

---

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Gutierrez, O.; Tellis, J.C.; Primer, D.N.; Molander, G.A.; Kozlowski, M.C. *J. Am. Chem. Soc.* **2015**, *137*, 4896–4899 — ベンジルラジカル/ブロモベンゼン系のDFT計算でDKRモデルと経路Bの優位性を最初に定式化（論文ref 24）；ただし非ベンジル系への拡張はなく、充填としては「出発点のみ」。
* **充填確立点（二級アルキル系への拡張）**: 未同定（§E参照）
* **充填の性質**: Partial（ベンジル系のみ；二級アルキルラジカルへの計算的拡張または実験的ラジカルクロックを提供した論文は文献確認が必要）
* **Confidence**: High（Gutierrez et al. JACS 2015の存在と内容は確信）; 二級アルキル拡張論文はMedium–Low
* **注記**:
  - ラジカルクロック実験（シクロプロピルカルビニル-BF₃K）を用いてラジカル中間体の自由度を実証した可能性のある後続論文として、Primer, D.N.; Molander, G.A. *J. Am. Chem. Soc.* **2015**, *137*, 2195–2198（ref 18）が挙げられるが、この論文がラジカルクロック実験を含むかどうかは確認が必要（Confidence: Low）
  - 近年の計算論文による二級アルキルNi-ラジカルPES計算の特定には文献検索が必要

---

**EP-04a Discrimination / replication pack（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点（温度依存性er）**: Chierchia, M.; Law, C.; Morken, J.P.（または関連するMolander group / Rovis group エナンチオ選択的photoredox/Niカップリング論文; 2017–2020年代; 具体論文は文献確認が必要） — エナンチオ選択的光レドックス/Niカップリングを主題として、温度・配位子変化とerの関係を系統的に検討した研究
* **充填確立点（Hammett + 統計的検証）**: 未同定（§E参照）
* **充填の性質**: Partial
* **Confidence**: Low（エナンチオ選択的photoredox/Niカップリングの文献は確認済みだが、温度依存性erとHammett解析の両方を提供した特定論文を確信を持って同定できない）
* **注記**:
  - DKRモデルの動力学的検証（khomolysis >> kRE の実験的確認）については、Molander グループの自己充填が最も可能性が高い；2017–2022年の同グループのエナンチオ選択的カップリング論文を精査する必要がある
  - Hammett解析（σ vs er相関、≥8点）を含む充填論文は現時点では特定できず

---

**EP-05a Quantitative-ranking substantiation pack（第二群）**

* **充填するRI**: RI-05 Qualitative overread; RI-03 (U-8: PC⁻→NiII SET熱力学)
* **充填開始点**: Arias-Rotondo, D.M.; McCusker, J.K. *Chem. Soc. Rev.* **2016**, *45*, 5803–5820 — 主要なIr/Ru光レドックス触媒の励起状態および基底状態酸化還元電位（vs SCE）を系統的に整備し、典型的なNi(II)/Ni(0)還元電位との熱力学的比較の枠組みを提供。
* **充填確立点**: 未同定（特定系での数値比較）
* **充填の性質**: Indirect（Arias-Rotondo等のレビューは数値枠組みを提供するが、アセトン/MeOH溶媒中でのIr光触媒とNiCl₂(dme)/dtbbpy特定系のΔE確認ではない）
* **Confidence**: High（Arias-Rotondo等のレビューの存在はHigh）; 特定系の数値比較はMedium–Low
* **注記**: SRG-7（C-3, U-8）に対応。このEPの完全充填には、実験溶媒中でのPC⁻/PCとNiII/Ni⁰の電位を同一条件で測定した論文が必要であり、既存の文献はどれも部分的充填に留まる可能性が高い

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点**: 未同定（直接比較実験の主題として発表された論文の特定が必要）
* **充填確立点**: 未同定（§E参照）
* **充填の性質**: —
* **Confidence**: Low（共通基質での光レドックス/Ni vs Pd/ホスフィン法の直接比較実験を主題とした論文は存在しないと推測するが、確認が必要）
* **注記**: RI-09の充填は通常、独立した「方法論比較論文」ではなく、新規合成標的の全合成論文中での条件スクリーニングとして間接的に現れる；photoredox/Ni法が先行法と直接比較されたものは総説・教科書レベルの記述に留まる可能性

---

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: Tellis, J.C.; Primer, D.N.; Molander, G.A. *Science* **2014**, *345*, 433–436（ref 16） — Full Paper相当の実験データを含む一次論文；典型的基質の収率データは同一条件で複数回測定が行われている可能性があるが、標準偏差の記載有無は確認が必要
* **充填確立点**: 同上
* **充填の性質**: Partial（Full Paper版の一次論文では再現実験が含まれると推定されるが、標準偏差の明示報告は慣行として疑わしい）
* **Confidence**: Medium（一次論文の存在はHigh; 標準偏差の報告はMedium）
* **注記**: 「標準偏差なし単回収率」はAccount形式に限らず合成化学のFull Paper全体での慣行であり、独立論文として充填される性質ではない；Account→Full Paper遷移で部分解消（B-3, B-11）

---

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: Primer, D.N.; Karakaya, I.; Tellis, J.C.; Molander, G.A. *J. Am. Chem. Soc.* **2015**, *137*, 2195–2198（ref 18）および Gutierrez et al. JACS 2015（ref 24）のSupporting Information — キラルHPLC条件とCV条件の詳細はFull Paper版の補足資料に記載されるのが慣行
* **充填確立点**: 同上（High confidence）
* **充填の性質**: Complete（Full Paper版Supporting Informationが存在すれば自動解消）
* **Confidence**: High（Full Paper SIでの解消は慣行的に確実）
* **注記**: このEPはAccount形式固有の問題であり、一次論文（ref 16, 18, 24等）のSIを参照すれば解消済みと見なせる；独立充填論文の探索は不要

---

**EP-07a Boundary-test pack（第三群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: —
* **Confidence**: Low
* **注記**: 失敗例の体系的報告はFull Paper版の補足または本文に含まれうるが、Account論文では意図的に省略されている；一次論文（ref 16, 18等）を確認することで部分解消可能。独立した「スコープ限界論文」は存在しない可能性が高い

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Gutierrez, O. et al. *J. Am. Chem. Soc.* 2015, 137, 4896 | EP-06a（部分）, EP-04a（基礎提供）| VQ-3 (Mechanism) | 2015 | High |
| 2 | Zuo, Z. et al. (MacMillan) *Science* 2014, 345, 437 | EP-03a（Stern-Volmer, 間接）| VQ-3 (Mechanism) | 2014 | High |
| 3 | Ting, S.I. et al. *J. Am. Chem. Soc.* 2020, 142, 5800 | EP-03a（PC*消光経路の競合定量）| VQ-3 (Mechanism) | 2020 | Medium |
| 4 | Primer, D.N.; Molander, G.A. *J. Am. Chem. Soc.* 2015, 137, 2195 | EP-08a（Full Paper版スコープ）, EP-01a（SI分析条件）| VQ-2 (Method) | 2015 | High |
| 5 | Arias-Rotondo, D.M.; McCusker, J.K. *Chem. Soc. Rev.* 2016, 45, 5803 | EP-05a（光触媒酸化還元電位の系統整備）| VQ-3 (Mechanism, 間接) | 2016 | High |
| 6 | エナンチオ選択的photoredox/Ni論文（Molander / Rovis グループ; 2017–2020年代; 具体論文は文献確認が必要） | EP-04a（温度依存性er, Hammett）| VQ-3 (Mechanism) | 2017–2020 | Low |

---

**選定理由：**

1番（Gutierrez et al. JACS 2015）は、この論文に対してVQ-3（Mechanism）の中核要件RI-06（Imported model）に最も直接的に関わる計算的充填の起点であり、論文自身がref 24として引用した唯一の機構DFT論文である。ただしベンジル系のみを扱い、二級アルキル外挿の問題（U-7）は未充填のまま残す。

2番（Zuo et al. Science 2014）は並行論文（ref 25）であり、Stern-Volmer消光という直接的実験手法でRI-03（Unobserved explanatory）への最初のアプローチを提供する間接的充填として重要。両論文を対比することで、Molander系とMacMillan系で共通の光触媒/ラジカル機構が支持されるかどうかを検証できる。

4番（Primer, Molander JACS 2015）はAccount論文の背後にある主要Full Paper相当の一次論文であり、RI-01・RI-08の自動解消源として機能する。実際に実験条件・分析詳細・スコープ再現データが含まれているかどうかを確認することで、VQ-2（Method）水準の充填を確認できる。

5番（Arias-Rotondo & McCusker）はSRG-7（C-3, U-8）に対応するEP-05aの間接的充填として機能し、光触媒系の熱力学的枠組み整備という観点でVQ-3への基礎を提供する。

6番はConfidence Lowのため暫定選定であり、実際のエナンチオ選択的photoredox/Ni論文の特定には文献検索が必要。EP-04a充填の確認が最もVQ-3達成に直結するため候補に加えた。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a, EP-08a → 2014–2015年 Primer, Molander JACS 2015 / Tellis et al. Science 2014（自己充填；Full Paper版SIへの移行で自動解消）
- VQ-3 要件 (RI-03): EP-03a → 2014年 Zuo et al. Science（間接、MacMillanグループによる充填開始）; 2020年 Ting et al. JACS（競合消光の定量）— 分野横断充填
- VQ-3 要件 (RI-06): EP-06a → 2015年 Gutierrez et al. JACS（ベンジル系DFT確立）; 二級アルキル系への拡張は未充填（長期遅延または未充填）
- VQ-3 要件 (RI-04): EP-04a → 2017–2020年代 エナンチオ選択的photoredox/Ni論文群（部分充填, Low confidence）— 技術駆動充填（エナンチオ選択的系の開発）
- VQ-3 要件 (RI-05, SRG-7): EP-05a → 2016年 Arias-Rotondo & McCusker（間接充填; 電位枠組み整備）
- VQ-4 要件: EP-09a → 現時点で未充填（直接比較実験なし）
- VQ-4 要件: EP-08a → 2015年（Full Paper版で部分解消）

**階層-時間対応の評価：**

本ケースは「VQ階層が上がるほど充填に要する時間が長くなる」という仮説を**部分的に支持する**。VQ-2要件（EP-01a, EP-08a）はAccount公表（2016年）以前に一次論文（2014–2015年）で実質解消されていた（自己充填）。VQ-3要件（RI-03, RI-06）は2014–2020年にかけて複数グループの研究で段階的に前進したが、二級アルキル系への計算的拡張（RI-06の核心）は6年後の2021年以降も充填されていない可能性がある。VQ-4要件（RI-09）はAccount公表から少なくとも8年以上が経過した現在も直接比較実験が確認されない。ただし時間的遅延が「技術的困難」によるものか「分野関心の欠如」によるものかはさらなる分析が必要。

**特筆すべきパターン：**

- **自己充填（VQ-2要件）**: Molander グループ自身が同年（2014–2015年）に公表した一次論文がAccount論文の背後でVQ-2水準を実質担保している。Accountは充填が完了した一次論文の概念的統合として機能しており、「Account出版時点ではVQ-2は既充填」という特殊な構造を持つ。
- **分野横断充填（RI-03）**: EP-03aのStern-Volmer充填はMacMillan/Doyleグループ（競合グループ）によって開始されており、競合グループの研究が充填を担う「競争的充填」パターン。
- **長期遅延充填（RI-06）**: ベンジルラジカルモデルから二級アルキルラジカル系への外挿検証（EP-06aの核心）は、convergence=3/3（全エージェントhigh評価）の最重要項目であったにもかかわらず、充填が遅延しているか未確認であり、分野がこの問いを体系的に回避している可能性を示唆する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

**EP-06a Analogy-validation pack（二級アルキルラジカル系への拡張部分）:**
* **未充填の理由**: 技術的困難 + 関心の欠如。ベンジルラジカルを二級アルキルラジカルに置き換えた場合のNi PES計算は、系の複雑さ（α位に置換基を持つ開殻Ni錯体の多配座TS探索）と計算コストの増大により技術的に困難であることが一因と推測される。分野が「ベンジル系での実証で十分」と暗黙的に受け入れた可能性も否定できない。
* **発見的意義**: あり。「光レドックス/Ni二元触媒の機構的理解はベンジルラジカルというactivated系に偏って構築されており、合成的に最も重要な二級アルキルラジカル系での計算的・実験的検証が2016年から現在まで欠落している」というパターンとして記録できる。これはRI-06（Imported model）が高頻度で充填されずに残存する合成方法論論文の典型例として、Codebookの事例集に追加できる。
* **将来の充填可能性**: 高。ORCA/Gaussian等での分散補正付きDFT（例：DLPNO-CCSD(T)/def2-TZVP//M06-L/def2-SVP）は現在十分に実用的であり、シクロペンチルラジカル系の計算は3–6ヶ月の計算研究で実行可能。また実験的にはシクロプロピルカルビニル-BF₃K合成（既知手順）と光レドックス/Ni条件での反応観察という実験的プローブも現在の標準的合成ラボで実施可能。

---

**EP-04a Discrimination / replication pack（Hammett解析部分）:**
* **未充填の理由**: 関心の欠如 + 分野慣行。エナンチオ選択的光レドックス/Niカップリングのer最適化研究は「配位子スクリーニング」として展開されており、Hammett解析（σ vs er回帰）という物理有機化学的アプローチは合成化学グループによって優先されにくい。
* **発見的意義**: あり。DKR立体制御モデルの統計的検証（n≥8, R², RMSE, Hammett解析）が提案から現在まで提供されていない場合、「定性的な3点相関を機構的証拠として扱う」という慣行が分野全体に定着している可能性を示す。
* **将来の充填可能性**: 高。合成が既知のpara置換アリールブロミド8–10種とラセミ二級アルキルBF₃Kを用いた系統的er測定は3–6ヶ月の実験で実施可能。

---

**EP-09a Internal benchmark pack（光レドックス/Ni vs 先行Pd-Suzuki直接比較）:**
* **未充填の理由**: 関心の欠如。光レドックス/Ni法の開発者グループにとって、先行法との直接比較実験は「先行法の優位性を一部認める可能性」を持つリスクがあり、独立した比較実験として発表する動機が低い。総説では言及されるが、主要論文の証拠として提示される例は少ない。
* **発見的意義**: あり。「手法論文が優位性を数値比較なしに主張し、分野全体がそれを受け入れる」という構造（RI-09が充填されないまま新手法が普及する）の事例として記録できる。これはパラダイム主張論文に特有の問題として、Stage 3 §6で提案したPRI-11（Format-mediated mechanistic shielding）とも関連する。
* **将来の充填可能性**: 中。直接比較実験は技術的には可能だが、発表の動機（誰がなぜこれを論文にするか）が依然として低い。総合的メタ分析または合成方法論比較論文の形での充填が現実的。
