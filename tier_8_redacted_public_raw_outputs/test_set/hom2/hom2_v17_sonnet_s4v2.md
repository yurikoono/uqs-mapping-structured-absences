```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Shirai et al. 2024（J. Org. Chem., Note）

### §A EP充填難易度の三群分類

Stage 3 §5に列挙された全EPを分類する。

**第一群（文献で明確に追跡可能）：EP-03a（SRG-7）、EP-07a（CLA-2）、EP-09a（SRG-4）**

- **EP-03a（SRG-7）**: CsF役割（fluoride activator vs Brønsted base）の分離実験は、Pd/フルオロシリカートのトランスメタル化機構という確立された独立研究領域を持つ（Hatanaka/Hiyama 1989, Sugiyama/Sakaki 2008が先行例）。独立論文の主題として存在する可能性が高い。
- **EP-07a（CLA-2）**: ArBr適用テスト・TEMPO添加によるラジカル排除・TON測定は、それぞれ独立したスコープ論文・機構論文として発表されやすい実験内容を持つ。Li/Gong/Song 2020（ArBr使用実績）、Hurst/Cook 2021（Pd/Si-H機構）が先行例として存在する。
- **EP-09a（SRG-4）**: Wang/Wu/Loh 2018をはじめとする先行手法論文が同基質系でのベースライン収率データを提供しており、直接比較のための参照点は存在する。独立論文による基質マッチド比較は将来論文で追跡可能。

**第二群（間接的に追跡可能）：EP-04a（SRG-3）、EP-03a（SRG-2）、EP-05a（SRG-8）**

- **EP-04a（SRG-3）**: AQ-directed Pd系の重水素標識実験は、Engle・Wu/Loh等の関連グループが実施した機構論文に部分的に含まれる可能性があるが、本論文の具体的な条件（PMHS/CsF）でのH/D交換コントロールという粒度での独立発表は限定的。
- **EP-03a（SRG-2）**: 添加速度条件依存の重水素実験は、本反応に固有の要件であり独立発表の主題にはなりにくいが、フロー化学・半回分式反応器における添加速度効果の機構論文として間接的に類似研究が存在しうる。
- **EP-05a（SRG-8）**: 反応速度プロファイルによるスコープ異常の機構的帰属は、Full Paper展開または関連機構論文の補助データとして含まれやすいが、本論文の異常（Thorpe-Ingold失敗・内部>末端逆転）に特化した独立論文は期待しにくい。

**第三群（充填が見つからない可能性あり）：EP-08a（SRG-1, CLA-1）、EP-01a（SRG-5）、EP-03a（SRG-6）**

- **EP-08a（SRG-1, CLA-1）**: 合成Noteでのreplicate欠如・内部標準安定性不確認はRI-01/RI-08に起因する報告形式問題であり、独立論文として充填される性質ではない。Full Paper展開時に自動解消されるか、分野慣行として未解消のまま残る。
- **EP-01a（SRG-5）**: Table 1訂正のchangelogは出版社・著者との手続き的対応によってのみ解消可能であり、独立した科学論文として充填されない。
- **EP-03a（SRG-6）**: PMHS量増加と副生成物収率の関係は本反応系に完全に固有であり、独立論文の主題になりにくい。Shirai/Kumamoto続報（自己充填）が最も現実的な解消経路。

---

### §B 各EPの充填論文候補

---

**EP-03a [Direct-observation / state-assignment pack]（SRG-7, 第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory] — CsF役割（fluoride activator vs Brønsted base）
* **充填開始点**: Hatanaka & Hiyama, *J. Org. Chem.* **1989**, *54*, 268–270 — フルオロシリカートがPd(II)とのトランスメタル化を促進することを最初に実験的に実証した（ビニルシラン/ArI系）。CsF添加によるフッ化物活性化の証明を提供。
* **充填確立点**: Sugiyama, Sakaki et al., *J. Am. Chem. Soc.* **2008**, *130*, 12975–12985 — フッ化物アニオンがビニルシラン-Pd(II)トランスメタル化を促進する理由を計算化学で詳解。五配位シリカートを経由した協奏的Si-C結合開裂機構を確立。
* **充填の性質**: Partial — fluoride activator機能（RI-03の一側面）は充填されているが、CsFのBrønsted base機能（pKaH of HF ~3.2）とprotodepalladationへの寄与は、これらの計算/実験（vinylsilane/vinylPd系）の直接的対象外。PMHS（ポリマーシラン）/アルキルPd系への外挿は実験的に未確認。
* **Confidence**: High（論文の存在と内容に確信あり。ただしPMHS/alkyl-Pd系への適用はIndirect）
* **注記**: 両論文はShirai 2024のrefs 39, 40として引用済み。充填論文として引用されているにもかかわらず、CsF役割の二機能分離（fluoride vs base）というEP-03aのcase-specific実装には対応する実験が本論文に存在しない——「引用あり・充填適用なし」という証拠的相補性の不活用パターン。

---

**EP-07a [Boundary-test pack]（CLA-2, 第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]（ArBr適用）+ RI-03（radical exclusion）

**（ArBr適用コンポーネント）**
* **充填開始点**: Li, Gong, Song, *Org. Chem. Front.* **2020**, *7*, 2216–2223 — AQ-directed reductive Heck反応においてArBr（およびArI）を3.0 equivで使用し、δ選択的ヒドロアリール化を達成（K2CO3, EtOH, 100°C）。ArBrがAQ-directed reductive Heckの基質として機能することを実証した。
* **充填確立点**: 同上
* **充填の性質**: Partial — AQ-directed系でのArBr適用可能性は示されているが、本論文のPMHS/CsF/r.t.条件下でのArBr適用可否は未検証。「AQ-directedでArBrは機能する」という先例は確立されているが、「PMHS/CsF/r.t.でもArBrが機能するか」は未充填。
* **Confidence**: High

**（ラジカル排除コンポーネント）**
* **充填開始点**: Hurst, Zakharov, Cook, *Chem. Sci.* **2021**, *12*, 13045–13060 — Pd(0)のSi-H結合への酸化付加機構（電子効果・反応機構・ヒドロシリル化）をFe/Pd触媒系で詳細に研究。イオン的メカニズム（協奏的Si-H酸化付加）対ラジカル経路の識別を含む。
* **充填確立点**: 同上
* **充填の性質**: Indirect — Pd/Si-H系でのイオン的vsラジカル経路の機構識別を一般的レベルで提供するが、本論文の具体的な系（Pd(OAc)2/PMHS/CsF/AcOEt, r.t.）でのTEMPO実験による確認ではない。
* **Confidence**: Medium
* **注記**: Shirai 2024のref 44として引用済み。充填はIndirectで、本論文の系への適用には実験的確認が必要。

---

**EP-09a [Internal benchmark pack]（SRG-4, 第一群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: Wang, Wu, Loh et al., *J. Am. Chem. Soc.* **2018**, *140*, 9332–9336 — AQ-directed reductive Heck hydroarylation of unactivated alkenes（amine hydride source, 130°C）を最初に報告。γ-arylated 58–97%, δ-arylated 41–86%の収率範囲を、aliphatic alkenes/aryl halides基質セットで確立。
* **充填確立点**: 未同定（基質マッチド直接比較が単一論文で実施されていない）
* **充填の性質**: Partial — Wang/Wu/Loh 2018はベースライン収率データを提供するが、Shirai 2024の条件と同一基質を並行実施した論文は存在しない。「収率範囲の外枠」は与えられているが「同一基質での直接比較」というEP-09aのcase-specific実装は未充填。
* **Confidence**: High（充填開始点の論文自体は確実に存在するが、EP-09aの完全充填は未確立）
* **注記**: インセンティブ構造の不整合（§E参照）：既存手法との直接収率比較は「新規性」を要求する出版慣行のもとで論文化されにくく、この特定のEPが埋まりにくい構造的理由がある。Shirai 2024自身がFull Paperとして続報を出せば自己充填が最も現実的な経路。

---

**EP-04a [Discrimination / replication pack]（SRG-3, 第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]（重水素取り込み精度 + H/D交換コントロール）
* **充填開始点**: Gurak, Engle, *ACS Catal.* **2018**, *8*, 8987–8992 — AQ-directed reductive Heck hydroarylation（Pd(OAc)2, PPh3, Zn粉末, Et3N条件）で機構的考察を含む。重水素実験を含む可能性があるが、H/D交換コントロールの実施は不確かである。
* **充填確立点**: 未同定
* **充填の性質**: Attempted（充填の方向には向かっているが、EP-04aの具体的要件——H/D交換コントロール + 反復2H NMR定量——を満たすかどうか未確認）
* **Confidence**: Low（論文の存在は確信があるが、EP充填との対応に推論が必要であり、実際の文献確認が必要）
* **注記**: Shirai/Kumamoto グループによる自己充填（Full Paper続報）が最も現実的な充填経路。本稿執筆時点（2026年4月）で後続論文は未認識。

---

**EP-03a [Direct-observation / state-assignment pack]（SRG-2, 第二群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（条件依存重水素実験：速い添加 vs 遅い添加でのδ位D取り込み比較）
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: — （現時点での充填論文候補なし）
* **Confidence**: — （N/A）
* **注記**: この実験（速い添加条件下での重水素実験）はShirai 2024の反応系に固有であり、他グループが行うインセンティブが存在しない。「二重触媒サイクルモデルが予測するδ-D増加」という内部的予測の検証は、自己充填（Shirai/Kumamoto続報）によって初めて実施されると予想される。§E参照。

---

**EP-03a [Direct-observation / state-assignment pack]（SRG-6, 第三群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（PMHS増量条件下での副生成物収率）
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: — （第三群）
* **Confidence**: — （N/A）
* **注記**: 本系に固有。自己充填経路のみ。§E参照。

---

**EP-08a [Replication / uncertainty pack]（SRG-1, CLA-1, 第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定**（独立論文として充填される性質ではない）
* **充填確立点**: **未同定**
* **充填の性質**: — （第三群：RI-01/RI-08起因の報告形式問題）
* **Confidence**: — （N/A）
* **注記**: Full Paper展開時の自動解消が唯一の現実的経路。§E参照。

---

**EP-01a [Reporting-coherence pack]（SRG-5, 第三群）**

* **充填するRI**: RI-01 [Reporting integrity]（Table 1訂正changelog）
* **充填開始点**: **未同定**（手続き的問題、独立論文では解消不可）
* **充填確立点**: **未同定**
* **充填の性質**: — （第三群）
* **Confidence**: — （N/A）
* **注記**: 著者またはACS Publicationsへの直接問い合わせのみで解消可能。

---

**EP-05a [Quantitative-ranking substantiation pack]（SRG-8, 第二群）**

* **充填するRI**: RI-05 [Qualitative overread]（スコープ異常の機構的帰属）
* **充填開始点**: Xu, Sigman et al., *J. Am. Chem. Soc.* **2014**, *136*, 1960–1967 — Pd触媒redox-relay Heck arylationの速度論・選択性・機構（chain walking含む）を詳細に研究。アルケン種類（末端vs内部）と反応速度の関係に関するデータを含む可能性あり。
* **充填確立点**: 未同定
* **充填の性質**: Indirect — Pd触媒でのアルケン反応性の速度論的分析手法を提供するが、AQ-directed PMHS系への直接適用ではない。
* **Confidence**: Medium
* **注記**: Werner/Sigman Science 2012（ref 41）およびXu/Sigman JACS 2014（ref 42）はShirai 2024に引用済み。chain walking機構（1b形成）を裏付けるが、Thorpe-Ingold失敗と内部>末端逆転の特定実験的説明は依然として未充填。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Sugiyama, Sakaki et al., *JACS* 2008 | EP-03a（SRG-7: CsF fluoride機構） | VQ-3 | 2008 | High |
| 2 | Wang, Wu, Loh et al., *JACS* 2018 | EP-09a（SRG-4: benchmark baseline） | VQ-4 | 2018 | High |
| 3 | Li, Gong, Song, *Org. Chem. Front.* 2020 | EP-07a（CLA-2: ArBr適用境界） | VQ-2 | 2020 | High |
| 4 | Hurst, Zakharov, Cook, *Chem. Sci.* 2021 | EP-07a（CLA-2: radical exclusion） | VQ-3 | 2021 | Medium |
| 5 | Xu, Sigman et al., *JACS* 2014 | EP-05a（SRG-8: chain walking / alkene reactivity） | VQ-3 | 2014 | Medium |
| 6 | Hatanaka, Hiyama, *J. Org. Chem.* 1989 | EP-03a（SRG-7: CsF fluoride機構 onset） | VQ-3 | 1989 | High |

**選定理由：**

リストはVQ-2（EP-07a/CLA-2）→ VQ-3（EP-03a/SRG-7, EP-07a radical, EP-05a）→ VQ-4（EP-09a/SRG-4）という階層的カバレッジを持ち、1989年から2021年の33年間にわたる時間的多様性を確保している。**Sugiyama/Sakaki 2008** と **Hatanaka/Hiyama 1989** はバンドル充填としてEP-03a（SRG-7）の充填開始点と確立点をそれぞれ担う（2論文で1つのSRG-7を充填）。**Li/Gong/Song 2020** はEP-07aのArBr境界コンポーネントを高信頼度でカバーし、VQ-2要件の部分充填として最も直接的。**Hurst/Cook 2021** はEP-07aのラジカル排除コンポーネントをIndirect充填として補完する。

重要な欠落：EP-04a（SRG-3: deuterium replication）、EP-03a（SRG-2: 条件依存D実験）については高信頼度の充填論文候補が同定できないため、リストに含めていない。これらは§Eで発見的意義を持つ未充填EPとして記録する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件（RI-07: ArBr境界）: EP-07a → 2020年 [Li/Gong/Song] [分野横断充填: 異なる条件系での先例]
- VQ-3 要件（RI-03: fluoride機構）: EP-03a(SRG-7) onset → 1989年 [Hatanaka/Hiyama] [技術駆動充填: フルオロシリカート化学の確立]; 確立 → 2008年 [Sugiyama/Sakaki] [技術駆動充填: 計算化学による機構解明]
- VQ-3 要件（RI-03: radical排除）: EP-07a(radical) → 2021年 [Hurst/Zakharov/Cook] [技術駆動充填: Pd/Si-H酸化付加機構研究]
- VQ-3 要件（RI-04/RI-03: deuterium replication）: EP-04a → **未充填**（2026年4月時点）
- VQ-3 要件（RI-03: 条件依存D実験）: EP-03a(SRG-2) → **未充填**（2026年4月時点）
- VQ-4 要件（RI-09: benchmark）: EP-09a onset → 2018年 [Wang/Wu/Loh] [分野横断充填: ベースライン確立]（直接比較は未充填）

**階層-時間対応の評価：**

階層-時間仮説（「VQ階層が上がるほど充填に要する時間が長くなる」）は**部分的に支持される**。CsF fluoride機構（VQ-3, RI-03）が1989年（Hatanaka/Hiyama）にすでに部分充填されており、VQ-3要件が2008年には理論的に確立されていたことは、VQ-3要件の充填が「発表時点で既存知識で原理的に対応可能だった」ことを示す。一方、最も重要なVQ-3要件（RI-04: 重水素実験の反復定量、SRG-3）は2026年時点で未充填であり、これは技術的困難よりも「システム固有性」と「インセンティブ欠如」による未充填のパターン（§E参照）として記録する。VQ-4要件（RI-09: EP-09a benchmark）の直接充填が最も遅れており（未充填）、これは階層-時間仮説の方向と一致する。

**特筆すべきパターン：**

- **引用あり・充填適用なしパターン**: Sugiyama/Sakaki 2008（EP-03a/SRG-7充填確立点）はShirai 2024のref 40として引用されているにもかかわらず、CsF役割の二機能分離（fluoride vs base）というEP-03aのcase-specific実装には活用されていない。このパターン——充填論文を参照しながらその充填的機能を活用しない——は「充填の不活用（Filling non-activation）」として記録する価値がある。
- **インセンティブ逆転の観察**: 充填済みEPがRI-06（モデル輸入）やRI-07（境界テスト）に集中している一方、未充填EPがRI-04（単一実験）やRI-08（複数測定）という「技術的に実施可能だが出版インセンティブのない」要件に集中している。VQ階層の論理的順序（VQ-2→3→4）と実際の充填パターンが部分的に逆転する構造として記録する。
- **著者回顧との照合**: 現時点でShirai/Kumamoto groupの後続論文や回顧発表は認識されていないため、著者自身がどのEPを認識しているかは未確認。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

**EP-04a [Discrimination / replication pack]（SRG-3）:**

* **未充填の理由**: インセンティブ構造の不整合 — 重水素取り込み値の反復定量（n≥3）とH/D交換コントロールは技術的に完全に実施可能だが、これらを独立論文として出版するインセンティブが存在しない。合成Noteの追加実験データとしてのみ意味を持ち、独立した「新規性」を持たない。
* **発見的意義**: あり — 「機構的主張の唯一の定量的プローブ（重水素実験）の信頼性を担保する実験が、2026年時点で文献に存在しない」という事実は、合成化学における機構的主張の証拠基準が計測精度の観点から体系的に過少要求されていることの証左として記録できる。0.2Dという値が使用され続けながら誰もその精度を確認しないというパターンは、UQSが検出した「分野が2年以上にわたって体系的に回避してきた問い」の候補。
* **将来の充填可能性**: 高 — 2H NMR定量法は確立されており、H/D交換コントロールも標準的な実験操作。Shirai/Kumamoto グループがFull Paperを発表する際に自動解消が期待される。

---

**EP-03a（SRG-2）[Direct-observation / state-assignment pack]（条件依存D実験）:**

* **未充填の理由**: 関心の欠如 + インセンティブ構造の不整合 — 速い添加条件下での重水素実験（Entry 12相当）は本論文の系に固有であり、他グループが実施するインセンティブが存在しない。また、モデルの予測（速い添加 → δ-D増加）が正しいかどうかを確認することは「モデルの検証」であり、化学的新発見として発表しにくい。
* **発見的意義**: あり — 「論文が提案するモデルの最も直接的な定量的予測（添加速度条件依存のδ-D比率変化）が、提案から2年後の時点で未検証のまま」という状況は、合成化学における機構提案が定量的予測の検証なしに受け入れられる傾向の直接的証拠として記録できる。これはStage 3 §6のPRI-11（Mechanism-kinetics decoupling）昇格の背景と一致する構造的パターンである。
* **将来の充填可能性**: 高 — 実験は標準的な有機合成ラボで実施可能。自己充填経路が最も現実的。

---

**EP-03a（SRG-6）[Direct-observation / state-assignment pack]（PMHS量-副生成物収率）:**

* **未充填の理由**: インセンティブ構造の不整合 — 試薬量と副生成物収率の関係は最適化実験の一環として実施されているはずだが、「モデルの予測と整合するか」という問いに答えるための追加データとして独立発表されにくい。
* **発見的意義**: あり（限定的）— 「PMHS増量時に副生成物が増えるか減るかを報告しない」という省略が、dual-cycle modelの内部一貫性の評価を不可能にしているという構造（U-1の自己矛盾的不在）は記録価値あり。ただし他の未充填EPより発見的重要性は低い。
* **将来の充填可能性**: 高 — Full Paper展開で自動解消が期待される。

---

**EP-08a [Replication / uncertainty pack]（SRG-1, CLA-1）:**

* **未充填の理由**: 分野慣行 + インセンティブ構造の不整合 — 合成論文でのreplicate測定の欠如は分野慣行として許容されており、内部標準安定性コントロールの省略も広く行われている。これらは「追試」として扱われ独立論文化されにくい。
* **発見的意義**: あり（制度的）— 「VQ-4（Benchmark）への到達に必要なRI-08要件が、合成化学のノート形式では構造的に充填されないインセンティブ構造を持つ」という観察は、UQSのVQ-4判定が合成化学の出版慣行において系統的に障害に直面することを示す制度的発見として記録できる。分野のインセンティブ構造がVQ-4未達を維持している一つの機構。
* **将来の充填可能性**: 中 — Full Paper展開または著者グループが追加実験を実施した場合に解消可能。独立グループによる充填は構造的に困難。

---

**EP-01a [Reporting-coherence pack]（SRG-5）:**

* **未充填の理由**: 報告形式問題 — 訂正changelog開示は出版慣行・著者への問い合わせによってのみ解消可能であり、科学論文として充填されない性質の問題。
* **発見的意義**: なし（技術的手続き問題）
* **将来の充填可能性**: 高（手続き的対応で即時解消可能。ACS PublicationsのCorrespondence著者への問い合わせで特定可能）

---

**VQ階層逆転の診断：**

未充填EPの分布：
- 未充填EPがRI-04（SRG-3: 唯一の機構的プローブの精度）、RI-03（SRG-2: 条件依存D実験）という**VQ-3要件**に集中している
- 充填済みEPがRI-03（SRG-7: CsF機構）、RI-07（CLA-2: ArBr）という**先行文献で既に確立された機構・境界**に集中している

この分布は「先行文献として既存の高VQ要件が間接的に充填される」一方、「本論文固有の低VQ/中VQ要件は出版インセンティブ欠如により未充填のまま」という非対称充填パターンとして記録する。**技術的実行可能性が高いにもかかわらず科学コミュニティのインセンティブ構造により充填されない問い**（EP-04a、EP-03a/SRG-2）が複数確認された。これはUQSが抽出した「語られていない問い」の中に、分野のインセンティブ構造によって維持される構造的不在が一定割合で含まれるという制度的発見の実例である。

inference_time_sec: not available — inject externally
```
