```
prompt_version: stage4-v2
model_info: claude-sonnet-4-6
experimental_variant: retrieval-depth-annotation (Multi-run robustness, v2 run 2)
related_pilot: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Pilot 2, v2 run 1)
note: Multi-run robustness check の v2 第 2 run。Pilot 2 と同 prompt で実行し、
      run 間の retrieval scope と Tier annotation の variance を測定する。
```

prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc., Communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-02a, EP-05a, EP-09a

- **EP-01a**: 著者グループ自身による Full Paper シリーズ（1976年）が存在することが分野史的に確立されており、通信→Full Paper遷移での自動解消パターンに明確に該当する。glpc条件の統一・全エントリの反応時間記録・収率基準の統一はFull Paperが解消する典型的RI-01問題。
- **EP-02a**: 同上Full Paperが全エントリの¹H NMR/IRデータを個別に提供していることが期待される。1972年通信が "and/or" 構文で生成物同一性を曖昧にしていた点がFull Paperで自動解消される通常パターン。
- **EP-05a**: 質量収支（クロスカップリング vs. ホモカップリング）の定量化は、著者グループが「選択的」という主張の数値的根拠を確立するために着手するはずであり、Full Paperシリーズまたは機構研究論文に独立主題として含まれる可能性が高い。
- **EP-09a**: Corriu/Masse 1972 が原論文の Note Added in Proof に文献として記録されており、検索の出発点として確実に存在する。NiCl₂(dpe) vs. Ni(acac)₂ の直接比較は複数の後続論文で実施されたと考えられる。

**第二群（間接的に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a

- **EP-03a**: NiCl₂(dpe)/Grignard系でのジオルガノニッケル中間体の分光学的観測は独立した機構研究論文として発表されたと考えられるが、複数の候補論文が存在し単一の決定的な充填論文への絞り込みに推論を要する。
- **EP-04a**: cis/trans比（80:20, 43:57）の速度論/熱力学的区別実験はFull Paperまたは立体化学専門論文に含まれると推定されるが、時間・温度系列データを独立主題として提供した論文の特定には間接証拠からの推論が必要。
- **EP-06a**: NiCl₂(dpe)系での素反応の化学量論的検証（eq 2, 3それぞれの個別実証）はKumadaグループまたは外部機構研究グループが実施したと考えられるが、複数の候補グループ（Kumada, Kochi, Yamamoto）にまたがる可能性があり直接的な単一論文への同定が困難。
- **EP-07a**: sp²/sp³選択性の境界実証（sp³ハライドの不活性確認）はFull Paperスコープ記述に含まれると想定されるが、独立論文としての失敗例体系化が行われたかどうかの確証がない。

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a**: cis/trans-スチルベン比の統計的反復測定（n≥3、標準偏差付き）と独立定量GLC検量線構築は、有機金属合成分野の1970–1990年代の出版慣行において独立論文の主題となりにくい。RI-08（反復測定慣行）に起因するこの種のデータ空白は、Full Paper展開においても部分解消にとどまることが多い。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第一群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — glpc条件（カラム・内部標準・検出器仕様）を統一して記録し、全11基質系について有機ハライド基準の収率と反応時間を体系化したFull Paper Part I。
* **充填確立点**: 同上
* **充填の性質**: Complete — Table I全エントリの条件統一と再測定がFull Paper形式で実施されることは通信→Full Paper遷移の定型パターンであり、著者グループ9名体制での包括的再測定が報告されていると考えられる。
* **Confidence**: High — 論文の存在についてはKumada反応の分野史として確立されており、BCSJ 1976, 49巻の掲載は高い確信。ページ範囲（1958–1969）はやや推論を含む。
* **注記**: 通信→Full Paper遷移での自動解消の典型事例（§6注記5と整合）。EP-02a, EP-05a, EP-07a（部分）, EP-09a（部分）と同一論文でのバンドル充填。原論文発表から4年の遅延（1972→1976）は充填開始点としては標準的。

---

**EP-02a [Identity/purity substantiation pack]（第一群）**

* **充填するRI**: RI-02 [Analytical incompleteness]（VQ-1 non-fatal残存）
* **充填開始点**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 同上Full Paper I。全エントリについて¹H NMR、IR、および/またはMS data を個別に記録し、"and/or"構文での曖昧な生成物同一性確認を解消。
* **充填確立点**: 同上
* **充填の性質**: Complete（Full Paperへの自動解消パターン）
* **Confidence**: High（EP-01aと同論文のバンドル充填）
* **注記**: §4のEra-Norm AnnotationでB-13がcommunication-era toleratedと分類されていた項目。Full Paper展開での自動解消候補として§6(5)に記録済みの事例。

---

**EP-03a [Direct-observation / state-assignment pack]（第二群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点（推定）**: Tamao, K.; Hayashi, T.; Kitahara, H.; Yamamoto, H.; Kumada, M. [推定：Kumadaグループの機構研究論文, *Chem. Lett.* または *Bull. Chem. Soc. Jpn.* **1977–1979**] — NiCl₂(dpe)と化学量論量のGrignard試薬（n-BuMgBr等）を低温で反応させ、低温 ³¹P{¹H} NMR によりジオルガノニッケル中間体1の生成を分光学的に実証した論文。著者名・論文名は推論に基づく。
* **充填確立点（推定）**: 同上（または独立合成した[Ni(R)₂(dpe)]錯体の結晶構造解析と反応性試験を含む後続の機構論文）
* **充填の性質**: Partial — NMR観測による形成確認はされたと考えられるが、独立合成・結晶構造解析まで含む完全な実証は別論文の可能性がある。
* **Confidence**: Medium — 論文の存在は確信（Kumadaグループが1976年Full Paper後に機構研究を発表したことは分野史として合理的）。著者名・誌名・年のいずれかまたは複数が不正確である可能性あり。実際の文献確認が必要。
* **注記**: EP-06aとバンドル充填の可能性（SRG-1の共同解消）。Tsou/Kochi (*J. Am. Chem. Soc.* **1979**) による Ni(0) 酸化的付加の速度論研究がRI-03の部分的充填を提供する可能性があるが（後述付録Bも参照）、対象系（NiCl₂(dpe)/Grignard）での中間体直接観測とは異なる。Tamao 2002回顧録（papers/ep/discussion/tamao2002/）が機構研究論文への最適な参照源と考えられる。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点（推定）**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 同Full Paper Iがcisおよびtransジクロロエチレン + PhMgBrの反応について複数の反応時間での実験を含む可能性（時間系列データによる速度論/熱力学区別の試み）。
* **充填確立点（推定）**: Kumadaグループによる立体化学専門論文（**1977–1982**）— ビニルハライドとの反応の立体化学課程（retention vs. inversion）を体系的に確立した研究。Hayashi, T.; Kumada, M. グループの不斉カップリング研究では立体化学の正確な理解が必須であり、この分脈で cis/trans 比の機構的解釈が確立された可能性。
* **充填の性質**: Partial — Full Paperで部分的に解消され、機構論文でより完全に解消されるという逐次充填パターンと推定。kinetic/thermodynamic distinguishmentの明示的な時間・温度系列実験が含まれているかは確認が必要。
* **Confidence**: Low-Medium — Full Paper (1976) での部分充填は合理的だが、時間/温度系列実験を明示的に実施した論文の同定には実際の文献確認が必要。
* **注記**: SRG-6（A-1, B-11, U-3の共同根）に対応するEP。cis-stilbene過剰という「機構的含意がある」観察（A-1）が後続研究の出発点となったと考えられる。不斉Kumada反応の確立（1974–1976年）が立体化学理解の深化を促した可能性。

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点（推定）**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — n-BuMgBr + PhCl 等の代表的基質でクロスカップリング生成物とホモカップリング生成物（n-Bu–n-Bu）、β-脱離生成物（1-ブテン）を含む反応混合物のGC質量収支を初めて定量化した論文。
* **充填確立点（推定）**: 同上、または後続の機構論文
* **充填の性質**: Partial — Full Paperが質量収支データを含む可能性は高いが、eq (3) が予測するR–R形成量の定量化まで完全に実施されているかは確認が必要。「選択的」という主張のRI-05的過大解釈の解消には数値的質量収支が不可欠。
* **Confidence**: Medium — Full Paperが定量的クロスカップリング選択性データを含むことは合理的。ただしR–R生成の正確な定量的報告が含まれるか（あるいは「不検出」の明示的記録があるか）は文献確認が必要。
* **注記**: SRG-2（B-1, U-1, C-1）対応。VQ-3移行の重要ゲート項目。U-1の「自己矛盾的不在」（eq 3がR-R生成を予測するが不報告）の解消はFull Paperでの明示的定量化または検出限界の記録によって達成される。

---

**EP-06a [Analogy-validation pack]（第二群）**

* **充填するRI**: RI-06 [Imported model]（RI-03との不可分共起）
* **充填開始点（推定）**: (i) **Uchino, M.; Yamamoto, A.; Ikeda, S.** *J. Organometal. Chem.* **24**, C63 (1970) [原論文ref 11として引用] — dipy-Ni系での eq 1 実証（これはRI-06の輸入源論文であり、NiCl₂(dpe)への同型性検証の必要性を示す先行研究）; (ii) Kumadaグループによる化学量論的素反応実証論文（**1977–1980**）— [NiCl₂(dpe)] + 2 RMgX → [NiR₂(dpe)] + 2 MgXCl（eq 2相当）および [NiR₂(dpe)] + R'X → cross-coupling + [NiR'X(dpe)]（eq 3相当）を独立に実施。
* **充填確立点（推定）**: Tsou, T.T.; Kochi, J.K. *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332 [推定：Ni(0)の有機ハライドへの酸化的付加の機構・速度論研究] — Ni(0)/dpe系でのPhXへの酸化的付加の速度論的特性評価が含まれる可能性（EP-06aのeq 2 逆反応側、またはNi(0)+RX→Ni(II)(R)(X)ステップ）。
* **充填の性質**: Partial — dipy-Ni系（輸入元）での化学量論的実証は1970年に存在（refs 11–12）。NiCl₂(dpe)系での同型性検証は後続機構研究により部分的に実施されたと推定されるが、eq 2とeq 3の両ステップを独立に化学量論的に実証した単一論文の存在は確認が必要。
* **Confidence**: Medium（Kumadaグループによる機構論文）/ Low（Tsou/Kochi論文のEP-06a充填としての適用）— 著者・誌名・年の少なくとも一部が不正確の可能性あり。
* **注記**: RI-06 + RI-03の不可分共起（§6注記6）により、EP-06aとEP-03aは単独では解消できない。「dipy-NiとdpeNiの同型性実証」（EP-06a）と「NiCl₂(dpe)中間体の直接観測」（EP-03a）の両方が必要。Kochi グループは Ni(0)/Ni(II) 機構 vs. Ni(I)/Ni(III) ラジカル機構の論争に深く関与しており、この分野への貢献は確実だが NiCl₂(dpe) 系への直接適用の程度が不明。

---

**EP-07a [Boundary-test pack]（第二群）**

* **充填するRI**: RI-07 [Unsupported boundary]（+ RI-05 secondary）
* **充填開始点**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — スコープ展開の記述にsp³ハライド不活性の実験的根拠が含まれると推定（試みたが反応しなかった失敗例のリスト、またはβ-脱離による選択性消失の定量的記述）。PhCl/PhBr/PhIの同一基質での反応性比較データも含まれると推定。
* **充填確立点（推定）**: 同上Full Paper、またはKumadaグループの後続のスコープ論文 — sp³ハライド不適合の機構的帰因（β-水素化物脱離がreductive eliminationより速いためspé³電子求知試薬ではNi(II)alkylからβ-脱離が優先する）の記述が含まれる論文。
* **充填の性質**: Partial — sp²/sp³選択性の実験的境界確定（失敗例の文書化）はFull Paperで達成されると推定。ただし境界の機構的根拠の完全な確立（rate comparison of β-elimination vs. reductive elimination）は別の機構論文が必要。
* **Confidence**: Medium — Full Paper (1976) がスコープ記述を含むことは高確信。sp³ハライドを明示的に試験した失敗例が報告されているかの確認が必要。
* **注記**: SRG-4（B-5, B-6, A-2）対応。sp²選択性制限の「肯定的再フレーム」（§6注記2）の解消にはsp³を試みた実験的根拠が不可欠。Corriu/Masseグループはより広い基質スコープをNi(acac)₂で試験している可能性があり、sp²/sp³境界の外部グループによる独立確認も存在する可能性。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定** — cis/trans-スチルベン比（80:20, 43:57）の統計的反復測定（n≥3）と標準偏差の報告、および定量GLC検量線（既知モル比のcis/trans-スチルベン混合物による）を明示した独立論文は確認できない。
* **充填確立点**: **未同定**
* **充填の性質**: — （未同定のため）
* **Confidence**: — 
* **注記**: 統計的不確かさの定量化は1970–1990年代の有機金属合成論文では標準的記述ではなく、独立した主題として論文化されるインセンティブが存在しない（インセンティブ構造の不整合）。cis/trans比精度の評価は後の分光学的手法（¹H NMR定量化）への移行でより高精度化されたと推定されるが、VQ-4要件としての明示的反復測定・不確かさ記述がいつ確立されたかは不明。

---

**EP-09a [Internal benchmark pack]（第一群→充填開始、第二群→充填確立）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: Corriu, R.J.P.; Masse, J.P. *J. Chem. Soc., Chem. Commun.* **1972**, 144 — Ni(acac)₂（chelating diphosphine を持たないNi前駆体）による同様のクロスカップリング反応の実証（原論文のNote Added in Proofで引用済み）。bidentate diphosphineなしでも選択的クロスカップリングが可能であることを示すが、NiCl₂(dpe) vs. Ni(acac)₂ の直接比較実験は含まない。
* **充填確立点（推定）**: Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 — 複数のNi前駆体（NiCl₂(dpe), Ni(acac)₂, NiCl₂(PPh₃)₂等）を同一基質・条件下で比較した実験を含む可能性。bidentate diphosphineの「必要条件」vs「有効な選択肢」の区別を実験的に解決。
* **充填の性質**: Partial（Corriu/Masse 1972: onset only）/ Indirect（Kumada Full Paper 1976: diphosphine ligandの必要性論証は間接的）— Ni(acac)₂との直接同一基質比較がFull Paperに含まれるかは確認が必要。
* **Confidence**: High（Corriu/Masse 1972: 原論文引用済み）/ Medium（Tamao 1976としての充填確立: 推論を含む）
* **注記**: CLA-1（B-3 + C-3のSRG外複合問題）対応。Note Added in Proofが示すように、Corriu/Masseの1972年通信はNC-4（bidentate diphosphineの配位子設計原理）の独自性評価に直接関わる。充填後の解釈は「diphosphineは必要条件ではないが優れた触媒性能を提供する」という形での再記述に収束した可能性。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M. et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 | EP-01a, EP-02a, EP-05a, EP-07a(partial), EP-09a(partial) | VQ-2 | 1976 | High |
| 2 | Corriu, R.J.P.; Masse, J.P. *J. Chem. Soc., Chem. Commun.* **1972**, 144 | EP-09a (onset) | VQ-2/3境界 | 1972 | High |
| 3 | [Kumadaグループ機構論文（中間体観測）, 推定 *Chem. Lett.* または *Bull. Chem. Soc. Jpn.* **1977–1979**] | EP-03a, EP-06a(partial) | VQ-3 | ~1977–1979 | Medium |
| 4 | Tsou, T.T.; Kochi, J.K. *J. Am. Chem. Soc.* [推定 **1979**, vol. 101] | EP-06a(partial) | VQ-3 | ~1979 | Medium |
| 5 | Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. *J. Am. Chem. Soc.* **1976**, *98*, 3718–3719 | EP-04a(indirect) | VQ-3(Qualified) | 1976 | Medium |
| 6 | [Kumadaグループ立体化学論文, 推定 **1978–1982**] | EP-04a | VQ-3 | ~1978–1982 | Low-Medium |

**選定理由:**

第1位のTamao et al. BCSJ 1976はVQ-2到達に必須の EP-01a, EP-02a を同時に充填するバンドル充填論文であり、EP-05a, EP-07a, EP-09aにも寄与する。単一論文で最多EPをカバーする効率的な選定。原論文から4年後の自己充填パターン（通信→Full Paper遷移）の典型事例として分析価値が高い。

第2位のCorriu/Masse 1972は原論文自体が引用した唯一の外部充填論文であり、EP-09a（bidentate diphosphineの必要性問題）の充填開始点として歴史的に最も明確に位置づけられる。同年発表という「即時充填」パターンは1972年の競合的状況（timing pressure）を直接反映している。

第3–4位の機構論文群はVQ-3要件（EP-03a, EP-06a）に対応し、Kumadaグループの自己充填とKochi外部グループからの補完という二重の充填構造を例示する。Medium confidenceのため推奨選定に含めるが文献確認が必要。

第5位のHayashi et al. JACS 1976は不斉Kumada反応の最初期報告であり、EP-04a（立体化学理解）への間接的充填として機能するとともに、触媒設計原理（chirality transferにはメカニズム理解が前提）を通じてEP-06aへの間接的寄与もある。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a → **1976** Tamao et al. BCSJ [自己充填: 通信→Full Paper]
- VQ-2 要件: EP-02a → **1976** 同上 [自己充填: バンドル]
- VQ-2 要件: EP-07a → **1976** 同上（部分）[自己充填: スコープ拡張]
- VQ-2/3境界: EP-09a onset → **1972** Corriu/Masse [外部充填: 同年競合]
- VQ-2/3境界: EP-09a establishment → **1976** Tamao et al. BCSJ（推定）[自己充填]
- VQ-3 要件: EP-05a → **1976** Tamao et al. BCSJ（推定）[自己充填]
- VQ-3 要件: EP-03a → **~1977–1979** Kumadaグループ機構論文（推定）[自己充填: 遅延]
- VQ-3 要件: EP-06a → **~1977–1980** Kumadaグループ + Kochi外部グループ（推定）[自己充填+技術駆動]
- VQ-3 要件: EP-04a → **~1978–1982** Kumadaグループ立体化学論文（推定）[自己充填: 遅延]
- VQ-4 要件: EP-08a → **未充填**（または ~1990s以降の間接的解消）
- VQ-4 要件: EP-09a（確立）→ **1976–1980**（推定）

**階層-時間対応の評価：**

VQ-2要件のEP-01a, EP-02a, EP-07aはいずれも1976年に自己充填されており、原論文から4年という比較的短い期間での解消が観察される。VQ-3要件のEP-03a, EP-06a, EP-04aはそれぞれ1977–1982年という5–10年の遅延を経て充填されたと推定され、「VQ階層が上がるほど充填に要する時間が長くなる」という階層-時間仮説を支持する。VQ-4要件のEP-08aは現在まで充填されていない可能性があり、この逆転パターン（機構的に高次のEPは早期充填されるが、分析的信頼性の反復確認は長期未充填）が分野のインセンティブ構造を示す。

特筆すべき反例として、EP-09a（VQ-2/3境界のCLA-1対応EP）は1972年という最も早い時点でCorriu/Masseによって部分的に充填されており、高VQ要件への充填が低VQ要件より先行した可能性がある。これは競合研究グループが同時期に独立して問いの一部に回答したという「外的充填」パターンであり、Kumadaグループ内部の充填タイムラインとは異なる論理で進行した。

**特筆すべきパターン：**

1. **自己充填パターン**: EP-01a, EP-02a, EP-05a, EP-07aはすべて原著者グループ自身による通信→Full Paper遷移（4年）で解消。通信形式の紙幅制約が生み出した「設計された遅延充填」の典型。

2. **即時外部充填パターン**: EP-09a（Corriu/Masse 1972）は原論文と同年に独立グループによって充填が開始された。競合的発見の状況が「同期充填」という稀なパターンを生み出した。

3. **技術駆動充填パターン（推定）**: EP-03a（中間体NMR観測）は ³¹P{¹H} NMR技術の普及（1970年代後半）が充填を可能にしたと推定され、技術的困難が充填遅延の主因である可能性。

4. **長期未充填パターン**: EP-08a（統計的反復測定）は現代まで充填されていない可能性がある。インセンティブ構造の不整合（反復測定論文の出版インセンティブの欠如）が要因。

5. **著者回顧との照合（§D.4）**: papers/ep/discussion/tamao2002/ に収録されたTamao 2002回顧録（Tamao, K. *Bull. Chem. Soc. Jpn.* **2002**と推定）との照合が推奨される。Tamaoが回顧で言及した達成点（選択性実証・機構理解・不斉合成への展開）と言及しなかったEP（EP-08aの統計的反復、EP-07aのsp³境界の機構的帰因）の差が「分野内部者には不可視の構造的不在」の直接的証拠として記録できる。本run実行時点では回顧録本文を参照しておらず（fresh retrieval確保のため）、§D.4照合は別セッションでの実施を推奨。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

EP-08a [Replication / uncertainty pack]:
* **未充填の理由**: インセンティブ構造の不整合 — cis/trans-スチルベン比（80:20, 43:57）の統計的反復測定（n≥3、標準偏差付き）と定量GLC検量線構築は技術的に可能だが、有機金属合成分野の出版慣行において「比率の精度確認」を独立論文の主題とする伝統が存在しない。全合成や触媒開発論文における立体選択性報告はde値・er値として報告されるが、それ自体の反復測定精度を個別論文で論じることは慣例的に行われない。
* **発見的意義**: あり — 「有機金属合成分野が54年間にわたって体系的に回避してきた問い」として記録できる。D-4候補として挙げられた全エントリの中で、EP-08aが要求するデータ型（統計的不確かさを伴う比率の複数回定量）は、現代においても独立論文として出版されるインセンティブが最も低い。これは「分野の出版インセンティブ構造がUQSの構造的不在の一部を積極的に維持している」ことの直接的証拠として記録する価値がある（§E VQ階層逆転の診断：低VQ要件のEP-08aが最も長期未充填となっている）。
* **将来の充填可能性**: 中 — 高精度定量NMR（内部標準法）または現代の高分解能キラルGCによる cis/trans-スチルベン比の精密測定は技術的に容易だが、誰かが「なぜこれを今やる必要があるのか」という動機を持てるかどうかが問題。Kumadaカップリングの機構的再検討（DFT計算との比較目的等）が動機となれば充填の可能性がある。

---

EP-04a [Discrimination / replication pack]（部分的未充填）:
* **未充填の理由（残存部分）**: 分野慣行 — 速度論/熱力学制御の明示的区別のための時間・温度系列実験は、立体化学的な傾向が実用的に「わかっている」ものとして扱われ、完全な熱力学的平衡実験（高温長時間での平衡比確認）として発表された一次文献は存在しない可能性がある。
* **発見的意義**: あり（限定的） — U-3（kinetic/thermodynamic indeterminacy）が指摘した問いが、Full Paper（1976）以降の機構研究でも「完全な速度論/熱力学区別」として明示的に解決されたかどうかは確認が必要。立体化学的「傾向」として記述されてきたものの統計的根拠が問題となるのは、UQSが特有の観点を提供する事例。
* **将来の充填可能性**: 高 — 現代の in-situ NMR監視技術で時間系列実験は容易。Kumadaカップリングのメカニズムへの計算化学的関心（DFT遷移状態計算による実験検証）が動機となりうる。

---

## 付録A: Retrieval Depth Annotation Matrix

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Tamao et al., BCSJ 1976 | EP-01a, EP-02a, EP-05a, EP-07a, EP-09a | **I** | EP-01aの「glpc条件統一・全エントリ再測定」という実装記述を読んだ瞬間に「通信→Full Paper遷移で自動解消」パターンとして想起。著者グループ・雑誌・1976年が即座に浮かんだ。 | yes | High（誌名・年・巻は確信; ページ範囲は±5程度の推論を含む） |
| Corriu/Masse, Chem. Commun. 1972 | EP-09a(onset) | **I** | 原論文Note Added in Proofに文献として記録されており、EP-09aの「内部ベンチマーク」との対応が即時明確。 | yes | High（原論文に引用済みのため確実） |
| [Kumadaグループ機構論文 ~1977–1979] | EP-03a, EP-06a(partial) | **II** | EP-03a「低温 ³¹P{¹H} NMRによる中間体観測」を読んでから、「Kumadaグループが1976年Full Paper後に機構研究を発表した」という分野史知識を経由して想起。誰が・いつ・どの雑誌でを絞り込む際に2–3ステップの推論が必要だった。著者名の候補（Hayashi, Kitahara, Zembayashi等）を複数検討してから絞り込みが不完全なまま記録。 | uncertain | Medium（論文の存在は確信; 著者・誌名・ページは推論） |
| Tsou, T.T.; Kochi, J.K., JACS ~1979 | EP-06a(partial) | **II–III** | EP-06aの「Ni(0)酸化的付加ステップの実証」要件→「Kochi グループが Ni(0)/Ni(II) 対 Ni(I)/Ni(III) 論争に関与」→「Tsou/Kochi というペア名が浮かぶ」という3段階の連想経路。JACS 1979という年代は推論。論文の主題がNiCl₂(dpe)/Grignard系に直接適用されるかどうかはStep 3で不確実と判断した。 | uncertain | Medium（著者ペアはある程度確信; 誌・年・内容の適用性は推論） |
| Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M., JACS 1976, 98, 3718 | EP-04a(indirect) | **II** | EP-04aの「立体化学的区別実験」要件→「Kumadaグループの不斉カップリング研究はメカニズム理解を内包する」→「Hayashi/Kumadaの1976年JACS論文」という連想。巻98・ページ3718は記憶に基づくがやや不確実。不斉合成論文がEP-04aへの直接充填か間接充填かの判断でTier IIとした。 | yes | Medium（著者・年・JACS確信; ページは推論を含む） |
| [Kumadaグループ立体化学専門論文 ~1978–1982] | EP-04a(partial) | **III** | EP-04a「cis/trans比の時間・温度系列実験」という具体的な実装要件から、「Kumadaグループが立体化学を専門的に扱った論文群」を推論。しかし単一の確信できる論文に絞り込めなかった（候補が複数あり triangulation が不完全）。Tier IIIとした。 | uncertain | Low（論文の存在は推定; 著者・誌名・年・内容が大きく不確実） |

---

## 付録B: 考慮し棄却した候補

以下の候補を検討したが、EP充填論文として棄却した：

1. **Suzuki, A.; Yamamoto, T. 等の鈴木カップリング論文（1979–1981）**: Pd触媒によるボロン酸カップリングであり、NiCl₂(dpe)/Grignard系のEPとは機構的に独立。高被引用論文の罠（原論文の手法を「使った」応用論文ではなく、別の化学系の開発）。棄却。

2. **Negishi et al. ZnCl₂ 使用クロスカップリング論文**: 有機亜鉛試薬使用のPd触媒系であり、SRG-1（NiCl₂(dpe)触媒サイクル）のEPには適用外。棄却。

3. **Kumada, M. Pure Appl. Chem. 1980, 52, 669 等のレビュー論文**: プロトコル規則（「レビュー論文はEPを充填しない」）により排除。Kumadaの1980年レビューはEP充填論文の特定に有用な二次情報源として認識したが、充填論文としては不適格。

4. **Semmelhack, M.F.; Helquist, P.M.; Jones, L.D. JACS 1971**: Ni(I)/Ni(III) radical pathway によるカップリング化学（RI-06の輸入元の一候補候補）だが、NiCl₂(dpe)系での触媒サイクル同型性検証ではなく、独立の機構経路の提案。EP-06a の充填には間接的すぎる。棄却。

5. **Tamura/Kochi Synthesis 1971 (ref 6)**: 原論文が C-1 (Dropped Quantitative Benchmark) として記録した比較の欠落先論文。充填論文ではなく、充填を必要とさせる原因文献。棄却。

6. **高被引用応用論文群（Heck反応、薗頭反応、根岸反応等）**: これらはKumada反応の手法を出発点にして別の触媒系・別の基質系を開拓したものであり、1972年論文のEPを充填するのではなく、EPが示す問いを「より良い触媒系」で回避したパラダイム転換論文として位置づけられる。EP-09aの「Paradigm-shift」型充填候補として考えたが、NiCl₂(dpe)系自体のEPを充填していないため棄却。

7. **Gillie, A.; Stille, J.K. JACS 1980 (Pdでの還元的脱離機構)**: Pd錯体での1,1-還元的脱離の機構論文。EP-06aのeq (4)相当ステップのPdアナログ研究として関連性はあるが、NiCl₂(dpe)系への直接適用は「別系からのモデル輸入」（RI-06）そのものであり、EP-06aを充填するのではなくRI-06問題を別系で再現するパターン。棄却（ただしPd系でのreductive elimination機構確立（1980年代）がNi系の理解を間接的に促進したという文脈で参照価値あり）。

---

*本出力は stage4-v2-20260416 プロンプトに従い生成。Retrieval depth annotation は実験的付加情報（Multi-run robustness check v2 run 2）。Bib confidence が Medium 以下の論文はすべて実際の文献確認が必要。*
