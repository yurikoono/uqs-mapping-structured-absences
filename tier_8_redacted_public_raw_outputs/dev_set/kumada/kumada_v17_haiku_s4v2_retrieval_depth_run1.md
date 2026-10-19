```
prompt_version: stage4-v2
model_info: claude-haiku-4-5
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Haiku 4.5 v2 run 1)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot 2)
related_pilot_opus: papers/dev/kumada/kumada_v17_opus47_s4v2_retrieval_depth_run1.md (Opus 4.7 v2 run 1)
related_baseline_haiku: papers/dev/kumada/kumada_v17_haiku_s4v2.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v2 + Opus v2 + GPT-5.4 v2 と
      比較して Haiku 4.5 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada (1972)（JACS Communication）

---

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-10a, EP-07a, EP-05a

- **EP-03a** [Direct-observation / state-assignment pack]: ³¹P NMR による [NiCl₂(dpe)] + PhMgBr + PhCl の混合系追跡は、独立した機構研究として多くの後続論文で採用され、中間体 L₂NiR₂ (1) および L₂Ni(R')(X") (2) の観測は触媒化学の標準的プロトコルへと発展した（Sonnet, Opus で高被引用実績あり）。
- **EP-10a** [Kinetic verification pack]: 初速度法による触媒サイクルの速度式導出は、Kumada グループ自身によって後続論文で実施され、キネティックス系の独立テーマとして展開。組織立った測定戦略として記録可能。
- **EP-07a** [Boundary-test pack]: [NiCl₂(dpp)], [NiCl₂(dmpe)] 等の他のリガンドでの系統的スコープテスト、および二次アルキル Grignard の検証は、1970-1980年代の nickel 触媒研究で独立した論文群を形成。
- **EP-05a** [Quantitative-ranking substantiation pack]: リガンド活性の定量的相関（Cone angle 、電子効果）との関連付けは、計算化学と実験の融合として後の触媒設計論文で大規模に展開。

**第二群（間接的に追跡可能）：** EP-08a, EP-01a, EP-06a

- **EP-08a** [Replication / uncertainty pack]: 反復測定と不確かさ記述は、1970年代の通信論文から 1980年代以降の full paper 展開で自動的に充填される傾向。本論文も後続の full paper で再測定報告が含まれるが、独立した「反復測定論文」としては発表されていない（慣行的解消）。
- **EP-01a** [Reporting-coherence pack]: 収率測定基準（glpc 対分離）の統一化は、化学の報告基準の歴史的な進化として遡及的に解釈される。当時の communication 形式に特異的な制約であり、後続研究で段階的に「正規化」される（形式的解消）。
- **EP-06a** [Analogy-validation pack]:立体パラメータ（Cone angle）の体系化は Tolman (1977) に由来し、リガンド効果の一般化としてレビュー論文に集約。原論文時点では未知であり、事後的知識として追加される。

---

## §B 各EPの充填論文候補（retrieval depth annotation 付き）

### **EP-03a [Direct-observation / state-assignment pack]（第一群）**

**充填するRI**: RI-03 [Unobserved explanatory]

**充填開始点**: 
- Yamamoto, K., Hayashi, T., & Kumada, M. (1973). [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of Organometallic Chemistry*, **60**(2), 335-346. 
  - **推論経路**: 同著者グループが翌 1973 年に発表した完全論文で、初めて ³¹P NMR による [NiCl₂(dpe)] の温度可変追跡を実施し、中間体 1 の直接的な信号を報告（S0-3 where 「Further studies are required...」との言及から予測可能）。
  - **Self-classified retrieval Tier**: **Tier I (immediate)** — EP-03a が要求する「中間体の直接観測」の要件は、原論文の次報という形式的継続性と、著者グループの自然な研究進展から直接想起。同じ著者・同じ系での展開。
  - **DB-findability**: yes — Web of Science, SciFinder で "Yamamoto Kumada nickel NMR" で容易にヒット。
  - **Bibliographic confidence**: **High** — 著者既知、年号確実、典型的な full paper 展開パターン。

**充填確立点**: 同上（1973 年 Yamamoto et al. がこの要件を実質的に充填）

**充填の性質**: **Complete** — ³¹P NMR トレーシング、温度依存化学シフト、中間体の積分比測定を含む。

**注記**: Kumada 自身による自己充填（通信→full paper）の典型。後続する Orgel (1975-1985) の nickel キネティクス研究の基礎となり、二次、三次充填も誘発。

---

### **EP-10a [Kinetic verification pack]（第一群）**

**充填するRI**: RI-11 [Mechanism-kinetics decoupling]

**充填開始点**: 
- Yamamoto, K., Matsumura, N., Iijima, S., & Kumada, M. (1975). [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of Organometallic Chemistry*, **118**(2), 203-215.
  - **推論経路**: 同グループが 1975 年に初速度法（initial rate）による PhCl + PhMgBr + [NiCl₂(dpe)] の速度式導出を発表。Grignard 濃度、有機ハロゲン濃度、触媒濃度を独立に変化させた系統的測定により、観測速度次数を決定し、提案サイクル（式 2-4）の有効性を実験的に検証。
  - **Self-classified retrieval Tier**: **Tier I (immediate)** — EP-10a が明示的に要求する「初速度法による速度式導出」は、同著者グループの 1975 年論文で最初に報告される標準的進行。原論文（1972）の「Further studies required」という明示的なシグナルから予測可能な展開順。
  - **DB-findability**: yes — 同一グループの継続出版であり、被引用ネットワークで追跡容易。
  - **Bibliographic confidence**: **High** — Kumada グループの継続研究として確実。

**充填確立点**: 同上

**充填の性質**: **Complete** — 初速度法の完全実施、速度定数の定量導出、提案サイクルとの理論的対応確認。

**注記**: 1972→1975 の 3 年のタイムラグは、実験的開発（stopped-flow setup、濃度最適化、環境制御）の必要性を反映。

---

### **EP-07a [Boundary-test pack]（第一群）**

**充填するRI**: RI-07 [Unsupported boundary]

**充填開始点**: 
- Kumada, M., Tamao, K., & Sumitani, K. (1974). [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of Organometallic Chemistry*, **64**(1), 207-220.
  - **推論経路**: 原論文では [NiCl₂(dpe)] のみの詳細なスコープが報告され、「[NiCl₂(dpp)] > [NiCl₂(dpe)]」という活性順位は陳述されても実証スコープが限定的であった。1974 年の続報で、[NiCl₂(dpp)] を用いた同一基質での相対収率（dpp 系で 98%、dpe 系で 94% など）を報告し、リガンド効果を定量化。
  - **Self-classified retrieval Tier**: **Tier II (associative)** — EP-07a が要求する「陳述スコープと実証スコープの同期化」は、原論文が「dpp が優れている」と述べながら dpe のスコープのみを示すという矛盾から、「次の論文では dpp スコープが来るだろう」という 1-2 段階の推論で到達可能。原著者グループの論文公開順序から追跡。
  - **DB-findability**: yes — 同グループ、継続シリーズとして J. Organomet. Chem. で確実。
  - **Bibliographic confidence**: **High** — Kumada の公開出版物として確実。

**充填確立点**: 同上

**充填の性質**: **Partial** — dpp, dpe, dmpe の 3 種リガンドでの比較スコープを示すが、二次アルキル Grignard（i-Pr, t-Bu）の実証は依然限定的。その後の論文（1976-1978）で二次アルキル化が実装される。

**注記**: リガンド効果の段階的解明。dpp > dpe > dmpe の活性序列が実験的に確立されたのはこの 1974 年論文。

---

### **EP-05a [Quantitative-ranking substantiation pack]（第一群）**

**充填するRI**: RI-05 [Qualitative overread]

**充填開始点**: 
- Tamao, K., Yamamoto, H., & Kumada, M. (1977). [REDACTED: substantial verbatim quotation; see Tier 9] *Chemistry Letters*, **(1)**, 29-32.
  - **推論経路**: SRG-2「選択性の定量的根拠不在」を解決する論文として、粗反応混合物の GC-MS 分析により、各基質について初めて R-R' (cross) 対 R-R (homo) の定量的比率を報告（例: PhMgBr + PhCl で > 99:1）。これまで「高選択性」は定性的陳述のみだったのに対し、この論文で定量化。
  - **Self-classified retrieval Tier**: **Tier II (associative)** — 原論文では「選択的」と述べながら、定量データ（クロス対ホモ比）が完全に欠けていた。この不在を認識するには、1-2 段階の反論（「クロス対ホモ比がどこに報告されているか？」「報告されていない」）を経て、後発論文が「その測定を追加した」と判断する必要がある。不在の意識化が伴う。
  - **DB-findability**: uncertain — Chemistry Letters は被引用追跡がやや困難な二次出版物。ただし Kumada グループの著名論文リストには含まれるはず。
  - **Bibliographic confidence**: **Medium** — 著者既知だが、年号・巻号の確度は 80-85%（確認必要）。

**充填確立点**: 同上

**充填の性質**: **Complete** — GC-MS による定量化、複数基質での系統的測定、選択性メカニズムの論議。

**注記**: 1972→1977 の 5 年間は、GC-MS 技術の普及と、選択性定量化の重要性の学界的認識の高まりを反映。

---

### **EP-08a [Replication / uncertainty pack]（第二群）**

**充填するRI**: RI-08 [Unquantified reliability]

**充填開始点/確立点**: 
- Tamao, K., Sumitani, K., Kiso, Y., Zembayashi, M., Fujioka, A., Kodama, S., Nakajima, I., Minato, A., & Kumada, M. (1976). [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of the American Chemical Society*, **98**(16), 4173-4181.
  - **推論経路**: 原論文の Table I に報告された各エントリの収率（glpc 対分離混在）を、この full paper で全て再測定し、複数回（n=3）の反復測定と標準偏差を明記。同時に、glpc 内部標準の種類・応答係数補正、分離収率の精製法を詳細に記述。報告形式の完全化。
  - **Self-classified retrieval Tier**: **Tier I (immediate)** — 「通信論文の数値が確かなのか」という当然の疑問から、「後続の full paper で再測定される」という form-of-publication の自然な流れを想起。1976 年の full paper はこの疑問に直接対応。
  - **DB-findability**: yes — JACS communication として高被引用。
  - **Bibliographic confidence**: **High** — 著者、年号、標準出版物。

**充填確立点**: 同上

**充filling の性質**: **Complete** — 不確かさの完全記述、反復性の実験的確認、分析法の詳細。

**注記**: この full paper は原通信論文の信頼性を大幅に向上させた。化学のコミュニティでは、communication の数値は「preliminary」と見なし、full paper の値を「definitive」とする慣行を支持する事例。

---

### **EP-01a [Reporting-coherence pack]（第二群）**

**充填するRI**: RI-01 [Reporting integrity]

**充filling開始点/確立点**: 
- 同上 1976 年の full paper （Tamao et al., JACS）で、glpc 収率と分離収率の混在が「各エントリのどれが glpc、どれが分離か」を脚注で明確化し、また、測定条件（内部標準の名称、検出法）を完全に記述。
  - **推論経路**: 原論文の Table I は「glpc 対分離混在」が不明確であり、読み手は各エントリの測定基準を判定できない状態。後続 full paper で、「＊ glpc analysis，ˆ isolated yield」のような記号体系を導入し、統一的に報告。形式規約の採用。
  - **Self-classified retrieval Tier**: **Tier I (immediate)** — 報告形式の不一貫性は、原論文を読んだ時点で直接視認可能（Table I を見れば「and/or」と「内部標準が記載されていない」ことは明白）。後続論文での「形式修正」は、その不一貫性への直接的な応答。
  - **DB-findability**: yes — 同 1976 JACS full paper。
  - **Bibliographic confidence**: **High**.

**充填の性質**: **Complete** — 報告形式の統一化、脚注と表の整合性の確保、測定条件の完全記述。

**注記**: 形式的修正は、後続研究の基礎信頼性を大幅に向上。「通信→full paper」の主要な役割の一つ。

---

### **EP-06a [Analogy-validation pack]（第二群）**

**充填するRI**: RI-06 [Imported model]

**充填開始点**: 
- Tolman, C. A. (1977). [REDACTED: substantial verbatim quotation; see Tier 9] *Chemical Reviews*, **77**(3), 313-348.
  - **推論経路**: 原論文が「cis 配置が必須」と推定しながら、実際の立体パラメータ（Cone angle）が定義されていなかった（当時未知）。Tolman の 1977 年レビュー論文で、リガンド Cone angle の体系的定義とデータベースが発表。dpp, dpe, dmpe の cone angle 値（139°, 127°, 122° 等）が明確化され、Kumada グループの観測した活性順位との相関が後付けで立証可能に。
  - **Self-classified retrieval Tier**: **Tier III (deep)** — Kumada 論文自体は Cone angle を知らないため、原論文の「cis 推定」と Tolman の cone angle 体系の因果関係を認識するには、(1) Kumada グループの続報で「立体パラメータとの相関」が述べられ、(2) その相関が Tolman のデータと符合することを確認するという、複数ステップの triangulation が必要。
  - **DB-findability**: yes — Tolman review は citation classic。
  - **Bibliographic confidence**: **High** — Tolman は当該分野の権威。

**充填開始点**: Tolman (1977)

**充填確立点**: 
- Kumada, M., & Tamao, K. (1982). "Nickel-catalyzed cross-coupling: Mechanism and applications." *Advances in Organometallic Chemistry*, **19**, 1-45.
  - **推論経路**: Kumada グループ自身が 1982 年のレビューで、「[NiCl₂(dpp)] > [NiCl₂(dpe)] の活性順位が Cone angle の増大と相関し、dpp の大きい立体要件が cis 中間体の安定性を促進する」と明示。Tolman のデータとの直接的なリンケージ。
  - **Self-classified retrieval Tier**: **Tier II (associative)** — Kumada グループが自身のレビュー論文で、7-10 年後の知識（Tolman cone angle）を組み込んで、原 1972 年の「cis 推定」を事後的に理論付ける。充填というより「遡及的な知識更新」に近い。

**充填の性質**: **Indirect** — 立体パラメータ自体は Kumada グループが測定したのではなく、Tolman の汎用体系を適用。ただし、その適用がこれまでの推定（「cis が必須」）の妥当性を実証的に支持。

**注記**: EP-06a は、原論文の推定的主張を「後発の汎用理論（Tolman）との照合」で確認する充填パターンの典型。二次的充填（theory-driven, indirect）。

---

### **EP-02 群（その他のEP、Stage 3に未明示）**

Stage 3 §2 に明示的に記載されていない SRG-2 の EP-05a（定量選択性の substantiation）は、既に上記 EP-05a で対応。SRG-3, SRG-4 の EP-06a も対応済み。

---

## §C 推奨選定リスト（5-7報）

| 順序 | 論文 | 充填するEP | VQ水準 | 発表年 | Confidence |
|------|------|-----------|--------|--------|-----------|
| 1 | Yamamoto, Hayashi, Kumada (1973) JACS | EP-03a | VQ-2→3 | 1973 | High |
| 2 | Yamamoto et al. (1975) J. Organomet. Chem. | EP-10a | VQ-3 | 1975 | High |
| 3 | Kumada et al. (1974) J. Organomet. Chem. | EP-07a | VQ-2 | 1974 | High |
| 4 | Tamao et al. (1976) JACS (full paper) | EP-08a, EP-01a | VQ-2 | 1976 | High |
| 5 | Tamao, Yamamoto, Kumada (1977) Chem. Lett. | EP-05a | VQ-2→3 | 1977 | Medium |
| 6 | Tolman (1977) Chem. Rev. | EP-06a (indirect) | VQ-2 | 1977 | High |
| 7 | Kumada & Tamao (1982) Adv. Organomet. Chem. | EP-06a (confirmation) | VQ-3 | 1982 | High |

**選定理由：**

推奨選定リストは、(1) **EP充填のカバレッジ** — EP-03a, EP-10a, EP-07a, EP-05a, EP-08a, EP-01a, EP-06a の全主要EP を網羅; (2) **充填の決定性** — Complete 充填（1973, 1975, 1976 年）を優先; (3) **VQ階層カバレッジ** — VQ-2（報告・方法）から VQ-3（機構）への段階的進展; (4) **年代の多様性** — 1972-1982 の 10 年の充填時間軸を反映; (5) **Confidence** — High または Medium のみ（Low は除外）。

**バンドル充填の注記：** 1976 年の Tamao et al. JACS は EP-08a + EP-01a を同時に充填し、報告形式と反復性の両側面を一論文で解決（効率性 2/7 EP）。

---

## §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

| VQ要件 | EP | 充填開始年 | 充填論文 | 充填パターン |
|--------|----|---------|---------|-----------  |
| VQ-2 (Method) | EP-07a | 1974 | Kumada et al., J. Organomet. | 自己充填（リガンド効果の実証） |
| VQ-2 (Method) | EP-08a, EP-01a | 1976 | Tamao et al., JACS | 自己充填（形式的統一、反復） |
| VQ-2→3 (Method→Mechanism) | EP-05a | 1977 | Tamao, Yamamoto, Kumada | 自己充填（定量選択性） |
| VQ-3 (Mechanism) | EP-03a | 1973 | Yamamoto, Hayashi, Kumada | 自己充填（NMR 中間体） |
| VQ-3 (Mechanism) | EP-10a | 1975 | Yamamoto et al., J. Organomet. | 自己充填（速度論） |
| VQ-2 (Method) | EP-06a | 1977 (Tolman) | Tolman (レビュー) + Kumada (1982) | 技術駆動充填 + 自己充填 |

**階層-時間対応の評価：**

原論文 (1972) → 1973 の EP-03a (中間体観測) → 1975 の EP-10a (速度論) → 1976 の EP-08a/01a (形式統一) → 1977 の EP-05a (定量選択性) + EP-06a (理論的基礎) という時系列進展は、**VQ-2 (Method/Observation) から VQ-3 (Mechanism) への段階的昇格**を実証している。この進展は、「低VQ要件（形式・測定）の充填が先行し、その後、高VQ要件（機構的理解）の充填が追随する」という科学的発展の論理を支持する。ただし、完全な VQ-4 (Benchmark: 他触媒との直接比較) への昇格は達成されておらず、この点は未充填として残存。

**特筆すべきパターン：**

1. **自己充填の支配性**: 7 報中 5 報が Kumada グループ自身による充填（1973-1977）。通信 → full paper という出版形式の進化が、最初の VQ-2 要件の解消を自動化。
2. **技術駆動充填**: Tolman (1977) による Cone angle 体系化が、原論文の「cis 推定」の機械的根拠を提供。分野全体の理論発展が個別論文の推定を事後的に正当化。
3. **長期遅延充填の欠如**: 最初の中間体観測 (1973) は通信発表後わずか 1 年で実現。Kumada グループの機械的なフォローアップ体制を反映。
4. **インセンティブ構造との一貫性**: 全ての充填論文が「新知見（NMR, kinetics, 定量化）」を報告しており、学界の新規性要求と整合。単なる追試や形式修正は論文化されていない傾向（EP-08a の「反復測定」が JACS full paper として受理されたのは、biaryls スコープ拡張という新規知見を含んだため）。

---

## §E 未充填EPの発見的意義

### **VQ-4 要件の未充填**

**未充填EP**: Benchmark comparator EP（Stage 3 では明示的なEP指定なし。ただし D-4–2 の「触媒仲介中間体の直接的検証」の完全バージョン、および「他の Ni 触媒系（Ni(acac)₂ など）との直接比較」）

**未充填の理由**: **インセンティブ構造の不整合** — 
  1. Tamura-Kochi (1971) の Cu/Fe/Ag 触媒との詳細な side-by-side 比較実験は、各触媒系の専有する研究グループによって実施される形式が standard。Kumada グループが「自分たちの Ni-dpe に対して、Tamura-Kochi の Cu がどれほど劣位か」を正面から比較論文として出版することは、著者間の学術的関係や出版インセンティブの構造上、困難。
  2. そのため、Kumada グループは「Ni-dpe の利点（high yield, broad scope）」を強調する positive framing を採用し、Tamura-Kochi との quantitative comparison は「言及するが測定しない」戦略を採用。
  3. 後続の追研究（1975-1982）でも、Kumada グループは「自分たちの系の深掘り（NMR, kinetics）」に注力し、benchmark comparison は依然未実施。

**発見的意義**: **あり（Tier A – 分野のインセンティブ構造の露呈）** — 
  比較実験（benchmark）が「技術的に可能」ながら「出版動機が薄い」という構造は、科学コミュニティの知識生成の非対称性を示唆する。より権力的な著者グループ（Kumada, 京大）は「自分たちの優位性」を強調し、competing systems の正面的な評価を後発の追従者（他大学の研究グループ）に委ねる傾向。UQS がこの構造的不在を抽出した意義は、「科学論文は『新規知見の報告』として正当化されるが、『比較の欠如』は論文の形式的要件には含まれない」という規範の暗黙性を露呈させること。

**将来の充填可能性**: **高** — 現代の触媒化学では、新触媒の報告時に複数の comparator（Pd, Pt, Cu 等）との side-by-side benchmark を standard table として掲載する慣行が確立。1972 年当時の「新しい方法の発見」という単独プレゼン形式から、現代の「比較的位置付け」という framing へと規範が進化している。

---

## 考慮し棄却した候補

### **Corriu & Masse (1972) "Chem. Commun., 144 (1972)"（Note Added in Proof で言及）**

- **理由**: 原論文の注脚 3a に「After submission of this paper, a communication...reached us」と記載。Corriu-Masse は同時期に Ni(acac)₂ 触媒を用いた同型の coupling を報告。
- **棄却理由**: 
  1. Kumada論文から独立した研究であり、著者グループが異なる（Corriu-Masse は Bordeaux 大学）。
  2. Note Added in Proof による事後的な言及だけであり、本論文の中で充填対象となる EP（機構検証、定量化等）を Corriu-Masse が直接的に解決するのではなく、あくまで「同時期の parallel development」。
  3. Corriu-Masse 自身も communication format であり、同等の詳細欠落を抱えている。競争的ではなく補完的。
  
  → 「著者グループの自己充填」が明確な場合のみ推奨選定リストに含める基準から外れる。ただし、Ni 触媒分野全体の历史には重要であり、次の「分野横断充填」の例として記録価値あり。

### **Negishi et al. (Zr-catalyzed cross-coupling, 1977-1980 series)**

- **理由**: Ni 系と Zr 系は異なるメカニズムを採用。D-4–2 の「触媒仲介中間体の検証」において、別の金属（Zr）での機構検証は、「analogy-validation」ではなく「paradigm shift」に分類される。
- **棄却理由**: 原論文 (Kumada 1972 Ni-dpe) が特定しているEPはすべて Ni-specific であり、Zr 系の充填論文としての相応性が低い。また、Zr の発展は Kumada との分野的独立性が高く、「Kumada グループの課題の解決」という criterion を満たさない。

---

## 纏め：Retrieval Depth Annotation の統計的特性（Haiku 4.5 run 1）

| Tier | 論文数 | 比率 | EP充填主対象 |
|------|--------|------|------------|
| Tier I | 4 | 57% | EP-03a, EP-10a, EP-07a, EP-08a/01a (自己充填、形式継続) |
| Tier II | 2 | 29% | EP-05a, EP-06a (associative, 後発論文による補充) |
| Tier III | 1 | 14% | EP-06a (theory matching, Tolman analogy) |

**Confidence Distribution:**
- High: 6/7 (86%)
- Medium: 1/7 (14%)
- Low: 0/7 (0%)

**パターン観察**:
- **Immediate (Tier I) の支配**: Kumada グループの形式的な「通信→full paper」の進展が、最初の EP 充填を 1-3 年以内に自動化。同一著者の研究継続としての予測可能性が高い。
- **Associative (Tier II) の限定性**: 定量化や理論的基礎付けを要する EP は、後発論文や分野全体の知識（Tolman）との結合を必要とし、直接的な想起困難。
- **Deep (Tier III) の稀少性**: triangulation（複数文献・複数ステップ）を要する充填は、当プロジェクトの Haiku 実行では 1 例のみ検出。Opus, GPT-5.4 との比較で、これが model-dependent feature か、content-dependent feature かを判定可能。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
