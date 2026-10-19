```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

C23 trigger: **applicable** — 対象論文はJACS Communication（Letter）形式。reporting completeness関連のEP-01a, EP-07a, EP-02aについてLetter→Full Paper auto-resolution patternを確認する。

**第一群（文献で明確に追跡可能）：** EP-07a, EP-03a, EP-06a, EP-05a, EP-09a

- EP-07a: sp²/sp³ハライドのスコープ境界試験と塩化物/臭化物/ヨウ化物の定量的比較は、Kumada反応のFull Paper続報の明確な実験的主題として独立論文化されやすい（RI-07はFull Paper展開で第一優先的に解消される）。
- EP-03a: NiCl₂(dpe)系でのジオルガノニッケル中間体の直接観測は、1970年代の有機ニッケル化学における主要研究課題であり、複数の独立研究グループが機構研究として発表している。
- EP-06a: dipy-Ni系から輸入したサイクルの対象系（NiCl₂(dpe)）での化学量論的素反応実証は、Kumada反応機構解明の中心課題として独立論文化されている。
- EP-05a: 代表的基質での反応混合物の質量収支（クロスカップリング vs. ホモカップリング vs. β-脱離）は、選択性の定量的根拠として続報論文で必要不可欠な実験内容。
- EP-09a: NiCl₂(dpe) vs. Ni(acac)₂の直接比較は、Corriu/Masseとの同時並行発見を踏まえ、配位子設計の独自性を問う研究として独立して扱われうる。

**第二群（間接的に追跡可能）：** EP-01a, EP-02a, EP-04a

- EP-01a: Table I全エントリの統一glpc条件・統一収率基準・反応時間の完全報告は、同一著者グループのFull Paper続報での自動解消候補（C23 Letter→Full Paper pattern）であり、独立研究の主題にはなりにくい。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-4 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```
- EP-02a: Table IエントリのGC-MSまたは¹H NMRデータの個別記録は、Full Paper展開時の補完事項であり独立論文の主題ではない（C23 pattern）。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-4 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```
- EP-04a: cis/trans-stilbene比の時間・温度系列と定量GLC反復測定は、立体化学的機構研究の文脈では実施されうるが、1970年代の合成化学的文脈ではこの特定の問い（速度論/熱力学制御の区別）が独立研究の主題として取り上げられた可能性は限定的。

**第三群（充填が見つからない可能性あり）：** EP-08a

- EP-08a: 代表的エントリの収率の独立した反復測定（n≥3）と標準偏差の報告は、1970年代有機合成化学の出版慣行では追試・反復測定が独立論文化されないインセンティブ構造のため第三群。「インセンティブ構造的未充填」に該当する。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 原著者グループによるFull Paper続報で、統一した反応条件・反応時間・glpc条件下での11基質以上のスコープを系統的に記述し、RI-01（報告フレームの不統一）を実質的に解消した。
* **充填確立点**: 同上
* **充填の性質**: Complete（format-driven auto-resolution）
* **Bibliographic confidence**: High（著者リスト・雑誌・年・巻号に高信頼性）
* **Filling adequacy confidence**: High（Full Paper形式でのscope拡大論文はRI-01要件を構造的に充たす）
* **Verification recommendation**: [必須] — (a) 1980年以前、(b) Kumadaグループから10+関連論文、(c) Kumada reactionとして命名規則が成立
  ```
  Bibliographic verification status: pending
  ```
* **Filling timescale category**: format-driven (4 yr: 1972→1976)
* **注記**: C23 Letter→Full Paper auto-resolution patternの典型事例。同論文はEP-02a, EP-05a, EP-07aも部分的にバンドル充填する（下記各エントリで相互参照）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 同Full Paperでsp²ハライドのみが有効なスコープ制限を失敗例（sp³ハライド不活性）を含めて体系的に記録し、「Only Csp² halides can be used」の実験的根拠を確立した。
* **充填確立点**: 同上（sp³ハライドの不活性確認）+ Hayashi, T.; Konishi, M.; Kobori, Y.; Kumada, M.; Higuchi, T.; Hirotsu, K. *J. Am. Chem. Soc.* **1984**, *106*, 158–163 — sp²選択性の機構的根拠（酸化的付加の選択性）を定量的に確立した（後継）。
* **充填の性質**: Complete（1976 Full Paper）; Indirect（1984 JACS, 機構的根拠の追加）
* **Bibliographic confidence**: High（1976 BCSJ）; Medium（1984 JACS — 著者・年・雑誌への信頼性はあるが巻号ページは要確認）
* **Filling adequacy confidence**: High（1976 BCSJ）; Medium（1984 JACS）
* **Verification recommendation**: [必須] — 全要因(a)(b)(c)に該当
  ```
  Bibliographic verification status: pending
  ```
* **Filling timescale category**: format-driven (4 yr, 1976 Full Paper); field-methodology (12 yr, 1984 JACS機構的根拠)
* **注記**: sp³ハライドの不活性確認（失敗例の記録）はFull Paper形式への展開で自動解消される典型的RI-07; 「塩化物の高反応性」の定量的根拠は、1970年代のKumadaグループおよびHayashi-Kumadaグループのligand-effect研究で段階的に確立された。Layer 2 (sp²選択性・塩化物反応性) 充填は Layer 1 (収率データ完全報告) よりも長いtimescale（field-methodology）を要した。

---

**EP-02a [Identity/purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Characterization completeness]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full Paperで各基質の生成物について個別の物性値・NMRデータ・元素分析を記録し、"and/or"構文（RI-02）を解消した。
* **充填確立点**: 同上
* **充填の性質**: Complete（format-driven auto-resolution）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: High
* **Verification recommendation**: [必須]
  ```
  Bibliographic verification status: pending
  ```
* **Filling timescale category**: format-driven (4 yr)
* **注記**: C23 Letter→Full Paper auto-resolution patternの典型；EP-01aと同一論文によるバンドル充填。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory entity]
* **充填開始点**: Tamao, K.; Zembayashi, M.; Kiso, Y.; Kumada, M. *J. Organomet. Chem.* **1973**, *55*, C91–C94 — 原著者グループが通信形式でNiCl₂(dpe)とGrignard試薬の反応中間体の化学量論的挙動を初めて記録した（部分的充填）。
* **充填確立点**: Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* **1975**, *97*, 7262–7270 — Ni-触媒クロスカップリングにおけるNi(I)/Ni(III)対Ni(0)/Ni(II)経路を識別する実験的研究（ラジカル中間体検証・クロス実験）を実施し、dpe-Ni類似系での機構的実体を確立した（類似系での充填）。
* **充填の性質**: Partial（充填開始点）; Indirect（充填確立点 — dpe-Niそのものではないが電子的に最も関連する比較系）
* **Bibliographic confidence**: Medium（Tamao 1973 J. Organomet. Chem. 55, C91 — 巻号ページ要確認）; High（Morrell & Kochi JACS 1975, 97, 7262）
* **Filling adequacy confidence**: Medium（充填開始点：化学量論的挙動の記録は中間体の直接分光観測には届かない）; Medium（Morrell/Kochi：類似Ni系でのラジカル検証であり、NiCl₂(dpe)系での³¹P NMR観測という要件は未充足）
* **Verification recommendation**: [必須] — 全要因(a)(b)(c)に該当
  ```
  Bibliographic verification status: pending
  ```
* **Filling timescale category**: field-methodology (1-3 yr, 充填開始点); incentive-aligned (3 yr, Morrell/Kochi)
* **注記**: NiCl₂(dpe)系でのジオルガノニッケル中間体の分光学的直接観測（低温³¹P{¹H} NMR）は、1970年代の技術的水準では可能だが、この特定の系に対する独立した論文化が確認されていない。EP-06a（RI-06: サイクルレベル輸入の検証）と不可分共起のため、EP-03aとEP-06aの充填はほぼ同一の実験的取り組みに収束する（§6「RI-06+RI-03の不可分共起」パターンと整合）。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model at cycle level]
* **充填開始点**: Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* **1975**, *97*, 7262–7270 — NiXR（ハロゲノ-オルガノNi）錯体の化学量論的反応を実施し、クロスカップリング触媒サイクルの個別素反応を独立に検証した最初の体系的研究。
* **充填確立点**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332 — Ni(0)錯体への酸化的付加を定量的に研究し、Ni(0)/Ni(II) 二電子経路の素反応を個別に実証（酸化的付加の速度論・立体化学）。
* **充填の性質**: Partial（Morrell/Kochi 1975: 素反応の化学量論的検証だがNiCl₂(dpe)系でない）; Indirect（Tsou/Kochi 1979: Ni(PPh₃)₂系での詳細機構だがdpe-Ni系への外挿可能）
* **Bibliographic confidence**: High（Morrell/Kochi JACS 1975, 97, 7262）; High（Tsou/Kochi JACS 1979, 101, 6319）
* **Filling adequacy confidence**: Medium（両論文とも dpe-Ni 系での直接実証ではなく関連 Ni 系での類似検証）
* **Verification recommendation**: [必須] — (a) 1980年以前、(b)(c)に部分該当
  ```
  Bibliographic verification status: pending
  ```
* **Filling timescale category**: incentive-aligned (3-7 yr: 1972→1975/1979)
* **注記**: dipy-Ni系からdpe-Ni系へのサイクルレベル輸入（RI-06）の検証は、Kochi グループの系統的なNi酸化状態・素反応研究によって間接的に充填された。NiCl₂(dpe)固有の化学量論的検証（EP case-specif実装の要件）は現在も完全な意味では未充填の可能性が残る。EP-03aとのバンドル充填候補。

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full PaperでGLC分析による副生物（ホモカップリング、β-脱離生成物）の定量を含む系統的スコープ研究を実施し、「選択的」クロスカップリングに数値的根拠を提供した。
* **充填確立点**: 同上（1976 Full Paper series）
* **充填の性質**: Partial（Full PaperがRI-05を部分解消するが、eq(3)が予測するR-R生成物の体系的質量収支は論文の主題ではない可能性あり）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: Medium（Full PaperがU-1の自己矛盾的不在——eq(3)予測のR-R未報告——を完全に解消しているかは内容確認が必要）
* **Verification recommendation**: [必須]
  ```
  Bibliographic verification status: pending
  ```
* **Filling timescale category**: format-driven (4 yr)
* **注記**: EP-01aと同一論文によるバンドル充填候補。RI-05（定性的主張からの過剰読み込み）の完全解消には、SRG-2（B-1, U-1, C-1）全体のカバレッジが必要であり、1976 Full Paperが質量収支を明示的に記録しているかの確認が必須。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: **未同定** — cis/trans-stilbene比の時間・温度系列実験と定量GLC反復測定（速度論/熱力学制御の区別）を主題とする独立論文は現時点で同定できない。
* **充填確立点**: Hayashi, T.; Konishi, M.; Fukushima, M.; Mise, T.; Kagotani, M.; Tajika, M.; Kumada, M. *J. Am. Chem. Soc.* **1982**, *104*, 180–186 — Ni-ジアミノホスフィン触媒を用いた不斉クロスカップリングの研究で、cis/trans立体化学制御の反応条件依存性を定量的に扱ったが、1972年報のcis/trans-stilbene問題の直接的検証ではない（間接充填）。
* **充填の性質**: Attempted（上記の文脈では直接検証ではない）; 実質的には **未同定**
* **Bibliographic confidence**: Medium（1982 JACS: Hayashi/Kumada不斉coupling関連の参照は複数存在するが具体的巻号要確認）
* **Filling adequacy confidence**: Low（EP case-specific実装——cis/trans比の速度論/熱力学識別——を直接扱う論文として同定できていない）
* **Verification recommendation**: [必須]
  ```
  Bibliographic verification status: pending
  ```
* **Filling timescale category**: non-applicable（充填論文が同定されていないため）
* **注記**: cis/trans-stilbene比の速度論/熱力学的起源という問い（U-3）は、Kumada反応が合成手法として実用化された後、機構研究の主題として選択されにくかった可能性がある（合成目的での問いの優先度低下）。§Eで詳述。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定**（インセンティブ構造的未充填）
* **充填確立点**: 未同定
* **充填の性質**: 非適用（第三群：インセンティブ構造的未充填）
* **Bibliographic confidence**: 非適用
* **Filling adequacy confidence**: 非適用
* **Verification recommendation**: 非適用
* **Filling timescale category**: non-applicable
* **注記**: 1970-1980年代の合成有機化学において、既発表系での反復測定（n≥3）と標準偏差の報告を独立論文化するインセンティブは存在しなかった。技術的には実施可能だが、出版規範のもとで論文化されない典型的インセンティブ構造的未充填。§Eで詳述。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority undisclosed]
* **充填開始点**: Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc., Chem. Commun.* **1972**, 144–145 — 同時期独立発見としてNi(acac)₂触媒によるクロスカップリングを報告（原論文のNote Added in Proofで既に記録済み）。これが実質的な「比較の起点」を形成する。
* **充填確立点**: Kumada, M.; Tamao, K.; Sumitani, K. *Org. Synth.* **1978**, *58*, 127–133 — KumadaグループのOrg. Synth. procedureで[NiCl₂(dpe)]触媒の実用条件を確立、他Ni系との選択の根拠を実践的に文書化した（部分的充填）。さらなる直接比較研究として: Hayashi, T.; Kumada, M. *Account Chem. Res.* **1982**, *15*, 395–401 — 配位子設計と反応性のレビューで、dphosphine vs. 非キレート型Niの活性を体系化した（間接充填）。
* **充填の性質**: Partial（Org. Synth. 1978: 実用化文書として充填）; Indirect（Acc. Chem. Res. 1982: レビューとしての系統化）
* **Bibliographic confidence**: Medium（Kumada, Tamao, Sumitani Org. Synth. 1978, 58, 127 — 巻号ページ要確認）; Medium（Hayashi, Kumada Acc. Chem. Res. 1982, 15, 395 — 年・巻号は推測含む）
* **Filling adequacy confidence**: Medium（Org. Synth. 1978）; Low（Acc. Chem. Res. 1982 — レビュー論文としての位置づけに注意; EPの要件は直接比較実験であり系統化レビューでは不足）
* **Verification recommendation**: [必須] — 全要因(a)(b)(c)に該当
  ```
  Bibliographic verification status: pending
  ```
* **Filling timescale category**: incentive-aligned (6-10 yr: 1972→1978/1982)
* **注記**: Corriu/Masse (1972)との対比（EP-09aの核心）は、配位子設計原理の独自性問題として科学コミュニティが体系的に検証した形跡は限定的。「キレートジホスフィンは必要条件か」という問い（CLA-1の核心）は、後続のPd触媒クロスカップリングの発展によって問い自体が再定義された（パラダイム転換的解消）。

---

**§B 末尾チェック：Bibliographic verification**

**トリガー条件の評価：**
- (a) 論文年代が古い（1980年以前）: 全エントリの充填開始点が1970-1979年 → 該当
- (b) 著者ネットワークが密（Kumadaグループから10+関連論文が存在）→ 該当
- (c) 「Kumada coupling」「Kumada reaction」として著者名由来の命名規則が成立 → 該当
- (d) Bibliographic confidence Medium-Low候補が2件以上含まれる → 該当

**Verification recommendation: 全エントリに [必須] を付与**。§Cの推奨選定リストでは、Bibliographic verification status: pending のエントリはすべて「⚠️ verification 待機中」として明示する。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958 | EP-01a, EP-02a, EP-05a, EP-07a | VQ-2 | 1976 | High | High (EP-01a/02a), Med (EP-05a/07a) | ⚠️ 必須 |
| 2 | Morrell & Kochi, *J. Am. Chem. Soc.* 1975, 97, 7262 | EP-03a, EP-06a | VQ-3 | 1975 | High | Medium | ⚠️ 必須 |
| 3 | Tsou & Kochi, *J. Am. Chem. Soc.* 1979, 101, 6319 | EP-06a | VQ-3 | 1979 | High | Medium | ⚠️ 必須 |
| 4 | Tamao et al., *J. Organomet. Chem.* 1973, 55, C91 | EP-03a | VQ-3 | 1973 | Medium | Medium | ⚠️ 必須 |
| 5 | Kumada, Tamao, Sumitani, *Org. Synth.* 1978, 58, 127 | EP-09a | VQ-2/実用 | 1978 | Medium | Medium | ⚠️ 必須 |
| 6 | Hayashi & Kumada, *Acc. Chem. Res.* 1982, 15, 395 | EP-09a (partial) | VQ-4参照 | 1982 | Medium | Low | ⚠️ 必須 |

**選定理由：**

最優先候補（順序1）はTamao et al. 1976 BCSJ Full Paperである。このバンドル充填論文は EP-01a, EP-02a（RI-01, RI-02: reporting completeness）、EP-05a（RI-05: selectivity quantification）、EP-07a（RI-07: scope boundary）の4EPをカバーし、VQ-2到達に必要な最短補強ルートの第一・第二ステップを一括解消する。Letter→Full Paper auto-resolution（C23）の決定的事例として、1976年（4年後）に充填が発生した。

VQ-3要件（RI-03, RI-06: 中間体・触媒サイクルの実験的検証）については、Kochi グループによる独立研究（順序2, 3）が最も適切な充填候補であり、Morrell/Kochi 1975がNi触媒素反応の化学量論的実証の起点、Tsou/Kochi 1979が酸化的付加の定量的機構研究として充填確立点を形成する。EP-03aとEP-06aの不可分共起（Stage 3 §6パターン6）を反映し、両EpPへの対応として同一グループの2論文（順序2, 3）を選んだ。

Tamao et al. 1973 J. Organomet. Chem.（順序4）は原著者グループ自身による中間体化学量論的研究として、EP-03aの充填開始点として独立させた。

EP-04a（cis/trans速度論/熱力学識別）については充填論文が同定されず選定リストに含めていない（§E参照）。EP-08a（反復測定）も第三群のため除外。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件（RI-01, RI-02: reporting completeness）: EP-01a, EP-02a → 1976年 [Tamao et al., BCSJ] [自己充填, format-driven]
- VQ-2 要件（RI-07: scope boundary）: EP-07a → 1976年 [Tamao et al., BCSJ] [自己充填, format-driven]
- VQ-2/3 要件（RI-05: selectivity quantification）: EP-05a → 1976年（部分）[Tamao et al., BCSJ] [自己充填, format-driven/field-methodology]
- VQ-3 要件（RI-03, RI-06: intermediate/cycle）: EP-03a → 1973年（部分）[Tamao et al., J. Organomet. Chem.] [自己充填]; 1975年 [Morrell/Kochi, JACS] [分野横断充填]; 1979年 [Tsou/Kochi, JACS] [分野横断充填]
- VQ-4 要件（RI-09: external benchmark）: EP-09a → 1978年（部分）[Kumada et al., Org. Synth.] [自己充填]; 1982年（間接）[Hayashi/Kumada, Acc. Chem. Res.] [自己充填]
- VQ-3 要件（RI-04: replication/discrimination）: EP-04a → **未充填**
- VQ-4 要件（RI-08: uncertainty quantification）: EP-08a → **未充填**（インセンティブ構造的）

**階層-時間対応の評価：**

VQ-2要件（reporting completeness, RI-01/RI-02/RI-07）はすべて1976年のFull Paper続報で一括充填され、format-driven auto-resolution（4年）として解消された。これは仮説の「VQ階層が上がるほど充填に要する時間が長くなる」を部分的に支持する。しかし**反例として**、VQ-3要件の中核（RI-03, RI-06: 中間体と触媒サイクルの直接証拠）は1973–1975年（1–3年）に部分的充填が開始し、VQ-2要件の完全充填（1976年）よりも先行した形跡がある。これはVQ-3の機構的問いが（VQ-2の報告形式問題と独立して）科学コミュニティの独立した研究動機を形成したことを示し、「VQ階層 ∝ 充填時間」という単純な線形仮説は成立しない。

**特筆すべきパターン：**

1. **自己充填の集中（VQ-2）**: EP-01a, EP-02a, EP-07a, EP-05aはすべて原著者Kumadaグループ自身のFull Paperシリーズで自己充填された。これはKumada反応の研究プログラムが単一グループの長期継続として展開された結果であり、外部充填（分野横断充填）が少ない。

2. **分野横断充填（VQ-3）**: EP-03a/EP-06aの機構的充填はKochiグループ（異なる研究グループ）が担った。これはNi触媒機構の問いが独立した研究関心を形成したことを示す。

3. **先行充填パターン（EP-03a）**: Tamao et al. 1973 J. Organomet. Chem.（1年後の早期通信）は、1972年論文のVQ-3要件充填を1976年のFull Paper展開より先行して開始した。原著者グループが機構的問い（EP-03a）を最優先で続報したことを示す。

4. **VQ階層逆転の診断**: RI-04（EP-04a）はVQ-3水準の問いだが未充填。RI-08（EP-08a）はVQ-4水準でインセンティブ構造的未充填。一方でVQ-3の別要件（RI-03, RI-06）は3年以内に充填開始。この非対称性は「機構的な問い（RI-03/06）は充填される; 統計的信頼性の問い（RI-04/08）は充填されない」というインセンティブ構造の選択的作用を示す。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-04a [Discrimination / replication pack]:**
* **未充填の理由**: 関心の欠如 + 成功による問いの抹消（Success-driven question erasure）。cis/trans-stilbene比（80:20, 43:57）の速度論/熱力学的起源という問い（U-3）は、Kumada反応が合成的に大成功を収めた後、「なぜcis富化が起こるか」を独立研究として検証するコミュニティの需要が消滅した。Pd触媒クロスカップリング（Heck, 鈴木, 根岸, 1970–80年代）の急速な発展が合成化学的関心をNiからPdに移行させ、Ni系固有のcis/trans選択性問題の体系的検証が優先されなかった。また技術的には（時間・温度系列実験で）可能だが、「速度論か熱力学か」という問いへの答えが合成実用性に直結しないことがコミュニティの動機を弱めた。
* **発見的意義**: あり。UQSはこの問いを1972年論文の構造的不在として抽出したが（U-3, A-1, B-11のSRG-6に収束）、同問いが50年以上体系的に未検証のまま「Kumada反応の特徴」として記録されてきたことを確認できる。「成功した方法が生み出す観察論理的前提の未検証ゾーン」という発見的意義を持つ。
* **将来の充填可能性**: 中。現代の定量GLC技術（internal standard + calibration curve）と低温反応停止技術で容易に実施可能だが、Kumada反応への現代的関心がNi触媒クロスカップリング復興（エアロビック, 地球豊富金属)に向いており、1972年論文固有の問いとして研究プログラム化される可能性は限定的。

---

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造的未充填。代表的エントリの収率の独立反復測定（n≥3）と標準偏差の報告は、1970年代から現代に至るまで合成有機化学の出版慣行において独立論文として価値を認められない。技術的には可能だが、新規性を要求する出版規範のもとで「既存反応の統計的評価」は論文化されにくい。Kumada反応の個々のエントリの収率の統計的信頼区間は、2026年現在でも体系的に報告されていない可能性が高い。
* **発見的意義**: あり。SRG-3（B-4, B-8, B-9, B-12, B-13）が示す「Table Iの収率データの解釈可能性の喪失」という問題は、1976年Full Paperで部分的に解消されたが（EP-01a自動解消）、収率の統計的信頼性（RI-08）については現代に至っても分野全体が「測定するが標準偏差を報告しない」という慣行を維持している。これは個別論文の問題ではなく合成有機化学全般のインセンティブ構造問題の典型事例として記録に値する。
* **将来の充填可能性**: 低（個別論文として充填される見込みは低いが、再現性研究の分野動向（ReplicationStudies in chemistry, 2020年代の動き）が進展すれば系統的充填の機会が生まれる可能性はある）。