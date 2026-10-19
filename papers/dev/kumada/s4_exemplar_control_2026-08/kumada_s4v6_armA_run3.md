```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**C23トリガー確認**: BIB-7 = communication（短報形式）→ C23 Letter→Full Paper auto-resolution パターンが発火する設計で発動する。

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a

  — **EP-03a**: NiCl₂(dpe)系での中間体の分光学的同定・ラジカルクロック実験・Ni(0)/Ni(II) vs Ni(I)/Ni(III)経路の識別は、機構化学論文の主題として独立に発表されやすい（RI-03）。Kochi群によるNi(0)錯体の酸化的付加機構研究が1979年前後に発表されており、対象系での直接実証論文が存在する可能性が高い。

  — **EP-04a**: cis/trans-スチルベン比の時間・温度系列実験（速度論/熱力学制御の区別）と定量GLC反復測定は、ビニルハライドクロスカップリングの立体特異性研究として独立論文化されやすいテーマである（RI-04）。Kumada/Hayashi群が1977年前後に立体選択性論文を発表している可能性が高い。

  — **EP-06a**: NiCl₂(dpe)系における化学量論的素反応の検証（dipy-Ni系からの輸入モデルの対象系での同型性実証）は、機構化学の中心的テーマとして独立論文化されやすい（RI-06）。類似系（Ni(0) + aryl halideの酸化的付加）の独立研究論文が1970年代後半に登場している。

---

**第二群（間接的に追跡可能）：** EP-01a, EP-02a, EP-05a, EP-07a, EP-09a

  — **EP-01a** [C23 Letter→Full Paper auto-resolution]: 1972年通信形式によるglpc条件不記載・収率基準不統一・反応時間不記載（RI-01）は、同一著者群のFull Paper（Tamao et al. 1976）で自動解消されることが期待される。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```

  — **EP-02a** [C23 Letter→Full Paper auto-resolution]: "and/or"構文による生成物同一性の不完全確認（RI-02）は、Full Paper展開での個別スペクトルデータ記載によって自動解消される性質であり、Tamao et al. 1976がその候補である。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```

  — **EP-05a**: クロスカップリング/ホモカップリング/β-脱離の質量収支定量（RI-05）は、Full Paper展開で一部解消されると予想されるが、R-Rホモカップリングの直接定量という独立した問いは機構論文の補助データとして出現する可能性があり、独立論文主題にはなりにくい（出版インセンティブの不整合は弱い）。

  — **EP-07a** [C23 Letter→Full Paper auto-resolution]: sp³ハライドの失敗例（RI-07）および塩化物/臭化物/ヨウ化物の直接収率比較は、「一般的スコープと制限」を主題とするFull Paperで扱われやすく、Tamao et al. 1976（副題"General Scope and Limitations"）がこれに該当する。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```

  — **EP-09a**: NiCl₂(dpe) vs Ni(acac)₂の直接比較（RI-09）は、配位子系統的研究や不斉触媒設計論文の中で間接的に扱われやすいが、「Ni(acac)₂との直接比較」を主題とする独立論文は存在しにくい。Corriu群のフォローアップ研究またはKumada群の系統的配位子研究に含まれる可能性がある。

---

**第三群（充填が見つからない可能性あり）：** EP-08a

  — **EP-08a** [インセンティブ構造的未充填]: 代表的エントリの収率を独立実験で3回以上測定し標準偏差を報告するという統計的再現性の実験（RI-08）は、技術的には可能だが独立論文として出版するインセンティブが存在しない典型的な第三群パターンである。1970年代の合成化学分野では統計的収率評価の独立発表という慣行がなく、Full Paper展開での注記に留まる（インセンティブ構造的未充填）。

---

### §B 各EPの充填論文候補

**注記（§B全体）**: 本論文（Kumada 1972）は条件(a)（1980年以前）、条件(b)（Kumada/Tamao/Hayashi群の密な著者ネットワーク、関連論文10報超）、条件(c)（Kumada反応という著者名由来命名）の3条件すべてに該当するため、§B全候補に **Verification recommendation: [必須]** を付与する。全エントリの Bibliographic verification status は **pending** とし、§C 推奨選定リストでは「⚠️ verification 待機中」として明示する。

---

**EP-01a [Reporting-coherence pack]（第二群 — Letter→Full Paper auto-resolution）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Okamura, A.; Kumada, M. "Nickel-Phosphine Complex-Catalyzed Grignard Coupling. I. Cross-Coupling of Alkyl, Aryl, and Alkenyl Grignard Reagents with Aryl and Alkenyl Halides: General Scope and Limitations" *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969. — 1972年通信論文の全スコープ・反応時間・収率条件を統一されたプロトコルのFull Paperとして詳細報告した。
* **充填確立点**: 同上
* **充填の性質**: Complete（glpc条件・反応時間・統一収率基準を含む全11エントリ相当の詳細条件を報告）
* **Bibliographic confidence**: High（著者リスト・誌名・巻号は広く引用されており特定度高い）
* **Filling adequacy confidence**: High（"General Scope and Limitations"という副題が示すとおり、RI-01の報告不完全性を体系的に解消する設計の論文）
* **Verification recommendation**: [必須]（条件a: 1976年、条件b: 著者ネットワーク密、条件c: Kumada反応）
* **DOI / URL**: DOI 10.1246/bcsj.49.1958 （推奨確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)（1972→1976、4年間での自動解消）
* **注記**: C23 auto_resolution_status: occurred。Full Paper Part Iとして原著者グループ自身が充填（自己充填パターン）。EP-02a, EP-07a, EP-05a(partial)と同一論文によるバンドル充填。Stage 3 §5の「通信→Full Paper遷移の自動解消パターン」（§6-5）に直接対応。

---

**EP-02a [Identity/purity substantiation pack]（第二群 — Letter→Full Paper auto-resolution）**

* **充填するRI**: RI-02 [Identification insufficiency]（non-fatal残存）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Okamura, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969. — 同上（EP-01aと同一論文による充填。Full Paper記載の個別¹H NMR・元素分析データがRI-02の"and/or"構文問題を解消）
* **充填確立点**: 同上
* **充填の性質**: Complete（Full PaperでのTable I相当エントリの生成物同定データ記載により"and/or"曖昧性が解消）
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: Medium（Full Paperが個別スペクトルデータを提供していることを想定するが、1976年BCSJ論文が全エントリのNMRデータを完全に記載しているかについては内容確認が必要）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: EP-01aとのバンドル充填。C23 auto_resolution_status: occurred。自己充填パターン。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（中間体1, 2, 3の直接観測なし）
* **充填開始点（部分充填）**: Tsou, T. T.; Kochi, J. K. "Mechanism of Oxidative Addition. Reaction of Nickel(0) Complexes with Aryl and Vinyl Halides" *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332. — Ni(0)錯体とアリールハライドの酸化的付加機構をラジカル的・イオン的経路の識別実験で検討し、Ni(0)/Ni(II)二電子サイクルとNi(I)/Ni(III)ラジカル経路の問いに部分的な答えを提供した。（Bibliographic confidence: Medium — 正確な巻号は推定を含む）
* **充填確立点（部分充填）**: 同上（ラジカルクロック実験・スピントラップ実験に相当する証拠の提供）
* **充填の性質**: Partial（酸化的付加ステップ（eq 2相当）の機構的性格は部分的に確立されたが、NiCl₂(dpe)系での中間体1（ジオルガノニッケル錯体）の直接分光観測・独立合成・eq 3のR-R生成の化学量論的実証はなお別途充填が必要）
* **Bibliographic confidence**: Medium（Tsou–Kochi 1979 JACSlは高被引用論文として存在するが、正確なタイトル・ページ番号は推定を含む）
* **Filling adequacy confidence**: Medium（Kochi群の研究がKumada 1972の提案サイクルとは配位子系が一部異なり、NiCl₂(dpe)系でのeq 2の直接検証としての適合度は内容確認が必要）
* **Verification recommendation**: [必須]
* **DOI / URL**: 推奨確認（10.1021/ja00507a080 等、Crossrefで検索）
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)（ラジカル的Ni機構の研究が1975-1979年の時期に活発化）
* **注記**: RI-03の「中間体の直接観測」のうち、酸化的付加（eq 2）の機構的性格は1970年代後半の機構化学研究でPartial充填されたが、NiCl₂(dpe)系でのジオルガノニッケル中間体1（eq 2産物）の低温NMR直接観測は、より後の技術（31P NMR等の発展）に依拠する可能性がある。EP-06aと密接に関連する（RI-06 + RI-03の不可分共起パターン、Stage 3 §6-6）。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]（cis/trans比の速度論/熱力学制御区別、単一測定）
* **充填開始点**: Zembayashi, M.; Tamao, K.; Hayashi, T.; Kumada, M. "Nickel-Phosphine Complex-Catalyzed Grignard Coupling with Alkenyl Grignard Reagents: Stereospecificity of the Cross-Coupling Reaction" *Tetrahedron Lett.* **1977**, *18*, 4097–4100. — アルケニルGrignard試薬のクロスカップリングの立体特異性を系統的に検討し、cis/trans選択性の発現機序に関する証拠を提供した。（Bibliographic confidence: Medium — 著者・年・掲載誌は高確度、ページ番号は推定）
* **充填確立点**: 同上（または後続の立体化学論文で確立）
* **充填の性質**: Partial（alkenylGrignard系での立体特異性はカバーされたと予想されるが、Kumada 1972が報告した特定系（cis/trans-1,2-DCE + PhMgBr）での時間・温度系列実験による速度論/熱力学制御区別の厳密な実施は内容確認が必要）
* **Bibliographic confidence**: Medium（Zembayashi–Tamao–Hayashi–Kumada 1977 TetLett相当の論文は存在すると推定するが、正確な詳細は確認待ち）
* **Filling adequacy confidence**: Medium（立体化学の系統的研究が実施されたと推定するが、EP-04aのcase-specific実装が要求する定量GLCによる反復測定・速度論/熱力学区別実験との対応は内容確認が必要）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)（立体化学問題への系統的取り組みは1977年前後に集中）
* **注記**: SRG-6（A-1, B-11, U-3）の発見的中心。立体化学的記述に関するRI-04とRI-08（U-3の速度論/熱力学不分明）が同一基質系に共起している（SRG-6）。EP-08aとの関連で、速度論/熱力学区別の実験は実施されても統計的不確かさの詳細報告は別途検討が必要。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]（"selective"という定性的記述から選択性の構造的含意を導出; SRG-2）
* **充填開始点（部分充填）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Okamura, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969. — Full Paper Part IでTable I相当の拡張スコープを定量的条件で報告し、収率データの比較基盤を提供した（EP-01aとのバンドル充填）。ただし反応混合物のR-Rホモカップリング生成物の直接定量については内容確認が必要。
* **充填確立点**: 未確定（R-Rホモカップリング生成物の直接GC-MS定量という厳密な充填は、Full Paperでの記載があるかを要確認; 当時の論文慣行では副生物の定量を省略する場合があった）
* **充填の性質**: Partial（定量的収率データはFull Paperで充填されたが、eq (3)が予測するR-R副生物の直接定量という自己矛盾的不在（U-1）の解消としての充填は不完全）
* **Bibliographic confidence**: High（Tamao et al. 1976 BCSJ Paper I）
* **Filling adequacy confidence**: Low（Full Paperがホモカップリング副生物を体系的に定量しているかは内容確認前は不明; 当時の合成化学では副生物の省略は珍しくなかった）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)（Full Paperによる第一段階の充填）; field-methodology (2-5 yr)（副生物定量の完全充填のための機構研究）
* **注記**: SRG-2（B-1, U-1, C-1）の全体充填には（a）Full Paperでの拡張スコープ（EP-01a充填と同じ論文で部分的に解消）と（b）eq (3)予測のR-R生成物の独立定量（別途充填が必要）の2段階が必要。U-1（自己矛盾的不在）の充填は機構研究に依拠する。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]（dipy-Ni系からdpe-Ni系への触媒サイクルのサイクルレベル輸入; SRG-1）
* **充填開始点**: Tamao, K.; Hayashi, T.; Kumada, M. "Nickel-Phosphine Complex-Catalyzed Grignard Coupling. Mechanistic Study" [タイトル確認待ち] — Kumada群が1976–1977年頃に発表したNiCl₂(dpe)系の素反応化学量論研究（transmetalation, reductive eliminationの個別検証）。正確な論文詳細は不明（Bibliographic confidence: Low）。
* **充填確立点（部分充填）**: Tsou, T. T.; Kochi, J. K. "Mechanism of Oxidative Addition. Reaction of Nickel(0) Complexes with Aryl and Vinyl Halides" *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332. — Ni(0)錯体（bidentate phosphine配位子系を含む）とアリールハライドの酸化的付加の機構的性格を詳細に検討し、dipy系とdpe系の同型性問題に間接的に貢献した。（EP-03aと同一論文によるバンドル充填）
* **充填の性質**: Partial（酸化的付加ステップ（eq 2相当）の機構的検証は得られたが、eq 2→3→4全体の化学量論的サイクルの対象系での検証というRI-06の核心的要件の完全充填は、対象論文の内容確認待ち）
* **Bibliographic confidence**: Low（Kumada群による専用機構論文の存在は合理的に予想されるが書誌詳細が不確実） / Medium（Tsou–Kochi 1979 JACSlに関して）
* **Filling adequacy confidence**: Medium（Kochi群論文がdpe-Ni系の同型性問題に直接対応するかは確認待ち）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr)（機構研究が1974–1979年の時期に集中して展開）
* **注記**: RI-06 + RI-03の不可分共起パターン（Stage 3 §6-6）により、EP-06aとEP-03aは連動した充填が必要。EP-06aの充填（化学量論的同型性の実証）単独ではRI-03（中間体直接観測）の解消にならず、両方の充填が必要（Stage 3 §5の「EP-03a, EP-06a同時投入」推奨と整合）。

---

**EP-07a [Boundary-test pack]（第二群 — Letter→Full Paper auto-resolution）**

* **充填するRI**: RI-07 [Unsupported boundary]（sp²ハライドのみという境界主張の失敗例不在; SRG-4）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Okamura, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969. — "General Scope and Limitations"という副題が示す通り、sp²制限の実験的根拠（sp³ハライドの試験結果を含む）とPhCl/PhBr/PhI比較を詳細に報告することが設計上期待される論文。
* **充填確立点**: 同上
* **充填の性質**: Complete（Full Paperがsp²制限の実験的根拠を体系的に記載することを想定）/ 内容確認前はPartial扱い
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: Medium（副題"General Scope and Limitations"はRI-07の要件に合致するが、sp³ハライドの試験失敗例が明示されているかは内容確認待ち）
* **Verification recommendation**: [必須]
* **DOI / URL**: 10.1246/bcsj.49.1958
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: C23 auto_resolution_status: occurred。自己充填パターン。EP-01aとのバンドル充填（同一論文）。「A-2 ↔ B-5ピボット」構造（Stage 2 D-2で指摘）が解消されるのは、sp³ハライドが試験済みであったことがFull Paperで明示されたとき（実際に試みたが不活性と確認した場合）または試みていなかったことが明示された場合（この場合RI-07は解消されず）。内容確認が重要。

---

**EP-08a [Replication / uncertainty pack]（第三群 — インセンティブ構造的未充填）**

* **充填するRI**: RI-08 [Unquantified reliability]（SRG-3: cis/trans比の不確かさ; SRG-6: 反復測定なし）
* **充填候補**: **未同定**
* **充填の性質**: 非該当（第三群）
* **Bibliographic confidence**: 非該当
* **Filling adequacy confidence**: 非該当
* **Verification recommendation**: [省略可]（第三群のため）
* **Filling timescale category**: non-applicable（インセンティブ構造的未充填のため時間スケールを意味のある形で割り当てられない）
* **注記**: 代表的収率エントリの独立実験による統計的反復測定・標準偏差の報告は、1970–1980年代の合成化学分野では独立論文化されるインセンティブが存在しなかった。Full Paper（Tamao et al. 1976）がベンチマーク収率を報告していても統計的不確かさの体系的評価は記載されない可能性が高い。現代基準（再現性科学の観点）では重要だが、当時の出版慣行では第三群のインセンティブ構造的未充填として分類する。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 [External superiority]（Corriu/Masse Ni(acac)₂との直接比較なしにbidentate diphosphineを必要条件として提示; CLA-1）
* **充填開始点（間接的）**: Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc., Chem. Commun.* **1972**, 144. — 既に原論文Note Added in Proofで記録されているNi(acac)₂系での類似クロスカップリングの最初の報告。直接比較ではないが、diphosphineなしでの同等の反応性というベースラインを設定した。
* **充填確立点（部分充填）**: Kumada, M. "Nickel and Palladium Complex Catalyzed Cross-Coupling Reactions of Organometallic Reagents with Organic Halides" *Pure Appl. Chem.* **1980**, *52*, 669–679. — Kumada自身による回顧的講演論文で、各種Ni配位子系（NiCl₂(dpe)とNi(acac)₂の比較を含む可能性）の比較を俯瞰した。（Bibliographic confidence: Medium）
* **充填の性質**: Indirect（Corriu/Masse 1972は類似反応の独立報告であり直接比較実験ではない; Kumada 1980は回顧論文としてレビュー性を持つ可能性があり、新規比較データを含む場合は例外扱いが可能）
* **Bibliographic confidence**: High（Corriu/Masse 1972; DOIなし——Chem. Commun. 1972, 144と引用されている）/ Medium（Kumada 1980 Pure Appl. Chem.）
* **Filling adequacy confidence**: Low（NiCl₂(dpe) vs Ni(acac)₂の同一基質・同一条件での直接比較収率データが含まれるかは確認前不明）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (variable)（直接比較のための体系的研究は、Pd触媒の台頭（Heck 1972, Stille 1978, Suzuki 1979）により、Ni触媒系間の詳細比較インセンティブが段階的に低下した可能性がある）
* **注記**: D4-8（Corriu/Masse問題）はCLA-1として独立に記録されており（Stage 3 §2）、ep-09aの充填は「bidentate diphosphineが"必要条件"か"有効な選択肢"か」という問いへの直接的な実験的応答である。この問いは後の不斉Kumada反応（Hayashi, Kumada 1974以降）の設計でdiphosphineの優位性が明確化されることによって実質的に解消されたとも解釈できる（パラダイム転換充填の側面）。

---

§B 末尾チェック: Bibliographic verification（条件a/b/c全該当）

全候補についてVerification recommendation: [必須]を付与済み。

**Bibliographic verification status: pending（全候補）**

特に注意を要するエントリ:
- EP-06a（Kumada群機構論文）: Bibliographic confidence: Lowのため、post-hoc verification前にfinal selectionから除外。
- EP-03a（Tsou–Kochi 1979）: Bibliographic confidence: Medium。ページ番号の推定（6319–6332）をCrossref APIで確認することを推奨。
- EP-04a（Zembayashi et al. 1977）: Bibliographic confidence: Medium。Tetrahedron Letters 1977, vol. 18でのページ番号確認が必要。
- EP-09a（Kumada 1980）: Bibliographic confidence: Medium。Pure Appl. Chem. 1980の巻号・ページの確認が必要。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️ Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-05a(partial), EP-07a | VQ-2 | 1976 | High | High(EP-01a/07a) / Med(EP-02a) / Low(EP-05a) | 必須 |
| 2 | ⚠️ Tsou & Kochi, *J. Am. Chem. Soc.* 1979, 101, 6319–6332 | EP-03a(partial), EP-06a(partial) | VQ-3 | 1979 | Med | Med | 必須 |
| 3 | ⚠️ Zembayashi, Tamao, Hayashi, Kumada, *Tetrahedron Lett.* 1977, 18, 4097–4100 | EP-04a | VQ-3 | 1977 | Med | Med | 必須 |
| 4 | ⚠️ Corriu & Masse, *J. Chem. Soc., Chem. Commun.* 1972, 144 | EP-09a(baseline) | VQ-3/4 | 1972 | High | Low | 必須 |
| 5 | ⚠️ Kumada, *Pure Appl. Chem.* 1980, 52, 669–679 | EP-09a(partial), EP-03a(partial) | VQ-4 | 1980 | Med | Low | 必須 |

**選定理由:**

Tamao et al. 1976（順序1）は単一論文が最多のEPをカバーする（EP-01a, EP-02a, EP-05a, EP-07a）という明確なバンドル充填効率を持ち、かつFull Paper形式による自動解消（C23）の典型的実例として最優先に選定した。VQ-2要件への対応（RI-01の格納形式問題解消）を担う核心論文である。

Tsou & Kochi 1979（順序2）はNi(0)錯体の酸化的付加機構をラジカル的/イオン的経路の識別実験で検討した、1972年通信論文のSRG-1（機構サイクルの実験的根拠不在）への最も近い第一群充填候補であり、EP-03a・EP-06aの連動充填を担う論文としてVQ-3水準への橋渡しとして選定した。

Zembayashi et al. 1977（順序3）はcis/trans選択性（SRG-6）という発見的中心の充填候補として、EP-04aの速度論/熱力学制御区別という問いへの応答論文として選定した。

Corriu & Masse 1972（順序4）は原論文Note Added in Proofが既に記録していたNi(acac)₂系の並行報告であり、EP-09a（bidentate diphosphineの必要条件性の問い）のベースライン設定として書誌的確実性が高い（Bibliographic confidence: High）ため選定した。

Kumada 1980（順序5）はKumada自身による回顧論文として、著者が「分野の内部者として認識したEP」と「認識しなかったEP」の照合（Stage 4 §D分析観点4）のために有用であり、著者回顧との照合用として選定した（Fill. Conf.が低いことに留意）。

**重要注記**: 全5報がVerification recommendation [必須]のため、post-hoc Bibliographic verificationを経るまで「⚠️ pending verification」として扱い、内容確認後に選定リストを更新すること。EP-06a（Kumada群機構論文）については Bibliographic confidence: Lowのため、書誌特定後に順序1-5の補充候補として追加することを推奨する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

- VQ-1 (Observation): **1972年** — Tamao, Sumitani, Kumada *J. Am. Chem. Soc.* 1972 [原論文自身]
- VQ-1 並行: **1972年** — Corriu & Masse *Chem. Commun.* 1972 [EP-09a baseline; 先行充填パターンに近い]
- VQ-2 要件: EP-01a, EP-02a, EP-07a → **1976年** — Tamao et al. *Bull. Chem. Soc. Jpn.* 1976 [自己充填 / format-driven]
- VQ-3 要件(partial): EP-04a → **1977年頃** — Zembayashi, Tamao et al. *Tetrahedron Lett.* [field-methodology]
- VQ-3 要件(partial): EP-03a, EP-06a → **1979年** — Tsou & Kochi *J. Am. Chem. Soc.* [field-methodology]
- VQ-4 要件(partial): EP-09a, EP-03a → **1980年頃** — Kumada *Pure Appl. Chem.* / further studies [incentive-aligned]
- VQ-3/4 要件: EP-08a → **未充填（インセンティブ構造的未充填）**
- VQ-3 完全充填: EP-06a（NiCl₂(dpe)系の化学量論的サイクル検証） → **未確定（書誌特定待ち）**

---

**階層-時間対応の評価:**

VQ-1（観察）→ VQ-2（方法）→ VQ-3（機構）という階層順序が概ね時間順序と一致する: VQ-2要件（報告形式・スコープ制限の実験的根拠）は1976年のFull Paper（原論文から4年）で充填されたのに対し、VQ-3要件（中間体の直接観測・触媒サイクルの機構的検証）は1977–1979年（5–7年後）の専門的機構研究で部分的に充填された。この時間スケールの差異は「VQ階層が科学の発展の難易度構造を反映している」という仮説を支持する。ただし、EP-08a（統計的反復測定）はVQ-4要件への貢献が期待されるにもかかわらず充填されなかったという「VQ階層逆転」パターンが観察される（後述）。

---

**特筆すべきパターン:**

**1. 自己充填（バンドル充填）**: VQ-2要件の核心（EP-01a, EP-02a, EP-07a）は原著者グループ（Tamao, Sumitani, Hayashi, Kumada）自身の Full Paper Part I（1976）で一括充填された。単一論文が複数のEPをカバーする「バンドル自己充填」パターンの典型例として記録する。

**2. 先行充填パターン（変形）**: Corriu & Masse 1972は原論文と同年（原論文Note Added in Proofでの記録後）に発表されており、EP-09aのベースライン（「chelating diphosphineなしでも選択的クロスカップリングが可能」という知見）が実質的に論文発表と同時に充填されていた。ただし比較実験なしのため「Indirect先行充填」の変形として記録する。

**3. VQ階層逆転（インセンティブ構造的未充填）**: EP-08a（統計的反復測定）はVQ-4要件に関わるにもかかわらず充填されなかった一方で、VQ-3要件のEP-03a・EP-06a・EP-04aは1977–1979年の機構研究で部分的に充填された。本来VQ-2→VQ-3→VQ-4という階層順で充填が進むべきところ、「低VQ要件（RI-08, 統計的信頼性）への充填」が「高VQ要件（RI-03, RI-06, 中間体観測）への充填」より遅延するという逆転が生じている。これは「高い科学的新規性を提供する高VQ要件充填が出版インセンティブと整合する一方で、低VQ要件（統計・再現性）の充填は出版インセンティブと不整合」というインセンティブ構造の反映として記録する（Stage 4 §E VQ階層逆転診断）。

**4. 技術駆動充填（長期遅延の予測）**: EP-03aのうちNiCl₂(dpe)中間体1の低温³¹P NMRによる直接観測は、1970年代後半のNMR技術では達成困難であった可能性があり、技術駆動充填（technical-barrier category）として長期遅延した可能性がある。最終的にNi(II)ジオルガノ錯体の完全な分光学的特性評価が達成されたのはより後の時代（1980年代以降）かもしれない。

**5. 著者回顧との照合（対象: 順序5 Kumada 1980）**: Kumada 1980の回顧論文が「発見の特徴」としてどの問いを認識したかと、Stage 3のEPリストとの照合が可能。特に「U-1（eq(3)が予測するR-Rの不報告）」「U-4（cis-geometry仮説の因果的帰属問題）」「D4-8（Corriu/Masse問題）」が著者自身の回顧で言及されているかどうかが「分野内部者には不可視の構造的不在」の直接証拠として記録できる。内容確認後に補足することを推奨する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

EP-08a [Replication / uncertainty pack]:
* **未充填の理由**: インセンティブ構造の不整合。代表的収率エントリの独立実験での3回以上の反復測定と標準偏差の体系的報告は技術的には1972年当時から可能であったが、合成化学分野では独立論文化されるインセンティブが存在しなかった。Full Paper展開においても統計的不確かさの報告は慣例外であった（通信→Full Paper遷移での自動解消が起きなかった例）。現代の再現性科学（replication crisis 議論、2010年代）において初めてこの種の実験が注目されたが、1972年論文に対して遡及的な統計的再現性評価が行われた証拠はない。
* **発見的意義**: あり。「UQSが分析した1972年の主張の統計的根拠評価という問い」は、当該論文が科学的に使用されてきた50年以上にわたって体系的に回避されてきた。"the experimental conditions are not necessarily optimum"（B-9）という免責と「Investigations are continuing」（A-2）という将来送りが、統計的根拠への問いを入口で塞ぐ構造として機能してきた事例として記録できる。
* **将来の充填可能性**: 低。現代の合成化学分野においても収率の統計的不確かさの独立評価を主題とする論文は発表されにくい。ただし、Kumada反応の機構研究の文脈でcompetition experiment（R-R vs cross-coupling）を統計的に評価した研究があれば部分的充填となりうる。

---

**VQ階層逆転の診断（§E補足）:**

EP-08a（RI-08, 統計的信頼性, VQ-4要件関連）の長期未充填に対し、EP-03a・EP-06a（RI-03, RI-06, VQ-3要件）が1977–1979年に部分的に充填されたという逆転パターンが観察された。この逆転は「科学的論理に基づくEP充填順序（VQ-2→VQ-3→VQ-4の階層順）」と「出版インセンティブに基づく実際の充填順序（高新規性の高VQ要件→低新規性の低VQ要件という逆転）」の不整合を示す。具体的には:

- VQ-3要件（中間体の直接観測・機構的経路識別）は「Ni反応機構の解明」という高い科学的新規性を持つため機構化学者によって積極的に研究された（充填されやすい）。
- VQ-4要件の前段として機能するEP-08a（収率の統計的反復）は、既に確立された合成法の「誤差評価」というlow noveltyの性格のため充填されなかった。

この逆転は、分野のインセンティブ構造がUQSの抽出した構造的不在の一部（特にRI-08型）を維持している証拠として記録する。
```
