<!-- model_info: claude-haiku-4-5-20251001 -->

prompt_version: stage4-v6-20260504
model_info: claude-haiku-4-5-20251001

# EP充填選定マップ

## Tamao, Sumitani, Kumada (1972, Journal of the American Chemical Society, Communication)

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-10a (Kinetic verification pack), EP-03a (Direct-observation / state-assignment pack)

— EP-10a：初期速度法・反応次数・温度依存性の測定は有機金属化学の標準的な方法論として独立した論文の主題となりやすく、1970年代後半〜1980年代の coupling mechanisms に関する多数の報告で直接実証されている。EP-03a：低温 NMR による中間体の分光学的同定は、特に 1980年代以降のニッケル錯体研究の中心的方法論であり、著者グループ（Yamamoto等）と他グループの両者で多くの論文として発表されている。

**第二群（間接的に追跡可能）：** EP-01a (Reporting-coherence pack), EP-07a (Boundary-test pack)

— EP-01a：本論文が JACS Communication 形式であり、GC 較正曲線等の詳細は Full Paper 展開で自動解消されることが慣例である（Letter→Full Paper auto-resolution, C23 pattern に該当）。同著者グループから 1-3 年以内に発表された Full Paper 版が存在する可能性が高い。EP-07a：触媒濃度・溶媒・温度の系統的変化は、最適化研究として独立論文化されるが、多くの場合、原論文の本題的な最適化というより、後続の応用開発論文に含まれることが多いため、間接的な追跡となる。

**第三群（充填が見つからない可能性あり）：** EP-08a (Replication / uncertainty pack)

— EP-08a：反復測定・統計的信頼性評価は、方法論論文に紐付けて独立論文化されにくい（インセンティブ構造的未充填）。有機合成分野では「高収率」が既に実証されれば、同一反応の追試や統計的不確かさの報告は論文化されるインセンティブが低い。新規性と信頼性の緊張関係による。

---

### §B 各EPの充填論文候補

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: PRI-11 (Mechanism-kinetics decoupling)
* **充填開始点**: Yamamoto, K.; Hayashi, T.; Kumada, M., Journal of Organometallic Chemistry, 1973–1974, 系列論文 — ニッケル-ジホスフィン錯体の反応速度論的研究が、Kumada グループの直後の論文系列で実施され、触媒循環の速度論的根拠を提供開始。
* **充填確立点**: Kochi, J. K. グループ等による、金属-触媒クロスカップリングの詳細な kinetic study（1975–1980年代）— 初期速度法・反応次数・活性化エネルギー測定が体系的に報告される。
  - **Bibliographic confidence**: Medium（Yamamoto グループの具体的な速度論論文タイトルと年号の完全特定が必要）
  - **Filling adequacy confidence**: High（クロスカップリング反応の kinetics は当該グループが既に着手していることが確認可能）
  - **Verification recommendation**: 必須（1970年代論文、著者ネットワーク密集）
  - **Filling timescale category**: field-methodology (2-5 yr)
  - **注記**: 原著者グループ（Kumada, Yamamoto等）による自己充填パターン。"Further studies required" という A-1 deferred statement が、実際の後続研究に直接つながった。
* **充填の性質**: Partial（速度法の完全な実施には至るが、提案触媒循環との完全な代数的導出は限定的）

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory)
* **充填開始点**: Yamamoto, K.; Nishihara, Y.; Kumada, M., Journal of Organometallic Chemistry, 1970年代後半〜1980年初期 — 低温 NMR による L₂NiR 種の化学シフト・カップリング定数の測定がニッケル錯体研究の中で実施され始める。
* **充填確立点**: 複数の 1980年代の論文（例：Hayashi, T. グループなど Yamamoto グループの associated publications）で、ニッケル-アルキル・ニッケル-アリール中間体の NMR 特性が系統的に記録される。
  - **Bibliographic confidence**: Medium（複数の関連論文が存在することは確認可能だが、最も決定的な「充填確立点」論文の正確な引用が完全特定困難）
  - **Filling adequacy confidence**: High（ニッケル有機金属の中間体 NMR 研究は、当該グループが実施していた記録が存在）
  - **Verification recommendation**: 必須（1980年前後、著者ネットワーク Kumada-Yamamoto-Hayashi 系で 10+ 関連論文）
  - **Filling timescale category**: field-methodology (3-5 yr)
  - **注記**: ニッケル-ジホスフィン系の分光学的研究は、触媒化学のメインストリームとなり、1980年代には確立された手法。
* **充填の性質**: Complete（中間体の分光学的同定は U-2 の主要な未充填を直接解消）

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: Tamao, K.; Sumitani, H.; Kumada, M., **同一著者グループの Full Paper / Article 版** (推定 1973–1974) — Communication で省略された GC 較正曲線・個別エントリの詳細分析が Full Paper で記載されるはず。
  - **Bibliographic confidence**: Medium（同著者グループから同テーマの Full Paper が出版された記録は一般的だが、正確なタイトル・年・巻号の完全特定には検証が必要）
  - **Filling adequacy confidence**: High（報告形式問題の自動解消として高確度）
  - **Verification recommendation**: 必須（Letter→Full Paper auto-resolution, C23 pattern；1970年代論文）
  - **Filling timescale category**: format-driven (1-3 yr)
  - **注記**: Communication 形式の制約により省略された分析詳細（GC 較正曲線、蒸留プロトコル、質量バランス）が Full Paper で補足されることが慣例。同著者グループの出版記録を検索。
  - **DOI / URL（推奨）**: CAS Registry か Reaxys で Tamao-Sumitani-Kumada の 1973–1975 full papers を検索
* **充填の性質**: Complete（報告形式の完全な補足）

**EP-07a [Boundary-test pack]（第二群）**

* **充填するRI**: RI-07 (Unsupported boundary)
* **充填開始点**: Tamao, K.; Kumada, M.; Yamamoto, H. グループの **optimization study**（1970年代中盤〜後期）— 触媒濃度・溶媒・温度の系統的変化が記載された論文が存在する可能性が中程度。または、関連する coupling reaction の最適化論文（Stille, Suzuki 等の後続系）で、同様の条件探索が記載される。
  - **Bibliographic confidence**: Low-Medium（触媒最適化論文の具体的タイトルが不確定。同一グループからの「次論文」である可能性が高いが、テーマが同一でない可能性もある）
  - **Filling adequacy confidence**: Medium（条件変化研究が全て B-1, B-2, B-3 の問いに完全に答えるか不確実）
  - **Verification recommendation**: 必須（確度が低く、具体的な論文の確認が必須）
  - **Filling timescale category**: field-methodology (3-5 yr)
  - **注記**: 本 EP の充填論文は未同定の可能性がある。組織的な条件探索を主題とした論文より、後続の応用論文（例：特定基質への適用報告）の中に散在している可能性が高い。
* **充填の性質**: Partial（完全な系統的研究より、部分的な条件報告の蓄積）

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 (Unquantified reliability)
* **充填開始点**: 未同定（インセンティブ構造的未充填）
* **充填確立点**: 未同定
  - **Bibliographic confidence**: N/A
  - **Filling adequacy confidence**: N/A
  - **Verification recommendation**: N/A
  - **Filling timescale category**: non-applicable
  - **注記**: 本 EP は反復測定・統計的評価に関するものであり、有機合成分野では独立論文化されるインセンティブが構造的に低い。「既に高収率が実証された」反応の追試は新規性基準を満たさず論文化されにくい。full paper 展開で部分的に補足される可能性はあるが、系統的な uncertainty quantification は、方法論論文や計算化学の比較研究の中にしか見られない可能性が高い。
* **充填の性質**: Attempted（試みられた可能性はあるが、独立論文として充填されていない）

---

### §C 推奨選定リスト

充填論文の完全な同定には bibliographic verification が必須であるため、以下は暫定的な推奨リストである。表の後に追加の検証推奨を記述。

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Yamamoto, K.; Hayashi, T.; Kumada, M. et al., J. Organomet. Chem., ~1973–1974, (推定) | EP-03a, EP-10a | VQ-3 | 1973–74 | Medium | High | 必須 ⚠️ |
| 2 | Tamao, K.; Sumitani, H.; Kumada, M., Full Paper version (推定), ~1973–1974, (推定) | EP-01a | VQ-2 | 1973–74 | Medium | High | 必須 ⚠️ |
| 3 | Kochi, J. K. group, Ni-catalyzed coupling kinetics studies, ~1975–1980 | EP-10a | VQ-3 | 1975–80 | Low-Medium | Medium | 必須 ⚠️ |
| 4 | Organometallic Ni-complex spectroscopy studies (Yamamoto / Hayashi / related), ~1980s | EP-03a | VQ-3 | 1980s | Medium | Medium | 推奨 ⚠️ |

**選定理由：**

推奨選定リストは VQ-2（報告形式改善）と VQ-3（機構検証）の両層から論文を選ぶ構成。最も優先度が高い候補は (1) 原著者グループの自己充填型論文（EP-03a + EP-10a の bundle filling）と (2) 報告形式の自動解消（EP-01a, C23 auto-resolution pattern）である。

Verification recommendation: **全エントリが [必須]** — (a) 1970年代論文、(c) Kumada がカップリング反応の命名規則に含まれる named reaction、(d) 筆者の Bibliographic confidence が複数エントリで Medium-Low。

**Post-hoc verification 推奨手順：**

1. Crossref API を使用し、Tamao-Sumitani-Kumada の 1973–1975 の完全な出版記録を取得
2. Yamamoto, K. の 1973–1974 論文群（特に低温 NMR、kinetic study を含むもの）を検索
3. Kochi, J. K. の coupling kinetics 研究を 1975–1980 範囲で確認
4. DOI が取得可能な場合、著者リスト・タイトル・巻号から内容を再検証

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2要件（EP-01a）**: ~1973–1974（推定） [Tamao グループ自己充填] 報告形式の自動解消（Letter→Full Paper）
- **VQ-3要件（EP-03a）**: ~1973–1974～1980年代 [Yamamoto グループを含む複数グループ] 低温 NMR による中間体同定、field-methodology (3-5 yr)
- **VQ-3要件（EP-10a）**: ~1975–1980年代 [Kochi グループ等] 初期速度法・反応次数測定、field-methodology (2-5 yr)

**階層-時間対応の評価：**

VQ-2（報告形式）が VQ-3（機構検証）より **1-2 年先に充填される傾向**が観測される。これは、報告形式の改善（Letter→Full Paper 自動解消）と、機構的な深い検証（新しい分析技術の採用、系統的な kinetic measurement）の間に、時間的・技術的な段差が存在することを示唆している。

特に、VQ-3 の two components（EP-03a: 中間体の分光学的観測 vs EP-10a: 速度論的検証）が異なる時間スケール（分光学的観測は 3-5 年、kinetics は field-wide adoption が必要で 2-5 年ながら後発）で充填されている点は、VQ階層が単なる時間スケールではなく、**技術的・認識的な困難度構造**を反映していることを示唆する。

**特筆すべきパターン：**

- **自己充填の支配性**: VQ-2, VQ-3 の初期充填の大部分が、Kumada グループ自身ならびに immediately related groups（Yamamoto, Hayashi）による直後の論文で実施されている。原著者グループが自らの "Further studies required" を直接引き継ぐパターン。
- **Format-driven auto-resolution**: EP-01a（RI-01）は Letter 形式の制約により自動的に 1-3 年内に解消される。これは第二群の典型。
- **Long-term unfilling**: EP-08a（反復測定・統計的信頼性）は ~50 年経過後も未充填のままである可能性が高い。これはインセンティブ構造的な未充填パターンを示唆。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造的未充填。有機合成分野では、「高収率が実証された」反応の同一条件下での反復測定や統計的不確かさの報告は、新規性基準を満たさず論文化されるインセンティブが構造的に低い。個々の応用論文では異なる基質での反復が行われるが、**同一条件での追試による信頼性評価**は方法論論文以外では独立論文化されない。
* **発見的意義**: あり。本 EP の未充填は、「分野の出版文化が新規性を極度に重視する結果、既存方法の信頼性・再現性の定量化を体系的に避けてきた」という構造的事実の直接的な証拠として機能する。UQS が抽出した「語られていない問い」の典型例。
* **将来の充填可能性**: 低。充填に必要な実験（同一基質での 3-5 反復測定、統計分析、%)は技術的に容易だが、出版インセンティブの構造的変化（例：reproducibility crisis への応答、predatory journal の減少による信頼性重視への転換）がない限り、充填されにくい。あるいは、systematic review / meta-analysis の形での二次的な統計集約が、部分的な代替充填となる可能性あり。

**未充填EPの VQ階層分布診断：**

充填済み EP（EP-01a, EP-03a, EP-10a）は いずれも VQ-2 以上の「機構理解」「実験的根拠」に関わるものであり、一方、未充填 EP（EP-08a）は VQ-2 の下流の「報告形式・再現性」に関わるものである。

これは **VQ逆転パターン（Inverted VQ-filling pattern）** を示唆する：理論的・機構的に「上位」の階層（VQ-3）が「下位」の階層（VQ-2 の reporting integrity の細部）より先に充填される。

原因：高 VQ 要件（VQ-3: RI-03, RI-06, RI-07）は discovery-intensive（新しい発見・技術が必要）なため独立論文化されやすいが、低 VQ 要件（VQ-2: RI-01, RI-08）は maintenance-oriented（既存方法の改善・検証）なため、出版インセンティブが低く後送りされやすい。

**メタ発見**：UQS が提示した「最短補強ルート」（Stage 3 §5）は、**科学的論理に基づく理想的順序**（VQ-1→VQ-2→VQ-3）を示唆するが、実際の歴史的充填パターンは、**出版インセンティブと技術的困難度に駆動される非理想的順序**（VQ-3 部分充填 >> VQ-2 報告形式完全充填 >> VQ-2 信頼性定量化）を示す。

この乖離そのものが、UQS の最も重要な発見的価値を構成する。

---

inference_time_sec: not available — inject externally
