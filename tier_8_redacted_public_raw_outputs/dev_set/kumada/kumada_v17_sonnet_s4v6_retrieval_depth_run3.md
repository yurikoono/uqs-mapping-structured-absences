```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6
experimental_variant: retrieval-depth-annotation (Multi-run robustness, v6 run 3)
related_pilot: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Pilot 1, v6 run 1)
note: Multi-run robustness check の v6 第 3 run。Pilot 1 と同 prompt で実行し、
      run 間の retrieval scope と Tier annotation の variance を測定する。
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**C23 trigger: applicable** — 本論文は JACS Communication 形式（3ページ）であり、reporting completeness 関連 EP（EP-01a, EP-02a）は Letter→Full Paper auto-resolution が発火する。

---

**第一群（文献で明確に追跡可能）：** EP-01a, EP-02a, EP-06a, EP-07a, EP-09a

— EP-01a：JACS Communication 形式に起因する glpc 条件・収率基準・反応時間の不記載は、同一著者グループの Bull. Chem. Soc. Jpn. Full Paper（1976年）で自動解消される典型的 Letter→Full Paper 遷移パターン（RI-01）。検索語「nickel phosphine Grignard coupling full paper scope BCSJ」で直接ヒットしうる。

— EP-02a：EP-01a と同一 Full Paper 遷移によって、全エントリの個別分光データが提供される。EP-01a とのバンドル充填候補（RI-02 non-fatal）。

— EP-06a：触媒サイクルの個別素反応（酸化的付加・トランスメタル化・還元的脱離）の化学量論的実証は、Ni(0)/Ni(II) 機構の有機金属化学として独立論文の主題になりやすい（RI-06）。Kochi グループの酸化的付加研究が検索語「nickel(0) oxidative addition aryl halide mechanism」で直接ヒットしうる。

— EP-07a：sp² 制限の実験的根拠（sp³ ハライドの不活性確認、Cl/Br/I 定量比較）は、Full Paper 展開でのスコープ記述として独立論文化されやすい（RI-07）。Tamao 1976 Full Paper が一次充填候補。

— EP-09a：Corriu/Masse（Ni(acac)₂）との直接比較は、1970年代の配位子設計論争の核心的問いであり、concurrent paper として既に部分的な答えが存在する（RI-09）。

**第二群（間接的に追跡可能）：** EP-03a, EP-04a, EP-05a

— EP-03a：NiCl₂(dpe) 系での低温 ³¹P{¹H} NMR によるジオルガノニッケル中間体観測は、類似系（dipy-Ni）での先行充填は確認できるが、対象系そのものでの直接観測論文の特定が困難（RI-03）。

— EP-04a：cis/trans-スチルベン比の速度論/熱力学的判定実験（時間・温度系列）は、本論文特定基質に特化した実験であり、独立論文の主題になりにくい（RI-04）。

— EP-05a：クロスカップリング対ホモカップリングの質量収支（GC-MS 定量）は、Tamao Full Paper（1976年）が一次充填候補だが、R-R 副生物の明示的定量が Full Paper でも欠落している可能性がある（RI-05）。

**第三群（充填が見つからない可能性あり）：** EP-08a

— EP-08a：収率の統計的反復測定（n≥3、標準偏差報告）は、クロスカップリング化学分野では独立論文として出版するインセンティブが存在せず、**インセンティブ構造的未充填**パターンに該当（RI-08）。

**Letter→Full Paper auto-resolution annotation（C23）：**

EP-01a および EP-02a:
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"（実際の充填は 4 年後 1976 年 — やや超過）
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第二群 → Letter→Full Paper auto-resolution）**

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点 / 充填確立点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969. — Table I 相当の全エントリについて glpc 条件（内部標準・カラム仕様）と収率計算基準を統一記述し、全基質の反応時間を明示する Full Paper。（充填開始点と確立点は同一）
* **充填の性質**: Complete（format-driven auto-resolution）
* **Bibliographic confidence**: High — Kumada カップリングの標準 Full Paper 引用として学術的に広く認識されている。著者リスト（特に Minato, A. の位置）の確認は要する。
* **Filling adequacy confidence**: High — Full Paper 形式への移行が RI-01 の構造的原因（通信形式の紙幅制約）を直接解消する。
* **Verification recommendation**: [必須] — 条件 (a)(b)(c) すべてに該当（1976年、Kumada グループ密集著者ネットワーク、named reaction）
* **Bibliographic verification status**: pending
* **DOI**: 10.1246/bcsj.49.1958（推定。Crossref 要確認）
* **Filling timescale category**: format-driven（4 yr — 1–3 yr window をわずかに超えるが、Full Paper 準備期間中に不斉クロスカップリングの開発も並行していたことによる遅延と推定）
* **注記**: EP-02a・EP-05a とのバンドル充填。§D 時間軸では最初の VQ-2 到達論文として位置づけられる。Stage 3 §5 の対応 EP に「format-driven auto-resolved」を付記する。

**[Retrieval depth annotation — EP-01a]**
- **Self-Tier**: I (immediate)
- **推論経路**: EP-01a の記述（「同一 glpc 条件での収率の再測定・再報告」）から「Kumada coupling Full Paper」という概念が思考の起点として即座に想起された。続いて BCSJ 1976, 49, 1958 という書誌情報が付随した。
- **DB-findability**: yes — Bull. Chem. Soc. Jpn. 1976, 49 は標準的データベースで検索可能。
- **Bib confidence**: High

---

**EP-02a [Identity/purity substantiation pack]（第二群 → Letter→Full Paper auto-resolution）**

* **充填するRI**: RI-02 (Identification completeness — non-fatal)
* **充填開始点 / 充填確立点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969（EP-01a と同一）— Full Paper 展開で Table I 全エントリの GC-MS または ¹H NMR データが個別記録される。
* **充填の性質**: Complete（format-driven auto-resolution、EP-01a バンドル）
* **Bibliographic confidence**: High（EP-01a と同一論文）
* **Filling adequacy confidence**: Medium — Full Paper が全エントリの個別スペクトルデータを提供しているかどうかは確認が必要（Full Paper でも代表例の詳細記述のみにとどまる可能性がある）。
* **Verification recommendation**: [必須]（EP-01a と同一理由）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（4 yr、EP-01a と同一）
* **注記**: EP-01a とのバンドル充填。RI-02 は VQ-1 non-fatal として原論文でも通過しており、充填の優先度は RI-01 より低い。

**[Retrieval depth annotation — EP-02a]**
- **Self-Tier**: I (immediate — EP-01a と同一論文)
- **推論経路**: EP-01a 充填論文特定後、「同一 Full Paper が分光データも提供する」として自動的に同定。独立した検索は要さなかった。
- **DB-findability**: yes（EP-01a と同一）
- **Bib confidence**: High（書誌情報は EP-01a と同一；filling adequacy は Medium）

---

**EP-03a [Direct-observation / state-assignment pack]（第二群）**

* **充填するRI**: RI-03 (Unobserved explanatory intermediate)
* **充填開始点（先行充填 — dipy-Ni 系）**: Uchino, M.; Yamamoto, A.; Ikeda, S. *J. Organomet. Chem.* **1970**, *24*, C63. — dipy 配位子を持つジオルガノニッケル中間体（原論文 eq 1 の前提となる系）の化学量論的形成・同定。原論文（1972年）より 2 年先行する充填だが、対象系（dpe-Ni）ではなく輸入元の系（dipy-Ni）での観察として機能する。
* **充填確立点（対象系 — dpe-Ni）**: 未同定（Low confidence）— Tamao グループの後続機構論文（1977–1985 年ごろ）または Yamamoto (Akira) グループの有機ニッケル中間体化学が最有力候補。低温 ³¹P{¹H} NMR での [Ni(n-Bu)₂(dpe)] 直接観測を含む論文は特定に至らず。
* **充填の性質**: Indirect（Uchino 1970 は dipy-Ni 系での観測；dpe-Ni 系での Complete 充填は文献特定未到達）
* **Bibliographic confidence**: High（Uchino/Yamamoto/Ikeda 1970 は原論文 ref 11 として実在確認済み）/ Low（dpe-Ni 系直接観測論文は未特定）
* **Filling adequacy confidence**: Medium（Indirect 充填として Uchino 1970 は RI-06 の部分解消には機能するが EP-03a の完全充填には不足）
* **Verification recommendation**: [必須] — 条件 (a)(b)(c) すべて該当
* **Bibliographic verification status**: pending（Uchino 1970 自体は実在確認済み）
* **Filling timescale category**: technical-barrier（dpe-Ni 系での直接観測は ³¹P NMR 技術の普及後 1975–1985 年ごろに条件が整ったと推定；dipy-Ni 先行充填は 1970 年）
* **注記**: 先行充填パターン（v18）として Uchino 1970 を記録。dipy 系 → dpe 系の同型性実証という EP-06a との不可分共起（SRG-1 の RI-06+RI-03 共起パターン）があるため、EP-06a の充填確立が EP-03a を Indirect から Complete に押し上げる前提条件となる。

**[Retrieval depth annotation — EP-03a]**
- **Self-Tier**: I（dipy-Ni 先行充填 Uchino 1970 の同定） / III（dpe-Ni 系直接観測論文）
- **推論経路（Uchino 1970）**: 原論文の ref 11 として直接引用されているため、Tier I の即時想起。「先行充填パターン」として機能する点は EP-03a 記述から演繹した（Tier I の派生判断）。
- **推論経路（dpe-Ni 直接観測）**: 「Yamamoto (Akira) グループ → 有機ニッケル中間体化学 → dpe 配位子系」という 3 段階の連想を辿ったが、具体的な論文に到達できなかった（Tier III）。この経路での候補は思い浮かんだが bibliographic confidence が Low であり出力を抑制した。
- **DB-findability**: yes（Uchino 1970）/ uncertain（dpe-Ni 特化論文）
- **Bib confidence**: High（Uchino 1970）/ Low（dpe-Ni 直接観測候補）

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 (Unreplicated discriminator — cis/trans stilbene ratio)
* **充填開始点（推定）**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969. — Full Paper 中に cis/trans-1,2-ジクロロエチレン + PhMgBr 反応の詳細条件が記述される可能性はあるが、時間・温度系列（速度論/熱力学的判定のための実験）が含まれるかは不明（Filling adequacy confidence: Low）。
* **充填確立点**: 未同定（Low confidence）
* **充填の性質**: Partial at best（cis/trans 比の分析的改善は Full Paper で期待されるが、速度論/熱力学的判定実験の独立論文化は確認できず）
* **Bibliographic confidence**: Low（具体的充填論文を特定できず）
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: non-applicable（充填論文を特定できないため）
* **注記**: A-1（deferred mechanism）と B-11（absent ratio details）のピボット構造（Stage 2 D4-5）が、この問いの充填を困難にしている。Kumada カップリングが合成ツールとして急速に応用展開されたため、速度論/熱力学的制御の区別という問いへの関心が希薄化した可能性（Success-driven question erasure の部分パターン）。

**[Retrieval depth annotation — EP-04a]**
- **Self-Tier**: III (deep) — 具体的な論文が想起されなかった。
- **推論経路**: 「cis/trans stilbene ratio kinetic vs thermodynamic control」という検索語から Hayashi/Kumada の立体化学研究を経由したが、この特定の問い（cis/trans-1,2-ジクロロエチレン + PhMgBr の時間/温度依存性）に特化した論文に到達できなかった。Hayashi/Kumada の立体化学論文は不斉クロスカップリング（別の問い）を扱っているため、対応関係が確立できなかった。
- **DB-findability**: uncertain（特定論文なし）
- **Bib confidence**: Low

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 (Qualitative overread — selectivity claim; chloride ranking)
* **充填開始点 / 充填確立点**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969. — Full Paper 中での GC 分析による反応混合物の定量（クロスカップリング vs. ホモカップリング vs. β-脱離）および PhCl/PhBr/PhI の収率・速度比較。
* **充填の性質**: Partial（Full Paper での選択性の定量記述は期待されるが、R-R ホモカップリング副生物の明示的定量が含まれるかどうかは検証待ち。VQ-3 の「完全な質量収支」レベルへの到達は確証なし）
* **Bibliographic confidence**: High（EP-01a と同一論文）
* **Filling adequacy confidence**: Medium（Full Paper が選択性の定量的改善を提供することは期待されるが、Stage 2 D4-1 で指摘された R-R 定量の完全な不在が Full Paper でも継続している可能性がある）
* **Verification recommendation**: [必須]（EP-01a と同理由）
* **Bibliographic verification status**: pending
* **DOI**: 10.1246/bcsj.49.1958（推定）
* **Filling timescale category**: format-driven（4 yr — EP-01a, EP-02a と同一論文）
* **注記**: EP-01a・EP-02a とのバンドル充填。CLA-1 の配位子活性序列定量化については、Hayashi et al. *J. Am. Chem. Soc.* **1976**, *98*, 3718 が配位子系の活性比較データを提供する可能性がある（第二候補として位置づけるが filling adequacy は Medium）。

**[Retrieval depth annotation — EP-05a]**
- **Self-Tier**: I (immediate) — EP-01a と同一の Full Paper が即座に想起され、そこに GC 質量収支データが含まれると期待された。
- **推論経路**: 「定量的質量収支」→「Full Paper」→ Tamao 1976 BCSJ の連想。R-R 副生物定量という特定要件については、Full Paper に含まれているかどうかが不明確であることを認識した（Tier I の到達に Tier II–III の不確実性が混在）。
- **DB-findability**: yes（論文自体は確実に存在）
- **Bib confidence**: High

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 (Imported model — catalytic cycle analogized from dipy-Ni)
* **充填開始点（酸化的付加ステップ）**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 7547–7560. — Ni(0) 錯体とアリールハライドの酸化的付加の速度論的・機構的研究。NiCl₂(dpe) 系の触媒サイクル eq (2) に対応する素反応を独立して実証し、dipy-Ni 系からの類推に実験的根拠を与える。
* **充填確立点（全サイクル化学量論的実証）**: 未同定（Medium confidence）— Kumada グループ自身の機構論文シリーズ（Full Paper Part II 以降、1977–1985 年ごろ）が最有力候補だが、具体的書誌の特定に至らず。
* **充填の性質**: Indirect（Tsou/Kochi 1979 は Ni(0) 酸化的付加を実証するが、monodentate phosphine-Ni 系を主対象とする可能性があり、dpe の bidentate 効果の評価には追加論文が必要）
* **Bibliographic confidence**: High（Tsou/Kochi 1979 JACS は有機金属機構化学の重要論文として高い確信）
* **Filling adequacy confidence**: Medium（Tsou/Kochi が EP 要件の「eq 2, 3, 4 の化学量論的個別実証 for dpe-Ni」を直接充填するかは不確実）
* **Verification recommendation**: [必須] — 条件 (a)(b)(c) 該当
* **Bibliographic verification status**: pending
* **DOI**: 10.1021/ja00519a024（推定。要確認）
* **Filling timescale category**: field-methodology（7 yr — 1972→1979；Ni(0)/Ni(II) 二電子機構の有機金属化学的確立が driving force）
* **注記**: EP-03a との不可分共起（SRG-1 RI-06+RI-03 共起）のため、EP-06a の充填確立が EP-03a の Indirect→Complete 充填への前提条件を構成する。Tamao Full Paper（1976）が Part II 以降で化学量論的検討を含む場合はバンドル充填。

**[Retrieval depth annotation — EP-06a]**
- **Self-Tier**: II (associative)
- **推論経路**: EP-06a の要件（「eq 2, 3, 4 の各素反応の NiCl₂(dpe) 系での実証」）→ 有機金属機構化学 1970–1980 年代 → Kochi グループの radical vs. ionic 論争 → Tsou/Kochi 1979（JACS 高被引用論文として想起）。Tsou/Kochi が具体的に NiCl₂(dpe) の dpe 系を扱っているかは不確実（Tier II 止まり）。
- **DB-findability**: yes（Tsou/Kochi 1979 JACS）
- **Bib confidence**: High（Tsou/Kochi 1979）/ Medium（dpe 特化の充填確立論文）

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary — sp² restriction) + RI-05 (chloride reactivity ranking, secondary)
* **充填開始点（sp³ 制限確認 + Cl/Br/I 定量比較）**: Tamao, K. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969. — Full Paper のスコープ節で sp³ ハライドの失敗例（または不活性確認実験）および PhCl/PhBr/PhI の収率・速度比較が記述されると推定。
* **充填確立点（sp² 制限の実用的確立）**: Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. *J. Am. Chem. Soc.* **1976**, *98*, 3718–3720. — キラルフェロセニルホスフィン-Ni 触媒を用いた不斉 Grignard クロスカップリング。sp² ハライドの使用が前提として確立されており、sp² 制限が実用的方法論として定着した時点を示す。
* **充填の性質**: Partial（sp²/sp³ 境界の実験的根拠は Full Paper で提示されると推定されるが、「Cl の高反応性」の定量的実証（初期速度の直接比較）は検証待ち；Hayashi 1976 は sp² 制限の実用的確立として Indirect 充填）
* **Bibliographic confidence**: High（Tamao 1976 BCSJ）/ High（Hayashi et al. 1976 JACS 98, 3718 — 著名な asymmetric coupling 論文として高確信）
* **Filling adequacy confidence**: Medium（Tamao 1976 Full Paper での sp³ 試験の明示的記述は未確認；Hayashi 1976 は sp² 制限の間接的確立として機能）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **DOI**: 10.1021/ja00475a060（Hayashi 1976 推定）/ 10.1246/bcsj.49.1958（Tamao 1976 推定）
* **Filling timescale category**: format-driven（4 yr — Tamao 1976）/ incentive-aligned（同年 Hayashi 1976 — sp² 制限を前提として不斉触媒開発が進んでいた）
* **注記**: sp³ ハライドの問題は後に Pd 触媒（Heck/Negishi/Suzuki）の発展によって別回路で解決される。Kumada 反応の sp² 制限は「sp² に限定された high-efficiency method」として固定化され（Success-driven question erasure の部分パターン）、sp³ を Ni で克服する検証需要が消滅した。

**[Retrieval depth annotation — EP-07a]**
- **Self-Tier**: II (associative)
- **推論経路**: 「sp³ halide boundary test in Kumada reaction」→「Full Paper でスコープが記述される」（Tier I に近い）+ 「Hayashi の不斉カップリング論文（1976）が sp² 前提として体系化された」という 2 段階の連想（Tier II）。Hayashi 1976 JACS 98, 3718 は「不斉 Kumada カップリング」という文脈で想起されたのであり、EP-07a 充填として先に想起されたわけではない（Tier II の典型的な associative 経路）。
- **DB-findability**: yes（両論文ともデータベース収録されている）
- **Bib confidence**: High（Tamao 1976, Hayashi 1976 いずれも著名論文）

---

**EP-08a [Replication / uncertainty pack]（第三群 — インセンティブ構造的未充填）**

* **充填するRI**: RI-08 (Unquantified reliability)
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: N/A（第三群）
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: N/A
* **Filling timescale category**: non-applicable
* **注記**: 反応収率の統計的反復測定（n≥3、標準偏差報告）は、1972–2000 年代のクロスカップリング化学において独立論文として出版するインセンティブが存在しなかった。新規基質・新触媒系・新反応の報告が出版優先事項であり、既存系の「追試と統計的評価」は不要と見なされた。現代の Reproducibility Crisis 文脈では充填需要が生じているが、Kumada 1972 に特化した再現実験の系統的報告は依然として稀である。**インセンティブ構造的未充填**。

**[Retrieval depth annotation — EP-08a]**
- **Self-Tier**: N/A（充填論文の探索を開始しなかった）
- **推論経路**: 第三群分類の時点で「インセンティブ構造的未充填」パターンとして診断済み。充填論文候補を意識的に探索する前に棄却。
- **DB-findability**: no（充填論文の存在を想定しない）
- **Bib confidence**: N/A

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 (External superiority — Ni(acac)₂ vs NiCl₂(dpe) comparison lacking)
* **充填開始点**: Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc., Chem. Commun.* **1972**, 144. — NiCl₂(dpe) を持たない Ni(acac)₂ で類似の選択的クロスカップリングを達成していることを示した concurrent communication（原論文 Note Added in Proof に記録済み）。「配位子なしでも選択性が得られる」という EP-09a の問いへの部分的な答えを提供している。これ自体は concurrent paper であり充填論文ではないが、比較の evidence として機能する。
* **充填確立点**: 未同定（Low confidence）— Corriu グループの後続比較論文（1975–1980 年ごろ）が最有力候補だが、具体的書誌は特定に至らず。「Corriu–Kumada reaction」という別称の定着が間接的な評価を示す。
* **充填の性質**: Partial（Corriu/Masse 1972 は Ni(acac)₂ での同様反応達成を示すが、NiCl₂(dpe) との直接比較ではない；bidentate 配位子の「必要条件」vs「有効な選択肢」への決定的答えは未確立）
* **Bibliographic confidence**: High（Corriu/Masse 1972 は原論文に引用されており実在確認済み）/ Low（後続比較研究の具体的書誌は未特定）
* **Filling adequacy confidence**: Medium（Corriu/Masse 1972 は「dpe なしでも類似反応が可能」という事実を提供し、dpe の必要条件という主張を否定する間接的充填として機能する）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending（Corriu/Masse 1972 自体は実在確認済みだが書誌の完全確認は推奨）
* **DOI**: 10.1039/c39720000144（推定）
* **Filling timescale category**: incentive-aligned（concurrent paper — 実質ゼロ時差の充填）
* **注記**: Corriu/Masse 1972 は「充填論文」ではなく原論文と並行する独立発見であり、Stage 2 D4-8 で「比較が欠落した不在」として記録された。充填としての機能は、後続の科学的記録（両グループの論文の参照関係）を通じて確立される。「Corriu–Kumada reaction」という命名の定着が、「配位子なしでも成立する」という EP-09a の問いへの科学コミュニティとしての評価を示している。

**[Retrieval depth annotation — EP-09a]**
- **Self-Tier**: I (immediate — Corriu/Masse 1972 は原論文 Note Added in Proof で明示されているため即時想起)
- **推論経路**: EP-09a の記述（「NiCl₂(dpe) と Ni(acac)₂ の直接比較」）→ 原論文 Note Added in Proof の Corriu/Masse 1972 → 即座の同定。後続比較研究については Corriu グループ 1970 年代後半論文を連想したが、具体的な書誌に到達できなかった（Tier II–III）。
- **DB-findability**: yes（Corriu/Masse 1972 Chem. Commun.）/ uncertain（後続比較研究）
- **Bib confidence**: High（Corriu/Masse 1972）

---

**§B 末尾チェック：Bibliographic verification（v18.3 追加、conditional triggering）**

トリガー条件の評価（本ケース全体）：
- (a) 論文年代が古い（1980年以前）: **該当** — 主要充填論文はすべて 1970–1979 年
- (b) 著者ネットワークが密（Kumada グループ 10+ の関連論文）: **該当**
- (c) Named reaction（Kumada coupling）: **該当**
- (d) Bibliographic confidence Medium-Low の候補が 2 件以上: **該当**（EP-03a dpe 直接観測論文, EP-04a, EP-06a 充填確立点, EP-09a 後続比較研究）

→ **全候補に [必須] Verification**。§C 推奨選定リストのすべての候補は「⚠️ verification 待機中」として表記。

**Known hallucination risk for this corpus:**
- **著者リスト捏造パターン**: 「Tamao–Sumitani–Hayashi–Kumada（1972年）」は実在しない（Hayashi は 1976 年以降に主要著者として登場；1972 Full Paper の共著者は Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato 等）
- **架空 coauthor**: Nagase や Miyake 等を 1972 年早期論文に混入するパターン
- **DOI の誤記**: 推定 DOI はすべて要確認

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️ Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-05a, EP-07a（一部） | VQ-2→VQ-3 境界 | 1976 | High | High/Med | 必須 |
| 2 | ⚠️ Hayashi, Tajika, Tamao, Kumada, *J. Am. Chem. Soc.* 1976, 98, 3718–3720 | EP-07a（確立）, EP-04a（Indirect）| VQ-2 確立 | 1976 | High | Medium | 必須 |
| 3 | ⚠️ Corriu, Masse, *Chem. Commun.* 1972, 144 | EP-09a（部分）| VQ-2 制限評価 | 1972 | High | Medium | 必須 |
| 4 | ⚠️ Uchino, Yamamoto, Ikeda, *J. Organomet. Chem.* 1970, 24, C63 | EP-03a（先行充填、Indirect）| VQ-3 前提 | 1970 | High | Medium | 必須 |
| 5 | ⚠️ Tsou, Kochi, *J. Am. Chem. Soc.* 1979, 101, 7547–7560 | EP-06a（Indirect）| VQ-3 | 1979 | High | Medium | 必須 |

（全エントリ **verification 待機中** — 条件 (a)(b)(c)(d) すべて該当）

**選定理由：**

No. 1（Tamao et al. 1976 BCSJ）は EP-01a・EP-02a・EP-05a・EP-07a の 4 つの EP をバンドル充填する最高効率候補として最優先。Letter→Full Paper auto-resolution（C23）の典型事例として、VQ-2 到達の実証的基盤となる。1 論文で VQ-2 要件の大部分をカバーする点で唯一無二の効率性を持つ。

No. 2（Hayashi et al. 1976 JACS）は EP-07a の sp² 制限を実用的方法論として確立した論文として選定。No. 1 と同年（1976 年）であり、VQ-2 到達クラスターの第 2 成分を形成する。不斉触媒を通じて sp² 制限への間接的 EP-04a 充填も提供する。

No. 3（Corriu/Masse 1972）は EP-09a の充填として機能するだけでなく、bidentate 配位子の必要条件論争（D4-8）への科学史的回答を提供する。Zero-lag の concurrent paper として VQ-2 水準の「制限評価」という独自の充填位置を占める。

No. 4（Uchino et al. 1970）は EP-03a の「先行充填」パターンとして機能し、SRG-1 の RI-06+RI-03 不可分共起のうち dipy-Ni 系での解消根拠を提供する。原論文 ref 11 として実在確認済みの唯一の先行論文。

No. 5（Tsou/Kochi 1979）は Ni(0) の酸化的付加を EP-06a（RI-06 Analogy-validation）の充填開始点として提供する。Kumada グループ以外からの分野横断充填として、VQ-3 達成への独立した貢献を示す。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件（EP-09a）: Corriu/Masse *Chem. Commun.* 1972 → **1972 年**（concurrent paper、ゼロ時差）
- VQ-2 要件（EP-01a, EP-02a, EP-07a）: Tamao et al. *BCSJ* 1976 → **1976 年**（自己充填、format-driven）
- VQ-2 確立（EP-07a 確立）: Hayashi et al. *JACS* 1976 → **1976 年**（自己充填、incentive-aligned）
- VQ-3 前提（EP-03a, Indirect）: Uchino et al. *J. Organomet. Chem.* 1970 → **1970 年**（先行充填）
- VQ-3 要件（EP-05a, Partial）: Tamao et al. *BCSJ* 1976 → **1976 年**（format-driven バンドル）
- VQ-3 要件（EP-06a, Indirect）: Tsou/Kochi *JACS* 1979 → **1979 年**（分野横断充填）
- VQ-3→VQ-4（EP-04a）: **未充填**（充填論文未同定）
- VQ-4（EP-08a）: **インセンティブ構造的未充填**（充填論文なし）

**階層-時間対応の評価：**

「VQ 階層が上がるほど充填に要する時間が長くなる」という仮説を概ね支持するが、重要な逸脱がある。VQ-2 要件（reporting completeness）は 4 年以内（Tamao 1976）またはゼロ時差（Corriu 1972）で充填された。VQ-3 要件（機構的実証）は 7 年（1972→1979、Tsou/Kochi）を要し、かつ Indirect 充填にとどまっている。VQ-4 要件（EP-04a, EP-08a）は本論文においては未充填のまま残存している。この単調増加パターンからの逸脱として、EP-03a の 1970 年先行充填（VQ-3 前提）があり、VQ-3 の一部が VQ-2 よりも早く（原論文より前に）部分充填されていたという逆転現象が記録される。

**特筆すべきパターン：**

1. **自己充填（format-driven）**: EP-01a, EP-02a, EP-05a, EP-07a は Tamao グループ自身の Full Paper（1976）によって自己充填される。Letter→Full Paper 遷移（C23）の典型事例。著者グループが自らの問いを後続論文で解消する最も直接的なパターン。

2. **先行充填（v18 パターン）**: EP-03a は原論文（1972 年）より 2 年前（Uchino 1970, dipy-Ni 系）に部分的に充填されていた。原論文は「既に充填されていた問いへの類似系からの理論的枠組み」として機能する構造。これは RI-06（サイクルレベル輸入）の科学史的正当化と解釈できる。

3. **分野横断充填**: EP-06a は Kochi グループ（有機金属機構化学）という Kumada グループとは独立したアプローチからの充填（1979 年）。Kumada 反応の合成的成功が有機金属機構化学の研究者を酸化的付加機構の研究へ誘引した構造を示す。

4. **Success-driven question erasure（部分）**: EP-04a（cis/trans 比の速度論/熱力学的判定）は、Kumada カップリングの合成ツールとしての成功によって検証需要が希薄化した。sp³ ハライドの問題（EP-07a の一側面）は後に Pd 触媒系（Negishi/Suzuki/Heck）で別回路解決され、Ni 系での解決需要が消滅。

5. **VQ 階層逆転の診断**: EP-08a（VQ-4 = RI-08 統計的信頼性）は技術的に最も解決容易だが完全に未充填のままであり、EP-03a（VQ-3 = RI-03 中間体観測）よりも充填されていない。これは「出版インセンティブに基づく実際の充填順序（高 novelty 優先→統計的評価は後回し）」と「VQ 階層順序（低 VQ 先に→高 VQ 後に）」の逆転パターンを示している。VQ-4 の統計的要件が完全に放棄されている一方で、VQ-3 の機構的要件は少なくとも Indirect 充填が達成されている。

---

### §E 未充填EPの発見的意義

**EP-04a [Discrimination / replication pack]:**

* **未充填の理由**: **成功による問いの抹消（Success-driven question erasure）** — cis/trans-スチルベン比が速度論的 vs 熱力学的産物のどちらかを区別する実験は、Kumada カップリングが合成ツールとして確立した後は科学的需要が消滅した。ビニルハライドの立体化学は「E/Z 保持型」として実用的経験則が定着したため、精密な時間・温度系列実験の動機が失われた。技術的困難（定量 GLC の反復実験）よりも関心の消滅が主因。

* **発見的意義**: **あり** — 「選択性が速度論的産物か熱力学的産物か」という問いは、Kumada カップリングの立体選択性制御の基盤を問うものであり、現代の遷移金属触媒クロスカップリングの機構理解（特に Pd 触媒系のステレオスペシフィシティ研究）において同型の問いが継続している。Kumada 1972 の cis/trans 問いが未回答のまま残ったことは、分野が「成功している方法の機構的深掘り」より「新規基質への展開」を優先したことの歴史的証拠として記録できる。

* **将来の充填可能性**: 中 — 現代の DFT 反応経路計算で NiCl₂(dpe) 触媒でのスチルベン形成の速度論的 vs 熱力学的選択性を評価することは技術的に可能。実験的確認は E/Z 選択性制御研究の文脈で実施されうる。

---

**EP-08a [Replication / uncertainty pack]:**

* **未充填の理由**: **インセンティブ構造的未充填** — 反応収率の統計的反復測定（n≥3、標準偏差報告）は、クロスカップリング合成化学の出版文化において独立論文化するインセンティブが存在しなかった。これは技術的困難ではなく、出版優先事項（新規反応 > 既知反応の統計的評価）の不整合による。Kumada 1972 の「76–98% 収率」という記述は統計的根拠なしに標準的引用として流通し続けている。

* **発見的意義**: **あり** — Kumada 反応を含むクロスカップリング化学全体に対して、収率の統計的評価が不在のまま数値が権威的に引用される構造は、Reproducibility Crisis の文脈で「分野が体系的に避けてきた問い」として記録できる。個別論文の問題ではなく、分野全体の出版インセンティブ構造の問題として提示可能。

* **将来の充填可能性**: 高 — 技術的には容易。Kumada 反応の代表基質（EtMgBr/PhCl → Ph-Et）を n≥10 回反復して収率の 95% 信頼区間を測定することは標準的な合成研究室で実施可能。再現性報告専門誌（Org. Synth. 等）の文脈では既に充填されている可能性があり、要確認。

---

**EP-03a の未充填部分（dpe-Ni 系直接観測）：**

* **未充填の理由**: **技術的バリア（部分）+ 関心の転換** — NiCl₂(dpe) 系でのジオルガノニッケル中間体 [Ni(n-Bu)₂(dpe)] を低温 ³¹P{¹H} NMR で直接観測するには、1972 年時点では技術的バリアがあった。1980 年代以降の NMR 技術進歩によりバリアは低下したが、Kumada 系よりも Pd 触媒系（Stille/Suzuki/Negishi）への関心集中により研究リソースが転換した可能性がある。

* **発見的意義**: **あり** — dpe-Ni 系での中間体直接観測が充填されなかった（推定）ことは、「機構的理解を欠いたまま実用的に発展した触媒反応」の典型例として、UQS の発見的価値を持つ。合成的成功が機構的探索を「不要」にした構造と、技術的バリアの複合パターンとして記録できる。

* **将来の充填可能性**: 中〜高 — 現代の低温 ³¹P{¹H} NMR および計算化学（DFT + NMR シフト予測）との組み合わせで実施可能。ただし NiCl₂(dpe) 系への特化した関心を持つ研究グループが必要。

---

## 総合 Retrieval Depth Annotation マトリクス

| 充填論文 | 充填 EP | Self-Tier | 推論経路（概要） | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Tamao et al. *BCSJ* 1976, 49, 1958 | EP-01a, EP-02a, EP-05a, EP-07a（一部）| I | 「Kumada coupling Full Paper」として直接想起 | yes | High |
| Hayashi, Tajika, Tamao, Kumada *JACS* 1976, 98, 3718 | EP-07a（確立）, EP-04a（Indirect）| II | 「不斉 Kumada 1976 chiral phosphine-Ni」の連想経由 | yes | High |
| Corriu, Masse *Chem. Commun.* 1972, 144 | EP-09a（部分）| I | 原論文 Note Added in Proof から直接同定 | yes | High |
| Uchino, Yamamoto, Ikeda *J. Organomet. Chem.* 1970, 24, C63 | EP-03a（先行充填、Indirect）| I | 原論文 ref 11 から直接同定 | yes | High |
| Tsou, Kochi *JACS* 1979, 101, 7547 | EP-06a（Indirect）| II | 「Kochi group Ni(0) oxidative addition mechanism」の連想 | yes | High |
| [未同定] dpe-Ni ジオルガノニッケル直接観測論文 | EP-03a（Complete 充填候補）| III | Yamamoto (A.) グループ有機 Ni 中間体化学を経由したが特定未到達 | uncertain | Low |
| [未同定] Corriu グループ後続比較研究 ~1975–1980 | EP-09a（確立点）| III | Corriu グループ後続論文の連想経路を辿ったが書誌特定不能 | uncertain | Low |
| [未充填] — | EP-04a（時間/温度系列）| N/A | Success-driven erasure パターンと診断；探索後に到達なし | no | N/A |
| [未充填] — | EP-08a（統計的反復）| N/A | インセンティブ構造的未充填と診断；探索開始前に棄却 | no | N/A |

---

## 付録：考慮し棄却した候補

1. **Kiso, Y.; 関連する Kumada グループの 1974 年前後の Tetrahedron Lett. 論文** — 不斉触媒開発への関心から連想されたが、主目的が立体選択性導入であり、EP の要件（中間体直接観測・質量収支定量）への充填としては Indirect すぎる。著者順と具体的な出版先の確信が Medium 以下（hallucination リスク高）のため除外。連想経路は辿ったが出力に採用しなかった（Tier II-III の探索段階で棄却）。

2. **Yamamoto, A.; Yamamoto, T.; Ikeda, S. *JACS* 1971, 93 関連論文** — Uchino/Yamamoto/Ikeda (1970) と同系列の Yamamoto グループの有機ニッケル中間体論文として連想されたが、ページ番号等の書誌情報の確信が低い（推測値を含む）。Uchino 1970（ref 11 として実在確認済み）で同系列の充填はカバーされているため、重複かつ低確信の候補として除外。

3. **Tamura, M.; Kochi, J.K. *Synthesis* 1971, 303（ref 6）** — 原論文に引用（ref 6）されており鉄触媒によるアルケニルハライド coupling の先行研究として重要だが、EP-09a のベンチマーク比較対象は「Ni(acac)₂ vs NiCl₂(dpe)」に特化しており、Tamura/Kochi（Fe 触媒系）は EP-09a の充填対象外。Stage 2 の C-1（dropped quantitative benchmark）として記録済みであり Stage 4 での充填候補ではないと判断。

4. **レビュー論文全般（Tsuji, Hegedus, Negishi 等による総説）** — 充填論文探索の過程でクロスカップリング総説が連想されたが、プロンプト規則（「レビュー論文は EP を充填しない」）に従って即座に棄却。Hayashi/Kumada *Acc. Chem. Res.* 1982, 15, 395 はこの判断の典型例。二次情報源としての参照価値は認めるが充填論文には採用しない。

5. **Heck, R. F. 関連論文（Pd 触媒系のビニルハライド coupling）** — EP-07a の sp³ 制限を「別回路で解決」した論文として連想されたが、Kumada 反応の EP 充填（NiCl₂(dpe) 系での sp³ ハライド試験）とは直接対応しない。Success-driven question erasure の「別回路解決」の文脈では言及するが、充填論文候補としては棄却。
```
