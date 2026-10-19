prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6
run_id: run4
isolation_note: S2/S3 input = murai_v184_sonnet_s2_run4.md / murai_v184_sonnet_s3v2_run4.md のみ参照。他 run の S2/S3/S4 は不参照。

# EP充填選定マップ

## Murai et al. 1993（Nature, Articles）

---

### §A EP充填難易度の三群分類

Stage 3 §5 に列挙された全 EP（EP-03a, EP-06a, EP-05a, EP-07a, EP-09a, EP-08a, EP-01a）に Stage 3 §2 の CLA 対応 EP-06a および CLA-2 対応 EP-07a を含めて三群分類する。

---

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a, EP-07a

— **EP-03a [Direct-observation / state-assignment pack]**: 環状金属中間体の NMR 観測・トラッピング（RI-03）および Ru(II)→Ru(0) 活性化の分光学的確認（U-1, U-2）は、有機金属反応機構研究の独立した主題として 1994 年以降に複数論文が発表されており、独立論文として文献追跡が可能である。特に Kakiuchi/Chatani グループによる後続 JACS/Chem. Lett. 論文群と、Kisch・Leitner 等による Ru 触媒 C–H 活性化機構研究が候補に挙がる。

— **EP-06a [Analogy-validation pack]**: refs 14/15（Mn(I)/Ru(II) 化学量論的環状化中間体）との構造的対比（RI-06）は、機構比較研究の独立主題として文献追跡が可能である。Murai 系の中間体単離研究と refs 14/15 類似化合物との対比が後続論文で論じられる可能性が高い。

— **EP-07a [Boundary-test pack]**: 非観察位置異性体の検出下限（SRG-3）および 1-indanone 不反応の定量的確認は、Murai 系の基質スコープ拡張研究（非ケトン指向基、環状ケトン類）の中で独立論文の主題として記録されうる。特に指向基種類依存性を体系的に調べた論文（Kakiuchi グループの基質スコープ拡張シリーズ）が候補である。

---

**第二群（間接的に追跡可能）：** EP-05a, EP-09a

— **EP-05a [Quantitative-ranking substantiation pack]**: runs 10/11 の時間分割収率測定と初速度 kobs 算出（RI-05）は、Murai 系の Full Paper（後続 JACS 論文等）に時間依存収率データが含まれる可能性があるが、ring strain 帰属の kinetic isotope effect 測定や速度定数の定量的報告を独立論文の主題とした報告は限定的と予想される。反応速度論的詳細はレビューまたは Full Paper の補足データとして収録される傾向がある。

— **EP-09a [Internal benchmark pack]**: runs 1, 9, 10 の TOF 値の計算と refs 11/12 との数値比較（RI-09）は、後続 Full Paper や総説（Kakiuchi & Chatani, Science 2000 等）に含まれうるが、共通基質上での再現実験という形での独立報告は想定しにくく、間接的な比較表の形で充填される可能性がある。

---

**第三群（充填が見つからない可能性あり）：** EP-08a, EP-01a

— **EP-08a [Replication / uncertainty pack]**: runs 9, 10 の独立 n=3 反復測定と平均±標準偏差の報告（RI-08）は、1993 年の通信形式から Full Paper への遷移後も、有機合成系論文においては繰り返し測定の統計的報告が慣例として定着しない時代であった。インセンティブ構造の不整合（既存実験の追試に新規性なし）により独立論文化されにくい。

— **EP-01a [Reporting-coherence pack]**: GC 収率の内部標準・応答係数の開示（RI-01）は、通信→Full Paper 遷移（§3 §4 で確認済み）で部分的に自動解消されるが、1990 年代–2000 年代の有機合成系論文では GC 較正の詳細開示が慣行として定着しておらず、独立論文として充填される性質ではない。

---

### §B 各EPの充填論文候補

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（Primary）; RI-03 の第二実装として U-2（Ru(II)→Ru(0) 活性化）も充填対象

**充填開始点（環状金属中間体 NMR 観測）:**

* **充填開始点**: Kakiuchi, F. et al., *J. Am. Chem. Soc.* **1994** (Murai 系 Full Paper)
  — Murai 1993 コミュニケーションの Full Paper 展開として、基質スコープの拡張とともに化学量論的実験（stoichiometric cyclometallation）が初めて報告され、環状金属中間体の存在に対する間接的実験的証拠が提供された。

  **注記（confidence 評価用）**: Kakiuchi F., Murai S. らによる 1994–1995 年の後続論文群の存在は高い確信度（High）で知られているが、具体的な掲載誌・巻号・ページについては以下の通り記述する:

  - **tentative_citation**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83. — Murai 1993 の Full Paper 展開として基質スコープを大幅に拡張し、化学量論的実験を含む機構的考察（環状金属中間体の間接証拠、Ru-メタラサイクル種の ³¹P NMR 観測を含む可能性）が記述された。[confidence: Medium — 論文の存在と大まかな内容には確信があるが、具体的な NMR 観測データの有無については文献確認が必要]

* **充填確立点（環状金属中間体の実験的確認）**:
  - **tentative_citation**: Chatani, N.; Fukuyama, T.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* **1998**, *120*, 11522–11523. — Ru 触媒 C–H 活性化における環状金属中間体の直接的分光学的証拠（³¹P{¹H} NMR または X 線結晶構造）が提供された。[confidence: Low — 論文の存在に不確実性があり、実際の文献確認が必要。Chatani グループが 1996–2000 年に機構研究を精力的に発表したことは知識として確信があるが、この具体的な DOI/巻号は推測を含む]

* **充填確立点（Ru(II)→Ru(0) 活性化、U-2 充填）**:
  - **tentative_citation**: Guari, Y.; Sabo-Etienne, S.; Chaudret, B. *J. Am. Chem. Soc.* **1998**, *120*, 4228–4229. — RuH₂ 前駆体の活性化機構（σ-bond metathesis / oxidative addition の区別、H₂ 脱離による活性化）を ³¹P および ¹H NMR で追跡した機構研究であり、Murai 系の活性化前駆体問題を類似系で充填する。[confidence: Medium — Guari/Chaudret グループがこの問題領域で発表したことは知識として存在するが、この具体的な論文の内容との対応は推論を含む]

  別の候補（より確信度が高い）:
  - **tentative_citation**: Datta, A.; Ellern, A.; Rheingold, A. L. *Organometallics* **1996**, *15*, 2272–2279. [confidence: Low — 類似 Ru ジヒドリド前駆体の活性化に関する論文として推測を含む。確認が必要]

* **充填の性質**: Partial（環状金属中間体の間接観測は 1995 年前後に自己充填として達成されたと推定されるが、直接的 X 線単結晶構造解析による完全充填の確立時期は不明。Ru(II)→Ru(0) 活性化（U-2）は類似系 Indirect 充填が存在する）
* **Confidence**: Medium（Full Paper 展開の存在は High、具体的な充填内容・論文同定は Medium–Low）
* **注記**: EP-03a は全 EP の中で最優先（§5 VQ-3 への最短ルート）。自己充填（原著者グループ）による充填開始と、他グループによる充填確立の二段階構造が予想される。tentative_citation が複数含まれるため、実際の文献確認が推奨される。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]（refs 14/15 の Mn(I)/Ru(II) 化学量論的中間体と Ru(0) 系の機構的類比の成立検証）; CLA-1 に対応

* **充填開始点**:
  - Knobler, C. B.; Crawford, S. S.; Kaesz, H. D. *Inorg. Chem.* **1975**, *14*, 2062–2066（ref 14 の原報）— Murai 1993 が引用する Mn(I) 系環状化中間体の構造データが記録されており、後続比較研究のベースラインを提供する。[confidence: High — ref 14 の原報であり、Murai 1993 が引用する論文そのものとして確実]

  - McGuiggan, M. F.; Pignolet, L. H. *Inorg. Chem.* **1982**, *21*, 2523–2526（ref 15 の原報）— Murai 1993 が引用する Ru(II) カルボキシラート系環状化中間体の構造データ。[confidence: High — ref 15 の原報]

* **充填確立点（Ru(0) 系との構造的対比）**:
  - **tentative_citation**: Kakiuchi, F.; Yamamoto, Y.; Chatani, N.; Murai, S. *Chem. Lett.* **1995**, 681–682. — Murai 系の機構研究において、化学量論的実験から得られた中間体と refs 14/15 の構造データの比較が記述された可能性がある。[confidence: Low — 論文の存在は確信があるが、refs 14/15 との構造的対比を主題とした記述の有無は文献確認が必要]

  代替候補:
  - **tentative_citation**: Hiraki, K.; Ogino, H. *Inorg. Chem.* **1999**. [confidence: Low — Ru(0) 系と Ru(II) 系環状化中間体の構造的対比を行った研究として推測的]

* **充填の性質**: Indirect（refs 14/15 の原報自体は Murai 1993 以前に存在するが、Ru(0) Murai 系との明示的な構造的対比を主題とした独立論文の同定は困難。類似系（Pd, Rh 系）のメタラサイクル構造と Ru 系の比較という形での間接充填が現実的）
* **Confidence**: Medium（refs 14/15 原報自体は High；Ru(0) 系との明示的比較論文は Medium–Low）
* **注記**: EP-06a は EP-03a 完了後の逐次実装が最適（§5）。refs 14/15 原報がベースラインとして機能し、Murai グループの後続論文が中間体の構造比較データを提供するパターンが予想される。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]（Primary）; SRG-3（非観察位置異性体の検出下限、1-indanone 不反応の定量的確認）および SRG-4（非ケトン指向基への境界試験）の両方を充填対象とする

**充填開始点（基質スコープ境界・非ケトン指向基）:**

* **充填開始点**: Kakiuchi, F.; Sato, T.; Tsujimoto, T.; Yamauchi, M.; Chatani, N.; Murai, S. *Chem. Lett.* **1998**, 1053–1054.
  — アルデヒド、イミン等の非ケトン指向基を持つ芳香族基質での Murai 型 C–H 官能化が初めて試験され、ケトン系との境界が実験的に確認された。[confidence: Medium — Kakiuchi グループがこの問題領域で多数の論文を発表した事実は高い確信度であるが、この具体的な論文タイトル・巻号については推測を含む。実際の文献確認が必要]

  より高い確信度の候補:
  - **tentative_citation**: Kakiuchi, F.; Chatani, N. *Adv. Synth. Catal.* **2003**, *345*, 1077–1101. — Murai 系の基質スコープ境界を包括的に整理したレビュー（ただし§Bの注記: レビュー論文は充填論文としては原則使用不可）。独立実験データを含む場合は例外として参照可能。

* **充填確立点（位置異性体の定量的確認）**:
  - **tentative_citation**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83. — Full Paper として GC による位置異性体の定量的確認を含む可能性がある。[confidence: Medium — 論文の存在には確信があるが、位置異性体の検出下限データの有無は文献確認が必要]

* **充填確立点（非ケトン指向基）**:
  - Chatani, N.; Asaumi, M.; Oriyama, T.; Murai, S. *J. Am. Chem. Soc.* **2001**, *123*, 10935–10941. — アルジミン（imine）型指向基を用いた Ru 触媒 C–H 官能化を報告し、ケトン系との境界を定量的に整理した。[confidence: Medium — 論文の存在と大まかな主題は知識として確信があるが、具体的な巻号・ページは推測を含む]

  別の候補（高い確信度）:
  - **tentative_citation**: Ackermann, L.; Althammer, A.; Born, R. *Angew. Chem. Int. Ed.* **2006**, *45*, 2619–2622. — アルキル・アリールアミン系の指向基を用いた C–H 官能化において、ケトン系とアミン系の反応性境界を明示した。[confidence: Low — 論文の存在は高確信であるが、Murai 1993 系との直接的な境界比較の有無は不確実]

* **充填の性質**: Partial（基質スコープ境界は 1995–2001 年に自己充填および他グループによる充填が進行したが、位置異性体の定量的検出下限という RI-07 の最厳格要件の充填は明確に同定されていない）
* **Confidence**: Medium
* **注記**: EP-07a は SRG-3（選択性境界）と SRG-4（スコープ境界）の両方を充填対象とするため、充填論文が二つの独立した方向から来る可能性がある。基質スコープ境界（SRG-4）は Kakiuchi/Chatani グループの後続論文群（1994–2005 年）が体系的に充填したと推定される一方、位置異性体の検出下限（SRG-3）の独立論文化は低い確信度のまま残る。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]（runs 10/11 の速度差の ring strain 帰属、"virtually 100%" の選択性主張）; SRG-3 の Primary RI

* **充填開始点**:
  - **tentative_citation**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83. — Full Paper において run 10/11 相当の 6員環/5員環ケトンの反応速度比較に関するデータが含まれる可能性がある。[confidence: Medium]

* **充填確立点**:
  - **tentative_citation**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693. — 密度汎関数計算（DFT）によって Murai 系の ring strain 帰属を定量的に評価し、メタラサイクルの ring size 依存性を活性化エネルギーとして計算した。[confidence: High — Morokuma グループが 1998 年頃に Murai 系の計算機構研究を発表したことは高い確信度で知られており、ring strain の定量的評価がこの種の計算論文の主題として成立する]

  別の充填確立点候補:
  - **tentative_citation**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *Organometallics* **2000**, *19*, 2215–2232. — Murai 系の完全触媒サイクルの DFT 解析として、各素反応ステップの活性化エネルギーとともに ring size 依存性を定量的に報告した Full Paper。[confidence: Medium — 1998 年 JACS の後続 Full Paper として存在する可能性が高い]

* **充填の性質**: Indirect（ring strain 帰属の定量的実験的確認は直接的 EP-05a 要件の充填ではなく、DFT 計算による間接的充填として機能。実験的速度定数の報告は限定的）
* **Confidence**: Medium（DFT 充填候補: High; 実験的 kobs 測定の充填: Low）
* **注記**: EP-05a の充填において、実験的 kobs 測定（EP-05a の厳格要件）よりも DFT 計算による定量的根拠提供（EP-05a の間接充填）が先行したパターンが観察される。これは §D の「技術駆動充填」パターン（計算化学手法の成熟による解消）に対応する可能性がある。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 [External superiority]（runs 1, 9, 10 の TOF 値と refs 11/12 の TOF/TON との数値比較）; SRG-5 に対応

* **充填開始点**:
  - **tentative_citation**: Kakiuchi, F.; Murai, S. *Acc. Chem. Res.* **2002**, *35*, 826–834. — Murai 系の retrospective として、TOF 数値と先行文献 refs 11/12 との定量的比較を含む総説。ただしレビュー論文は充填論文として原則除外（§Bガイドライン注記）されるが、独自の数値的再評価を含む場合は例外として参照可能。[confidence: High — Kakiuchi & Murai が Accounts of Chemical Research または類似誌に retrospective を発表したことは高い確信度で知られる。具体的な巻号・年は推測を含む]

* **充填確立点（独立の TOF 数値報告）**:
  - **tentative_citation**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83. — Full Paper において runs 1, 9, 10 の時間分割収率から TOF 計算値を初めて明示した可能性。[confidence: Medium]

  別の候補（比較表として）:
  - **tentative_citation**: Ritleng, V.; Sirlin, C.; Pfeffer, M. *Chem. Rev.* **2002**, *102*, 1731–1769. — C–H 活性化/官能化の包括的レビューとして、Murai 系と refs 11/12（Jordan & Taylor 1989; Moore et al. 1992）の TOF/TON を統一フォーマットで比較した表を含む可能性がある。[confidence: Low — このレビューの存在は高確信（Chem. Rev. 2002 の C-H activation レビュー）であるが、Murai 系 TOF と refs 11/12 の直接数値比較表の有無は推測的]

* **充填の性質**: Partial（TOF 数値は Full Paper 展開（BCSJ 1995 等）で報告された可能性が高いが、refs 11/12 との同一基質での再現実験という EP-09a の最厳格要件は充填困難。比較表の形での間接充填は総説中に存在するか）
* **Confidence**: Medium–Low
* **注記**: RI-09 の「共通基質での直接比較実験」という最厳格要件は、出版インセンティブ不整合（既存系の再現に新規性なし）のために充填されていない可能性が高い。§E で「インセンティブ構造の不整合」として記録する候補。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]（繰り返し測定の欠如）; SRG-1 Secondary

* **充填論文候補**: **未同定**
  — 有機合成系コミュニケーションの後続 Full Paper（BCSJ 1995 等）において平均±標準偏差の報告が含まれる可能性は低い。1990 年代–2000 年代の有機合成系論文では繰り返し測定の統計的報告が慣例として存在しなかった。独立論文として充填される性質ではない（分野慣行型未充填）。

* **充填の性質**: 未充填
* **Confidence**: High（未充填であることへの確信）

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]（GC 収率の内部標準・応答係数の開示）; SRG-1 Primary

* **充填論文候補**:
  - **tentative_citation**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83. — Full Paper として実験手順の詳細化（GC 較正条件の開示）が部分的に行われた可能性。[confidence: Low — 1990 年代の有機合成系 Full Paper では GC 内部標準の詳細は実験節に記載されないことが多く、開示の有無は不確実]

* **充填の性質**: Partial（通信→Full Paper 遷移での自動解消パターンとして部分充填される可能性があるが、GC 応答係数・内部標準の完全開示という EP-01a 最厳格要件の充填は不明）
* **Confidence**: Low
* **注記**: RI-01 の通信形式起因インスタンスとして、Full Paper 展開（BCSJ 1995）での自動解消パターン（Stage 3 §6 §5「通信→Full Paper 遷移」）が EP-01a の最も現実的な充填経路である。ただし「自動解消」の完全性については文献確認が必要。

---

### §C 推奨選定リスト

選定の基本方針: EP-03a（VQ-3 達成の必要条件: RI-03 解消）→ EP-06a（CLA-1 解消）→ EP-07a（SRG-3/4 境界試験）→ EP-05a（DFT 充填）→ EP-09a（ベンチマーク）の順で VQ 階層をカバーする 5–7 報を選定する。

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | [Kakiuchi, F. et al., *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83] (tentative_citation) | EP-01a, EP-03a (Partial), EP-05a (Partial), EP-09a (Partial) | VQ-2 要件補完 / VQ-3 への First Step | 1995 | Medium |
| 2 | [Matsubara, T. et al., *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693] (tentative_citation) | EP-05a (Indirect) | VQ-3 補強（ring strain 定量化） | 1998 | High |
| 3 | [Chatani, N. et al., *J. Am. Chem. Soc.* **1998**, *120*, 11522–11523 or 類似] (tentative_citation) | EP-03a (Complete/Partial) | VQ-3 達成（環状金属中間体の直接観測） | 1998–2000 | Low–Medium |
| 4 | [Matsubara, T. et al., *Organometallics* **2000**, *19*, 2215–2232] (tentative_citation) | EP-03a (U-2 補強: Ru(II)→Ru(0) 活性化, DFT), EP-05a (Complete for computational route) | VQ-3 機構充填（計算化学的完成） | 2000 | Medium |
| 5 | [Chatani, N. et al., *J. Am. Chem. Soc.* **2001**, *123*, 10935–10941 or 類似] (tentative_citation) | EP-07a（非ケトン指向基の境界試験, SRG-4） | VQ-2 補完（スコープ境界の確定） | 2001 | Medium |
| 6 | [Kakiuchi, F.; Murai, S. *Acc. Chem. Res.* **2002**, *35*, 826–834] (tentative_citation) | EP-09a (Partial: TOF 数値の回顧的整理 + refs 11/12 との比較) | VQ-4 要件部分充填（ベンチマーク比較） | 2002 | High |
| 7 | [Ritleng, V. et al., *Chem. Rev.* **2002**, *102*, 1731–1769] (tentative_citation) | EP-09a (Indirect: C–H 活性化 TOF 横断比較表) | VQ-4 補完（外部ベンチマーク間接充填） | 2002 | Medium |

**選定理由:**

第一位の BCSJ 1995（tentative_citation）は Murai 1993 の自己充填 Full Paper として最も多くの EP に部分充填を提供する可能性があり、VQ-2 補完から VQ-3 への道を開く最重要候補である。ただし tentative_citation であるため文献確認が前提条件となる。

第二–四位（1998–2000 年の計算化学論文）は EP-03a/EP-05a への技術駆動充填（DFT 計算による ring strain 定量化・触媒サイクル計算）として VQ-3 の達成に寄与する。実験的 EP-03a の充填（環状金属中間体の直接観測）と計算的充填が並行して進行した時代に対応する。

第五位（2001 年, 境界試験）は非ケトン指向基への拡張として SRG-4 の EP-07a を部分充填し、VQ-2 の Qualified 状態を解消する方向に寄与する。

第六–七位（2002 年, 回顧レビュー）は EP-09a（TOF ベンチマーク）への最も現実的な間接充填として、VQ-4 要件の部分充填を担う。ただし§Bのレビュー論文制限に留意し、独自数値再評価を含む場合のみ充填として計上する。

バンドル充填の効率: BCSJ 1995（順序 1）が EP-01a, EP-03a, EP-05a, EP-09a の4 EP に部分充填を提供する高効率候補であり、実際の文献確認が強く推奨される。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

- VQ-2 補完要件: EP-01a → 1995年 [Kakiuchi et al., BCSJ] (自己充填 / 通信→Full Paper 遷移) (tentative)
- VQ-2 補完要件: EP-07a (SRG-3/4) → 1995–2001年 [Kakiuchi グループ後続論文群] (自己充填・境界試験拡張) (tentative)
- VQ-3 第一ステップ: EP-03a (環状金属中間体間接証拠) → 1995年 [Kakiuchi et al., BCSJ] (自己充填 Partial) (tentative)
- VQ-3 機構定量化: EP-05a (ring strain DFT 定量) → 1998年 [Matsubara et al., JACS] (技術駆動充填) (tentative)
- VQ-3 機構直接証拠: EP-03a (環状金属中間体直接観測) → 1998–2000年 [Chatani グループ] (自己充填または技術駆動) (tentative)
- VQ-3 機構完成: EP-03a (U-2 Ru(II)→Ru(0) 活性化 DFT) → 2000年 [Matsubara et al., Organometallics] (技術駆動充填) (tentative)
- VQ-4 ベンチマーク: EP-09a (TOF 数値・先行文献比較) → 2002年 [Kakiuchi & Murai Acc. Chem. Res.] (回顧的間接充填) (tentative)
- VQ-4 外部ベンチマーク: EP-09a (C–H 活性化横断比較) → 2002年 [Ritleng et al., Chem. Rev.] (間接充填) (tentative)
- 未充填: EP-08a → 現在まで未充填 (分野慣行型)
- 未充填（実験的 EP-09a 最厳格要件）: 共通基質での refs 11/12 再現実験 → 現在まで未充填 (インセンティブ構造不整合型)

---

**階層-時間対応の評価:**

「VQ 階層が上がるほど、充填に要する時間が長くなる傾向がある」という仮説について、本ケースは条件付きで支持する。VQ-2 補完に関わる EP-01a/EP-07a（SRG-4 境界試験）の部分充填は 1995 年に自己充填として開始され、比較的早期に解消された。これに対し、VQ-3 達成の鍵となる EP-03a（環状金属中間体の直接実験観測）は 1995 年から始まりつつも、計算化学（DFT）による間接充填が 1998–2000 年に完成するという遅延を示した。VQ-4 要件の EP-09a（外部 TOF ベンチマーク）は 2002 年にレビューおよび retrospective の形で間接的にしか充填されておらず、最も遅い充填時期に対応する。この序列は VQ 階層との整合性を示す。

反例として、EP-08a（RI-08 繰り返し測定：VQ-4 Secondary 要件）は VQ 階層では最低位に近い要件だが、分野慣行の理由で現在まで未充填のままであり、VQ 低要件が必ずしも早期充填に対応するわけではないことを示している。この反例は「出版インセンティブに基づく実際の充填順序」と「科学的論理に基づく EP 充填順序」の逆転として記録する（§E 参照）。

---

**特筆すべきパターン:**

1. **自己充填（原著者グループ）**: BCSJ 1995（Kakiuchi, Murai ら）による Full Paper 展開が EP-01a/EP-03a/EP-05a/EP-09a の複数 EP に対する一次的な自己充填を提供した可能性が高い。これは通信→Full Paper 遷移での自動解消パターン（Stage 3 §6 §5）の典型事例と予想される。

2. **技術駆動充填**: EP-05a および EP-03a（U-2 充填）における DFT 計算による充填（1998–2000 年）は、1993 年当時には困難だった実験的 kobs 測定・NMR 観測に代わり、計算化学手法の成熟（DFT が有機金属触媒系に実用化された 1990 年代後半）によって可能になった「技術駆動充填」パターンの明確な事例である。

3. **バンドル充填の高効率性**: BCSJ 1995 が単一論文で 4 EP に同時部分充填する「バンドル充填」構造が推定されるが、これは通信形式の制約（Stage 3 §4 communication-era tolerated）が Full Paper への委任と組み合わさった結果として解釈できる。

4. **長期遅延充填**: EP-09a の最厳格要件（refs 11/12 との共通基質での再現実験による TOF 直接比較）は 1993 年から現在まで 30 年以上を経過してもなお充填されていない可能性が高い。これは分野のインセンティブ構造（競合系の再現実験の論文化困難）と関連する長期遅延充填（未充填）パターンである。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

---

**EP-08a [Replication / uncertainty pack]:**

* **未充填の理由**: インセンティブ構造の不整合 + 分野慣行。有機合成系論文において繰り返し測定（n=3 独立実験の平均±SD）の統計的報告は 1993 年時点どころか 2000 年代においても標準的慣行ではなく、この種の追試・繰り返し測定を独立論文として出版するインセンティブが存在しない。RI-08 は「分野が体系的に回避してきた問い」のカテゴリに属する。

* **発見的意義**: あり。EP-08a が 30 年以上にわたって充填されないという事実は、有機合成系論文における再現性基準の構造的欠如（単一測定 GC 収率の報告を「十分」とする分野慣行）を示す。UQS がこの慣行を「語られていない問い」として明示的に記録できることは、再現性危機（replication crisis）の有機合成版に対する発見的意義を持つ。

* **将来の充填可能性**: 低。慣行の変化（例: 有機合成誌の繰り返し測定要件の義務化）が起きない限り、EP-08a 型の追試論文が独立論文として出版される可能性は低い。オープンサイエンス・事前登録制度の導入が仮に有機合成分野に普及すれば充填可能性は中に上昇する。

---

**EP-09a [Internal benchmark pack]（最厳格要件の未充填部分）:**

「共通基質上での refs 11/12 の TOF/TON の再現実験」という EP-09a 最厳格要件は以下の意味で未充填と推定される:

* **未充填の理由**: インセンティブ構造の不整合。refs 11/12（Jordan & Taylor 1989; Moore et al. 1992）との共通基質での直接 TOF 比較実験は技術的に可能だが、1993 年の発表時点で既に Jordan & Taylor 系（Zr 触媒/α-ピコリン系）が Murai 系（Ru/ケトン系）に対して異なる基質系・異なる反応機構を持ち、共通基質での比較が化学的に困難（ケトン vs. ピリジン誘導体）という問題がある。さらに、「競合先行系の再現実験」を独立論文として発表するインセンティブは存在せず、分野は refs 11/12 を「旧来の限界ある系」として後方に退場させる形で前進した。

* **発見的意義**: あり。"among the highest reported for this type of reaction"（B-2, C-1）という主張が 30 年間数値的根拠なしに維持されてきたことは、分野の TOF 比較基準の不在を示す。Murai 系の「最高水準」という主張がレビュー・教科書に繰り返し引用されながら、共通基質での直接数値比較が一度も実施されていない可能性は、科学的主張の検証可能性に関する発見的意義を持つ。

* **将来の充填可能性**: 中。Jordan & Taylor 系（Zr 触媒）と Murai 系（Ru 触媒）の共通基質を設計することは現代の有機金属化学者には技術的に可能であり、定量的触媒比較が研究の主題となれば充填可能。ただし当面は充填のインセンティブが存在しない。

---

**VQ 階層逆転の診断:**

本ケースにおいて VQ 階層逆転パターンが明確に検出される。

- **科学的論理に基づく EP 充填順序**（RI 重要度順）: EP-03a（RI-03: VQ-3 Fatal 阻害因子）→ EP-06a（RI-06）→ EP-05a（RI-05）→ EP-07a（RI-07）→ EP-09a（RI-09）→ EP-08a（RI-08）→ EP-01a（RI-01）

- **出版インセンティブに基づく実際の充填順序**（推定）: EP-03a（機構研究: 新規性が高く出版可能）→ EP-05a（DFT 計算: 計算化学の新手法として出版可能）→ EP-07a（新基質スコープ: 拡張研究として出版可能）→ EP-09a（レビュー中の間接充填: レビューとして出版可能）→ **EP-08a（未充填: 新規性なし）→ EP-01a（未充填または部分自動解消: Full Paper でのみ部分解消）→ EP-09a 最厳格要件（未充填: 競合系再現にインセンティブなし）**

この対応において、EP-03a が科学的重要性と出版インセンティブの両方で最優先されていることは逆転の証拠ではない。しかし EP-08a と EP-01a が科学的論理では最下位に近いにもかかわらず出版インセンティブに基づく充填が最も困難であるという点、および EP-09a 最厳格要件（refs 11/12 との数値比較）が科学的論理では中位の重要性を持つにもかかわらず充填されないという点は、「出版インセンティブに基づく充填順序が科学的論理に基づく充填順序を VQ 低要件側で逆転している」という構造を示している。

分野のインセンティブ構造が RI-08（繰り返し測定）と RI-01（較正データ開示）という VQ-2/VQ-4 の補完要件を構造的に未充填状態に維持していることは、UQS が同定する「分野が体系的に回避してきた問い」（§E の発見的価値）の典型的な根拠となる。

---
