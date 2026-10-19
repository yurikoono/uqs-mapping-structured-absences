```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

C23トリガー確認：本論文はJACS Communication（BIB-7: communication）であり、C23（Letter→Full Paper auto-resolution）が発火条件を満たす。

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a, EP-07a

- **EP-03a** (Direct-observation / state-assignment pack, RI-03): Ni(dpe)系のジオルガノニッケル中間体の直接観測は、有機金属化学の主流的研究テーマとして独立論文化されやすく、σ-オルガノニッケル錯体合成・分光観測を専門に扱う複数の研究グループの論文を検索語から直接追跡できる。
- **EP-06a** (Analogy-validation pack, RI-06): dipy-Ni系から輸入した触媒サイクル各素反応（酸化的付加、トランスメタル化、還元的脱離）の化学量論的検証は、機構研究の独立した論文主題として継続的に発表されており、文献検索で直接追跡可能。
- **EP-07a** (Boundary-test pack, RI-07): sp²制限の実験的根拠（sp³ハライドの不活性確認）およびPhCl/PhBr/PhIの反応性比較は、Kumada反応のスコープ拡張研究として独立論文化された明確な候補が存在する。

**第二群（間接的に追跡可能）：** EP-01a, EP-02a, EP-04a, EP-05a, EP-09a

- **EP-01a** (Reporting-coherence pack, RI-01): C23該当——JACS Communication → Bull. Chem. Soc. Jpn. Full Paper遷移（1976）が確認されており、glpc条件・反応時間・収率計算基準の統一記述はLetter→Full Paper自動解消として追跡可能。独立論文の主題ではなく、Full Paper展開での自動解消として間接的に追跡する。
- **EP-02a** (Identity/purity substantiation pack, RI-02): C23該当——EP-01aと同一のFull Paper展開によって個別エントリの分光データ記載が自動解消される可能性。独立論文としての充填ではなくFull Paper経由での間接的追跡。
- **EP-04a** (Discrimination / replication pack, RI-04): cis/trans-スチルベン比の速度論/熱力学制御の区別は、Full Paperの1部節またはKumada反応の立体化学を専門に扱った続報論文で部分的に対処されているが、独立した主題として単独論文化された可能性は中程度。
- **EP-05a** (Quantitative-ranking substantiation pack, RI-05): クロスカップリング選択性の定量的質量収支（ホモカップリング・β-脱離副生物の定量）はFull Paper（1976）に部分的に含まれる可能性があるほか、触媒設計論文（配位子効果研究）での副次的データとして間接的に追跡可能。
- **EP-09a** (Internal benchmark pack, RI-09): NiCl₂(dpe)とNi(acac)₂の同一基質・条件での直接比較は、両系を体系的に取り扱ったレビューや体系的リガンド比較論文として間接的に追跡可能だが、単独論文での直接比較は限定的。

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a** (Replication / uncertainty pack, RI-08): インセンティブ構造的未充填——合成化学分野では「既存反応の収率の統計的再現性評価」という内容の独立論文化は1970年代から現在まで出版インセンティブの不整合により慣例的に行われない。技術的には可能だが、新規性を要求する出版慣行の下で独立論文として発表されることは期待できない。

---

### §B 各EPの充填論文候補

**§B Bibliographic verification check（全候補）**

トリガー条件：
(a) 論文年代が古い（1980年以前）→ YES（主要候補のほぼ全てが1970年代）
(b) 著者ネットワークが密（Kumada/Tamaoグループから10+の関連論文）→ YES
(c) 反応名がauthor nameに由来（Kumada coupling, Kumada-Corriu coupling）→ YES
(d) Medium-Low Bibliographic confidence候補が2件以上 → YES

判定：全候補に **Verification recommendation: [必須]**

---

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — 原論文の通信→Full Paper遷移として、glpc条件・反応時間・収率計算基準の統一記述を含む詳細な実験条件が提供されたと推定される。
* **充填確立点**: 同上
* **充填の性質**: Partial（Full Paperへの展開により形式的欠落は解消されるが、EP-01aが問うTable I全11エントリの同一条件での比較可能な収率データが揃ったかどうかは要検証）
* **Bibliographic confidence**: Medium（雑誌・年・巻号について高い確信；著者リストの順序・ページ範囲は参照による確認が必要）
* **Filling adequacy confidence**: Medium（Full Paperが通信の欠落を補う構造は典型的だが、11エントリ全てを同一glpc条件で測定し直したかは不明）
* **Verification recommendation**: [必須]（(a)(b)(c)全条件該当）
* **Bibliographic verification status**: pending
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```
* **注記**: 発表から約4年後（1976）の全文論文展開。Stage 3 §5の「通信→Full Paper遷移の自動解消パターン（§6 item 5）」として記録済みの事例と対応。Layer 1（合成実用性層）の充填として機能する。

---

**EP-02a [Identity/purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Insufficient identity verification]（Stage 3 VQ-1でnon-fatalとして残存）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — EP-01aと同一のFull Paperにおいて、Table I各エントリの個別分光データ（¹H NMR, IR, MS）が記載されたと推定される。
* **充填確立点**: 同上
* **充填の性質**: Partial（"and/or"構文への対処としての分光データ記載を含むと推定されるが、全エントリの完全な構造確認データが揃ったかは要確認）
* **Bibliographic confidence**: Medium（EP-01aと同一書誌）
* **Filling adequacy confidence**: Medium（Full Paperが"and/or"問題を解消するとは限らない）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```
* **注記**: EP-01aとのバンドル充填候補。同一Full Paperが両EPを部分的に充填する可能性が高い。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

充填するRI: RI-03 [Unobserved explanatory] ——NiCl₂(dpe)系でのジオルガノニッケル中間体（中間体1）の直接観測

* **充填開始点（候補1）**: Morrell, D. G.; Kochi, J. K. J. Am. Chem. Soc. 1975, 97, 7262–7270 — アルキルニッケル錯体の調製・特性評価とそのハライドとの反応機構を報告した初期のσ-オルガノニッケル研究；本論文で提案された中間体1（ジアルキルニッケル(II)(dpe)）に対応する化合物クラスの独立的な合成・分光観測の先行事例を提供。
* **充填確立点（候補1）**: 同上（アルキルニッケル中間体の形成に関する部分的充填）
* **充填開始点（候補2）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — Full Paperにおいて触媒前駆体とGrignard試薬との化学量論的反応条件が記述されていれば、中間体1の形成確認（低温NMRまたは単離）が部分的に含まれる可能性。
* **充填確立点（候補2）**: 未同定（Full Paperで中間体直接観測が主題化されたかは不明）
* **充填開始点（候補3）**: Tsou, T. T.; Kochi, J. K. J. Am. Chem. Soc. 1979, 101, 7547–7560 — Ni(0)複合体へのアリールハライド酸化的付加の機構研究；中間体2（(ハロ)(オルガノ)ニッケル錯体）に相当するNi(II)錯体の形成と特性評価を含む可能性。
* **充填確立点（候補3）**: 同上（酸化的付加段階の充填として機能する可能性）
* **充填の性質**: Partial（いずれの候補も対象系（NiCl₂(dpe)系）での中間体1〜3の全段階に対する直接観測ではなく、特定素反応段階の部分的充填）
* **Bibliographic confidence**: Medium（Morrell & Kochi 1975; Tsou & Kochi 1979 ——著者名・雑誌・概算年については確信があるが、正確な巻号ページは要検証）
* **Filling adequacy confidence**: Medium（論文内容がcase-specific実装の要件——特にNiCl₂(dpe)系で中間体1を低温³¹P{¹H} NMRで観測する——に直接対応するかは内容確認が必要）
* **Verification recommendation**: [必須]（(a)(b)(c)(d)全条件該当）
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (7 yr for Kochi 1979 candidate)
* **注記**: Stage 3 §6「RI-06+RI-03の不可分共起パターン」が指摘する通り、EP-03a（RI-03）はEP-06a（RI-06）と独立に解消される必要がある。EP-03aの完全充填のためには、NiCl₂(dpe)系での素反応各段階を経路上の独立した化学量論的実験で実証する必要があり、充填開始点と充填確立点が異なる論文になる典型的な分割パターンと予想される。

---

**EP-04a [Discrimination / replication pack]（第二群）**

充填するRI: RI-04 [Unreplicated discriminator] ——cis/trans-スチルベン比の速度論vs熱力学制御の区別および定量GLC反復測定

* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — Full Paperに立体化学の詳細検討（cis/trans比の反応時間・温度依存性）が含まれている可能性がある。
* **充填確立点**: 未同定（Full Paperの内容が速度論/熱力学制御の区別実験まで含むかどうかは現時点で確認できない。含まない場合、別途充填論文が必要）
* **充填の性質**: Partial（Full Paperでは反復測定条件の改善は期待されるが、速度論/熱力学制御の明示的な区別実験は独立した研究課題として別論文が必要な可能性）
* **Bibliographic confidence**: Medium（候補論文はEP-01aと同一書誌）
* **Filling adequacy confidence**: Low（cis/trans比の時間・温度系列実験がFull Paperの主要テーマの一つとして扱われたかどうかを判断する直接証拠なし）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（もしFull Paperで解消されるなら）
* **注記**: Stage 3 §2 SRG-6の注記では、cis/trans比の観察はVQ-1の範囲に留まり、機構的解釈のための証拠基盤は未整備とされている。EP-04aがFull Paperで充填されない場合、この問いはD4-5（選択性の速度論/熱力学的性格）として、Kumada反応の機構研究が進んだ1980年代以降まで未充填として残った可能性がある。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

充填するRI: RI-05 [Qualitative overread] ——「選択的クロスカップリング」という主張の定量的質量収支（クロスカップリング vs. ホモカップリング vs. β-脱離）

* **充填開始点（候補1）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — Full Paperにおいて、代表的基質でのホモカップリング生成物（R–R）・β-脱離生成物の定量的GC-MS分析が含まれていれば部分的充填。
* **充填確立点（候補1）**: 未同定（Full Paperの質量収支データの記述範囲不明）
* **充填開始点（候補2）**: Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. J. Am. Chem. Soc. 1976, 98, 3718–3719 — キラルフェロセニルホスフィン-Ni触媒を用いた不斉クロスカップリングにおける不斉誘起とともに、反応混合物の選択性評価データを含む可能性がある（副生成物の定量を間接的に含む可能性）。
* **充填の性質**: Partial（いずれの候補もEP-05aのcase-specific実装——n-BuMgBr + PhClの反応混合物のGC-MS分析による完全質量収支——を直接の主題とした論文ではないため、選択性の定量データが副次的情報として含まれる可能性）
* **Bibliographic confidence**: Medium（Hayashi et al. JACS 1976, 98, 3718——著者名・雑誌については確信；巻号ページは要確認）
* **Filling adequacy confidence**: Low（選択性の定量的評価がcase-specificな実装レベルで実施されたかどうかは論文内容の直接確認なしには判定できない）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（もしFull Paperで解消されるなら）; incentive-aligned（別途機構論文で充填されるなら3-5 yr）
* **注記**: Stage 3 §2 SRG-2のERが明示する通り、質量収支データを含む充填論文の不在はSRG-2（選択性主張とホモカップリング生成物データの自己矛盾的不在）の構造的問題と連動する。EP-05aが充填されるまでの間、D4-1（選択性主張の定量的根拠の不在）はKumada反応の「機能することは分かるが選択性の起源は不明」という状態として科学史的に継続する。

---

**EP-06a [Analogy-validation pack]（第一群）**

充填するRI: RI-06 [Imported model] ——dipy-Ni系から輸入した触媒サイクル（eqs 2-4）の、NiCl₂(dpe)系での化学量論的素反応の実証

* **充填開始点（候補1）**: Tsou, T. T.; Kochi, J. K. J. Am. Chem. Soc. 1979, 101, 7547–7560 — Ni(0)錯体とアリールハライドの酸化的付加機構の系統的研究；eq (2)（Ni(0) + R'X → (ハロ)(オルガノ)Ni(II)）に対応する素反応を、phosphine配位子を持つNi(0)系で実証した可能性がある。
* **充填確立点（候補1）**: 同上（酸化的付加段階に関しては充填確立点として機能する可能性）
* **充填開始点（候補2）**: Morrell, D. G.; Kochi, J. K. J. Am. Chem. Soc. 1975, 97, 7262–7270 — アルキルニッケル錯体（eq (3)の産物に相当するR–R生成に関連する化学）の調製・特性評価；eq (3)（(ハロ)(オルガノ)Ni(II) + RMgX → R–R + Ni(0) regeneration）の類似素反応の部分的実証となる可能性。
* **充填の性質**: Partial（ep-06aのcase-specific実装——(i) NiCl₂(dpe)系でeq (2)を化学量論的に実証、(ii) 独立合成した[Ni(n-Bu)₂(dpe)]のPhClとの反応でeq (3)のR–R生成を確認——の完全な充填は、単一の独立論文ではなく複数論文による段階的な充填として達成されたと推定される）
* **Bibliographic confidence**: Medium（Tsou & Kochi 1979——著者名・雑誌・年については確信；正確なページ範囲は要検証）
* **Filling adequacy confidence**: Medium（論文がphosphine-Ni(0)系での酸化的付加の化学量論的実証を含むとしても、NiCl₂(dpe)の特定系で全素反応を網羅するかどうかは不明）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (7 yr for Kochi 1979 candidate; Stage 3 §6が指摘するRI-06+RI-03の不可分共起を考慮すると、完全充填はさらに遅延する可能性)
* **注記**: Stage 3 §6「RI-06サイクルレベル輸入の代表事例」として記録済み。dipy-Ni（N配位子）とdpe-Ni（P配位子）の電子的差異（Codebook v0.2スコープ注記）を考慮すると、EP-06aの完全充填にはdpe-Ni系での独立した化学量論的実証が不可欠であり、他系からの類推充填（Indirect）は受け入れられない。EP-06aはEP-03aとの共起問題（Stage 3 §6 item 6）のため、完全充填には両EPの解消が必要。

---

**EP-07a [Boundary-test pack]（第一群）**

充填するRI: RI-07 [Unsupported boundary] ——「sp²ハライドのみ使用可能」という境界主張の実験的根拠（sp³ハライド不活性確認）および塩化物の反応性の定量的比較

* **充填開始点（候補1）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — Full Paper（副題: "General Scope and Limitations"を含む可能性）においてsp³ハライドの不活性確認実験と、PhCl/PhBr/PhIの反応性比較データが記述されることが期待される。
* **充填確立点（候補1）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 — 副題が示すスコープと制限の系統的評価がEP-07aのcase-specific実装の主要部分を満たすと推定（確認待ち）。
* **充填の性質**: Partial（Full Paperがsp²/sp³境界の実験的確認を含む場合でも、速度論的根拠（氧化付加段階の速度比較）までは対象外の可能性）
* **充填候補2（sp³ハライドの機構的根拠）**: Tsou, T. T.; Kochi, J. K. J. Am. Chem. Soc. 1979, 101, 7547–7560 — sp² vs sp³ハライドの酸化的付加速度の差を機構的に説明する可能性がある。
* **Bibliographic confidence**: Medium（候補1はEP-01aと同一書誌で確信度は同様；候補2は著者名・年については確信、正確なページは要検証）
* **Filling adequacy confidence**: Medium（Full Paperが「スコープと制限」を体系的に扱っていれば高い充填可能性；sp²/sp³境界の速度論的説明は別途機構論文が必要）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（1976 Full Paper経由での解消なら4 yr）; field-methodology（機構的根拠まで充填するなら7-10 yr）
* **注記**: Stage 3 §2 SRG-4のRIコード（RI-07拡張適用）が指摘する「制限を肯定的特徴に再フレーム」という構造（§6 item 2）により、sp²制限の実験的根拠不在は「発見」として記録されているが、実際にはFull Paper展開で部分的に解消された典型的なformat-driven自動解消候補。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填論文候補**: **未同定**
* **未同定の理由**: 合成化学分野では収率データの統計的再現性評価（複数独立試行の標準偏差報告）を主題とした独立論文は1970年代から現在まで慣例的に発表されない。EP-08aのcase-specific実装（Table Iの3-5エントリを3回以上独立に繰り返し標準偏差を報告）は、技術的には可能だが新規性を要求する出版慣行の下で論文化されない典型的なインセンティブ構造的未充填パターンに該当する。
```yaml
incentive_structure_type: "incentive-structural unfilling"
filling_substitute: "全合成・応用論文での同一反応の再現（副次的充填）が最大限の代替"
```
* **Bibliographic confidence**: N/A（充填論文が存在しないと判定）
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: [省略可]（充填論文自体が存在しない）
* **Filling timescale category**: non-applicable
* **注記**: 合成化学分野でEP-08a型の充填が起こるとすれば、Kumada反応の信頼性を主題とするメタアナリシス（現代のsystematic reviewに相当）の中でのみ現れる可能性があるが、1972年当時の問いに遡及して充填する動機は発生しない。

---

**EP-09a [Internal benchmark pack]（第二群）**

充填するRI: RI-09 [External superiority] ——NiCl₂(dpe)とNi(acac)₂の同一基質・同一条件での直接比較（Corriu/Masse問題, D4-8対応）

* **充填開始点（候補）**: Corriu, R. J. P.; Masse, J. P.; 後続全文論文（同グループ、1972年以降推定）——Ni(acac)₂系の詳細な基質スコープ・選択性データが記述されれば、対象論文のNiCl₂(dpe)との間接的比較が可能になる。ただし同一基質・同一条件での**直接比較**を主題とした単独論文は未同定。
* **充填確立点**: 未同定（直接比較実験を主題とした単独論文の存在が確認できない。1970年代-1980年代のレビュー論文（例: Kumada, M. Pure Appl. Chem. 1980, 52, 669）において、複数のNi系の反応性がまとめて記述された場合に間接的充填として機能する可能性があるが、レビューは充填論文に該当しない）。
* **充填の性質**: Indirect（Corriu後続グループ論文がNi(acac)₂の詳細データを独立に提供しており、研究者がNiCl₂(dpe)の本論文データと個別に比較できるとしても、単一論文内での直接比較実験という意味でのEP-09a充填は達成されていない可能性が高い）
* **Bibliographic confidence**: Low（Corriu後続全文論文の正確な書誌は未特定；Kumada 1980レビューは著者名・年について確信があるが充填として機能しない）
* **Filling adequacy confidence**: Low（直接比較実験の単独論文化が達成されたかどうかの証拠なし）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: non-applicable（直接比較論文が存在しない場合）; field-methodology（間接的充填なら10-20+ yr、成熟したNi触媒レビューが出た1980年代以降）
* **注記**: Stage 3 §2 CLA-1の注記が指摘する通り、「Note Added in Proofが記録したがNi(acac)₂との比較が欠落したCorriu/Masse問題」はNC-4（配位子設計原理）の独自性評価において最重要の未解決問いである。Pd触媒クロスカップリング（鈴木、薗頭、根岸）の展開がNiキレートリガンドの「必要条件」問題の検証需要を間接的に（別パラダイムで）回答した可能性があるが、これはParadigm-shift型のEP処理であり直接充填には該当しない。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao et al., Bull. Chem. Soc. Jpn. 1976, 49, 1958–1976 | EP-01a, EP-02a, EP-05a (部分), EP-07a (部分) | VQ-2 | 1976 | Medium | Medium | 必須 ⚠️ pending |
| 2 | Morrell, D. G.; Kochi, J. K. J. Am. Chem. Soc. 1975, 97, 7262–7270 | EP-03a (部分), EP-06a (部分) | VQ-3 | 1975 | Medium | Medium | 必須 ⚠️ pending |
| 3 | Tsou, T. T.; Kochi, J. K. J. Am. Chem. Soc. 1979, 101, 7547–7560 | EP-06a (酸化的付加段階), EP-07a (機構的根拠) | VQ-3 | 1979 | Medium | Medium | 必須 ⚠️ pending |
| 4 | Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. J. Am. Chem. Soc. 1976, 98, 3718–3719 | EP-05a (部分), EP-07a (スコープ拡張) | VQ-2 | 1976 | Medium | Low | 必須 ⚠️ pending |
| 5 | Corriu, R. J. P.; Masse, J. P. J. Chem. Soc. Chem. Commun. 1972, 144 | EP-09a (間接) | VQ-2 (間接) | 1972 | High | Low | 必須 ⚠️ pending |

**選定理由：**

5報の選定は以下の設計原則による。第1位はバンドル充填の効率性が最大であり、EP-01a/EP-02a（VQ-2, format-driven）を中心として複数のEPを同時に部分充填する最重要論文として選定した。C23（Letter→Full Paper auto-resolution）の典型事例として、Kumada反応の通信→Full Paper遷移を実証する核心論文である。第2・3位はVQ-3要件（RI-03, RI-06）の充填候補として、Kochi研究グループによる機構研究論文を選定した。これらはBibliographic confidenceがMediumであり、要検証だが、Stage 3 §6のRI-06+RI-03不可分共起パターンを解消する方向での独立研究として最も可能性が高い。第4位は不斉誘起実験を通じてKumada反応のスコープと選択性評価（EP-05a, EP-07a）に貢献する可能性のある、Tamaoグループ自身による同年論文として選定した。第5位はEP-09a（NiCl₂(dpe) vs Ni(acac)₂比較）の唯一の既知基準点として原論文のNote Added in Proofで言及されたCorriu/Masse論文を選定した（Bibliographic confidence Highだが、充填としてはIndirectかつFilling adequacy Low）。

全候補が[必須]検証対象（Kumada coupling命名規則、著者ネットワーク密度、1980年以前の年代）に該当するため、最終選定は bibliographic verification 完了後に正式確定する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件 (RI-01, RI-02 → EP-01a, EP-02a): 1976年 [Tamao et al., Bull. Chem. Soc. Jpn.] [自己充填 / format-driven auto-resolution] — 約4年後に原著者グループ自身がFull Paperを発表し、通信形式の分析的欠落（glpc条件、反応時間、個別分光データ）を自動解消。
- VQ-2 要件 (RI-07 → EP-07a): 1976年 [Tamao et al., Bull. Chem. Soc. Jpn.] [自己充填 / format-driven auto-resolution] — 同Full Paperがスコープ・制限を体系化した場合（⚠️ verification待機中）、sp²/sp³境界の実験的根拠は4年後に充填。
- VQ-3 要件 (RI-06 → EP-06a, 酸化的付加段階): 1975–1979年 [Morrell-Kochi 1975 / Tsou-Kochi 1979] [分野横断充填 — 機構化学グループによる独立解消] — 3–7年後に異なる研究グループ（Kochi研）による機構研究として部分的充填。
- VQ-3 要件 (RI-03 → EP-03a, 中間体直接観測): 1975–1979年 [Morrell-Kochi 1975 / Tsou-Kochi 1979] [分野横断充填] — 上記と同時期、部分的充填。完全充填（dpe-Ni系での全中間体の低温NMR観測）は20年以上を要した可能性。
- VQ-3 要件 (RI-05 → EP-05a, 選択性定量): 1976年以降（未確定）[自己充填候補 / 分野横断充填候補] — 充填確立点が特定できず。
- VQ-3 要件 (RI-04 → EP-04a, cis/trans速度論): 1976年以降（未確定）[自己充填候補] — 充填確立点が特定できず。VQ-4 要件 (RI-08 → EP-08a): 未充填（インセンティブ構造的未充填、永続）。
- VQ-4 要件 (RI-09 → EP-09a): 1972年以降（未確定）[間接的充填のみ確認] — 直接比較論文は未同定。

**階層-時間対応の評価：**

本論文において、VQ-2要件（EP-01a, EP-02a, EP-07a）の充填は概ね1976年（約4年後）に原著者グループ自身によるLetter→Full Paper遷移という形で最初に達成されており、format-drivenな自動解消パターンとして機能している。VQ-3要件（EP-03a, EP-06a）の充填は1975–1979年の範囲でKochi研究グループによる独立した機構研究として達成されており（部分充填）、VQ-2充填よりやや遅延したパターンが観察される。VQ-4要件のEP-08a（統計的再現性）は永続的に未充填であり、EP-09a（直接ベンチマーク比較）は直接充填論文が確認できない。この結果は「VQ階層が上がるほど充填に要する時間が長くなる」という仮説を大局的に支持するが、EP-03a（VQ-3要件）の充填が一部Kochi 1975論文（VQ-2要件の充填より早い1975年）で先行した可能性があり、階層間の厳密な時間的順序性は反例を持つ。

**特筆すべきパターン：**

1. **自己充填 + format-driven auto-resolution（バンドル充填）**: 第1位選定論文（Tamao et al. 1976 BCSJ）が複数のVQ-2要件EP（EP-01a, EP-02a, EP-07a）を一括で自己充填するパターン。Letter→Full Paper遷移という通信形式の制度的特性が自動充填機構として機能している。

2. **分野横断充填（異なる研究グループ）**: VQ-3要件（EP-03a, EP-06a）の部分的充填をKochi研究グループが独立に実施したと推定される。原著者グループによる機構研究よりも、機構化学を専門とする別グループが先行充填した構造は、「合成化学コミュニティが機構的問いを別研究者グループに委託する」という分業構造を示唆する。

3. **未充填EP（VQ逆転）**: EP-08a（RI-08, 統計的信頼性）は最も低次のVQ要件（VQ-4の一部）に関連しながら永続的に未充填である。より高次のVQ要件（VQ-3: RI-03, RI-06）の充填が機構研究コミュニティの関心を集め進展した一方で、低次要件（反復測定・収率の不確かさ評価）が未充填のまま残るというVQ階層の逆転パターンが観察される。これは「出版インセンティブ（機構的新発見優先）が科学的論理（低VQ→高VQ充填の順序）と逆行して分野のインセンティブ構造的不在を維持している」という記録的事例として解釈できる。

4. **D4-8（Corriu/Masse問題）の長期未充填**: Note Added in Proofに記録されながら比較されなかったNi(acac)₂との比較（EP-09a）は、Pd触媒クロスカップリングの革命的展開（1975年以降、Heck, Suzuki, Negishi等）によって「Niキレートリガンドが必要条件かどうか」という問いの検証需要が**成功による問いの抹消（パラダイム転換充填）**として消滅した可能性がある。Pd触媒での汎用的クロスカップリングの確立により、「Ni(dpe)が特別に優れているか」というUQSが検出した問いは実用上意味をなさなくなった——これは分野が問いを解決した（充填）のではなく、問いの前提が変わったことで問い自体が無意味化したパターンである。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造の不整合——合成化学分野では独立した反復実験による収率の統計的評価（標準偏差報告）は独立論文として出版されるインセンティブがなく、技術的に可能であっても慣例的に実施されない。1970年代から現在まで、この慣行は本質的に変化していない。
* **発見的意義**: あり——「収率データの統計的信頼性評価は合成化学が体系的に避けてきた問い」として記録できる。Kumada反応が「76–98%収率」と記述され数十年にわたって参照されてきた一方で、この収率数値の再現性（特にTable Iの最適化非保証エントリ）は一度も統計的に評価されていない可能性が高い。再現性危機（replication crisis）が有機合成化学に及んだ2015年以降でも、個別反応の収率分布の統計的評価は独立論文として発表されていない——これはUQSが検出した「分野が構造的に回避してきた問い」の典型事例として記録する価値がある。
* **将来の充填可能性**: 低——出版インセンティブの不整合という構造的問題が継続しており、「収率の再現性評価」という独立論文の出版は現在の刊行慣行では実現困難。AI支援の自動合成評価や高スループット実験技術（HTE）の普及によってデータが蓄積されれば、副次的なデータとして充填される可能性はあるが、それも充填の主目的にはならない。

---

**EP-09a [Internal benchmark pack]（部分記載）:**
* **未充填の理由**: 成功による問いの抹消（Success-driven question erasure）および技術的実現可能だが動機消失——Pd触媒クロスカップリング（Heck 1972, Negishi 1977, Suzuki 1979等）の急速な確立により、「Ni(dpe)がNi(acac)₂より優れているか」という問いが実用的コミュニティから関心を失った。Ni触媒クロスカップリングは特定のアリール系で継続使用されているが、配位子設計原理の実験的検証（EP-09aが求める同一基質での直接比較）は、Pd触媒の圧倒的優位により研究動機を失った。
* **発見的意義**: あり——論文のNote Added in Proofが記録し、D4-8として抽出されたCLA-1（配位子設計原理の独自性）の核心的問いが、後続パラダイムの成功によって問いの枠組みごと置換されたという構造は、「問いの外部化ではなく問いの無意味化」という別の不在パターンとして記録できる。これはUQSが検出した問い（「bidentate diphosphineが必要条件か」）が科学史的に解決されずに放棄されたことを示す事例として意義がある。
* **将来の充填可能性**: 中——Ni触媒クロスカップリングへの再注目（C–O, C–N活性化や電気化学的Niサイクルへの応用）の文脈で、配位子設計原理の系統的研究が再び主流になりつつある。現代の高速配位子スクリーニング技術（HTE + 統計的モデリング）により、NiCl₂(dpe) vs Ni(acac)₂の直接比較が複数基質で実施されるデータが将来的に蓄積される可能性は中程度ある。

---

**EP-04a/EP-05a（部分記載、充填確立点未同定）:**
* **未充填の理由（EP-04a）**: 関心の欠如——cis/trans-スチルベンの速度論/熱力学制御の区別は、Kumada反応のスコープが不斉合成（Hayashi JACS 1976）・交差カップリングの一般化（Negishi、Suzuki等）へと急速に展開したことで、この特定基質系の立体化学制御問題に対する関心が分散したと考えられる。速度論的vs熱力学的制御の区別実験（時間・温度系列）は技術的に単純だが、独立論文化されるほどの科学的インパクトが認識されなかった可能性がある。
* **発見的意義（EP-04a）**: あり（限定）——「機構的含意がある」と著者自身が記述した観察（"interesting mechanistic implications"）が50年以上にわたって系統的に検証されていない可能性は、UQSが記録すべき「著者回顧との照合」の候補。
* **将来の充填可能性（EP-04a）**: 高——現代のin situ NMR・反応プロファイリング技術により、技術的障壁は存在せず、関心を持つ研究者が実施すれば充填可能。

---

**全体的な未充填パターンの意義：**

Kumada 1972の未充填EPは2つのカテゴリに集約される。(i) **インセンティブ構造的未充填**（EP-08a）——合成化学の統計的信頼性評価という慣行的回避。(ii) **成功による問いの抹消**（EP-09a, EP-04a）——後続パラダイム（Pd触媒、不斉合成）の成功による検証需要の消滅。これらのパターンはいずれも「技術的障壁」ではなく「科学コミュニティの動機構造」によって未充填が維持されているという意味で、UQSが「分野の内部者には不可視の構造的不在」を検出する機能の具体例を提供する。特にEP-08a（収率の統計的信頼性）が50年以上未充填であることは、合成化学における再現性危機の前史として、UQSの発見的意義が最も高い未充填項目として記録する。
```
