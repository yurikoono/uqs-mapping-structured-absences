```
prompt_version: stage4-v2-20260416
model_info: Claude Sonnet (current snapshot)
experimental_variant: "Murai cross-vendor multi-run sonnet v2 run 2"
date: 2026-06-12
```

# EP充填選定マップ

## Murai et al. 1993（Nature, communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a, EP-09a

- **EP-03a** (Direct-observation / state-assignment pack): Ru系C–H活性化の中間体観測・触媒サイクル解明はChatani・Kakiuchi・Murai本人らの後続Full Paperで独立研究として発表されており、文献追跡が容易。
- **EP-04a** (Discrimination / replication pack): KIE測定および重水素標識実験によるC–H切断律速の確認は、後続の機構研究論文が独立した主題として取り上げており、文献で直接ヒットしうる。
- **EP-06a** (Analogy-validation pack): 化学量論モデル反応によるシクロメタル化中間体の独立検証は、Ru錯体化学の文脈でより広いグループが実施し、独立論文として発表されている。
- **EP-07a** (Boundary-test pack): キレーション支援の有効範囲・配位子種依存性・適用基質の拡大はKakiuchi・Chataniグループが体系的に論文化しており、境界条件が独立論文として明確に追跡可能。
- **EP-09a** (Internal benchmark pack): TOF値の数値比較・Ru触媒活性評価は後続のスコープ拡張論文が定量的比較表を掲載しており、独立論文として存在する可能性が高い。

**第二群（間接的に追跡可能）：** EP-05a, EP-08a

- **EP-05a** (Quantitative-ranking substantiation pack): 選択性の速度論的/熱力学的制御の判別は、後続Full Paper（Kakiuchi et al. JACS 1994等）の一部として含まれることが多く、独立論文の主題というよりは内包されている形が多い。
- **EP-08a** (Replication / uncertainty pack): 収率のSD付き再現データは後続のFull Paper展開時に自動的に拡充されるが、「再現実験それ自体」を独立テーマとした論文は存在せず、レビュー・Full Paperに分散して含まれる形となる。

**第三群（充填が見つからない可能性あり）：** EP-01a

- **EP-01a** (Reporting-coherence pack): GC校正プロトコルの遡及的明示・応答係数の独立測定という要件は、通信→Full Paper遷移でも完全には解消されないことが多く、後続論文が別基質系で報告する際に自動的に既存データが再校正される構造にはなっていない。分野慣行として校正省略が継続されている可能性が高い。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 Reporting integrity / RI-08 Unquantified reliability
* **充填開始点**: Kakiuchi et al., *J. Am. Chem. Soc.* 1994 — アセトフェノン/アクリル酸エチル系のFull Paper展開において単離収率と反応条件の詳細を記載（通信からの自己充填）。
* **充填確立点**: 未同定（GC校正プロトコルの独立した明示という要件は、1994年のFull Paperでも完全には充足されなかった可能性が高い）。
* **充填の性質**: Partial（Full Paper展開で報告形式は改善されるが、校正プロトコルの独立的明示という要件は充足されていない可能性が高い）
* **Confidence**: Low
* **注記**: RI-01の完全充填はjournal policy強制によってのみ実現しうる性質であり、後続論文が事後的にMurai 1993の収率を再校正することは想定しにくい。第三群の理由はインセンティブ構造の不整合に起因する。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory / RI-06 Imported model
* **充填開始点**: Kakiuchi, F.; Murai, S. et al., *J. Am. Chem. Soc.* 1994, 116, 3139–3140 — アセトフェノン系のFull Paperであり、触媒サイクルに関する追加証拠（H₂発生の言及、前駆体挙動）を含む。
* **充填確立点**: Chatani, N.; Fukumoto, Y.; Ida, T.; Murai, S., *J. Am. Chem. Soc.* 1993, 115, 11614–11615 — Ruシクロメタル化中間体の直接分光学的観測試行（関連系での中間体trapping）。ただし本系の直接観測かは不確か。
* **充填の性質**: Partial（活性種の直接観測は類似系で進んだが、本反応系のRu(0)/cyclometallated Ru(II)中間体の分光学的同定という要件の完全充足は不確か）
* **Confidence**: Medium
* **注記**: Ru-H結合活性化のメカニズム研究はYamamoto、Bergman、Jones各グループが1990年代に大きく進展させたが、Murai反応の固有の活性種同定は難しかった。Chatani後続論文群（1997年以降）がより詳細な機構を提供。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator / RI-03 Unobserved explanatory
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S., *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 — Full Paper（通信の完全版）。重水素標識実験を含む機構証拠を提供した可能性。
* **充填確立点**: Kakiuchi, F.; Murai, S., *Acc. Chem. Res.* 2002, 35, 826–834 — KIE・同位体標識を含む機構考察を集約するAccounts論文。ただしAccounst/レビューは直接充填しないため、そこに引用された原著（KIE実験を実施した論文）が充填確立点となる。
* **充填の性質**: Partial（Full Paperでの機構データ追加はあるが、M–H対M–C挿入経路の明確な区別という厳密な要件への対応は限定的）
* **Confidence**: Medium
* **注記**: Murai系の直接KIE測定論文を独立の論文として思い出せない。Bull. Chem. Soc. Jpn. 1995のFull Paperが最も有望な候補だが、その具体的内容について確信が持てない。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 Qualitative overread / RI-04 Unreplicated discriminator
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S., *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 — 位置選択性の詳細なデータ（電子的・立体的基質依存性）を定量的に追加し、ortho選択性の要因分析を提供。
* **充填確立点**: 同上（Full Paperが選択性の定量的根拠として機能した場合）
* **充填の性質**: Partial（選択性の定量的実証は進むが、速度論的対熱力学的制御の明示的判別実験は不明）
* **Confidence**: Medium
* **注記**: EP-05aの要件（速度論/熱力学的制御の実験的判別）は後続論文でも完全には対処されていない可能性がある。基質スコープ拡張論文が主であり、制御機構の判別が独立テーマになりにくい。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Chatani, N.; Asaumi, M.; Ikeda, T.; Yorimitsu, H.; Ishii, Y.; Kakiuchi, F.; Murai, S., *J. Am. Chem. Soc.* 2000, 122, 10335–10336 — Ru触媒C–H活性化の機構論文。類似系での化学量論モデル反応を実施しCyclometallated中間体の証拠を提供。
* **充填確立点**: Siegbahn, P. E. M.; Crabtree, R. H., *J. Am. Chem. Soc.* 1996, 118, 4442–4450 — DFT計算によるRuシクロメタル化経路の理論的検証。C–H酸化的付加とσ-bond metathesis経路の比較エネルギーを提供し、輸入モデルの量子化学的検証という形でRI-06を前進。
* **充填の性質**: Indirect（Siegbahnは計算、Chataniは類似系での実験であり、原反応系の直接的化学量論モデルではない）
* **Confidence**: Medium
* **注記**: Siegbahn & Crabtree 1996はRu(0)によるaromatic C–H activationのDFT研究として著名であり、Murai反応の機構を直接検討した可能性がある。ただし正確な論文タイトルと内容への対応について確信が中程度。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S., *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 — キレーター種のバリエーション（アシル基以外への展開）と反応する基質の境界条件を体系的に調査した最初の詳細報告。
* **充填確立点**: Kakiuchi, F.; Yamada, A.; Chatani, N.; Murai, S., *Organometallics* 1999, 18, 2033–2036 — pyridine系・imino基等の異なるキレーターへの展開を実証し、キレーション支援の構造的境界を実験的に確立した論文の一つ。
* **充填の性質**: Partial（キレーター種の拡張は示されるが、「6員vs5員金属環の反応性境界」という要件の明示的充足は不確か）
* **Confidence**: Medium
* **注記**: Kakiuchi et al. 1995 Full PaperがEP-07aの最重要充填候補。Organometallics 1999の論文は記憶の確信度が低い（タイトル・年・巻号の正確性に不確実性あり）。

---

**EP-08a [Replication / uncertainty pack]（第二群）**

* **充填するRI**: RI-08 Unquantified reliability / RI-01 Reporting integrity
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S., *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 — 13例を超える基質での単離収率データを再現試験的に拡充し、SD的な信頼性の向上に寄与。
* **充填確立点**: 同上（Full Paperがreplication要件の部分的充填として機能する）
* **充填の性質**: Partial（Full Paperは収率データを拡充するが、SD値・再現実験の明示という厳密な要件の充足は不明）
* **Confidence**: Low
* **注記**: EP-08aの要件（SD付き再現データ）は分野慣行として現在も徹底されていない。Full Paperへの展開で収率データが増加することはEP-08aの部分充填として機能するが、完全充填にはならない可能性が高い。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 External superiority / RI-08 Unquantified reliability
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S., *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 — TOF値の計算と先行系との数値比較が含まれる可能性（Full Paperへの展開で定量的benchmark比較が追加された場合）。
* **充填確立点**: Kakiuchi, F.; Murai, S., *Acc. Chem. Res.* 2002, 35, 826–834 — 当時の反応として達成されたTOFを先行系と比較する文脈がAccounts論文に含まれる。ただしAccounts自体は充填しない——そこに引用された定量的比較が含まれるFull Paperが充填確立点となる。
* **充填の性質**: Partial（TOFの定量的比較は後続論文で提示されるが、同一軸での厳密な換算比較という要件への対応は不明）
* **Confidence**: Low
* **注記**: RI-09のFull充填には、Jordan & Taylor (1989) とMoore et al. (1992) の条件を本Ru系と同一軸で換算した比較表が必要。このような厳密な換算比較が独立論文として存在するかは不確か。

---

**追加候補（バンドル充填の可能性があるもの）：**

**Chatani, N.; Fukumoto, Y.; Ida, T.; Murai, S., *J. Am. Chem. Soc.* 1993, 115, 11614–11615**
- 1993年同年の関連論文。ルテニウム触媒によるsp³ C–H活性化（飽和アルデヒド系）を報告。機構的含意を含む可能性があり、EP-03aとEP-06aへの間接的関連が考えられる。ただし論文の主題がMurai 1993の要件と直接対応するかは不確か。Confidence: Low。

**Chatani, N.; Asaumi, M.; Yorimitsu, H.; Kavamoto, T.; Kakiuchi, F.; Murai, S., *J. Am. Chem. Soc.* 2001, 123, 10935–10941**
- RhまたはRuを用いたC–H/CO挿入系の機構研究。中間体の分光学的同定を含む。EP-06aへの間接充填候補。Confidence: Low（論文の詳細に不確実性あり）。

**Lim, Y.-G.; Kang, J.-B.; Kim, Y. H., *J. Chem. Soc., Chem. Commun.* 1996**
- Rh触媒によるC–H活性化のMurai反応類似研究。EP-07a（境界条件：Ru以外の金属での成立）の間接充填候補。Confidence: Low。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Kakiuchi, Sekine, Tanaka, Kamatani, Sonoda, Chatani, Murai et al., *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 | EP-03a, EP-04a, EP-05a, EP-07a, EP-08a, EP-09a | VQ-2→VQ-3 | 1995 | Medium |
| 2 | Kakiuchi, Murai et al., *J. Am. Chem. Soc.* 1994, 116, 3139–3140 | EP-01a, EP-03a | VQ-2 | 1994 | Medium |
| 3 | Siegbahn, Crabtree, *J. Am. Chem. Soc.* 1996, 118, 4442–4450 | EP-06a | VQ-3 | 1996 | Medium |
| 4 | Chatani et al., *J. Am. Chem. Soc.* 2000, 122, 10335–10336 | EP-06a, EP-03a | VQ-3 | 2000 | Medium |
| 5 | Kakiuchi, Murai, *Acc. Chem. Res.* 2002, 35, 826–834 | EP-09a (benchmark文脈), EP-07a | VQ-4参照 | 2002 | Medium |

**選定理由：**

第1位のBull. Chem. Soc. Jpn. 1995 Full Paperは、Murai 1993通信の著者グループによる自己充填の最重要候補であり、6つのEPに跨るバンドル充填の可能性が最も高い。通信→Full Paper遷移は自動的にRI-01/08を前進させるため、VQ-2への階段を一報でカバーできる。第2位のJACS 1994もMurai・Kakiuchi Firstの自己充填であり、Full Paperの初報として報告形式の改善を期待できる（ただし異なる基質を対象とした可能性もあり、Confidence Mediumとした）。

第3位のSiegbahn & Crabtree 1996は理論研究（DFT）として、EP-06aの輸入モデル検証という要件に最も正面から対応する可能性がある。Ru(0)のC–H酸化的付加経路の計算的検証はRI-06の前進として機能し、実験的中間体同定なしの理論的裏付けという形でVQ-3要件に寄与しうる。

第4位のChatani 2000はRu系の機構研究として中間体の直接証拠を提供する可能性があり、EP-03aとEP-06aへの実験的充填として期待できる。

第5位のAcc. Chem. Res. 2002はレビューとして直接充填はしないが、TOFの定量的文脈整理（EP-09a）とキレーター種境界（EP-07a）についてのconsensus形成を確認できる二次情報源として有用。

なお、本推奨リストはConfidence: Highの論文がゼロである点に注意が必要である。全候補がMediumまたはLowであり、実際の文献確認が不可欠である。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a → 1994–1995年（Kakiuchi JACS 1994 / Bull. Chem. Soc. Jpn. 1995、部分充填、自己充填パターン）
- VQ-2 要件: EP-08a → 1995年（Bull. Chem. Soc. Jpn. 1995 Full Paper、部分充填、自己充填パターン）
- VQ-3 要件: EP-03a → 1995–2000年（Bull. Chem. Soc. Jpn. 1995 + Chatani 2000、部分充填、自己充填→技術駆動）
- VQ-3 要件: EP-04a → 1995年（Bull. Chem. Soc. Jpn. 1995 推定、部分充填、自己充填）
- VQ-3 要件: EP-05a → 1995年（Bull. Chem. Soc. Jpn. 1995 推定、部分充填、自己充填）
- VQ-3 要件: EP-06a → 1996年（Siegbahn & Crabtree 1996 DFT、Indirect充填、技術駆動充填）
- VQ-3 要件: EP-07a → 1995年以降（Bull. Chem. Soc. Jpn. 1995 + 後続スコープ拡張群、部分充填、自己充填→分野横断）
- VQ-4 要件: EP-09a → 2000年代（benchmark比較の数値化は段階的、部分充填のまま停滞の可能性）

**階層-時間対応の評価：**

「VQ階層が上がるほど充填に要する時間が長くなる」という仮説への支持は部分的に確認される。VQ-2要件（EP-01a、EP-08a）は1994–1995年のFull Paper展開で最初に前進している（原論文から1–2年）。VQ-3要件（EP-03a、EP-06a）は1995–2000年という時間幅で進展しており、やや遅い。VQ-4要件（EP-09a）については、厳密なTOF換算比較という要件の充足が、2020年代の現在に至っても不明確という意味で最長の遅延を示している可能性がある。ただしConfidence Mediumの推定に基づくため、仮説の検証には実際の文献確認が必要。

**特筆すべきパターン：**

1. **自己充填パターンが支配的**: 最重要EPの多くは、Murai・Kakiuchi・Chataniという原著者グループ自身の後続論文によって充填されている。これは通信→Full Paper遷移の自己充填パターンとして典型的であり、外部グループによる独立充填よりも自己充填が先行している。

2. **技術駆動充填（DFT）**: EP-06a（輸入モデルの検証）については、1990年代中盤から進んだDFT計算法（NL-DFT、B3LYP等）の成熟がSiegbahn & Crabtreeのような理論的充填を可能にした。実験的充填が困難なRI-06を技術駆動で前進させた例として記録できる。

3. **EP-09aの長期遅延充填の疑い**: TOF数値の厳密な換算比較（同一軸でのJordan/Moore比較）は、後続論文が異なる基質・異なる定義でTOFを報告することで問いが散逸し、原論文が主張した「最高水準」の真偽検証が体系的に行われなかった可能性がある。これは出版インセンティブ構造の不整合（新規系のTOF報告>既存系の再測定）によって維持された未充填パターンとして記録できる。

4. **著者回顧との照合**: Kakiuchi & Murai, *Acc. Chem. Res.* 2002において、著者らはキレーション支援の概念拡張と基質スコープ拡大（EP-07a相当）を回顧の中心に置いた可能性が高い。機構の詳細（EP-03a、EP-04a、EP-06a相当）は回顧でも「提案」として残されており、著者自身がこれらを未解決として認識していた可能性がある。一方、EP-09a（定量的TOF比較）はAccounts論文において著者回顧に現れない場合、「分野の内部者には不可視の構造的不在」の直接的証拠として記録できる。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

EP-01a [Reporting-coherence pack]:
* **未充填の理由**: インセンティブ構造の不整合。GC校正プロトコルの独立的明示という要件は、通信→Full Paper遷移では自動解消されず、後続論文が異なる基質系で同じ省略を繰り返す傾向がある。2020年代以降のNatureやJACSが補足情報に校正データ要求を強化しているが、1990年代・2000年代の論文遡及的修正は行われない。
* **発見的意義**: あり。GC収率のみによる主張の量的実証は有機合成通信の分野慣行として1993年以降も持続しており、「分野が30年にわたって体系的に回避してきた報告形式問題」として記録できる。RI-01の未充填は個別論文の欠落ではなく分野レベルの慣行として位置付けられる。
* **将来の充填可能性**: 中。Journal policyの強制（Nature系列のopen data要求等）によって将来の論文では充填されうるが、Murai 1993という個別論文のRI-01を遡及的に充填するメカニズムは存在しない。

EP-09a [Internal benchmark pack]（部分充填のみ）:
* **未充填の理由**: 分野慣行とインセンティブ構造の不整合。後続論文は新しい基質系・新しい触媒・新しいリガンドのTOFを報告するが、Jordan/Moore (1989/1992) 系との同一軸での換算比較を後追い的に行う動機がない。Murai 1993の比較優位性主張の真偽はこの意味で現在も未検証のまま残っている可能性がある。
* **発見的意義**: あり。「最高水準のTOFを達成した」という比較主張が、独立した定量的検証なしに分野に受容された事例として記録できる。引用回数の多さがRI-09の未解消を隠蔽してきた可能性がある。
* **将来の充填可能性**: 低。Jordan/Moore系のTOFを現代のRu系と同一軸で換算する作業は、研究者にとって独立した出版価値を持たないため、論文として充填される可能性は低い。教科書・総説での定量比較が唯一の充填形態となりうる。

EP-04a [Discrimination / replication pack]（部分充填止まりの可能性）:
* **未充填の理由**: 技術的困難とインセンティブ構造の不整合。M–H対M–C挿入経路の区別は精巧な重水素標識実験を要求するが、この区別が反応の有用性（スコープ拡大）に直結しないため、機構家以外の研究者がこのEPを独立研究として追求するインセンティブが弱い。Murai反応は「使える反応」として急速に広まり、機構の詳細は二次的関心に留まった。
* **発見的意義**: あり。反応の「実用化」が機構理解に先行し、機構的問いが置き去りにされるパターン——「成功が問いを消す」構造——の典型事例として記録できる。
* **将来の充填可能性**: 中。現代のNMR技術（isotope labeling + 低温NMR）と計算化学の組み合わせで理論的には充填可能。ただし現時点で明確な充填論文が存在するかは不確か。

**VQ階層逆転の診断：**

本論文では、以下の逆転パターンが観察される：

- **充填が比較的進んでいるEP**: EP-07a（境界条件の拡張）、EP-05a（選択性データの定量的拡充）— これらはVQ-3要件に対応し、新規基質での応用展開という出版価値が高い。
- **充填が遅延・未完のEP**: EP-01a（GC校正）、EP-09a（TOF換算比較）— これらはVQ-2要件に対応し、既存データの検証・再測定という形で独立出版価値が低い。

「科学的論理に基づくEP充填順序（低VQ→高VQ）」と「実際の充填順序（高VQ要件に対応するEPが先行）」の逆転が確認される。VQ-2の基盤（RI-01の収率信頼性）が未解決のまま、VQ-3以上の要件（機構、選択性、境界条件）を充填する後続研究が先行したことは、分野のインセンティブ構造（新規性重視・応用拡大重視）がUQSの構造的不在の一部を維持してきた証拠として記録できる。
