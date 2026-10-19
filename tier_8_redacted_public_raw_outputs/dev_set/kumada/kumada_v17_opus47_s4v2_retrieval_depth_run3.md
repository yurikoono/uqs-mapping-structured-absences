```
prompt_version: stage4-v2-20260416
model_info: claude-opus-4-7
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Opus 4.7 v2 run 3)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot 2)
related_baseline_opus: papers/dev/kumada/kumada_v17_opus47_s4v2.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v2 multi-run と GPT-5.4 v2 multi-run と
      比較して Opus 4.7 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc., Communication）

---

### Externalized Thinking Process（retrieval depth 測定のための思考過程記録）

**初期想起（task を読んで最初 30 秒以内）:**

「Kumada 1972 Stage 4」というタスク記述を読んだ瞬間、以下の論文が即座に surface した：

1. **Kumada グループ自身の 1976 BCSJ Full Paper** — 「Kumada coupling 1972 communication の続編」という文脈マーカーで即座に想起。著者列が長い（Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada）ことも記憶として残っている。Tier I。
2. **Corriu-Masse Ni(acac)₂ 1972 論文** — 原論文の Note Added in Proof に明記されているため即時想起。Tier I。
3. **Kochi の Ni 機構研究** — Tsou-Kochi (1979) と Morrell-Kochi (1975) の二報がペアとして surface。「Ni-catalyzed cross-coupling の機構」という連想で第一群に入る。Tier I。

**第二段階の連想（30 秒〜2 分、EP リストを精査）:**

EP-09a（Cl/Br/I 比較）を見て **Foa & Cassar JCS Dalton 1975** が surface。これは「Kochi 単独」では出ず、「Ni 0価酸化的付加の Hammett 速度論」という連想を経由する。Tier II。

EP-07a（C_sp³ 境界）を見て **Knochel/Devasagayaraj 1995 Angew. Chem.** が surface。これは「Ni alkyl-aryl coupling の出発点」という比較的明確な連想で Tier II。さらに **Fu group (2003-)** が「modern Ni alkyl-alkyl」として続く。

**第三段階（triangulation を要する候補、5 分以上）:**

EP-04a の cis-stilbene scrambling specific 論文 — 直接対応する論文は思いつかず、複数候補を考えて棄却するプロセスを経た：「Ratovelomanana の Ni vinyl-coupling stereochem 研究」候補は思い浮かんだが confidence Low。Tier III かつ未同定気味。

EP-06a の β-D 標識実験 in NiCl₂(dpe) — Tier III、specific 論文は同定できず。

EP-05a 配位子比較の体系研究 — Hayashi/Kumada 後続論文に dpp/dpe/dmpe 系統比較があるかを triangulate するも、specific paper の同定に至らず Tier III、Confidence Medium-Low。

**棄却プロセスの記録:**

- **Negishi review 1982 (Acc. Chem. Res.)** — surface したが「レビューは充填しない」プロンプト規則で棄却。
- **Hartwig "Organotransition Metal Chemistry" textbook** — 二次資料として棄却。
- **Tamao 1972 sister communication（hydrosilylation, ref 14）** — 原論文と同号 JACS、別反応のため棄却。
- **Wilke の Ni(0) 化学** — 連想で surface したが Kumada coupling との直接対応なし、棄却。
- **Yamamoto, Yamamoto, Ikeda 1971（ref 11）** — 原論文の引用文献、発表前のため棄却。

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a, EP-09a, EP-10a
- EP-03a：直接観測・状態同定は機構研究の中心であり、Kochi グループの一連の研究が独立論文として存在する。
- EP-04a：cis-stilbene scrambling は単一論文の主題になりうる選択性研究で、Ni vinyl coupling の機構論文に対応する。
- EP-06a：β-H 寛容性の機構研究は同位体ラベル実験を伴い独立論文化されやすい。
- EP-07a：C_sp³ 境界拡張は scope-extension の独立論文として体系的に発表されている（Knochel, Fu 等）。
- EP-09a：Cl/Br/I 比較や Ni(acac)₂ vs NiCl₂(dpe) は Hammett/kinetic 研究として論文化される。
- EP-10a：速度論的検証は機構論文の標準形態であり Tsou-Kochi 系列が直接対応。

**第二群（間接的に追跡可能）：** EP-02a, EP-05a, EP-08a
- EP-02a：純度・同定の基準は Full Paper への展開で部分解消されるが、独立論文の主題ではない。
- EP-05a：配位子順位の定量裏付けは Full Paper および後続の系統研究の一部として現れるが、9 種配位子 × 3 基質ペアの完全 matrix を実施した独立論文は限定的。
- EP-08a：複製・不確かさ報告は Full Paper への展開で部分解消されるが、独立論文化はされない（分野慣行）。

**第三群（充填が見つからない可能性あり）：** EP-01a
- EP-01a：per-entry reporting coherence は Communications フォーマット起因の問題であり、当該論文の Full Paper（Tamao 1976 BCSJ）への遷移で自動解消される性質。独立論文としては存在しないが、Full Paper 形式での充填は明確に存在するため第三群と第二群の境界。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Communications での collapse された 10 エントリ + 2 worked example を、Full Paper 形式で per-entry conditions（mol%, T, t, scale）+ characterization battery として展開。
* **充填確立点**: 同上
* **充填の性質**: Complete（Full Paper 慣行下での per-entry 開示）
* **Confidence**: High
* **Self-classified retrieval Tier**: Tier I (immediate)
* **推論経路**: 「Kumada 1972 + reporting coherence」→ 即座に「同グループの 1976 BCSJ Full Paper」が surface。Communications → Full Paper の自動解消パターンの教科書事例として記憶されている。
* **DB-findable?**: yes — Bull. Chem. Soc. Jpn. 1976 vol 49 のページ番号で直接検索可能。
* **Bibliographic confidence**: High — 著者列の長さ（9 名）、雑誌・年・巻が複数の独立な記憶チャネルから一致して想起される。Verification recommendation: BCSJ archive で実際の page range と DOI を確認推奨（ページ範囲は 1958-1969 と推定、要確認）。
* **注記**: 自己充填パターンの典型例。同論文は EP-02a, EP-05a, EP-08a も同時にバンドル充填する。

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Object identification]
* **充填開始点**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — 全製品の元素分析（C, H）+ NMR + IR + GLPC 純度を per-entry で開示。
* **充填確立点**: 同上
* **充填の性質**: Complete（era-norm 標準下での Full Paper 同定要件を満たす）
* **Confidence**: High
* **Self-classified retrieval Tier**: Tier I (immediate)
* **推論経路**: EP-01a と同じ Tamao 1976 BCSJ への即時想起。Full Paper では EA が標準慣行のため、「1976 BCSJ なら EA 付き」という前提で連結。
* **DB-findable?**: yes
* **Bibliographic confidence**: High（EP-01a と同論文）
* **注記**: SRG-5 の触媒終状態（black mixture / much salt の Ni 同定）は本論文では限定的にしか扱われず、EP-02a の SRG-5 部分は別系統で充填されると予測（後述）。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory], RI-02 [Object identification, SRG-5 部分]
* **充填開始点**: Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* **1975**, *97*, 7262 — Ni(I) / Ni(III) 中間体を EPR で in situ 観測し、L₂NiR₂ 系の電子状態を割り当て。NiCl₂ 系前駆体からの活性種同定に貢献。
* **充填確立点**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319 — Ni(0)/Ni(I)/Ni(III) サイクル全体を分光学・速度論の両面から確立。NiBr₂(PPh₃)₂ 系での aryl halide 酸化的付加と reductive elimination のラジカル鎖機構を提示。
* **充填の性質**: Indirect（NiCl₂(dpe) ではなく類似 Ni(II) ホスフィン系での充填、ただし機構的同型性が確立されている範囲で機能的 Complete）
* **Confidence**: High
* **Self-classified retrieval Tier**: Tier I (immediate)
* **推論経路**: 「Ni cross-coupling mechanism 1970s」と入力された瞬間に Kochi が surface。Tsou & Kochi 1979 はこの分野の機構研究の代表として強く記憶されており、Morrell & Kochi 1975 はそのペア論文として連結想起。
* **DB-findable?**: yes — JACS 1979, 101, 6319 / JACS 1975, 97, 7262 のいずれも一意検索可能。
* **Bibliographic confidence**: High（両論文とも記憶上明瞭、ページ番号も一致確認感あり）。Verification recommendation: ACS DOI で確認推奨（特に Morrell-Kochi 1975 のページ番号は 7262 と想起したが、複数の Kochi 論文が同年同雑誌に存在するため要確認）。
* **注記**: NiCl₂(dpe) 特異的研究ではないため Indirect だが、SRG-2 の RI-03（中間体未観測）を機構レベルで前進させる。原論文系（dpe）への完全 transfer は EP-10a 系列と組み合わせて達成される。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator], RI-01 [Reporting integrity]
* **充填開始点**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319 — radical chain mechanism の確立。1,2-dichloroethylene cis/trans scrambling と機構的に対応するラジカル経路の存在を vinyl 系で実証。
* **充填確立点**: 未同定（NiCl₂(dpe) + 1,2-dichloroethylene 系での specific stereochemical time-course study は記憶から特定できず）
* **充填の性質**: Partial — ラジカル機構の存在は確立されたが、cis-stilbene scrambling の per-paper specific 解析は限定的。
* **Confidence**: Medium
* **Self-classified retrieval Tier**: Tier II (associative)
* **推論経路**: 「cis-stilbene scrambling Ni vinyl coupling」→ Kochi のラジカル機構（既出）+ Stille/Negishi の vinyl coupling stereochem で連想する流れ。直接対応する vinyl 系 specific 研究は思い当たらず、Tsou-Kochi の vinyl-coupling 部分が最も近い候補として triangulation。
* **DB-findable?**: uncertain — Kochi 系列論文は findable だが、cis-/trans-stilbene specific な Ni 系 mechanism paper は keyword 検索の hit 精度に依存。
* **Bibliographic confidence**: Medium — Tsou-Kochi 1979 の bibliography は High だが、cis-stilbene scrambling 専論への transfer は推論を含む。
* **注記**: 完全充填は未同定。後続研究（80年代以降の Ni vinyl coupling 機構論文）に潜在的候補が存在する可能性が高いが、specific 同定は triangulation 不足。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread], RI-08 [Unquantified reliability]
* **充填開始点**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Full Paper で配位子効果の系統データを部分的に展開（dpp, dpe, dmpe, dppp, dppb 等の二座ホスフィンの比較表）。
* **充填確立点**: 未完全同定 — 9 配位子 × 3 基質ペアの完全 matrix を発表した specific 論文は記憶上特定できず。
* **充填の性質**: Partial（Full Paper での部分展開、cis-強制制御実験は未充填）
* **Confidence**: Medium
* **Self-classified retrieval Tier**: Tier II (associative)
* **推論経路**: 「配位子効果系統研究 Ni Kumada」→ Tamao 1976 BCSJ への展開部分（既出 Tier I 論文の content layer）と Hayashi-Kumada 後続研究（asymmetric coupling 系列、specific paper unclear）の連想ネットワークを 2 段階たどる。
* **DB-findable?**: uncertain — 二座ホスフィン系統研究は多数存在するが、Kumada 系列のフォロアップとして specific entry を identify するには追加検索が必要。
* **Bibliographic confidence**: Medium-Low — 1976 BCSJ への部分充填は High、specific 系統研究論文の同定は Low。
* **注記**: cis-強制単座配位子による「chelation vs cis-geometry」分離制御は、Hartwig グループ等の現代の機構論文に部分的に存在する可能性があるが specific 候補なし。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory], RI-06 [Imported model]
* **充填開始点**: Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* **1975**, *97*, 7262 — β-H 不安定性の Ni(I)/(III) 系での速度論的検討。
* **充填確立点**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319 — β-H 経路 vs reductive elimination の競合機構を Ni 系で確立。
* **充填の性質**: Indirect（NiCl₂(dpe) 特異的研究ではなく Ni 系の analogy 確立として機能）
* **Confidence**: Medium-High
* **Self-classified retrieval Tier**: Tier I (immediate, from EP-03a の連続)
* **推論経路**: EP-03a と同じ Kochi 系列が β-H 機構研究としても surface。「Ni alkyl complex β-H elimination 1970s Kochi」の連想で即想起される。
* **DB-findable?**: yes（同上）
* **Bibliographic confidence**: High（EP-03a と同論文）
* **注記**: β-D ラベル specific 研究は未同定。Whitesides, Schlosser, Felkin 系列の β-H 一般論研究は ref 17 として原論文が引用済み（C-04 で C 項目）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary], RI-09 [External superiority]
* **充填開始点**: Devasagayaraj, A.; Stüdemann, T.; Knochel, P. *Angew. Chem. Int. Ed.* **1995** — Ni-catalyzed alkyl-aryl cross-coupling、C_sp³ Grignard / アルキル halide 拡張の先駆。
* **充填確立点**: Zhou, J.; Fu, G. C. *J. Am. Chem. Soc.* **2003**, *125*, 14726 — Ni-catalyzed alkyl-alkyl cross-coupling、C_sp³ × C_sp³ 系の確立。
* **充填の性質**: Paradigm-shift — 「C_sp³ halides cannot be used」という 1972 年の境界主張は、配位子設計の進化（terpyridine, 二座 N 配位子等）により 25-30 年後に置換された。EP-07a は元の主張の検証ではなく、主張の前提が paradigm-shift で変わった事例として機能。
* **Confidence**: High
* **Self-classified retrieval Tier**: Tier II (associative)
* **推論経路**: 「Ni alkyl-alkyl cross coupling」→ 1990 年代の Knochel が surface、続いて 2000 年代の Fu group が連結。Kumada の 1972 sp²-only 制限の paradigm-shift として確立されている知識と接続。
* **DB-findable?**: yes — Knochel 1995 と Fu 2003 はいずれも well-cited.
* **Bibliographic confidence**: Medium-High — Knochel 1995 の page number / volume は記憶上 vague（Angew. Chem. 1995 vol 34 周辺と想起だがページ未確定）。Fu 2003 JACS 125 14726 は High。Verification recommendation: 両論文とも DOI 確認推奨。
* **注記**: これは「充填」というより「主張の paradigm-shift」の代表例。原論文の RI-07 は当時の知見では妥当な境界宣言だったが、後続研究はその境界自体を方法論的に push した。

---

**EP-08a [Replication / uncertainty pack]（第二群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Full Paper で複数バッチの収率範囲を部分的に開示。
* **充填確立点**: 未同定 — Table I 全 10 エントリの n=3 標準偏差付き複製は当時の出版慣行下で実施されなかった可能性が高い。
* **充填の性質**: Partial — Full Paper では representative range 開示、SD 開示は限定的。
* **Confidence**: Medium
* **Self-classified retrieval Tier**: Tier I (immediate, EP-01a の連続)
* **推論経路**: Tamao 1976 BCSJ の content layer から導出。
* **DB-findable?**: yes（同論文）
* **Bibliographic confidence**: High（同論文）/ Medium（充填の completeness 評価）
* **注記**: SRG-1 のマスバランス定量は EP-08a に含まれるが、これは別系統の充填が必要（後述）。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority], RI-08 [Unquantified reliability]
* **充填開始点**: Foa, M.; Cassar, L. *J. Chem. Soc., Dalton Trans.* **1975**, 2572 — Ni(0) + ArX oxidative addition の Hammett 速度論研究。Ar-Cl, Ar-Br, Ar-I の比較速度定数を提供。
* **充填確立点**: 同上 + Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319 — Br/I の比較速度を機構的に位置づけ。
* **充填の性質**: Indirect（Ni(0) 系での比較。NiCl₂(dpe) 系での head-to-head 比較ではない）
* **Confidence**: Medium-High
* **Self-classified retrieval Tier**: Tier II (associative)
* **推論経路**: 「Ni(0) Hammett oxidative addition aryl halide」の連想で Foa-Cassar が surface。「Cl/Br/I rates Ni」というキーワードでこの論文以外に specific 候補が思い当たらないため triangulation 終了。
* **DB-findable?**: yes — JCS Dalton 1975 のページ 2572 は specific だが、ページは記憶上 vague で要確認。
* **Bibliographic confidence**: Medium — Foa & Cassar の Ni 系 Hammett 研究の存在は High、specific JCS Dalton 1975 entry は Medium（年・雑誌は High、page は Low）。Verification recommendation: Foa M. Cassar L. 1975 で著者検索推奨。
* **注記**: Ni(acac)₂ vs NiCl₂(dpe) の head-to-head 比較（CLA-1 の核心）は specific には未同定。Corriu-Masse 1972 は同変換の独立発見として記録されるが、NiCl₂(dpe) との直接比較ではない。

---

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: PRI-11 [Mechanism-kinetics decoupling, 暫定], RI-03
* **充填開始点**: Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319 — Ni(0)/(I)/(III) サイクル全体の速度論的検証、初期速度次数の決定。
* **充填確立点**: 同上
* **充填の性質**: Indirect（NiCl₂(dpe) 系特異的ではないが機構的同型性が確立）
* **Confidence**: High
* **Self-classified retrieval Tier**: Tier I (immediate)
* **推論経路**: EP-03a と同じ系列。「Ni catalyzed cross coupling kinetics 1970s」で即想起。
* **DB-findable?**: yes
* **Bibliographic confidence**: High（既出論文）
* **注記**: PRI-11 の代数的速度式導出は Tsou-Kochi で部分達成、完全な dpe 系移植には追加研究が必要。

---

**CLA-1（Corriu-Masse 比較）追加充填候補**

* **充填するRI**: RI-09
* **候補**: Corriu, R. J. P.; Masse, J. P. *Chem. Commun.* **1972**, 144 — 同時期独立発見の Ni(acac)₂ 系。
* **充填の性質**: Attempted（同変換の independent 報告だが直接比較は未実施）。head-to-head 比較は両グループのいずれによっても systematic に実施された記憶なし。
* **Confidence**: High（Corriu-Masse 1972 の存在は High、直接比較論文の不在判定は Medium）
* **Self-classified retrieval Tier**: Tier I (immediate, 原論文の Note Added in Proof で言及)
* **推論経路**: 原論文 footnote 3a から direct extraction。
* **DB-findable?**: yes
* **Bibliographic confidence**: High
* **注記**: ホスフィン要件の直接検証論文は未同定。Hayashi/Kumada 後続および Hartwig 系列で部分的に扱われる可能性あり。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 | EP-01a, EP-02a, EP-05a (部分), EP-08a | VQ-2 | 1976 | High |
| 2 | Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* **1975**, *97*, 7262 | EP-03a, EP-06a | VQ-3 | 1975 | High |
| 3 | Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319 | EP-03a, EP-04a, EP-06a, EP-09a, EP-10a | VQ-3 | 1979 | High |
| 4 | Foa, M.; Cassar, L. *J. Chem. Soc., Dalton Trans.* **1975**, 2572 | EP-09a | VQ-3/VQ-4 | 1975 | Medium-High |
| 5 | Corriu, R. J. P.; Masse, J. P. *Chem. Commun.* **1972**, 144 | CLA-1 (Attempted) | VQ-2 | 1972 | High |
| 6 | Devasagayaraj, A.; Stüdemann, T.; Knochel, P. *Angew. Chem. Int. Ed.* **1995** | EP-07a (paradigm-shift 開始点) | VQ-2 | 1995 | Medium-High |
| 7 | Zhou, J.; Fu, G. C. *J. Am. Chem. Soc.* **2003**, *125*, 14726 | EP-07a (paradigm-shift 確立点) | VQ-2/VQ-3 | 2003 | High |

**選定理由：**

選定 1（Tamao 1976 BCSJ）は最大バンドル充填（4 EPs を Full Paper 形式で同時解消）し、Communications → Full Paper 自動解消パターンの代表例。VQ-2 要件のほぼ全層をカバー。

選定 2 と選定 3（Kochi 系列 1975/1979）は VQ-3（Mechanism）の要件を Ni 系で establish する pair。Morrell-Kochi 1975 は Ni(I)/(III) 中間体観測の pioneer、Tsou-Kochi 1979 は機構サイクル全体の確立。両者を含むことで EP-03a, EP-04a, EP-06a, EP-09a, EP-10a の機構層を覆う。

選定 4（Foa-Cassar 1975）は VQ-3/VQ-4 の境界要件として Cl/Br/I の Hammett 比較を提供。Kochi 系列とは独立な Ni(0) 化学からのアプローチで、機構像の triangulation に寄与。

選定 5（Corriu-Masse 1972）は CLA-1 の attempted 充填として、原論文自身が認識した contemporary。phosphine 要件の直接検証は未実施だが、独立確認として歴史的価値が高い。

選定 6 と選定 7（Knochel 1995 + Fu 2003）は EP-07a の paradigm-shift として、原論文の境界主張（"Only C_sp² halides"）を覆す方法論進化を代表する。VQ 階層の時間的展開を最も鮮明に示す pair。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件: EP-01a, EP-02a → 1976 Tamao BCSJ Full Paper（自己充填、4 年遅延）
- VQ-3 要件: EP-03a, EP-06a → 1975 Morrell-Kochi（技術駆動充填、3 年遅延）
- VQ-3 要件: EP-09a → 1975 Foa-Cassar（分野横断充填、3 年遅延）
- VQ-3 要件: EP-04a, EP-10a → 1979 Tsou-Kochi（技術駆動充填、7 年遅延）
- VQ-4 要件: EP-07a → 1995-2003 Knochel/Fu（パラダイム転換充填、23-31 年遅延）
- VQ-3/VQ-4 要件 (CLA-1): 部分充填 1972 Corriu-Masse（同時期独立発見）、完全充填 未達

**階層-時間対応の評価：**

VQ-2 の自己充填（1976）が最早。VQ-3 の Ni 機構研究が中期（1975-1979）。VQ-4 相当の境界拡張（C_sp³ paradigm-shift）が最遅（1995-2003）。仮説「VQ 階層が上がるほど充填に要する時間が長くなる」は本ケースで定性的に支持される。VQ-3 が VQ-2 とほぼ同時期（1975-1976）に充填された点は、Kochi グループの独立した機構関心が原因であり、VQ-3 が VQ-2 に必ずしも先行依存しないことを示す（継承原則は認定の論理であり、研究の歴史的実施順序ではない）。

**特筆すべきパターン：**
- **自己充填**: Tamao 1976 BCSJ は典型的な Communications → Full Paper 4 年遅延の自己充填。
- **技術駆動充填**: Kochi グループの EPR / 速度論ツールが Ni 中間体観測を可能にした。
- **分野横断充填**: Foa-Cassar の研究は Kumada とは独立な Ni(0) 化学コミュニティから機構データを供給。
- **長期遅延充填**: EP-07a の C_sp³ 境界拡張は 23-31 年遅延、paradigm-shift 型。
- **部分未充填**: CLA-1 の Ni(acac)₂ vs NiCl₂(dpe) 直接比較は 50 年以上未実施。
- **著者回顧との照合**: Kumada 自身（および Tamao の retrospective、Tamao 2002 など）は feature 1-5 のうち β-H 寛容性と二座ホスフィン優位を主に回顧で強調する一方、cis-stilbene scrambling の機構問題（A-04, A-14）は回顧で前面化されない傾向がある。これは「分野の内部者には不可視な構造的不在」の候補だが、回顧資料の独立確認なしには結論不能。

---

### §E 未充填EPの発見的意義

**部分未充填／未同定 EP 一覧：**

**EP-04a [Discrimination / replication pack] の cis-stilbene 部分**:
* **未充填の理由**: 関心の欠如 + インセンティブ構造の不整合。Ni vinyl coupling の stereochem scramble は機構的興味を持つ問いだが、cross-coupling の実用化は selectivity や scope 拡張の方向に進化したため、原論文の specific 観察を mechanism-level に解明する研究は出版インセンティブが弱い。
* **発見的意義**: あり — 「分野が 50 年にわたって体系的に避けてきた問い」候補。1972 年の anomalous cis enrichment は機構的診断として価値があったが、合成的有用性に回収されたまま深掘りされなかった。
* **将来の充填可能性**: 中 — 現代の TEMPO trap、time-resolved EPR、in situ ¹³C labeling で技術的には充填可能。

**EP-05a [Quantitative-ranking substantiation pack] の cis-強制制御部分**:
* **未充填の理由**: 技術的困難 + インセンティブ構造の不整合。chelation vs cis-geometry の operational 分離は配位子設計上 demanding であり、独立論文として publish される魅力が限定的。
* **発見的意義**: あり — Ni-phosphine 触媒の geometric requirement を厳密に検証した specific 研究は限定的。
* **将来の充填可能性**: 中 — 現代のリン化学で cis-強制配位子合成は可能。

**EP-08a [Replication / uncertainty pack] の n=3 SD 開示部分**:
* **未充填の理由**: 分野慣行 + インセンティブ構造の不整合。1972-1976 年の cross-coupling 文献で n=3 SD 開示は標準でなく、そのまま分野慣行として未充填のまま現代に至る。
* **発見的意義**: あり — 「分野が 50 年体系的に避けてきた問い」の典型。RI-08 は cross-coupling 全分野で持続する構造的不在。
* **将来の充填可能性**: 高 — 実験的には平易、ただし出版インセンティブの欠如が main barrier。

**CLA-1 の Ni(acac)₂ vs NiCl₂(dpe) head-to-head 比較**:
* **未充填の理由**: 関心の欠如。両系の独立確立後、それぞれ別経路で発展したため直接比較の必要性が認識されなかった。
* **発見的意義**: あり — 原論文のタイトルが主張する "phosphine" 要件は 50 年検証されないまま分野標準となった。VQ 階層逆転の典型例（低 VQ 要件の RI-09 が長期未充填、高 VQ 要件の RI-03 が早期充填）。
* **将来の充填可能性**: 高 — 実験的には平易だが、現代の cross-coupling 研究の関心は他に移っている。

**VQ階層逆転の診断:**

本ケースでは VQ-3 (Mechanism, RI-03) が 3-7 年で技術駆動充填された一方、VQ-2 内の RI-01（per-entry 報告）は Full Paper 自己充填で 4 年遅延、RI-08（複製不確かさ）は 50 年以上未充填、RI-09（Ni(acac)₂ 比較）も 50 年未充填というパターンが見られる。これは「科学的論理に基づく EP 充填順序（低 VQ → 高 VQ）」と「出版インセンティブに基づく実際の充填順序（高 VQ → 低 VQ）」の典型的逆転であり、分野のインセンティブ構造が UQS の構造的不在の一部を維持していることの empirical 証拠となる。

---

### Retrieval Depth Annotation Matrix（最終マトリクス）

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Tamao et al. *BCSJ* **1976** *49*, 1958 | EP-01a, EP-02a, EP-05a(部分), EP-08a | I | "Kumada coupling Full Paper" 即時想起、自己充填の教科書事例 | yes | High |
| Morrell & Kochi *JACS* **1975** *97*, 7262 | EP-03a, EP-06a | I | "Ni cross-coupling mechanism 1970s Kochi" 即時想起 | yes | High（page 要確認） |
| Tsou & Kochi *JACS* **1979** *101*, 6319 | EP-03a, EP-04a, EP-06a, EP-09a, EP-10a | I | Morrell-Kochi のペア論文として連結想起 | yes | High |
| Foa & Cassar *JCS Dalton* **1975**, 2572 | EP-09a | II | "Ni(0) Hammett oxidative addition aryl halide" の 2 段階連想 | yes | Medium-High（page 要確認） |
| Corriu & Masse *Chem. Commun.* **1972**, 144 | CLA-1 (Attempted) | I | 原論文 footnote 3a から direct extraction | yes | High |
| Devasagayaraj, Stüdemann & Knochel *Angew. Chem. Int. Ed.* **1995** | EP-07a (paradigm-shift 開始) | II | "Ni alkyl-aryl coupling 1990s Knochel" 連想 | yes | Medium-High（vol/page 要確認） |
| Zhou & Fu *JACS* **2003** *125*, 14726 | EP-07a (paradigm-shift 確立) | II | "Ni alkyl-alkyl Fu 2000s" 連想 | yes | High |

---

### 棄却候補の明示記録（Rejected Candidates Appendix）

以下は task 実行中に思い浮かんだが採用しなかった候補：

| 棄却候補 | 棄却理由 | Tier (もし採用したら) |
|---|---|---|
| Negishi *Acc. Chem. Res.* **1982**, *15*, 340 (review) | プロンプト規則：レビューは充填しない | I |
| Hartwig "Organotransition Metal Chemistry" textbook | 二次資料、教科書 | I |
| Tamao, Kiso, Sumitani, Kumada *JACS* **1972** (hydrosilylation, ref 14 of 原論文) | 同号別反応、Kumada coupling との対応なし | I |
| Yamamoto, Yamamoto, Ikeda *J. Organomet. Chem.* **1971** *24*, C63 (ref 11 of 原論文) | 原論文発表前の文献、引用元 | I |
| Wilke 系列の Ni(0) 化学（COD, COT 錯体等） | Kumada coupling との直接対応欠如 | II |
| Stille 系 Pd-catalyzed cross coupling | Pd 系で Ni と異なる、Kumada coupling 直接充填ではない | I |
| Corey-Posner cuprate 系列 (refs 7-9 of 原論文) | 原論文が cite-and-dismiss、対応 EP なし | I |
| Hayashi, Kumada asymmetric phosphine 研究（70年代後半-80年代） | Kumada coupling 充填ではなく asymmetric synthesis の独立発展 | II |
| Cassar, L. *J. Organomet. Chem.* **1975** (Pd系) | Pd vs Ni 違い、specific 候補として弱い | III |
| Kochi 単独 review papers | レビューは充填しない | I |
| Buchwald/Hartwig modern Pd amination 系列 | Pd 系で Ni Kumada coupling 直接充填ではない | II |

---

### 参考：Self-classified Tier 分布の整理

採用 7 候補中：
- Tier I: 4 報（Tamao 1976, Morrell-Kochi 1975, Tsou-Kochi 1979, Corriu-Masse 1972）
- Tier II: 3 報（Foa-Cassar 1975, Knochel 1995, Fu 2003）
- Tier III: 0 報（採用された候補のうち deep retrieval を要したものはなし、ただし EP-04a の cis-stilbene 部分と EP-05a の cis-強制制御部分は Tier III triangulation で具体候補同定に至らず未充填判定）

棄却候補 11 件中：
- Tier I 棄却: 7 件（即時想起したが規則／対応問題で除外）
- Tier II 棄却: 3 件
- Tier III 棄却: 1 件

Confidence 分布：
- High: 4 報（Tamao 1976, Tsou-Kochi 1979, Corriu-Masse 1972, Fu 2003）
- Medium-High: 3 報（Morrell-Kochi 1975 page 要確認、Foa-Cassar 1975 page 要確認、Knochel 1995 vol 要確認）
- 完全 verification 推奨: 全候補について DOI / page range の独立確認推奨。特に 1970 年代雑誌のページ番号は記憶上の信頼度が低い箇所。

---

### Verification Recommendation Summary

全候補論文について、以下の verification を推奨する：
1. Tamao 1976 BCSJ: 著者列の完全性、ページ範囲（1958-1969 想起）、DOI
2. Morrell-Kochi 1975: ページ 7262 の確認（複数の同年同雑誌 Kochi 論文との混同リスク）
3. Tsou-Kochi 1979: 高信頼想起だが DOI 確認
4. Foa-Cassar 1975: JCS Dalton ページ番号（2572 想起）の確認、可能性として alternative 候補（J. Organomet. Chem. 等の年同雑誌混同）の検討
5. Corriu-Masse 1972: 原論文 footnote 3a に直接記載、最高信頼
6. Knochel 1995: Angew. Chem. Int. Ed. の vol 34 周辺と想起、ページ未確定
7. Fu 2003: JACS 125, 14726 高信頼だが DOI 確認

特記：UQS Project memory（user_email memory）に記録された LLM Stage 4 author-field hallucination 5 patterns（A-E）に照らし、本実行では：
- D-pattern（cross-paper hybrid）リスク：Kochi の同年同雑誌複数論文があり Morrell-Kochi 1975 の中身が Tsou-Kochi 1979 と混同している可能性は低いが warning level 監視推奨。
- E-pattern（non-anglicized given names）リスク：Tamao グループの Zembayashi, Fujioka, Kodama, Nakajima, Minato は記憶上 Romanized 形で再現したが original Japanese 表記との対応は未確認。

inference_time_sec: not available — inject externally
