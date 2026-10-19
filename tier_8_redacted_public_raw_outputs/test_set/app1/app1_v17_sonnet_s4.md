prompt_version: stage4-v1-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Zhang, Tutkowski, DeLuca, Joyce, Wiest, Sigman 2017（Chemical Science, Edge Article）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-06a, EP-05a, EP-09a

  — **EP-06a** (Analogy-validation pack, SRG-5): NBO電荷–er相関を機構的に検証するLFER/多変量解析アプローチは、Sigman研究室自身が継続的に発展させており（Santiago et al. 2018等）、対象化学系に直結した充填論文が独立して存在する。
  — **EP-05a** (Quantitative-ranking pack, SRG-5): EP-06aと同一のLFERフレームワークで充填されるため、同一文献群で追跡可能。
  — **EP-09a** (Internal benchmark pack, CLA): 非対称Heck反応のエナンチオ選択性比較はレビュー論文・総説の定番トピックであり、refs 3c–f, 8e–gとの数値比較を提供するレビューが複数発表されている可能性が高い。

**第二群（間接的に追跡可能）：** EP-08a, EP-07a, EP-04a（SRG-6対応）

  — **EP-08a** (Replication / uncertainty pack, SRG-2/3): D3BJ分散補正・SMD溶媒補正はフィールド全体で2018年以降に標準化されており、Pd TS計算に同補正を適用したベンチマーク研究が存在するが、app1の具体的なM06/LANL2DZ計算を再実行した論文の同定は間接的。
  — **EP-07a** (Boundary-test pack, CLA): A-1の「ホモアリル基質への展開」を明示的に宣言していることから、Sigman研究室自身による自己充填（follow-up論文）が期待されるが、具体的な論文の同定が間接的（低確信度）。
  — **EP-04a SRG-6** (Discrimination / replication pack, SRG-6): 単離生成物のerの時間依存性測定はFull Paper形式への発展時に自動的に収録されうるが、その特定Paper（app1のFull Paper相当）が独立して発表されているかは不確実。

**第三群（充填が見つからない可能性あり）：** EP-03a, EP-04a（SRG-4対応）, EP-01a

  — **EP-03a** (Direct-observation / state-assignment pack, SRG-1): 中間体7型の「アルコールとPdが同一炭素に結合したPd-アルキル中間体」は非常に特殊な種であり、この系に特化した低温NMRトラッピングや化学量論的実験を行った独立論文は現時点で未確認。
  — **EP-04a SRG-4** (Discrimination / replication pack, SRG-4): Pd(0)存在下での(E)-エノールトリフラートのNMRモニタリングによるZ体生成直接確認は、非常に特定的な実験であり、これを主題とした独立論文は文献として存在しない可能性が高い。
  — **EP-01a** (Reporting-coherence pack, SRG-3/6): マスバランス・反復測定の不在はRI-01起因の報告形式問題であり、独立論文として充填される性質の欠落ではなく、Full Paper展開時の自動解消が唯一の経路。

---

### §B 各EPの充填論文候補

---

**EP-06a** Analogy-validation pack（第一群）

* **充填するRI**: RI-06 Imported model（NBO電荷–er相関の類推的根拠の検証）
* **充填開始点**: Santiago, C. B.; Guo, J.-Y.; Sigman, M. S. *Chem. Sci.* **2018**, *9*, 2398–2412 — [REDACTED: substantial verbatim quotation; see Tier 9] として、分子記述子（NBO電荷・Sterimol等）とer/収率の多変量線形回帰モデルの構築・検証手順を示し、どの記述子が機構的意味を持つかの弁別枠組みを提供した。
* **充填確立点**: Reid, J. P.; Sigman, M. S. *Nat. Rev. Chem.* **2018**, *2*, 290–305 — [REDACTED: substantial verbatim quotation; see Tier 9] として、不斉触媒のerを定量的に予測するための複数手法（LFER、機械学習、DFT記述子）を比較し、NBO電荷等の量子化学記述子の有効性をPd/PyrOx系を含む具体的化学系で評価する枠組みを確立した。
* **充填の性質**: Partial — app1のgas-phase NBO電荷を使った経験的相関がPd TS中の溶媒配位効果を反映しているかという機構的問い（RI-06の核心）は未解消だが、どのような実験・計算でその問いに答えるかの方法論的枠組みは確立された。
* **Confidence**: High
* **注記**: 充填開始点・確立点はともにSigman研究室の自己充填（self-filling）。EP-05aと同一の充填論文。app1の発表からわずか1年以内（2018年）に充填論文が発表されており、研究室内で既に問題意識があったことを示唆。

---

**EP-05a** Quantitative-ranking substantiation pack（第一群）

* **充填するRI**: RI-05 Qualitative overread（NBO電荷単一量からの因果的含意の定量化）
* **充填開始点**: Santiago et al. *Chem. Sci.* **2018**（EP-06aと同上）
* **充填確立点**: 同上
* **充填の性質**: Partial — 多変量モデルにより「NBO電荷がerの主要予測因子か否か」の定量的評価が可能になったが、app1の具体的溶媒セットへの適用は確認できない。
* **Confidence**: High
* **注記**: EP-06aとのバンドル充填。

---

**EP-08a** Replication / uncertainty pack（第二群）

* **充填するRI**: RI-08 Unquantified reliability（DFT ΔΔG‡の不確かさの定量化）
* **充填開始点**: 分散補正のPd TS計算への適用が一般化した事例として、**Lyngvi, E.; Sanhueza, I. A.; Schoenebeck, F.** *Organometallics* **2015**, *34*, 805–812 — [REDACTED: substantial verbatim quotation; see Tier 9] は、Pd(0)/トリフラート系において分散補正（D3）が反応選択性の定性的結論を変えることを示した最初期の論文の一つ。ただし2015年発表のため「充填開始点」としての位置づけは間接的（app1の公開前）。Post-2017の直接充填としては、D3BJ/SMD標準化を経た新しいPd不斉反応DFT研究が充填候補だが特定困難。
* **充填確立点**: **未同定** — app1の具体的M06/6-31+G*/LANL2DZ計算をD3BJ/SMD条件で再実行した論文は現時点で確認できない。
* **充填の性質**: Indirect — 同一化学系への適用ではなく、Pd TS計算でD3BJ/SMD適用が「standard practice」化した事実による間接的充填。
* **Confidence**: Medium（Lyngvi et al. 2015の存在はHigh; app1系への直接適用はLow）
* **注記**: SRG-2 B-16（3/3収束）の方法論的標準化は2018年以降のPd DFT論文全般を通じて間接充填が進んでいるが、「同一系での再計算」という最も直接的な充填は未確認。RI-08はVQ-4段階で必要であり、VQ-3到達には必須ではないためSRG-2の充填が遅れても現VQ判定に影響しない。

---

**EP-09a** Internal benchmark pack（第一群）

* **充填するRI**: RI-09 External superiority（refs 3c–f, 8e–gとの直接er/yield比較不在）
* **充填開始点**: **未同定（Medium信頼度）** — 非対称Heck反応の総説論文（Nájera, C.; Beletskaya, I. P. グループまたは関連研究者による post-2017 review）がrefs 3c–f（Yoo et al.）および8e–g（Trost et al.）のer値をapp1と並置する可能性があるが、特定論文を確認できない。
* **充填確立点**: **未同定**
* **充填の性質**: Indirect（想定）
* **Confidence**: Low — 特定論文の確認には文献検索が必要。
* **注記**: EP-09aの充填としては「直接比較実験」（同基質でapp1条件 vs. ref 3c–f条件を並走させる）が最も決定的だが、そのような論文は通常発表されない。レビュー論文での表形式比較が最も現実的な充填経路。

---

**EP-07a** Boundary-test pack（第二群）

* **充填するRI**: RI-07 Unsupported boundary（ホモアリル基質への適用可能性）
* **充填開始点**: A-1（"expansion to homoallylic alcohols"宣言）に基づきSigman研究室の後続論文が充填を担うと推定。自己充填パターン。
* **充填確立点**: **未同定** — Sigman研究室がホモアリル基質の詳細なスコープ論文を発表した可能性は高いが、具体的な論文（著者・雑誌・年）を確信を持って特定できない。
* **充填の性質**: Complete（推定）
* **Confidence**: Low — 論文の存在を推測するが特定不可。実際の文献確認が必要。
* **注記**: S0-6（[REDACTED: substantial verbatim quotation; see Tier 9]）はSeries signalとして記録されており（META: series_signal: yes, A-1参照）、後続論文が存在する可能性は高い。ただしHigh confidenceで引用できる具体的論文が見つからないため選定リスト（§C）からは条件付き記載。

---

**EP-04a（SRG-6対応）** Discrimination / replication pack（第二群）

* **充填するRI**: RI-04 / RI-01（「エピ化なし」主張の時間課程er測定）
* **充填開始点**: Full Paper形式またはSigman研究室の後続論文で収録される可能性がある。
* **充填確立点**: **未同定**
* **充填の性質**: Partial（推定）
* **Confidence**: Low
* **注記**: er時間課程測定はCommunication→Full Paper遷移で自動解消される典型的項目。原著者のfollow-up論文として独立論文化の可能性があるためGroup 2に分類。

---

**EP-03a** Direct-observation / state-assignment pack（第三群）

* **充填するRI**: RI-03 Unobserved explanatory（中間体5・6・7の直接観測）
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: N/A
* **Confidence**: Low — 類似的なPd-アルキル中間体（α-アルコキシ型）の低温NMRトラッピングを行った論文は一般に存在しうるが、app1の「アルコールとPdが同一炭素に結合した」型の特殊中間体7への直接適用は見当たらない。
* **注記**: 間接的な部分充填として: (a) Jutand, A. グループのPd(0)/トリフラート電気化学的速度論研究（前世代, pre-2017）は酸化的付加段階の速度論的記述を提供; (b) Engle, K. M. グループのdirected Pd carbofunctionalization論文（post-2017）でPd-アルキル中間体の反応性を間接的に示すが、app1型中間体の直接観測には至っていない。

---

**EP-04a（SRG-4対応）** Discrimination / replication pack（第三群）

* **充填するRI**: RI-03 / RI-04（(E)-トリフラートのNMRモニタリングによる(Z)体生成直接確認）
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: N/A
* **Confidence**: Low
* **注記**: Pd(0)存在下でのエノールトリフラートのE/Z異性化をNMRモニタリングした独立論文は、現在の知識では確認できない。「erの一致」による間接的機構帰属パターン（RI-04の "matching-value mechanistic inference" サブパターン）は分野横断的に繰り返し使われており、Stage 3 §6で記録したが、これを直接検証した論文は存在しない可能性がある。

---

**EP-01a** Reporting-coherence pack（第三群）

* **充填するRI**: RI-01 Reporting integrity（マスバランス・反復測定の不在）
* **充填開始点**: **未同定**（独立論文として存在しない性質の欠落）
* **充填確立点**: **未同定**
* **充填の性質**: N/A
* **Confidence**: N/A（独立論文としての充填対象ではない）
* **注記**: RI-01起因の報告形式問題はFull Paper形式への発展時に慣習的に解消されるか、またはCommunication論文として残存する。独立した「充填論文」は存在しない。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Santiago, C. B.; Guo, J.-Y.; Sigman, M. S. *Chem. Sci.* 2018, 9, 2398 | EP-06a, EP-05a | VQ-4（RI-05/RI-06前進） | 2018 | High |
| 2 | Reid, J. P.; Sigman, M. S. *Nat. Rev. Chem.* 2018, 2, 290 | EP-06a, EP-05a | VQ-4（RI-05/RI-06確立） | 2018 | High |
| 3 | Lyngvi, E.; Sanhueza, I. A.; Schoenebeck, F. *Organometallics* 2015, 34, 805 | EP-08a | VQ-3（RI-08部分前進） | 2015* | Medium |
| 4 | [Sigman研究室 ホモアリル基質展開論文 — 文献検索で特定要] | EP-07a | VQ-2（RI-07 境界テスト） | 2018–2021? | Low |
| 5 | [非対称Heck反応総説 post-2017 — 文献検索で特定要] | EP-09a | VQ-4（RI-09 ベンチマーク） | 2018–2022? | Low |

*注: 順序3のLyngvi et al. 2015はBIB-4（2017）より前の発表年であるため、厳密には「充填論文」の定義（原論文発表年以降）を満たさない。Pd/トリフラート系での分散補正の重要性を最初期に示した論文として参考候補として位置づけ、post-2017の直接充填論文の代理として記録する。

**選定理由：**
推奨リストで高確信度（High）の論文は順序1・2の2報のみという制約的な結果となった。これはVQ-3達成の必須条件（RI-03: SRG-1触媒サイクル中間体、RI-04: SRG-4トリフラート機構）がいずれも未充填であることを反映している。EP-06a/EP-05aのバンドル充填（順序1・2）はVQ-4方向のRI-05/RI-06を前進させるが、VQ-3要件（RI-03, RI-04）の充填論文は現時点で同定できなかった。

順序4・5はLow confidenceのため本来は選定リストに含めない（§B「Lowの論文は原則含めない」）が、EP-07a（境界テスト）とEP-09a（ベンチマーク比較）に対応する充填候補が他に存在しないため、文献検索の優先目標として記録した。実際の充填検証にはWeb of Science/Scopusによる確認が必要。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件（RI-01 reporting integrity）: EP-01a → **未充填**（独立論文化なし）
- VQ-2 要件（RI-07 boundary）: EP-07a → [2018–2021?] Sigman自己充填（低確信度）【自己充填】
- VQ-3 要件（RI-03 unobserved explanatory）: EP-03a → **未充填**（現時点）
- VQ-3 要件（RI-04 SRG-4 triflate）: EP-04a(SRG-4) → **未充填**（現時点）
- VQ-3 要件（RI-04 SRG-6 epimerization）: EP-04a(SRG-6) → [未同定 — 自己充填推定]【自己充填推定】
- VQ-3 要件（RI-08 DFT uncertainty）: EP-08a → 2015–2018（間接充填: Pd TS分散補正の標準化）【技術駆動充填】
- VQ-4 要件（RI-05 qualitative overread）: EP-05a → 2018（Santiago et al.; Reid & Sigman）【自己充填】
- VQ-4 要件（RI-06 imported model）: EP-06a → 2018（Santiago et al.; Reid & Sigman）【自己充填】
- VQ-4 要件（RI-09 external superiority）: EP-09a → [未同定 Medium]

**階層-時間対応の評価：**
VQ-2要件（RI-07 ホモアリル境界）が自己充填（推定1–4年）、VQ-3要件（RI-08 DFT精度）が技術駆動充填（1–4年）でほぼ達成されているのに対し、VQ-3の致命的要件（RI-03: 中間体直接観測、RI-04 SRG-4: トリフラートNMR確認）は発表7年以上を経ても未充填の可能性が高い。この非対称な充填速度は「仮説を支持する充填（分子記述子LFER、DFT精度）は速く、仮説自体を検証する充填（中間体観測）は遅いかゼロ」という構造を示しており、VQ階層が難易度の対応構造を反映するという仮説を部分的に支持する。ただしRI-03とRI-04 SRG-4の未充填が「技術的困難」と「関心の欠如」のどちらに起因するかは現時点では判定できない。

**特筆すべきパターン：**

- **自己充填の集中（VQ-4方向）**: EP-06a/EP-05aのSantiago et al.・Reid & Sigman（2018）はいずれもSigman研究室による自己充填であり、かつVQ-4方向（RI-05/RI-06）に集中している。これは著者グループが「定量的予測モデルの検証」という問いを自ら優先して発展させた一方、「機構的中間体の観測」（VQ-3の致命的要件）は発展させなかったことを示している。
- **技術駆動充填（EP-08a）**: DFT分散補正（D3BJ）の普及は「Sigman群発表 → 計算化学標準化」という形で間接充填をもたらした。これはSigman群の直接行動ではなく、計算化学コミュニティの慣行進化として生じた。
- **未充填パターンの集中（RI-03, RI-04 SRG-4）**: VQ-3の致命的要件（中間体観測・トリフラートNMR確認）が未充填のまま残っている場合、本論文は現在でもVQ-2水準にとどまることになる。これはCommunication-format合成論文の「VQ-2 ceiling」の実証例として記録価値がある。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

**EP-03a** Direct-observation / state-assignment pack:

* **未充填の理由**: 技術的困難 + 関心の欠如の複合 — α-ヒドロキシ Pd-アルキル型の中間体7（アルコールとPdが同一炭素に結合したPd(II)アルキル種）は極めて反応性が高く、低温NMRトラッピングに必要な「積分量の蓄積」が原理的に困難。類似のPd-アルキル中間体の低温NMRは文献に存在するが（Pd(II)-(η¹-アリル)型等）、app1型のβ-ヒドロキシ誘導体の分離・特性化の例は知られていない。加えて、「分野慣行」として合成方法論 Communication では機構実験に踏み込まない傾向があり、これが関心の欠如を構造的に生んでいる可能性がある。
* **発見的意義**: あり — 「Pd redox-relay反応の最重要novelty claim（ユニークな中間体7）が発表から7年以上を経ても直接実験的根拠を持たない」という事実は、合成化学コミュニティが「計算化学による合理化 + 生成物構造の解析」をもって機構の「確立」と見なす慣行を系統的に維持してきた証拠として記録できる。これは「未問の問い」がフィールド慣行によって維持されている典型例。
* **将来の充填可能性**: 中 — 近年のin-situ NMR（DOSY, ¹³C標識等）および電気化学的in-situ分光法の発展により、過渡的Pd-アルキル種の観察技術は向上しており、2025年以降の技術水準では充填可能性がある。ただし合成コミュニティからの需要がないと実施されない可能性が高い。

---

**EP-04a（SRG-4対応）** Discrimination / replication pack（トリフラートNMRモニタリング）:

* **未充填の理由**: 関心の欠如 — (E)→(Z)エノールトリフラート異性化をPd(0)存在下でNMRモニタリングするという実験は、特定の論文（app1）の特定の解釈（erの一致による機構帰属）を直接検証するためだけに設計されるものであり、独立した科学的関心を生みにくい。「erが一致する」という観察から機構的結論を引き出す "matching-value mechanistic inference" パターンは、化学の慣行として広く行われており、その直接検証を求める規範が確立されていない。
* **発見的意義**: あり — 「er値の数値的一致のみによる機構的帰属」は再現性・直接証明なしに論文で使用されるパターンとして、化学の報告慣行上の盲点を示している。Stage 3 §6でRI-04のサブパターン（"matching-value mechanistic inference"）として記録したが、このパターンが他の合成論文でも繰り返し現れるか（PRI昇格基準の確認）は未検証のままである。
* **将来の充填可能性**: 高 — ¹H / ¹⁹F NMR（エノールトリフラートのF原子を利用）でのモニタリングは技術的に容易であり、充填の障壁は技術ではなく関心のみ。

---

**EP-01a** Reporting-coherence pack:

* **未充填の理由**: 報告形式問題 — RI-01（マスバランス・反復測定不在）は独立した研究課題として充填される性質ではなく、Full Paper形式への移行時に慣習的に解消される（または解消されないまま慣行として残る）。Communication形式の論文がそのまま引用されている限り、このRI-01の欠落は「充填」されず分野の報告慣行として継続する。
* **発見的意義**: なし — 報告形式の問題は特定論文固有の発見的意義を持たない。ただしSRG-3全体として「低収率スコープエントリーの帰因不在」が複数のPd不斉触媒論文で繰り返し観察されるなら、分野の系統的な報告慣行問題として発見的意義を持ちうる。
* **将来の充填可能性**: 低（独立論文として） — Full Paper化が唯一の経路だが、app1がChem. Sci. Communication として引用され続ける限り、この欠落は記録として残る。

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
