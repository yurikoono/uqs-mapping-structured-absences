```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Yuan et al. 2018（Journal of the American Chemical Society, full_paper）

### §1 Claim Architecture

**コア主張：**
Yuan et al. (2018) は、Pd@MOF触媒によるHeckカップリング反応中のPd活性種の時系列変化を、カスタム設計の反応セルを用いたオペランドXAS（XANES + EXAFS）とPXRDの同時測定によって初めて追跡し、以下の三点を確立したと主張する。(1) 単核Pd(II)錯体が90°C以下での主要活性種であること、(2) 90°Cで平均13〜20個のPd原子から成るPdナノクラスターへの転換が起きること、(3) 触媒失活の主因が、PdナノクラスターへのCl⁻配位子による不可逆的被覆（Cl⁻毒化）であり、Pdリーチングでもたくし MOF構造崩壊でもないこと。

Novelty柱：MOF担持Pd触媒に対するオペランドXAS+PXRD法の初適用（方法論的先駆性）と、スペシエーション時系列・Cl⁻失活機構という具体的科学的結論（機構的先駆性）の両立。
Utility柱：「不均一系触媒に広く適用可能な手法」という一般化可能性の主張と、注入プロトコルによる触媒寿命延長への応用可能性。

**Layered structure：** あり。独立した二層構造が存在する。
- **層(a) 方法論的層**：カスタム反応セルによるオペランドXAS+PXRD同時測定が技術的に機能することを示す層。この層は、得られた化学的知見の正否とは独立して成立する。「ある種の不均一系触媒反応に対しオペランドXASが時分解スペシエーションデータを提供できる」という主張は、個別の機構的解釈が修正されても崩れない。
- **層(b) 科学的層**：XANES/EXAFS解析に基づくPdスペシエーション配列（Figure 7）とFigure 8の触媒サイクル提案、および「Cl⁻毒化が失活原因」という因果的結論。この層は、EXAFS/LCF解析の定量的信頼性（SRG-1）と対照実験の充足（SRG-5）に強く依存する。

層間の依存関係：層(a)は層(b)の前提条件であり、逆は成立しない。層(a)が崩れれば層(b)も崩れるが、層(b)の特定主張（例：Cl⁻毒化の因果性）が否定されても層(a)は存続する。この非対称性はVQ判定の層別分析に反映される。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [EXAFS/LCF定量的信頼性]**

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: EXAFS精密化においてLCF R-factor・χ²ν・残差スペクトルを全時点で開示し、二成分モデル（単核Pd(II) + Pd(0)クラスター）の三成分代替との比較を提示すること。固定パラメータの選択根拠と統計誤差を超えた系統誤差の定量的見積もりを付記すること。これらが充足されて初めて、Figure 6の分率曲線とFigure 7のスペシエーション時系列は独立検証可能な実験事実となる。
* **EP**: EP-08a [Replication / uncertainty pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: Pd K-edge LCFについて、全測定時点（オペランド実験の全スキャン）でR-factor・χ²ν・残差スペクトルを開示する。遷移期（44〜63分）における二成分モデルと三成分モデル（単核Pd(II) + 小Pdクラスター + 大Pdナノ粒子）のBIC比較を実施する。EXAFS精密化においてはS₀²・バックグラウンドスプライン・参照位相シフトに由来する系統誤差を数値的に評価（例：S₀²を±10%変動させた場合のCN変化量の明示）し、独立グループによる再解析が可能なrawデータとCIFを公開する。
* **注記**: B-1（high_convergence_low_gap, V1=high, V3=high, convergence 2/3, gap: none）、B-2（high_convergence_low_gap, V1=high, V3=high, convergence 2/3, gap: none）。SRG-1はVQ-4の必須要件（RI-08）の中核を構成する。

---

**SRG-2 [実験再現性と時間分解能]**

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: 動力学プロファイル（Figure 3）とオペランドXAS時系列（Figures 4–6, Table 1）について、少なくとも独立した3回の実験を行い、Pd–Pd CN値の初期値（31分: 0.4±0.8）など統計誤差の大きいデータポイントの再現性を確認すること。3.4 min/scan という時間分解能が検出可能な最短寿命中間体を定量的に限定する記述を付記すること。
* **EP**: EP-08a [Replication / uncertainty pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: Pd(II)@MIL-101-NH₂の同一オペランドXASプロトコルを3回独立に繰り返し、動力学プロファイルの転換率-時間曲線とTable 1の各CN値の平均・標準偏差を報告する。3.4 min/scan の時間分解能から、半減期 < 3 min の中間体は原理的に検出不能であることを明示し、それがFigure 8の中間体I〜VIの時間スケール評価に与える含意を議論する。時間分解能の向上（例：2020年代以降のbunch-modeシンクロトロン）で得られうる追加情報を展望として記述する。
* **注記**: B-3（V3 only, convergence 1/3）、B-13（high_convergence_low_gap, V1=medium, V3=medium, convergence 2/3, gap: none）。SRG-2はVQ-4の必須要件（RI-08）に属するが、B-3の低収束（1/3）は致命性判定においてNon-fatalの傾向を示す。

---

**SRG-3 [Figure 8触媒サイクルの実験的根拠]**

* **Primary RI**: RI-06 [Imported model]
* **Secondary RI**: RI-03 [Unobserved explanatory]; RI-05 [Qualitative overread]
* **ER**: Figure 8の触媒サイクルが輸入元（均一系Pd触媒の既知機構）と対象系（MOF担持Pd）において同型の動力学を持つことを、独立した実験（Hammett相関、添加塩実験、または中間体相当物のXAS特性評価）で示すこと。Aniline surrogateがMOFリンカーと同一の配位幾何学を提供することをXASまたはNMRで実証すること。「陰イオン機構（OAc⁻）は起こりにくい」という排除を定性的議論ではなく速度論的数値で支持すること。
* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: (a) aniline–Pd錯体とMOF担持Pd両者のPd K-edge EXAFS（Pd–N距離・CN値）を同一条件で測定し、配位幾何学の等価性または差異を数値的に示す。(b) 電子特性の異なるアリールハライド（σ_p: −0.66〜+0.78）でのHammett実験を実施し、ρ値の符号からcationic/neutral pathwayの速度論的優劣を判別する。(c) Figure 8の中間体IVに相当する「Pd(II)–L–アリール–オレフィンπ錯体」モデルをin situでXANES観測する、または溶液モデル系で¹H NMR/XASにより特性評価する。
* **注記**: U-1（high_convergence_low_gap, V1=high, V2=high, convergence 2/3, gap: none）、A-1（V1=high, V2=high, convergence 2/3）、B-16（V2 only, convergence 1/3）。**PRI-11（Mechanism-kinetics decoupling）の適用候補：** XASスペシエーション比率（Pd(II)/Pd(0)）から速度式を代数的に導出せず、「cationic機構が優位」と結論している点は、PRI-11の定義に合致する。昇格判断の3報目確認事例として記録する。RI-05の重大残存（「OAc⁻は起こりにくい」という定性的排除）はVQ-3をQualifiedにする直接因子。**標識不整合（Labeling mismatch）パターン：** 本文の「a mechanism … was proposed and shown in Figure 8」という事実的記述語と、図注内の「Alternative neutral mechanism … is possible but unlikely」という限定的仮説標識が共存している。仮説標識の位置が図の末尾1文に集約される典型的パターン。

---

**SRG-4 [Cl⁻毒化メカニズムの因果実験の不在]**

* **Primary RI**: RI-07 [Unsupported boundary]（RI-07拡張適用：否定的境界主張）
* **Secondary RI**: RI-08 [Unquantified reliability]; RI-04 [Unreplicated discriminator]
* **ER**: 「Cl⁻が活性部位を不可逆的に遮断する」という因果的失活主張には、(a) 活性触媒への外因性Cl⁻添加による失活の再現実験、(b) 失活触媒からのCl⁻除去（スカベンジャー処理）による活性回復実験、(c) [Cl⁻]と失活速度の定量的用量応答関係が最低限必要である。ICP-OESのPd/Cl比は反復測定（n≥3）と分析不確かさの明示が必要。
* **EP**: EP-07a [Boundary-test pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: (a) 活性なPd@MIL-101-NH₂触媒（転換率30〜50%の段階）に定量的NaClまたはTBAClを添加し、GCで転換率-時間プロファイルへの影響を測定して[Cl⁻]依存の失活速度定数を算出する。(b) 失活後の触媒をAg⁺（AgNO₃, 3当量）またはチオールスカベンジャーで処理してCl⁻を除去し、新鮮試薬を加えた際の触媒活性回復の可否を確認する（回復すればCl⁻毒化の可逆性、回復しなければ他の不可逆的失活因子の存在を示す）。(c) ICP-OESによるPd/Cl比をn=3以上で反復測定し、95%信頼区間を報告する。
* **注記**: U-3（high_convergence_low_gap, V2=high, V3=high, convergence 2/3, gap: none）、B-11（V3 only, convergence 1/3）、B-12（V1 only, convergence 1/3）。「不可逆的なCl⁻キャッピング」という断定的結論はRI-07拡張適用の明確な事例。B-12の陰性リサイクルデータがESIのみに存在する（A-2 ↔ B-12のpivot構造）。

---

**SRG-5 [Pdスペシエーション帰属のための対照実験の不在]**

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: Pdスペシエーション変化の時系列が触媒的ターンオーバーに起因することを確立するには、(a) 基質不在（溶媒+塩基のみ）での同一昇温プロトコル実験、(b) 90°Cへの直接等温開始実験（昇温プロトコルの履歴効果排除）、(c) H₂O閾値濃度の定量化が必要である。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-07a [Boundary-test pack]
* **Case-specific実装**: (a) DME/H₂O（3:1）/NaOAc（2当量）を含む反応セルにPd@MIL-101-NH₂を分散させ、ArI・スチレン不在でFigure 2と同一プロトコル（RT→60→80→90°C）のオペランドXANES/EXAFSを取得し、Pdスペシエーション変化の「熱的成分」を定量する。(b) Pd触媒を全試薬と共に直接90°Cの反応セルに注入し、オペランドXASを取得してstepwise-rampプロトコルとのスペシエーション軌跡を比較する（ramp-history効果の分離）。(c) H₂O体積を0.05〜2.0 mLで系統変化させた一連のXAS実験を実施し、Pd(0)ナノクラスター出現のH₂O閾値体積を決定する。
* **注記**: U-2（high_convergence_low_gap, V1=medium, V2=medium, convergence 2/3, gap: none）、B-7（high_convergence_low_gap, V1=medium, V2=high, convergence 2/3, gap: low）、B-8（high_convergence_low_gap, V1=medium, V3=medium, convergence 2/3, gap: none）。SRG-5はVQ-3の必須要件（RI-03）の中で最も実験的に解消しやすく、既存ビームライン装置でブランク実験として実施可能。

---

**SRG-6 [定量的性能指標と汎用性主張]**

* **Primary RI**: RI-09 [External superiority]
* **Secondary RI**: RI-05 [Qualitative overread]; RI-07 [Unsupported boundary]
* **ER**: 「広く適用可能な手法」および「Pdナノクラスターはより高活性」という主張には、TON/TOFの計算と引用先行研究との数値比較、表面原子当たりTOFの報告、複数基質での活性確認が必要。
* **EP**: EP-09a [Internal benchmark pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: (a) p-ヨードベンゾニトリル＋tert-ブチルアクリレートの完全転換から得たGCデータを用い、触媒量（0.075 mmol Pd）基準のTON（mol product/mol Pd）とTOF（h⁻¹）を算出し、Introduction引用のMOF-Heck先行研究（ref 13, 14: Pascanu et al.）の同一数値軸で比較する。(b) EXAFS由来のPd–Pd CN値とPdクラスターサイズモデル（~13原子, ~1 nm）から表面Pd原子数を見積もり、表面原子当たりTOFを報告してref 35の文献値と比較する。(c) 電子的に異なるアリールハライド（ブロモベンゼン、ヨードアニソール）を用いた追加Heck実験を実施して「広く適用可能」の根拠を拡張する。
* **注記**: C-1（引用先行研究との定量比較なし）、B-17（TOF規格化なし, V2 only, 1/3）、B-4（high_convergence_low_gap, V1=medium, V2=high, convergence 2/3, gap: low）。SRG-6はVQ-4の第二目的関数に位置し、VQ-3到達後の追加実験として位置づける。

---

SRG外：CLA

**CLA-1: E/Z選択性未活用と内球機構診断の欠如** (B-6)

* **Primary RI**: RI-03 [Unobserved explanatory]（サブタイプ: Available-but-unutilized characterization）
* **ER**: GC分析によって取得済みのスチルベンデータからE/Z比を抽出・報告すること。Figure 8が提案する内球migratory insertion（Eスチルベン優先）の診断として、E/Z比が各反応条件（60°C単核Pd優位 vs. 90°Cクラスター優位）で温度・触媒種に依存するかを評価すること。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: 既存GC実験のクロマトグラムからE/Z-スチルベンピーク面積比を再抽出し（新規実験不要）、温度と触媒種変化に対するE/Z比の変動を報告する。内球（β-H脱離優位 → E選択的）vs. 外球（Heck-Smiles機構 → E/Z混合）のどちらを支持するかを議論する。
* **注記**: B-6（V2 only, convergence 1/3）。**RI-03 Available-but-unutilizedサブタイプの典型事例：** GC分析は実施済みであり転換率計算に使用されているにもかかわらず、診断的価値を持つE/Z比がいかなる場所にも報告されていない。追加実験なしに既存データの再解析のみで部分的充足が可能な点でEP投入コストが最も低い。

**CLA-2: オペランド条件代表性の報告問題** (B-5, B-14)

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-07 [Unsupported boundary]
* **ER**: 試薬濃度2倍・カスタム反応器というオペランド固有の条件が標準条件（0.1 mmolスケール、通常ガラス器具）に対して「測定可能な差異を導入しない」ことを、ペア実験（matched-pair control）で定量的に確認すること。本文には「Control experiments confirmed … no further differences were observed」との記述があるが、この制御実験の定量的データ（転換率-時間プロファイルの比較、Pdスペシエーションの比較）が主文・SIのいずれにも開示されていない。
* **EP**: EP-01a [Reporting-coherence pack]; EP-07a [Boundary-test pack]
* **Case-specific実装**: 標準条件（0.1 mmol ArI, DME 1.5 mL, 0.003 mmol Pd@MOF）でのHeck反応のNMR動力学プロファイルをFigure 3と並置して比較する。反応完了後の標準条件触媒のXANES edge position（Pd酸化状態）とEXAFS Pd–Cl CNをオペランド実験の対応値と比較し、2倍濃度条件が最終スペシエーション（recycled触媒状態）に影響しないことを数値で示す。
* **注記**: B-5（V1 only, convergence 1/3）、B-14（V1 only, convergence 1/3）。本文に「Control experiments confirmed … no further differences」とある点から、実験は実施済みの可能性が高く、データ開示の問題として記録する。

**CLA-3: Wacker型酸化の量論的予測検証の欠如** (U-4)

* **Primary RI**: RI-04 [Unreplicated discriminator]（サブタイプ：自己矛盾的不在——論文自身のモデルが予測する量が未検証）
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: Figure 8のPd(II)→Pd(0)還元がWacker型オレフィン酸化と量論的に連動するという機構的提案に対し、30 mol% Pd実験で観測されたアルデヒドの¹H NMRシグナルを積分定量し、EXAFS Figure 6から算出したPd(0)形成モル数との量論的一致（理論比1:1）を検証すること。
* **EP**: EP-04a [Discrimination / replication pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: 30 mol% Pd条件でのXAS実験において、¹H NMRの9.9〜9.6 ppmアルデヒドシグナルを内部標準に対して積分し、アルデヒド生成物のモル収率を算出する。EXAFS Figure 6の対応時間点でのPd(0)フラクション（LCF）×Pd負荷量（mmol）から予測されるオレフィン酸化量と比較し、量論的整合性（理論値との一致または乖離）を評価する。
* **注記**: U-4（V2 only, convergence 1/3）。論文が「Wacker型酸化でPd(0)が生成する」という機構的主張の検証に30 mol%実験を使用しながら、その検証量を定量していない点は自己矛盾的不在パターンの典型。

---

### §3 現在のVQ判定

**現在判定: VQ-2 [Method]**（非致命的残存を伴う）

**VQ-1 [Observation] は通る。**
触媒材料（Pd(II)@MIL-101-NH₂, Pd(II)@MIL-88B-NH₂）の同定はXAS・PXRD・TEM/EDSで確立されており、生成物（スチルベン、アルデヒド）の同定もGC・NMRで裏付けられている。RI-02に対する致命的欠如はない。

**VQ-2 [Method] は通る**（非致命的残存を伴う）。
VQ-1継承を前提とする。CLA-2（B-5, B-14）にRI-01の残存がある——試薬2倍・カスタム反応器の代表性は「制御実験で差異なし」と本文に明記されているが、その制御実験データが定量的に開示されていない点でRI-01が部分的に残存する。しかし本文記述により方法論の境界設定は明示されており、Non-fatalとみなせる。SRG-4（RI-07）とSRG-6（RI-07）の残存は機構的主張の境界問題であり、VQ-3の文脈でより重要であるためVQ-2の水準では致命的ではない。

**VQ-3 [Mechanism] は未達。**
VQ-2継承を前提とする。RI-03（SRG-3, SRG-5）、RI-04（SRG-1, SRG-2）、RI-06（SRG-3）が未解消。
- **RI-03（Fatal）**: SRG-3（U-1）では、Figure 8の触媒サイクルの中間体I〜VIが直接観測も速度論的拘束もされておらず、XASスペシエーションデータが素反応を確立できないことが示されている。SRG-5（U-2）では、触媒添加直後のPdスペシエーション変化が触媒的ターンオーバーに起因するのか単純な熱的・溶媒和効果によるのかを区別するブランク実験が存在しない。両者は機構的帰属の基盤に関わりFatalである。
- **RI-04（Fatal）**: SRG-1では、LCF分析の二成分モデル（Figure 6）が全時点でfit品質指標を欠いており、スペシエーション配列の定量的信頼性が独立検証不能。SRG-2では単一ランのデータのみで再現性未確認。
- **RI-06（Non-fatalだが構造的）**: SRG-3のaniline surrogate妥当性は未実証だが、aniline–Pd配位の一般的受容を考慮するとNon-fatal。ただしRI-06の「サイクルレベル輸入」（均一系Heck機構をMOF系に一括輸入）は構造的問題として残存する。
- **RI-05の重大残存**: SRG-3（「OAc⁻機構は起こりにくい」という定性的排除）とSRG-6（「サイズのみから判断して活性が高い」という定性的優位性）の両所でRI-05が重大に残り、VQ-3到達時もQualifiedとなる。

**VQ-4 [Benchmark] は未達。**
VQ-3が未達のため継承原則によりVQ-4も未達。SRG-1（RI-08）、SRG-2（RI-08）、SRG-6（RI-09）が未解消。

**層別VQ非対称性：**
§1のLayered structureより：
- **方法論的層(a)単独では：** カスタム反応セルの設計・動作記述（Figure 1, 2）はRI-01の非致命的残存のみを伴い、VQ-2 [Method]に到達している。「オペランドXAS+PXRD反応セルがMOF-Heck系において機能する」という主張は現在のデータで支持される。
- **科学的層(b)は：** RI-03（Figure 8の機構的帰属）とRI-04（EXAFS/LCFの定量的信頼性）が未解消のままであり、VQ-3に到達していない。

---

### §4 Era-Norm Annotation

**communication-era tolerated（2018年 JACS Full Paper の文脈）：**

- B-3（単一ランの動力学プロファイル）: 2018年のオペランドXAS研究では、ESRFビームタイムは通常72時間以下の割り当てであり、単一触媒系の完全実験（昇温+冷却サイクル）が1回3〜5時間を要することを考慮すると、複数回独立実験は慣行上行われていなかった。
- B-9（GCキャリブレーション詳細の省略）: GCの詳細なプロトコル（カラム種、検出器、キャリブレーション標準）をSIに委ねる慣行は2018年当時のJACS Full Paperで標準的であり、今日よりも許容度が高かった。
- B-10（TEM粒子計数の省略）: TEM観察に際して統計的に十分な粒子計数（n≥100）を報告することは2018年には普及しておらず、代表的ミクログラフの提示が慣行であった。
- B-13（時間分解能の限界の非開示）: オペランドXASの時間分解能が観測可能な中間体寿命を制限することへの明示的議論は、2018年当時の関連コミュニティでまだ標準化されていなかった（2020年代に入ってから慣行化が進んだ）。
- B-15（多重散乱パスの未検討）: 2018年当時のEXAFS精密化において、Pd–Cl–Pdのような多重散乱パスを包括的に試験・排除することは一般的慣行ではなかった。

**modern-era deficient（現代の再認定では許容できない欠落）：**

- B-1, B-2（LCF fitメトリクス、EXAFS系統誤差の非開示）: 2020年代以降、XAS分野の報告標準（IUCr guidelines, XAFS Society protocols）においてLCF R-factor・残差スペクトルの開示と系統誤差の定量的見積もりは必須化されており、現代の査読では必ず要求される。*両タグ記載：当時も高水準論文では期待されたが現代では必須。*
- U-3（Cl⁻毒化の因果実験の不在）: 現代の触媒科学では、失活機構の断定には相関から因果への橋渡し実験（添加・除去実験、用量応答）が必須とみなされる。
- SRG-5全体（U-2, B-7, B-8の対照実験不在）: 段階的温度プロトコルと基質なしブランク実験の不在は、現代では機構的帰属の根拠として原則認められない。
- B-12（陰性リサイクルデータのESIのみへの集約）: 主要な陰性結果（標準プロトコル下の完全失活）をESI専用とし、main textで注入プロトコルを「リサイクル可能性」として提示する慣行は、現代の再現性・透明性基準の下では問題視される。

---

### §5 最短補強ルート

**VQ-3への最短ルート（第一目的関数）：**

1. EP-08a [Replication / uncertainty pack] — LCF全時点R-factor/χ²ν/残差スペクトルの開示と、オペランドXASの3回独立複製実験を実施する。RI-08を前進（SRG-1, SRG-2）。最高情報利得：論文の中核定量データ（Figure 6のLCF分率）の独立検証可能性を確立し、SRG-1とSRG-2を同時に前進させる。既存データのre-analysisとrawデータ公開で部分充足可能。
2. EP-03a [Direct-observation / state-assignment pack] — 基質不在（溶媒+塩基のみ）での同一昇温プロトコルのオペランドXAS（ブランク実験）を実施する。RI-03を前進（SRG-5）。最小コストで触媒的 vs. 熱的Pdスペシエーション変化を分離でき、U-2の「自己矛盾的不在」を解消する最も直接的な実験。
3. EP-07a [Boundary-test pack] — H₂O閾値定量（EP-03aと連動）+ 活性触媒へのCl⁻添加実験を実施する。RI-07を前進（SRG-4）、RI-03を前進（SRG-5 B-8）。Cl⁻毒化の因果性（U-3）とH₂O必須性の定量的確立（B-8）を同時に進める。
4. EP-06a [Analogy-validation pack] — aniline–Pd錯体のXAS測定によるMOFリンカー代替妥当性の検証 + Hammett実験によるcationic/neutral pathway区別。RI-06を前進（SRG-3）。SRG-3のRI-03とRI-05への間接的前進にもつながる（Hammett ρ値が機構的排除に定量的根拠を与える）。

認定ゲート順注記：実験投入順は情報利得順（EP-08a → EP-03a → EP-07a → EP-06a）だが、最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4のゲート順で確定する。すなわちEP-03aとEP-06aがRI-03とRI-06を解消してもVQ-3への認定にはRI-04（SRG-1, SRG-2）の解消（EP-08a）が前提として必要である。

**VQ-4への最短ルート（第二目的関数、VQ-3到達後）：**

5. EP-09a [Internal benchmark pack] — TON/TOF計算と先行研究（ref 13, 14）との数値比較、Pd表面原子当たりTOF報告。RI-09を前進（SRG-6）。
6. EP-05a [Quantitative-ranking substantiation pack] — 複数基質ペア（3系以上）での活性確認と「広く適用可能」主張の実証。RI-05を前進（SRG-6）。RI-05の残存解消によりVQ-3 QualifiedからVQ-3 Fullへの引き上げ効果もある。

---

### §6 制度設計への寄与

**1. RI-08の新代表事例（XAS/LCF分野）：**
EXAFS/LCFにおける「LCF R-factor未報告」パターンは、オペランドXAS研究でRI-08が適用される典型的事例を提供する。特に、時間分解測定では全時点でのfit-quality開示が要求されるため、時分解オペランドXAS論文に対するRI-08の適用基準として「全時点でR-factor・残差スペクトルを要求する」という定義の強化候補として記録する。

**2. PRI-11（Mechanism-kinetics decoupling）の3報目確認事例：**
Figure 8の触媒サイクルが、Pd(II)/Pd(0)のXANES LCF分率変化からcationic pathwayの優位性を速度式導出なしに結論している点は、PRI-11の定義「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」に合致する。Breitenfeld 2014とPengfei 2024に続く3報目の確認事例として記録する。2報の独立確認が既に充足されており、本ケースが加わることでPRI-11の正式昇格を推奨する。

**3. RI-06 スコープ注記（サイクルレベル輸入）の新事例：**
aniline surrogateによるMOFリンカー配位環境の代替は、個別の素反応ステップの類推ではなく、均一系Heck触媒サイクル全体（cationic Pd(0)サイクル）をMOF担持系に一括輸入した「サイクルレベル輸入」である。この適用事例はRI-06のサイクルレベル輸入注記の代表的実装例として記録する。

**4. 標識不整合（Labeling mismatch）パターンの確認：**
本文「a mechanism … was proposed and shown in Figure 8」という事実的記述語と、Figure 8の末尾注「Alternative neutral mechanism … is possible but unlikely」という仮説標識が共存する。仮説標識の位置が図内の末尾1文に集約され、本文記述が事実的叙述語を使用するパターンは、RI-06と連動するlabeling mismatchの典型例として記録する。SRG-3のRI-05残存の直接的原因でもある。

**5. RI-03 Available-but-unutilized サブタイプの明確事例：**
CLA-1（B-6: E/Z比）は、GC分析が実施済みで転換率計算に使用されているにもかかわらず、診断的価値を持つE/Z比が論文本文で抽出されていない純粋な「Available-but-unutilized」ケースである。追加実験なしにデータ再解析のみで部分的充足が可能な最低コスト事例として、EP-03aのcase-specific実装に追加する。

**6. VQ-3 Qualified の構造的固定パターン（オペランドXAS論文）：**
本論文はRI-05の重大残存（定性的活性比較、定性的機構排除）がVQ-3をQualifiedに固定するパターンの典型例を提供する。オペランドXAS論文において、スペクトロスコピーデータが「種の存在比」を提供するが「速度順序」を提供しない構造的制限は、SRG-3とSRG-6の組み合わせとして「オペランドXAS論文のVQ-3 Qualified固定因子」パターンに記録する。
```
