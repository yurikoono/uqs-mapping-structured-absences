prompt_version: stage3-v4-20260427
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Jones et al. 2005（Chem. Commun. 2005, Communication, DOI: 10.1039/b504996b）

### §1 Claim Architecture

**コア主張：** 4,4',4''-トリ-tert-ブチルテルピリジン（tpy'）を配位子として用いることで、Ni(I)–アルキル錯体（1b）とNi(II)–アルキルハライド錯体（2a）を安定単離し、アルキルクロスカップリングの鍵的素過程の機構的プローブとして使用した。2aのX線結晶構造解析により「σ結合型Ni(I)–アルキル錯体とその一電子酸化対が構造決定された第二例」という構造的新規性を確立した（Novelty柱）。化学量論的実験（式3: 8%收率、テトラデカン30%）から「トランスメタル化によりNi(II)–ジアルキル中間体を与える経路は主経路でない」という機構的帰結を導いた。tpy'システムはtpyより高いGC收率を与える（Utility柱）。

**Layered structureの判定：** 独立3層構造あり。
- **層1（構造化学）**: 1bと2aの合成・同定・XRD構造（2a）——機構解釈の真偽とは独立。
- **層2（機構的帰結）**: 式(3)(4)の化学量論的実験から「トランスメタル化でない」という結論——層1の成立を前提とし、かつon-cycle検証が省略されている。
- **層3（触媒性能）**: Table 1のtpy'触媒によるGC收率改善——層2の機構解釈から独立して成立する経験的主張。

層2が単一の反証実験（条件マッチした化学量論実験でも収率が同様に低い、またはトランスメタル化が実際に起きる）で崩れうる一方、層1と層3は独立して成立する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [マスバランス未閉鎖]**（B-2, U-1, B-9）

* **Primary RI**: RI-01 [Reporting integrity] — 式(3)のGC收率（クロスカップリング8% + テトラデカン30% = 38%）が全炭素の62%を未帰属のまま放置しており、機構的帰結（「トランスメタル化でない」）を支持するデータセットとして横比較不可能。
* **Secondary RI**: RI-08 [Unquantified reliability] (内部矛盾型サブタイプ) — GC値の取得精度（n未報告、SD未報告、内部標準未明示）が不明であり、「8%のみ」という値の信頼性が評価できない。
* **ER**: 化学量論実験が機構的主張の根拠となる場合、全生成物（クロスカップリング体・ホモカップリング体・β-H脱離生成物・未反応出発物・Ni含有残分）を定量的に報告し、炭素（および亜鉛）のマスバランスを閉鎖する。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: 式(3)（2a + 5等量 n-HepZnBr, THF, RT）の実験を繰り返し（n≥3）、GC内部標準（ドデカン等）で全生成物収率を定量。未反応HepZnBrをGCまたは¹H NMRで定量。Ni含有残分をESI-MSまたはICP-OESで確認し、炭素バランスを≥90%閉鎖する。
* **注記**: B-2 (3/3高収束)、U-1 (self-contradictory absence)、B-9 (反応速度データ不在) が収束。TEMPERATURE_SUMMARY: high_convergence_low_gap (B-2, 3/3)。U-1 severity=high。

---

**SRG-2 [On-cycle位置・活性種正体]**（A-1, A-2, U-2, B-12）

* **Primary RI**: RI-03 [Unobserved explanatory] — 1bおよび2aが触媒サイクルのon-cycle中間体であることが直接観測も速度論的拘束もされていない。「機構的プローブ」という命名はon-cycle前提を意味するが、その前提は論文内で検証されない（U-2: self-contradictory absence）。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 2aの前触媒機能（entry 7, 58%）から「活性種への変換」を推定する実験が単一の条件・単一時点のエンドポイント観察に留まり、誘導期・ローディング依存性・変換速度の評価なし。
* **ER**: 1bまたは2aをon-cycle中間体と主張するには：(a) 触媒反応中でのin situ観測（EPR/UV-Vis）、または(b) 独立合成した1b/2aを添加した触媒反応と、1b/2a非添加での触媒反応の動力学比較、または(c) 前触媒ローディング依存性の速度プロファイルが要求される。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-10a [Kinetic verification pack]
* **Case-specific実装**: tpy'/Ni(COD)₂触媒によるアルキルクロスカップリング反応（Table 1エントリー4条件）の時間変化をin situ EPR（Ni(I)種の検出）またはUV-Visで追跡。または1b（0.05 equiv）を走行中の触媒反応に添加し、收率プロファイル変化を確認（on-cycle intercept実験）。
* **注記**: A-1（deferred, "more mechanistic studies are needed"）、A-2（deferred）、U-2（critical severity, V2）が収束。TEMPERATURE_SUMMARY: low_convergence_high_gap (U-2, critical)；high_convergence_low_gap (A-1, 2/3)。

---

**SRG-3 [ラジカルvs非ラジカル経路]**（A-3, B-10, C-2）

* **Primary RI**: RI-03 [Unobserved explanatory] — Ni(I)/Ni(III)経路のアルキルハライド付加（内圏vs外圏ラジカル）が直接観測も速度論的拘束も受けていない。
* **Secondary RI**: RI-06 [Imported model] — ref 12（terpyridyl–Ni/Grignard系での同位体実験「非ラジカルエタン生成」）を亜鉛求核剤/tpy'系に直接適用しているが、Grignard→Zn系での機構的同型性は論文内で議論されていない（C-2）。
* **ER**: ラジカル経路の排除には：ラジカルクロック基質（5-ヘキセニルヨウ化物）、TEMPO捕捉実験、交叉実験（²H標識基質の混合）のいずれかを実施する。ref 12の結果の適用可能性を示すには、tpy'/Zn系で同位体実験を繰り返す。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: 式(4)条件（1b + 5等量 HepI, THF, RT）においてTEMPO（2 equiv）添加実験。または5-ヘキセニルヨウ化物を求電子剤として用い、環化生成物（5-ヘキセニル → シクロペンタニルメチル）の有無でラジカル中間体を診断。
* **注記**: A-3（deferred）、B-10（"non-radical"定義不在）、C-2（ref 12の系差への言及なし）が収束。V2=high (1/3)。

---

**SRG-4 [GC収率の測定精度]**（B-1, B-9）

* **Primary RI**: RI-08 [Unquantified reliability] — Table 1全エントリーの單一GC收率値（n未報告、SD未報告）および式(3)(4)の單一GC值は再現性・不確かさを評価できない。GC内部標準の種類・校正曲線範囲も未明示。
* **Secondary RI**: RI-01 [Reporting integrity] — 收率計算基準（Ni基準 vs. 基質基準）が式(4)のみ明示され（"relative to nickel"）、式(3)とTable 1では不明確。
* **ER**: n≥3の繰り返し實験とSDの明示。GC内部標準の種類・校正曲線範囲を方法のsectionに明記。收率計算基準（limiting reagent）をすべての實験で統一して明示。
* **EP**: EP-08a [Replication / uncertainty pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: Table 1エントリー2および4（tpy' with Br/I）でn=3繰り返し，GC SD（±%)を報告。内部標準としてドデカンを使用し，応答因子を別途測定。
* **注記**: B-1（V1+V2+V3, 3/3収束; high convergence, low gap）、B-9（V2+V3）が収束。

---

**SRG-5 [錯体キャラクタリゼーション完全性]**（B-3, B-7, B-8, B-4）

* **Primary RI**: RI-02 [Object identification] — 「機構的プローブ」として中心的役割を担う1bのX線結晶構造がない（B-3）；2aの合成收率・純度が未記載（B-8）；2aが単結晶状態でbulk sampleを代表するかどうかの確認なし。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 2aの構造から得られる機構的含意（Ni–C/Ni–I結合長の解釈）が、単結晶1個の構造データに基づくが、PXRD等によるbulk確認なし。
* **ER**: 1bのX線結晶構造または等価の高分解能同定法（EPR g値 + 結晶場解析 + 元素分析）；2aの合成收率（bulk batch）とPXRD一致；1bおよび2aの電気化学（E₁/₂、ΔEp、スキャン速度依存性）を完全に報告。
* **EP**: EP-02a [Identity / purity substantiation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: 1bの単結晶X線構造（できればEPR(ν-band)スペクトルで溶液構造とのコンシステンシーも確認）。2aのPXRD（合成batch全体の純度確認）と合成後の單離收率（至少3 batch平均）。サイクリックボルタモグラム（1a, 1b, 2a）の完全提示（E₁/₂、ΔEp、スキャン速度0.01〜1 V/s）。
* **注記**: B-3（1b XRD不在; 2/3収束）、B-8（2a合成收率不明; 2/3収束）、B-7（電気化学; 2/3収束）、B-4（安定性定量なし; 1/3）が収束。

---

**SRG外：CLA（独立主張レベル付属）**

---

**CLA-1: 化学量論実験条件と触媒条件の対応性不在**（D-4-5, B-14, B-5）

* **Primary RI**: RI-05 [Qualitative overread] — 純粋錯体2aを使った式(3)（5等量RZnBr, RT, 純THF）から「触媒的tpy'/Ni系でのトランスメタル化は主経路でない」という定量的含意を導出しているが、条件差（in situ vs. 純粋錯体、COD配位子の有無、対イオン差）の影響が評価されていない。
* **Secondary RI**: RI-06 [Imported model] — 化学量論的条件（dead-end stoichiometric complex）を触媒条件（in situ複合体）のモデルとして輸入。
* **ER**: 化学量論的実験を触媒条件に揃えるか（Ni(COD)₂ + tpy' + RX → in situ 2a, then + RZnBr）、または両条件間の変数を系統的に変えた実験セットを行い、機構的帰結の条件依存性を評価する。
* **EP**: EP-06a [Analogy-validation pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: Ni(COD)₂/tpy'/PhPrI混合物（前触媒 in situ形成条件）に対して、5等量 n-HepZnBrを加えた化学量論的実験を実施し、式(3)と収率を比較。

---

**CLA-2: tpy'による收率向上の主因帰属（可溶性vs電子効果）**（D-4-6, B-11, B-7, C-1）

* **Primary RI**: RI-05 [Qualitative overread] — 収率改善の主因を「溶解性向上」と定性的に帰属（B-11）しているが、定量的溶解性測定も電子効果の分離実験も行われていない。還元電位差（-0.12 V、B-7）は電子的差異の存在を示唆するが、これが活性に与える影響は未評価。
* **ER**: tpyとtpy'のNi錯体の溶解度をUV-Vis校正曲線で測定。電子効果を分離するために、4位のt-Bu基以外の置換基（例: 4-メトキシ）を持つtpy誘導体Ni錯体を合成しTable 1条件でテストする。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: tpy/tpy'/tpy''-OMe（4-MeO-tpy）でのNi–n-Hept–I錯体系列合成 → THF中溶解度（UV-Vis, mg/mL）と触媒活性（GC收率、n=3）をTable 1条件で測定し、溶解度–收率相関と還元電位–收率相関を比較。

---

**PRI-11 適用チェック：**
本論文は式(3)(4)の化学量論的エンドポイント観察から触媒機構（「トランスメタル化でない」）を主張するが、反応速度の次数決定・活性化パラメータ・KIE・提案サイクルからの速度式の代数的導出のいずれも実施していない。PRI-11（Mechanism-kinetics decoupling）が適用される。2005年通信論文としてはera-norm tolerated寄りだが、VQ-3昇格の致命的ブロッカーである。EP-10aが最優先の充填パックとなる。

**Self-referential validation チェック（PRI-12 Cluster A）：**
本論文は新しい記述子・指標・スコア関数を提案する計算化学論文ではないため、PRI-12 Cluster Aは適用対象外。

**Deductive-retrospective structure チェック（PRI-12 Cluster B）：**
本論文は演繹的な原理提案論文ではなく、実験的観察から機構推定を行う合成・機構論文であるため、PRI-12 Cluster Bは適用対象外。

---

### §3 現在のVQ判定

**Step 3a: Modern reassessment baseline**

**VQ-1 (Observation): 達成**
- RI-02（Object identification）: 1bは複数の分析法（NMR、EPR、元素分析）でESI確認済み。XRDはないが代替同定として許容範囲。2aはXRD構造あり（bulk確認はないがVQ-1水準では非致命的）。
- 触媒生成物はGC同定（合成品との保持時間比較で構造帰属）。
- RI-02: Non-fatal → VQ-1達成。

**VQ-2 (Method): 現代基準では未達（RI-01 Fatal）**
- RI-01（Reporting integrity）: 式(3)の62%未帰属炭素が主機構的根拠の reporting coherence を破壊する。GC收率のn/SD未記載。→ Modern baseline では致命的。
- RI-07（Unsupported boundary）: 「トランスメタル化でない」という否定的境界主張が、条件マッチ実験なしの単一stoichiometric observationに基づく（RI-07拡張適用、否定的境界主張）。→ Non-fatal（"argues against"という限定的言語を使用）。
- **Modern baseline判定: VQ-2 not reached (RI-01 Fatal)**

**Step 3b: Era-norm補正**
- RI-01（マスバランス不完全）: ChemComm 2005通信論文では完全マスバランス報告の慣行がなかった。→ era-norm tolerated
- RI-08（GC收率精度）: 通信論文でのn/SD不記載は2005年の慣行。→ era-norm tolerated
- RI-07: era-norm tolerated（否定的境界主張が通信論文で常に検証されたわけではない）

**Step 3c: Final VQ judgment**

現在判定: **VQ-2 (era-norm qualified)**

- VQ-1: Achieved（RI-02 non-fatal、1bのESI多法確認 + 2aのXRD）
- VQ-2: era-norm qualified（modern baselineではRI-01 Fatalだが、ChemComm 2005通信フォーマット慣行でera-norm tolerated）
- VQ-3: Not reached（RI-03 Fatal: on-cycle status未検証；RI-04 Fatal: 単一stoichiometric experiment；RI-06 Fatal: ref 12のGrignard→Zn輸入未検証 + PRI-11適用）

**層別VQ非対称性：**
- 層1（構造化学: 2aのXRD構造）単独では: VQ-2達成（XRD + 複数分析法。RI-02 non-fatal, RI-08 non-fatal）。構造的Novelty主張はVQ-3近接（RI-03不適用、RI-04: bulk確認で非致命的化可能）。
- 層2（機構的帰結）単独では: VQ-1止まり（RI-03, RI-04, RI-06 Fatal）。
- 層3（触媒性能: Table 1）単独では: VQ-2 achieved（GC收率の era-norm tolerated RI-08内）。

---

### §4 Era-Norm Annotation

**communication-era tolerated (ChemComm 2005):**
- **B-1（单離收率なし）**: 2005年のChemComm通信論文ではGC収率による報告が標準であり、単離收率不記載は許容慣行だった。
- **B-2, U-1（マスバランス62%未閉鎖）**: 化学量論的実験でのGC以外の生成物定量は、通信フォーマットでは期待されていなかった（2005年当時の慣行）。
- **B-8（2aの合成收率不明）**: 通信論文では新規錯体の合成收率が本文から省かれることがあった（ESI参照）。
- **B-7（電気化学データ不完全）**: 電気化学データの詳細報告は通信論文のESIで十分とされていた。
- **B-9（stoichiometric反応の速度データ不在）**: 通信フォーマットでの速度論実験は「ongoing studies」として将来課題とすることが許容された。
- **B-3（1bのXRD不在）**: 通信論文フォーマットでは新規錯体の単結晶XRDが常に要求されなかった（NMR + 元素分析で許容）。

**modern-era deficient:**
- **B-2, U-1（62%未帰属炭素）**: 現代の機構論文では、機構的帰結を主張するための化学量論的実験には完全炭素バランスが要求される。62%の不帰属は式(3)の結論の根拠として現代基準では不十分。
- **RI-03（on-cycle status未検証）**: 現代の均一系触媒機構論文では、提案中間体のon-cycle証明（in situ観測またはkinetic trapping）が標準要件。1b/2aがプローブとして機能するという主張に対し、現代基準は直接証明を要求する。
- **RI-06（ref 12のGrignard→Zn analogy輸入）**: 現代の機構論文では、異なる求核剤系（Grignard vs. Zn）からの機構的類推の転用には、同型性の実証（ラジカルクロック、KIE比較等）が要求される。
- **RI-04（単一stoichiometric discriminator）**: 機構判定実験（式3）をn=1エンドポイント観察のみで実施することは、現代基準では不十分。特に mass balance が未閉鎖の場合は致命的。

---

### §5 最短補強ルート

**現在: VQ-2 (era-norm qualified)**

**第一目的関数: VQ-3 (Mechanism) 達成**
必要: RI-03 (Fatal)、RI-04 (Fatal)、RI-06 (Fatal) の解消

1. **EP-10a [Kinetic verification pack]** — ラジカルトラップ（TEMPO 2 equiv, 式4条件）+ ラジカルクロック基質（5-ヘキセニルヨウ化物を求電子剤として使用）での環化生成物定量。RI-03（ラジカルvs内圏経路未観測）、RI-04（単一discriminator）を同時前進。→ PRI-11解消の中核実験。
2. **EP-03a [Direct-observation / state-assignment pack]** — in situ EPRまたはUV-Visによる触媒反応中のNi(I)/Ni(II)/Ni(0)酸化状態モニタリング。RI-03（on-cycle status）の中核解消。
3. **EP-06a [Analogy-validation pack]** — tpy'/n-PrZnBr/tpy'Ni(II)–Alk–I系での¹³C同位体標識実験またはKIE測定（ref 12のGrignard系実験の亜鉛系等価物）。RI-06（Grignard→Zn輸入）を解消。
4. **EP-01a [Reporting-coherence pack]** — 式(3)の繰り返し（n=3）+全生成物GC定量（内部標準付き）+Ni残分ICP確認でマスバランス閉鎖。RI-01を解消し、VQ-2のmodern baselineでの達成も確立。

認定ゲート順注記：実験投入順は情報利得順（EP-10a → EP-03a → EP-06a → EP-01a）だが、最終認定はVQ-1 → VQ-2 → VQ-3の継承ゲート順で確定する。EP-03aとEP-10aが完了し、RI-03とRI-04が解消された時点でVQ-3を評価する（VQ-2のmodern baseline達成が前提）。

**第二目的関数: VQ-4 (Benchmark) 達成（VQ-3達成後）**

5. **EP-08a [Replication / uncertainty pack]** — Table 1の全エントリーをn=3で繰り返し、SD付きで報告。RI-08（GC収率精度）を解消。
6. **EP-09a [Internal benchmark pack]** — Table 1での先行Ni-アルキル系との直接比較（同一基質ペアで文献系を再現。refs 5-11のうちデータが再現可能なもの）。RI-09（外部文献値のみでの優位性主張）を解消。

---

### §6 制度設計への寄与

**1. PRI-11（Mechanism-kinetics decoupling）の追加確認事例**

jones2005は、stoichiometric endpoint observation（式3: 8%收率）から触媒機構（「トランスメタル化でない」）を主張するが、速度式の代数的導出も、反応速度次数の測定も、KIEも、ラジカル捕捉も実施していない。これはPRI-11（提案触媒サイクルまたは反応機構から速度式を代数的に導出せずに観測と一致のみで機構を支持）の典型的適用事例である。先行確認（Breitenfeld 2014、Pengfei 2024）に続く追加確認事例として記録する。注：2005年ChemComm通信形式ではera-norm toleratedだが、VQ-3の致命的ブロッカーであることに変わりない。

**2. RI-03 + RI-04共起パターン：「機構的プローブ論文」の構造的特徴**

「孤立した有機金属錯体をon-cycle機構的プローブとして使用する」という論文設計では、構造的に以下の共起が生じる：
- **RI-03**（Unobserved explanatory）: 錯体がon-cycle中間体であることが直接観測されない
- **RI-04**（Unreplicated discriminator）: 単一の化学量論的実験（条件・时間点・基質が限定）が主たるdiscriminatorとなる

この共起は、in situ観測技術が未発達だった時代の有機金属機構論文に構造的に現れる。EP-03a（direct-observation）がRI-03の解消、EP-10aがRI-04の解消を担う。この2 RI共起パターンは「mechanistic probe論文RI共起」と名付け、早期段階の有機金属機構論文における定番パターンとしてCodebookに注記することを提案する。

**3. Labeling mismatch（ラベル不整合）パターンの記録**

本論文は1bと2aを「mechanistic probes」とラベルするが、このラベルは暗黙的にon-cycle前提を含む。論文テキスト自体は "can be used as mechanistic probes"（使用できる）という可能性表現を使っており、on-cycle性を直接主張していない。しかし論文の論理構造（式3の収率から「トランスメタル化でない」を結論）はこれらをon-cycle probesとして扱っている。これは§6で指定する「仮説標識の位置」パターンの一種——可能性表現（"can be"）とtitleレベルの強い含意（"mechanistic probes"）の不整合——であり、RI-03との連動が強い。

**4. RI-06（Model import）: Grignard→亜鉛求核剤の機構移転パターン**

本論文のref 12（tpy系Ni/Grignard試薬からの非ラジカルエタン生成、同位体実験）をtpy'/Zn系に輸入するパターンは、Ni触媒クロスカップリング機構論文で繰り返し現れる可能性がある。Grignardと亜鉛では対イオン（MgX vs. ZnX）、配位性、還元電位が異なるため、機構的類推の無条件移転は RI-06の典型例となる。亜鉛求核剤を用いるNi-Negishi機構論文において、Grignard系機構実験を参照として使用する際には「亜鉛系での同型性検証」を EP-06a として要求することを、本事例をcase-specific実装例としてEP辞書に追加する。

**5. 通信→Full Paper遷移の自動解消パターン（潜在的）**

§4で挙げたera-norm tolerated項目（B-2, B-3, B-7, B-8, B-9）の多くは、Full Paper展開（Organometallics, J. Am. Chem. Soc.等への完成版論文）で自動解消される可能性がある。特にB-3（1b XRD）とB-8（2a收率）は、Full Paperでは標準的に要求されるため、本論文のongoing studiesが完成論文として発表された場合のVQ昇格パスは比較的短い（EP-02a → EP-10a → VQ-3）。Jones et al.の後続論文が存在すれば、このパターンの実現を確認できる。
