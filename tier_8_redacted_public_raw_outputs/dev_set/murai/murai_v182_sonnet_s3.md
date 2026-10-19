```
prompt_version: stage3-v3-20260425
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, communication）

### §1 Claim Architecture

**コア主張の要約:**
本論文の中核はRuH2(CO)(PPh3)3触媒によるルテニウム触媒C–H/オレフィンカップリング反応の実証である。Novelty柱は「キレーション補助による選択的C–H活性化」という設計原理の確立（NC-4）であり、Utility柱は「効率・選択性・汎用性すべてが実用的有機合成に要求される水準を達成した」という三重主張（NC-1, NC-2, NC-3）である。この三重主張は互いに相補的：高収率のみではGenerality性が問われ、基質汎用性のみでは実用性が問われるが、三者が揃って「実用的」という枠組みが成立する。

**Layered structureの判定:**
4層構造が成立する。NC-1（効率）・NC-2（選択性）・NC-3（汎用性）は経験的に独立しており、単一の反証では崩せない。NC-4（キレーション補助）は機構的層であり、この層が崩れてもNC-1〜NC-3は経験的事実として残るが、戦略的・説明的価値は消失する。機構的層（NC-4）は実証的層（NC-1〜NC-3）の説明枠組みを提供しているが、両者は論理的に独立している。この層間独立性が、論文が「機構は不明」と認めながら「実用的合成」主張を維持できる構造的根拠である。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [メカニズム的証拠の不在：キレーション補助の正の実証]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 機構の中核を担うシクロメタル化中間体および各素反応ステップが、直接観測も速度論的拘束も受けていない
* **Secondary RI**: RI-06 [Imported model] — シクロメタル化中間体の類推がMn(CO)5・Ru(OAc)錯体という構造的に異なる系から輸入されている（B-3）
* **ER**: RuH2(CO)(PPh3)3から生成するシクロメタル化中間体を単離またはNMR/MS/X線でin situ同定し、さらにキネティクスまたは同位体標識によってその中間体が触媒サイクルの主要経路上にあることを実証すること。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: (a) RuH2(CO)(PPh3)3とアセトフェノンの低温反応によるシクロメタル化錯体の単離・X線構造解析; (b) D₂標識RuD2(CO)(PPh3)3または重水素化アセトフェノンを用いたKIE測定によるM–H結合へのD–H導入経路の追跡; (c) 化学量論的反応でH₂ガスまたはホモカップリング生成物を検出・定量する質量収支実験。
* **注記**: A-1, B-3, B-4, B-7, U-1がこのSRGの構成要素。B-7（1-インダノンの非反応性）は3/3収束（high_convergence_low_gap）、B-3・B-4はV2単独でcritical（low_convergence_high_gap）。PRI-11（Mechanism-kinetics decoupling）の適用候補として§6に記録。

**SRG-2 [GC収率の信頼性と質量収支]**

* **Primary RI**: RI-01 [Reporting integrity] — GC収率の定量法（内部標準・応答係数）が未記載であり、runs間の横比較が不可能
* **Secondary RI**: RI-08 [Unquantified reliability] — 質量収支が全ランで閉じておらず（特にラン1: 83%、ラン2: ~95%）、不確かさの定量がない
* **ER**: GC定量法（内部標準または外部標準、応答係数の実験的決定法）を記載し、全ランについて質量収支を報告すること。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: (a) 内部標準（例：テトラデカン）を用いた検量線作成と全runへの適用; (b) 少なくとも代表的な3–5ランについて単離収率との差の定量的比較; (c) ラン1の残余17%物質の同定（高沸点残渣、Ruへの配位等の検討）。
* **注記**: B-1, B-5が構成要素。high_convergence_low_gap: B-1（2/3収束、gap: none）。Full Paper展開で自動解消される可能性のある通信時代許容パターン。

**SRG-3 [挿入経路の区別: M–H vs. M–C]**

* **Primary RI**: RI-04 [Unreplicated discriminator] — M–H挿入かM–C挿入かの判断に必要な識別実験がなく、単一の機構代替が選ばれていない
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: 重水素標識RuD2(CO)(PPh3)3を用いた実験で、生成物中の重水素位置を決定することでM–H挿入経路とM–C挿入経路を区別すること。
* **EP**: EP-04a [Discrimination / replication pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: RuD2(CO)(PPh3)3とアセトフェノン/トリエトキシシリルエチレンの反応生成物を²H NMRで解析し、重水素の組み込み位置を決定する。
* **注記**: B-4, A-1が構成要素。low_convergence_high_gap: B-4（V2のみ、critical）。SRG-1のサブセット。

**SRG-4 [選択性制御の起源: 速度論的vs.熱力学的]**

* **Primary RI**: RI-05 [Qualitative overread] — 観察された選択性差（ラン1 vs. 9の単/二重カップリング、ラン10 vs. 11の反応速度）から「立体込み合い」「角度歪み」という構造的・因果的含意を数値なしで導出
* **Secondary RI**: RI-07 [Unsupported boundary] — 「virtually 100%」選択性の境界（いつ選択性が崩れるか）が失敗例なしに主張されている
* **ER**: (a) ラン1の1:1付加物を単離し、同条件下で再暴露して二重付加が進行するかを確認（速度論的制御の検証）; (b) ラン10とラン11の時間-転化率プロファイルを取得し、速度差を定量化; (c) 位置選択性の逆転条件（温度・触媒変更）の探索。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-07a [Boundary-test pack]
* **Case-specific実装**: ラン1（アセトフェノン + triethoxysilylethylene）の1:1生成物をbulb-to-bulb蒸留で単離し、標準触媒条件下で2 mmolスケールで再反応させ、二重付加物への転化率をGCで測定する。
* **注記**: B-9, B-8, U-2が構成要素。high_convergence_low_gap: B-9（2/3収束、gap: low）。

**SRG-5 [生成物構造と位置化学の分光学的実証]**

* **Primary RI**: RI-02 [Object identification] — 13種の生成物の構造が「標準的方法」でのみ確認されており、位置化学を確証する具体的な分光データが示されていない
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: 各生成物のアルキル化位置（オルト選択性）を確証するための¹H NMRおよび¹³C NMRデータ、あるいは少なくとも1報について単結晶X線構造解析を提示すること。
* **EP**: EP-02a [Identity / purity substantiation pack]
* **Case-specific実装**: 少なくとも5種の代表的生成物について、¹H NMR（300または500 MHz）の全シグナル帰属、¹³C NMRを報告し、一種についてX線構造解析を行い、ortho選択性の直接証拠とする。
* **注記**: B-2, B-8, U-2が構成要素。high_convergence_low_gap: B-2（2/3収束、gap: low）。

**SRG外：CLA**

**CLA-1 [先行文献との定量的比較の欠如]**（D-4-5に対応）
* **Primary RI**: RI-09 [External superiority] — TOFが「最高水準」と主張するが、数値比較なし（B-5, C-2）
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: refs. 11–12（Jordan & Taylor 1989; Moore et al. 1992）のTOF・収率・基質/触媒比を表形式で比較し、本論文が具体的に何倍優れているかを数値で示すこと。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: Jordan & Taylor (1989) のα-ピコリン/プロペン系のTOF（報告値）と、本論文ラン1・9・10のTOF（計算値、h⁻¹）を同一単位で並列比較した表を作成する。
* **注記**: C-2はantagonist reference exclusionには該当しない（Jordan/Moore論文は批判対象ではなく比較対象）。high_convergence_low_gap: B-5（2/3収束、gap: low）。

**Self-referential validation チェック:**
本論文に該当なし。既知錯体（ref. 13）を用いた実験化学論文であり、新しい記述子・指標・スコア関数を提案していない。PRI-12クラスターAは適用外。

**Deductive-retrospective structure チェック:**
本論文に該当なし。演繹的に導出された選択則・原理を中心主張とする方法論・理論提案論文ではない。PRI-12クラスターBは適用外。

---

### §3 現在のVQ判定

現在判定: **VQ-2 (Method)** — qualified（RI-05残存）

**VQ-1 [Observation] の通過:**
RI-02（Object identification）の解消が必須要件。本論文は13種の生成物の構造を「standard methods」により「unequivocally」確認したと主張しており（B-2）、具体的分光データは不在だが、Nature通信の格式内で最低限の構造帰属主張が存在する。GC収率データは実験の実施を示す証拠として機能する。VQ-1は通る（Non-fatal: B-2は構造帰属の詳細が欠如するが、生成物の実在を否定するものではない）。

**VQ-2 [Method] の通過:**
VQ-2はRI-01とRI-07の解消が必須要件（VQ-1継承を前提）。RI-01（GC定量法の未記載）はNon-fatal：GC法は実験化学の標準であり、1993年のNature通信では応答係数の記載省略は許容範囲内（Era-norm tolerated）。RI-07については、「virtually 100%」の位置選択性は13ランにわたり観察されており、境界条件の欠如はmethodological limitationだがNon-fatal。VQ-2は通る（qualified: RI-05が残存—角度歪み/立体込み合いの定量的根拠なし）。

継承原則注記：VQ-2の成立はVQ-1の通過（RI-02が非致命的）を前提とする。

**VQ-3 [Mechanism] の未達:**
VQ-3はRI-03、RI-04、RI-06の解消が必須要件。
- RI-03: シクロメタル化中間体の直接観測なし → Fatal
- RI-06: 中間体の類推が異種系から輸入 → Fatal
- RI-04: M–H vs. M–C挿入経路の識別実験なし → Fatal
VQ-3 は未達。未解消RI: RI-03（Fatal）、RI-04（Fatal）、RI-06（Fatal）。

**VQ-4 [Benchmark] の未達:**
VQ-3継承原則により評価不可。

**層別VQ非対称性:**
NC-1–NC-3（経験的主張）は独立してVQ-2水準に到達。NC-4（機構的主張：キレーション補助）は単独でVQ-1水準に留まる。**NC-1–NC-3単独では：VQ-2到達の根拠として、13基質の実験データが独立した機構的解釈なしにmethod-level evidenceを構成する。**

---

### §4 Era-Norm Annotation

**communication-era tolerated:**
- B-1（GC定量法・質量収支の未記載）: 1993年のNature通信形式ではGC収率の定量方法の詳細記載は標準要件ではなかった; Full Paper展開で解消される典型的パターン。
- B-2（分光データの未記載）: Nature通信（3頁）では全生成物のNMR/MSデータ記載は不可能; 当時の通信論文の慣行として、実験手順と最終生成物の帰属主張のみが典型的。
- B-6（不活性触媒の収率未記載）: スクリーニング結果の定量記載は通信形式の紙幅制約内で省略可能と当時みなされていた。
- B-7（1-インダノンの条件・転化率未記載）: 陰性結果の詳細条件記載は通信形式では当時許容された省略。

**modern-era deficient:**
- B-7（1-インダノン非反応性）: 現代基準では、機構的主張の根拠として使用された陰性結果には検出下限・反応条件・GC転化率データが必須; VQ-3到達の必要条件（RI-03の解消）に直接抵触。
- A-1 + B-3 + B-4（機構の明示的不明記載と類推のみの提案）: 現代の有機金属化学Full Paperでは最低限のメカニズムプローブ（KIE測定、ラジカルクロック、同位体標識）が期待される; VQ-3の必須要件に直接抵触。
- U-2（位置選択性の分光学的未実証）: 現代基準では「virtually 100% regioselectivity」主張にはX線またはNOESY等の分光学的位置化学確証が必須。

---

### §5 最短補強ルート

**VQ-3 への最短ルート（第一目的関数）：**

1. EP-03a [Direct-observation / state-assignment pack] — RuH2(CO)(PPh3)3とアセトフェノンの低温反応によるシクロメタル化中間体のNMR/MS同定または単結晶X線構造解析。RI-03 を前進。
2. EP-04a [Discrimination / replication pack] — RuD2(CO)(PPh3)3を用いた重水素標識実験で生成物中のD位置を決定し、M–H vs. M–C挿入経路を識別。RI-04 を前進。
3. EP-06a [Analogy-validation pack] — RuH2(CO)(PPh3)3と遊離カルボニル配位子の有無に応じて選択性が変化するかの競争実験で、カルボニル配位の速度論的役割を実証。RI-06 を前進。

認定ゲート順注記：実験投入順は情報利得順（EP-03a → EP-04a → EP-06a）だが、VQ認定は VQ-1 → VQ-2 → VQ-3 の継承ゲート順で確定する。

**VQ-4 への最短ルート（第二目的関数、VQ-3達成後）：**

4. EP-09a [Internal benchmark pack] — Jordan & Taylor (1989) およびMoore et al. (1992)と共通基質・条件でTOFを数値比較。RI-09 を前進。
5. EP-08a [Replication / uncertainty pack] — 代表的3ランについて独立3連測定を実施し、GC収率の再現性と標準偏差を報告。RI-08 を前進。

認定ゲート順注記：VQ-4は VQ-3 の完全成立を前提とし、RI-08とRI-09の解消が必要。

---

### §6 制度設計への寄与

**既存RIコードの代表事例提供:**
- RI-03（Unobserved explanatory）の典型事例：「The mechanism is not yet clear」から始まり触媒サイクルを提案する通信論文パターン。直接観測なし・類推のみの提案（RI-03 + RI-06の共起）として記録。

**PRI昇格判断材料:**
- **PRI-11（Mechanism-kinetics decoupling）の適用候補**: 本論文はラン10とラン11の反応速度差を機構的主張（角度歪み→キレーション効率）の証拠として使用しているが、速度式の代数的導出なしに速度差から機構を支持している。Breitenfeld 2014、Pengfei 2024に次ぐPRI-11の3報目候補として機能しうる（弱い形態：速度次数ではなく反応時間からの推論）。

**VQ判定の境界条件:**
- **層別VQ非対称性の実例**: 経験的主張（VQ-2到達）と機構的主張（VQ-1止まり）が単一論文内で共存。通信論文において系統的に観察されるパターン。層別VQ非対称性判定の運用実例として記録する。

**否定的証拠の不完全性パターン:**
- B-7（1-インダノンの非反応性）は機構的主張の正証拠として使用された否定的証拠の典型例。「陰性結果を機構的証拠として使用する際の最低要件（条件・検出下限・基質回収の記載）」をRI-04のcase-specific実装として制度化すべきパターンを提供する。
```
