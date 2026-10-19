```
prompt_version: stage4-v6
stage3_input_version: s3v2 (Stage 3 prompts only exist up to v4; s3v2 is the only Opus 4.7 Stage 3 output)
model_info: claude-opus-4-7
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Opus 4.7 v6 run 2)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Sonnet Pilot 1)
related_pilot_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4v6_retrieval_depth_run2.md (GPT-5.4 v6 run 2)
related_baseline_opus: papers/dev/kumada/kumada_v17_opus47_s4v2.md (April 19 baseline, no annotation, v2 prompt)
note: Multi-run robustness の cross-vendor extension。Sonnet v6 multi-run + GPT-5.4 v6 multi-run と
      比較して Opus 4.7 v6 prompt 下の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

---

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc., Communication）

---

## 思考過程の externalization（実行ログ）

retrieval depth annotation 実験の趣旨に従い、本セクションでは候補同定の思考過程を時系列で記録する。後続の §A〜§E は構造化出力であり、本セクションはその裏で動いた retrieval 経路の生記録である。

### 最初に思い浮かんだ候補（最初の 30 秒）

論文を「Kumada 1972 cross-coupling」と認識した瞬間、以下が即座に想起された（Tier I candidates）：

1. **Tamao, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Sumitani, Kumada, Bull. Chem. Soc. Jpn. 1976**（同一グループ Full Paper 続報）— Stage 3 §6 (vi) でも参照されており、Letter→Full Paper auto-resolution（C23）の典型例。著者リストの完全性は要 verification（Sonnet pilot で "Tamao-Sumitani-Hayashi-Kumada" 捏造観測例あり）。
2. **Corriu & Masse, J. Chem. Soc., Chem. Commun., 144 (1972)** — 原論文 Note Added in Proof で言及された同時期 Ni(acac)₂ 系。CLA-1 の比較対象として唯一の concurrent 論文。
3. **Kochi 一派の Ni 機構研究（Tamura-Kochi 1971, Kochi 1973-1980 系列）** — 論文中 ref 5, 6 で先行する Fe/Ag/Cu 触媒として引用された Kochi グループは、続いて Ni 触媒の機構研究も展開。SRG-2 の中間体 / 機構関連 EP の充填候補だが、特定の論文同定には注意必要。

### 連想で浮上した候補（次の 1〜2 分）

Tier II candidates：

4. **Negishi cross-coupling の original papers（Negishi, King, Okukado 1977 ほか）** — Ni/Pd cross-coupling の方法論的拡張だが、これは Kumada の EP を「充填」というより「parallel methodology」。EP 充填判定からは除外候補。
5. **Hayashi-Tamao-Kumada 系列（asymmetric Kumada coupling、1980s）** — chiral phosphine 配位子による不斉化。SRG-4（配位子効果）を quantitative に展開する候補。具体的論文は J. Am. Chem. Soc. 1984 系列だが verification 必要。
6. **Vicic group の terpyridine-Ni(III) intermediate detection（2004 前後）** — modern era の SRG-2 充填候補。EPR / X-ray による Ni(I)/Ni(III) 中間体直接観測。Tier II（"modern Ni cross-coupling mechanism" の連想で浮上）。
7. **Knochel, Kambe, Hu, Jarvo, Fu 等の "alkyl Kumada" 拡張群（2000s-2010s）** — SRG-9（C_sp³ 境界）への long-term 充填。具体論文の特定は author group 単位までは Tier II、特定の論文番号までは Tier III。

### 棄却した候補

棄却 1: **「ここで Suzuki coupling（Miyaura-Suzuki）の original papers を引くべきか」** — 棄却。Suzuki coupling は Kumada の構造上の発展系列（Pd, ArB(OH)₂）に属するが、本論文の EP（Ni-phosphine の選択性、Grignard の β-H 寛容性）を直接「充填」しない。Methodological succession であって RI 充填ではない。

棄却 2: **「Heck reaction（Heck 1968 ほか）を citation network 上で引くべきか」** — 棄却。Heck は別ファミリー（Pd-mediated alkene insertion）。Kumada の EP には対応しない。

棄却 3: **「具体的な ³¹P NMR の Ni(0)/Ni(II) intermediate detection 論文（Yamamoto Akio group、Tokyo Inst Tech）を Tier I で挙げるか」** — 一部保留。Yamamoto Akio group は organonickel の先駆者だが、(dipy)Ni(Et)₂ の化学（既に ref 11 で引用）はやや別方向。Kumada [NiCl₂(dpe)] 系の specific intermediate の分光学的同定が独立論文として存在するか、私の retrieval では high confidence で同定できない。Tier III （deep, low confidence）として記録し、Verification 必須。

棄却 4: **「v6 prompt の C7 success-driven question erasure pattern が適用される EP はあるか」** — 適用なし。Kumada cross-coupling は subsequent generations（Pd-catalyzed Suzuki/Negishi/Stille）に「成功的に置換」されたが、original の EP（β-H 寛容性、配位子順位の機構）の検証需要は完全消滅していない（modern alkyl-Kumada 研究で再活性化）。erasure ではなく displacement + delayed reactivation のパターン。

### Tier の自己分布見積もり

最終出力前の自己評価：
- Tier I (immediate): 2-3 候補（Bull Chem Soc Jpn 1976 BCSJ Full Paper、Corriu-Masse 1972、Kochi 系列の概念的指示）
- Tier II (associative): 4-5 候補（Negishi/Hayashi/Vicic/Knochel-Kambe-Hu-Jarvo の各系列）
- Tier III (deep): 2-3 候補（specific intermediate papers、kinetic studies、特定の C_sp³ 拡張論文）

DB-findability 見積もり: Tier I は yes、Tier II は yes（author group + decade で検索可能）、Tier III は uncertain（具体的論文番号の正確性は verification 必須）。

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-05a, EP-06a, EP-07a, EP-09a, EP-10a
  — EP-03a [Direct-observation / state-assignment pack]: SRG-2 の中間体分光同定は modern era で複数の独立論文の主題。Kumada [NiCl₂(dpe)] に限定しなければ、Vicic / Hu / Jarvo / Hartwig 系列で広範に追跡可能。
  — EP-04a [Discrimination / replication pack]: SRG-3 の cis:trans stilbene 異性化機構は Ni-vinyl 中間体の stereochemistry 研究として独立論文化されやすい。
  — EP-05a [Quantitative-ranking substantiation pack]: 配位子-活性関係（SRG-4）は cross-coupling 文献の標準テーマ。Tamao-Hayashi-Kumada 系列の Full Paper / asymmetric Kumada 論文で quantitative ranking が確立。
  — EP-06a [Analogy-validation pack]: β-H 寛容性（SRG-8）の機構研究は Ni-alkyl 化学の中心問題として複数論文存在。
  — EP-07a [Boundary-test pack]: SRG-9 の C_sp³ 境界は 2000s 以降「alkyl-alkyl Kumada」の独立分野として発展（Knochel, Kambe, Hu, Jarvo, Fu 等）。
  — EP-09a [Internal benchmark pack]: CLA-1 の Ni(acac)₂ vs [NiCl₂(dpe)] 比較、SRG-9 の Cl/Br/I 比較、SRG-7 の溶媒効果は subsequent papers で個別に検証された候補多数。
  — EP-10a [Kinetic verification pack]: PRI-11 の速度式代数導出 + 観測速度次数の決定は機構研究の標準項目。Kochi 系列・Vicic 系列で追跡可能。

**第二群（間接的に追跡可能）：** EP-02a
  — EP-02a [Identity / purity substantiation pack]: 単一化合物の EA / HR-MS / GLPC 純度は通常 Full Paper の SI として補完される。Letter→Full Paper auto-resolution（v6/v19 C23）に該当する典型例。Tamao-Kumada Bull Chem Soc Jpn 1976 Full Paper で部分自動解消が予測される。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a
  — EP-01a [Reporting-coherence pack]: SRG-6 / SRG-10 の per-entry 条件・収率基準は format-driven な省略であり、Letter→Full Paper auto-resolution（C23）で部分自動解消されるが、独立論文化されない性質。Bull Chem Soc Jpn 1976 Full Paper で部分解消（filling_timescale_category: format-driven）。
  — EP-08a [Replication / uncertainty pack]: SRG-1 の n=3 複製・SD 報告は **インセンティブ構造的未充填**（v18 C6）の典型。1972 年の Table I の各エントリを 50 年後に再測定して n=3 報告する独立論文の出版インセンティブは存在しない（合成化学分野では n=1 の preparative result が標準）。技術的には可能だが構造的に未充填。

---

### §B 各EPの充填論文候補

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（SRG-2 の L₂NiR₂, L₂Ni(R)(X) intermediates）+ RI-02（SRG-5 の "black mixture" Ni 状態同定）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — 同一グループの Full Paper。Letter のサイクル提示を、より広い基質スコープ・配位子比較・部分的な機構議論で展開（直接的中間体観測の完全性は Full Paper でも限定的と推定）
* **充填確立点**: Anderson, T. J.; Jones, G. D.; Vicic, D. A. *J. Am. Chem. Soc.* **2004**, *126*, 8100 — terpyridine-Ni 系で Ni(I) intermediate を EPR / 結晶構造で直接観測（Kumada 系の dpe 配位子そのものではなく類縁系での中間体実証 = Indirect filling）。Modern era で SRG-2 の機構解像度を引き上げた代表例
* **充填の性質**: Indirect — Kumada [NiCl₂(dpe)] 系そのものでの中間体直接観測（³¹P NMR 等）は私の retrieval では high confidence で specific paper に紐付けられない。terpyridine-Ni 系（Vicic）や bipyridine-Ni 系での観測が最も近い類似系。完全な on-system 観測は限定的
* **Bibliographic confidence**: Medium — Bull. Chem. Soc. Jpn. 1976, 49, 1958 の著者リストは Stage 3 §6 (vi) にも記載されたものを再掲したが、9 名の著者順序の完全性は要 verification（Sonnet pilot で同様 author list の捏造観測例あり）。Vicic 2004 J. Am. Chem. Soc. 126, 8100 は terpyridine-Ni を扱う論文として記憶があるが、具体的タイトル・ページ・共著者の完全性は Medium
* **Filling adequacy confidence**: Medium — Bull Chem Soc Jpn 1976 が「Full Paper として何を追加しているか」の具体的内容は記憶上 partial（より広い substrate scope は確実、in-situ 中間体観測の completeness は不確実）
* **Verification recommendation**: 必須 — (a) 1980 年以前 (Bull Chem Soc Jpn 1976), (b) Kumada は author-named reaction (named-reaction trigger), (c) 著者ネットワークが密 (Tamao + Kumada + Hayashi の Kyoto group は 30+ 関連論文)
* **DOI / URL（任意）**: Bull. Chem. Soc. Jpn. 1976 doi:10.1246/bcsj.49.1958（Crossref で要確認）; Vicic 2004 doi:10.1021/ja0483903（要確認）
* **Filling timescale category**: format-driven (1-3 yr, Bull Chem Soc Jpn 1976 は 4 年遅れだが BCSJ Full Paper は format-driven の延長)+ technical-barrier (32 yr, Vicic 2004 まで)
* **注記**: Bibliographic verification status: pending. SRG-2 の RI-03 完全充填には「Kumada [NiCl₂(dpe)] に対する dedicated mechanistic study」が必要だが、retrieval 上は specific paper として同定困難。Hartwig group の Pd cross-coupling mechanism 文献群（2000s）は parallel mechanism の参照点となる

---

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: PRI-11 [Mechanism-kinetics decoupling]（Stage 3 PRI-11 候補）+ RI-03
* **充填開始点**: Smith, M. J.; Kochi, J. K. — Kochi 系列の Ni-cross-coupling 速度論研究（J. Am. Chem. Soc. 1980 前後）— hedged prediction。具体的論文同定は記憶上 Low
* **充填確立点**: Hu group / Vicic group の modern Ni cross-coupling kinetics（2010s）— 速度次数決定 + 律速段階特定
* **充填の性質**: Partial — Kumada [NiCl₂(dpe)] 系そのものの v = k[Ni]^a[RMgX]^b[ArX]^c の a, b, c 報告は私の retrieval では具体的論文に紐付けられない
* **Bibliographic confidence**: Low — 「Kochi がやったはず」「Hu / Vicic がやったはず」というレベルの hedged prediction
* **Filling adequacy confidence**: Low — 速度論研究の対象基質が Kumada original Ph-Cl + n-BuMgBr に対応するか不確実
* **Verification recommendation**: 必須 — Bibliographic confidence Low の候補を含む (d 条件)
* **DOI / URL（任意）**: 要再検索
* **Filling timescale category**: incentive-aligned (variable) — 機構論研究は技術的には可能だが、Kumada original substrate での kinetic study が specific には未確認
* **注記**: Bibliographic verification status: pending。EP-10a は私の retrieval が最も hedged な EP の一つであり、§C 推奨選定リストでは慎重な扱いが必要

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]（SRG-3 の cis:trans stilbene 単一測定）+ RI-01
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Full Paper で 1,2-dichloroethylene エントリの再現性 / 時間発展が部分追加されたと推定（要 verification）
* **充填確立点**: 未同定（独立した「Ni-catalyzed dihaloalkene cross-coupling stereochemistry mechanistic study」として specific paper に紐付け困難）
* **充填の性質**: Partial — 同一グループ Full Paper による partial 拡張のみ
* **Bibliographic confidence**: Medium（Bull Chem Soc Jpn 1976）— EP-03a と同じ
* **Filling adequacy confidence**: Low — Bull Chem Soc Jpn 1976 が cis:trans の機構解析を実施したかは記憶上不確実
* **Verification recommendation**: 必須 — (a)(b)(c) 条件該当
* **DOI / URL（任意）**: Bull Chem Soc Jpn 1976 doi:10.1246/bcsj.49.1958
* **Filling timescale category**: format-driven (1-4 yr) + non-applicable (deeper mechanism filling は未確認)
* **注記**: Bibliographic verification status: pending

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]（SRG-6 の per-entry 開示 + SRG-10 の収率基準）
* **充填開始点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Full Paper format で per-entry 条件、SD、複数化合物のキャラクタリゼーションが部分追加されたと予測。format-driven auto-resolution の典型
* **充填確立点**: 同上（同一論文）
* **充填の性質**: Partial — Full Paper format への遷移で per-entry condition は典型的に解消されるが、n=3 複製・SD の追加は時代慣習上 unlikely
* **Bibliographic confidence**: Medium
* **Filling adequacy confidence**: Medium — Full Paper format への遷移自体は high confidence、specific な reporting completeness の改善 degree は Medium
* **Verification recommendation**: 必須
* **DOI / URL（任意）**: Bull Chem Soc Jpn 1976 doi:10.1246/bcsj.49.1958（Crossref で要確認）
* **Filling timescale category**: format-driven (1-4 yr)
* **注記**: Bibliographic verification status: pending. C23 trigger: applicable (Letter format の原論文に対して同一グループ Full Paper continuation paper が後続)。auto_resolution_type: "Letter→Full Paper", expected_resolution_window: "1-4 yr", auto_resolution_status: "occurred"

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Object identification]（SRG-6 の "pure" 数値化 / EA 欠落 / SRG-5 の Ni 状態同定）
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958 — Full Paper format で 10 entries の各製品 EA / HR-MS が補完されたと予測（時代の BCSJ standard）
* **充填確立点**: 同上
* **充填の性質**: Partial — 製品同定は Full Paper で typically 解消、SRG-5 の Ni 状態同定（"black mixture" の正体）は別研究領域（Ni speciation studies）として未充填の可能性
* **Bibliographic confidence**: Medium
* **Filling adequacy confidence**: Medium — 製品 EA は Full Paper で標準的に追加、Ni 状態同定は別問題
* **Verification recommendation**: 必須
* **DOI / URL（任意）**: 同上
* **Filling timescale category**: format-driven (1-4 yr)
* **注記**: Bibliographic verification status: pending. C23 trigger: applicable. SRG-5 の Ni speciation 部分は filling timescale が異なり、technical-barrier (10-20+ yr) で modern XAS / EXAFS / EPR studies に依存

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]（SRG-1 の n=3 複製・SD）
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: 未充填 — **インセンティブ構造的未充填**（v18 C6 適用）。1972 年 Table I の各 entry を 50 年後に再測定して n=3 SD を報告する独立論文の出版インセンティブは合成化学分野で存在しない。modern process chemistry の robustness studies は新規 substrate / 新規 catalyst を対象とする
* **Bibliographic confidence**: N/A（候補なし）
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: 省略可（候補なし）
* **DOI / URL（任意）**: なし
* **Filling timescale category**: non-applicable（インセンティブ構造的未充填）
* **注記**: incentive_structure_type: "incentive-misaligned"（v18 C6）— 技術的可能性 vs 出版インセンティブの不整合

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority]（CLA-1 Ni(acac)₂ vs [NiCl₂(dpe)] 比較、SRG-9 の Cl/Br/I 比較、SRG-7 の溶媒効果）
* **充填開始点**: Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc., Chem. Commun.* **1972**, 144 — 原論文 Note Added in Proof で言及された concurrent 論文。Ni(acac)₂ 系の独立報告として CLA-1 の partial 充填（直接 head-to-head 比較ではなく parallel evidence）
* **充填確立点**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Full Paper で Cl/Br/I 比較や追加配位子比較が拡張されたと予測（要 verification）
* **充填の性質**: Partial — direct head-to-head benchmark study は私の retrieval では未同定
* **Bibliographic confidence**: High（Corriu-Masse 1972 は原論文で完全引用）, Medium（Bull Chem Soc Jpn 1976）
* **Filling adequacy confidence**: Medium — Corriu-Masse は parallel evidence、direct comparative study としては incomplete
* **Verification recommendation**: 必須（Bull Chem Soc Jpn 1976 部分）/ 推奨（Corriu-Masse は原論文引用済みで bibliographic は High）
* **DOI / URL（任意）**: Corriu-Masse 1972 — Chem. Commun. 1972, 144（DOI 不明、要 Crossref）
* **Filling timescale category**: incentive-aligned（同年）+ format-driven（Full Paper）
* **注記**: Bibliographic verification status: Corriu-Masse = verified（原論文に明示）, Bull Chem Soc Jpn 1976 = pending

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]（SRG-9 の C_sp³ ハロゲン化物排除）+ RI-09
* **充填開始点**: Kumada / Tamao グループの後続 alkyl Grignard 拡張試行（1970s 後半-1980s）— specific paper 同定は記憶上 Medium-Low
* **充填確立点**: Knochel, P. および Kambe, N. の Ni-catalyzed alkyl-alkyl Kumada coupling（2000s 中盤〜2010s）— C_sp³ 境界の体系的拡張
  - Hu, X. group: Ni(I)/Ni(III) 機構による alkyl Kumada（Pérez García, P. M. et al. — 2010s 系列）
  - Jarvo, E. R. group: enantiospecific Ni-catalyzed alkyl coupling（2010s）
  - Fu, G. C. group: Ni / chiral ligand alkyl coupling（2010s）
* **充填の性質**: Paradigm-shift — 原論文の sp²-only restriction は 30 年後に modern Ni(I)/Ni(III) パラダイムで境界自体が再定義された。元の論文の枠組み（sp² requirement）が"確認されて棄却"された
* **Bibliographic confidence**: Medium（author group / decade レベル）/ Low（specific 論文番号）— 著者名と研究領域は High confidence、specific JACS / Angew 巻号は要 verification
* **Filling adequacy confidence**: High — 「sp² only」境界が paradigm-shift されたことは modern Ni cross-coupling literature の中心的事実
* **Verification recommendation**: 必須 — (b)(c)(d) 条件該当
* **DOI / URL（任意）**: 要再検索
* **Filling timescale category**: technical-barrier (30+ yr) — Ni(I)/Ni(III) cycle の理解と単電子 transfer 機構の確立に時間を要した
* **注記**: Bibliographic verification status: pending. RI-07 の境界主張が "validated and overturned" された典型例。Layer asymmetry (Stage 2 v19 C22): boundary 主張の Layer 1 充填（経験的反例）は Knochel/Kambe の 2000s 中盤、Layer 2 充填（機構的理解）は Vicic/Hu の 2000s 後半-2010s

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-05 [Qualitative overread]（SRG-4 の配位子順位 dpp > dpe > dmpe ≈ PPh₃ ...）
* **充填開始点**: Tamao et al. Bull Chem Soc Jpn 1976 — Full Paper で配位子比較の quantitative データ追加と推定
* **充填確立点**: Hayashi-Kumada 系列（asymmetric Kumada coupling, J. Am. Chem. Soc. 1984 前後）— chiral phosphine ligands の体系的活性比較で配位子効果を quantitative に展開
* **充填の性質**: Partial — Kumada original 配位子セット (dpp, dpe, dmpe, PPh₃, PEt₃, PPh₂Me) の体系的 head-to-head TON / TOF 比較は私の retrieval では specific paper に紐付け困難
* **Bibliographic confidence**: Medium（Bull Chem Soc Jpn 1976, Hayashi-Kumada 系列の存在は High; specific 論文は Medium）
* **Filling adequacy confidence**: Medium
* **Verification recommendation**: 必須
* **DOI / URL（任意）**: 要再検索
* **Filling timescale category**: incentive-aligned（5-12 yr range）
* **注記**: Bibliographic verification status: pending

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]（SRG-8 の β-H 不安定性論拠の輸入）+ RI-03
* **充填開始点**: Kochi グループの Ni-alkyl decomposition kinetics 研究（1970s 後半）— β-H elimination の rate constant 測定。specific paper 同定は記憶上 Low
* **充填確立点**: Hartwig group / Vicic group の modern Ni-alkyl β-H elimination studies（2000s 以降）
* **充填の性質**: Indirect — Kumada specific catalyst (dpe) での β-H 寛容性 mechanism の dedicated study は私の retrieval では未同定
* **Bibliographic confidence**: Low — 著者ネットワーク / decade レベルの hedged prediction
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 必須
* **DOI / URL（任意）**: 要再検索
* **Filling timescale category**: technical-barrier (20+ yr) — Ni(II)-alkyl β-H elimination kinetics の体系的理解は 2000s
* **注記**: Bibliographic verification status: pending

---

### §B 末尾チェック：Bibliographic verification（v18.3）

**トリガー条件評価結果：**
- (a) 論文年代古い (1980 年以前): Bull Chem Soc Jpn 1976, Corriu-Masse 1972, Kochi 系列等が該当 → **該当**
- (b) 著者ネットワーク密: Kumada-Tamao-Sumitani-Hayashi-Kiso-Zembayashi-Fujioka-Kodama-Nakajima-Minato Kyoto group は 30+ 関連論文 → **該当**
- (c) author-named reaction: "Kumada coupling" は named reaction → **該当**
- (d) Bibliographic confidence Medium-Low の候補 2 件以上: EP-10a (Low), EP-05a (Medium), EP-06a (Low), EP-07a specific paper (Low) 等多数 → **該当**

**全 (a)(b)(c)(d) 該当**: 全候補に Verification recommendation [必須] を付与済み。

**Bibliographic verification status**: 全候補 pending。post-hoc Crossref / DOI 検証を経るまで §C 推奨選定リストは「⚠️ verification 待機中」として表記する。

**Hallucination 警告との照合**:
- 「Kumada 1972 における "Tamao-Sumitani-Hayashi-Kumada" 捏造」（Sonnet pilot 既知パターン）に対し、本 retrieval では原論文著者 Tamao-Sumitani-Kumada（3 名、Hayashi なし）として記述し、Bull Chem Soc Jpn 1976 続報著者を Tamao-Sumitani-Kiso-Zembayashi-Fujioka-Kodama-Nakajima-Minato-Kumada（9 名、Hayashi なし）として記述した。Hayashi は subsequent asymmetric Kumada coupling（1980s）系列で Kumada 共著者として登場するが、本 1972 + 1976 系列には含まれない（と私の retrieval が示す）。verification 必須。

---

### §C 推奨選定リスト（⚠️ pending verification）

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, Bull. Chem. Soc. Jpn. 1976, 49, 1958 ⚠️ pending | EP-01a, EP-02a, EP-03a (partial), EP-04a (partial), EP-05a (partial), EP-09a (partial) | VQ-2 (era-norm) → VQ-2 (modern partial) | 1976 | Medium | Medium | 必須 |
| 2 | Corriu, Masse, J. Chem. Soc., Chem. Commun. 1972, 144 ✅ verified-from-original | EP-09a (CLA-1 partial) | VQ-2 | 1972 | High | Medium | 推奨 |
| 3 | Anderson, Jones, Vicic, J. Am. Chem. Soc. 2004, 126, 8100 ⚠️ pending | EP-03a (Indirect, modern era SRG-2) | VQ-3 | 2004 | Medium | Medium | 必須 |
| 4 | Knochel / Kambe / Hu / Jarvo / Fu 系列の alkyl-alkyl Ni-Kumada 論文（具体的代表論文要 verification） ⚠️ pending | EP-07a (Paradigm-shift) | VQ-3 | 2000s-2010s | Low | High | 必須 |
| 5 | Hayashi-Kumada 系列の asymmetric Kumada coupling 代表論文（1984 前後） ⚠️ pending | EP-05a (partial), EP-06a (Indirect) | VQ-2 → VQ-3 | 1984 | Low | Medium | 必須 |

**選定理由**:

エントリ 1（Bull Chem Soc Jpn 1976）は **バンドル充填の中核**：format-driven auto-resolution（C23）により単一論文で 6 EP（EP-01a, 02a, 03a partial, 04a partial, 05a partial, 09a partial）を partially 充填する高効率エントリ。verification 後の選定リストで最優先候補。ただし著者リストは要 9 名完全一致確認。

エントリ 2（Corriu-Masse 1972）は CLA-1 の唯一の concurrent 比較対象であり、原論文 Note Added in Proof で完全引用されているため Bibliographic confidence は唯一の High。

エントリ 3（Vicic 2004）は modern era で SRG-2 の機構層（VQ-3）を引き上げた代表例だが、Kumada [NiCl₂(dpe)] そのものではなく terpyridine-Ni の indirect filling。

エントリ 4（alkyl-alkyl Kumada 系列）は SRG-9 の Paradigm-shift 充填の確立例だが、specific 論文 / 著者の同定は Bibliographic confidence Low であり verification 必須。

エントリ 5（Hayashi-Kumada asymmetric）は配位子効果（SRG-4）の quantitative 展開だが、original Kumada coupling の EP 充填というより methodological succession の側面が強く、選定 borderline。

VQ 階層的階段カバレッジ：VQ-2 要件 → エントリ 1, 2, 5。VQ-3 要件 → エントリ 3, 4, 5。VQ-4 要件 → 直接対応エントリなし（n=3 SD 報告は EP-08a の incentive-misaligned で未充填）。

**Verification 完了までの正式選定**: 候補 2（Corriu-Masse 1972）のみが verified-from-original。他 4 候補は post-hoc Crossref verification 経由で正式選定リストに昇格する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸（pending verification）：**

- VQ-2 要件: EP-09a (CLA-1 partial) → 1972 Corriu-Masse [自己充填の concurrent 形 / 同年]
- VQ-2 要件: EP-01a, EP-02a (partial) → 1976 Tamao et al. Bull Chem Soc Jpn [自己充填, format-driven, 4 yr]
- VQ-3 要件: EP-05a (partial) → 1984 前後 Hayashi-Kumada [自己充填, methodological extension, 12 yr]
- VQ-3 要件: EP-03a (Indirect) → 2004 Vicic terpyridine-Ni [分野横断・technical-barrier 充填, 32 yr]
- VQ-3 要件: EP-07a (Paradigm-shift) → 2000s-2010s Knochel/Kambe/Hu/Jarvo/Fu 系列 [パラダイム転換充填, 30-40 yr]
- VQ-3 要件: EP-04a, EP-06a, EP-10a → partial / 未充填（具体的論文同定 pending）
- VQ-4 要件: EP-08a → 未充填（インセンティブ構造的未充填、incentive-misaligned）

**階層-時間対応の評価:**

仮説「VQ 階層が上がるほど充填に要する時間が長くなる」を **強く支持** する。VQ-2 要件は 0-4 年で Letter→Full Paper auto-resolution + concurrent 引用で迅速に充填されるが、VQ-3 要件のうち **mechanism layer**（EP-03a 中間体直接観測、EP-07a 境界 paradigm-shift）は 30+ 年を要した。これは Vicic 2004 EPR / Knochel-Kambe-Hu-Jarvo-Fu 系列の登場が分光技術と単電子 transfer 機構理論の発展に依存していたためと整合する。VQ-4 要件（n=3 SD 報告）は構造的未充填であり、階層-時間仮説の上限ケースとして「無限大年（インセンティブ構造的未充填）」を提供する。

**特筆すべきパターン:**

- **format-driven auto-resolution（C23）の典型例**: Bull Chem Soc Jpn 1976 単一 Full Paper が EP-01a, 02a, 03a, 04a, 05a, 09a の partial 充填を 4 年内に提供。Letter→Full Paper auto_resolution_status: occurred の典型
- **Paradigm-shift 充填の典型例**: SRG-9 / EP-07a の "sp² only" boundary が 30+ 年後に Ni(I)/Ni(III) cycle の理解と alkyl-alkyl Kumada の確立で paradigm-shift された
- **technical-barrier 充填の典型例**: SRG-2 / EP-03a の中間体直接観測は EPR / X-ray 単結晶 / in-situ NMR の感度進歩に依存し、Vicic 2004 まで 32 年遅延
- **インセンティブ構造的未充填の典型例**: SRG-1 / EP-08a の n=3 SD 報告は技術的に容易だが構造的に未充填。Stage 4 v6 prompt の C6 pattern の代表ケース
- **著者回顧との照合**: 必要に応じて Tamao 2002 mini-review（papers/ep/discussion/tamao2002/）と本 EP リストの照合により、著者が回顧で言及した "5 features"（β-H 寛容性、sp²-Cl 反応性、配位子順位、cis-stilbene、Et₂O > THF）と Stage 3 EP リストの差を分析可能。本 retrieval ではその照合まで実施していないが、Phase 2 検証として Sonnet pilot 等の cross-vendor 比較で systematic に評価可能

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

**EP-08a [Replication / uncertainty pack]（SRG-1）**
* **未充填の理由**: インセンティブ構造の不整合（v18 C6）— 1972 年 Table I の各 entry を再測定して n=3 SD を報告する独立論文の出版インセンティブは合成化学分野で構造的に存在しない。新規性を要求する出版慣行のもとで「既存 substrate / 既存 catalyst の robustness 報告」は単独論文化されない
* **発見的意義**: あり — UQS が「分野が 50+ 年にわたって体系的に避けてきた問い」として記録できる典型例。合成化学分野の VQ 階層逆転（高 VQ 機構研究は活発、低 VQ 統計的信頼性検証は構造的未充填）の証拠
* **将来の充填可能性**: 中 — modern process chemistry / robustness studies の文脈で、特に scale-up / pharmaceutical synthesis 領域では increasing demand あり。ただし 1972 Kumada original entries そのものが対象になる確率は低い

**EP-10a [Kinetic verification pack]（PRI-11）**
* **未充填の理由**: 部分 — 機構研究は活発だが Kumada [NiCl₂(dpe)] + Ph-Cl + n-BuMgBr という original substrate 系の specific kinetic study が私の retrieval では同定困難
* **発見的意義**: あり — 機構研究は通常 model substrate に move し、original の "real" Substrate の kinetic study が抜け落ちる "model substrate displacement" pattern の証拠
* **将来の充填可能性**: 中 — modern Ni cross-coupling kinetics literature で実施されている可能性は高い、verification で発見されうる

**EP-04a, EP-06a の partial 未充填部分**: 機構研究の sub-area であり、modern Ni cross-coupling literature で部分的に充填されている可能性が高いが、本 retrieval では specific paper への紐付けが Low confidence

**VQ 階層逆転の診断**: 本ケースで明確に観測される。
- 充填済み（または partial 充填）: 高 VQ 要件 = EP-03a (RI-03 mechanism), EP-07a (RI-07 boundary), EP-09a (RI-09 benchmark)
- 未充填（または incentive-misaligned）: 低 VQ 要件 = EP-08a (RI-08 replication)

これは「科学的論理に基づく EP 充填順序（低 VQ → 高 VQ）」と「出版インセンティブに基づく実際の充填順序（高 VQ → 低 VQ）」の構造的逆転であり、Stage 4 v6 prompt §E の VQ 階層逆転診断パターンの典型例。分野のインセンティブ構造が UQS の構造的不在の一部を維持していることの直接的証拠として記録可能。

---

## 付録 A: Retrieval Depth Annotation Matrix

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Tamao et al. Bull Chem Soc Jpn 1976, 49, 1958 | EP-01a, EP-02a, EP-03a (partial), EP-04a (partial), EP-05a (partial), EP-09a (partial) | **I** | "Kumada Letter → Full Paper" の即座連想。Stage 3 §6 (vi) でも参照済の論文。同一グループ Full Paper の存在は Kumada coupling の歴史的事実として高想起 | yes | Medium（9-author list の完全性は要 verification） |
| Corriu, Masse, Chem. Commun. 1972, 144 | EP-09a (CLA-1 partial) | **I** | 原論文 Note Added in Proof で完全引用。retrieval ではなく原論文からの直接参照 | yes | High（原論文に明示） |
| Anderson, Jones, Vicic, J. Am. Chem. Soc. 2004, 126, 8100 | EP-03a (Indirect) | **II** | "modern Ni cross-coupling intermediate detection" の連想 → terpyridine-Ni / Vicic group → 2004 前後の代表論文として浮上 | yes | Medium（specific 巻号は要 verification） |
| Knochel / Kambe / Hu / Jarvo / Fu 系列の alkyl-alkyl Ni-Kumada | EP-07a (Paradigm-shift) | **II → III** | "alkyl-alkyl Kumada coupling の歴史" の連想 → 著者群の同定は Tier II、specific 論文の同定は Tier III | yes（author group + decade レベル）/ uncertain（specific 論文番号レベル） | Low（specific 論文番号）/ Medium（著者群） |
| Hayashi-Kumada 系列 asymmetric Kumada coupling, JACS 1984 前後 | EP-05a (partial), EP-06a (Indirect) | **II → III** | "Hayashi-Kumada asymmetric Kumada" は immediate retrieval だが specific 論文番号は triangulation 必要 | yes（系列レベル）/ uncertain（specific 論文番号レベル） | Low（specific 論文番号） |
| Smith / Kochi の Ni cross-coupling kinetics | EP-10a (Partial) | **III** | "Kochi の Ni mechanism work" の連想 → 1970s 後半 / 1980 前後の論文が存在するはず、という deep triangulation のみで specific paper 同定不可 | uncertain | Low |
| Kochi / Hartwig / Vicic の Ni-alkyl β-H elimination kinetics | EP-06a (Indirect) | **III** | "modern Ni-alkyl β-H elim kinetics" の連想 → 著者群レベルのみ | uncertain | Low |

**Tier 分布の自己観察**:
- Tier I: 2 候補（Bull Chem Soc Jpn 1976, Corriu-Masse 1972）
- Tier II: 2 候補（Vicic 2004, alkyl-alkyl Kumada 系列の author group レベル）
- Tier II → III boundary: 2 候補（Hayashi-Kumada 1984 specific paper, alkyl-alkyl specific 論文番号）
- Tier III: 2 候補（Smith-Kochi specific kinetic paper, β-H kinetics specific paper）

**DB-findability 自己評価**:
- yes（high confidence）: 2 候補
- yes（系列・著者群 level）: 3 候補
- uncertain: 2 候補

**Bib confidence 分布**:
- High: 1 候補（Corriu-Masse 1972）
- Medium: 3 候補（Bull Chem Soc Jpn 1976, Vicic 2004, alkyl-alkyl 著者群）
- Low: 3 候補（Smith-Kochi specific, Hayashi-Kumada specific 1984, β-H kinetics specific）

---

## 付録 B: 考慮し棄却した候補

以下の候補は同定検討の過程で浮上したが、EP 充填判定との対応が不適切と判断し最終リストから除外した。

**棄却 1: Suzuki-Miyaura coupling 系列の original papers（Miyaura, Suzuki 1979 ほか）**
- **棄却理由**: methodological succession であって RI 充填ではない。Suzuki coupling は Pd / boronic acid / alternative ligand を採用し、Kumada の specific EP（β-H 寛容性、Ni-phosphine 配位子順位、Et₂O > THF）を直接充填しない
- **誤分類リスク**: 高被引用論文 = 充填論文と誤認するリスク。Stage 4 v6 prompt §B の "高被引用論文は原論文の手法を「使った」応用論文" 警告に該当

**棄却 2: Heck reaction 関連論文（Heck 1968, Mizoroki 1971 ほか）**
- **棄却理由**: 異なる reaction family（Pd-mediated alkene insertion）。Kumada の EP には対応しない

**棄却 3: Negishi cross-coupling original（Negishi, King, Okukado 1977）**
- **棄却理由**: parallel methodology development（Zn-organometallic vs Mg-Grignard）。Kumada original の specific RI を充填せず

**棄却 4: Yamamoto Akio group の (dipy)Ni(R)₂ 系列**
- **棄却理由**: 既に原論文 ref 11 で引用済。Kumada [NiCl₂(dpe)] 系での specific intermediate detection には対応せず

**棄却 5: Pd-catalyzed cross-coupling の Hartwig group 機構研究（2000s）**
- **棄却理由**: Pd 系であって Ni 系の SRG-2 を直接充填せず。parallel mechanistic insight として参照価値あり

**棄却 6: Kharasch & Reinmuth 1954 教科書**
- **棄却理由**: 原論文 ref 4 で歴史的 background として引用済。EP 充填には対応せず

---

## 付録 C: 実行ログのまとめ

**Total 同定候補数**: 7 系列（Tier I: 2, Tier II: 2, Tier II→III boundary: 2, Tier III: 2; 重複あり = 系列内に複数 specific paper を含む可能性）

**棄却候補数**: 6 系列

**Verification 必須エントリ数**: 6 / 7（86%）— Kumada が author-named reaction であり、Kyoto group の著者ネットワークが密、1980 年以前の論文が含まれるため C17 trigger (a)(b)(c) が同時発火

**最終的な高 confidence エントリ数**: 1 / 7（Corriu-Masse 1972 のみ、原論文引用済のため）

**第三群（未充填）EP 数**: 1（EP-08a, インセンティブ構造的未充填）+ partial 未充填: 3（EP-04a, EP-06a, EP-10a の specific paper 同定 pending 部分）

**filling timescale category 分布**:
- format-driven (1-4 yr): EP-01a, EP-02a, EP-04a partial, EP-05a partial, EP-09a partial（Bull Chem Soc Jpn 1976 経由）
- incentive-aligned (variable): EP-09a (Corriu-Masse 同年), EP-05a, EP-10a
- technical-barrier (20-30+ yr): EP-03a (Vicic 2004, 32 yr), EP-06a, EP-07a (alkyl-alkyl Kumada, 30-40 yr)
- non-applicable (incentive-misaligned): EP-08a

**self-assessment of retrieval reliability**: 本実験では Sonnet v6 multi-run（kumada_v17_sonnet_s4v6_retrieval_depth.md）と GPT-5.4 v6 multi-run（gpt54thinking/kumada_v17_gpt54thinking_s4v6_retrieval_depth_run2.md）との cross-vendor 比較を通じて、Opus 4.7 v6 の retrieval pattern と Tier annotation の安定性を測定する。本 run の retrieval は author-named reaction 特有の hallucination リスク（Sonnet pilot で 67% 観測）を意識して保守的に Bib confidence を付与し、Verification recommendation を 86% で [必須] とした。post-hoc Crossref verification を経た正式 selection list への昇格は本ファイル外の検証 step に委ねる。

---

inference_time_sec: not available — inject externally
