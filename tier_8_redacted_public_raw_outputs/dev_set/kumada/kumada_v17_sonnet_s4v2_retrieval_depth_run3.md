```
prompt_version: stage4-v2
model_info: claude-sonnet-4-6
experimental_variant: retrieval-depth-annotation (Multi-run robustness, v2 run 3)
related_pilot: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Pilot 2, v2 run 1)
note: Multi-run robustness check の v2 第 3 run。Pilot 2 と同 prompt で実行し、
      run 間の retrieval scope と Tier annotation の variance を測定する。
```

---

```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-02a, EP-03a, EP-04a, EP-06a, EP-07a, EP-09a

- **EP-01a (Reporting-coherence pack)**: RI-01（報告形式）由来だが、Kumada グループが 1976 年に Full Paper シリーズを発表しており、独立論文として存在する（デフォルト第三群の例外規則を適用）。
- **EP-02a (Identity/purity substantiation pack)**: 同上。Full Paper で各エントリの個別分析データが提供された。
- **EP-03a (Direct-observation / state-assignment pack)**: RI-03（中間体未観測）に対応；diorganonickel-dpe 中間体の分光学的同定は独立論文の主題として発表されやすく、Kumada グループ・Kochi グループが機構研究を発表。
- **EP-04a (Discrimination / replication pack)**: cis/trans-stilbene 比の速度論/熱力学的制御の区別は立体化学機構論文として独立発表される性質を持つ。
- **EP-06a (Analogy-validation pack)**: RI-06（サイクルレベル輸入）に対応；NiCl₂(dpe)系での化学量論的素反応検証は機構論文の主題として独立発表されやすい。
- **EP-07a (Boundary-test pack)**: RI-07（未サポート境界）に対応；sp²/sp³ハライドのスコープ実験は Full Paper の主要コンテンツとして発表される。
- **EP-09a (Internal benchmark pack)**: RI-09（外部優位性）に対応；Ni(acac)₂ との直接比較は Corriu/Masse 1972 が同時期に発表しており、独立論文として追跡可能。

**第二群（間接的に追跡可能）：** EP-05a

- **EP-05a (Quantitative-ranking substantiation pack)**: RI-05（定性的過大解釈）に対応；クロスカップリング vs. ホモカップリングの質量収支定量は、単独論文の主題ではなく Full Paper・機構論文の一部として報告されやすい。

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a (Replication / uncertainty pack)**: RI-08（定量的信頼性）に対応；反復測定（n≥3）と標準偏差の明示は、出版インセンティブ構造のもとで独立論文化されにくく、分野慣行として未解消のまま残る可能性が高い。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第一群）**

* **充填するRI**: RI-01 [Reporting integrity] + RI-08 [Unquantified reliability]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Uchida, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 同一 Kumada グループによる Full Paper Part I が、Table I の全エントリについて統一されたglpc 条件・収率基準・反応時間を記録し、通信の報告形式問題を自動解消した。
* **充填確立点**: 同上
* **充填の性質**: Complete（通信→Full Paper 自動解消パターン）
* **Confidence**: High
* **注記**: 著者グループ自身による自己充填（self-filling）の典型。S1 の `series_signal: yes`（A-2「Investigations are continuing...」）が明示的に予告していた後続論文。EP-02a、EP-07a 部分も同一論文がバンドル充填。

---

**EP-02a [Identity/purity substantiation pack]（第一群）**

* **充填するRI**: RI-02 [Identity substantiation]
* **充填開始点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full Paper で全Table I 生成物の個別分光データ（NMR、IR、元素分析）が記録され、"and/or" 問題（B-13）が解消された。
* **充填確立点**: 同上
* **充填の性質**: Complete
* **Confidence**: High
* **注記**: EP-01a と同一論文によるバンドル充填。通信→Full Paper 遷移の自動解消パターン（Stage 3 §5 で予告済み）。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点（推定）**: Kumada グループによる機構研究（推定 1973–1977 年）— NiCl₂(dpe)系での化学量論的反応と中間体の部分的特性評価が報告されたと推定されるが、特定の論文タイトル・巻号に確信が持てない。候補：*J. Organomet. Chem.* に掲載された Tamao, K.; Kumada, M. 連名論文（1973–1976 年頃）。
* **充填確立点（推定）**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 7547–7560（推定） — Kochi グループが Ni 触媒クロスカップリングの機構（Ni(0)/Ni(II) vs. Ni(I)/Ni(III) ラジカル経路）を化学量論的実験で検討した。dpe-Ni 系に特有の低温 ³¹P{¹H} NMR による中間体 [Ni(R)₂(dpe)] の直接観測がこの論文またはその後続で達成されたと推定。
* **充填の性質**: Partial（dpe-Ni 系に特化した低温 NMR 観測の達成時期と論文は不確実）
* **Confidence**: Low（充填の方向性は確信できるが、特定論文の書誌情報に高い不確実性）
* **注記**: EP-03a は EP-06a（Analogy-validation）と不可分共起（Stage 3 §6 の RI-06+RI-03 共起パターン）。一方だけの解消では VQ-3 到達に不十分。DB による実際の文献確認が必須。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator] + RI-08 [Unquantified reliability]
* **充填開始点（推定）**: Corriu グループによるビニルハライド/Grignard 立体化学研究（推定 1974–1978 年）— Corriu, R. J. P.; Moreau, J. J. E. *J. Organomet. Chem.* ca. **1975** が、Ni 触媒クロスカップリングにおける cis/trans 生成物比の温度・時間依存性を検討した可能性がある。
* **充填確立点（推定）**: Tamao et al. Full Paper シリーズ（1976–1977 年）の Part II 以降でステレオケミストリーが系統的に扱われた可能性がある。または、Hayashi, T.; Kumada, M. らによるアリールおよびビニルハライドのステレオ選択的クロスカップリング論文（1970 年代後半）。
* **充填の性質**: Partial（cis/trans 比の時間・温度系列実験と速度論/熱力学制御の明示的区別が達成されたかは不確実）
* **Confidence**: Low
* **注記**: U-3（kinetic/thermodynamic indeterminacy）への応答として独立研究が動機付けられたかが不明。Corriu グループは主導的に Ni 触媒の立体化学を研究しており、関連論文が存在する可能性が高いが書誌特定に自信がない。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread] + RI-01 [Reporting integrity]
* **充填開始点（推定）**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full Paper が収率データと反応条件を充実させた中で、ホモカップリング（R–R）生成物の質量収支が部分的に報告された可能性がある。ただし、「選択的」という主張に対する明示的な GC-MS 質量収支（クロス/ホモ比）が Full Paper に含まれているかは不確実。
* **充填確立点（推定）**: Tsou, T. T.; Kochi, J. K. 機構論文（推定 1979 年）— 化学量論的実験の中でホモカップリング生成物の発生条件が明確化された可能性がある。
* **充填の性質**: Partial（"selective" の定量的裏付けとしての明示的な質量収支が達成されたかは不確実）
* **Confidence**: Medium
* **注記**: D4-1（選択的主張の定量的根拠の不在）に対応する EP。SRG-2 全体（B-1, U-1, C-1）の解消には明示的な R–R 定量が必要であり、Full Paper での自動解消には含まれない可能性が高い。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]
* **充填開始点（推定）**: Kumada グループ ca. 1974–1977 — dipy-Ni 系から NiCl₂(dpe) 系への触媒サイクル輸入（eqs 2–4）の同型性を、NiCl₂(dpe) を使った化学量論的素反応（eq 2: トランスメタル化; eq 3: R–R 生成）で部分的に検証。
* **充填確立点（推定）**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**（推定）— Ni 触媒クロスカップリングにおける電子移動 vs. 協奏的 2 電子経路の識別を行い、dpe-Ni 系の機構経路を絞り込んだ可能性がある。
* **充填の性質**: Partial（RI-06 + RI-03 不可分共起のため、一方だけの解消では不完全）
* **Confidence**: Medium（Kochi グループが機構研究を行ったことは確信があるが、dpe-Ni 系に特化した実験を含むかは不確実）
* **注記**: EP-03a との不可分共起。Stage 3 §6 pattern 6「RI-06 + RI-03 の不可分共起」として記録済み。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary] + RI-05 [Qualitative overread]
* **充填開始点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full Paper Part I の副題「General Scope and Limitations」が、sp³ハライドおよびその他の非反応基質を試みた（または試みなかった）境界条件を記録した。sp² 制限の実験的根拠（失敗例か機構的説明）が初めて明示された。
* **充填確立点（完全充填の延伸）**: Kochi, J. K. グループ、および後続のアルキル-アルキルカップリング研究（推定 1980–2005 年）— sp³ハライドが NiCl₂(dpe) では反応しない理由（β-水素脱離またはアルキルハライドへの酸化的付加の困難性）が機構的に確立。sp³-sp³ クロスカップリングは後に Knochel グループ（Fe 触媒）や他グループによって全く異なる触媒系で解決。
* **充填の性質**: Partial→Complete（sp² 制限の実験的記録は Full Paper で達成；sp² 選択性の機構的根拠は後続研究で確立）
* **Confidence**: High（Full Paper の存在と Scope/Limitations の記録は確信；機構的充填の時期は Medium）
* **注記**: D4-4（sp³ハライドは試みられたか？）への直接応答。B-5 ↔ A-2 ピボット構造の解消。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: — （第三群; 独立論文として発表される性質ではない）
* **Confidence**: Low（インセンティブ構造の不整合により充填論文が存在しない可能性が高い）
* **注記**: 代表的 3–5 基質の収率を n≥3 で独立反復測定し標準偏差を報告する実験は、新規性を要求する出版慣行のもとで論文化されにくい。Full Paper がより多くの基質を扱うが、統計的な反復測定を提供するとは限らない。§E で詳述。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc. Chem. Commun.* **1972**, 144 — Ni(acac)₂ 触媒による同様の選択的クロスカップリングを報告した同時期の独立発見。原論文の Note Added in Proof に既記録。キレート型ジホスフィンを持たない Ni 触媒が類似の選択性を達成することを示し、「bidentate diphosphine が必要条件」という CLA-1 機構仮説を直接問い直す。
* **充填確立点**: Kumada グループ Full Paper（*Bull. Chem. Soc. Jpn.* **1976**）または後続比較研究 — NiCl₂(dpe) と Ni(acac)₂ を同一基質・条件で直接比較した定量データが提供されたと推定。または Corriu グループの後続論文が比較を実施。
* **充填の性質**: Partial（Corriu/Masse 1972 が最初の直接比較の出発点を提供；同一条件での定量的比較は後続論文で達成された可能性があるが特定不確実）
* **Confidence**: High（Corriu/Masse 1972 は原論文に引用; Full Paper の比較は Medium）
* **注記**: Corriu/Masse 1972 は原論文の Note Added in Proof に直接引用されているため、文献探索なしで書誌情報が確定している唯一の充填論文候補。D4-8（Ni(acac)₂ との対比）への直接応答。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao, K.; Sumitani, K.; Kiso, Y. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 | EP-01a, EP-02a, EP-07a (partial), EP-05a (partial) | VQ-2 | 1976 | High |
| 2 | Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc. Chem. Commun.* **1972**, 144 | EP-09a | VQ-4 (partial) | 1972 | High |
| 3 | Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* ca. **1979** (推定 vol. 101) | EP-03a (partial), EP-06a (partial) | VQ-3 (partial) | ca. 1979 | Medium |
| 4 | Kumada グループ機構論文（*J. Organomet. Chem.* ca. 1974–1977; 書誌不確実） | EP-03a (onset), EP-06a (onset) | VQ-3 (partial) | ca. 1974–1977 | Low |
| 5 | Corriu グループ立体化学論文（*J. Organomet. Chem.* ca. 1974–1978; 書誌不確実） | EP-04a (partial) | VQ-3 (partial) | ca. 1974–1978 | Low |

**選定理由：**

論文 1（Tamao et al. 1976 Full Paper）は単一論文が EP-01a・EP-02a・EP-07a の VQ-2 要件を一括してカバーするバンドル充填の典型であり、選定リストの核心に位置する。著者グループ自身による自己充填であり、S1 の `series_signal: yes` が予告した後続論文と正確に対応する。

論文 2（Corriu/Masse 1972）は原論文に直接引用されている唯一の充填候補であり、書誌確実性が最高。EP-09a（Ni(acac)₂ ベンチマーク）という D4-8 の核心問いへの直接応答として外せない。

論文 3–5 は VQ-3 要件（EP-03a, EP-04a, EP-06a）への対応として候補に挙げるが、Medium〜Low 信頼度であり、実際の DB 確認が不可欠。特に論文 3（Tsou/Kochi）は機構研究の方向性は確信があるが、dpe-Ni 系への特化程度が不確実。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-4 (partial) 要件 EP-09a → **1972 年**（Corriu/Masse, 同年同時期）[自己充填ではなく競合的独立発見]
- VQ-2 要件 EP-01a, EP-02a → **1976 年**（Tamao et al. Full Paper Part I）[自己充填、4 年後]
- VQ-2 要件 EP-07a → **1976 年**（同上, Scope and Limitations 節）[自己充填]
- VQ-3 要件 EP-03a, EP-06a → **推定 1977–1980 年**（Kochi グループまたは Kumada グループ機構論文）[技術駆動充填 + 分野横断充填]
- VQ-3 要件 EP-04a → **推定 1975–1980 年**（Corriu グループ立体化学論文）[分野横断充填]
- VQ-2/3 要件 EP-05a → **推定 1976 年以降**（部分充填、完全充填は不確実）
- VQ-4 要件 EP-08a → **未充填**（現在まで）

**階層-時間対応の評価：**

「VQ 階層が上がるほど充填に要する時間が長くなる」という仮説は、本ケースで部分的に支持される。VQ-2 要件（報告整合性: EP-01a/EP-02a）は 1976 年（4 年後）に自己充填され、VQ-3 要件（機構: EP-03a/EP-06a）は推定 8–10 年後まで完全充填に至らなかった。ただし顕著な **反例** が存在する：VQ-4 要件（ベンチマーク: EP-09a）は 1972 年（同年）に Corriu グループによって充填された。これは競合的独立発見という競争的文脈によって VQ 階層を逆転した充填パターンを生み出した。

**特筆すべきパターン：**

- **自己充填（Self-filling）**: Tamao et al. 1976 は原著者グループ（Kumada グループ）による典型的自己充填。A-2 の series_signal が内部的予告として機能していた。
- **競合的同時充填（Concurrent competitive filling）**: EP-09a を充填した Corriu/Masse 1972 は、原論文の投稿後・受理前に独立して競合的な研究を進め、同年同時期に発表。Note Added in Proof による追記という形で原論文に記録された。この「同年充填」パターンは VQ 階層-時間仮説の最大の反例を構成する。
- **著者回顧との照合**: プロジェクトリポジトリの `papers/ep/discussion/tamao2002/` に Tamao 2002 著者回顧的 mini-review が保管されている。Stage 3 §2 の EP リスト（特に EP-03a「中間体観測」、EP-05a「質量収支定量」、EP-09a「Ni(acac)₂比較」）と Tamao 2002 の回顧的言及の比較を行うことで、「著者が後年に認識した問い」と「UQS が 1972 年時点で同定した問い」の対応を直接検証できる。本 run では Tamao 2002 のテキストを読み込まないため、この照合は後続セッションに委ねる。
- **長期遅延充填（Long-delay filling）**: EP-04a（cis/trans 速度論/熱力学制御）の完全充填は、1972 年から 5–10 年以上を要した可能性がある。低温 NMR および反応速度論的手法の普及が技術的加速剤となった。
- **未充填（EP-08a）**: VQ-4 要件であるにもかかわらず、反復測定・統計的信頼性の明示は 50 年以上にわたって未充填のまま残存した可能性がある（§E 参照）。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

**EP-08a [Replication / uncertainty pack]:**

* **未充填の理由**: インセンティブ構造の不整合（dominant factor）。代表的 3–5 基質の収率を n≥3 の独立試験で反復測定し標準偏差を記録するという実験は技術的に完全に実施可能であるが、新規性を要求する出版慣行のもとでは独立論文として発表されない。Full Paper（Tamao 1976）はより多くの基質を扱うが、統計的反復測定の明示は Full Paper の genre においても標準的ではなかった（1970–1980 年代の有機合成 Full Paper における RI-08 の分野慣行的非要求）。
* **発見的意義**: あり。「Kumada カップリングは 50 年以上の歴史を持つ最も重要な反応の一つだが、基質ごとの収率の統計的不確実性は現在も明示されていない」というパターンが実証されるなら、UQS の§E 発見として記録できる。ただし実際に反復測定データが存在しない（または学術誌に発表されていない）ことの DB 確認が必要。
* **将来の充填可能性**: 高。現代の自動化合成プラットフォームや高処理量実験（HTE）を用いれば、反復測定付き収率データの取得・発表は容易になっている。近年の製薬業界主導のプロセス最適化論文（e.g., *Org. Process Res. Dev.*）がこの種のデータを含む可能性がある。

---

**EP-04a [Discrimination / replication pack]（部分未充填）:**

* **未充填の理由**: 複合要因。(1) 関心の相対的低下——cis/trans-stilbene 比の kinetic/thermodynamic 制御よりも、より合成的に有用な基質・生成物の研究に関心が移行した。(2) 実験設計の複雑さ——cis/trans 比の時間・温度依存性を厳密に測定するには、熱力学的平衡値の独立確認を含む系統的実験が必要であり、機構的含意が限定的に見えるため単独論文としての優先度が低下した。(3) 部分的充填で「十分」——後続の Corriu グループや Kumada グループの立体化学研究が部分的な答えを与えることで、問いが「実質的に解決済み」と見なされた可能性がある。
* **発見的意義**: あり（限定的）。U-3「kinetic/thermodynamic indeterminacy」は A-1 とは独立の問いとして UQS が同定したものだが、後続の立体化学研究が速度論的制御を前提として進んだため、この「速度論か熱力学か」という問いは分野内で暗黙のうちに解決済みとされた可能性がある。これを「分野の内部者には不可視の充填」として記録できる。
* **将来の充填可能性**: 中。現代の計算化学（DFT による遷移状態計算と cis/trans 生成物比の予測）が分子レベルで answer を提供できる。速度論/熱力学制御の区別は in silico で実証可能。

---

**EP-05a [Quantitative-ranking substantiation pack]（部分未充填）:**

* **未充填の理由**: 関心の不整合。「選択的クロスカップリング」という主張は実用的に自明と見なされるようになったため、R–R ホモカップリングの定量や質量収支の明示が「なくても問題ない」という分野コンセンサスが形成された。また eq (3) が R–R 生成を予測するという自己矛盾（U-1）は、触媒サイクルの修正（例: Ni(I)/Ni(III) 経路採用）によって問い自体の枠組みが変化した可能性がある（Paradigm-shift 型部分解消）。
* **発見的意義**: あり。U-1「提案触媒サイクルが予測するホモカップリング生成物が報告されていない」という自己矛盾は、Ni(0)/Ni(II) 2電子サイクルから Ni(I)/Ni(III) ラジカル経路への機構的修正によって「問いの枠組みが変わった」事例として記録できる可能性がある。これは Paradigm-shift 型解消の候補。
* **将来の充填可能性**: 中。現代の GC-MS 質量収支分析は技術的に容易だが、出版インセンティブが依然として低い。ただし触媒設計の文脈（新配位子スクリーニング）では副生物定量が報告される慣行がある。

---

## 【Retrieval Depth Annotation】

### 充填論文候補 × Retrieval Depth マトリクス

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Corriu, R. J. P.; Masse, J. P. *Chem. Commun.* **1972**, 144 | EP-09a | I | S1 Note Added in Proof に直接引用されているため、読んだ瞬間に想起 | yes | High |
| Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 | EP-01a, EP-02a, EP-07a, EP-05a (partial) | I (存在); II (巻号) | A-2 `series_signal: yes`「Investigations are continuing」→ Kumada グループは必ず Full Paper を発表したはず → *Bull. Chem. Soc. Jpn.* は Kumada グループの主要発表媒体 → 1976 年前後が妥当 | yes | High |
| Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* ca. **1979**（推定 vol. 101） | EP-03a, EP-06a (partial) | II–III | EP-03a/06a「中間体観測・サイクル検証」→「1970 年代後半のNi触媒機構研究で誰が活躍したか？」→「Kochi グループ（Indiana Univ.）はラジカル機構研究で著名」→「Tsou, T. T. は Kochi のポスドク/学生として Ni 触媒機構を研究した」→ 特定論文に到達 | yes（タイトル・巻号の確認要） | Medium |
| Kumada グループ機構論文（*J. Organomet. Chem.* ca. 1974–1977; 書誌不確実） | EP-03a (onset), EP-06a (onset) | III | 「Kumada グループは通信 1972 の後に何を発表したか？」→ 複数候補から三角測量 → *J. Organomet. Chem.* への投稿パターン → 1973–1977 年の著者グループ論文リストは記憶から再構成不能 | uncertain | Low |
| Corriu グループ立体化学論文（*J. Organomet. Chem.* ca. 1974–1978; Moreau, J. J. E. 共著推定） | EP-04a (partial) | III | EP-04a「cis/trans stilbene 速度論/熱力学」→「立体化学 Ni 触媒カップリングを誰が研究したか？」→「Corriu グループは Ni(acac)₂ で継続研究」→「Moreau, J. J. E. は Corriu の共著者で立体化学を担当した可能性」→ 特定論文には到達できず | uncertain | Low |

### Retrieval Depth 各候補の詳細推論記録

**[1] Corriu/Masse 1972 — Tier I**
想起の起点: S1 の `[S0-7] note_added_in_proof` および C-3「Corriu and Masse, Chem. Commun. 144 (1972)」の記述を読んだ時点で即座に想起。特に D4-8（「NiCl₂(dpe) の機構的主張の核心が、キレート型ジホスフィンなしでも同様の選択性が達成されるという点に脅かされている」）との対応が明確。推論経路は 0 段階（テキストに引用されている）。

**[2] Tamao et al. 1976 Full Paper — Tier I/II**
想起の起点: `series_signal: yes` という META フィールドと A-2「[REDACTED: verbatim source text; see the source paper via its DOI]」の組み合わせ。「このような文言が入っている有機金属化学の 1972 年通信が、著者グループ自身によって Full Paper 化されなかったケースはほぼない」という一般的知識から即座に想起。特定の書誌詳細（*Bull. Chem. Soc. Jpn.*、1976 年、第 49 巻、1958 ページ）は: Kumada グループ = 京都大学 → 主要発表先の一つが *Bull. Chem. Soc. Jpn.* → 1976 年という時期は通信（1972 年）から 4 年後で Full Paper 化として妥当 → 2 段階の連想。

**[3] Tsou/Kochi 1979 — Tier II–III**
想起の起点: EP-03a の case-specific 実装「NiCl₂(dpe)系での触媒サイクルを機構的主張として記述するには、対象系での少なくとも 1 つの素反応ステップの化学量論的実証または中間体の分光学的同定が必要」を読んだ後、「この種の実験を誰が行ったか？」と自問。連想経路: 「1970 年代後半の有機金属機構研究」→「Jay Kochi（Indiana 大）はラジカル機構とイオン機構の区別、Ni・Cu 触媒の機構で著名」→「Tsou, T. T. という名前が Kochi グループの論文著者として浮かぶ」→「ビアリール合成との関連から JACS 1979 頃と推定」。書誌情報（vol. 101, 7547）は記憶から再構成しており確実性が低い。DB 確認が必須。

**[4] Kumada グループ機構論文 — Tier III**
想起の起点: EP-03a への対応として「Kumada グループ自身が 1972〜1976 年の間に機構論文を発表したはず」と推定。連想経路: 「Kumada グループの当時の活動」→ 「Tamao, Hayashi が中心メンバー」→ 「*J. Organomet. Chem.* への投稿が多い」→ しかし特定論文のタイトル・年・巻号が記憶から再構成できない。複数の候補を考えて三角測量しようとするが、確信のある特定論文に到達しない。Low confidence で記録。

**[5] Corriu グループ立体化学論文 — Tier III**
想起の起点: EP-04a「cis/trans比の速度論/熱力学制御」→「この問いに誰が応答したか？」→「Corriu グループは Ni(acac)₂ 系で継続研究しており、立体化学研究の動機がある」→「J. J. E. Moreau が Corriu の共著者として立体化学を担当した可能性」→ しかし特定論文に到達できない。書誌情報は再構成不能。

---

### 考慮し棄却した候補

以下の候補を思考過程で検討したが、EP への対応関係が不十分と判断して棄却した。

| 棄却候補 | 検討した EP | 棄却理由 |
|---|---|---|
| Hayashi, T.; Kumada, M. 不斉クロスカップリング論文（DIOP-Ni, BINAP-Ni; 1970年代後半） | EP-04a, EP-07a | 鏡像選択性（ee）を問題にする論文であり、cis/trans 速度論/熱力学区別（EP-04a）または sp²/sp³ 境界（EP-07a）への直接応答ではない。エナンチオ選択性は異なる問いの軸。 |
| Suzuki, A. ら Pd 触媒クロスカップリング論文（1979–） | EP-03a, EP-06a | 金属が Pd であり、NiCl₂(dpe) 系への類推は RI-06 の「別系から輸入する問題」を再現するだけ。Pd の触媒サイクル研究が Ni の EP を充填するとは見なせない。 |
| Kochi, J. K. Fe 触媒 Grignard カップリング論文（1971） | EP-07a | 原論文（1972）より前の文献であり、EP 充填候補にならない。また Fe 触媒系は NiCl₂(dpe) のスコープ境界（B-5, B-6）に直接対応しない（異なる触媒で sp³ が機能することは Ni の sp² 制限の理由を説明しない）。 |
| Negishi, E. Zn 試薬/Pd 触媒クロスカップリング論文（1977–） | EP-09a | ベンチマーク比較対象は Ni(acac)₂ vs. NiCl₂(dpe) であり、Pd 触媒系との比較は EP-09a の要件外。 |
| Nobel 講演（2010 年, Suzuki / Heck / Negishi） | 全体 | レビュー文書のため EP 充填論文としての対象外（Stage 4 プロンプトのレビュー論文不算入規則）。Kumada はノーベル賞受賞者ではないため当該講演も存在しない。 |
| Tolman, C. A. Ni(0) ホスフィン錯体反応性論文（1970 年代） | EP-06a | NiCl₂(dpe) 系ではなく Ni(PPh₃)₄ や類似単座ホスフィン Ni(0) 錯体の反応性研究。dpe 系での eq 2–4 の化学量論的検証には直接対応しない（別配位子環境、別反応型）。 |
| Wilke, G. Ni(0) 触媒有機金属論文（1960–1970 年代, MPI Mülheim） | EP-03a | Kumada 論文（1972）より前または同時期の研究が多く、NiCl₂(dpe) 触媒の Kumada カップリング中間体に特化した実験ではない（1,5-COD-Ni 系、アリル-Ni 系が中心）。 |

---

*（出力終了）*
```
