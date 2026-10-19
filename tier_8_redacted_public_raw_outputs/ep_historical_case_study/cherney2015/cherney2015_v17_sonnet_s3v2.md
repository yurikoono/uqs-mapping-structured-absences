```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6
```

# 科学的知見の再認定判定票

## Cherney, Kadunce & Reisman 2015（Chemical Reviews, review）

---

### §1 Claim Architecture

**コア主張の要約**

Novelty柱は二層構造をなす。N-1は「エナンチオ選択的反応（触媒が立体化学を定義）とエナンチオ特異的反応（基質が立体化学を定義）を単一の概念的枠組みで統合し、すべての不斉様式（中心・軸・平面）にわたって整理した初の総合的レビューである」という建築的主張であり、N-3はその枠組みの分類原理自体（エナンチオ選択的/エナンチオ特異的タクソノミー）を novelty として暗示する分類的主張である。Utility柱は N-2（2014年末までの文献の包括的網羅）と N-4（DYKAT・DKR・DET・ラジカル酸化的付加・SET という機構的フレームによる解釈的統一）から成り、"profound growth" を記録し "a wealth of new tools" を提示するという rhetorical 主張（N-4）がそれを包む。

**Layered structureの判定**

4層は独立している。N-1（建築的・概念的層）は個々の反応データや機構解釈の正否によって崩れない——構造化した初の統合レビューという事実は保たれる。N-2（書誌的層）は誤記載や系統的な文献見落しがなければ成立し、機構的主張の正否に左右されない。N-3（分類的層）は「エナンチオ選択的/エナンチオ特異的」という区分の論理的一貫性に依拠し、実データ（es < 100%）との乖離（CLA参照）が問われなければ成立し続ける。N-4（rhetorical層）は最も反証されにくく、「多数の新ツールが存在する」という主張は機構の正確さとは独立である。単一の反証で全体が崩れるシングルポイント・フェイルはなく、最も脆弱な層は N-3（分類的整合性）と N-4の機構的部分（DYKAT・DET・SET の検証なし）であり、N-2（書誌網羅）と N-1（統合性）が最も堅牢である。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [DYKAT/KR識別のための転化率依存データの不在]**

* **Primary RI**: RI-06 Imported model — DYKAT という触媒サイクルモデルが「配置不安定な金属試薬の一般動力学論」から輸入され、Ni触媒 sec-アルキルMg系における同型性（krac >> kproductive の条件充足）の実証なしに適用されている。
* **Secondary RI**: RI-03 Unobserved explanatory — krac/kproductive という説明の核心を担う速度比が、直接計測も速度論的拘束（転化率-ee プロファイル）もされていない。
* **ER**: DYKAT適用の規範的要件は、基質ラセミ化速度（krac）と有用産物形成速度（kproductive）の比の実測、または転化率依存 ee プロファイルによる間接検証である。KR ならば ee は転化率増加で単調増加し、DYKAT ならば転化率非依存となるため、両者は原理的に区別可能である。
* **EP**: EP-06a Analogy-validation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: Ni/PPFA (L13) 系の sec-ブチルMgBr / クロロベンゼン反応（Figure 3基準系、1973年 Kumada 条件）において、転化率 10%, 30%, 50%, 70%の各時点でのサンプリングと ee 測定（キラルHPLC）を実施する。ee が転化率に依存しない場合 DYKAT、単調増加する場合 KR と判定できる。代替として、sec-アルキルMgBr のラセミ化半減期（t₁/₂,rac）をDeuterium標識競合実験で直接測定し、DYKAT 条件の充足を確認する。
* **注記**: 下位項目 B-1（anchor）、B-8（歴史的 KR/DYKAT 曖昧性の明示的承認）、U-2（Kagan-Durst 定量的予測の未検証）。TEMPERATURE_SUMMARY: B-1 は high_convergence_low_gap（convergence=3/3, temperature_gap=none, 全エージェント high）。SRG-1 は VQ-3 達成の一次障壁。

---

**SRG-2 [触媒サイクル機構提案の直接実験的検証不在]**

* **Primary RI**: RI-03 Unobserved explanatory — DET経路（U-1）、π-アリルPd中間体（B-7）、NiIII/IrII ラジカル中間体（U-3）という複数の触媒サイクル中の説明的中核種が、直接観測も速度論的拘束もされていない。
* **Secondary RI**: RI-04 Unreplicated discriminator — B-7 において収束生成物形成という単一の観測から π-アリルPd中間体の存在が推論されており、同等の産物分布を与える代替機構（DET型の直接 SN2' 攻撃）が排除されていない。
* **ER**: 機構提案の規範的要件は、(i) 提案中間体の分光学的捕捉または独立した合成による予言的検証、(ii) 代替機構（DET vs KR, π-アリル vs 直接 SN2', SET vs 二電子トランスメタル化）を排除する制御実験の提示である。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-04a Discrimination / replication pack
* **Case-specific実装（U-1向け）**: Cu/L32 系の環状アリル基質（Figure 64 基準系）において、転化率 10-90% の範囲での ee プロファイルを測定する。DET ならば ee 転化率非依存；KR ならば単調増加。**（U-3向け）**: Ni(cod)₂/BiOX L34/Ir[dF(CF₃)ppy]₂(dtbbpy)PF₆ 系（Figure 11基準系）で EPR 測定（NiIII の検出: g ≈ 2.1–2.2付近の常磁性シグナル）および Stern-Volmer クエンチング実験（アリールトリフルオロボラートの添加による *Ir(III) 発光強度の消光確認）を実施する。**（B-7向け）**: 収束生成物を与える異性体アセタート 408/409 双方の実験において、ラジカルクロック基質（シクロプロピルカルビニル型）を導入した対照実験でラジカル経路の有無を排除する。
* **注記**: 下位項目 B-4（ジ置換アルケン選択性の機構的未帰属）、B-7（π-アリル収束推論）、U-1（DET ee-転化率不変性の未確認; low_convergence_high_gap, V2-Q6=high）、U-3（NiIII/IrII の未観測; low_convergence_high_gap, V2-Q10=high）。SRG-2 と SRG-4 は RI-03 において連立しており、単一の EP-03a 投入で両 SRG を同時に前進させることができる。

---

**SRG-3 [ee/収率データの横断比較不能性]**

* **Primary RI**: RI-01 Reporting integrity — 1972〜2014年にわたる文献から収集した ee 値が、旋光度比較・NMR キラルシフト試薬・キラル GC・キラル HPLC/SFC という異なる分析手法で測定されており、測定フレームと条件記述が不統一で横断比較が原理的に困難である。Figure 5 キャプションの局所的免責（"comparisons should be drawn with caution"）はセクション全体に拡張適用されていない（B-3）。
* **Secondary RI**: RI-08 Unquantified reliability — 比較データに反復測定や測定不確かさ（±N%）の記述が皆無であり、単一測定値が代表値として流通している。
* **ER**: データ比較の規範的要件は、(i) 使用した分析手法の明示（HPLC カラム名・移動相・検出器・GC カラム名）、(ii) 測定不確かさ（少なくとも反復 n=2 以上）の報告、(iii) 異なる手法間での精度差の開示（例：旋光度 ±5% vs HPLC ±0.5%）である。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: Figure 5 に示される 20 種以上の配位子-ee データセットについて、各データ点の取得論文・分析手法・測定条件を系統的に付記した補完メタデータ表を作成する。さらに、最も多く引用されているベンチマーク系（α-methylbenzyl Grignard + vinyl bromide + NiCl₂/PPFA, L13）について独立 3 報以上の再現実験から得た ee データを集計し、測定法間差異を定量化する。
* **注記**: 下位項目 B-2（検索手法の非開示）、B-3（Figure 5 の局所的免責のみ; high_convergence_low_gap, convergence=2/3, temperature_gap=none）。SRG-3 は主に RI-01 + RI-08 の共起パターン（両者の同時解消が必要）であり、VQ-4 達成の主要障壁。

---

**SRG-4 [Ni/Ir光レドックス二重触媒サイクルの熱力学的・分光学的検証不在]**

* **Primary RI**: RI-03 Unobserved explanatory — SET → アルキルラジカル → NiIII → 還元的脱離 → NiI → IrII という提案サイクルの核心的中間体（NiIII, IrII）が観測されておらず、SET の熱力学的実現可能性（オルガノボラン基質の酸化電位 vs *IrIII 励起状態還元電位の比較）も未確認であり、Stern-Volmer クエンチングデータも不在。
* **Secondary RI**: RI-06 Imported model — 本 Ni/Ir 光レドックスサイクルは Molander ら（Tellis et al., Science 2014, ref 63）の Suzuki-Miyaura 系から触媒サイクル全体を構成し（サイクルレベル輸入）、BiOX L34/NicBOX 系での同型性実証（酸化電位の適合性）なしに不斉化応用へ転用されている。
* **ER**: 二重触媒サイクル提案の規範的要件は、(i) SET の熱力学的実現可能性（基質酸化電位と *Ir 励起状態還元電位の cyclic voltammetry による実測と比較）、(ii) Stern-Volmer 実験による *Ir(III) 発光クエンチングの確認、(iii) NiIII 中間体の EPR または UV-vis 観測（または電気化学的酸化ポテンシャルからの熱力学的推定）の提示である。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific実装**: Figure 11 の BiOX L34/Ni(cod)₂/Ir[dF(CF₃)ppy]₂(dtbbpy)PF₆ 系で、(i) アリールBF₃K 基質の電気化学的酸化電位（cyclic voltammetry, vs SCE or Fc/Fc⁺）、(ii) Ir[dF(CF₃)ppy]₂(dtbbpy)⁺ の *Ir(III) 励起状態還元電位（文献値: E* ≈ +1.3 V vs SCE）との比較、(iii) Stern-Volmer 実験（基質添加量増加に対する *Ir 発光強度の消光プロット、kq の取得）を実施する。BF₃K 酸化電位が *Ir 還元電位より負であれば SET は熱力学的に許容される。
* **注記**: 下位項目 B-6（"proof of concept" 修辞による未検証の軟着陸; high_convergence_low_gap, convergence=3/3, temperature_gap=low）、U-3（NiIII/IrII の未観測; low_convergence_high_gap）、A-4（"additional investigations toward asymmetric catalysis" として検証を外置）。SRG-4 は SRG-2 のサブケースとして機能し、U-3 は両 SRG に属するが、SRG-4 は SET の熱力学的実現可能性という問いを独立に含む点で SRG-2 より広い。

---

**SRG-5 [実用合成との橋渡し：境界の文書化不全と定量的実証の不在]**

* **Primary RI**: RI-07 Unsupported boundary — "yet to be realized"（A-1: sec×sec クロスカップリング）、"largely undeveloped"（B-5: tert-アルキル系）という境界主張が、失敗例・試行済みの低 ee 文献・スクリーニング結果の体系的引用なしに行われており、「未試行」と「試行済みだが未達」の区別が不明。
* **Secondary RI**: RI-05 Qualitative overread — "wealth of new tools"（N-4）および "streamline the synthesis of complex molecules"（A-3, D-2 audience_targeting）という定性的主張から実用的有用性という構造的・因果的含意を導出しているが、全合成への適用頻度、スケール実証、触媒量の実用化適合性の定量的根拠を欠く。
* **ER**: 境界主張の規範的要件は、「試みられたが成功しなかった」系の文献列挙（負の結果の体系的報告）または「当該文献は存在しない」ことの検索開示であり、定性的有用性主張の要件は全合成適用例の包括的カタログ（適用論文数、基質多様性、スケール、触媒量）の提示である。
* **EP**: EP-07a Boundary-test pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: sec×sec クロスカップリング（A-1）について 2008-2014 年の文献検索で「試行済みだが低 ee（<50%）または低収率（<30%）」で報告された例を列挙し、"not yet realized" の意味を「未試行」と「未達成」に区別する注釈を追加する。並行して、Section 2–5 の全手法（推定 100+ 手法）のうち多段階全合成に適用された例を系統的に集計し（goniofurane, glucokinase activator, bourgenic acid 等）、全体に占める割合を算出する。
* **注記**: 下位項目 A-1（sec×sec 未達, T1）、A-2（sp³ ボロン/スズ試薬調製の bottleneck, T1）、A-3（アトロポ選択性の一般化不足, T1）、B-5（tert-アルキルの "largely undeveloped" 根拠不明）。SRG-5 は VQ-2 水準の RI-07 に対応するが、RI-05 の残存により VQ-3 でも Qualified 判定の原因となる。

---

**SRG外：CLA**

**CLA: D-4-5 [エナンチオ特異的分類定義と実測 es 値の内的不整合]**

grounded_in: U-4（定義と実測 es の乖離; いずれの SRG にも属さない）、C-2（Crudden Rh ヒドロホウ素化の ee が独立に未報告; いずれの SRG にも属さない）

このCLAはN-3（enantioselective/enantiospecific タクソノミー）という Novelty Pillar の論理的一貫性に直接関わる。

* **Primary RI**: RI-05 Qualitative overread — "エナンチオ特異的"という定義（[REDACTED: substantial verbatim quotation; see Tier 9]）は立体化学の完全伝達を含意するが、Section 3 の実測 es 値（65–99%）が定義と矛盾する範囲にわたっており、es 低下の原因（基質部分ラセミ化・触媒による立体反転・副経路での情報消失）が系統的に議論されていない。
* **Secondary RI**: RI-02 Object identification — es < 100% の各反応において、es 低下が生じる反応段階（酸化的付加段階のラセミ化、トランスメタル化段階の立体反転、還元的脱離段階の立体保持失敗）が特定されておらず、「エナンチオ特異的」カテゴリの構成要件（= どの段階での立体情報が産物 ee を決定するか）が不確定のまま分類体系が運用されている。
* **ER**: 分類定義の規範的要件は、定義が含意する特性（立体化学的完全伝達）からの逸脱事例について、es 低下の反応段階的帰属と、「エナンチオ特異的」と呼べる閾値（例: es ≥ 95%）の明示である。es 65% の反応が es 99% の反応と同一カテゴリに属することの妥当性を文書化する必要がある。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-02a Identity / purity substantiation pack
* **Case-specific実装**: Section 3 の全「エナンチオ特異的」反応について es 値の分布図（ヒストグラム）を作成し、es < 95% の例（推定 20-30%）に対してトランスメタル化段階の立体完全性を単独で評価する制御実験（基質 ee を変化させて es/ee 線形性を確認する de Mayo プロット）を設計する。また、C-2 の Crudden 系（boronate 163 → 164）でのヒドロホウ素化ステップの ee を独立測定し、Suzuki-Miyaura ステップの es を基質 ee から分離して評価する。
* **注記**: 自己矛盾的不在パターン該当——論文自身の定義が "defines the stereochemistry" という完全伝達を予言するが、実測データはこれを否定する。CLA は N-3 の Novelty 主張に対する最も直接的な反証起点であり、SRG-1 の DYKAT/KR 区別問題と構造的に類似する（定義が観測データで検証されないパターン）。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method, qualified)**

---

**VQ-1 (Observation) は通る。**

生成物の構造・純度については、論文全体を通じて多数の化合物が ee（またはes）測定値と収率とともに報告されており、RI-02 の致命的問題は存在しない。C-2（Crudden Rh ヒドロホウ素化産物 163 の ee が独立に未報告）は非致命的な局所的 RI-02 問題として残存するが、この不在は Suzuki-Miyaura ステップの es 評価を困難にするものの、生成物 164 の同定自体を無効化しない。VQ-1通過。

---

**VQ-2 (Method) は通る（qualified）。** VQ-1継承前提。

RI-07（Unsupported boundary）については、SRG-5 の B-5・A-1〜A-3 が境界主張を失敗例なしに行っているが、Chemical Reviews 形式のナラティブレビューにおいて "future directions" として未達領域を記述することは 2015年時点の出版慣行内（Era-norm tolerated）であり、非致命的と判断する。

RI-01（Reporting integrity）については、SRG-3 の B-3 が ee 測定法の不統一を系統的に問わない点で残存するが、2015年時点のナラティブレビューでは PRISMA型報告や分析手法の統一記述は標準要件ではなかった（Era-norm tolerated）。現代基準では致命的だが、対象論文の発表年（2015年）での判定では非致命的。

RI-05（Qualitative overread）については、CLA（D-4-5）と SRG-5 で残存するが、定性的な有用性主張はレビュー形式では広く許容されており、VQ-2 の通過を妨げる致命的問題ではない。ただし RI-05 の残存により、VQ-3 の評価は「qualified（限定的）」となる（後述）。

VQ-2通過（qualified: RI-01, RI-05が非致命的に残存; SRG-3, CLA D-4-5が解消未済）。

---

**VQ-3 (Mechanism) は未達。** VQ-2継承前提。

RI-03（Unobserved explanatory）が SRG-1（krac/kproductive 未測定）、SRG-2（DET経路・π-アリルPd・NiIII/IrII の未観測）、SRG-4（SET 熱力学的実現可能性未確認・NiIII/IrII 未観測）に致命的に集積しており、いずれも現代の機構論的基準で致命的。B-1（DYKAT モデルの krac/kproductive 未実測）はレビュー全体の機構的解釈フレームの根幹に位置し、U-1（DET転化率-ee 不変性の未確認）・U-3（NiIII/IrII 未観測）はいずれも論文が提案するモデルが予言する観測量が未報告という自己矛盾的不在に該当する。

RI-06（Imported model）も SRG-1（DYKAT モデル輸入）と SRG-4（Ni/Ir サイクルレベル輸入）で致命的に残存する。

なお、RI-05 が CLA（D-4-5）で重大に残存するため、VQ-3 に達したとしても「VQ-3 (qualified)」となる。

VQ-3未達（主未解消RI: RI-03 in SRG-1, SRG-2, SRG-4; RI-06 in SRG-1, SRG-4）。

---

**VQ-4 (Benchmark) は未達（VQ-3継承不成立のため）。**

参考として、VQ-4 独自要件を評価すると：RI-08（Unquantified reliability）は SRG-3 で致命的に残存し（反復測定・不確かさ記述の全般的不在）、RI-09（External superiority）は C-3・C-4・C-5 の定量的 es 比較不在として非致命的に残存する。

---

**層別VQ非対称性：**

§1の Layered structure で独立層として同定された N-2（書誌的層）単独では：VQ-2（B-2のRI-07が非致命的）を通る。網羅的レビューとしての書誌的完全性は 2015年時点の Chem. Rev. 形式において VQ-2 に到達している。

N-1（建築的統合層）単独では：VQ-1を大きく超え VQ-2 に到達しているが、N-3（分類的層）は CLA（D-4-5）のRI-05 + RI-02 により VQ-1 (qualified) 相当に留まる。このN-1 vs N-3の非対称性は、「統合アーキテクチャは堅牢だが、その基礎となる分類定義が内的に不整合」という論文の最も根本的な脆弱性を示す。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- B-2（検索手法・inclusion criteria の非開示）: Chem. Rev. 2015年時点では PRISMA型系統的文献検索の開示は narrative review には求められておらず、「包括的」は著者の判断として許容されていた。
- B-3（Figure 5 のみへの比較注意書き; 全体への拡張なし）: 2015年の合成化学レビューにおいて ee データの横断比較は分析手法の統一なしに慣例的に行われており、局所的免責でのみ対処する形式は Chem. Rev. 形式内で許容されていた。
- B-8（1972-1974年 Kumada 初期反応の KR/DYKAT 曖昧性の明示）: 50年前の一次論文に対してマスバランス遡及を要求することは 2015年当時の review 規範外であり、曖昧性を「重要な proof of concept であるが機構的に不確定」と歴史的に位置づける記述は適切な許容範囲内にあった。
- B-5（"yet to be realized"/"largely undeveloped" という Future Directions 記述）: Chemical Reviews の conclusion 節で未達領域を定性的に記述することは 2015年時点の標準フォーマットであり、負の結果の体系的引用は要求されていなかった。
- A-4（"additional investigations toward asymmetric catalysis would be valuable" という proof-of-concept の外置）: 50% ee という限定的結果を"proof of concept"として提示し、最適化を将来課題とする記述様式は、新手法の初報告を含むレビューの書き方として 2015年当時許容されていた。

**modern-era deficient:**

- B-1（DYKAT の krac/kproductive 未測定; Section 2.1–2.2 全体にわたる致命的 RI-03）: 2025年の機構論的基準では、DYKAT という機構分類の適用には速度論的根拠（転化率-ee プロファイルまたは競合動力学実験）が必須とされ、未測定のまま DYKAT を標準的機構説明として採用することは致命的欠落。
- B-6, U-3（光レドックス SET の熱力学的・分光学的未検証）: 2018年以降の光レドックス研究では基質の電気化学的酸化電位測定、Stern-Volmer クエンチング実験、EPR による金属中間体の直接観測が標準的報告要件となっており、これら全てが不在であることは現代基準では致命的。なお B-6 は Era-norm tolerated と modern-era deficient の両タグに該当する——2015年当時は "proof of concept" として許容されたが、現代ではその許容範囲が消滅している。
- SRG-3（RI-01, RI-08: ee 測定法の統一記述・反復測定の不在）: 2020年以降の系統的レビュー化の要求（PRISMA-Chem などの動き）および再現性危機への対応として、分析手法の明示と測定不確かさの記述は現代では必須とされる。
- CLA D-4-5（es < 100% の系統的未分析）: 現代では立体特異的反応の報告において、es 低下の反応段階的帰属（de Mayo プロットによる基質 ee-産物 ee 線形性確認）が求められており、未分析のまま "enantiospecific" という分類を一括適用することは現代基準では不十分。

---

### §5 最短補強ルート

**現在 VQ-2 (qualified) → 第一目的関数: VQ-3**

VQ-3 達成に必要な主要未解消 RI: RI-03（SRG-1, SRG-2, SRG-4）、RI-06（SRG-1, SRG-4）

---

**VQ-3 への最短ルート：**

1. **EP-03a** Direct-observation / state-assignment pack — Ni/Ir 光レドックス系（Figure 11 基準系）で EPR 測定（NiIII 検出）+ Stern-Volmer 実験（*Ir(III) クエンチング確認）+ cyclic voltammetry（BF₃K 基質酸化電位）を実施するバンドル実験。SRG-2（U-3）と SRG-4（B-6, U-3）を同時に前進させる——最大の情報利得。**RI-03（SRG-2・SRG-4）を前進。**

2. **EP-06a** Analogy-validation pack — Ni/PPFA (L13) 系（Figure 3 基準系、または Figure 5 の標準系）で転化率 10-70% 範囲の ee プロファイルを取得し、DYKAT モデルの同型性を対象系で直接検証する。**RI-06（SRG-1）を前進；RI-03（SRG-1）を同時に前進。**

3. **EP-04a** Discrimination / replication pack — Cu/L32 系環状アリル基質（Section 4.1.1）での転化率-ee プロファイルにより DET vs KR を識別；B-7 のπ-アリル推論に対するラジカルクロック対照実験。**RI-03（SRG-2: U-1, B-7）を前進；RI-04（B-7）を解消。**

*認定ゲート順注記: 実験投入順は情報利得順（EP-03a → EP-06a → EP-04a）だが、最終認定は VQ-1 → VQ-2 → VQ-3 の継承ゲート順で確定する。VQ-3認定にはRI-03の解消（SRG-1, SRG-2, SRG-4 の三SRG全て）とRI-06の解消が必須。また RI-05 が CLA D-4-5 で残存する場合、VQ-3 (qualified) 止まりとなる。*

---

**VQ-4 への最短ルート（VQ-3達成後）：**

4. **EP-01a** Reporting-coherence pack — Figure 5 の全 ee データ点について分析手法メタデータ（HPLC カラム・移動相・測定温度）を付加した補完表を作成し、RI-01 の測定フレーム不統一を解消する。**RI-01（SRG-3）を前進。**

5. **EP-08a** Replication / uncertainty pack — ベンチマーク系（α-methylbenzyl Grignard / vinyl bromide / NiCl₂/PPFA）について独立グループによる n=3 以上の反復実験で ee 不確かさを定量化（±N%）する。**RI-08（SRG-3）を前進。**

6. **EP-09a** Internal benchmark pack — C-3（Cu-媒介 vs Pd触媒 Stille カップリングの定量的 es 比較）と C-4（1985年 Fiaud/Aribi-Zouioueche の es 数値の回収）の数値ベンチマークを補完する。**RI-09（C-3, C-4, C-5）を前進。**

---

### §6 制度設計への寄与

**1. RI-06「サイクルレベル輸入」サブタイプの強力な代表事例**

本論文は RI-06 の「サイクルレベル輸入」サブタイプ（Codebook v0.2a 注記）の最も明確な事例を提供する。SRG-1（DYKAT モデル）と SRG-4（Ni/Ir 光レドックスサイクル）の両方が「個別素反応の類推ではなく触媒サイクル全体を別系から構成する大規模モデル輸入」に該当する。特に SRG-4 は、Tellis et al.（Science 2014）の Suzuki-Miyaura 系から不斉化への転用という「応用先が異なるサイクルレベル輸入」であり、転用に際して基質の酸化電位適合性が未確認のまま提案されている。この事例は今後の RI-06 適用判断の参照事例として Codebook に追加すべきである。

**2. PRI-11（Mechanism-kinetics decoupling）の3報目確認——正式昇格判断材料**

本論文は PRI-11（「提案触媒サイクルまたは反応機構から速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持している」）の新たな事例を複数提供する。B-1（DYKAT：krac/kproductive の速度的検証なし）、B-7（π-アリル Pd：収束産物形成から機構的推論、速度論的導出なし）、U-3（光レドックス SET：サイクルの熱力学的検証なし）の3事例が独立して PRI-11 パターンを示す。Breitenfeld 2014 と Pengfei 2024 に続く3報目の独立確認（1論文内で複数事例）として、PRI-11 の正式昇格（暫定コードからの格上げ）を支持する証拠として記録する。

**3. RI-05の複合問題としての新規CLA（D-4-5）パターン**

本論文では「分類定義が予測する特性（完全立体化学伝達 = es ≡ 100%）が実測データ（es = 65–99%）で内部的に矛盾するにもかかわらず、定義修正・例外規定・閾値明示なしに分類体系が運用される」というパターンが CLA（D-4-5）として同定された。これは RI-05（Qualitative overread）の特殊形——「定義内の含意的数値予言と実観測値の乖離が問われない」ケース——であり、既存の RI-05 代表事例（順位からの因果含意導出）とは構造が異なる。EP-05a の Case-specific 実装における「de Mayo プロット（基質 ee vs 産物 ee の線形性確認）」を RI-05 の新規検証手順として EP 辞書に追加することを提案する。

**4. 標識不整合パターンの分布**

本論文における機構的提案の標識不整合（仮説標識と事実的記述語の混在）は、文書全体に分散している。B-6（"would generate an alkyl radical"、"can then combine"）は文の中央部に仮説標識（助動詞 would/can）があり末尾の "would be valuable"（A-4）で仮説性を再確認する構造。B-7（"suggests that they proceed through"）は提案であることを示すが、直前の Section 4.2 全体では π-アリルPd が事実的語法で記述されている。SRG-1 全体にわたって DYKAT という名称が仮説標識なしで標準的機構語として使用されている（B-1）のが最も広範な標識不整合事例。RI-06 と連動するこの標識不整合は、Chem. Rev. 形式が「機構的提案を引用により継承した場合に著者の批判的距離が消失する」という書式的脆弱性を示しており、§4 の Era-norm tolerated の根拠の一部をなす。

**5. VQ判定：Chem. Rev. ナラティブレビュー形式の Era-norm 境界条件**

本論文を通じて、「ナラティブレビュー形式での RI-01（報告整合性）・RI-08（測定不確かさ不在）は 2015年基準では非致命的、2025年基準では致命的」という Era-norm の時間的境界が明確になった。この境界は §4 の判定マニュアルに参照事例として記録されるべきであり、特に「Chem. Rev. 2015年発表の合成化学レビューで ee 測定法の統一記述が不在 → Era-norm tolerated（2015）かつ modern-era deficient（2025）」という二重タグの事例として追加する。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
