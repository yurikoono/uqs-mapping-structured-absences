```
prompt_version: stage4-v2
model_info: Claude Opus 4.8 (current; note: Kumada study used Opus 4.7)
experimental_variant: "Murai cross-vendor multi-run opus48 v2 run 3"
date: 2026-06-12
```

# EP充填選定マップ

## Murai et al. 1993（Nature, communication）（Efficient catalytic addition of aromatic carbon–hydrogen bonds to olefins）

---

### §A EP充填難易度の三群分類

Stage 3 §5に列挙された全EP（EP-01a, EP-03a, EP-04a, EP-05a, EP-06a, EP-07a, EP-08a, EP-09a）を充填論文の検出しやすさで三群に分類する。

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a

— **EP-03a**（Direct-observation / state-assignment, RI-03）: Murai/Chatani/Kakiuchi グループおよび競合グループが、Ru-H(CO)(PPh₃)系の機構を独立した機構論文（速度論・分光・中間体観測）の主題として発表しており、文献検索で直接ヒットしうる。
— **EP-04a**（Discrimination / replication, RI-04）: C–H切断の律速性を判定するKIE測定・重水素標識実験は、本系の機構論文の中心的話題として独立に発表されている。
— **EP-06a**（Analogy-validation, RI-06）: シクロメタル化中間体・Ru(0)活性種のモデル化学量論反応は有機金属化学の独立した研究主題であり追跡可能。
— **EP-07a**（Boundary-test, RI-07）: directing-group・tether長・5員/6員環依存性の境界探索は、scope拡張論文（芳香族ケトン以外の directing group への展開）として大量に独立発表されている。

**第二群（間接的に追跡可能）：** EP-05a, EP-09a

— **EP-05a**（Quantitative-ranking substantiation, RI-05）: 位置選択性の速度論的/熱力学的起源の定量判別は、本系特化の機構論文の一部として含まれるが、選択性起源のみを主題とする独立論文は限定的。
— **EP-09a**（Internal benchmark, RI-09）: TOF・先行研究との同一軸数値比較は review・総説・full paper の比較表として含まれるが、ベンチマーク比較自体を主題とする独立論文は稀。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a

— **EP-01a**（Reporting-coherence, RI-01）: GC校正プロトコル・応答係数の明示は、Murai系のフルペーパー（Bull. Chem. Soc. Jpn. 等の続報）への展開で部分自動解消される性質であり、独立論文の主題にはならない。
— **EP-08a**（Replication / uncertainty, RI-08）: 13例の3重複・SD提示は新規性を要求する出版慣行下では独立論文化されにくく、フルペーパーの実験項に吸収される。

---

### §B 各EPの充填論文候補

---

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: Kakiuchi, F. & Murai, S. et al.（Murai グループの続報 full paper 群、1990s後半〜2000s）— Bull. Chem. Soc. Jpn. / Chem. Lett. 系の続報で単離収率・実験条件の詳細が記載され、通信→full paper 遷移により部分解消。
* **充填確立点**: 同上（特定の単一論文として decisive な充填は同定困難）
* **充填の性質**: Partial
* **Confidence**: Low
* **注記**: RI-01 はジャンル慣行上 full paper 展開で自動解消される性質であり、特定論文を decisive filling として固有同定する確信は低い。Murai グループの続報群が条件・収率の詳細化を担ったと推測されるが、書誌的に特定の1報を確信を持って指せない。

---

**EP-03a Direct-observation / state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点**: Kakiuchi, F.; Murai, S. et al.（機構研究、1990s後半）— Ru-H(CO)(PPh₃)系のC–H切断機構について速度論・標識実験を報告。
* **充填確立点**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K., *Organometallics* 2000, 19, 2318（DFT 計算による Murai 反応触媒サイクルの理論的解明）— Ru(0)活性種・シクロメタル化中間体・オレフィン挿入経路を計算化学で帰属し、提案された未観測中間体を理論的に拘束。
* **充填の性質**: Partial（計算による拘束。直接観測ではないが、未観測種の状態帰属を理論で補完）
* **Confidence**: Medium
* **注記**: Morokuma グループが Murai 反応の機構を DFT で扱った理論論文を発表したことは確信があるが、正確な巻号・年（2000前後）の書誌詳細には推論を含む。EP-06a と相互参照（同じ機構サイクルの中間体検証）。

---

**EP-04a Discrimination / replication pack（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: Kakiuchi, F.; Murai, S. et al.（重水素標識・KIE 研究）— ortho-重水素化アセトフェノン等を用いた標識実験で C–H 切断の律速性と H/D スクランブリングを報告。
* **充填確立点**: 同上（Murai グループの機構論文群）
* **充填の性質**: Partial
* **Confidence**: Low
* **注記**: Murai/Kakiuchi グループが本反応の標識・KIE 実験を行った機構論文を発表したと recall するが、特定の書誌（雑誌・年・巻号）を確信を持って同定できない。M–H vs M–C 経路判別の decisive 論文の固有同定も不確実。

---

**EP-05a Quantitative-ranking substantiation pack（第二群）**

* **充填するRI**: RI-05 Qualitative overread
* **充填開始点**: Kakiuchi, F. & Murai, S.（選択性・基質効果の系統研究）— 電子的・立体的に変化させた基質系列で ortho 選択性を定量化した scope 論文。
* **充填確立点**: 未同定（選択性起源の速度論的/熱力学的判別を主題とする decisive な単一論文を確信を持って指せない）
* **充填の性質**: Partial
* **Confidence**: Low
* **注記**: 選択性の系統的定量化は Murai グループの後続 scope 論文に含まれると推測されるが、RI-05（定性的過読）を decisive に解消する固有論文の書誌特定はできない。

---

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K., *Organometallics* 2000, 19, 2318 — DFT による触媒サイクル全体の検証（輸入された有機金属モデルを本系で計算的に検証）。
* **充填確立点**: 同上
* **充填の性質**: Partial（計算的検証。シクロメタル化中間体の単離・分光同定は別途）
* **Confidence**: Medium
* **注記**: EP-03a と同一論文によるバンドル充填。Morokuma グループの Murai 反応 DFT 論文は recall に確信があるが書誌詳細に推論を含む。

---

**EP-07a Boundary-test pack（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Kakiuchi, F.; Sonoda, M.; Murai, S. et al.（directing-group 拡張 scope 論文群、1990s後半〜2000s）— アセトフェノン以外の directing group（エステル、イミン、アルデヒド、ニトリル等）および異なる tether 長への展開で chelation assistance の構造的境界を経験的に確定。
* **充填確立点**: Kakiuchi, F. & Murai, S., *Acc. Chem. Res.* 2002, 35, 826（"Catalytic C–H/Olefin Coupling"）— ただし review 性格のため一次充填でなく二次集約（注記参照）。一次充填は上記 scope 論文群。
* **充填の性質**: Partial
* **Confidence**: Low（一次 scope 論文の固有書誌）/ Medium（Acc. Chem. Res. review の存在）
* **注記**: Kakiuchi & Murai による Account（Acc. Chem. Res. 2002 前後）が本反応の scope・境界を集約したことは recall に比較的確信があるが、review はそれ自体は充填せず、境界実験を行った一次論文を集約する二次源である。一次充填 scope 論文の個別書誌は確信が低い。

---

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: （該当論文なし）
* **Confidence**: Low
* **注記**: 13例の3重複・SD 提示は独立論文化のインセンティブを欠き、Murai 系のフルペーパー実験項に吸収される性質。decisive な充填論文は構造的に存在しにくい。第三群典型。

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点**: 未同定（Jordan & Taylor 1989 / Moore et al. 1992 と同一軸での TOF 数値比較表を提示する decisive 論文を確信を持って指せない）
* **充填確立点**: 未同定
* **充填の性質**: （該当論文なし／review の比較表に部分的に含まれる可能性）
* **Confidence**: Low
* **注記**: ベンチマーク比較は review・総説の比較表に間接的に含まれうるが、review は新規実験証拠を提供せず充填しない。RI-09 を decisive に解消する独立論文は同定できない。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Matsubara, Koga, Musaev & Morokuma, *Organometallics* 2000, 19, 2318 | EP-03a, EP-06a | VQ-3 | 2000 | Medium |
| 2 | Kakiuchi & Murai, *Acc. Chem. Res.* 2002, 35, 826 (review; 二次集約) | EP-07a (間接) | VQ-2/VQ-3 | 2002 | Medium |

選定理由：本ケースは hallucination-measurement run であり、確信を持って固有書誌を recall できる充填論文が極めて限定的である。decisive な機構充填として唯一 Medium confidence で同定できるのは Morokuma グループの DFT 論文（Matsubara et al., *Organometallics* 2000）であり、これは EP-03a（未観測中間体の状態帰属）と EP-06a（輸入モデルの検証）を計算的にバンドル充填する。Kakiuchi & Murai の Account（*Acc. Chem. Res.* 2002）は review であり一次充填しないが、scope・境界（EP-07a）を集約する二次源として選定表に含め、その旨を明記する。

選定基準（Confidence: High > Medium、Low は原則除外）に厳密に従うと、High confidence の固有書誌が一つもないため、選定表は Medium confidence の2報のみとなる。EP-01a・EP-04a・EP-05a・EP-08a・EP-09a については、充填が起きた可能性は高いものの（特に Murai/Kakiuchi グループの続報・標識実験群）、特定の書誌を捏造せずに確信を持って同定することができないため、選定表から除外した。これは retrieval の浅さを正直に反映した結果である。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-3 要件: EP-03a → 2000 Matsubara/Morokuma [技術駆動充填（DFT 計算手法の成熟）]
- VQ-3 要件: EP-06a → 2000 Matsubara/Morokuma [技術駆動充填（同上、バンドル充填）]
- VQ-2/VQ-3 要件: EP-07a → 2002前後 Kakiuchi & Murai [自己充填（原著者グループの scope 拡張・Account による集約）]
- VQ-2 要件: EP-01a → 不確実（Murai グループ full paper 遷移で部分解消と推測、書誌特定不能）
- VQ-3 要件: EP-04a → 不確実（Murai/Kakiuchi 標識実験群、書誌特定不能）
- VQ-3 要件: EP-05a → 未同定
- VQ-4 要件: EP-09a → 未同定
- VQ-4 要件: EP-08a → 未充填（構造的）

**階層-時間対応の評価：**
「VQ階層が上がるほど充填に時間を要する」仮説について、本 run で確信を持って同定できたのは VQ-3 機構要件（EP-03a/06a）が1993→2000の約7年後に DFT 技術の成熟により充填されたという1点のみである。これは技術駆動充填の典型であり、機構（VQ-3）の充填が実験ではなく計算手法の登場を待ったという点で仮説と整合的に読めるが、n=1（しかも書誌に推論を含む）であり、階層-時間仮説の robust な検証には至らない。VQ-2 要件（EP-01a, 報告整合性）はジャンル慣行上 full paper 遷移で早期解消されたと推測され、これは「低VQ要件が早く充填される」方向の弱い傍証となるが、書誌特定できないため確証ではない。

**特筆すべきパターン：**
- **技術駆動充填（VQ-3）**: Morokuma グループの DFT 論文（2000）が EP-03a と EP-06a をバンドル充填。直接観測でなく計算による状態帰属で未観測中間体問題が前進した点が特徴的。原論文の機構「不明」宣言（B-3）が、7年後に実験ではなく理論計算で部分解消された。
- **自己充填（EP-07a）**: chelation assistance の境界探索は原著者グループ（Kakiuchi/Murai）自身が scope 拡張で担い、Account で集約した自己充填パターン。
- **retrieval の浅さ**: 本 run では8 EP中、Medium confidence で書誌同定できたのは実質1報（Morokuma DFT、EP-03a/06a をカバー）のみ。Murai/Kakiuchi グループが機構・KIE・scope の充填論文を多数発表したことは確信があるが、個別書誌を捏造せず recall する深さに達しなかった。これは hallucination-measurement の観点で正直に記録すべき retrieval depth の限界である。

---

### §E 未充填EPの発見的意義

**未充填EP一覧（本 run で充填論文を確信を持って同定できなかったもの）：**

EP-01a Reporting-coherence pack:
* **未充填の理由**: 報告形式問題（通信→full paper 遷移で部分解消されるが、GC校正・応答係数を decisive に明示する独立論文は同定できない）+ インセンティブ構造の不整合（校正手順の明示は独立論文化されない）。
* **発見的意義**: あり。GC収率の校正プロトコル明示が独立論文の主題にならず、full paper 実験項に吸収される構造は、「報告整合性の充填が書誌的に不可視化される」パターンを示す。
* **将来の充填可能性**: 中（技術的には容易だが、独立出版インセンティブを欠く）。

EP-04a Discrimination / replication pack:
* **未充填の理由**: 関心の欠如ではなく、本 run の retrieval 限界（Murai/Kakiuchi の標識・KIE 論文は実在すると確信するが書誌特定不能）。
* **発見的意義**: なし（充填は実際には起きたと推測され、未充填は分野の問題でなく retrieval の問題）。
* **将来の充填可能性**: 高（既に充填されている公算が大きい）。

EP-05a Quantitative-ranking substantiation pack:
* **未充填の理由**: 分野慣行（選択性起源の速度論的/熱力学的判別のみを主題とする独立論文は稀）+ retrieval 限界。
* **発見的意義**: あり（限定的）。選択性の構造的直観への帰因が定量判別実験で decisive に置換される論文が稀である点は、分野が選択性の「説明」に定量を要求しない慣行を示唆しうる。
* **将来の充填可能性**: 中。

EP-08a Replication / uncertainty pack:
* **未充填の理由**: インセンティブ構造の不整合（13例3重複・SD 提示は新規性を欠き独立論文化されない）。
* **発見的意義**: あり。反復測定・不確かさ定量が出版インセンティブ構造の下で構造的に論文化されないパターンの典型事例。
* **将来の充填可能性**: 低（技術的に容易だが出版動機が原理的に存在しない）。

EP-09a Internal benchmark pack:
* **未充填の理由**: インセンティブ構造の不整合（matched-pair ベンチマーク比較は新規性を要求する出版慣行下で論文化されにくい）+ retrieval 限界。
* **発見的意義**: あり。先行研究（Jordan & Taylor 1989 / Moore et al. 1992）との同一軸 TOF 比較が decisive に閉じられる独立論文を同定できない点は、優位性主張の数値的閉鎖が分野で構造的に回避されるパターンを示す。
* **将来の充填可能性**: 低〜中。

**VQ階層逆転の診断：**
本 run で Medium confidence で充填同定できたのは高VQ要件（EP-03a/06a, RI-03/RI-06, VQ-3 機構）であり、低VQ要件（EP-01a RI-01, EP-08a RI-08, EP-09a RI-09）はいずれも未同定または構造的未充填に留まった。これは Stage 4 v2 §E が予測する逆転パターン——「科学的論理に基づく充填順序（低VQ→高VQ）」と「実際の充填順序（高VQ→低VQ、機構論文・計算論文が先に出版される）」の逆転——と整合する。RI-08/RI-09（反復測定・ベンチマーク）が出版インセンティブを欠いて未充填のまま残り、RI-03/RI-06（機構）が DFT 技術駆動で充填された構造は、分野のインセンティブ構造が UQS の構造的不在の一部（定量信頼性層）を維持していることの証拠となる。

ただし本 run では retrieval の浅さ（低VQ要件の充填論文を捏造せず recall できなかったこと）が逆転パターンの観測に混入している点を注記する。逆転が分野構造によるものか retrieval bias によるものかは、本 run 単独では分離できない。
