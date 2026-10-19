```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

C23 trigger 評価：本論文はJACS Communication形式（BIB-7: communication）であり、EP-01a（RI-01起因）に対してC23（Letter→Full Paper auto-resolution）が発火する。Kumadaグループは1976年にBull. Chem. Soc. Jpn.に包括的Full Paperを発表している（auto_resolution_status: occurred）。

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a, EP-07a

— EP-03a (Direct-observation / state-assignment pack): NiCl₂(dpe)系での化学量論的素反応・中間体の低温分光観測は、遷移金属有機化学の独立研究主題として1970年代後半に展開し、Kochiグループ（酸化的付加機構）・Yamamoto A.グループ（ジオルガノニッケル錯体合成）の独立論文として文献追跡が可能；RI-03は独立論文化されやすいRI-type。

— EP-06a (Analogy-validation pack): dipy-Ni系からdpe-Ni系へのサイクル輸入の同型性実証（個別素反応の化学量論的検証）は、Ni(0)/Ni(II)サイクルの酸化的付加・還元的脱離それぞれについて独立論文が存在し、特にKochiグループがその実験的骨格を提供している；RI-06は独立研究として発展しやすい。

— EP-07a (Boundary-test pack): sp²ハライドとsp³ハライドの反応性対比は、Kumadaカップリングのスコープ研究として1972年以降の複数グループ（Kumadaグループ自身・Corriuグループ）がFull Paper形式で実施しており、スコープ限界の文書化として文献追跡が可能；RI-07は境界条件の実験的確認として独立論文化されやすい。

**第二群（間接的に追跡可能）：** EP-01a, EP-02a, EP-04a, EP-05a, EP-09a

— EP-01a (Reporting-coherence pack): RI-01起因。C23適用 — auto_resolution_type: "Letter→Full Paper"; expected_resolution_window: "1-3 yr"（実際は約4年後の1976年); auto_resolution_status: occurred。Kumadaグループのの包括的Full Paper（Bull. Chem. Soc. Jpn. 1976）がglpc条件・反応時間・収率基準の統一報告を自動解消しているが、独立論文の「主題」ではなく付随的解消であるため第二群。

— EP-02a (Identity/purity substantiation pack, 補助EP): RI-02起因。Full Paper展開（C23）で個別GC-MS・NMRデータが提供されたと推定されるが、"and/or"構文問題の完全解消の追跡は限定的；独立論文の主題とはならない性質。

— EP-04a (Discrimination / replication pack): cis/trans比の速度論/熱力学制御を区別する時間・温度系列実験は、Kumadaカップリングの立体化学研究として間接的に充填されたと推定されるが、cis/trans-DCE + PhMgBrという特定の基質系への焦点を当てた独立論文は限定的で、立体化学研究の一部として組み込まれる形。

— EP-05a (Quantitative-ranking substantiation pack): RI-05起因。反応混合物の質量収支（クロスカップリング vs. ホモカップリング）の定量は、Full Paper展開で部分的に充填されたと推定されるが、ホモカップリング生成物を主目的として定量した独立論文は存在しにくい；収率データは通常クロスカップリング生成物のみで報告される慣行。

— EP-09a (Internal benchmark pack): RI-09起因。NiCl₂(dpe) vs. Ni(acac)₂の直接比較は競合グループ（Kumada系 vs. Corriu系）の並行展開によって間接的に比較データが蓄積したが、同一基質・同一条件下での体系的比較を主題とした独立論文は存在しにくく、レビュー・総説に含まれる形での充填。

**第三群（充填が見つからない可能性あり）：** EP-08a

— EP-08a (Replication / uncertainty pack): RI-08起因。合成化学の収率データに対する独立反復測定・統計的信頼区間の報告は、インセンティブ構造的未充填に該当 — 新規性要求の出版慣行下では独立論文化されない。Kumadaカップリングの場合は他グループによる応用実施が「実質的な再現確認」として機能したが、元のTable I収率の統計的信頼区間を主題とした論文は存在しない。

---

### §B 各EPの充填論文候補

**注記（Bibliographic verification 適用）:** 本論文は以下の複合トリガーに該当するため、全候補に [必須] を付与する: (a) 1980年以前の論文が大半、(b) Kumadaグループから10報以上の関連論文群が存在、(c) 「Kumada coupling」として著者名由来の命名規則をもつ反応、(d) Medium-Low confidence候補が複数含まれる。全候補に "Bibliographic verification status: pending" を付与する。

---

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — Kumadaグループによる包括的Full Paper（11エントリを超える拡張基質表・統一glpc条件・各エントリの反応時間・収率基準の統一報告）
* **充填確立点**: 同上
* **充填の性質**: Complete（glpc条件・反応時間・収率基準の統一化について実質的に完全に解消；ただし紙幅の制約から一部エントリでは省略あり）
* **Bibliographic confidence**: Medium（著者名・年・雑誌は高信頼、巻号49・ページ1958–1976は推定を含む）
* **Filling adequacy confidence**: High（Full PaperがCommunicationのRI-01不足を解消するパターンは当該報告形式の典型的自動解消）
* **Verification recommendation**: [必須]（条件a/b/c複合）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr; 実際は約4年 = 許容範囲の境界)

```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```

* **注記**: Stage 3 §5の「EP-01a → format-driven auto-resolved」注記と整合。Kumada, M.; Sumitani, K. Org. Synth. 1978, 58, 127–133 も標準化手順として副次的な充填候補（Bibliographic confidence: High; Filling adequacy: Partial — 手順の再現性を提供するが、glpc定量条件の完全開示は限定的）。同Org. Synth.論文はBibliographic verification status: pending。

---

**EP-02a [Identity/purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Reporting integrity: product identity verification]
* **充填開始点**: Tamao, K. et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — Full Paper展開で個別化合物の物性データ（bp, n²⁰D等）と分光データが拡充報告
* **充填確立点**: 同上
* **充填の性質**: Partial（主要生成物の¹H NMR・MS データが記載されるが、"and/or"構文が完全に解消されるかは確認要）
* **Bibliographic confidence**: Medium（EP-01aと同文献、同信頼度）
* **Filling adequacy confidence**: Medium（Full Paperが個別characterizationを改善したことは推定できるが、全エントリへの適用程度が不明）
* **Verification recommendation**: [必須]（EP-01aと同条件）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (同上)
* **注記**: EP-01aとバンドル充填（同一論文が両EPを充填）。補助EPであり独立選定不要。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点（部分的）**: Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979, 101, 6319–6332 — Ni(0)ホスフィン錯体のアリールハライドへの酸化的付加の速度論・機構研究（触媒サイクルeq (2)の対象系への実験的対応；[NiCl₂(dpe)]ではなくNi(0)ジホスフィン系での酸化的付加を実証）
* **充填確立点（間接・部分的）**: 未同定（NiCl₂(dpe)系での中間体1の直接31P NMR観測を主題とした論文は個別同定困難）
* **充填の性質**: Partial（酸化的付加ステップへの間接充填；ジオルガノニッケル中間体1の直接観測・独立合成には到達せず）
* **Bibliographic confidence**: High（Tsou/Kochi JACS 1979は広く引用された機構研究として高信頼）
* **Filling adequacy confidence**: Medium（酸化的付加ステップの対応はあるが、EP-03aが要求する低温31P NMR観測・[Ni(n-Bu)₂(dpe)]の独立合成への対応は間接的）
* **Verification recommendation**: [必須]（条件a/b）
* **DOI / URL**: 10.1021/ja00517a061（推定、verification要）
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (7 yr; 1972→1979)
* **注記**: EP-03a要件の全体（eq 2・eq 3・eq 4の各ステップの化学量論的実証、中間体の低温NMR）に対応するバンドル充填論文は存在しない可能性が高い。ジオルガノニッケル錯体の独立合成については、Yamamoto, A. グループの系統研究（Bull. Chem. Soc. Jpn. 1970年代後半）が間接的に関連するが、NiCl₂(dpe)特有の中間体への適用は確認困難 — 未同定として処理。EP-06aとのバンドル充填がKochi 1979にとって最も効率的な利用。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点（部分的）**: Tamao, K. et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — Full Paper中の立体化学データ（vinyl halideとの反応のcis/trans比の複数基質・複数条件での報告）
* **充填確立点**: 未同定（cis/trans-dichloroethylene + PhMgBrという特定の基質系についての速度論/熱力学的制御の区別実験を主題とした独立論文は確認困難）
* **充填の性質**: Partial（Full Paperが複数基質のcis/trans比データを提供するが、速度論/熱力学的制御の明示的区別実験および定量GLC反復測定はEP-04a要件の完全充填に至らない可能性）
* **Bibliographic confidence**: Medium（充填開始点としての Bull. Chem. Soc. Jpn. 1976 は EP-01aと同信頼度）
* **Filling adequacy confidence**: Low（EP-04aが要求する時間・温度系列実験による速度論/熱力学的区別が、Full Paperの立体化学データに含まれるかは不明）
* **Verification recommendation**: [必須]（条件a/b/c）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（Full Paper展開での立体化学データ拡充）/ incentive-aligned（速度論/熱力学区別の独立研究は実施された場合）
* **注記**: Kumadaカップリングの立体化学研究は1977–1982年にかけて展開したが（Hayashi, T.; Kumada, M.らによる不斉版の立体化学分析）、「cis/trans-1,2-DCE + PhMgBr特定系の速度論/熱力学的制御」という問いに正面から答えた論文は存在しない可能性がある。SRG-6の「成功による問いの抹消」に近い構造（ビニルグリニャール試薬の立体保持カップリングが優先研究として展開し、特定の基質系の動力学的解析需要が後退した可能性）。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点（部分的）**: Tamao, K. et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — Full Paper中の拡張基質スコープ・収率データ（クロスカップリング選択性の定性的改善として機能）
* **充填確立点**: 未同定（反応混合物の完全質量収支 — クロスカップリング生成物 + R–R + β-脱離生成物の定量 — を主題とした独立論文は確認困難）
* **充填の性質**: Partial（Full Paperが収率データを改善するが、eq (3)が予測するR–Rの定量報告はFull Paperにも存在しない可能性；SRG-2の根本問題が持続）
* **Bibliographic confidence**: Medium（Full Paper候補はEP-01aと同）
* **Filling adequacy confidence**: Low（R–Rホモカップリング生成物を定量した記述がFull Paperに含まれるかは不明）
* **Verification recommendation**: [必須]（条件a/b/c）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（部分充填）/ non-applicable（完全充填は存在しない可能性）
* **注記**: SRG-2の中核問題（「selective」という主張のホモカップリング定量的根拠の不在）は、Kumada反応が実用的成功を収めた結果として検証需要が低下し、長期的に部分充填状態にとどまっている可能性が高い（成功による問いの抹消パターンに近い）。eq (3)のR–R生成の系統的定量は1990年代以降の精密機構研究（NMRスペクトルのモニタリング）で間接的に触れられるが、独立充填論文としては未同定。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]
* **充填開始点**: Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979, 101, 6319–6332 — Ni(0)ジホスフィン錯体のアリールおよびベンジルハライドへの酸化的付加の速度論・立体化学研究（dipy-Ni系からdpe-Ni系へのサイクル輸入のうち、酸化的付加ステップの対象系での実証として機能）
* **充填確立点**: 同上（酸化的付加ステップについて）
* **充填の性質**: Partial（酸化的付加ステップの実証はあるが、EP-06aが要求するeq 2・eq 3・eq 4全ステップの個別化学量論的実証への完全対応は単一論文では達成されていない）
* **Bibliographic confidence**: High（Tsou/Kochi 1979はNi(0)機構研究の代表的論文として高信頼）
* **Filling adequacy confidence**: High（EP-06a case-specific実装の酸化的付加部分に直接対応）
* **Verification recommendation**: [必須]（条件a/b）
* **DOI / URL**: 10.1021/ja00517a061（推定、verification要）
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (7 yr; 1972→1979)
* **注記**: EP-03aとバンドル充填（Kochi 1979が両方の部分充填候補）。トランスメタル化（eq 2）と還元的脱離（eq 4）については、Yamamoto A.グループの関連研究（Bull. Chem. Soc. Jpn. 1970年代後半–1980年代）が間接充填候補となるが書誌信頼度はLow。RI-06完全解消には触媒サイクル全ステップの独立実証が必要であり、複数論文の組み合わせでのみ近似充填が可能。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Tamao, K. et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — 拡張スコープ研究でsp³ハライドの反応性の欠如および塩化物・臭化物・ヨウ化物の相対反応性を記録
* **充填確立点（sp³/sp² boundary）**: Negishi, E.; King, A.O.; Okukado, N. J. Org. Chem. 1977, 42, 1821–1823 — Pd触媒が必要とされる基質範囲の確立（Ni触媒ではsp³ハライドが不活性であることの対照として機能）
* **充填の性質**: Partial（Full Paper展開でsp²制限が実験的に文書化されるが、ep-07aが要求する「sp³ハライドを試みた失敗例の条件変化による体系的確認」および「PhCl/PhBr/PhIの定量的初期速度比較」への完全対応は限定的）
* **Bibliographic confidence**: High（Tamao et al. BCSJ 1976はMedium; Negishi 1977はHigh — J. Org. Chem. 1977の対応論文は広く引用されている）
* **Filling adequacy confidence**: Medium（境界の実験的文書化はあるが、EP-07aの要求する系統的失敗例記録と反応速度定量への対応は間接的）
* **Verification recommendation**: [必須]（条件a/b/c）
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (5 yr for Negishi 1977: 1972→1977; format-driven for BCSJ 1976)
* **注記**: sp³ハライドの失敗例は、合成化学では「負の結果」として独立論文化されにくいため、スコープ制限はFull Paperの付随記述として充填される。Negishi 1977はsp³ハライドでの反応性確立論文として、Ni触媒の限界と対照的にPd触媒の優位性を示す。塩化物/臭化物/ヨウ化物の比較については、Kumada Full Paper（1976）に関連データが含まれる可能性が高い。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填論文候補**: 未同定
* **充填の性質**: non-applicable（インセンティブ構造的未充填）
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: [省略可]（第三群のため）
* **Filling timescale category**: non-applicable
* **注記**: 合成有機化学における収率データの統計的信頼区間報告は、出版慣行として独立論文化されない — インセンティブ構造的未充填。Kumadaカップリングの場合、多数のグループによる独立応用が「実質的な再現確認」として機能したが、Table I各エントリの標準偏差を報告した論文は構造的に存在しない。§EおよびVQ逆転パターンの分析対象。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点（間接的）**: Corriu, R.J.P.; Masse, J.P. J. Chem. Soc. Chem. Commun. 1972, 144 — 同時独立報告として Ni(acac)₂での類似選択的クロスカップリングを記録（比較の出発点となる）
* **充填確立点**: 未同定（NiCl₂(dpe) vs. Ni(acac)₂の同一基質・同一条件下での体系的比較を主題とした独立論文は確認困難）
* **充填の性質**: Indirect（Kumada系 vs. Corriu系の競合展開によって比較データが蓄積したが、単一論文での直接比較は存在しにくい）
* **Bibliographic confidence**: High（Corriu/Masse 1972はS0-7で既出・BIB-8に言及あり）
* **Filling adequacy confidence**: Low（Corriu/Masse 1972はEP-09aの「充填開始点」としても機能しないほど比較データが欠落 — Stage 1 C-3で指摘済み）
* **Verification recommendation**: [必須]（条件a/b）
* **Bibliographic verification status**: pending
* **Filling timescale category**: non-applicable（直接比較論文が構造的に存在しにくいため）
* **注記**: Kumadaグループのbidentate diphosphineとCorriuグループのNi(acac)₂は競合触媒として並行展開したが、両者の同一基質での直接比較を主目的とした独立研究は確認困難。レビュー（例：Cross-Coupling Reactions, Topics in Current Chemistry等）が比較の場となったが、レビューはEP充填としてカウントしない。後年の合成化学者がcases-by-case basis で条件選択をした「暗黙の比較」が唯一の間接充填として存在する。

---

**§B 末尾チェック：Bibliographic verification**

全候補が以下のトリガー条件に複合該当するため、全エントリに [必須] を付与済み:
- (a) 1980年以前の論文が大半（Tsou/Kochi 1979, Tamao et al. 1976, Hayashi et al. 1976）
- (b) Kumadaグループ関連論文が10報以上存在する密な著者ネットワーク
- (c) 「Kumada coupling」として著者名由来の命名規則が確立（Wittig/Diels–Alder等と同格）

**書誌検証推奨リスト:**
1. Tamao et al. Bull. Chem. Soc. Jpn. 1976 — Crossref検索推奨（著者名・年・雑誌・巻号49・ページ1958–1976の確認）
2. Tsou, Kochi J. Am. Chem. Soc. 1979, 101 — DOI: 10.1021/ja00517a061（推定）の検証
3. Hayashi, Tajika, Tamao, Kumada J. Am. Chem. Soc. 1976, 98 — DOI検索推奨（3718–3725ページの確認）
4. Negishi, King, Okukado J. Org. Chem. 1977, 42 — DOI検索推奨（1821–1823ページの確認）
5. Kumada M. Pure Appl. Chem. 1980, 52 — 書誌検索推奨（retrospective lecture実在確認）

**既知のハルシネーションリスク:** Kumadaグループは多数の著者を有する複数論文シリーズを発表しており、著者の組み合わせと巻号/ページ番号の不一致（著者組み合わせ捏造・書誌内容誤記）のリスクがある。Tamao et al. BCSJ 1976の著者リスト（8–9名）と巻号/ページは特に要確認。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 | EP-01a, EP-02a, EP-05a（部分）, EP-07a（部分）, EP-04a（部分） | VQ-2（主）| 1976 | Medium | High（EP-01a）/ Medium（EP-04a, EP-05a） | [必須] ⚠️ pending |
| 2 | Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979, 101, 6319–6332 | EP-06a, EP-03a（部分） | VQ-3（部分） | 1979 | High | High（EP-06a）/ Medium（EP-03a） | [必須] ⚠️ pending |
| 3 | Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. J. Am. Chem. Soc. 1976, 98, 3718–3725 | EP-01a（部分・スコープ拡張）, EP-07a（部分）| VQ-2 | 1976 | High | Medium | [必須] ⚠️ pending |
| 4 | Negishi, E.; King, A.O.; Okukado, N. J. Org. Chem. 1977, 42, 1821–1823 | EP-07a（sp²/sp³ boundary確立） | VQ-2 | 1977 | High | Medium（Ni系限界への間接的対照） | [必須] ⚠️ pending |
| 5 | Kumada, M. Pure Appl. Chem. 1980, 52, 669–679 | EP-09a（間接・著者回顧視点）, レトロスペクティブ分析用 | VQ-2/3（著者観点） | 1980 | Medium | Low（研究論文ではなく回顧） | [必須] ⚠️ pending |

選定理由: 順位1（Tamao et al. BCSJ 1976）は単一論文でVQ-2要件の最大カバレッジを達成し、EP-01a/EP-02a/EP-05a/EP-07aの複数充填を担う最重要候補として選定した。順位2（Tsou/Kochi 1979）はVQ-3要件（EP-06a）の実験的骨格を提供する唯一の高信頼候補であり、機構検証の起点として不可欠。順位3（Hayashi et al. JACS 1976）は順位1と年代が同じ1976年だが、独立グループ（順位3は同一グループだが別論文）として別資料が存在することを示す点で選定した。順位4（Negishi 1977）はPd触媒との対照によるNi触媒のsp²制限の間接的確立として、EP-07aの「境界確立」側を補完する。順位5（Kumada 1980回顧）はEP-09a（Ni(acac)₂との比較）の唯一の間接的候補として、また著者回顧との照合（§D step 4）のために選定した。

バンドル充填: Tamao et al. BCSJ 1976 が EP-01a, EP-02a, EP-05a（部分）, EP-07a（部分）, EP-04a（部分）を一括充填する最高効率の単一文献。Tsou/Kochi 1979 が EP-06a + EP-03a（部分）を兼ねる。

全エントリが [必須] verification 待機中。Bibliographic verification 完了後に最終選定リストへ正式昇格。EP-09aの充填確立点が未同定のため、表からは除外（§Eで記録）。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

```
1972年: 原論文発表（Kumada Communication、JACS）
  → VQ判定: VQ-1通過 / VQ-2以上未達

1976年: Tamao et al. Bull. Chem. Soc. Jpn. 1976 [推定]
  → VQ-2要件: EP-01a（完全）, EP-07a（部分）, EP-05a（部分）, EP-04a（部分）
  → 充填パターン: 自己充填（原著者グループによる後続Full Paper）

1976年（並行）: Hayashi, Tajika, Tamao, Kumada JACS 1976
  → VQ-2要件: EP-01a（部分・スコープ拡張）
  → 充填パターン: 自己充填（同一グループ、別論文軸）

1977年: Negishi, King, Okukado J. Org. Chem. 1977
  → VQ-2要件: EP-07a（sp³境界の間接的確立）
  → 充填パターン: 分野横断充填（Pd触媒の展開という形での反証的確立）

1979年: Tsou, Kochi JACS 1979
  → VQ-3要件: EP-06a（部分）, EP-03a（部分）
  → 充填パターン: 技術駆動充填（機構研究の方法論的精緻化）/ 分野横断充填（Kochiグループという異なる研究グループ）

1980年（推定）: Kumada Pure Appl. Chem. 1980
  → レトロスペクティブ（EP充填としては機能しないが著者視点の記録として有価値）
  → 充填パターン: 著者回顧との照合資料

EP-08a（未充填）: 1972→現在まで
  → 充填パターン: 未充填（インセンティブ構造的未充填）

EP-09a（未充填・充填確立点なし）: 1972→現在まで
  → 充填パターン: 実質的未充填（Corriu系とKumada系の競合展開が代替したが直接比較は欠落）
```

**階層-時間対応の評価:**

階層-時間仮説は本ケースで**部分的に支持される**。VQ-2要件（EP-01a, EP-07a）は1976–1977年に充填されたのに対し、VQ-3要件（EP-06a）は1979年まで待たなければならなかった（7年）。ただし、VQ-2内部での充填は原著者グループによる「自己充填」として実現しており（形式的には自発的補完）、独立した科学コミュニティの応答としての充填とは性格が異なる。また、EP-03a（VQ-3要件の中核）は2026年現在も完全充填に至らず、VQ-3への最終到達が50年以上にわたって未達であることは、機構的理解の難易度構造と整合している。

**特筆すべきパターン:**

1. **自己充填（Self-filling）と分割提示充填の組み合わせ**: Kumadaグループは1976年のFull Paper発表という形で、VQ-2要件のほぼ全体を自ら充填した。これは「Paper I（Communication）→ Paper II（Full Paper）」という分割提示充填パターンの典型例であり、Stage 3 §5が指摘した「format-driven auto-resolved」と完全に整合する。

2. **VQ逆転なし（正常な充填順序）**: 本ケースでは、低VQ要件（RI-01, RI-07/VQ-2）が先に充填され、高VQ要件（RI-03, RI-06/VQ-3）の充填が後になっている。これは理想的な科学的論理に沿った充填順序であり、インセンティブ構造との対立が最小のケース。

3. **EP-05a（R–R定量）の長期的部分充填**: SRG-2の中核問題（「selective」の定量的根拠）は、成功による問いの抹消パターンに近い形で長期的に部分充填状態にとどまっている。Kumada反応の実用的成功が「R–Rは確かに生成しない（または無視できる）」という暗黙知として定着し、eq (3)が予測するR–R生成の明示的否定実験需要が消滅した。

4. **著者回顧との照合（§D step 4）**: Kumadaグループの回顧（Kumada, M. Pure Appl. Chem. 1980 推定）は、「選択的クロスカップリング法の確立」「塩化物の高反応性」「bidentate diphosphineの重要性」を研究の成果として提示したと推定される。UQSが抽出した最重要問い（D4-1: selectivity定量的根拠の不在、D4-2: 触媒サイクルの実験的根拠の不在）は、回顧において認識・言及されなかった可能性が高い。これは「分野の内部者には不可視の構造的不在」の証拠として記録できる：回顧がhighlight する「成果」（収率・スコープ・有用性）と、UQSが「語られていない問い」として抽出した「機構的根拠の欠落・ホモカップリング定量の欠落」の間に明確な非対称性がある。

5. **Negishi 1977の間接的先行充填**: Negishi cross-coupling（Pd触媒、sp³ハライドに有効）の登場は、Ni触媒のsp²/sp³境界（EP-07a）を間接的に確立した。これは「競合技術の成功によるEP充填」という分野横断充填の一形態であり、先行充填ではなく「確立充填」として機能した。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

**EP-05a [Quantitative-ranking substantiation pack]（部分充填・完全充填未達）:**
* **未充填の理由**: 成功による問いの抹消（Success-driven question erasure）— Kumada反応の実用的成功と広範な応用により、eq (3)が予測するR–Rホモカップリング生成物の系統的定量需要が社会的に消滅した。技術的には可能（GC-MSで検出・定量可能）だが、「この反応は選択的だ」という経験則が50年以上にわたって追試なしに受容された。Full Paper（1976）が部分的な改善を提供したにとどまり、eq (3)の機構的予測と実験的不在の矛盾（U-1）は完全には解消されていない。
* **発見的意義**: あり — 「化学反応の選択性主張において、提案機構自身がその逆の産物を予測している場合（U-1型自己矛盾的不在）、実用的成功が検証需要を50年以上にわたって隠蔽するという構造」の代表事例として記録できる。UQSが抽出したSRG-2（B-1, U-1, C-1）は、科学コミュニティが長期間にわたって体系的に回避してきた問いの典型を示す。
* **将来の充填可能性**: 高 — 現代のin situ NMRモニタリング（低温31P/1H NMR）またはGC-MS反応追跡実験で技術的に実施可能。ただし、充填を動機づけるインセンティブが現在のところ存在しない。

**EP-08a [Replication / uncertainty pack]（完全未充填）:**
* **未充填の理由**: インセンティブ構造的未充填 — 合成化学における収率データの統計的信頼性評価（反復測定・標準偏差報告）は、新規性を要求する出版慣行のもとでは独立論文化されない。Kumadaカップリングの場合、多数グループによる成功的応用が統計的信頼性の代替シグナルとして機能したが、Table I収率（76–98%）の統計的信頼区間は50年以上にわたって未報告のまま。
* **発見的意義**: あり — ただし発見的意義は限定的。統計的信頼性評価の不在はKumada 1972特有の問題ではなく1970年代合成化学の分野慣行に起因し、UQS固有の発見というよりは分野全体のRI-08充填パターンの一事例として位置づけられる。
* **将来の充填可能性**: 低 — 統計的信頼区間を目的として元のTable I収率を反復測定する実験を独立論文として発表するインセンティブが現在も存在しない。現代の自動化高スループット合成プラットフォームを使えば技術的には可能だが、知的貢献の観点から独立論文化されない。

**EP-09a [Internal benchmark pack]（充填確立点なし）:**
* **未充填の理由**: インセンティブ構造の不整合 + 分野の競合展開による迂回充填 — NiCl₂(dpe) vs. Ni(acac)₂の直接比較は、Kumadaグループ（chelating diphosphine推進）とCorriuグループ（Ni(acac)₂継続使用）の研究戦略上の利害が一致せず、中立的な第三者による直接比較実験を独立論文として発表するインセンティブが不在だった。両系の比較はレビュー論文・教科書・総説の場でのみ実現し、研究論文レベルの充填は未達。
* **発見的意義**: あり — 「同時独立発見（Corriu/Masse 1972, Note Added in Proof）が存在しながら、50年以上にわたって同一基質での直接比較実験が独立論文として発表されなかった」という構造はUQS発見として記録価値がある。Stage 1 C-3（Dropped Quantitative Benchmark: Ni(acac)₂との比較不在）が提起した問いが、科学コミュニティレベルで50年以上にわたって正面から検証されなかったことは、競合グループ間での問いの棚上げ（問い自体の存在は認識されながら解決されない）パターンとして記録できる。
* **将来の充填可能性**: 中 — 技術的には容易（両触媒を同一基質・条件で比較する実験）。Kumada coupling methodologyへの現代的関心（不斉版・Pd遊離version等）に付随して実施される可能性はあるが、NiCl₂(dpe)とNi(acac)₂の比較そのものを主目的とした論文の動機付けは限定的。

**VQ階層逆転の診断:**

本ケースではVQ階層逆転（低VQ要件が未充填のまま高VQ要件が先に充填される）は**観察されない**。EP-01a（低VQ = VQ-2要件）が1976年に充填され、EP-06a（高VQ = VQ-3要件）が1979年に部分充填されるという正常な充填順序が確認された。ただし、EP-08a（RI-08 = VQ-4要件の一部）とEP-09a（RI-09 = VQ-4要件の一部）が永続的に未充填であることは、VQ-4への最終到達を妨げる構造的欠落として記録される。VQ-4要件が低VQ要件（RI-01/VQ-2）の完全解消なしに超えられる事例（VQ逆転）ではなく、むしろ「高VQ要件は中程度に前進したが最も低VQ要件の一部（RI-08/RI-09起因）が永続的に未充填」という非対称充填パターンとして観察される。
```
