```
prompt_version: stage4-v2-20260416
model_info: Claude Opus 4.7 (claude-opus-4-7[1m])
```

# EP 充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc., Communication）

---

### §A EP 充填難易度の三群分類

Stage 3 §5 に列挙された 10 の EP（EP-01a, EP-02a, EP-03a, EP-04a, EP-05a, EP-06a, EP-07a, EP-08a, EP-09a, EP-10a）を充填可能性で三群に分類する。

**第一群（文献で明確に追跡可能）:** EP-03a, EP-04a, EP-06a, EP-07a, EP-10a

- **EP-03a** は Ni-ホスフィン中間体の分光学的同定を要求し、1970 年代以降の in situ ³¹P NMR / EPR / X 線結晶構造解析による中間体キャラクタリゼーションが独立論文として確立した領域である（RI-03 は第一群候補規則にも該当）。
- **EP-04a** はラジカルプローブ・立体化学制御・TEMPO トラップを要求し、Kochi 派（1975-1978）以降、Ni 触媒クロスカップリングのラジカル機構検証は主題として独立論文化されてきた。
- **EP-06a** は β-H 脱離の Eyring / D 標識実験で、1970 年代後半の Kochi 書籍および Whitesides の Ni-alkyl 分解機構研究を中核として追跡可能。
- **EP-07a** は C_sp³ 境界試験で、2002 年以降の alkyl-Kumada 研究（Kambe, Vicic, Fu）が独立主題として確立。RI-07 第一群候補規則に該当。
- **EP-10a** は初期速度次数の測定で、Morrell & Kochi 1975 が典型的独立論文として存在。PRI-11 の充填に該当。

**第二群（間接的に追跡可能）:** EP-02a, EP-05a, EP-09a

- **EP-02a** は EA + HR-MS + 純度の開示で、原著者グループの Full Paper（1976 BCSJ）で部分的に充填されるが、独立主題の論文は存在しない。
- **EP-05a** は配位子順位の定量化で、レビュー論文や総説・方法論論文の一部として触れられるが、9 配位子 × 3 基質ペア matrix を独立主題として系統的に測定した論文は限定的。
- **EP-09a** は Ni(acac)₂ vs NiCl₂(dpe) の直接比較で、Corriu-Masse 1972 と Tamao-Kumada 1972 の「間接的比較」は後のレビュー（Negishi 2002 等）で扱われるが、matched pair の直接実験論文は稀。

**第三群（充填が見つからない可能性あり）:** EP-01a, EP-08a

- **EP-01a** は Table I の per-entry 条件開示・基準統一で、原論文固有の報告形式問題（RI-01 起因）。Full Paper 遷移（Tamao 1976 BCSJ）で部分的に解消されるが、本論文の Table I そのものに対する「逆引き」形式での独立充填論文は存在しない。RI-01 第三群候補規則に該当。
- **EP-08a** は Table I 全エントリの複製 n=3 + SD 報告で、1972 年の同じエントリの再現を独立主題として行った論文は存在しない（RI-08 第三群候補規則に該当、reproduction-only 研究は新規性要請で出版されにくい）。

---

### §B 各 EP の充填論文候補

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填する RI**: RI-03 [Unobserved explanatory], RI-06 [Imported model]（一部）
* **充填開始点**: Yamamoto, Kohara, Yamamoto, Bull. Chem. Soc. Jpn. 51, 2091 (1978) — trans-NiPh(Cl)(PEt₃)₂ および関連 L₂Ni(Ar)(X) 錯体の単離と X 線構造を報告し、Tamao-Kumada が仮定した中間体 2 の構造的実体性を確立した。Parshall, J. Am. Chem. Soc. 96, 2360 (1974) も trans-NiAr(X)(PEt₃)₂ の単離を独立に報告。
* **充填確立点**: Anderson, Jones, Vicic, J. Am. Chem. Soc. 126, 8100 (2004) および Jones, Martin, McMurdo, Vicic, J. Am. Chem. Soc. 128, 13175 (2006) — alkyl-alkyl Kumada 系で Ni(I) / Ni(III) 中間体を単離・EPR 検出し、Tamao-Kumada の Ni(II)/Ni(IV) vs Ni(0)/Ni(II) の曖昧性を alkyl 系では Ni(I)/Ni(III) 経路に再定式化（sp² 系とは異なる機構の可能性を含む、相関的充填）。
* **充填の性質**: Partial（sp² 系では L₂Ni(Ar)(X) の分光学的観測は確立したが、活性種の全てのステップを isolate できたわけではない）+ Paradigm-shift（alkyl 系ではラジカル機構経由の Ni(I)/Ni(III) cycle が支配的であることが判明し、eqs 2-4 の単純な Ni(II)→Ni(II) cycle は全ての場合に妥当ではないと示された）
* **Confidence**: High（Yamamoto 単離、Vicic Ni(III) 単離はいずれも広く引用）
* **注記**: sp²-Kumada の mechanism は Ni(0)/Ni(II) サイクルに近いが、alkyl-alkyl の場合は Ni(I)/Ni(III) ラジカル経路である——これは原論文の "working hypothesis" が基質依存であることを後付けで示した典型例。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填する RI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: Morrell, Kochi, J. Am. Chem. Soc. 97, 7262 (1975) — [REDACTED: substantial verbatim quotation; see Tier 9] ラジカル clock、disproportionation / dimerization ratio 分析、TEMPO-類似 trap、および mass balance 閉鎖（これは SRG-1 の RI-08 も同時に部分充填）を実施。
* **充填確立点**: Phapale, Guisán-Ceinos, Buñuel, Cárdenas, Chem. Eur. J. 15, 12681 (2009) — 現代の Ni-alkyl-Kumada における単電子 transmetalation / ラジカル中間体の存在を時間発展と trap で立証。
* **充填の性質**: Complete（ラジカル vs 二電子経路の discrimination は Morrell-Kochi 1975 で確立、sp²-Kumada の stereochem scramble の機構解釈も Kochi 以降の書籍で扱われる）
* **Confidence**: High（Morrell-Kochi 1975 は Ni-mechanism の canonical 論文）
* **注記**: Tamao-Kumada 1972 の cis/trans-ClCH=CHCl の "rather nonstereospecifically" 観察の機構的起源は、Morrell-Kochi の枠組みで「σ-vinyl-Ni 回転 vs radical cage-pair」の比較として議論可能。1,2-dichloroethylene 系での time-course は未充填（§E 参照）。

---

**EP-10a [Kinetic verification pack]（第一群、暫定）**

* **充填する RI**: PRI-11 [Mechanism-kinetics decoupling]
* **充填開始点**: Morrell, Kochi, J. Am. Chem. Soc. 97, 7262 (1975) — 同上。Ni-触媒 RMgX + R'X の初期速度依存性を [Ni], [RMgX], [R'X] について測定し、速度式と機構の代数的整合性を検証。
* **充填確立点**: Tsou, Kochi, J. Am. Chem. Soc. 101, 7547 (1979) — Ni(0)L_n + ArX の酸化的付加キネティクスを単独素反応として測定。活性化エネルギー、ΔH‡, ΔS‡ を報告。
* **充填の性質**: Complete（Ni-Kumada の速度次数は Kochi 派で確立）
* **Confidence**: High
* **注記**: Tamao-Kumada 1972 の触媒サイクル（eqs 2-4）から代数的に導出される速度式 v = k[Ni][RMgX][RX] は、Morrell-Kochi の実測次数と整合しないケースがあり、実際のサイクルは pre-equilibrium を含む（PRI-11 の具体的充填）。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填する RI**: RI-06 [Imported model]
* **充填開始点**: Kochi, "Organometallic Mechanisms and Catalysis" (Academic Press, 1978) — ref 17 が参照した β-H 脱離の一般論を Ni-alkyl 系で具体的に検証し、k_RE / k_{β-H} の定量的取り扱いを提供。
* **充填確立点**: Whitesides グループ（Grubbs, Miyashita, Ozaki et al.）の 1970-80 年代 Ni-dialkyl の熱分解研究（J. Am. Chem. Soc. 98, 1976 等） — L₂NiR₂ の β-H 脱離 vs reductive elimination の Eyring パラメータを測定。
* **充填の性質**: Complete（β-H 論拠の Ni 系への応用は定量化された）
* **Confidence**: High
* **注記**: Tamao-Kumada 1972 の feature 1（β-H Grignard が働く）は、現代的には「k_RE が k_{β-H} より大きい配位子条件を dpe が提供する」として理解される。SRG-8 の RI-03 と RI-06 が同時に解消。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填する RI**: RI-07 [Unsupported boundary], RI-09 [External superiority]
* **充填開始点**: Terao, Watanabe, Ikumi, Kuniyasu, Kambe, J. Am. Chem. Soc. 124, 4222 (2002) — [REDACTED: substantial verbatim quotation; see Tier 9] Tamao-Kumada 1972 の "Only C_sp² halides... can be used" 境界を、1,3-butadiene 添加剤により C_sp³ 側に拡張。RI-07 の境界主張が 30 年後に否定的に解消された典型例。
* **充填確立点**: Anderson, Jones, Vicic, J. Am. Chem. Soc. 126, 8100 (2004) — terpyridyl-Ni 触媒で alkyl-alkyl Kumada を達成（原論文 Tamao-Kumada で排除された変換を実現）。
* **充填の性質**: Paradigm-shift（C_sp³ 境界そのものが Ni 触媒設計の変更で解消可能と判明——これは Tamao-Kumada の境界主張を「Ni-ホスフィン系では成立する限定」として文脈化）
* **Confidence**: High
* **注記**: Kambe 2002 は 1,3-butadiene を添加剤として用いる新しい Ni 化学を提示しており、dpe や dppe とは異なる配位子系統。RI-07 「otherwise C_sp² のみ」の boundary の「あるべき姿」を具体化した。Cl/Br/I の halide 優位性は同じ Kambe 派と Fu 派の後続研究で系統化。

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填する RI**: RI-02 [Object identification]
* **充填開始点**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, Bull. Chem. Soc. Jpn. 49, 1958 (1976) — 原著者グループの Full Paper。Table I の 10 エントリを含む広範な scope を、EA + bp + NMR + IR で完全開示。
* **充填確立点**: 同上
* **充填の性質**: Complete（原著者グループによる自己充填）
* **Confidence**: High（著者と Full Paper 展開は広く知られる）
* **注記**: 通信 → Full Paper 遷移の自動解消パターンの典型例。SRG-6 の B-17（EA 欠落）、B-11（bp 圧力整合）、B-16（純度）がこの 1976 BCSJ で解消。B-08（isolated/GLPC 混在）および B-14（yield 基準）も Full Paper 内で per-entry 列構造により解消。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填する RI**: RI-05 [Qualitative overread]
* **充填開始点**: Kumada 自身の総説（Kumada, Pure Appl. Chem. 52, 669 (1980) [REDACTED: substantial verbatim quotation; see Tier 9]）— 配位子ごとの yield / time data を部分的に表形式で開示。
* **充填確立点**: 独立な matrix 論文は未同定。部分充填として、de Vries グループや Fürstner の Ni-Kumada レビュー（Fürstner, Leitner, Angew. Chem. Int. Ed. 41, 609 (2002) 等）に cross-compilation として存在する。
* **充填の性質**: Partial（SRG-4 の 9 × 3 matrix は独立論文として充填されていないが、個別の配位子ペアごとの yield 比較は多数の後続論文に断片的に存在）
* **Confidence**: Medium（Kumada 1980 の総説は実在するが、SRG-4 Case-specific の matrix そのものの完全実装は未同定）
* **注記**: SRG-4 の「cis-強制単座配位子との制御」は独立論文として未同定で、§E で未充填として扱う。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填する RI**: RI-09 [External superiority]
* **充填開始点**: Negishi 2002 のレビュー（Negishi, Coperet, Tour et al. — Ni-Kumada / Negishi 系列のレビュー）が間接的に Ni(acac)₂ vs [NiCl₂(dpe)] の scope 差を体系化。
* **充填確立点**: 独立な matched-pair 直接比較論文は **未同定**。CLA-1 の「phosphine 要件」の直接検証は primary literature で稀である（両系列が独立に発展したため、head-to-head 比較のインセンティブが低かった）。
* **充填の性質**: Indirect + Attempted（間接的に scope 比較はあるが、Case-specific 実装の matched-pair 比較は未達成）
* **Confidence**: Low（Ni(acac)₂ vs NiCl₂(dpe) の直接比較論文の存在について知識不確実）
* **注記**: §E で部分的に未充填として扱う。インセンティブ構造の不整合の典型例。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填する RI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 49, 1958 (1976) — Full Paper で Table I の各エントリが per-entry 条件開示を伴う形で拡張再掲される。
* **充填確立点**: 同上（通信固有の RI-01 は同一著者の Full Paper 発表で解消）
* **充填の性質**: Complete（通信 → Full Paper 遷移による自動解消）
* **Confidence**: High
* **注記**: §D で「自己充填」パターンとして分類。4 年の遅延で解消。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填する RI**: RI-08 [Unquantified reliability]
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: Attempted（Tamao 1976 Full Paper でも複製 n や SD は通常開示されていない）
* **Confidence**: n/a
* **注記**: §E で未充填として扱う。RI-08 は分野全体で「新規性要請の下で独立論文化されない」典型カテゴリ。ただし SRG-1 の「マスバランス」側面は Morrell-Kochi 1975 で mechanistic kinetics の一環として部分充填（EP-04a 経由）。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填する EP | VQ 水準 | 年代 | Confidence |
|------|------|--------------|---------|------|------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, Bull. Chem. Soc. Jpn. 49, 1958 (1976) | EP-01a, EP-02a, EP-05a (部分) | VQ-2 | 1976 | High |
| 2 | Morrell, Kochi, J. Am. Chem. Soc. 97, 7262 (1975) | EP-04a, EP-10a, EP-03a (部分) | VQ-3 | 1975 | High |
| 3 | Yamamoto, Kohara, Yamamoto, Bull. Chem. Soc. Jpn. 51, 2091 (1978) + Parshall, J. Am. Chem. Soc. 96, 2360 (1974) | EP-03a | VQ-3 | 1974-1978 | High |
| 4 | Kochi, "Organometallic Mechanisms and Catalysis" (Academic Press, 1978) + Whitesides group Ni-dialkyl thermolysis 1970s | EP-06a, EP-04a (部分) | VQ-3 | 1976-1978 | High |
| 5 | Terao, Watanabe, Ikumi, Kuniyasu, Kambe, J. Am. Chem. Soc. 124, 4222 (2002) | EP-07a | VQ-3 | 2002 | High |
| 6 | Anderson, Jones, Vicic, J. Am. Chem. Soc. 126, 8100 (2004) + Jones, Martin, McMurdo, Vicic, J. Am. Chem. Soc. 128, 13175 (2006) | EP-03a, EP-07a (部分) | VQ-3 | 2004-2006 | High |
| 7 | Phapale, Guisán-Ceinos, Buñuel, Cárdenas, Chem. Eur. J. 15, 12681 (2009) | EP-04a (近代検証) | VQ-3 | 2009 | Medium |

**選定理由:**

本リストは 4 つの設計原則に従って構成した。

第一に、**VQ 階層の階段状カバレッジ**：順序 1（Tamao 1976 BCSJ）は VQ-2 の modern 要件（EP-01a, EP-02a）を自己充填で解消、順序 2-7 は VQ-3 要件（EP-03a, EP-04a, EP-06a, EP-07a, EP-10a）を段階的に充填する。VQ-4 までの到達は部分的（SRG-1 のマスバランス側面は Morrell-Kochi 1975 経由で前進）。

第二に、**バンドル充填の優先**：Morrell-Kochi 1975（順序 2）は EP-04a + EP-10a + EP-03a を同時に充填する稀少な論文で、PRI-11 の充填例としても重要である。これを入れることで 3 つの EP を単一の引用で扱える。

第三に、**年代の多様性**：1974 年（Parshall）から 2009 年（Phapale）まで 35 年に渡る充填の時間軸を押さえた。通信 → Full Paper 自動解消（1976）、機構学派による系統的充填（1975-1978）、単離中間体化学の成熟（2004-2006）、および現代の radical 機構再検証（2009）の 4 フェーズを含む。

第四に、**Paradigm-shift 充填の記録**：順序 5（Kambe 2002）と順序 6（Vicic 2004-2006）は Tamao-Kumada の「C_sp²のみ」境界と Ni(0)/Ni(II) cycle の両方を、sp³ alkyl 系の Ni(I)/Ni(III) 機構で再定式化した。これは単純な充填ではなく paradigm-shift 的充填で、原論文の枠組みの文脈依存性を事後的に明らかにした事例。

---

### §D VQ 階層と充填時間順序の対応分析

**充填の時間軸:**

- **VQ-2 要件**: EP-01a → 1976 Tamao 自身の Full Paper（BCSJ 49）【自己充填】
- **VQ-2 要件**: EP-02a → 1976 Tamao 自身の Full Paper【自己充填】
- **VQ-3 要件**: EP-03a（sp² 中間体単離）→ 1974 Parshall, 1978 Yamamoto【技術駆動充填（X 線結晶構造）】
- **VQ-3 要件**: EP-04a（ラジカル vs 2e 経路）→ 1975 Morrell-Kochi【分野横断充填（Kochi 派の機構学的アプローチ）】
- **VQ-3 要件**: EP-06a（β-H kinetic）→ 1976-1978 Kochi 書籍, Whitesides【技術駆動充填（Eyring 精密化）】
- **VQ-3 要件**: EP-10a（速度次数）→ 1975 Morrell-Kochi【分野横断充填】
- **VQ-3 要件**: EP-07a（C_sp³ 境界）→ 2002 Kambe【パラダイム転換充填（30 年遅延）】
- **VQ-3 要件**: EP-03a 再検（alkyl-Ni(I)/Ni(III)）→ 2004-2006 Vicic【パラダイム転換充填（32-34 年遅延）】
- **VQ-3 要件**: EP-04a 現代検証 → 2009 Phapale-Cárdenas【長期遅延充填】
- **VQ-2 要件**: EP-05a（配位子順位 matrix）→ 1980 Kumada 総説【部分充填のみ、独立 matrix 論文は未同定】
- **VQ-2/3 要件**: EP-09a（Ni(acac)₂ vs dpe matched-pair）→ 未同定
- **VQ-2 要件**: EP-08a（Table I 複製 + SD）→ 未同定

**階層-時間対応の評価:**

仮説「VQ 階層が上がるほど充填に要する時間が長くなる」は、本ケースでは **部分的に支持されるが顕著な反例を伴う**。支持する証拠として、VQ-2 要件（EP-01a, EP-02a, RI-01/RI-02 系）は 4 年（1976 Tamao Full Paper）で自己充填された一方、VQ-3 要件の主要部分は 3-6 年（1975-1978 の Kochi / Parshall / Yamamoto / Whitesides 系）で充填された。しかし反例として、VQ-3 要件の一部（EP-07a の C_sp³ 境界解消、EP-03a の alkyl 系中間体）は 30 年以上遅延している——これは VQ 階層ではなく「原論文の暗黙的前提（sp² 限定）が破られる技術的前提条件（1,3-butadiene 添加剤、terpyridyl-Ni）の登場」に律速された。むしろ「低 VQ 要件（RI-08 の複製 n）が未充填のまま残り、高 VQ 要件（RI-03 の中間体単離）が先に充填された」という **VQ 階層逆転パターン**が観察される——これは §E で扱う。

**特筆すべきパターン:**

1. **自己充填の典型例**: Tamao 1976 BCSJ Full Paper は通信 → Full Paper 遷移の典型的自動解消。EP-01a, EP-02a を単一論文で同時充填し、Stage 3 §6 で予測された「通信 → Full Paper 自動解消パターン」を実証する。
2. **バンドル充填の典型例**: Morrell-Kochi 1975 は EP-04a + EP-10a + EP-03a（部分）を同時充填。単一論文で RI-04, PRI-11, RI-03（部分）の 3 つの RI を前進。これは分野横断充填（Kochi のラジカル機構学派が Tamao-Kumada の機構問題に外部から切り込んだ）の典型。
3. **パラダイム転換充填の典型例**: Kambe 2002（1,3-butadiene 添加剤で sp³ Kumada 実現）+ Vicic 2004-2006（Ni(I)/Ni(III) cycle）は、Tamao-Kumada の境界主張（sp² のみ）と機構提案（Ni(II) cycle）の両方が基質依存的であることを 30 年後に示した。これは EP-07a の充填というより「原論文の前提の再定式化」であり、問い自体の再生成。
4. **長期遅延充填**: EP-07a と EP-03a の alkyl 側充填は 30 年遅延。これは技術的前提（Ni-terpyridyl 錯体、butadiene 添加剤、EPR で Ni(III) 検出）の整備に要した時間を反映する。
5. **著者回顧との照合**: Kumada 1980 総説（Pure Appl. Chem. 52, 669）および後年のノーベル関連文献で Kumada 派が振り返る「成果」は主に scope 拡張と Full Paper 整備に集中し、機構層（EP-03a, EP-10a）の自己充填はあまり主題化されていない——これは「分野の内部者には可視的な構造的不在（RI-03, PRI-11）が外部充填（Kochi 派）に委ねられた」という UQS 観察を事後的に支持する。

---

### §E 未充填 EP の発見的意義

**未充填 EP 一覧:**

---

**EP-05a [Quantitative-ranking substantiation pack]（部分未充填）:**

* **未充填の理由**: インセンティブ構造の不整合。SRG-4 Case-specific の「9 配位子 × 3 基質ペア matrix + cis-強制単座制御」は独立論文として充填されていない。独立した ligand-screening study は 1980 年代以降存在するが、Tamao-Kumada の feature 3（配位子順位）を matched-pair で検証する目的で構成されたものはない——これは「原論文の主張の定量的裏付け」が独立論文として新規性を持たないという出版インセンティブの不整合。
* **発見的意義**: あり。feature 3 の「cis configuration is the first requisite」という構造的含意は、45 年経過後も定量的に検証されていない。分野が「効いた配位子を使う」という実用的レベルで満足し、「なぜ効くか」の操作的検証を回避してきたことの証拠。
* **将来の充填可能性**: 中。現代の高速 HT-screening 技術（Merck / Doyle の HT screening platform）で実行可能だが、「1972 年論文の主張の再検証」という主題化が必要で、インセンティブは限定的。

---

**EP-09a [Internal benchmark pack]（未充填）:**

* **未充填の理由**: インセンティブ構造の不整合 + 分野慣行。Ni(acac)₂（Corriu-Masse 1972）vs [NiCl₂(dpe)]（Tamao-Kumada 1972）の matched-pair 直接比較は、両系列が独立発展したため、head-to-head 論文として成立しにくい。CLA-1 の「phosphine 要件の実証」は現代の触媒開発のレンズでは重要だが、1972 年当時の両グループはそれぞれ独自の scope 拡張を優先。
* **発見的意義**: あり。Tamao-Kumada 論文のタイトル "Nickel-Phosphine Complexes" が主張する暗黙の phosphine 要件は、54 年経過後も matched-pair 比較で確認されていない——これは「タイトルの主張が primary literature 内で直接検証されないまま歴史化される」パターンの典型例。
* **将来の充填可能性**: 低。両系列はそれぞれ独立に発展したため、現代の研究者に「1972 年の両論文の直接比較」を行うインセンティブはほぼ存在しない。

---

**EP-08a [Replication / uncertainty pack]（未充填）:**

* **未充填の理由**: 分野慣行 + インセンティブ構造の不整合。Table I の 10 エントリを n=3 で複製し SD を報告する独立論文は存在しない。再現研究は新規性要請の下で出版されにくく、Full Paper（1976）でも複製統計は通例的に開示されない。RI-08 第三群候補規則に該当。
* **発見的意義**: 大。Stage 3 §6 で提案した新規 PRI 候補「PRI-12: Self-prediction-observation gap」に関連し、**VQ 階層逆転パターン**の直接的証拠となる——科学的論理では VQ-2 要件（RI-08）の解消が VQ-3 要件（RI-03, RI-04）の解消より優先されるべきだが、実際には VQ-3 要件が 1975-1978 年に先に充填され、VQ-2 要件（複製 SD）は 54 年経過後も未充填。これは「出版インセンティブに基づく実際の充填順序（高 VQ → 低 VQ）」が「科学的論理に基づく充填順序（低 VQ → 高 VQ）」を逆転している証拠として記録される。
* **将来の充填可能性**: 低。Tamao-Kumada 1972 の再現を目的とする論文のインセンティブは現代でも存在しない。

---

**EP-03a の一部（Ni(0) 活性種の単離、cis-constrained 対照の中間体）（部分未充填）:**

* **未充填の理由**: 技術的困難 + 分野関心の限定。SRG-4 Case-specific 実装の「cis-強制単座配位子対照」中間体（cis-固定シクロパラジフェニレン系等）は独立論文として合成・単離されていない。sp² 系の L₂Ni(0) 活性種（L = dpe）の直接単離も限定的で、通常は L₂NiR₂ の熱分解経由で推定される。
* **発見的意義**: あり。SRG-2 の 6 下位項目中、中間体 1, 2 は Yamamoto 1978 + Parshall 1974 で部分充填されたが、中間体 3 の L₂Ni(R)(R′) + R″X″ → L₂Ni(R)(R′)(R″)(X″) の Ni(IV) 経由 or Ni(0) 経由の discrimination はなお曖昧。これは原論文の機構的曖昧性が 50 年経過後も完全解消に至っていない証拠。
* **将来の充填可能性**: 中。現代の低温 ³¹P NMR / cryo-EPR 技術、および quantum mechanical calculations（DFT + multireference）で discriminating 実験設計可能。

---

**EP-04a の一部（1,2-ジクロロエチレンの cis:trans time-course + control 異性化試験）（部分未充填）:**

* **未充填の理由**: 分野関心の限定。1,2-ジクロロエチレン特異的な stereochem 時間発展（SRG-3 Case-specific 実装）を独立主題として追跡した論文は未同定。Morrell-Kochi 1975 以降の Ni-Kumada ラジカル機構研究はもっぱら alkyl 系に集中し、sp²-sp² cross-coupling の stereochem scrambling は分野の中心関心から外れた。
* **発見的意義**: あり。feature 4（cis-stilbene ルート）は原論文の 6 層 novelty 柱の 1 つだが、54 年経過後もその機構的起源は検証されていない。SRG-3 の「合成的ラッピング（"may offer a facile route"）による機構問題の回避」が長期に維持されたパターンの直接証拠。
* **将来の充填可能性**: 中-高。現代の chiral stilbene 需要（OLED 材料、光学活性 ligand）が復活させる可能性あり。

---

**VQ 階層逆転の総合診断:**

本ケースは Stage 4 の分析枠組みが予言する **VQ 階層逆転パターン** の明瞭な実例を提供する。

未充填 EP のうち、EP-08a（RI-08 低 VQ 要件）および EP-09a（RI-09 VQ-4 要件）は分野のインセンティブ構造の下で未充填のまま残り、**充填済み EP** の主力は EP-03a / EP-04a / EP-10a / EP-06a（いずれも RI-03 / RI-04 / RI-06 / PRI-11 の VQ-3 要件）である。論理的充填順序（RI-01 / RI-02 / RI-08 → RI-03 / RI-04 / RI-06 → RI-08 / RI-09）と実際の充填順序（RI-02 (1976) → RI-03 / RI-04 / RI-06 / PRI-11 (1975-1978) → RI-08 / RI-09 未充填）は明確に逆転している。

この逆転は、**「機構的 insight（VQ-3）を提供する実験は独立論文としての新規性を持つが、報告整備（VQ-2）や複製（VQ-2-4）を目的とする実験は新規性要請の下で論文化されない」**という分野のインセンティブ構造が、UQS の構造的不在の一部（RI-08, RI-09）を長期維持していることを示している。このパターンは Stage 3 §6 の institutional 知見を支持し、本ケースを既存 Codebook における VQ 階層逆転パターンの代表事例として記録する。

---

**充填状況のサマリー:**

- 完全充填: EP-01a (1976), EP-02a (1976), EP-06a (1976-78), EP-10a (1975), EP-04a (1975 基本, 2009 現代), EP-07a (2002 パラダイム転換)
- 部分充填: EP-03a（sp² 中間体は 1974-1978, alkyl 中間体は 2004-2006, cis-強制対照は未充填）, EP-05a（scope 別・独立 matrix は未充填）
- 未充填: EP-08a, EP-09a

10 EP 中、完全充填 6、部分充填 2、未充填 2。科学史的には 54 年経過後も 20% の EP が未充填で残存しており、これは **分野のインセンティブ構造が UQS の一部を制度的に維持している**ことの定量的証拠である。

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
