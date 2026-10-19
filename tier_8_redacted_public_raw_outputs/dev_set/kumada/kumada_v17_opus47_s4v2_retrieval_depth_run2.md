```
prompt_version: stage4-v2-20260416
model_info: claude-opus-4-7
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Opus 4.7 v2 run 2)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot 2)
related_baseline_opus: papers/dev/kumada/kumada_v17_opus47_s4v2.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v2 multi-run と GPT-5.4 v2 multi-run と
      比較して Opus 4.7 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

# EP充填選定マップ — Tamao, Sumitani, Kumada 1972 (JACS Communication)

## 0. Externalization preface — retrieval-process narration

このセクションは出力規律の §A〜§E に追加された **本実験 variant 固有の preface** である。
通常の Stage 4 v2 出力では省略される思考過程を明示的に externalize する。

### 0.1 First-wave associations（最初に思い浮かんだ候補）

EP リストを読んだ瞬間、Tier I として以下が即座に想起された：

1. **Tamao et al. BCSJ 1976 (Full Paper)** — Stage 3 §6 (vi) にも明示されている、
   1972 通信の Full Paper 拡張版。Communications → Full Paper の自動解消パターンの
   標準ケース。EP-01a, EP-02a, EP-05a, EP-08a を bundle で充填する候補として最初に
   confidence High で立ち上がった。

2. **Corriu-Masse Chem. Commun. 1972 (page 144)** — 論文自身の Note Added in Proof で
   引用されている同時期発表論文。Ni(acac)₂ vs NiCl₂(dpe) の対照をなす存在として
   EP-09a / CLA-1 の "比較対象側" の候補として即座に想起。ただし Corriu-Masse 自身も
   1972 communication なので「比較を提供する」というよりは「比較対象を提供する」位置。

3. **Kochi group の radical-clock 系列研究** — 1970s 後半。Tamura & Kochi（既に
   refs 5, 6 として論文に引用）の延長線上で、Ni 触媒下の RX + RMgX' 反応における
   ラジカル機構の直接 probe を行った系列。Tsou & Kochi 1979 が代表として浮かぶが
   exact citation には自信が medium。EP-04a の充填候補。

4. **Akio Yamamoto group の organonickel 中間体単離研究** — 1970 年代の Ni(II) ジオルガニル
   錯体の単離・構造解析研究。eq 1 の (dipy)Ni(Et)₂ + PhCl 系の precedent に直接連なる
   仕事。EP-03a の充填候補（中間体の物質としての実在を確立）。Confidence: medium で
   1973-1975 の時期に JACS または J. Organomet. Chem. に出版された記憶があるが
   exact citation には自信なし。

### 0.2 Second-wave associations（2-3 段階の連想で surface した候補）

5. **Negishi-King-Okukado JACS 1977** — Pd/Ni 触媒下のアリール-アリール cross-coupling。
   Kumada coupling の延長として organozinc に拡張された方法論論文。EP-07a (boundary)
   と EP-09a (benchmark) の双方に間接的に関連。Confidence: high（Negishi 1977 の存在は
   確実）だが EP 充填への対応は推論を含む。

6. **Yamamoto-Yamamoto-Ikeda 系列（1971-1973）** — refs 11 で言及されている Uchino,
   Yamamoto, Ikeda 1970 の延長線。L₂NiR₂ → L₂Ni(R)(X) 変換の直接観測、そして
   homocoupling vs cross coupling 選択性の議論を含む可能性。U-01 / U-04 の自己矛盾的
   不在に直接対応する候補。Confidence: medium-low（具体的な citation には自信なし）。

7. **Tamao Kumada 1980 年代の β-H tolerance / sp³ 拡張研究** — 1972 年以降、Kumada/Tamao
   グループは sp³ 基質や β-H Grignard への拡張を継続的に発表。EP-06a / EP-07a の
   充填候補だが、具体的な citation の信頼度は低い。

### 0.3 Third-wave associations（triangulation で surface した候補）

8. **Vicic group の Ni(I)/Ni(III) 触媒サイクル研究（2000 年代）** — alkyl 系での Ni 触媒
   cross-coupling の機構解明。Kumada 1972 の C_sp³ 排除 (B-05) の境界を打ち破った系列。
   Anderson & Vicic Organometallics 2004 として記憶しているが、年と巻号には自信なし。
   EP-07a (sp³ boundary) のパラダイム転換型充填候補。

9. **Greg Fu group の stereoconvergent Ni 触媒（2000s-2010s）** — alkyl halides の Ni 触媒
   cross-coupling での radical pathway の確立。Kumada 1972 の cis/trans scramble 観察
   (A-04, A-14) との機構的繋がりを retrospectively 提供する候補。Confidence: medium
   for general existence, low for specific 1-2 報の特定。

10. **Hu group / Knochel group の現代的拡張** — sp³-sp³ cross coupling や C-H activation
    との統合。Confidence: low for specific citations.

11. **Diccianni & Diao Trends Chem. 2019** — Ni 触媒機構レビュー。Reviews は EP を充填
    しないが、二次情報源として認識。Confidence: medium for existence.

### 0.4 Considered-and-rejected 候補

- **Hartwig group の Pd 触媒研究** — Pd 系であり、Ni 系の Kumada 1972 への直接充填では
  ない。Reject。
- **Suzuki-Miyaura 1979** — B-based であり Kumada 1972 の機構を直接検証する充填では
  ないため reject。Negishi 1977 と並んで cross-coupling family の拡張として brief mention
  に留める。
- **Sonogashira 1975** — Pd-Cu 系で alkynyl-aryl 結合形成、Kumada 系の機構には直接対応
  しない。Reject。
- **Stille 1978 (Sn-based)** — Pd 系であり direct filling には該当しない。Reject。
- **Hiyama 1988 (Si-based)** — Pd 系であり direct filling には該当しない。Reject。
- **Wilkinson catalyst 系列研究** — Rh/H₂ であり Ni-Grignard 系ではない。Reject。

### 0.5 Honesty disclosure

本 retrieval は LLM の internal knowledge のみによる。文献データベースへの実時間照会は
行っていない。各候補の「Bibliographic confidence」フィールドは、私自身が「この citation を
論文を読んだことのない well-read colleague に提示した時、彼らが容易に検証できるか」
という視点で評価した。Low と記載した候補は、実際の文献確認なしには引用すべきでない。

各候補の「Self-classified retrieval Tier」は以下の私的定義による：
- **Tier I (immediate)**: EP description を読んだ瞬間（数秒以内）に想起された候補。
- **Tier II (associative)**: EP の case-specific 実装を読み解く 2-3 ステップの連想で
  surface した候補。
- **Tier III (deep)**: 複数の candidate 群を triangulate して、「このパターンに該当する
  論文があるはず」という構造的推論を経て同定した候補。

---

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-05a, EP-06a, EP-07a, EP-09a, EP-10a
  — EP-03a (RI-03 中間体観測): Ni-phosphine 中間体の分光・単離は独立論文の主題として典型的。
  — EP-04a (RI-04 立体機構 probe): radical clock や stereochem 系列研究は単独論文として確立。
  — EP-05a (RI-05 配位子定量比較): ligand-screen 論文は方法論論文として独立しうる。
  — EP-06a (RI-03/RI-06 β-H 機構): 同位体ラベル研究は独立論文として典型的。
  — EP-07a (RI-07 sp³ 境界): sp³ Ni 触媒 cross-coupling は 2000 年代に独立分野化。
  — EP-09a (RI-09 触媒系比較): Ni(acac)₂ vs Ni-phosphine の対照実験を含む論文が存在する。
  — EP-10a (PRI-11 速度式): 速度論研究は独立論文として典型的。

**第二群（間接的に追跡可能）：** EP-01a, EP-02a
  — EP-01a (RI-01 報告整合性): per-entry 条件開示は通常 Full Paper 展開で吸収される。
    独立論文の主題ではないが、Tamao et al. BCSJ 1976 の Full Paper で吸収される類型。
  — EP-02a (RI-02 同定): 燃焼分析・HR-MS の補完は Full Paper で吸収される類型。

**第三群（充填が見つからない可能性あり）：** EP-08a
  — EP-08a (RI-08 反復・不確かさ): 1972 年代の触媒系の Table I を再現複製した独立論文は
    出版されにくい（既存系の追試は新規性ハードルを越えない）。インセンティブ構造の
    不整合により未充填の典型候補。

---

## §B 各EPの充填論文候補

### EP-03a [Direct-observation / state-assignment pack]（第一群）

* **充填するRI**: RI-03 [Unobserved explanatory], RI-02 [Object identification], RI-06 [Imported model]
* **充填開始点**: Yamamoto et al., JACS or J. Organomet. Chem. ~1973-1974 — diphosphine-Ni(II)
  ジオルガニル錯体の単離と熱分解挙動の研究で、L₂NiR₂ 中間体の物質としての実在を確立。
* **充填確立点**: Anderson & Vicic, Organometallics 2004 (uncertain volume/page) — Ni(I) 中間体
  の直接観測を含む現代的研究。Kumada 1972 の触媒サイクルを Ni(II)/Ni(IV) ではなく
  Ni(I)/Ni(III) に再帰属する流れの起点。
* **充填の性質**: Partial（NiCl₂(dpe) + Grignard + ArCl 系そのものでの中間体観測は
  なお限定的だが、類似系での観測により mechanism class は確立）
* **Confidence**: Medium for existence of class of work; Low for specific citation
* **注記**: Tamao et al. BCSJ 1976 Full Paper も部分的に EP-03a を進めている可能性が高いが
  紙幅の中心は scope 拡張にあり、中間体観測は副次的扱いと記憶している。
* **Self-classified retrieval Tier**: Tier I for general-Yamamoto-class associations; Tier III
  for Vicic 系列の triangulation。
* **推論経路**: Stage 3 §2 SRG-2 の "中間体 1, 2, 3 の直接観測" → Yamamoto 群の organonickel
  化学（refs 11 経路）→ 後年の Vicic / Diao 系列。
* **DB-findability**: yes (Yamamoto 系列), uncertain (Anderson-Vicic 2004 の正確な citation)
* **Bibliographic confidence**: Low — Verify against Web of Science / SciFinder before
  manuscript citation.
* **Verification recommendation**: Yamamoto group の 1973-1975 organonickel papers を
  系統的に検索し、L₂NiR₂ + R'X → L₂Ni(R')(X) + R-R 反応を直接観測した論文を 2-3 報
  特定する必要がある。

### EP-10a [Kinetic verification pack]（第一群）

* **充填するRI**: PRI-11 [Mechanism-kinetics decoupling], RI-03 (副次)
* **充填開始点**: Tsou & Kochi, JACS 1979 (uncertain exact volume/page; recall as ~101, 7547) —
  Ni 触媒 R-X + R'M cross-coupling における初期速度法とラジカル diagnostic を組み合わせ、
  速度則と機構を結合させた系列。
* **充填確立点**: 同上系列の延長 + Vicic 群の現代的速度論。
* **充填の性質**: Partial（NiCl₂(dpe) + Grignard 系特異的な kinetic study はなお限定的）
* **Confidence**: Medium for Tsou-Kochi general work; Low for specific 1979 citation
* **注記**: Kochi 自身が refs 5, 6 として論文に既に引用されているため、Kumada-Kochi
  系列の continuity は強い。
* **Self-classified retrieval Tier**: Tier II — Tamura-Kochi 1971 から Kochi グループの
  radical mechanism 研究系列への 2-step 連想。
* **推論経路**: Stage 3 §2 SRG-2 / CLA-2 の速度論不在 → Kochi グループの Ni 触媒機構研究
  → Tsou & Kochi 1979 系列。
* **DB-findability**: yes (Kochi の Ni mechanism 研究は ChemRxiv / Web of Science で容易に検索可能)
* **Bibliographic confidence**: Medium — author + 系列 high; exact citation low.
* **Verification recommendation**: "Tsou Kochi nickel cross coupling kinetics" で SciFinder
  検索。Volume 101 vs 102, 1979 vs 1980 の確認が必要。

### EP-04a [Discrimination / replication pack]（第一群）

* **充填するRI**: RI-04 [Unreplicated discriminator], RI-01 (副次)
* **充填開始点**: Tamura & Kochi, JACS 1971 (既に refs 5 として論文に引用) — Fe 触媒 Grignard
  カップリングのラジカル機構研究で Ni 系への先例。
* **充填確立点**: Tsou & Kochi 1979 系列 + Fu group の現代的 stereoconvergent Ni 触媒研究
  (2000s-2010s)。
* **充填の性質**: Partial → Indirect（1,2-dichloroethylene 系での cis:trans scramble の
  時間発展研究は限定的。類似 vinyl halide 系での radical probe は確立）
* **Confidence**: Medium for general radical-mechanism work in Ni cross coupling
* **注記**: Stage 3 §2 SRG-3 の "ラジカル vs σ-vinyl-Ni 回転 vs post-coupling isomerization"
  の三経路分離は、Kumada の cis-stilbene 系では direct fill が見当たらない。Negishi/Suzuki
  系での後続研究が間接的に類似 question に回答している。
* **Self-classified retrieval Tier**: Tier I (Kochi associations) + Tier III (Fu group
  triangulation)。
* **推論経路**: Stage 3 §2 SRG-3 → Tamura-Kochi 1971 既存引用 → Kochi 系列 → 現代の
  stereoconvergent Ni 触媒。
* **DB-findability**: yes for Tamura-Kochi (refs 5, 6); medium for Fu group sp³ coupling.
* **Bibliographic confidence**: Medium for systems-level knowledge; Low for specific citations
  filling Kumada's 1,2-dichloroethylene observation.
* **Verification recommendation**: 1,2-dihaloalkene の Ni 触媒 cross-coupling での
  時間発展 stereochem 研究は実は limited literature の領域。Possibly never explicitly filled.

### EP-01a [Reporting-coherence pack]（第二群）

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato,
  Kumada, Bull. Chem. Soc. Jpn. 49, 1958 (1976) — 1972 通信の Full Paper 展開で per-entry
  条件・収率・分析法を完全開示。
* **充填確立点**: 同上
* **充填の性質**: Complete（Communications → Full Paper 自動解消の典型）
* **Confidence**: Medium-High（CLAUDE.md / Stage 3 §6 (vi) で言及されている。
  正確な volume 49, page 1958 の細部は要 verification）
* **注記**: Self-filling パターンの教科書例。Stage 3 §6 (vi) の予測通り。
* **Self-classified retrieval Tier**: Tier I — Stage 3 §6 (vi) で既に言及されており直接想起。
* **推論経路**: Stage 3 §6 (vi) の自動解消パターン → 当該 BCSJ 1976 paper.
* **DB-findability**: yes (BCSJ は完全に database 化されている)
* **Bibliographic confidence**: Medium — author 順序と volume/page は要 verification。
* **Verification recommendation**: BCSJ 1976 vol 49 で著者を Tamao, Kumada で検索して即時確認可能。

### EP-02a [Identity / purity substantiation pack]（第二群）

* **充填するRI**: RI-02 [Object identification]
* **充填開始点**: Tamao et al. BCSJ 1976 (同上) — Full Paper で各製品の燃焼分析・物理定数を
  完全開示。
* **充填確立点**: 同上
* **充填の性質**: Complete（Full Paper 展開で吸収）
* **Confidence**: Medium-High
* **注記**: EP-01a と bundle で BCSJ 1976 が一括充填する。
* **Self-classified retrieval Tier**: Tier I (bundle inference from EP-01a)
* **推論経路**: Same as EP-01a。
* **DB-findability**: yes
* **Bibliographic confidence**: Medium
* **Verification recommendation**: EP-01a と同時に確認。

### EP-08a [Replication / uncertainty pack]（第三群）

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: 未充填（インセンティブ構造の不整合）
* **Confidence**: N/A
* **注記**: Table I の 10 エントリの n=3 複製と SD を独立論文として出版する研究計画は
  新規性要件と整合しない。BCSJ 1976 Full Paper でも複製数の体系的開示は行われていない
  と推測される。これは UQS の §E で扱う「分野が体系的に避けてきた問い」の典型例。
* **Self-classified retrieval Tier**: N/A — no candidate surfaced.
* **推論経路**: 不在の同定。
* **DB-findability**: no — the absence is the finding.
* **Bibliographic confidence**: N/A
* **Verification recommendation**: 反復測定研究の不在を確認するには Tamao/Kumada/Murahashi
  系の Full Paper で SD/error bar 表示の有無を体系的に scan する必要がある。

### EP-09a [Internal benchmark pack]（第一群）

* **充填するRI**: RI-09 [External superiority], CLA-1 (Ni-phosphine vs Ni(acac)₂)
* **充填開始点**: Corriu & Masse, Chem. Commun. 144 (1972) — 論文自身の Note Added in Proof
  で言及される Ni(acac)₂ 系の同時期論文。直接の対照を提供。
* **充填確立点**: Kumada/Tamao group の後続 BCSJ 1976 Full Paper で部分比較がなされた可能性
  + 1980 年代の Ni 触媒 ligand effect 論文。Specific 1 報を特定できない。
* **充填の性質**: Partial（Corriu-Masse 1972 が対照系を提供するが、両者を head-to-head で
  比較した独立論文は限定的）
* **Confidence**: High for Corriu-Masse 1972 (cited in target paper); Low for explicit comparison studies.
* **注記**: 興味深いことに、Kumada と Corriu-Masse は同時期に独立に発見しており、
  互いの直接比較を行う論文は historiographic にも稀。Negishi の reviews などで
  retrospective に整理される。
* **Self-classified retrieval Tier**: Tier I for Corriu-Masse (already in target paper);
  Tier III for explicit comparison studies (which I cannot specifically identify).
* **推論経路**: Stage 3 §2 CLA-1 → Note Added in Proof → Corriu-Masse 1972.
* **DB-findability**: yes for Corriu-Masse 1972; uncertain for comparison papers.
* **Bibliographic confidence**: High for Corriu-Masse; Low for downstream comparisons.
* **Verification recommendation**: Corriu-Masse 1972 は target paper に明記されているので
  verification 不要。Comparison papers は要 SciFinder 検索。

### EP-07a [Boundary-test pack]（第一群）

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Kambe, Iwasaki, Terao 系列 (~2002 onwards in Chem. Soc. Rev. or JACS) —
  Ni 触媒 alkyl-alkyl cross-coupling で C_sp³ halide の使用を確立し、Kumada 1972 の
  "Only C_sp² halides" 境界を打ち破った系列。
* **充填確立点**: Vicic, Fu, Hu groups の 2000-2010s 系列 — sp³-sp³ cross-coupling の
  ラジカル機構解明と組み合わせて C_sp³ 境界を完全に打破。
* **充填の性質**: Paradigm-shift — EP の前提（"sp³ halides cannot be used"）が
  新しい配位子 / 機構（NHC, Ni(I)/Ni(III) cycle）の登場で反転した。EP が解消された
  というより、問いの枠組みが変わった。
* **Confidence**: Medium for general framework; Low for specific citations.
* **注記**: Stage 3 §2 SRG-9 の C_sp³ 境界主張は、30 年後に paradigm-shift filling を
  受けた典型例。1972 年の "only C_sp²" は当時の触媒系の限界であり、現代では誤りと判明。
* **Self-classified retrieval Tier**: Tier II (Kambe 系列) + Tier III (Fu/Vicic triangulation)
* **推論経路**: Stage 3 §2 SRG-9 → "Ni-catalyzed sp³ cross coupling" → Kambe / Fu / Vicic.
* **DB-findability**: yes (sp³ Ni cross-coupling は確立した分野)
* **Bibliographic confidence**: Medium for framework; Low for specific 1-2 報の特定.
* **Verification recommendation**: Phapale & Cárdenas Chem. Soc. Rev. 2009 (review, 充填には
  使えないが二次情報源) を出発点に Kambe / Fu / Vicic の representative papers を特定。

### EP-05a [Quantitative-ranking substantiation pack]（第一群）

* **充填するRI**: RI-05 [Qualitative overread], RI-08 (副次)
* **充填開始点**: 1980-2000s の Ni-phosphine ligand-screen 論文系列 — bite angle と活性の
  相関を体系化した研究 (Casey, van Leeuwen, Whiteker 系列)。
* **充填確立点**: van Leeuwen group の bite-angle 系列 + 現代の DOE-based ligand
  optimization 論文。
* **充填の性質**: Indirect（Pd-phosphine 系での充填が主流であり、Ni-phosphine 系での
  Kumada 1972 の dpp > dpe > dmpe 序列の体系的再現と説明はやや限定的）
* **Confidence**: Medium for bite-angle framework; Low for direct Kumada series filling.
* **注記**: Stage 3 §2 SRG-4 の dpp > dpe > dmpe 序列を bite angle で説明する研究は
  van Leeuwen 系列で確立。
* **Self-classified retrieval Tier**: Tier II — bite angle concept から van Leeuwen への連想。
* **推論経路**: SRG-4 dpp/dpe/dmpe 序列 → bite angle/electronic effect 分離 → van Leeuwen
  系列。
* **DB-findability**: yes (bite angle research は確立した分野)
* **Bibliographic confidence**: Medium for framework; Low for Kumada-specific filling.
* **Verification recommendation**: van Leeuwen Chem. Rev. ~2000 (reviews, 二次情報源としてのみ)
  + 元論文 (Casey 1992?, Whiteker 系列) を特定。

### EP-06a [Analogy-validation pack]（第一群）

* **充填するRI**: RI-03 [Unobserved explanatory] (β-H specific), RI-06 [Imported model]
* **充填開始点**: Yamamoto, Yamamoto, Ikeda 系列 (~1973-1974) — refs 11 系列の延長で
  L₂NiR₂ の β-H 脱離挙動を直接観測。
* **充填確立点**: 1980s の organonickel 化学 + Hartwig group の Pd 系での β-H 機構研究の
  Ni 系への拡張。
* **充填の性質**: Partial — β-D 標識 Grignard を使った Ni 触媒 cross-coupling の直接
  研究はなお限定的。
* **Confidence**: Medium for general organonickel β-H chemistry; Low for direct Kumada filling.
* **注記**: Stage 3 §2 SRG-8 の k_RE/k_{β-H} 直接測定は Ni 系では充填がやや弱い領域。
* **Self-classified retrieval Tier**: Tier II — refs 11 の Yamamoto 系列の延長として。
* **推論経路**: SRG-8 β-H 寛容性 → Yamamoto 群 organonickel 系列 → Hartwig Pd 系列拡張。
* **DB-findability**: yes for Yamamoto 系列; uncertain for direct β-D Kumada studies.
* **Bibliographic confidence**: Medium for class; Low for specific filling citation.
* **Verification recommendation**: Yamamoto group 1973-1975 J. Organomet. Chem. を体系的に
  検索。

---

## §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, Bull. Chem. Soc. Jpn. 49, 1958 (1976) | EP-01a, EP-02a (bundle) | VQ-2 | 1976 | Medium-High |
| 2 | Corriu & Masse, J. Chem. Soc. Chem. Commun. 144 (1972) | EP-09a (CLA-1 partial) | VQ-2 | 1972 | High (cited in target) |
| 3 | Tsou & Kochi, JACS ~1979 (uncertain exact citation) | EP-04a, EP-10a (radical mechanism + kinetics) | VQ-3 | ~1979 | Medium |
| 4 | Yamamoto group, J. Organomet. Chem. ~1973-1974 (uncertain exact citation) | EP-03a, EP-06a (organonickel intermediate + β-H) | VQ-3 | ~1973-1974 | Low-Medium |
| 5 | Anderson & Vicic, Organometallics ~2004 (uncertain) | EP-03a (Ni(I)/Ni(III) intermediate) | VQ-3 | ~2004 | Low |
| 6 | Kambe / Fu group sp³-sp³ Ni cross-coupling representative paper (uncertain specific citation) | EP-07a (paradigm-shift) | VQ-2/VQ-3 | 2000s-2010s | Low-Medium |
| 7 | van Leeuwen group bite-angle ligand-screen (Casey 1992 / van Leeuwen Chem. Rev. ~2000 系列) | EP-05a (quantitative ligand ranking) | VQ-3 | 1990s-2000s | Low-Medium |

**選定理由：**

選定リストの上位 2 報（BCSJ 1976 Full Paper + Corriu-Masse 1972）は confidence high で
identified できる「明示的な前提」候補であり、残り 5 報（#3〜#7）は confidence
medium-low の「構造的推測」候補である。

VQ 階段カバレッジ：
- VQ-2 要件（method-level の completeness）: BCSJ 1976 Full Paper #1 が EP-01a + EP-02a を
  bundle 充填し、Corriu-Masse 1972 #2 が EP-09a (CLA-1) を partial 充填。
- VQ-3 要件（mechanism-level）: Tsou-Kochi #3 が radical mechanism と kinetics を、
  Yamamoto #4 が organonickel 中間体を、Anderson-Vicic #5 が Ni(I)/Ni(III) サイクルを、
  van Leeuwen #7 が ligand bite angle を、それぞれ partial 充填。
- VQ-2/3 boundary: Kambe/Fu #6 は paradigm-shift 充填で「sp³ 排除」境界自体を反転。

バンドル充填：BCSJ 1976 Full Paper が EP-01a + EP-02a を 1 報で bundle 充填する効率性が
特筆される。これは Communications → Full Paper の自動解消パターンの典型。

**重要な留保：** 選定リストの #3〜#7 は、author + 系列レベルでは medium confidence だが、
exact citation（volume / page / year）の信頼度は low。原稿で引用する前に SciFinder /
Web of Science で系統的 verification が必須。

---

## §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件: EP-09a (CLA-1) → 1972 [Corriu-Masse] [自己充填外、同時期 independent]
- VQ-2 要件: EP-01a + EP-02a → 1976 [Tamao/Kumada] [自己充填、Communications → Full Paper]
- VQ-3 要件: EP-03a + EP-06a → ~1973-1974 [Yamamoto] [分野横断充填、organonickel 化学]
- VQ-3 要件: EP-04a + EP-10a → ~1979 [Tsou & Kochi] [技術駆動充填、radical clock 法]
- VQ-3 要件: EP-05a → 1990s-2000s [van Leeuwen] [長期遅延充填、bite angle 概念の確立]
- VQ-3 要件: EP-03a (Ni(I)/(III)) → ~2004 [Anderson-Vicic] [長期遅延充填、新世代分光法]
- VQ-2/3 boundary: EP-07a → 2000s-2010s [Kambe / Fu] [パラダイム転換充填、長期遅延 30+ years]
- VQ-4 要件: EP-08a → 未充填

**階層-時間対応の評価：**

仮説「VQ 階層が上がるほど充填時間が長い」は本ケースでは **部分的に支持** される。
VQ-2 要件（EP-01a, EP-02a）は 4 年以内の自己充填、VQ-3 要件のうち中間体観測
（EP-03a, EP-06a）は 1-2 年の隣接分野充填、機構解明（EP-04a, EP-10a）は 7 年、
配位子定量（EP-05a）と現代的中間体観測（EP-03a Ni(I)/Ni(III)）は 30+ 年、
sp³ 境界破り（EP-07a）も 30+ 年を要した。VQ-4 要件（複製・不確かさ）は未充填。

ただし、興味深い反例：CLA-1 (EP-09a) は 1972 年に Corriu-Masse によって即時に
"対照系の存在" として充填されたが、両系の head-to-head 比較研究は今に至るまで
limited であり、これは単純な "VQ 階層 → 充填時間" 線形仮説では説明できない。
インセンティブ構造（独立発見の競合者間での直接比較は科学社会学的に書きにくい）が
overlay している可能性。

**特筆すべきパターン：**

1. **自己充填パターン**：BCSJ 1976 が EP-01a + EP-02a を bundle 充填するのは
   Communications → Full Paper 遷移の教科書例。Stage 3 §6 (vi) の予測通り。

2. **長期遅延充填**：EP-07a (sp³ 境界破り) と EP-03a (Ni(I)/Ni(III)) が 30+ 年遅延した
   のは、(a) NHC 配位子の登場 (1990s)、(b) X-band EPR の Ni 開殻種への適用、(c)
   computational mechanism studies の成熟、という技術スタックが揃うのを待つ必要が
   あったため。技術駆動充填の側面が強い。

3. **未充填パターン**：EP-08a (反復測定) は科学的論理上は VQ-4 で要求されるが、
   出版インセンティブ構造と整合しないため未充填のまま 50+ 年経過。

4. **著者回顧との照合（推測）**：Kumada は 1980 年代以降の reviews / retrospectives で
   この 1972 年論文を方法論論文として回顧しており、機構的問い（SRG-2 中間体観測など）
   を「著者自身が認識していた未解決問題」として明示的に挙げた記憶はない。これは
   Stage 4 v2 prompt §D Step 4 の「分野の内部者には不可視の構造的不在」の直接証拠候補
   となりうる。Tamao 2002 retrospective mini-review を参照することで verify 可能。

---

## §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-08a [Replication / uncertainty pack]:**

* **未充填の理由**: インセンティブ構造の不整合。Table I の 10 エントリの n=3 複製と SD を
  独立論文として出版する研究計画は、新規性要件と整合しない。Tamao et al. BCSJ 1976
  Full Paper でも複製数の体系的開示は行われていない（推測）。
* **発見的意義**: あり。「Ni-phosphine cross-coupling 分野が 50+ 年にわたって体系的に
  避けてきた問い」として記録できる。これは UQS の発見の一つ：科学的論理上は重要だが
  出版インセンティブ構造と整合しないため、学術出版システムの構造的死角となる EP の典型例。
* **将来の充填可能性**: 中。現代のロボット化合成 + ハイスループット GLPC により技術的には
  容易に充填可能だが、出版価値の問題は残る。Lab automation の論文で副次的に充填される
  可能性が現実的経路。

**部分的に未充填の項目：**

**EP-04a の中で 1,2-dihaloalkene 系 stereochem 時間発展：**

* **未充填の理由**: 技術的困難（時間発展 GLPC は実行可能だが、シンプルな result が
  期待しにくい複雑なシステム）+ 関心の欠如（cis-stilbene synthesis の代替手法が
  豊富であり、機構解明への driver が弱い）。
* **発見的意義**: あり。Stage 3 §2 SRG-3 で同定された "ラジカル vs σ-vinyl-Ni 回転
  vs post-coupling isomerization" の三経路分離は、実は historically never definitively
  performed for the Kumada 1,2-dichloroethylene system。
* **将来の充填可能性**: 高。現代の重水素ラベル + DFT + in situ NMR で実行可能。

**EP-05a の中で cis-強制単座配位子対照：**

* **未充填の理由**: 技術的困難（cis-強制された二座価単座配位子の合成は通常困難）+
  分野慣行（bite angle 研究は二座配位子の bite angle 変化で行われ、cis-強制対照は
  まれ）。
* **発見的意義**: あり。Kumada 1972 の "cis configuration is the first requisite" 主張は
  bite angle と cis-強制を分離する対照実験なしには維持できない。
* **将来の充填可能性**: 中。NHC や carbene-based cis-強制配位子で現代的に試行可能。

**VQ階層逆転の診断：**

本ケースでは部分的な VQ 階層逆転パターンが観察される：

- 充填済み（高 confidence）: EP-01a (RI-01), EP-02a (RI-02) — 低 VQ 要件 (VQ-2)
- 充填済み（partial）: EP-03a (RI-03), EP-04a (RI-04), EP-10a (PRI-11) — 高 VQ 要件 (VQ-3)
- 未充填: EP-08a (RI-08) — 中 VQ 要件 (VQ-4)

これは厳密な逆転ではないが、「VQ-2 (low-VQ) は自己充填で速やかに解消、VQ-3 (high-VQ) は
分野横断で時間をかけて解消、VQ-4 (RI-08 反復・不確かさ) は出版インセンティブと整合せず
未充填のまま」というパターンを示す。後者は「分野のインセンティブ構造が UQS の構造的不在の
一部を維持している」ことの間接証拠と読める。

---

## 付録 A: Retrieval Depth Annotation Matrix

本実験 variant 固有の付録。各充填論文候補について retrieval depth を記録する。

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Tamao et al. BCSJ 49, 1958 (1976) | EP-01a, EP-02a (bundle) | I | Stage 3 §6 (vi) で既に明示 → 直接想起 | yes | Medium-High |
| Corriu & Masse, Chem. Commun. 144 (1972) | EP-09a (CLA-1 partial) | I | 論文自身の Note Added in Proof で明示 | yes | High (target paper 内) |
| Tsou & Kochi, JACS ~1979 | EP-04a, EP-10a | II | refs 5 (Tamura-Kochi 1971) → Kochi グループの Ni 触媒系列研究 | yes | Medium for class; Low for exact citation |
| Yamamoto group, J. Organomet. Chem. ~1973-1974 | EP-03a, EP-06a | II | refs 11 (Uchino-Yamamoto-Ikeda 1970) → Yamamoto 群の延長 | yes | Low for exact citation |
| Anderson & Vicic, Organometallics ~2004 | EP-03a (Ni(I)/Ni(III)) | III | sp³ Ni cross-coupling 文脈での Ni(I)/(III) 議論の triangulation | uncertain | Low |
| Kambe / Fu / Vicic group sp³ representative paper | EP-07a (paradigm-shift) | III | "sp³ Ni cross coupling field" の triangulation | yes (field-level) | Low (specific citation) |
| van Leeuwen / Casey bite-angle series | EP-05a (quantitative ligand) | II | dpp > dpe > dmpe 序列 → bite angle 概念 → van Leeuwen | yes | Low-Medium |
| 未同定 (EP-08a 反復測定研究) | EP-08a | N/A | 不在の同定 | no | N/A |

**Tier 分布の自己観察：**
- Tier I: 2 報（target paper / Stage 3 で既に明示された候補）
- Tier II: 3 報（既存引用からの 1-2 step 連想）
- Tier III: 2 報（field-level triangulation）
- Unfilled: 1 (EP-08a)

**Confidence 分布の自己観察：**
- High: 1 報のみ（Corriu-Masse、target paper 内）
- Medium-High: 1 報（BCSJ 1976、CLAUDE.md / Stage 3 で言及済み）
- Medium: 1 報（Tsou-Kochi の class）
- Low-Medium: 2 報（van Leeuwen, Kambe/Fu の class）
- Low: 2 報（exact citations of Yamamoto 1973-1974, Anderson-Vicic 2004）

**Retrieval pattern の特徴：**
1. Target paper の Note Added in Proof と Stage 3 §6 で明示された候補（Corriu-Masse,
   BCSJ 1976）は Tier I + High confidence で安定して想起される。
2. 化学者として広く認知された author グループ（Kochi, Yamamoto, van Leeuwen, Fu, Vicic）
   は Tier II-III で想起されるが、exact citation の信頼度は系統的に下がる。
3. 「不在の同定」（EP-08a）は明示的な structural inference の結果であり、確信を持って
   "未充填" と判定できる。

**この variant 実験への含意（私の自己観察）：**
- LLM の retrieval は target paper 内の citations や前段 Stage 出力からの直接想起では
  high confidence、author グループ + 系列レベルの class-level 知識では medium、
  exact citation の特定では low confidence、と段階的に劣化する pattern を示す。
- これは「LLM hallucination as uncertain recall from a well-read colleague」frame と
  整合的：colleague は author + 系列を覚えているが exact citation は曖昧、という現実の
  human expert の recall pattern と類似する。
- Manuscript citation には Tier I + High confidence の候補のみを採用し、Tier II/III の
  候補は「verification recommended」フラグ付きで二次的位置に置くことが妥当。

---

## 付録 B: 棄却した候補の明示記録

最終リストから棄却したが retrieval 過程で考慮した候補：

1. **Hartwig group の Pd cross-coupling 機構研究** — Pd 系であり Ni 系の Kumada 1972 への
   direct filling ではないため棄却。ただし Pd 系での mechanism understanding が Ni 系の
   後続研究に転写された影響は大きく、「indirect inspiration」としては機能している。

2. **Suzuki-Miyaura JACS 1979 (B-based cross-coupling)** — Cross-coupling family の
   拡張であるが、Kumada 1972 の機構 EP（中間体観測、kinetics）を直接充填しない。
   Method-family の拡張として brief context のみ。

3. **Sonogashira 1975 (Pd-Cu, alkyne-aryl)** — Pd-Cu 二金属系であり Ni-Grignard 系の
   機構 EP には direct correspondence なし。棄却。

4. **Stille 1978 (Sn-based)** — Pd 系であり direct filling に該当しないため棄却。

5. **Hiyama 1988 (Si-based)** — Pd 系であり direct filling に該当しないため棄却。

6. **Wilkinson catalyst + H₂ 系** — Rh/H₂ 系であり Ni-Grignard 系の触媒サイクルとは
   本質的に異なるため棄却。

7. **Phapale & Cárdenas, Chem. Soc. Rev. 38, 1598 (2009)** — Ni cross-coupling の review。
   Stage 4 v2 prompt §B の規則「レビュー論文は EP を充填しない」により棄却。
   ただし二次情報源として §B の verification recommendation で再活用。

8. **Diccianni & Diao Trends Chem. 2019** — Ni 触媒機構 review。同上の規則により棄却。

9. **Negishi-King-Okukado JACS 1977** — Pd 系 organozinc cross-coupling。Ni 系の Kumada
   1972 への direct filling ではないため、リスト外。Cross-coupling 分野史の context として
   mention 価値あり。

10. **NHC-Ni catalyst 系列 (Hu, Diao 2010s)** — sp³ Ni cross-coupling の現代的展開だが、
    Kumada 1972 の sp² + Grignard 系への direct filling というより paradigm-shift 充填で
    EP-07a に分類済（リスト #6 として採用）。

---

## 付録 C: 本 run の自己評価ノート

本 run（Opus 4.7 v2 run 2）の retrieval pattern について：

1. **Tier I 候補の安定性（cross-run robustness の予測）**：
   target paper 内の citations（Corriu-Masse 1972）と Stage 3 §6 (vi) で明示された
   候補（BCSJ 1976）は、cross-run / cross-vendor 全 run で安定して Tier I + High
   confidence で再現されると予測する。これは "input-anchored retrieval" の安定性。

2. **Tier II/III 候補の cross-run 変動の予測**：
   Yamamoke / Tsou-Kochi / Anderson-Vicic / Kambe / Fu / van Leeuwen のような class-level
   knowledge は、author / 系列レベルでは cross-run で安定すると予測するが、exact citation
   や year は cross-run で変動する可能性が高い。これは "field-anchored retrieval" の
   半安定性。

3. **「不在の同定」の安定性**：
   EP-08a の「未充填」判定は構造的推論に基づくため、cross-run で安定すると予測する。
   これは structural-reasoning の安定性。

4. **本 run 固有の特徴（observed self-pattern）**：
   - 各候補の confidence を保守的に評価する傾向。Low/Medium/High の境界で迷った場合、
     一段下の confidence を選ぶ傾向。
   - 棄却した候補を明示記録する habit は本 prompt の指示に従う形で実行されたが、
     "considered-and-rejected" 候補が 10 報と比較的多い。これは Stage 4 v2 prompt の
     "considered-and-rejected" の明示要求に sensitive に反応した結果。
   - "Bibliographic confidence" と "Self-classified retrieval Tier" が必ずしも線形に
     対応しない例（Tier I だが Confidence Medium-High な BCSJ 1976）が観察された。
     これは Tier（retrieval ease）と Confidence（accuracy of recall）が独立な軸で
     あることを示す。

5. **Multi-run cross-vendor 実験の文脈**：
   本 run は Sonnet v2 multi-run および GPT-5.4 v2 multi-run と比較されることを
   想定している。比較 axis として：
   - Tier I 候補の一致度（input-anchored retrieval の robustness）
   - Tier II/III 候補の class-level 一致度（field-anchored retrieval の semi-robustness）
   - 「未充填」判定の一致度（structural reasoning の robustness）
   - Confidence calibration の vendor-by-vendor 差
   - Considered-and-rejected 候補の重複度
   
   これらの axis での cross-vendor 一致度が、multi-run robustness の量的測定として
   機能する。

inference_time_sec: not available — inject externally
