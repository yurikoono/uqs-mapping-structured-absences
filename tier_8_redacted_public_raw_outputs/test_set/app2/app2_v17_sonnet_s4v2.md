```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Meck, Omer et al. 2025（Journal of the American Chemical Society, Communication）

### §A EP充填難易度の三群分類

Stage 3 §5に列挙されたEP（EP-01a, EP-03a, EP-04a, EP-05a, EP-06a, EP-07a, EP-08a, EP-09a）を三群に分類する。

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a, EP-09a

- EP-03a: Pd-N酸化的付加体・パラジウサイクル中間体の分光学的同定は「Pd/N-O基質の化学」として独立研究の主題になりうる（関連系でのPd-N中間体同定論文が複数存在する）。RI-03は実験型EPとして文献で追跡可能。
- EP-06a: 同位体標識（²H）またはHammett解析によるaza-Heck/carbo-Heck類推の検証は、asymmetric Heck mechanismの独立論文として頻出する実験パターン。RI-06に対応する類似系での先行論文が存在する。
- EP-09a: Atkinson 2015（ref 27）およびArchambeau 2024（ref 9）との比較表作成は、Watson群の自己充填（Full Paper）または外部グループの条件比較研究として検索可能。RI-09はベンチマーク比較として独立論文に現れやすい。

**第二群（間接的に追跡可能）：** EP-04a, EP-07a

- EP-04a: aza-Wacker経路 vs. aza-Heck経路の時系列SFC監視やNLE試験は、機構論文の一部として現れることが多いが、単独論文の主題として独立発表される事例も存在する（Stahl群の競合経路解析論文等）。RI-04の充填は間接的にも確認可能。
- EP-07a: N置換基・ハロゲン系列の境界試験は通常、原著者グループのFull Paperまたはスコープ拡張論文として発表される。Watson群の先行aza-Heck論文（Shuler 2016, Xu 2018）が類似系での部分充填候補。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-05a, EP-08a

- EP-01a: 報告形式の改善（ee決定条件の全開示、収率基盤の明示）はFull Paper遷移での自動解消を主要経路とし、独立論文として発表される性質ではない。RI-01に対応する充填論文は実質的に「Watson群のFull Paper」のみ。
- EP-05a: 「pharmaceutically relevantヒダントインの定量的スコープ評価」は、医薬品化学における応用研究として断片的に現れることはあるが、このEPの要件（本法の排除する薬剤構造クラスの定量化）を直接主題とする独立論文は存在しない可能性が高い。RI-05の充填は分野の慣行として回避されやすい。
- EP-08a: グラムスケール最適化と最終生成物eeの確認は、原著者グループの後続論文（Full Paper）での自動解消候補だが、独立した論文として発表されることはまれ。RI-08はFull Paper遷移型自動解消パターンに該当。

---

### §B 各EPの充填論文候補

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Shuler, Yin, Krause, Vesper, Watson. *J. Am. Chem. Soc.* **2016**, *138*, 13830–13833 — Watson群による最初のaza-Heck反応論文（ラクタム合成）；Pd-N中間体の直接観測はないが、N-OPh基質からのPd(0)によるN-O酸化的付加を「提案する」という記述様式でaza-Heckサイクルを初めて定式化した先行論文として充填開始点に相当する（Partial/Indirect）。
* **充填確立点**: **未同定** — Pd(0)/キラルリガンド/N-O基質から生成するPd-N酸化的付加体を、NMRまたはX線回折で直接同定した独立論文は、2026年4月時点で著者の知識の範囲では確認できない。Watson群の後続機構論文（"currently ongoing"として言及）が充填確立点となる見込みだが未発表。
* **充填の性質**: Indirect（Shuler 2016）→ 未確立（確立点未同定）
* **Confidence**: Medium（Shuler 2016の存在は確実；充填確立点については Low）
* **注記**: 関連するPd-N中間体同定の先行研究として、Pd(0)による活性化N-O基質のOA体同定を試みた論文が期待されるが、本系（Pd/phosphoramidite/N-O/BuCN条件）に固有の試験は、"ongoing computational studies"として先送りされた機構研究の一部として自己充填される可能性が最も高い。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]
* **充填開始点**: Race, Faulkner, Fumagalli, Bower et al. *Chem. Sci.* **2017**, *8*, 1981–1985 — Bower群による最初の不斉aza-Heck（オキシム基質、N-C結合形成）；この論文はaza-Heck/carbo-Heck類推の実験的根拠として、同位体標識ではなく立体化学的解析によりsyn挿入→syn β-ヒドリド脱離を間接的に支持する最初の論文として位置づけられる（Indirect）。
* **充填確立点**: **未同定** — ²Hラベル化アルケン基質または動力学同位体効果を用いてaza-HeckのN-O基質に対するsyn挿入を直接実証した論文は確認できない。Hammett解析によるaza-Heck電子効果の研究も現時点では未発表と推定。
* **充填の性質**: Indirect（Race 2017）
* **Confidence**: Medium（Race 2017は確実に存在；充填確立点は Low）
* **注記**: Ma, Hazelden, Bower et al. *J. Am. Chem. Soc.* **2019**, *141*, 3356–3360も、不斉aza-Heck（N-tosyloxycarbamates）の立体化学的分析を含む充填候補として記録するが、N-O基質の種類が異なるため類似系充填（Indirect）として分類。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: Thomas, Nagamalla, Sathyamoorthi. *Chem. Sci.* **2020**, *11*, 8073–8088 — aza-Wacker反応の機構的特徴に関する総合的論文（ref 24e）；この論文はaza-Wacker/aza-Heck競合経路の一般的な区別法を提供するが、EP-04aが要求する本系固有の時系列SFC監視やNLE試験は含まない（Indirect）。
* **充填確立点**: **未同定** — Watson系（Pd(OAc)₂/L1/N-OPh基質）に対するNLE試験（配位子ee対生成物ee相関）を実施した論文は確認できない。時系列SFC監視（[5] vs. [26] のee追跡）も未発表と推定。
* **充填の性質**: Indirect（Thomas 2020）
* **Confidence**: Medium（Thomas 2020は確実；充填確立点は Low）
* **注記**: Trend, Ramtohul, Stoltz. *J. Am. Chem. Soc.* **2005**, *127*, 17778–17788（ref 24b; oxypalladationの立体化学研究）も、Wacker vs. Heck経路の識別実験の先行例として部分的充填候補。ただしaza-Heck/aza-Wacker競合の定量的時系列分析ではなくメカニズムの立体化学的解析として実施されており、EP-04aの直接充填には至らない。

---

**EP-05a [Quantitative-ranking substantiation pack]（第三群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: **未同定** — 本法で合成可能な/不可能な「pharmaceutically relevant quaternary hydantoin」の構造クラスを定量的に評価した論文は存在しない。Villaescusa, Oiarbide et al. *J. Org. Chem.* **2023**, *88*, 972–987（ref 6a; Michael付加による四級ヒダントイン合成）は医薬品関連ヒダントインを合成対象として含むが、Watson法との系統的スコープ比較は行っていない。
* **充填確立点**: 未同定
* **充填の性質**: 未同定
* **Confidence**: Low
* **注記**: この種の定量的スコープ評価は「独立論文として発表する新規性がない」ため、インセンティブ構造上発表されにくい（§E参照）。

---

**EP-07a [Boundary-test pack]（第二群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Xu, Shuler, Watson. *Angew. Chem. Int. Ed.* **2018**, *57*, 12081–12085 — Watson群によるN-H型イミダゾリジノン・ジヒドロイミダゾロンへの不斉aza-Heck（N-OPh基質）；この論文はN-H基質の反応性をN置換体と比較した最初の系統的データを含み、N置換効果の境界試験として部分充填候補（Indirect）。ただしヒダントインではなくイミダゾリジノン骨格が対象。
* **充填確立点**: **未同定** — ヒダントイン基質に対するN-置換基系列（Me/Et/Cy/Ph/N,N-ジアルキル）およびハロゲン系列（F/Cl/Br/I）の系統的境界試験を実施した論文は現時点では確認できない。Watson群のFull Paperが充填確立点となる見込みだが未発表。
* **充填の性質**: Indirect（Xu 2018）
* **Confidence**: Medium（Xu 2018は確実；充填確立点は Low）
* **注記**: CLA-1（L9一般性試験）も本EP-07aの延長線上にあり、L9 vs. L1の系統的比較もFull Paperでの自己充填として最も期待される。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定** — グラムスケール収率急落（化合物6: 78% → 31%）の原因分析と最終生成物(R)-メフェニトイン（化合物30）のee確認を実施した論文は現時点では確認できない。Watson群のFull PaperまたはSI補遺が最初の充填点となる見込み。
* **充填確立点**: 未同定（自己充填予定）
* **充填の性質**: 未同定
* **Confidence**: Low（内容の存在は高確率で予測されるが、論文として未発表）
* **注記**: JACS CommunicationのSI（ref 16）にグラムスケール条件の詳細が一部含まれている可能性があるが、31%収率の原因分析は含まれないと推定。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点（比較対象論文の同定）**: Atkinson, Fernández-Nieto, Mas Roselló, Clayden. *Angew. Chem. Int. Ed.* **2015**, *54*, 8961–8965（ref 27） — (R)-メフェニトインの唯一の既存不斉合成（擬エフェドリン補助基使用）；Watson 2025との比較のための基準点として存在するが、Watson論文自身がこの比較を数値的に実施していないため、EP-09aはこの論文「が充填する」のではなく「が充填されるべき対象を提供する」という位置づけ。
* **充填開始点（EP実際の充填として）**: **未同定** — Watson法 vs. Atkinson法の工程数・収率・ee・触媒量の数値比較を実施した論文は現時点では確認できない。Watson群のFull Paperが自己充填候補。
* **充填確立点**: 未同定
* **充填の性質**: 未同定（Atkinson 2015はEP-09aの「対象」であり「充填論文」ではない）
* **Confidence**: Low（充填論文が存在しないという意味でのLow；Atkinson 2015の存在はHigh）
* **注記**: Archambeau群の論文（Busicchia et al. *J. Org. Chem.* **2024**, *89*, 12370–12377; ref 9）はWatson法との比較基準として機能しうるが、同様に「比較対象論文」であって「充填論文」ではない。EP-09aの直接充填は、Watson群のFull Paperまたはhydantoin合成法の比較研究（第三者による）として期待される。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]（SRG-3, SRG-4, SRG-6に分散）
* **充填開始点**: Watson群のFull Paper（未発表） — SRG-4（ee決定条件の全開示、収率基盤の化合物別明示）、SRG-3（21化合物での副生物量報告）、SRG-6（全48配位子スクリーニング表）はいずれもFull Paper展開で自動解消されることが高確率で予測される。
* **充填確立点**: 未同定（Watson群のFull Paper）
* **充填の性質**: 未同定
* **Confidence**: Low（論文として未発表）
* **注記**: EP-01aの充填はFull Paper遷移の「自動解消パターン」（§6参照）に該当し、Watson群の後続論文以外での充填は期待できない。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Atkinson, Fernández-Nieto, Mas Roselló, Clayden. *Angew. Chem. Int. Ed.* 2015, 54, 8961 | EP-09a（対象提供） | VQ-4 | 2015 | High |
| 2 | Shuler, Yin, Krause, Vesper, Watson. *J. Am. Chem. Soc.* 2016, 138, 13830 | EP-03a（Indirect）, EP-07a（Indirect） | VQ-3/VQ-2 | 2016 | Medium |
| 3 | Race, Faulkner, Fumagalli, Bower et al. *Chem. Sci.* 2017, 8, 1981 | EP-06a（Indirect） | VQ-3 | 2017 | Medium |
| 4 | Xu, Shuler, Watson. *Angew. Chem. Int. Ed.* 2018, 57, 12081 | EP-07a（Indirect） | VQ-2 | 2018 | Medium |
| 5 | Thomas, Nagamalla, Sathyamoorthi. *Chem. Sci.* 2020, 11, 8073 | EP-04a（Indirect） | VQ-3 | 2020 | Medium |
| 6 | Busicchia, Archambeau et al. *J. Org. Chem.* 2024, 89, 12370 | EP-09a（対象提供）, EP-07a（Indirect） | VQ-4/VQ-2 | 2024 | High |
| 7 | Watson群Full Paper（未発表、2026〜予定） | EP-01a, EP-07a, EP-08a, EP-09a（自己充填） | VQ-2〜VQ-4 | 未定 | Low |

**選定理由：**
推奨リストの中核は、Watson群の先行aza-Heck論文（Shuler 2016, Xu 2018）と競合グループの不斉aza-Heck論文（Race/Bower 2017）の3報であり、これらがEP-03a・EP-06a・EP-07aの間接充填として最大のカバレッジを持つ。Thomas 2020はaza-Wacker経路の機構論文としてEP-04aを間接的に充填する唯一の独立論文候補。Atkinson 2015とArchambeau 2024は充填論文ではなく「充填のための比較基準論文」として特別枠で選定した。Watson群のFull Paper（未発表）は確信度が低いものの、EP-01a/EP-07a/EP-08a/EP-09aの決定的充填として最重要であるため参考として含めた。

本論文が2025年11月発表（2026年4月の本分析時点では発表から約5ヶ月）という時間的制約が、充填論文の不在の主因である。ほぼ全てのEPが「未同定」または「Indirect」にとどまる状況は、論文の新規性（先行研究が存在しない領域）を逆説的に証明している。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件（RI-07）: EP-07a → 2016年〜 (Shuler, Watson; Indirect) / 2018年〜 (Xu, Watson; Indirect) — N置換基効果の部分データは先行Watson論文に散在するが、ヒダントイン系に対する系統的境界試験は未充填。
- VQ-2 要件（RI-01）: EP-01a → 未充填（Full Paper遷移での自動解消待ち）
- VQ-3 要件（RI-03）: EP-03a → 2016年〜 (Shuler 2016; Indirect) — Pd-N中間体の直接観測は未充填。
- VQ-3 要件（RI-04）: EP-04a → 2020年〜 (Thomas 2020; Indirect) — 本系固有の時系列SFC監視・NLE試験は未充填。
- VQ-3 要件（RI-06）: EP-06a → 2017年〜 (Race 2017; Indirect) — ²H標識実験またはHammett解析は未充填。
- VQ-4 要件（RI-08）: EP-08a → 未充填（自己充填待ち）
- VQ-4 要件（RI-09）: EP-09a → 比較対象論文（Atkinson 2015, Archambeau 2024）は存在するが、頭-to-頭比較研究は未充填。

**階層-時間対応の評価：**
本論文が2025年末発表という新しさから、全EPが実質的に未充填という状況は、VQ階層による充填難易度の差異を評価するには時間が短すぎる。ただし間接充填の時間軸を見ると、VQ-2要件（EP-07a）はWatson群の先行論文（2016, 2018）により部分的に先取り充填されており、VQ-3要件（EP-03a, EP-04a, EP-06a）はより専門的な機構論文（2017, 2020）が間接充填候補となっている。この傾向は「VQ階層が上がるほど充填に要する時間が長くなる」という仮説を弱く支持する。

**特筆すべきパターン：**
1. **VQ逆転パターンの予兆**: 低VQ要件（EP-01a: RI-01、EP-08a: RI-08）は「Full Paper自動解消」として最も早く解消される一方、高VQ要件（EP-03a: RI-03）は「機構研究」として最も遅い充填を要する。これはVQ階層-充填時間の仮説を支持する。
2. **自己充填の中心性**: 充填の主要経路として「Watson群のFull Paper」が全EP-01a/EP-07a/EP-08a/EP-09aをバンドル充填する構造になっている。このパターンは通信→Full Paper遷移型自己充填の典型例。
3. **遡及的間接充填**: EP-07a（境界試験）はWatson群自身の先行aza-Heck論文（Shuler 2016, Xu 2018）が「同一グループによる関連系での部分充填」として最早の充填候補となっており、原論文より前から存在する「遡及的間接充填」という特殊パターンを形成している。
4. **技術駆動充填の予測**: A-01（立体誘導の計算先送り）に対応するEP-03aの充填確立点として最も期待されるのは「DFT計算による遷移状態構造解析」であり、計算化学技術の発展が充填の駆動力となる「技術駆動充填」パターンと予測される。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-01a [Reporting-coherence pack]（第三群）:**
* **未充填の理由**: 報告形式問題（RI-01）に起因するため独立論文として充填される性質ではない（通信→Full Paper遷移での自動解消パターン）。充填に必要な情報（全21化合物のSFC条件、収率基盤）はWatson群のFull PaperまたはSI改訂によって解消される。
* **発見的意義**: なし（報告形式問題は分野慣行の範囲内であり、構造的に新しい問いを生成しない）。
* **将来の充填可能性**: 高（Watson群のFull Paper公表が充填の主要経路；技術的困難なし）。

**EP-03a [Direct-observation / state-assignment pack]（第一群）:**
* **未充填の理由**: 技術的実現可能性とインセンティブの組み合わせ問題。Pd(0)/chiral phosphoramidite/N-O基質から生成するPd-N酸化的付加体の単離・同定は実験的に実現可能であるが、Watson群が"ongoing"と述べた計算研究が先行しており、実験的中間体同定の独立論文としてのインセンティブが機構研究全体の中で後回しにされている可能性がある。
* **発見的意義**: あり — 「触媒サイクルを提案するが中間体を探索しない」というパターンが2025年のJACS Communicationで維持されていることは、不斉Pd触媒分野が機構的検証を完全に先送りすることを許容する査読慣行の現れとして記録できる。
* **将来の充填可能性**: 中（Watson群の後続機構論文として充填可能；計算研究が先行するため実験的充填は計算充填の後続になる可能性）。

**EP-04a [Discrimination / replication pack]（第二群）:**
* **未充填の理由**: インセンティブ構造の不整合。時系列SFC監視と外部添加ラセミ26実験は技術的に実行可能であるが、「aza-Wacker副生物26→5変換の速度」を定量する独立論文は新規性が低く出版されにくい。NLE試験も「既知の不斉Pd触媒系への適用」として独立論文になりにくい。
* **発見的意義**: あり — EP-04aが未充填のまま残ることは、機構的証拠として「排除的証拠（26がラセミ）」が「確認的証拠（NLE試験、時系列監視）」よりも軽い実験負担で受容される分野慣行の直接証拠として記録できる。
* **将来の充填可能性**: 中（Watson群のFull PaperまたはWatson群の機構論文で自己充填される可能性が最も高い）。

**EP-05a [Quantitative-ranking substantiation pack]（第三群）:**
* **未充填の理由**: インセンティブ構造の不整合と関心の欠如。「この合成法が医薬品として重要なヒダントインの何%をカバーするか」を定量する研究は、薬剤開発と合成方法論の境界に位置し、いずれのコミュニティからも独立論文としての評価を受けにくい。
* **発見的意義**: あり — 「pharmaceutically relevant」という形容詞が定量的裏付けなしに繰り返し許容される分野慣行は、RI-05（Qualitative overread）が不斉合成論文全般において系統的に維持されていることの証拠として記録できる。UQSが抽出した「医薬品関連性の定量的評価」という問いは、2026年4月時点で分野が集団的に回避してきた問いである。
* **将来の充填可能性**: 低（この種の定量的評価を独立論文として発表する動機が分野に存在しないため）。

**EP-07a [Boundary-test pack]（第二群）:**
* **未充填の理由**: 原著者グループの自己充填（Full Paper）待ち。技術的困難は低いが、N置換基系列・ハロゲン系列の系統的境界試験はFull Paperの「拡張スコープ」部分として通常実施されるため、独立論文として先行発表されるインセンティブが低い。
* **発見的意義**: なし（通常の通信→Full Paper遷移プロセスの範囲内）。
* **将来の充填可能性**: 高（Watson群のFull Paperでの自己充填が最も確実な経路）。

**EP-08a [Replication / uncertainty pack]（第三群）:**
* **未充填の理由**: 報告形式問題とFull Paper自動解消パターン。グラムスケール最適化と最終生成物eeの確認は実験的に容易であるが、独立論文として発表する新規性が存在しない。
* **発見的意義**: なし（EP-01aと同様に報告慣行問題の範囲内）。
* **将来の充填可能性**: 高（Watson群のFull Paperまたは後続のmephenytoin応用研究で自己充填される）。

**EP-09a [Internal benchmark pack]（第一群）:**
* **未充填の理由**: インセンティブ構造の不整合と原著者グループの先送り。Watson法 vs. Atkinson法の頭-to-頭比較は、両論文とも既に独立発表されているため「比較のための独立論文」を発表するインセンティブが低い。Watson群のFull Paperで自己充填されるか、第三者によるヒダントイン合成法比較研究で部分充填される可能性がある。
* **発見的意義**: あり — 「最初の不斉合成」という主張が数値比較なしに許容される慣行は、RI-09（External superiority）が不斉合成論文の通信形式で系統的に維持されていることの証拠として記録できる。優位性の主張が定性的言語（「prior approach employed a chiral-auxiliary approach」）で維持されることが、UQSの解析で繰り返し確認されるパターンであることを付記する。
* **将来の充填可能性**: 中（Watson群のFull Paperでの自己充填が最も確実だが、頭-to-頭比較が含まれるかどうかは不明）。

**総括：VQ逆転パターンの診断**
本ケースでは、低VQ要件（EP-01a: RI-01, EP-08a: RI-08）が「Full Paper自動解消」として最も早期に解消されることが予測され、高VQ要件（EP-03a: RI-03, EP-06a: RI-06）が機構研究として最も遅い充填を要する。一方、EP-05a（VQ-2のRI-05要件）は「難易度が低い（技術的には容易）にもかかわらず、インセンティブがないため永続的に未充填のまま残る」というパターンとして記録される。これは「科学的論理に基づくEP充填順序（低VQ→高VQ）」と「出版インセンティブに基づく実際の充填順序（高VQ→低VQ）」の逆転として、UQSの分野診断における重要な発見として位置づけられる。

inference_time_sec: not available — inject externally
```
