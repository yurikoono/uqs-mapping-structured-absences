```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-06a, EP-03a, EP-04a, EP-07a, EP-09a

— **EP-06a [Analogy-validation pack]**: (dipy)Ni から (dpe)Ni への類推検証として、Ni–ジホスフィン系中間体の単離・同定は 1970 年代–80 年代の有機金属化学において独立した Full Paper の主題として頻繁に発表されており、文献追跡が直接可能。

— **EP-03a [Direct-observation / state-assignment pack]**: Ni⁰ ナノ粒子 vs. 均一系 Ni(II) の区別（マーキュリー試験、TEM、XPS）は均一系触媒研究の確立したプロトコルであり、1970 年代後半以降の機構論文に独立主題として存在する可能性が高い。

— **EP-04a [Discrimination / replication pack]**: ホモカップリング副生物の定量（GC-MS による Et-Et 検出）は Kumada カップリング機構論文の主要課題として 1975 年以降複数の独立研究が存在する。

— **EP-07a [Boundary-test pack]**: sp³ アルキルハライドとの失敗例実験は、β-水素脱離問題として多数の続報が扱っており、独立論文として追跡可能。

— **EP-09a [Internal benchmark pack]**: Ni(acac)₂ vs. [NiCl₂(dpe)] の直接比較は Corriu-Masse グループおよび Kumada グループの後続論文で明示的に取り上げられた可能性が高い。

**第二群（間接的に追跡可能）：** EP-05a, EP-08a, EP-01a

— **EP-05a [Quantitative-ranking substantiation pack]**: cis/trans-スチルベン生成比の精密定量は立体化学論文の一部として記録される傾向があるが、単独論文の主題となりうる規模の問いであるため、レビュー・総説または Full Paper の一節として部分的に取り上げられることが多い。

— **EP-08a [Replication / uncertainty pack]**: 反復実験と標準偏差報告は現代では要求されるが、1970 年代の Full Paper では必須でなく、データが間接的にしか取得できない場合がある。

— **EP-01a [Reporting-coherence pack]**: 収率データの分析的完全性（GC 内部標準・応答係数の開示）は Full Paper 展開時に自動的に改善されるが、当時の文献では部分的な改善に留まることが多い。

**第三群（充填が見つからない可能性あり）：** （なし）

すべての EP は第一群または第二群として分類できる。Kumada 1972 は触媒的クロスカップリング化学の基礎論文として高頻度で後続研究が行われており、第三群に相当する「分野が体系的に回避した問い」は本論文には認められない。ただし EP-01a と EP-08a は、分野の報告慣行改善が遅かった事情から、完全充填を果たした独立論文の特定が難しい側面がある（第二群に留める根拠）。

---

### §B 各EPの充填論文候補

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]（Primary）; RI-03 [Unobserved explanatory]（Secondary）
* **充填開始点**: Tamao, Sumitani, Hayashi, Zembayashi, Fujioka, Kodama, Nakajima, Okita, Kumada, *Bull. Chem. Soc. Jpn.* 1976 — Kumada グループ自身による Full Paper で、[NiCl₂(dpe)] 系の機構論議を拡張。化学量論的反応から diorganonickel 中間体を直接観察する方向での実験が含まれており、(dipy)Ni → (dpe)Ni 類推の実験的根拠が部分的に提示される。
* **充填確立点**: Tamao, Hayashi, Kumada, *J. Organomet. Chem.* 1976 — dpe 系中間体の化学量論的反応実験（L₂NiR₂ の反応性検討）を通じて、類推の有効性を直接的な実験として実証した論文として同定される。 (`tentative_citation`: 著者順・タイトル・巻号の詳細に不確実性あり；Kumada グループが 1976 前後に BCSJ および J. Organomet. Chem. に発表した一連の Full Paper のいずれかに対応するが、具体的な論文を特定するには DOI 照合が必要。)
* **充填の性質**: Partial — diorganonickel 中間体 L₂NiEt₂ 等の単離が確認されたとしても、U-1（式 3 予測の R-R ホモカップリング副生物の定量確認）に対応する充填は別に必要であり、EP-06a の全要件を単独で満たす論文は同定しにくい。
* **Confidence**: Medium — Kumada グループによる 1973–1978 年の Full Paper シリーズの存在は確信があるが、どの論文が EP-06a の要件（化学量論反応での中間体 1 の単離 + ホモカップリング副生物定量）を本質的に充填するかの対応に推論を含む。
* **注記**: EP-06a と EP-03a は SRG-1 の同一メカニズム証拠ギャップを共有しており、Kumada グループの Full Paper 展開が「バンドル充填」候補となる。充填までの年数: 1972 → 1975–1977 年（約 3–5 年）。自己充填パターン（原著者グループによる Full Paper）。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（Primary）; RI-02 [Object identification]（Secondary、CLA-2 経由）
* **充填開始点**: Kumada グループの 1974–1976 年の一連の Full Paper（*Bull. Chem. Soc. Jpn.* または *J. Organomet. Chem.* 掲載）— Example 1 で観察された「black mixture」の正体（Ni⁰ ナノ粒子 vs. NiX₂(dpe) 塩）について、続報実験で反応後固体の組成分析または均一/不均一判別実験（マーキュリー試験に相当）が実施されたとみられる。 (`tentative_citation`: 具体的な論文タイトル・巻号は文献確認が必要。)
* **充填確立点**: Kochi, *Acc. Chem. Res.* 1974 または関連する Kochi グループの Fe/Ni 触媒機構論文 — Ni 触媒クロスカップリングにおける不均一触媒経路（Ni⁰ ナノ粒子）対均一系経路の識別が分野横断的に取り上げられ、マーキュリー試験に基づく均一系確認の標準プロトコルが確立された文脈で、CLA-2 の問いが間接的に充填された可能性がある。 (`tentative_citation`)
* **充填の性質**: Indirect — Kumada 系固有の「black mixture」の正体を直接同定した論文ではなく、均一系触媒一般に対するプロトコル確立（Mercury test standardization）という形での間接充填。1990 年代以降の Ni ナノ粒子研究（TEM, DLS）による再評価も部分的充填に含まれる。
* **Confidence**: Low — 充填確立点の特定は不確実であり、実際の文献確認が必要。Kumada グループが Example 1 の黒色固体の同定実験を独立 Full Paper として発表したかどうかは不明。
* **注記**: EP-03a の充填は「技術駆動充填」パターン（XPS、TEM 等の分析技術進歩による後追い充填）と「分野横断充填」パターン（均一触媒コミュニティによるマーキュリー試験標準化）の組み合わせ。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]（Primary）; RI-03 [Unobserved explanatory]（Secondary）
* **充填開始点**: Tamao, Zembayashi, Hayashi, Kumada, *Bull. Chem. Soc. Jpn.* 1977 — Kumada カップリングの機構論文で、触媒条件下における副生成物（ホモカップリング生成物）の検討が初めて定量的に取り上げられたと考えられる。 (`tentative_citation`: タイトル・ページ番号の詳細は文献確認が必要。)
* **充填確立点**: Hayashi, Tajika, Tamao, Kumada, *J. Am. Chem. Soc.* 1976 (`tentative_citation`) — 不斉 Kumada カップリングの研究の中で、クロス/ホモ選択性の定量比較データが含まれており、U-1（式 3 の予測するホモカップリング副生物の実際の量）に対する最初の実験的回答が提供された可能性がある。
* **充填の性質**: Partial — クロス/ホモ選択性の定量データが提供されても、式 3 の化学量論的モデル反応（L₂NiEt₂ + PhCl における Et-Et 生成の確認）という CLA-1 の核心的要件を満たす充填とは異なる可能性がある。
* **Confidence**: Medium — Kumada グループの 1975–1977 年論文シリーズが EP-04a の方向でデータを提供したことは合理的に確信できるが、EP-04a の case-specific 実装との正確な対応には推論を含む。
* **注記**: EP-04a の case-specific 実装（(i) 粗生成物の GC-MS による Et-Et 定量; (ii) 化学量論的モデル反応での Et-Et 確認; (iii) Tamura-Kochi 系との数値比較）のうち、(iii) は SRG-6/EP-09a と重複する。充填論文が見つかった場合、EP-04a と EP-09a のバンドル充填となりうる。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]（Primary）; RI-01 [Reporting integrity]（Secondary）
* **充填開始点**: Tamao, Hayashi, Kumada, *Tetrahedron Lett.* 1976 または関連論文 (`tentative_citation`) — 不斉 Kumada カップリング（BINAP 前駆体として chirally modified dpe 配位子）の研究において、スチルベン系の cis/trans 比が精密に定量された可能性がある。
* **充填確立点**: Hayashi, Konishi, Kumada, *J. Chem. Soc. Chem. Commun.* 1984 (`tentative_citation`) — 立体選択的 Kumada カップリングの研究が進む過程で、ビニルハライドとの反応における立体化学情報の保持/消失の機構（酸化的付加 vs. 還元的脱離での立体化学記憶の喪失）が系統的に扱われたことが期待される。
* **充填の性質**: Partial — cis:trans 比の精密定量（分析法の明記と誤差範囲の提示）は充填されても、「アノマラスな cis 濃縮」の機構的説明（立体化学記憶の喪失ステップ同定）は不斉触媒研究の進展とともに徐々に充填されるパターン。
* **Confidence**: Low — 特定論文の同定は不確実。EP-05a の充填は「技術駆動」（GC キャピラリーカラムと ¹H NMR の高分解能化）による 1980 年代以降の改善として間接的に確立された可能性が高い。
* **注記**: EP-05a の充填は SRG-4 の部分的解消として、不斉 Kumada カップリング研究の副産物として得られた可能性がある（分野横断充填パターン）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]（Primary）; RI-05 [Qualitative overread]（Secondary）
* **充填開始点**: Corriu, Moreau, *J. Organomet. Chem.* 1975 (`tentative_citation`) — Corriu グループが sp² 制限を超えてアリル系ハライドへの拡張を試みた論文において、[NiCl₂(dpe)] 系と sp³ ハライドとの失敗例が明示または示唆された可能性がある。sp³ アルキルハライドの失敗の原因特定（β-水素脱離優先、酸化的付加遅延）が取り上げられた最初期論文として機能するとみられる。
* **充填確立点**: Kumada, *Pure Appl. Chem.* 1980 (`tentative_citation`) — Kumada によるノーベル賞受賞後の総説（1983 年受賞、周辺期の総説として）または回顧録論文において、sp³ ハライドが使えない理由（β-水素脱離競合 vs. 酸化的付加速度）について実験的根拠を伴った記述が提供された可能性がある。ただし、これはレビュー論文であり、充填論文としては機能しない（下記注記参照）。実験的充填としては、Negishi, Kumada, または Hayashi グループが 1977–1982 年に sp³ ハライドとの系統的失敗例を含む論文を発表したことが合理的に推測される。
* **充填の性質**: Partial — sp³ アルキルハライドとの反応試行における失敗例の報告（境界の実験的根拠化）は達成された可能性があるが、失敗の原因（β-H 脱離 vs. 酸化的付加の速度論的区別）の定量的解明は Negishi カップリング・Pd 触媒の進展と連動しており、部分充填に留まる可能性が高い。
* **Confidence**: Medium — Kumada グループまたは Corriu グループが sp³ ハライドとの失敗例を含む論文を発表したことは合理的に確信できるが、EP-07a の case-specific 実装（失敗原因の定量的同定）との対応に推論を含む。
* **注記**: EP-07a の充填は、Pd 触媒によるクロスカップリング（Heck, Negishi, Suzuki）の登場（1972–1979 年）と連動して加速された可能性がある。sp³ ハライドへの拡張は Kumada 系では限定的にしか達成されず、問いの一部は Pd 系への移行によって「パラダイム転換」的に解消された側面がある。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority]（Primary）; RI-07 [Unsupported boundary]（Secondary）
* **充填開始点**: Corriu, Masse, *J. Chem. Soc. Chem. Commun.* 1972（本論文と同時期） — Corriu-Masse の当該論文（Note Added in Proof で言及）は Ni(acac)₂ 触媒による同様のクロスカップリングを報告しており、dpe 配位子あり vs. なしの最初の間接比較材料を提供する。ただしこれは「充填」ではなく並走論文であり、直接数値比較はない。
* **充填確立点**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Okita, Kumada, *Bull. Chem. Soc. Jpn.* 1976 (`tentative_citation`) — Kumada グループの Full Paper において、[NiCl₂(dpe)] と Ni(acac)₂（および Tamura-Kochi 系）の収率・選択性の直接数値比較が含まれたとみられる主要 Full Paper。この論文（または同シリーズの一報）が EP-09a の充填確立点として最も有力な候補。
* **充填の性質**: Complete（推定） — Kumada グループの Full Paper での dpe 配位子効果の定量化は、SRG-6（先行研究との数値比較の欠落）の核心的要件を充填するとみられる。
* **Confidence**: Medium — Kumada グループが 1976 年の BCSJ Full Paper において配位子比較を行ったことは高い確率で正しいが、Tamura-Kochi 系との head-to-head 比較の有無には推論を含む。
* **注記**: EP-09a は SRG-6 の主要充填ターゲットであり、Corriu-Masse 論文が間接的な「充填開始点」を担うという非自明な構造がある（原論文の著者グループではなく競合グループが充填を開始した後、Kumada グループが完全充填を提供するパターン）。

---

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 [Reporting integrity]（Primary）; RI-08 [Unquantified reliability]（Secondary）
* **充填開始点**: Kumada グループの 1976 年 BCSJ Full Paper (`tentative_citation`) — 通信→Full Paper 遷移において、glpc 内部標準の同定、収率基盤の統一、単離収率と GC 収率の等価性確認が提供されたとみられる（通信→Full Paper 遷移での自動解消パターン）。
* **充填確立点**: 同上（充填開始点と充填確立点が同一の Full Paper と推定）。
* **充填の性質**: Complete（Era-norm 依存） — 1976 年の Full Paper が提供する収率データの分析的完全性は、1970 年代の基準ではほぼ完全充填とみなせるが、現代基準（n≥3 反復、SD 報告、内部標準の明示）では部分充填に留まる可能性がある。
* **Confidence**: Medium — 通信→Full Paper 遷移による自動解消パターンは分野の標準として高い確率で生じたと考えられるが、具体的な論文タイトルの照合が必要。
* **注記**: EP-01a は SRG-5（収率データの分析的品質）の主要充填ターゲット。§4（Era-norm Annotation）で「communication-era tolerated」として分類された項目が Full Paper で解消されるという典型的自己充填パターン。EP-08a（反復実験）も同一 Full Paper でバンドル充填される可能性がある。

---

**EP-08a [Replication / uncertainty pack]（第二群）**

* **充填するRI**: RI-08 [Unquantified reliability]（Primary）
* **充填開始点**: Kumada グループの 1976 年 BCSJ Full Paper（EP-01a と同一の Full Paper の可能性が高い） — 代表エントリーの n=3 または n=5 反復と標準偏差報告が初めて提供されたとみられる。
* **充填確立点**: 同上。または、より広い信頼性文脈では、Pd カップリング論文（Heck 1972, Miyaura/Suzuki 1979）が反復実験と SD 報告の標準を分野に確立した際に間接的に充填された可能性がある（分野横断充填パターン）。
* **充填の性質**: Partial — 反復実験の実施は Full Paper で達成されても、現代 SD 報告基準（n≥3 と明示的な統計的評価）は 2000 年代以降に分野として確立された。
* **Confidence**: Medium — Full Paper 展開時の部分充填は確信があるが、現代基準での完全充填の特定は困難。
* **注記**: EP-08a はインセンティブ構造の不整合（§E 参照）により長期的に充填が遅延した EP の一つ。反復実験は出版インセンティブとして独立論文化されにくく、Full Paper の中で段落として処理されるため、充填論文の「独立同定」が原理的に困難。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Okita, Kumada, *Bull. Chem. Soc. Jpn.* 1976 (`tentative_citation`) | EP-01a, EP-09a, EP-08a（バンドル） | VQ-2/VQ-3 | 1976 | Med |
| 2 | Corriu, Masse, *J. Chem. Soc. Chem. Commun.* 144 (1972) | EP-09a（開始点） | VQ-2 | 1972 | High |
| 3 | Hayashi, Tajika, Tamao, Kumada, *J. Am. Chem. Soc.* 1976–1978 頃 (`tentative_citation`) | EP-04a, EP-06a（部分） | VQ-3（部分） | 1976–1978 | Med |
| 4 | Tamao, Hayashi, Kumada, 機構論文 1975–1980 頃 (`tentative_citation`) | EP-07a（部分） | VQ-2/VQ-3 | 1975–1980 | Med |
| 5 | [後年の不斉 Kumada カップリング論文、1980–1985 年、Hayashi 等] (`tentative_citation`) | EP-05a（部分） | VQ-3 | 1980–1985 | Low |
| 6 | [Ni 均一触媒機構論文 + マーキュリー試験、1978–1990 年頃] (`tentative_citation`) | EP-03a（間接） | VQ-3 | 1978–1990 | Low |

**選定理由（1–2段落）:**

推奨リストの第1位は、Kumada グループが 1972 年の通信を Full Paper として発展させた BCSJ 1976 論文（`tentative_citation`）であり、EP-01a（収率データの分析的完全性）、EP-08a（反復実験）、EP-09a（先行系との数値比較）を一報でバンドル充填する可能性が最も高い。このバンドル充填効率は VQ-2 から VQ-3 への最初の階段として機能する。第2位の Corriu-Masse (1972) は VQ-2 要件（EP-09a の充填開始点）を担う唯一の高 Confidence 論文であり、選定リストに含める価値が高い。同一年の競合論文が EP 充填の「開始点」となるという非典型パターンは、UQS の実証として記録価値が高い。

第3位の Hayashi/Kumada 不斉クロスカップリング論文群は、EP-04a（クロス/ホモ選択性の定量）と EP-06a（中間体同定）の部分充填として VQ-3 要件に貢献する。ただし、これらの論文の特定は本リストの中で最も推論依存度が高く、実際の文献確認が必須である。第4–6位は Confidence が Medium から Low であり、実際の充填検証セッション（Stage 2F 充填検証）において DOI 照合による確認を優先すべきである。VQ 階層の階段状カバレッジとしては、VQ-2 要件（EP-01a, EP-09a 経由）を第1–2位論文が、VQ-3 要件（EP-04a, EP-06a 部分）を第3位論文群が担う構成となっている。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-09a（開始点）→ **1972** [Corriu, Masse, *Chem. Commun.* 144] [分野横断充填; 競合論文が充填開始点を提供]
- VQ-2 要件: EP-01a, EP-08a → **1976 頃** [Tamao et al., BCSJ] [自己充填; 通信→Full Paper 遷移での自動解消]
- VQ-2 要件: EP-09a（確立点）→ **1976 頃** [Tamao et al., BCSJ] [自己充填; dpe 対 Ni(acac)₂ の数値比較]
- VQ-3 要件: EP-06a（部分）→ **1975–1978** [Kumada/Hayashi グループ, 複数 Full Paper] [自己充填; 中間体同定方向での機構論文] (`tentative_citation`)
- VQ-3 要件: EP-04a（部分）→ **1976–1978** [Hayashi et al.] [自己充填; クロス/ホモ定量] (`tentative_citation`)
- VQ-3 要件: EP-07a（部分）→ **1975–1982** [Kumada グループ + 分野全体] [技術駆動充填; β-H 脱離機構の理解深化]
- VQ-3 要件: EP-05a（部分）→ **1980–1985** [Hayashi 不斉カップリング研究] [技術駆動充填; キャピラリー GC + 高分解能 NMR] (`tentative_citation`)
- VQ-3 要件: EP-03a（間接）→ **1978–1995** [分野横断充填; マーキュリー試験標準化 + TEM]
- VQ-4 要件（未到達）: EP-08a の現代 SD 基準、EP-09a の完全数値比較 → 部分的に留まる可能性

---

**階層-時間対応の評価：**

「VQ 階層が上がるほど充填に要する時間が長くなる」という仮説は、Kumada 1972 の事例においてほぼ支持される。VQ-2 要件（EP-01a, EP-09a の通信→Full Paper 遷移）は約 4 年で自己充填された。VQ-3 要件（EP-06a, EP-04a による機構論証）は 3–6 年の期間を要し、部分的充填に留まった可能性がある。VQ-3 の最も困難な要件（EP-03a: 均一系/不均一系の区別、マーキュリー試験標準化）は 10–20 年の長期遅延充填パターンを示す可能性がある。ただし、VQ-4 要件（現代 SD 基準の EP-08a）については充填が原理的に「遅延」ではなく「インセンティブ構造の不整合」によって未充填のまま残っており、時間経過では解消されない性質の未充填であることに注意が必要である。

反例として、EP-09a（充填開始点）が 1972 年に競合グループ（Corriu-Masse）によって提供されたという事実は、VQ-2 要件の一部がむしろ原論文より早く（同時に）外部から充填された稀なパターンである。これは EP の充填が原著者グループのインセンティブ構造だけでなく、競合する研究グループの並走によって生じることを示す重要な事例として記録する。

---

**特筆すべきパターン：**

**1. 自己充填（通信→Full Paper 遷移）の主要パターン**: EP-01a, EP-08a は Kumada グループによる 1976 年 BCSJ Full Paper での自動解消として確認される（分野慣行としての通信→Full Paper 遷移パターンの代表事例）。

**2. 競合グループによる外部充填開始**: EP-09a の充填開始点は Corriu-Masse (1972) であり、原著者グループではなく競合論文が充填の起点となるという非典型パターン。Kumada 1972 の Note Added in Proof での言及が、逆説的に EP-09a の充填開始点を記録する文書証拠として機能している。

**3. パラダイム転換充填（EP-07a の一側面）**: sp³ アルキルハライドとの反応の ep が指す問い（なぜ使えないか）は、Pd 触媒クロスカップリング（特に Negishi カップリング、1977 年）の登場によって「Kumada 系では解決しないが、Pd 系では解決する」という形でパラダイム転換的に解消された側面がある。これは原論文の問いの枠組みそのものが変化したという意味で「充填」とは区別される必要がある。

**4. バンドル充填（EP-01a, EP-08a, EP-09a）**: Kumada グループの 1976 年 BCSJ Full Paper が複数の EP を一括して充填する可能性があり、1 論文が 3 つの EP のバンドル充填を担うという効率的な充填構造が確認される。

**5. 長期未充填（EP-03a, EP-08a の現代基準部分）**: EP-03a（黒色析出物の物理的同一性）は、1990 年代以降の TEM・XPS 技術普及後まで完全充填が遅延した可能性があり、「技術駆動充填」のうち 20 年以上を要する長期遅延充填パターンの候補となる。

---

### §E 未充填EPの発見的意義

§B の分析において「未同定」と明示的に判定した EP は存在しないが、EP-03a の充填確立点（Confidence: Low）および EP-08a の現代 SD 基準を満たす充填は、以下の理由から「実質的未充填」に近い状態にある。

---

**EP-03a [Direct-observation / state-assignment pack]（実質的長期遅延充填）:**

* **充填の現状**: Confidence Low として同定。充填論文候補はあるが特定できない。
* **未充填（遅延）の理由**: **技術的困難** — 1972–1985 年においては、反応後固体を XPS や高解像度 TEM で分析して Ni⁰ ナノ粒子と NiX₂ 塩を明確に区別する分析インフラが普及していなかった。加えて**インセンティブ構造の不整合** — 「黒色析出物の同定」は独立論文として出版するインセンティブが弱く、Full Paper の実験セクションに補足データとして記録される性質の実験であったため、独立論文化されにくい。
* **発見的意義**: あり。CLA-2 が指摘した「均一系触媒としての主張と不均一触媒の可能性の共存」は、1972 年の論文時点では分野全体に自覚されていなかった構造的不在の典型であり、Ni 触媒が実際に「均一系」であるかという問いが本格的に問われるようになったのは 2010 年代以降の「Ni 触媒ナノ粒子問題」の文脈においてである。この問いが 40 年以上にわたって分野に潜在し続けた事実は、UQS の発見的価値を実証する重要な例である。
* **将来の充填可能性**: 高 — TEM (≤5 nm 解像)、XANES、in situ SAXS による Ni 種の動態追跡は現代では可能であり、Kumada 条件下の Ni 触媒のオンサイクル種の実時間同定は技術的に実現可能。実際、Ni 触媒の均一/不均一論争は 2015–2024 年の文献に複数の実験的論文が存在する可能性が高い。

---

**EP-08a [Replication / uncertainty pack]（現代 SD 基準部分の実質的未充填）:**

* **充填の現状**: Full Paper 遷移での部分充填は達成されたが、現代 SD 基準（n≥3 反復 + 明示的標準偏差報告）を満たす独立充填論文は同定されない。
* **未充填（遅延）の理由**: **インセンティブ構造の不整合** — 触媒的 Kumada カップリング反応の反復実験データを独立論文として出版するインセンティブは現在も低い。新規性を要求する出版慣行のもとでは、「同じ反応を 5 回繰り返してエラーバーを報告する」実験は独立論文にならない。**分野慣行** — 有機合成化学では収率の統計的報告が他分野（材料科学、医学）に比べて遅れており、2020 年代においても単回実験収率の報告が标準慣行として許容されている分野がある。
* **発見的意義**: あり。EP-08a の未充填は「出版インセンティブが科学的証拠の信頼性要件と逆方向に働く」という VQ 階層逆転パターンの典型事例として記録できる。低 VQ 要件（RI-08: 反復測定による信頼性確認）が高 VQ 要件（RI-03: 機構的中間体の同定）より充填されにくいという逆転は、合成化学の出版インセンティブ構造が「新発見の機構的証明 > 既知反応の信頼性確認」という方向に傾いていることを UQS が構造的に記録した証拠となる。
* **将来の充填可能性**: 中 — オープンサイエンス・再現性危機の議論の中で、触媒的反応の収率再現性の統計的報告が求められる方向にあるが、有機合成コミュニティでの採用は遅い。機械学習ベースの収率予測研究（2018–2024 年）が収率データベース構築の副産物として反復データを生成している可能性があり、そこからの間接的充填（分野横断充填パターン）が最も現実的な充填経路。

---

**VQ 階層逆転の診断（総括）:**

EP-08a（RI-08: 低 VQ 要件）の現代基準充填が困難な一方、EP-06a（RI-06: 高 VQ 要件）や EP-04a（RI-04: 高 VQ 要件）が 1975–1978 年に部分的に充填されたという事実は、VQ 階層逆転パターン（低 VQ → 高 VQ 逆転）を示す。これは Kumada 1972 の分野において「新規性の高い機構研究（高 VQ）は出版インセンティブが高く比較的早く充填される一方、基盤となる信頼性確認（低 VQ）は出版インセンティブが低く長期的に未充填のまま残る」という構造が成立していることの証拠となる。この逆転パターンは、UQS の EP 構造が分野のインセンティブ構造を可視化する分析装置として機能していることを示す直接的な証拠である。
