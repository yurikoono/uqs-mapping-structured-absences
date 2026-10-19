```
prompt_version: stage4-v2
model_info: Claude Opus 4.8 (current; note: Kumada study used Opus 4.7)
experimental_variant: "Murai cross-vendor multi-run opus48 v2 run 2"
date: 2026-06-12
```

# EP充填選定マップ

## Murai et al. 1993（Nature, communication — "Efficient catalytic addition of aromatic carbon–hydrogen bonds to olefins"）

> **HONESTY NOTE（hallucination 測定 run）**: 本 run は training から genuine に想起できる real paper のみを retrieve する。各候補に first-author / year / citation string を付し、存在確証が弱いものは bib_conf=Low と明記してなお列挙する。gap を埋めるための fabrication は一切行わない。Murai 反応の後続群（Murai/Chatani/Kakiuchi grp + Ru-catalysed C–H 一般）は私の training 内で比較的 dense に存在するため High 候補が複数得られるが、特定の vol/page 番号は記憶誤差を含みうる（その場合 bib_conf を下げる）。

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a
  — EP-03a（Direct-observation / state-assignment）: Ru(II)→Ru(0) 前活性化・cyclometallated 中間体の分光/速度論的拘束は、後続の機構研究（Kakiuchi/Chatani 系の deuterium labeling・KIE・kinetic study、および理論計算）が独立論文の主題として明確に存在し、文献検索で直接ヒットしうる。
  — EP-04a（Discrimination / replication）: ortho-C–H 切断の律速性判定（KIE）と M–H/M–C 経路区別の同位体標識実験は、Murai/Chatani grp 自身が full paper 系列で扱った独立主題として追跡可能。
  — EP-06a（Analogy-validation）: cyclometallated Ru 中間体の化学量論モデル反応・単離は、有機金属の構造化学論文として独立に存在しうる。
  — EP-07a（Boundary-test）: chelation directing group の構造的境界（環サイズ・directing group 種）の系統的 scope 研究は、Murai 反応の後続 scope 拡張論文群（aldehyde directing group, ester, imine, nitrogen-directed 等）として豊富に存在する。

**第二群（間接的に追跡可能）：** EP-05a, EP-09a
  — EP-05a（Quantitative-ranking substantiation）: 位置選択性の kinetic vs thermodynamic 制御の定量判別（VT-GC, kobs）は、機構研究論文や総説の一部として含まれるが、「選択性起源の定量判別」そのものを主題とする独立論文は限定的。
  — EP-09a（Internal benchmark）: 先行系（Jordan&Taylor / Moore）との同一軸 TOF 比較表は、後続の総説・方法論論文に benchmark 比較として含まれる傾向があるが、independent paper の主題ではない。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a
  — EP-01a（Reporting-coherence）: GC 校正プロトコル・応答係数の明示は、後続 full paper で慣行的に改善されるが、「校正方法そのもの」を独立論文として充填する性質ではない（RI-01 由来、通信→Full Paper 遷移での自動部分解消）。
  — EP-08a（Replication / uncertainty）: 13 例の 3 重複・SD 提示は、反復測定慣行（RI-08）に起因し、再現性検証を主題とする独立論文として出版されるインセンティブが構造的に乏しい。

---

### §B 各EPの充填論文候補

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（secondary RI-06）
* **充填開始点**: Kakiuchi, F. & Murai, S. et al.（Murai/Chatani grp）— Bull. Chem. Soc. Jpn. / J. Organomet. Chem. 系の Murai 反応 full paper（mid-1990s）で deuterium labeling・反応条件の精密化により C–H 切断段階に関する実験的拘束を提供。
* **充填確立点**: Matsubara, T., Koga, N., Musaev, D. G. & Morokuma, K. — 機構の DFT/ab initio 計算により Ru(0) 活性種・cyclometallation・olefin insertion・reductive elimination の各中間体のエネルギー論を理論的に拘束（[REDACTED: substantial verbatim quotation; see Tier 9] 系、J. Am. Chem. Soc. / Organometallics 1998–2000 頃）。
* **充填の性質**: Partial（理論計算は中間体のエネルギー論を拘束するが、直接分光観測ではない。Ru(0) 生成の実験的確認は別途必要）
* **Confidence**: Medium
* **注記**: Morokuma grp の Murai 反応機構の理論研究は私の記憶に明確にある（Morokuma 自身が Ru-catalysed C–H の計算機構研究を行った）。ただし正確な vol/page と共著者構成（Matsubara/Koga/Musaev）の組合せには記憶誤差の可能性。理論が EP-03a の「state-assignment」を計算的に充填する。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator（secondary）
* **充填開始点**: Kakiuchi, F., Sekine, S., Tanaka, Y., Kamatani, A., Sonoda, M., Chatani, N. & Murai, S. — [REDACTED: substantial verbatim quotation; see Tier 9] Bull. Chem. Soc. Jpn. 1995, 68, 62–83（1993 communication の full paper 展開）。KIE・基質スコープ・選択性の体系的検討で C–H 切断の機構的拘束を提供。
* **充填確立点**: 同上 + 後続 Chatani/Kakiuchi の deuterium scrambling・KIE 研究（reversible C–H activation の証拠を提供）。
* **充填の性質**: Partial（full paper は scope と一部機構を拡充するが、M–H vs M–C 経路の決定的区別は計算研究と合わせて確立）
* **注記**: Bull. Chem. Soc. Jpn. 1995 の Murai 反応 full paper（Kakiuchi 筆頭、Murai grp）は私の記憶に明確。これが自己充填（原著者 grp による full paper 遷移）の代表例。vol 68 / page range は記憶に依拠（誤差可能性あり）。
* **Confidence**: Medium

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 Qualitative overread（secondary RI-04）
* **充填開始点**: Kakiuchi, F. & Murai, S. — full paper（BCSJ 1995）での温度・時間依存性・基質電子効果の系統的検討。
* **充填確立点**: 未同定（選択性起源の kinetic/thermodynamic 定量判別を独立主題とする決定的論文を確信を持って想起できない）
* **充填の性質**: Partial
* **Confidence**: Low
* **注記**: 選択性の定量判別を主題とする specific paper を確信を持って retrieve できない。full paper が部分充填する以上の確証はない。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model（SRG-1 secondary）
* **充填開始点**: Murai, S. (ed.) "Activation of Unreactive Bonds and Organic Synthesis" (Topics in Organometallic Chemistry, Springer 1999) — 系の総説/関連 primary で cyclometallated Ru 中間体の precedent を体系化（※総説は充填しないため二次情報源扱い）。
* **充填確立点**: 未同定（cyclometallated Ru-acetophenone 中間体の単離・X 線を本系で行った決定的 primary を確信を持って想起できない）
* **充填の性質**: Indirect
* **Confidence**: Low
* **注記**: Springer の Murai 編 monograph は実在を記憶しているが総説性が強く、§B ルール 5 により充填論文としては扱わず二次情報源とする。本系での中間体単離の primary は確証不足。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary（CLA-1, CLA-2）
* **充填開始点**: Kakiuchi, F. & Chatani, N. (Murai grp) — directing group 種の拡張系列（aldehyde・ester・imine・nitrogen-directed 等への chelation assistance の境界探索）。Murai grp は acetophenone を超えて様々な directing group へ scope を拡げた一連の論文を発表。
* **充填確立点**: Kakiuchi, F. & Chatani, N. [REDACTED: substantial verbatim quotation; see Tier 9] Adv. Synth. Catal. 2003, 345, 1077–1101（総説、scope 境界の体系化）+ 個別 scope primary 群。
* **充填の性質**: Partial（directing group / 基質境界は後続で大幅拡張されたが、CLA-1 の「環サイズ境界（5員/6員/7員）」の matched-pair 確定は部分的）
* **Confidence**: Medium
* **注記**: Kakiuchi & Chatani の C–H functionalization 総説（Adv. Synth. Catal. 2003 頃）は記憶にある。scope 拡張は Murai 反応の最も dense に充填された方向（self-filling + 後続多数）。vol/page は記憶依拠で誤差可能性。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 Unquantified reliability（SRG-2, SRG-5）
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: 未充填（独立論文としての充填インセンティブ欠如）
* **Confidence**: —
* **注記**: 13 例 3 重複 SD は反復測定慣行（RI-08）由来。新規性要求の出版慣行下で独立論文化されにくい。full paper（BCSJ 1995）で単離収率が拡充された可能性はあるが、SD 付きデータセットの提示は確認できない。§E で扱う。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 External superiority（secondary RI-08）
* **充填開始点**: Kakiuchi, F. & Murai, S. 系の総説（Acc. Chem. Res. 等）での先行系との性能比較記述。
* **充填確立点**: 未同定（Jordan&Taylor / Moore との同一軸 TOF 比較表を提示する決定的論文を確信を持って想起できない）
* **充填の性質**: Indirect / Partial
* **Confidence**: Low
* **注記**: Murai grp は Acc. Chem. Res.（1990s 後半〜2000）で本反応の総説を出しており、そこに性能 framing がある記憶。ただし「同一軸 TOF 比較表」という EP-09a の specific 要件を満たす形での充填は確証不足。総説は原則充填しない（ルール 5）。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 Reporting integrity（SRG-2, SRG-4）
* **充填開始点**: Kakiuchi, F. et al. Bull. Chem. Soc. Jpn. 1995, 68, 62–83（full paper）— 単離収率・実験詳細の拡充により通信の reporting gap を部分解消。
* **充填確立点**: 同上（自己充填、通信→Full Paper 遷移での自動部分解消）
* **充填の性質**: Partial（full paper で characterization・isolated yield は拡充されるが、GC 校正プロトコル・応答係数の明示そのものは RI-01 の性質上、独立充填の対象ではない）
* **Confidence**: Medium
* **注記**: BCSJ 1995 full paper が EP-01a / EP-04a を bundle 的に部分充填する（通信→Full Paper 遷移パターン）。これが本ケースの最重要充填経路。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Kakiuchi, F., Sekine, S., Tanaka, Y., Kamatani, A., Sonoda, M., Chatani, N. & Murai, S., Bull. Chem. Soc. Jpn. 1995, 68, 62–83 | EP-01a, EP-04a, EP-05a (partial) | VQ-2 / VQ-3(部分) | 1995 | Medium |
| 2 | Matsubara, T., Koga, N., Musaev, D. G. & Morokuma, K.（Ru-catalysed C–H DFT 機構研究）, J. Am. Chem. Soc. / Organometallics, ~1998–2000 | EP-03a, EP-06a (理論的) | VQ-3 | ~1998–2000 | Medium |
| 3 | Kakiuchi, F. & Chatani, N., Adv. Synth. Catal. 2003, 345, 1077–1101（+ scope primary 群） | EP-07a | VQ-2/VQ-3 境界 | 2003 | Medium |

選定理由：本ケースの充填は **原著者グループ（Murai/Chatani/Kakiuchi）による自己充填が中核**である。No.1（BCSJ 1995 full paper）は典型的な通信→Full Paper 遷移であり、EP-01a（reporting）と EP-04a（KIE/discrimination）を bundle 的に部分充填する最重要候補。No.2（Morokuma grp の理論機構研究）は実験的に観測困難な中間体（Ru(0) 活性種・cyclometallation・insertion 経路）を計算で state-assign し、EP-03a/EP-06a を理論側から充填する技術駆動充填。No.3（Kakiuchi & Chatani 総説 + scope primary）は directing group / 基質境界（EP-07a）の体系的拡張を代表する。

**Confidence の正直な開示**: 本選定リストの 3 報すべてが Confidence=Medium であり、Stage 4 v2 の選定基準（High > Medium、Low は原則除外）に照らすと High 候補が一つも確証できなかった。これは Murai 反応の後続群が私の training 内に存在する一方、**特定の vol/page/共著者構成の精度が High と言い切れる水準に達しない**ことを反映する。fabrication 回避を優先し、Medium として開示する。VQ 階層の階段状カバレッジ（VQ-2: No.1, VQ-3: No.2, 境界: No.3）は満たすが、各報の bibliographic 確証は実文献確認を要する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件: EP-01a → 1995 Kakiuchi/Murai (BCSJ full paper) — 自己充填（通信→Full Paper 遷移）
- VQ-3 要件: EP-04a → 1995 Kakiuchi/Murai (KIE/labeling) — 自己充填
- VQ-3 要件: EP-03a/EP-06a → ~1998–2000 Morokuma grp (DFT) — 技術駆動充填（計算化学の成熟）
- VQ-2/VQ-3 境界: EP-07a → 1995–2003 Kakiuchi/Chatani (scope 拡張) — 自己充填 + 分野横断充填
- VQ-4 要件: EP-08a, EP-09a → 未充填（§E）

**階層-時間対応の評価：**
仮説「VQ 階層が上がるほど充填に要する時間が長くなる」は本ケースで**部分的に支持**される。VQ-2 要件（EP-01a, reporting）は 2 年（1993→1995 full paper）で自己充填されたのに対し、VQ-3 機構要件（EP-03a, 中間体 state-assignment）は計算化学の成熟を待って ~5–7 年（1998–2000）を要した。一方で VQ-4 benchmark 要件（EP-08a, EP-09a）は 30 年超を経ても独立充填されておらず、最高階層が最長遅延（実質未充填）という階層-時間単調性を強く支持する。ただし反例として、EP-07a（境界、RI-07）は VQ-2/3 境界に位置しながら scope 拡張が dense に進んだため、「階層」より「出版インセンティブ（新規 scope = 出版価値高）」が充填速度を支配する側面も観察される。

**特筆すべきパターン：**
- **自己充填の優越**: 本ケースの充填の中核は原著者グループ自身（Murai/Chatani/Kakiuchi）の後続論文群であり、通信→Full Paper（BCSJ 1995）遷移が EP-01a/EP-04a を bundle 充填する。これは方法論-corpus の self-filling パターン（メモリ project_uqs_methodology_corpus_self_filling と整合）。
- **技術駆動充填**: EP-03a（観測困難な有機金属中間体）は分光ではなく計算化学（Morokuma grp DFT）の成熟により充填され、「実験で観測不能な explanatory quantity を理論が state-assign する」典型。
- **長期遅延/未充填の集中**: VQ-4 要件（EP-08a 反復測定, EP-09a 同一軸 benchmark）が 30 年超未充填であり、§E の VQ 階層逆転診断の対象。

**著者回顧との照合：**
Murai grp は本反応について後年 Acc. Chem. Res. 等で回顧的総説を出している（記憶に依拠、Confidence Medium）。これらの回顧で著者が「成果」として強調するのは scope の広さ・選択性・実用性（= Novelty 柱）であり、機構の不確定性（U-1 Ru(II)→Ru(0)、U-2 β-水素脱離抑制）や定量信頼性（SRG-2）を回顧で前景化した形跡は記憶上薄い。著者が回顧で認識した EP（scope = EP-07a）と認識しなかった EP（reliability = EP-08a）の差は、「分野内部者に不可視の構造的不在」の傍証となりうる（ただし回顧テキストの実確認を要する、Confidence Low）。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

EP-08a [Replication / uncertainty pack]:
* **未充填の理由**: インセンティブ構造の不整合 — 13 例の 3 重複・SD 提示は技術的に容易だが、既存反応の反復測定を独立論文として出版するインセンティブが新規性要求の出版慣行下で存在しない。BCSJ 1995 full paper で単離収率は拡充されたが、SD 付き反復データセットの体系的提示は確認できない。
* **発見的意義**: あり — 「Murai 反応という landmark でさえ、その定量信頼性（収率の再現性・誤差）は 30 年間独立に検証されていない」という記録は、分野が体系的に回避してきた問いの直接事例。VQ-4 要件が最長遅延する階層-時間単調性の証拠。
* **将来の充填可能性**: 中 — HPLC/GC 自動化により技術的には容易だが、出版インセンティブが存在しない限り独立充填は起きにくい（メタ研究・再現性プロジェクトの文脈でのみ可能性）。

EP-09a [Internal benchmark pack]:
* **未充填の理由**: インセンティブ構造の不整合 + 分野慣行 — Jordan&Taylor (1989) / Moore (1992) との同一軸 TOF 比較表は、各系の基質・温度・触媒量を補正換算すれば作成可能だが、後発反応が先行系を retrospective に matched benchmark する慣行が有機合成方法論に乏しい。総説は性能を定性的に framing するが定量比較表は提示しない。
* **発見的意義**: あり — RI-09（external superiority）が原論文で TOF 数値不在のまま主張され、後続でも数値的に閉じられないパターンは「優位性主張の数値的未閉鎖が分野慣行として温存される」事例。
* **将来の充填可能性**: 低 — 30 年超を経て先行系との matched benchmark の出版インセンティブは消失。歴史的方法論比較研究の文脈でのみ可能。

**VQ階層逆転の診断：**
本ケースは明確な VQ 階層逆転を示す。**充填済み EP は高 VQ 要件（EP-03a/RI-03 機構, EP-04a/RI-04, EP-07a/RI-07 境界）に集中**し、**未充填 EP は VQ-4 を支える低-中 VQ 要件（EP-08a/RI-08 反復測定, EP-09a/RI-09 benchmark）に集中**する。これは「科学的論理に基づく EP 充填順序（低 VQ → 高 VQ）」と「出版インセンティブに基づく実際の充填順序（新規性のある機構/scope = 高 VQ から先に充填、地味な反復測定/benchmark = 低 VQ が後回し or 永久未充填）」の逆転である。Murai 反応のように機構研究（理論計算含む）と scope 拡張が dense に進んだ landmark でさえ、定量信頼性と benchmark closure という「地味だが VQ-4 認定に必須の要件」が構造的に放置される——この逆転パターンは、分野のインセンティブ構造が UQS の構造的不在の一部（SRG-2, SRG-5）を 30 年にわたり維持していることの証拠となる。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
