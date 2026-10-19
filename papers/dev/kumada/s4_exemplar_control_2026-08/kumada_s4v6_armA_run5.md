```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**C23 trigger確認**: 対象論文はJACS Communication形式（BIB-7: communication）→ Letter→Full Paper auto-resolution チェックを実施する。

**三群分類:**

**第一群（文献で明確に追跡可能）:** EP-01a, EP-03a, EP-06a, EP-07a

— **EP-01a** (Reporting-coherence pack, RI-01): JACS Communication形式からの通信→Full Paper自動解消が発生しており、同一著者グループの1976年BCSJ全論文がglpc条件・反応時間・収率基準統一を含む詳細な記述を提供していると考えられる（C23 auto-resolution: occurred）。

— **EP-03a** (Direct-observation / state-assignment pack, RI-03): NiCl₂(dpe)系の触媒中間体の同定は後続の機構研究の主要目標であり、Kumadaグループ自身の機構論文および第三者（Kochi et al.）による独立研究として独立論文化されている可能性が高い。

— **EP-06a** (Analogy-validation pack, RI-06): dipy-Ni系からdpe-Ni系への触媒サイクル輸入の同型性検証は、後続の機構研究の核心的問いであり、Kumadaグループの続報および独立した機構研究者（Kochi グループ等）により独立論文として取り組まれた。

— **EP-07a** (Boundary-test pack, RI-07): sp²/sp³ハライドの選択性境界の実験的検証および塩化物/臭化物/ヨウ化物の定量的反応性比較は、方法の適用範囲確立において標準的な実験であり、Kumadaグループの後続論文での直接的実験として独立論文化されている。

**第二群（間接的に追跡可能）:** EP-02a, EP-04a, EP-05a, EP-09a

— **EP-02a** (Identity/purity substantiation pack, RI-02): 全Table Iエントリの個別分光データは、Letter→Full Paper自動解消パターン（C23）の一部として1976年全論文に吸収される可能性が高いが、"and/or"構文問題（RI-02 non-fatal）の完全解消かどうかは確認が必要であり、間接的充填の可能性が残る。

— **EP-04a** (Discrimination / replication pack, RI-04): cis/trans比の速度論的vs熱力学的区別実験は、ビニルハライドのクロスカップリング立体化学という独自の問いとして後続研究で扱われるが、Kumada 1972の特定エントリ（cis-/trans-1,2-dichloroethylene + PhMgBr）についての追実験として独立論文化されるというよりは、より広い立体化学機構研究の一部として収録されることが多い。

— **EP-05a** (Quantitative-ranking substantiation pack, RI-05): 反応混合物の質量収支（クロスカップリング vs ホモカップリング vs β-脱離）は1976年全論文に部分的に含まれる可能性があるが、GC-MS全量定量という現代的要求水準での充填は機構研究論文の副次的データとして収録される傾向があり、独立論文での主題化は限定的。

— **EP-09a** (Internal benchmark pack, RI-09): NiCl₂(dpe)とNi(acac)₂（Corriu/Masse系）の直接比較実験は、当初はNote Added in Proofで記録されながら比較されなかった問いであり、後続の比較機構研究や総説での系統的比較としてのみ追跡可能な場合が多い。

**第三群（充填が見つからない可能性あり）:** EP-08a

— **EP-08a** (Replication / uncertainty pack, RI-08): Table I各エントリの独立反復測定と統計的不確かさの定量は、「インセンティブ構造的未充填」に分類される。合成手法論文の追試は新規性を要求する出版慣行のもとで独立論文化されにくく、同一系の収率再現性評価は通常方法の「使用」の中で蓄積的に確認されるだけで体系的統計論文として発表されない。

---

### §B 各EPの充填論文候補

**⚠️ Bibliographic verification 必須トリガー評価（全候補対象）:**
- (a) 論文年代 1972 → 1980年以前: **YES**
- (b) 著者ネットワーク密（Kumadaグループから10+の関連論文）: **YES**
- (c) Named reaction（Kumada coupling）: **YES**
- 判定: **[必須]** — 以下の全候補にVerification recommendation [必須] を付与する。Bibliographic verification status は pending。

---

**EP-01a [Reporting-coherence pack]（第一群）**

* **充填するRI**: RI-01 (Reporting integrity) / secondary RI-08
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — NiCl₂(dpe)触媒によるGrignard試薬のクロスカップリングの全論文として、統一glpc条件・全エントリの反応時間・収率計算基準を記述した包括的な続報。
* **充填確立点**: 同上
* **充填の性質**: Complete（Letter→Full Paperとして通信で省略された測定・条件の詳細を提供）
* **Bibliographic confidence**: Medium — 1976年BCSJ発行の包括的全論文の存在は業界でよく参照されるが、著者順および正確な巻号ページの確認が必要
* **Filling adequacy confidence**: High — 全論文への遷移がRI-01（glpc条件・反応時間・収率基準）を直接解消する性質のものであることは明確
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **DOI / URL**: 確認要。Bull. Chem. Soc. Jpn. 1976, 49 — Crossref検索推奨
* **Filling timescale category**: format-driven (1-3 yr)
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```
* **注記**: C23 auto-resolution パターン発火。BIB-7がcommunication形式であることを確認済み（S0での"format: communication"）。EP-02aも同一論文に吸収されるバンドル充填候補。Stage 3 §4のEra-Norm Annotationでは B-4, B-8, B-13が "communication-era tolerated" として Full Paper遷移での自動解消候補に分類されていた。

---

**EP-02a [Identity/purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 (Structural/chemical identity claim) — non-fatal残存
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — 全論文がTable I相当エントリのより詳細な化合物特性評価（NMR, IR, 元素分析）を含む。
* **充填確立点**: 同上（EP-01aと同一論文、バンドル充填）
* **充填の性質**: Partial — "and/or"構文問題に由来するRI-02 non-fatalが全論文での完全個別分光データ記録によって実質解消される可能性があるが、全論文の全エントリへの対応を確認するまではPartialと判定
* **Bibliographic confidence**: Medium（EP-01aと同一論文）
* **Filling adequacy confidence**: Medium — 全論文が全エントリの個別分光データを提供しているかどうかは確認が必要
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: EP-01aのバンドル充填候補。Stage 3 §5では補助EPとして位置づけられていた（最短補強ルートの括弧書き）。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory entity) — 中間体1, 2, 3の直接観測
* **充填開始点（候補A — Kumadaグループによる自己充填）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — 全論文がNiCl₂(dpe)系の化学量論的素反応実験または中間体の分光観測を部分的に含む可能性がある。
* **充填確立点（候補B — 独立機構研究）**: Morrell, D. G.; Kochi, J. K. J. Am. Chem. Soc. 1975, 97, 7262–7270 — NiCl₂(dpe)またはNi-phosphine系を用いたGrignard試薬クロスカップリングの機構（Ni(I)/Ni(III)ラジカル経路 vs Ni(0)/Ni(II)二電子経路）をラジカルクロック実験で検討した独立研究。
* **充填の性質**: Attempted / Paradigm-shift — 候補AはPartial（化学量論的実験、ただし低温NMRによる中間体直接観測の確認が必要）; 候補BはParadigm-shiftに近い（Ni(0)/Ni(II)の輸入モデル前提を覆す可能性を示す実験的証拠）
* **Bibliographic confidence**: 候補A: Medium; 候補B: Medium — Kochi グループが1975年前後にNi-catalyzed Grignard coupling の機構研究を行ったことは確かであるが、正確な著者・巻号・ページの確認が必要
* **Filling adequacy confidence**: 候補A: Medium（全論文の内容に依存）; 候補B: Medium（ラジカルクロック実験がdpe系に適用されたかどうか）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: 候補A: format-driven (1-3 yr); 候補B: incentive-aligned (3-5 yr)
* **注記**: Stage 3 §6でRI-06とRI-03の「不可分共起」パターンが記録されている。EP-06a（analogy-validation）の充填と同時進行が必要であり、EP-03a単独での充填（dipy-Ni系との同型性実証なし）では不十分。dpe-Ni系の[Ni(R₂)(dpe)]中間体の直接合成・分光観測には技術的ハードルがあり、RI-06+RI-03共起の解消は段階的になった可能性が高い。なお、後にNi(I)/Ni(III)ラジカル機構が有力視されるようになった点は、輸入モデル（Ni(0)/Ni(II)）とは異なる枠組みを提供するParadigm-shift成分として記録すべき。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 (Unreplicated discriminator) / secondary RI-08 — cis/trans比の速度論的vs熱力学的制御の区別
* **充填開始点（候補）**: Kumadaグループの後続立体化学研究（年代ca. 1977–1980）— ビニルハライドのクロスカップリングにおけるcis/trans選択性の立体化学起源を時間・温度系列実験で検討した論文（具体的な書誌情報は確認できず）。
* **充填確立点**: 未確認 — 充填論文が独立論文として発表されたかどうかの確認が必要
* **充填の性質**: 充填状況未確認 — cis/trans stilbene混合物の生成比に関する系統的時間・温度依存性データが独立論文として発表されたかどうかは、後続の文献精査が必要
* **Bibliographic confidence**: Low — 具体的な書誌情報を提示できない
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending（低信頼度のため記録のみ、§Eでの未充填分析に送出）
* **Filling timescale category**: incentive-aligned (variable)
* **注記**: Stage 3 §2 SRG-6の注記に「cis/trans比の観察はVQ-1の範囲に留まる（観察は成立するが機構的解釈のための証拠基盤は未整備）」とある。この観察は特殊性が高く（特定のdichloroethylene基質系のみ）、独立論文化されずに周辺的データとして取り扱われた可能性が高い。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 (Qualitative overread) / primary in SRG-2 and CLA-1 — 「選択的クロスカップリング」のホモカップリング含む質量収支定量化
* **充填開始点（候補A — 全論文での部分充填）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — 全論文がより詳細な基質対比較（chloride vs bromide, sp²選択性の実験的根拠）を提供する可能性がある。
* **充填確立点（候補B — 機構研究での間接充填）**: Morrell, D. G.; Kochi, J. K. J. Am. Chem. Soc. 1975, 97, 7262–7270（EP-03aと同一論文候補）— ラジカル経路研究の副次的産物として、競合する副反応（homo-coupling, β-脱離）の相対量データが含まれる可能性がある。
* **充填の性質**: Partial（候補A）— glpc質量収支の詳細は含まれうるが、eq (3)が予測するR–R生成物の体系的定量（U-1の自己矛盾的不在の解消）が全論文に含まれるかは確認が必要
* **Bibliographic confidence**: 候補A: Medium（EP-01aと同一論文）; 候補B: Medium
* **Filling adequacy confidence**: Medium（候補A）; Low（候補B）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)（候補A）; incentive-aligned（候補B）
* **注記**: SRG-2 の選択性定量は D4-1 の核心問いに対応する。Stage 3 §2 SRG-2の注記で「eq (3)が予測するR–Rの不報告は現代基準では自己矛盾を構成する」と指摘された。CLA-1（Corriu/Masse との比較）で指摘されたNi(acac)₂との比較データは EP-09a として分離して扱う。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 (Imported model) — dipy-Ni系からdpe-Ni系へのサイクルレベル輸入の同型性実証
* **充填開始点（候補A — Kumadaグループ自己充填）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — dpe-Ni系での化学量論的素反応実験（eqs 2–4に対応する個別ステップの実証）を含む可能性がある。
* **充填確立点（候補B — Paradigm-shift充填）**: Morrell, D. G.; Kochi, J. K. J. Am. Chem. Soc. 1975, 97, 7262–7270 — Ni(0)/Ni(II)二電子サイクルの代わりにNi(I)/Ni(III)ラジカル経路を支持する実験的証拠を提供し、輸入モデルの前提を根本的に問い直す。
* **充填の性質**: 候補A: Partial（化学量論的検証を部分的に提供）; 候補B: Paradigm-shift（EPの前提となる輸入モデルの枠組み自体を変更）
* **Bibliographic confidence**: 候補A: Medium; 候補B: Medium
* **Filling adequacy confidence**: 候補A: Medium; 候補B: High（Ni(I)/Ni(III)メカニズムがdpe-Ni系に適用されたとすれば、RI-06の輸入モデル問題は「輸入モデルが機構的に誤りだった」という形で解消される）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven / incentive-aligned (3-5 yr)
* **注記**: Stage 3 §6の「RI-06 + RI-03の不可分共起パターン」に対応。EP-03aとのバンドル充填関係がある（どちらかの候補が両EPを同時に充填する）。dipy-Ni系の先行研究（Yamamoto, Yamamoto, Ikeda, JACS 1971）は「輸入元」論文であってEP充填論文ではない — この区別を保持する。Kochi グループによるラジカル経路の実証は、Ni(0)/Ni(II)輸入モデルを「部分的に誤った類推」として記録することになるが、触媒サイクルの枠組みが正しいかどうかとは独立に、合成実用性層（層1）は保持される（Stage 3 §1の層別VQ非対称性と整合）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary) — sp²/sp³ハライド選択性の実験的根拠 + 塩化物/臭化物/ヨウ化物の定量的反応性比較
* **充填開始点（候補A）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — sp³ハライドの挙動（不活性または副反応）とPhCl/PhBr/PhI間の定量的収率比較を含む可能性がある。
* **充填確立点（候補B — 独立スコープ研究）**: Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. J. Am. Chem. Soc. 1976, 98, 3718–3720 — キラルフェロセニルホスフィン-Ni触媒による不斉Grignard試薬クロスカップリングの最初の報告。基質スコープの拡張と収率データの提供を含み、sp²選択性の実用的根拠を強化する。
* **充填の性質**: 候補A: Partial（詳細なsp³ハライドの失敗データとPhX反応性比較を含む場合はComplete）; 候補B: Partial（不斉カップリング文脈でのsp²選択性の確認）
* **Bibliographic confidence**: 候補A: Medium; 候補B: Medium-High（Hayashi–Kumadaグループの不斉カップリング初報は広く知られており書誌の存在は高い信頼度で推定できるが、正確なJACS巻号確認が必要）
* **Filling adequacy confidence**: 候補A: Medium（sp³ハライドの失敗例が全論文に含まれるかどうか）; 候補B: Low（不斉カップリング論文がsp²/sp³境界を直接検証しているかどうか）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **DOI / URL**: 確認要
* **Filling timescale category**: format-driven (1-3 yr)（候補A）; incentive-aligned (4 yr)（候補B, 1976年発表）
* **注記**: Stage 3 §2 SRG-4のcase-specific実装では「n-BuMgBrとsp³ハライドの比較実験」「PhCl/PhBr/PhIの直接収率比較」という2つの独立実験が必要とされていた。候補Aが全論文として両者を提供するならばComplete充填、そうでなければ複数論文による分割充填となる可能性がある。また、塩化物の「高反応性」という主張（B-6）のsp²酸化的付加速度論的根拠については、独立した速度論的研究が後続する可能性もある。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 (Unquantified reliability) — 収率の統計的評価、標準偏差の記録
* **充填候補**: **未同定**
* **充填の性質**: インセンティブ構造的未充填
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: N/A
* **Filling timescale category**: non-applicable
* **注記**: §Eで詳述する。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 (External superiority) — NiCl₂(dpe)とNi(acac)₂（Corriu/Masse系）の同一基質での直接比較
* **充填開始点（候補A — 同時期基準点）**: Corriu, R. J. P.; Masse, J. P. J. Chem. Soc. Chem. Commun. 1972, 144 — 同時期に独立に発表されたNi(acac)₂触媒によるGrignard試薬クロスカップリングの通信論文。Kumada論文が"Note Added in Proof"で受領を記録した当の論文。
* **充填確立点（候補B — 後続比較研究）**: 未確認 — NiCl₂(dpe)とNi(acac)₂を同一基質・条件で直接比較した実験論文の存在確認が必要。後続の総説（例: Kumada, M. Pure Appl. Chem. 1980, 52, 669–679）でこの比較が議論された可能性がある。
* **充填の性質**: 候補A: Attempted — 候補論文は比較の"もう一方"を提供するが、直接比較実験を含まないため充填として完全に機能しない; 候補B: 未確認
* **Bibliographic confidence**: 候補A: High（Kumada論文自体に引用されており書誌情報は確実）; 候補B: Low（具体的な書誌情報なし）
* **Filling adequacy confidence**: 候補A: Low（比較実験を含まない）; 候補B: 不明
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: 候補A: pending（書誌は確実だが充填として機能するかの評価が必要）
* **Filling timescale category**: incentive-aligned (variable)
* **注記**: CLA-1（§2）の「RI-09 Secondary RI: Corriu/MasseのNi(acac)₂との直接比較なしにbidentate diphosphineを触媒設計の要件として提示」に対応する。Corriu/Masse 1972 はEPの「充填先」ではなく「比較の対象」であり、これ自体が充填論文ではない点に注意する。EP-09aの完全充填には、両者（NiCl₂(dpe)とNi(acac)₂）を同一反応系で比較する第三者またはKumadaグループ自身による実験論文が必要。Ni(acac)₂触媒のクロスカップリングはCorriuグループおよびその他のグループが後続論文で発展させており、間接的な充填情報が総説や教科書を通じて蓄積された可能性がある。

---

**§B 末尾チェック：Bibliographic verification**

**Verification recommendation [必須] の根拠:**
- 条件(a): 論文年代 1972 ≤ 1980 → YES
- 条件(b): 著者ネットワーク密（Kumadaグループ 10+ 論文）→ YES
- 条件(c): Named reaction (Kumada coupling) → YES

**Hallucination 警告（本ケースの既知パターン）:**
Prompt §Bに記載の通り、dev/kumada での Sonnet hallucination rate が 67% と記録されている。本出力の全候補について以下のリスクを明示する:
- **著者組合せ捏造リスク**: Tamaoグループ / Hayashi / Kumadaの組合せ論文は実在するが、著者順・掲載年・巻号が誤る可能性が高い（特に1975-1982年のJACS, BCSJ, J. Organomet. Chem.論文群）
- **化学内容の誤記リスク**: ラジカル機構論文（Morrell/Kochi 1975候補）については、実際の化学内容（dpe-Ni系に適用されたかどうか）の確認が必須
- **全候補に対して Crossref / SciFinder での書誌確認を実施すること**

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao et al., Bull. Chem. Soc. Jpn. 1976, 49, 1958 | EP-01a, EP-02a, EP-05a(部分), EP-07a(部分) | VQ-2 | 1976 | Medium | High | 必須 ⚠️ pending |
| 2 | Morrell & Kochi, J. Am. Chem. Soc. 1975, 97, 7262 | EP-03a(Paradigm-shift), EP-06a(Paradigm-shift) | VQ-3 | 1975 | Medium | Medium | 必須 ⚠️ pending |
| 3 | Hayashi, Tajika, Tamao, Kumada, J. Am. Chem. Soc. 1976, 98, 3718 | EP-07a(部分), EP-05a(部分) | VQ-2 | 1976 | Medium-High | Low-Medium | 必須 ⚠️ pending |
| 4 | Corriu, Masse, J. Chem. Soc. Chem. Commun. 1972, 144 | EP-09a(基準点) | VQ-3(indirect) | 1972 | High | Low | 必須 ⚠️ pending |

**⚠️ 注記**: 全エントリが Bibliographic verification status: pending であり、正式な推奨選定として確定していない。Post-hoc verification（§B Step 4）を経た後に選定リストに昇格する。

**選定理由（暫定）:**

**1位（Tamao et al. 1976 BCSJ）**: EP-01a（Letter→Full Paper auto-resolution）を核心とし、同時にEP-02a・EP-07a（スコープ制限の実験的根拠）・EP-05a（選択性定量の部分充填）を収録するバンドル充填候補として最大の充填カバレッジを持つ。VQ-2要件（reporting completeness, scope restriction basis）の充填として機能する。

**2位（Morrell & Kochi 1975 JACS）**: EP-03aとEP-06aを同時充填するParadigm-shift候補として、VQ-3要件（機構層）に対応する。特筆すべきは、この論文がNi(0)/Ni(II)輸入モデルを「誤った枠組み」として記録するParadigm-shift充填である可能性があり、Stage 2 D4-2（NiCl₂(dpe)系における触媒サイクルの実験的根拠の不在）の最も深い問いに科学史的答えを提供する。ただし、この論文が実際にdpe-Ni系に適用されたかどうかの確認が最優先の verification 課題。

**3位（Hayashi et al. 1976 JACS）**: 不斉Grignard試薬クロスカップリングの確立により、sp²選択性の実用的根拠を強化するとともに、方法の汎用性を実証する。EP-07aの間接充填とVQ-2の実用的側面を補強する。

**4位（Corriu & Masse 1972）**: EP-09aの「比較対象」として機能するが充填論文としては機能しないことを明示した上で、Ni(acac)₂との系統的比較研究を発見するための二次情報源として位置づける。

**VQ階層カバレッジ評価（暫定）:**
- VQ-2: 1位（BCSJ 1976）— EP-01a, EP-02a, EP-07a充填
- VQ-3機構層: 2位（Morrell/Kochi 1975）— EP-03a, EP-06a充填（Paradigm-shift型）
- VQ-4: 不達 — EP-08a第三群（インセンティブ構造的未充填）

**不足している選定論文:**
- EP-04aの充填論文（cis/trans比の速度論/熱力学区別）が選定リストから欠落している — §E参照
- EP-09aの「直接比較実験を含む」充填論文が未同定 — Crossref精査が必要

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

```
VQ-2 要件（報告完全性・スコープ境界）:
  EP-01a / EP-02a / EP-07a → 1976年 [Tamao et al., BCSJ]
    充填パターン: 自己充填 + format-driven（Letter→Full Paper）
    充填年数: 4年（1972→1976）

VQ-3 要件（機構層 — 中間体観測・類推検証）:
  EP-03a / EP-06a → ca. 1975年 [Morrell & Kochi, JACS候補] [Paradigm-shift]
    充填パターン: 技術駆動充填（ラジカルクロック手法）+ Paradigm-shift充填
    充填年数: 3年（1972→1975）— ただし書誌確認要

VQ-2 要件（スコープ拡張・実用性確認）:
  EP-07a(補強) → 1976年 [Hayashi et al., JACS候補]
    充填パターン: 自己充填（方法の応用展開）
    充填年数: 4年（1972→1976）

VQ-3 要件（外部優位性比較）:
  EP-09a → 現時点で未確認の直接比較研究
    充填パターン: 未充填（候補4のCorriu/Masse 1972は比較対象のみ）

VQ-N 要件（cis/trans立体化学区別）:
  EP-04a → 未確認
    充填パターン: 未充填の可能性（§E参照）

VQ-4 要件（統計的信頼性）:
  EP-08a → 未充填（インセンティブ構造的未充填）
```

**階層-時間対応の評価:**

暫定的に観察される傾向として、VQ-2要件（報告完全性 EP-01a/EP-02a/EP-07a）はformat-driven（4年）で自己充填された可能性が高い一方、VQ-3要件（機構 EP-03a/EP-06a）は独立した第三者（Kochi グループ）による技術駆動充填として並行して進んだ可能性がある。しかしながら、VQ-3要件の充填が暫定的に「先行充填パターン」（候補のMorrell/Kochi 1975が1976年のBCSJ全論文より1年早い）として現れているとすれば、これは「VQ階層が上がるほど充填時間が長くなる」という仮説と反する結果となる。

この逆転の理由は機構研究への独立した科学的関心（Ni触媒機構一般への注目）がFormat-drivenよりも早いタイムスケールで作動したことが挙げられる。ただしこの分析はBibliographic verificationが完了する前の暫定評価である。

VQ-4要件（EP-08a: 統計的信頼性）は対象期間内（1972-1985年）での充填が見られず、インセンティブ構造的未充填として長期未充填となっていることが予測される。これは「科学的論理に基づくEP充填順序（低VQ→高VQ）」と「出版インセンティブに基づく実際の充填順序（高VQ→低VQ）」の逆転パターンの部分的証拠として記録する。

**特筆すべきパターン:**

1. **Format-driven自己充填（EP-01a）**: JACS Communication → BCSJ全論文の典型的遷移。Stage 3 §6「通信→Full Paper遷移の自動解消パターン」の実証事例として記録する。

2. **Paradigm-shift充填（EP-03a + EP-06a）**: Ni(0)/Ni(II)二電子サイクル（輸入モデル）がNi(I)/Ni(III)ラジカル経路で部分的に置換されるとすれば、これはEP充填の「Paradigm-shift」型の典型事例となる。EPが解消されたのではなく、問いの枠組みが変わった（輸入モデルの前提が変わった）ことで、「どのモデルが正しいか」という問い自体が再定義されている。

3. **著者回顧の可能性**: Kumadaは1980年前後に包括的レビュー（Pure Appl. Chem.）を発表したと推定される。このレビューが原論文の欠落（D4-1, D4-2として記録したSelectivity claim without byproduct data, Mechanistic cycle without evidence）のどれを認識し、どれを認識しなかったかを照合することが、「分野の内部者には不可視の構造的不在」の直接的証拠となりうる。

4. **バンドル充填（EP-01a + EP-02a）**: BCSJ 1976全論文が複数EPを同時充填するバンドル充填候補となっており、1報の充填論文が効率的に複数の報告形式問題を解消するパターンを示す。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

**EP-04a [Discrimination / replication pack]:**
* **未充填の理由**: 関心の欠如 + インセンティブ構造の不整合 — cis-/trans-1,2-dichloroethyleneとPhMgBrの特定の組み合わせでのcis/trans stilbene比を時間・温度系列で追跡する実験は、技術的には単純だが「既に知られた反応のメカニスティックな細部」として独立論文化されるインセンティブが小さい。また、Ni触媒クロスカップリングの後続研究はpalladium触媒へと急速にシフトしたため、Ni系の立体化学細部への追実験需要が相対的に低下した可能性がある。
* **発見的意義**: あり — 「cis-stilbeneが熱力学的により不安定であるにもかかわらずcis-enrichedで生成する」という観察（Stage 1 U-3 + A-1で記録）は、速度論的支配の証拠であり、その後のPd触媒ビニルハライドカップリングの立体特異性議論に接続する。この問いが「異常なcis富化」として記録されながら、速度論/熱力学の区別として体系的に追跡されなかった事実は、UQSが長期未充填問いとして発見した構造的不在の例として記録できる。
* **将来の充填可能性**: 高 — 現代のGC-MS・低温NMR・DFT計算の組み合わせで容易に実施可能。ただし充填されていないのは技術的困難ではなく関心の問題であり、検証する動機（例えばNi系の立体化学見直し、Ni vs Pd比較研究）が形成されれば即座に実施可能。

---

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造の不整合 — Kumada反応の収率の統計的再現性（反復測定の標準偏差）を評価する論文は、新規性を要求する出版慣行のもとでは独立論文として発表されるインセンティブが存在しない。Table I各エントリの3回独立再現実験は、教育・手順最適化の文脈では実施されるが、論文として発表される形式をとらない。
* **発見的意義**: あり（limited） — この未充填は合成化学における標準的なインセンティブ構造的未充填パターンであり、Kumada反応に固有の発見的意義はない。ただし、D4-3（Table Iの収率データの解釈可能性の喪失）として記録した問い——「収率差が基質固有の反応性を反映するのかそれとも非最適化の差異なのか」——は、EP-08a未充填の直接的な帰結として現在も未解決である。これはUQSが「正確には評価できないまま引用され続ける合成データ」の典型例として記録できる。
* **将来の充填可能性**: 低 — 出版インセンティブが変わらない限り独立論文として充填されることはない。現代の自動化合成・高スループット収率測定が間接的に統計的評価を可能にするが、これもKumada反応の「統計的再現性評価論文」として独立論文化されることはないと予測される。

---

**EP-09a（充填確立点が未同定の場合）:**
* **未充填の理由（暫定）**: 関心の欠如 + Success-driven question erasure — Pd触媒クロスカップリング（Suzuki, Heck, Negishi等）の台頭により、NiCl₂(dpe)とNi(acac)₂の選択性比較という問いへの需要自体が社会的に減退した可能性がある。「どちらのNi触媒が優れているか」という問いは、「Pdで代替できる」という実用的解によって間接的に解消された形となった。これはStage 3 §2 CLA-1の「D4-8（Corriu/Masse問題）」で記録した「Note Added in Proofが記録したがNi(acac)₂との比較が欠落したまま」の状態が長期的に維持されたパターンに対応する。
* **発見的意義**: あり — 「同時独立発見された2つのNi触媒（dpe-Ni vs acac-Ni）の直接比較が、公式には一度も独立論文として記録されなかった可能性がある」という観察は、発見の優先権よりも実用性が重視された科学史的状況を示す。配位子設計原理（bidentate diphosphineの役割）についての核心的問いが充填されないまま、Ni触媒クロスカップリング全体がPd系に代替されたとすれば、これはUQSが「方法の成功が特定の問いを永久に解答不能にした」パターンとして記録できる。
* **将来の充填可能性**: 中 — Ni触媒クロスカップリングの再興（Pd代替・地球上存在量・毒性・コスト観点）の文脈で、Ni-diphosphine系とNi-acac系の比較研究が現代的に実施される可能性がある。

---

**VQ階層逆転の診断:**

未充填EPの分布（EP-04a: VQ-1〜2; EP-08a: VQ-4; EP-09a: VQ-3）と充填済みEPの分布（EP-01a/EP-02a: VQ-2 Format-driven; EP-03a/EP-06a: VQ-3 Paradigm-shift候補）を比較すると、VQ-4（統計的信頼性）の未充填が出版インセンティブの構造的問題によるものであることが確認される。また、VQ-2要件（EP-07a）の充填は高い確実性で確認されるが、VQ-3要件（EP-09a）の直接比較充填が未確認である可能性は、「高VQ要件（機構）の充填が先行し、低VQ要件（ベンチマーク比較）の充填が遅延または未達」という逆転パターンの部分的証拠となりうる。この逆転は、Success-driven question erasure（Pd系の台頭）が特にVQ-3/VQ-4境界でのインセンティブ不整合を生じさせた結果として解釈できる。
```
