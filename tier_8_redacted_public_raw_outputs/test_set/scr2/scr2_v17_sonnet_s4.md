```
prompt_version: stage4-v1-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Templ, Hwang, Schwemin, Baltaci, Borchardt 2025（RSC Mechanochemistry, full_paper）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-07a

- **EP-03a** Direct-observation / state-assignment pack：「不均一触媒か均一系溶出Pd触媒か」という帰属問題は、Pd多相触媒の分野全体で繰り返し争われてきた中心的問いであり、ホットフィルトレーション・Hg毒化・ICP-MS定量を主題とする独立論文が継続的に発表されている。メカノ触媒系に特化した同種の研究も2022年以降加速しており、直接追跡可能。
- **EP-07a** Boundary-test pack：Pdボール触媒のリサイクル実験は「直接メカノ触媒」の実用性主張の中核的検証項目であり、BorchardtグループのコンSuzuki/Sonogashira先行論文では実際に実施されている。Heck反応への拡張も同グループの自己充填または後続論文での充填として追跡可能。

---

**第二群（間接的に追跡可能）：** EP-02a, EP-04a, EP-05a, EP-06a, EP-09a

- **EP-02a** Identity / purity substantiation pack：XPSによるPdボール表面状態の同定はメカノ触媒論文の標準的補足データとして登場しているが、独立論文の主題になることは少なく、触媒特性評価論文の一部として間接的に追跡可能。
- **EP-04a** Discrimination / replication pack：ArI/ArBr競合実験はPd触媒論文で汎用的だが、ミリング系に特化した系統的競合実験は限定的。類似系（溶液相Heck）経由での間接充填は高確度で存在する。
- **EP-05a** Quantitative-ranking substantiation pack：Hammettスキームによる電子効果の定量はPd Heck反応の古典的手法だが、ミリングボール系への適用例は稀であり、間接充填（溶液相データの類推転用）が主体となる。
- **EP-06a** Analogy-validation pack：KCl/KOAc使用後のSEMによる「snowballing」視覚確認はBorchardtグループ内の装置的課題として解決可能だが、独立論文の主題にはなりにくく、関連するバルキング剤比較論文の一部として間接的に追跡可能。
- **EP-09a** Internal benchmark pack：先行メカノ化学的Heckプロトコル（refs 7–10）との定量比較は、メカノケミカルC–C結合形成に関するレビュー論文やメタ分析論文の中で部分的に充填される可能性がある。

---

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a

- **EP-01a** Reporting-coherence pack：NMR収率（最適化Table）と単離収率（スコープTable）の混在・反応時間不整合はRI-01（報告形式問題）に起因し、Full Paperへの論文拡張時に自動解消されるか、当該短報の修正版（corrigendum）で解消される類の問題であり、独立した充填論文として発表されない。
- **EP-08a** Replication / uncertainty pack：複数回測定・標準偏差の報告は分野慣行の問題であり、RI-08は報告形式上の不足に過ぎない。Full Paper展開時に自動解消されるが、それ自体を主題とする論文は存在しない。

---

### §B 各EPの充填論文候補

---

**EP-03a Direct-observation / state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（+ RI-04 Unreplicated discriminator; SRG-1）
* **充填開始点**: Basoccu, Caboni, Porcheddu — *ChemSusChem* 2025, e202402547 — scr2が参照する浸出実験の方法論論文（ICP-MSによるPd定量とフィルトレーション後活性確認を含む）であり、RI-03の閾値設定に必要な分析フレームワークを提供している。ただし本論文はscr2に先行して発表されており、scr2著者が既にこの手法を参照した上で「not mainly」という定性的結論のみを本文に記載した点で、EPの完全充填ではなく方法論的基盤を構築している。
* **充填確立点**: **未同定**。Borchardtグループがscr2の後続論文（Full PaperまたはMechanistic Study）でホットフィルトレーション試験またはHg毒化試験を実施し、結果を定量的閾値付きで報告する論文が有力候補だが、2026年4月時点で特定できていない。
* **充填の性質**: Partial（Basoccu 2025は方法論的基盤のみ；直接充填論文は未同定）
* **Confidence**: Medium（Basoccu 2025の存在と内容は確信あり；EP充填確立論文は未同定でLow）
* **注記**: scr2のref 48として引用されているため、Basoccu 2025はscr2に先行する論文。直接充填としては、Borchardtグループの後続論文または第三者グループによるメカノ触媒Pd漏出問題の系統的研究が候補。EP-02aおよびU-1, U-2とバンドル充填される可能性が高い。

---

**EP-07a Boundary-test pack（第一群）**

* **充填するRI**: RI-07 Unsupported boundary（+ RI-02 secondary; SRG-3）
* **充填開始点（間接）**: Pickhardt, Schindler, Borchardt et al. — *Angew. Chem. Int. Ed.* 2022, 61, e202201031（推定; scr2 ref 44に相当する可能性が高い）— PdボールによるSuzuki–Miyaura coupling論文で、複数回のリサイクル実験（収率/サイクル、ボール質量変化）が実施されている可能性が高い。ただし対象はSuzuki条件であり、Heck固有の充填ではない。
* **充填確立点**: **未同定**。BorchardtグループによるHeck反応のFull Paper版または続報で、Heck条件下（DMF、120°C、K₂CO₃、ArI）でのリサイクル実験が実施される可能性が高い。2026年4月時点で特定できていない。
* **充填の性質**: Indirect（Pickhardt 2022はSuzuki系のみ；Heck系直接充填は未同定）
* **Confidence**: Medium（Pickhardt 2022の存在はHigh；Heck系充填はLow）
* **注記**: Borchardtグループがscr2を「速報」として発表し、Full Paperで詳細データ（リサイクル、温度プロファイル、表面分析）を提供するパターンは同グループの先行例から示唆される。自己充填の可能性が最も高い。EP-02aとバンドル充填が期待される。

---

**EP-02a Identity / purity substantiation pack（第二群）**

* **充填するRI**: RI-02 Object identification（SRG-3 secondary）
* **充填開始点（間接）**: Wohlgemuth, Mack, Schindler, Pickhardt, Borchardt — *Angew. Chem. Int. Ed.* 2024, 63（ref 39に対応する可能性が高い）— 直接メカノ触媒の総合的評価論文であり、XPS（Pd 3d領域）またはSEMによるボール表面の反応前後分析が含まれている可能性がある。ただし本論文はscr2に先行して発表されており、直接の充填論文ではない。
* **充填確立点**: **未同定**。反応条件下（空気、120°C）でのPd表面酸化状態のin situ XPS または反応後XPS分析は、専門的な表面科学グループとの共同研究として充填される可能性がある。
* **充填の性質**: Indirect（Wohlgemuth 2024は別反応系の可能性；直接充填未同定）
* **Confidence**: Low
* **注記**: Pd(0)表面がPdOに部分酸化される問題（B-18, U-2）はEP-03aとも関連しており、XPS分析がホットフィルトレーション研究とバンドルで充填される可能性がある。技術的難易度（ミリング条件下のin situ分析）から、充填に時間がかかる可能性がある。

---

**EP-04a Discrimination / replication pack（第二群）**

* **充填するRI**: RI-04 Unreplicated discriminator（SRG-1 secondary; SRG-5, SRG-6）
* **充填開始点**: **未同定**。ArI/ArBr等量混合競合実験はHeck反応機構研究の標準手法だが、ミリングボール系での系統的な競合実験はscr2以降の発表として特定できていない。
* **充填確立点**: **未同定**
* **充填の性質**: —（未同定）
* **Confidence**: Low
* **注記**: フェノール用量-応答実験については、Pd毒化実験の一般的な文献（Sheldon, Biffis, Reetz等の溶液相Pd触媒論文）で間接的な方法論的根拠が存在する。ミリングボール系固有の実験としての充填は、Borchardtグループのメカニズム論文（A-1の解消に向けた論文）に含まれる可能性がある。

---

**EP-05a Quantitative-ranking substantiation pack（第二群）**

* **充填するRI**: RI-05 Qualitative overread（SRG-2）
* **充填開始点（間接）**: Heck反応の電子効果に関するHammett相関は、Amatore, Jutand et al. の溶液相研究（1990年代〜2000年代）で確立されており、C(sp²)–I vs C(sp²)–Br選択性の速度論的根拠として間接的に充填可能。
* **充填確立点**: **未同定**。ミリングボール系固有のHammett相関またはArI/ArBr競合速度論データは特定できていない。
* **充填の性質**: Indirect（溶液相Heck速度論からの類推転用）
* **Confidence**: Medium（間接充填の存在はHigh；直接充填はLow）
* **注記**: RI-03（SRG-1）が解消されない限り、活性種が表面Pd(0)か溶出Pd種かが不明のため、Hammett相関の解釈自体が宙吊りになる。SRG-2の充填にはSRG-1の先行解消が実質的に必要。

---

**EP-06a Analogy-validation pack（第二群）**

* **充填するRI**: RI-06 Imported model（SRG-6）
* **充填開始点**: **未同定**。KCl/KOAc使用後のPdボール表面のSEM/光学顕微鏡観察を主題とする独立論文は特定できていない。
* **充填確立点**: **未同定**
* **充填の性質**: —（未同定）
* **Confidence**: Low
* **注記**: 「snowballing」現象はK₂CO₃を用いるメカノ化学反応に特有の観察であり、分野横断的な充填よりもBorchardtグループ内での後続充填の可能性が高い。NaCl vs KClアニオン/カチオン弁別実験は、溶液相Pd触媒のCl⁻配位効果文献（Amatore, Jutand）からの間接的根拠は存在するが、ミリング系固有の実験は未充填。

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority（VQ-4ルート）
* **充填開始点（間接）**: メカノケミカルC–C結合形成の総説論文（Bolm, Hernández, or Friščić group レビュー; *Chem. Soc. Rev.* 2023-2025）が先行Heckプロトコル（Declerck/Lamaty 2012, Tullberg/Frejd 2004-2006, Xiang/Yu 2024）との比較データを部分的に含む可能性がある。
* **充填確立点**: **未同定**（特定のレビュー論文が直接比較を行っているかは確認できていない）
* **充填の性質**: Indirect（レビュー論文経由の部分充填）
* **Confidence**: Low
* **注記**: VQ-4は現時点でVQ-3が未達なため到達不能。EP-09aの充填は研究の成熟段階の問いであり、scr2から5–10年後のレビュー論文での体系的比較が最も自然な充填経路。

---

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity（SRG-4 primary; CLA）
* **充填開始点**: **未同定**（独立論文としての充填を期待しない）。Full Paper展開（Borchardtグループ）でのブリッジ実験の追加が最も現実的な解消経路。
* **充填確立点**: **未同定**
* **充填の性質**: —（第三群）
* **Confidence**: Low（Full Paper存在自体が未確認）
* **注記**: 第三群の定義通り、RI-01起因のEPは論文形式拡張で解消される性質のもの。scr2がFull Paperに展開されれば自動解消が期待されるが、これ自体の存在が未確認。

---

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability（SRG-4 secondary; CLA）
* **充填開始点**: **未同定**（独立論文としての充填を期待しない）
* **充填確立点**: **未同定**
* **充填の性質**: —（第三群）
* **Confidence**: Low
* **注記**: EP-01aと同様、Full Paper展開での自動解消が最も自然な経路。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Borchardt group, Heck Full Paper / Mechanistic Study（未同定） | EP-01a, EP-07a, EP-08a（自己充填） | VQ-2 | 2025–2026 | Low |
| 2 | Borchardt group, Pd ball surface catalysis mechanistic study（未同定） | EP-03a, EP-02a, EP-04a | VQ-3 | 2025–2026 | Low |
| 3 | Basoccu, Caboni, Porcheddu — *ChemSusChem* 2025, e202402547 | EP-03a（方法論的基盤） | VQ-3 基盤 | 2025 | Medium |
| 4 | Pickhardt, Schindler, Borchardt et al. — *Angew. Chem. Int. Ed.* 2022（推定 ref 44） | EP-07a（Suzuki系間接充填） | VQ-2 間接 | 2022 | Medium |
| 5 | レビュー論文：Mechanochemical cross-coupling comparative analysis（未同定） | EP-09a | VQ-4 基盤 | 2025–2026 | Low |

**選定理由:**

本推奨リストは、EP充填の実現可能性が最も高い経路を優先順に配置している。第1位と第2位はBorchardtグループ自身による自己充填論文（Full PaperまたはMechanistic Study）であり、scr2という速報論文の後続展開として最も自然かつ情報量が大きい。これらが実現すれば、VQ-2要件（EP-01a, EP-07a）とVQ-3要件（EP-03a, EP-02a）の主要部分が1–2論文でバンドル充填される可能性がある。第3位は現時点でMedium confidenceで存在が確認できる唯一の関連論文であり、EP-03a充填のmethodological onsetとして位置づける。第4位はscr2 ref 44に対応する既存論文で、EP-07aのSuzuki系間接充填として追跡可能。第5位はVQ-4要件に向けた長期的な充填経路として提示する。

**重要な限界の注記:** scr2は2025年出版の論文であり、本分析時点（2026年4月）では後続充填論文の特定が困難である。リストの第1・2・5位はConfidence: Lowであり、EP充填検証を実施するには実際の文献検索（Web of Science、Scopus等での被引用論文検索、Borchardtグループの最新発表確認）が必要。推奨選定の主目的は「充填すべきEPの優先順位の明示」と「充填経路の構造化」にある。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

```
VQ-2 要件:
  EP-01a (RI-01) → 未同定（Full Paper展開で自動解消、時期不明）     [自己充填候補]
  EP-07a (RI-07) → 2022 [Pickhardt et al.] Suzuki系間接充填         [間接充填]
                 → 未同定 Heck直接充填（推定2025-2026）              [自己充填候補]

VQ-3 要件:
  EP-03a (RI-03) → 2025 [Basoccu et al.] 方法論的基盤（間接）       [分野横断充填]
                 → 未同定 直接充填（推定2025-2026）                 [自己充填候補]
  EP-04a (RI-04) → 未同定                                          [未充填]
  EP-06a (RI-06) → 未同定                                          [未充填]
  EP-02a (RI-02) → 未同定（XPS研究として推定2025-2026）             [技術駆動充填候補]
  EP-05a (RI-05) → 1990s-2010s [溶液相Heck速度論] 間接のみ          [分野横断間接充填]

VQ-4 要件:
  EP-08a (RI-08) → 未同定（Full Paper展開で部分解消）               [自己充填候補]
  EP-09a (RI-09) → 未同定（レビュー論文経由）                       [分野横断間接充填候補]
```

**階層-時間対応の評価:**

VQ階層と充填時間の対応仮説（「上位VQほど充填に時間を要する」）については、現時点では以下のことが言える。EP-07a（VQ-2要件）は2022年のPickhardt論文が間接充填として利用可能であり、EP-03a（VQ-3要件）の方法論的基盤は2025年のBasoccu論文が提供するが直接充填は未同定であり、EP-09a（VQ-4要件）は現時点で完全に未充填という序列は仮説を支持する。一方、EP-05a（VQ-3要件、RI-05）については溶液相研究による間接充填がすでに1990年代から存在しており、充填時間が長くなるという仮説と必ずしも一致しない点は留意が必要。ただし間接充填はVQ-3の要件を完全には満たさないため、直接充填の不在という点では仮説は保持される。

**特筆すべきパターン:**

- **自己充填の高い蓋然性**: BorchardtグループはSuzuki(2022)→Sonogashira→Heck(2025)という直接メカノ触媒の系統的拡張を行っており、Heck Full Paperでの自己充填（EP-01a, EP-07a, EP-08a, EP-02a, EP-03aのバンドル充填）が最も蓋然性の高い充填経路である。自己充填は通常原論文から1–3年以内に起こる。
- **分野横断充填（EP-03a）**: Pd浸出問題はメカノケミストリー分野外（不均一触媒化学、電気触媒化学）で長く研究されており、方法論（ホットフィルトレーション、Hg毒化、ICP-MS）が外部から充填される分野横断充填パターンが確認できる。
- **未充填の可能性（EP-04a, EP-06a）**: ArI/ArBr競合実験（EP-04a）とSnowballing機構検証（EP-06a）は、scr2固有の問いであり分野横断充填が起こりにくい。自己充填論文の登場を待つ状況。
- **長期遅延充填候補（EP-05a, EP-09a）**: Hammett相関（EP-05a）および先行プロトコルとの定量的ベンチマーク（EP-09a）は、VQ-3が達成されたのち初めて意味ある充填が可能になる問いであり、5–10年スケールの長期遅延が予想される。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

**EP-04a Discrimination / replication pack（SRG-1 secondary, SRG-5, SRG-6）:**

* **未充填の理由**: 技術的困難 + 関心の欠如の組み合わせ。ArI/ArBr競合実験はミリング中のサンプリングが困難であり（密閉された高温系でのリアルタイム計測）、かつ「ArBrが反応しない」という観察が合成上の利点として提示されるため、その機構的根拠を問う独立論文が発表されにくい状況にある。
* **発見的意義**: あり。「反応しない基質が合成的に価値ある選択性として提示される場合、その不活性の機構が問われないまま分野の共通前提になる」というパターンはUQSが検出できる系統的回避の典型形態であり、メカノ触媒Heck文献が今後蓄積した際に横断的に確認すべき点として記録価値がある。
* **将来の充填可能性**: 中。in situ固体¹H NMRまたはラマン分光法によるミリング中のモニタリング技術が普及すれば充填可能。BorchardtグループのA-1に対応する機構研究が発表される際にバンドル充填される可能性がある。

---

**EP-06a Analogy-validation pack（SRG-6）:**

* **未充填の理由**: 関心の欠如。「Snowballing」という観察は論文中では嫌塩基環境の補足説明として位置づけられており、独立した表面科学的研究として発展する機会が生まれにくい。KCl/KOAcの阻害機構（物理的 vs 配位子的）という問いは合成論文の読者にとって副次的関心事に留まる。
* **発見的意義**: あり。「実用的最適化を経て発見されたバルキング剤効果の機構が問われないまま残る」という構造は、合成論文における「条件探索→合成例示→機構放置」パターンの典型例として記録できる。この問いを独立して拾い上げたのはUQSのみであり、後続研究のフラグとして機能しうる。
* **将来の充填可能性**: 低。SEM/EDSによるボール表面組成分析は技術的には容易だが、独立論文として発表されるには追加的な動機（別の反応でも同様の現象が観察される、工業的に問題になる等）が必要。

---

**EP-09a Internal benchmark pack（VQ-4ルート）:**

* **未充填の理由**: VQ-3が未達という構造的制約。EP-09aが完全に充填されるためには、（a）先行プロトコル（refs 7–10）の詳細なデータが再現実験で確認され、（b）本論文プロトコルとの直接比較（収率、E-factor、基質スコープ幅、TON）が実施される必要がある。VQ-3未達の現状では比較の基盤となる活性種の同一性も未確立であり、定量比較の解釈が困難。
* **発見的意義**: あり。「後続研究がなければ導入部の数値引用（Dropped Quantitative Benchmark: C-1）が永遠に宙吊りになる」という構造は、短報形式の論文が引用したベンチマークを実質的に放棄するパターンとして記録できる。この構造はUQSのC-1分類が捕捉したものであり、EP-09aの未充填を通じて「C-1が引用された数値への責任を後続研究に転嫁する構造」であることが実証される。
* **将来の充填可能性**: 中。メカノケミカルHeck反応の複数プロトコルを比較するメタ分析型論文（Borchardt, Porcheddu, またはReviewグループ）が発表された際に充填可能。分野の成熟度が上がれば自然に実現される種類の問い。

---

**EP-01a, EP-08a（第三群）:**

* **EP-01a 未充填の理由**: 報告形式問題 — NMR収率/単離収率の混在と時間不整合はFull Paper展開での自動解消を期待する種類の問題であり、独立論文としての充填を期待しない。
* **EP-08a 未充填の理由**: 報告形式問題 — 標準偏差と複数回測定の欠如は分野慣行（合成短報）に起因し、Full Paper展開での自動解消が最も現実的な経路。
* **発見的意義**: EP-01aとEP-08aについては「UQSの発見」としてよりも「分野慣行上の未解消」として記録するに留める。ただし両者が組み合わさって「最適化データとスコープデータの横比較が不能」という構造（SRG-4）を形成しており、この複合的な報告整合性の問題はRI-01の「単独論文では低影響だが複合すると横比較を無効化する」事例として制度的記録価値がある。
* **将来の充填可能性**: EP-01a: 高（Full Paper展開で解消）。EP-08a: 高（Full Paper展開または標準偏差報告の分野慣行化）。

inference_time_sec: not available — inject externally
```
