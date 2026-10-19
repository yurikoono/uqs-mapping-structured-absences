```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6
```

# EP充填選定マップ

## Martin & Buchwald 2007（J. Am. Chem. Soc. 2007, 129, 3844–3845）

---

### §A EP充填難易度の三群分類

本論文（JACS Communication、2007）について、C23トリガー確認：
**C23 trigger: applicable（Communication/Letter 形式）**

本論文は JACS Communication（2 ページ）であり、reporting completeness 関連 EP（EP-01a 系）が Letter→Full Paper auto-resolution パターンの評価対象となる。しかし Martin & Buchwald は本論文で Full Paper への言及（"details to be reported"等）をしておらず、後続 Full Paper の存在は別途確認が必要。

---

**第一群（文献で明確に追跡可能）：** EP-10a, EP-04a, EP-03a, EP-07a

- **EP-10a（Kinetic verification pack）**: Pd/biarylphosphine 系での酸化的付加の速度論的研究は Buchwald グループ自身と Hartwig グループが独立した論文として発表しており、"palladium biarylphosphine oxidative addition kinetics" という検索語で直接ヒットする独立研究が存在する。
- **EP-04a（Discrimination/replication pack）**: Kumada-Corriu の化学選択性（ArI > ArCl/Br）を競争実験で実証した研究は、Kumada クロスカップリングの method 展開論文群（2010年代以降）に含まれる。独立論文として発表されている可能性が高い。
- **EP-03a（Direct-observation / state-assignment pack）**: Pd(0)/biarylphosphine 錯体の低温 NMR 観察・単離は、Buchwald グループの ligand mechanistic studies に含まれる可能性が高い。³¹P NMR および X 線結晶構造解析による Pd 錯体キャラクタリゼーションは独立論文の主題として発表されている。
- **EP-07a（Boundary-test pack）**: ArBr/ArCl への適用範囲の拡張は、後続の Kumada-Corriu 一般条件論文（Buchwald 2010 以降）で対応する可能性が高い。

**第二群（間接的に追跡可能）：** EP-05a, EP-08a

- **EP-05a（Quantitative-ranking substantiation pack）**: L2 vs L3 の配位子選択性の定量的根拠は、Buchwald グループの biarylphosphine 配位子設計論文（Acc. Chem. Res. / J. Am. Chem. Soc. 系の配位子 scope 論文）に間接的に含まれる可能性があるが、本論文の Table 3 ヘテロアリールグリニャール系に特化した配位子スクリーニングが独立研究として存在するかは不確実。
- **EP-08a（Replication/uncertainty pack）**: GC 応答係数の開示と反復実験の統計処理は、Full Paper 展開時に自動解消される可能性がある（C23 パターン）が、2007 年以降の JACS Full Article においても低温 Kumada-Corriu の独立再現研究はインセンティブ構造的に行われにくい（第三群のインセンティブ構造的未充填に近い）。

C23 Letter→Full Paper auto-resolution 評価：
- Martin & Buchwald（2007）の直後（2007–2010 年）に同一著者グループからの Full Paper が発表されたかは確認が必要（auto_resolution_status: pending）。

**第三群（充填が見つからない可能性あり）：** EP-01a（報告形式），EP-08a（反復測定慣行）

- **EP-01a（Reporting-coherence pack）**: GC 応答係数の不開示と mass balance の欠如は、計算化学・物理化学のベンチマーク文脈では追試論文が存在するが、合成化学の JACS Communication では分野慣行として未開示が継続する可能性が高い。「インセンティブ構造的未充填」パターン：合成化学分野では mass balance 開示と GC 応答係数補正が独立論文の主題になることは稀であり、出版インセンティブの不整合により第三群と判定。
- **EP-08a（反復測定慣行）**: n≥3 の独立再現実験による標準偏差報告は、新規合成方法論の領域では技術的に可能だが、追試論文として独立発表されることは合成化学分野では構造的に起こりにくい。「インセンティブ構造的未充填」として明記。

---

### §B 各EPの充填論文候補

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory] + PRI-11 [Mechanism-kinetics decoupling]
* **充填開始点**: Alcazar-Roman, L. M.; Hartwig, J. F. *Organometallics* **2002**, *21*, 491–502 — ArI および ArOTf の Pd(0) 触媒への酸化的付加の速度論的研究；第二次速度論的データと活性化パラメータを報告（原論文自身が ref 10a として引用）。ただしこの論文は原論文（2007）より**先行**しており、先行充填パターン（v18追加）に該当。
  - **注記**: この充填は「先行充填」（原論文より時間的に先行する論文による充填）であり、Martin & Buchwald は Alcazar-Roman 2002 を引用して自己の機構主張を支持しようとしているが、Alcazar-Roman 2002 の実験系（L: DPPF, 室温-30°C 条件）は必ずしも本論文の Pd/biarylphosphine 系（−20〜−65 °C）と対応しない。したがって「充填の性質」は Indirect に留まる。
* **充填確立点**: Stambuli, J. P.; Bühl, M.; Hartwig, J. F. *J. Am. Chem. Soc.* **2002**, *124*, 9346–9347（or similar Buchwald group kinetic study on biarylphosphine OA, ~2007-2012） — Buchwald グループ自身による biarylphosphine/Pd 系の OA 速度論的研究が充填確立点の有力候補（要 verification）。
* **充填の性質**: Indirect（Alcazar-Roman 2002 は類似系での先行充填；biarylphosphine 系 + 低温でのケース特異的充填は別途必要）
* **Bibliographic confidence**: Medium（Alcazar-Roman 2002 は原論文 ref 10a として確認可能 = High；Buchwald グループの後続 kinetic study は ~Medium、要 verification）
* **Filling adequacy confidence**: Medium（Alcazar-Roman 2002 は直接の系ではなく Indirect 充填；対象系特異的充填は推定）
* **Verification recommendation**: [必須]（(c) 反応名 = Kumada-Corriu クロスカップリング / named reaction、(b) Buchwald グループから 10+ 関連論文）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven / field-methodology (5-10 yr、2007 以降の Buchwald グループ機構論文が充填確立点の候補)
* **注記**: EP-03a と部分的にバンドル充填（Pd resting state 観察は OA 速度論研究の副産物として現れる可能性）。先行充填パターンの記録として重要：原論文が ref 10a で先行充填を援用しようとしているが、系の非対応性が「部分充填」に留まらせている構造。

---

**EP-04a [Discrimination/replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator] + RI-01 [Reporting integrity]
* **充填開始点**: —未同定（合成化学分野でのクロスカップリング化学選択性の競争実験を主題とする論文を特定できず）。類似の方法論的検討は Negishi または Suzuki 系で行われている可能性があるが、Kumada-Corriu 系特異的な ArI vs ArCl 競争実験論文は Low confidence でのみ推定可能。
* **充填確立点**: 未同定
* **充填の性質**: 未同定
* **Bibliographic confidence**: Low（具体的な充填論文を特定できない）
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]（(c) Kumada named reaction、(d) Confidence Low）
* **Bibliographic verification status**: pending（充填論文候補未同定）
* **Filling timescale category**: non-applicable（未同定のため）
* **注記**: SRG-2 の核心 RI（RI-04）への充填は、合成化学の出版慣行では「化学選択性の直接競争実験」が独立論文として発表されることが稀であり、第三群に近い位置付け。ただし、方法論化学の review 論文（例：Knochel グループの総説）に部分充填データが含まれる可能性は残る。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Christmann, U.; Vilar, R. *Angew. Chem. Int. Ed.* **2005**, *44*, 366–374（または Buchwald グループの biarylphosphine-Pd(0) 錯体単離論文）— biarylphosphine/Pd(0) 錯体の構造キャラクタリゼーション（¹H/³¹P NMR + X 線）が先行充填の有力候補。ただし本論文の低温（−20 °C）における resting state 特異的な観察ではない。
* **充填確立点**: Fors, B. P.; Buchwald, S. L. *J. Am. Chem. Soc.* **2010**, *132*, 15766–15768（または同グループの Pd/biarylphosphine 構造論文）— 要 verification。
* **充填の性質**: Partial/Indirect（低温 resting state 特異的観察は未確認；室温での biarylphosphine-Pd(0) 構造 = Indirect）
* **Bibliographic confidence**: Medium（Christmann 2005 = High；Buchwald 後続の具体的論文 = Medium）
* **Filling adequacy confidence**: Low-Medium（低温特異的 Pd resting state の観察充填 = Low；室温構造での Indirect 充填 = Medium）
* **Verification recommendation**: [必須]（(c) named reaction 系、(b) Buchwald グループ 10+ 関連）
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (5-10 yr)
* **注記**: EP-10a とバンドル候補（速度論研究と resting state 観察は同一論文に現れることが多い）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]（ArBr/ArCl への適用範囲）+ RI-05 [Qualitative overread]（L2/L3 切替え）
* **充填開始点（ArBr/ArCl 境界）**: Martin, R.; Buchwald, S. L. *Acc. Chem. Res.* **2008**, *41*, 1461–1473（または同年代の Buchwald の汎用 Kumada-Corriu 条件論文）— 著者自身が後続 Account/Full Paper でより広い基質スコープ（ArBr/ArCl 含む）を報告する可能性が高い（自己充填パターン）。
* **充填確立点**: Jiang, X.; Nohara, Y.; Hatanaka, M. または Buchwald グループの「low-temperature Kumada coupling of aryl bromides/chlorides」論文（~2009–2015、要 verification）
* **充填の性質**: Partial（ArBr/ArCl 境界が拡張されたとしても、それは「現在は ArI のみ」という限界の克服であり、限界の機構的説明（RI-07）は別途 EP-10a が必要）
* **Bibliographic confidence**: Medium（Buchwald 2008 Acc. Chem. Res. の存在は High；specific ArBr/ArCl extension paper は Medium）
* **Filling adequacy confidence**: Medium（自己充填パターンとして合理的に推定可能）
* **Verification recommendation**: [必須]（(c) Kumada, (b) Buchwald グループ, (d) 複数 Medium-Low候補）
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)（著者グループによる自己充填の典型的タイムスケール）
* **注記**: 「A-1」（A 分類の ongoing 宣言）との対応関係は直接的：A-1 と A-2 は著者が後続論文で自己充填することを示唆しており、EP-07a は自己充填の有力候補。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]（L2/L3 選択の "no explanation" 言及）
* **充填開始点**: Surry, D. S.; Buchwald, S. L. *Chem. Sci.* **2011**, *2*, 27–50（Buchwald グループの配位子設計総説、または配位子 SPhos/XPhos 設計論文）— biarylphosphine の電子・立体パラメータと触媒特性の相関が間接的に含まれる可能性（Indirect 充填）。
* **充填確立点**: 未同定（L2/L3 具体的なヘテロアリール Grignard 専用配位子比較論文は未特定）
* **充填の性質**: Indirect（配位子設計の一般論としての充填；本論文の Table 3 ヘテロアリール系に特化した比較は未同定）
* **Bibliographic confidence**: Medium（Surry & Buchwald 2011 は High；ヘテロアリール専用の比較論文 = Low）
* **Filling adequacy confidence**: Low（全体配位子論文は存在するが Table 3 特異的な比較の充填は不明）
* **Verification recommendation**: [推奨]（単一要因：1990–2000 年代論文群 + Buchwald グループ）
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (5-10 yr)

---

**EP-08a [Replication/uncertainty pack]（第二群/第三群境界）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: 「インセンティブ構造的未充填」。合成化学方法論において n≥3 反復 + SD 報告を主題とした独立論文は存在しない。Full Paper 展開（C23 pattern）で部分解消の可能性はあるが：
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "promised" # 未確認
  filling_timescale_category: "format-driven"
  ```
* **充填の性質**: インセンティブ構造的未充填（Full Paper 展開時に部分解消の可能性）
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]（インセンティブ構造的未充填の記録）
* **Filling timescale category**: format-driven（Full Paper 展開による自動部分解消）/ non-applicable（独立充填論文として）

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填の性質**: constraint-disclosure-impossible / インセンティブ構造的未充填
* **未同定理由**: GC 応答係数補正・mass balance 開示・元素分析完全実施は、2007 年の合成化学 Communication では分野慣行として不完全な形が許容されており、追試論文や方法論論文として独立発表されることは構造的にない。
  ```yaml
  incentive_structure_type: "incentive-misaligned"
  filling_substitute: "Full Paper 続報（該当する場合）での GC 補正開示が部分代替"
  ```
* **Bibliographic verification status**: non-applicable
* **Filling timescale category**: non-applicable

---

### §B 末尾チェック：Bibliographic verification

**トリガー条件の評価：**
- (a) 論文年代が古い（1980 年以前）: 非該当（2007 年）
- (b) 著者ネットワークが密（Buchwald グループから 10+ の関連論文）: **該当**
- (c) 反応名が author name 由来（Kumada-Corriu）: **該当**
- (d) Bibliographic confidence Medium-Low の候補が 2 件以上: **該当**（EP-04a, EP-07a, EP-03a）

**結論: Verification recommendation = [必須]（全候補）**

§C では全エントリに「⚠️ verification 待機中」を付記する。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Alcazar-Roman & Hartwig, *Organometallics* 2002, 21, 491 | EP-10a（先行充填 Indirect） | VQ-3方向 | 2002 | High | Medium | 必須 ⚠️ |
| 2 | Buchwald グループ 後続 Full Paper/Account（~2008–2010）| EP-07a, EP-08a（auto-resolution） | VQ-2 | ~2008 | Medium | Medium | 必須 ⚠️ |
| 3 | Christmann & Vilar, *Angew. Chem. Int. Ed.* 2005, 44, 366 | EP-03a（Indirect）| VQ-3方向 | 2005 | High | Medium | 必須 ⚠️ |
| 4 | Surry & Buchwald, *Chem. Sci.* 2011, 2, 27 | EP-05a（Indirect） | VQ-2 | 2011 | Medium | Low | 推奨 ⚠️ |
| 5 | Buchwald グループの ArBr/ArCl 拡張論文（~2009–2015）| EP-07a（CLA-1 境界）| VQ-2 | ~2010 | Medium | Medium | 必須 ⚠️ |

全エントリ ⚠️ verification 待機中。

**選定理由：**
本論文（2007 JACS Communication）の EP 充填においては、Buchwald グループ自身による自己充填（後続 Full Paper / Account）が中心的役割を果たすと推定される。Alcazar-Roman & Hartwig（2002）は唯一 Bibliographic confidence High の先行充填候補であり、原論文 ref 10a での引用が確認されている（充填が先行している点に注意）。EP-10a は VQ-3 到達への最重要 EP であり、先行充填の質（Indirect）の評価が推奨選定リストの中核的判断事項となる。EP-04a（chemoselectivity 競争実験）は充填論文が未同定であり、VQ-3 到達への致命的障壁として記録する。EP-01a / EP-08a は第三群として未充填記録。

Bibliographic verification が必須であるため、本推奨選定リストは暫定であり、全エントリの DOI 照合を完了してから最終リストとして確定する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2 要件（RI-01, RI-07, RI-08）:**
  - EP-08a (RI-08) → Full Paper 展開時（~2008–2010 推定）自己充填 [format-driven]
  - EP-07a (RI-07, ArBr/ArCl) → 著者グループ後続論文（~2010）自己充填 [field-methodology, 2-3 yr]
  - EP-01a (RI-01) → インセンティブ構造的未充填 [non-applicable]

- **VQ-3 要件（RI-03, RI-04, RI-05）:**
  - EP-10a (RI-03) → Alcazar-Roman 2002（先行充填 Indirect）→ Buchwald 後続機構論文（~2007–2012）[field-methodology]
  - EP-04a (RI-04) → **未同定**（最重要 Fatal 未充填）
  - EP-05a (RI-05) → Surry & Buchwald 2011 [field-methodology, ~4 yr]
  - EP-03a (RI-03) → Christmann 2005（先行充填 Indirect）[field-methodology]

**階層-時間対応の評価：**

VQ-2 要件の充填（EP-07a, EP-08a）は format-driven auto-resolution（~2-3 年）と field-methodology（~5 年）の組み合わせで比較的早期に解消されると推定される。一方、VQ-3 要件の核心（EP-04a: RI-04 chemoselectivity 競争実験）は充填論文が未同定であり、仮説「VQ 階層が上がるほど充填に要する時間が長くなる」を支持するが、その理由は「技術的困難」ではなく「分野慣行による構造的回避（インセンティブ構造的未充填）」である。VQ 階層-時間仮説は本ケースでは部分的に支持されるが、driving force は技術的バリアではなく出版インセンティブの不整合である。

**特筆すべきパターン：**

1. **先行充填パターン（2 件）**: EP-10a（Alcazar-Roman 2002）と EP-03a（Christmann 2005）はいずれも原論文（2007）より**先行**する充填候補であり、Martin & Buchwald がこれらを引用しながら機構支持に使用しているにもかかわらず、その系特異性（biarylphosphine、−20〜−65 °C）が不一致であるため Indirect 充填に留まる。これは、分野に「近い」充填論文が存在するにもかかわらず、対象系特異的な充填が未達である構造的不在の典型例。

2. **自己充填予測パターン（A-1, A-2）**: A 分類の「ongoing investigations」宣言（A-1: ArBr/ArCl, A-2: その他基質）は、EP-07a への自己充填を著者自身が予告するものである。これは「通信→Full Paper 遷移の自動解消パターン」（C23）の典型的発火条件。

3. **VQ-3 Fatal 未充填（EP-04a）**: SRG-2 の核心（chemoselectivity 競争実験の不在）は、分野慣行として「産物単離での化学選択性確認」が標準であり、競争実験論文が独立発表されることは合成化学では構造的に稀。これが VQ-3 未到達の持続的障壁として記録される。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-04a [Discrimination/replication pack]:**
* **未充填の理由**: インセンティブ構造の不整合。ArI vs ArCl/ArBr の競争実験は技術的に可能だが、「chemoselectivity の直接的競争実験」を主題とした独立論文として合成化学コミュニティで発表される慣行が確立していない。産物単離による間接的化学選択性確認が分野標準であるため、競争実験データが独立論文の主題になることなく、方法論 Scope 内の一データポイントとして包埋されるか、または方法論的改善論文の補足データとして埋没する。
* **発見的意義**: あり。「chemoselectivity を産物単離のみで主張し、競争実験を行わない」パターンは Kumada-Corriu のみならず Pd 触媒クロスカップリング方法論論文に共通する構造的不在であり、「分野が体系的に回避してきた実験設計」として記録できる。UQS-based 分析における RI-04 の cross-domain pattern（SRG-2 / EP-04a 型）の代表事例として位置付けられる。
* **将来の充填可能性**: 中。ハイスループット実験（HTE）や自動化合成プラットフォームを用いた方法論的評価論文が 2020 年代に増加しており、ArI/ArBr/ArCl の選択性を定量的に評価した HTE 論文での充填可能性は中程度。

**EP-01a [Reporting-coherence pack]（mass balance / GC 応答係数）:**
* **未充填の理由**: インセンティブ構造の不整合 + 分野慣行。合成化学 JACS Communications での GC 応答係数補正と mass balance 開示は、2007 年当時も現代（2026 年）も、独立論文の主題として発表されることはなく、Full Paper 展開時の補足的開示（SI 記載）に留まる。出版インセンティブが「新規基質スコープ」に集中し、「既存エントリの定量的精度向上」には向かない。
* **発見的意義**: あり（限定的）。mass balance 不開示の組織的パターンは UQS が指摘しうるが、これは本論文固有の不在ではなく分野全体の慣行を反映するため、本論文の特殊性を示す発見としての意義は低い。RI-01 の field-wide prevalence の例証として記録する価値はある。
* **将来の充填可能性**: 低。分野慣行として構造的に維持される不在であり、合成化学 Communication のフォーマット規範が変わらない限り充填されない。

**VQ階層逆転の診断：**
充填の実際の進行順（観察・予測）は EP-07a（VQ-2 要件、~2-3 年）→ EP-05a（VQ-2, ~4 年）→ EP-10a（VQ-3 方向, 先行充填あり）の順であり、EP-04a（VQ-3 の Fatal 要件）が長期未充填になると推定される。「科学的論理に基づく EP 充填順序（VQ-2 優先 → VQ-3 確立）」に対し、「実際の充填順序（化学選択性の直接検証 = EP-04a が後回し）」が逆転しているパターンが本ケースに観察される。これは出版インセンティブが「新規基質スコープ（EP-07a, VQ-2）→ 配位子設計（EP-05a, VQ-2）→ アカウント総説」の順に働き、「競争実験による chemoselectivity 直接実証（EP-04a, VQ-3 Fatal）」を系統的に後退させていることを示唆する。
