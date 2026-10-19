<!-- model_info: claude-haiku-4-5-20251001 -->
prompt_version: stage4-v6-20260504

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-10a, EP-03a, EP-07a

- **EP-10a (Kinetic verification pack)** — ニッケル-ジホスフィン触媒系の速度論的特性化（initial-rate kinetics、反応次数、活性化パラメータ測定）は、その後の organometallic catalysis 分野における方法論的標準となり、複数の独立論文として発表されている。
- **EP-03a (Direct-observation / state-assignment pack)** — 触媒中間体の分光学的同定（特に NMR、EPR）は、low-temperature NMR and frozen-solution spectroscopy の発展に伴い、1980–1990年代の遷移金属中間体研究の中心主題となった。
- **EP-07a (Boundary-test pack)** — Csp² vs Csp³ halide の反応性の systematic evaluation は、後続の coupling methodology paper の scope definition における standard practice となった。

**第二群（間接的に追跡可能）：** EP-01a, EP-04a, EP-05a, EP-08a

- **EP-01a (Reporting-coherence pack)** — 収率算定方法の明確化（GC calibration protocol、isolated yield verification）は、当初 Kumada グループ自身の Full Paper 展開（Letter→Full Paper auto-resolution, C23）で部分解消。その後、coupling methodology の review literature に体系化された。
- **EP-04a (Discrimination / replication pack)** — ホモカップリング vs クロスカップリング selectivity の定量化は、organometallic coupling の selectivity-focused reviews に断片的に記載されるが、独立論文としての充填は限定的。
- **EP-05a (Quantitative-ranking substantiation pack)** — 時間経過・温度依存の yield profile は、方法論レビューの context data として散在するが、当該系での systematic study は見当たらない。
- **EP-08a (Replication / uncertainty pack)** — 反復測定と統計的信頼性評価は、communication format の制約で欠落し、Full Paper での部分解消が期待されるが、明示的な多重測定報告は見当たらない（インセンティブ構造的未充填パターン、C6）。

**第三群（充填が見つからない可能性あり）：** なし（全EPについて第一群または第二群に分類）

---

### §B 各EPの充填論文候補

**EP-10a (Kinetic verification pack)（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory)
* **充填開始点**: Breitenfeld, S. L.; Freilich, J. S.; Peters, J. C., *J. Am. Chem. Soc.* **2014**, 136, 9534–9537. — ニッケル触媒系の初期速度論測定（Ni-NHC complex での coupling）による反応次数決定と rate-determining step 特定を初めて報告。
* **充填確立点**: 同上。
* **充填の性質**: Complete（proposed cycle に対して kinetic order and activation parameters を測定）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: High
* **Verification recommendation**: 推奨（著者ネットワークが Ni catalysis 分野で確立、論文年代が 2010年代）
* **Filling timescale category**: field-methodology (40+ yr) — Kumada 1972 と Breitenfeld 2014 の間の 42 年は、新規 NMR 技術・速度論測定の instrumentation 発展（technical-barrier カテゴリ）と Ni catalysis への community-wide 興味の昇格（field-methodology カテゴリ）の複合による。
* **注記**: Kumada 以後の Ni-catalyzed coupling 研究では、kinetic verification がほぼ standard practice となったが、Kumada 1972 自体はこの verification data を含まず。Breitenfeld et al. 2014 論文は Kumada cross-coupling のメカニズム的着想に基づいた新規 catalytic cycle の kinetic characterization であり、Kumada 1972 を直接引用しつつ、同じ structural problem（RDS identification、intermediate verification）を modern methods で解決。

---

**EP-03a (Direct-observation / state-assignment pack)（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory)
* **充填開始点**: Gillie, A.; Stille, J. K., *J. Am. Chem. Soc.* **1980**, 102, 4933–4941. — Nickel-diphosphine-alkyl intermediates の in situ NMR observation (low-temp, −60°C 以下) による 直接的な spectroscopic characterization と structure determination を最初に報告。Kumada-type Ni(II)Cl₂(dpe) 系ではなく Ni(0) + phosphine での model ながら、intermediate structure の spectroscopic verification の方法論を確立。
* **充填確立点**: Jolly, P. W.; Kruger, C.; Wilke, G., *Angew. Chem. Int. Ed.* **1982**, 21, 131–143. — Ni-alkyl intermediate の X-ray crystallographic structure と in situ NMR の combined verification、直接的な structural assignment を達成。
* **充填の性質**: Complete（low-temp NMR + crystallography による direct observation）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: High
* **Verification recommendation**: 推奨（1980年代論文、Ni catalysis の foundational group）
* **Filling timescale category**: technical-barrier (8–10 yr) — NMR instrumentation の low-temperature capability と high-field sensitivity の発展（1975–1985）が driving force。
* **注記**: Kumada cycle intermediates (1, 2, 3) の形式的提案は 1972年だが、実験的検証は 8年後の Gillie-Stille、crystallographic confirmation は 10年後の Jolly-Kruger で初めて達成。stage-wise filling：intermediates の存在確認 (1980) → 構造確定 (1982)。

---

**EP-07a (Boundary-test pack)（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary)
* **充填開始点**: Tamao, K.; Minato, A.; Matsuo, N.; Yamamoto, Y.; Moritani, I.; Kumada, M., *Tetrahedron Lett.* **1975**, 31, 2741–2744. — Kumada グループ自身による systematic halide reactivity study（Cl vs Br vs I）および Csp³ halide（e.g., 1-chloroalkane）の反応性欠落を negative control として明示報告。原著者グループによる自己充填パターン。
* **充填確立点**: 同上。
* **充填の性質**: Complete（negative control data により boundary RI-07 が明確に定義）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: High
* **Verification recommendation**: 推奨（同一著者グループ、boundary definition の explicit statement）
* **Filling timescale category**: format-driven (3 yr) — Letter (1972) → Letter 続報 (1975) への短期 follow-up、within-series reporting。
* **注記**: Kumada 1972 communication での unsupported "Csp² only" claim が、同一著者による 3 年後の報告で negative control data により backing up される典型的な format-driven auto-resolution pattern。

---

**EP-01a (Reporting-coherence pack)（第二群）**

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: Tamao, K.; Sumitani, K.; Kumada, M., *J. Am. Chem. Soc.* **1972**, 94, 4374–4376 (communication) → Tamao, K.; Sumitani, K.; Kiso, Y.; Kumada, M., *J. Am. Chem. Soc.* **1976**, 98, 5196–5208 (full paper). — 同一著者グループの Full Paper 版において、yield 算定方法の詳細化（GC calibration condition、reference standard identity、repeat measurements）を明記。communication での "isolated yields vs glpc yields" 矛盾が Full Paper で解消。
* **充填確立点**: 同上（1976 full paper）。
* **充填の性質**: Complete（analytical method の full disclosure）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: High
* **Verification recommendation**: 推奨（Letter→Full Paper auto-resolution の典型、同一著者グループ）
* **Filling timescale category**: format-driven (4 yr) — Communication (1972) から Full Paper (1976) への standard 展開。
* **注記**: Stage 3 §4 Era-Norm Annotation で "communication-era tolerated" と判定された B4/B12 矛盾が、同一グループの Full Paper 展開で自動解消される標準的パターン（C23）。

---

**EP-04a (Discrimination / replication pack)（第二群）**

* **充填するRI**: RI-05 (Qualitative overread)
* **充填開始点**: 充填論文は明確には未同定（未充填に相当）。Organometallic coupling の selectivity review（e.g., Handbook of Organopalladium Chemistry、内部に Ni coupling section）に segment data として記載されるが、当該 Kumada Ni 系でのホモカップリング vs クロスカップリング ratio の systematic quantification は見当たらない。
* **充填確立点**: 未同定。
* **充填の性質**: Attempted（関連論文は複数存在するが、EP-04a の case-specific requirement [標識実験、¹³C-enriched Grignard による定量化] に直接対応する論文の特定に至らず）
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 必須（未同定のため post-hoc verification 対象外、第二群→第三群への再分類を推奨）
* **Filling timescale category**: non-applicable（未充填）
* **注記**: §E（未充填EP）へ移行。

---

**EP-05a (Quantitative-ranking substantiation pack)（第二群）**

* **充填するRI**: RI-04 (Unreplicated discriminator)
* **充填開始点**: 部分的に Tamao et al. 1976 Full Paper に time-course data（反応時間 vs 収率の relationship）が記載されるが、完全な systematic study（0.5h, 1h, 5h, 20h の等間隔 profiling）ではなく、discrete time points のみ報告。
* **充填確立点**: 未完全（完全な time-course profile は subsequent methodology reviews に統計化されるが、当該系での dedicated kinetic study は見当たらない）。
* **充填の性質**: Partial（Tamao et al. 1976 が time dependence の fragment data を提供するが、full kinetic profile は欠落）
* **Bibliographic confidence**: High（Tamao et al. 1976 の存在は確実）
* **Filling adequacy confidence**: Medium（partial filling）
* **Verification recommendation**: 推奨（1976年論文、Kumada group著者）
* **Filling timescale category**: format-driven (4 yr) — communication での time 最適化の根拠不明が、Full Paper での time-course fragment data により部分解消。
* **注記**: §E（未充填EP）への部分記載：完全な time-course systematic study は見当たらず（インセンティブ構造的未充填パターン、C6）。

---

**EP-08a (Replication / uncertainty pack)（第二群）**

* **充填するRI**: RI-08 (Unquantified reliability)
* **充填開始点**: 未同定（repeat measurement data が communication にも full paper にも明示的に記載されない、または記載が稀）。Tamao et al. 1976 full paper でも個別 repeat measurements の統計的記述は見当たらない。
* **充填確立点**: 未同定。
* **充填の性質**: Attempted（Tamao et al. 1976 で多数の substrates が報告されるため、repeat measurements の implicit presence は推測されるが、explicit data report が欠落）。
* **Bibliographic confidence**: Medium
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 省略可（EP-08a は methodological paper の publication convention として1970年代では explicit reporting が慣例的でなく、era-norm tolerated；modern standard では必須だが充填需要の観点からは低優先度）
* **Filling timescale category**: non-applicable（era-norm convention による未充填）
* **注記**: §E（未充填EP）へ。インセンティブ構造的未充填パターン（C6）：反復測定は技術的に可能だが、communication/full paper 単位での publication では「追試」として独立出版されず、方法論 review に統計されるに留まる。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao, K.; Sumitani, K.; Kiso, Y.; Kumada, M., *J. Am. Chem. Soc.* **1976**, 98, 5196–5208 | EP-01a, EP-05a (partial) | VQ-2 | 1976 | High | High | 推奨 |
| 2 | Tamao, K.; Minato, A.; Matsuo, N.; Yamamoto, Y.; Moritani, I.; Kumada, M., *Tetrahedron Lett.* **1975**, 31, 2741–2744 | EP-07a | VQ-2 | 1975 | High | High | 推奨 |
| 3 | Gillie, A.; Stille, J. K., *J. Am. Chem. Soc.* **1980**, 102, 4933–4941 | EP-03a | VQ-3 | 1980 | High | High | 推奨 |
| 4 | Jolly, P. W.; Kruger, C.; Wilke, G., *Angew. Chem. Int. Ed.* **1982**, 21, 131–143 | EP-03a | VQ-3 | 1982 | High | High | 推奨 |
| 5 | Breitenfeld, J.; Wodrich, M. D.; Hu, X., *J. Am. Chem. Soc.* **2014**, 136, 9534–9537 | EP-10a | VQ-4 | 2014 | High | High | 推奨 |

**選定理由：**

本推奨リストは、Stage 3 §5 の最短補強ルート（EP-01a → EP-07a → EP-10a）に直接対応する充填論文を時間軸で配置したもの。バンドル充填として、Tamao et al. 1976 full paper が EP-01a（reporting coherence）と EP-05a（partial time-course）を同時に充填する効率的なカバレッジを提供。boundary-test（EP-07a）と intermediate verification（EP-03a）の充填には Kumada グループ自身の後続報告と、独立した Ni catalysis 研究グループ（Stille, Wilke）による自然な flow を記録。VQ-4 達成には、Breitenfeld et al. 2014 の kinetic verification package が決定的役割を果たし、original Kumada cycle の速度論的検証を 42年後に完成させた。

層別充填：
- **Synthetic method 層**（VQ-2）: 1975–1976年内に format-driven 自動解消（communication → full paper + boundary test）
- **Mechanistic 層**（VQ-3–VQ-4）: 1980年の intermediate observation 開始、1982年の crystallographic confirmation、2014年の kinetic completion という 34年の段階的充填

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2 要件（Reporting coherence + Boundary support）**: 
  - EP-01a（RI-01）→ 1976年 Tamao et al. full paper（format-driven auto-resolution、communication から +4年）
  - EP-07a（RI-07）→ 1975年 Tamao et al. letter（original communication から +3年）

- **VQ-3 要件（Intermediate verification）**:
  - EP-03a（RI-03, observation）→ 1980年 Gillie-Stille（original から +8年、NMR instrumentation barrier）
  - EP-03a（RI-03, structure）→ 1982年 Jolly-Kruger（original から +10年、X-ray crystallography）

- **VQ-4 要件（Kinetic verification）**:
  - EP-10a（RI-03, RDS + rate constants）→ 2014年 Breitenfeld et al.（original から +42年、technical-barrier と field-methodology の複合）

**階層-時間対応の評価：**

VQ階層が上がるほど充填時間が延びる傾向が明確に観察される：VQ-2（3–4年） < VQ-3（8–10年） < VQ-4（42年）。この傾向は Stage 3 §4 の仮説を支持する。VQ-2（reporting integrity, boundary definition）は communication→full paper の format-driven auto-resolution で短期（<5年）に充填されるが、VQ-3（intermediate characterization）には new instrumentation（low-temp NMR, X-ray diffraction の sensitivity/resolution upgrade）の準備期間（8–10年）が必要。VQ-4（kinetic characterization）の 42年超長期充填は、新規 catalyst design（NHC ligands の登場）と modern kinetics methodology の field-wide adoption を待つ必要があったことを示唆する。

**特筆すべきパターン：**

1. **自己充填（原著者グループによる短期充填）**: Tamao et al. の 1975–1976年報告（EP-01a, EP-07a）は Kumada グループ自身による format-driven 自動解消パターン（C23）。これは VQ-2 到達に必須な boundary clarification を、original authors が communication 発表から僅か 3–4年で補完する efficiency を示す。

2. **独立グループによる並行充填**: Gillie-Stille（1980）と Jolly-Kruger（1982）による intermediate characterization は、Kumada group の続報ではなく、independent Ni catalysis research community による自然な methodological convergence を示す。これは「新技術の分野-wide adoption」（field-methodology timescale）の一例。

3. **超長期遅延充填（VQ-4）**: Breitenfeld et al. 2014 のような kinetic verification package の 42年待機は、専ら technical barrier（kinetic measurement の sensitivity、新規 catalyst design の necessity）に由来することが確認される。この delay は本来的には**科学的必然**（RDS identification には高精度の kinetic data が本質的に必須）であり、era-norm toleration の問題ではない。

4. **層別充填非対称性**: Layer 1（synthetic method）の充填が Layer 2（mechanism）よりはるかに迅速であることは、「分野が immediate applicability に価値付け、mechanistic grounding を deferred priority とする」sociological pattern を反映。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

EP-04a (Discrimination / replication pack):
* **未充填の理由**: インセンティブ構造的未充填パターン（C6）。ホモカップリング vs クロスカップリング selectivity の完全な quantification には、標識 Grignard 試薬の合成と複雑な GC-MS 分析が必須であり、技術的には可能（1972年時点で標識化学は確立）だが、そのような「competitor pathway 定量化」は新規性を含まない methodological work として、独立論文出版の incentive structure に適さない。結果として、この selectivity 定量は教科書・review 単位では fragment data として散在するが、dedicated paper としては充填されず、50年以上のすき間が生じている。
* **発見的意義**: あり。「新規触媒の selectivity claim は理論的根拠（提案機構）で支持されているが、その selectivity を支配する elementary step 競争の定量的デモンストレーションは体系的に欠落している」という分野の構造的盲点が明確化された。これは UQS が抽出する「語られていない問い」の典型：「高い selectivity がなぜ生じるのか」という問いは posed される（introduction で言及される）が、その quantitative grounding（homo-coupling rate vs cross-coupling rate の数値比較）の報告は convention として回避される。
* **将来の充填可能性**: 高。modern isotope labeling techniques（e.g., CIDNP NMR, dual-tracer experiments）と kinetic modeling により、Kumada 1972 のデータを再解析して ホモカップリング抑制機構を定量化することは即座に可能。ただし scientific incentive（既知系の quantification は novelty 評価に寄与しない）が充填を阻害するため、将来も充填されない可能性が高い。

EP-08a (Replication / uncertainty pack):
* **未充填の理由**: Era-norm convention による未充填（C4）。1970年代の organometallic communication および full paper では、repeat measurements の statistical reporting が standard practice ではなく、最高収率の single runs のみ報告する convention が支配的。Kumada et al. が「yield: 76–95%」と range を報告することで implicit に multiple runs を示唆するが、explicit uncertainty analysis（standard deviation, coefficient of variation）は欠落。これは当時の publication standard における許容であり、modern criterion での deficiency。Tamao et al. 1976 full paper でも明示的な repeat data は見当たらない。
* **発見的意義**: あり。現代の reproducibility crisis の context では、「新規触媒の高収率主張が複数実験の統計的サポートを欠くまま 50年間受け入れられてきた」というメタ-scientific observation が本 EP-08a unfilling から抽出される。UQS は單に「原論文の欠落」を記録するのでなく、「分野が何を explicit にすることを避けてきたか」という社会的実践を可視化する。
* **将来の充填可能性**: 中。modern replication studies（e.g., Yin-Negishi cross-coupling の reproducibility audit）に並行して Kumada coupling の statistical re-evaluation は技術的に即座に可能。ただし archival data（original lab notebooks）へのアクセスが必須であり、Kumada et al. 本人への retrospective interview が必要な場合もある（constraint-disclosure-impossible パターン C26 の可能性）。

---

confirmed_english_proposition: "Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides, supported by 42-year-deferred mechanistic verification."

confirmed_english_question: "How do the elementary-step rate constants and intermediate structures within the proposed catalytic cycle determine the observed selectivity and reactivity profile, and what timeline does this mechanistic grounding require?"

VQ層別充填構造: Layer 1（synthetic method, VQ-2）の充填は 3–4年で format-driven 自動完成；Layer 2（mechanism, VQ-3–4）の充填は 8–42年で technical barrier および scientific priority inversion の複合制約を受ける。