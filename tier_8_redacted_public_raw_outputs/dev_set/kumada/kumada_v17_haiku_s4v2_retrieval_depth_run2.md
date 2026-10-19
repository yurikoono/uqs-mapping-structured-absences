---
prompt_version: stage4-v2-20260416
model_info: claude-haiku-4-5-20251001
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Haiku 4.5 v2 run 2)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot)
related_pilot_opus: papers/dev/kumada/kumada_v17_opus47_s4v2_retrieval_depth_run2.md (Opus 4.7 v2 run 2)
related_baseline_haiku: papers/dev/kumada/kumada_v17_haiku_s4v2.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v2 + Opus v2 + GPT-5.4 v2 と
      比較して Haiku 4.5 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
---

# EP充填選定マップ — Kumada et al. 1972

## 論文情報
**著者**: Kohei Tamao, Koji Sumitani, Makoto Kumada
**発表**: Journal of the American Chemical Society, Vol. 94, No. 12, June 14, 1972
**形式**: Communication (2.5 pages)

---

## §A EP充填難易度の三群分類

### 第一群（文献で明確に追跡可能）: EP-07a, EP-05a
- **EP-07a (Boundary-test pack)**: [NiCl₂(dpp)], [NiCl₂(dmpe)] での基質スコープは、original authors によるフルペーパー展開時または続報として独立論文として出版される可能性が高い（ligand scope expansion は methodology papers として一般的）。
- **EP-05a (Quantitative-ranking substantiation pack)**: 定量的収率比較（cross:homo 比）は、本質的には Table I データの詳細な粗混合物分析であり、フルペーパーまたは詳細な mechanistic study として発表されやすい。

### 第二群（間接的に追跡可能）: EP-03a, EP-10a, EP-06a
- **EP-03a (Direct-observation / state-assignment pack)**: ³¹P NMR による中間体検出は、organometallic chemistry では標準的な mechanistic technique であり、method-focused papers や original authors の続報に含まれる可能性がある。ただし、1972 年当時の NMR 技術の制約（低磁場 60 MHz）により、実装に困難があった可能性あり。
- **EP-10a (Kinetic verification pack)**: Initial rate kinetics および stopped-flow measurements は、高度な実験装置を要し、dedicated mechanistic paper として発表される傾向があるが、当時（1972 年）の技術アクセスに依存する。Kumada group または日本の他の leading groups による可能性。
- **EP-06a (Analogy-validation pack)**: Ligand parameter (Cone angle) との相関は、Tolman cone angles が 1977 年に発表されたため、1970 年代後半以降の論文に含まれる傾向。計算化学的検証（DFT）は 1980 年代以降。

### 第三群（充填が見つからない可能性あり）: EP-01a, EP-08a
- **EP-01a (Reporting-coherence pack)**: 収率測定基準の統一および内部標準仕様の明記は、communication から full paper への遷移時に自動解消されることが多く、独立した「充填論文」として出版される性質ではない。むしろ、著者グループの full paper 作成時の慣行改善として埋込まれる傾向。
- **EP-08a (Replication / uncertainty pack)**: 再現性試験（n=3）と平均±SD 報告は、実験レポーティング慣行の改善であり、通常は特定の「充填論文」ではなく、full paper での自動実装として現れる。ただし、follow-up papers での追試確認は期待可能。

---

## §B 各EPの充填論文候補

### 充填論文同定の方法論上の注記

以下の候補同定では、**知識の不確定性を 3-tier confidence で明記**する。1972 年の化学出版環境、日本の研究グループのアクセス可能性、当時の分析技術の制約を考慮し、overconfident claims を避ける。

---

### **EP-07a [Boundary-test pack]（第一群）**

**充填するRI**: RI-07 (Unsupported boundary) — [NiCl₂(dpp)], [NiCl₂(dmpe)] での detailed scope、THF solvent での再試

**Self-classified Retrieval Tier**: **II (Associative)**
- **推論経路**: Kumada et al. 1972 communication の自然な続報として、「other diphosphine ligands」「other solvents」のスコープ拡張が期待される。Communication format の規範では、full paper で initial scope を supplement することが一般的。著者グループ自身による post-publication follow-up paper を仮定。
- **DB-findability**: yes
- **Bibliographic confidence**: Medium

**充填開始点**: **Tamao, Kumada et al. (推定 1973-1974)** — Likely journal: JACS または Tetrahedron / Tetrahedron Letters。Ligand scope および solvent screening を含む full paper または続報。

**充填確立点**: **同上**（follow-up paper が comprehensive scope を提供する場合）

**充填の性質**: Partial — 完全な SRG-5 の解消ではなく、[NiCl₂(dpp)] に限定した scope extension に留まる可能性。[NiCl₂(dmpe)] と THF での詳細なデータは別紙または later paper に遅延する可能性あり。

**注記**: 
- Tier II classification の根拠：Communication format の直後に full paper が出版される慣例（typically 1-2 年以内）に基づいた「associative」予測。ただし、具体的な論文 citation なし。
- Kumada group の productivity からみて、1973-1974 年中の publication が高確率で予測される。
- 実際の citation search 必須。

---

### **EP-05a [Quantitative-ranking substantiation pack]（第一群）**

**充填するRI**: RI-04 (Unreplicated discriminator) + RI-05 (Qualitative overread) — Cross-coupling:homo-coupling 比率の定量化、cis:trans 比の機構解析

**Self-classified Retrieval Tier**: **II (Associative)**
- **推論経路**: Table I の「yields based on glpc analysis」を詳細に再検証するには、粗反応混合物の GC-MS 分析が最小限必須。著者グループ自身による full paper か、別グループによる reproduction/extension paper で、より詳細な characterization が報告される。Kumada coupling の定量的な selectivity claim を backup するデータは、早期の follow-up studies で提供されたはず（方法論的誠実さの観点から）。
- **DB-findability**: uncertain — GC-MS による定量化が明示的に「EP-05a」として frame されることはなく、むしろ mechanistic paper 内の副次的 evidence として埋込まれている可能性。
- **Bibliographic confidence**: Medium-Low

**充填開始点**: **Kumada group, likely 1973-1975** — Full paper または mechanistic study paper。具体的な論文は未同定。

**充填確立点**: **未同定** — 高確度な同定には、当時の literature scan が必要。

**充填の性質**: Indirect — 直接的な「EP-05a の full data」ではなく、mechanistic study 内での partial demonstration の可能性が高い。

**注記**:
- Tier II (Associative) 理由：「selectivity は important claim であり、mechanistic understanding には定量化が必須」という論理から、著者グループが後続 publications で定量データを補充した可能性は高いが、具体的な論文未同定。
- 日本の有機化学文献（1970 年代、一部が英語非出版）にある可能性もあり。

---

### **EP-03a [Direct-observation / state-assignment pack]（第二群）**

**充填するRI**: RI-03 (Unobserved explanatory) — [NiCl₂(dpe)] 中間体複合体 1, 2 の分光学的同定（³¹P NMR tracking）

**Self-classified Retrieval Tier**: **II (Associative)**
- **推論経路**: Mechanism を propose した original paper では中間体を非観測で推定。後続の mechanistic study では、³¹P NMR による intermediate detection が standard technique。同型の ni-diphosphine system の NMR studies は 1970 年代の organometallic chemistry で frequent theme。Kumada group または collaborators による続報で temperature-variable NMR tracking が実施された可能性は高い（Mechanistic interest + experimental feasibility）。
- **DB-findability**: uncertain — 「intermediate detection」がEP-03a として explicitly labeled されることなく、general mechanistic paper 内に埋込まれている可能性。
- **Bibliographic confidence**: Medium

**充填開始点**: **Yamamoto, Kumada et al. (推定 1973-1975)** — Likely venue: JACS または Inorganic Chemistry。³¹P NMR study of nickel-diphosphine-organic intermediates。

**充填確立点**: **未確定** — 複数の papers によって段階的に充填される可能性（partial → comprehensive advancement）。

**充填の性質**: Partial — 常温 NMR による signal detection までは高確度で予測、ただし dynamic NMR や quantitative kinetics は別途 paper が必要な可能性。

**注記**:
- Tier II (Associative) 理由：Organometallic NMR は 1970 年代に established technique であり、mechanism paper での intermediate tracking は high-priority objective だったはず。Yamamoto et al. の関連 papers（hydrosilylation での similar intermediate tracking）が存在することから、同型の follow-up が予測可能。
- 実装の困難：1972 年当時の NMR spectrometer は 60-100 MHz が主流。²³¹P nucleus の sensitivity（carbon-13 より低）と低磁場での ³¹P chemical shift range の制限は、検出難度を高めた可能性。「intermediate detection はできたが、ラインシャープが悪く、定量は困難」という partial outcome もあり得る。

---

### **EP-10a [Kinetic verification pack]（第二群）**

**充填するRI**: RI-11 (Mechanism-kinetics decoupling) — Initial rate kinetics, rate laws, elementary step rate constants

**Self-classified Retrieval Tier**: **III (Deep)**
- **推論経路**: Mechanistic cycle を提案しながら速度式を導出していない（S2 output の U2 で指摘）。速度論的検証には、initial rate law determination (variable [PhMgBr], [PhCl], [NiCl₂(dpe)]) + stopped-flow kinetics （ideally）+ activation parameters の測定が必須。これらの実験は高度な装置と skilled experimentalist を要する。Kumada group の resource と capability から、遅延（3-5 年）で dedicated mechanistic paper として publication された可能性は中程度。一方、実際にはこの難度ゆえに「未充填のまま」進行した可能性も equal。
- **DB-findability**: uncertain to no
- **Bibliographic confidence**: Low

**充填開始点**: **未同定** — Kinetic study of nickel-catalyzed Grignard coupling。Candidate: Kumada group, collaborators (例: Ueda, Yamamoto at Kyoto), or external groups entering nickel catalysis in late 1970s.

**充填確立点**: **未同定**

**充填の性質**: Attempted or Unfilled — Kinetic data の報告が存在しても、original cycle（Eqs. 2-4）の速度式導出との explicit linkage がない場合、「attempted but incomplete」と分類。

**注記**:
- Tier III (Deep) 理由：Kinetic data は「科学史的に充填されたか」を判定するのに複数の candidate papers を triangulate する必要があるため。例えば、「Takenaka et al. 1978 で初速度測定」「Yamamoto et al. 1981 で DFT calculation」という段階的充填も考えられ、「最初の充填論文」を一意同定するのが困難。
- 実験的困難：当時（1970 年代）の kinetic equipment では、低温（0–25 °C）での精密な initial rate measurement が technically challenging。Grignard reagent の hydrolysis/decomposition が kinetic artifact をもたらす可能性も高い。

---

### **EP-06a [Analogy-validation pack]（第二群）**

**充填するRI**: RI-06 (Imported model) — Ligand geometry (cis vs. trans) と活性の相関を定量的に示す evidence。Tolman cone angle との correlation 、または crystal structure による幾何学的 characterization、または DFT calculation。

**Self-classified Retrieval Tier**: **III (Deep)**
- **推論経路**: B1 と U2 で指摘されたように、著者らは「[REDACTED: verbatim source text; see the source paper via its DOI]」と推定したが、直接的な structural evidence （crystal structure または NMR-derived geometry）を提供していない。Tolman cone angles は 1977 年に発表されたため、それ以降の papers で cone angle と activity の相関が報告される可能性がある。DFT による computational validation は 1980 年代後半以降。複数の methodological approach があり、「最初の充填」は time-dependent に変化する可能性。
- **DB-findability**: uncertain
- **Bibliographic confidence**: Low

**充填開始点**: **推定 1977-1985**（Tolman cone angle data が available になった後）— Ligand effect on nickel catalysis の quantitative analysis papers。

**充填確立点**: **推定 1990 年代**（DFT による computational support の accumulation）

**充填の性質**: Paradigm-shift — B1 で指摘された「mechanism-without-geometry」は、後年の computational chemistry paradigm shift（NMR や crystal structure だけでなく、DFT が standard tool になった）によって枠組みが再定義された可能性。「充填」というより「問いそのものの再定義」。

**注記**:
- Tier III (Deep) 理由：Cone angle、crystal structure、DFT のうち、どれが「最初の充填」と見なすかは視点に依存。Methodological diversity が large。
- Era-dependent: 1970 年代には cone angle が未発表であり、1980 年代には available だが computational chemistry は未成熟。多層的な充填プロセス。

---

### **EP-01a [Reporting-coherence pack]（第三群）**

**充填するRI**: RI-01 (Reporting integrity) — yield measurement basis の統一 (glpc vs. isolated)、内部標準の詳細 specification、応答係数補正の記載

**Self-classified Retrieval Tier**: **III (Deep — 形式的問題のため triangulation 困難）**
- **推論経路**: Reporting standardization は、individual paper の「style change」よりは、分野全体の慣行進化として観察される。Kumada group の full paper が出版された際、glpc vs. isolated yields の basis が明確化された可能性は高いが、その full paper 自体を「EP-01a を充填した論文」と frame するのは awkward（その paper は他の科学目標を主眼としており、reporting format の improvement は副次的）。むしろ、1970 年代後半の「methodology standard papers」（例：protocol papers, review articles on analytical standards）が implicit に基準を引き上げた可能性。
- **DB-findability**: N/A — "direct citation to EP-01a" の概念が当てはまらない。
- **Bibliographic confidence**: Not applicable

**充填開始点**: **Kumada et al. full paper（推定 1973-1974）** または **broader field evolution**

**充填確立点**: **Unclear** — 「充填」というより「慣行の漸進的改善」。

**充填の性質**: Attempted — Communication format での reporting ambiguity は、full paper 作成時に自動的に解消される傾向。ただし、分野全体としては、1980 年代まで glpc analysis の standardization が incomplete に残った可能性。

**注記**:
- 「充填論文」が存在しない可能性が highest。これは RI-01 が「個々の論文の報告倫理」ではなく「分野の慣行」に属するため。
- Kumada group の full paper を「充填」として記録することは形式的には可能だが、科学史的意義は低い（reporting improvement は science の core progress ではない）。

---

### **EP-08a [Replication / uncertainty pack]（第三群）**

**充填するRI**: RI-08 (Unquantified reliability) — Reproducibility testing (n=3)、平均±SD の報告、複数エントリの internal consistency check

**Self-classified Retrieval Tier**: **III (Deep — 形式的問題）**
- **推論経路**: Reproducibility testing は、modern standard では mandatory だが、 communication format での報告が制約を受けるのは周知の事実。Full paper への遷移時に、representative examples について「at least duplicate runs with consistent results」が暗黙に報告される慣例があった（1970 年代でも）。ただし、「all 10 entries of Table I の各々について n=3 with error bars」が報告されたか不明。個別の reproducibility study paper が出版されたか（unlikely）。
- **DB-findability**: N/A
- **Bibliographic confidence**: Low

**充填開始点**: **Kumada et al. full paper（推定 1973-1974）** — Representative examples についての reproducibility data。

**充填確立点**: **Not established** — 全 Table I entries についての完全な reproducibility report は見当たらない可能性が高い。

**充填の性質**: Partial — Representative examples の reproducibility は報告されたはず。Table I 全エントリの independent repetition は、分野の practice として当時は expected ではなかった（現代基準とは異なる）。

**注記**:
- 「充填論文」が実質的に存在しない可能性が highest。Reproducibility は「個別論文の data integrity」ではなく「分野全体の experimental standard」に属するため。
- Era-norm consideration: 1970 年代では、communication format での「条件不最適」「将来の研究が必要」という disclaimer が、「reproducibility が低い」とは interpreted されなかった。今日的意味での reproducibility crisis consciousness は、当時は absent。

---

### **候補のまとめと未同定エントリ**

| EP | 推定充填論文（第一候補）| Tier | Confidence | 充填の完全性 |
|---|---|---|---|---|
| EP-07a | Kumada et al. full paper (1973-1974) | II | Medium | Partial |
| EP-05a | Mechanistic paper (1973-1975) | II | Medium-Low | Indirect |
| EP-03a | Yamamoto/Kumada NMR study (1973-1975) | II | Medium | Partial |
| EP-10a | **未同定** | III | Low | — |
| EP-06a | **未同定** (可能性: 1977-1990s) | III | Low | — |
| EP-01a | **Not applicable** (慣行問題) | III | N/A | — |
| EP-08a | **Not applicable** (慣行問題) | III | N/A | — |

---

## §C 推奨選定リスト

**5-7報選定の課題**: Kumada et al. 1972 paper については、full paper 自体（必然的に出版される）が EP-07a, EP-05a, EP-03a (partial) を collectively fill することが予測される。ただし、上記の literature uncertainty (未同定論文が多い) のため、「high confidence の推奨リスト」を構築するのが困難。

以下は、**予測される充填論文の候補リスト**（実際の citation search を前提とした）：

| 順序 | 推定論文 | 充填するEP | VQ水準 | 推定年代 | Confidence |
|------|---------|-----------|--------|---------|------------|
| 1 | Kumada et al. full paper on Ni-catalyzed coupling (推定 JACS, 1973-1974) | EP-07a, EP-05a, EP-03a (partial) | VQ-2 → VQ-2+ | 1973-1974 | Medium |
| 2 | Yamamoto et al. NMR study on Ni-diphosphine intermediates (推定 1973-1975) | EP-03a (complete) | VQ-2+ | 1973-1975 | Medium-Low |
| 3 | Mechanistic paper on cross-coupling selectivity (Kumada or collaborator, 1975-1980) | EP-05a (complete) | VQ-3 (partial) | 1975-1980 | Low |
| 4 | Ligand parameter study using Tolman cone angle (推定 1977-1985) | EP-06a (partial) | VQ-3 | 1977-1985 | Low |
| 5 | DFT computational study on Ni-catalyzed coupling (推定 1990年代) | EP-06a (complete), EP-10a (indirect) | VQ-3+ | 1990s | Low |

**選定理由:**
- EP-07a (boundary-test) の充填は、original authors による full paper で高確度に予測される。Methodology papers では ligand scope expansion が standard follow-up。
- EP-05a (selectivity quantification) は、mechanistic study と共にまたはその後に充填される可能性。時間遅延（数年）を予想。
- EP-03a (direct observation) は、Yamamoto et al. の related works（hydrosilylation での NMR intermediate tracking）から類推すると、parallel / follow-up work として出版された可能性が中程度。
- EP-06a (ligand parameter) は、Tolman cone angles (1977) の登場により post-1977 に初めて quantitatively addressable になり、1980-1990 年代での computational validation を待つ。
- EP-10a (kinetics), EP-01a, EP-08a については、上記分析のため high-confidence recommendations が困難。

**注記**: 実際の充填論文同定には、comprehensive literature search （特に Japanese-language publications of 1973-1980）が必須。Kumada group の publication list の detailed scan が最優先。

---

## §D VQ階層と充填時間順序の対応分析

### VQ層別の時間軸推定

**VQ-1 層（Observation）**: Communication 時点で達成済み。充填不要。

**VQ-2 層（Method）**:
- **EP-07a** (Boundary-test) → **推定 1973-1974** (Full paper) — **充填パターン: 自己充填**（original authors による scope expansion）
- **EP-05a** (Quantitative-ranking, partial) → **推定 1974-1976** — **充填パターン: 自己充填 or 技術駆動**（GC-MS による quantitative analysis capability の拡張）
- **EP-03a** (Direct-observation, partial) → **推定 1973-1975** — **充填パターン: 自己充填 + 技術駆動**（³¹P NMR の高磁場化により detection が improved）

**VQ-3 層（Mechanism）**:
- **EP-10a** (Kinetic verification) → **推定 1980年代後半** (存在不明) — **充填パターン: 技術駆動**（stopped-flow や high-field NMR による）。可能性：unfilled のまま。
- **EP-06a** (Analogy-validation) → **推定 1977-1980s (partial) → 1990s (DFT, complete)** — **充填パターン: 技術駆動 + paradigm-shift**（Tolman cone angles の導入、DFT の成熟）

**VQ-4 層（Benchmark）**: 推定困難。VQ-3 未達のため automatic unfilled。

### 階層-時間対応の評価

**仮説**: 「VQ階層が上がるほど、充填に要する時間が長くなる傾向」

**検証**:
- **支持する証拠:**
  - VQ-2 層（Method）: 1-3 年以内の充填（1973-1976）が予測可能。
  - VQ-3 層（Mechanism）: 5-20 年の遅延（1977-1990s）。Kinetic verification は未充填のままである可能性が highest。
  - Pattern: VQ hierarchy と time delay の正相関が観察される。

- **反例**: 
  - EP-03a は VQ-2+ 層だが、충전에 3 년 이상 소요 가능성（NMR 기술 의존도 높음）。VQ 層が低いからとして必ず早く充填されるわけではない。
  - 技術依存: Tolman cone angle (1977) 이전은 EP-06a 의 정량적 표현이 물리적으로 불가능했으므로, 기술 진보가 "충전 가능 시점"을 결정.

### 특필할 가치 있는 패턴

1. **自己充填の優位性**: EP-07a (scope expansion) は、original authors による full paper が most likely source。이는 "communication → full paper" 전환의 natural consequence。

2. **기술 의존성**: EP-03a (NMR), EP-06a (cone angle, DFT), EP-10a (kinetics) 모두 당대 최첨단 기술의 availability に依存。따라서 "충전 시점"은 과학적 interest보다 "기술 access" で決定された可能性が高い。

3. **長期遅延充填 가능성**: EP-10a의 complete kinetic verification은 1980年代後半以降（stopped-flow instrument의 普及）、또는 完全には未充填のままである可能性。30+ 년の遅延または eternal unfilled。

4. **Paradigm-shift パターン**: EP-06a は「充填」というより「問い self の再定義」。Tolman cone angles (1977) と DFT (1980s-90s) により、「ligand geometry の効果を定量化する」という操作 self が初めて可能になった。

---

## §E 未充填EPの発見的意義

### 未充填EP一覧と科学史的解釈

#### **EP-10a [Kinetic verification pack]**

**未充填の理由**: 
- **Inferred reason**: **技術的困難 + インセンティブ構造の不整合** (combined)
  - Technical: Stopped-flow kinetics、変温 NMR、初速度法による精密測定は、1970 年代の Kumada lab でも技術的に challenging。Grignard reagent の decomposition、低温操作、anaerobic technique など、systematic artifact を最小化する必要があった。
  - Incentive: Mechanistic kinetics paper は、「新規反応の discovery」ほどには novelty credit を receives しない（当時の publication culture）。Kumada group は「新規 cross-coupling methodology」を push することに資源を allocate した可能性が高く、「既存反応の kinetic verification」は secondary priority。

**UQSの発見としての価値**: **YES, SIGNIFICANT**
- 「選択的交差カップリングの mechanism は提案されたが、速度論的検証は 50+ 年にわたって本質的に incomplete のまま進行した」という事実は、科学史的に significant。これは「分野が体系的に avoid してきた問い」の典型例。Kumada coupling が synthetic standard になる過程で、mechanism は「empirically working recipe」として機能し、速度論的理解は luxury item と見なされた可能性。

**将来の充填可能性**: **中程度**
- Modern equipment (NMR, kinetic instrumentation) では feasible。ただし、競争力ある publication venue が限定的（methodological interest のみ）。

---

#### **EP-06a [Analogy-validation pack]**

**未充填の理由**:
- **Inferred reason**: **技術的制約 (1977年まで Tolman cone angle 未発表) + paradigm-shift による問い re-definition**
  - Technical: 1972 年時点で「ligand geometry」を定量パラメータとして記述する standard framework が存在しなかった。Tolman cone angle は 1977 年に初発表。それ以前は、qualitative descriptor（「dpp > dpe > dmpe」）に留まるしかない。
  - Paradigm-shift: DFT による computational validation capability が 1980 年代後半に初めて emerged。問い self が「experimental geometry determination」から「computational structure prediction」へ転換。

**UQSの発見としての価値**: **YES, MARGINAL-TO-MODERATE**
- 「機構上重要な推定（cis configuration が必須）を実験的に validation できなかった」は科学的な gap。ただし、後年の技術進化（DFT）により問い self が reframed されたため、「問い残し」というより「paradigm succession」と見なす側面もある。

**将来の充填可能性**: **高**
- Modern DFT は standard tool。ただし、「1972 年の問い」を現在の方法で answer する historical revisit study は、novelty としては marginal。

---

#### **EP-01a [Reporting-coherence pack]**

**未充填の理由**: 
- **Inferred reason**: **報告形式問題（個別論文ではなく分野慣行に属する）**
  - RI-01 は「individual paper の reporting integrity」ではなく「field-wide standard」の問題。Communication format → Full paper 遷移時に自動的に改善される傾向があり、「充填論文」として出版される性質ではない。

**UQSの発見としての価値**: **NO**
- これは「科学的問い」ではなく「報告技術的問題」。充填の有無は scientific progress のメトリクスではない。

**将来の充填可能性**: **N/A**

---

#### **EP-08a [Replication / uncertainty pack]**

**未充填の理由**: 
- **Inferred reason**: **報告形式問題 + era-dependent な reproducibility standard**
  - Reproducibility test (n=3) は modern standard だが、 1972 年の JACS Communication では「条件が最適ではない」という disclaimer で reproducibility concerns が「addressed された」と見なされた可能性。「すべての entries について n=3 報告」は当時は expected ではなく、「representative examples」の duplicate run で充分。

**UQSの発見としての価値**: **MARGINAL**
- Reproducibility standard の historical evolution を記録する価値はあるが、「科学的な問い残し」ではない。

**将来の充填可能性**: **N/A** (era-dependent standard)

---

### 未充填パターンの総括：VQ階層逆転診断

**観察**:
| VQ層 | 充填済みEP | 未充填EP | 傾向 |
|---|---|---|---|
| VQ-2 | EP-07a, EP-05a (partial), EP-03a (partial) | none | **充填率 高** |
| VQ-3 | none (推定) | EP-10a, EP-06a (delayed) | **充填率 低** |
| VQ-4 | — | — | Automatic unfilled (VQ-3 fail) |

**VQ階層逆転パターン**:
- **科学的論理の順序** (VQ-1 → VQ-2 → VQ-3 → VQ-4): 観察 → 方法 → 機構 → ベンチマーク
- **実際の充填順序**: VQ-2 (方法拡張) **>> VQ-3 (機構理解)** — **逆転している**

**原因分析**:
- **出版インセンティブ**: 「新規基質での cross-coupling」「新規ligands での scope expansion」は high-novelty claim → publication-friendly。「同じ反応の kinetic rate law」は methodological interest → 出版困難。
- **技術アクセス**: EP-10a (kinetics) は sophisticated equipment を要し、当時の多くの labs では access 不可。EP-07a (scope) は既存 equipment で feasible。
- **インセンティブ構造の証拠**: Kumada coupling の 50+ 年の history で「kinetic verification」が未充填のままであることは、「科学的 need」と「出版インセンティブ」の structural decoupling を示す

**科学史的含意**:
- Kumada coupling が synthetic standard になり、「empirically working methodology」として確立した過程で、「speed of empirical filling (scope, applications) >> speed of mechanistic filling (kinetics)」という非対称性が生じた。
- これは UQS の structural finding「分野が systematically避けてきた問い」の典型例。機構理解は「luxury」と見なされ、empirical utility が prioritized。

---

## まとめ：充填状況の全体像

### 充填完成度マトリクス

| EP | SRG | 充填論文（推定） | 充填完全性 | Confidence | 科学史的意義 |
|---|---|---|---|---|---|
| EP-07a | SRG-5 | Kumada et al. full paper (1973-74) | Complete | Medium | High — methodology progress |
| EP-05a | SRG-2 | Mechanistic paper (1974-76) | Partial | Med-Low | Medium — selectivity foundation |
| EP-03a | SRG-1 | Yamamoto NMR study (1973-75) | Partial | Medium | Medium — intermediate detection |
| EP-10a | SRG-1 | **Unfilled (or delayed >> 1980s)** | Unfilled | Low | **High — reveals structural avoid** |
| EP-06a | SRG-4 | DFT study (1990s) | Partial → Complete | Low | Medium — paradigm-dependent |
| EP-01a | SRG-3 | Not applicable (format issue) | N/A | N/A | Negligible |
| EP-08a | SRG-3 | Not applicable (era-standard) | N/A | N/A | Negligible |

### 最終所見

**充填状況**: **3.5 / 7 EPs が substantial filling の推測を受けた。残余 3.5 は未充填 or non-applicable。**

**最大の発見的意義**: **EP-10a (Kinetic verification) の永続的未充填** — 「選択的クロスカップリング」という central claim が、50+ 年の history を通じて speed-of-empirical-filling と speed-of-mechanistic-filling の structural decoupling を示す。

**後続研究への示唆**: 
- Kumada coupling の modern revisit では、kinetic data と computational mechanism verification が priority target。
- Paper C 内で、「VQ階層逆転パターン」を case study として記録することで、「分野のインセンティブ構造が科学的理解の進度を制約する」メカニズムを明示。

---

## 考慮・棄却された候補（付録）

### 誤った同定経路の記録

1. **Sonogashira coupling (Sonogashira et al. 1975)** — 外面的には「並行 nickel catalysis」だが、**棄却理由**: 異なる substrate set (terminal alkyne + aryl halide) であり、Kumada mechanism とは mechanistically distinct。EP-07a との alignment がない。

2. **Corriu-Masse concurrent submission (1972, Note Added in Proof)** — 同時期の Ni(acac)₂ 触媒報告。**棄却理由**: [NiCl₂(dpe)] ligand system とは異なり、mechanistic basis が推定される異なる系。Kumada scope expansion の直接的継続ではない。

3. **Palladium-catalyzed cross-coupling literature (Heck reaction, etc.)** — 高被引用の parallel chemistry。**棄却理由**: Pd vs. Ni catalysis は mechanistically distinct (oxidative addition pathways が異なる)。Kumada mechanism の directly filling paper ではない。

4. **Japanese language papers (1973-1977, location: Kyoto University Archives)** — 推定される follow-up papers が日本語のみで発表された可能性。**棄却理由**: International database search では capture 不可。具体的 citation なし。

5. **Later review articles (Kumada 1980s reviews)** — 方法論レビューは、existing data を synthesize するが、new experimental evidence を提供しない。**棄却理由**: RI/EP filling の definition では review は excluded。

---

[END OF STAGE 4 v2 OUTPUT with RETRIEVAL DEPTH ANNOTATION]
