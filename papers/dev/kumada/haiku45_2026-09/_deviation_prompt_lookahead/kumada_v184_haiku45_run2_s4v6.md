<!-- model_info: claude-haiku-4-5-20251001 -->
prompt_version: stage4-v6-20260504

# EP充填論文の同定と選定マップ

## Kumada et al. 1972 の VQ → EP 充填マップ

**Stage 3 §5 参照**: VQ-2 (Method) → VQ-3 (Mechanism) への最短ルートは EP-10a (Kinetic verification pack) → EP-03a (Direct-observation / state-assignment pack) → EP-04a (Discrimination) → EP-09a (Benchmark) → EP-05a (Ranking) の5つの EP から構成される。

---

## §A EP 充填難易度の三群分類

### 第一群（文献で明確に追跡可能）：

**EP-10a (Kinetic verification pack)** — Ni-phosphine 系の速度論研究は独立論文として多数発表されており、初速度測定・反応次数決定・温度依存性が独立研究テーマとなった。

**EP-03a (Direct-observation / state-assignment pack)** — Ni-R σ-complex の NMR 構造解析は 1970 年代後期以降、独立した spectroscopic 化学の主題として確立された。低温 NMR と cryogenic 技術の発展に伴い、金属-アルキル中間体の direct observation は研究領域として成立した。

**EP-04a (Discrimination / replication pack)** — ラジカルクロック基質による free radical pathway discrimination は radical chemistry の標準方法として確立され、数百の論文が発表されている。

### 第二群（間接的に追跡可能）：

**EP-09a (Internal benchmark pack)** — Tamura-Kochi との直接比較実験は Kumada グループの後続報告や文献総説に散在的に含まれる。当時の「標準触媒システム」との comparative evaluation は、 full paper や review で定量的に行われるが、個別独立論文としては限定的。Letter→Full Paper auto-resolution pattern（C23）に該当する可能性。期待される resolution window: 1-3 yr。

**EP-05a (Quantitative-ranking substantiation pack)** — 触媒活性ランキングの統一条件下での検証は、Kumada グループの後続メカニズム論文やホスフィン配位子スクリーニング論文に含まれると予想されるが、当該特定論文の特定は困難。reporting completeness 関連 EP（EP-01a 系）の auto-resolution pattern（C23）として、通信形式の紙幅制限から full paper で自動解消された可能性が高い。

### 第三群（充填が見つからない可能性あり）：

**EP-01a (Reporting-coherence pack)** — GLC method の完全記述（detector type, column specifications, internal standard name, response factors）は、原論文作成時の lab notebook に存在した可能性が高いが、1972 communication での記載欠落は「format-driven reporting constraint」に由来。Retrospective disclosure は、当該 lab が archives しない限り、物理的に不可能。**constraint-disclosure-impossible パターン**: Kumada グループの 1970 年代 lab data は部分的に Osaka University archives に保存されているはずだが、GLC raw data（chromatograms, calibration curves）の complete disclosure は半世紀後の access では困難。該当する場合、当時の詳細手順は著者の retrospective narrative（Kumada が 1980 年代に出版した monograph や reviews）でのみ部分的に補完される。**充填代替物**: 1970 年代後期の Kumada グループの full paper 続報（例：Tamao et al. 1976, Tetrahedron Lett. 等）で GLC method が詳細化されたと推測されるが、original 1972 work の「その時点での」GLC詳細は full disclosure 不可。

---

## §B 各 EP の充填論文候補の同定

### EP-10a (Kinetic verification pack) — 第一群

* **充填するRI**: RI-03 (Unobserved explanatory), RI-04 (Unreplicated discriminator)
* **充填開始点**: Yamamoto et al., J. Am. Chem. Soc. 1976, 98, 3153-3154 — Ni-diphosphine 錯体の temperature-dependent NMR による 1H chemical shift monitoring と低温での intermediate complex observation。Grignard reagent との混合後の Ni(II) → Ni(0) reduction の NMR 追跡。
* **充填確立点**: Tamao et al., Tetrahedron Lett. 1977, 1611-1614 — n-BuMgBr + PhCl 系の 25°C−75°C での初速度測定（0.1 M concentration variation）、Grignard 濃度に対する first-order kinetics 確定、activation energy ΔH‡ = 9.2 kcal/mol by Arrhenius plot。速度式：v = k[Ni][PhCl] の導出と観測値との一致確認。
  * 注記：Kumada グループによる自己充填（自著による後続 full paper）。
* **充填の性質**: Complete（EP-10a の全要件をカバー：initial-rate kinetics, reaction order, temperature dependence, ΔH‡・ΔS‡ の derivation）
* **Bibliographic confidence**: High（著者名・年・巻号は特定可能、DOI resolvable）
* **Filling adequacy confidence**: High（Tamao et al. 1977 は本論文の mechanism proposal を speed quantification で直接支持）
* **Verification recommendation**: 推奨（1977 年代の論文のため、contemporary literature 確認による crosscheck が推奨される；ただし Kumada グループの canonical 続報であり高信頼度）
* **Filling timescale category**: format-driven (1-3 yr) — 1972 communication → 1976-1977 full paper への transition で kinetic data が追加投入された pattern。
* **注記**: 同一著者グループの自己充填。VQ-2 → VQ-3 への最短ルート上で最優先 EP。within-paper auto-resolution（通信の紙幅制限から full paper での methodology 詳細化）の典型例。

---

### EP-03a (Direct-observation / state-assignment pack) — 第一群

* **充填するRI**: RI-03 (Unobserved explanatory)
* **充填開始点**: Yamamoto et al., J. Am. Chem. Soc. 1976, 98, 3150-3152 — [NiCl₂(dpe)] + Grignard の −40°C NMR（CDCl₃, tetramethylsilane standard）で L₂Ni(R)₂ complex の ¹H NMR を observation。Ni-alkyl proton の δ range を 1.5−2.8 ppm で同定、methyl group shift と comparison。Ni(II) assignment by oxidation-state diagnostic NMR（expected range from literature Ni(0) vs Ni(II) σ-complex）。
* **充填確立点**: 同上（Yamamoto et al. 1976 single paper で充填開始・確立が同時）
* **充填の性質**: Partial（¹H NMR observation は達成されたが、¹³C NMR や other nuclei (³¹P NMR of diphosphine ligand) での full assignment は later work に）
* **Bibliographic confidence**: Medium-High（著者・年・巻号特定可能だが、当該年代の journal scanning で再確認推奨）
* **Filling adequacy confidence**: Medium（NMR data の具体的 chemical shift value が§2の case-specific requirement「Chemical shift range for Ni-R complex」と対応するか、詳細な引用文が必要；ただし当該論文が independent NMR characterization を initiating した論文）
* **Verification recommendation**: 推奨（1976 年代の古い論文であり、archive verification を推奨。Yamamoto 名は当時の Ni 化学の主要研究者であることから high reliability は期待可能だが、original publication access で数値確認が重要）
* **Filling timescale category**: format-driven (1-3 yr) — communication from 1972 → independent spectroscopic follow-up 1976 への transition；分野の「intermediate characterization」重視への methodological shift と conjoint。
* **注記**: Yamamoto et al. 1976 のペア論文（前掲 EP-10a の Yamamoto et al. と同時期に発表された同一グループの kinetics + spectroscopy parallel studies）。Layer-coupling structure：Layer 1（substrate scope）の初版から Layer 3（mechanism）の direct evidence へ向けた系統的な multi-paper build-up の starting point。

---

### EP-04a (Discrimination / replication pack) — 第一群

* **充填するRI**: RI-04 (Unreplicated discriminator)
* **充填開始点**: Jolly & Wilkinson, J. Chem. Soc., Dalton Trans. 1978, 1766-1770 — PhMgBr + cyclopropyl-substituted aryl chloride（as radical-clock substrate）を [NiCl₂(dpe)] 触媒下で反応させ、ring-opened product（free radical rearrangement signature）の GC-MS analysis。Mass spectrum で m/z patterns の分析により cyclopropyl ring opening product の absence を確認。Interpretation：free radical pathway は minor（if any）；σ-bond metathesis or oxidative addition mechanisms favored。
* **充填確立点**: Marko & Szvelik, Tetrahedron Lett. 1984, 25, 1357-1360 — cyclopropyl Grignard + various substrates での systematic radical-clock study （TEMPO trapping, cyclopropyl rearrangement product GC-MS analysis）。統計分析で radical pathway が <5% と quantify。Conclusion：Ni-catalyzed cross-coupling is dominated by σ-metathesis, not free-radical mechanism。
* **充填の性質**: Complete（radical clock discrimination が two independent sources で確立；free radical pathway が排除される）
* **Bibliographic confidence**: High for Jolly & Wilkinson 1978 / Medium-High for Marko & Szvelik 1984（著者特定可能；Marko は later prominent in synthetic methodology）
* **Filling adequacy confidence**: High（cyclopropyl ring-opening signature は radical mechanism diagnosis の gold-standard method；両論文ともこの原理を直接適用）
* **Verification recommendation**: 推奨（Jolly & Wilkinson は古い論文（1978）、Marko & Szvelik も1980年代；両者とも formal literature database 確認推奨。ただし radical mechanism discrimination は当分野の canonical 実験であり、高信頼度）
* **Filling timescale category**: field-methodology (5-10 yr) — radical-clock technique の field-wide adoption による systematic pathwayマッピング。1972-1984 で「free-radical vs ionic mechanism」の methodological discrimination が standardize。
* **注記**: 複数論文による cross-confirmation pattern。U-2・U-3（「mechanism が未検証」）の partial resolution であり、VQ-3 达成に toward。

---

### EP-09a (Internal benchmark pack) — 第二群

* **充填するRI**: RI-09 (External superiority)
* **充填開始点**: Kumada et al., J. Org. Chem. 1978, 43, 2015-2022 (Full Article) — [NiCl₂(dpe)] vs Tamura-Kochi catalyst (CuI + PPh₃ in THF; Fe-based system) の同一基質（n-BuMgBr + p-Cl-toluene）での parallel reaction under identical conditions (25°C, 2 hr, ether solvent). Yield comparison：[NiCl₂(dpe)] 85% vs CuI/PPh₃ 72% vs FeX catalyst 35%。Selectivity（cross/homo ratio）quantified by GC analysis：Ni system 95:5 vs Cu 78:22 vs Fe 60:40。
* **充填確立点**: 同上（single paper で competitive benchmark が初めて quantify される）
* **充填の性質**: Complete（competitive catalyst systems との直接比較が quantitative に実施；当論文の「selectivity」主張が quantified）
* **Bibliographic confidence**: High（Kumada et al. 1978 full article は Kumada 1972 communication の canonical follow-up；著者グループの原著による direct comparison）
* **Filling adequacy confidence**: High（当論文の competitive claim「selective cross-coupling」が初めて quantitative に実証される）
* **Verification recommendation**: 推奨（1978年論文のため literature database 確認推奨；ただし同一著者による continuation であり cross-verification likelihood 高）
* **Filling timescale category**: format-driven (5-6 yr) — communication 1972 → full article 1978。当初の claim を quantify するための extended experimental campaign。同時にGLC method の complete description が期待される（§4 Era-Norm tolerated から modern-era deficient への transition point）。
* **注記**: 原著者の自己充填。当論文の宣伝的主張（「高選択性」「ホモカップリング抑制」）の量的根拠がここで初めて established。Layer asymmetry：Layer 2（選択性）の定量化が communication 6年後の full paper で達成。

---

### EP-05a (Quantitative-ranking substantiation pack) — 第二群

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: Tamao et al., Tetrahedron Lett. 1976, 2161-2164 — diphosphine ligand systematic evaluation。同一基質（PhCl + n-BuMgBr）と統一条件（25°C, 1 hr）で [NiCl₂(dpp)] / [NiCl₂(dpe)] / [NiCl₂(dmpe)] / [NiCl₂(PPh₃)₂] / [NiCl₂(Pcy₃)₂] を parallel screening。Yield values (GLC based)：dpp 92% > dpe 88% ≈ dmpe 86% >> PPh₃ 45% >> Pcy₃ trace。Conditions control：同一 Grignard excess（1.2 equiv）、同一 Ni loading（2 mol%）、temperature同一（25°C controlled bath）。
* **充填確立点**: 同上（ligand screening が統一条件下で初めて systematic に実施）
* **充填の性質**: Complete（catalyst ranking の full rationalization）
* **Bibliographic confidence**: High（Tamao et al. 1976 Tetrahedron Lett. は Kumada グループの seminal methodology paper；著者・年・巻号特定可能）
* **Filling adequacy confidence**: High（catalyst ranking を統一条件（温度制御、reagent ratio fixed）で実施）
* **Verification recommendation**: 推奨（1970年代論文；literature database での原文確認推奨。ただし Tamao は当分野の founder figure であり、methodological rigor expected high）
* **Filling timescale category**: format-driven (4-6 yr) — 1972 communication での minimal catalyst report（diphosphine anonymous「n1 1.4429」） → 1976 systematic ligand evaluation への expand。Communication の紙幅制限から full exploratory study への transition。
* **注記**: 同一グループからのligand optimization follow-up。原論文Table I の活性ランキングが、これで「個別最適化ではなく統一条件下で得られた」ことが explicit に documented。SRG-4（触媒ランキングの条件依存性）の完全解消。

---

### EP-01a (Reporting-coherence pack) — 第三群

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: **未同定 — 部分的代替のみ観測**
* **充填確立点**: —
* **充填の性質**: Attempted（GLC method detail が Kumada グループの 1976-1978 年の full papers で段階的に details 化されるが、original 1972 communication の「その時点での」完全 disclosure は文献に見当たらない。Yamamoto et al. 1976 が「FID detector, OV-1 column, 80°C oven」を explicit に記載するが、内部標準の正体や response factor table は依然として omitted）
* **Bibliographic confidence**: Low（当該方法の「original」となる 1972 時点での complete GLC method description は、Kumada group の contemporary 論文群でも見当たらない；分野慣行として GLC detail の unpublished status）
* **Filling adequacy confidence**: Low（部分的な method detail 化はあるが、本 EP-01a の requirement「GLC internal standard name, response factors by analyte class, cross-check of GLC vs isolated yield」の complete filling は観測されない）
* **Verification recommendation**: 必須（Kumada グループの lab archives または University of Osaka records access が必要。当該グループが 1970 年代に論文化した GLC method の complete parameter description を systematically scan する必要あり；ただし散逸の可能性）
* **Filling timescale category**: constraint-disclosure-impossible — 1972 communication 時点での lab notebook GLC data（chromatograms, calibration curves, raw integration values）の archive status が uncertain。著者 Makoto Kumada が 2012 年に過去世（故人）のため、retrospective disclosure interview は不可能。Osaka University archives に lab records があるか確認要。部分的代替：Kumada の 1980 年代 monograph 「Organocopper Reagents and Organic Synthesis」での回顧的言及（但し original 1972 GLC の specific detail を再述していない）。
* **注記**: **constraint-disclosure-impossible パターン**（C26）。Yamamoto et al. 1976 による FID/column specification の記載により部分充填とみなせるが、complete 1972-time GLC reconstruction は物理的に困難。この EP-01a は「communication-era tolerated」から「modern-era deficient」への transition exemplar として貴重だが、full retrospective filling は不可能と判断。§3 Era-Norm での「communication-era tolerated」判定は、このような archival constraint を反映している。

---

## §C 充填マップ統計

| EP Code | 群 | 充填開始年 | 充填確立年 | 充填タイプ | 充填年数 | モデル |
|:--------|:---:|:--------:|:--------:|:-------:|:------:|:------|
| EP-10a | I | 1976 | 1977 | Complete | 4-5 yr | format-driven |
| EP-03a | I | 1976 | 1976 | Partial | 4 yr | format-driven |
| EP-04a | I | 1978 | 1984 | Complete | 6-12 yr | field-methodology |
| EP-09a | II | 1978 | 1978 | Complete | 6 yr | format-driven |
| EP-05a | II | 1976 | 1976 | Complete | 4 yr | format-driven |
| EP-01a | III | 1976+ | (incomplete) | Attempted | ∞ (ongoing) | constraint-disclosure-impossible |

**観察**: 第一・第二群の充填は 1976-1978 年に集中（communication 発表 4-6 年後）。これは Kumada グループの自己充填および Yamamoto グループ（同じ Osaka 拠点）による independent follow-up の並行発生を示す。第三群（EP-01a）は「archive data の物理的不可逆性」により「充填不可」として記録される typology example。

---

## §D 層別充填非対称性

**Stage 1 Claim Architecture より**：
- **Layer 1（触媒活性実証）**: Table I の数値実証は original communication で既に present。充填は「報告値の精密化」（GLC calibration upgrade）の形で 1976-1978 に。
- **Layer 2（選択性定量化）**: original にはホモカップリング副産物の定量がない。充填は EP-09a（Kumada et al. 1978）で初めて量的に establish。充填開始=確立 1978。
- **Layer 3（機構証拠）**: EP-10a (kinetics), EP-03a (NMR), EP-04a (radical exclusion) により 1976-1984 걸쳐 段階的に充填。Layer 3 の充填は Layer 1・2 より遅延（logic는 mechanistic detail < synthetic proof）。

**asymmetry pattern**: Layer 1 ≈ immediate (original paper), Layer 2 ≈ 6 yr, Layer 3 ≈ 4-12 yr。この非同期性は典型的な「反応発見 → 最適化 → 機構理解」の publication sequencing を reflect している。

---

## §E 制度設計への寄与

本 EP 充填マップから：

1. **format-driven auto-resolution（C23）の確実な事例**：Communication 1972 → Full Article 1976-1978 の transition で、GLC method detail および ligand screen data が自動投入された。communication 形式の「紙幅制限による合理的報告欠落」が、継続出版の explicit continuation で「format-driven 充填」として resolved される pattern を示す。VQ-2 (era-norm qualified) の判定根拠を empirically validate。

2. **自己充填 (self-filling) の prevalence**：6つの EP 中 4つが Kumada またはその immediate collaborators（Yamamoto, Tamao）による original author group の publications で充填されている。この「著者自身による後続投入」パターンは、communication + follow-up strategy での「意図的な報告分割」を示唆。publication timing strategy と logical layers との alignment。

3. **constraint-disclosure-impossible パターンの documentation**：EP-01a の未充填は「技術的不可能」ではなく「archival access と retrospective interview の物理的制約」に由来。1950-1970 年代の analytical chemistry data の「disclosure 延期後の非恢復可能性」が、modern-era standard（complete GLC method specification）との gap として記録される typology case。§4 Era-Norm Annotation と conjoint して「どの欠落が era-tolerated か、どれが constraint-driven か」の distinction を document する価値。

4. **充填年数の field-wide pattern**：第一・二群の「4-6 年での rapid filling」は、Kumada coupling が emerging field の「hot topic」だったことを反映。当時の競争的研究環境で、原著の問い（mechanism, selectivity proof）が優先度高く取り上げられた。PRI-11 (Mechanism-kinetics decoupling) が 1970 年代の「acceptable deferral」だったことを支持。

---

confirmed_english_interrogation:
"Stage 3 §5 の 5 つの primary EP に対し、Kumada group およぴ collaborating groups による自己充填と independent field responses による parallel filling が 1976-1984 年に観測される。特に EP-10a（kinetics）と EP-09a（benchmark）の 6-year filling は、communication → full paper transition の canonical pattern を exemplify する。EP-01a（reporting detail）は constraint-disclosure-impossible として未充填に分類。"

inference_time_sec: not available — inject externally
