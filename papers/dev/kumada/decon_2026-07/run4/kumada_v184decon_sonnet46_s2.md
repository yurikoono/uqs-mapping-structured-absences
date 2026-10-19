```
prompt_version: stage2-v184-20260502
model_info: claude-sonnet-4-6
```

---

[D-1] declared_motivation

novelty_claims:
1. (T1) [REDACTED: verbatim source quotation; see the source paper via its DOI] — The paper explicitly claims novelty in the combination of selectivity (cross- over homo-coupling), Grignard reagent compatibility, and nickel-phosphine catalysis.

2. (T1) [REDACTED: verbatim source quotation; see the source paper via its DOI] — The novelty is framed against the known problem of selectivity failure in prior metal-halide-catalyzed coupling.

3. (T1) [REDACTED: verbatim source quotation; see the source paper via its DOI] — Compatibility with β-H-bearing Grignard reagents is presented as a distinct achievement relative to the known instability of transition-metal alkyls.

4. (T1) [REDACTED: verbatim source quotation; see the source paper via its DOI] — Use of aryl and vinyl chlorides (rather than bromides or iodides employed in prior work) is claimed as a distinctive feature.

5. (T1) [REDACTED: verbatim source quotation; see the source paper via its DOI] — Bidentate diphosphine ligands are presented as the key enabling element, with an activity ordering given as established fact.

success_criteria:
The paper invokes (T1) isolated yield and glpc yield as primary metrics for success; selectivity is implied by the absence of explicit homo-coupling product reports (not measured). Substrate breadth (alkyl, aryl, vinyl Grignard reagents; aryl and vinyl chlorides) and the accessibility of "hardly accessible" compounds (m-di-n-butylbenzene) are treated as success indicators (T1/T2).

layered_structure: yes — The claims are structured in four separable layers such that refutation of one does not collapse the others: (i) selectivity advantage over prior methods; (ii) β-H Grignard reagent compatibility; (iii) chloride reactivity; (iv) bidentate ligand requirement. A finding that β-H elimination occurs would not disprove the selectivity claim and vice versa. However, layers (i) and (iv) are interdependent: the ligand ordering is proposed to explain the selectivity mechanism, so refutation of the cis-configuration hypothesis (A-5) would weaken but not collapse the selectivity claim (layer i). [T2: paper-grounded inference]

---

[D-2] inferred_motivation

competitive_positioning: The paper explicitly positions itself against Tamura-Kochi's iron/copper/silver catalysts (refs 5-6) and against Corey-Semmelhack, Corey-Posner, and Whitesides stoichiometric reagents (refs 8-10). Both comparisons are asserted, not experimentally verified within this paper — no side-by-side yield or selectivity data are provided (C-1, C-2). The comparison to Tamura-Kochi is the more operationally direct positioning (both are catalytic), making the absence of comparative data for Et2O/THF, substrate overlap, or yield comparison (B-4) the most consequential gap in competitive positioning. [T2]

concurrent_submissions:
(a) The Note Added in Proof (footnote 3a) discloses a concurrent submission by Corriu and Masse (Chem. Commun., 144 (1972)) describing "similar cross-coupling reactions" using Ni(acac)₂. The paper draws no experimental or conceptual distinction between its system and the concurrent work; the Note merely acknowledges its existence. No scope comparison, substrate comparison, or mechanistic differentiation is provided.
(b) affects_novelty_claims: yes — the concurrent disclosure of similar Ni-catalyzed cross-coupling without comparative analysis means the paper's claim of a "new and useful preparative method" cannot be independently evaluated for novelty relative to the concurrent work from this paper's text alone. The absence of even a single distinguishing feature claimed relative to Corriu-Masse is a gap in competitive positioning (C-4, A-4). [T2]

timing_pressure: The short deferral list (A-1 through A-4 all to "investigations continuing") and the broad scope of claims relative to the narrow experimental base (two detailed examples, thirteen Table I entries, no mechanistic data) are consistent with accelerated submission ahead of the concurrent work. The Note Added in Proof establishes that the concurrent submission appeared after this paper's submission but before publication. A-1 (not optimum conditions), A-2 (mechanism deferred), and A-4 (extension deferred) all converge on this reading. However, the communication format itself makes extensive documentation structurally impossible — timing pressure and format convention cannot be independently distinguished from the paper's text. [T2: paper-grounded inference; not further elaborated to avoid T3 expansion]

format_exploitation: The JACS Communications format (≈2 full pages of results text) structurally prevents full reporting of optimization studies (B-1, B-4), ligand screening data (B-3), analytical characterization per entry (B-5, B-6), and mechanistic evidence (A-2). The choice to present thirteen substrate entries without comparative mechanistic controls or homo-coupling quantification leverages the format's brevity conventions. The acknowledgment that "conditions are not necessarily optimum" (A-1) is a format-appropriate hedge that compresses the absence of optimization data into a single footnote. [T2]

audience_targeting: The paper is directed at a preparative synthetic chemistry audience — the vocabulary emphasizes "new and useful preparative method," "readily accessible," "one step," "high yields," and names targeted compound classes (di-n-butylbenzene, vinylnaphthalene). The mechanistic content (eqs 2-4) is presented at the level of a working hypothesis rather than a kinetic or spectroscopic study, suggesting it is secondary to the synthetic utility demonstration. [T1]

institutional_visibility: [external inference] The concurrent Corriu-Masse submission and the attribution of priority via a Note Added in Proof suggest the Kumada group was aware of the competitive landscape in Ni-catalyzed cross-coupling in early 1972. [One sentence — not elaborated further.]

---

[D-3] institutional_motivation

journal_constraint: JACS Communications format (≤ 4 journal pages based on the 2-page target paper) structurally prohibits the reporting of: optimization tables (B-1, A-1), comparative solvent experiments (B-4), full ligand screening data with numbers (B-3), mechanistic probes (A-2), or mass balance data for β-hydride elimination (U-2). The result is that all B-items (reporting omissions) are consistent with being genre-enforced omissions rather than willful data suppression — the format cannot accommodate them. The paper's framing of several absences as footnotes or single-sentence statements ("not necessarily optimum," "further studies are required") is genre-appropriate for a communication.

field_competition_state: [external inference] Transition-metal-catalyzed C–C bond formation was an active frontier in 1972, with work from Corey, Kochi, and other groups occurring simultaneously; the concurrent Corriu-Masse submission confirms this. The field's state at the time favored stoichiometric organometallic methods (cuprate, allylnickel) over catalytic cross-coupling, so a demonstration of catalytic selectivity with a defined Ni complex represented a distinct advance in the type of reagent, even if the scope was incompletely characterized. [T3]

entry_criteria: The paper implies that to be taken seriously in 1972, a new cross-coupling method needed to demonstrate (a) high isolated yields with diverse substrates, (b) compatibility with the reactive sp2-chloride bond, and (c) a proposed mechanistic rationale — all of which the paper addresses, however incompletely. The implicit entry criterion for the claims it makes is selectivity over homo-coupling (the stated deficiency of prior art), but the paper does not measure homo-coupling product quantity, meaning the primary entry criterion is satisfied by negative space (homo-coupling not mentioned) rather than by positive demonstration. [T2]

holy_grail_narrative: no — The paper uses standard problem-solution framing ("new and useful preparative method," "promising reaction") without aspirational or quest language. No equivalent of "long-sought," "elusive goal," or "dream reaction" appears in the target paper's text.

commercialization_potential: (T1) [REDACTED: verbatim source quotation; see the source paper via its DOI] — The paper explicitly frames synthetic accessibility as a practical advantage. (T2) The emphasis on "high yields" with diverse Grignard reagents and "high reactivity of chlorides" (T1) implies industrial practical relevance given the cost advantage of chlorides over bromides/iodides, though this is not stated explicitly as a commercial argument. [T2: paper-grounded inference]

---

[D-4] 問われていない動機

D-4 候補数: 9（拡張上限適用、根拠: critical severity の U 項目が2件 [U-1, U-2]）

high_convergence_high_gap: none — フォールバック規則を適用。
フォールバック (a): low_convergence_high_gap = 空（単独エージェントの critical 評価は他エージェントの overlap に統合済み）。
フォールバック (b): high_convergence_low_gap の convergence=3/3 項目: B-1/U-1, U-2 を最優先。
フォールバック (c): SRG-1, SRG-2, SRG-3 が最多の A/B 項目を収束させる。

---

**D-4-1（最優先 — U-1 + B-1 + SRG-1）：自己の触媒サイクルが予測するホモカップリング生成物を、なぜ論文は定量しないのか**

この論文が問わずにいる問いは：「新法が主張する選択性（クロスカップリング優位）を、論文自身の触媒サイクルの予測と突き合わせて定量的に確認したか」である。

論文は eq. 3 において「L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R」と明示的に記述し、ジオルガノニッケル中間体 1 が有機ハライドと反応する際にホモカップリング生成物 R–R が放出されると予測している。すなわち論文自身の提案機構は、ホモカップリングがクロスカップリング生成の同一ステップで競合して生成することを要求する。しかし Table I のいかなるエントリーにおいても R–R の量は定量されておらず、全体的な質量収支も報告されていない。論文は先行法が「ホモカップリング生成物が相当量生成する」ために実用的でないと述べてから、自法ではその問題が解決したとほのめかすが、ホモカップリング量の測定値は提示されない。

この定量データが得られていれば、eq. 3 の選択性（クロスvsホモのモル比）が少なくとも一つのエントリーで確認され、提案機構の中核的主張が支持または否定できた。逆に言えば、現状の空白は「検出されなかった」ではなく「定量されなかった」であり、選択性の根拠は負の空間（ホモカップリングへの言及が存在しない）に依存している。

Stage 1 では B-1（reporting_omission、3/3 エージェント収束）と U-1（self-contradictory absence: eq.3 がホモカップリングを予測するにもかかわらずその定量がない）が同一の根拠の二側面として記録され、SRG-1 にまとめられている。温度メタデータ: convergence=3/3, temperature_gap=low（V1=high, V2=critical, V3=high）。

grounded_in: U-1, B-1
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: high_convergence_low_gap（fallback (b) で最優先; convergence=3/3）
same_root_group: SRG-1

---

**D-4-2（最優先 — U-2 + B-8 + C-5 + SRG-3）：β水素を持つアルキルグリニャール試薬が高収率を与えると主張しながら、なぜβヒドリド脱離を測定しないのか**

この論文が問わずにいる問いは：「触媒サイクルが不可避的に形成するアルキル-Ni(II) 中間体は、なぜβヒドリド脱離を起こさないのか」である。

論文は [REDACTED: verbatim source quotation; see the source paper via its DOI] と主張し、n-BuMgBr および n-C₅H₁₁MgCl で高収率を示す。同時に脚注 17 で「遷移金属アルキル錯体でβ水素を持つものは通常不安定である」と記してその参照文献を引用する。提案触媒サイクルでは eq. 2 と eq. 4 において n-Bu–Ni(II) 等のアルキルニッケル中間体（1 および 3）が必然的に形成される。こうした中間体は 1972 年時点で β-ヒドリド脱離の典型例として知られていたが、論文は 1-ブテン等のアルケン副生成物の GC 検出を行っておらず、その検出下限や検出の試みさえ記述していない。

もし β-ヒドリド脱離が起きている場合、「高収率」という表現は未測定の β-ヒドリド脱離ロスを無視しており、実際の触媒効率の記述として不完全になる。一方、β-ヒドリド脱離が本当に抑制されているなら、その抑制機構（dpe の立体・電子効果による金属側の制約、反応速度の速さによるトラッピング、等）の説明は提案触媒サイクルの重要な補強であり、現在の「今後の研究が必要」という処理で問われないままになっている。

Stage 1 では B-8（reporting_omission for scope claim）、U-2（self-contradictory absence）、C-5（β-ヒドリド不安定性文献の引用後放棄）が SRG-3 に収束している。B-8 ↔ U-2 のリンクは、報告漏れ（B）と自己矛盾的不在（U）の補完的性格を示す。温度メタデータ: convergence=3/3（V1, V2, V3 すべてが独立に指摘）、temperature_gap=low（V1=high, V2=critical, V3=high）。

grounded_in: U-2, B-8, C-5
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: high_convergence_low_gap（fallback (b)、convergence=3/3）
same_root_group: SRG-3

---

**D-4-3（SRG-2 + A-2 + A-3 + C-3）：「作業仮説」として提示された触媒サイクルの、どの elementary step に実験的根拠があるか**

この論文が問わずにいる問いは：「提案する Ni 触媒サイクル（eqs 2–4）の各素反応ステップは個別に確認されているか、それとも全体が単一の類推から組み立てられた作業仮説にすぎないか」である。

論文は eq. 1 として Uchino ら（ref 11）および Miller ら（ref 12）の化学量論的 Ni 反応（ジアルキル-dipy-Ni + PhCl → PhCl 0.5 + Et-Et）を引用し、それを自らの触媒サイクルの一素反応の類推証拠として使う。しかしそれ以外の素反応（Grignard 試薬との反応による中間体 1 の生成、eq. 2; 有機ハライドによる 1 から 2 への変換、eq. 3; Grignard による 2 から 3 の生成と 3 からのクロスカップリング生成物放出、eq. 4）については、速度データ、中間体の分光観測、同位体実験、ラジカルトラップ実験のいずれも存在しない。論文自身が "apart from the working hypothesis" と明記している。

この問いが答えられていれば、提案サイクルが Ni(0)/Ni(II) 経路か Ni(II)/Ni(IV) 経路かの区別、ラジカル連鎖経路との区別、律速段階の同定、そして立体化学上の「異常な cis エンリッチ」（A-3）の機構的起源が解明できた可能性がある。特に、eq. 1 に使われた dipy-Ni（bipyridyl 配位子）の反応を dpe-Ni 系に外挿することの妥当性（C-3）も問われていない。

Stage 1 の A-2（機構を作業仮説として外置き）、A-3（cis エンリッチを説明不能として外置き）、C-3（素反応類推文献の非検証引用）が SRG-2 に収束する。

grounded_in: A-2, A-3, C-3
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: high_convergence_low_gap（A-2: convergence=2/3, temperature_gap=none; A-3: convergence=2/3, temperature_gap=low）
same_root_group: SRG-2

---

**D-4-4（U-3 + B-9）：反応混合物が「黒くなる」という観察は、活性触媒の同一性について何を意味するか**

この論文が問わずにいる問いは：「Example 1 で生成した黒色混合物の正体は何であり、それが [NiCl₂(dpe)] が終始活性触媒として機能しているという主張と整合するか」である。

論文は Example 1 の手順の中で [REDACTED: verbatim source quotation; see the source paper via its DOI] と記す。ニッケル触媒反応における黒色沈殿は、金属 Ni(0) 粒子またはコロイド状 Ni への還元を示す典型的な観察であり、均一系 [NiCl₂(dpe)] 触媒が不均一系 Ni 種に変換されている可能性を示唆する。均一系触媒と不均一系 Ni では、提案されている eqs 2–4 の触媒サイクル（配位子配位に依存する分子論的なサイクル）の適用可能性が根本的に異なる。

論文はこの観察を手順記述の中で淡々と述べるだけで、(a) 黒色種の分光分析、(b) 黒色種の触媒活性試験（ろ過後の上清でも反応が進むか）、(c) 黒色物質の回収量や同定、を行っていない。もし活性触媒が不均一系 Ni であれば、配位子 dpe の役割は触媒前駆体からの Ni(0) の発生を制御することに限定され、「bidentate diphosphine が著しい触媒活性を示す」という主張の解釈が変わる。

Stage 1 では B-9（手順観察の reporting_omission）と U-3（self-contradictory absence: 活性触媒の同一性主張を揺るがす観察の非解析）がリンクされている。U-3 は high severity の独立 U 項目として記録されており、D-4-1/D-4-2 への吸収を行わない（v18.1 C11 保護）。

grounded_in: U-3, B-9
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: V3 単独 (high severity); 他エージェントの個別 overlap なし
same_root_group: none（B-9 と U-3 の 2 項目のみのリンク）

---

**D-4-5（B-2 + A-2）：sp² ハライドのみが使えるという制限の、機構的または電子的根拠は何か**

この論文が問わずにいる問いは：「なぜ sp² 炭素-ハロゲン結合（ビニル・アリール）は反応するのに、sp³ アルキルハライドは使えないのか、そしてこの境界を決める化学的要因は何か」である。

論文は [REDACTED: verbatim source quotation; see the source paper via its DOI] と明記し、これを"最も注目すべき特徴の一つ"と肯定的にフレームする。しかしアルキルハライドで試みた実験は全く報告されておらず、sp³ ハライドを使うと何が起きるか（反応しない、ホモカップリングが起きる、触媒が失活する等）も言及されない。提案機構では eq. 1 の酸化的付加ステップが sp² C–Cl 結合に特有のものであるとも読めるが、論文はこれを明示しない。

sp³ ハライドとの失敗実験データ（または試みの不在の理由）があれば、sp² 選択性が基質の酸化的付加速度（π 活性化による加速）によるのか、それとも Ni(II) 中間体と sp³ ハライドの反応性の低さによるのかという機構的区別が可能だった。現在の記述は「制限事項」を「特徴」として再フレームしており（B-2 の mixed classification）、その制限の化学的根拠は問われていない。

grounded_in: B-2, A-2
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: V1 単独 (medium)
same_root_group: none

---

**D-4-6（A-3 + B-11 + SRG-4）：cis エンリッチという「異常」は、ラジカル機構の証拠として解析されたか**

この論文が問わずにいる問いは：「cis-および trans-ClCH=CHCl がともに cis エンリッチのスチルベン混合物を与えるという立体化学的「異常」は、提案する Ni(II) 協奏機構と矛盾するか、それともラジカル中間体の証拠として解析できるか」である。

立体特異的 syn 付加または anti 付加が維持される協奏的メカニズム（Ni(0)による酸化的付加 + 還元的脱離）では、幾何異性体が明確な立体化学的相関を持つはずである。しかし論文が示すように、cis-基質は 80:20 を、trans-基質は 43:57 の cis:trans スチルベン比を与え、両者ともに cis 異性体を優先または含み、単純な立体保持も反転も成立しない。論文自身が "anomalously enriched" という表現を用いてこれが予想外であることを認識している。

ラジカルメカニズム（Ni が一電子プロセスを経由する場合）では、ビニルラジカル中間体がアルケン幾何を急速に異性化し、cis エンリッチが独立した熱力学的分布から来るという説明が可能である。しかし論文はラジカルトラップ実験、ESR、またはクロスオーバー実験を行っておらず、「さらなる研究が必要」と外置きする（A-3）。B-11 は同エントリーにおけるホモカップリング生成物（PhPh）の非定量を記録している。

立体化学的「異常」とホモカップリング定量の不在（SRG-4）は同一エントリーで重なっており、この二つのデータ空白が合わさってラジカル機構の可能性を問われていない問いとして残している。

grounded_in: A-3, B-11
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: high_convergence_low_gap（A-3: convergence=2/3, temperature_gap=low）
same_root_group: SRG-4

---

**D-4-7（SRG-6 + B-3 + A-5）：配位子活性順序という「構造-活性相関」の、設計指針への変換可能性**

この論文が問わずにいる問いは：「提示された配位子活性順序は、どの配位子パラメータ（噛み合い角、リン供与性、立体障害）を最適化すれば次の触媒が設計できるかという設計原理を与えるか」である。

論文は [NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] ≈ [NiCl₂(PPh₃)₂] ≫ [NiCl₂(PEt₃)₂] ≈ [NiCl₂(PPh₂Me)₂] という順序を一箇所の脚注で「観察された」と述べ（脚注 21: n-BuMgBr と PhCl の反応で測定）、[REDACTED: verbatim source quotation; see the source paper via its DOI] という解釈を提示する。しかし (a) この順序の定量的根拠（各複合体の収率または反応速度）が示されない（B-3）、(b) dpp/dpe/dmpe は噛み合い角・電子性・立体障害の三変数を同時に変化させているため、どの変数が活性を決めるかが切り分けられない、(c) A-5 の cis 配置仮説は仮説のレベルに留まっており、中間体 3 の配位構造観測に基づいていない。

この問いが答えられていれば、「次に試すべき配位子」を予測する構造-活性相関の基礎が得られ、反応の拡張・精製を加速する触媒設計指針となる。現状では活性順序は観察的事実として提示されるだけで、それを design rule に変換する機構的根拠が欠けている。

grounded_in: B-3, A-5
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: high_convergence_low_gap（B-3: convergence=2/3, temperature_gap=none）
same_root_group: SRG-6

---

**D-4-8（B-4 + B-12 + C-1）：ジエチルエーテル優位性とクロライド反応性という二つの「特徴」の、定量的根拠の不在**

この論文が問わずにいる問いは：「Et₂O が THF より『明らかに優れている』という溶媒選択と、塩化物が臭化物・ヨウ化物より反応しやすいという主張は、本論文の実験データによって実証されているか」である。

論文は [REDACTED: verbatim source quotation; see the source paper via its DOI] と断言しながら（B-4）、Table I の全エントリーは Et₂O（または Et₂O/PhH/THF 混合）条件下でのみ実施され、THF 単独での比較データは示されていない。同様に、臭化物やヨウ化物を使った場合の結果は [REDACTED: verbatim source quotation; see the source paper via its DOI] と先行文献状況のみ述べるだけで（B-12）、同一 Ni-dpe 条件でのクロライドvsブロミドの比較実験は行われていない。Tamura-Kochi 触媒との溶媒比較も数値なしに「対照的に」と述べるのみ（C-1）。

「塩化物の高い反応性」と「Et₂O の優位性」という二つの特徴主張は、論文内のデータに基づかない asserted comparisons であり、両者をまとめた競合的ポジショニングの数値的裏付けが完全に欠けている。これらを確認する比較実験が示されていれば、実用的なプロトコルへの外挿（実用条件での溶媒・ハライド選択）がより堅固になる。

grounded_in: B-4, B-12, C-1
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: 各 B 項目 V1 単独 (medium)
same_root_group: none

---

**D-4-9（A-4 + C-4 + B-2）：同時代の競合研究（Corriu-Masse）との接点と、本系が提供する固有の価値**

この論文が問わずにいる問いは：「Corriu-Masse（1972 年同期提出）の Ni(acac)₂ 触媒系と比較して、本論文の Ni-ジホスフィン系は何を追加するのか」である。

論文は Note Added in Proof で Corriu-Masse の "similar cross-coupling reactions" を認識しながら（C-4）、(a) 基質カバレッジの重複範囲、(b) 収率の比較、(c) 配位子（dpe vs acac）の違いがもたらす実用的・機構的な差異、について一切言及しない。A-4（「今後の研究が継続している」）と B-2（sp² 制限を正の特徴として再フレーム）の組み合わせは、本系の固有価値の定義を開かれたまま置く構造を形成している。

もし両系の比較がなされていれば、リン配位子の役割（チュータビリティ / 回収可能性 / 特定基質への適合）という付加価値が明確になり、単に「同時に達成された」という状況から「何が異なる問いに答えているか」という構造的差別化が可能になった。現在の Note は競合的文脈を開示するが、それを競合的分析に変換しない。

grounded_in: A-4, C-4, B-2
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: V2 のみ (medium)
same_root_group: none

---

questions_that_cannot_be_asked:

QNC-1 [grounded_in: none (retrospective)]: 論文の送稿判断（1972年2月15日受理）に Corriu-Masse の類似研究の存在についての著者の事前知識がどの程度あったかは、論文テキストからは原理的に判断できない。

QNC-2 [grounded_in: none (retrospective)]: 京都大学 dpe 配位子合成の研究室内最適化試行回数や、なぜ dpe が代表例として選ばれたかの詳細な実験的選択理由（著者の知識背景・偶発的発見経緯）は、テキストから復元できない。

---

priority_structure:

この論文全体を横断して読むと、「触媒的選択性の実証（主張）」を成立させるために「選択性の機構的根拠の定量（説明）」が意図的ではなくとも体系的に後回しにされた、という構造として読むことができる。

具体的には：

ピボット 1: A-2 ↔ B-1（ピボット）
—— 触媒機構は "working hypothesis" として外置き（A-2）されているが、その同じ機構（eq. 3）が定量されていないホモカップリング（B-1）を予測している。A-2 が B-1 の説明を引き受けることを回避することで、B-1 の空白が維持される。

ピボット 2: A-2 ↔ U-2（ピボット）
—— 同様に、機構の外置き（A-2）は、β-ヒドリド脱離の不在という反直感的主張（U-2）を未解決のまま置く。「今後の研究が必要」という一文が B-8 の scope 主張の空白を事実上覆う。

ピボット 3: B-3 ↔ A-5（ピボット）
—— 配位子活性順序（B-3、数値なし）が cis 配置仮説（A-5）を支持する唯一の根拠として機能しているが、B-3 の定量が欠けているため A-5 は仮説のまま残る。

SRG-1（B-1 + U-1）はこの構造の中核をなしており、論文の主張（選択性の達成）と実験記録（ホモカップリングの非測定）の間の最大の緊張点として機能している。

---

[E] 射程の問い

この論文が化学の文脈で答えた問いを抽象化すると：

「あるクラスの金属錯体触媒が、複数の競合反応経路のうち特定の経路のみを選択的に促進できるかどうかを、基質スコープと収率で実証する」

derived_from: D-4-1, D-4-3, U-1, A-2
anchoring_note: この抽象化は T2（paper-grounded inference）— 論文が示す実証パターン（基質スコープ表 + 収率）から一ステップの推論で到達できるが、"selectivity" という概念の抽象化は論文テキストの明示的言語ではない。

この形式が別の文脈でどのような問いに変形されるか：

1. **酵素触媒の選択性実証（最も直接的な類似）**: ある酵素変異体が、野生型が生成する複数の副生成物のうち一つの生成経路のみを選択的に閉じているかどうかを、産物プロファイルで実証する。構造の同じ現れ——競合経路の選択的排除を産物スコープで示す。

2. **機械学習モデルの選択的分類**: ある分類器が、複数の誤分類パターンのうち特定の型のみを抑制できるかどうかを、ベンチマークデータセットへの適用で実証する。比喩的な類似——「選択性」と「基質スコープ」は「精度」と「テストセット」に対応するが、機構的記述は非類似。

3. **政策介入の標的効果実証**: ある政策手段が、複数の社会的アウトカムのうち特定のアウトカムのみを変化させ、他を変化させないことを、パイロットデータで実証する。比喩的な類似——「選択性」が「特異的効果」に対応。

4. **情報フィルタリングシステムの特異性**: あるフィルタアルゴリズムが、類似するノイズ信号群のうち特定の型のみをブロックし、他を通過させることをサンプルセットで示す。比喩的な類似。

最も射程が広い変形として (3) または (4) のような非化学領域への変形を選ぶ理由：D-4-1 が浮き彫りにしているように、この論文の核心的な問われない問いは「競合経路の抑制を、その競合経路が生成するはずの副生成物を定量せずに主張できるか」という認識論的問いである。この問いは化学的文脈に固有ではなく、「ある機構が予測する帰結を測定することなしに、その機構による選択性を主張できるか」という一般的な科学的論証の問題に対応する。

最も化学的文脈に忠実な変形（1 の酵素催媒）を選んだ上で、一方で化学内での射程（他の触媒系への問い形式の転用）として確定する。

```confirmed_english
confirmed_english_propositional: "Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides."
confirmed_english_question: "Can nickel-phosphine complexes selectively catalyze the cross-coupling of Grignard reagents with vinyl or aryl halides?"
scope_type: "tool_question"
```

inference_time_sec: not available — inject externally

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
