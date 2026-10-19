prompt_version: stage3-v2-20260416
model_info: GPT-5.4 Thinking

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society communication）

### §1 Claim Architecture

コア主張は、Ni-phosphine complex により Grignard reagent と vinyl or aryl halide の selective cross-coupling が可能になる、という**Novelty柱**と、その方法が代表例で高収率・chloride 反応性・β-hydrogen 含有 alkylmagnesium reagent への適用可能性を示す、という**Utility柱**から成る。前者は変換の成立そのもの、後者はその変換の有用性・広がり・特徴づけであり、論文はこの二本柱を「new and useful preparative method」「remarkable features」「high yields」などの語で接続している。

Layered structure は**あり**。単一の反証で全主張が同時に崩れる構造ではなく、(i) Ni-phosphine による cross-coupling の成立、(ii) preparative usefulness、(iii) chloride/β-hydrogen tolerance という特徴づけ、(iv) literature-backed catalytic-cycle framing が部分的に独立している。ただし依存関係としては、(ii)〜(iv) は (i) の成立を前提にし、(iii) と (iv) はさらに matched comparison や direct observation を欠くため (i) より脆弱である。

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [定量的副生成物・中間体データの不在]**

- **Primary RI**: RI-03 Unobserved explanatory
- **Secondary RI**: RI-06 Imported model
- **ER**: 選択的 cross-coupling と提案触媒サイクルを同時に採るには、サイクルが予測する副生成物経路と状態変数を、直接観測または速度論的拘束で対象系に結びつける必要がある。少なくとも、R-R homocoupling と想定 Ni 種の存在可能性が本文データ上で評価されていなければならない。
- **EP**: EP-03a Direct-observation / state-assignment pack；EP-06a Analogy-validation pack
- **Case-specific実装**: [NiCl2(dpe)]/RMgX/R'X 系で、Table I の代表基質について glpc 校正下で R-R homocoupling と disproportionation を定量し、加えて stoichiometric 条件で L2NiR2 および halo(organo)Ni 種を低温分光・rapid quench・独立生成/反応試験で拘束する。
- **注記**: 下位項目 = B1, B5, U1。TEMPERATURE_SUMMARY = high_convergence_low_gap(B1, B5)。U1 は self-contradictory absence として独立中核。

**SRG-2 [収率・同定フレームの不統一と分析仕様の省略]**

- **Primary RI**: RI-01 Reporting integrity
- **Secondary RI**: RI-02 Object identification；RI-08 Unquantified reliability
- **ER**: scope table を方法論的に比較可能にするには、収率の計算基準、内部標準補正、分析法の entry-by-entry 対応、反復と不確かさが同一フレームで与えられる必要がある。生成物同定も、少なくとも代替構造や isomer を排除できる粒度で記述される必要がある。
- **EP**: EP-01a Reporting-coherence pack；EP-02a Identity / purity substantiation pack；EP-08a Replication / uncertainty pack
- **Case-specific実装**: isolated yield と glpc yield を単一軸に統一し、内部標準・response factor・回収補正を明示し、各 entry ごとに NMR/IR/MS/GC 同定根拠と cis/trans 割り当てを対応づけ、主要 entry で反復測定とばらつきを付す。
- **注記**: 下位項目 = B2, B12, B14。TEMPERATURE_SUMMARY = high_convergence_low_gap(B2)。B12/B14 は convergence 情報なしだが SRG としては同根。

**SRG-3 [境界条件・比較設計なしの scope / condition 主張]**

- **Primary RI**: RI-07 Unsupported boundary
- **Secondary RI**: RI-09 External superiority；RI-01 Reporting integrity
- **ER**: 「Only Csp2 halides」「chlorides が remarkable」「ether が superior」「β-hydrogen-containing reagents に一般的」などの境界・優位主張は、同一測定軸・同一設計上の matched comparison により内部で支持される必要がある。失敗例や比較対照なしの境界主張は、方法境界ではなくレトリックに留まる。
- **EP**: EP-07a Boundary-test pack；EP-09a Internal benchmark pack；EP-01a Reporting-coherence pack
- **Case-specific実装**: 同一基質骨格で chloride/bromide/iodide、Csp2/non-Csp2、ether/THF、標準条件/bomb-tube 条件を matched-pair で比較し、成功例だけでなく failure matrix を本文に含める。
- **注記**: 下位項目 = B4, B8, B10, B11, B15。TEMPERATURE_SUMMARY = high_convergence_low_gap(B4, B8, B10, B11)。SRG 全体として比較設計欠如が中核。

**SRG-4 [立体化学異常の単発過読と将来送り]**

- **Primary RI**: RI-04 Unreplicated discriminator
- **Secondary RI**: RI-05 Qualitative overread
- **ER**: 異常な cis enrichment は、それ自体では識別力の高い単発観測に過ぎず、再現・時間依存性・生成後異性化の排除がない限り高位の立体化学解釈に上げられない。特に prolonged reflux を伴う系では、生成段階と後異性化段階を分離する要件が加わる。
- **EP**: EP-04a Discrimination / replication pack；EP-10a Kinetic verification pack
- **Case-specific実装**: cis/trans-1,2-dichloroethylene の各 coupling を反復し、反応時間ごとの stilbene cis/trans 比、生成物単独加熱対照、quench timing 依存性を測定して、formation-selectivity と post-formation scrambling を分離する。
- **注記**: 下位項目 = A1, B7。TEMPERATURE_SUMMARY = high_convergence_low_gap(B7; convergence=3/3, temperature_gap=low)。

**SRG-5 [反応状態異常と触媒状態未同定]**

- **Primary RI**: RI-03 Unobserved explanatory
- **Secondary RI**: RI-02 Object identification
- **ER**: 提案された homogeneous catalytic cycle と両立しない可能性のある visible state change が本文に現れた場合、活性種・失活種・析出相のいずれかを割り当てるか、少なくとも主張から切り離す必要がある。反応液の黒色化は単なる作業記述では済まない。
- **EP**: EP-03a Direct-observation / state-assignment pack；EP-02a Identity / purity substantiation pack
- **Case-specific実装**: 黒色混合物について可溶/不溶 Ni の mass balance、固体相の元素・状態解析、ろ過/再投入試験、反応初期と長時間後の Ni speciation の比較を行い、触媒持続か分解かを区別する。
- **注記**: 下位項目 = B9, U2。TEMPERATURE_SUMMARY = high_convergence_low_gap(B9)。U2 は self-contradictory absence として補強。

**SRG-6 [非最適条件の宣言と最適化空間の未提示]**

- **Primary RI**: RI-01 Reporting integrity
- **Secondary RI**: RI-08 Unquantified reliability
- **ER**: 「not necessarily optimum」と明言するなら、少なくとも採用条件がどの探索空間から選ばれたかの最小地図が必要である。そうでなければ代表条件の意味づけができず、再現的 method claim ではなく exploratory note に留まる。
- **EP**: EP-01a Reporting-coherence pack；EP-08a Replication / uncertainty pack
- **Case-specific実装**: catalyst loading、Grignard/halide 比、溶媒、温度、時間について最小限の optimization matrix を提示し、代表条件が近傍条件に対してどの程度頑健かを示す。
- **注記**: 下位項目 = A2, B3。TEMPERATURE_SUMMARY 直接該当なし。A2 が follow-up への外部化を示す。

SRG外：CLA
該当なし。Stage 2 D-4 候補のうち claim-level adjunct として独立抽出すべきものは、本件では既存 SRG（特に SR1, SR3, SR4）に吸収される。

### §3 現在のVQ判定

現在判定: **VQ-1 (Observation)**

**VQ-1 Observation は通る。**
代表例では cross-coupled products が単離され、Table I でも生成物が割り当てられており、「Ni-phosphine 条件下でこの種の cross-coupling が起こり得る」という observation-level claim は保持できる。SRG-2 に RI-02 の要素は残るが、少なくとも exemplar level の生成物存在そのものを覆すほどには致命化していない。

**VQ-2 Method は未達。**
VQ-1 を前提としても、RI-01 が SRG-2/SRG-6 で未解消、RI-07 が SRG-3 で未解消であり、method claim を scope つきで再認定する条件を満たさない。とくに yield basis の混在、calibration 欠如、matched boundary tests の不在により、「どこまで一般的方法か」を本文だけでは確定できない。

**VQ-3 Mechanism は未達。**
RI-03 が SRG-1/SRG-5 で、RI-06 が SRG-1 で、RI-04/RI-05 が SRG-4 で残っており、提案 catalytic cycle や stereochemical reading は mechanistic knowledge としては立ち上がらない。論文自身も “working hypothesis” とし、さらなる mechanistic / stereochemical study を future work に送っている。

**VQ-4 Benchmark は未達。**
RI-08 は SRG-2/SRG-6 で、RI-09 は SRG-3 で未解消であり、内部 benchmark と uncertainty つき比較の水準に達していない。Tamura–Kochi 系や halide class 間の superiority framing はあるが、同一測定軸の直接比較は本文にない。

ただし**変換成立の exemplars**単独では、m-di-n-butylbenzene と α-vinylnaphthalene への到達という observation layer は比較的堅く、論文全体より高い mechanistic robustness を持つわけではないが、少なくとも VQ-1 の中核を支えている。

### §4 Era-Norm Annotation

communication-era tolerated:

- **A1** — communication では transformation を先に出し、stereochemical / mechanistic detail を follow-up に回す構図は当時の genre convention 内で理解可能である。
- **A2** — “extension, refinement, and application” を将来論文に送る書き方は、短報が系列化される前提では当時許容されやすい。
- **B3** — 非最適条件のまま representative results を示すことは、紙幅制約下の速報としては当時容認されやすい。
- **B12 / B14** — 分析法や反復・不確かさの詳細を footnote レベルに圧縮する報告様式は、1972年 JACS communication では genre 的に珍しくない。
- **B13** — catalyst-free や ligand-free の baseline omission も、当時の concise communication では mechanistic completeness より transformation announcement が優先されやすかった。

modern-era deficient:

- **B2 / B12 / B14** — 現代の再認定では、mixed yield basis、calibration 欠如、replication / uncertainty 不在は横比較不能を生み、method claim の評価に耐えない。
- **B4 / B8 / B10 / B11 / B15** — scope・solvent・special protocol の主張を matched-pair design なしに提示することは、現代では unsupported boundary とみなされる。
- **B5 / B6 / B7 / B9** — catalytic cycle、ligand geometry 解釈、stereochemical anomaly、black mixture を direct observation なしで高位解釈に上げることは、現代では mechanistic reaccreditation の要件を満たさない。
- **A1 / A2** — future work への deferral 自体は許容されても、現代の VQ 昇格では deferral は未解消の証拠として扱われ、現論文本体の根拠には置換できない。

### §5 最短補強ルート

**VQ-2 への最短ルート：**

1. **EP-01a Reporting-coherence pack** — isolated/glpc yield を単一フレームに統一し、internal standard・response factor・entry別分析法対応・最小反復を付す。RI-01 を前進。
2. **EP-07a Boundary-test pack** — chloride/bromide/iodide、Csp2/non-Csp2、ether/THF、standard/bomb-tube を matched-pair で比較し、failure matrix を明示する。RI-07 を前進。
3. **EP-02a Identity / purity substantiation pack** — representative entries と stereochemical issue entries に対して、生成物・isomer の同定根拠を明示する。RI-02 を前進。
4. **EP-08a Replication / uncertainty pack** — anchor entries の収率・比率の反復とばらつきを付す。RI-08 を部分的に前進。

認定ゲート順注記：実験投入順は情報利得順だが、最終認定は継承原則に従い VQ-1 → VQ-2 の順で確定する。

**VQ-3 への最短ルート：**

1. **EP-03a Direct-observation / state-assignment pack** — R-R homocoupling と disproportionation を定量し、Ni 活性種/失活種/析出相を分離して触媒状態を割り当てる。RI-03 を前進。
2. **EP-06a Analogy-validation pack** — imported organonickel cycle を、この catalytic system 内で stoichiometric step validation により検証する。RI-06 を前進。
3. **EP-04a Discrimination / replication pack** — cis/trans anomaly を反復し、単発識別データからの過読を止める。RI-04 を前進。
4. **EP-10a Kinetic verification pack** — time-course と heating controls により formation-selectivity と post-formation isomerization を分離する。RI-05 を抑制しつつ SRG-4 を mechanistic discrimination に変換する。

認定ゲート順注記：VQ-3 の認定は VQ-2 通過後にのみ確定し、RI-03・RI-04・RI-06 の同時解消を要する。

**VQ-4 への拡張ルート：**

1. **EP-08a Replication / uncertainty pack** — key yields・cis/trans ratios・solvent/halide comparisons に uncertainty を付与する。RI-08 を前進。
2. **EP-09a Internal benchmark pack** — Tamura–Kochi 系、同一基質での halide class 比較、ether/THF 比較を同一測定軸で head-to-head に置く。RI-09 を前進。

認定ゲート順注記：VQ-4 の認定は VQ-3 通過を前提とし、benchmark は transformation claim の上に後置される。

### §6 制度設計への寄与

本ケースは、既存 Codebook を**追加確認しつつ、いくつかの境界を明瞭化した代表事例**である。第一に、**RI-03 と RI-06 の共起**が典型的に現れている。すなわち、他系文献から輸入した organonickel cycle を本文では “reacts,” “forms,” “is converted to” の事実記述語で進めながら、末尾では “working hypothesis” と future study に戻す。この**labeling mismatch** は、仮説標識が結論部にのみ退避し、本文中央の叙述は assertive になるパターンとして記録価値が高い。

第二に、**自己矛盾的不在**が RI-03 の case-specific 強化例として有用である。論文自身の catalytic cycle が R-R と intermediates 1–3 を予測するのに、その観測・定量がないという構図は、新規 PRI を立てるよりも、RI-03/RI-06 接続部の強い代表例として扱うのが妥当である。これは「未観測」一般ではなく、「論文自身のモデルが予測する観測量の未報告」という sharpened subtype として EP-03a 実装に反映できる。

第三に、**RI-07 + RI-09 + RI-01 の共起**が SRG-3 で確認される。「Only Csp2 halides」「chlorides が remarkable」「ether が superior」という boundary/superiority claim は、失敗例不在・内部 benchmark 不在・報告フレーム不統一が同時に起きており、いずれか一つだけの解消では足りない。この共起構造は、scope claim の再認定において EP-07a と EP-09a を分離せず設計すべきことを示す。

第四に、**communication→Full Paper 遷移の自動解消パターン**が明瞭である。A1/A2 と B3/B4/B5 の組合せは、短報が transformation announcement を先行させ、optimization・boundary・mechanism を後続報に逃がす典型を示す。これは Era-norm annotation において、「当時は tolerated だが現代 reaccreditation では deficient」という二重記載が必要な類型として有益である。

第五に、EP 辞書には case-specific 実装例を追加できる。**EP-03a** には「Ni-phosphine cross-coupling では homocoupling R-R の定量と black-mixture の catalyst-state assignment を一体で要求する」を、**EP-07a** には「scope boundary は chloride/bromide/iodide と Csp2/non-Csp2 の matched matrix で確認する」を追加例として記録できる。新しい PRI 候補は本件単独では不要であり、Stage 2F もないため昇格判断材料は追加されていない。総じて、本ケースは既存制度設計を拡張するというより、**RI-03/06 接続部、RI-07 の boundary rhetoric、RI-01 の yield-basis coherence**を強く再確認したケースである。