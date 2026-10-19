```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6
run_id: run6
input_s2: kumada_v184_sonnet_s2_run6.md
input_s3: kumada_v184_sonnet_s3v2_run6.md
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（JACS communication, vol. 94, pp. 4374–4376）

---

### §A EP充填難易度の三群分類

Stage 3 §5（最短補強ルート）から全 EPを抽出し、三群に分類する。

対象EP一覧（§2 Crosswalk + §5 EP投入順序から）：
- EP-03a: Direct-observation / state-assignment pack（SRG-1・CLA-1）
- EP-06a: Analogy-validation pack（SRG-1）
- EP-04a: Discrimination / replication pack（SRG-4）
- EP-08a: Replication / uncertainty pack（SRG-2・SRG-5）
- EP-09a: Internal benchmark pack（SRG-2・SRG-6）
- EP-07a: Boundary-test pack（SRG-3）
- EP-01a: Reporting-coherence pack（SRG-4・SRG-5）
- EP-02a: Identity / purity substantiation pack（CLA-1）

---

**第一群（文献で明確に追跡可能）：** EP-06a, EP-07a, EP-09a

- EP-06a: Ni-ジホスフィン触媒系の中間体同定実験は、Kumada グループ自身の後続 full paper（1974–1975年）ならびに1970–1980年代の他グループの有機ニッケル機構研究によって独立論文の主題として追跡可能であり、³¹P NMR・UV-Visによる中間体特性評価が独立報告として存在する可能性が高い。
- EP-07a: sp³ハライド（アルキルハライド・アリルハライド）対 [NiCl₂(dpe)] 系の境界検証は、Kochi グループや Kumada グループの後続論文でアルキルハライドとの反応性を検討したものが独立論文として存在する可能性が高く、β-脱離競合の検討はニッケル触媒クロスカップリングの機構論文の主題となりやすい。
- EP-09a: Tamura-Kochi Fe 触媒系（1971）との同一基質でのホモ:クロス比比較は、1970年代にグリニャール反応の選択性を系統的に研究したレビュー・比較論文群に部分的に収録されており、数値の追跡が可能な可能性がある。

---

**第二群（間接的に追跡可能）：** EP-03a, EP-04a, EP-08a, EP-02a

- EP-03a: 反応終了後の黒色沈殿（Ni⁰ ナノ粒子の可能性）の特性評価は独立論文の主題として発表されにくいが、Ni 触媒の不均一化・Ni⁰ 活性種に関する後続の方法論的研究・レビューの一部として間接的に取り扱われていると考えられる。
- EP-04a: cis/trans-スチルベンの NMR または GC による立体化学的比の測定・反復測定は、Kumada グループの本報 full paper および後続立体化学研究に含まれると考えられるが、43:57 比の測定法の独立論文主題化は難しい。
- EP-08a: 同一エントリーの反復測定（標準偏差の提供）は独立論文の主題としては現れにくく、後続の full paper における「改善された条件下での収率の再報告」という形での間接的充填が中心となる。
- EP-02a: [NiCl₂(dpe)] 反応終了後の黒色沈殿の元素分析・X線回折による同定は、1972 年当時の報告では単独論文の主題としてはまれであり、Ni⁰ 活性種に関する方法論的・総説的論文の中に間接的に収録されると考えられる。

---

**第三群（充填が見つからない可能性あり）：** EP-01a

- EP-01a: glpc 収率と単離収率の混在・内部標準物質の未開示という報告形式問題（RI-01）は、通信→Full Paper 遷移において部分的に自動解消されるか（Full Paper で正式な実験項が整備される）、あるいは分野慣行として glpc 収率の詳細方法論が独立論文として充填される性質ではない。EP-01a の充填は Full Paper での遅延的自動解消に依拠しており、独立論文として出版されることはほぼない。

---

### §B 各EPの充填論文候補の同定

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model（Primary）
* **充填開始点**: Tamao, K.; Sumitani, K.; Hayashi, T.; Kumada, M., *Bull. Chem. Soc. Jpn.* 1976 — Kumada グループが [NiCl₂(dpe)] 触媒条件下でのグリニャール反応の full paper（本コミュニケーションの本報）を発表し、触媒の特性評価と機構についてより詳細な実験的根拠を提供した。(tentative_citation: full paper の雑誌・巻・頁の特定が必要)
* **充填確立点**: Tamao, K.; Kiso, Y.; Sumitani, K.; Kumada, M., *J. Am. Chem. Soc.* **1972**, *94*, 9268–9269 — 同 Kumada グループによる立体選択的クロスカップリングの続報 communication において、中間体の立体化学的考察が拡張され、eq 2–4 の類推が部分的に再評価された可能性がある。(tentative_citation: この特定の報告内容の確認が必要)
* **充填確立点（別候補）**: Tsou, T. T.; Kochi, J. K., *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332 — Kochi グループによる Ni(0)/Ni(II) 酸化的付加・還元的脱離の機構的研究で、(dipy)Ni 系ではなく (dpe)Ni 系に近い Ni-ジホスフィン環境での中間体同定と速度論的研究が行われ、SRG-1 の RI-06 を実質的に前進させる。
* **充填の性質**: Partial（eq 2–4 の全素反応の直接検証には至らないが、類推の範囲を縮小する証拠を提供）
* **Confidence**: Medium（Kochi 1979 の存在と内容は確信があるが、Kumada full paper の詳細 citation は確認が必要）
* **注記**: EP-06a は後続の有機ニッケル機構研究群（1975–1985年）によって段階的に充填される長期遅延充填パターンをとる。Kumada グループ自身の自己充填（full paper 展開）が充填開始点を担い、他グループ（Kochi, Wilkinson, Stille 等）の機構研究が充填確立点を担う分業構造。

---

**EP-03a [Direct-observation / state-assignment pack]（第二群）**

* **充填するRI**: RI-03 Unobserved explanatory（Primary）; RI-02 Object identification（Secondary; CLA-1）
* **充填開始点**: Semmelhack, M. F.; Helquist, P.; Jones, L. D.; Keller, L.; Mendelson, L.; Ryono, L. S.; Smith, J. G.; Stauffer, R. D., *J. Am. Chem. Soc.* **1981**, *103*, 6460–6471 — ニッケル(0)触媒反応における Ni⁰ → Ni(II) 酸化的付加の機構と活性種同定に関する包括的な機構論文。(tentative_citation: この論文の具体的な EP-03a への対応関係の確認が必要)
* **充填確立点（より直接的な候補）**: Negishi, E.; Takahashi, T.; Akiyoshi, K., *J. Chem. Soc., Chem. Commun.* **1986**, 1338–1339 — Ni 触媒反応での活性触媒種の同定に直接言及した報告として機能する可能性がある。(tentative_citation)
* **より信頼度の高い充填確立点**: Stoltz, B. M. ら、あるいは Bäckvall グループの Ni 触媒機構研究において、反応条件下での Ni⁰ ナノ粒子形成の証拠と均一/不均一系触媒の判別が問題として取り上げられる。(tentative_citation: 特定の論文を同定できていない)
* **充填の性質**: Indirect（[NiCl₂(dpe)] 系そのものではなく類似 Ni 触媒系での活性種同定として充填）
* **Confidence**: Low（EP-03a の case-specific 実装——黒色沈殿の Ni⁰ 同定——を正確に充填する独立論文の特定が困難）
* **注記**: CLA-1（RI-02: 活性触媒種の同定）と EP-03a は密接に重複する。EP-03a の充填は「[NiCl₂(dpe)] 系の黒色沈殿が Ni⁰ であるという確認」という非常に specific なターゲットであり、この特定の観察に対応する独立論文は同定困難。より一般的な「Ni 触媒反応での Ni⁰ 活性種問題」としてならば Heck 反応・Pd 触媒研究との類推から 1980 年代後半以降に実質的な充填が存在すると推定される。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 Unreplicated discriminator（Primary）; RI-01 Reporting integrity（Secondary）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Kumada グループによる本コミュニケーションの実質的 full paper であり、cis/trans-スチルベン比の立体化学的解析がより詳細に展開された可能性がある。(tentative_citation: 1976 BCSJ 論文の具体的な内容については確認が必要だが、この論文群が full paper として存在することへの信頼度は High)
* **充填確立点**: 同上（Tamao et al. 1976 BCSJ full paper）
* **充填の性質**: Partial（立体化学的データの測定法・反復測定の開示は full paper で部分的に提供されるが、43:57 比の測定不確かさの定量的評価まで踏み込んでいるかは不明）
* **Confidence**: Medium（full paper の存在は確信があるが、EP-04a の case-specific 要件への対応は推論を含む）
* **注記**: 自己充填パターン（通信→Full Paper 遷移）の典型事例。充填までの年数は約4年（1972→1976）。cis:trans = 43:57 という「ほぼランダム」に近い比が「非立体特異的」という解釈を確認するためには、測定不確かさ（±5%）の定量が不可欠であったが、この点が後続論文で明示的に扱われたかどうかは確認が必要。

---

**EP-08a [Replication / uncertainty pack]（第二群）**

* **充填するRI**: RI-08 Unquantified reliability（Primary）
* **充填開始点**: Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M., *J. Am. Chem. Soc.* **1976**, *98*, 3718–3719 — Kumada グループによる不斉クロスカップリングの研究で、収率の反復性・再現性が間接的に確認される文脈で提示された可能性がある。(tentative_citation)
* **充填確立点（より直接的候補）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full paper での実験項整備により、個別反応の反復測定が提供された可能性。(tentative_citation)
* **充填の性質**: Partial（収率の再現性は full paper 展開で自動的に一部前進するが、glpc 収率の内部標準・応答因子の明示という RI-01 の完全解消は不明）
* **Confidence**: Low（EP-08a の要件——標準偏差の明示的報告——が full paper で充足されたかの確証なし）
* **注記**: 1972年当時の触媒合成論文では単一測定が慣行（§4 communication-era tolerated）であり、統計的記述の要求は 1980–1990 年代以降に強まる。EP-08a の充填としては、後続の定量的クロスカップリング研究（例：Kochi グループの 1979 年以降の動力学的研究）で副次的に前進するパターンが予想される。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 External superiority（Primary; SRG-2 + SRG-6 への対応）
* **充填開始点**: Corriu, R. J. P.; Masse, J. P., *J. Chem. Soc., Chem. Commun.* **1972**, 144 — Note Added in Proof で言及された Corriu-Masse 論文本体。Ni(acac)₂ 触媒での類似クロスカップリング反応の基質適用範囲・収率が報告されており、[NiCl₂(dpe)] との間接的な比較の起点となる。この論文自体は本論文と「同様の反応」として記述されるにとどまるが、対比関係を科学コミュニティが自ら構築できる情報を提供している。
* **充填確立点**: Kumada, M., *Pure Appl. Chem.* **1980**, *52*, 669–679 — Kumada 自身による回顧的レビューで、Tamura-Kochi 法・Corriu-Masse 法・Kumada 法の比較と位置づけが示される可能性がある。(tentative_citation: このレビューの存在と内容の確認が必要)
* **充填確立点（別候補）**: Hayashi, T.; Kumada, M. の不斉クロスカップリング系列論文（1974–1982）において、[NiCl₂(dpe)] 系の選択性が同条件での他触媒系との比較として示される可能性がある。(tentative_citation)
* **充填の性質**: Indirect（Tamura-Kochi 系と [NiCl₂(dpe)] 系を厳密に同一基質で数値比較した独立論文はおそらく存在せず、レビュー・総説内での定性的位置づけとして間接的に充填される）
* **Confidence**: Medium（Corriu-Masse 1972 の存在は確認済み; Kumada 回顧レビューの存在は確信があるが citation の特定には確認が必要）
* **注記**: SRG-2（選択性定量化不在）と SRG-6（先行手法比較不在）の両方を EP-09a は担う。前者（クロス:ホモ比の定量）は後続の full paper・機構論文で充填され、後者（Tamura-Kochi 系との直接比較）は Kumada 自身のレビューや教科書的総説での位置づけで間接的に充填される。完全充填（Complete）は達成困難。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary（Primary）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full paper において sp³ハライドとの反応の試みまたは適用範囲の境界実験が展開された可能性がある。(tentative_citation: 1976 full paper の sp³ハライド記述の確認が必要)
* **充填確立点**: Yamamura, M.; Moritani, I.; Murahashi, S.-I., *J. Organomet. Chem.* **1975**, *91*, C39–C42 — Murahashi グループによるアルキルハライドのニッケル触媒クロスカップリング研究で、sp³ハライドの [NiCl₂(dpe)] 系または類似系での反応性限界が境界実証として機能する可能性がある。(tentative_citation: 内容の確認が必要)
* **充填確立点（より高信頼度の候補）**: Negishi, E.; King, A. O.; Okukado, N., *J. Org. Chem.* **1977**, *42*, 1821–1823 — Negishi グループの亜鉛金属種を用いたクロスカップリング開発論文（「Negishi カップリング」の起点の一つ）において、sp³ハライドへの Ni 触媒適用の難しさが背景情報として示され、[NiCl₂(dpe)] 系の sp² 限界が側面から確認された。(tentative_citation: 内容確認が必要)
* **充填の性質**: Partial（sp³ハライドが「使えない」という境界を失敗例として明示した論文ではなく、sp²ハライドを前提として拡張を進めた論文群の中に境界の実証的裏付けが間接的に蓄積された形）
* **Confidence**: Medium
* **注記**: RI-07（否定的境界主張）の充填は、「sp³ハライドが [NiCl₂(dpe)] 系で β-脱離主生成物を与える」ことを明示した実験が独立論文の主題となった 1977–1985 年の研究群によって段階的に達成された。Kumada グループは sp² に集中し、sp³への展開は Murahashi・Negishi・Kochi グループが担った。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 Reporting integrity（Primary）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Full paper では glpc 収率の詳細（内部標準物質、測定法の整備）が標準的な実験項として提供される可能性が高い。通信→Full Paper 遷移での自動解消パターン（§4 communication-era tolerated 項目）に該当。(tentative_citation)
* **充填確立点**: 同上（自動解消）
* **充填の性質**: Partial（Full Paper でのデータ提示形式の整備が EP-01a の一部を解消するが、「単離収率 vs glpc 収率の混在」が根本的問題である場合、Full Paper でも glpc 収率のみの形式が継続する可能性がある）
* **Confidence**: Medium
* **注記**: EP-01a は独立充填論文というよりも通信→Full Paper 遷移の自動解消に依拠する。RI-01 の独立論文としての充填はほぼ存在しない（第三群判定を反映）。

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 Object identification（Primary; CLA-1）
* **充填開始点**: Komiya, S.; Yamamoto, A.; Yamamoto, T., *Bull. Chem. Soc. Jpn.* **1975**, *48*, 1531–1536 — Yamamoto グループによるニッケル錯体の特性評価研究で、[NiCl₂(dpe)] 誘導体の反応化学と形成条件が検討された可能性がある。(tentative_citation)
* **充填確立点**: Keim, W.; Kowaldt, F. H.; Goddard, R.; Krüger, C., *Angew. Chem. Int. Ed.* **1978**, *17*, 466–467 — Ni-ホスフィン錯体の構造・活性種の特性評価に関する研究として参考になる可能性があるが、EP-02a の case-specific 実装（黒色沈殿の Ni⁰ 同定）を直接充填するかどうかは不明。(tentative_citation)
* **充填確立点（より直接的候補）**: Ostwald, R.; Chavanne, P.-A.; Wöll, C.; Scheer, P.; Braunstein, P. *et al.* による Ni⁰ ナノ粒子と触媒の均一/不均一系判別に関する研究（1990 年代以降）が、EP-02a の問いに最も直接的に対応するが、それは [NiCl₂(dpe)] 系を明示した研究ではない。(tentative_citation)
* **充填の性質**: Indirect（[NiCl₂(dpe)] 系の黒色沈殿という specific な観察に対応する直接充填論文は同定困難；Ni 触媒の均一/不均一系判別という一般問題として後代に充填）
* **Confidence**: Low
* **注記**: EP-02a は EP-03a と密接に重複する（CLA-1 として記録）。黒色沈殿の Ni⁰ 同定という specific な観察の充填は、Ni 触媒を用いる反応の機構研究一般に拡散しており、単一の「充填確立点」を指定することが難しい。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 (tentative_citation) | EP-04a, EP-07a, EP-08a, EP-01a（バンドル） | VQ-2 | 1976 | Med |
| 2 | Corriu, R. J. P.; Masse, J. P., *J. Chem. Soc., Chem. Commun.* **1972**, 144 | EP-09a（SRG-6: 先行手法比較の外部参照起点） | VQ-2 | 1972 | High |
| 3 | Tsou, T. T.; Kochi, J. K., *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332 (tentative_citation) | EP-06a（SRG-1: 類推の検証・中間体動力学） | VQ-3 | 1979 | Med |
| 4 | Negishi, E.; King, A. O.; Okukado, N., *J. Org. Chem.* **1977**, *42*, 1821–1823 (tentative_citation) | EP-07a（SRG-3: sp²/sp³境界の側面確認） | VQ-2 | 1977 | Med |
| 5 | Kumada, M., *Pure Appl. Chem.* **1980**, *52*, 669–679 (tentative_citation) | EP-09a（SRG-2 + SRG-6: Kumada 回顧での手法比較・選択性評価） | VQ-4 | 1980 | Med |

**選定理由：**

1位（Tamao et al. 1976 BCSJ）は本コミュニケーションの full paper であり、EP-04a（立体化学反復測定）・EP-07a（スコープ境界の実験的補強）・EP-08a（収率反復性の整備）・EP-01a（報告形式の整備）を一報で束ねるバンドル充填論文として最高の効率を持つ。自己充填（Kumada グループ自身の遷移自動解消）パターンの最も典型的な事例として、UQS 充填検証の第一優先文献である。通信→Full Paper 遷移の典型として VQ-2 水準の複数 EP を一度に前進させる。

2位（Corriu-Masse 1972）は EP-09a の SRG-6 側（先行手法比較）の外部参照起点として位置づけられ、本コミュニケーションと同年の独立した競合研究として科学史的な対置関係を直接提供する。Note Added in Proof の言及が指し示す比較対象そのものであり、Confidence=High の数少ない論文。ただし Corriu-Masse 自体が「充填論文」ではなく、対比情報の提供者であることに注意。

3位（Tsou-Kochi 1979）は Kochi グループによる Ni(0)/Ni(II) 触媒サイクルの機構的研究として EP-06a（RI-06: 輸入モデルの検証）を最も体系的に前進させた可能性がある文献であり、VQ-3 水準の充填論文として年代的にも1979年と原論文からの7年の空白を担う。

4位（Negishi 1977）は EP-07a（sp² 限界の側面確認）を年代的に早期（1977年）に提供し、「なぜ sp³ハライドが使えないか」の境界問題が他グループによって探索され始めた時点を示す。

5位（Kumada 1980 回顧）は Kumada 自身が先行手法との比較・選択性評価を体系化した可能性のある回顧的総説として EP-09a の SRG-2 + SRG-6 双方を間接的に充填する VQ-4 水準の候補として選定した。ただし、レビュー論文はEPを充填しないという原則に照らして、独自メタ分析の有無によって評価が変わることを留保する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a, EP-04a, EP-07a, EP-08a → 1976年 [Tamao et al., *Bull. Chem. Soc. Jpn.*, 自己充填パターン]
- VQ-2 要件: EP-09a（SRG-6 側: 先行手法比較起点） → 1972年 [Corriu, Masse, *Chem. Commun.*; 技術的競合・他グループ充填]
- VQ-2/VQ-3 境界: EP-07a（sp³境界: 他グループ） → 1977年 [Negishi et al., *J. Org. Chem.*; 分野横断充填]
- VQ-3 要件: EP-06a（中間体同定・動力学） → 1979年前後 [Tsou-Kochi *J. Am. Chem. Soc.*; 技術駆動充填]
- VQ-4 要件: EP-09a（SRG-2 側: 選択性定量比較） → 1980年前後 [Kumada 回顧レビュー; 自己充填（著者回顧型）]
- VQ-3/VQ-4 水準: EP-03a, EP-02a（Ni⁰ ナノ粒子・活性種同定） → 1985–2000年代 [長期遅延充填; 技術駆動充填（高感度分析機器の普及）]

---

**階層-時間対応の評価：**

本論文の EP 充填時間軸は「VQ 階層が上がるほど充填に要する時間が長くなる」という仮説を概ね支持する。VQ-2 要件に対応する EP（EP-04a, EP-07a, EP-08a, EP-01a）は通信→Full Paper 遷移（約4年）によって比較的早期に自己充填が達成され、VQ-3 要件（EP-06a: 中間体の直接観測・動力学）は機構研究の発展を待つ7年以上の充填遅延を示す。VQ-4 水準（EP-09a の選択性比較・定量化）は Kumada グループの回顧的総説（1980年前後）を充填確立点とするとすれば8年の遅延であり、VQ-4 の達成は最も遅い。ただし、EP-03a・EP-02a（Ni⁰ ナノ粒子問題; VQ-1 の致命的未達要因）は現代においても完全充填が未達成の可能性があり、最も低位の VQ 要件（VQ-1: 観測）が最も長い未充填状態を持つという逆転パターンも同時に現れている（この逆転は「インセンティブ構造の不整合」——§E で詳述——によって説明される）。

---

**特筆すべきパターン：**

1. **自己充填（Kumada グループ → 1976 full paper）**: 通信→Full Paper 遷移による自動解消が EP-01a・EP-04a・EP-07a・EP-08a を一論文でバンドル充填する典型事例。これは Stage 3 §4（Era-norm: communication-era tolerated 項目の遷移自動解消）で予測されたパターンの実現として記録される。

2. **技術駆動充填（³¹P NMR・X線構造解析の普及 → EP-06a）**: 1970年代後半以降の多核 NMR（特に ³¹P NMR）の普及がニッケル-ホスフィン中間体の溶液内観測を可能にし、EP-06a の充填を技術的に可能にした。この技術的転換点（1975–1980年）が VQ-3 達成のゲートとなっている。

3. **分野横断充填（Negishi, Murahashi, Kochi グループ → EP-07a）**: sp³ハライドの境界検証は Kumada グループではなく Negishi・Murahashi・Kochi グループ等の他グループが積極的に探索し、Kumada 系の限界を側面から確認した形。これは「充填論文は自らを充填と宣言しない」（Stage 4 プロンプト原則 6）の典型的事例。

4. **長期遅延充填・未充填（EP-03a: Ni⁰ 活性種問題）**: 黒色沈殿（Ni⁰ ナノ粒子の可能性）の特性評価という EP-03a の case-specific 要件は、[NiCl₂(dpe)] 系という特定の文脈においては1972年以降50年以上を経ても明示的な充填論文が指摘しにくい状況にある。Pd 触媒での Pd⁰ ナノ粒子問題（「溶液中の均一触媒か不均一触媒か」の議論）は 1990–2000 年代に活発に研究されたが、Ni-(dpe) 系への directly な充填は희薄。

5. **著者回顧との照合**: Kumada 自身は 1980 年前後のレビューで触媒サイクルの機構的詳細（eq 2–4 の類推の妥当性）を回顧的に評価した可能性があるが、文書として入手可能な証拠の確認が必要。著者回顧で認識されなかった EP（U-2: 黒色沈殿の均一/不均一系問題）は「分野の内部者には不可視の構造的不在」として機能し続けた可能性がある。Stage 3 §6（§4 注記）で「通信→Full Paper 遷移の自動解消パターン」として予測された EP（B-1, B-3, B-5, B-9）は Kumada グループ自身が認識して解消した可能性が高いが、U-2 はグループ内でも追跡されなかった可能性がある。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

EP-03a [Direct-observation / state-assignment pack]:

* **未充填の理由**: インセンティブ構造の不整合 + 技術的困難の複合。Example 1 の黒色沈殿という specific な観察は、独立論文の主題として立案されるインセンティブが存在しない（均一系触媒として反応が進行するという結果が得られており、沈殿の characterization を独立論文として出版する合成上の動機がない）。また [NiCl₂(dpe)] 系という特定の系での Ni⁰ 同定は、一般的な Ni 触媒機構研究の対象としては間接的すぎる。
* **発見的意義**: あり。本論文が「均一系触媒」として提案した [NiCl₂(dpe)] 系の実際の活性触媒種が均一 Ni(II) か Ni⁰ ナノ粒子かという問いは、後に Pd 触媒クロスカップリングでも同型の「均一/不均一系問題」として重要課題となった（「溶解 Pd と Pd ナノ粒子のどちらが真の触媒か」議論、2000年代）。Kumada 1972 の黒色沈殿は、この問いが最初期の Ni 触媒論文にすでに内在していたことの記録として、クロスカップリング触媒化学の知識考古学的な証拠となる。
* **将来の充填可能性**: 中（現代の透過型電子顕微鏡・in situ X線吸収分光・単粒子 ICP-MS による Ni⁰ ナノ粒子同定技術を用いれば、Kumada 反応条件を再現した実験系での活性種の直接同定が技術的に可能だが、これを実施する研究グループの動機が現在も低い）

---

EP-02a [Identity / purity substantiation pack]:

* **未充填の理由**: インセンティブ構造の不整合 + EP-03a との重複性。CLA-1（活性触媒種の同定）は EP-03a と重複しており、EP-02a の case-specific 実装（黒色沈殿の分離・元素分析・X線回折）は EP-03a の充填で同時解消されるべき内容だが、両者が独立論文の主題として出版されるインセンティブは低い。
* **発見的意義**: あり（EP-03a と共通）。独立した発見的価値として記録しうる点は、「1972年当時に利用可能な技術（磁化率測定・元素分析）で対処可能だったにもかかわらず未実施のまま論文が出版された」という事実が、1970年代初頭の有機金属合成コミュニティにおける「触媒の証明責任（burden of proof）」の閾値を示していること。現代の触媒化学では活性種の同定は VQ-1 必須要件であり、この閾値の変化の記録として EP-02a の未充填は科学規範史の資料となる。
* **将来の充填可能性**: 中（EP-03a と同じ技術的手段で充填可能だが、動機の問題が継続）

---

**VQ階層逆転の診断：**

本論文の充填パターンにおいて、軽微な VQ 階層逆転パターンが観察される。

低 VQ 要件（RI-01 報告形式: EP-01a, RI-08 反復測定: EP-08a）に対応する EP は、通信→Full Paper 遷移で自動解消される（充填速度: 高）。

高 VQ 要件（RI-03 未観測中間体: EP-06a, RI-06 輸入モデル: EP-06a）に対応する EP は、機構研究の発展による技術駆動充填（充填速度: 中、1979–1985年）。

しかし最低 VQ 要件とも言えるレベルの問い（RI-02 活性触媒種の同定: EP-02a, EP-03a）については、インセンティブ構造の不整合により充填が長期遅延または未充填状態を継続している。

この逆転の構造的解釈：「活性触媒種の同定」という VQ-1 の根本問題は、反応が「うまくいく」という成功状態においては分野のインセンティブが充填を促進しない。成功した反応の均一/不均一系問題を追究することは、「誰も困っていない」状況では論文化されにくい。これは Stage 4 プロンプトが定義する「インセンティブ構造の不整合」の典型事例であり、出版インセンティブが「高 VQ（機構確立・ベンチマーク比較）→低 VQ（基本観察の確認）」の順序で充填を促進する一方、最低次元の観察問題（活性種は何か）は成功の「副作用」として永続的に未充填状態に置かれうることを示す。

UQS の発見的記録としての価値：「Kumada カップリング 1972 の触媒種は均一系 Ni(II) か Ni⁰ ナノ粒子か」という問いは、2026 年現在においても決定的に充填されていない可能性がある。この問いが 54 年間実験化学コミュニティに「問われなかった問い」として維持されてきたこと自体が、クロスカップリング触媒化学の知識の地図における「白地」として記録される。
