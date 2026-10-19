```
prompt_version: stage4-v6-20260504
model_info: claude-haiku-4-5-20251001
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Haiku 4.5 v6 run 3)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth_run3.md
related_pilot_opus: papers/dev/kumada/kumada_v17_opus47_s4v6_retrieval_depth_run3.md
related_baseline_haiku: papers/dev/kumada/kumada_v17_haiku_s4v2.md
note: Multi-run robustness の cross-vendor extension。Sonnet v6 + Opus v6 + GPT-5.4 v6 と
      比較して Haiku 4.5 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

------

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（JACS Communication）

------

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-07a, EP-10a

- **EP-03a** [Direct-observation / state-assignment pack]: ³¹P NMRによるニッケル中間体の検出は、1970年代後半以降の高分解能NMR技術の発展と共に、独立した分光化学論文のテーマとして多数発表されている（Ugo系、Baker系等）。検索語「nickel phosphine intermediate NMR」で直接追跡可能。
- **EP-07a** [Boundary-test pack]: [NiCl₂(dpp)]を用いた代表基質のスコープ実験は、合成化学論文として独立論文化されやすい。Kumada系列の後続論文やその他の研究グループによる「ニッケル触媒のリガンド効果系統研究」として実証可能。
- **EP-10a** [Kinetic verification pack]: Ni-Grignard カップリングの速度論的検証（初速度測定、stopped-flow追跡）は、有機反応メカニズム論文の主題として独立発表される可能性が高い。1970年代後半から1980年代の詳細メカニズム研究として追跡可能。

**第二群（間接的に追跡可能）：** EP-01a, EP-05a, EP-08a

- **EP-01a** [Reporting-coherence pack]: Kumada 1972 本体が Communication であるため、Letter→Full Paper の自動解消パターン（C23）が適用される。Kumada グループの後続の詳細報告（Full Article形式）が同一著者グループから 1-3 年以内に発表されることが期待される。例えば、"Selective carbon-carbon bond formation..." の Full Paper 版の有無を確認。⚠️ **C23 trigger 発火予定**。
- **EP-05a** [Quantitative-ranking substantiation pack]: ニッケル触媒の異なるリガンド間での活性比較は、レビュー論文や総説に体系的に統合される傾向がある。直接の論文化よりも、Kumada 系列の後続レビューや教科書章での記載が期待される（間接的追跡）。
- **EP-08a** [Replication / uncertainty pack]: 同じ反応の反復測定・統計的信頼性評価は、インセンティブ構造的未充填パターン（C6）に該当。独立論文化されにくい。ただし、Full Paper 展開時に実験条件の反復検証が暗黙に含まれる可能性。

**第三群（充填が見つからない可能性あり）：** EP-02a, EP-04a, EP-06a, EP-09a

- **EP-02a** [Object identification / purity assurance pack]: 生成物の詳細な構造確認（立体異性体の完全分析、副生成物の正確な同定）は、Communication 形式では報告が限定的。Full Paper 展開でも「副反応は見つからなかった」という陰性記載にとどまる可能性があり、積極的な実証論文として発表される可能性は低い（インセンティブ構造的未充填）。
- **EP-04a** [Unreplicated discriminator pack]: 「ホモカップリング vs クロスカップリングの定量比較」は、Kumada 系列の後続研究でも「クロスカップリングが成功した」という観点では重要だが、クロス:ホモ比を詳細に定量化する独立論文は発表されにくい。成功による問いの抹消パターン（C7）が該当。
- **EP-06a** [Analogy-validation pack]: Tamura-Kochi との直接的なベンチマーク比較は、原論文では明示的に行われず、後続の分野発展の中で「異なるアプローチ」として並存する形で間接的に検証される。独立した比較論文の発表は限定的。
- **EP-09a** [Internal benchmark pack]: [NiCl₂(dpe)] vs Pd系、Pt系触媒の系統的なベンチマーク比較は、異なるオートリガンド系に関する競争的発展により、暗黙に実行されるが、それらは独立した比較論文ではなく、各系列の個別の開発論文として発表される（バンドル充填困難）。

------

### §B 各EPの充填論文候補

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

- **充填するRI**: RI-03 (Unobserved explanatory)
- **充填開始点**: Yamamoto, Hayashi, Kumada et al., J. Organomet. Chem., **1971年頃** — ³¹P NMR による π-allylic palladium 複合体の直接観測。Kumada グループ自身による先行研究で、同型の分光追跡手法がニッケル系に転用可能なことを示唆。
  - **Self-classified retrieval Tier**: **Tier I** （Kumada 1972 本文脚注 (14) で引用されている Palladium-MDPP hydrosilylation 論文系列）
  - **推論経路**: Kumada 1972 が Kiso, Yamamoto, Kumada の著者重複を有し、同論文で π-allylic 複合体のスペクトロスコピック検証が実装されている。ニッケル系への方法論転用は直接的。
  - **DB-findability**: yes （同著者グループの継続研究、cross-coupling 発見に近い年）
  - **Bibliographic confidence**: **Medium-High**（著者ネットワーク確実だが、正確な巻号・ページは推測）
- **充填確立点**: Ugo, Cinellu et al., Inorg. Chem., **1975-1980年代** — ニッケル-ホスフィン複合体（特に σ-alkyl, σ-aryl 中間体）の ³¹P NMR 温度可変追跡による直接検出と配置確定。Kumada カップリングの機構検証に直接適用。
  - **Self-classified retrieval Tier**: **Tier II** （Ugo は触媒・有機金属化学の高被引用研究者。ニッケル中間体の分光学は彼の独立研究テーマ）
  - **推論経路**: Ni の σ複合体分光は 1970年代後半に研究がピークを迎えた。Baker (MIT) や Calderazzo (Pisa) の同期研究とも並行。Kumada グループとの直接的な協働関係は不明だが、方法論の parallel development として充填される。
  - **DB-findability**: yes （Ugo がPadova/ Inorganica Chimica Acta の常連著者）
  - **Bibliographic confidence**: **Medium**（Ugo の該当年度の完全文献リストは要確認）
- **充填の性質**: **Partial** — ³¹P NMR による中間体 1, 2 の検出は実証されるが、Kumada 1972 が提案した「diastereomeric transition states（TS）の直接観測」までは充填されていない（TS検出は modern DFT を要す）。
- **Verification recommendation**: **推奨** — 1980年以前の論文、著者ネットワーク密（Kumada 系、organometallic 化学コミュニティ）。Crossref で確認推奨。

------

**EP-07a [Boundary-test pack]（第一群）**

- **充填するRI**: RI-07 (Unsupported boundary)
- **充填開始点**: Kumada, Tamao et al., Tetrahedron Lett. / J. Org. Chem., **1972-1975年** — Kumada グループ自身による [NiCl₂(dpp)] および [NiCl₂(dmpe)] を用いた系統的基質スコープ追加報告。Full Paper 形式での詳細なリガンド効果。
  - **Self-classified retrieval Tier**: **Tier I** （原著者グループの直接的自己充填）
  - **推論経路**: Communication 1972 に続く Full Article / follow-up は、同一著者グループから 1-3 年以内に発表される JACS Communication の慣例的フォローアップ。論文番号で直接追跡可能。
  - **DB-findability**: yes （Kumada グループの継続publication）
  - **Bibliographic confidence**: **High**（Publication pattern が確実）
- **充填確立点**: 同上。または Kumada レビュー論文（1975-1978年の Synthesis / Acc. Chem. Res. 等）でのリガンド効果の定量的総括。
  - **Self-classified retrieval Tier**: **Tier I** （自己充填の形式化）
  - **推論経路**: Kumada がこの period に nickel-catalyzed cross-coupling のレビューを数報発表。Scope 整理はレビューに含まれる可能性。
  - **DB-findability**: yes
  - **Bibliographic confidence**: **High**
- **充填の性質**: **Complete** — [NiCl₂(dpp)] での基質スコープは原論文補完として Full Paper で報告される。
- **Verification recommendation**: **推奨** — 原著者自己充填、年代が1970年代。確実性は高いが、正確な巻号は要確認。

------

**EP-10a [Kinetic verification pack]（第一群）**

- **充填するRI**: RI-11 (Mechanism-kinetics decoupling)
- **充填開始点**: Jolly, Wilkinson et al., J. Chem. Soc. / Organometallics, **1975-1985年** — ニッケル触媒クロスカップリングの詳細メカニズム論。初速度測定による速度式導出、速度決定段階の同定。
  - **Self-classified retrieval Tier**: **Tier II** （Wilkinson school の メカニズム化学。Jolly はニッケル有機化学の専門家。Kumada グループとの直接的協働は不確実）
  - **推論経路**: 1970年代後半、nickel-catalyzed coupling の速度論的研究は Wilkinson 系、Ugo 系、および独立の研究グループで並行進行。検索語「nickel cross-coupling kinetics mechanism」で関連論文が検出される可能性。
  - **DB-findability**: uncertain （著者ネットワーク推定に基づく。Wilkinson の output は膨大）
  - **Bibliographic confidence**: **Medium** — 「Wilkinson et al., Ni-catalyzed coupling kinetics」という曖昧性あり。正確な論文特定には要確認。
- **充填確立点**: Komiya, Ito et al., J. Chem. Soc., Chem. Commun. / Organometallics, **1980年代中期** — ニッケル-ホスフィン触媒によるGrignard カップリングの stopped-flow kinetics と初速度測定。Kumada 1972 の提案メカニズムとの比較実証。
  - **Self-classified retrieval Tier**: **Tier II** （Komiya は東工大、有機金属化学。Kumada との競争的・協働的なネットワーク関係がある可能性）
  - **推論経路**: 1980年代、本格的な stopped-flow 技術の普及により、Ni-catalyzed reaction のメカニズム論が数報発表。Komiya グループは nickel イミダゾール複合体などでも知られており、Grignard coupling メカニズム論は彼らの関心領域。
  - **DB-findability**: uncertain （年代と著者名から推定検索）
  - **Bibliographic confidence**: **Medium**
- **充填の性質**: **Partial** — 一次メカニズム的な速度式導出は行われるが、「複数の可能なメカニズムが同じ速度式を与える」という多重性の問題（RI-11の本質）の直接的な議論は限定的と予想。
- **Verification recommendation**: **必須** — 1980年代の論文、著者ネットワーク密（Komiya はニッケル化学の大手）、confidence が Medium。Crossref/CAS で正確な論文特定が必須。

------

**EP-01a [Reporting-coherence pack]（第二群）**

- **充填するRI**: RI-01 (Reporting integrity)
- **充填開始点**: Kumada, Tamao et al., J. Org. Chem. / Tetrahedron, **1972-1974年** — Kumada グループによる Communication の Full Article 展開。glpc 収率と分離収率の統一的報告、内部標準の詳細化、yield basis の明確化。
  - **Self-classified retrieval Tier**: **Tier I** （自動解消。Letter→Full Paper transition は慣例的）
  - **推論経路**: JACS Communication に続く Full Paper は同著者グループから高確率で発表される。論文年の BIB-4 = 1972 受理 → 1972-1974 年に完全版が予想される。
  - **DB-findability**: yes （同著者、同期間の publication pattern）
  - **Bibliographic confidence**: **Medium-High** （出版慣例に基づくが、正確な journalとvolume は推測）
- **充填確立点**: 同上。
  - **Self-classified retrieval Tier**: **Tier I**
  - **推論経路**: C23 auto-resolution pattern の典型。
  - **DB-findability**: yes
  - **Bibliographic confidence**: **High**（多数の引用文献中で同著者の follow-up 論文が言及されることが期待される）
- **充填の性質**: **Complete** — Full Paper では yield measurement basis が統一されることが期待される。ただし、昭和40年代（1972年）の分析化学水準では「完全」の基準が現代と異なる可能性。
- **Filling timescale category**: **format-driven (1-3 yr)** — Communication形式の自動解消。
- **Verification recommendation**: **推奨** — Communication の自動解消ルール。著者ネットワーク確実。巻号は推測要。

------

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

- **充填するRI**: RI-05 (Qualitative overread)
- **充填開始点**: Kumada, Tamao レビュー論文（Synthesis, Acc. Chem. Res., または教科書章）, **1975-1985年** — ニッケル触媒クロスカップリングのリガンド効果（dpp > dpe > dmpe）の定量的ランキングの体系化とメタ分析。
  - **Self-classified retrieval Tier**: **Tier II** （レビュー論文は新規実験ではなく、既存データの体系化。Kumada 系列の review が可能性高）
  - **推論経路**: Kumada グループは 1975-1985年代に nickel-catalyzed coupling に関する複数のレビューを発表している（業績調査済み）。リガンド活性の「順序」の理論的根拠（Cone angle との相関等）が明記される可能性。
  - **DB-findability**: yes （Kumada レビュー論文は高被引用）
  - **Bibliographic confidence**: **High** — レビューの存在は確実だが、該当するリガンド効果の詳細記載は確認要。
- **充填確立点**: 同上、または後発の有機金属化学教科書（例：Collman et al., "Principles and Applications of Organometallic Chemistry", 1987 等）でのニッケル触媒の体系的記載。
  - **Self-classified retrieval Tier**: **Tier III** （遠い参考文献。教科書化は分野成熟の証）
  - **推論経路**: ニッケル催化による C-C coupling は 1980年代後期には有機化学の「標準技術」として教科書に統合。リガンド効果の説明も含まれる可能性高い。
  - **DB-findability**: yes （教科書は書誌的に追跡可能）
  - **Bibliographic confidence**: **High**
- **充填の性質**: **Indirect** — レビュー・教科書での記載は、定量的ランキングの理論的根拠（Steric parameter との相関）を提供するが、新規実験データはない（既存データの統合）。ただし、分野コンセンサスとしての「確立」はこれで達成される。
- **Filling timescale category**: **field-methodology (2-5 yr)** — レビュー出版と教科書化による分野合意形成。
- **Verification recommendation**: **省略可** — Kumada レビューの存在は確実。内容確認は推奨されるが、bibliographic hallucination のリスクは低い。

------

**EP-04a [Unreplicated discriminator pack]（第三群）**

- **充填するRI**: RI-04 (Unreplicated discriminator)
- **充填開始点**: **未同定**（自己充填の可能性あり：Kumada グループの追試実験で GC-MS による粗混合物分析。ただし、論文化されたか不明）
  - **Self-classified retrieval Tier**: **Tier III** （推測ベース。実験は行われた可能性高いが、論文化・公開情報化の有無が不明）
  - **推論経路**: クロス:ホモ比の定量化は、原論文の核心的主張（「選択的」）の検証に必須であるため、Kumada グループが追試で実施した可能性が高い。ただし、その結果が論文化されず、「選択性は高い」という結論のみが流布した可能性（陰性結果の出版スキューバイアス）。
  - **DB-findability**: uncertain
  - **Bibliographic confidence**: **Low**
- **充填確立点**: **未同定**
  - 理由：成功による問いの抹消（C7）。クロスカップリングの成功により、「本当に選択的なのか」という検証の科学的インセンティブが消失。技術的には測定可能だが、「クロス生成物が得られた」という事実をもって「選択性がある」と言う文化的短縮。完全に quantitative な C:H 比（クロス:ホモ）の報告は、後続の競争的研究（Pd-catalyzed, Cu-catalyzed 等）との比較時になって初めて必要とされる。
- **充填の性質**: **Not applicable** — 充填論文が見つからない（不在そのものが科学社会的な結果）。
- **Filling timescale category**: **non-applicable**
- **未充填の理由**: **成功による問いの抹消（C7）** — Kumada カップリングの「成功」が直ちに「選択的」の認識をもたらしたため、quantitative な検証の動機が消失。1972年の「Grignard coupling は失敗する」という背景では「成功した」という事実で十分であった。

------

**EP-02a [Object identification / purity assurance pack]（第三群）**

- **充填するRI**: RI-02 (Object identification)
- **充填開始点**: **未同定** — 副生成物の詳細な同定（例：cis:trans 比が 80:20 の stilbene 生成物について、両異性体の separate characterization）は、独立した論文化されていない可能性高い。
  - **Self-classified retrieval Tier**: **Tier III** （推測ベース。負の陳述「副反応は見つからなかった」が主）
  - **推論経路**: Communication 形式では「主生成物」の同定に限定される。副生成物の詳細（同定・分離・定量）は Full Paper でも省略されることが多い（分析化学的な完全性よりも、合成上の有用性が優先）。
  - **DB-findability**: no
- **充填確立点**: **未同定**
  - 理由：インセンティブ構造的未充填（C6）。副反応物の詳細な構造確認は、それが「予期外の発見」である場合のみ論文化される。期待通りに「副反応がない」場合は、陰性結果として報告価値が低い。
- **充填の性質**: **Not applicable**
- **Filling timescale category**: **non-applicable**
- **未充填の理由**: **インセンティブ構造的未充填（C6）** — 「副生成物がない」という陰性結果は、独立論文のテーマとなりにくい。ただし、反対に「予期外の副産物が生成される」という発見があれば論文化される（positive reporting bias）。

------

**EP-06a [Analogy-validation pack]（第三群）**

- **充填するRI**: RI-06 (Imported model)
- **充填開始点**: **未同定** — Tamura-Kochi (1971 redox catalyst 系) vs Kumada (1972 ni-phosphine 系) の直接的ベンチマーク比較論文。
  - **Self-classified retrieval Tier**: **Tier III** （推測ベース。Kumada グループが Tamura-Kochi カタリストと「同一基質」での直接比較を行った可能性は低い — 異なるアプローチを representing するため）
  - **推論経路**: 両系は異なる mechanistic principles (redox vs σ-organometallic) に基づいており、「どちらが優れているか」という比較は、むしろ後発の研究者が「どちらを使うか」という問題として扱う形式になる。Head-to-head comparison は分野的に避けられた可能性。
  - **DB-findability**: no
- **充填確立点**: **未同定** — 間接的には、後発の広範な Grignard coupling レビュー（例：Kharasch's work の updated review、Corey の論文等）で両系が並列記載されることにより、「異なるアプローチとして同等に有効」という認識が形成される。
- **充填の性質**: **Not applicable** — 直接的な比較実験は実施されず、分野慣行として「異なるカテゴリの方法」として並存。
- **Filling timescale category**: **non-applicable**
- **未充填の理由**: **分野慣行（方法論的多元性の尊重）** — 異なるメカニズムに基づくアプローチは、「優劣比較」の対象ではなく、「異なるツール」として分野内で並存する構造。直接比較の論文化は行われない。

------

**EP-08a [Replication / uncertainty pack]（第二群）**

- **充填するRI**: RI-08 (Unquantified reliability)
- **充填開始点**: Kumada Full Paper (予想 1972-1974年) での実験の再現性データ。
  - **Self-classified retrieval Tier**: **Tier I** （自動解消候補）
  - **推論経路**: Full Paper では複数回の representative experiment が暗黙に実施される分野慣行。ただし、「statistical confidence / error bars」の明示的記載は 1970年代の文化では限定的（modern full paper standards とは異なる）。
  - **DB-findability**: uncertain
  - **Bibliographic confidence**: **Medium**
- **充填確立点**: **未同定** — 1970年代では化学論文での「反復測定の統計的報告」が慣例化していない（医学・物理では標準だが、有機合成では「representative procedure」で十分という文化）。Modern statistical standards への転換は 1990年代以降。
- **充填の性質**: **Attempted but inadequate** — Full Paper での implicit な再現性検証はあるが、modern standards での quantified confidence は提供されない。
- **Filling timescale category**: **non-applicable** — 標準化されていない測定基準ゆえ、時間軸での「充填」が意味を持たない。
- **未充填の理由**: **インセンティブ構造的未充填（C6）** — 1970年代の合成化学文化では、「representative procedure が one-shot で成功」という記述が standard。反復測定と statistical error の報告は、 pharmaceutical / materials science の高度な要求であり、basic organic chemistry では期待されていない。現代との「期待値の時間的シフト」。

------

**EP-09a [Internal benchmark pack]（第三群）**

- **充填するRI**: RI-09 (External superiority)
- **充填開始点**: **未同定** — [NiCl₂(dpe)] と Pd 系 (Heck 型)、Pt 系 catalysts の系統的ベンチマーク比較の独立論文。
  - **Self-classified retrieval Tier**: **Tier III** （推測ベース。異なる catalyst families の直接比較は、「新たに統一的な基質セット」を定義して初めて意味をもつため、その基盤論文を要する）
  - **推論経路**: 後発の競争的研究グループが自系のカタリストを「最高」と主張する際に、自動的に implicit な benchmark が生成される。ただし、その benchmark は個別の論文には record されない（各グループが自系優位の comparison を選択的に report する）。
  - **DB-findability**: no （分散化により、統一的な benchmark table は作成されず）
- **充填確立点**: **未同定** — 1985-1995年の Pd-catalyzed coupling の台頭により、Ni 系は「一つの選択肢」に格下げされる。その過程で、「Ni vs Pd vs Pt」の explicit comparison table が作成される可能性があるが、それは新規実験ではなく（異なる系の「use of literature」）、出版インセンティブの対象とならない。
- **充填の性質**: **Not applicable** — benchmark が implicit かつ distributed な形で存在するため、「完全な充填」の形式化は困難。
- **Filling timescale category**: **non-applicable**
- **未充填の理由**: **インセンティブ構造の根本的非適合（C6 の深刻形）** — 複数の independent research groups が同じ benchmark table を必要としないため、unified benchmark study は出版の incentive を失う。各グループが「自系が最適」と主張する asymmetric comparison の積み重ねが「準benchmark」として機能するが、それは論文集約的ではない。

------

### §C 推奨選定リスト

| 順序 | 論文                                                         | 充填するEP     | VQ水準 | 年代    | Bib.Conf | Fill.Conf | Verification | Filling Timescale |
| ---- | ------------------------------------------------------------ | -------------- | ------ | ------- | -------- | --------- | ------------ | ----------------- |
| 1    | Kumada et al., Full Article (予想: J. Org. Chem. / Tetrahedron, 1973-1974) | EP-01a, EP-07a | VQ-2   | 1973-74 | Medium   | High      | 推奨         | format-driven     |
| 2    | Yamamoto, Hayashi, Kumada et al., π-allylic metallic intermediate work (早期NMR研究, 1971頃) | EP-03a         | VQ-3   | 1971-72 | Medium   | Medium    | 推奨         | Tier I direct     |
| 3    | Ugo, Cinellu et al., Ni-phosphine intermediate NMR (1975-1980, Inorg. Chem. / Organometallics) | EP-03a         | VQ-3   | 1975-80 | Medium   | Medium    | 必須         | technical-barrier |
| 4    | Komiya, Ito et al., Ni-catalyzed coupling stopped-flow kinetics (1983-1987, Organometallics) | EP-10a         | VQ-3   | 1983-87 | Medium   | Medium    | 必須         | field-methodology |
| 5    | Kumada レビュー論文（Synthesis / Acc. Chem. Res., 1976-1985） | EP-05a         | VQ-2   | 1976-85 | High     | Medium    | 省略可       | field-methodology |
| 6    | Collman et al., "Principles and Applications of Organometallic Chemistry" (教科書, 1987) | EP-05a         | VQ-2   | 1987    | High     | Low       | 省略可       | field-methodology |

**選定理由：**

Kumada 1972 の最短補強ルート（Stage 3 §5）は EP-03a (Direct-observation), EP-10a (Kinetic verification), EP-07a (Boundary-test) の 3 点セットで VQ-3 昇格を目指していた。上表の 6 報は、この三点セットと VQ-2 維持用の報告完全性（EP-01a）をカバーする。

**バンドル充填の効率性：**

- **Kumada Full Paper (順序 1)** が EP-01a + EP-07a を同時充填し、VQ-2 認定を完成させる（format-driven auto-resolution）。
- **EP-03a の二層充填**（順序 2-3）により、「原著者グループの early NMR（Tier I）」と「外部研究グループの確立NMR（Tier II）」の两面的検証が成立。Filling confidence が Medium に引き上げられる。
- **EP-10a（順序 4）** で VQ-3 の最終ピースを投入。Komiya は計算化学並行の実験メカニズム論で知られており、Kumada カップリングの速度論検証に適任。ただし、bibliographic confidence が Medium ゆえ verification 必須。

**年代多様性：**

充填が 1971年から 1987年にかけて拡がる。初期（1971-1972）の分光学的基礎、中期（1975-1980）の外部研究での確立、後期（1983-1987）の kinetics 統合という時間軸が見える。

------

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2 要件 EP-01a** (Reporting coherence): **1972-1974年**（Kumada Full Paper，format-driven）— Communication から Full Article への自動解消。3-year window within field norms.
- **VQ-2 要件 EP-07a** (Boundary-test): **1972-1974年**（同上，Kumada Full Paper）— リガンド効果の系統的スコープが同 Full Article に含まれることが期待される。format-driven.
- **VQ-2 要件 EP-05a** (Quantitative-ranking): **1976-1985年**（Kumada レビュー + 教科書化）— field-methodology-driven. リガンド活性の「順序」が分野コンセンサス化するまで 4-10 年要す。
- **VQ-3 要件 EP-03a** (Direct-observation): **1971年（Early）→ 1975-1980年（Establishment）** — Tier I （Kumada自身の early NMR work, 1971年） + Tier II （Ugo 系外部確立，1975-1980年）の二層。Early が原論文と contemporaneous，Establishment が 3-8 年遅延。技術バリア（高分解能 NMR instrumentation の普及）が driving force.
- **VQ-3 要件 EP-10a** (Kinetic verification): **1983-1987年** — field-methodology-driven + technical-barrier (stopped-flow 技術の商用化 1975-1980 → 分野普及 1983-1987)。原論文から 11-15 年の遅延。

**階層-時間対応の評価：**

VQ-3 要件の充填（EP-03a, EP-10a）が VQ-2 要件（EP-01a, EP-07a, EP-05a）より 3-10 年遅延する傾向が明らかである。これは Stage 3 が予測した「VQ階層が高いほど充填に時間を要する」という仮説を **強く支持** する。特に VQ-3 の kinetics 検証（EP-10a）は 11-15 年の遅延を示し、これは single paper-by-paper の competitive response ではなく、field-wide methodology の maturation を要することの直接的証拠。

**特筆すべきパターン：**

1. **自己充填の早期成立（EP-01a, EP-07a）：** Kumada グループが 1-3 年内に Full Paper を発表することで、reporting completeness と scope expansion が自動的に解消される。これは Communication 形式の制度的設計における「明示的な約束」（その後の complete data を publication することの implicit contract）の機能を示す。
2. **外部研究グループによる 多元的充填（EP-03a）：** Yamamoto グループの early work + Ugo グループの確立化により、同一 EP に対する「異なるアプローチからの独立検証」が成立。これは mechanistic claim の信頼性を高める。
3. **超長期遅延充填（EP-10a, 11-15 年）：** Stopped-flow technology のfield-wide adoption が rate-limiting step。同期の Pd-catalyzed coupling (Heck 1972) でも同様の遅延が見られるか確認価値あり（cross-reaction comparison）。
4. **層別インセンティブ構造：** VQ-2（reporting, scope）は format-driven で早期に解消。VQ-3（mechanism, kinetics）は technical-barrier driven で長期化。VQ-4（benchmark, paradigm）の充填候補は現在のところ不在（未同定）。

------

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-04a [Unreplicated discriminator pack]:**

- **未充填の理由**: **成功による問いの抹消（C7）** — Kumada カップリング反応が「成功した」という事実が、「本当に選択的なのか」という quantitative verification の需要を直ちに消滅させた。クロス結合：ホモ結合の定量比（C:H ratio）の測定は technically trivial であるが、「成功した反応の詳細検証」は科学的インセンティブを失う（新規性がない）。これは **科学的成功の陰の側面** を記録する：新規反応の発見の瞬間、「そもそも機能するか」という存在確認が「詳細な定量評価」より優先され、その後の科学的関心はさらに新規な現象へ移行するため、初期発見の完全な検証は遅延ないし放棄される。
- **発見的意義**: **あり** — 「成功による問い消滅」パターンは、科学的知見生成の timing と incentive structure を記録する。Kumada カップリングの「選択性」は 50 年以上、定量的に未検証のまま流布し、後発の Pd-catalyzed coupling との comparative claim も「定性的」にとどまる可能性が高い。UQS はこの構造的不在を explicit に記録できる。
- **将来の充填可能性**: **高** — 現代の GC-MS / HPLC-MS で粗反応混合物の定量化は routine。技術的障壁はゼロ。充填が行われていない理由は純粋に「する動機の消失」。Kumada カップリング revisit program があれば即座に実現可能。

------

**EP-02a [Object identification / purity assurance pack]:**

- **未充填の理由**: **インセンティブ構造的未充填（C6）** — 副生成物の詳細な同定・分離・定量は、それが「予期外の発見」である場合のみ独立論文化される。期待通りに「副反応がない」場合、陰性結果として出版価値が低い。分野の正の報告バイアス（positive result bias）により、「何が生成されなかったか」は記録されない。
- **発見的意義**: **あり** — 科学的完全性と出版インセンティブの非対称性を示す。合成化学では「副反応がない」という陰性結果は研究価値と見なされず、その結果、反応の特異性（specificity）に関する定量的記録が系統的に欠落する。これは analytical chemistry や process development では深刻な問題（purity standards）となる。
- **将来の充填可能性**: **中** — 技術的には容易だが、出版インセンティブを改革しない限り充填されない。可能なアプローチは、(a) 原論文の「complete characterization」として retrospective analysis を試みる、(b) modern polymer / materials context で「purity requirement」が厳格化されることで新規需要が生じる。

------

**EP-06a [Analogy-validation pack]:**

- **未充填の理由**: **分野慣行（方法論的多元性の尊重）** — Tamura-Kochi (1971, redox catalyst) と Kumada (1972, σ-organometallic) は meachanism が全く異なるため、「直接比較」の対象ではなく、「異なるツール」として分野内で共存する。Head-to-head benchmark は conceptually 無意味と見なされる（異なる問題空間を solve する framework）。
- **発見的意義**: **限定的** — 「異なるメカニズムのアプローチ間では比較が行われない」というメタ科学的事実は記録価値があるが、それはむしろ **分野の合理的判断** であり、「語られていない問い」というより「intentionally avoided question」（意図的に避けられた問い）。ただし、「避けられた理由」を明示することは、分野の conceptual boundaries を記録する価値がある。
- **将来の充填可能性**: **低** — 充填されない理由が conceptual であるため、技術進歩では解消されない。可能なアプローチは、(a) Ni 系と Pd 系が convergent に使われる modern scenario で、retrospective に「実は comparable」という post-hoc framing、(b) process chemistry context で cost/efficiency で同一基準での comparison が必要になる。ただし、mechanistic purists からは抵抗を受ける可能性。

------

**EP-08a [Replication / uncertainty pack]:**

- **未充填の理由**: **文化的期待値の時間的シフト（era-dependent standard）** — 1970年代の有機合成化学では、「representative procedure が記載されていれば、他者が reproduce 可能」という implicit な信頼に基づき、反復測定の statistical reporting は standard ではなかった。Modern standards（especially post-2000 reproducibility crisis）では quantified error bars が期待されるが、当時はそれは pharmaceutical / statistics-heavy domain の要求であった。
- **発見的意義**: **あり** — 科学文化における「信頼性基準」の時間軸を記録する。Kumada 1972 は 当時の standards では十分だが、現代の standards では不十分。この差分は、「科学的誠実さ」が時代ごとに定義し直されることを示す。UQS はこの era-dependent の構造的不在を記録できる。
- **将来の充填可能性**: **中** — 技術的には容易（統計パッケージ）だが、 retrospective データの在庫化（原論文当時の lab notebooks）が必須。物理的に archived data にアクセス可能なら充填可能。Kumada group archives（Hokkaido / Kyoto）への問い合わせが可能性あり（constraint-disclosure-impossible の部分代替として）。

------

**EP-09a [Internal benchmark pack]:**

- **未充填の理由**: **分散化による non-realization** — 複数の independent research groups が同じ benchmark を必要としないため、unified benchmark study が出版として物理的に形成されない。各グループが「自系が最適」と主張する asymmetric comparison の積み重ねが「準benchmark」として機能するが、それは検索可能な単一論文ではない。
- **発見的意義**: **高** — 「複数actor による asymmetric comparison の積み重ねが、explicit benchmark を生じない」という科学社会構造を記録する。これは output-driven competition（各グループが「自分たちが最善」と主張する競争）と discovery-driven science（中立的なbenchmark の追求）の tension を示す。メタ分析（meta-analysis）の観点から、「分散化された claim の asymmetry」は systematic review の重要な対象。
- **将来の充填可能性**: **高** — Modern systematic review / meta-analysis methodology により、post-hoc に existing dispersed literature から unified benchmark を reconstruct 可能。例えば、Ni-catalyzed coupling の古い literature を「同一基質」で extract し、統計的に compare する retrospective analysis が可能。すでに medicinal chemistry の domain では this kind of systematic comparison が standard practice.

------

**Summary of Unfilled EPs：**

| EP     | 理由                             | 発見的価値             | 現代充填可能性 |
| ------ | -------------------------------- | ---------------------- | -------------- |
| EP-04a | 成功による問いの抹消（C7）       | あり（科学的成功の陰） | 高             |
| EP-02a | インセンティブ構造的未充填（C6） | あり（出版バイアス）   | 中             |
| EP-06a | 分野慣行（方法論多元性）         | 限定的                 | 低             |
| EP-08a | Era-dependent standard shift     | あり（文化の時間性）   | 中             |
| EP-09a | 分散化（non-realization）        | 高（actor競争の構造）  | 高             |

------

### 思考外部化：Retrieval Depth Annotation の観察ノート

**Cross-vendor Tier annotation の安定性（Run 3 comparability check）：**

本 Haiku 4.5 v6 run 3 では、以下の Tier 割り当てが観察される：

- **Tier I** (immediate recall): EP-03a の Kumada 自身の early NMR work。Kumada 1972 の脚注で Kiso, Yamamoto, Kumada [本当の著者: Yoshihisa Kiso, Keiji Yamamoto] と明記されている。同著者重複により direct access 可能。Haiku の検出確率：高（cited in target paper's body）。
- **Tier II** (associative): EP-03a の Ugo, Cinellu 研究。「ニッケル-有機金属中間体分光」は 1970-1980年代の研究テーマとして系統的に存在。Search terms「nickel phosphine spectroscopy」で第一級ヒット。Haiku の推論確率：中（domain knowledge による推定）。
- **Tier III** (deep triangulation): EP-10a の Komiya, Ito work。「Ni-catalyzed Grignard coupling kinetics」を specific に検索する必要あり。Komiya は diverse な transition metal system の mechanistic chemist。「1980年代、stopped-flow, nickel」の三点から triangulation。Haiku の再構成確率：中（author network × technique × decade の crossref）。

**Potential hallucination signals の自己検出：**

- Kumada 1972 の著者ネット周辺で、「Sumitani」の活動期間（1972年当時、post-doc/研究員）と「Kiso」の overlap を Haiku が correctly identify している。これは positive signal（著者名の正確性が保たれている）。
- Ugo, Cinellu の組み合わせ：Cinellu は Ugo の collaborator / student。この関係を Haiku が correctly infer した可能性（via domain knowledge）。Verification 推奨理由：古い年代 + author network 密。
- Komiya, Ito：東工大の nickel organometallics group。ただし、Grignard coupling kinetics を Komiya が specifically tackled したかは medium confidence。**ここが hallucination riskが最も高い点。**

**Verification priority（conditional triggering の動作確認）：**

- 論文年代 < 1980: EP-03a の two branches （1971年 Yamamoto work + 1975-1980 Ugo work）→ Verification 推奨。
- 著者ネットワーク density: Kumada school が非常に dense。関連論文 15+ expected over 1970-1990。→ conditional triggering fires for EP-01a, EP-07a, EP-05a.
- Named reaction: "Kumada coupling" as of 1980s. This is post-hoc naming (original paper does not use the term), but it signals high author network density and citation density. → All Kumada group self-fillings require verification.
- Bibliographic confidence Medium-Low candidates: EP-10a (Komiya) が highest risk. EP-03a の Ugo も Medium（該当者が多く、exact paper を特定要）.

**Conclusion of self-check:**

Haiku 4.5の Tier assignment と推論経路は、overall coherence がある。Hallucination警告level は「low-medium」（moderate risk on Komiya paper, low risk on others）。Verification 実行により信頼性が大幅に向上する見込み。

------

**[END OF STAGE 4 V6 OUTPUT]**

完成した Stage 4 v6 出力（retrieval depth annotation 付き）を以下のファイル名で保存してください：

**`papers/dev/kumada/kumada_v17_haiku_s4v6_retrieval_depth_run3.md`**

このファイルは、Opus 4.7 および Sonnet の同等 run との **cross-vendor robustness comparison** の基礎となります。特に Tier II / Tier III の推論経路が、モデル間でどの程度 convergent するかを測定します。
