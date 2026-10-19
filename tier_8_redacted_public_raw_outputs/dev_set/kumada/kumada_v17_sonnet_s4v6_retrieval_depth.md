```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6
experimental_variant: retrieval-depth-annotation
note: 通常の Stage 4 v6 出力に retrieval depth annotation を付加した実験変体。
      各充填候補について Self-Tier (I/II/III) / 推論経路 / DB-findability を記録。
      末尾に retrieval depth matrix を統合表として再掲。
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc., Communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-03a, EP-06a, EP-07a

— **EP-01a (RI-01 SRG-3)**: Communication 形式の報告完全性問題（glpc条件、反応時間、収率基準）は同一著者グループの Full Paper で系統的に再報告されるのが分野慣行であり、C23（Letter→Full Paper auto-resolution）が高確度で発火する。
— **EP-03a (RI-03 SRG-1)**: ジオルガノニッケル中間体 [NiR₂(L)₂] の単離・分光観測は1970年代から独立した有機金属化学の主題として複数グループが取り組み、対象系（dpe ligand）でも Yamamoto/Komiya グループの体系的研究が存在する。
— **EP-06a (RI-06 SRG-1)**: dpe-Ni 系での化学量論的素反応（trans-metalation、酸化的付加、還元的脱離）は触媒サイクルの validation として機構化学の独立トピックを成す。
— **EP-07a (RI-07 SRG-4)**: 基質スコープ拡張（sp³ ハライド・塩化物 vs 臭化物 vs ヨウ化物の直接比較）は方法論論文として頻出する形式。Kumada 系の sp³ 拡張は遅延した（VQ-4 段階の長期遅延充填パターン）。

**第二群（間接的に追跡可能）：** EP-02a, EP-04a, EP-05a, EP-09a

— **EP-02a (RI-02 補助)**: VQ-1 non-fatal 残存の identity/purity は Full Paper 展開（Tamao 1976 BCSJ）で個別 ¹H NMR・元素分析データとして自動解消される性格。Letter→Full Paper auto-resolution（C23）の典型副次効果。
— **EP-04a (RI-04 SRG-6)**: cis/trans-stilbene 比の速度論/熱力学区別実験は Kumada 群と Kochi 群の機構研究で部分的に扱われたが、温度系列・反復測定を独立論文の主題として統合した報告は限定的。
— **EP-05a (RI-05 SRG-2)**: ホモカップリング R–R の質量収支データは Kochi 群の機構論文で別文脈として記録されたが、Kumada 反応そのものの「選択性」主張への反駁／支持として記録された独立論文は希薄（ただし Tamao 1976 Full Paper にホモカップリング副生量の言及が部分的にある）。
— **EP-09a (RI-09 CLA-1)**: NiCl₂(dpe) と Ni(acac)₂（Corriu/Masse 系）の同一基質・同一条件での直接比較は、文献中で散在的にしか記録されていない。**C7 trigger 候補**: 1980年代以降の Pd-cross-coupling（鈴木・根岸・Stille）への分野的 pivot により、原 Ni-ligand 設計議論の検証需要が部分的に erased された pattern が観察される。

**第三群（充填が見つからない可能性あり）：** EP-08a

— **EP-08a (RI-08)**: 統計的反復測定・標準偏差報告は合成化学分野の出版慣行に組み込まれていないため、原論文の検証目的で独立に行われた追試論文は事実上存在しない。**C6 trigger**: 「インセンティブ構造的未充填」— 技術的には可能だが、追試・反復測定が独立論文として出版されにくい publication incentive misalignment による。

---

### §B 各EPの充填論文候補

> **Hallucination 警告**: Kumada 系統は memory 記録上 Sonnet 67% hallucination 率を示す高警戒対象（cross_model_kumada_vs_murai_meta より）。Tamao-Sumitani-Kiso-Kumada と Tamao-Sumitani-Kumada は別論文の著者組合せであり、混同リスクあり。各候補に Verification recommendation を付与する。

---

#### **EP-01a [Reporting-coherence pack]（第一群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao K., Sumitani K., Kiso Y., Zembayashi M., Fujioka A., Kodama S., Nakajima I., Minato A., Kumada M., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — Kumada 反応の Full Paper として Table I の全エントリを統一 glpc 条件・反応時間・基質基準で再報告し、追加スコープ（11 エントリ → 30+ エントリ規模）を提供。
* **充填確立点**: 同上
* **充填の性質**: Complete — Communication 形式の紙幅制約に起因した報告不足が同一著者グループの Full Paper で実質的に解消される C23 の典型事例。
* **Bibliographic confidence**: Medium-High — 著者列・年・雑誌は強い確信を持つが、巻号 49/1958 と全著者リストの正確性に対しては Crossref 検証が必要。
* **Filling adequacy confidence**: High — Kumada 反応の Full Paper として SRG-3 の RI-01 を構造的に解消する論文であることは分野的合意がある。
* **Verification recommendation**: 必須 — トリガー条件 (a)+(c)+(b) 該当（1980 年以前 + named reaction + 著者ネットワーク密）。
* **DOI / URL**: 推定 https://doi.org/10.1246/bcsj.49.1958（要 Crossref 確認）
* **Filling timescale category**: format-driven (1-3 yr) → **実際は 4 yr** 該当。format-driven の典型範囲（1-3 yr）をやや超えるが、Communication-Full Paper auto-resolution パターンとしては典型的。
* **Bibliographic verification status**: pending
* **注記**: 本論文は EP-02a, EP-04a, EP-05a を**バンドル充填**する可能性が高い（Tamao 1976 BCSJ 内で Table 全エントリの個別 NMR 等同定 + cis/trans 比の追加データ + 副生物への言及）。**Self-Tier: I (immediate)** — EP-01a を読んだ瞬間に「Tamao の BCSJ Full Paper」が想起された。**推論経路**: EP-01a → "Communication 形式の Letter→Full Paper auto-resolution (C23)" → "Kumada 群の Full Paper として 1976 BCSJ 49 巻が標準引用" → 直接想起。**DB-findable**: yes — title に "Nickel-Phosphine Complex" "Cross-Coupling" "Grignard" を含むはず。

---

#### **EP-02a [Identity/purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Product identity, non-fatal residual]
* **充填開始点**: Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969（同上）— Full Paper として Table 各エントリの個別 ¹H NMR・IR・元素分析データを提供することで "and/or" 構文による不完全同定（VQ-1 non-fatal）を解消。
* **充填確立点**: 同上
* **充填の性質**: Complete（C23 副次効果として）
* **Bibliographic confidence**: Medium-High（EP-01a と同一論文）
* **Filling adequacy confidence**: Medium — Full Paper の典型的内容として個別データが含まれることは強く期待されるが、本確認には実物確認が必要。
* **Verification recommendation**: 必須（EP-01a と同一）
* **DOI / URL**: 同上
* **Filling timescale category**: format-driven (1-3 yr) → 実際 4 yr
* **Bibliographic verification status**: pending
* **注記**: EP-01a とのバンドル充填。**Self-Tier: I (immediate)** — EP-01a と同一論文として一括想起。**推論経路**: EP-02a → "Full Paper では個別分光データが標準" → 同じ Tamao 1976 BCSJ。**DB-findable**: yes（同上）。

---

#### **EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory entity]
* **充填開始点**: Yamamoto T., Yamamoto A., Ikeda S., *Bull. Chem. Soc. Jpn.* **1971**, *44*, 1505 ほか — diorganonickel-bisphosphine 錯体 [NiR₂(L₂)] の単離・特性評価の系列（Kumada 1972 paper では ref 11/12 として近接系が引用済）。
* **充填確立点**: Komiya S., Abe Y., Yamamoto A., Yamamoto T., *Organometallics* **1983**, *2*, 1466 — cis-[NiR₂(dppe)] 型錯体の還元的脱離の速度論・立体化学を体系的に記述（dpe/dppe = 1,2-bis(diphenylphosphino)ethane, Kumada 系と同一配位子）。
* **充填の性質**: Partial-to-Complete — 中間体 1 の構造類似体としては実証されたが、Kumada 反応条件下（in situ）での観測ではない。
* **Bibliographic confidence**: Medium-Low — 著者列・グループは確信あるが、特定の年・巻号・ページについては確信度低い。"Komiya, Yamamoto 1980年代" の枠組みは正しいが、**1983 Organometallics 2/1466 という具体ペアは要 Crossref 検証**。
* **Filling adequacy confidence**: Medium — dpe/dppe 系統での関連報告は確実に存在するが、Kumada 反応の中間体 1 に直接対応する観測かは精査必要。
* **Verification recommendation**: 必須 — トリガー (b)+(d) 該当（Yamamoto 群は10+論文ネットワーク + Bib confidence Medium-Low）。
* **DOI / URL**: 未推定（要検索）
* **Filling timescale category**: field-methodology (2-5 yr) — Yamamoto 群は Kumada 1972 と並行・直後に diorganonickel 化学を独立に展開しており、方法論的 field 応答パターン。実時間幅は10年以上に及ぶ。
* **Bibliographic verification status**: pending（高警戒）
* **注記**: **Self-Tier: II (associative)** — EP-03a → "diorganonickel intermediate observation" → "1970年代の有機金属化学で誰がやっていたか" → "Akio Yamamoto group, Komiya as key author"（2-3 段階の連想）。**棄却した候補**: Wilkinson group(英国) の関連研究を一瞬考慮したが、ニッケル系より白金・ロジウム系の特性評価が中心で、kumada 関連性が弱いと判断し棄却。**DB-findable**: yes — title に "diorganonickel" "reductive elimination" 等を含むはず。

---

#### **EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: Tamao K., Kiso Y., Sumitani K., Kumada M., *J. Am. Chem. Soc.* **1972**, *94*, 9268 — 同一著者群が原論文の数ヶ月後に発表した stereochemistry-focused communication として、ビニル halide cross-coupling の cis/trans selectivity の追加データ。
* **充填確立点**: Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958（同 Full Paper）— cis/trans 比の reaction time 依存性データを含む可能性大。
* **充填の性質**: Partial — kinetic vs thermodynamic 区別を直接目的とした実験設計ではなく、scope-extension の副産物として記録される傾向。
* **Bibliographic confidence**: Low-Medium — 1972 の続報は **存在の確信は中程度だが、JACS 94/9268 の正確な page は要検証**（同号近傍に Tamao 続報があるはずだが page を hallucination するリスク）。
* **Filling adequacy confidence**: Low — 速度論的/熱力学的区別を独立トピックとして扱った論文を Kumada 系統で同定するのは困難。
* **Verification recommendation**: 必須
* **DOI / URL**: 未推定
* **Filling timescale category**: format-driven (immediate, 同年内) → 続報 communication パターン
* **Bibliographic verification status**: pending（特に高警戒）
* **注記**: **Self-Tier: II→III** — EP-04a → "cis/trans selectivity follow-up by same group" → "Tamao 1972 続報[REDACTED: substantial verbatim quotation; see Tier 9]stereochemistry" 等を含むかは不明。

---

#### **EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: Smith G., Kochi J. K., *J. Org. Chem.* **1976**, *41*, 502 ほか Kochi 系列 — 遷移金属触媒下 Grignard + alkyl halide cross-coupling の機構研究で、ホモカップリング R–R の質量収支とラジカル中間体の関与を定量化（Ni 触媒は AgI/CuI 触媒と並行して扱われる文脈）。
* **充填確立点**: Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958（同 Full Paper）— Kumada 系統の側からの "selectivity" 主張の数値裏付けとして部分的に機能。
* **充填の性質**: Partial — Kochi 側は alkyl-alkyl coupling の文脈、Tamao 1976 側は scope 拡張の副次データ。Kumada 反応そのものの "selectivity" 主張を数値的に直接検証した独立論文は希薄。
* **Bibliographic confidence**: Low — Kochi の Ni 関連論文の特定の書誌情報には確信度低い。"Smith, Kochi" の組合せは複数論文にまたがる可能性あり。
* **Filling adequacy confidence**: Low-Medium
* **Verification recommendation**: 必須
* **DOI / URL**: 未推定
* **Filling timescale category**: incentive-aligned (variable) — 複数グループの分散応答
* **Bibliographic verification status**: pending（高警戒）
* **注記**: **Self-Tier: II→III** — EP-05a → "selectivity quantification, R–R byproduct" → "Kochi as radical/cross-coupling mechanism authority" → "Smith-Kochi paper(s) in mid-1970s"（複数候補からの triangulation を要する）。**棄却した候補**: Schwartz J. の hydrozirconation/Ni 関連、Negishi E. の Ni-mediated coupling — 両者とも別反応系の文脈で Kumada 反応の selectivity 主張への直接検証ではないため棄却。**DB-findable**: yes (Kochi の論文は標準的タイトル) / uncertain (Tamao 1976 内の言及は subsection level)。

---

#### **EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]
* **充填開始点**: Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958（同 Full Paper）— Kumada 系統側からの NiCl₂(dpe) 系の独立的検証（化学量論実験を含む可能性）。
* **充填確立点**: Komiya S., Abe Y., Yamamoto A., Yamamoto T., *Organometallics* **1983**, *2*, 1466 もしくは Komiya/Yamamoto グループの 1978-1985 の系列 — cis-[NiR₂(dppe)] 還元的脱離の機構的詳細を化学量論的・速度論的に検証することで、Kumada が提案した「cis-diorganonickel 経由の還元的脱離」というメカニズム要素に独立証拠を提供。
* **充填の性質**: Partial — eq (3) の R-X' 酸化的付加 / cross-coupling 産物放出の素反応については別途検証要。
* **Bibliographic confidence**: Low-Medium — Komiya/Yamamoto 系列の存在は確信度高いが、特定論文との EP マッピングの粒度に不確定性。
* **Filling adequacy confidence**: Medium — cis-diorganonickel reductive elimination の直接実証は Kumada 機構仮説の中核要件を満たす。
* **Verification recommendation**: 必須
* **DOI / URL**: 未推定
* **Filling timescale category**: technical-barrier→field-methodology (5-15 yr) — 低温 NMR・X 線結晶構造解析等の発展との相互作用。
* **Bibliographic verification status**: pending
* **注記**: **Self-Tier: II** — EP-03a と同一論文系列での想起。**DB-findable**: yes — "reductive elimination" "diphosphine nickel" は標準キーワード。

---

#### **EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958（同 Full Paper）— sp²/sp³ 境界と halide 種比較を scope 拡張として系統的に再検討。
* **充填確立点**:
  (a) sp³ alkyl halide 拡張: Devasagayaraj A., Stüdemann T., Knochel P., *Angew. Chem. Int. Ed. Engl.* **1995**, *34*, 2723 — Ni-触媒 sp³ alkyl halide cross-coupling の本格的拡張開始点。
  (b) Vicic D. A. グループ・Fu G. C. グループ（2003-2010年代）— sp³-sp³ Negishi/Kumada 型 cross-coupling の包括的展開。
* **充填の性質**: Paradigm-shift（sp³ 拡張に関しては）— 「sp² halides only」境界は 23 年後に Knochel 等によって部分的に超えられたが、これは Kumada 反応の枠組み内ではなく、新触媒系（Ni/diamine 等）への遷移を伴った。
* **Bibliographic confidence**:
  - Tamao 1976 BCSJ: Medium-High（同上）
  - Knochel 1995: Medium — 著者・年・雑誌は確信、巻号要検証。
* **Filling adequacy confidence**: Medium-High（halide 種比較）/ Partial（sp³ 拡張は paradigm-shift）
* **Verification recommendation**: 必須
* **DOI / URL**: 未推定
* **Filling timescale category**:
  - 塩化物 vs 臭化物 vs ヨウ化物: format-driven (4 yr, Tamao 1976)
  - sp³ 拡張: technical-barrier (15-30 yr) — 触媒設計のパラダイム変化を要した長期遅延充填
* **Bibliographic verification status**: pending
* **注記**: **Self-Tier: I (Tamao 1976 BCSJ) + III (Knochel/Fu/Vicic 系列)** — **二段階 retrieval**: 塩化物比較は Tamao Full Paper で即想起（Tier I）、sp³ 拡張は「20年以上の遅延、Knochel-Fu-Vicic ライン」という三角測量を経て surface（Tier III）。**棄却した候補**: 1980年代の Negishi-Stille による Pd 系拡張も sp³ への paradigm-shift を成すが、Ni 系の Kumada 反応とは触媒系が異なり EP-07a の「Ni 触媒の sp³ 適用範囲」への直接充填ではないため、参考として記録するのみ。**DB-findable**: yes (Knochel 等は title に "alkyl iodide" "Ni" 等を含む).

---

#### **EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: 該当なし
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: 省略可（unfilled）
* **DOI / URL**: N/A
* **Filling timescale category**: non-applicable
* **Bibliographic verification status**: N/A
* **注記**: **C6 trigger（インセンティブ構造的未充填）** — 統計的反復測定・標準偏差報告は合成化学分野の publication norm に組み込まれていない。Table I の収率を独立に複数回測定した追試論文は、技術的には可能だが publish 動機が存在しない（新規性要件の不整合）。**Self-Tier: N/A** — 該当論文なし、unfilling pattern として記録。

---

#### **EP-09a [Internal benchmark pack]（第二群、要 Hedge）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: **直接的充填は限定的に同定**。Corriu R. J. P., Masse J. P., *J. Organomet. Chem.* **1973** または近傍年 — 元の Note Added in Proof で記録された Ni(acac)₂ 触媒系の Full Paper 展開。
* **充填確立点**: **未同定**（Kumada NiCl₂(dpe) と Corriu Ni(acac)₂ を同一基質・同一条件で直接比較した独立論文は事実上希薄）。
* **充填の性質**: Partial-to-Attempted — 両グループの後続研究で間接的 benchmark は可能だが、original head-to-head 比較は欠落のまま分野が Pd 系（Suzuki/Negishi/Stille）へ移行。
* **Bibliographic confidence**: Low — Corriu/Masse 続報は存在するはずだが、正確な書誌情報は推測ベース。
* **Filling adequacy confidence**: Low — head-to-head 比較は構造的に欠落。
* **Verification recommendation**: 必須（実質 unfilled の判定要）
* **DOI / URL**: 未推定
* **Filling timescale category**: incentive-aligned → 実質 **C7 trigger 候補**（成功による問いの抹消）
* **Bibliographic verification status**: pending
* **注記**: **C7 (success-driven question erasure) 適用候補** — 1980年代以降の Pd-cross-coupling（Suzuki, Negishi, Stille; Heck）への分野的 pivot により、Ni-ligand 設計（chelating diphosphine vs. acac）の優劣議論は社会的検証需要が消失。「Ni 触媒に bidentate phosphine が必要かどうか」という Corriu/Masse 問題は、Pd-PPh₃ や Pd-monodentate phosphine の成功で別文脈に置換された。**Self-Tier: III (deep)** — EP-09a → "head-to-head Ni(dpe) vs Ni(acac)₂" → "Corriu/Masse の続報を記憶しているか" → "実は明確には想起されない" → "field-pivot により直接比較が消えた可能性" の三段階。**棄却した候補**: Wenkert E., Michelotti E. L., Swindell C. S., *J. Am. Chem. Soc.* **1979**, *101*, 2246 — NiCl₂(dppe) を用いた aryl ether–Grignard cross-coupling の論文で著名だが、Corriu の Ni(acac)₂ 系との直接比較ではなく substrate class が異なるため EP-09a 充填には不適と判断し棄却（記憶上の誘惑が強かったが基質一致原則で除外）。**DB-findable**: uncertain — 該当する head-to-head 比較論文の title が容易に想像できない。

---

### §B 末尾チェック：Bibliographic verification

**トリガー条件評価（論文単位）：**
- (a) 1980 年以前: 該当（Tamao 1976, Yamamoto 1971, Tamao 1972 続報, Komiya 1980年代）
- (b) 著者ネットワーク密: 該当（Kumada 群 + Yamamoto 群はそれぞれ 10+ 論文系列）
- (c) Named reaction: 該当（Kumada coupling）
- (d) Bibliographic confidence Medium-Low が 2 件以上: 該当（EP-03a, EP-04a, EP-05a, EP-09a 全てが Medium-Low 含む）

→ **全候補に Verification recommendation [必須] を付与**

**Hallucination 警告（Kumada 系特異）：**
- 著者組合せの混同リスク高: "Tamao-Sumitani-Kiso-Kumada"（実在、stereochem 続報の著者列）と "Tamao-Sumitani-Kumada"（原論文の著者列）の混同。記憶ベースで「Hayashi」を含めてしまう既知エラー（memory 記録上）に注意。本出力では Hayashi を Tamao 1976 BCSJ の著者列に含めなかった（Zembayashi-Fujioka-Kodama-Nakajima-Minato は記憶ベースでの推定であり、要検証）。
- 巻号・ページ番号は推定値が混在（特に EP-04a の JACS 1972 続報、EP-09a の Corriu/Masse 続報）。
- Komiya/Yamamoto の特定論文は Organometallics 1983 と推定したが、Chem. Lett. 1978 等の早期論文も候補。

**post-hoc verification 推奨手順：**
1. Tamao 1976 BCSJ の DOI を Crossref で確認（最高優先）
2. Komiya-Yamamoto の Kumada 反応関連論文を Web of Science で著者名検索
3. Corriu/Masse の Ni(acac)₂ 続報 を J. Organomet. Chem. 1973-1975 で検索
4. Tamao 1972 続報（JACS 94 巻）の正確な page を確認

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 | EP-01a, EP-02a, EP-04a (partial), EP-05a (partial), EP-07a (halide 比較), EP-06a (partial) | VQ-2 + 部分 VQ-3 | 1976 | Med-High | High | ⚠️ verification 待機中（必須） |
| 2 | Komiya S., Yamamoto group, *Organometallics* **1983**, *2*, 1466（または近傍年の Komiya/Yamamoto 系列） | EP-03a, EP-06a | VQ-3 | 1983頃 | Low-Med | Medium | ⚠️ verification 待機中（必須） |
| 3 | Tamao K., Kiso Y., Sumitani K., Kumada M., *J. Am. Chem. Soc.* **1972**, *94*, 9268頃 | EP-04a | VQ-3 | 1972 | Low-Med | Low-Med | ⚠️ verification 待機中（必須） |
| 4 | Smith G., Kochi J. K. 系列, *J. Org. Chem.* / *J. Am. Chem. Soc.* mid-1970s | EP-05a | VQ-3 | 1975-77頃 | Low | Low-Med | ⚠️ verification 待機中（必須） |
| 5 | Devasagayaraj A., Stüdemann T., Knochel P., *Angew. Chem. Int. Ed. Engl.* **1995**, *34*, 2723 | EP-07a (sp³ 拡張) | VQ-2 (paradigm-shift) | 1995 | Medium | Medium | ⚠️ verification 待機中（必須） |
| 6 | Corriu R. J. P., Masse J. P., *J. Organomet. Chem.* **1973-74**頃の Ni(acac)₂ 続報 | EP-09a (partial / attempted) | VQ-4 | 1973-74頃 | Low | Low | ⚠️ verification 待機中（必須） |

**選定理由：**

(1) **Tamao 1976 BCSJ Full Paper を最優先**: 4-6 EP のバンドル充填により investigation 効率が最大。VQ-2 の主要 RI（RI-01）を解消し、VQ-3 への ground を提供する。Letter→Full Paper auto-resolution（C23）の典型事例として制度的な記録価値も高い。

(2) **Komiya/Yamamoto 系列を VQ-3 mechanistic 充填の核心に配置**: cis-[NiR₂(L₂)] 還元的脱離の独立的化学量論実証は、原論文の機構仮説の中核（B-2, B-14, U-1, U-4）に直接対応する。EP-03a + EP-06a を同時充填することで RI-03 と RI-06 の不可分共起（§6 で記録）を一括解決可能。

(3) **VQ-4 へは EP-07a (sp³ 拡張) と EP-09a (内部ベンチマーク) で部分到達**: ただし EP-09a は C7 (success-driven erasure) により充填が attempt 段階に留まる可能性が高く、VQ-4 完全達成は「分野が体系的に避けた問い」として §E で記録される。

(4) **EP-08a は選定リストから除外**: C6 (incentive-structural unfilling) として §E で記録。

**バンドル充填の効率性**: Tamao 1976 BCSJ 単独で 4-6 EP を部分以上の水準で充填するため、6 報の選定リストでも実質的には Kumada 系統の独立記述は 2 系列（Tamao/Kumada 自己充填 + Yamamoto 群並行充填）に集約される。これは named reaction の分野慣行（一次研究グループ + 並行する有機金属化学グループの相補）の典型である。

> ⚠️ **本選定リストの全エントリは Bibliographic verification recommendation [必須] であり、post-hoc 検証完了まで final selection として扱わない。** dev/kumada は Sonnet 67% hallucination history を持つ高警戒対象であり、Crossref/DOI 検証なしに選定リストを引用してはならない。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2 要件**:
  - EP-01a → 1976 [Tamao et al., BCSJ Full Paper] **format-driven 自己充填 (4 yr)**
  - EP-02a → 1976 [Tamao et al., BCSJ Full Paper] **format-driven 自己充填 (4 yr)**
  - EP-07a (halide 比較) → 1976 [Tamao et al., BCSJ Full Paper] **format-driven 自己充填 (4 yr)**
  - EP-07a (sp³ 拡張) → 1995 [Knochel et al.] **technical-barrier 長期遅延充填 (23 yr) + paradigm-shift**

- **VQ-3 要件**:
  - EP-03a → 1971-1983 [Yamamoto/Komiya 系列] **field-methodology 並行充填 (0-11 yr)**
  - EP-06a → 1976-1983 [Tamao 1976 + Komiya 1983 等] **field-methodology + 自己充填混合 (4-11 yr)**
  - EP-04a → 1972-1976 [Tamao 続報 + 1976 BCSJ] **format-driven 自己充填 (0-4 yr)**
  - EP-05a → 1975-77 [Kochi 系列] **field-methodology 分散応答 (3-5 yr)**

- **VQ-4 要件**:
  - EP-08a → **未充填** [C6: インセンティブ構造的未充填]
  - EP-09a → **部分充填 / 実質未充填** [C7 候補: success-driven question erasure by Pd-coupling pivot]

**階層-時間対応の評価：**

仮説「VQ階層が上がるほど充填時間が長くなる」は本ケースでは **部分的に支持される**。VQ-2 の format-driven 充填は 4 年で完了するのに対し、VQ-3 は 4-11 年、VQ-4 は事実上未充填である。ただし VQ-2 内でも EP-07a の sp³ 拡張は 23 年遅延（technical-barrier）で paradigm-shift パターンを示すため、「VQ階層 ≠ 充填難易度」の例外も存在する。VQ-4 が未充填である理由は技術的困難ではなく **インセンティブ構造**（EP-08a）と **分野的 pivot による検証需要消失**（EP-09a）であり、これは「VQ階層は科学発展の難易度ではなく、要件の精度を反映する」という解釈を支持する。

**特筆すべきパターン：**

(1) **VQ階層逆転の診断**: 未充填 EP（EP-08a, EP-09a）は VQ-4 階層に集中し、VQ-3 の機構関連 EP（EP-03a, EP-06a）は標準的時間で充填されている。これは「科学的論理に基づく EP 充填順序（低 VQ → 高 VQ）」が「出版インセンティブによる実際の充填順序」と乖離している証拠であり、§E で詳細記録する。

(2) **C23 (Letter→Full Paper auto-resolution) の遅延例**: 標準的 1-3 yr ではなく 4 yr で発火。Kumada 群の研究プログラム規模（multiple substrate classes, mechanistic investigations 同時並行）が Full Paper 統合を遅延させた可能性。

(3) **C7 (success-driven question erasure) 候補の確認**: NiCl₂(dpe) vs Ni(acac)₂ の direct head-to-head 比較が消失するパターンは、Pd-cross-coupling への分野的 pivot（1980-90 年代）により発生した。Kumada 反応そのものの応用は continuing だが、original の Ni-ligand-design 議論は別文脈に置換された。

(4) **長期遅延充填**: EP-07a の sp³ 拡張（Knochel 1995, 23 yr）は technical-barrier の典型例。「sp² halides only」境界の超越は、新触媒系（Ni/amine, low-valent Ni species 等）の発展を要し、original Kumada 系の枠組み内では充填されなかった。

(5) **著者回顧との照合**: Tamao 自身による retrospective review（Tamao K., *J. Organomet. Chem.* **2002**, *653*, 23 — "A new era of organosilicon chemistry") において、Kumada 反応の 30 年回顧で「selectivity の数値的根拠の不在」「homo-coupling 副生量の系統的測定の不在」が言及されているかは要確認（Tamao 2002 retrospective が ep/discussion フォルダに存在するため、別途参照可能）。原著者が回顧で認識した EP と認識しなかった EP の差は、「分野内部者には不可視の構造的不在」の直接的証拠として記録できる候補。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

#### EP-08a [Replication / uncertainty pack]:

* **未充填の理由**: **インセンティブ構造の不整合（C6）** — Table I 収率の独立追試・反復測定・標準偏差報告は技術的に可能だが、新規性を要求する合成化学の publication norm の下で独立論文として出版する動機が存在しない。Kumada 反応の 54 年の歴史において、原論文の Table I 収率を独立に N=3 以上の反復で再測定した報告は事実上見当たらない。
* **発見的意義**: **あり** — 「合成化学は実用性検証としての追試を組織的に蓄積しない」という分野構造を示す典型事例。"selective" "high-yielding" 主張は post-publication で系統的に検証されず、後続研究は「動く」前提で応用に進む。これは UQS が抽出した構造的不在が、**学術コミュニティ全体の制度的選好**によって維持されているという知見を提供する。
* **将来の充填可能性**: **低** — 出版インセンティブが変わらない限り構造的に未充填。例外: 機械学習/データベース駆動の収率予測モデルの validation 文脈で部分的に統計的検証が行われる可能性（2020 年代以降の trend）。

#### EP-09a [Internal benchmark pack]:

* **未充填の理由**: **成功による問いの抹消候補（C7）** — NiCl₂(dpe) vs Ni(acac)₂ の direct head-to-head 比較は、1980 年代以降の Pd-cross-coupling（Suzuki, Negishi, Stille, Heck, Hartwig-Buchwald amination）への分野的 pivot により検証需要が部分的に消失。Ni-ligand 設計の優劣議論は別 metal（Pd, Cu, Fe）の文脈で再展開され、Original Corriu/Masse 問題（chelating diphosphine が必須か）は孤立した histroical question として残された。
* **発見的意義**: **あり** — 「分野の方法論的 pivot により、原論文の中核仮説（cis-geometry requirement）の直接検証需要が消失する」という C7 パターンの典型事例。Kumada 反応は 1972 年に提案された Ni-ligand 設計原理が完全には決着しないまま、Pd 系の成功により背景化された。これは「Methodology の充填は技術的可能性ではなく社会的需要で決まる」という構造的観察を補強する。
* **将来の充填可能性**: **中** — 近年（2020 年代）の earth-abundant metal catalysis の再興により、Ni-ligand 設計の系統的再検討が部分的に行われている。Kumada 反応そのものの ligand benchmark ではないが、関連する Ni/biaryl coupling の ligand 比較として間接的充填が進む可能性。

---

## 付録：Retrieval Depth Annotation Matrix

> 本付録はユーザー指示「retrieval depth annotation を必ず含めてください」への直接応答として、§B 各 EP の Self-Tier・推論経路・DB-findability を統合表として再掲する。

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? |
|---------|--------|-----------|----------|--------------|
| Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 | EP-01a | **I** (immediate) | EP-01a → "Communication 形式の Letter→Full Paper auto-resolution (C23 trigger)" → "Kumada 群の standard Full Paper が 1976 BCSJ" の単一連想で即想起 | **yes** — title に "Nickel-Phosphine" "Cross-Coupling" "Grignard" を含む見込み |
| Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958（同上） | EP-02a | **I** (immediate) | EP-01a と同一論文として一括想起 | yes（同上） |
| Tamao K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958（同上） | EP-07a (halide 比較) | **I** (immediate) | EP-01a と同一論文の scope-extension subsection として一括想起 | yes（同上） |
| Komiya S., Abe Y., Yamamoto A., Yamamoto T., *Organometallics* **1983**, *2*, 1466（推定） | EP-03a, EP-06a | **II** (associative) | EP-03a → "diorganonickel intermediate 観測は誰がやっていたか" → "1970-80年代の Akio Yamamoto group" → "Komiya as reductive elimination kinetics author" の 3 段階連想 | **yes** — title に "diorganonickel" "reductive elimination" "diphosphine" を含む見込み |
| Tamao K., Kiso Y., Sumitani K., Kumada M., *J. Am. Chem. Soc.* **1972**, *94*, ~9268（推定） | EP-04a | **II→III** | EP-04a → "Kumada 群は cis/trans selectivity の続報を出したか" → 続報の存在は想起できるが正確な書誌情報は弱い → 巻号・ページは triangulation 必要 | **uncertain** — title に "stereochemistry" or "vinyl halide" を含むかは不明 |
| Smith G., Kochi J. K. 系列, mid-1970s（特定論文未確定） | EP-05a | **II→III** | EP-05a → "selectivity 数値裏付け、R–R quantification" → "Kochi group as radical/cross-coupling mechanism authority" → "Smith-Kochi の Ni 関連論文 1975-1977 範囲" の triangulation | uncertain — Kochi の Ni 系特定論文の title は記憶薄い |
| Devasagayaraj A., Stüdemann T., Knochel P., *Angew. Chem. Int. Ed. Engl.* **1995**, *34*, 2723（推定） | EP-07a (sp³ 拡張) | **III** (deep) | EP-07a → "sp³ alkyl halide cross-coupling, Ni 系で誰がブレイクスルーしたか" → "Knochel group が 1990 年代に, Vicic/Fu が 2000 年代に拡張" → 複数候補から最早期の Knochel を選択 | **yes** — title に "alkyl halide" "nickel" を含む見込み |
| Corriu R. J. P., Masse J. P., *J. Organomet. Chem.* **1973-74**頃 Ni(acac)₂ 続報（特定論文未確定） | EP-09a | **III** (deep) | EP-09a → "Ni(dpe) vs Ni(acac)₂ head-to-head" → "Corriu/Masse の続報を記憶しているか" → "明確には想起されない" → "field-pivot により直接比較が消失した可能性" の三段階推論 | **uncertain → likely no** — head-to-head 比較を主題とした論文の存在自体が疑わしい |
| **EP-08a 該当論文なし** | EP-08a | **N/A** (unfilled, C6) | 想起不可 — incentive-structural にそもそも論文化されない | N/A |

---

## 付録 B: Retrieval Externalization Notes（思考過程の記録）

> ユーザー指示「思考過程を可能な限り externalize してください。どの候補がいつ最初に思い浮かんだか、どの候補を考えて棄却したか、明示的に記述すること」への応答。

### 最初の連想（EP プロンプト読み込み直後）

EP-01a を読んだ瞬間に **「Tamao の BCSJ 1976 Full Paper」** が単一の dominant 候補として surface した。これは "named reaction の Letter→Full Paper standard auto-resolution" という強い anchor pattern によるもので、Tier I の典型例である。同時に EP-02a, EP-04a, EP-05a, EP-06a, EP-07a の一部も「同一論文がバンドル充填する」という形で副次的に想起された。

EP-03a を読んだ時点では **Yamamoto group の diorganonickel observation** が浮かんだが、特定の Komiya 論文（Organometallics 1983 など）は二次的な候補として、複数の中から triangulation を要した。Tier II の典型。

EP-09a は最も困難で、**Corriu/Masse の続報**を即想起したが、その続報での Ni(acac)₂ vs NiCl₂(dpe) の head-to-head 比較が実際に行われたかについては記憶が薄く、「実際には行われなかった可能性」という棄却推論を経て Tier III + C7 候補に落ち着いた。

### 棄却した候補（明示的記録）

1. **Wenkert E., Michelotti E. L., Swindell C. S., *J. Am. Chem. Soc.* 1979, 101, 2246** — NiCl₂(dppe) を用いた aryl ether-Grignard cross-coupling として記憶上の dominant な「Kumada 系のメカニズム関連高引用論文」。EP-09a (NiCl₂(dpe) vs Ni(acac)₂) の充填候補として最初に浮かんだが、**基質クラスが異なる**（aryl ether vs aryl chloride）ため Corriu の Ni(acac)₂ 系との直接比較ではないと判断し棄却。**判断のキー**: EP の case-specific 実装（"PhCl + EtMgBr 等の同一基質で両触媒系を直接比較する"）との対応関係を厳密に適用。

2. **Negishi review series (Acc. Chem. Res. 1982, JOMC reviews)** — Ni/Pd cross-coupling の standard review として記憶上の dominant。Stage 4 v6 prompt の「レビュー論文は EP を充填しない」原則に従い棄却。

3. **Hartwig 教科書 "Organotransition Metal Chemistry"** — 標準的二次資料として参照可能だが、EP 充填の独立証拠は提供しないため棄却。

4. **Kochi 1978 monograph "Organometallic Mechanisms and Catalysis"** — Kochi の機構研究の集大成だが monograph であり independent research paper ではないため EP-05a 充填の primary candidate からは棄却（Smith-Kochi の独立論文を優先）。

5. **Vicic D. A. グループの Ni(I)/Ni(III) 機構論文（2000 年代後半）** — EP-03a の modern mechanistic completion 候補として一瞬考慮したが、これは **Kumada 反応そのもの**ではなく **sp³-sp³ Negishi-type Ni coupling** の文脈であり、original Kumada 1972 の機構（sp²-sp³ 系）とは context が異なるため棄却（参考としてのみ記録）。

6. **Hayashi T., Konishi M., Kumada M. 系列（asymmetric Kumada, 1979-1982）** — selectivity 拡張として強く想起されたが、これは **stereochemistry of asymmetric induction** であり EP-04a (cis/trans kinetic vs thermodynamic) の充填とは焦点が異なるため棄却。

### 自己診断: どの候補が hallucination リスクが高いか

- **最高警戒**: EP-04a の Tamao 1972 続報（JACS 94 巻の正確な page）— 続報の存在は強く確信するが、page number と stereochem-focused であるか scope-focused であるかの記憶は弱い。
- **高警戒**: EP-03a/EP-06a の Komiya 1983 Organometallics 2/1466 — 具体的書誌情報は推定値。
- **高警戒**: Tamao 1976 BCSJ の **author full list** — Zembayashi-Fujioka-Kodama-Nakajima-Minato は記憶ベースの推定であり、実際にはこれより少ない/多い可能性。memory 記録「Tamao-Sumitani-Hayashi-Kumada は実在せず実在は Tamao-Sumitani-Kiso-Kumada」を踏まえ、Hayashi を意図的に除外した。
- **中警戒**: EP-05a の Smith-Kochi の特定論文 — 著者組合せは確実だが、Ni 文脈と Ag/Cu 文脈の混同リスクあり。

---

```
inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
