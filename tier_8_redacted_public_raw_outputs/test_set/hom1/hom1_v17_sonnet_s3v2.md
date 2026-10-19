```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Wang et al. 2020（Chemical Science, Edge Article）

### §1 Claim Architecture

**コア主張の要約**

本論文は、Pd(II)/SOHPシステムによりインドールの酸化的Heck反応において世界初の配位子制御型C2選択的アルケニル化を実現したことを報告する。**Novelty柱**は二本立て：(1)「選択性決定段階のスイッチ」という機構概念——従来C3選択的であったC–H活性化ステップではなく、アルケン挿入ステップを選択性決定段階にすることでC2選択性を達成できるという設計原理——と、(2)その原理を体現するSOHPリガンド（κ²-S,N配位）の新規設計。**Utility柱**は、C2-アルケニル化インドール誘導体の合成手段の提供（Table 2の18+基質スコープ）と、「後続官能基化ステップも配位子設計対象」という化学界への指針。

**Layered structureの判定**

論文の主張は独立三層構造を成す（Stage 2 D-1 layered_structure: yes）：

- **Layer 1（合成的成果）**: Table 2のC2選択的スコープは実験的事実として独立して成立。機構層（Layer 3）が覆されても合成事実は残る。
- **Layer 2（配位子設計コンセプト）**: SOHPリガンドがC2選択性を誘起するという事実はLayer 1と同時に成立。設計概念は機構説明なしにも主張できる。
- **Layer 3（機構）**: 「挿入ステップスイッチ」はDFT+実験証拠の両方を必要とし、他の二層から独立に反証可能。DFTエネルギープロファイル（SRG-2）、準可逆性証拠（SRG-3）、KIE解釈（SRG-1）の複合的担保に依存する。

**層間依存関係**: Layer 3が否定されてもLayer 1, 2は残る。Layer 2はLayer 3の機構説明を援用しているが、C2選択性という事実（Layer 1）があれば配位子設計の有効性（Layer 2）は維持される。単一の反証でLayer 3は崩れ得るが、全体主張は崩れない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [KIE/kinetic data package]**（members: B-5, B-12）

* **Primary RI**: RI-04 Unreplicated discriminator — KIE = 3.48 ± 0.03という単一値（複製実験なし、個別速度値未報告）に速度決定段階の機構帰属が依拠；[acrylate]への速度依存性も反応次数を特定していない。
* **Secondary RI**: PRI-11 Mechanism-kinetics decoupling（暫定）— 触媒サイクルから速度式を代数的に導出せずに[acrylate]依存性のみで「挿入ステップが速度決定的」と帰属。RI-08 Unquantified reliability — KIEの個別速度値と誤差が未報告。
* **ER**: 速度決定段階の帰属には、(a)完全速度則（[Pd], [indole], [acrylate], [Cu], [O₂]への反応次数）の決定、(b)個別初速度値と測定誤差を含むKIEデータの報告、(c)DFT遷移状態振動数から計算した理論的KIEとの比較が必要。
* **EP**: EP-04a Discrimination / replication pack; EP-10a Kinetic verification pack（暫定）
* **Case-specific実装**: KIEを同一フラスコでの¹H/²H競争実験（n≥3）と独立した二つの初速度測定（n≥3）の両方で実施し、kH/kD比とEyring解析を報告；[Pd], [indole], [Cu(II)], [O₂]の全反応次数を初速度法で決定して速度式を代数的にDFTサイクルと照合する。
* **注記**: B-5はTEMPERATURE_SUMMARYでhigh_convergence_low_gap（convergence=3/3, gap=low; V1=medium, V2=medium, V3=high）。PRI-11昇格候補の3例目として記録（§6参照）。

---

**SRG-2 [DFT methodology quality]**（members: B-1, B-2, B-3, B-14）

* **Primary RI**: RI-06 Imported model — 実験的最適リガンドL17でなくL13を「代表」として用いたDFT計算結果を、L17/実験系の機構証拠として輸入；κ²-S,N配位部位の構造差（スルホキシド置換基）が与えるPES影響が無評価。
* **Secondary RI**: RI-04 Unreplicated discriminator — 系統的コンフォメーション探索なしの単一遷移状態（TS-1a/1b, TS-2a/2b）を確定PESとして提示（B-2）。RI-08 Unquantified reliability — 分散補正（D3BJ）欠如・熱力学補正レベル未明記・参照状態の触媒休止状態非対応（B-1, B-14）。
* **ER**: DFT計算が選択性決定の定量的根拠となるには、(a)実験最適リガンドL17でのPES再計算またはL13→L17の感度解析、(b)D3BJ分散補正の適用、(c)全TSの系統的コンフォメーション探索の記述、(d)熱力学補正レベルの明示と反応温度（343 K）への補正が必要。
* **EP**: EP-06a Analogy-validation pack（L13モデルの類推妥当性検証）; EP-04a Discrimination / replication pack（TS構造の局所/大域最小確認）
* **Case-specific実装**: L17を用いDFT/B3LYP-D3BJ/6-31G(d)/LANL2DZ(Pd)で全TS構造を再最適化し、SMD(DMF)/M06-D3BJ/6-311+G(d,p)単点エネルギーを計算；343 Kでの熱力学補正を適用；複数の配座異性体TSを比較しΔΔG‡の変動幅を感度解析として報告。
* **注記**: B-2はhigh_convergence_low_gap（convergence=2/3, gap=low; V2=high, V3=medium）。B-1, B-3はlow_convergence_high_gap（single-agent high; V2のみ）。SRG内の4項目が複合することでΔΔG‡ ≈ 5.9 kcal mol⁻¹という定量的主張の信頼性評価が不可能。

---

**SRG-3 [Quasi-reversibility mechanistic evidence]**（members: B-6, U-1）

* **Primary RI**: RI-05 Qualitative overread — 重水素取り込みの定性的時間経過パターン（Scheme 5右パネル）から「準可逆的C2-パラジウム化」という構造的・因果的含意を導出；定量的D%値・測定誤差・速度定数の抽出なし。
* **Secondary RI**: RI-03 Unobserved explanatory — 準可逆性の前進/逆反応速度定数は速度論的拘束なしに直接観測されていない；論文が予測する速度定数が自身のデータから検証されていない（U-1: self-contradictory absence）。
* **ER**: 準可逆的C2-パラジウム化の主張には、(a)複数の時点でのD%定量値（NMR積分誤差付き）をモデルに当てはめてkfwd, krevを算出、(b)「C2-Pd中間体がC3位でプロトン化される一方向経路」との速度論的区別が必要。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: Scheme 5右パネルの各時点のD%値をNMR定量（d₆-DMF基準またはMeSi内標準）し、可逆二段階反応モデル（IndH ⇌ IndD at C2; IndH ⇌ IndD at C3）に非線形最小二乗法で当てはめkfwd/krev/kquench（C3プロトン化定数）を算出；C3取り込みの独立経路（C2-Pd→C3プロトン化）をDO₃P添加（プロトン源置換）実験で定量的に評価。
* **注記**: B-6はTEMPERATURE_SUMMARYで最高収束項目（convergence=3/3, gap=none; V1=high, V2=high, V3=high）。RI-05とRI-03の共起パターン：定性的読み取り（RI-05）が未観測中間体の存在（RI-03）の証拠として使われており、一方のみの解消では不十分（§6参照）。

---

**SRG-4 [Table 2 scope data completeness]**（members: B-4, B-11）

* **Primary RI**: RI-01 Reporting integrity — Table 1では変換率・C3収率・C2収率・副生物収率・NMR収率を統一報告しているが、Table 2のC2-alkenylation条件では単離C2収率のみを報告；報告単位の不統一により横比較が不能（低収率entries 9, 10, 17が選択性不良か変換率不良かを区別不能）。
* **Secondary RI**: RI-08 Unquantified reliability — Table 1, 2のすべてのエントリが単一実験値；GC内標準・NMR定量プロトコル未記述；標準偏差なし。
* **ER**: 選択性制御の実証にはC2/C3比・変換率・質量収支の統一報告と、有意差評価のための誤差記述（少なくとも代表エントリのtriplicate）が必要。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: Table 2の全C2-alkenylation条件エントリ（特に低収率entry 9, 10, 17と高収率entry 1）について変換率（GC）・C3副生物収率（NMR）・質量収支を追記；triplicate実験のSDを付記。
* **注記**: B-4はhigh_convergence_low_gap（convergence=2/3, gap=low; V1=medium, V3=high）。SRG-4はLayer 1（合成的成果）の報告品質に直接影響し、VQ-2到達の主要実務的障壁。

---

**SRG-5 [Scope failure attribution and deferral]**（members: B-7, A-1, A-2）

* **Primary RI**: RI-07 Unsupported boundary — 4種の失敗例（アクリロニトリル22%、N-Ts-インドールC3不反応、5-OMe-6-CO₂Me-インドール、tryptophan/tryptophol誘導体24–39%）の機構的原因を「C2-パラジウム化困難」という独立証拠なしの帰属で説明；この帰属が誤り（実際は挿入ステップの困難）の場合、「挿入ステップスイッチ」という中心機構と矛盾する。
* **Secondary RI**: RI-03 Unobserved explanatory — 失敗基質でのDFT計算なし（本論文DFTはtBuアクリレートのみ）；失敗の原因となるステップが直接観測または速度論的拘束により同定されていない。
* **ER**: 基質スコープの機構的帰属には、当該基質での選択性決定ステップのDFT計算、または基質変更による速度論的プロファイルの変化の測定が必要。
* **EP**: EP-07a Boundary-test pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: アクリロニトリル（entry 17）についてtBuアクリレートと同じDFTプロトコルでC2-パラジウム化TSとC=C挿入TSのΔG‡を比較計算；N-Ts-インドール（entry 3）についてDMSOシステムでのC3選択性喪失を速度論実験（[acrylate]依存性）で原因帰属。
* **注記**: B-7はlow_convergence（V1のみ, convergence=1/3）。A-2は「ピボット項目」（Stage 2 D-4 priority_structure）：この帰属が誤りなら「挿入ステップスイッチ」（Layer 3）の普遍性が崩れる。

---

**SRG-6 [Catalytic cycle experimental grounding]**（members: B-10）

* **Primary RI**: RI-03 Unobserved explanatory — Cu(II)のHCl捕捉剤役割・β-H脱離選択性中立性・Pd(0)→Pd(II)再酸化の経路はすべてDFTのみに依拠し、実験的に観測も速度論的拘束もされていない。
* **Secondary RI**: RI-06 Imported model — Pd(0)再酸化はDFTサイクルに未組み込みであり（未計算）、他系の慣習から推定。
* **ER**: 触媒サイクルの各ステップが速度・選択性に影響しないという主張には対照実験による独立した検証が必要；Cu(II)役割の実験的証明はCu非存在下・非酸化性塩基置換実験で実行可能。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific実装**: Cu(II)をK₂CO₃（10 mol%）またはEt₃N（10 mol%）で置換したcontrol実験を実施し収率・C2/C3比をCu(II)条件と比較；Cu非存在下でのTON測定でPd(0)再酸化経路を評価。
* **注記**: B-10はhigh_convergence（convergence=2/3, gap=none; V1=medium, V2=medium）。Layer 3の機構サイクル完全性に関わる。

---

**SRG-7 [Anomalous observation unaddressed]**（members: B-13, U-3）

* **Primary RI**: RI-04 Unreplicated discriminator — Table 1 entry 1（配位子なし）でのC2生成物10%は単一実験値であり、GC測定誤差が記述されていないため「有意な10% C2」vs「測定ノイズ」の判別不能；DFT予測（ΔΔG‡ = 5.9 kcal mol⁻¹でC2は不利）と矛盾するデータ点が未説明（U-3: self-contradictory absence）。
* **Secondary RI**: RI-08 Unquantified reliability — GC内標準・応答係数・複製実験なし。
* **ER**: 「配位子なしでの固有C3選択性」という機構的ベースラインの確立には、entry 1のtriplicate実験とGC定量の測定誤差（±X%）の明示が必要；10%が誤差内ならDFT予測と整合、有意なら代替C2経路の検討が必要。
* **EP**: EP-08a Replication / uncertainty pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: Table 1 entry 1をtriplicate（n=3）で繰り返し、C2生成物収率の標準偏差を算出；10%がσ以内かどうかでDFT予測との整合性を評価し、有意な場合は微量C2経路の起源（例：DMSO不純物、微量配位種）を検討。
* **注記**: B-13はlow_convergence（V1のみ）；U-3はself-contradictory absence（DFTが予測しないデータ点）。SRG-7はLayer 3の「SOHPなしではC3固有」という前提の実験的根拠に関わる。

---

**SRG外：CLA**

**CLA: C2/C3選択性の速度論/熱力学制御論争**（grounded_in: U-2; 補助: B-5, B-6）

* **Primary RI**: RI-05 Qualitative overread — DFT遷移状態エネルギー・KIE・[acrylate]依存速度という速度論的証拠群から「C2選択性は速度論的制御による」と断言しているが、C2/C3-アルケニル化生成物の相対熱力学的安定性（ΔG°(C2) vs ΔG°(C3)）は論文のどこにも計算・測定されていない。
* **ER**: 速度論的制御の主張には、競合する熱力学的制御の排除——C2/C3-アルケニル化生成物の相対ΔG°の計算または高温加熱平衡化実験——が必要。
* **EP**: EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: 同一DFT水準でC2-アルケニル化インドール（3b型）とC3-アルケニル化インドール（3a型）の全エネルギー最適化を行いΔΔG°を算出；または高温条件（例120°C, 10 h, Pd触媒存在下）でC2:C3混合物を再処理し平衡比を測定。
* **注記**: U-2はどのSRGにも属さず独立CLA。「DFT計算が実験値と比較可能な量（ΔG°(生成物)）を予測するが比較が行われていない」という自己矛盾的不在のCLAチェック条件に合致。Layer 3の機構主張に直接関わる。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

**VQ-1 [Observation]** — **通る**（Non-fatal残存あり）
生成物の構造同定はNMRおよびHRMSにより確認されており、主要生成物3bはX線結晶構造（CCDC 1978349）、C2-挿入中間体4はX線構造（CCDC 1978351）で確認済み。RI-02（Object identification）は解消。Non-fatal項として、Table 2でのC3副生物の構造確認は報告外だが、主生成物の同定としては成立している。

**VQ-2 [Method]** — **未達**
VQ-1継承前提。VQ-2の必須要件はRI-01（Reporting integrity）とRI-07（Unsupported boundary）の解消。
- **RI-01**: SRG-4（B-4, B-11）で未解消。Table 2のC2-alkenylation条件で変換率・C3副生物収率・質量収支・誤差が報告されておらず、Table 1との報告単位の不統一が存在する。**致命性: Non-fatal（Layer 1の合成事実は失われないが、選択性の方法論的評価としては致命的）。**
- **RI-07**: SRG-5（B-7, A-1, A-2）で未解消。失敗基質の機構帰属（「C2-パラジウム化困難」）が独立証拠なしであり、スコープの限界が方法論的に確立されていない。**致命性: Non-fatal（VQ-2の「方法論的境界確立」要件に抵触するが全スコープを否定しない）。**

**ただし合成的成果層（Layer 1）単独では: VQ-2 (qualified)** — 18種以上の基質でのC2選択性の実証は方法論的に一定の水準に達しており、RI-01をNon-fatalとすれば基本的な方法論報告は満たされている。RI-05（SRG-3、準可逆性の定性的過読）が残存するため「qualified」。

**VQ-3 [Mechanism]** — **未達**
VQ-2継承前提。VQ-3の必須要件はRI-03, RI-04, RI-06の解消（RI-05が重大に残存する場合はqualified）。
- **RI-03**: SRG-3（B-6, U-1）とSRG-6（B-10）で未解消。準可逆性の速度定数が未測定（SRG-3）、Cu(II)の役割・Pd再酸化が実験未検証（SRG-6）。**致命性: Fatal（機構主張の根幹証拠が定量的根拠なし）。**
- **RI-04**: SRG-1（B-5, B-12）とSRG-7（B-13, U-3）で未解消。KIE=3.48の単一未複製値、entry 1の10% C2の有意性未確認。**致命性: Non-fatal（機構主張を根底から覆さないが定量的信頼性を損なう）。**
- **RI-06**: SRG-2（B-1〜B-3, B-14）で未解消。L13モデルの類推妥当性未検証、ΔΔG‡の定量的信頼性未担保。**致命性: Fatal（選択性決定ステップのスイッチという定量的主張の根拠が無効化される可能性）。**
- **RI-05**: CLA（U-2）とSRG-3で残存。
→ **VQ-3は未達（RI-03, RI-06が致命的；RI-05が残存するためRI-03解消後もqualifiedにとどまる可能性）。**

**機構層（Layer 3）単独では: VQ-1止まり** — 挿入ステップスイッチの機構的主張はRI-03（準可逆性未定量、Cu役割未検証）、RI-06（L13モデル輸入）、RI-05（定性的過読）の複合により観測レベルを超えていない。

**VQ-4 [Benchmark]** — **未達**
VQ-3継承前提。RI-08（SRG-1, SRG-4で未解消）、RI-09（C-1, C-2で先行ベンチマークとの数値比較なし）が未解消。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-11**（GC内標準・NMR定量プロトコル・誤差なし）: 2020年の合成化学論文では単一実験値の収率表が標準的な報告プラクティスであり、Chem. Sci. Edge Article形式でも誤差なし収率表は一般的だった。
- **B-1の一部**（熱力学補正レベル未明記・気相最適化）: 2020年時点でのDFT報告水準では、補正レベルの明示要求度は現在より低く、気相最適化+溶媒単点計算はStandard practiceとして許容されていた。
- **B-5の一部**（KIE比率のみ報告、個別速度値なし）: 動力学研究の不確かさ報告の要求水準は2020年の実験有機化学では現代より緩く、KIE比の報告のみは許容範囲とされていた。

**modern-era deficient:**

- **B-6**（準可逆性の定量データ欠如・速度論的モデリングなし）: 現代の機構論文では速度論的モデリングの結果（kfwd/krevまたは「導出不可能」の明示）が中心的機構主張の最低要件とされており、定性的時間経過プロットのみでは不十分。VQ-3到達に致命的。
- **B-1**（分散補正D3BJ欠如）: B3LYPへのD3BJ補正は2020年時点でも推奨ベストプラクティスとして確立されており（Grimme et al. 2010先行）、Pd/π系を含む計算では特に必要とされていた。現代では事実上必須。VQ-3到達に致命的。
- **B-2**（TS構造のコンフォメーション探索記述なし）: 現代のDFT機構論文では複数の配座異性体TSの比較が標準要件であり、単一TS構造の提示のみでは主張の定量的根拠として不十分とされる。
- **B-4**（Table 2変換率・副生物収率・C2/C3比未報告）: 現代の選択性制御論文ではC2/C3比と変換率の同時報告が位置選択性の実証として最低必要要件とされる。VQ-2到達に必要。

両タグ該当（当時は許容されたが現代では不足）: **B-11**（誤差なし収率表は当時は許容されたが、現代の再認定ではRI-08として記録される）。

---

### §5 最短補強ルート

**現在VQ-1 → 目的関数1: VQ-2；目的関数2: VQ-3（VQ-2前提）**

**VQ-2への最短ルート：**

1. **EP-01a** Reporting-coherence pack — Table 2の全C2-alkenylation条件エントリ（特に低収率entry 9, 10, 17）に変換率（GC）・C3副生物収率（NMR）・質量収支を追記し、Table 1との報告単位を統一する。**RI-01を解消。**
2. **EP-07a** Boundary-test pack — アクリロニトリル（entry 17）についてtBuアクリレートと同一DFTプロトコルでC2-パラジウム化TSとC=C挿入TSのΔG‡を比較し、失敗原因をパラジウム化ステップか挿入ステップかに帰属；N-Ts-インドール（entry 3）の失敗についてDMSOシステムでの速度論実験で原因確認。**RI-07を前進。**

認定ゲート順注記: Layer 1（合成的成果）のVQ-2 (qualified)はEP-01aのみで達成可能。全体としてのVQ-2はEP-01a + EP-07aが必要。最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4のゲート順で確定する。

---

**VQ-3への最短ルート（VQ-2到達後）：**

1. **EP-03a** Direct-observation / state-assignment pack（最優先・情報利得最大）— Scheme 5右パネルのD%時間経過データを各時点で定量化（NMR, n≥3, 誤差付き）し、可逆二段階速度論モデルに当てはめてkfwd(C2)/krev(C2)を算出；C3取り込みの独立経路（C2-Pd→C3プロトン化）をDO₃P添加実験で定量評価。同時にCu(II)をK₂CO₃で置換したcontrol実験でHCl捕捉役割を実験検証。**RI-03（SRG-3, SRG-6）を同時に前進。SRG-3のRI-03は致命的のため優先最高。**
2. **EP-06a** Analogy-validation pack — L17を用いたDFT再計算（D3BJ補正付き、TS構造系統的探索、343 K熱力学補正）でSRG-2の全4項目（B-1, B-2, B-3, B-14）を解消；ΔΔG‡の変動幅を感度解析として報告。**RI-06（SRG-2）を解消；RI-04（SRG-2）も同時前進。**
3. **EP-04a** Discrimination / replication pack — KIEをH/D競争実験（n≥3）と独立速度測定（n≥3）の両方で実施し個別速度値・誤差・計算値との比較を報告；[Pd], [indole], [Cu], [O₂]の反応次数を決定して速度式を代数的に触媒サイクルと照合。**RI-04（SRG-1）を解消；PRI-11の検証。**
4. **EP-08a** Replication / uncertainty pack — Table 1 entry 1をtriplicate実施してC2 10%の有意性を確認（SRG-7）；Table 2代表エントリのSD付き複製。**RI-08（SRG-7）を解消；RI-08（SRG-4）も前進。**
5. **EP-05a** Quantitative-ranking substantiation pack — 同一DFT水準でC2/C3-アルケニル化生成物のΔΔG°を算出（CLA解消）。**RI-05（CLA）を前進；VQ-3 (qualified)の「qualified」を解除。**

認定ゲート順注記: VQ-3認定にはRI-03（致命的）とRI-06（致命的）の両解消が前提。EP-03a + EP-06aがVQ-3到達の必須投入であり、EP-04a・EP-08a・EP-05aはRI-04・RI-08・RI-05を前進させVQ-3 (qualified)をVQ-3に昇格させる。投入順は情報利得の大きさ（EP-03a → EP-06a → EP-04a → EP-08a → EP-05a）を推奨する。

---

### §6 制度設計への寄与

**1. PRI-11（Mechanism-kinetics decoupling）昇格候補の3例目確認**

SRG-1（B-5, B-12）は、[acrylate]への速度依存性（Scheme 7）と「挿入ステップが速度決定的」という機構帰属の対応が速度式の代数的導出なしに行われるPRI-11の典型パターンを示す。「[acrylate]に正の依存性 → 挿入が速度決定的」という推論が、C–Hパラジウム化・アルケン配位・C=C挿入・HX脱離・Pd再酸化を含む多ステップサイクルの速度式を代数的に導出せずに成立させている。Breitenfeld 2014とPengfei 2024に続く3例目の独立確認として記録する。PRI-11の昇格に必要な「独立2報確認」はBreitenfeld/Pengfei 2例で満たされており、本ケースが追加確認となる。

**2. RI-05 + RI-03の共起パターン（SRG-3の構造）**

SRG-3では、定性的時間経過プロット（RI-05）から、直接観測されていない動的平衡状態（RI-03: quasi-reversible C2-palladation）の存在が推論されている。このRI-05 + RI-03の共起は「定性的パターン→未観測過程への因果的帰属」という認識論的飛躍の典型であり、RI-05の解消だけでは不十分（RI-03の解消にはkfwd/krevの測定が追加必要）。Codebook v0.2aの運用注記に「RI-05 + RI-03共起時の解消条件：両方の独立解消が必要」として追記することを提案する。

**3. RI-07「否定的境界主張」拡張適用の典型事例（SRG-5）**

SRG-5（B-7, A-2）は「C2-パラジウム化が困難」という否定的境界主張をデータなしに行うRI-07の拡張適用規則の明確な事例を提供する。この帰属が誤りの場合「挿入ステップスイッチ」の普遍性が反証されるという高リスク構造（Stage 2の「ピボット項目」）を持つ点は、否定的境界帰属の実践的危険性を示す典型事例として記録する。

**4. Layer構造とVQ水準の層別非対称性の鮮明な事例**

本論文の三層構造（Layer 1合成/Layer 2配位子/Layer 3機構）により、Layer 1はVQ-2 (qualified)、Layer 3はVQ-1止まりという鮮明な非対称性が存在する。「合成成果層が機構層よりも高いVQ水準に到達している」このパターンは、Novelty柱とUtility柱の独立性が高い概念実証論文で繰り返し現れる可能性があり、VQ判定の層別適用の有用性を示す好例として記録する。

**5. 新規PRI候補の不在**

本ケースで既存RIコードに収まらない新パターンは検出されなかった。SRG-3の準可逆性証拠問題はRI-05 + RI-03の共起（既存コード）で説明可能。本ケースは既存の制度設計を複数の観点から追加確認した。
```
