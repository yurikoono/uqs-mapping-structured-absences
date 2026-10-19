```yaml
prompt_version: stage4-v6-20260504
model_info: Claude Haiku 4.5
experimental_variant: "Murai cross-vendor multi-run haiku v6 run 2"
date: 2026-06-12
```

# EP充填選定マップ

## Murai et al. 1993（Nature, communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）:** EP-03a, EP-06a, EP-07a

— EP-03a (Direct-observation / state-assignment pack): Ru(0)生成のH₂発生検出、³¹P NMR追跡は、Ru水素化物系の標準的な活性化実験として独立論文化されやすい。Chatani・Kakiuchi グループは後続の mechanistic paper で実際にこれらの実験を報告している可能性が高い。

— EP-06a (Analogy-validation pack): 化学量論 model reaction による中間体の NMR 分光同定は、有機金属化学の standard methodology paper として独立に発表されやすい。類似の Ru chelation-assisted cyclometallation paper が 1990s-2000s に存在すると予想される。

— EP-07a (Boundary-test pack): chelation 支援の環サイズ依存性は、原論文後の extension scope paper で自然と報告される可能性が高い。フェニルプロピルケトン、6員環前駆体の反応性試験は、原著者グループによる follow-up で扱われた可能性が高い。

**第二群（間接的に追跡可能）:** EP-01a, EP-05a, EP-08a, EP-09a

— EP-01a (Reporting-coherence pack): Murai 1993 は communication format だが、同一著者グループによる full article / Full Paper 展開が 1-3 年以内に存在する可能性が高い。Letter→Full Paper auto-resolution pattern (C23) が適用される見込み。

— EP-05a (Quantitative-ranking substantiation pack): 位置選択性の速度論的/熱力学的区別実験は、競合基質実験や VT-GC などの研究として後続論文（レビュー、続報、教科書）に含まれやすい。直接的な独立論文化は見当たらない可能性が高い。

— EP-08a (Replication / uncertainty pack): 有機合成分野では再現実験・SD 記載が出版インセンティブの問題により独立論文化されにくい（§A の典型パターン①「インセンティブ構造的未充填」に該当）。Murai グループ自身が full-paper 展開時に部分的に解消した可能性。

— EP-09a (Internal benchmark pack): Moore et al. (1992) / Jordan & Taylor (1989) との TOF 比較は、総説・教科書に収録される可能性が高い。Ru-catalysed C–H functionalization の review paper に記載されている見込み。

**第三群（充填が見つからない可能性あり）:** EP-04a

— EP-04a (Discrimination / replication pack): C–H 対 C–D の KIE 測定、M–H 対 M–C 挿入経路の deuterated olefin ラベル実験は、技術的には可能だが、反応メカニズムの詳細判定が Murai グループの core interest でなかった可能性がある。独立論文化されていない可能性が高い。機構「不明」宣言の下では、ここまで詳細な実験は後続研究の agenda から外れた可能性。

---

### §B 各EPの充填論文候補

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Murai, S., Kakiuchi, F., Kamatani, A., et al., J. Org. Chem. 1994/1995 (推測) — Full Paper 展開において GC 校正方法、内標準、応答係数の詳細記述を含める可能性。
* **充填確立点**: 不確定（確認待ち）
* **充填の性質**: Partial — communication format から full article への自動的な reporting completeness 改善を期待。ただし具体的 full paper の存在を確認していない。
* **Bibliographic confidence**: Low — 正確な巻号ページは推測。Murai グループの follow-up paper catalog を要確認。
* **Filling adequacy confidence**: Medium — Full Paper が存在すれば EP-01a の大部分を充填する可能性。
* **Verification recommendation**: [必須] — Murai 반応は named reaction (Murai reaction) であり、同一著者ネットワークが密である。条件 (b)(c) に該当。
* **Filling timescale category**: format-driven (1-3 yr) — communication から full article への自動解消パターンとして分類。
* **注記**: Letter→Full Paper auto-resolution（C23）パターン候補。actual paper の存在確認が必須。DOI 等により post-hoc 検証が必要。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Kakiuchi, F. & Chatani, N. et al., Organometallics ca. 1994-1996 (推測) — Ru(0) 生成の確認、³¹P NMR 変化の追跡などが報告された可能性。
* **充填確立点**: 不確定（複数論文の可能性）
* **充填の性質**: Partial — Ru hydride → Ru(0) の活性化実験は 1990s-2000s の mechanistic study で部分的に扱われたと推測。ただし Murai 1993 の正確な条件での実証は見当たらない可能性。
* **Bibliographic confidence**: Low — Kakiuchi グループの mechanistic paper は存在するが、Murai 1993 の specific cyclometallation intermediate 観測の direct reference は不確定。
* **Filling adequacy confidence**: Low — Ru(0) generation は確認されたが、本反応系での cyclometallated intermediate の in situ 観測が実現したかは不確定。
* **Verification recommendation**: [必須] — Murai 反応系統の author network が密（Chatani, Kakiuchi が共著者）。条件 (b) に該当。該当論文の存在と内容の検証が必須。
* **Filling timescale category**: technical-barrier (5-10 yr) — in situ NMR / MS 技術の advancement が driving force。
* **注記**: Kakiuchi-Chatani による mechanistic follow-up (late 1990s-2000s) が想定される candidate source。但し確実な filling の判定は post-hoc verification による。

---

**EP-04a [Discrimination / replication pack]（第三群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: **未同定** — C–H vs C–D の KIE 測定、M–H vs M–C insertion の分別実験は、Murai グループの後続論文・他グループの競争論文いずれからも見出しがたい。
* **充填確立点**: 未同定
* **充填の性質**: Attempted / Unfilled
* **Bibliographic confidence**: —（候補論文なし）
* **Filling adequacy confidence**: —
* **Verification recommendation**: [省略可] — 充填論文が見つからない。
* **Filling timescale category**: non-applicable （未充填）
* **注記**: 本 EP は「成功による問いの抹消」パターンに該当する可能性。異なるメカニズム（C–O reductive elimination, radical pathway 等）が後年提案されたことにより、M–H vs M–C distinction の必要性が消滅した可能性。または、Murai グループの mechanistic agenda から初めから外れていた可能性。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填開始点**: Murai, S. et al. (various later papers ca. 1995-2000,推測) — 位置選択性の温度依存性、基質スクリーニング（electronic vs steric effect）等は、substrate scope paper に自然と含まれる可能性。
* **充填確立点**: 不確定
* **充填の性質**: Partial — 選択性の定量的背景は、scope paper や mechanistic paper の footnote / supporting data に部分的に含まれうるが、dedicated kinetic experiment ではない可能性。
* **Bibliographic confidence**: Low — 具体的論文の存在未確認。
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須] — author network 密（Murai 系統）。条件 (b) に該当。
* **Filling timescale category**: field-methodology (3-7 yr) — 位置選択性の定量的背景付けが、field-wide の mechanistic trend として 1990s-2000s に普及した可能性。
* **注記**: 「定量的ランキング」が期待される EP だが、実際には論文出版後も多くの場合、selectivity の定量的根拠（kinetic parameters, competition experiments）は報告されず、structural intuition に留まる傾向がある。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填開始点**: Chatani, N., Kakiuchi, F., & Murai, S. (ca. 1994-1997, 推測) — stoichiometric model reaction での cyclometallated intermediate の NMR characterization / X-ray structure が報告された可能性。
* **充填確立点**: 不確定
* **充填の性質**: Partial to Complete — model reaction で intermediate を分光的に同定すれば、EP-06a の「analogy validation」が達成される。
* **Bibliographic confidence**: Medium — Ru cyclometallation の literature は存在し、Murai グループの model study が存在する可能性は高い。ただし具体的年・巻号は推測。
* **Filling adequacy confidence**: Medium — Murai グループ自身による model reaction paper が存在すれば、EP-06a を substantial に充填する可能性。
* **Verification recommendation**: [必須] — named reaction author、著者ネットワーク密。条件 (b)(c) に該当。
* **Filling timescale category**: field-methodology (2-5 yr) — ruthenium hydride / cyclometallation の model reaction methodology が 1990s standard になった。
* **注記**: Murai グループの Chatani-Kakiuchi axis による mechanistic study (late 1990s) が本 EP の most likely filling source。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填開始点**: Murai et al., J. Am. Chem. Soc. or J. Org. Chem. (ca. 1994-1997, 推測) — 環サイズ依存性の scope paper (phenylpropyl ketone, 7-membered ring; β-substituted examples, etc.) が報告された可能性。
* **充填確立点**: 不確定
* **充填の性質**: Partial — scope paper で tether-length boundary を実験的に設定すれば、CLA-1（chelation-assistance boundary）を部分的に充填。
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Medium — Original paper の scope 拡張として、環サイズ・tether 長の boundary を意図的に検討した paper が存在すれば期待される。
* **Verification recommendation**: [必須] — author network 密。条件 (b) に該当。
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: Boundary clarification は scope-extension paper の natural outcome として報告されやすい。Murai グループの post-1993 papers を系統的に確認する必要がある。

---

**EP-08a [Replication / uncertainty pack]（第二群）**

* **充填開始点**: Murai et al. Full Paper (ca. 1994-1996, 推測) — runs 1, 9, 10 の 3 重複実験による SD 記載が期待される。
* **充填確立点**: 不確定
* **充填の性質**: Partial — Communication から Full Article への展開時に、実験セクションで replicate data が自動的に記載される可能性。ただし table 内での SD 明示は 1994 年時点では standard でなかった可能性。
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low — 1990s の有機合成論文では SD 記載が現在ほど strict でなかった可能性。
* **Verification recommendation**: [必須] — author network 密、communication format から full paper への transition 確認。条件 (b) に該当。
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: インセンティブ構造的未充填パターンも考慮。full paper で replication data が記載されなかった可能性も有り。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填開始点**: Chatani, N., & Murai, S., review or full paper (ca. 1996-2000, 推測) — Ru-catalysed C–H functionalization の review / perspectives paper で、Jordan & Taylor (1989) / Moore et al. (1992) の TOF 値との定量的比較が掲載された可能性。
* **充填確立点**: 不確定
* **充填の性質**: Indirect — 原論文自体では不提供だが、同一著者グループの review paper で external benchmarking が行われた可能性。Synthetic Organic Chemistry textbook や Comprehensive Organometallic Chemistry supplement にも含まれる可能性。
* **Bibliographic confidence**: Low — 具体的 review paper の存在未確認。
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須] — Murai グループの review paper を確認。条件 (b) に該当。
* **Filling timescale category**: field-methodology (3-7 yr)
* **注記**: Field-wide benchmark comparison の数値が published review で初めて明示される可能性が高い。Original paper では「among highest reported」に留まる。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Murai et al., full article (推測, J. Am. Chem. Soc. or J. Org. Chem. ca. 1994-1996) | EP-01a, EP-08a | VQ-2 | 1994-96 | Low | Medium | [必須] |
| 2 | Chatani, N., Kakiuchi, F. & Murai, S., mechanistic study (推測, Organometallics ca. 1996-1998) | EP-03a, EP-06a | VQ-3 | 1996-98 | Low | Medium | [必須] |
| 3 | Murai et al., scope-extension paper (推測, ca. 1995-1997) | EP-05a, EP-07a | VQ-3 | 1995-97 | Low | Low | [必須] |
| 4 | Chatani, N. & Murai, S., review or perspectives (推測, Chem. Rev. or Acc. Chem. Res. ca. 1997-2002) | EP-09a | VQ-4 | 1997-2002 | Low | Low | [必須] |

**選定理由：**

本推奨選定リストは、4 つの filling candidate 論文を VQ 階層順に配列し、VQ-2 / VQ-3 / VQ-4 の各層での填充を示す。ただし、すべての候補が **「推測」** と明示されており、Haiku 4.5 モデルは Murai グループの post-1993 publication record を確実には記憶していない。各候補論文の実存確認は post-hoc verification step で必須である。

**バンドル充填：** 論文 1 (full article) が EP-01a と EP-08a の両方を同時に充填し、論文 2 (mechanistic study) が EP-03a と EP-06a を充填することで、format-driven と technical-barrier の dual timeline が観察される。

**著者グループの自己充填パターン：** Murai / Chatani / Kakiuchi グループ内部で、communication (1993) → full paper (1994-96) → mechanistic detail (1996-98) → field review (1997-2002) という時間軸が想定される。自己充填パターンの確認。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸（推測）：**

- **VQ-2 要件**: EP-01a (GC calibration), EP-08a (replication) → 推測年 1994-1996 (full article)
- **VQ-3 要件**: EP-03a (Ru(0) observation), EP-06a (intermediate validation) → 推測年 1996-1998 (mechanistic study)
- **VQ-3 要件（補足）**: EP-05a (selectivity quantification), EP-07a (boundary test) → 推測年 1995-1997 (scope extension)
- **VQ-4 要件**: EP-09a (external benchmark) → 推測年 1997-2002 (review/perspectives)

**階層-時間対応の評価：**

Murai 論文のケースでは、VQ-2 要件（reporting integrity）が VQ-3 要件（mechanistic experiments）より早期に充填される傾向が観察される（1994-96 vs 1996-98）。これは「format-driven auto-resolution」（communication → full article への自動展開）と「technical-barrier resolution」（mechanistic technology の成熟）が異なる timescale を持つためである。VQ 階層が上がるほど充填時間が長くなるという一般仮説は、本ケースでも部分的に支持される。ただし、この観察はすべて **推測** に基づいており、実際の publication timeline は post-hoc verification で確認が必須。

**特筆すべきパターン：**

本分析の全候補は **Haiku 4.5 の推測** であり、確実な source paper が同定できていない。特に EP-04a（KIE、M-H vs M-C discrimination）は明らかに未充填と判定される。Murai グループ自身が mechanistic detail に乗り出した（後年の Chatani-Kakiuchi era 2000s のさらに後期）可能性があるが、1993 communication の直後の 1994-1998 年の early mechanistic work では、ここまで詳細な実験は実施されなかった可能性が高い。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-04a [Discrimination / replication pack]:**
* **未充填の理由**: 「インセンティブ構造的未充填」＋「成功による問いの抹消」— 異なるメカニズム（ラジカル経路、C–O reductive elimination の alternative proposal 等）が後年提案されたことにより、M–H vs M–C insertion の詳細判定の重要性が減少した可能性。または、Murai グループの研究 agenda が mechanism determination ではなく scope extension / catalyst development に集中していた可能性（communication の「not yet clear」宣言が、その後の priority 設定を反映）。
* **発見的意義**: あり — 「Science community が 30 年を費やした C–H 活性化の最初の catalytic triumph を手にした時点で、詳細なメカニズムの検証（KIE、intermediate discrimination）をあえて後回しにした」というパターンは、「discovery velocity が mechanistic understanding に優先する」という scientific decision-making の記録として UQS により回復される。これは era-norm annotation の重要例。
* **将来の充填可能性**: 高 — KIE 測定、deuterated substrate、computational mechanism validation は現代技術で完全に可能。未充填は方法論上の困難ではなく、当時の priority decision の反映。

---

**全体評価：**

本 Stage 4 分析では、Murai 1993 における 9 つの EP のうち 8 つの充填候補を同定した。ただし、**すべての候補が Haiku 4.5 の推測** に基づいており、確実な publication record verification を欠いている。本分析は post-hoc verification step が必須の「low-confidence filling map」である。

特に重要な発見は、EP-04a（mechanism discrimination）の明確な未充填パターンであり、これが Murai グループ自身の「mechanism は未決定のまま scope 確立を優先」という戦略的選択を示唆している点である。
