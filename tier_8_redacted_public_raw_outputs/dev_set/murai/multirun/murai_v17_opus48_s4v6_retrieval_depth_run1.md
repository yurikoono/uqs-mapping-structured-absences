```
prompt_version: stage4-v6
model_info: Claude Opus 4.8 (current; note: Kumada study used Opus 4.7)
experimental_variant: "Murai cross-vendor multi-run opus48 v6 run 1"
date: 2026-06-12
```

prompt_version: stage4-v6-20260504
model_info: Claude Opus 4.8

# EP充填選定マップ

## Murai et al. 1993（Nature, communication）— Efficient catalytic addition of aromatic carbon–hydrogen bonds to olefins

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a

— **EP-03a**（Direct-observation / state-assignment pack, RI-03）：Ru(0) 活性種・シクロメタル化中間体の分光学的同定・速度論的拘束は、Murai/Chatani グループ自身が後続の機構論文・full paper で独立に追究しており、独立論文として直接ヒットしうる。
— **EP-04a**（Discrimination / replication pack, RI-04）：KIE 測定・重水素標識による M–H/M–C 挿入経路の判別は、C–H 切断律速性の検証として organometallic mechanism 論文の独立主題になりやすい。
— **EP-06a**（Analogy-validation pack, RI-06）：化学量論モデル反応によるシクロメタル化中間体の単離・分光同定は、Ru–H 系の有機金属反応として独立に発表されやすい。
— **EP-07a**（Boundary-test pack, RI-07）：キレーター（directing group）の構造的境界・金属環サイズ依存性の検証は、後続の基質スコープ拡張・directing-group 系統研究として独立論文化されやすい。

**第二群（間接的に追跡可能）：** EP-05a, EP-09a

— **EP-05a**（Quantitative-ranking substantiation pack, RI-05）：位置選択性・速度論的対熱力学的制御の定量判別は、機構 full paper や総説の一部に含まれるが、本反応そのものを対象とした独立 kinetic 論文は限定的。
— **EP-09a**（Internal benchmark pack, RI-09）：TOF の内部ベンチマーク比較は、後続 full paper・総説の一部として埋め込まれることが多く、原論文の優位性主張を直接検証する独立論文としては存在しにくい（C6 インセンティブ構造的未充填の傾向）。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a

— **EP-01a**（Reporting-coherence pack, RI-01）：GC 収率校正プロトコル・応答係数・内標準の明示は、報告形式問題（RI-01）であり、独立論文の主題ではなく Communication→Full Paper 遷移（C23）で部分自動解消される性質。本論文は Communication 形式のため C23 トリガー該当：Murai/Kakiuchi グループの full paper（Bull. Chem. Soc. Jpn. 系）で format-driven に部分解消が期待される（`auto_resolution_status: occurred`、ただし校正データの完全開示は構造的に限定的）。
— **EP-08a**（Replication / uncertainty pack, RI-08）：代表 run の3重複・SD 提示は、合成化学分野で「追試・反復測定」として独立論文化されないインセンティブ構造的未充填（C6）。技術的には可能だが出版インセンティブの不整合により第三群。

---

### §B 各EPの充填論文候補の同定

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（Secondary RI-06 Imported model）
* **充填開始点**: Kakiuchi, Murai et al., Bull. Chem. Soc. Jpn. 1995, 68, 62–83 — Murai 反応の full paper として、より広い基質スコープと機構的考察を提供し、提案触媒サイクルの検証を前進させる。
* **充填確立点**: Matsubara, Chatani, Murai et al., Organometallics 2001, 20, 2168–2173 — Ru–H 系の C–H 切断機構・関連中間体を分光学的/速度論的に追究し、シクロメタル化経路を実験的に拘束する。
* **充填の性質**: Partial — Ru(0) 活性種・中間体の直接観測は完全には達成されないが、機構の実験的拘束が前進する。
* **Bibliographic confidence**: Low
  — full paper（BCSJ 1995）と Organometallics 機構論文の存在は recall するが、正確な巻号ページは不確実で推測を含む。
* **Filling adequacy confidence**: Medium
  — 機構追究の方向性は EP-03a に対応するが、Ru(0) 直接観測という case-specific 要件の完全充足は不確実。
* **Verification recommendation**: 必須
  — トリガー (c) named reaction（Murai）+ (b) 同一グループ密ネットワーク + (d) Medium-Low confidence。
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: 原著者グループ自己充填パターン。EP-06a と相互参照（化学量論モデル反応で intermediate を同定する試みは同系統）。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: Kakiuchi, Murai et al., Bull. Chem. Soc. Jpn. 1995, 68, 62–83 — 同位体標識・KIE による C–H 切断律速性の検討を含む full paper（部分的）。
* **充填確立点**: 未同定 — Murai 反応の KIE/重水素標識による M–H vs M–C 挿入経路の決定的判別を主題とする独立論文を確信を持って特定できない。後続の機構研究（Chatani グループ）に部分的に含まれる可能性が高い。
* **充填の性質**: Partial
* **Bibliographic confidence**: Low
  — full paper の存在は recall するが KIE 実験の具体的所在は不確実。
* **Filling adequacy confidence**: Low
  — M–H/M–C 経路判別という case-specific 要件への直接対応は不明確。
* **Verification recommendation**: 必須
  — トリガー (c) named reaction + (d) Low confidence。
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: EP-03a と同一 full paper（BCSJ 1995）が部分充填源となる可能性（バンドル充填）。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 Qualitative overread（Secondary RI-04）
* **充填開始点**: Kakiuchi & Murai, Acc. Chem. Res. / Top. Curr. Chem. 系総説（2000年代前半）— 位置選択性・基質依存性を体系化（レビューのため新規データは限定）。
* **充填確立点**: 未同定 — 本反応の ortho 選択性について速度論的対熱力学的制御を定量判別する独立論文を確信を持って特定できない。
* **充填の性質**: Indirect / Partial
* **Bibliographic confidence**: Low
  — Kakiuchi & Murai の総説は実在を recall するが（Chem. Rev. 系含む）、具体的書誌は推測。
* **Filling adequacy confidence**: Low
  — 総説はデータ体系化であり EP 充填の例外（独自定量再評価）に該当するか不明確。
* **Verification recommendation**: 必須
  — トリガー (c) named reaction + (d) Low confidence。
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: レビューは原則 EP を充填しない（二次情報源）。本エントリは充填候補としては弱く、§C 選定には含めない。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Matsubara, Chatani, Murai et al., Organometallics 2001, 20, 2168–2173 — 化学量論的 Ru 系の反応で関連中間体・経路を実験的に検討。
* **充填確立点**: 同上（部分）
* **充填の性質**: Partial — 類似系での中間体検証であり、本反応活性種そのものの単離には至らない可能性。
* **Bibliographic confidence**: Low
  — Organometallics 機構論文の存在は recall するが正確な巻号ページは不確実。
* **Filling adequacy confidence**: Low
  — シクロメタル化中間体の分光同定という case-specific 要件への直接対応は不確実。
* **Verification recommendation**: 必須
  — トリガー (c) named reaction + (b) 密ネットワーク + (d) Low confidence。
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: EP-03a と同一論文が両 EP を部分充填する可能性（バンドル充填、相互参照）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Kakiuchi, Murai et al., Bull. Chem. Soc. Jpn. 1995, 68, 62–83 — 基質スコープ拡張により directing group（カルボニル等）の構造的境界を経験的に画定。
* **充填確立点**: Kakiuchi & Chatani, Adv. Synth. Catal. 2003, 345, 1077–1101（総説的だが scope 体系化）/ あるいは Kakiuchi, Kochi et al. による imine/ketone directing group 系統研究（2000年代）— キレーター変換による境界条件を拡張的に検証。
* **充填の性質**: Partial / Indirect
* **Bibliographic confidence**: Low
  — Kakiuchi & Chatani の総説・scope 拡張論文の存在は recall するが具体的書誌は推測。
* **Filling adequacy confidence**: Medium
  — directing-group 境界の経験的画定は EP-07a の方向に直接対応。
* **Verification recommendation**: 必須
  — トリガー (c) named reaction + (b) 密ネットワーク。
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: CLA-1（キレーション支援の構造的境界）に直接対応。Novelty-3（汎用性）スコープ境界の充填。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: 未同定 — 代表 run の3重複・SD 提示を主題とする独立論文は存在しない。
* **充填確立点**: 未同定
* **充填の性質**: 未充填（インセンティブ構造的未充填、C6）
* **Bibliographic confidence**: n/a
* **Filling adequacy confidence**: n/a
* **Verification recommendation**: 省略可
* **Bibliographic verification status**: n/a
* **Filling timescale category**: non-applicable
```yaml
incentive_structure_type: "incentive-misaligned (C6)"
filling_substitute: [REDACTED: substantial verbatim quotation; see Tier 9]
```
* **注記**: 合成化学分野では追試・反復測定が新規性要件のもとで独立論文化されない典型。第三群。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 External superiority（Secondary RI-08）
* **充填開始点**: Kakiuchi, Murai et al., Bull. Chem. Soc. Jpn. 1995, 68, 62–83 — full paper で TOF・反応条件を詳細化し内部ベンチマークを部分提供。
* **充填確立点**: 未同定 — Jordan & Taylor / Moore 系との同一軸 TOF 比較表を提示する独立論文を確信を持って特定できない。
* **充填の性質**: Partial（インセンティブ構造的未充填傾向、C6）
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 必須
  — トリガー (c) named reaction + (d) Low confidence。
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (variable)
* **注記**: SRG-5 は SRG-2 解消なしには部分解消に留まる。EP-08a と依存関係。

---

**§B 末尾チェック：Bibliographic verification（conditional triggering）**

本ケースは Murai named reaction（トリガー c）+ 同一グループ密ネットワーク（トリガー b：Murai/Kakiuchi/Chatani グループから多数の関連論文）+ Low confidence 候補多数（トリガー d）に該当するため、**全候補に [必須] verification** を付与。全候補 `Bibliographic verification status: pending`。

**Hallucination 自己警告（本 run 固有）**：本 run では具体的巻号ページ（BCSJ 1995, 68, 62–83 / Organometallics 2001, 20, 2168–2173 / Adv. Synth. Catal. 2003, 345, 1077–1101）を記載したが、これらは training からの recall に基づく推定であり、正確な巻号ページの confidence は Low。著者組合せ・年代の大枠（Kakiuchi/Murai/Chatani by BCSJ full paper 1990年代後半、Chatani 機構論文 Organometallics 2000年代前半）は Medium だが、ページ番号は捏造リスクを認識して Low と明示する。架空の coauthor は追加していない。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Kakiuchi, Murai et al., Bull. Chem. Soc. Jpn. 1995, 68, 62–83 | EP-03a, EP-04a, EP-07a, EP-09a | VQ-2/VQ-3 | 1995 | Low | Medium | ⚠️ pending（必須） |
| 2 | Matsubara, Chatani, Murai et al., Organometallics 2001, 20, 2168–2173 | EP-03a, EP-06a | VQ-3 | 2001 | Low | Low | ⚠️ pending（必須） |
| 3 | Kakiuchi & Chatani, Adv. Synth. Catal. 2003, 345, 1077–1101 | EP-07a | VQ-2 | 2003 | Low | Medium | ⚠️ pending（必須） |

**選定理由：**

本ケースは hallucination-measurement study の制約下にあり、Murai 反応の後続文献を正確な書誌で recall できる confidence が全般的に Low である。確信を持って実在を主張できる充填論文は、(1) Murai/Kakiuchi グループの **BCSJ full paper**（Communication→Full Paper 自動解消 C23 の核心、複数 EP をバンドル充填する効率性から第1位）、(2) Chatani グループの **Organometallics 機構論文**（中間体・経路の実験的拘束）、(3) Kakiuchi & Chatani の **scope 拡張/総説**（directing-group 境界）の3報に絞る。いずれも正確な巻号ページの confidence は Low のため、全エントリを「⚠️ pending verification」とし、post-hoc Crossref 検証を経るまで final selection としない。

VQ 階層カバレッジ：BCSJ 1995（VQ-2 報告整合 + VQ-3 機構の部分）、Organometallics 2001（VQ-3 機構）、Adv. Synth. Catal. 2003（VQ-2 境界）。VQ-4 ベンチマーク要件（EP-09a）の決定的充填論文は同定できず、§E で未充填として扱う。

バンドル充填：BCSJ 1995 full paper は EP-03a/04a/07a/09a を部分的にまとめて充填する候補であり、Communication の報告形式問題（EP-01a）も format-driven に部分解消する効率性をもつ。ただし全て Low bib.conf のため verification 必須。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件: EP-01a → ~1995（Kakiuchi/Murai BCSJ full paper）自己充填 / format-driven auto-resolution（C23, occurred 推定、bib.conf Low）
- VQ-2 要件: EP-07a → 1995–2003（Kakiuchi/Chatani scope 拡張）自己充填 / 分野横断充填
- VQ-3 要件: EP-03a → 1995–2001（BCSJ + Organometallics）自己充填 / 技術駆動充填（部分）
- VQ-3 要件: EP-06a → ~2001（Chatani Organometallics）自己充填（部分）
- VQ-3 要件: EP-04a → 部分のみ（KIE 決定的論文は未同定）
- VQ-4 要件: EP-09a → 未充填（インセンティブ構造的未充填傾向）
- VQ-2 要件: EP-08a → 未充填（C6 インセンティブ構造的未充填）

**階層-時間対応の評価：**
「VQ 階層が上がるほど充填に時間がかかる」仮説は本ケースでは弱い支持に留まる。VQ-2 報告整合（EP-01a）は full paper 遷移で比較的早期（~2年）に部分解消される一方、VQ-3 機構要件（EP-03a/04a/06a）は2001年頃まで（~8年）かかり部分充填止まり、VQ-4 ベンチマーク（EP-09a）と VQ-2 反復（EP-08a）はインセンティブ構造により未充填のまま残る。すなわち「科学的論理上の充填順序（低 VQ→高 VQ）」と「出版インセンティブ上の実際の充填順序」が逆転し、最も低次の RI-01/RI-08（報告形式・反復）が高次の機構要件より遅く（または永久に）充填されないパターンを示す。

**特筆すべきパターン：**
- **自己充填の優越**：充填候補の大半が原著者グループ（Murai/Kakiuchi/Chatani）自身の後続論文であり、named-reaction 系の典型パターン。
- **VQ 階層逆転**：EP-08a/EP-09a（低 VQ 報告・反復・ベンチマーク要件）が未充填で残り、機構系 EP-03a/06a が部分充填されるという逆転。出版インセンティブが UQS の構造的不在の一部を維持している証拠。
- **bib.conf 全般 Low**：本 run では充填論文の具体的書誌を確信を持って recall できず、全候補が verification 待機。これ自体が hallucination-measurement の観測点。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

EP-08a [Replication / uncertainty pack]:
* **未充填の理由**: インセンティブ構造の不整合（C6）— 代表 run の3重複・SD 提示は技術的に容易だが、新規性を要求する合成化学の出版慣行のもとで独立論文化されない。
* **発見的意義**: あり — 「分野が30年以上にわたり反復測定・不確かさ報告を独立検証対象としてこなかった」構造的不在の記録。
* **将来の充填可能性**: 低 — 現代でも追試の独立出版インセンティブは存在しない。

EP-09a [Internal benchmark pack]:
* **未充填の理由**: インセンティブ構造の不整合（C6）+ RI-08 依存 — Jordan & Taylor / Moore 系との同一軸 TOF 比較表は、原論文の優位性主張を直接検証する独立論文として出版されにくい。SRG-2 解消なしには意味が確定しない依存関係。
* **発見的意義**: あり — 「最高水準 TOF」という比較優位性主張が30年以上数値的に閉じられないまま残る、分野の benchmark 文化の構造的不在。
* **将来の充填可能性**: 低 — named reaction が確立した現在、原論文の TOF 優位性を遡及検証する動機は失われている（成功による問いの抹消に近い）。

EP-04a [Discrimination / replication pack]（部分未充填）:
* **未充填の理由**: 部分的には機構 full paper に含まれるが、M–H vs M–C 挿入経路を決定的に判別する独立論文を確信を持って同定できない（本 run の recall 制約も含む）。
* **発見的意義**: あり（条件付き）— 2経路並置のまま判定保留された機構的曖昧性が、後続でどこまで決定的に解消されたかは verification を要する。
* **将来の充填可能性**: 中 — 現代の同位体標識・computational mechanism 研究で充填可能。

**VQ階層逆転の診断**：未充填 EP（EP-08a, EP-09a）が低 VQ 要件（RI-08, RI-09）に集中し、部分充填済み EP（EP-03a, EP-06a, EP-07a）が高 VQ 要件（RI-03, RI-06, RI-07）に偏るパターンが観察される。これは「科学的論理に基づく EP 充填順序（低 VQ→高 VQ）」と「出版インセンティブに基づく実際の充填順序（高 VQ→低 VQ）」の逆転であり、分野のインセンティブ構造が UQS の構造的不在の一部を維持している証拠として記録できる。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
