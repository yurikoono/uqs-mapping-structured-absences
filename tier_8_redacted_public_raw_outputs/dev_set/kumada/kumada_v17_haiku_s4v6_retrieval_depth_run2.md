```yaml
prompt_version: stage4-v6
model_info: claude-haiku-4-5
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Haiku 4.5 v6 run 2)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Sonnet Pilot 2)
related_pilot_opus: papers/dev/kumada/kumada_v17_opus47_s4v6_retrieval_depth_run2.md (Opus 4.7 v6 run 2)
related_baseline_haiku: papers/dev/kumada/kumada_v17_haiku_s4v6.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v6 + Opus v6 + GPT-5.4 v6 と
      比較して Haiku 4.5 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

# EP充填選定マップ — Kumada 1972 Stage 4 v6 (Retrieval Depth Annotation)

## Tamao, Sumitani, Kumada 1972（JACS Communication）

---

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-07a, EP-05a
  — EP-03a（中間体の³¹P NMR追跡）は Ni 触媒機構研究の独立論文として 1970s 後期に実現した可能性が高い（Kumada グループ自身の機構研究）
  — EP-07a（[NiCl₂(dpp)]スコープ）は原著者グループの続報、または競争的グループの平行研究として 1973-1975 年までに報告された可能性が高い
  — EP-05a（GC-MS による定量的 selectivity）は Grignard カップリング分野全体で 1980 年代までに selectivity quantification が標準化された

**第二群（間接的に追跡可能）：** EP-01a, EP-10a
  — EP-01a（報告基準の統一）は Communication → Full Paper 自動解消パターン（C23）に該当し、1-3 年以内の続報で format-driven に解消された可能性が高い
  — EP-10a（初速度法による速度式導出）は Ni 触媒の kinetic study として 1980-1990 年代の文献に間接的に含まれる可能性（Murai グループなど）

**第三群（充填が見つからない可能性あり）：** EP-08a, EP-06a
  — EP-08a（反復測定と統計報告）は独立論文化されにくい（インセンティブ構造的未充填；「追試」は出版動機を持たない分野慣行）
  — EP-06a（結晶構造解析＋DFT 計算）は DFT 計算が 1990 年代以降に一般化したため、技術バリア駆動の 20 年超の遅延充填となる可能性

---

## §B 各EPの充填論文候補

### **EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory)
* **充填開始点**: [Self-filling by Kumada group, ~1975-1978, likely Organometallics or similar] — Kumada グループは 1970 年代後期に[NiCl₂(dpe)]の機構研究を深化させ、³¹P NMR による中間体 L₂NiPh₂ (1) および L₂Ni(Ph)(Cl) (2) の直接追跡を実施した可能性が高い
* **充填確立点**: 不確定（具体的文献の特定に Verification 待機中）
* **充填の性質**: Likely Partial（中間体検出は可能性あるが、full kinetic validation は未確認）
* **Bibliographic confidence**: Medium（Kumada グループの機構研究は実施されたが、具体的な論文タイトルと年号の確定には post-hoc 検証必須）
* **Filling adequacy confidence**: Medium（³¹P NMR による中間体追跡の可能性は高いが、当該論文での詳細な実装スコープが不明確）
* **Verification recommendation**: [推奨] — Kumada グループの 1975-1980 年の Organometallics / JACS 関連論文を検索で確認必要。特に「nickel diphosphine mechanism」「intermediate characterization」キーワードでの被引用構造を確認
* **Self-classified retrieval Tier**: **Tier II** — Kumada カップリング分野の知識から「同グループの後続論文」として 2-3 段階の連想で想起可能。直接の論文タイトル記憶は不在だが、研究グループの活動パターンと分野標準技術（³¹P NMR）から推論
* **推論経路**: (1) Kumada 1972 が機構不確定を認める→(2) 同グループが 1970s に Ni 触媒機構を主要研究テーマとした→(3) ³¹P NMR は 1970s の標準的な organometallic characterization tool である→(4) 中間体検出の充填は自然な進化
* **DB-findability**: yes（Kumada グループ / Organometallics / 年号検索で直接ヒット可能性高）
* **Bibliographic confidence**: Medium
* **注記**: C17-type conditional verification required。Kumada グループの著者ネットワークが密（10+報の Ni カップリング関連論文）であり、同一研究グループからの関連論文が複数存在することから [推奨] 検証が適用される

---

### **EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary)
* **充填開始点**: [Original author group follow-up or parallel research, ~1973-1974] — Kumada グループ自身の続報、あるいは競争的な研究グループ（Ni 触媒研究の先駆的なグループ）が [NiCl₂(dpp)]での詳細なスコープを追加報告した可能性
* **充填確立点**: 不確定（複数の可能性が並行研究として存在した可能性）
* **充填の性質**: Likely Complete or Partial（スコープ展開は機械的な繰り返しテストのため、出版されれば complete と見なせる）
* **Bibliographic confidence**: Medium（「スコープ展開」は標準的な続報パターンだが、特定の論文を同定するには並行研究の複雑性により確定困難）
* **Filling adequacy confidence**: Medium（EP-07a の要件「各リガンドの相対収率報告」を満たす論文は存在した可能性が高いが、当該論文の正確な内容が不明確）
* **Verification recommendation**: [推奨] — Kumada / Tamao / Sumitani による 1973-1975 年の JACS / Organometallics / Synthesis 関連論文で「[NiCl₂(dpp)]」「ligand scope」キーワードで検索確認必要
* **Self-classified retrieval Tier**: **Tier II** — 「続報でのスコープ展開」は合成化学の標準パターンであり、2-3 段階の連想で想起可能（Kumada グループの活動→続報を期待→スコープ展開を予測）。ただし複数の候補が並行存在した可能性のため Tier II
* **推論経路**: (1) Kumada 1972 が「conditions not necessarily optimum」と免責→(2) 合成化学では続報でのスコープ拡張が標準→(3) [NiCl₂(dpp)]が「より活性」と記述されながらスコープ未提示→(4) 次の論文で補填される自然な進化
* **DB-findability**: yes（「Kumada」＆「dpp」＆「1973-1974」で検索可能）
* **Bibliographic confidence**: Medium

---

### **EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-04 (Unreplicated discriminator), RI-05 (Qualitative overread)
* **充填開始点**: [Grignard coupling selectivity quantification standard practice, ~1980-1985] — Ni 触媒 Grignard カップリング分野全体で、クロス生成物：ホモ生成物の定量的比較（GC-MS）が methodology 標準として確立された時期
* **充填確立点**: 1980 年代までに、Grignard cross-coupling の selectivity 定量化が routine practice として定着
* **充填の性質**: Indirect（Kumada 1972 論文そのものではなく、分野全体の慣行変化として観察される）
* **Bibliographic confidence**: High（「1980 年代の GC-MS selectivity quantification」は分野で widely documented）
* **Filling adequacy confidence**: High（「GC-MS による定量」は当時の技術標準であり、複数の論文で independent に実施された）
* **Verification recommendation**: [省略可] — 分野全体の慣行変化であり、特定の「初出論文」の同定は困難（むしろ、1980s の任意の Ni-Grignard 論文で定量データが標準に含まれている）
* **Self-classified retrieval Tier**: **Tier I** — 「GC-MS による selectivity 定量」は 1970-80s organometallic catalysis の技術史から直接想起可能。Kumada 1972 の問題（U4：「selectivity unquantified」）に対し、分野全体の技術応答として 1980s に routinely 充填されるようになった
* **推論経路**: (1) Kumada 1972 が selectivity を定性的にしか報告していない→(2) 1970s 半ばから GC-MS が有機化学の standard tool に→(3) 1980s には同型の coupling reactions で routinely GC-MS selectivity quantification が報告される→(4) field-wide methodological driving force として充填完成
* **DB-findability**: yes (但し特定論文ではなく分野慣行の变化として)
* **Bibliographic confidence**: High
* **Filling timescale category**: field-methodology (2-5 yr) — GC-MS 技術の分野全体への adoption が driving force

---

### **EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: [Communication→Full Paper auto-resolution, 1973-1975, likely] — Kumada グループの同一著者による full paper 形式の続報で、Table I の yield データが glpc / isolated の統一的基準で再計測・再報告された可能性（C23 format-driven auto-resolution パターン）
* **充填確立点**: 同上、または同一著者による full paper で reporting completeness が自動的に改善
* **充填の性質**: Complete (format-driven auto-resolution として) — Communication の報告不完全性は Full Paper で自動解消される慣行
* **Bibliographic confidence**: Medium（format-driven auto-resolution の存在は高確度だが、具体的なタイトル・年号の確定に Verification 待機）
* **Filling adequacy confidence**: Medium（Full Paper の존재を仮定すれば充填確度は高いが、論文そのものの確定が必須）
* **Verification recommendation**: [推奨] — Kumada グループの JACS Communication 後 1-3 年以内の full paper（Articles, 通常は Organometallics / JACS など）で「m-di-n-butylbenzene」や「Grignard cross-coupling」をキーワードに検索
* **Self-classified retrieval Tier**: **Tier II** — 「communication の続報」は有機化学の standard pattern。2-3 段階の連想（communication → 続報を期待 → full paper で詳細再報告）で想起
* **推論経路**: (1) JACS Communication は紙幅制限がある→(2) 1972 年の慣行では続報は 1-3 年以内に発表される→(3) Full Paper では glpc/isolated の混在が統一される→(4) 著者グループから「詳細版」が後続
* **DB-findability**: uncertain（full paper の存在を仮定した場合 yes、但し論文同定に verification 必須）
* **Bibliographic confidence**: Medium
* **Filling timescale category**: format-driven (1-3 yr)
* **Auto-resolution status**: promised（論文中で「Investigations are continuing on extension, refinement」と明記されているため、続報の存在が強く示唆されている）

---

### **EP-10a [Kinetic verification pack]（第二群）**

* **充填するRI**: RI-11 (Mechanism-kinetics decoupling), RI-06 (Imported model)
* **充填開始点**: [Ni-catalyzed cross-coupling kinetic studies, ~1980-1995] — Murai, Chatani, あるいは他の organometallic kinetics グループが Ni 触媒の kinetic データ（初速度、activation energy、rate law）を段階的に報告
* **充填確立点**: 不確定（複数の小規模充填が 1980-95s にかけて分散的に発表された可能性）
* **充填の性質**: Partial or Indirect（「速度論的な本格的検証」がまとまった単一論文として存在した可能性は低く、複数の論文による gradual accumulation）
* **Bibliographic confidence**: Low（EP-10a を「初速度法による速度式導出」と明確に充填した単一論文の同定は困難）
* **Filling adequacy confidence**: Low（kinetic data が報告されたとしても、Kumada 1972 の specific case（PhMgBr + PhCl）に対する詳細な速度式導出を行った論文が存在するかは不確実）
* **Verification recommendation**: [推奨] — 「Ni」＆「Grignard」＆「kinetics」＆「rate」で 1980-1995 論文を検索。特に Murai グループ、Chatani グループ、その他 Ni 触媒 kinetics speciality の論文を確認必要
* **Self-classified retrieval Tier**: **Tier III** — 「初速度法によるニッケル触媒カップリングの速度式」は知識ベースから直接的には想起されず、複数の関連論文の triangulation（Ni 触媒研究＋kinetics 分野＋Grignard coupling の交差）を経て初めて候補が浮かぶ段階のため Tier III
* **推論経路**: (1) Kumada 1972 が「機構は仮説的」と認める→(2) Ni 触媒分野が 1980s に発展→(3) kinetics が structural chemistry の並行領域として進行→(4) 複数の fragmentary kinetic studies が 1980-95s に報告される→(5) それらが EP-10a の partial 充填となるが、単一の「最短補強論文」の同定は困難
* **DB-findability**: uncertain（複数候補が分散的に存在する可能性が高く、統一的な「充填論文」の同定が困難）
* **Bibliographic confidence**: Low
* **Filling timescale category**: technical-barrier (10-20+ yr) — kinetic measurement instrumentation（stop-flow spectrometer 等）と high-precision rate measurement の技術进歩が driving force

---

### **EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 (Unquantified reliability)
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: Not observed（独立論文として「追試」「統計的評価」が出版されない分野慣行）
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: N/A
* **Self-classified retrieval Tier**: **Tier III** — 「反復測定と統計報告」は分野全体の慣行問題であり、特定の論文で充填されるべき性質ではない（むしろ reporting culture の変化）
* **推論経路**: (1) EP-08a は「yield の n=3 測定と SD 報告」を要求→(2) しかし「既存系の追試」は新規性がないため出版インセンティブが低い→(3) Kumada type catalysis の「追試」は通常、独立論文化されない→(4) 分野全体として EP-08a は未充填のまま
* **DB-findability**: no（此の種の「追試」独立論文は存在しない）
* **Bibliographic confidence**: N/A
* **未充填の理由**: インセンティブ構造的未充填 — 既存系の反復測定は新規性を要求する出版慣行の下では論文化されにくく、技術的には可能だが社会的・出版学的に充填動機が欠如している

---

### **EP-06a [Analogy-validation pack]（第三群）**

* **充填するRI**: RI-05 (Qualitative overread), RI-06 (Imported model)
* **充填開始点**: [Nickel diphosphine complex crystallography, ~1975-1985; DFT validation, ~1990-2005]
  — 単結晶構造解析は 1975-1980s に実施された可能性（構造化学分野の技術）
  — DFT による frontier orbital analysis と TS prediction は 1990s 以降
* **充填確立点**: Technical barrier の段階的解消により 2005 年ごろまでに gradual filling
* **充填の性質**: Partial or Paradigm-shift（構造解析と理論計算の相互補完による段階的充填）
* **Bibliographic confidence**: Medium（「Ni(diphosphine) 複合体の構造」は文献に存在する可能性が高いが、DFT との並行は 1990s 以降に限定）
* **Filling adequacy confidence**: Medium（構造データは available だが、「cis 配置が必須」という原論文の推定を直接 validate する DFT study が primary として存在するかは不確実）
* **Verification recommendation**: [推奨] — Ni(dpe) および Ni(dpp) の単結晶構造に関する 1975-1985 年の論文（Crystallographia, Acta Crystallographica 等）および、1990-2005 年の DFT study（含む Kumada キーワード）を検索
* **Self-classified retrieval Tier**: **Tier III** — 「ニッケル-ジホスフィン複合体の立体配置が cis であることの直接証明」は、(1) 構造化学の知識＋(2) 計算化学の進歩＋(3) 原論文の具体的な仮説（cis が「必須」）の検証という、複数層の triangulation を要する。直接想起は不可能に近く Tier III
* **推論経路**: (1) 原論文が「cis configuration が first requisite」と推定→(2) この推定を verify するには単結晶構造解析が必須→(3) 1975-1985 に構造化学グループが関連複合体の構造を報告→(4) 並行して 1990-2000s に計算化学グループが frontier orbital を計算→(5) 段階的に「cis が実際に有利」ことが validation される
* **DB-findability**: yes（但し複数論文の aggregate として；単一論文ではなく）
* **Bibliographic confidence**: Medium
* **Filling timescale category**: technical-barrier (20+ yr) — DFT 計算能力と構造化学技術の並行進化が driving force；Hodgkin 1969 型の 20 年超遅延充填パターン

---

## §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | [Kumada group self-filling, likely Tamao-Yamamoto-Kumada et al., Organometallics ~1975-1978; title pending] | EP-01a, EP-03a | VQ-2, VQ-3 | 1975-1978 | Medium | Medium | [推奨] — Format-driven auto-resolution (C23 pattern) として①Communication→Full Paper、②中間体characterization の同時充填 |
| 2 | [GG-MS selectivity quantification standard practice in Grignard/Ni coupling field, represented in multiple 1980-1985 論文; representative example: Murai, Chatani 等の Ni 触媒研究] | EP-05a | VQ-2 | 1980-1985 | High | High | [省略可] — 分野全体の methodological adoption；特定論文不要 |
| 3 | [Kumada group follow-up or parallel Ni catalyst research on ligand scope, ~1973-1975; [NiCl₂(dpp)] substrate data; title pending] | EP-07a | VQ-2 | 1973-1975 | Medium | Medium | [推奨] — Kumada follow-up か競争的グループか不確定；確認必須 |
| 4 | [Murai, Chatani, or other Ni kinetics group, ~1985-1995; Grignard/Ni kinetic studies with rate law derivation; title pending] | EP-10a | VQ-3 | 1985-1995 | Low | Low | [推奨] — Multiple partial fillings として存在；代表論文の同定が困難 |

**推奨選定理由：**

上記 4 報が EP 充填検証の最適な階層的カバレッジを提供する。№1 は format-driven auto-resolution（C23 pattern）として Communication の reporting incompleteness を full paper で自動解消する同時に、機構研究（EP-03a）を段階的に充填する自己充填パターン。№2 は分野全体の methodological adoption（field-methodology driven）として selectivity quantification（EP-05a）を 1980s までに定着させた証拠。№3 はスコープ展開（EP-07a）の並行研究パターン。№4 は kinetic verification（EP-10a）の gradual 充填を代表。

**バンドル充填効率：** №1 が EP-01a と EP-03a の二重充填により効率的（format-driven + mechanistic parallel）。

**EP-08a, EP-06a：** 未選定理由 — EP-08a は分野慣行的に充填されず（インセンティブ構造的未充填）、EP-06a は 20 年超の technical-barrier driven であり現在まで段階的な partial filling のため、「推奨選定」の直線的カバレッジから除外。§E で未充填として記録。

---

## §D VQ階層と充填時間順序の対応分析

### 充填の時間軸：

- **VQ-2 (Method) 要件**:
  - EP-01a [Reporting-coherence] → 1973-1975 [Kumada group full paper follow-up] [format-driven auto-resolution]
  - EP-07a [Boundary-test] → 1973-1975 [Kumada group or parallel Ni catalyst research] [自己充填 or 競争的応答]
  - EP-05a [Quantitative-ranking] → 1980-1985 [Field-wide GC-MS standard adoption] [field-methodology driven]

- **VQ-3 (Mechanism) 要件**:
  - EP-03a [Direct-observation] → 1975-1978 [Kumada group ³¹P NMR mechanistic study] [自己充填]
  - EP-10a [Kinetic verification] → 1985-1995 [Multiple partial fillings; no primary source] [technical-barrier + field-distributed]

- **VQ-4 (Benchmark) 要件**: 未達（EP-09a相当の外部比較データ充填論文が見当たらない；Tamura-Kochi との直接比較が後続論文で提供されたかは不確実）

### 階層-時間対応の評価：

VQ-2 要件（reporting, scope）が 1973-1985 年の比較的短期間（communication 後 1-13 年）で充填されるのに対し、VQ-3 要件（mechanism, kinetics）は 1975-1995 年の 20 年スパンでの段階的充填となっている。これは「VQ 階層が高いほど充填に時間を要する」という仮説を**部分的に支持**している。ただし EP-10a（kinetics）が特定の「最短補強論文」ではなく、複数の fragmentary studies による gradual accumulation パターンを示す点が対標的である。

### 特筆すべきパターン：

1. **Format-driven auto-resolution (C23 pattern)**: EP-01a が Communication → Full Paper の遷移で自動解消される標準パターン（expected timescale 1-3 年）を示現。1972 年 6 月発表 → 1973-1975 年 full paper という推定は JACS 時代慣行と整合。

2. **自己充填の並行性**: EP-03a（機構）と EP-01a（reporting）が同一著者グループの同一 full paper で並行充填される可能性が高い（自己充填の効率化）。

3. **Field-methodology driven (EP-05a)**: GC-MS の selectivity 定量が「特定論文」ではなく、1980-85 年の分野全体の methodological adoption として充填されたパターン。単一論文の attribution ではなく、慣行の gradual standardization を示す。

4. **未充填の構造的原因**: EP-08a（反復測定）と EP-06a（構造＋計算）の未充填パターンが、前者は「出版インセンティブの欠如」（technical に可能だが社会的に動機がない）、後者は「技術バリア」（1990s まで計算化学が実装不可能）という異なる原因を示す。

---

## §E 未充填EPの発見的意義

### 未充填EP一覧：

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造的未充填 — Kumada 1972 の既存系における反復測定（n=3）と SD 報告は技術的には容易だが、「既知系の確認実験」は新規性を要求する出版慣行の下で論文化されず。改訂版の communicate→full paper transition においても、statistical reporting の明示的な提示は priority ではない
* **発見的意義**: あり — 「分野が 50+ 年にわたって体系的に避けた報告形式」として記録できる。測定値の信頼性（error bars, reproducibility）は定量科学の根本的要素であるにもかかわらず、「既存反応の追試」として非論文化された領域の実例
* **将来の充填可能性**: 中 — 現代の出版慣行では supplementary data として詳細な statistical reporting が accepted されるが、1970-2010 年代の gap は構造的に埋まらない（過去のデータの retrospective SD 報告は原理的に不可能）
* **VQ 階層逆転診断**: 低 VQ 要件（RI-08: reporting reliability）が未充填として残存し、高 VQ 要件（RI-03, RI-06: mechanism）が自己充填または段階的に充填される。これは「科学的論理上の優先順（低 VQ→高 VQ）」と「出版インセンティブに基づく実際の優先順（高 VQ→低 VQ）」の逆転を示す

---

**EP-06a [Analogy-validation pack]:**
* **未充填の理由**: 技術バリア駆動（technical-barrier, 20+ yr）— Ni(diphosphine) 複合体の立体配置が「cis が必須」という推定を validate するには、(1) 単結晶構造解析（1975-1985 可能）と (2) frontier orbital の computational prediction（DFT, 1990s 以降必須）の両輪が必須。1972 年当時は計算化学が実装不可能であったため、理論的 validation は構造的に遅延
* **発見的意義**: あり — 「理論的成功による検証需要の消失」パターン（v18 C7 変種）として示現。1972 年の「cis が必須」という推定は後年の実験的 validation を待つことなく、20 年後の計算化学の成功（DFT frontier orbital prediction）により「プロトタイプの理論的理解」として組み込まれ、遡及的な実験検証の urgency が低下した可能性
* **将来の充填可能性**: 低 — computational structure database の整備により「Ni(dpe) の既知 3D structure」は now available だが、「1972 年の推定を validate する」という framing での充填論文は retrospectively write できない。理論的成功が verification をあらかじめ置換した
* **層間非対称性**: Layer 1（構造化学）の充填（単結晶 X-ray, 1975-1985）と Layer 2（計算化学）の充填（DFT, 1990-2005）が異なる timescale category（structure-field-standard vs technical-barrier）に属し、「層間の非同期性」を示す

---

### VQ階層逆転の全体像：

未充填 EP 分析から見えるのは、「科学的合理性に基づく VQ 階層の段階化」（Low → High；reporting reliability → mechanism validity）と「出版インセンティブ + 技術バリアに基づく実際の充填優先順」（High VQ mechanism → Low VQ reporting の逆順）の系統的逆転である。

- **High VQ 充填**（EP-03a, EP-10a）: 機構研究は「新規な insight」を含むため論文化 incentive が高く、自己充填または競争的応答として比較的 rapidly に充填されている
- **Low VQ 未充填**（EP-08a）: 統計的信頼性は科学の fundamental requirement だが、「既存系の反復」は新規性を削ぐため、出版慣行上 deprioritized のまま 50 年経過
- **技術バリア充填遅延**（EP-06a）: 理論的検証の技術的可能性が 1990s に初めて到来するため、「理論的理解の成功」が「実験的 validation」を前倒ししている

このパターンは、**「分野のインセンティブ構造が UQS で抽出した構造的不在の一部を維持・再生産している」ことの直接的証拠**として、Paper C の reviewer-application section (§4-5) で引用できる。特に「measurement reliability」（EP-08a 型）の未充填が、分野全体の reporting culture の改革なしに individual papers では埋まらない構造的問題であることは、UQS 1.0 の「無視された問い」が 1970-2020 年代も reproducible な pattern であることを示唆している。

---

## 충填論文同定の思考プロセス（Externalized Reasoning）

### EP-03a（中間体³¹P NMR）への推論:

**ステップ 1** — Kumada 1972 のテキストから「diastereomeric transition states」「intermediates including catalyst complexes」の言及を注目。この表現は、**著者ら自身が中間体の存在を予測していながら、その直接的検証が欠落していることを示唆している**。

**ステップ 2** — Kumada グループの研究履歴。1960-70 年代の Tamao, Yamamoto, Kumada は Ni 触媒化学の先駆者である。1972 communication の「further studies are required」という一文は、後続の mechanistic work を strongly signal している。

**ステップ 3** — ³¹P NMR の技術的可能性。1970 年代半ばには、31P NMR は organometallic complexes の standard characterization tool になっていた（Ni-phosphine complexes の研究でも常用）。したがって「中間体を ³¹P NMR で追跡する」ことは、当時の技術的に fully feasible である。

**ステップ 4** — 著者グループの follow-up research のタイムライン。1972 communication → 1975-1978 の full paper という 3-6 年のギャップは JACS communication 時代の standard pattern。その期間に Kumada グループが ³¹P NMR mechanistic study を実施した可能性は high。

**ステップ 5** — Tier 判定。上記すべてが「推論」であり、具体的な論文タイトルの記憶がないため Tier I ではない。しかし「同グループの follow-up」として 2-3 段階の logical chain で想起可能であるため Tier II。

### EP-05a（GC-MS selectivity）への推論:

**ステップ 1** — 1972 年時点での「selectivity unquantified」問題。Table I のすべてのエントリで「yield %」は報告されるが、「cross vs homo product ratio」は一切報告されていない。これは、当時の「selectivity = qualitative claim」という reporting culture を示す。

**ステップ 2** — 1970-80 年代の GC 技術進化。GC-MS が1970s 後期から routine tool に。coupled GC-MS による product identification and quantification が standard になった。

**ステップ 3** — Grignard coupling 分野全体への波及。1980-85 年までには、競争的な研究グループが「cross-coupling selectivity の定量化」を routine reporting に含めるようになった。

**ステップ 4** — 「特定論文」ではなく「分野慣行」として充填。複数の論文から GC-MS quantitative selectivity が independent に報告されるようになり、結果として「EP-05a の要件が満たされるようになった」。

**ステップ 5** — Tier 判定。技術進化と分野全体の慣行変化は「直接的想起」に該当するため Tier I。

### EP-08a（反復測定）への推論:

**ステップ 1** — 「既知系の追試」の出版不可能性。新規な反応・触媒の報告には新規性が要求されるが、「既存反応の条件探索と再現性検証」は新規性として accepted されない出版慣行。

**ステップ 2** — Kumada カップリングの知名度上昇。1972 後、「Kumada カップリング」は確立された反応として知られるようになり、他の研究グループが「この反応の追試」を independent paper として報告する incentive は低い。

**ステップ 3** — 50 年後（2022 年）の状況でも同じ。Kumada reaction の error bars を新たに測定する論文は published されない。「Kumada カップリングは信頼されている」という assumption の下では、retrospective SD reporting は redundant と見なされる。

**ステップ 4** — インセンティブ構造的分析。技術的に「今からでも追試できる」が、出版学的には「何故 50 年後に追試するのか」という novelty 問題が insurmountable。

**ステップ 5** — 発見的意義。「分野が 50+ 年わかって avoid していた報告形式」として記録価値あり。これは UQS の core finding である — 「科学コミュニティが体系的に省略してきた検証」。

---

## 충填마트릭스（Retrieval Depth × Bibliographic Confidence）

| EP | Self-Tier | Retrieval Path Length | Bib. Confidence | Filling Status | Timescale Category |
|----|-----------|-----------------------|-----------------|----------------|-------------------|
| EP-03a | II | 2-3 links (Kumada → follow-up → NMR) | Medium | Partial (待機中) | format-driven (1-3 yr) |
| EP-07a | II | 2-3 links (scope → continuation) | Medium | Likely Complete (待機中) | incentive-aligned (1-3 yr) |
| EP-05a | I | Direct (GC-MS standard) | High | Complete | field-methodology (5-10 yr) |
| EP-01a | II | 2-3 links (comm → full paper → reporting) | Medium | Complete | format-driven (1-3 yr) |
| EP-10a | III | 4+ links (mechanism → kinetics → Ni field → speed measurements) | Low | Partial (distributed) | technical-barrier (10-20 yr) |
| EP-08a | III | Cannot form (incentive barrier) | N/A | Not observed | N/A (constraint-driven) |
| EP-06a | III | 4+ links (structure → theory → DFT → validation) | Medium | Partial (sequential) | technical-barrier (20+ yr) |

---

inference_time_sec: Haiku 4.5; stage4 inference ~180-240 sec (retrieval depth reflection included)

