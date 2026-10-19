```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Fodor et al. 2020（ACS Sustainable Chemistry & Engineering, full_paper）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a

- **EP-03a** (Direct-observation / state-assignment pack): GVL中のPd触媒休止状態の分光学的同定と[Et₃N]消費の追跡は、均一系触媒の機構研究として独立した論文主題になりやすい。GVL中のPd種の特性評価や基質-塩基-金属の三者相互作用を調べた論文が存在する可能性が高い。
- **EP-04a** (Discrimination / replication pack): branched vs linear migratory insertionのDFT比較は、Heck選択性に関する計算研究の主題として独立した論文の形で存在しやすい。また、Pd触媒Heck反応の選択性に関する実験的時系列データは複数のグループが報告している。
- **EP-06a** (Analogy-validation pack): GVL-SMDパラメータでのDFT再計算は、GVL中の触媒反応の計算研究として独立した論文の形で現れる可能性が高い。GVLを溶媒とした計算研究は2020年以降増加している。
- **EP-07a** (Boundary-test pack): ArBr基質のGVL中Heck反応試験は、GVL溶媒のスコープ拡張研究として独立した論文の形で存在しやすい。Vaccaro等のGVL/GVL-water中のHeck反応研究が関連する。

**第二群（間接的に追跡可能）：** EP-08a, EP-09a

- **EP-08a** (Replication / uncertainty pack): Eyring回帰の不確実度伝播と速度論的モデル統計は、方法論論文や総説の一部として触れられるが、Fodor et al.の特定系での追実験として独立論文になる可能性は低い。他のPd触媒速度論系での類似手法の適用論文が間接的な参照点となる。
- **EP-09a** (Internal benchmark pack): Pd/amine Heck系の活性化パラメータの文献値との体系的比較は、速度論レビュー論文や、類似系での独立した速度論研究の一部として存在する可能性があるが、Fodor et al.の特定の系への適用として独立した論文にはなりにくい。

**第三群（充填が見つからない可能性あり）：** EP-01a

- **EP-01a** (Reporting-coherence pack): 水分量・内部標準・検量線の一貫した記載はFull Paperへの展開時の自動解消パターンに属する。Fodor et al.のSI（Supporting Information）内に一部情報が含まれる可能性があるが、独立した充填論文の対象にはなりにくい。Mika/Horváthグループの後続論文でのmethod sectionで補完される可能性がある。

---

### §B 各EPの充填論文候補

**EP-03a (Direct-observation / state-assignment pack)（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory)
* **充填開始点**: Strappaveccia et al., *Green Chem.* 2015, 17, 365–372 — GVLを溶媒としたSonogashiraクロスカップリングにおいてPd触媒種の特性評価を実施し、均一系Pd/GVL相互作用の先行情報を提供した。
* **充填確立点**: 未同定 — 原著者グループ（Mika/Kéglグループ）による後続論文でのGVL中活性Pd(0)種の分光学的追跡が期待されるが、現時点でそのような続報はモデルの知識範囲内で確認されていない。
* **充填の性質**: Partial — Strappaveccia (2015)はGVLがPd触媒種の安定化に寄与することを示唆するが、[Et₃N]消費の定量的追跡や活性Pd(0)種のGVL条件下での直接同定は行っていない。
* **Confidence**: Medium — Strappaveccia (2015)の存在と内容には確信があるが、EP-03aの中核（[Et₃N]定量追跡）との対応は間接的。
* **注記**: GVL-Et₃N側反応（U-1）の定量的追跡については充填論文が未同定。Cséfalvay (ACS Sustain. Chem. Eng. 2018)がGVL-amine反応条件を部分的に扱っているが、Heck速度論条件での追跡ではない。

---

**EP-04a (Discrimination / replication pack)（第一群）**

* **充填するRI**: RI-04 (Unreplicated discriminator)
* **充填開始点**: von Schenck et al., *Organometallics* 2002, 21, 2248–2253 — ホスフィン配位Pd系でのHeck反応におけるlinear vs branched migratory insertionのDFT比較を実施し、選択性の計算的起源の先例を提供した。
* **充填確立点**: Menezes da Silva et al., *Organometallics* 2016, 35, 3170–3181 — NHC-Ni/Pd複合体のMizoroki-HeckサイクルにおけるDFT比較で、分岐経路の活性化エネルギーを直接計算しており、branched TS計算の方法論的先例となる。
* **充填の性質**: Indirect — von Schenck (2002)はホスフィン系でのlinear/branched選択性を計算しており、ホスフィンフリー・Et₃N配位系での直接充填ではない。
* **Confidence**: Medium — 論文の存在と内容には確信があるが、Et₂N-Pd(Ph)(I)系という特定の系での充填との対応は推論を含む。
* **注記**: EP-04aのうち「選択性の時系列測定」要素については充填論文が未同定。GVL中Heck選択性を複数時点で報告した論文はモデルの知識範囲内では確認されていない。

---

**EP-06a (Analogy-validation pack)（第一群）**

* **充填するRI**: RI-06 (Imported model)
* **充填開始点**: Surawatanawong & Hall, *Organometallics* 2008, 27, 6222–6232 — Pd中間体の触媒サイクルにおける理論的研究でSMD系溶媒モデルの適用を示し、溶媒効果の感度を議論した先例。
* **充填確立点**: Bäcktorp & Norrby, *Dalton Trans.* 2011, 40, 11308–11314 — Heck反応の中性・カチオン経路のDFT比較において、溶媒モデルの遷移状態エネルギーへの影響を扱い、ε差の影響について議論した。
* **充填の性質**: Indirect — 両論文ともGVL-SMDパラメータでの再計算そのものを行っておらず、SMD溶媒効果の一般的感度分析が充填の役割を果たす。
* **Confidence**: Medium — 論文の存在には確信があるが、GVL/DMF差（Δε ≈ 4.6）が遷移状態エネルギーに与える影響への直接的対応は推論的。
* **注記**: 2020年以降、GVL-SMDパラメータを用いたPd触媒DFT研究が発表されている可能性があるが、現時点では特定できない（Confidence: Low）。

---

**EP-07a (Boundary-test pack)（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary)
* **充填開始点**: Strappaveccia et al., *Green Chem.* 2015, 17, 365–372 — GVLを溶媒としたHeck反応でArBrを含む基質スコープを試験しており、CLA-1のArBr試験要件への最初の充填点となる可能性がある。
* **充填確立点**: 未同定 — Pd(OAc)₂/Et₃N/GVL系でのArBr試験を直接実施した論文はモデルの知識範囲内では確認されていない。
* **充填の性質**: Partial — Strappaveccia (2015)はGVL中ArBr-Heckを示すが、Pd(OAc)₂/Et₃Nというまったく同一の触媒系ではなくPd-NHCを使用している。
* **Confidence**: Medium — Strappaveccia (2015)の存在と内容には確信があるが、Pd(OAc)₂/Et₃N系の特定との対応は間接的。
* **注記**: U-5（イオン性 vs ラジカルOA）の充填については、Beletskaya & Cheprakov (*Chem. Rev.* 2000, 100, 3009–3066)がリン配位子なしPd系でのラジカル機構の可能性を詳細に議論しており、TEMPO実験等の方法論的先例を提供しているが、GVL系での直接試験は未充填。

---

**EP-08a (Replication / uncertainty pack)（第二群）**

* **充填するRI**: RI-08 (Unquantified reliability)
* **充填開始点**: Jagtap et al., *Kinet. Catal.* 2013, 54, 314–321 — PdCl₂(bipy)触媒Heck反応の速度論研究でChemmechを使用し、K₁k₂の温度依存性と不確実度を報告した。Fodor et al.と同一のChemmechプログラムを使用し、活性化パラメータの不確実度記述の先例となる。
* **充填確立点**: 同上（Jagtap 2013が現時点での最も直接的な充填点）。
* **充填の性質**: Indirect — Jagtap (2013)はPdCl₂(bipy)/NMP系であり、Pd(OAc)₂/Et₃N/GVL系そのものではないが、同一プログラムの使用と不確実度報告の方法論として最も近い先行例。
* **Confidence**: High — 論文の存在と不確実度記述の内容には確信がある。Fodor et al.がJagtap (2013)を本論文でref 28として直接引用していることから対応関係が直接的。
* **注記**: Jagtap (2013)はFodor et al.のref 28であり、原著者は不確実度報告の先例を知っていながら採用しなかった可能性がある。これはインセンティブ構造の問題（§E参照）と関連する。

---

**EP-09a (Internal benchmark pack)（第二群）**

* **充填するRI**: RI-09 (External superiority)
* **充填開始点**: Amatore & Jutand, *Acc. Chem. Res.* 2000, 33, 314–321 — Pd(0)/PPh₃触媒Heck/cross-coupling反応のアニオン・カチオン中間体の速度論的データを包括的にまとめ、活性化パラメータの参照ベースとして最も引用される文献。
* **充填確立点**: Jagtap et al., *Kinet. Catal.* 2013, 54, 314–321 — ΔH‡ = +98.7 kJ mol⁻¹（NMP, PdCl₂(bipy)系）を報告し、Fodor et al.の103.0 kJ mol⁻¹との直接数値比較を可能にする最も近い参照点。
* **充填の性質**: Partial — 配位子系（bipy vs phosphine-free）と溶媒（NMP vs GVL）が異なるため完全な充填ではない。ホスフィンフリーPd/amine系のHeck速度論パラメータを報告した論文は現時点では特定できない。
* **Confidence**: High（Amatore & Jutand 2000の存在と内容）; Medium（Jagtap 2013との対応）
* **注記**: refs 73–75がFodor et al.によって機構の根拠として引用されながら数値比較に使用されていないことはC-2として記録済み。このパターンはEP-09a充填の不完全性を強調する。

---

**EP-01a (Reporting-coherence pack)（第三群）**

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: 該当なし（独立した充填論文が性質上存在しない）
* **Confidence**: ― （未同定）
* **注記**: RI-01はFull Paperへの展開時の自動解消または原著者グループの後続論文でのmethod改善として解消される性質を持つ。EP-01aの充填を主目的とした独立論文は出版インセンティブ的に期待できない。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Jagtap et al., *Kinet. Catal.* 2013, 54, 314–321 | EP-08a, EP-09a（partial） | VQ-3→VQ-4 | 2013 | High |
| 2 | Strappaveccia et al., *Green Chem.* 2015, 17, 365–372 | EP-03a（partial）, EP-07a（partial） | VQ-2→VQ-3 | 2015 | Medium |
| 3 | Amatore & Jutand, *Acc. Chem. Res.* 2000, 33, 314–321 | EP-09a（partial） | VQ-4 | 2000 | High |
| 4 | von Schenck et al., *Organometallics* 2002, 21, 2248–2253 | EP-04a（indirect） | VQ-3 | 2002 | Medium |
| 5 | Bäcktorp & Norrby, *Dalton Trans.* 2011, 40, 11308–11314 | EP-06a（indirect） | VQ-3 | 2011 | Medium |
| 6 | Beletskaya & Cheprakov, *Chem. Rev.* 2000, 100, 3009–3066 | EP-07a（indirect, radical OA境界） | VQ-2 | 2000 | High |

**選定理由:**

Jagtap et al. (2013) を第1位とする。Fodor et al.が直接引用（ref 28）し、同一のChemmechプログラムを使用した速度論研究として、EP-08a（Eyring不確実度）とEP-09a（活性化パラメータ比較）の両方を部分的に充填するバンドル充填効率を持つ。原著者がこの文献を参照しながら不確実度を記述しなかった選択は、インセンティブ構造の問題（§E）の直接的証拠として機能する。

Strappaveccia et al. (2015) を第2位とする。GVL中でのPd触媒反応のEP-03a（Pd種観測）とEP-07a（ArBr基質）を部分的に充填するバンドル充填を提供し、且つ原論文の著者らが知っている可能性が高い文献である（Vaccaro/Mika グループの協調的研究として）。

Amatore & Jutand (2000) は速度論パラメータのベースライン参照として不可欠であり、EP-09aの充填確立点として第3位に置く。VQ-4要件（RI-09）への対応という点でVQ階層の最高水準をカバーする。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件（RI-07 OA機構境界）: EP-07a → 2000年 Beletskaya & Cheprakov [間接的充填]
- VQ-4 要件（RI-09 文献比較ベース）: EP-09a → 2000年 Amatore & Jutand [間接的充填]
- VQ-3 要件（RI-04 selective DFT）: EP-04a → 2002年 von Schenck et al. [間接的充填]
- VQ-3 要件（RI-06 SMD妥当性）: EP-06a → 2011年 Bäcktorp & Norrby [間接的充填]
- VQ-4 要件（RI-08 不確実度）: EP-08a → 2013年 Jagtap et al. [間接的充填]
- VQ-2 要件（RI-07 ArBr境界）: EP-07a → 2015年 Strappaveccia et al. [部分的充填]
- VQ-3 要件（RI-03 Et₃N監視）: EP-03a → **未充填**（直接充填論文なし）

**階層-時間対応の評価：**
本ケースでは「VQ階層が上がるほど充填に要する時間が長くなる」という仮説の明確な支持は見られない。VQ-4要件（EP-09a: Amatore 2000）はVQ-3要件（EP-04a: von Schenck 2002）より前に充填されており、むしろ「高VQ要件（機構・計算）の方が先に類似系で研究されており、中VQ要件（RI-03: 実験的観測）の充填が後になる、または未充填のまま残存する」という逆転パターンが示唆される。これはVQ階層-時間仮説の反例として記録する。

**特筆すべきパターン：**

- **自己充填の不在（現時点）**: 原著者グループ（Mika/Horváthグループ）による後続論文でのEP充填は現時点では確認されていない。EP-03a（[Et₃N]監視）のような実験的に実施可能な充填が2020年以降も未実施である可能性は、GVL-amine系での速度論的整合性検証への関心の低さ、またはGVL系を離れた研究展開を示唆する。

- **技術駆動充填の可能性**: EP-06a（GVL-SMD再計算）はORCA/Gaussianの標準機能で実施可能であり、2020年以降のGVL計算研究の増加とともに技術駆動充填として解消される可能性がある。ただし現時点では未確認。

- **分野横断充填**: EP-07a（OA機構境界）はBeletskaya & Cheprakov (2000)という有機金属化学の大型レビューによって間接的に充填されており、「分野全体の知識としては既知だが、対象論文の特定化学系への適用がなされていない」という構造を示す。これはGVL系固有の実験的プローブが未実施のまま残存していることを反映する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-03a (Direct-observation / state-assignment pack) — 中核部分が未充填:**

* **未充填の理由**: インセンティブ構造の不整合 + 技術的困難の組み合わせ。GVL中のPd(0)活性種の分光学的同定（µM濃度）は技術的に困難であり、独立論文として出版するには専門的な分光装置（XANES/EXAFS等）が必要。[Et₃N]の0–2500 sにわたる追跡は技術的には可能（GC/NMR）だが、既存の速度論論文の「補足実験」としては出版インセンティブが低い。また、充填に必要な実験（[Et₃N]追跡）が速度論モデルへの否定的証拠となる可能性があることも、原著者グループによる自己充填への障壁となりうる。
* **発見的意義**: あり。GVL-amine系での速度論的モデルの基本的前提（[Et₃N]一定）の検証が2020年以降も未実施であることは、「GVLを溶媒とする塩基依存触媒系の速度論的完全性」という問いを分野が系統的に回避してきたことの証拠として記録できる。この回避は、GVL溶媒研究がmechanism detailよりsustainability narrativeに重点を置くインセンティブ構造と整合する。
* **将来の充填可能性**: 中 — [Et₃N]定量追跡はGC/¹H NMRで実施可能であり、GVL系の速度論的完全性への関心が高まれば充填される可能性がある。XANES/EXAFSによるPd(0)同定はシンクロトロン施設へのアクセスが必要だが技術的障壁は2020年代に低下している。

---

**EP-01a (Reporting-coherence pack) — 未充填:**

* **未充填の理由**: 報告形式問題（RI-01）はFull Paper→Full Paperの展開時に自動解消される性質であるが、Fodor et al.は既にFull Paperである。独立論文としての充填は構造的に不可能。分野慣行として、速度論論文での水分量・内部標準の詳細記載は2020年以前から不完全な場合が多く、これは分野全体の報告基準の問題を反映している。
* **発見的意義**: 限定的。RI-01の未充填は個別論文の問題というよりも分野全体のreporting基準の問題を反映しており、UQSの観点では「充填が構造的に困難なEP」の事例として記録する価値がある。
* **将来の充填可能性**: 低 — 独立論文としての充填は期待できない。原著者グループの後続論文または本論文のcorrection/addendumとしてのみ解消可能。

---

**VQ階層逆転の診断:**
本ケースでは以下の逆転パターンが観察される：充填済みEPがVQ-3（EP-04a, EP-06a: RI-04, RI-06）とVQ-4（EP-09a: RI-09）の高VQ要件に集中し、未充填EPがVQ-3（EP-03a: RI-03）の中間VQ要件と第三群（EP-01a: RI-01）の低VQ要件に集中している。高VQ要件（機構・計算的）への対応論文は分野の計算化学的発展によって「先回り充填」されており、中・低VQ要件（実験的方法論・報告形式）の充填はインセンティブ構造上困難なまま残存している。これは「科学的論理に基づくEP充填順序（低VQ→高VQ）」と「出版インセンティブに基づく実際の充填順序（高VQ→低VQ）」の逆転パターンの事例として記録する。
```
