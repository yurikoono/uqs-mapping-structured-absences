```
prompt_version: stage4-v2
model_info: Claude Opus 4.8 (current; note: Kumada study used Opus 4.7)
experimental_variant: "Murai cross-vendor multi-run opus48 v2 run 1"
date: 2026-06-12
```

# EP充填選定マップ

## Murai et al. 1993（Nature 366, 529–531, communication）

EP対象（Stage 3 §2/§5）: EP-01a, EP-03a, EP-04a, EP-05a, EP-06a, EP-07a, EP-08a, EP-09a

**ハルシネーション抑制方針（本run）**: 充填論文候補は訓練データから実在を想起できるもののみ記載する。確信が低い場合は bib_conf="Low" とし、それでも測定対象として記載する。引用文字列は想起のまま（巻号・頁の細部は誤りうる）。Murai系（Murai, Chatani, Kakiuchi, Sonoda, Fukuyama）および Ru/directed C–H 触媒分野（Trost, Genet, Darses, Glorius, Ackermann 等）を中心に逆算検索。

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a
— **EP-03a**（Direct-observation / state-assignment）: Ru活性種・cyclometallated中間体の分光学的/速度論的拘束は、Murai/Chatani自身および後続の機構研究（Ru cluster活性種、KIE、in-situ NMR）が独立論文の主題として存在しうる。RI-03/RI-06は機構研究として発表されやすい。
— **EP-04a**（Discrimination / replication）: M–H対M–C挿入経路の判別・KIE測定は、重水素標識を用いた独立した機構論文として典型的に存在する（C–H切断律速判定）。
— **EP-06a**（Analogy-validation）: 化学量論モデル反応によるcyclometallated中間体の単離・同定は有機金属化学の標準的研究形式であり、Ru–aryl中間体の構造研究として独立に存在しうる。
— **EP-07a**（Boundary-test）: directing group / tether長境界（5員 vs 6員金属環）・基質スコープ拡張は、Murai系のフルペーパー群・directing group系統研究として豊富に存在する。

**第二群（間接的に追跡可能）：** EP-05a, EP-09a
— **EP-05a**（Quantitative-ranking substantiation）: 位置選択性の速度論的/熱力学的制御判別は、機構フルペーパーやレビューに部分的に含まれるが、本系そのものでの独立した定量選択性論文は限定的。
— **EP-09a**（Internal benchmark）: TOF/対外比較数値の閉鎖は、レビュー・総説や方法論比較に含まれやすく、独立論文の主題にはなりにくい。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a
— **EP-01a**（Reporting-coherence）: GC校正・応答係数・マスバランスの明示はRI-01起因の報告形式問題であり、communication→フルペーパー遷移で部分解消されるが、独立論文の主題として発表される性質ではない。
— **EP-08a**（Replication / uncertainty）: 反復測定・SD提示はRI-08起因の反復測定慣行であり、新規性を要求する出版慣行のもとで独立論文化されにくい（インセンティブ構造不整合）。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 Reporting integrity（+ RI-08 Unquantified reliability）
* **充填開始点**: Murai系 Bull. Chem. Soc. Jpn. フルペーパー（Kakiuchi & Murai, 1990s後半）— communicationの後続フルペーパーで単離収率・反応条件の詳細が拡充された可能性。— *bib_conf: Low*（特定フルペーパーの巻号・収率報告様式を確実には想起できない）
* **充填確立点**: 未同定 — GC校正プロトコル/応答係数の明示それ自体を主題とする独立論文は構造的に存在しにくい。
* **充填の性質**: Partial（フルペーパー遷移で報告精度は上がるが、校正手順の明示という要件そのものは慣行的に充填されない）
* **Confidence**: Low
* **注記**: RI-01はVQ-2の致命的未解消項。報告形式問題は独立充填の対象になりにくく第三群。§Eで詳述。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（+ RI-06 Imported model）
* **充填開始点**: Kakiuchi, F. et al.（KIE / 重水素標識による機構研究、Murai系、1990s後半–2000s）— ortho C–H/C–D基質を用いたKIE測定でC–H切断ステップを拘束。— *bib_conf: Medium*（Murai/Kakiuchi系がこの種のKIE機構研究を行ったことは確信があるが、特定論文の書誌詳細は不確実）
* **充填確立点**: 後続のRu活性種同定研究（in-situ NMR / Ru(0)–phosphine種の関与確認）— *bib_conf: Low*（特定論文を確実には想起できない）
* **充填の性質**: Partial
* **Confidence**: Medium（開始点） / Low（確立点）
* **注記**: 活性種がRu(0)かどうか（U-1）の解消は、後年 Ru3(CO)12 や RuH2(CO)(PPh3)3 の活性化機構研究へ展開。EP-06aと相互参照（化学量論モデル反応）。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: Murai系 KIE / 同位体標識機構論文 — ortho-d標識アセトフェノンによるC–H活性化律速の判定、およびオレフィン挿入経路（M–H vs M–C）の標識実験。— *bib_conf: Low–Medium*（この種の標識実験がMurai系で行われた蓋然性は高いが特定論文は不確実）
* **充填確立点**: 同上
* **充填の性質**: Partial
* **Confidence**: Low
* **注記**: EP-03aとバンドル充填の可能性（同一機構論文がKIE+中間体観測を同時に扱う）。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 Qualitative overread（+ RI-04）
* **充填開始点**: 位置選択性の温度依存性/競合実験を扱う機構フルペーパー — 速度論的対熱力学的制御の判別。— *bib_conf: Low*（本系そのものでの定量選択性論文を特定想起できない）
* **充填確立点**: 未同定
* **充填の性質**: Indirect（類似 directed C–H系での選択性定量はあるが本系での独立充填は限定的）
* **Confidence**: Low
* **注記**: 選択性の構造的帰因（環歪み・立体閉塞）は後年の計算化学（DFT機構研究）で部分的に裏付けられた可能性があるが、特定論文を確実には想起できない。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model（+ RI-03）
* **充填開始点**: 化学量論的cyclometallation研究（acetophenone + Ru前駆体によるRu–aryl/cyclometallated中間体の単離・同定）— Murai系または有機金属グループによる中間体構造研究。— *bib_conf: Low*（cyclometallated Ru中間体の構造研究は分野に存在するが、本系に直結する特定論文を確実には想起できない）
* **充填確立点**: 未同定
* **充填の性質**: Indirect
* **Confidence**: Low
* **注記**: 原論文がref 14（Knobler/Kaesz, CH3Mn(CO)5）・ref 15（Pignolet, Ru–acetate）を輸入モデルとして引用しており、これらの本系での検証が充填に相当する。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Kakiuchi, F. & Murai, S. — directing group / 基質スコープ拡張のフルペーパー群（aromatic ketones以外のdirecting group: imines, esters, nitriles等への拡張、tether長境界の探索）。— *bib_conf: Medium*（Murai/Kakiuchiがdirected C–H functionalizationのスコープ拡張を多数発表したことは確信があるが、境界実験を主題とする特定論文の書誌は不確実）
* **充填確立点**: Kakiuchi & Murai のレビュー的フルペーパー / Acc. Chem. Res.（後述）でスコープ境界が体系化された。
* **充填の性質**: Partial–Complete（スコープ境界は後続研究で広範に確定）
* **Confidence**: Medium
* **注記**: CLA-1/CLA-2（D-4候補7/8）に対応。directing group dependenceは後年のRu directed C–H分野全体（Ackermann, Glorius等）で確立。EP-09aと年代多様性を補完。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: 未同定 — 反復測定・SD提示それ自体を主題とする独立論文は構造的に存在しない。
* **充填確立点**: 未同定
* **充填の性質**: 未充填（インセンティブ構造不整合）
* **Confidence**: —（候補なし）
* **注記**: §Eで詳述。EP-01aと同根（SRG-2）の報告形式問題。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 External superiority（+ RI-08）
* **充填開始点**: Ritleng, Sirlin & Pfeffer, Chem. Rev. 2002（[REDACTED: substantial verbatim quotation; see Tier 9]）— directed C–H functionalization触媒のTOF/性能を横断的に整理。— *bib_conf: Medium*（このレビューの存在は確信があるが、Murai系のTOFを数値比較軸に乗せたかは不確実 ; レビューは原則として充填しない点に注意）
* **充填確立点**: 未同定（独立した数値比較論文としては成立しにくい）
* **充填の性質**: Indirect（レビューによる体系化であり、新規実験データの提供ではない — 原則として非充填）
* **Confidence**: Low
* **注記**: レビューはEPを充填しないという規律に従い、二次情報源として記載。本系のTOF対外比較の数値的閉鎖は独立論文化されにくく第二群。

---

**自己充填（著者グループ後続）に関する横断注記:**

Murai/Kakiuchi/Chatani グループは本communicationの後、Ru触媒directed C–H functionalizationを体系的に展開し、機構（KIE）・スコープ（directing group多様化）・選択性を後続論文群で扱った。総説として **Kakiuchi, F. & Murai, S., Acc. Chem. Res.（2000年前後、"Catalytic C–H/Olefin Coupling"）** を想起する（*bib_conf: Medium*、書誌詳細不確実）。これはEP-03a/04a/07aの充填を特定するための二次情報源として有用だが、レビュー自体は充填論文ではない。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Kakiuchi, F. et al.（Murai系 KIE/同位体標識機構論文, 1990s後半–2000s） | EP-03a, EP-04a | VQ-3 | ~1995–2002 | Low–Med |
| 2 | Kakiuchi, F. & Murai, S.（directing group / スコープ拡張フルペーパー） | EP-07a | VQ-2/VQ-3境界 | ~1996–2005 | Med |
| 3 | Kakiuchi, F. & Murai, S., Acc. Chem. Res.（C–H/olefin coupling 総説, 二次情報源） | EP-03a, EP-07a（特定用） | VQ-3 | ~2000 | Med |
| 4 | Ritleng, V., Sirlin, C. & Pfeffer, M., Chem. Rev. 102, 1731 (2002)（二次情報源） | EP-09a（特定用） | VQ-4 | 2002 | Med |

選定理由（1–2段落）:

本選定リストは confidence=Low の候補を原則除外する規律のもとで、Medium以上で想起できる候補に絞った結果、特定の単一充填論文を High で固定できなかった。これは本runの正直な状態であり、Murai系の後続機構・スコープ研究が「存在することは確信できるが特定書誌を確実に想起できない」ことを反映する。順序1–2は著者グループ自己充填（EP-03a/04a/07a）を核とし、VQ-3要件（機構）とVQ-2/VQ-3境界（スコープ境界）を階段状にカバーする。順序3–4はレビュー/総説であり**充填論文ではなく二次情報源**として、EP-03a/07a/09aの実際の充填論文を特定するための参照として掲げた（Stage 4規律: レビューは充填しない）。

バンドル充填: 順序1（KIE+中間体標識機構論文）はEP-03aとEP-04aを同時にカバーしうる効率的候補である（C–H切断律速判定と挿入経路判別は同一機構研究で扱われる）。順序2はEP-07a（境界）を単独でカバーし、CLA-1/CLA-2に直結する。VQ-4要件（EP-09a, 対外TOF比較）はレビューによる体系化に依存し、独立充填としては未閉鎖のまま残る。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件: EP-01a → 未同定（フルペーパー遷移で部分解消、報告形式問題）
- VQ-2 要件: EP-07a → ~1996–2005 Kakiuchi & Murai 自己充填（スコープ境界）
- VQ-3 要件: EP-03a → ~1995–2002 Kakiuchi et al. 技術駆動充填（KIE/in-situ分光）[Low–Med]
- VQ-3 要件: EP-04a → ~1995–2002 同上 自己充填（同位体標識判別）[Low]
- VQ-3 要件: EP-05a → 未同定（選択性の定量的制御判別、本系での独立充填限定的）
- VQ-3 要件: EP-06a → 未同定（化学量論モデル中間体の本系検証）[Low]
- VQ-4 要件: EP-09a → 2002頃 レビューによる体系化（充填でなく二次情報源）
- VQ-4 要件: EP-08a → 未充填（反復測定のインセンティブ構造不整合）

**階層-時間対応の評価：**

本runで想起できた範囲では「VQ階層が上がるほど充填に時間を要する」仮説を強く支持も反証もできない。むしろ顕著なのは**VQ階層逆転の兆候**である: 機構（VQ-3, RI-03/04, 高VQ）に対応するEP-03a/04a/07aは著者グループの自己充填として比較的早期（1990s後半–2000s）に前進した一方、報告形式（VQ-2, RI-01, 低VQ）に対応するEP-01a/08aは独立論文として充填されないまま残る。これは「科学的論理上の充填順序（低VQ→高VQ）」と「出版インセンティブ上の実際の充填順序（機構の新規性が論文化されやすい高VQ→低VQ）」の逆転として記録できる。

**特筆すべきパターン：**
- **自己充填の優位**: EP-03a/04a/07aは Murai/Kakiuchi グループ自身の後続研究で前進する典型的な「communication→体系的研究プログラム」パターン。本ケースは原著者が後年 Acc. Chem. Res. 総説で「KIE」「directing group依存」「スコープ」を回顧的に整理しており、Stage 3のEPリスト（機構・境界）と概ね一致する。一方、報告形式（RI-01/RI-08）に対応するEPは回顧で言及されず、「分野内部者には不可視の構造的不在」の候補となる。
- **未閉鎖のVQ-4**: 対外TOF比較（EP-09a）は分野全体のレビューで体系化されるが、本系単独の数値比較論文としては未充填。
- 本runの書誌確信度は全般にLow–Mediumであり、High固定の充填論文を提示できない正直な状態として記録する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

EP-01a [Reporting-coherence pack]:
* **未充填の理由**: 報告形式問題（RI-01）+ インセンティブ構造不整合。GC校正プロトコル・応答係数・マスバランスの明示は技術的には容易だが、それ自体を主題とする独立論文を出版するインセンティブが存在しない。communication→フルペーパー遷移で部分解消されうるが、校正手順の明示という要件そのものは慣行的に充填されない。
* **発見的意義**: あり。「分野が新規化合物のGC収率を校正なしで報告する慣行を体系的に維持してきた」ことの記録になる。
* **将来の充填可能性**: 中（現代のSI必須化により新規論文では自動的に満たされるが、1993年原論文への遡及的充填は行われない）。

EP-08a [Replication / uncertainty pack]:
* **未充填の理由**: 反復測定慣行（RI-08）+ インセンティブ構造不整合。代表例の3重複・SD提示は技術的に可能だが、既存系の反復測定を独立論文として出版するインセンティブがない。新規性要求の出版慣行下で論文化されにくい典型。
* **発見的意義**: あり。EP-01aと同根（SRG-2）で、「定量的信頼性の独立検証」が分野で構造的に回避されてきたことを示す。
* **将来の充填可能性**: 低（独立論文化のインセンティブが原理的に欠如）。

EP-05a [Quantitative-ranking substantiation pack]（部分未充填）:
* **未充填の理由**: 関心の欠如 + 技術的困難。位置選択性の速度論的/熱力学的制御の判別は本系そのものでは独立論文化されにくく、後年の計算化学（DFT）で間接的に扱われた可能性はあるが本runでは特定論文を想起できない。
* **発見的意義**: あり（選択性の起源が「構造的直観」のまま広く受容され続けた可能性）。
* **将来の充填可能性**: 中（現代の計算機構研究で充填可能）。

EP-06a [Analogy-validation pack]（部分未充填）:
* **未充填の理由**: 輸入モデル（ref 14/15）の本系での検証は化学量論モデル反応として可能だが、本runでは特定の充填論文を確実に想起できない。
* **発見的意義**: あり（cyclometallated中間体の輸入アナロジーが検証なしに機構の根拠として機能し続けた可能性）。
* **将来の充填可能性**: 中–高（現代の有機金属/分光技術で充填可能）。

**VQ階層逆転の診断**: 本ケースは未充填EPが低VQ要件（EP-01a/RI-01, EP-08a/RI-08）に集中し、前進したEPが高VQ要件（EP-03a/RI-03, EP-04a/RI-04, EP-07a/RI-07）に集中するパターンを示す。これは出版インセンティブ構造（機構の新規性は論文化されやすく、報告形式の修繕は論文化されにくい）がUQSの構造的不在の一部を維持していることの証拠となる。ただし本runの充填論文同定が全般に Low–Medium confidence である点を併記し、この診断は書誌的に確証された充填ではなく構造的傾向の推定であることを明記する。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
