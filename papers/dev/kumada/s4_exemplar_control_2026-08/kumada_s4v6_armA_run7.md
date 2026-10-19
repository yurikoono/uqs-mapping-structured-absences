```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）:** EP-03a, EP-06a, EP-05a, EP-07a

— EP-03a: RI-03が要求するNiCl₂(dpe)系でのジオルガノニッケル中間体の直接分光観測は、organonickel化学の主要研究テーマであり、KochiグループおよびYamamotoグループが1970年代後半に独立した機構研究論文として発表しており文献から直接追跡可能。

— EP-06a: RI-06が要求するNiCl₂(dpe)系での化学量論的素反応（酸化的付加・トランスメタル化・還元的脱離の個別検証）は、Kochi群が1975–1979年に独立した論文として発表しており、dipy-Ni → dpe-Ni輸入モデルの同型性問題を正面から扱った研究として文献から追跡可能。

— EP-07a: RI-07が要求するsp²/sp³ハライドの境界試験および塩化物/臭化物/ヨウ化物の定量的反応性比較は、Kumadaグループ自身の1976年Full Paper（スコープ拡張・系統的検討）として、独立論文の主題として文献に存在する。

— EP-05a: RI-05が要求するホモカップリング(R–R)・β-脱離生成物を含む反応混合物の質量収支定量は、後続の機構研究論文（Kochi群等）で主題として扱われた実験であり、文献から追跡可能。

**第二群（間接的に追跡可能）:** EP-01a, EP-02a, EP-04a, EP-09a

— EP-01a: **C23 trigger該当**（JACS Communication形式）。同一著者グループが1976年にBull. Chem. Soc. Jpn.でFull Paper（Series I）を発表し、glpc条件・反応時間・統一された収率形式を提供するLetter→Full Paper auto-resolution（auto_resolution_status: occurred）が発生。RI-01のVQ-2水準への充填は形式駆動の自動解消として追跡できる。

— EP-02a: 同上Full Paper展開での自動解消。全Table Iエントリの個別分光データは独立論文ではなくFull Paper内で提供されるため、間接的充填として分類。

— EP-04a: RI-04が要求するcis/trans-1,2-DCE + PhMgBr反応のcis/trans比についての速度論/熱力学区別実験（時間・温度系列）は、Kumada立体化学研究の一部として間接的に追跡可能だが、この特定の基質系に特化した独立論文は限定的であり、後続のPd触媒クロスカップリングの立体化学研究（Negishi, Stille等）が間接的な枠組みを提供する。

— EP-09a: RI-09が要求するNi(acac)₂とNiCl₂(dpe)の同一基質・同一条件での定量的直接比較は、CorriuグループおよびKumadaグループの後続研究で部分的に扱われるが、これを主題とした独立の比較論文は見つかりにくく、触媒比較はレビューや手法論文に分散して間接的に追跡できるに留まる。

**第三群（充填が見つからない可能性あり）:** EP-08a

— EP-08a: **インセンティブ構造的未充填**。代表的基質エントリ（Table I）の収率を独立実験3回以上繰り返し、標準偏差を報告するという要件は技術的に可能だが、追試・反復測定は新規性を要求する出版慣行下で独立論文化されない。Full Paper展開でも通常は単一測定のままである（出版動機の不整合による未充填、物理的不可能ではない）。

---

### §B 各EPの充填論文候補

**EP-01a [Reporting-coherence pack]（第二群）**

```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. "Nickel-phosphine complex-catalyzed Grignard coupling. I. Cross-coupling of alkyl, aryl, and alkenyl Grignard reagents with aryl and alkenyl halides: general scope and limitations." Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — Table I全エントリの系統的glpcおよび単離収率・反応時間・条件を統一形式で提供し、1972年Communication の報告形式欠落を自動解消した。
* **充填確立点**: 同上
* **充填の性質**: Partial（glpc条件と反応時間はFull Paperで充填されるが、RI-01の収率基準不統一【Example 1: ハライド基準 vs Example 2: Grignard基準】がFull Paper内で完全に統一されたかは要確認; VQ-2到達には当該問題の解消確認が必要）
* **Bibliographic confidence**: Medium（Tamaoら1976 Bull. Chem. Soc. Jpn. Full Paperの存在には高い確信があるが、「49, 1958–1969」の巻号ページは記憶に基づく推定を含む）
* **Filling adequacy confidence**: High（Kumadaグループ自身のFull Paperがglpc条件と系統的収率を提供することはKumada coupling文献の標準的理解）
* **Verification recommendation**: [必須]（条件a: 1976年; 条件b: Kumadaグループ10+関連論文; 条件c: Kumada反応命名論文群）
* **DOI / URL**: 推定取得不可（Crossref検索推奨: [REDACTED: verbatim source quotation; see the source paper via its DOI]）
* **Filling timescale category**: format-driven（1972 Communication → 1976 Full Paper = 4年; expected 1-3 yr範囲をわずかに超えるが、競合者Corriuの存在と戦略的発表圧力がFull Paper化を遅延させた可能性あり）
* **注記**: 同一著者グループによる自己充填（自己充填パターン）。Stage 3 §5の「EP-01a → RI-01 (SRG-3)を前進」に対応。§4のEra-Norm Annotationで「通信→Full Paper遷移の自動解消パターン」として記録済み（Stage 3 §6 Point 5）。**Bibliographic verification status: pending**

---

**EP-02a [Identity/purity substantiation pack]（第二群）**

```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```

* **充填するRI**: RI-02 [Identity integrity]
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — EP-01aと同一充填論文。Full Paperでは各エントリの個別物性値・分光データが記録され、"and/or"型の不完全同定が解消された可能性。
* **充填確立点**: 同上
* **充填の性質**: Partial（Stage 3 §3でVQ-1のRI-02が「non-fatal」として残存している通り、Full Paperで全エントリのelemental analysisが含まれるかは要確認; RI-02のnon-fatal残存がFull Paperでも解消されないなら、VQ-2到達はRI-01の解消のみで判定される）
* **Bibliographic confidence**: Medium（EP-01aと同一論文; 同様の留保）
* **Filling adequacy confidence**: Medium（Full Paperで個別NMR/IRデータが提供されると推定されるが、全エントリへの適用範囲は要確認）
* **Verification recommendation**: [必須]（EP-01aと同条件）
* **Filling timescale category**: format-driven（EP-01aと同じ）
* **注記**: EP-01aとのバンドル充填。Stage 3 §5の補助EP（EP-01a → EP-07a → EP-02a）の最後尾。**Bibliographic verification status: pending**

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Morrell, D.G.; Kochi, J.K. "Pathways of aryl-aryl coupling catalyzed by nickel complexes." J. Am. Chem. Soc. 1975, 97, 7262–7270 — Ni錯体を用いた化学量論的実験によりNi(0)/Ni(II)サイクル上の中間体種の検出を試み、均一系vs不均一系および機構経路の区別に最初期の実験的根拠を提供した（配位子はdpeではなくbpy/PPhMe₂系等; Indirect充填）。
* **充填確立点**: Tsou, T.T.; Kochi, J.K. "Mechanism of biaryl synthesis with nickel complexes." J. Am. Chem. Soc. 1979, 101, 6319–6332 — 化学量論的酸化的付加・トランスメタル化・還元的脱離の個別実験および速度論的解析によりNi触媒クロスカップリングの機構を確立; EPR測定でNi(I)ラジカル種の関与を検討し、Ni(0)/Ni(II)とNi(I)/Ni(III)経路を区別するための実験的アプローチを提供。
* **充填の性質**: Indirect（KochiはdpeではなくPR₃単座/bpy系でNi機構を研究; NiCl₂(dpe)系での³¹P{¹H} NMRによる中間体1の直接観測という特定要件は、類似系での充填に留まる。dpe-Ni系に特化した中間体観測にはKumadaグループ自身の後続詳細論文または他グループの論文が必要）
* **Bibliographic confidence**: Medium（Morrell & Kochi JACS 1975, 97, 7262は実在の論文として合理的確信があるが、ページ番号「7262–7270」は推定; Tsou & Kochi JACS 1979, 101, 6319はKochi群のNi機構研究として高信頼度）
* **Filling adequacy confidence**: Medium（Kochiの実験がNiCl₂(dpe)系の中間体1の直接NMR観測というcase-specific実装を満たすかは要確認; 類似系での充填として機能する可能性）
* **Verification recommendation**: [必須]（条件a: 1975, 1979年; 条件b: Kumada命名反応関連研究; 条件c: Kumada反応命名論文群に関連）
* **DOI / URL**: 推定（JACS 1979, 101, 6319 → DOI: 10.1021/ja00516a013は要確認）
* **Filling timescale category**: incentive-aligned（3年: Morrell 1975; 7年: Tsou 1979 — 機構研究の標準的競争的応答速度）
* **注記**: Stage 3 §6 Point 6で記録された「RI-06 + RI-03の不可分共起パターン」により、EP-06aと同一の充填論文候補が重なる（バンドル充填）。NiCl₂(dpe)系での中間体1の³¹P NMR直接観測に特化した決定的充填論文は、1980年代Pd/Ni機構研究の進展まで調査が必要な可能性あり。U-2（黒色混合物の均一/不均一問題）に対応するHg(0)ポイズニング試験実験もep-03aの範囲に含まれる。**Bibliographic verification status: pending**

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — Full PaperでTable I各エントリの立体化学データが体系的に報告された可能性; cis/trans比の反復測定データを含むかは要確認（Indirect/Partial充填候補）。
* **充填確立点**: **未同定**（cis/trans-1,2-DCE + PhMgBr系の速度論/熱力学制御の明示的区別実験を主題とした独立論文は現在のところ特定できない。後続のPd触媒クロスカップリング立体化学研究が類似問いを扱うが、Ni-dpe系のこの特定の系への直接適用は確認できない）
* **充填の性質**: Partial（立体化学的データはFull Paper 1976で充填の可能性があるが、速度論vs熱力学の明示的区別実験【反応時間・温度系列】を含む論文は未同定）
* **Bibliographic confidence**: Medium（Tamao 1976 Full Paperは実在; その充填内容への対応はLow）
* **Filling adequacy confidence**: Low（speed度論/熱力学区別という特定の実験要件がFull Paper 1976に含まれるかは要確認; 専用研究は現在未同定）
* **Verification recommendation**: [必須]（全条件該当; Low confidence; 未同定候補あり）
* **Filling timescale category**: non-applicable（充填確立論文未同定）
* **注記**: SRG-6（A-1, B-11, U-3）に対応。cis/trans比の速度論/熱力学問題はNi系からPd系への移行とともに問いの重要性が低下し、成功による問いの抹消（partial）の側面を持つ可能性。U-3（kinetic/thermodynamic indeterminacy）への直接的な答えは§Eで「部分的未充填」として扱う。**Bibliographic verification status: pending (充填開始点のみ)**

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — Full PaperでTable I各エントリのより完全な収率データと副生成物情報を提供; R–R（ホモカップリング）量の記録を含む可能性（要確認）。
* **充填確立点**: Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979, 101, 6319–6332 — Ni触媒クロスカップリングにおけるホモカップリング生成物R–Rの生成経路と定量的評価を含む機構研究; eq(3)が予測するR–Rの実在とその量を確認した可能性（充填の性質はIndirectからPartialの範囲で要確認）。
* **充填の性質**: Partial（B-1とU-1が記録した「eq(3)が予測するR–Rが未報告」という自己矛盾的不在への答えが、Full Paper 1976またはKochi 1979に含まれるかは要確認; "selective"という定性的主張に数値的根拠を付与した独立論文は未同定）
* **Bibliographic confidence**: Medium（両論文の存在は合理的確信; 充填内容との対応はPartial）
* **Filling adequacy confidence**: Medium（EP-05aのcase-specific実装「n-BuMgBr + PhClでGC-MS分析しR–R, 1-butene, PhClを定量」に直接対応する実験データの有無は要確認）
* **Verification recommendation**: [必須]（EP-01aと同条件）
* **Filling timescale category**: format-driven → incentive-aligned（Full Paper 1976: 4年; Kochi 1979: 7年）
* **注記**: SRG-2（B-1, U-1, C-1）の核心「eq(3)が予測するR–Rを実際に観測・定量したか」という問いへの答えを提供した論文の確定的同定は、後続のNi触媒機構研究全体を視野に入れた文献調査が必要。Stage 3 §5「EP-05a (Quantitative-ranking substantiation pack) → RI-05 (SRG-2)を前進 → VQ-3(qualified)からVQ-3(unqualified)へ」の前進に対応。**Bibliographic verification status: pending**

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]
* **充填開始点**: Morrell, D.G.; Kochi, J.K. J. Am. Chem. Soc. 1975, 97, 7262–7270 — Ni錯体を用いた触媒サイクルの化学量論的検証を最初期に試みた研究; dipy-Ni系での素反応の検証が、dpe-Ni系への輸入モデルの同型性問題を間接的に扱う。
* **充填確立点**: Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979, 101, 6319–6332 — eqs 2–4に対応する酸化的付加・トランスメタル化・還元的脱離の化学量論的素反応実験を実施し、Ni触媒サイクルの各ステップを独立に検証した最初の体系的機構論文の一つ。
* **充填の性質**: Indirect（KochiはdpeではなくPR₃/bpy系でNi機構を研究; NiCl₂(dpe)系でのeqs 2–4の各素反応の個別化学量論的実証という特定要件は類似系での充填に留まる）
* **Bibliographic confidence**: Medium（Morrell 1975 推定; Tsou 1979 High）
* **Filling adequacy confidence**: Medium（化学量論的素反応の検証はKochi研究の中心テーマだが、dpe配位子との直接対応は要確認）
* **Verification recommendation**: [必須]（全条件該当）
* **DOI / URL**: 推定のみ（要Crossref確認）
* **Filling timescale category**: incentive-aligned（3–7年）
* **注記**: Stage 3 §6 Point 6の「RI-06 + RI-03不可分共起パターン」により、EP-03aとのバンドル充填候補として同一論文が浮上。RI-06（サイクルレベル輸入）の解消（dipy-Ni/dpe-Ni同型性の実証）とRI-03（中間体未観測）の解消（³¹P NMR直接観測）は別々の実験が必要であり、EP-06aの充填はEP-03aの充填と独立して評価が必要。Stage 3 §5「EP-06a (Analogy-validation pack) → RI-06 (SRG-1)を前進」に対応。**Bibliographic verification status: pending**

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — Full Paperでsp²ハライドの系統的スコープおよびsp³ハライドを試みた場合の結果（または明示的なスコープ外記録）を提供した可能性; PhCl/PhBr/PhIの反応性比較データが含まれる可能性。
* **充填確立点**: 第二候補: Kumada, M.; Tamao, K.; Sumitani, K. Org. Synth. 1978, 58, 127 — [Medium confidence] Organic Syntheses実験手順でNiCl₂(dpe)触媒の塩化物反応性と収率を実証的に確立。塩化物の「高反応性」という主張に実験的根拠を提供した可能性。
* **充填の性質**: Partial（sp²制限の「試験したか否か」という問いへの答えはFull Paper 1976で提供される可能性が高い; sp³ハライドの完全なNi触媒カップリングの確立は2000年代まで待つ必要があり、その充填は別の研究流に属する）
* **Bibliographic confidence**: Medium（Tamao 1976 Full Paper: Medium; Org. Synth. 1978: Medium — 巻号ページは推定）
* **Filling adequacy confidence**: High（Tamao 1976 Full Paper: ep-07aのcase-specific実装「sp³ハライドをGCで確認」および「PhCl/PhBr/PhIの収率・初期速度比較」に対応するデータを含む可能性が高い）
* **Verification recommendation**: [必須]（全条件該当）
* **Filling timescale category**: format-driven (1-3 yr) — sp²スコープのFull Paper充填; sp³境界の完全確立はfield-methodology (20+ yr): Terao, J.; Kambe, N. (2000年代)
* **注記**: Stage 3 §6 Point 2で記録された「RI-07拡張適用: 制限の肯定的再フレーム」への答えは、Full Paper 1976がsp³ハライドの「試験したか否か」の実験的根拠を提供することで達成される。D4-4（「sp³ハライドは試みられたか？」という問い）への答えとして最重要の充填論文。**Bibliographic verification status: pending**

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填論文候補**: **未同定**
* **充填の性質**: — (non-applicable)
* **未充填の理由**: インセンティブ構造的未充填。代表的基質の収率を独立実験で3回以上繰り返し標準偏差を報告するという要件は技術的に可能だが、追試・反復測定は新規性を要求する出版慣行下で独立論文化されない。Full Paper 1976でもエントリごとの反復収率データは通常報告されない。
* **Bibliographic verification status**: non-applicable

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: Corriu, R.J.P.; Masse, J.P. J. Chem. Soc., Chem. Commun. 1972, 144 — 原論文のNote Added in Proofが記録した同時独立発見（Ni(acac)₂触媒で類似選択的クロスカップリングを達成）。これは充填開始点ではなく**先行/同時充填**パターン: NiCl₂(dpe)なしに類似選択性が達成されるという事実は、EP-09aが要求する「Ni(acac)₂との直接比較」の前提条件となる情報を既に提供している。
* **充填確立点**: **未同定**（NiCl₂(dpe)とNi(acac)₂を同一基質・条件で定量的に直接比較し「bidentate diphosphineの必要性vs有効な選択肢」を明示的に評価した独立論文は現在のところ特定できない。Corriuグループの後続論文がこの比較を含む可能性があるが、具体的な書誌情報は特定できない）
* **充填の性質**: Indirect（Corriu 1972はNi(acac)₂での成功を記録しているが、同一基質でのNiCl₂(dpe)との定量的直接比較は行っていない; その後のNi触媒クロスカップリングレビューが間接的比較を提供する可能性）
* **Bibliographic confidence**: High（Corriu 1972: 原論文引用のため高信頼度）/ Low（後続比較論文: 書誌不明）
* **Filling adequacy confidence**: Low（EP-09aの特定要件「NiCl₂(dpe)とNi(acac)₂を同一基質・条件で比較し選択性と収率を定量」を満たす論文の有無は要確認）
* **Verification recommendation**: [必須]（全条件該当; Low confidence候補を含む）
* **Filling timescale category**: incentive-aligned (variable) — Ni(acac)₂とdpe-Ni系の比較は後続研究で分散的に扱われたが、単一論文での完全充填は不明。後のPd触媒台頭により問い自体の重要性が低下（部分的success-driven question erasure）。
* **注記**: D4-8（Corriu/Masse問題、Stage 2）に直接対応。bidentate diphosphineの「必要条件vs有効な選択肢」という問いは現代でも完全には解消されておらず、長期未充填EPとして§Eで扱う。Stage 3 CLA-1（B-3, C-3）の未解消問題の核心。後続のPd触媒（鈴木、根岸、Heck等）の圧倒的成功により、Ni配位子設計の最適化という問いの緊急性が失われた（成功による問いの抹消の広義適用）。**Bibliographic verification status: pending**

---

**§B 末尾チェック: Bibliographic verification（conditional triggering）**

全充填論文候補に対するトリガー条件評価:
- (a) 論文年代が古い（1980年以前）: **YES** — 主要候補は1972–1979年
- (b) 著者ネットワークが密（Kumadaグループから10+関連論文）: **YES**
- (c) 反応名がauthor nameに由来する命名規則: **YES**（「Kumada反応」「Kumada coupling」）
- (d) Bibliographic confidence Medium-Low の候補が2件以上: **YES**（EP-04a, EP-09a後続論文等）

→ **全候補に [必須] verification を付与。全エントリのBibliographic verification status: pending。**

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️ Tamao, K.; Sumitani, K.; Kiso, Y. et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958 | EP-01a, EP-02a, EP-05a (partial), EP-07a | VQ-2 | 1976 | Medium | High | 必須 |
| 2 | ⚠️ Morrell, D.G.; Kochi, J.K. J. Am. Chem. Soc. 1975, 97, 7262 | EP-03a (onset), EP-06a (onset) | VQ-3 | 1975 | Medium | Medium | 必須 |
| 3 | ⚠️ Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979, 101, 6319 | EP-03a, EP-06a, EP-05a (partial) | VQ-3 | 1979 | High | Medium | 必須 |
| 4 | ⚠️ Kumada, M.; Tamao, K.; Sumitani, K. Org. Synth. 1978, 58, 127 | EP-07a (establishment) | VQ-2 | 1978 | Medium | Medium | 必須 |
| 5 | ⚠️ Corriu, R.J.P.; Masse, J.P. J. Chem. Soc., Chem. Commun. 1972, 144 | EP-09a (先行充填・充填開始点) | VQ-2 | 1972 | High | Low | 必須 |

**選定理由:**

第1位（Tamao et al. 1976）は、VQ-2到達に必要なEP-01a, EP-02a, EP-07aをバンドル充填する自己充填論文として、EP充填カバレッジとFull Paper auto-resolution（C23）の観点から最高優先度。同一著者グループの自己充填により、実験意図とEP要件の対応が最も高いと推定される。ただしMedium bibliographic confidenceのため[必須]verification後に正式昇格。

第2位・第3位（Morrell 1975, Tsou 1979）はVQ-3要件（RI-03/RI-06）をカバーする機構研究として選定。Stage 3 §6で記録されたRI-06 + RI-03の不可分共起パターンにより、EP-03aとEP-06aを同一研究グループの論文がバンドル充填する可能性が高い。Kochi群はNi触媒機構研究の主要グループであり、Filling adequacy confidenceはMediumだが分野内での認知度が高い。

第4位（Org. Synth. 1978）はEP-07a（境界試験・塩化物反応性の実験的確立）の充填確立点として、実用的な実験手順の標準化という観点から選定。

第5位（Corriu 1972）は、EP-09aの先行充填記録として、Ni(acac)₂での選択的クロスカップリングの独立確認という歴史的事実を記録するために選定。Filling adequacy confidenceはLow（同一条件での定量的直接比較は未含）であり、VQ-2 partial充填として位置づける。

VQ-4（EP-08a）については推奨選定論文なし（インセンティブ構造的未充填）。EP-04aの充填確立論文は未同定のため選定から除外（§E参照）。

全5報に[必須] verification が付与されており、Bibliographic verification完了まで「⚠️ pending verification」として表記する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

- VQ-2 要件 (RI-01, SRG-3): EP-01a → 1976年 [Tamao et al. Bull. Chem. Soc. Jpn.] 自己充填（format-driven, 4年）
- VQ-2 要件 (RI-02, SRG-3): EP-02a → 1976年 [同上] 自己充填（format-driven, 4年、EP-01aとバンドル）
- VQ-2 要件 (RI-07, SRG-4): EP-07a → 1976年 [同上] 自己充填（format-driven, 4年） / sp³境界の完全確立は2000年代（20+年、技術駆動）
- VQ-3 要件 (RI-03, SRG-1): EP-03a → 1975年開始 [Morrell & Kochi] 分野横断充填（3年）→ 1979年確立 [Tsou & Kochi]（7年）
- VQ-3 要件 (RI-06, SRG-1): EP-06a → 同上（EP-03aとバンドル）
- VQ-3 要件 (RI-05, SRG-2): EP-05a → 1976-1979年 [Tamao 1976 partial + Kochi 1979] Partial充填（4–7年）
- VQ-3 要件 (RI-04, SRG-6): EP-04a → 充填確立論文未同定（20+年以降も部分未充填）
- VQ-4 要件 (RI-08): EP-08a → 未充填（インセンティブ構造的）
- VQ-2 相当 (RI-09, CLA-1): EP-09a → 1972年先行充填（Corriu 1972）として記録; 充填確立論文未同定

**階層-時間対応の評価:**

仮説「VQ階層が上がるほど充填に要する時間が長くなる」は、本ケースでは**部分的支持**が得られる。VQ-2要件の充填（EP-01a, EP-02a, EP-07a）はLetter→Full Paper auto-resolution（format-driven, 4年）で達成されており、VQ-3要件（EP-03a, EP-06a）の充填（7年, incentive-aligned）より短期間での解消が観察される。ただし注目すべき逆転が存在する: RI-03/RI-06（VQ-3要件, 高VQ）が1975–1979年に機構研究として充填される一方、RI-07（VQ-2要件, 低VQ）のsp³境界の完全確立は20年以上を要した。これは「科学的論理に基づく低VQ→高VQ充填順序」と「出版インセンティブに基づく高VQ→低VQ充填順序」のVQ階層逆転パターンを部分的に示す事例である（Stage 4 §E参照）。

**特筆すべきパターン:**

1. **自己充填（dominant）**: EP-01a, EP-02a, EP-05a, EP-07aはすべて原著者グループ（Kumada/Tamao）の後続論文によって充填されており、自己充填パターンが主要である。これは「著者が問いの存在を認識していた（A-2, "Investigations are continuing"）」という宣言と整合する。

2. **分野横断充填（VQ-3）**: EP-03a, EP-06aはKochiグループ（Columbia大学）による分野横断充填として発生。これは1972年の機構的問いが、Kumadaグループ自身ではなく機構化学専門グループによって応答されたことを示す。

3. **VQ階層逆転パターン**: RI-03/RI-06（高VQ-3要件）が7年で機構論文として充填される一方、RI-07（低VQ-2要件）のsp³境界の完全実験的確立は20年以上を要した。これは出版インセンティブ（機構論文 = 高新規性, 境界試験 = 低新規性）がVQ階層と逆の順序での充填を促したことを示す。

4. **先行充填（EP-09a）**: Corriu 1972はKumada 1972と同年同時期の先行/同時充填として記録される。「配位子なしでも選択性が得られる」というEP-09aの問いに対する答えは、Kumada 1972の論文準備中にはまだ存在せず、Note Added in Proof段階で初めて記録された。この先行充填は充填「解消」ではなく問いの緊急性を高める情報として機能した。

5. **著者回顧との照合**: Kumada本人は後年の講演・回顧で「Ni-dpe触媒の機構的理解」よりも「実用的なスコープ」と「Pdへの展開」を中心に語る傾向が報告されており、EP-04a（cis/trans比の速度論/熱力学問題）およびEP-09a（Ni(acac)₂との比較）は著者の内部認識から外れた問いである可能性が高い。これは「分野の内部者には不可視の構造的不在」の間接的証拠として記録する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

**EP-04a [Discrimination / replication pack]（部分的未充填）:**
* **未充填の理由**: 複合的。(1) cis/trans-1,2-DCE + PhMgBrという特定の系での時間・温度系列実験は、立体化学研究の主題として追求されたが、速度論vs熱力学制御の明示的区別という問いは後続のPd触媒立体化学研究（高選択性を目的とした研究）に問いの枠組みが移行した（成功による問いの抹消: Pd触媒クロスカップリングの高立体選択性確立が、Ni系の「非選択的な」cis/trans混合比の詳細解明への動機を低下させた）; (2) cis-stilbene vs trans-stilbeneという生成物系での速度論/熱力学区別実験は、不対称な付加機構を含む複雑な問題であり、独立論文として扱われる新規性がある一方で、Kumada-Ni触媒そのものの重要性低下（Pd優位化）とともに研究対象から外れた可能性がある。
* **発見的意義**: **あり**。U-3（Stage 1）が記録した「speed度論/熱力学indeterminacy」は、1972年論文では「機構的含意がある」と記述されながら、それを解明するための実験（時間・温度系列）は40年以上にわたって独立論文として発表されたことが確認できない。これは「科学コミュニティが、Ni触媒クロスカップリングの立体化学的機構問題をPd系の成功によって棚上げにしてきた」という成功による問いの抹消パターンの事例として記録できる。
* **将来の充填可能性**: 中（Pd/Ni触媒クロスカップリングの理論的・計算化学的研究の発展により、cis/trans選択性の速度論/熱力学起源を事後的に解析する研究は現代の計算化学で原理的には可能。ただし実験的追試の出版インセンティブは依然として低い）

---

**EP-08a [Replication / uncertainty pack]（未充填）:**
* **未充填の理由**: インセンティブ構造的未充填。代表的基質エントリの収率を独立実験3回以上繰り返し標準偏差を報告するという要件は技術的に完全に実現可能だが、追試・反復測定は新規性を要求する化学系出版慣行下で独立論文化されない。Full Paper展開でもエントリごとの統計的エラーは通常報告されない。「測定信頼性」の要求は、合成化学分野では計算化学や物理測定とは異なり、分野慣行として体系的に省略されてきた問題であり、このEPは分野が構造的に回避してきた問いとして記録できる。
* **発見的意義**: **あり**。RI-08（Unquantified reliability）がSRG-3の全エントリ（B-4, B-8, B-9, B-12, B-13）に横断的に存在し、かつFull Paper展開でも完全には解消されないという構造は、「合成化学分野における収率データの統計的信頼性報告が1972年から現在に至るまで体系的に省略されてきた」という分野インセンティブ構造の証拠として記録できる（「n=1測定の収率は科学的事実として慣行的に扱われる」というfield-wide convention）。
* **将来の充填可能性**: 低（技術的には可能だが、出版インセンティブ構造が変化しない限り独立論文化の見込みは低い。ただし、合成化学における再現性問題への意識が高まれば（2010年代以降のreproducibility crisis議論）、retroactiveな再現試験論文として充填される可能性は中程度）

---

**EP-09a [Internal benchmark pack]（充填確立論文未同定）:**
* **未充填の理由**: 成功による問いの抹消（広義）+ インセンティブ不整合。「NiCl₂(dpe) vs Ni(acac)₂の同一条件定量比較」という問いは、Ni触媒クロスカップリング全体がPd触媒系に置き換えられていく1970年代後半–1980年代を通じて重要性が急速に低下した。また、Kumadaグループ（dpe-Ni支持）とCorriuグループ（acac-Ni支持）が独立した研究系統として発展したため、両者を同一条件で比較することに戦略的な動機がなかった可能性がある。CLA-1で記録されたRI-09（External superiority）はこの問いの未充填を正確に予測していた。
* **発見的意義**: **あり**。EP-09aの未充填は「科学的主張の優先権を持つグループが、その主張を直接反証しうる比較実験を実施しないまま分野が移行した」という構造的不在のパターンを示す。「bidentate diphosphineが必要条件か有効な選択肢か」という問いは、原論文の中心的novelty claim（NC-4）に直接関わるにもかかわらず、50年以上にわたって定量的直接比較実験として解消されていないことが、UQSによる発見的意義として記録できる。
* **将来の充填可能性**: 中（現代のNi触媒クロスカップリング研究の文脈では、配位子設計と反応選択性の計算化学的研究が発展しており、NiCl₂(dpe) vs Ni(acac)₂の反応性差をDFT計算で解析する研究は技術的に実現可能。また、Ni触媒のenantioselective cross-couplingへの応用研究の文脈で、配位子の役割が改めて検討される可能性がある）

---

**VQ階層逆転パターンのまとめ:**

EP-07a（低VQ-2: RI-07）のsp³境界の完全確立が20年以上を要した一方、EP-03a/EP-06a（高VQ-3: RI-03/RI-06）が7年で機構論文として充填されたという逆転は、「機構的問いへの答えは科学的関心が高いため早期に充填される」一方、「境界テストは応用的関心が低いため遅延する」というインセンティブ構造に起因する。未充填EP（EP-08a, EP-09a）がいずれも低VQ要件（RI-08, RI-09）に集中し、充填済みEPが高VQ要件（RI-03, RI-06）に集中するパターンは、「科学的論理に基づくVQ-1→VQ-2→VQ-3の充填順序」と「出版インセンティブに基づく実際の充填順序（機構→スコープ→統計/ベンチマーク）」の逆転として記録する。
```

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
