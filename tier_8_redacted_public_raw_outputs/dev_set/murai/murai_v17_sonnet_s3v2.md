prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, communication）

### §1 Claim Architecture

**コア主張（1段落）：**
RuH2(CO)(PPh3)3を触媒として、芳香族ケトンのオルト位C–H結合とオレフィンとのカップリングをキレーション支援を鍵として実現した。Novelty柱：「キレーション誘導Ru触媒による芳香族C–H結合の不活性化を伴わない直接カップリング」——過去30年の化学蓄積を背景に、触媒的C–H官能化で初めて「両基質ともにほぼ定量収率（bilateral near-quantitative yield）」を達成したと主張する（B-12）。Utility柱：「効率性・選択性・汎用性の3基準を同時に満たす実用的有機合成ツール」——13例のTable 1スコープと定量的GC収率によって支持される。

**Layered structureの判定：**
独立3層構造が存在する。(1)効率性層（bilateral ≈定量収率；runs 8–13）、(2)選択性層（位置選択性≈100%；runs 8, 13）、(3)汎用性層（基質多様性；全13例）は独立して主張され、独立して証拠化されている。ただし3層の定量的根拠はすべてTable 1のGC収率という単一の証拠形式に収束するため、GC収率の信頼性（SRG-2）が揺らぐと3層が同時に動揺する構造的脆弱点を持つ。さらに機構（SRG-1）は3層すべての「理由」を担うはずだが、「not yet clear」宣言（B-3）により機構的説明が選択性主張の責任を引き受けることを回避する保護構造が存在する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [触媒機構の完全欠如]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 提案触媒サイクルの鍵種（Ru(0)活性種、シクロメタル化中間体、M-アルキル種）がすべて直接観測も速度論的拘束もされていない。
* **Secondary RI**: RI-06 [Imported model] — 触媒サイクル全体を化学量論的シクロメタル化（refs 14, 15）および酸化的付加/挿入の先行研究類推（refs 17, 18）から構成しており、触媒条件下での同型性を検証していない。
* **ER**: 少なくとも1つの触媒中間体の分光学的または速度論的証拠、およびRuH2(CO)(PPh3)3からRu(0)活性種の生成経路の同定が、機構主張成立の規範的要件。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: 触媒条件下（トルエン還流）でのin situ IR/NMRによるRu種モニタリング；シクロメタル化中間体（Fig. 1の5員Ru–C環）の単離または31P NMRによる検出；反応開始時のH2発生（Ru(II)→Ru(0)還元的脱離）の定量；β-水素脱離由来のオレフィン異性化体のGCまたはGC-MSによる探索。
* **注記**: B-3（high_convergence_low_gap, V1=high, V2=critical, convergence=2/3——V2=criticalがこのSRGの最高優先指標）; B-14; B-18; U-1（自己矛盾的不在: Ru(II)前駆体からRu(0)生成が未記述）; U-2（自己矛盾的不在: M-アルキル中間体からβ-水素脱離が予測されるが異性化生成物の不在が未説明）。

---

**SRG-2 [定量的証拠の信頼性]**

* **Primary RI**: RI-01 [Reporting integrity] — GC収率の決定に校正プロトコル・内部標準・応答係数が記述されておらず、新規化合物13例の定量値が独立に検証不能。
* **Secondary RI**: RI-08 [Unquantified reliability, 内部矛盾型サブタイプ] — 全13例で反復測定なし、誤差推定なし；runs 1–2のマスバランス欠損（17%）が内部矛盾として残存。
* **ER**: 内部標準を用いた応答係数補正GC収率（各新規化合物ごと）と、主要runs（8–13）の少なくとも3反復測定による平均・標準偏差の報告が必須。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: ドデカン等の内部標準を用い各生成物の応答係数を独立に決定；runs 8–13（効率性主張の根拠）を3反復実施；全runについてGCによる出発物・オレフィン回収率を計測してマスバランスを閉鎖；B-9のTOF計算にも同じGC校正データを使用。
* **注記**: B-1（high_convergence_low_gap, convergence=3/3, temperature_gap=low——フォールバック規則(b)の最優先候補）; B-4（V3=high）; B-5（runs 1, 2マスバランス）; B-9（V1=high）; B-15（全例unreplicated）。

---

**SRG-3 [選択性帰因の定性的読み過ぎ]**

* **Primary RI**: RI-05 [Qualitative overread] — 位置選択性（B-8）、run 1/9の1:2対1:1生成物比（B-7）、run 10/11の反応速度差（B-7）、1-インダノン不反応（B-6）がいずれも立体/環歪みの構造的直観に帰因されており、速度定数・活性化パラメータ・競争実験等の定量的支持がない。
* **Secondary RI**: RI-03 [Unobserved explanatory] — 位置選択性を制御するオルト選択的C–H切断の速度論的優先性が、金属環形成の遷移状態として未観測。
* **ER**: 電子的・立体的に差別化されたアレーン間の競争実験、およびkH/kD KIEがオルト選択的C–H切断の速度決定段階帰属のための規範的要件。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-07a [Boundary-test pack]
* **Case-specific実装**: 電子的に対称な基質（4-フルオロアセトフェノン vs アセトフェノン）の競争実験でオルト選択性の電子的寄与を定量；H/D KIE（PhC(O)Me vs PhC(O)Me-d4）でC–H切断の律速性を確認；run 10（テトラロン）vs run 11（テトラロン環拡大体）の活性化エネルギー差をアレニウス解析で決定し環歪みパラメータと比較；1-インダノン実験を条件明示（基質量・オレフィン量・反応時間・GC検出限界）で再実施。
* **注記**: B-6（high_convergence_low_gap, V1=medium, V2=medium, convergence=2/3）; B-7（V2=high）; B-8（V1=medium, V2=high, convergence=2/3）; B-19。

---

**SRG-4 [触媒構造活性相関の定性的記述]**

* **Primary RI**: RI-05 [Qualitative overread] — 「equally effective」「modestly effective」「not effective」という定性語で触媒スクリーニング結果を報告し、収率・TOF・条件の定量データがない。
* **Secondary RI**: RI-01 [Reporting integrity] — スクリーニングに使用した基質・条件が記述されていない。
* **ER**: ベンチマーク基質（アセトフェノン/トリエトキシビニルシラン）を用い、各代替触媒について同一条件下で単離収率とTOFを定量的に報告。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: Ru(CO)2(PPh3)3、RuH2(PPh3)4、Ru(CO)3(PPh3)2各触媒について標準条件（2 mmol, 3 mL toluene, 135°C）でrun 9に相当する実験を3反復実施し収率・TOF・反応時間を定量報告；配位子要件（ヒドリドの役割・CO数・ホスフィン数）をコントロール実験で切り分け。
* **注記**: B-10（high_convergence_low_gap, V1=medium, V3=medium, convergence=2/3）; B-18（SRG-1にも重複登録）。

---

**SRG-5 [性能優位性の数値的未閉包]**

* **Primary RI**: RI-09 [External superiority] — 「among the highest reported」というTOF優位性主張が、本論文内にTOF数値なし・比較先（refs 11, 12）の数値なしの二重欠如状態で提示。
* **Secondary RI**: RI-08 [Unquantified reliability] — TOF自体が計算・報告されていない（校正済み収率と明確な終点時間がないと計算不能）。
* **ER**: runs 1, 9, 10のTOFを校正済みGC収率と反応終点時間から計算した数値、ならびにJordan & Taylor (1989) とMoore et al. (1992) のTOF値を同一軸上で比較した表が必要。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: GC校正（SRG-2のEP-01a）完了後、runs 1, 9, 10のTOFを[mol product / mol Ru / h]単位で計算；文献11（Zr/α-ピコリン/プロペン系）と文献12（Ru/ピリジン/CO/1-ヘキセン系）のTOF値を原著から取得し同一表に並記；副生成物・異性体収率も同一軸で比較。
* **注記**: B-9（SRG-2にも重複登録, V1=high, V3=medium, convergence=2/3）; C-2（Dropped Quantitative Benchmark）。

---

**SRG外：CLA**

**CLA-1 [実用条件への外挿根拠不在]**

* **Primary RI**: RI-07 [Unsupported boundary] — 「practical organic synthesis」に必要な条件（触媒低量化、スケールアップ、雰囲気感受性の確定）が未検証のまま「達成した」と宣言。
* **ER**: 低触媒量（≤1 mol%）、合成スケール（≥10 mmol）、明示的な雰囲気条件下での代表的基質の再現実験が、「実用的」主張の規範的要件。
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: run 10に相当する基質で1 mol% Ru触媒・10 mmolスケールで実施；N2下と大気下で収率を比較し空気感受性を定量；温度スクリーニング（100°C, 120°C, 135°C）で実用温度域を評価。
* **注記**: B-16（大気条件記述なし）; A-1（「applicable more widely」との連動）。D-4候補5に対応。

---

**CLA-2 [キレーション有効境界の未検証]**

* **Primary RI**: RI-07 [Unsupported boundary, 拡張適用：否定的境界主張] — キレーション支援が有効に機能するキレート環サイズの境界（5員環有効・7員環不活性等）が実験で確定されていない；1-インダノン（不反応）が唯一の陰性例だが実験条件の記述なし。
* **ER**: キレート環サイズを系統的に変化させた基質群（5員環: フェニルメチルケトン；6員環: フェニルエチルケトン；7員環: フェニルプロピルケトン）の反応性比較実験が境界確定の規範的要件。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: フェニルプロピルケトン（7員前駆体、不活性予測）とフェニルエチルケトン（6員前駆体）を標準条件で反応；1-インダノン実験を条件明示（基質量・オレフィン量・反応時間・GC検出限界）で再実施；DFT計算で5/6/7員金属環形成の活性化エネルギーを比較し実験値と対照。
* **注記**: B-17（キレーション支援の境界未検証）; A-1（「applicable more widely」の外挿根拠不在）。D-4候補7に対応。

---

### §3 現在のVQ判定

**現在判定: VQ-1 [Observation]（RI-02 非致命的）**

**VQ-1 [Observation]——通過（RI-02 非致命的）：**
「[REDACTED: verbatim source text; see the source paper via its DOI]」（B-2）は1993年Nature communication形式において、NMRおよび元素分析による一次データが取得されていることを前提とした慣用表現であり、13例の生成物はいずれも比較的単純なアルキル化芳香族化合物であるため、標準NMR解析による構造帰属は代替構造を原理的に排除可能な粒度に達していると判断できる。RI-02は非致命的（データ存在、未掲載）——Era-norm依存として§4に記録。

**VQ-2 [Method]——未達：**
RI-01（Reporting integrity）が致命的。GC収率は新規化合物に対する応答係数・内部標準・校正プロトコルなしに報告されており、論文の3つの性能主張（効率性・選択性・汎用性）の定量的根拠をなすTable 1の数値が独立に検証不能。単一の証拠形式（GC収率）の信頼性欠如が3層の主張を同時に不確実にする。RI-07（CLA-1, CLA-2）は非致命的（性能主張の核心を直接覆すものではなく、実用性外挿の問題）。なお、VQ-2の通過はVQ-1が非致命的RI-02のもとで成立していることを前提とする。

**VQ-3 [Mechanism]——未達：**
VQ-2が未達であることに加え、RI-03（Unobserved explanatory: Ru(0)活性種・中間体の直接観測なし、SRG-1）、RI-06（Imported model: 化学量論類推の輸入、SRG-1）、RI-04（Unreplicated discriminator: 全13例が単一反復）がいずれも未解消。RI-05（SRG-3: 選択性の定性的帰因）が重大に残存するため、仮にRI-03/RI-04/RI-06が解消されてもVQ-3は「VQ-3 qualified（限定的）」に留まる。

**VQ-4 [Benchmark]——未達：**
VQ-3が未達であることに加え、RI-08（反復測定・誤差推定なし、SRG-2）、RI-09（TOF優位性の数値的未閉包、SRG-5）が未解消。

**層別VQ非対称性：**
§1のLayered structureより独立3層を評価する。
- **効率性層**（bilateral ≈定量収率）: VQ-1通過。VQ-2未達——効率性はGC絶対収率に完全依存するため、RI-01が直撃する最脆弱層。
- **選択性層**（位置選択性≈100%）: VQ-1通過。ただし**選択性層単独ではVQ-2 qualified（限定的）に到達**と判定——「1生成物のみ検出」という定性的観察はGC校正の絶対値に依存しないためRI-01の影響が効率性層より軽い（RI-07が残存するが非致命的）。
- **汎用性層**（基質多様性）: VQ-1通過。13基質クラスの対応は定性的な反応有無として読めGC収率の絶対値への依存度が低い。**汎用性層単独ではVQ-2 qualifiedに到達**と判定（RI-07が残存するが非致命的）。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-2**（characterization data省略）: 1993年のNature communication（3ページ）では、主要化合物の同定データ（NMR、元素分析）は取得済みを前提に省略が許容されており、「standard methods」の記載で代替するのが慣行だった。
- **B-15**（反復測定なし）: 1993年の合成コミュニケーションでは、基質スコープの実証において各基質を単一反復で示すことが標準だった。
- **B-16**（雰囲気条件未記述）: 1993年の有機金属化学コミュニケーションでは、不活性雰囲気の使用は暗黙的に前提とされることが多く、明示しないことが許容されていた。
- **B-3**（機構を「not yet clear」として一段落で記述）: 1993年の合成優先論文では、機構解明を将来の課題として明示的に先送りすることは科学的誠実さとして許容された。

**modern-era deficient:**

- **B-1**（GC収率の校正プロトコル不在）: 現代の合成論文では新規化合物のGC収率に内部標準・応答係数が必須であり、未校正GC収率は主要収率主張の根拠として許容されない。
- **B-15**（反復測定なし）: 現代では主要収率主張（「ほぼ定量」）に少なくとも3反復が要求される。
- **B-9**（TOF数値不記載）: 現代の触媒化学コミュニケーションではTOF数値の明示的計算・記載が標準。
- **B-16**（雰囲気条件未記述）: 現代の再現性基準では、空気感受性触媒を用いた反応の雰囲気条件は必ず明記する必要がある。

**両タグに該当する項目（当時は許容、現代では不足）：**
- **B-2**: 当時は通信形式慣行として許容されたが、現代ではSI（Supporting Information）への完全な分光データ掲載が標準要件。
- **B-15**: 当時は合成コミュニケーションの慣行として許容されたが、現代では主要主張の反復確認が必須。

---

### §5 最短補強ルート

現在VQ: VQ-1（RI-02 非致命的）
第一目的関数: VQ-2到達
第二目的関数: VQ-3到達（VQ-2前提）

**VQ-2 への最短ルート：**

1. **EP-01a [Reporting-coherence pack]** — ドデカン等の内部標準を用いて各生成物の応答係数を独立に決定し、全13例のGC収率を校正済み数値に更新する（runs 1–2のマスバランス閉鎖を含む）。RI-01 を前進。
2. **EP-08a [Replication / uncertainty pack]** — runs 8–13（効率性主張の根拠）を3反復実施し平均収率・標準偏差を記録；run 9（TOF主張）も含む。RI-08 を前進。

*この2実験で3層の定量的根拠が同時に強化され、VQ-2到達の最短経路となる。*

認定ゲート順注記：実験投入順は情報利得順（EP-01a → EP-08a）だが、最終VQ認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承原則に従って確定する。

---

**VQ-3 への最短ルート（VQ-2達成後）：**

1. **EP-03a [Direct-observation / state-assignment pack]** — in situ IR/NMRによるRu活性種の追跡とH2発生（Ru(II)→Ru(0)）の定量；シクロメタル化中間体の31P NMR検出または単離。RI-03 を前進（SRG-1の核心）。
2. **EP-04a [Discrimination / replication pack]** — kH/kD KIEで律速段階（C–H切断）を確認；クロスオーバー実験でラジカル経路排除；β-水素脱離由来オレフィン異性化体のGC-MSによる探索・定量（U-2の自己矛盾的不在の解消）。RI-03, RI-04 を前進。
3. **EP-06a [Analogy-validation pack]** — 化学量論的シクロメタル化類推（refs 14, 15）が触媒条件下でも成立することを速度論的に検証；触媒サイクルの各素反応（酸化的付加、挿入、還元的脱離）の相対速度比較。RI-06 を前進（SRG-1のSecondary RI解消）。
4. **EP-07a [Boundary-test pack]** — フェニルプロピルケトン（7員キレート、不活性予測）と1-インダノン（条件明示再実施）で境界を実験確定。RI-07 を前進（CLA-2の解消）。

認定ゲート順注記：実験投入順は情報利得順（EP-03a → EP-04a → EP-06a → EP-07a）だが、最終VQ認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承原則に従って確定する。

---

**VQ-4 への最短ルート（VQ-3達成後）：**

1. **EP-09a [Internal benchmark pack]** — EP-01a完了後のGC校正データを用いてruns 1, 9, 10のTOFを[mol product / mol Ru / h]で計算；refs 11–12（Jordan & Taylor 1989; Moore et al. 1992）のTOF値を原著から取得して同一表に並記。RI-09 を前進（SRG-5解消）。

認定ゲート順注記：同上継承原則による。

---

### §6 制度設計への寄与

**1. 標識不整合（Labeling mismatch）パターンの代表事例：**
本論文の「Possible mechanisms」節は冒頭で「not yet clear」と明示的に仮説標識を配置しながら、後続文で「results in easier, highly site-selective C-H bond cleavage」「chelation assistance results in」という事実的叙述語を使用する。仮説標識が節の第1文に集約され、以降の4文が事実叙述として流れる構造であり、RI-03（未観測中間体）とRI-06（輸入モデル）の共起と連動する典型的なLabeling mismatchパターンとしてCodebook事例に記録する。

**2. 通信→Full Paper遷移の自動解消パターン（確認）：**
B-2（characterization data）、B-15（replication）、B-16（reaction atmosphere）はFull Paper展開で自動解消されるEra-norm依存項目であり、§4のcommunication-era toleratedと完全に一致する。一方、RI-07（CLA-1: 実用条件、CLA-2: キレーション境界）はFull Paper展開後に追加実験が必要であり自動解消されない——この区別がEra-norm分析の実用的価値を示す事例として記録する。

**3. RI-01 + RI-08の構造的共依存（RI共起パターン）：**
SRG-2においてRI-01（校正不在）とRI-08（反復測定なし）が共起する。RI-01（EP-01a: 応答係数校正）を解消しても、RI-08（EP-08a: 反復測定）を解消しないと「校正済み単一測定値」に留まり信頼性は部分的。逆に、RI-08を解消してもRI-01なしでは「精度のない平均値」に過ぎない。両者の解消が連動して必要であり、いずれか一方の解消だけでは不十分というRI共起構造の典型例として記録する。

**4. PRI-11（Mechanism-kinetics decoupling）境界事例の記録：**
本論文は提案触媒サイクル（酸化的付加→挿入→還元的脱離）から速度式を代数的に導出しておらず、PRI-11の定義前半（「速度式を代数的に導出せず」）には該当する。ただし定義後半（「観測速度次数との一致のみで機構を支持」）は成立しない——速度次数データ自体が存在しないため、速度次数との「一致」の主張すら行われていない。本ケースはPRI-11よりも原始的な形態（「速度次数測定が実施されていない」）であり、RI-03のサブケースとして分類するのが適切。PRI-11の適用境界条件の明確化に資する事例として記録する。

**5. RI-07の二方向適用（拡張適用事例の確認）：**
本論文では「practical organic synthesis」という肯定的境界主張（効率性・選択性・汎用性を「達成した」）と「applicable more widely」という外挿（将来の適用範囲の肯定）の両方にRI-07が独立したCLA（CLA-1, CLA-2）として適用される。Codebook運用注記（v0.2a）の「否定的境界主張」拡張に加え、「外挿による肯定的境界の過大主張」にもRI-07が適用される事例として記録する。A-1という単一のDeferred itemが複数のRI-07インスタンスを生成する構造を持つことを注記する。
