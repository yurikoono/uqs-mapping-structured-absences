# 判定確認シート（arm 伏せ、140 セル）

各行は 1 つの model 出力 × 1 軸。**判定**は判定者 2 名（Claude subagent、完全一致）または全文確認（Claude）の結果。
確認していただきたいのは「判定」の列が基準（`adjudication_rubric_20260929.md`）に照らして正しいかどうかです。違うと思う行に ✗ と理由を書いてください。
「不在」の行は、抽出された候補箇所の最初の 2 件を載せています（全候補は `adjudication_packets.json`）。

## homocoupling — homo-coupling の副生成物が未定量

| cell | 判定（狭義/広義） | 根拠または最も近い候補 | 確認 |
|---|---|---|---|
| C100364 | あり / あり | no yields or detection limits for homo-coupling products (R–R or R'–R') are reported for any entry | |
| C198292 | あり / あり | no glpc or NMR data confirm their absence in the new method | |
| C269685 | あり / あり | homo-coupling and disproportionation byproduct amounts are nowhere quantified | |
| C349650 | なし / あり | cited as giving homo-coupling and disproportionation products, but no comparative product distributions are shown | |
| C401244 | あり / あり | Homo-coupling products not quantified | |
| C457293 | あり / あり | no GC data or mass balance quantifying homo-coupling byproducts under the new conditions is reported | |
| C462894 | なし / なし | **Evidence needed:** Detection or quantification of β-hydride elimination by-products (alkenes, alkanes) under the reaction conditions; deuterium-labelling expe | |
| C509103 | あり / あり | No GC ratio of cross-coupling to homo-coupling product is reported for any entry | |
| C509126 | あり / あり | Homo-coupling byproduct not quantified — "selective" claimed without byproduct data | |
| C516652 | なし / あり | The origin of cross-coupling selectivity over homo-coupling is not explained | |
| C532298 | あり / あり | Evidence needed: Quantification of homo-coupling by-products (R–R and R′–R′) across the substrate range | |
| C590288 | あり / あり | the ratio of cross-coupling product to homo-coupling product R–R is not reported for any Table I entry | |
| C662677 | あり / あり | What quantities of homo-coupling and disproportionation products are formed under the new Ni-phosphine conditions? | |
| C667702 | あり / あり | The amounts of homo-coupled (R–R and R′–R′) and disproportionation products are nowhere quantified. | |
| C705476 | あり / あり | Are homo-coupling products absent from the Ni-diphosphine reactions, or merely unquantified? | |
| C847033 | あり / あり | Table I reports no homo-coupling product quantities and the "mass balance" is entirely absent | |
| C855313 | あり / あり | the paper does not show that homo-coupling is absent, does not quantify it | |
| C938611 | なし / なし | *Evidence needed:* Attempted reactions with representative primary, secondary, and tertiary alkyl chlorides/bromides under the same conditions; characterisation ／ *Evidence needed:* Side-by-side yield comparison in Et₂O vs. THF for the same substrate pair; analysis of side products (homo-coupling, reduction) in each solve | |
| C938890 | あり / あり | no byproduct quantification data are provided for the Ni system | |
| C970764 | あり / あり | What quantity of homo-coupling byproduct is present ... no mass fraction or GC ratio ... is reported | |

## black_precipitate — Example 1 の black mixture の正体

| cell | 判定（狭義/広義） | 根拠または最も近い候補 | 確認 |
|---|---|---|---|
| C009596 | なし / なし | The paper reports that only vinylic and aryl halides couple successfully, and calls this "one of the most remarkable features," but offers no mechanistic ration ／ **Evidence needed:** Attempted reactions with representative sp³ alkyl halides under identical conditions with quantification of products; rate measurements for | |
| C076838 | なし / なし | **Evidence needed:** Explicit experiments with representative alkyl halides (primary, secondary) under condition A and B to confirm inactivity; kinetic or elect | |
| C210790 | あり / あり | Is the active catalytic species the originally added [NiCl2(dpe)] complex or a decomposition product (Ni0, colloidal Ni) | |
| C247811 | あり / あり | the paper neither characterizes the black solid nor discusses whether it represents active catalyst, precatalyst activation product, or decomposition product | |
| C390170 | なし / あり | is the active Ni(0) species characterized under the actual [NiCl2(dpe)]-catalyzed conditions described in this paper? | |
| C455077 | あり / あり | Example 1の「黒い混合物と大量の塩」（V3-Q6）は触媒状態の変化を示唆するが、分析されていない。 | |
| C456416 | なし / なし | High yields with n-BuMgBr and n-C₈H₁₇MgCl are noteworthy because footnote 17 concedes that "[REDACTED: verbatim source text; see the source paper via its DOI] ／ *Evidence needed:* Mechanistic study of the oxidative addition of cis- and trans-1,2-dichloroethylene to Ni(0); trapping of the vinylnickel intermediate; crosso | |
| C481737 | なし / なし | （候補箇所なし・全文確認） | |
| C542931 | あり / あり | Black mixture during reaction not characterized ... paper neither characterizes the solid nor discusses catalyst fate. | |
| C570446 | あり / あり | The black coloration during reaction is noted but not addressed. | |
| C638115 | なし / なし | [B] B-8 \| p.4376, left col, feature (4) \| [REDACTED: verbatim source quotation; see the source paper via its DOI]L2NiR2 + R'X'' → L2Ni(R')(X'') + R-R" \| The paper's proposed catalytic cycle explicitly predicts homo-coupling product R-R  | |
| C664476 | なし / なし | **Evidence needed:** Attempted reactions with primary and secondary alkyl halides under both condition sets A and B with product analysis; oxidative-addition ex ／ **SRG-1: Uncharacterised catalytic intermediates** — Items 1, 6, and the implicit dependency in Item 13 share the same root: no direct observation of any Ni(II) | |
| C698771 | なし / なし | （候補箇所なし・全文確認） | |
| C726203 | あり / あり | The identity and role of the "black mixture" formed in Example 1 are not addressed | |
| C795497 | なし / なし | （候補箇所なし・全文確認） | |
| C844231 | あり / あり | What is the chemical identity of the black mixture and the precipitated salt? | |
| C858164 | あり / あり | What is the chemical identity of the "black mixture" and "much salt"? Is the catalyst recovered, decomposed, or converted | |
| C892650 | あり / あり | does the black material imply heterogeneous rather than homogeneous catalysis? | |
| C949963 | なし / なし | **(2)** Attempted reactions with alkyl halides paired with monitoring for β-hydride elimination products; comparison of oxidative-addition rates of Csp2 vs. Csp ／ **(2)** Side-by-side yield comparison of at least one representative reaction in Et₂O and THF under otherwise identical conditions; kinetic measurements to dete | |
| C959133 | なし / なし | （候補箇所なし・全文確認） | |

## exotherm_radical — Table I の発熱の脚注（広義: ラジカル経路の可能性）

| cell | 判定（狭義/広義） | 根拠または最も近い候補 | 確認 |
|---|---|---|---|
| C014890 | なし / あり | Radical vs. ionic pathway not distinguished — no mechanistic probes reported | |
| C046133 | なし / あり | would confirm whether selective cross-coupling ... is consistent with a bimetallic or radical chain mechanism | |
| C062696 | なし / なし | *(The entry "PhMgBr / Cl₂C=CH₂ / Ph₂C=CH₂ / 82" appears in Table I with footnote* f *"Reaction proceeded exothermally," the only remark made about this mechanis | |
| C131308 | なし / あり | 酸化状態が定義されていれば、ラジカル対イオン機構の区別...が可能となったはずである | |
| C152345 | なし / あり | labelling studies to confirm that the C–C bond formed is ... between the two organic groups already on nickel rather than a radical pathway | |
| C190387 | なし / なし | [U] U-2 \| loc: P3 (left col, feature 3)* \| quote: [REDACTED: verbatim source quotation; see the source paper via its DOI][REDACTED: verbatim source text; see the source paper via its DOI]"という記述がExample 1に一行あるが、黒色物質の化学的同定・in situ分光観察・活性種の同定に関する議論は存在しない。eqs 2– | |
| C326459 | なし / あり | distinguish radical, ionic, or η²-vinyl pathways that could account for stereochemical scrambling | |
| C429842 | あり / あり | The exothermic reaction (PhMgBr + Cl2C=CH2) is noted without reporting temperature-control measures or their effect on yield | |
| C466303 | なし / なし | Example 1 states that a black mixture forms on heating, which is consistent with Ni(0) colloid or catalyst decomposition, but the paper does not discuss catalys ／ key_quote: [REDACTED: verbatim source quotation; see the source paper via its DOI] | |
| C466925 | なし / なし | （候補箇所なし・全文確認） | |
| C547398 | なし / なし | The paper describes the anomalous outcome as a "feature" and suggests it may provide a route to cis-stilbene, but gives no explanation for why both geometric is | |
| C590287 | なし / なし | key_quote: [REDACTED: verbatim source quotation; see the source paper via its DOI] | |
| C628833 | なし / あり | Ni(0)/Ni(II) サイクルか Ni(I)/Ni(III) サイクルかの区別が可能になる（ラジカル経路の可能性） | |
| C731449 | あり / あり | "Reaction proceeded exothermally." \| question: What temperature control or safety parameters apply to the exothermal reactions? | |
| C771464 | なし / あり | Radical vs ionic pathway not probed ... No crossover experiment, radical clock substrate, or CIDNP data | |
| C775967 | なし / なし | （候補箇所なし・全文確認） | |
| C777480 | なし / あり | Is the cross-coupling proceeding by a radical mechanism (Ni(I)/Ni(III)) or an ionic mechanism? No radical clock | |
| C787421 | なし / あり | The proposed two-electron ionic mechanism and a radical/SET pathway are experimentally indistinguishable based on the data presented. | |
| C797990 | なし / なし | **Evidence needed:** Comparative mechanistic study establishing whether Fe operates via radical or organometallic pathways, versus the ionic two-electron pathwa | |
| C835067 | なし / なし | （候補箇所なし・全文確認） | |

## stereo_nonspec — 1,2-ジクロロエチレンの立体非特異性

| cell | 判定（狭義/広義） | 根拠または最も近い候補 | 確認 |
|---|---|---|---|
| C095234 | あり / あり | "Anomalously" signals the authors' awareness of a mechanistic tension; no explanation is offered | |
| C174967 | あり / あり | Anomalous cis-enrichment in stilbene synthesis is unaccounted for | |
| C193026 | あり / あり | cis/trans stilbene outcome described as "anomalous" without mechanistic explanation | |
| C196578 | あり / あり | なぜ異なる幾何配置のビニルハライドがいずれもcis-stilbene優先を与えるのか？ | |
| C204934 | あり / あり | Loss of stereospecificity with dichloroethylene substrates is flagged as anomalous but unexplained | |
| C304738 | あり / あり | cis/trans non-stereospecificity unexplained | |
| C309117 | あり / あり | What mechanism accounts for the anomalous cis enrichment from both geometric isomers of the starting material? | |
| C383765 | あり / あり | 「anomalous」と認識しながら機構に触れない | |
| C524814 | あり / あり | the paper offers no rationale for the loss of stereospecificity or the systematic cis-enrichment | |
| C526315 | あり / あり | The nonstereospecific outcome with 1,2-dichloroethylene is unexplained | |
| C541888 | あり / あり | What mechanism accounts for the anomalous cis-enrichment from both cis and trans precursors | |
| C605296 | あり / あり | なぜ cis 富化が起きるかについての説明は全く与えられていない | |
| C647684 | あり / あり | Anomalous stereochemical outcome ... is acknowledged without mechanistic explanation or kinetic/thermodynamic analysis. | |
| C814122 | あり / あり | What is the mechanistic basis for the anomalous cis enrichment, and how is this consistent with the proposed catalytic cycle | |
| C834046 | あり / あり | The anomalous cis enrichment in stilbene formation ... is left unexplained | |
| C843631 | あり / あり | The anomalous cis-enrichment in stilbene formation from both cis- and trans-1,2-dichloroethylene is unexplained | |
| C862615 | あり / あり | The anomalous cis-enrichment in the stilbene products ... is acknowledged but left without explanation | |
| C876433 | あり / あり | reported but left without mechanistic interpretation | |
| C922358 | あり / あり | The nonstereospecific stilbene result ... is reported as a fact but left mechanistically open | |
| C982830 | あり / あり | Non-stereospecificity of the reaction with 1,2-dichloroethylenes is unexplained | |

## ligand_ranking — 配位子の活性序列

| cell | 判定（狭義/広義） | 根拠または最も近い候補 | 確認 |
|---|---|---|---|
| C009384 | あり / あり | Within the bidentate ligand series the activity order (dpp > dpe > dmpe) is reported without rationalisation | |
| C058100 | あり / あり | Is the reported ligand activity order ... valid across other substrate combinations, or is it specific to n-BuMgBr/PhCl? | |
| C126713 | あり / あり | The cis-geometry claim is an inference from activity order alone | |
| C158499 | あり / あり | footnote 21 restricts its empirical basis to a single substrate pair | |
| C169548 | あり / あり | inferred from a ligand activity rank measured in a single substrate combination (n-BuMgBr + PhCl) | |
| C170200 | あり / あり | Ligand activity order attributed to cis geometry of complex 3 without structural evidence | |
| C212783 | あり / あり | Is cis-configuration the only factor? What is the role of chelate ring size ... or phosphine electronic properties? | |
| C264603 | あり / あり | The argument is purely structural and analogical ... whether cis-complex formation correlates with turnover are all unaddressed | |
| C266440 | あり / あり | supported by a single n-BuMgBr/PhCl measurement; generalizability to other Grignard/halide combinations is not demonstrated | |
| C392814 | あり / あり | 配位子活性順序の根拠不在——「シス配置要件」仮説の実験的未検証 | |
| C448470 | あり / あり | rests on a ligand-activity correlation, not structural proof | |
| C469687 | あり / あり | cis-Geometry hypothesis for ligand activity order is unsupported | |
| C478693 | あり / あり | The requirement for a cis-diorganonickel geometry is inferred from the ligand activity order but not mechanistically justified. | |
| C505764 | あり / あり | Ligand activity order and structural inference presented without tabulated supporting data. | |
| C558323 | あり / あり | The ligand activity order presented as a general feature (3) was determined from one substrate pair | |
| C611339 | あり / あり | The cis-configuration argument for ligand activity order is not demonstrated | |
| C657547 | あり / あり | The ligand activity order is presented without structural or kinetic derivation | |
| C697948 | あり / あり | Ligand activity order without tabulated data | |
| C832172 | あり / あり | The ligand activity order spans six catalysts but derives from a single substrate pair | |
| C849512 | あり / あり | Ligand activity order is stated without electronic or steric rationalisation | |

## glpc_standard — GLPC 収率の基準（内部標準・校正・単離収率との混在）

| cell | 判定（狭義/広義） | 根拠または最も近い候補 | 確認 |
|---|---|---|---|
| C022473 | あり / あり | The mixed basis prevents direct comparison across Table I entries. | |
| C137139 | なし / なし | （候補箇所なし・全文確認） | |
| C138030 | なし / なし | **Unsupported claim:** The title and introduction foreground selectivity over homo-coupling as the key advantage, but Table I reports only isolated (or internal ／ **Evidence needed:** Explicit mass-balance accounting for each reaction entry; glpc quantitation of all products including R–R′ along with homo-coupling byprodu | |
| C142558 | あり / あり | GC internal standard, column, temperature program, detector not stated | |
| C318715 | あり / あり | What internal standard was used for glpc analysis, and how were detector response factors calibrated | |
| C355133 | あり / あり | several yields are measured by GLPC rather than as isolated material | |
| C453760 | あり / あり | which internal standard was used, and were relative response factors calibrated against authentic samples | |
| C485520 | あり / あり | GC internal standard not named ... making the GC yield values unverifiable. | |
| C512498 | なし / なし | （候補箇所なし・全文確認） | |
| C603286 | なし / なし | High isolated yields are reported for couplings using n-BuMgBr and n-C₈H₁₇MgCl, reagents whose derived alkylnickel species would ordinarily undergo rapid β-hydr ／ The paper explicitly contrasts the new method with prior reactions "[REDACTED: verbatim source text; see the source paper via its DOI]  | |
| C621060 | なし / なし | （候補箇所なし・全文確認） | |
| C640816 | あり / あり | The yield column in Table I mixes isolated yields and glpc yields without specifying which metric applies to each entry. | |
| C649417 | あり / あり | internal standard identity are entirely absent ... no rationale for choosing isolated vs. GC yield per entry | |
| C666824 | あり / あり | Mixed yield-measurement bases ... without internal standard identity, response factor, or calibration curve | |
| C705277 | なし / なし | （候補箇所なし・全文確認） | |
| C728745 | なし / なし | （候補箇所なし・全文確認） | |
| C857161 | あり / あり | no entry provides both measures simultaneously; the internal GC standard is unnamed | |
| C943181 | なし / なし | **Evidence needed:** Mass-balance accounting for homo-coupled product (R–R and R′–R′) and disproportionation products alongside the cross-coupled product in rep | |
| C948842 | なし / なし | (1) The paper's central claim is *selective* cross-coupling, contrasting with prior methods that gave homo-coupling in "substantial amounts." However, no yields | |
| C967411 | あり / あり | no metadata (internal standard identity, calibration basis, response factor) is given for the GC entries | |

## ether_thf — ether が THF より優れるという断言

| cell | 判定（狭義/広義） | 根拠または最も近い候補 | 確認 |
|---|---|---|---|
| C018975 | あり / あり | The claim of "definite" solvent superiority is stated without comparative yield or rate data | |
| C071525 | あり / あり | No yield or conversion data comparing diethyl ether against THF is presented for any substrate | |
| C138802 | あり / あり | Diethyl ether superiority over THF asserted without data | |
| C150136 | あり / あり | The superiority of diethyl ether over THF is asserted without quantitative comparison | |
| C154160 | あり / あり | Ether superiority over THF not demonstrated ... No comparative yield data for THF | |
| C194883 | あり / あり | What comparative yield or selectivity data establishes that diethyl ether is "definitely superior"? | |
| C239255 | あり / あり | The superiority of diethyl ether over THF is asserted without comparative data | |
| C255693 | あり / あり | The superiority of diethyl ether over THF is asserted without a comparative experiment | |
| C315836 | あり / あり | the solvent effect is neither quantified (no yield comparison) nor rationalised mechanistically | |
| C317015 | あり / あり | Ether superiority over THF asserted without comparative data | |
| C330482 | あり / あり | No side-by-side yield comparison between Et2O and THF for any substrate is presented | |
| C437843 | あり / あり | no comparative yield data in THF vs ether appears in Table I or the text | |
| C443322 | あり / あり | Diethyl ether is reported to be "definitely superior" to THF but the basis ... is not addressed | |
| C460986 | あり / あり | "definitely superior" but no comparative yield data for the same substrate in ether vs THF appear | |
| C527118 | あり / あり | no comparative yield data are presented in the paper for the same reaction in both solvents | |
| C723162 | あり / あり | The claim that diethyl ether is definitively superior to tetrahydrofuran rests on no comparative data within this work | |
| C737945 | あり / あり | The preference is described as "definite" ... but no data are shown | |
| C745280 | あり / あり | Ether "definitely superior" to THF — no comparative data shown | |
| C853150 | あり / あり | What comparative yield or rate data supports "definitely superior"? No ether vs. THF comparison appears | |
| C951423 | あり / あり | "Definitely superior" asserted without comparative yield data in THF for any Table I substrate | |

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
