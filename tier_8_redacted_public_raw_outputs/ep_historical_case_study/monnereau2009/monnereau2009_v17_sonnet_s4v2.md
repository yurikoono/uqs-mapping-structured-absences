prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Monnereau et al. 2009（Advanced Synthesis & Catalysis, Full Paper）

### §A EP充填難易度の三群分類

Stage 3 §5に列挙されたEP一覧（VQ-2パス: EP-01a, EP-08a, EP-07a；VQ-3パス: EP-02a, EP-03a, EP-04a, EP-06a, EP-09a）を三群に分類する。

---

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a

- **EP-03a** Direct-observation / state-assignment pack — Ni(I)/Ni(III)経路の可能性は2009年以降に爆発的に研究されており、EPRおよびXASによるNi酸化状態の直接決定は多数の独立論文の主題として存在する。独立論文として発表された可能性が高い。
- **EP-06a** Analogy-validation pack — 剛直化カリクサレン類縁体の合成比較は著者自身が「非常に有益」と明言した実験であり、後続グループによる独立研究の主題として存在する。加えて、Ni(II)ジアリール錯体からの化学量論的REとバイトアングルの関係はOsakada・Hartwig等の独立研究として報告されており、文献検索で追跡可能。

---

**第二群（間接的に追跡可能）：** EP-02a, EP-04a, EP-09a

- **EP-02a** Identity / purity substantiation pack — Ni活性化種の同定はある特定系の続報として報告される可能性があるが、カリクサレン-Ni特定系での完全充填が独立論文として存在するかは不確か。類似系（NiCp(diphosphine)型錯体の活性化）では関連報告があるが対象系そのものではない。
- **EP-04a** Discrimination / replication pack — 水銀滴下試験およびTEMPO阻害は多くのNi触媒論文に含まれるが、Monnereau条件（100°C、dioxane、calixdiphosphine）での直接実施は間接的な充填に限られる可能性が高い。
- **EP-09a** Internal benchmark pack — dppb、dppf、DPEphosを含む系統的ジホスフィン比較はレビュー論文に含まれているが（van Leeuwen 2000が代表例）、Monnereau論文の反応条件での独立した比較実験論文の存在は限定的。

---

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-07a, EP-08a

- **EP-01a** Reporting-coherence pack — GCレスポンスファクター検証は触媒論文の内部手続き問題であり、それ自体が独立論文の主題になることはない。分野全体がこの種のデータを論文化しないという慣行的インセンティブ構造の下で永続的に未充填となるタイプ。
- **EP-07a** Boundary-test pack — 特定基質（ブロモメシチレン）のスコープ失敗説明は、より広い基質スクリーニング論文の中で言及される可能性はあるが、この単一の外れ値を埋めることを目的とした独立論文の主題にはなりにくい。
- **EP-08a** Replication / uncertainty pack — 反復測定と不確かさ評価は触媒スコープ論文の報告慣行の問題であり、独立論文の主題にならない。Full Paper再版や続報があれば部分解消されうるが、Monnereau系の続報論文が存在するかは不明。

---

### §B 各EPの充填論文候補の同定

---

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: N/A — 第三群として独立論文充填が想定されない
* **Confidence**: N/A
* **注記**: GCレスポンスファクター検証は触媒化学分野全体で独立論文として発表されない。IncentiveなしのFull Paperへの展開が自動解消するか（通信→Full Paper遷移）に見えるが、Monnereau 2009はすでにFull Paperであり、遷移による自動解消も期待できない。§Eで詳述。

---

**EP-02a Identity / purity substantiation pack（第二群）**

* **充填するRI**: RI-02 Object identification
* **充填開始点**: Lejeune M, Sémeril D, Jeunesse C, Matt D, Peruch F, Lutz PJ, Ricard L. Chem. Eur. J. 2004, 10, 5354–5360（Ref [15] in Monnereau） — n-プロピル置換カリクサレン-Ni錯体（2の類縁体）のNMR動性と触媒特性を記述。類縁NiCp(diphosphine)錯体の溶液状態キャラクタリゼーションを含む可能性があるが、100°C活性化種の明示的同定は不明。
* **充填確立点**: 未同定 — calixarene系での活性化種の分光学的完全同定（Ni酸化状態を含む）に特化した独立論文は確認できない。
* **充填の性質**: Partial（Lejeune 2004が関連動性の間接前提を提供）/ 未確立
* **Confidence**: Medium（Lejeune 2004の内容）/ Low（完全充填論文の存在）
* **注記**: Matt/Sémeril groupは2009年以降もカリクサレン-Ni触媒研究を継続している可能性があるが、特定の後続論文における41.8 ppm種の完全同定については文献確認が必要。

---

**EP-03a Direct-observation / state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点（Partial、pre-2009）**: Tsou TT, Kochi JK. J. Am. Chem. Soc. 1979, 101, 6319–6332 — Ni(0)/phosphine錯体のKumada型カップリングにおけるNi(0)/Ni(II)サイクルをUV-Vis分光および化学量論的実験で検証した基礎的機構研究。単純ホスフィンNi系でのNi酸化状態帰属の先行充填として機能する（Monnereau 2009より30年前）。
* **充填確立点（Paradigm-shift）**: Diao T, Weix DJ. J. Am. Chem. Soc. 2012, 134, 2969（推定）; Schley ND, Fu GC. J. Am. Chem. Soc. 2014, 136, 16588（推定） — EPR分光によるNi(I)中間体の直接検出と、Ni(I)/Ni(III)という代替触媒径路の確立。EP-03aが要求する「Ni酸化状態の直接決定」を実験的に解決するが、「解決」の内容がMonnereau 2009の前提（Ni(0)/Ni(II)サイクル）の枠組みを変更するパラダイム転換として機能する。
* **充填の性質**: Paradigm-shift — EP-03aが問う「Ni酸化状態はNi(0)か」という問いは、2012年以降「Ni(0)/Ni(II)でもNi(I)/Ni(III)でもあり得る、条件依存」という形で枠組みが変化した。EPの前提（Ni(0)/Ni(II)サイクルの確認）ではなく、その前提自体の再検討として充填が機能する。
* **Confidence**: High（Tsou & Kochi 1979）；Medium（Diao/Weix 2012、Schley/Fu 2014の具体的内容との対応）
* **注記**: Ni(I)/Ni(III)径路の確立は2009年のMonnereau論文の範囲外だが、U-2とU-4で問われた「Ni酸化状態の未同定」と「ラジカル/不均一系経路の可能性」は、このparadigm-shift充填によって原問いの枠組みが変化した。これは充填というよりも問いのsuccessionとして解釈できる。

---

**EP-04a Discrimination / replication pack（第二群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: 未同定（特定系） — 水銀滴下試験をNi/diphosphine KTC coupling（dioxane、100°C条件）に適用した独立論文は特定できなかった。Ni触媒化学全般では水銀試験の報告が2010年代に増加しているが、calixarene系または類似Ni/chelating diphosphine KTC系への直接適用を報告した論文は確認できない。
* **充填確立点**: 未同定
* **充填の性質**: Attempted（複数のNi/phosphine coupling論文に水銀試験が含まれているが、Monnereau条件とのmatched-pairの問題は未解消）
* **Confidence**: Low
* **注記**: EP-04aのcase-specific実装（100°C dioxane条件でのmatched-pair水銀試験）は技術的に実行可能であるが、インセンティブ構造の問題（既存触媒系の対照実験は単独論文化されにくい）から充填されていない可能性がある。§Eで詳述。

---

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点（Indirect/Pd系）**: Marcone JE, Moloy KG. J. Am. Chem. Soc. 1998, 120, 8527–8528（Ref [27] in Monnereau） — ビスホスフィンPd(II)(Ar)₂錯体からのREとバイトアングルの関係を化学量論的に実証。Monnereau 2009が輸入したモデルそのものであり、Pd系については充填済みだが、Ni系については未充填。
* **充填開始点（Partial/Ni系）**: Osakada K, Yamamoto T group（J. Organomet. Chem. または Organometallics、1990年代複数論文） — Ni(II)ジアリール錯体の化学量論的合成とビフェニル生成（RE）を記述した先行研究群。バイトアングル系統変化については限定的だが、Ni(II)(Ar)₂からのREの実験的基盤を提供する。
* **充填確立点**: 未同定 — 複数のバイトアングル既知ジホスフィンを用いたNi(II)(Ar)₂錯体のRE速度論の系統的研究（Marcone-Moloy実験のNi版）を独立論文として報告したものは特定できなかった。カリクサレン剛直類縁体については情報なし。
* **充填の性質**: Partial（Osakada group; Ni(II)ジアリールREの実験的フレームワーク）/ Indirect（Marcone & Moloy 1998、Hartwig et al. 1998; Pd/Rh系での実証）
* **Confidence**: High（Marcone & Moloy 1998）；Medium（Osakada group Ni RE papers; 具体的タイトル・年の文献確認要）
* **注記**: EP-06aの充填開始点は実はMonnereau 2009よりも前（1998年のMarcone/Moloy、Hartwig論文）だが、これらはPdおよびRh系に限定されており、論文自身がNi系への外挿の正当性を示さずに引用している。これがRI-06（Imported model）として分類された理由である。「Ni系でのMarcone-Moloy実験」はMonnereau 2009以降も独立した研究課題として残っている。

---

**EP-07a Boundary-test pack（第三群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: N/A
* **Confidence**: N/A
* **注記**: bromomesityleneのような2,4,6-三置換ArBrの反応性限界は基質スクリーニングの付帯事項として多くの触媒論文に登場するが、calixarene-Ni/2,4,6-triarylbromide系での立体効果の系統的研究として独立論文化されたものは見当たらない。

---

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: N/A
* **Confidence**: N/A
* **注記**: 既存データの反復測定と不確かさ評価を目的とした独立論文は分野慣行として存在しない。Monnereau系の続報論文があれば部分解消される可能性があるが、確認できない。

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点（Indirect）**: van Leeuwen PWNM, Kamer PCJ, Reek JNH, Dierkes P. Chem. Rev. 2000, 100, 2741–2769（Ref [12] in Monnereau） — バイトアングル効果の包括的レビュー。dppp、dppb、dppf、DPEphosを含む多様なジホスフィンのKumada coupling活性比較データを含む。ただしレビューであり新規実験データは提供しない。
* **充填確立点**: 未同定 — Monnereau論文の反応条件（100°C、dioxane、PhMgBr/ArBr=2:1、前活性化、1時間）で[NiCl₂(dppb)]、[NiCl₂(dppf)]、[NiCl₂(DPEphos)]をcomplex 2と直接比較した独立論文は特定できなかった。
* **充填の性質**: Indirect（van Leeuwen 2000 review; 条件非一致の既存比較データのみ提供）
* **Confidence**: High（van Leeuwen 2000の存在）；Low（完全充填論文の存在）
* **注記**: EP-09aの充填に必要な実験（同一条件での複数ジホスフィン比較n=3）は技術的に容易であるが、「既存触媒との詳細比較」のみを目的とした論文は新規性要件を満たさないため出版インセンティブが低い。インセンティブ構造の不整合による未充填の典型例。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tsou TT, Kochi JK. J. Am. Chem. Soc. 1979, 101, 6319–6332 | EP-03a（Partial） | VQ-3（機構） | 1979 | High |
| 2 | Marcone JE, Moloy KG. J. Am. Chem. Soc. 1998, 120, 8527–8528 | EP-06a（Indirect; Pd系） | VQ-3（機構） | 1998 | High |
| 3 | Lejeune M et al. Chem. Eur. J. 2004, 10, 5354–5360 | EP-02a（Partial） | VQ-2（方法） | 2004 | Medium |
| 4 | van Leeuwen PWNM et al. Chem. Rev. 2000, 100, 2741–2769 | EP-09a（Indirect） | VQ-4（ベンチマーク） | 2000 | High |
| 5 | Diao T, Weix DJ. J. Am. Chem. Soc. 2012, 134, 2969（推定） | EP-03a（Paradigm-shift） | VQ-3（機構） | 2012 | Medium |
| 6 | Schley ND, Fu GC. J. Am. Chem. Soc. 2014, 136, 16588（推定） | EP-03a（Paradigm-shift; EPR-based Ni(I)検出） | VQ-3（機構） | 2014 | Medium |

---

**選定理由:**

選定リストは「EP充填のカバレッジ」と「充填の決定性」を優先した。

EP-03a（Direct-observation/state-assignment）は最も追跡可能な充填パターンを示しており、1979年のTsou & Kochi（Ni(0)/Ni(II)の化学量論的確立）から2012〜2014年のNi(I)/Ni(III)パラダイム転換文献（Diao/Weix、Schley/Fu）まで段階的充填の時間軸が存在する。EP-03aは単独でSRG-1（RI-03）、SRG-3（RI-03）、SRG-5（RI-03）の3SRGに関与するため、複数EPへの充填効率が最高。

EP-06a（Analogy-validation）は第一群として理論的に追跡可能だが、Ni特異的な充填（calixarene剛直化類縁体またはNi版Marcone-Moloy実験）が未同定のため、Pd系の充填（Marcone & Moloy 1998）を暫定的に選定した。

Van Leeuwen 2000はEP-09aへの唯一の間接充填候補として含めた（VQ-4要件の間接的前進）。

**注意**: Monnereau 2009より前の論文（Tsou 1979、Marcone 1998、Lejeune 2004、van Leeuwen 2000）が選定リストの大部分を占める。これは本論文が自身の主張に必要な実験的基盤を、当時すでに利用可能だった先行研究に求めながら同型性の実証を省略した構造を反映している。後発充填（2012年以降）はParadigm-shiftとして機能しており、EP充填というよりも問いの枠組み変更として解釈される。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a → 未充填 — 分野慣行として充填なし
- VQ-2 要件: EP-07a → 未充填 — 関心の欠如
- VQ-2 要件: EP-08a → 未充填 — 分野慣行として充填なし
- VQ-3 要件: EP-02a → Partial充填 2004年（Lejeune et al.）— 自己充填パターン（同グループ先行研究）；完全充填は未確立
- VQ-3 要件: EP-03a → Partial充填 1979年（Tsou & Kochi）→ Paradigm-shift充填 2012〜2014年（Diao/Weix、Schley/Fu）— 技術駆動充填（EPR分光の普及）
- VQ-3 要件: EP-04a → 未充填（特定系では）— インセンティブ構造不整合
- VQ-3 要件: EP-06a → Indirect充填 1998年（Marcone & Moloy、Pd系）— 分野横断充填（Pd→Niの外挿が残存）；Ni系は未確立
- VQ-4 要件: EP-09a → Indirect充填 2000年（van Leeuwen review）— レビュー経由の間接充填

---

**階層-時間対応の評価：**

「VQ階層が上がるほど充填に要する時間が長くなる」という仮説は本ケースでは**逆転パターン**を示す。最も早く充填された項目はEP-03a（Tsou & Kochi 1979、Monnereau 2009より30年前）であり、VQ-3要件に対応する。一方、VQ-2要件のEP-01a、EP-07a、EP-08aは2026年現在も未充填のまま残存している。この逆転は「VQ階層が科学的難易度を反映する」という仮説よりも「VQ階層が出版インセンティブ構造と逆相関する」という解釈を支持する。低VQ要件（RI-01、RI-07、RI-08）のEPは技術的に容易でも論文化インセンティブがなく、高VQ要件（RI-03、RI-06）のEPは独立研究の主題として成立するために先に充填される。

**特筆すべきパターン：**

- **Paradigm-shift充填（EP-03a）**: Ni(I)/Ni(III)径路の確立（2012〜2016年）は、EP-03aが問う「Ni(0)か否か」という問いを「場合による」という形で再定義した。これはEP充填ではなく問いの枠組みのsuccesseionとして解釈すべき事例。
- **自己充填の不在**: 原論文著者（Matt/Sémeril group）による後続論文でEPが自己充填されたかどうかは確認できなかった。EP-02a（活性化種の同定）は自己充填の最有力候補だが、文献確認を要する。
- **VQ階層逆転（§3 §6との整合）**: Stage 3 §6で「VQ階層逆転の予兆」として記録したパターンが、§Dの分析で実際に確認された。EP-01a/EP-08a（VQ-2, RI-01/RI-08）が長期未充填であり、EP-03a（VQ-3, RI-03）が科学的関心の高さから先に充填されている。
- **技術駆動充填（EP-03a）**: EPRおよびXAS分光の触媒化学への普及（2010年代）が、EP-03aの充填を技術的に可能にした。

---

### §E 未充填EPの発見的意義

**EP-01a Reporting-coherence pack:**
* **未充填の理由**: インセンティブ構造の不整合 — GCレスポンスファクター検証は技術的に容易（数時間の実験）だが、「既存論文のGC校正を後から検証した」という内容は新規性を要求する出版慣行のもとで論文化されない。触媒スコープ論文では全般的にこの種のデータが省略されており、分野慣行として非充填。
* **発見的意義**: あり — 「触媒化学コミュニティが15年以上にわたって系統的に避けてきた定量的バリデーション」として記録できる。TOF競争（記録更新の動機）が測定精度の検証を抑制する構造は、触媒化学全般のVQ-2停滞の一因を示す。
* **将来の充填可能性**: 低 — 出版インセンティブ構造が変わらない限り、単独論文として充填されない。

---

**EP-07a Boundary-test pack:**
* **未充填の理由**: 関心の欠如 + インセンティブ構造の不整合 — ブロモメシチレンの低活性は立体効果として一般的に理解されており、「このNi触媒がbromomesityleneに弱い」という事実の詳細な説明は科学コミュニティにとって新規な知見を提供しない。
* **発見的意義**: なし（分野にとって自明な問い）
* **将来の充填可能性**: 低

---

**EP-08a Replication / uncertainty pack:**
* **未充填の理由**: インセンティブ構造の不整合 — 既存データの反復測定は「新しい科学的発見」を生まないため、独立論文として出版されない。
* **発見的意義**: あり — 「TOF値の3.8パーセントポイント差（50.9% vs 47.1%）が測定誤差の範囲を超えているか否か」は、complex 2とdpppの「優劣」が17年間（2009〜2026）にわたって検証されないまま引用され続けてきたことを意味する。これは未充填EPが単純な分析的欠如ではなく、分野が共有する根拠なき比較的主張の蓄積として機能している実例。
* **将来の充填可能性**: 低（単独論文として）/ 中（大規模触媒比較データベースプロジェクトの枠組みでは間接的充填の可能性）

---

**EP-04a Discrimination / replication pack（特定系での未充填）:**
* **未充填の理由**: インセンティブ構造の不整合 — 水銀滴下試験とTEMPO阻害はNi触媒論文に付帯的に含まれることがあるが、Monnereau論文の反応条件（100°C、dioxane、前活性化あり）でのmatched-pair対照実験を報告することを主目的とした論文は成立しない。
* **発見的意義**: あり（条件付き） — Ni(I)/Ni(III)パラダイム転換（EP-03a; paradigm-shift）を踏まえると、EP-04aが問う「均一系か」という問いは「どの酸化状態径路か」という問いと不可分になった。2009年時点での「均一系Ni(0)/Ni(II)の実証」は、2026年時点では「均一系Ni(I)/Ni(III)の実証」として再定義が必要であり、この問いは現代基準では未解消のまま。
* **将来の充填可能性**: 中 — 技術的には可能。calixarene-Ni系が活発な研究対象として残っている場合のみ充填動機が生じる。

---

**EP-09a Internal benchmark pack（完全充填の未達）:**
* **未充填の理由**: インセンティブ構造の不整合 — 「Monnereau 2009の条件をそのまま使って他の4種のジホスフィンと比較する」実験は、既存系の検証以上の意義を持たないため、独立論文として出版されない。
* **発見的意義**: あり — 「最速ジホスフィン触媒を凌駕する」という本論文の中心的比較主張が、17年間（2009〜2026）にわたって実験的に検証されないまま引用された可能性がある。これはSRG-2の未解消が知識伝播の「事実」として固定化される過程の証拠として記録できる。
* **将来の充填可能性**: 低（単独論文として）/ 中（大規模触媒比較データベースプロジェクトとして）

---

**VQ階層逆転の診断（総合）:**

未充填EPの分布を確認すると、VQ-2要件（RI-01: EP-01a, RI-07: EP-07a, RI-08: EP-08a）がすべて未充填・充填困難であるのに対し、VQ-3要件（RI-03: EP-03a）が充填済み（Paradigm-shift）、VQ-4要件（RI-09: EP-09a）が間接充填という明確な逆転パターンが成立している。

この逆転構造の意味：「測定の信頼性（VQ-2）」という科学的下位層が未充填のまま、「機構の同定（VQ-3）」という上位層の研究が先行する。これは、科学的論理に基づくEP充填順序（VQ-1 → VQ-2 → VQ-3 → VQ-4）と、出版インセンティブに基づく実際の充填順序（高VQ → 低VQ）の逆転として記録する。VQ-2要件に対応する実験（GCレスポンスファクター検証、反復測定）は新規性がなく独立論文にならないのに対し、VQ-3要件に対応する実験（Ni酸化状態の直接同定）は新たな科学的問いを提起するため先に充填される。この逆転構造はMonnereau 2009固有の問題ではなく、合成触媒化学分野全般のインセンティブ構造が生み出す系統的パターンとして記録する。
