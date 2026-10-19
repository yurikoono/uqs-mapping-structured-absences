```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a, EP-07a, EP-09a

  — EP-03a: RI-03（Unobserved explanatory）に対応する中間体の直接観測は、有機ニッケル錯体化学の独立研究テーマとして1970年代後半に活発に展開されており、Ni-ジホスフィン系の特定中間体を対象とした分光学的観測論文が独立して発表される蓋然性が高い。
  — EP-06a: RI-06（Imported model）に対応するdipy-Ni系からdpe-Ni系への類推の同型性検証は、化学量論的素反応の実証という明確な実験的課題として独立論文の主題になりうる。
  — EP-07a: RI-07（Unsupported boundary）に対応するsp²/sp³ハライドの境界試験と塩化物/臭化物/ヨウ化物比較は、Full Paper展開・スコープ拡張論文・不斉応用論文において系統的に実施される性質の実験であり、文献検索で直接ヒットしうる。
  — EP-09a: RI-09（External superiority）に対応するNi(acac)₂対NiCl₂(dpe)の直接比較は、Corriu/Masse 1972の並行通信が既に実験的枠組みを提供しており、追跡が容易である。

**第二群（間接的に追跡可能）：** EP-01a, EP-02a, EP-04a, EP-05a

  — EP-01a: RI-01（Reporting integrity）—対象論文はJACS Communication形式（短報）であり、C23パターン（Letter→Full Paper auto-resolution）が発火する。同一著者グループによるBull. Chem. Soc. Jpn.への全論文（Full Paper）がglpc条件・反応時間・収率基準の統一を自動解消する候補として存在する。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```
  — EP-02a: RI-02（非致命的、VQ-1 non-fatal）—EP-01aと同じFull Paper自動解消パターン（C23）により副次的に解消される。独立論文主題ではなく、Full Paperおよび有機合成手順書（Org. Synth.等）への移行で充填される性質。
  — EP-04a: RI-04（Unreplicated discriminator）—cis/trans比の速度論/熱力学的区別実験は、Kumada反応の立体化学研究として機構論文の一部に含まれるが、このパラメータのみを主題とした独立論文は稀であり、間接的な充填となる。
  — EP-05a: RI-05（Qualitative overread）—「選択的クロスカップリング」の定量的根拠（質量収支、ホモカップリング生成物の定量）はFull Paperに部分的に含まれるが、反応混合物の完全な質量収支を独立研究主題とする論文は少なく、機構論文の副次的データとして充填される形態が多い。

**第三群（充填が見つからない可能性あり）：** EP-08a

  — EP-08a: RI-08（Unquantified reliability）—収率の反復測定・標準偏差の報告は、出版インセンティブの不整合により第三群に分類される。「インセンティブ構造的未充填」：対象系（同一条件での複数回反復測定）を独立論文化する動機が1970年代以降の有機合成化学において存在しない。統計的再現性の報告は分野慣行として現在も系統的に回避されている。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第二群）**
C23パターン発火：本論文はJACS Communication（短報）形式であり、Letter→Full Paper auto-resolutionが適用される。

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — 同一著者グループによるFull Paper第1報で、glpc条件の詳細、統一された収率計算基準（有機ハライド基準）、全エントリの反応条件を系統的に記述する。
* **充填確立点**: 同上
* **充填の性質**: Complete（format-driven自動解消の典型例、SRG-3のRI-01を構造的に解消）
* **Bibliographic confidence**: Medium — 著者リスト（Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada）とジャーナル（Bull. Chem. Soc. Jpn.）・年（1976）・巻号（49）の組み合わせに信頼はあるが、正確なページ番号および論文タイトルの逐語には推測を含む。
* **Filling adequacy confidence**: High — Communication形式の紙幅制約に起因するRI-01（SRG-3）はFull Paperへの自動解消で原理的に解消される。glpc条件・収率基準・反応時間の完全記述はFull Paperの定義的要件。
* **Verification recommendation**: [必須] — (a) 1970年代論文、(c) Kumada named reaction、(b) 同一グループから10件以上の関連論文
* **Bibliographic verification status**: pending
* **DOI / URL**: DOI未確認、Crossref検索推奨（"Tamao Kumada Bull Chem Soc Jpn 1976"）
* **Filling timescale category**: format-driven (1-3 yr) — 1972年通信→1976年Full Paper（4年）。やや遅延しているが制度的・競争的文脈に照らして"format-driven"に分類可。
* **注記**: SRG-3（B-4, B-8, B-9, B-12, B-13）のRI-01は通信→Full Paper遷移の自動解消候補として§4で既に分類済み（B-4, B-8, B-13: communication-era tolerated / both-era-tagged）。同論文はEP-02a, EP-05a, EP-07aをバンドル充填する（相互参照）。

---

**EP-02a [Identity/purity substantiation pack]（第二群）**
C23パターン発火（EP-01aと同一充填）。

* **充填するRI**: RI-02 [Identity / purity] (VQ-1 non-fatal残存)
* **充填開始点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — EP-01aと同一論文。Full Paperへの移行により各エントリの個別NMR・IR・MSデータが記述される。
* **充填確立点**: 同上（EP-01aとバンドル充填）
* **充填の性質**: Complete（Full Paper展開での自動解消）
* **Bibliographic confidence**: Medium（EP-01aと同一）
* **Filling adequacy confidence**: High — B-13の"and/or"構文によるRI-02の不完全同定問題はFull Paperの各エントリ個別データ記述で構造的に解消される。
* **Verification recommendation**: [必須]（EP-01aと同一理由）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: EP-01aとの完全バンドル充填。副次的充填候補としてKumada, M.; Tamao, K.; Sumitani, K. *Org. Synth.* 1978, 58, 127が機能する可能性（Org. Synth.手順書は製品の完全キャラクタリゼーションを要求）— Bibliographic confidence: Medium、verification: [必須]。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — Full PaperはNiCl₂(dpe)との化学量論的反応における反応混合物の分析を含む可能性がある（Partial充填候補）。
* **充填確立点**: Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* 1975, 97, 7262–7274 — Kochi研究グループによる遷移金属触媒クロスカップリングの機構的研究で、Ni(0)/Ni(II)サイクルの化学量論的検証に向けた実験的アプローチを確立した可能性がある（Partial〜Complete候補）。
* **充填の性質**: Partial（Indirect） — ³¹P{¹H} NMRによる[Ni(n-Bu)₂(dpe)]の低温観測という最も厳密な実装は、1970年代中期の計測技術的制約（FT-NMR普及途上）から単独論文化されにくく、間接的充填（類似diphosphine-Ni錯体での実証または化学量論的実験）が実態として支配的と推定。
* **Bibliographic confidence**: Medium（Morrell-Kochi 1975のJACS掲載・著者名は概ね信頼できるが、タイトルと正確な頁番号は推測を含む）
* **Filling adequacy confidence**: Medium — Kochi論文がNi-ジホスフィン系中間体の直接観測を実施したかどうかは論文アクセスなしには断定できず、NiCl₂(dpe)の対象系での実装には更なる検証が必要。
* **Verification recommendation**: [必須] — (a) 1975年論文、(c) Kumada named reaction関連
* **Bibliographic verification status**: pending
* **DOI / URL**: DOI未確認、"Morrell Kochi JACS 1975 97 7262"でCrossref検索推奨
* **Filling timescale category**: field-methodology (2-5 yr) — 1972年通信→1975年Kochi機構論文（3年）
* **注記**: ³¹P NMR観測に特化した充填として、Yamamoto, T. らによるBull. Chem. Soc. Jpn.の1970年代後半〜1980年代初頭のジオルガノニッケル-ホスフィン錯体に関する論文が候補として存在する（Bibliographic confidence: Low — 具体的な著者・年・巻号の同定には独立した文献調査が必要）。EP-06aとの密接な充填連動（SRG-1のRI-06/RI-03不可分共起）に注意：EP-03a単独の充填はRI-03を前進させるが、RI-06の解消なしにVQ-3到達は困難（§6のコードブック注記と整合）。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: 未同定の明確候補なし — cis/trans-スチルベン比の時間・温度系列データを報告し速度論/熱力学的制御を区別した論文は現時点で特定できない。
* **充填確立点**: 未同定
* **充填の性質**: 未同定
* **Bibliographic confidence**: Low — SRG-6（A-1, B-11, U-3）のcis/trans選択性問題を主題的に扱う独立論文の存在確認が必要。部分的充填候補として、Hayashi, T.; Konishi, M.; Fukushima, M.; Mise, T.; Kagotani, M.; Tajika, M.; Kumada, M. *J. Am. Chem. Soc.* 1982 頃 — Kumada不斉カップリングの立体化学研究の可能性（著者群・年代・雑誌は推測域）。
* **Filling adequacy confidence**: Low — 上記候補が速度論/熱力学の区別実験（時間・温度系列）を明示的に実施したかは不明。
* **Verification recommendation**: [必須] — (a) 1970-1980年代論文、(c) Kumada named reaction
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned（variable）
* **注記**: cis/trans比の速度論/熱力学的区別は、Kumada反応の立体化学論文（ビニルハライドの立体保持/反転問題）では間接的に取り上げられる可能性が高いが、U-3のような時間・温度依存性の単独研究は分野インセンティブ的に独立論文化されにくい。§Eで「分野的回避」パターンとして記録する。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — Full Paperがcross-couplingとhomo-couplingの選択性について1972年通信より詳細な反応混合物分析を含む可能性（Partial充填候補）。
* **充填確立点**: （未同定の完全充填候補）— 反応混合物の質量収支（n-Bu–n-Bu、1-ブテン、PhClを含む）を明示的に定量したGC-MS分析論文は現時点で特定できない。
* **充填の性質**: Partial（Full Paperへの移行は収率データの精度向上をもたらすが、eq (3)が予測するR-Rの定量的不在証明という最も厳密な実装が行われた論文は未同定）
* **Bibliographic confidence**: Medium（Tamao et al. 1976）/ Low（完全充填候補の単独論文）
* **Filling adequacy confidence**: Medium（Tamao Full Paper）/ Low（完全充填候補）
* **Verification recommendation**: [必須] — (a)(b)(c)条件に該当
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)（Full Paper経由のPartial充填）/ incentive-aligned（完全充填は長期遅延）
* **注記**: SRG-2（B-1, U-1, C-1）の「選択的クロスカップリング主張の定量的根拠」は、Kumada反応が合成化学的成功を収めた結果として、反応機構の詳細検証（eq(3)予測のR-R定量）よりも応用・拡張・不斉化の方向に研究関心が流れた。§5で「成功による問いの抹消」パターンとして記録可能性あり。EP-01aとのバンドル充填（Full Paper経由）。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]（サイクルレベル輸入: dipy-Ni系→dpe-Ni系）
* **充填開始点**: Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* 1975, 97, 7262–7274 — Ni触媒クロスカップリングの化学量論的素反応の部分的実証（候補）。NiCl₂(PPh₃)₂またはNiCl₂(dppe)系でのeq (2)相当反応またはeq (3)相当反応の化学量論的実証が含まれる可能性。
* **充填確立点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — Full Paperがdipy-Ni系と対象系（dpe-Ni系）の同型性を少なくとも部分的に実証する化学量論的実験を含む可能性（Partial）。より完全な充填として、Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* 1979, 101巻 — Ni(0)への酸化的付加反応の機構的研究（候補）。
* **充填の性質**: Partial（Indirect）— dpe-Ni系に特定したeqs 2–4全体の化学量論的実証（RI-06の最厳格実装）は1970年代の単独論文では部分的にしか充填されていない可能性が高い。配位子が異なる系（NiCl₂(PPh₃)₂またはNiCl₂(dppb)等）での類推的実証が主たる充填経路。
* **Bibliographic confidence**: Medium（Morrell-Kochi 1975、Tsou-Kochi 1979）— Kochi研究グループによるJACS掲載論文の存在は信頼できるが著者順・タイトル・正確な巻号は推測を含む。
* **Filling adequacy confidence**: Medium — dpe-NiというKumada系特定の配位子でeqs 2–4が化学量論的に実証されたかは論文アクセスなしには確認できない。
* **Verification recommendation**: [必須] — (a)(b)(c)条件
* **Bibliographic verification status**: pending
* **DOI / URL**: "Tsou Kochi JACS 1979"でCrossref検索推奨。
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: RI-06とRI-03の不可分共起（§6コードブック注記）により、EP-06aとEP-03aは連動して充填される必要がある。EP-06aの解消（dipy-Ni系とdpe-Ni系の同型性実証）だけではRI-03（中間体の直接観測）を解消しない。NiCl₂(dpe)系でのeq (2)〜(4)の化学量論的個別実証は、1972年〜2000年代にわたって段階的に蓄積された分散的充填である可能性が高く、単一の「充填確立点」が存在しない形態（分割提示充填の変形）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]（拡張適用: 制限の肯定的再フレーム形態、§6コードブック注記）
* **充填開始点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — Full Paperがsp²ハライドの系統的スコープ拡張とsp³ハライド試験（不活性確認）を含む可能性（充填開始点候補）。
* **充填確立点**: Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. *J. Am. Chem. Soc.* 1976, 98, 3718–3719（候補）— Kumada不斉カップリングの初報で、フェロセニルジホスフィン（PPFA等）配位子を用いた系統的スコープ検討と配位子活性比較データを含む可能性。PhCl/PhBr/PhIの収率比較もこの文脈で報告される可能性。
* **充填の性質**: Partial（sp²/sp³境界の実験的確認がFull Paperに含まれる可能性があるが、sp³ハライドを試みて明示的に不活性と報告した単独記述は不確か）
* **Bibliographic confidence**: Medium（Hayashi et al. JACS 1976の存在には高い信頼があるが、著者順・正確なページの確認が必要）
* **Filling adequacy confidence**: Medium（sp²制限を実験的に確認したかどうかはFull Paperの内容アクセスなしには断定不可）
* **Verification recommendation**: [必須] — (a)(b)(c)条件
* **Bibliographic verification status**: pending
* **DOI / URL**: "Hayashi Tajika Tamao Kumada JACS 1976"でCrossref検索推奨。
* **Filling timescale category**: format-driven / incentive-aligned (1-5 yr) — Full Paperが充填開始点なら format-driven; 不斉カップリング論文が充填確立点なら incentive-aligned。
* **注記**: 塩化物高反応性（B-6）の定量的充填として、PhCl/PhBr/PhIの速度比較を明示的に実施した論文の独立同定が必要。Minato, A.; Tamao, K.; Hayashi, T.; Suzuki, K.; Kumada, M. *Tetrahedron Lett.* 1981 — スコープ拡張（secondary Grignard試薬への適用）論文として存在する可能性（Bibliographic confidence: Low、verification: [必須]）。EP-01aとのバンドル充填（Full Paper経由）。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: 未同定（インセンティブ構造的未充填）
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: 省略可（未充填のため）
* **Filling timescale category**: non-applicable（インセンティブ構造的未充填）
* **注記**: 対象系（Kumada反応、Table I各エントリ）での収率反復測定（n≥3）・標準偏差報告を独立主題とする論文は1972年以降に発表されていないと推定される。有機合成化学のインセンティブ構造（新規性を要求する出版慣行）のもとでは追試・反復測定の独立論文化が極めて困難であり、§Eで「インセンティブ構造的未充填」として記録する。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority]（Corriu/MasseのNi(acac)₂との直接比較不在）
* **充填開始点**: Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc., Chem. Commun.* 1972, 144 — 本論文のNote Added in Proofで引用された並行通信（Ni(acac)₂を使用）。技術的には対象論文と同時期の独立報告であり、「先行充填」または「並行充填」の変形として機能する（RI-09の問いを実験的形態で部分的に提示）。
* **充填確立点**: Kumada, M. et al. *Bull. Chem. Soc. Jpn.* 1976（Full Paper系列）— NiCl₂(dpe)とNi(acac)₂を同一基質・条件で直接比較するデータが含まれた可能性（中程度の信頼）。または独立した比較研究論文として: Jabri, N.; Alexakis, A.; Normant, J. F. — Ni触媒Grignardカップリングの配位子比較研究（Bibliographic confidence: Low — 著者名・年・雑誌ともに推測域）。
* **充填の性質**: Partial（Corriu/Masse 1972はNi(acac)₂での選択的カップリングを実証したが、NiCl₂(dpe)との同一基質・同一条件での直接比較という最厳格実装は未同定）
* **Bibliographic confidence**: High（Corriu/Masse 1972 — 対象論文に明示引用）/ Low（比較論文候補）
* **Filling adequacy confidence**: High（Corriu/Masse: Ni(acac)₂での選択的カップリング実証という部分充填は確実）/ Low（直接比較という完全充填は未同定）
* **Verification recommendation**: [必須] — (a)(c)条件（Corriu/Masse 1972、Kumada named reaction関連）
* **Bibliographic verification status**: Corriu/Masse 1972はpending verification（書誌は高信頼だが内容確認推奨）; 比較論文候補はpending
* **DOI / URL**: Corriu/Masse 1972: J. Chem. Soc., Chem. Commun. 1972, 144 — Crossref検索推奨。
* **Filling timescale category**: incentive-aligned（variable）— Ni(acac)₂との比較問題は配位子設計の概念的問いとして充填されるまで数年を要した可能性。
* **注記**: D4-8（Corriu/Masseとのbidentate ligand必要性問題）に直接対応。対象論文と並行して提出されたCorriu/Masse通信は「先行充填」の変形として機能するが、「同一基質・同一条件でのNiCl₂(dpe)対Ni(acac)₂の収率・選択性比較」という最厳格実装は、1972年時点でも1976年Full Paper以降も単独論文主題として充填されなかった可能性がある。この問いは成功したカップリング化学（Pd触媒系の台頭、不斉Kumada展開）による研究関心の移動により部分的に抹消された可能性を§Eで記録する。

---

**§B 末尾チェック：Bibliographic verification（条件付き実行）**

トリガー条件の評価：
- (a) 論文年代が古い（1972–1976年、1980年以前）: ✓ 全候補
- (b) 著者ネットワークが密（Tamao-Kumada研究グループから10件以上の関連論文）: ✓
- (c) 反応名がauthor nameに由来する命名規則（Kumada coupling）: ✓
- (d) Bibliographic confidence Medium-Lowの候補が2件以上: ✓

**判定: Verification recommendation [必須]** — §B中の全充填候補に適用。

「Bibliographic verification status: pending」のエントリは§C推奨選定リストで「⚠️ verification 待機中」として明示。

既知の hallucination パターン（Kumada系で報告済み）に注意：
- 著者組合せ捏造（"Tamao-Sumitani-Hayashi-Kumada"等の架空組合せ）
- 化学内容の誤記（Ni触媒をPdと混同、配位子の誤記）
- Morrell-Kochi 1975 の正確な主題（Ni対Pd、cross-couplingの対象系）

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958 | EP-01a, EP-02a, EP-05a（Partial）, EP-07a（Partial） | VQ-2（format-driven自動解消） | 1976 | Medium | High | ⚠️ 必須 / pending |
| 2 | Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc., Chem. Commun.* 1972, 144 | EP-09a（Partial） | VQ-4（RI-09充填起点） | 1972 | High | High | ⚠️ 必須 / pending |
| 3 | Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. *J. Am. Chem. Soc.* 1976, 98, 3718–3719 | EP-07a（Partial）, 配位子効果データ | VQ-2（スコープ・配位子系統化） | 1976 | Medium | Medium | ⚠️ 必須 / pending |
| 4 | Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* 1975, 97, 7262–7274 | EP-03a（Partial）, EP-06a（Partial） | VQ-3（機構的素反応実証） | 1975 | Medium | Medium | ⚠️ 必須 / pending |
| 5 | Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* 1979, 101巻（巻号ページ推測） | EP-06a（Partial〜Complete）, EP-03a（Partial） | VQ-3（Ni(0)/Ni(II)サイクル素反応実証） | 1979 | Medium | Medium | ⚠️ 必須 / pending |
| 6 | Kumada, M.; Tamao, K.; Sumitani, K. *Org. Synth.* 1978, 58, 127 | EP-02a（Partial〜Complete）, EP-07a（Partial） | VQ-2（手順書完全化） | 1978 | Medium | Medium | ⚠️ 必須 / pending |

**選定理由：**

推奨リストはVQ-2（論文1, 3, 6）→VQ-3（論文4, 5）の段階的な充填構造を示し、独自のVQ-4起点として機能するCorriu/Masse 1972（論文2）を加えて6報構成とした。論文1（Tamao et al. 1976 Full Paper）は格式上の自動解消（EP-01a, EP-02a）に加えてEP-05a・EP-07aのバンドル充填候補として最も効率的な選定である。論文2（Corriu/Masse 1972）は対象論文自身が引用した唯一の「充填起点」であり書誌信頼性が最高位であるため選定に値する（Partial充填にとどまるが、EP-09aの「先行充填」パターンを例示する）。論文4・5はKochi研究グループによる機構的研究として、SRG-1のRI-06/RI-03共起の分散的充填を記録するものであり、VQ-3要件の段階的解消を年代別に示す。

全候補が「⚠️ verification 待機中」であることは、Kumada named reaction・1972–1979年論文というトリガー条件の複合に由来する。Crossref APIまたはSciFinder/Web of Scienceによる書誌検証を経て正式選定リストへの昇格を推奨する（特に論文4・5のKochi論文の正確な主題確認）。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件 (EP-01a, EP-02a): Tamao et al. *Bull. Chem. Soc. Jpn.* 1976 → [1976年] [Tamao-Kumada研究グループ] [format-driven自動解消 / 自己充填]
- VQ-2 要件 (EP-07a, Partial): Tamao et al. 1976 Full Paper / Hayashi et al. JACS 1976 → [1976年] [自己充填 + 不斉応用からの副次的充填] [incentive-aligned]
- VQ-3 要件 (EP-03a, EP-06a, Partial): Morrell/Kochi JACS 1975 → [1975年] [Kochi研究グループ] [field-methodology / 自己充填なし / 分野横断充填]
- VQ-3 要件 (EP-06a, Partial): Tsou/Kochi JACS 1979 → [1979年] [分野横断充填] [field-methodology]
- VQ-3 要件 (EP-05a, Partial): Full Paper 1976経由 → [1976年] [自己充填] [format-driven]
- VQ-4 要件 (EP-09a, Partial): Corriu/Masse 1972 → [1972年] [独立グループ / 先行充填変形] [incentive-aligned]
- VQ-2 要件 (EP-04a): 未充填（または分散的間接充填、年代未確定）
- VQ-2–3 要件 (EP-08a): 未充填（インセンティブ構造的未充填）

**階層-時間対応の評価：**

本論文における充填の時間軸は、「VQ階層が高いほど充填に時間を要する」という一般仮説を部分的にしか支持しない。VQ-2要件（EP-01a）は1976年のFull Paper自動解消で充填されたが（4年後）、VQ-4起点（EP-09a, Corriu/Masse）は対象論文と並行する1972年に既に部分充填が存在した（「先行充填」変形）。VQ-3要件（EP-03a/EP-06a）はKochi 1975–1979の分野横断充填で段階的に前進したが、dpe-Ni特定の厳格な実装は現在も未確認である可能性がある。この非単調な時間構造は、「合成実用性層（層1-2）は早期にFull Paper経由で充填され、機構層（層3）はより長期・分散的に充填される」という§3の層別VQ非対称性（§6 [4]）と整合する。

**特筆すべきパターン：**

1. **自己充填（format-driven）**: SRG-3（RI-01）はTamao-Kumada研究グループ自身の1976年Full Paperによる自己充填として解消。通信→Full Paper遷移の自動解消パターン（§6 [5]）の典型事例として確認される。

2. **先行充填変形（EP-09a）**: Corriu/Masse 1972は「先行充填」の変形として機能する。対象論文（提出時）と競合する独立報告が、D4-8が記録したRI-09の実験的枠組みを提供している。しかしこれは「充填」というより「問いの構造的共有」であり、NiCl₂(dpe)とNi(acac)₂の同一条件比較（EP-09aの最厳格実装）は先行充填でも後続充填でも明確に実施されていない可能性がある。

3. **分野横断充填（EP-03a/EP-06a）**: Kochi研究グループ（Morrell 1975, Tsou 1979）による機構的研究は、Kumada研究グループの自己充填ではなく独立した機構化学研究グループからの分野横断充填として機能する。RI-06（サイクルレベル輸入）とRI-03（中間体未観測）の不可分共起（§6 [6]）により、どちらの充填も「部分的」にとどまる。

4. **「成功による問いの抹消」の予備的証拠（EP-05a, EP-09a）**: Kumada反応が合成化学的成功（不斉合成への展開、ノーベル賞関連化学との接続）を収めた結果、SRG-2（選択性の定量的根拠不在）およびSRG-4（sp²制限の機構的根拠不在）への直接検証需要が部分的に社会的消滅した可能性がある。この「成功による問いの抹消」は§Eで記録する。

5. **著者回顧との照合**: Kumada M.は*Pure Appl. Chem.* 1980, 52, 669（または類似の回顧論文）で本反応の成果と展開を振り返った可能性があり（Bibliographic confidence: Medium）、著者が回顧で認識した「特徴」とStage 3のEPリストの対応・非対応は「分野の内部者には不可視の構造的不在」の直接証拠として機能しうる。この回顧論文のverificationも推奨する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-04a [Discrimination / replication pack]**:
* **未充填の理由**: 分野的回避 + インセンティブ構造の不整合。cis/trans-スチルベン比の時間・温度系列実験（速度論/熱力学的制御の区別）はKumada反応の立体化学研究の一側面であるが、この問い（U-3: 比率の速度論的vs熱力学的性格の区別）は独立論文として主題化されにくい。cis-エンリッチという「異常な」観察（A-1）は機構的説明が困難であるため、後続研究が回避した可能性がある。さらに、Pd触媒クロスカップリングへの関心移動（1970年代後半）により、Ni触媒系の立体化学的詳細への専念的研究が相対的に縮小した可能性がある。
* **発見的意義**: あり。「cis/trans選択性の速度論的vs熱力学的性格」という問いは、Kumada反応が確立した「合成手法」として広く使用されている現在でも実験的に未解決のまま残存している可能性がある。現代のin-situ NMRおよびDFT計算で原理的に充填可能な問いが50年以上未充填という事実は、「成功した合成手法の選択性起源は問われない」という分野インセンティブの構造的証拠として記録できる。
* **将来の充填可能性**: 高 — 現代のin-situモニタリング（低温 ¹H NMR, 低温 ³¹P NMR）と停止法実験（quench at multiple time points）およびDFT計算（反応経路エネルギープロファイル）の組み合わせで原理的に充填可能。

---

**EP-05a [Quantitative-ranking substantiation pack] — 完全充填の欠落部分**:
* **未充填の理由**: 成功による問いの抹消（Success-driven question erasure）。eq (3)が予測するR-R（ホモカップリング生成物）の定量的不在証明という最厳格実装は、Kumada反応が「選択的」という評判を合成コミュニティで確立した後、その証明需要が消滅したと推定される。現代のGC-MSを用いた反応混合物の完全質量収支はFull Paperにも記述されていない可能性があり、SRG-2のB-1/U-1が提示した「eq(3)予測のR-Rが検出されない条件の定量的確認」は後続研究の主題にならなかったと推定される。
* **発見的意義**: あり。「選択的」という記述が50年以上にわたって定量的根拠なしに使用されてきた可能性を示す。eq(3)が予測するホモカップリング生成物の明示的定量は、Kumada反応の機構論文（RI-06関連）でも欠落している可能性があり、「分野が体系的に実施しなかった質量収支測定」として記録できる。
* **将来の充填可能性**: 高 — 現代のGC-MSで容易に実施可能。技術的障壁は存在しない。充填されない理由はインセンティブ構造のみ。

---

**EP-08a [Replication / uncertainty pack]**:
* **未充填の理由**: インセンティブ構造的未充填（パターン①）。Table Iの各収率エントリの独立反復測定（n≥3）・標準偏差報告を主題とする論文は、有機合成化学の出版慣行において1972年以降も系統的に実施されない。新規性を要求する学術誌での「追試・反復測定」の独立論文化は困難であり、方法論論文としても対象系の統計的評価は主題にならない。Org. Synth.の手順書への収録（候補: Kumada et al. 1978）が反復実施の唯一のインセンティブ整合的枠組みであるが、Org. Synth.でも統計的記述は慣行的に行われない。
* **発見的意義**: 中程度。「合成収率データの統計的信頼性」問題は有機合成化学全般の分野慣行として現在も未解決であり、Kumada 1972がその典型的事例として機能する。しかし、この問いの未充填は対象論文固有の問題ではなく分野普遍的な構造的問題であり、個別論文分析の発見的意義は限定的。
* **将来の充填可能性**: 中 — 技術的に可能だが出版インセンティブの不整合が解消されない限り独立論文化は困難。再現性危機への科学コミュニティの対応（open science, replication journals）が進展すれば充填可能性が高まる。

---

**VQ階層逆転の診断：**

EP-08a（RI-08, VQ-2要件）が未充填の一方で、EP-03a/EP-06a（RI-03/RI-06, VQ-3要件）への充填が（部分的にではあれ）進展した事実は、「低VQ要件（reporting quality, RI-01/RI-08）が未充填、高VQ要件（mechanism, RI-03/RI-06）が充填」というVQ階層逆転パターンを示している。これは「科学的論理に基づく充填順序（VQ-2→VQ-3）」ではなく「出版インセンティブに基づく充填順序（新規性の高いVQ-3が先行）」の逆転として記録できる。Kumada反応において機構的解明（新規性高、独立論文化容易）が統計的再現性確立（新規性なし、独立論文化困難）より先行したことは、分野インセンティブ構造がUQSの構造的不在の一部（SRG-3の完全充填不在）を維持していることの実証例として機能する。
```
