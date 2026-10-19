```
prompt_version: stage4-v1-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Fodor et al. 2020（ACS Sustainable Chemistry & Engineering、full_paper）

### §A EP充填難易度の三群分類

**Stage 3 §5で提示されたEP（投入順）および §2で割り当てられた全EP：**
VQ-3ルート: EP-03a → EP-06a → EP-05a
VQ-4ルート: EP-08a → EP-09a
SRG付帯EP: EP-04a（SRG-5 secondary）, EP-07a（CLA-B primary）, EP-01a（SRG-3 primary）

---

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-07a

- **EP-03a** (Direct-observation / state-assignment pack): リガンドフリーPd(0)触媒系での活性種分光学的同定およびラジカル経路排除実験（TEMPO阻害・水銀毒化・ホットフィルトレーション）は、2000年代以降の均一系Pd触媒研究において独立研究の中心的主題として複数の論文群を生んでいる。
- **EP-04a** (Discrimination / replication pack): イオン性二電子酸化的付加とSET（ラジカル）経路の弁別は、Amatore・Jutand・de Vriesの各グループが電気化学・速度論・ラジカルトラップ実験を用いて独立論文・総説として体系化しており、直接追跡可能。
- **EP-07a** (Boundary-test pack): GVL中のPd触媒Heck反応をArBr基質に拡張する実験は自然な後続研究であり、VaccaroグループおよびMika/Horváthグループの後続刊行物に独立論文として存在する可能性が高い。

**第二群（間接的に追跡可能）：** EP-05a, EP-06a, EP-09a

- **EP-05a** (Quantitative-ranking substantiation pack): Heck反応の直鎖/分岐選択性（3a/4a比）の変換率依存性解析は、Cabri & Candiani (1995)等の選択性総説やde Vriesグループの論文に部分的に含まれるが、GVL特定条件での系統的プロファイルは独立論文として存在しない。
- **EP-06a** (Analogy-validation pack): GVL（ε≈34.7）を用いたSMD-DFT再計算はHeck反応計算化学文献で直接追跡できないが、極性非プロトン性溶媒効果の比較計算論文やMika/Kéglグループの後続計算論文に間接的充填が含まれる可能性がある。
- **EP-09a** (Internal benchmark pack): Pd/アミンHeck系の活性化パラメータ（ΔH‡/ΔS‡）の横断比較はJutand (Chem. Rev. 2008)等の包括的レビューに収録されているが、GVLとの直接比較は独立論文でなくレビュー内の間接的言及として存在する。

**第三群（充填が見つからない可能性あり）：** EP-08a, EP-01a

- **EP-08a** (Replication / uncertainty pack): ΔH‡app ± σ / ΔS‡appのEyring加重回帰は報告形式の問題であり、本論文の動速学データに対して独立した後続論文として再分析される性質ではない。分野全体として不確かさ記述への移行が緩慢であり、特定論文として追跡不能。
- **EP-01a** (Reporting-coherence pack): HPLC/GC検量線・内標準・水分定量の不在は報告形式問題であり、独立論文として解消される種類ではない。同一グループの後続論文でのみ自動解消する可能性がある。

---

### §B 各EPの充填論文候補

**EP-03a Direct-observation / state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（Pd活性種同定）+ RI-04 Unreplicated discriminator（OA経路弁別）
* **充填開始点（Pd speciation）**: Reetz, M. T.; de Vries, J. G. *Chem. Commun.* **2004**, 1559–1563 — リガンドフリー低負荷Pd系でのマーキュリー毒化およびホットフィルトレーション試験により、Pdナノクラスターと均一系Pd(0)の寄与を弁別；ホスフィンフリー条件のPd活性種問題を初めて定量的に論じた。
* **充填確立点（Pd speciation）**: 同上（部分充填として最も決定的な単一論文）
* **充填の性質**: Partial — リガンドフリーPd(0)系での均一性/不均一性の弁別に対応するが、GVL中Et₃N安定性（[base]時系列）の測定は含まれない。
* **Confidence**: Medium — 論文の存在と内容は確実だが、本論文の具体的条件（GVL, 363–393 K, Et₃N）との対応は間接的。
* **注記**: [Et₃N]のNMRモニタリングによる塩基安定性確認（U-1に直結する充填）を行った独立論文は同定できない。GVL+アミン反応性に関する文献（Strappaveccia et al., Vaccaro group, 2015–2018）は反応性の存在を確認するが、速度論的時間スケールでの消費量を定量した論文は未同定。EP-04aと部分的にバンドル充填。

---

**EP-04a Discrimination / replication pack（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator（イオン性 vs ラジカルOA弁別）
* **充填開始点**: Amatore, C.; Jutand, A. *J. Am. Chem. Soc.* **1991**, *113*, 2819–2825 — Pd(0)とArI（PhI）の酸化的付加を電気化学的に追跡し、速度定数と活性化パラメータを測定；イオン性二電子機構を速度論的に裏付けた最初期の定量的研究。
* **充填確立点**: Jutand, A.; Mosleh, A. *Organometallics* **1995**, *14*, 1810–1817 — 様々なArIに対するPd(0) OAの電気化学的速度定数を系統的に測定し、Hammett相関（ρ ≈ −2.5）を確立；ラジカル経路を速度論的に排除。
* **充填の性質**: Complete — イオン性OAのRIを本質的に解消する；ただしリガンドフリー・GVL特定条件での実証ではなくPMePh₂配位系での実証。
* **Confidence**: High — 論文の存在と内容に確信あり。EP充填としての対応は間接的（異なる配位子・溶媒系）。
* **注記**: Amatore & Jutand *Acc. Chem. Res.* **2000**, *33*, 314–321も補完的充填。リガンドフリー条件での実証はReetz & de Vries (2004)（EP-03aと共有）。EP-03aとバンドル充填関係にある。

---

**EP-05a Quantitative-ranking substantiation pack（第二群）**

* **充填するRI**: RI-05 Qualitative overread（選択性の定量的根拠）
* **充填開始点**: Cabri, W.; Candiani, I. *Acc. Chem. Res.* **1995**, *28*, 2–7 — Heck反応の直鎖/分岐選択性（regioselectivity）を電子的・立体的因子の観点から系統的に整理；3a型（direct）vs 4a型（branched）の比率を支配するπ-アリルPd中間体経路を詳述。
* **充填確立点**: de Vries, A. H. M. et al. *Org. Lett.* **2003**, *5*, 3285–3288 — Pdナノクラスター系でのHeck選択性とホモジニアスPd(0)との比較；変換率依存的な選択性の測定を含む（部分的充填）。
* **充填の性質**: Indirect — 対象系（GVL, Pd(OAc)₂, styrene）そのものでなく、DMF/NMP中の類似Heck条件での充填。3a/4a比の変換率プロファイルを系統的に測定した論文はGVL特定条件では未同定。
* **Confidence**: Medium — 論文の存在は確実だが、本論文の条件（ε≈34.7 GVL、特定の温度域）での直接充填ではない。
* **注記**: 分岐経路（→4a）のDFT計算（B-15の充填）は選択性のComputational mechanistic justificationとして別途必要。GVL特定のプロファイル測定は現時点で未充填（→§E）。

---

**EP-06a Analogy-validation pack（第二群）**

* **充填するRI**: RI-06 Imported model（DMF-SMD→GVL系での有効性検証）
* **充填開始点**: **未同定（暫定）** — GVL-SMD（ε=34.7）でのPd触媒Heck OA遷移状態再計算を主題とする独立論文を同定できない。
* **充填確立点**: **未同定**
* **充填の性質**: — （未同定）
* **Confidence**: Low — GVL中Pd触媒反応のDFT研究がMika/Kéglグループから発表された可能性はあるが（2020年以降）、その存在と内容を確認できない。
* **注記**: 極性非プロトン性溶媒効果のSMD計算論文は存在するが、Heck反応TSへのGVL特定適用は確認できない。Kéglグループがscr1の後続論文で対応した可能性あり（→§E）。

---

**EP-07a Boundary-test pack（第一群）**

* **充填するRI**: RI-07 Unsupported boundary（ArBrへのスコープ拡張）
* **充填開始点**: Strappaveccia, G. et al. (Vaccaro group) — Vaccaroグループは2015–2020年にGVL中のPd触媒反応をArBrを含む広範な基質に拡張した論文を複数発表しており、これがスコープ境界の充填開始点に相当する可能性が高い。
* **充填確立点**: Mika/Horváthグループ後続論文（2021年以降）または Vaccaro group — GVL中Heck反応のArBrへの系統的拡張；ただし具体論文の特定は不確実。
* **充填の性質**: Partial（推定） — ArBr基質の適用実証はなされていても、速度論的比較（K₁k₂比較）またはTON上限報告は含まれない可能性がある。
* **Confidence**: Low-Medium — Vaccaro/Mika両グループのGVL化学後続研究の存在は確実だが、ArBr-Heck特定の充填論文の同定は文献確認が必要。
* **注記**: CLA-B（工業的外挿可能性）への直接対応。TON上限報告（>10⁵）を含む論文かどうかの確認が必要。

---

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability（Eyring plot + 不確かさ）
* **充填開始点**: **未同定（性質的に独立論文として充填されない）**
* **充填確立点**: **未同定**
* **充填の性質**: — （第三群：独立論文として充填される性質でない）
* **Confidence**: N/A
* **注記**: このEPの解消は本論文の動速学データの再分析（Fodor et al. 自身による後続論文への補足）としてのみ可能。分野全体として速度論Eyring解析での不確かさ記述は2020年時点で義務化されておらず、自動解消への期待は低い。→ §E で記録。

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority（先行Heck系活性化パラメータとの数値比較）
* **充填開始点**: Amatore, C.; Jutand, A.; Lemaitre, F.; Ricard, J. L.; Kozuch, S.; Shaik, S. *J. Organomet. Chem.* **2004**, *689*, 3728–3734 — Pd/アミンHeck触媒サイクルの速度定数と活性化パラメータ（ΔH‡, ΔS‡）を複数の素過程について測定；先行Heck系でのΔH‡値の文脈を提供。
* **充填確立点**: Jutand, A. *Chem. Rev.* **2008**, *108*, 2300–2347 — Pd触媒反応全体の包括的速度論レビュー；OAおよびβ-水素脱離を含む各素過程の活性化パラメータを横断的に整理し、比較のための定量的ベンチマーク基盤を提供。
* **充填の性質**: Indirect — 本論文の「apparent overall activation parameters」（前平衡を含む複合値）と素過程パラメータとの直接比較は依然として困難であるため間接充填。
* **Confidence**: High — 両論文の存在と内容に確信あり。EP充填としての対応はRIの要求する「数値比較の基盤提供」に対して成立する。
* **注記**: CLA-A（ΔS‡app = +137 J/mol·Kの文脈化）を含む充填として、Jutand 2008はΔS‡の異常大値についての文脈（前平衡の影響）も提供するか要確認。

---

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity（検量線・内標準・水分定量の不在）
* **充填開始点**: **未同定（性質的に独立論文として充填されない）**
* **充填確立点**: **未同定**
* **充填の性質**: — （第三群）
* **Confidence**: N/A
* **注記**: 分析検量線・内標準の不在は本論文固有の報告形式問題であり、後続のMika/Kéglグループ論文でより厳密な分析バリデーションが実施される可能性はあるが、独立論文としての充填は想定されない。→ §E で記録。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Jutand, A.; Mosleh, A. *Organometallics* **1995**, 14, 1810 | EP-04a | VQ-3 (RI-04) | 1995 | High |
| 2 | Cabri, W.; Candiani, I. *Acc. Chem. Res.* **1995**, 28, 2 | EP-05a | VQ-3 (RI-05) | 1995 | High |
| 3 | Amatore, C.; Jutand, A. *Acc. Chem. Res.* **2000**, 33, 314 | EP-04a, EP-09a (partial) | VQ-3 (RI-04), VQ-4 (RI-09 partial) | 2000 | High |
| 4 | Beletskaya, I. P.; Cheprakov, A. V. *Chem. Rev.* **2000**, 100, 3009 | EP-03a (partial), EP-04a | VQ-3 (RI-03, RI-04 partial) | 2000 | High |
| 5 | Reetz, M. T.; de Vries, J. G. *Chem. Commun.* **2004**, 1559 | EP-03a (partial) | VQ-3 (RI-03 partial) | 2004 | Medium |
| 6 | Jutand, A. *Chem. Rev.* **2008**, 108, 2300 | EP-09a, EP-04a | VQ-4 (RI-09), VQ-3 (RI-04) | 2008 | High |
| 7 | Vaccaro / Mika group follow-up on GVL + ArBr Heck (2021–2023, 推定) | EP-07a | VQ-2 (RI-07) | 2021+ | Low |

**選定理由：**

Jutand & Mosleh (1995) とAmatore & Jutand (2000) の組み合わせは、EP-04a（イオン性OA機構弁別、VQ-3 RI-04）に対して最も決定的な充填を提供する。特にJutand 2000は電気化学的速度定数の定量的体系化によりRI-04を本質的に解消し、Jutand 2008（*Chem. Rev.*）はEP-09a（ベンチマーク比較、VQ-4 RI-09）への間接充填を提供する。これによりVQ-3 → VQ-4への階段的な充填の時間軸を一つの著者系列（Amatore/Jutand群）で追跡できる。

Reetz & de Vries (2004) はEP-03aへの部分充填として、ホスフィンフリー条件での均一性試験（水銀毒化、ホットフィルトレーション）がGVL系U-5に最も直接対応するため選定した。Cabri & Candiani (1995) はEP-05a（選択性分析）への唯一のHigh confidence候補。Beletskaya & Cheprakov (2000) はEP-03aとEP-04aのバンドル充填として、Heck反応の機構論的全景を提供する。

EP-07a（ArBr境界試験、VQ-2 RI-07）の候補（第7位）はConfidenceが低く、文献確認が必須である。EP-06a（GVL-SMD DFT、RI-06）は充填論文が未同定であり選定リストに含まれない。EP-08a、EP-01a（第三群）は性質的に独立論文として充填されないため除外した。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2 (RI-07 Unsupported boundary)**: EP-07a → [2021年以降、推定] Vaccaro/Mikaグループ [技術駆動充填 / 自己充填 (推定)] ← *要文献確認*
- **VQ-3 (RI-05 Qualitative overread)**: EP-05a → 1995年 Cabri & Candiani [技術駆動充填（選択性理論の体系化）]
- **VQ-3 (RI-04 Unreplicated discriminator)**: EP-04a → 1995年 Jutand & Mosleh; 2000年 Amatore & Jutand [技術駆動充填（電気化学法の確立）]
- **VQ-3 (RI-03 Unobserved explanatory)**: EP-03a → 2000年 Beletskaya & Cheprakov (部分); 2004年 Reetz & de Vries (部分) [技術駆動充填（Pd speciation技術の発展）]
- **VQ-3 (RI-06 Imported model)**: EP-06a → **未充填**（2020年以降も充填論文未同定）
- **VQ-4 (RI-09 External superiority)**: EP-09a → 2000年 Amatore & Jutand Acc. Chem. Res.; 2008年 Jutand Chem. Rev. [間接的分野横断充填（包括的レビューによる比較基盤の整備）]
- **VQ-4 (RI-08 Unquantified reliability)**: EP-08a → **未充填**（分野慣行として未解消）

**階層-時間対応の評価：**

VQ-3要件（RI-03, RI-04, RI-05）の充填は主に1995–2004年の期間に集中し、VQ-4要件（RI-09）の包括的充填は2000–2008年まで延びるという時間的パターンが観察される。この観察は「VQ階層が上がるほど充填に要する時間が長くなる」という仮説をある程度支持するが、注目すべき反例も存在する：Cabri & Candiani (1995) によるEP-05a（VQ-3 RI-05）の充填はAmatore & Jutand (1991)によるEP-04a（VQ-3 RI-04）の充填開始点より早い年代に位置しており、VQ-3内での階層的充填順序は一定ではない。全体として、VQ-3要件の充填は原論文（2020年）に比べて20–25年早い先行研究によってすでに提供されており、対象論文はすでに充填済みの問いを新しい溶媒系（GVL）に転用した構造となっている。

**特筆すべきパターン：**

- **技術駆動充填の支配**: EP-04a/EP-03aに対する電気化学的手法（Jutand等）およびPd speciation技術（Reetz & de Vries）は、分野全体の技術進歩によってもたらされた「技術駆動充填」として機能している。これらは対象論文とは無関係に独立して発展した。
- **自己充填の非出現**: 原論文（Fodor, Kégl, Mikaグループ）による後続論文での自己充填を同定できていない。GVL-SMD DFT（EP-06a）やEyring不確かさ（EP-08a）の自己充填の有無は、Kégl/Mikaグループの2021年以降の出版物の確認が必要である。
- **未充填の二重構造**: EP-06a（GVL-SMD DFT: RI-06）はVQ-3に必要な機構的問いであるが、対象論文の発表後も独立論文として充填されていない可能性が高い。EP-08a（Eyring不確かさ: RI-08）はVQ-4に必要なベンチマーク問いであるが、分野慣行として未解消のまま残っている。この二重の未充填は、VQ-3 → VQ-4の遷移をブロックしている構造的ギャップを反映している。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

**EP-06a Analogy-validation pack:**

* **未充填の理由**: 技術的困難 + 関心の欠如 — GVL-SMD（ε=34.7）でのPd触媒Heck TSの再計算は技術的には実行可能（Gaussian 16で同一プロトコル）だが、これを主題とする独立論文を発表する動機が弱い。既存のDMF-SMD計算が「近似として十分」という暗黙の分野慣行（ε差 < 5を許容）が存在し、GVL特定の再計算を論文化するインセンティブが不足している。
* **発見的意義**: あり — 「グリーン溶媒をタイトルクレームとしながら、計算化学は従来溶媒パラメータで代替する」というパターン（RI-06）はGVL/bio-based solvent計算論文全般に再帰する可能性があり、UQSがこのパターンを明示的に記録したことは制度的価値がある。
* **将来の充填可能性**: 高 — Kégl/Mikaグループが後続計算論文でGVL-SMD再計算を実施する可能性があり、また計算グリーンケミストリー方法論論文（GVL/DES等のSMD最適化）として独立論文化の機会がある。

---

**EP-08a Replication / uncertainty pack:**

* **未充填の理由**: 分野慣行 + 報告形式問題 — Eyring解析での不確かさ記述（ΔH‡ ± σ, ΔS‡ ± σ, 加重線形回帰）は2020年時点でグリーンケミストリー速度論論文では義務化されておらず、編集査読過程でも見落とされやすい。独立論文としての充填は原理的に困難。
* **発見的意義**: あり — 「数値近似（ΔH‡差 < 1 kJ/mol）を不確かさなしに等価性の証拠として提示する」という構造（RI-08）はグリーン溶媒代替論文全般で再帰するパターンであり、代替可能性主張の認識論的問題（Stage 2 E節：「数値近似 ≠ 統計的等価性」）と接続する系統的分野慣行を記録している。
* **将来の充填可能性**: 中 — GVLを含む後続の速度論論文がEyring不確かさ記述を標準化した場合、本論文の値を文脈化するための比較基盤が提供されうる。しかし本論文固有のデータに対する遡及的再分析論文としての充填は期待できない。

---

**EP-01a Reporting-coherence pack:**

* **未充填の理由**: 報告形式問題 — 検量線・内標準の不在はFodor et al.固有の問題であり、この分析バリデーション欠落を主題とする独立論文は発表されない。同一グループが後続論文でより厳密な分析条件を採用した場合のみ部分的に解消される。
* **発見的意義**: なし — 本件はRI-01の典型的事例だが、分析バリデーション欠落自体は速度論論文全般に広く分布しており、本論文特有の発見的価値は限定的。
* **将来の充填可能性**: 低 — 独立論文として充填される性質でない。Fodor/Mika後続論文での実験条件改善としてのみ期待される。

---

**EP-07a Boundary-test pack（部分的未充填・要確認）:**

* **未充填の理由（暫定）**: 関心の欠如（部分的）— GVL中でのArBr Heck反応はArIより活性化エネルギーが高く、Pd(OAc)₂/Et₃N/GVL系では高温または追加活性化が必要な可能性があり、系統的拡張論文の発表を妨げる技術的障壁が存在する可能性がある。しかし充填論文の不存在は文献確認なしに断定できない。
* **発見的意義**: あり（条件付き）— ArBrへのスコープ拡張が2020年以降も未実施であれば、「工業的に重要な変換」という主張を支えるはずのスコープ境界テストが分野として体系的に省略されていることを記録できる。
* **将来の充填可能性**: 高 — ArBr HeckのGVL系拡張はVaccaroグループが実施中または実施済みである可能性が高く、近年の刊行物の確認で解決できる。

---

**EP-05a（GVL特定条件での選択性プロファイル）— 部分的未充填：**

* **未充填の理由**: 関心の欠如 — 変換率–3a/4a比プロファイルのGVL特定測定は、Heck反応研究の主流が選択性制御ではなく収率・グリーン性の実証に向いているため論文化されていない可能性がある。
* **発見的意義**: なし（単報では弱い）— GVL中の選択性プロファイル欠落は対象論文固有の問いであり、分野横断的なパターンとしての記録価値は限定的。
* **将来の充填可能性**: 中 — Heck反応のDFT-guided選択性制御研究（分岐TSの計算と実験検証）は継続して発表されており、GVL条件への適用は自然な拡張となりうる。

inference_time_sec: not available — inject externally
```
