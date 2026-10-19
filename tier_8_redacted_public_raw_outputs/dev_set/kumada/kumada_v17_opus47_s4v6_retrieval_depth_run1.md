```
prompt_version: stage4-v6
stage3_input_version: s3v2 (Stage 3 prompts only exist up to v4; s3v2 is the only Opus 4.7 Stage 3 output)
model_info: claude-opus-4-7
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Opus 4.7 v6 run 1)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Sonnet Pilot 1)
related_pilot_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4v6_retrieval_depth_run1.md (GPT-5.4 v6 run 1)
related_baseline_opus: papers/dev/kumada/kumada_v17_opus47_s4v2.md (April 19 baseline, no annotation, v2 prompt)
note: Multi-run robustness の cross-vendor extension。Sonnet v6 multi-run + GPT-5.4 v6 multi-run と
      比較して Opus 4.7 v6 prompt 下の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

---

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc., Communication）

---

## Retrieval methodology disclosure（思考過程の外在化）

このセッションでは、§B の各 EP 候補を構築するに先立ち、まず「Kumada 1972 の機構・境界・報告完全性 EP に対する充填候補として最初に思い浮かぶもの」をリストアップした：

**最初の retrieval pass（即座に浮かんだもの、Tier I）:**
1. Tamao et al. 1976 Bull Chem Soc Jpn — Full Paper の auto-resolution（EP-01a, EP-02a, EP-09a の format-driven 候補）
2. Corriu & Masse 1972 Chem Commun 144 — already cited as ref 3a, 並行発表

**第二 retrieval pass（連想 2–3 段階で surface、Tier II）:**
3. Hayashi-Kumada asymmetric Ni-coupling 1982 系列 — author group 自己拡張、C_sp³ への extension の萌芽
4. Akira Yamamoto group（Tokyo Institute of Technology）— Ni(II)-organyl 中間体の単離・分光研究、1970s 後半–1980s
5. Knochel organozinc 1990s — 別パラダイムだが C_sp³ 制約の打破を提供
6. Kochi 系列 — radical 機構研究、stereochem probe

**第三 retrieval pass（triangulation を経て surface、Tier III）:**
7. Fu group secondary alkyl Ni coupling（2003+）— C_sp³ 制約の決定的解消だが 30+ 年遅延
8. Vicic group Ni(I)/Ni(III) 機構 — modern radical Ni catalysis
9. Norrby / Hartwig computational studies — 機構の DFT 検証

**早期に考えて棄却した候補（rejection log は §F に詳述）:**
- Negishi 1977（J. Am. Chem. Soc.）— ZnCl₂ 経由は別 paradigm、Kumada 1972 の EP を「充填」するより並走関係
- Suzuki 1979 / Stille 1978 — 同様に別 paradigm（B, Sn 転移金属化）
- Heck reaction 系列 — 機構が異なる（migratory insertion vs reductive elimination）
- Tsuji-Trost 系列 — π-allyl Pd で機構が異なる
- レビュー論文（de Meijere-Diederich "Metal-Catalyzed Cross-Coupling Reactions" 等）— プロンプト規則で EP 充填と認めない

この preliminary retrieval を踏まえ、Step 1（三群分類）から進める。

---

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-02a, EP-07a

— **EP-01a [Reporting-coherence pack]**: RI-01 起源だが本ケースは Communication → Full Paper の format-driven auto-resolution（C23）に該当する典型例。原著者グループ（Tamao-Kumada）の Full Paper（Bull Chem Soc Jpn 1976 系列）が独立刊行物として存在するため第一群。

— **EP-02a [Identity / purity substantiation pack]**: RI-02 起源。EP-01a と同じく Full Paper auto-resolution の対象。EA・HR-MS・GLPC 純度の per-entry 開示は Full Paper 形式で慣例的に提供される。

— **EP-07a [Boundary-test pack]**: RI-07 起源。C_sp³ 基質の境界試験は cross-coupling 化学の中心的展開課題として独立論文の主題となった。Knochel group（organozinc, 1990s）と Fu group（secondary alkyl Ni, 2003+）に明確な独立刊行物列が存在する。

**第二群（間接的に追跡可能）：** EP-03a, EP-04a, EP-05a, EP-06a, EP-09a, EP-10a

— **EP-03a [Direct-observation / state-assignment pack]**: RI-03 起源。Ni(II)-organyl 中間体や Ni(0)-phosphine 種の単離・分光研究は organometallic 中心テーマだが、NiCl₂(dpe)+Grignard 系そのものでの中間体検出は限定的（類似系での充填）。Akira Yamamoto group の Ni(II) 単離研究が間接充填候補。

— **EP-04a [Discrimination / replication pack]**: RI-04 起源。cis/trans-dichloroethylene の stereochem 機構は Ni-cross-coupling の特殊題材で、独立論文化されにくい。Kochi 系列の radical 機構レビュー・Smith-Kochi 1976 が間接充填候補。

— **EP-05a [Quantitative-ranking substantiation pack]**: RI-05 起源。配位子スクリーニング文化は Pd 系で Hartwig/Buchwald 1990s-2000s に確立。Ni 系での network-style ligand screen は modern Ni-catalysis の体系的応答として一部充填。

— **EP-06a [Analogy-validation pack]**: RI-06 起源。β-D 標識実験は β-H elimination kinetics の標準テスト。Whitesides 系列・Yamamoto 系列で類似系での実証はあるが、NiCl₂(dpe)+n-BuMgBr 直接系では限定的。

— **EP-09a [Internal benchmark pack]**: RI-09 起源。Ni(acac)₂ vs NiCl₂(dpe) head-to-head は Tamao 1976 Full Paper で部分対応 + Corriu-Masse 1972 との対比は概念的にのみ後続文献に登場。完全な head-to-head 表は方法論教科書（Hartwig 2010 等の textbook）に集約される。

— **EP-10a [Kinetic verification pack]（暫定）**: PRI-11 起源。NiCl₂(dpe) 系の初期速度次数測定は機構研究として可能だが、Pd cross-coupling の運動論研究と異なり Ni 系では historic に手薄。Yamamoto group・近年の Vicic / Hu group が間接充填候補。

**第三群（充填が見つからない可能性あり）：** EP-08a

— **EP-08a [Replication / uncertainty pack]**: RI-08 起源。「Table I 全 10 エントリの n=3 複製と SD 報告」は合成化学分野のインセンティブ構造上、独立論文化されない。Full Paper（Tamao 1976）でも複数エントリの SD 表は通常含まれない。**インセンティブ構造的未充填**として明記。

---

## §B 各EPの充填論文候補

### EP-01a [Reporting-coherence pack]（第一群）

* **充填するRI**: RI-01 [Reporting integrity], RI-02 [Object identification]（二次）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Communication 1972 の Full Paper 続報。per-entry 条件（mol%, T, t, scale）と GLPC 解析条件を表形式で開示することで RI-01 を解消。
* **充填確立点**: 同上（単一論文で確立）
* **充填の性質**: Complete（Full Paper 形式で per-entry 開示は慣例）
* **Bibliographic confidence**: Medium — author list（Tamao-Sumitani-Kiso-Zembayashi-Fujioka-Kodama-Nakajima-Minato-Kumada）と journal は記憶しているが正確な巻号 1958–1969 は推測値。
* **Filling adequacy confidence**: High — Full Paper の標準内容として per-entry 開示は確実に含まれる。
* **Verification recommendation**: 必須 — トリガー (a) 1980 年以前 + (b) 著者ネットワーク密 + (c) Kumada named reaction を全て満たす。
* **Bibliographic verification status**: pending
* **DOI / URL（任意）**: DOI 未確認。Crossref 検索推奨：title keyword "Selective Carbon-Carbon Bond Formation" + author "Kumada" + year 1976。
* **Filling timescale category**: format-driven (1–3 yr → 4 yr)
* **注記**: Communication（1972）→ Full Paper（1976）の auto-resolution。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```
  実際の resolution は 4 年と expected window をやや超えるが定型 pattern。

**Self-classified retrieval Tier**: I (immediate)
**推論経路**: 「Communication → Full Paper auto-resolution」という C23 patternが prompt 内に明示されており、Kumada group の Full Paper が Bull Chem Soc Jpn 1976 系列で出ていることは organometallic 教科書レベルの知識。第一想起。
**DB-findability**: yes
**Bibliographic confidence**: Medium（巻号要確認）

---

### EP-02a [Identity / purity substantiation pack]（第一群）

* **充填するRI**: RI-02 [Object identification], RI-01（二次）
* **充填開始点**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 同 Full Paper で各製品の elemental analysis、IR / NMR データ、bp / n_D を per-entry 開示。
* **充填確立点**: 同上
* **充填の性質**: Complete（1976 年標準の characterization 開示は EA + IR + NMR + bp/n_D で完結）
* **Bibliographic confidence**: Medium — EP-01a と同論文。
* **Filling adequacy confidence**: High
* **Verification recommendation**: 必須（EP-01a と同じトリガー）
* **Bibliographic verification status**: pending
* **DOI / URL**: 同上
* **Filling timescale category**: format-driven (1–3 yr → 4 yr)
* **注記**: EP-01a と bundle filling（同一論文）。

**Self-classified retrieval Tier**: I (immediate)
**推論経路**: EP-01a と同じ Full Paper 内で per-entry characterization が開示される。Tier I で同論文 bundling。
**DB-findability**: yes
**Bibliographic confidence**: Medium

---

### EP-03a [Direct-observation / state-assignment pack]（第二群）

* **充填するRI**: RI-03 [Unobserved explanatory], RI-06 [Imported model]（二次）
* **充填開始点**: Yamamoto, T.; Yamamoto, A.; Ikeda, S. *J. Am. Chem. Soc.* **1971**, *93*, 3350 系列、または Yamamoto, A. *Organotransition Metal Chemistry* (Wiley, 1986) 内で総括 — Ni(II)-diorganyl 種 (L₂NiR₂) の単離・分光（³¹P/¹H NMR、UV-Vis）研究。NiCl₂(dpe) 系直接ではなく類似配位子系での実証。
* **充填確立点**: Kohara, T.; Yamamoto, T.; Yamamoto, A. *J. Organomet. Chem.* **1980**, *192*, 265 前後 — Ni-phosphine alkyl 中間体の crystal 構造または solution 検出（記憶曖昧、要 verification）。
* **充填の性質**: Indirect（NiCl₂(dpe) + n-BuMgBr 直接ではなく類似 Ni(II) 配位子系での充填）
* **Bibliographic confidence**: Low — Yamamoto group の Ni 中間体研究の存在は確実だが、特定論文の年・巻号・ページは推測。
* **Filling adequacy confidence**: Medium — 中間体構造論的 EP は類似系充填で部分的に成立するが complete とは言えない。
* **Verification recommendation**: 必須（1980 年以前 + 著者ネットワーク密 + Bibliographic Low）
* **Bibliographic verification status**: pending
* **DOI / URL**: 未確認
* **Filling timescale category**: field-methodology (5–10 yr)
* **注記**: 直接充填（NiCl₂(dpe) 系特異）はない可能性が高い。後年の DFT 機構研究（Norrby, Maseras 等、2000s+）が機構層では補完。

**Self-classified retrieval Tier**: II (associative, 2–3 step)
**推論経路**: Ni-phosphine 中間体研究 → Tokyo Tech の Akira Yamamoto group → 1970s-80s の Ni(II)-organyl 単離・分光研究、と連想。具体的論文の bibliographic recall は不確実。
**DB-findability**: yes（Akira Yamamoto + Ni + organonickel + 1970s で検索可能）
**Bibliographic confidence**: Low

---

### EP-04a [Discrimination / replication pack]（第二群）

* **充填するRI**: RI-04 [Unreplicated discriminator], RI-01（二次）
* **充填開始点**: 直接充填は **未同定**。1,2-dichloroethylene + Grignard + Ni-phosphine 系での time-course / TEMPO probe / radical clock の独立研究は記憶上見当たらない。
* **充填確立点**: 部分代替候補：Smith, G.; Kochi, J. K. *J. Organomet. Chem.* 1976 年代の Ni-catalyzed coupling 機構研究、または Kochi の 1978 年単行本 *Organometallic Mechanisms and Catalysis*（Academic Press, 1978）— radical vs 2e 機構の枠組みを提供するが NiCl₂(dpe) + dichloroethylene 直接系の充填ではない。
* **充填の性質**: Indirect / Partial（類似系での radical 機構の枠組みのみ）
* **Bibliographic confidence**: Low — Kochi の Ni 機構著作は確実だが、cis/trans stilbene scrambling 直接系は記憶上ヒットしない。
* **Filling adequacy confidence**: Low — 対象系直接の充填ではない。
* **Verification recommendation**: 必須（Bibliographic Low + 1980 年以前）
* **Bibliographic verification status**: pending
* **DOI / URL**: 未確認
* **Filling timescale category**: incentive-aligned (variable, possibly never directly filled)
* **注記**: 1,2-dichloroethylene scramble は珍しい題材で、直接充填は **未同定**の可能性が高い。Kumada 系列が後続研究で取り上げたかは要確認。

**Self-classified retrieval Tier**: III (deep, triangulation)
**推論経路**: 「Ni-cross-coupling の stereochem probe」→「radical vs 2e 機構の文献的枠組み」→「Kochi の 1970s-80s organometallic mechanism 著作」の triangulation を経て surface。直接的な「dichloroethylene + Ni + Grignard cis/trans 機構」論文は recall に至らず。
**DB-findability**: uncertain（cis/trans stilbene scramble + Ni catalyst で検索しても limited result の可能性）
**Bibliographic confidence**: Low

---

### EP-05a [Quantitative-ranking substantiation pack]（第二群）

* **充填するRI**: RI-05 [Qualitative overread], RI-08（二次）
* **充填開始点**: Pd 系の網羅的 ligand screening は Hartwig group / Buchwald group 1990s-2000s に成熟。Ni 系特異的では Tamao-Kumada の後続論文（Hayashi-Kumada 1980s 不斉 Ni-coupling）で配位子効果が複数基質ペアで報告。
* **充填確立点**: Hayashi, T.; Konishi, M.; Fukushima, M.; Kanehira, K.; Hioki, T.; Kumada, M. *J. Org. Chem.* 1983 系列（不斉 Ni-coupling、bidentate phosphine 比較）または同 group の 1980s 論文系列。
* **充填の性質**: Partial（不斉 coupling 文脈での bidentate phosphine 比較は cis-geometry inference の補強だが、cis-強制単座制御は未充填）
* **Bibliographic confidence**: Low — Hayashi-Kumada 系列の存在は確実だが特定論文の年・巻号は曖昧。
* **Filling adequacy confidence**: Medium — 配位子順位の定量基盤は提供されるが「cis-geometry is the first requisite」の構造的含意の直接検証ではない。
* **Verification recommendation**: 必須（1980 年代 + 著者ネットワーク密 + Kumada named reaction）
* **Bibliographic verification status**: pending
* **DOI / URL**: 未確認
* **Filling timescale category**: field-methodology (10+ yr)
* **注記**: Hayashi-Kumada は author group self-extension。

**Self-classified retrieval Tier**: II (associative)
**推論経路**: 「配位子効果の定量化」→「Kumada group 自己拡張」→「Hayashi-Kumada 不斉 coupling 1980s」の連想 + Pd 系教科書化された Hartwig/Buchwald のフレームワーク knowledge。
**DB-findability**: yes（Hayashi + Kumada + asymmetric coupling で検索）
**Bibliographic confidence**: Low

---

### EP-06a [Analogy-validation pack]（第二群）

* **充填するRI**: RI-06 [Imported model], RI-03（二次）
* **充填開始点**: β-D 標識・添加オレフィン交換実験は Whitesides group（MIT, 1970s）の Ni-alkyl reductive elimination 研究で開拓。Whitesides, G. M.; Gaasch, J. F.; Stedronsky, E. R. *J. Am. Chem. Soc.* **1972**, *94*, 5258 系列。
* **充填確立点**: 同 Whitesides group の 1970s 後半論文 + 後年の Norrby / Hartwig DFT 研究（2000s+）。
* **充填の性質**: Indirect（NiCl₂(dpe) + n-BuMgBr 直接系ではない、Ni-alkyl elimination の類似系）
* **Bibliographic confidence**: Medium — Whitesides 系列は記憶しているが Kumada 系直接ではない。
* **Filling adequacy confidence**: Medium — β-H elimination の機構枠組みは確立、ただし Kumada 反応特異の β-H 寛容性（feature 1）の直接検証ではない。
* **Verification recommendation**: 必須（1970s 論文）
* **Bibliographic verification status**: pending
* **DOI / URL**: 未確認
* **Filling timescale category**: field-methodology (variable)
* **注記**: ref 17（Coates-Green-Wade + Yagupsky-Wilkinson）の輸入モデルへの empirical 補強。

**Self-classified retrieval Tier**: II (associative)
**推論経路**: 「β-H tolerance の機構検証」→「Ni-alkyl reductive elimination 系」→「Whitesides 1972 + 1970s 系列」。Ni-alkyl の機構研究は organometallic textbook（Hartwig 2010）に集約されている記憶。
**DB-findability**: yes
**Bibliographic confidence**: Medium

---

### EP-07a [Boundary-test pack]（第一群）

* **充填するRI**: RI-07 [Unsupported boundary], RI-09（二次）
* **充填開始点**: C_sp³ 制約の打破は cross-coupling 史の中心テーマ。Kumada group 自身も Hayashi 等で C_sp³ Grignard を扱う。Knochel 系列の organozinc 1990s で C_sp³ 拡張。決定的な Ni-secondary-alkyl coupling は Fu group: Zhou, J.; Fu, G. C. *J. Am. Chem. Soc.* **2003**, *125*, 14726 系列。
* **充填確立点**: Fu group 系列（2003–2010 多数）— Ni 触媒で secondary alkyl halide cross-coupling を Negishi 経由で達成。これにより「Only C_sp² halides」の境界主張が決定的に否定される。
* **充填の性質**: Paradigm-shift — Csp³ 制約の打破は Ni 触媒設計の新パラダイム（radical Ni, single-electron transfer cycle）を伴う。原論文の枠組みでは Csp³ は不可能だったが、新パラダイムにより可能になった。
* **Bibliographic confidence**: High — Fu group の Ni-secondary-alkyl coupling は organometallic chemistry の well-established milestone。
* **Filling adequacy confidence**: High — 境界主張への直接反例として機能。
* **Verification recommendation**: 推奨（Fu group は author network 中規模、年代 2003 以降）
* **Bibliographic verification status**: pending
* **DOI / URL**: Zhou-Fu 2003 JACS は DOI 検索可能。
* **Filling timescale category**: technical-barrier (30+ yr) — radical Ni 機構の理解と新規 ligand 設計が必要だった。
* **注記**: 原論文 1972 → Fu 2003 で **31 年遅延**。長期遅延充填の典型例。

**Self-classified retrieval Tier**: I–II
**推論経路**: 「C_sp³ cross-coupling」→「Fu group」が即座に浮かぶ（Tier I）。Knochel zinc は 2 段階目の連想（Tier II）。
**DB-findability**: yes
**Bibliographic confidence**: High（Fu 2003 は確実）

---

### EP-08a [Replication / uncertainty pack]（第三群）

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: 該当なし — インセンティブ構造的未充填。
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: 省略可
* **Bibliographic verification status**: N/A
* **Filling timescale category**: non-applicable
* **注記**: 合成化学分野では、特定論文の Table I の 10 エントリ全てに n=3 複製と SD を提供する独立論文は出版インセンティブが存在しない。Full Paper（Tamao 1976）でも標準的に SD 表は含まれない。「インセンティブ構造的未充填」として §E に詳述。
  ```yaml
  incentive_structure_type: "incentive-misaligned"
  filling_substitute: [REDACTED: substantial verbatim quotation; see Tier 9]
  ```

**Self-classified retrieval Tier**: N/A（充填候補なし）
**推論経路**: 合成化学の出版慣行に対する meta-knowledge から第三群と判定。
**DB-findability**: no
**Bibliographic confidence**: N/A

---

### EP-09a [Internal benchmark pack]（第二群）

* **充填するRI**: RI-09 [External superiority], RI-06（二次）
* **充填開始点**: 部分充填: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969（Full Paper）— Ni(acac)₂ vs NiCl₂(L₂) の対比は Full Paper で言及される可能性あり（要 verification）。
* **充填確立点**: Modern Ni cross-coupling textbook（Hartwig, *Organotransition Metal Chemistry*, 2010）で Ni 触媒前駆体の比較表として総括される。
* **充填の性質**: Partial — Corriu-Masse Ni(acac)₂ vs NiCl₂(dpe) の direct head-to-head は textbook level で総括されるが、原論文の同基質ペアでの直接実験対比は限定的。
* **Bibliographic confidence**: Low — Tamao 1976 内での Ni(acac)₂ 記載の有無は記憶曖昧。
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 必須（1976 論文 + Bibliographic Low）
* **Bibliographic verification status**: pending
* **DOI / URL**: 未確認
* **Filling timescale category**: incentive-aligned (variable)
* **注記**: CLA-1（タイトル "phosphine" 要件の検証）に直結する重要 EP だが、direct head-to-head の独立論文は recall に至らない。

**Self-classified retrieval Tier**: III (triangulation)
**推論経路**: 「Ni(acac)₂ vs NiCl₂(dpe) direct comparison」→「Tamao 1976 Full Paper で扱われたか」→「organometallic textbook で benchmarking されたか」と triangulate するも独立論文として recall に至らず。
**DB-findability**: uncertain
**Bibliographic confidence**: Low

---

### EP-10a [Kinetic verification pack]（第二群、暫定）

* **充填するRI**: PRI-11 [Mechanism-kinetics decoupling], RI-03（二次）
* **充填開始点**: Yamamoto group 1970s-80s の Ni(II)/Ni(0) 系運動論研究、または近年の Vicic / Hu group の Ni 触媒運動論研究（2010s）。
* **充填確立点**: Diccianni, J. B.; Diao, T. *Trends Chem.* **2019**, *1*, 830 等の modern Ni-coupling mechanism review が間接代替（review なので EP 充填ではないが、本格的な独立論文への索引として機能）。Vicic group の Ni(I)/Ni(III) 詳細運動論。
* **充填の性質**: Indirect / Partial — NiCl₂(dpe) + Grignard 直接系の v = k[Ni]^a[RMgX']^b[ArCl]^c は historic に手薄。Pd 系の運動論は豊富だが Ni 系は近年（2010s+）まで限定的。
* **Bibliographic confidence**: Low — 個別論文の特定は困難。
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 推奨（modern Ni mechanism は author network が広く特定論文の hallucination リスク中程度）
* **Bibliographic verification status**: pending
* **DOI / URL**: 未確認
* **Filling timescale category**: technical-barrier (40+ yr) — modern Ni-radical 機構の理解と運動論ツールの整備が必要だった。
* **注記**: 1972 → 2010s+ の長期遅延。Pd / Ni の機構的非対称な発展を反映。

**Self-classified retrieval Tier**: III (deep)
**推論経路**: 「Ni cross-coupling 運動論」→「historic に Pd 偏重の機構研究」→「modern Ni-radical の Vicic / Diao group」と triangulate。
**DB-findability**: yes（modern Ni catalysis review で entry point 確保可能）
**Bibliographic confidence**: Low

---

### §B 末尾チェック：Bibliographic verification（v18.3 conditional triggering）

**トリガー条件評価**:
- (a) 1980 年以前: ✓（EP-01a, EP-02a, EP-03a, EP-04a, EP-06a, EP-09a）
- (b) 著者ネットワーク密: ✓（Tamao-Kumada group は 10+ 関連論文 確実）
- (c) 反応名 = author name: ✓（Kumada coupling）
- (d) Bibliographic Medium-Low が 2 件以上: ✓（EP-01a Medium, EP-02a Medium, EP-03a Low, EP-04a Low, EP-05a Low, EP-09a Low, EP-10a Low）

**結論**: 全候補で **必須** verification。`Bibliographic verification status: pending` を全エントリに付与済み。

**Hallucination 警告**:
- Tamao 1976 Full Paper の author list（Tamao-Sumitani-Kiso-Zembayashi-Fujioka-Kodama-Nakajima-Minato-Kumada）は author 順序・スペルの完全一致を Crossref で要検証。dev/kumada の Sonnet が "Tamao-Sumitani-Hayashi-Kumada" と捏造した既知 pattern と類似のリスクあり。
- Yamamoto group の特定論文（Kohara-Yamamoto-Yamamoto 1980 *J. Organomet. Chem.* 192, 265）は記憶 fragmentary、強く verification 推奨。
- Whitesides 1972 JACS 94, 5258 は記憶しているが page 番号は推測。
- Fu group 2003 *J. Am. Chem. Soc.* 125, 14726 は比較的高 confidence だが要確認。

---

## §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-09a (partial) | VQ-2 | 1976 | Medium | High | ⚠️ 必須 (pending) |
| 2 | Whitesides, Gaasch, Stedronsky, *J. Am. Chem. Soc.* 1972, 94, 5258 系列 | EP-06a (indirect) | VQ-3 | 1972 | Medium | Medium | ⚠️ 必須 (pending) |
| 3 | Kohara, Yamamoto, Yamamoto, *J. Organomet. Chem.* 1980, 192, 265 前後 | EP-03a (indirect) | VQ-3 | 1980 | Low | Medium | ⚠️ 必須 (pending) |
| 4 | Hayashi, Konishi, Kumada 系列, *J. Org. Chem.* / *J. Am. Chem. Soc.* 1980s | EP-05a (partial), EP-07a (partial) | VQ-2 / VQ-3 | 1980s | Low | Medium | ⚠️ 必須 (pending) |
| 5 | Zhou, Fu, *J. Am. Chem. Soc.* 2003, 125, 14726 系列 | EP-07a (paradigm-shift) | VQ-2 / VQ-3 | 2003 | High | High | ⚠️ 推奨 (pending) |
| 6 | Smith, Kochi, *J. Organomet. Chem.* 1976 + Kochi *Organometallic Mechanisms and Catalysis* 1978 | EP-04a (indirect) | VQ-3 | 1976–78 | Low | Low | ⚠️ 必須 (pending) |
| 7 | Diccianni, Diao, *Trends Chem.* 2019, 1, 830 系列（review entry point） | EP-10a (partial proxy) | VQ-3 | 2019 | Medium | Low | 推奨 (pending) |

**選定理由**:

1. **Tamao 1976 Full Paper** は Communication → Full Paper auto-resolution（C23）の中核論文として VQ-2 modern 要件を 4 年で充填。EP-01a / EP-02a / 部分的に EP-09a の bundle filling。
2. **Whitesides 1972 系列** は β-H elimination 機構の field-methodology 充填として EP-06a を間接充填。
3. **Yamamoto group 1980 前後** は Ni(II)-organyl 中間体の単離・分光研究として EP-03a を間接充填。
4. **Hayashi-Kumada 1980s** は author group self-extension として EP-05a の配位子順位定量基盤と EP-07a の C_sp³ 拡張の萌芽を提供。
5. **Fu 2003** は EP-07a の paradigm-shift 充填として境界主張を決定的に否定。**31 年遅延**の典型例。
6. **Smith-Kochi / Kochi 1978** は radical 機構の枠組みとして EP-04a の間接代替。直接充填は依然 **未同定**。
7. **Diccianni-Diao 2019** は modern Ni-radical 運動論研究への entry point。EP-10a は **長期遅延・proxy 充填**。

**バンドル充填の効率性**: 順序 1 の Tamao 1976 が EP-01a + EP-02a + EP-09a (partial) を bundle covering（VQ-2 modern 要件の核心）。順序 5 の Fu 2003 が EP-07a を paradigm-shift で覆う。残りの mechanism EP は分散充填（Whitesides, Yamamoto, Kochi が個別に partial 充填）。

**Verification 待機エントリの注記**: 全候補で post-hoc Crossref verification が必要。順序 1（Tamao 1976）の author 順序・スペルは特に重要（dev/kumada cross-vendor verification で Sonnet が Hayashi 捏造を起こした既知 pattern）。順序 3（Kohara-Yamamoto-Yamamoto 1980）は最も hallucination リスクが高い（Bibliographic Low）。

---

## §D VQ階層と充填時間順序の対応分析

**充填の時間軸**:

- VQ-2 (modern) 要件: EP-01a → 1976 (Tamao) [自己充填、format-driven]
- VQ-2 (modern) 要件: EP-02a → 1976 (Tamao) [自己充填、format-driven]
- VQ-3 要件: EP-06a → 1972+ (Whitesides 系列) [field-methodology, 同時期]
- VQ-3 要件: EP-03a → 1980 前後 (Yamamoto group) [field-methodology, 8 年]
- VQ-2 / VQ-3 要件: EP-05a → 1980s (Hayashi-Kumada) [自己充填、10+ yr]
- VQ-3 要件: EP-04a → **未同定**（Kochi 1978 が間接代替）
- VQ-2 (boundary) 要件: EP-07a → 2003 (Fu) [paradigm-shift、31 yr 長期遅延]
- VQ-4 要件: EP-09a → 1976 partial + textbook 集約 [partial、自己充填]
- VQ-3 要件: EP-10a → 2010s (Vicic/Diao) [technical-barrier、40+ yr]
- VQ-4 要件: EP-08a → **未充填**（インセンティブ構造的未充填）

**階層-時間対応の評価**:

仮説「VQ階層が上がるほど充填時間が長くなる」は本ケースで **部分的に支持**される。VQ-2 modern 要件（EP-01a, EP-02a）は format-driven auto-resolution で 4 年内に充填されたが、VQ-3 要件は EP-03a / EP-06a が 1970s 末–1980s（同時期 8 年）、EP-04a が間接代替のみ、EP-10a が 40+ 年と幅広い。VQ-2 の境界主張（EP-07a）は **paradigm-shift により逆に長期遅延**（31 年）した点が反例。VQ-4 要件（EP-08a）はインセンティブ構造的未充填で「VQ が下がるほど未充填化する」逆転 pattern も観察される。これは「科学的論理に基づく EP 充填順序（低 VQ → 高 VQ）」と「出版インセンティブに基づく実際の充填順序」の **不整合**を示す。

**特筆すべきパターン**:

1. **自己充填**: Tamao 1976 (Full Paper) と Hayashi-Kumada 1980s が author group self-extension として EP-01a / EP-02a / EP-05a / EP-07a (partial) を bundle 自己充填。Communication → Full Paper auto-resolution の典型。
2. **長期遅延充填（31 yr）**: Fu 2003 による EP-07a 充填は radical Ni 機構の理解と新規配位子設計（terpyridine 系等）を伴う paradigm-shift 充填。1972 当時の枠組みでは原理的に到達不能。
3. **超長期遅延（40+ yr）**: EP-10a の運動論検証は modern Ni-radical 機構研究（2010s+）まで本格化せず、Pd / Ni 機構研究の historical 非対称（Pd 偏重）を反映。
4. **インセンティブ構造的未充填**: EP-08a は技術的に充填可能だが、合成化学の出版インセンティブ構造で独立論文化されない。
5. **直接充填の不在**: EP-04a (cis/trans-dichloroethylene scramble 機構) は 54 年経過後も直接充填が **未同定**。Kochi の枠組み輸入による間接充填のみ。

**著者回顧との照合**: Tamao 2002 retrospective mini-review（papers/ep/discussion/tamao2002/）が Kumada 系列の自己語りを提供しており、Stage 3 の EP リストとの照合で「分野内部者には不可視の構造的不在」の直接的証拠となりうる（要 Stage 4 別 run での詳細照合）。

---

## §E 未充填EPの発見的意義

**未充填EP一覧**:

### EP-04a [Discrimination / replication pack] — 直接充填未同定

* **未充填の理由**:
  - 関心の欠如：1,2-dichloroethylene + Grignard + Ni-phosphine の cis/trans scramble は、後続の Pd 主導 cross-coupling 時代では測定対象として retire された。基質として dichloroethylene を採用する研究者層が縮小。
  - 機構的関心は radical Ni 文脈で 2010s に再浮上したが、Kumada 1972 の特定基質（dichloroethylene）への直接回帰は起こっていない。
* **発見的意義**: あり。「分野が 54 年にわたって体系的に避けてきた問い」の典型。cis-stilbene 偏向への合成的有用性ラッピング（feature 4）が機構的検証の動機を吸収した社会的な「success-driven question erasure」の萌芽。
* **将来の充填可能性**: 中。modern radical Ni 機構研究（Vicic group）で原理的には充填可能だが、historic interest が薄いため独立論文化のインセンティブは弱い。

### EP-08a [Replication / uncertainty pack] — インセンティブ構造的未充填

* **未充填の理由**:
  - **インセンティブ構造の不整合**：Table I の n=3 反復測定と SD 表は、合成化学の出版慣行（新規性要求）の下で独立論文化されない。Full Paper（Tamao 1976）でも標準的に SD 表は含まれない。
  - 部分代替：Pharmaceutical industry の process chemistry スケールアップ報告（Kumada coupling industrial implementation reports, Negishi review 等）で実用的信頼性は集約されるが、原論文 Table I 直接の充填ではない。
* **発見的意義**: あり。「分野の出版インセンティブが UQS の構造的不在の一部を維持している」ことの典型例。VQ-4 要件（VQ 階層の最上位）が **VQ-2 modern より長期に未充填**であるという VQ 階層逆転の典型。
* **将来の充填可能性**: 低。出版インセンティブ構造が変わらない限り、独立論文化されない。

### EP-09a [Internal benchmark pack] — Direct head-to-head 未同定

* **未充填の理由**:
  - Tamao 1976 Full Paper での Ni(acac)₂ vs NiCl₂(dpe) head-to-head 比較の詳細記載は要 verification（Bibliographic Low）。Modern textbook（Hartwig 2010）で集約されるが原論文の同基質ペアでの直接実験対比は限定的。
  - 関心の欠如：1980s 以降は Pd 触媒主導となり、Ni 触媒前駆体の比較研究自体が縮小。
* **発見的意義**: あり。CLA-1（タイトル "Nickel-Phosphine Complexes" の "phosphine" 要件検証）に直結する重要 EP が、historic に正面から検証されないまま「phosphine 必要」の暗黙了解が業界標準化した。
* **将来の充填可能性**: 中。Modern Ni catalysis 文脈で再検討する研究グループが現れる可能性あり。

### EP-10a [Kinetic verification pack] — 部分充填のみ（40+ yr 遅延）

* **未充填の理由（部分充填の限界）**:
  - **Technical barrier**: NiCl₂(dpe) + Grignard 系の運動論測定は historic に Pd 系より遅れた。Modern Ni-radical 機構研究（2010s+）は新パラダイムでの運動論を扱うため、原論文の Ni(II)/Ni(0) サイクル想定での運動論検証とは枠組みが異なる。
* **発見的意義**: あり。「mechanism-kinetics decoupling（PRI-11）」が 40+ 年保持された典型例。
* **将来の充填可能性**: 中–高。modern Ni catalysis の運動論ツールで原理的に充填可能。

---

## §F 考慮し棄却した候補（rejection log）

retrieval 段階で考慮したが充填候補から棄却した論文を、棄却理由とともに明示記録する。

| 候補 | 棄却理由 |
|---|---|
| Negishi, *J. Am. Chem. Soc.* 1977（Negishi coupling 初出） | 別パラダイム（organozinc）。Kumada 1972 の EP を充填するというより並走系。「同じ問いへの異なる解」だが本プロンプトでは EP 充填と認めない。 |
| Suzuki, *Tetrahedron Lett.* 1979（Suzuki coupling 初出） | 別パラダイム（organoboron）。同上。 |
| Stille, *J. Am. Chem. Soc.* 1978 系列 | 別パラダイム（organotin）。同上。 |
| Heck, *J. Am. Chem. Soc.* 1968-1972 系列 | 機構が異なる（migratory insertion）。Kumada cycle の EP を充填しない。 |
| Tsuji-Trost π-allyl Pd 系列 | 機構が異なる。Kumada cycle に対応しない。 |
| de Meijere & Diederich, *Metal-Catalyzed Cross-Coupling Reactions*（Wiley, 2004）レビュー | レビュー論文は EP 充填と認めない（プロンプト規則）。entry point として有用だが選定リストには含めない。 |
| Hartwig, *Organotransition Metal Chemistry*（University Science Books, 2010）教科書 | 教科書は EP 充填と認めない。同上、entry point として有用。 |
| Knochel zinc reagents 1990s 系列 | EP-07a 候補だが Fu 2003 が paradigm-shift 充填として優先。Knochel zinc は organozinc paradigm の系列であり Negishi 系の延長として位置付ける方が適切。 |
| Vicic group Ni(I)/Ni(III) 機構研究 2010s 系列 | EP-10a の partial proxy として §C 順序 7 (Diccianni-Diao 2019 review) に集約。直接論文の bibliographic recall が低 confidence のため個別エントリ化を回避。 |
| Tamao 2002 retrospective mini-review（papers/ep/discussion/tamao2002/） | レビュー / retrospective は EP 充填と認めないが、§D の「著者回顧との照合」の二次資料として参照価値あり。 |
| Corriu & Masse, *Chem. Commun.* 144 (1972) | 並行発表（C-01）。EP-09a 候補としては Tamao 1976 内での比較記載に依存するため独立充填ではない。 |

---

## §G Retrieval Depth Annotation Matrix

各 §C 推奨選定リスト候補（および §B 主要候補）について、Tier / 推論経路 / DB-findability / Bib confidence を集約する。

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Tamao et al. 1976 *Bull Chem Soc Jpn* 49, 1958 | EP-01a, EP-02a, EP-09a (partial) | I | C23 prompt + Kumada Full Paper の organometallic 教科書知識から即座 | yes | Medium |
| Whitesides-Gaasch-Stedronsky 1972 *J Am Chem Soc* 94, 5258 | EP-06a (indirect) | II | β-H elimination 機構研究 → Whitesides MIT 1970s 系列の連想 | yes | Medium |
| Kohara-Yamamoto-Yamamoto 1980 *J Organomet Chem* 192, 265 前後 | EP-03a (indirect) | II | Ni-phosphine 中間体研究 → Akira Yamamoto group 1970s-80s 連想 | yes | Low |
| Hayashi-Konishi-Kumada 系列 1980s | EP-05a (partial), EP-07a (partial) | II | Kumada group 自己拡張 → 不斉 Ni-coupling Hayashi 系列の連想 | yes | Low |
| Zhou-Fu 2003 *J Am Chem Soc* 125, 14726 | EP-07a (paradigm-shift) | I | C_sp³ Ni cross-coupling の milestone として即座 | yes | High |
| Smith-Kochi 1976 *J Organomet Chem* + Kochi 1978 単行本 | EP-04a (indirect) | III | radical 機構枠組み → Kochi 1970s 著作の triangulation | uncertain | Low |
| Diccianni-Diao 2019 *Trends Chem* 1, 830 系列（review entry） | EP-10a (proxy) | III | modern Ni-radical 機構研究 → review level entry の triangulation | yes | Medium |
| Yamamoto-Yamamoto-Ikeda 1971 *J Am Chem Soc* 93, 3350 系列 | EP-03a (indirect, alt) | II | refs 11-12 の precedent group 想起から Yamamoto 連想 | yes | Low |
| Corriu & Masse 1972 *Chem Commun* 144 | (already in paper as ref 3a) | I | 論文内引用、再 retrieval 不要 | yes | High |

**Retrieval pattern 観察**:

- **Tier I**（即座想起、3 件）: Tamao 1976 / Fu 2003 / Corriu-Masse 1972。Communication → Full Paper auto-resolution の核心 + cross-coupling 史の milestone + 論文内既知引用。
- **Tier II**（連想 2-3 段、4 件）: Whitesides 1972 / Yamamoto group 1980 / Hayashi-Kumada 1980s / Yamamoto 1971。author group / 機構 keyword の連想で surface。
- **Tier III**（triangulation、2 件）: Kochi-Smith 1976 / Diccianni-Diao 2019。複数候補の triangulation を経て surface、bibliographic recall が低 confidence。
- **DB-findability uncertain**: 1 件のみ（EP-04a 直接系）。
- **Bib confidence High**: 2 件のみ（Fu 2003 + Corriu-Masse 1972）。Medium 3 件、Low 4 件。1980 年以前の Communication / Full Paper（特に Bull Chem Soc Jpn 系列）と Yamamoto group 関連は強く verification 必須。

**Multi-run robustness expectation**:
本 run は Opus 4.7 v6 prompt 下の retrieval pattern の baseline。Sonnet v6 multi-run（dev/kumada Sonnet pilot 1）と GPT-5.4 v6 multi-run の比較で、Tier I 候補（Tamao 1976 / Fu 2003）の cross-vendor 一致率と Tier III 候補（Kochi-Smith / Diccianni-Diao）の divergence 率が rotational stability の指標となる。

---

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
