```
prompt_version: stage4-v6-20260504
model_info: Claude Sonnet (current snapshot)
experimental_variant: "Murai cross-vendor multi-run sonnet v6 run 2"
date: 2026-06-12
```

# EP充填選定マップ

## Murai et al. 1993（Nature, communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-05a, EP-06a, EP-07a

- **EP-03a** (Direct-observation / state-assignment pack): Ru(0)活性種・シクロメタル化中間体の分光学的同定は、後続のChatani・Kakiuchi・Murai各グループによる機構研究の独立論文主題として直接的に発展した。中間体の単離・NMR観測を報告した論文が複数存在する。
- **EP-04a** (Discrimination / replication pack): KIE測定・重水素標識によるC–H切断の律速性確認は、C–H活性化の機構論文の定番実験として1990年代後半から独立して報告されている。
- **EP-05a** (Quantitative-ranking substantiation pack): 温度依存性・電子効果・基質速度論を扱う定量的選択性研究は後続Chatani/Kakiuchi論文で系統的に実施された。独立論文としての発表が確認しやすい。
- **EP-06a** (Analogy-validation pack): モデル化学量論反応によるシクロメタル化中間体の検証は、Ru錯体の反応性を扱う有機金属化学論文群で独立研究の対象となった。
- **EP-07a** (Boundary-test pack): キレーション支援の構造的スコープ（5員/6員金属環境界、配位基タイプ）は、Murai反応の多数の後続スコープ拡張論文の中核テーマであり、独立論文として発表されやすい。

**第二群（間接的に追跡可能）：** EP-01a, EP-09a

- **EP-01a** (Reporting-coherence pack): GC校正プロトコルの完全開示・単離収率・再現実験は、Murai 1993の直後にKakiuchi・Mukai et al.（同グループFull Article、JACS 1993/1994）が実施したが、論文形式の自動解消パターンとして追跡可能。ただし独立論文の主題というよりFull Paper展開での自動解消。
  - C23 trigger: **Letter→Full Paper auto-resolution** 該当（Nature communication → JACS Full Article）
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```
- **EP-09a** (Internal benchmark pack): TOF値の定量的比較はレビュー論文やPerspective記事で間接的に扱われる傾向があり、独立したTOF比較論文は少ない。類似系のベンチマークは複数存在するが対象系そのものでの定量比較は限定的。

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a** (Replication / uncertainty pack): Murai反応は有機合成分野で広く「使われる」反応となったが、本反応系の統計的信頼性評価・反復測定を独立論文として行うインセンティブは低い。後続論文群はすべて「反応を用いる」論文であり、Murai 1993の収率データの統計的再評価を目的とした論文は存在しない可能性が高い。**インセンティブ構造的未充填**。

---

### §B 各EPの充填論文候補

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点**: Kakiuchi, F.; Sato, T.; Tsujimoto, T.; Yamada, H.; Chatani, N.; Murai, S. *Chem. Lett.* 1998, 27, 1053–1054 — RuH₂(CO)(PPh₃)₃存在下でのアセトフェノン-Ru錯体の反応追跡により、触媒サイクルの前活性化段階（H₂放出・Ru(0)生成）を分光学的証拠と関連付けた。
* **充填確立点**: Chatani, N.; Fukuyama, T.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* 1998, 120, 11522–11523 — C–H結合活性化の中間体（シクロルテニウム化中間体）の直接観測的証拠を提示し、Ru(0)活性種経由の経路を実験的に裏付けた。
* **充填の性質**: Partial（活性種の帰属は前進したが完全なサイクル中間体の単離・特定は未達）
* **Bibliographic confidence**: Medium（著者名・年・雑誌の組み合わせに高い確信があるが、正確な巻号・ページは推測を含む）
* **Filling adequacy confidence**: Medium（論文の主題がEP-03aの要件と対応する方向性は明確だが、具体的な実験内容とEPの対応は推論を含む）
* **Verification recommendation**: [必須]（条件(c) Murai named reactionに該当、条件(b) 同グループ10+論文）
* **DOI**: 要検証
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr) — 機構論文の分野的成熟による充填
* **注記**: Chatani 1998とKakiuchi 1998はほぼ同年であり、同一研究グループ（Murai/Chatani/Kakiuchi大阪大学グループ）による自己充填パターン。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: Guari, Y.; Sabo-Etienne, S.; Chaudret, B. *J. Am. Chem. Soc.* 1998, 120, 4228–4229 — Ru錯体によるC–H活性化の速度論的同位体効果（KIE）測定を報告し、C–H切断が律速段階であることを重水素標識実験で確認した（類似Ru系ではあるが直接的なKIEデータを提供）。
* **充填確立点**: Kakiuchi, F.; Sato, T.; Igi, K.; Chatani, N.; Murai, S. *Chem. Lett.* 2001, 30, 386–387 — ortho-d₁-アセトフェノン類似体を用いたKIE実験によりC–H切断の律速性を直接確認した。
* **充填の性質**: Partial（M–H対M–C挿入経路の完全な区別には至らなかったが、C–H切断律速の確認という部分充填）
* **Bibliographic confidence**: Low（Kakiuchi 2001のChem. Lett.論文の存在について中程度の確信があるが、正確な巻・ページは不確か。Guari 1998 JACSnは高確信）
* **Filling adequacy confidence**: Medium
* **Verification recommendation**: [必須]
* **DOI**: 要検証
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: EP-03aとバンドル関係にある（同じ機構実験の枠組みに属する）。

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-05 Qualitative overread
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 — Murai 1993の全スコープを定量化したFull Article（同グループによる自己充填の代表論文）。13例以上の基質について単離収率・再現実験を含む詳細データを提供し、選択性の基質依存性を定量的に検証した。
* **充填確立点**: 同上（BCSJ 1995が充填確立点として機能する）
* **充填の性質**: Complete（位置選択性の定量的確認・選択性の基質依存性の系統的検討がなされた）
* **Bibliographic confidence**: High（BCSJ 1995のKakiuchi・Murai Full Articleは広く参照されており、著者名・雑誌・年に高い確信がある。巻号は要確認）
* **Filling adequacy confidence**: High（Full Articleとしての展開がEP-05aの要件を直接満たす）
* **Verification recommendation**: [必須]（条件(c)）
* **DOI**: 要検証（BCSJ 1995年68巻）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr) — Letter→Full Article自動解消
* **注記**: EP-01aとも部分的にバンドル（GC校正・単離収率が同時に提供された可能性）。自己充填パターンの典型事例。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Hiraki, K.; Matsunago, T.; Kawano, H. *Organometallics* 1994, 13, 1878–1884 — Ru錯体によるarene C–H結合の酸化的付加および化学量論モデル反応の系統的研究。類似系でのシクロルテニウム化中間体の分光学的同定に関するデータを提供（内容は推測を含む）。
* **充填確立点**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* 1998, 120, 12692–12693 — DFT計算によりMurai反応の触媒サイクル（C–H酸化的付加→オレフィン挿入→還元的脱離）のエネルギープロファイルを計算し、類似系からの輸入モデルを計算レベルで検証した。
* **充填の性質**: Indirect（Matsubara 1998は実験的充填でなく計算的充填。計算レベルではRI-06を前進させるが、実験的検証は別途必要）
* **Bibliographic confidence**: High（Matsubara-Koga-Morokuma 1998 JACSnはMurai反応の理論論文として参照頻度が高い。Hiraki 1994については確信が低い）
* **Filling adequacy confidence**: Medium（Matsubara 1998はEP-06aの計算的版の要件を満たすが、実験的要件（化学量論モデル反応）は間接的）
* **Verification recommendation**: [必須]
* **DOI**: 要検証（JACS 1998, 120, 12692）
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr) — 計算化学手法の成熟による充填
* **注記**: 計算論文によるRI-06充填は「証拠的相補性」の点で実験充填とは異なる。実験的充填（化学量論モデル反応での中間体単離）は別途必要。Matsubara 1998はEP-03aにも部分的にバンドル。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Kakiuchi, F.; Yamamoto, Y.; Chatani, N.; Murai, S. *Chem. Lett.* 1995, 681–682 — キレーション基タイプの系統的変更（ケトン→アルジミン・アミン・アミド等）によるスコープ拡張を報告し、5員環/6員環形成基質の反応性境界を定量的に示した。
* **充填確立点**: Kakiuchi, F.; Murai, S. *Acc. Chem. Res.* 2002, 35, 826–834 — 著者グループ自身による回顧的総説（レビュー）で、キレーション依存性スコープの境界条件を体系的に記述した。ただし本エントリはレビューのため選定除外。充填確立点としては1995–1998年の一連のスコープ拡張Full Papers群が相当する。
* **充填の性質**: Complete（キレーション境界の実験的確定という要件を複数論文で達成）
* **Bibliographic confidence**: Medium（Kakiuchi 1995 Chem. Lett.の存在に高確信。正確な巻号・ページは推測）
* **Filling adequacy confidence**: High（スコープ拡張論文がEP-07aの要件を直接満たす構造になっている）
* **Verification recommendation**: [必須]
* **DOI**: 要検証
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (variable) — 合成化学における標準的なスコープ拡張研究として充填
* **注記**: CLA-1（キレーション支援の構造的境界）に対応するEP-07aは、後続論文群の最もアクティブなテーマとなった。境界実験は単一論文ではなく複数論文の累積として充填。

---

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 — Murai 1993のFull Article展開。単離収率・再現実験・詳細な実験条件（雰囲気、溶媒乾燥）を含む系統的データを提供し、communicationの報告形式問題を解消した。
* **充填確立点**: 同上
* **充填の性質**: Complete（letter→Full Article遷移として報告形式問題を構造的に解消）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: High
* **Verification recommendation**: [必須]
* **DOI**: 要確認
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: EP-05aとバンドル。同一論文（BCSJ 1995）がEP-01aとEP-05aを同時充填する可能性が高い。

```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点**: Chatani, N.; Asaumi, M.; Ikeda, T.; Yorimitsu, S.; Ishii, Y.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* 2000, 122, 12882–12883 — 異なる配位子環境のRu触媒系を比較し、TOF/TON値を明示的に算出して比較する数値表を含む論文。Murai 1993との数値的比較に利用可能なデータポイントを提供する。
* **充填確立点**: **未同定** — Murai 1993で参照されたJordan & Taylor (1989) / Moore et al. (1992)とのTOF直接比較を行った論文は現時点で特定できない。
* **充填の性質**: Partial（後続論文群でTOF値記載が定着したが、1993年論文固有の比較文脈での充填は限定的）
* **Bibliographic confidence**: Low（Chatani 2000 JACSnの存在は確認できるが、内容がEP-09aの要件に正確に対応するかは不確か）
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]
* **DOI**: 要確認
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (variable)
* **注記**: RI-09の実質的充填は単一の比較論文によってではなく、フィールド全体での数値化規範の成熟（2000年代）によって間接的に達成された可能性が高い。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 Unquantified reliability + RI-01
* **充填の性質**: 未同定
* **未充填の理由**: **インセンティブ構造的未充填** — Murai 1993の収率データの統計的再評価・反復測定を目的とした独立論文は、出版インセンティブの観点から論文化されにくい。後続論文群はすべて新基質・新配位子系の探索に向かい、1993年の元データセット（13例）の統計的精査は行われていない。
* **Bibliographic confidence**: N/A
* **Filling timescale category**: non-applicable（インセンティブ構造的未充填）
* **注記**: EP-08aの部分的解消はBCSJ 1995（Full Article）で単離収率・再現実験が追加されることで達成されたが、GC収率の校正プロトコル開示・SDの明示という要件は依然として未充填。

---

**§B 末尾チェック：Bibliographic verification**

**トリガー条件の評価：**
- (a) 論文年代: 1990年代論文が多い（1980年以前ではないが中程度のリスク）
- (b) 著者ネットワーク: Murai/Chatani/Kakiuchi大阪大学グループから10+以上の関連論文が存在する
- (c) 反応名: 「Murai反応」（著者名由来の named reaction） — **最強トリガー**
- (d) Medium-Low confidence候補が2件以上含まれる（EP-04a候補、EP-06a Hiraki候補等）

**判定**: 上記(c)最強トリガーにより全候補に **[必須]** を付与。

**Bibliographic verification status**: 全エントリ **pending**

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Kakiuchi, Sekine, Tanaka, Kamatani, Sonoda, Chatani, Murai, *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83 | EP-01a, EP-05a | VQ-2, VQ-3 | 1995 | High | High | ⚠️ pending [必須] |
| 2 | Matsubara, Koga, Musaev, Morokuma, *J. Am. Chem. Soc.* 1998, 120, 12692–12693 | EP-06a | VQ-3 | 1998 | High | Medium | ⚠️ pending [必須] |
| 3 | Chatani, Asaumi, Ikeda, Yorimitsu, Ishii, Kakiuchi, Murai, *J. Am. Chem. Soc.* 2000, 122, 12882–12883 | EP-09a, EP-05a | VQ-4 | 2000 | Low | Low | ⚠️ pending [必須] |
| 4 | Kakiuchi, Yamamoto, Chatani, Murai, *Chem. Lett.* 1995, 681–682 | EP-07a | VQ-3 | 1995 | Medium | High | ⚠️ pending [必須] |
| 5 | Chatani, Fukuyama, Kakiuchi, Murai, *J. Am. Chem. Soc.* 1998, 120, 11522–11523 | EP-03a, EP-04a | VQ-3 | 1998 | Medium | Medium | ⚠️ pending [必須] |
| 6 | Kakiuchi, Sato, Tsujimoto, Yamada, Chatani, Murai, *Chem. Lett.* 1998, 27, 1053–1054 | EP-03a | VQ-3 | 1998 | Medium | Medium | ⚠️ pending [必須] |

**選定理由：**

第1位のKakiuchi et al. BCSJ 1995はMurai 1993のFull Article展開として、EP-01a（報告形式の完全化）とEP-05a（定量的選択性確認）を同時に充填するバンドル論文として最優先。同一著者グループによる自己充填であり、format-drivenな1–3年以内の充填として充填時間軸の最初のマイルストーン。

第2位のMatsubara et al. JACS 1998はDFT計算による触媒サイクル全エネルギープロファイルの提供であり、RI-06（類似系からの輸入モデルの検証）を計算的に充填する代表論文。EP-06aの計算的版充填として重要であり、「触媒サイクルはどのように閉じているのか」という核心問いへの理論的回答を提供する。

第4位のKakiuchi Chem. Lett. 1995はキレーション基のスコープ拡張（アルジミン・アミン等への展開）を報告し、EP-07a（境界テスト）の早期充填として1993年から2年以内の充填を実証する。

全候補に [必須] verification を付与したのは Murai named reaction（条件c）と著者ネットワーク密度（条件b）によるものであり、Sonnet固有のhallucination riskが既知文書（`improvements/`内メタ分析）で指摘されている経緯による。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a → 1995年 Kakiuchi et al. BCSJ（自己充填、format-driven）
- VQ-2 要件: EP-07a → 1995年 Kakiuchi et al. Chem. Lett.（自己充填、incentive-aligned）
- VQ-3 要件: EP-05a → 1995年 Kakiuchi et al. BCSJ（EP-01aとバンドル、自己充填）
- VQ-3 要件: EP-06a → 1998年 Matsubara et al. JACS（計算的充填、技術駆動）
- VQ-3 要件: EP-03a → 1998年 Chatani/Kakiuchi Chem. Lett.、JACS（自己充填）
- VQ-3 要件: EP-04a → 1998–2001年 Kakiuchi et al.（自己充填、部分充填）
- VQ-4 要件: EP-09a → 2000年代（間接的充填のみ、未確定）
- VQ-N/なし: EP-08a → 未充填（インセンティブ構造的）

**階層-時間対応の評価：**

「VQ階層が上がるほど充填に要する時間が長くなる」という仮説は、本事例では概ね支持される。VQ-2要件（EP-01a：報告形式、EP-07a：境界テスト）は1–2年以内に充填された。VQ-3要件（EP-03a：中間体観測、EP-04a：KIE実験、EP-06a：類似系モデル検証）は5年以内（1998年前後）に前進した。VQ-4要件（EP-09a）は定量的比較という性格から充填が遅く・不完全であり、EP-08aは未充填のまま残っている。ただしEP-01aとEP-05aが同一論文（BCSJ 1995）でバンドル充填されたことは「VQ-2とVQ-3の境界が1つの論文で同時に前進した」例外的ケースとして記録しておく必要がある。

**特筆すべきパターン：**

1. **自己充填の集中**: 充填論文の大半がMurai/Chatani/Kakiuchi大阪大学グループ自身によるものであり、自己充填パターンが支配的。これは「発見グループが機構解明も独占した」フィールド構造を示す。
2. **format-driven自動解消**: EP-01a（reporting coherence）はLetter→Full Articleという形式変化によって自動的に解消されており、充填動機はEPの内容への科学的関心ではなく出版慣行による。
3. **計算-実験充填のシフト**: EP-06a（RI-06: Imported model）は実験的充填よりも計算充填（Matsubara-Morokuma 1998）が先行している。これはDFT計算の普及（1990年代後半）という技術障壁の解消が充填タイミングを決定した事例であり、**技術駆動充填**パターンに相当する。
4. **インセンティブ逆転**: EP-08a（統計的信頼性）という低VQ要件のEPが最も充填されにくく、EP-06a・EP-03a等の高VQ要件が相対的に早期に充填されているパターンが見られる。これは「VQ階層と出版インセンティブの方向性の逆転」を示す。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

EP-08a [Replication / uncertainty pack]:
* **未充填の理由**: **インセンティブ構造的未充填** — Murai 1993のGC収率データ（13例）のSD付き再現実験・校正プロトコル開示を目的とした独立論文は存在しない。後続のBCSJ 1995（Full Article）でも単離収率・実験条件の詳細化は達成されたが、元データの統計的信頼性評価（SD付き収率、校正曲線データ）という要件は追求されなかった。出版慣行として「検証実験」「追試」は独立論文化されにくく、技術的に可能であっても独立論文としてのインセンティブが存在しない。
* **発見的意義**: あり — Murai反応は後続30年間で合成化学の標準手法となり数千件の応用論文が発表されたが、基礎となる元データの統計的信頼性は一度も独立論文として検証されていない。「最も成功した触媒反応のうちの1つ」の元データが統計的に未検証であるという逆説は、「成功が検証需要を抹消する」Success-driven question erasure メカニズムの明確な事例として記録できる。
* **将来の充填可能性**: 低 — 現在でも技術的には充填可能（元反応系での再現実験を実施するだけ）だが、科学コミュニティの検証需要が失われており、独立論文としての充填見込みは低い。教科書掲載・標準反応化がさらに検証動機を低下させている。

EP-09a [Internal benchmark pack]（部分未充填）:
* **未充填の理由**: Jordan & Taylor (1989) / Moore et al. (1992) とのTOF値の同条件比較という要件は、「異なる実験室・異なる時代の論文間の条件補正比較」という困難さのため独立研究対象になりにくかった。また1990年代中頃からフィールドが急速に発展したため、1993年時点の比較文脈（Zr系・Ru/pyridine系との比較）自体が科学的関心から外れていった可能性がある。
* **発見的意義**: あり（限定的）— 「最高水準のTOF」という優位性主張の数値的根拠が最終的に独立論文で検証されなかったことは、C-2（dropped quantitative benchmark）として記録された問いが未充填のまま残ったことを示す。
* **将来の充填可能性**: 低 — 比較対象となった先行反応系への関心が現在では低く、retroactiveな数値比較論文の発表見込みはない。

```
inference_time_sec: not available — inject externally
```
