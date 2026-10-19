```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Shirai et al. 2024（J. Org. Chem., Note）

### §1 Claim Architecture

**コア主張の要約**

本論文は、パラジウム触媒による未活性化アルケンのReductive Heck ヒドロアリール化を室温条件下で達成したと主張する。Novelty柱は二つある：（i）**合成的新規性**——従来法（>100 °C、アミン/アルコールヒドリド源）の三つの欠点（高温、極性官能基不適合、還元感受性置換基不耐性）を、PMHS/CsFの遅い添加という操作で克服した室温プロトコル；（ii）**機構的新規性**——重水素標識実験に基づく二重触媒サイクル（主サイクルvs副サイクル）の提案。Utility柱として、脂肪酸アルキルアレーン骨格を持つFDA承認医薬品への適用可能性と「laboratory-scale and industrial synthesis」への有用性が主張されている。

**Layered structure の判定**

独立層構造：**有り（3層独立）**

- 層a（合成的新規性：室温反応 + PMHS/CsF系）
- 層b（スコープ新規性：極性・還元感受性官能基への適用）
- 層c（機構的新規性：二重触媒サイクルの提案）

層間依存：層bは層aに依存する（mild conditionsがない場合、FG耐性の文脈が失われる）。層cは層a・bから独立している——双触媒サイクルモデルを反証しても合成的・スコープ的主張は崩れない。逆に層cを確立しなくても層a・bの成立は損なわれない。**単一の反証で全主張が崩れる構造ではない。**

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Mass balance incompleteness]**（B-1, B-2）

* **Primary RI**: RI-08 [Unquantified reliability] — RI-08 内部矛盾型サブタイプ：Entry 12（38% + 21% + 19% + 16% = 94%）およびEntry 13（82% + 0% + 11% = 93%）で各成分の合計が100%に未達。
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: 全成分の収率合計が100% ± 測定誤差になるよう物質収支を完閉させるか、不一致がある場合はその原因（測定誤差範囲内か未同定副生成物か）を明記する必要がある。
* **EP**: EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: Entry 12およびEntry 13の反応をn≥3で繰り返し、各成分（1a, 3aa, 1b, 1c）のNMR収率と標準偏差を報告する。6〜7%の未回収分を確認するためにGC-MSまたはLC-MSで反応混合物の全成分を検索する。
* **注記**: B-1（V1=medium, V3=high; convergence 2/3; gap=low）、B-2（V1=medium, V3=high; convergence 2/3; gap=low）。TEMPERATURE_SUMMARY: high_convergence_low_gap。

---

**SRG-2 [Side cycle evidence inadequacy]**（A-1, U-2）

* **Primary RI**: RI-03 [Unobserved explanatory] — 副サイクルの鍵中間体であるベンジルPd中間体（IX）が直接観測も速度論的拘束もされておらず、唯一の証拠がδ位0.2D取り込みという単一値。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 0.2Dという値に精度保証がなく（SRG-3と連動）、これを副サイクル存在の識別子として使用している。
* **ER**: 副サイクル中間体（IX）を直接観測（分光学的同定または捕捉実験）するか、または速い添加条件下での重水素実験（Entry 12相当）でδ位D取り込みが遅い添加条件より増加することを示し、モデルの中心的予測を検証する必要がある。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: 重水素標識アミド基質（1a, 0.9D）を速い添加（0 h、Entry 12条件）と遅い添加（6 h、Entry 13条件）の両条件で反応させ、各生成物（3aa-d2相当）のγおよびδ位D取り込み比率を2H NMRで定量比較する。U-2が提起する「速い添加でδ-D増加」というモデル予測を直接検証する。
* **注記**: A-1（V1=high, V2=critical; convergence 2/3; gap=low; high_convergence_low_gap）、U-2（self-contradictory absence; severity=high）。SRG-3と密接に連動：RI-04の解消（SRG-3のEP-04a）が本SRGのRI-03前進の前提条件となる。

---

**SRG-3 [Deuterium experiment reliability]**（A-4, B-7）

* **Primary RI**: RI-04 [Unreplicated discriminator] — 0.8D（γ位）および0.2D（δ位）という値が単一NMR測定から報告されており、精度・再現性データなし。0.2Dは1H NMR積分誤差（±5〜10%）と同程度の値であり、分析的識別力が担保されていない。
* **Secondary RI**: RI-08 [Unquantified reliability] — NMR測定法（1H積分 vs 2H NMR）、取得回数、不確かさ範囲が記載されていない。
* **ER**: 重水素取り込み値に不確かさ範囲を付して報告する（n≥3の2H NMR定量推奨）。加えて、反応条件下（Pd(OAc)2, CsF, AcOEt, r.t.）でのアミドN-D → N-H交換速度をコントロール実験で確認し、重水素化アミドからのH/D交換が測定値に影響しないことを示す必要がある。
* **EP**: EP-04a [Discrimination / replication pack]
* **Case-specific実装**: 重水素化アミド（1a, 0.9D）を反応条件下でArI不在（または基質不在）でインキュベートし、24 h後のN-D保持率を1H NMRで定量（H/D交換コントロール）。本重水素実験（Figure 3b）を独立3回実施し、γ位（0.8D）とδ位（0.2D）の平均値と標準偏差を2H NMRで報告する。
* **注記**: A-4（V1=medium, V2=high; convergence 2/3; gap=low）、B-7（V2=high, V3=high; convergence 2/3; gap=none）。両方ともhigh_convergence_low_gap。RI-04 + RI-08の共起パターン（§6参照）。

---

**SRG-4 [Dropped Quantitative Benchmark]**（B-5, C-1）

* **Primary RI**: RI-09 [External superiority] — 「comparable to or higher than those previously reported」という主張が、先行研究（refs 16, 18, 19, 20）との基質対応直接比較なしに文章のみで提示されている。
* **Secondary RI**: RI-05 [Qualitative overread] — 数値根拠なしに半定量的「comparable」比較を行っている。
* **ER**: 先行研究（少なくとも Wang/Wu/Loh 2018、ref 16）と同一の基質（2〜3例）を本条件と先行条件で並行実施し、同一内部標準を用いたNMR収率で直接比較する対照実験を設ける必要がある。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: Ref 16（Wang/Wu/Loh JACS 2018）の報告基質セットから、γ位選択例（n=1, 末端アルケン）およびδ位選択例（n=2, 末端アルケン）を各1例選択し、本条件（PMHS, CsF, AcOEt, r.t., 24h）とref 16条件（Pd2(dba)3, Cy-Johnphos, PS/TFA, DMPU, 130°C）で同一基質を並行実施する。
* **注記**: B-5（V1=high, V3=medium; convergence 2/3; gap=low）、C-1（refs 16, 18, 19, 20の対称的引用切断）。high_convergence_low_gap。

---

**SRG-5 [Table 1 correction unspecified]**（B-6）

* **Primary RI**: RI-01 [Reporting integrity] — 2024年2月6日に再掲載された訂正版Table 1に変更点のchangelogがなく、機構解釈の中核であるEntry 12（21%）およびEntry 13（82%）が訂正対象だったか否かを検証できない。
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: 訂正Noteまたは著者への問い合わせを通じて、変更されたセル（Entry番号、旧値、新値）を特定し、機構的解釈に影響する値が訂正対象か否かを確認する必要がある。
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific実装**: J. Org. Chem. DOI 10.1021/acs.joc.3c02488の出版履歴（ASAP版vs最終版）の差分をACS Publications履歴またはCorrespondence著者へのコレスポンデンスで確認し、変更対象をリスト化する。Entry 12/13のどちらかが変更されていた場合は、機構的主張（dual cycle hypothesis）の証拠基盤の再評価が必要となる。
* **注記**: B-6（V1=medium, V3=high; convergence 2/3; gap=low）。high_convergence_low_gap。erratum-corrected-version-unclear。

---

**SRG-6 [Excess PMHS contradicts dual-cycle model]**（B-8, U-1）

* **Primary RI**: RI-03 [Unobserved explanatory] — 脚注b/c/d条件（PMHS 3.1〜4.1 equiv）で使用されたSi-PdII-Hの定常濃度が未測定であり、dual-cycle modelの「PMHS増量 → Si-PdII-H増加 → 副生成物増加」という予測が成立しているかどうかを確認できない。
* **Secondary RI**: RI-06 [Imported model] — dual-cycle modelそのものが先行研究（refs 8–10）から輸入されており、対象系（PMHS/CsF/Pd(OAc)2/r.t.）での過剰PMHS使用時の挙動が独立に検証されていない。
* **ER**: 脚注b/c/d条件での基質について副生成物（1b, 1c）の収率を報告し、PMHS増量に対する副生成物比率の応答（モデルの予測と整合的か）を確認する必要がある。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: 3aa基質について、PMHS量を0.5（2.0 equiv）→ 0.75（3.1 equiv）→ 1.0 mmol（4.1 equiv）と段階的に増加させ（遅い添加速度比を一定に保ちながら）、各条件でのEntry 13相当の1b, 1c収率をNMR内部標準法で定量比較する。
* **注記**: B-8（V1=medium, V2=medium; convergence 2/3; gap=none）、U-1（self-contradictory absence; severity=medium）。

---

**SRG-7 [CsF role uncharacterized]**（B-11）

* **Primary RI**: RI-03 [Unobserved explanatory] — CsFのfluoride activator機能（五配位シリカート形成）とBrønsted base機能（pKaH of HF ≈ 3.2）が実験的に分離されておらず、CsFの役割が未確定。
* **Secondary RI**: RI-05 [Qualitative overread] — CsFのfluoride活性化機構のみを先行研究から引用することでBrønsted base機能を定性的に排除している。
* **ER**: フッ化物供給能と塩基性を独立に変化させた試薬（CsF, CsOAc, TBAF, TBASF等）の比較コントロール実験によって、CsFの各機能への寄与を実験的に分離する必要がある。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: 3aa形成について、CsF（2.0 equiv）/ CsOAc（2.0 equiv, non-fluoride塩基）/ TBAF（2.0 equiv, fluoride非塩基）/ CsI（2.0 equiv, non-fluoride非塩基）を等量比較する一連のコントロール実験を実施し、収率とprotodepalladation比率（重水素標識実験での0.8D/0.2D）のCsF依存性を確認する。
* **注記**: B-11（V1=low, V2=medium; convergence 2/3; gap=low）。high_convergence_low_gap。

---

**SRG-8 [Scope anomalies unexplained]**（B-4）

* **Primary RI**: RI-05 [Qualitative overread] — Thorpe-Ingold効果の予測に反する低収率と、内部アルケン > 末端アルケンという反直感的収率逆転が観察として記録されるが機構的説明が添えられていない。
* **Secondary RI**: RI-03 [Unobserved explanatory] — 速度決定段階（移行挿入前後）のどこで基質依存性が生じるかが観測されていない。
* **ER**: 各スコープ異常について、少なくとも反応速度プロファイル（時間 vs 収率）の比較か、または副生成物（1b, 1c）比率の比較によって、速度決定段階に関する定量的なデータを提示する必要がある。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: 末端（3aa）vs 内部アルケン（3ea）のペアを同一条件下で3, 6, 12, 24 h時点でサンプリングし、3aa/1b/1cの時間プロファイルを比較する。直鎖（3aa）vs 分岐（3fa, 3ga）のペアについても同様のプロファイルを取得し、Thorpe-Ingold効果の発現するはずの環化段階（移行挿入）が律速でないことを検証する。
* **注記**: B-4（V1=medium, V2=medium; convergence 2/3; gap=none）。

---

### SRG外：CLA

---

**CLA-1: NMR yield foundation**（B-3）

* **Primary RI**: RI-08 [Unquantified reliability] — ジベンジルエーテル内部標準の反応条件下（Pd(OAc)2, PMHS, CsF, AcOEt, r.t., 24h）での安定性確認実験が存在しない。かつ、Table 1および Figure 2の全収率データが単一測定値に基づく。
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: 全収率データの信頼性基盤として、（i）ジベンジルエーテルの反応条件下安定性コントロール実験、および（ii）Entry 12とEntry 13（機構解釈の核心）のn≥3反復測定が必要。
* **EP**: EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: ジベンジルエーテル（内部標準量相当）をPd(OAc)2 10 mol%, PMHS 2.0 equiv, CsF 2.0 equiv, AcOEt, r.t., 24hで基質不在下にインキュベートし、回収率を1H NMRで定量する（代替標準：PhSiH3など過剰PMHSに対して安定な候補と並行比較）。
* **注記**: B-3（V3=high; convergence 1/3）。D-4候補3のうちSRG未割当部分。

---

**CLA-2: Practical synthesis claim vs actual conditions**（B-10, U-3, A-2）

* **Primary RI**: RI-07 [Unsupported boundary] — 「laboratory-scale and industrial synthesis」という肯定的境界主張が、ArI限定スコープ・10 mol% Pd・TON未報告・ラジカル/イオン機構未区別という実験的状況と対立している。
* **Secondary RI**: RI-03 [Unobserved explanatory] — 遅い添加条件下でのSi-H不足によるPdII→Pd0再生効率（触媒の生産的ターンオーバー）が未観測（U-3 self-contradictory absence）。
* **ER**: 触媒量-収率プロファイル（TON算出）、ArBrまたはArClの適用テスト（またはその不可根拠の明示）、および反応後のPd回収率確認（触媒失活の有無）が必要。ラジカル経路はTEMPO添加実験で排除する必要がある。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: 3aa形成について触媒量を10→5→2→0.5 mol%と変化させ最大TONを決定する。ArBr（Li/Gong/Song 2020, ref 20で使用）を3.0 equivで本条件下に試し収率を報告する。TEMPO（1.0 equiv）を添加した条件と無添加条件を比較してラジカル経路を排除する。
* **注記**: B-10（V1=medium; convergence 1/3）、A-2（V2=high; convergence 1/3）、U-3（self-contradictory absence; severity=medium）。D-4候補5に対応。

---

**CLA-3: γ/δ selectivity kinetic/thermodynamic underdetermination**（A-3）

* **Primary RI**: RI-03 [Unobserved explanatory] — 5員環vs6員環パラダサイクル（intermediate V）の形成が速度論的制御か熱力学的制御かを実験的に識別する観測が存在しない。
* **ER**: 反応時間を変化させたγ/δ生成物比率の時間依存プロファイル、または温度依存性測定によって、速度論的制御（時間不変）か熱力学的制御（時間とともに比率変化）かを判定する必要がある。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: 3aa（γ選択）および類縁δ体を生成するn=2基質について、r.t.と-20 °Cでの反応のγ/δ比率を測定する（温度依存性）。またはr.t.でのγ/δ比率を1, 3, 6, 12, 24 h時点でサンプリングし、比率が時間不変（速度論的制御）か変化（熱力学的制御）かを確認する。
* **注記**: A-3（V2=high; convergence 1/3）。D-4候補6のうちSRG未割当（A-3）部分。B-4（SRG-8）とリンク。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method)**

---

**VQ-1 [Observation]：通る**

生成物（3aa, 3aa-d1, 3aa-d2）はNMRスペクトルとHRMSによる同定がSIで確立されている（RI-02は非致命的残存として解消されている）。VQ-1を通過する根拠：基質・生成物の構造同定は当該化学系で標準的な粒度で実施されており、代替構造を排除できる。Non-fatal残存：触媒中間体（Si-PdII-H, Ar-PdII-I）は同定されていないが、これはVQ-1ではなくVQ-3（RI-03）の要件に属する。

---

**VQ-2 [Method]：通る（non-fatal残存を明記）**

VQ-1継承前提で成立。RI-01とRI-07の状況：
- **RI-01（SRG-5: Table 1訂正）**: Table 1の訂正内容が未開示だが、実験方法の記述（試薬、当量、時間、温度）自体は改訂されていない可能性が高く、VQ-2の**非致命的**残存として扱う。ただし、Entry 12/13が訂正対象だった場合は本判定が変わる（条件付き）。
- **RI-01（CLA-1: 内部標準安定性）**: 内部標準の安定性コントロールが欠如しているが、主実験方法の妥当性を根底から覆すものではない（非致命的）。
- **RI-07（CLA-2: 実用合成主張）**: 「industrial synthesis」という境界主張はNon-fatal——スコープの記述は実験方法の精度に依存しない。

**VQ-2はRI-01（SRG-5、CLA-1）のnon-fatal残存、およびRI-07（CLA-2）のnon-fatal残存を前提として成立している。**

---

**VQ-3 [Mechanism]：未達**

VQ-2継承前提で、RI-03, RI-04, RI-06を確認：
- **RI-03（SRG-2: 副サイクル中間体未観測）—致命的**：論文の機構的新規性の核心である副サイクル（ベンジルPd中間体IX）が直接的観測も速度論的拘束もなく、0.2D(δ)という単一値のみで提案されている。機構主張の成立に原理的に不可欠な中間体証拠が存在しない。
- **RI-04（SRG-3: 重水素実験の精度・H/D交換コントロール欠如）—致命的**：唯一の機構的プローブである重水素標識実験（Figure 3）の信頼性が担保されていない。0.2Dはintegration誤差と同程度の値であり、H/D交換による汚染の可能性も排除されていない。
- **RI-06（SRG-6: dual-cycle model輸入）—非致命的**：先行研究からの概念輸入として構造的に問題があるが、モデルの妥当性が否定されたわけではない。
- **RI-05（SRG-4, SRG-8）—残存**：VQ-3が「限定的（Qualified）」になる要因として残存するが、RI-03/RI-04の致命的未解消のため、まずVQ-3自体が未達。

**未解消RI（致命的）: RI-03（SRG-2, SRG-6, SRG-7, CLA-3）、RI-04（SRG-3）**

---

**VQ-4 [Benchmark]：未達（VQ-3未達のため未到達）**

RI-08（SRG-1, SRG-3, CLA-1）およびRI-09（SRG-4）も未解消。VQ-3の解消なしにVQ-4に到達できない（継承原則）。

---

**層別VQ非対称性：**

- **合成的新規性（層a）単独**では：RI-03/RI-04は機構的主張（層c）に属し合成的スコープの実証とは独立している。RI-09（SRG-4）がVQ-4要件として残存するため、**VQ-3 (qualified: RI-05残存)** が上限。
- **機構的主張（層c）単独**では：RI-03（Fatal）、RI-04（Fatal）が直接的に機構主張に対して致命的であり、**VQ-2止まり**。
- **スコープ新規性（層b）単独**では：層aに依存するが実験的スコープ（Figure 2）は実証されており、RI-07（CLA-2）がNon-fatal残存として**VQ-3 (qualified)** が到達水準。

---

### §4 Era-Norm Annotation

**communication-era tolerated（J. Org. Chem. Note, 2024年）：**

- **B-1, B-2（物質収支不完全）**: 合成Note形式では全副生成物の定量的追跡は省略が許容される慣行であり、2024年J. Org. Chem. Noteの通信形式内で許容される。
- **B-3（replicates欠如）**: 合成NoteおよびLetterでは単一測定値報告が標準的慣行であり、2024年においても繰り返し測定は通常要求されない。
- **B-12（スコープ失敗例未開示）**: スコープ論文での失敗例の非開示はJ. Org. Chem. Note 2024の慣行範囲内。
- **B-14（添加時間の用量反応関係未示）**: 当該情報はSI（p. S7）に委譲されており、通信形式での省略として許容される。
- **A-1〜A-4（機構解明の「ongoing」先送り）**: 速度論データを持たない機構提案は、合成Note形式でのプレリミナリー機構議論として許容されている。

**modern-era deficient（現代の再認定基準で不足）：**

- **B-7（重水素取り込み精度・H/D交換未検証）**: 重水素標識実験の定量値を機構的証拠として主要本文で引用する場合、2H NMRによる定量とH/D交換コントロールは現代の機構化学の標準要件であり、2024年の論文として不足している。
- **B-6（Table 1訂正のchangelog不在）**: 事後訂正のchangelogは現代の再現性・データ完全性基準（FAIR data原則、open science）で要求されるが、2024年ACS Publications訂正慣行では任意のため当時は許容されていた（**両タグ該当**）。
- **U-2（速い添加条件下での重水素実験不在）**: 二重触媒サイクルモデルの中心的予測を検証しない重水素実験は、2024年時点の機構論文の標準として不足している。
- **CLA-1（内部標準安定性コントロール不在）**: Pd/Si-H系での還元的条件で使用する内部標準には安定性確認が現代的分析化学の要件であり、2024年基準では不足。

**両タグ該当（当時許容→現代不足）：**
- **B-6（Table 1訂正changelog）**: ACS Publications 2024の訂正慣行では任意であるため当時は許容されていたが、データ完全性の現代基準では不足。
- **B-3のreplicates欠如**: Note形式では許容されていたが、Entry 12/13という機構的判断の核心データが単一測定値に依拠することは、現代の機構論文標準では不足。

---

### §5 最短補強ルート

**目的関数の設定：**
- 第一目的関数：VQ-3（現在VQ-2）— RI-03（Fatal）, RI-04（Fatal）の解消が必須
- 第二目的関数：VQ-4（VQ-3達成後）— RI-08, RI-09の解消が必須

---

**VQ-3 への最短ルート：**

1. EP-04a [Discrimination / replication pack] — 重水素実験（Figure 3b）を3回独立で2H NMRにより実施し、γ位（目標0.8D）とδ位（目標0.2D）の取り込み値と標準偏差を報告するとともに、反応条件下でのアミドN-DからN-Hへの交換速度をコントロール実験で確認する。RI-04を前進（SRG-3 Fatal解消に直結）。情報利得：RI-04 + RI-08（SRG-3）の同時前進。

2. EP-03a [Direct-observation / state-assignment pack] — 速い添加条件（Entry 12相当）と遅い添加条件（Entry 13）の両方で重水素標識アミド（1a, 0.9D）を用いた平行実験を実施し、δ位D取り込みが速い添加で増加するかを確認する。RI-03を前進（SRG-2 Fatal解消に直結）。U-2の自己矛盾的不在を同時解消。

3. EP-03a [Direct-observation / state-assignment pack] — PMHS量を段階的変化（2.0→3.1→4.1 equiv）させた条件での副生成物（1b, 1c）収率を定量し、dual-cycle modelの予測の成否を確認する。RI-03を前進（SRG-6）、RI-06（Non-fatal）も同時前進。

4. EP-03a [Direct-observation / state-assignment pack] — CsF / CsOAc / TBAF / CsI（各2.0 equiv）比較コントロールにより、CsF役割（fluoride activator vs Brønsted base）を分離する。RI-03を前進（SRG-7）。実験3との並行実施が可能。

**認定ゲート順注記：実験投入順は情報利得順（EP-04a先行、次いでEP-03a ×3）だが、最終認定はVQ-1→VQ-2→VQ-3→VQ-4のゲート順で確定する。VQ-3認定にはRI-03（SRG-2, SRG-6, SRG-7）とRI-04（SRG-3）の全Fatal項目解消が必要（継承原則）。RI-06（Non-fatal残存）がある場合はVQ-3 qualifiedとして記録。**

---

**VQ-4 への最短ルート（第二目的関数、VQ-3達成後）：**

5. EP-08a [Replication / uncertainty pack] — Entry 12とEntry 13のNMR収率測定をn≥3で反復し、標準偏差と完全な物質収支を報告する。内部標準（ジベンジルエーテル）の安定性コントロール（CLA-1）も同バッチで実施する。RI-08を前進（SRG-1, SRG-3, CLA-1の同時前進）。情報利得最大（3つのSRG/CLAを同時に前進）。

6. EP-09a [Internal benchmark pack] — 先行研究（ref 16: Wang/Wu/Loh JACS 2018）と同一基質2〜3例を本条件と先行条件で並行実施し、直接収率比較を報告する。RI-09を前進（SRG-4）。

7. EP-01a [Reporting-coherence pack] — Table 1訂正のchangelogを確認・公開し、Entry 12/13の値が変更対象か否かを特定する。RI-01を前進（SRG-5）。独立した手続き事項であり実験と並行して進められる。

---

### §6 制度設計への寄与

---

**1. RI-03の「model-prediction-untested subtype」の確認**

SRG-2（U-1, U-2）はStage 1でU（Unclassified）として分類されたが、Stage 3の視点ではいずれも「提案されたモデル（双触媒サイクル）が予測する観測量が、論文自身のデータとして存在しない」という構造を持つ。これはRI-03（Unobserved explanatory）の特殊形——「中間体が観測されていない」ではなく「モデルが自分自身の予測を実験的に検証していない」——として記録できる。本ケースはRI-03の**model-prediction-untested subtype**の代表事例として追加記録する価値がある。

---

**2. RI-04 + RI-08 共起パターンの確認**

SRG-3において、RI-04（単一実験の高位解釈：0.2D at δ を副サイクルの識別子として使用）とRI-08（不確かさ記述なし：2H NMR精度・H/D交換未確認）が共起している。この共起では「0.2Dという測定値自体の信頼性（RI-08）が確立されていなければ、その値を識別子として使用すること（RI-04）の解消が意味をなさない」という依存関係が生じる。**RI-04単独の解消（H/D交換コントロール）だけでは不十分であり、RI-08の解消（反復定量）も必要**。このRI-04 + RI-08の依存的共起は「精度不明の単一標識値を機構的分岐比率の定量的証拠として使用するパターン」の典型事例として記録する。

---

**3. PRI-11（Mechanism-kinetics decoupling）の追加確認根拠**

本論文の双触媒サイクルモデルから速度式を代数的に導出する試みはなく、「遅い添加 → Si-PdII-H濃度低下 → 副サイクル抑制 → 収率向上」という定性的論理のみで機構を支持している。これはPRI-11の暫定定義（「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」）に合致する。Breitenfeld 2014、Pengfei 2024に続く追加確認事例として記録する。**PRI-11はこれで独立2報以上の確認を満たしており、正式昇格の判断材料として提出する。**

---

**4. 標識不整合（Labeling mismatch）パターンの記録**

Figure 4の触媒サイクルを説明する本文では「we propose a side cycle where...」という仮説標識が1回用いられているが、直後の叙述では「[REDACTED: verbatim source text; see the source paper via its DOI]」と事実的記述語が連続して使用されている。**仮説標識が単一の導入文に集約され、その後の個別素反応の記述が事実語に移行するパターン**（仮説標識位置：本文先頭1文に集約、以降は事実語）を記録する。このパターンはRI-06（Imported model/サイクルレベル輸入）と連動しており、副サイクルの先行研究からの構造輸入が仮説として名指されながら、素反応記述が既知事実として叙述されている。

---

**5. Full Paper遷移の自動解消パターン（bundle auto-resolution）の予測**

B-1, B-2（物質収支）、B-3（replicates）、B-12（スコープ失敗例）、B-14（添加時間用量反応）はすべてNote形式の紙幅制約に由来するRI-01/RI-08項目であり、Full Paper展開で自動解消される候補。A-1〜A-4（「ongoing」機構研究）がFull Paperとして発表された場合、これら4つのデファーラルも同時に解消される可能性があり、この**束型自動解消（bundle auto-resolution）**パターンを記録する。本稿執筆時点（2026年4月）でShirai et al.からのFull Paper続報は認識されていない。

---

**6. VQ-3における層別非対称性の制度的含意**

§3で検出された層別VQ非対称性——合成的新規性（層a）はVQ-3 qualifiedに達しているが、機構的主張（層c）はVQ-2止まり——は「合成Noteとして機構的提案を同時に行う場合に生じるVQ水準の体系的分裂」として記録する。合成的主張を単独で認定するとVQ-3に到達するが、機構的主張を同一論文に含めることでVQ-3判定全体が「機構層の未達」に引きずられる。これは合成Note形式における機構提案の追加が**VQ判定全体を引き下げるコスト**を持つことを示しており、UQSのVQ判定において通信形式の機構提案を分離評価する「層別VQ判定」が有効な分析ツールであることの証左となる。

inference_time_sec: not available — inject externally
```
