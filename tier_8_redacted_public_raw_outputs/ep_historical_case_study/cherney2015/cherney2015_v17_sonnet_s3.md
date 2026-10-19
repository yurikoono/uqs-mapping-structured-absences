prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Cherney, Kadunce & Reisman 2015（Chemical Reviews, Review）

---

### §1 Claim Architecture

**コア主張の要約**

本レビューのノベルティ柱は、（1）エナンチオ選択的クロスカップリング（触媒制御型）とエナンチオ特異的クロスカップリング（基質制御型）を初めて単一の概念的枠組みのもとに統合したこと、および（2）2014年末までの文献を金属触媒・有機金属求核剤・不斉中心の種類（中心・軸・平面）に基づいて網羅的に整理したことである。ユーティリティ柱は、不斉合成化学者に対して遷移金属触媒 C–C 結合形成の「豊富なツール群」を一覧参照可能な形で提供することである。具体的には、Ni・Pd・Cu・Rh・Ir・Co 触媒にわたる 100 以上の反応系が、DYKAT・DKR・DET・ラジカル酸化的付加・SE2(cyclic)/SE2(open) などの機構的フレームで整理されている。

**Layered structure の判定**

4 層独立構造（D-1 参照）：N-1（概念的統合）は単一の実験的反証では崩れない。N-2（書誌的網羅性）は文献の系統的見落としの指摘によってのみ揺らぐ。N-3（分類学的枠組み）は enantioselective/enantiospecific の二項分類が機能しない反応系の存在によってのみ問われる。N-4（場の変容の記録）は修辞的主張であり実験的には反証不可能。いずれか一層が崩れても他三層は独立に成立するため、単一の反証で全主張が崩れる構造にはなっていない。ただし N-3 の enantiospecific 定義と実測 es 値の乖離（U-4/CLA-1）は N-1 の統合枠組みの内的一貫性を間接的に傷つける。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [DYKAT/KR 識別不能 — 転化率依存 ee データ不在]**

* **Primary RI**: RI-06 Imported model
  — DYKAT は物理有機化学の速度論モデル（krac >> kproductive という条件が満たされるとき、DYKATが KR より高 ee を与える）を有機金属触媒系に輸入したものだが、対象反応系での krac/kproductive 比がいかなる条件下でも測定・推定されておらず、モデルの同型性が実証されていない。

* **Secondary RI**: RI-03 Unobserved explanatory
  — sec-アルキル金属試薬の二つのエナンチオマー間の「速い平衡」は機構の中核に置かれているが、この平衡過程そのものを直接観測または速度論的に拘束したデータは報告されていない。

* **ER**: DYKAT を支配的機構として割り当てるには、（1）反応温度での krac の独立測定または速度論的下限の推定、および（2）転化率を段階的に変えた時点での ee の測定（ee が転化率に依存しない→DYKAT；単調増加→KR）が規範的に要求される。

* **EP**: EP-06a Analogy-validation pack ; EP-04a Discrimination/replication pack

* **Case-specific 実装**: Section 2.1.1 の Ni/DIOP (L1) 系において、sec-ブチルマグネシウムブロミドの自己ラセミ化半減期を反応温度（例: 0 °C）で NMR または偏光測定で測定し、Ni 存在下の反応速度（TON/time）と比較する。並行して、5%・20%・50%・80% 転化率での ee を chiral HPLC で測定し、ee-転化率プロファイルが DYKAT 型（平坦）か KR 型（単調増加）かを判定する。

* **注記**: B-1（SRG-1 anchor, high_convergence_low_gap, convergence=3/3, 全エージェント=high）, B-8（KR/DYKAT 曖昧性の歴史的記録, convergence=1/3）, U-2（Kagan-Durst 定量検証の自己矛盾的不在, medium）。TEMPERATURE_SUMMARY で最優先（フォールバック規則(b)最上位）。

---

**SRG-2 [機構的提案群の直接的実験検証不在]**

* **Primary RI**: RI-03 Unobserved explanatory
  — DET の各エナンチオマー固有反応経路（U-1）、Pd π-アリル中間体（B-7）、ラジカル酸化的付加中間体（B-4）、SET で生成する NiIII と IrII（U-3）は、いずれもレビューの機構的説明の中核を担いながら直接観測も速度論的拘束もされていない。

* **Secondary RI**: RI-04 Unreplicated discriminator
  — 立体収束（stereoconvergence）・産物収束（convergent products）・単一時点 ee という単一の間接的観察が、代替機構排除なしに機構的割り当ての決め手として使用されている（B-7: π-アリルを産物収束から推定、U-1: DET を転化率-ee 独立性の未実測のまま計算提案のみで採用）。

* **ER**: 各機構的割り当てに対して、それぞれの中間体の直接観測（EPR・UV-vis・NMR）または代替機構を排除する識別実験（ラジカルクロック・クロスオーバー・転化率プロファイル）が規範的に要求される。

* **EP**: EP-03a Direct-observation/state-assignment pack ; EP-04a Discrimination/replication pack

* **Case-specific 実装**:
  — DET (U-1): Section 4.1.1 の Cu/L32 触媒環状アリル置換（Figure 64）で、転化率 10%・30%・60%・90% の各時点で ee を chiral HPLC 測定し、ee-転化率プロファイルが DET 型（平坦）か KR 型（単調増加）かを判定する。
  — π-アリル Pd (B-7): Section 4.2.1 の酢酸アリル基質 408/409 を用いた反応で、ストイキオメトリック量の Pd を使って π-アリル Pd 錯体の生成を NMR または ESI-MS で確認する。
  — ラジカル OA (B-4): 1-ブロモインダン等のラジカルクロック基質を用いた対照実験で、環開環産物の有無によりラジカル中間体の寿命を評価する。

* **注記**: B-4 (SRG-2, convergence=1/3), B-7 (SRG-2, convergence=1/3, medium), U-1 (low_convergence_high_gap, V2-Q6=high), U-3 (low_convergence_high_gap, V2-Q10=high)。SRG-2 は D-4-3 (DET) のフォールバック規則(a) 候補を含む。

---

**SRG-3 [ee/収率データの測定法異質性と網羅性の系統的未評価]**

* **Primary RI**: RI-01 Reporting integrity
  — 1972年〜2014年の ee 値は旋光度・NMR キラルシフト試薬・chiral GC・chiral HPLC/SFC と異なる分析手法で測定されており、手法間の精度差と誤差範囲に関する系統的評価がない。Figure 5 キャプションのみに注意書きがある（B-3）が、全体の横断比較に適用されない。

* **ER**: 横断的 ee 比較に依拠するレビューは、測定手法別のデータ群を明示し、旧来の旋光度データについては現代のキラル HPLC との対比可能性をコメントする必要がある。また、系統的文献検索の方法論（データベース・検索語・収録基準）を報告する必要がある（B-2）。

* **EP**: EP-01a Reporting-coherence pack

* **Case-specific 実装**: （1）1985年以前に旋光度のみで ee が測定されている代表的反応系（Consiglio/Kumada Ni/DIOP 系, Figure 3）について、現代の chiral HPLC で ee を再測定しクロス検証を試みる。（2）レビューの ee データを測定年代別・分析手法別に層別化し、各グループの平均誤差範囲を推定する。

* **注記**: B-2 (convergence=1/3, medium), B-3 (high_convergence_low_gap, convergence=2/3, temperature_gap=none, V1=medium/V3=medium)。SRG-3 は D-4-4 の根拠 SRG。

---

**SRG-4 [Ni/Ir 光レドックス二重触媒サイクルの熱力学的・分光学的未検証]**

（SRG-2 の部分集合だが、触媒サイクル全体の自己一貫性という固有の問いを持つため独立記録する）

* **Primary RI**: RI-06 Imported model
  — Ni/Ir 二重触媒サイクル（SET → アルキルラジカル → NiIII → 還元的脱離 → NiI → IrII）は Tellis et al. (Science 2014) の初期 proof-of-concept から輸入されており、本レビューが取り上げる有機ボラン基質での SET の熱力学的実現可能性（オルガノボランの E_ox vs. *IrIII の E_red）が評価されていない。

* **Secondary RI**: RI-03 Unobserved explanatory
  — NiIII と IrII は機構の予言する常磁性中間体として原理的に観測可能だが、EPR・UV-vis のいずれの観測報告もない。

* **ER**: 二重触媒サイクルの提案には、（1）SET の熱力学的実現可能性（サイクリックボルタンメトリーまたは文献酸化還元電位による比較）と、（2）有機ボラン基質による *IrIII 励起状態の Stern-Volmer クエンチングが規範的に要求される。

* **EP**: EP-06a Analogy-validation pack ; EP-03a Direct-observation/state-assignment pack

* **Case-specific 実装**: Section 2.1.3 の反応系で、（1）有機ボラン基質の E_ox を CV で測定し、*Ir(dF(CF₃)ppy)₂(dtbpy)⁺ の E*III/II と比較して SET が発熱かどうかを確認する。（2）*IrIII 発光を有機ボランの添加量に対してモニターし、Stern-Volmer 定数 Ksv を決定する。（3）反応系に EPR プローブを加えた条件でラジカル中間体のシグナルを検出する。

* **注記**: B-6 (high_convergence_low_gap, convergence=3/3, temperature_gap=low), U-3 (low_convergence_high_gap, V2-Q10=high), A-4 (convergence=2/3, temperature_gap=low)。A-4 ↔ B-6 はピボット項目（D-4 priority_structure 参照）。

---

**SRG-5 [前向き主張における「未実現」「未発展」の根拠文書化不在]**

* **Primary RI**: RI-07 Unsupported boundary
  — "yet to be realized"（A-1, sec×sec カップリング）および "largely undeveloped"（A-3, tert-アルキル）という境界主張は、試みられたが失敗した例（負の結果）の系統的記録なしに提示されており、「文献が存在しない」のか「レビューが除外した」のかが区別できない（B-5）。

* **ER**: 「実現不可能」または「未発展」という境界主張には、（1）既存の試みとその失敗モード（低収率・低 ee・再現不能の根拠）の明示、または（2）探索が行われていないことの明示が必要である。

* **EP**: EP-07a Boundary-test pack

* **Case-specific 実装**: Section 6 の展望記述に対応して、(a) sec-電解質 × sec-求核剤 の組み合わせを試みた一次論文を系統的に参照し、失敗モードを収録する。(b) tert-アルキルハライドを試みた論文が報告する不活性条件（主にβ-H脱離の速さ）を表化する。

* **注記**: A-1 (convergence=1/3, medium), A-2 (convergence=1/3, medium), A-3 (convergence=1/3, medium), B-5 (convergence=1/3, medium)。D-4-6 および D-4-7（部分的）の根拠 SRG。

---

**SRG 外：CLA（Claim-level Adjunct）**

---

**CLA-1：「エナンチオ特異的」分類フレームの内的不整合**

（grounded_in: U-4, C-2 — いずれの SRG にも属さない）

* **Primary RI**: RI-05 Qualitative overread
  — "chirality exchange"（完全な立体化学伝達を含意する）という定義を二項ラベル（enantiospecific / non-enantiospecific）として適用しているが、Section 3 で報告される es 値は 65–99% に連続分布しており、定義と実データの乖離に対する定量的・機構的説明がない（U-4）。C-2（Crudden Rh 水素化ホウ素化）はこの乖離の具体例として、出発ボロン酸の ee と生成物の ee の独立測定なしに es が報告されているケースを示す。

* **ER**: 分類フレームが es < 100% を許容するなら、その許容根拠（どの es 値以上をエナンチオ特異的とするか）と、es 侵食の機構（基質のラセミ化・触媒による立体反転・副反応経路）の説明が必要である。

* **EP**: EP-05a Quantitative-ranking substantiation pack

* **Case-specific 実装**: Section 3 全体の反応系について、es 値を Kumada 型分類（es > 95%: 完全伝達、80–95%: 部分侵食、< 80%: 有意侵食）で層別化し、侵食が大きい反応系（例: Rh/基質 163, C-2 参照）では転化率複数点での ee 測定（出発材料と生成物を同一分析で）を行い、侵食がいつ・どこで生じるかを特定する。

* **注記**: CLA は D-1 の N-3（enantioselective/enantiospecific 分類体系）の内的一貫性に直結するため、CLA として記録。U-4 は TEMPERATURE_SUMMARY 対象外（単一エージェント由来、medium）。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method, Qualified)**

---

**VQ-1 Observation — 通過（Non-fatal 注記あり）**

本レビューが記述する化学的変換（反応基質、触媒、生成物構造）は一次論文の記述を通じて構造的に同定されており、RI-02（対象同定の粒度）は非致命的残存として通過する。ただし SRG-3/RI-01（測定法の異質性）は VQ-1 段階でも ee データの "観測" の信頼性に関わる Non-fatal な残存問題として記録する。

---

**VQ-2 Method — 通過（Qualified）**

VQ-1 の通過を前提とする。RI-01（SRG-3）は B-3 で局所的に認識されているものの系統的には未解消であり Non-fatal 残存。RI-07（SRG-5）は "yet to be realized" 等の境界主張に対して負の結果の文書化がなく Non-fatal 残存。両 RI は Non-fatal であり、レビューの主要な記述的機能（surveying what works）を根底から覆さないため、Qualified 通過とする。

「Qualified」の理由：RI-05 が CLA-1 を通じて残存している。U-4 に示された enantiospecific/non-enantiospecific の二項分類が es の連続分布に対応できていないことは、分類体系の方法論的精度の問題（RI-05）として VQ-2 Qualified に相当する。

---

**VQ-3 Mechanism — 未達**

VQ-2 Qualified 通過を前提とするが、以下の RI が致命的未解消として VQ-3 への昇格を阻む。

- **RI-06 (SRG-1, SRG-4): Fatal** — DYKAT（krac/kproductive 未測定）および SET（オルガノボランの E_ox と *IrIII の E_red 未比較）はいずれも対象系での同型性実証なしに輸入されたモデルであり、これらを機構的結論として採用するには VQ-3 が原理的に不成立である。

- **RI-03 (SRG-2, SRG-4): Fatal** — DET 固有の反応経路（U-1）、π-アリル Pd 中間体（B-7）、NiIII/IrII（U-3）はいずれも非観測の説明変数として機構の中核に置かれており、直接観測または速度論的拘束なしには機構的主張が成立しない。

- **RI-04 (SRG-2): Fatal（DET 割り当てに対して）** — DET vs. KR の識別に必要な転化率依存 ee プロファイルが存在せず、計算提案のみで分類が採用されている（U-1）。

RI-03, RI-04, RI-06 の三つが同時に Fatal で残存するため、VQ-3 は未達。

---

**VQ-4 Benchmark — 判定保留（VQ-3 未達のため）**

---

### §4 Era-Norm Annotation

**communication-era tolerated（2015年当時の Chemical Reviews レビュー論文として許容範囲）：**

- **B-3（ee 注意書きの局所適用）**: 2015年時点の化学系レビューでは、異なる研究条件下の ee 値を定量比較する際にも統一注意書きを要求する慣習がなく、Figure 5 キャプションの局所的免責事項は当時の genre convention 内で許容された。

- **B-2（系統的文献検索手順の不記載）**: PRISMA 型方法論の記述は医学系系統的レビューでは 2009年以降義務化されているが、化学系の narrative review では 2015年時点で標準化されておらず、省略は communication-era tolerated。

- **B-7（産物収束から π-アリル Pd を推定）**: 産物収束を π-アリル中間体の傍証として使用する論法は、有機金属化学の一次論文・レビュー双方で 2015年以前から standard practice であり、当時の分野規範内で許容された。

- **B-4（スコープ制限の機構帰属なし）**: Chemical Reviews での methodology scope limitations の報告において、制限の原因機構の提案は 2015年時点では任意であり省略は慣習として許容された。

---

**modern-era deficient（現代の再認定基準では許容不可）：**

- **B-1（DYKAT の krac/kproductive 未測定）**: 2020年代の不斉触媒機構論文では、DYKAT/KR/DKR の識別に転化率依存 ee データまたは速度論的測定を求めるレビューが増加しており、DYKAT を確立した機構として提示するには RI-06 と RI-03 の解消が modern-era では必要。当時は許容されたが現代基準では不足（両タグ対象）。

- **B-6 + U-3（光レドックス機構の酸化還元電位・分光データ不在）**: 2020年代の光レドックス触媒論文では、Stern-Volmer クエンチングデータと関連する酸化還元電位データが標準報告項目として定着しており、これらなしの機構提案は modern-era deficient。

- **B-2（系統的文献検索手順の不記載）**: Chemistry 分野でも 2020年代には PRISMA 準拠またはそれに類する記述が高インパクトジャーナルで推奨されるようになっており、modern-era では不足（両タグ対象）。

- **U-1（DET 仮説の転化率-ee 実験不在）**: 計算提案のみを根拠とした機構分類（DET）は、現代の計算・実験融合研究の文脈では、予言される実験シグネチャ（ee 転化率独立性）との対比が期待される。

---

### §5 最短補強ルート

**第一目的関数：VQ-2 (Qualified) → VQ-3 (Mechanism)**

解消が必要な RI: RI-03 (Fatal), RI-04 (Fatal), RI-06 (Fatal)

---

**VQ-3 への最短ルート：**

1. **EP-04a Discrimination/replication pack** — Section 4.1.1 の Cu/L32 系（Figure 64）で転化率 4 点（10%・30%・60%・90%）における ee を chiral HPLC で測定し、ee-転化率プロファイルを DET (平坦) vs. KR (単調増加) に分類する; 同時に Section 2.1.1 の Ni/DIOP 系で同様の転化率-ee プロファイルを取得して DYKAT vs. KR を判定する。**RI-03（DET 機構の観測）と RI-04（DET vs. KR 識別）を同一実験で同時前進させる最高情報利得アクション。**

2. **EP-06a Analogy-validation pack** — Section 2.1.1 の反応条件下での sec-ブチルマグネシウムブロミドの自己ラセミ化速度（krac）を旋光度または NMR で測定し、触媒 TOF と比較して krac/kproductive >> 1 が成立するかを実証する。**RI-06 (SRG-1) を前進させ、DYKAT の kinetic requirement を対象系で直接検証する。**

3. **EP-03a Direct-observation/state-assignment pack** — Section 2.1.3 の Ni/Ir 系で、（a）有機ボラン基質の CV 測定により E_ox を決定し *Ir(III) の E*III/II と比較、（b）*IrIII 発光の Stern-Volmer クエンチング定数を測定、（c）可能なら EPR でラジカル種を確認。**RI-06 (SRG-4) と RI-03 (SRG-4) を同時前進させ、SET 熱力学と中間体の存在を直接検証する。**

4. **EP-05a Quantitative-ranking substantiation pack** （CLA-1, Non-fatal 扱いだが VQ-3 Qualified 解消に貢献）— Section 3 の enantiospecific 反応を es 値で層別化し、es < 90% の反応系について転化率複数点での ee 測定を実施し侵食段階を特定する。**RI-05 残存を解消し、VQ-3 Qualified 条件を除去する。**

---

**第二目的関数：VQ-3 → VQ-4 (Benchmark)**（VQ-3 達成を前提）

必要な追加解消: RI-08 (Unquantified reliability), RI-09 (External superiority)

5. **EP-08a Replication/uncertainty pack** — ee 測定に系統誤差を評価するため、代表的反応 5 系統について異なる chiral HPLC カラムを用いた平行測定を実施し、測定法間の再現性と不確かさ範囲を記録する。RI-08 を前進させる。

6. **EP-09a Internal benchmark pack** — 配位子ファミリー（L1–L55 等）を横断する ee 値の比較に際して、同一の基質・条件で再測定した内部参照データセットを構築する。RI-09 (外部文献値のみでの優位性主張) を内部比較で置換する。RI-08 および RI-09 を前進させる。

---

**認定ゲート順注記：**
実験投入順は情報利得（EP-04a ≫ EP-06a > EP-03a > EP-05a > EP-08a ≥ EP-09a）だが、最終的な VQ 認定は継承原則に従い VQ-1 → VQ-2 → VQ-3 → VQ-4 のゲート順で確定する。EP-04a・EP-06a・EP-03a が揃って RI-03, RI-04, RI-06 を解消することが VQ-3 認定の前提となり、その後 EP-08a・EP-09a で VQ-4 を目指す流れとなる。

---

### §6 制度設計への寄与

**1. RI-06 (Imported model) の「Named Mechanism」亜型**

本ケースは RI-06 の新しい代表事例を提供する。DYKAT・DET は化学コミュニティ内で固有名詞化した機構フレームであり、それ自体が一種の権威として機能するため、「輸入元モデルの適用条件検証」が系統的に省略される傾向がある。これは「異なる化学系からのモデル輸入」という RI-06 の典型事例とは異なり、「同一化学領域内の確立された名前付きフレームの無検証適用」という亜型（RI-06b: Named-mechanism overclaim）として Codebook 注釈に追加することを検討する価値がある。独立 2 報での確認は単報モードでは判断できないが、PRI 候補として提案は保留する。

**2. SRG-4（光レドックス二重触媒サイクル）に対する PRI 候補の示唆**

SRG-4 のパターン（二重触媒サイクルの提案において、SET の熱力学的実現可能性の確認が体系的に省略される）は、2013–2020 年代の光レドックス触媒一次論文に繰り返し見られるパターンと構造的に一致する可能性がある。もし Stage 2F でこのパターンが cross-case confirmed されれば、PRI-11「Dual-catalysis SET claim without oxidation potential/spectroscopic validation」として昇格を検討できる。現時点では単報による示唆にとどまる。

**3. レビュー論文特有の「format-mediated RI-06」への注目**

本ケースで観察された「レビューが一次論文の機構的提案を批判なく承継することで、提案が確立した機構として流通する」という構造は、現行の RI コード体系では RI-06 に最も近いが、輸入元が "別の化学系" ではなく "同一化学系の一次論文" であるという特徴を持つ。VQ 判定において、これが "era-norm tolerated（review format では想定内）" と "modern-era deficient（mechanistic classification として不十分）" の両タグに該当するという§4 の記録は、将来の VQ 基準改訂時に「review paper モード」での致命性判定の基準化に貢献できる知見である。

**4. VQ-2 Qualified の境界条件事例**

RI-05 が CLA として VQ-2 段階で Qualified 判定をもたらしたケースとして記録する。es の連続分布に対して二項分類フレームを適用することが RI-05 に相当するという判定は、定性的分類体系を用いる実験データ解析全般に適用可能な境界条件の事例を提供する。

本ケースは既存の制度設計（RI-06 の Named Mechanism 亜型、SRG-4 に対する PRI 候補）に新しい具体例と将来改訂への示唆を追加した。

---

inference_time_sec: not available — inject externally
