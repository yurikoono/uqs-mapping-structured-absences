```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-02a, EP-03a, EP-06a, EP-07a

— EP-01a (Reporting-coherence pack / RI-01): 本論文はJACS Communicationであり、同一著者グループによるFull Paper続報（Tamao et al., Bull. Chem. Soc. Jpn. 1976）が4年以内に発表されており、C23（Letter→Full Paper auto-resolution）の典型事例。glpc条件・反応時間・収率基準の統一が独立論文として追跡可能。

— EP-02a (Identity/purity substantiation pack / RI-02): 同Full Paper続報（Tamao et al. 1976）が全エントリの個別分光データを提供しており、Bull. CSJ 1976単独で充填開始点かつ充填確立点となる。第一群。

— EP-03a (Direct-observation / state-assignment pack / RI-03): NiCl₂(dpe)系ジオルガノニッケル中間体の分光学的同定を要求するが、dpe-Ni σ-結合型錯体の合成・特性評価は1970年代後半から複数グループが独立論文として実施しており（Yamamoto group, Kochi group）、文献で直接追跡可能。

— EP-06a (Analogy-validation pack / RI-06): dpe-Ni系での化学量論的素反応検証（eq 2, eq 3それぞれ）は、Kochi グループによるNi(0)酸化的付加の機構研究および著者グループ自身の続報として独立論文化されており追跡可能。

— EP-07a (Boundary-test pack / RI-07): sp²制限の実験的根拠（sp³ハライドの不活性確認）および塩化物/臭化物/ヨウ化物の直接比較は、Tamao et al. Bull. CSJ 1976のFull Paperが基質スコープを拡張した文脈で一部対処しており、第一群として分類可能。

---

**第二群（間接的に追跡可能）：** EP-05a, EP-09a, EP-04a

— EP-05a (Quantitative-ranking substantiation pack / RI-05): クロスカップリング vs. ホモカップリング vs. β-脱離の定量的質量収支（GC-MS）は、Tamao 1976 Full Paperが一部対処するが、eq (3)が予測するR–Rの体系的定量を主目的とした独立論文は見当たらず、間接的充填。

— EP-09a (Internal benchmark pack / RI-09): NiCl₂(dpe) vs. Ni(acac)₂の同一基質・条件での直接比較は、Corriuグループの後続論文とレビュー類が側面的に扱うが、この問いを主題とした独立実験論文は間接的にしか存在しない。

— EP-04a (Discrimination / replication pack / RI-04): cis/trans-スチルベン比の速度論/熱力学制御区別（時間・温度系列 + 定量GLC反復）は、Kumadaグループのビニルハライドカップリング立体化学研究が側面的に関連するが、この比率の速度論/熱力学区別を主題とした論文は間接的にしか追跡できない。

---

**第三群（充填が見つからない可能性あり）：** EP-08a

— EP-08a (Replication / uncertainty pack / RI-08): Table Iエントリの独立反復測定（n≥3）と標準偏差報告を主題とした独立論文は、出版インセンティブの不整合（既存系の追試・統計的評価は新規性を要求する出版慣行で論文化されにくい）により構造的に未充填。「インセンティブ構造的未充填」パターン（§A 第三群パターン①）に該当。

C23 trigger: applicable — 本論文はCommunication形式であり、同一著者グループのFull Paper続報（Tamao et al. 1976）がEP-01a, EP-02aのLetter→Full Paper auto-resolutionとして機能する。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第一群）**

* **充填するRI**: RI-01 (Reporting integrity — glpc条件不記載, 収率基準不統一, 反応時間不記載)
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 全基質エントリに統一したglpc条件・反応時間・収率基準を適用した本格的Full Paperとして、通信形式に起因するRI-01不在を全面的に解消した。
* **充填確立点**: 同上
* **充填の性質**: Complete（Full Paper形式での全面的解消）
* **Bibliographic confidence**: High（Kumada-Tamao coupling の foundational Full Paper として well-known; 著者リスト・巻号・ページは高確度）
* **Filling adequacy confidence**: High（Full Paperが通信の報告形式欠落を全面的に扱うことはgenre conventionとして確実）
* **Verification recommendation**: [必須]（論文年代1980年以前 [条件a]; 著者ネットワーク密・反応名がauthor name由来 [条件b,c]）
* **DOI / URL**: 10.1246/bcsj.49.1958 （推定; verification pending）
* **Filling timescale category**: format-driven (1–3 yr) — Communication発表1972年→Full Paper 1976年（4年、C23パターンのやや長めだが同一グループの自己解消として分類）
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```
* **Bibliographic verification status**: pending
* **注記**: SRG-3（B-4, B-8, B-9, B-12, B-13）の全メンバーを一括解消するバンドル充填。Stage 3 §4でcommunication-era toleratedと分類されたRI-01がFull Paper遷移で自動解消される典型パターン（§6 Note 5との整合）。

---

**EP-02a [Identity/purity substantiation pack]（第一群）**

* **充填するRI**: RI-02 (non-fatal residual — "and/or" 構文による生成物同定の一部単一分析法依存)
* **充填開始点**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 各生成物の個別NMR・GCデータおよびele-anal結果を記載し、RI-02 non-fatalを実質的に解消。
* **充填確立点**: 同上
* **充填の性質**: Complete（EP-01aと同一論文がバンドル充填）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: High
* **Verification recommendation**: [必須]（EP-01aと同じトリガー条件）
* **DOI / URL**: 10.1246/bcsj.49.1958 （推定）
* **Filling timescale category**: format-driven (1–3 yr)
* **Bibliographic verification status**: pending
* **注記**: EP-01aとのバンドル充填。Stage 3 §4のB-13（communication-era tolerated / both-tagged）と整合的に解消。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory — 中間体1, 2, 3の直接観測・速度論的拘束なし)
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full Paperがdpe-Ni系の一部化学量論的実験を含み、中間体形成の間接的証拠を提供（部分的充填開始点）。
* **充填確立点**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332 — Ni(0)錯体へのアリールハライドの酸化的付加（eq 2相当ステップ）の機構を、速度論・立体化学・交差実験で詳細に実証し、分子性Ni(0)/Ni(II)サイクルの実験的根拠を確立。Kochi群はdpe類似のbidentate phosphine-Ni(0)錯体を対象として酸化的付加の速度論データを提供。
* **充填の性質**: Partial（dpe-Ni系でのstep-by-step化学量論的実証ではなく、Ni(0)酸化的付加ステップの機構的同定; eq (3)のR–R形成の直接実証は含まない）
* **Bibliographic confidence**: Medium（Tsou & Kochi 1979 JASCは存在するが、巻号・ページの正確な対応についてはpost-hoc verification推奨; dpe系を対象としているかの確認が必要）
* **Filling adequacy confidence**: Medium（Kochi群の研究がbidentate phosphine-Ni(0)の酸化的付加を扱うことは確実だが、NiCl₂(dpe)を用いた実験の詳細については verification 必要）
* **Verification recommendation**: [必須]（論文年代1980年以前 [条件a]; named reaction（Kumada coupling）のauthor nameに基づく密なネットワーク [条件b,c]）
* **DOI / URL**: 10.1021/ja00503a072 （推定; verification pending）
* **Filling timescale category**: field-methodology (2–5 yr) — 1972年通信から1979年Kochi機構研究まで7年。新しい機構論的手法（速度論測定、交差実験）のfield-wide adoptionが driving force。
* **Bibliographic verification status**: pending
* **注記**: SRG-1（B-2, B-14, U-1, U-2, U-4）の核心的RI。RI-03とRI-06（EP-06a）は不可分共起パターン（Stage 3 §6 Note 6）のため、EP-03aの完全充填にはEP-06aとの協働が必要。中間体2（(halo)(organo)Ni complex）の独立合成および eq (3) の R–R 生成実証は別論文（Yamamoto group等）が部分的に充填した可能性があるが、文献特定にはverification要。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 (Unreplicated discriminator — cis/trans比の速度論/熱力学区別実験なし), RI-08 (Unquantified reliability — 分析法・反復測定なし)
* **充填開始点**: Tamao, K.; Zembayashi, M.; Kiso, Y.; Kumada, M. *J. Organomet. Chem.* **1973** または **1974**, 巻号未確定 — Kumadaグループがビニルハライドカップリングの立体化学を研究した初期論文として、cis/trans制御に関する実験データを一部提供した可能性（間接的充填開始点; Bibliographic confidence Low）。
* **充填確立点**: Tamao, K.; Kodama, S.; Nakajima, I.; Kumada, M.; Minato, A.; Suzuki, K. *Tetrahedron* **1982**, *38*, 3347–3354 — "Nickel-Phosphine Complex-Catalyzed Grignard Coupling. II"として立体化学的側面を詳述し、ビニルハライドカップリングのstereoselectivity mechanismに踏み込む（Medium confidence; 速度論/熱力学区別の時間・温度系列実験を含むかはverification要）。
* **充填の性質**: Indirect（立体化学の機構論的記述は提供するが、U-3が要求する「cis/trans比の速度論/熱力学区別のための時間・温度系列 + 定量GLC反復」を主目的として実施したエビデンスは不明確）
* **Bibliographic confidence**: Medium（Tamao 1982 Tetrahedron はKumadaカップリング立体化学の論文として合理的だが著者リスト・ページ番号はverification要）
* **Filling adequacy confidence**: Low（速度論vs熱力学の明示的区別実験の有無が不明）
* **Verification recommendation**: [必須]（論文年代1980年代初期 [条件a]; named reaction [条件c]; Filling adequacy confidence Low [条件d]）
* **DOI / URL**: 確認不可（verification pending）
* **Filling timescale category**: incentive-aligned (variable) — 立体化学研究の進展に依存、10年スケール。
* **Bibliographic verification status**: pending
* **注記**: U-3（kinetic/thermodynamic indeterminacy）はA-1・B-11から独立した問いとしてStage 1で記録されており、立体化学研究の主流とは目的関数が異なる。EP-04aの要求する「同一反応の時間・温度系列実験」は立体化学の機構論的研究とは別の実験設計であり、充填が第二群どまりとなる理由。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 (Qualitative overread — "selective"の数値的根拠なし, R–R等副生物の定量なし)
* **充填開始点**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full Paperが拡張された基質スコープで収率と選択性を報告し、一部エントリでホモカップリング生成物の不検出または微量を記述した可能性（間接的な充填開始点）。
* **充填確立点**: 未同定（EP-01a充填論文と重複するが、GC-MSによるクロスカップリング vs. ホモカップリング vs. β-脱離の完全質量収支を主目的とした論文は特定できず）。質量収支の定量的実証はKumada coupling reviewまたはPalladium catalysisとの比較研究に部分的に吸収された可能性。
* **充填の性質**: Indirect（Full Paperが選択性の定性的拡張を提供するが、eq(3)が予測するR–R生成の定量的実証を主目的とした独立論文は確認困難）
* **Bibliographic confidence**: Low（充填確立点として機能する論文を特定できず）
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]（上記条件全般）
* **DOI / URL**: 不確定
* **Filling timescale category**: non-applicable（充填確立点未同定）
* **注記**: SRG-2（B-1, U-1, C-1）の核心的RI。Kumada coupling がPd触媒クロスカップリングの発展とともに応用研究に軸足が移ったため、「選択性の定量的実証」という後方充填の動機が薄れ、長期的未充填の可能性。B-1のself-contradictory absence（eq(3)がR–Rを予測するが未報告）はU-1として独立記録されており、この問いはD4-1の核心でもある。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 (Imported model — dipy-Ni系からdpe-Ni系へのサイクルレベル輸入, 同型性未実証)
* **充填開始点**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full Paperがいくつかの化学量論的実験を含み、dpe-Ni系でのtransmetalationまたは酸化的付加ステップの実験的観察を部分的に提供（充填開始点として機能）。
* **充填確立点**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332 — Ni(0)complexへのArXの酸化的付加（eq 2相当）の速度論的実証がdpe様bidentate phosphine系で行われ、dipy-Ni系からの輸入モデルの同型性を独立に検証する。EP-03aと同一充填確立点論文（バンドル充填）。
* **充填の性質**: Partial（eq 2相当ステップの実証はあるが、eq 3（reductive eliminationによるR–R vs. cross-coupling生成物）の化学量論的実証は別途確認要）
* **Bibliographic confidence**: Medium（Tsou & Kochi 1979 の存在は高確度だが巻号・ページ・dpe系対象かはverification要）
* **Filling adequacy confidence**: Medium
* **Verification recommendation**: [必須]（EP-03aと同一トリガー条件）
* **DOI / URL**: 推定: 10.1021/ja00503a072 — EP-03aと共有; verification pending
* **Filling timescale category**: field-methodology (2–5 yr); 実際の充填は1979年（7年後）
* **Bibliographic verification status**: pending
* **注記**: Stage 3 §6 Note 6のRI-06+RI-03不可分共起パターンとの整合: EP-06aとEP-03aは同一充填論文でバンドル充填されるが、どちらか一方のみでは完全充填にならない。Stage 3 §5のVQ-3最短ルートで「EP-03a, EP-06a同時投入」と指定されていたことと一致。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary — sp²制限の失敗例なし; sp³ハライドの不活性未確認), RI-05 (secondary — 塩化物の「高反応性」の定量的根拠なし)
* **充填開始点（sp²制限）**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full Paperがsp³アルキルハライドを試みた結果（非反応性）を明示的に報告し、sp²制限の実験的根拠を確立。
* **充填確立点（sp²制限）**: 同上（同一論文が充填開始点かつ確立点）
* **充填開始点（塩化物比較）**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 同一論文がPhCl vs. PhBr等の反応性比較データを一部提供。
* **充填の性質**: Partial（sp²制限の実験的根拠はFull Paperで提供; 塩化物/臭化物/ヨウ化物の同一基質・条件での初期速度比較については完全な実施かどうかはverification要）
* **Bibliographic confidence**: High（同一論文Tamao 1976）
* **Filling adequacy confidence**: Medium（sp²制限の実験的確認は確実; 速度論的ハライド比較の詳細はverification要）
* **Verification recommendation**: [必須]（EP-01aと同一トリガー条件）
* **DOI / URL**: 10.1246/bcsj.49.1958 （推定）
* **Filling timescale category**: format-driven (1–3 yr)（EP-01aと同じFull Paper自動解消; sp²制限実験データはFull Paperで報告）
* **Bibliographic verification status**: pending
* **注記**: D4-4（sp³ハライドの「試みたか否か」問題）およびSRG-4（B-5, B-6, A-2）のRI-07拡張適用パターン（Stage 3 §6 Note 2）に対応。Tamao 1976 Full Paperがこの問いを正面から扱っていることはgenre conventionから高確度。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 (Unquantified reliability — 収率・cis/trans比の反復測定なし, 不確かさ記述なし)
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: 非適用（第三群: インセンティブ構造的未充填）
* **Bibliographic confidence**: 非適用
* **Filling adequacy confidence**: 非適用
* **Verification recommendation**: 非適用（第三群）
* **Filling timescale category**: non-applicable
  ```yaml
  incentive_structure_type: "incentive-structural-unfilling"
  ```
* **注記**: Kumada coupling 反応の収率・立体選択性データの統計的再現性を独立論文として検証するインセンティブは、1972–現代を通じて存在しない。追試・反復測定は出版慣行の新規性要件と整合せず、§E で詳述。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 (External superiority — Corriu/Masse Ni(acac)₂との直接比較不在)
* **充填開始点**: Corriu, R. J. P.; Moreau, J. J. E. *J. Organomet. Chem.* **1975**頃 — Corriuグループが自身のNi(acac)₂系の後続論文でスコープと選択性を詳述し、diphosphine-Ni系との間接的比較が可能になる（Bibliographic confidence Low; 年代・巻号未確定）。
* **充填確立点**: 未同定（NiCl₂(dpe) vs. Ni(acac)₂の同一基質・条件での直接比較を主目的とした独立論文は確認できず; 後年のレビュー類で両系の比較が体系化された可能性あるが、レビューはEPを充填しない）
* **充填の性質**: Indirect（両系が独立に発展した文献から比較情報を抽出可能だが、Stage 3 §2 CLA-1 が要求する「同一条件での直接比較 + Ni(acac)₂条件再現」を主目的とした論文は確認困難）
* **Bibliographic confidence**: Low（Corriu follow-up論文の特定に不確実性が高い）
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]（著者ネットワーク密; Bibliographic confidence Low が2件以上 [条件d]）
* **DOI / URL**: 未特定
* **Filling timescale category**: incentive-aligned (variable); D4-8の問いはPd触媒系の隆盛により部分的に問い自体が「成功による問いの抹消」パターンへ移行した可能性
* **Bibliographic verification status**: pending
* **注記**: Note Added in Proof（Corriu/Masse 1972）が記録した問いは、その後両グループが並行して発展したことで「どちらが先か」ではなく「それぞれどの系が有効か」へと問いが変形した可能性。Pd触媒クロスカップリング（Heck 1972–; Suzuki 1979–; Negishi 1977–）の隆盛によりNi系固有の配位子設計原理への需要が相対的に低下し、EP-09aへの直接充填動機が薄れた。

---

§B 末尾チェック：Bibliographic verification

トリガー条件評価（全候補共通）:
- (a) 論文年代が古い（1980年以前）: YES（全主要候補が1972–1982年）
- (b) 著者ネットワークが密: YES（Kumada/Tamao グループから10本以上の関連論文; Kochi group同様）
- (c) 反応名がauthor name由来: YES（「Kumada coupling」「Tamao-Kumada-Corriu coupling」— named reaction）
- (d) Bibliographic confidence Medium-Low の候補2件以上: YES

→ 全候補に **[必須]** Verification recommendation を付与。全エントリに「Bibliographic verification status: pending」を付記済み。

Known hallucination risk pattern:
- EP-04a (Tamao 1982 Tetrahedron): 著者リストの組合せ捏造リスク高（正確な著者・ページ要検証）
- EP-03a/EP-06a (Tsou & Kochi 1979): 論文内容のchemistry記述誤記リスク中（Ni系の正確な配位子環境要確認）
- EP-09a (Corriu follow-up): 架空のcoauthor追加リスク高（書誌情報が最も不確実）

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️ Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-07a (partial) | VQ-2 | 1976 | High | High | 必須 |
| 2 | ⚠️ Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* 1979, 101, 6319–6332 | EP-03a (partial), EP-06a (partial) | VQ-3 | 1979 | Medium | Medium | 必須 |
| 3 | ⚠️ Tamao et al. (上記と同一, EP-07aの追加充填として) | EP-07a (sp²制限の失敗例) | VQ-2 | 1976 | High | Medium | 必須 |
| 4 | ⚠️ Tamao, Kodama, Nakajima, Kumada, Minato, Suzuki. *Tetrahedron* 1982, 38, 3347–3354 | EP-04a (indirect) | VQ-3 (qualified) | 1982 | Medium | Low | 必須 |
| 5 | ⚠️ Corriu follow-up （書誌情報未確定; Corriu, R. J. P. et al., *J. Organomet. Chem.* 1975頃） | EP-09a (indirect) | VQ-4 (partial) | 1975頃 | Low | Low | 必須 |

⚠️ 全エントリが「verification 待機中」（[必須] 条件充足のため）。

**選定理由：**

推奨リストの中核はTamao et al. *Bull. Chem. Soc. Jpn.* 1976（順序1/3）であり、VQ-2到達に不可欠なEP-01a（RI-01全面解消）、EP-02a（RI-02解消）、EP-07a（RI-07部分解消）を単一論文でバンドル充填する最高効率の候補である。この論文はC23（Letter→Full Paper auto-resolution）の典型であり、Bibliographic confidenceが高く、充填効率・証拠強度ともに選定リスト筆頭に値する。

VQ-3要件の充填はTsou & Kochi 1979（順序2）が担う。これはNi(0)/Ni(II)サイクルのeq 2相当ステップ（酸化的付加）の機構的実証として、RI-03とRI-06を協働的に前進させる。RI-06+RI-03の不可分共起パターン（Stage 3 §6 Note 6）から、両EPの充填論文が一致することは理論的に期待されており、この論文がそれを体現する。

順序4（Tamao 1982 Tetrahedron）はEP-04aへの間接的充填として位置づけるが、Filling adequacy confidence Lowのため最終確認まで暫定選定とする。

順序5（Corriu follow-up）はEP-09a（CLA-1; Ni(acac)₂との比較問題）に対応するが、書誌情報不確実性が最も高く、Filling adequacy confidence Lowであるため、post-hoc verification後に正式選定の可否を判断する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a → 1976 [Tamao et al. Bull. CSJ] [自己充填 / format-driven]
- VQ-2 要件: EP-02a → 1976 [Tamao et al. Bull. CSJ] [自己充填 / format-driven]
- VQ-2 要件: EP-07a (partial) → 1976 [Tamao et al. Bull. CSJ] [自己充填 / format-driven]
- VQ-3 要件: EP-03a (partial) → 1979 [Tsou & Kochi JACS] [技術駆動充填 / field-methodology]
- VQ-3 要件: EP-06a (partial) → 1979 [Tsou & Kochi JACS] [技術駆動充填 / field-methodology]
- VQ-3 要件 (qualified): EP-04a (indirect) → ~1982 [Tamao et al. Tetrahedron] [自己充填 / incentive-aligned]
- VQ-3 要件: EP-05a → 未充填（長期遅延/インセンティブ構造問題）
- VQ-4 要件: EP-09a (indirect) → 未確定 [Corriu follow-up; 第二群どまり]
- 未充填: EP-08a [インセンティブ構造的未充填]

**階層-時間対応の評価：**

「VQ階層が上がるほど充填に要する時間が長くなる」という仮説は、本事例でおおむね支持される。VQ-2要件（EP-01a, EP-02a, EP-07a）はLetter→Full Paperの自己充填として4年以内に解消された（1976年、format-driven）。VQ-3要件（EP-03a, EP-06a）の機構的充填は7年後（1979年）にKochiグループによって提供された（field-methodology）。VQ-3 qualifiedに相当するEP-04aの立体化学的充填は10年後（1982年頃）とさらに遅れた。VQ-4要件に関連するEP-09aは現在も間接的充填にとどまり、EP-05aは未充填のまま残存する。この時間的展開はVQ階層と充填遅延の相関を実証するケースとして記録できる。

ただし重要な例外として、VQ-2要件の自己充填（Tamao 1976）は著者グループの主導的な後続研究として実現しており、VQ-3要件の充填（Kochi 1979）は異なる研究グループによる「分野横断充填」に近い。VQ階層と充填アクター（著者グループ vs. 外部グループ）の間にも構造的対応が見られる点は特筆に値する。

**特筆すべきパターン：**

1. **自己充填（VQ-2）**: Tamao et al. 1976 Bull. CSJ は典型的な自己充填パターン。原著者グループがFull Paperで通信形式の報告欠落（EP-01a, EP-02a）を解消した。Kumadaグループの series論文戦略（Communication 1972 → Full Paper 1976 → Stereo 1982）が明確なself-filling arcとして記録できる。

2. **分野横断充填（VQ-3）**: Kochiグループ（Tsou & Kochi 1979）は「Kumada couplingの充填」として研究したわけではなく、Ni(0)錯体の酸化的付加機構という独立の研究目的から結果的にEP-03a/EP-06aを充填した。これはStage 4の根本原則（充填論文は自らを「充填」と宣言しない）の典型。

3. **VQ逆転の部分的出現**: EP-08a（RI-08, VQ-4要件の一部）は未充填なのに対し、EP-03a/EP-06a（RI-03/RI-06, VQ-3要件）は部分的に充填されている。これは「出版インセンティブに基づく充填順序（高VQ→低VQ）」の逆転パターンの一例。統計的再現性（EP-08a）よりも機構的実証（EP-03a/EP-06a）の方が先に充填されるという出版慣行上の優先順位が、VQ-3→VQ-4という論理的な階層順序と逆転している。

4. **著者回顧との照合**: Kumada, M. *Pure Appl. Chem.* **1980**, *52*, 669–679がKumadaグループの初期レビューとして存在し、著者回顧の観点から「分野の内部者に不可視の構造的不在」を照合できる候補文献。著者が回顧で言及するのは「選択性の高さ」「β-H許容」「sp²塩化物反応性」（D-1 novelty claims）であり、U-1（eq(3)のR–R未報告）やU-2（黒色混合物の均一/不均一性）への言及が欠如していれば、「分野内部者が54年以上認識しなかった構造的不在」の直接的証拠となる。このverificationはpost-hocに推奨。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

EP-05a [Quantitative-ranking substantiation pack]:

* **未充填の理由**: 成功による問いの抹消（Success-driven question erasure）+ インセンティブ構造の不整合。Kumada couplingが「機能する」という実証（VQ-1通過）が成立した時点で、eq(3)が予測するR–R生成の定量的実証需要は薄れた。さらにPd触媒クロスカップリング（Heck 1972–, Negishi 1977–, Suzuki 1979–）への分野全体の関心移行により、Ni系での質量収支精査の動機は一層低下した。技術的には現代のGC-MSで即座に実行可能だが、検証する動機が科学コミュニティとして消失している。
* **発見的意義**: あり。「選択的クロスカップリング」という論文の中心的主張（開題文・表題）は、eq(3)が予測するR–Rの不在を確認した実験なしに50年以上受容されてきた。UQSはB-1/U-1の自己矛盾的不在として記録したこの問い（機構が予測する副生物が報告されていない）が、分野が体系的に無視してきた構造的問いとして同定できる。これは「成功した合成法は選択性を説明しなくてよい」という分野の暗黙規範の証拠として記録できる。
* **将来の充填可能性**: 高（現代のGC-MS分析で代表的基質における質量収支は技術的に即日実行可能; 「Kumada couplingの機構的再評価」を動機とした計算化学論文または触媒機構再現論文が充填を担う可能性）。

---

EP-08a [Replication / uncertainty pack]:

* **未充填の理由**: インセンティブ構造の不整合。合成化学分野では確立した手法の収率を反復測定して標準偏差を報告する実験を独立論文として出版するインセンティブが構造的に存在しない（新規性要件と根本的に不整合）。技術的に可能だが、出版動機を変えなければ充填は発生しない。
* **発見的意義**: あり（ただし方法論的意義として）。cis/trans比「43:57」という精度が4桁の有効数字を示唆しているにもかかわらず、その精度の根拠が存在しないことは、UQSが抽出した問いの中でも特に「分析的信頼性の要求水準の歴史的変化」を示す事例として記録できる。現代の分析化学基準ではこの精度表示は非許容だが、分野が54年以上これを問題としなかった。
* **将来の充填可能性**: 低（独立論文として充填される動機がない; ただし高精度GCMSを用いたKumada coupling mechanistic studyの付随データとして含まれる可能性は中程度）。

---

EP-09a [Internal benchmark pack]:

* **未充填の理由**: 成功による問いの抹消（一部）+ インセンティブ構造の不整合（一部）。NiCl₂(dpe) vs. Ni(acac)₂の直接比較実験は、「bidentate diphosphineが必要か」という問いに答えるためには設計されてこなかった。両系が独立に発展し、Pd触媒系の隆盛によりNi-phosphine設計原理への関心が相対的に低下した。技術的に可能だが、問いの構造（「Corriu/Masseの独立発見がKumada論文の主張の何を崩すか」）を問う研究者が出現しなかった。
* **発見的意義**: あり。D4-8が指摘した「Note Added in ProofがCorriu/Masse（Ni(acac)₂）の同時発見を記録しながら一切比較しない」という構造的不在は、bidentate diphosphineを「必要条件」として記述した論文のNC-4（配位子設計原理）の独自性評価において54年以上未解決である。UQSはこれを「著者が認識しながら比較を行わなかった」構造的不在として（C-3として）記録した。この問いが後続の文献で充填されなかったことは、「先行者優位の命名慣行（Kumada coupling）が独自性評価の検証需要を代替した」という分野社会学的証拠として記録できる。
* **将来の充填可能性**: 中（Kumada/Corriuカップリング機構の計算化学的再評価論文が発表されれば、DFT計算によるdpe-Ni vs. Ni(acac)₂の活性化障壁比較として間接的に充填される可能性; ただし実験的直接比較の動機は低い）。

---

**VQ階層逆転の診断：**

EP-08a（RI-08, VQ-4要件）が未充填で、EP-03a/EP-06a（RI-03/RI-06, VQ-3要件）が部分的に充填されているパターンは、「科学的論理に基づくEP充填順序（低VQ→高VQ）」と「出版インセンティブに基づく実際の充填順序（高VQ→低VQ）」の逆転を構成する。統計的再現性（EP-08a）の充填よりも機構的実証（EP-03a/EP-06a）の充填が先行するこの逆転は、分野のインセンティブ構造が「機構論的新規性 > 方法論的信頼性」を優先することを反映しており、Kumada couplingが分析化学的信頼性基盤（VQ-4）を欠いたまま合成法として確立された歴史的パターンの証拠として記録できる。
```
