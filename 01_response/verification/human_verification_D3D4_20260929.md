# 人による確認のお願い — D3/D4（2026-09-29）

> **Note (2026-10-19).** This is the request sheet of 2026-09-29 with the author's marks (☑️) and notes added on 2026-10-05, as reported in SI-6.10 and SI-11.20. The sentences of the request below that say no human has checked the items yet were written before the check.

著者に確認していただきたい項目を、ここに全部まとめました。確認が済んだ項目の結果を、Methods 6 と SI-11.20 に「著者が確認した」と書きます（それまで SI-11.20 には TODO 印が残っています）。

**確認の仕方**: 各行の「確認」欄に ✓（判定に同意）か ✗（同意しない、理由を一言）を書いてください。所要時間の目安は A が 20 分、B が 60–90 分、C が 10 分、D が 20–30 分、E が 30–40 分です（E は同じ箇所を判定者 A・B が重ねて挙げている行が多いので、同じ箇所は 1 回見れば足ります）。B は軸ごとに独立しているので、途中までの確認でも使えます。

（2026-10-05 復元: 9/29 の commit 762128d で E 部を足したときに A〜D 部を誤って上書きしていました。A〜D は 19f8216 の版から戻し、内容は変えていません。）

判定したのはすべて Claude（判定者 2 名の subagent、および私）です。人はまだ誰も確認していません。

---

## A. 原典を正確に伝えていない引用（10 件）

原典の頁と、原典の記述を並べました。PDF で該当箇所を見て、「原典を正確に伝えていない」という判定に同意できるかを確認してください。判断が分かれるもの（語の追加や、図中の式の転記での欠落）は「境界」としています。

| # | 由来 | 出力の記述 | 原典（頁） | 判定 | 確認 |
|---|---|---|---|---|---|
| A1 | D3 wu2026（CCS Chem.）S1 C-1 と S2 key_quote | [REDACTED: verbatim source quotation; see the source paper via its DOI] | p. 2 右段: [REDACTED: verbatim source quotation; see the source paper via its DOI] | 誤り（語の置換） | ☑️ |
| A2 | D3 wang2026（J. Org. Chem.）S2 D-3 | nitrogen heterocycles described as found in "anti-cancer agents, pesticide research, and functional materials" | 序論の第 1 段落: [REDACTED: verbatim source quotation; see the source paper via its DOI]（"anticancer" は ref. 1 の題名にのみ） | 誤り（語の置換） | ☑️ |
| A3 | D3 liu2026（Org. Lett.）S2 D-4 候補 4 | "The paper assigns the ring-forming step as a 'concerted [4+2] electrocyclization'" | 本文・SI とも "[4+2] electrocyclization" のみ。"concerted" は出てこない | 誤り（限定語の追加。D-4 の論証がこれに依拠） | ☑️ |
| A4 | D3 wang2026 S1 GAP-2 | "merely four esterification derivatives" | 序論: "…offering merely four derivatives." | 境界（引用符内の語の追加） | ☑️ |
| A5 | D4 UQS repro run5（Kumada 1972）S1 V2-Q2 | "the following processes may be involved"（Kumada の触媒サイクルとして引用） | p. 4374 左段 = 直前の hydrosilylation の報（Kiso ら）の文。Kumada の報には無い | 誤り（隣接の報からの引用） | ☑️ |
| A6 | D4 UQS repro run1 S1 V2-Q7 | "L₂Ni(X″) + RMgX′ → [L₂Ni(R)(R′)] + MgX′X″"（eq 4） | p. 4375 eq 4 は図: L₂Ni(X″)(R′) + RMgX′ → L₂Ni(R)(R′) + MgX′X″ | 境界（図の式の転記で R′ が欠落） | ☑️ |
| A7 | D4 B2 run1 | "[NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] << [NiCl₂(PPh₃)₂]" | p. 4376 左段: "[NiCl₂(dmpe)] ≈ [NiCl₂(PPh₃)₂] ≫ [NiCl₂(PEt₃)₂] ≈ …" | 誤り（関係の逆転） | ☑️ |
| A8 | D4 B2 run2 | "n-C₈H₁₇MgCl / CH₂=CHCl / Condition B / n-C₈H₁₇CH=CH₂ / 95%. Reaction proceeded exothermally." | p. 4375 Table I: この行の注は e（glpc 収率）。注 f（発熱）は PhMgBr の行の CH₂=CHCl、ClCH=CHCl、Cl₂C=CH₂ に付く | 誤り（脚注の付け違い） | ☑️ |
| A9 | D4 B2 run5 | "n-C₆H₁₃MgCl / CH₂=CHCl / B / n-C₈H₁₇CH=CH₂ / 95" | p. 4375 Table I: n-C₈H₁₇MgCl | 誤り（試薬の読み違い） | ☑️ |
| A10 | D4 B2 run4 | "(dipy)Ni + PhCl → (dipy)Ni · 0.5PhCl + Et–Et"（eq 1） | p. 4375 eq 1 は図: (dipy)NiEt₂ + PhCl → (dipy)Ni(Ph)(Cl)·0.5PhCl + Et–Et | 境界（図の式の転記で配位子が欠落） | ☑️ |

PDF: `papers/paperA_heldout_R1/{wang2026,liu2026,wu2026}/*.pdf`、`papers/dev/kumada/Kumada_1972.pdf`。出力: 同フォルダの `*_v184_sonnet46_s*.md`、`papers/dev/kumada/repro_2026-07/`、`papers/dev/kumada/baseline_R1_2026-09/`。

**あわせて**: 誤りでないと判定した残り（D3 は 50 行中 46 行、`d3_heldout/d3_quote_adjudication.md`。D4 は `d4_baseline/d4_quote_adjudication.md`）に、見逃した誤りが無いかを拾い読みしていただけると助かります（任意）。

---

## B. benchmark 所見の判定（4 軸 × 25 セル = 100 行、arm を伏せています）

判定基準の全文は `d4_baseline/adjudication_rubric_20260929.md`。「あり」= 出力がその点を未解決の問い・欠落・未裏付けの主張として挙げていること（論文の記述の言い直しだけでは「なし」）。一部だけ当てはまる場合は「なし」。
各行は 1 つの出力（pipeline・baseline のどれかは伏せてあります）。「判定」は判定者 2 名の一致した結果です（狭義 / 広義）。「あり」の行には決め手の箇所、「なし」の行には抽出された候補箇所の最初の 2 件を載せています（全候補は `adjudication_v2_packets.json`）。

**特に見ていただきたい点**: 「なし」の行に、実は所見を述べているものが紛れていないか。前回の独立査読（Fable）は、発熱の脚注を引いて問題にしているのに「なし」とされたセルを指摘しています（下の表で ★ を付けた行）。

### homocoupling — homo-coupling の副生成物が定量・報告されていない（選択性が中心の主張なのに）

| cell | 判定（狭義 / 広義） | 根拠、または候補箇所 | 確認 |
|---|---|---|---|
| C047036 | あり / あり | no yields or detection limits for homo-coupling products (R–R or R'–R') are reported for any entry in Table I | ☑️ |
| C195572 | あり / あり | Homo-coupling byproduct not quantified — "selective" claimed without byproduct data | ☑️ |
| C273847 | あり / あり | The amounts of homo-coupled (R–R and R′–R′) and disproportionation products are nowhere quantified. | ☑️ |
| ★ C278040 | なし / あり | Head-to-head experiment of the new catalyst vs. an iron or copper catalyst on the same substrate, reporting yields of cross-, homo-, and disproportionation products. | ☑️ |
| C281982 | あり / あり | Are homo-coupling products absent from the Ni-diphosphine reactions, or merely unquantified? | ☑️ |
| C287714 | あり / あり | Table I reports no homo-coupling product quantities and the "mass balance" is entirely absent for all entries | ☑️ |
| C290414 | あり / あり | selective cross-coupling rests on the implied absence of homo-coupling products, but no glpc or NMR data confirm their absence | ☑️ |
| C301479 | あり / あり | Homo-coupling product yields are never quantified; the claim of "selectivity" cannot be independently assessed | ☑️ |
| C311008 | あり / あり | Homo coupling and disproportionation by-products are not quantified in Table I | ☑️ |
| C405809 | あり / あり | no byproduct quantification data are provided for the Ni system | ☑️ |
| C413573 | あり / あり | "Selective" cross-coupling is the central claim, but homo-coupling and disproportionation byproduct amounts are nowhere quantified | ☑️ |
| C456848 | あり / あり | the ratio of cross-coupling product to homo-coupling product R–R is not reported for any Table I entry | ☑️ |
| C466320 | あり / あり | the paper does not show that homo-coupling is absent, does not quantify it, and does not explain why the Ni-diphosphine system suppresses it | ☑️ |
| C485266 | あり / あり | The central selectivity claim is not supported by any quantitative data on homo-coupling byproducts R–R or R′–R′ for any Table I entry. | ☑️ |
| C489619 | なし / なし | *Evidence needed:* Attempted reactions with representative primary, secondary, and tertiary alkyl chlorides/bromides under the same conditions; charac ／ *Evidence needed:* Side-by-side yield comparison in Et₂O vs. THF for the same substrate pair; analysis of side products (homo-coupling, reduction) in  | ☑️ |
| C558840 | あり / あり | no mass fraction or GC ratio of homo-coupling to cross-coupling product is reported for any entry in Table I | ☑️ |
| C665468 | なし / なし | **Evidence needed:** Detection or quantification of β-hydride elimination by-products (alkenes, alkanes) under the reaction conditions; deuterium-labe | ☑️ |
| C670925 | あり / あり | no GC data or mass balance quantifying homo-coupling byproducts under the new conditions is reported for any Table I entry | ☑️ |
| C730479 | あり / あり | What quantities of homo-coupling and disproportionation products are formed under the new Ni-phosphine conditions? | ☑️ |
| C769759 | あり / あり | Selectivity against homo/disproportionation products is claimed as a distinguishing feature but not quantified. | ☑️ |
| C780101 | あり / あり | The amounts of homo-coupling and disproportionation byproducts are never quantified | ☑️ |
| C828011 | あり / あり | No GC ratio of cross-coupling to homo-coupling product is reported for any entry | ☑️ |
| C852136 | あり / あり | The amount of homo-coupling product formed in the cross-coupling reaction is never quantified | ☑️ |
| C861811 | あり / あり | Quantification of homo-coupling by-products (R–R and R′–R′) across the substrate range | ☑️ |
| C941125 | なし / あり | The paper does not identify which step in the catalytic cycle prevents homo-coupling | ☑️ |

### black_precipitate — Example 1 の black mixture の正体・役割を問う（広義: 前駆体から生じる Ni⁰ を未同定の化学種として問う）

| cell | 判定（狭義 / 広義） | 根拠、または候補箇所 | 確認 |
|---|---|---|---|
| C023254 | なし / なし | The paper reports that only vinylic and aryl halides couple successfully, and calls this "one of the most remarkable features," but offers no mechanis ／ **Evidence needed:** Attempted reactions with representative sp³ alkyl halides under identical conditions with quantification of products; rate measur | ☑️ |
| C041814 | あり / あり | The formation of a black reaction mixture suggests possible catalyst decomposition, which is not addressed | ☑️ |
| C042145 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C048184 | なし / なし | **(2)** Attempted reactions with alkyl halides paired with monitoring for β-hydride elimination products; comparison of oxidative-addition rates of Cs ／ **(2)** Side-by-side yield comparison of at least one representative reaction in Et₂O and THF under otherwise identical conditions; kinetic measuremen | ☑️ |
| C048312 | なし / なし | **Evidence needed:** Explicit experiments with representative alkyl halides (primary, secondary) under condition A and B to confirm inactivity; kineti | ☑️ |
| C069999 | あり / あり | Identity of "black mixture" in Example 1 not characterized | ☑️ |
| C077375 | なし / なし | [B] B-8 ／ p.4376, left col, feature (4) ／ "[REDACTED: verbatim source text; see the source paper via its DOI]  ／ [U] U-1 ／ p.4375, right col, eq 3 ／ "L2NiR2 + R'X'' → L2Ni(R')(X'') + R-R" ／ The paper's proposed catalytic cycle explicitly predicts homo-coupling pr | ☑️ |
| C153127 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C174642 | あり / あり | The nature of the "black mixture" is uncharacterised | ☑️ |
| C200382 | あり / あり | Nature of the "black mixture" during Example 1 is uncharacterized | ☑️ |
| C278489 | なし / なし | High yields with n-BuMgBr and n-C₈H₁₇MgCl are noteworthy because footnote 17 concedes that "[REDACTED: verbatim source text; see the source paper via its DOI] ／ *Evidence needed:* Mechanistic study of the oxidative addition of cis- and trans-1,2-dichloroethylene to Ni(0); trapping of the vinylnickel intermedia | ☑️ |
| C351167 | あり / あり | The identity and nature of the "black mixture" formed during reaction is unreported | ☑️ |
| C366163 | あり / あり | What is the chemical identity of the black mixture and the precipitated salt? | ☑️ |
| C402504 | なし / なし | **Evidence needed:** Attempted reactions with primary and secondary alkyl halides under both condition sets A and B with product analysis; oxidative-a ／ **SRG-1: Uncharacterised catalytic intermediates** — Items 1, 6, and the implicit dependency in Item 13 share the same root: no direct observation of  | ☑️ |
| C425182 | あり / あり | Black mixture during reaction not characterized. | ☑️ |
| C526335 | あり / あり | the paper neither characterizes the black solid nor discusses whether it represents active catalyst, precatalyst activation product, or decomposition product | ☑️ |
| C723286 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C784582 | あり / あり | The identity and role of the "black mixture" formed in Example 1 are not addressed | ☑️ |
| C788273 | なし / あり | is the active Ni(0) species characterized under the actual [NiCl2(dpe)]-catalyzed conditions described in this paper? | ☑️ |
| C810433 | あり / あり | The appearance of a "black mixture" in Example 1 hints at possible catalyst decomposition or reduction, but this is left unaddressed. | ☑️ |
| C878997 | あり / あり | Is the active catalytic species the originally added [NiCl₂(dpe)] complex or a decomposition product (Ni⁰, colloidal Ni) | ☑️ |
| C883626 | あり / あり | Exmaple 1の「黒い混合物と大量の塩」（V3-Q6）は触媒状態の変化を示唆するが、分析されていない。 | ☑️ |
| C911180 | あり / あり | The black coloration during reaction is noted but not addressed. | ☑️ |
| C964958 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C979641 | あり / あり | What is the chemical identity of the "black mixture" and "much salt"? Is the catalyst recovered, decomposed, or converted to a different Ni species? | ☑️ |

### exotherm_radical — Table I の発熱の脚注を挙げ、その意味を問う（広義: ラジカル経路の可能性を未検証の代替として挙げる）

| cell | 判定（狭義 / 広義） | 根拠、または候補箇所 | 確認 |
|---|---|---|---|
| C036858 | あり / あり | The exothermic reaction (PhMgBr + Cl2C=CH2) is noted without reporting temperature-control measures or their effect on yield and reproducibility. | ☑️ |
| C052265 | なし / あり | to distinguish radical, ionic, or η²-vinyl pathways that could account for stereochemical scrambling and the cis enrichment | ☑️ |
| C067718 | なし / あり | 中間体が確認されていた場合、(i) Ni(0)/Ni(II)対Ni(II)/Ni(IV)サイクルの区別、(ii) ラジカル対イオン機構の区別 | ☑️ |
| C080384 | あり / あり | What temperature control or safety parameters apply to the exothermal reactions ... No thermal monitoring data is provided. | ☑️ |
| C143155 | なし / あり | Radical vs. ionic pathway not distinguished — no mechanistic probes reported | ☑️ |
| C225304 | なし / なし | key_quote: [REDACTED: verbatim source quotation; see the source paper via its DOI] | ☑️ |
| C254868 | なし / あり | labelling studies to confirm that the C–C bond formed is specifically between the two organic groups already on nickel rather than a radical pathway | ☑️ |
| C359622 | あり / あり | The exothermic character may indicate a faster, potentially less selective process, or heat management issues at scale. | ☑️ |
| C366418 | なし / あり | Is the cross-coupling proceeding by a radical mechanism (Ni(I)/Ni(III)) or an ionic mechanism (Ni(0)/Ni(II) two-electron)? No radical clock, crossover experiment, or isotope effect is reported. | ☑️ |
| C395515 | なし / なし | **Evidence needed:** Comparative mechanistic study establishing whether Fe operates via radical or organometallic pathways, versus the ionic two-elect | ☑️ |
| C483564 | なし / なし | [U] U-2 ／ loc: P3 (left col, feature 3)* ／ quote: [REDACTED: verbatim source quotation; see the source paper via its DOI][REDACTED: verbatim source text; see the source paper via its DOI]"という記述がExample 1に一行あるが、黒色物質の化学的同定・in situ分光観察・活性種の同定に関する議論は存在 | ☑️ |
| C517237 | なし / なし | The paper describes the anomalous outcome as a "feature" and suggests it may provide a route to cis-stilbene, but gives no explanation for why both ge | ☑️ |
| C521500 | あり / あり | The exothermal reaction of vinylidene chloride (Cl₂C=CH₂) is noted without characterisation of selectivity or safety implications | ☑️ |
| C536799 | なし / なし | Example 1 states that a black mixture forms on heating, which is consistent with Ni(0) colloid or catalyst decomposition, but the paper does not discu ／ key_quote: [REDACTED: verbatim source quotation; see the source paper via its DOI] | ☑️ 注: black mixture は還流前から黒（Example 1）。この軸（発熱）の判定には影響しない |
| C635359 | なし / あり | No radical clock, crossover experiment, CIDNP, isotope labeling, or Hammett correlation is reported. The proposed two-electron ionic mechanism and a radical/SET pathway are experimentally indistinguishable | ☑️ |
| C648929 | あり / あり | whether the exotherm drives the reaction through a different temperature regime and thus affects product distribution is not considered | ☑️ |
| C661165 | なし / あり | Radical vs ionic pathway not probed. | ☑️ |
| C698802 | あり / あり | The exothermic nature of the reaction with vinyl chloride (footnote f) is noted without safety or scale-up discussion | ☑️ |
| C735287 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C747482 | なし / あり | Ni(0)/Ni(II) サイクルか Ni(I)/Ni(III) サイクルかの区別が可能になる（ラジカル経路の可能性） | ☑️ |
| C768172 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C780863 | なし / あり | would confirm whether selective cross-coupling requires both organic groups on the same metal center ... or is consistent with a bimetallic or radical chain mechanism | ☑️ |
| C910142 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C914170 | あり / あり | The "reaction proceeded exothermally" note for Cl₂C=CH₂ is not examined as a safety or mechanistic indicator | ☑️ |
| ★ C989632 | なし / なし | *(The entry "PhMgBr / Cl₂C=CH₂ / Ph₂C=CH₂ / 82" appears in Table I with footnote* f *"Reaction proceeded exothermally," the only remark made about thi | ☑️ |

### glpc_standard — GLPC 収率の基準（内部標準・校正・方法、単離収率との混在）を問う

| cell | 判定（狭義 / 広義） | 根拠、または候補箇所 | 確認 |
|---|---|---|---|
| C013754 | あり / あり | The yield column in Table I mixes isolated yields and glpc yields without specifying which metric applies to each entry. | ☑️ 注: 決め手の文は誤り（脚注 d/e で行ごとに区別でき、出力自身も引用している）。基準は事実の正しさを問わないため判定は維持（SI-11.20） |
| C036105 | あり / あり | The mixed basis prevents direct comparison across Table I entries. | ☑️ |
| C094832 | なし / なし | **Unsupported claim:** The title and introduction foreground selectivity over homo-coupling as the key advantage, but Table I reports only isolated (o ／ **Evidence needed:** Explicit mass-balance accounting for each reaction entry; glpc quantitation of all products including R–R′ along with homo-coupli | ☑️ |
| C105430 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C139509 | なし / なし | **Evidence needed:** Mass-balance accounting for homo-coupled product (R–R and R′–R′) and disproportionation products alongside the cross-coupled prod | ☑️ |
| C172476 | なし / なし | **(2)** GC or NMR quantification of homocoupling products (e.g., biphenyl in Ph/PhCl reactions, or dibutylbiphenyl) alongside the cross-coupling yield ／ ### Item 27 — The claim of "high yields" for all conditions is contradicted by the 76% isolated yield entry (n-BuMgBr/PhCl) without discussion **[U]** | ☑️ |
| C185976 | なし / なし | **(1) Question.** A central motivation for the paper is that prior Grignard cross-coupling methods produce "homo coupling products and a variety of di ／ **(2) Evidence needed.** Quantitative GC analysis reporting yields of all coupling products (R–R', R–R, R'–R') relative to both starting partners; mea | ☑️ |
| C335396 | あり / あり | GC column type, stationary phase, temperature program, detector type, and internal standard identity are entirely absent | ☑️ |
| C343129 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C357369 | あり / あり | The criteria for choosing glpc vs. isolated yields are not stated | ☑️ |
| C410842 | あり / あり | At least five entries use glpc yield and seven use isolated yield, but these are measured differently and the choice of method is not explained | ☑️ 注: 「GLPC 少なくとも 5 件」は誤り（4 件: 98, 95, 95, 89%）。判定は維持（SI-11.20） |
| C436543 | あり / あり | which internal standard was used, and were relative response factors calibrated against authentic samples | ☑️ |
| C450671 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C530266 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C600888 | なし / なし | High isolated yields are reported for couplings using n-BuMgBr and n-C₈H₁₇MgCl, reagents whose derived alkylnickel species would ordinarily undergo ra ／ The paper explicitly contrasts the new method with prior reactions "[REDACTED: verbatim source text; see the source paper via its DOI] | ☑️ |
| C647655 | あり / あり | GC internal standard, column, temperature program, detector not stated | ☑️    |
| C675149 | あり / あり | no entry provides both measures simultaneously; the internal GC standard is unnamed | ☑️ |
| C698542 | なし / なし | (1) The paper's central claim is *selective* cross-coupling, contrasting with prior methods that gave homo-coupling in "substantial amounts." However, | ☑️ |
| C707305 | あり / あり | no metadata (internal standard identity, calibration basis, response factor) is given for the GC entries — are GC and isolated yields directly comparable? | ☑️ |
| C707603 | あり / あり | GC internal standard not named. ... The identity and calibration of the internal standard are not stated | ☑️ |
| C786577 | なし / なし | （候補なし。全文は packet の fulltext） | ☑️ |
| C865859 | あり / あり | The paper reports only internal standard-based glpc yields for some entries, without isolated yield validation | ☑️ |
| C882216 | あり / あり | several yields are measured by GLPC rather than as isolated material ... Evidence needed: ... isolated yields for all entries | ☑️ |
| C967057 | あり / あり | What internal standard was used for glpc analysis, and how were detector response factors calibrated | ☑️ |
| C980690 | あり / あり | Mixed yield-measurement bases within Table I (isolated vs. GC-internal-standard) without internal standard identity, response factor, or calibration curve | ☑️ |

（残りの 3 軸——立体非特異性、配位子の序列、ether と THF——は全 arm・全 run で「あり」で、判定者も一致しています。確認は任意です。）

---

## C. D3 で「anchor なし」とした Evidence Pack（7 ブロック）

事前登録の基準は「各 EP が、要求する証拠の class と、本文への anchor（key_quote か節の参照）を持つこと」。次のブロックは、論文の数値や内容には触れているが、引用も場所（頁・表・図・Scheme・SI・節）の参照も持たないため「anchor なし」と判定しました。この読み方で良いかを確認してください。

| # | 論文 | ブロック | 確認 |
|---|---|---|---|
| C1 | wang2026 | **SRG-1** (A-2, B-2, U-2): Mechanistic evidence for the ionic pathway relies on acknowledged-as-indirect negative contro | ☑️ |
| C2 | wang2026 | **SRG-4** (B-6): Diastereomeric ratios (1.2–1.5:1) for secondary and tertiary alcohol products are reported without spec | ☑️ |
| C3 | liu2026 | **SRG-1 [Mechanistic elementary steps unsupported]** (B-5, B-6, U-1, U-2, U-3) | ☑️ |
| C4 | liu2026 | **SRG-4 [Stereochemical outcome reporting incomplete]** (B-3, B-4) | ☑️ |
| C5 | shekarizadeh2026 | **SRG-5 [Particle size characterization methodology]** (B-4, B-5) | ☑️ |
| C6 | shekarizadeh2026 | **SRG-7 [N-Pd coordination characterization gap]** (B-13, U-2) | ☑️ |
| C7 | shekarizadeh2026 | **CLA-1 [EDS vs AAS Pd content discrepancy]** (B-6) | ☑️ |

各ブロックの全文は `papers/paperA_heldout_R1/{論文}/{論文}_v184_sonnet46_s3v2_en.md` の §2。

---

## D. SRG の根の対応づけ（46 ブロック、2026-09-29 追加）

Results Part 4 の「4 モデルが同じ 6 つの SRG に一致」を一次出力から数え直した結果です（SI-6.10）。各ブロックが Sonnet の記録の 6 つの根（R1 触媒サイクル / R2 副生成物 / R3 収率の分析 / R4 範囲限定 / R5 溶媒・条件 / R6 cis/trans；定義は `srg_root_mapping/rubric_srg_root_mapping.md`）のどれを中心の欠落として扱っているかを、判定者 2 名（LLM）が判定しました（44/46 で一致）。ここはモデル名を伏せずに並べています（確認の都合上）。

| 出力 | ブロックの見出し | 判定（A / B） | 確認 |
|---|---|---|---|
| sonnet46_2026-04 | SRG-1 [Mechanistic cycle without experimental evidence in dpe-Ni system] | R1 / R1 | ☑️ |
| sonnet46_2026-04 | SRG-2 [Selectivity claim without byproduct data] | R2 / R2 | ☑️ |
| sonnet46_2026-04 | SRG-3 [Analytical quality of Table I yield data] | R3 / R3 | ☑️ |
| sonnet46_2026-04 | SRG-4 [Scope restriction basis] | R4 / R4 | ☑️ |
| sonnet46_2026-04 | SRG-5 [Solvent and condition effects without quantitative basis] | R5 / R5 | ☑️ |
| sonnet46_2026-04 | SRG-6 [Cis/trans selectivity observation] | R6 / R6 | ☑️ |
| sonnet46_2026-04 | CLA-1: 配位子活性序列からcis-geometry仮説 + Corriu/Masse問題（D4-8対応） | none: ligand activity order / cis-geometry requirement; Corriu-Masse Ni(acac)2 comparison / none: ligand ranking → cis-geometry + Corriu–Masse Ni(acac)₂ comparison ⚠ 不一致 | ☑️ |
| haiku45_2026-04 | SRG-1 [機構サイクルの検証不在] (U1, U2, U3由来) | R1 / R1 | ☑️ |
| haiku45_2026-04 | SRG-2 [選択性の定量的根拠不在] (U4, U3, B17, B6由来) | R2+R6 / R2+R6 | ☑️ |
| haiku45_2026-04 | SRG-3 [収率測定基準の混在と不確定性] (B3, B4, B12, V3-Q1-3由来) | R3 / R3 | ☑️ |
| haiku45_2026-04 | SRG-4 [リガンド効果と立体化学要件の推定] (B1, V2-Q5, RI-05由来) | none: ligand effect / cis-configuration requirement / none: ligand effect / cis-configuration requirement | ☑️ |
| haiku45_2026-04 | SRG-5 [スコープ陳述と実証スコープの乖離] (B5, V1-Q1, V1-Q4, V1-Q6, V1-Q7由来) | R5 / R5 | ☑️ |
| haiku45_2026-04 | CLA (SRG外): なし。SRG-1–5で網羅される。 | header / header | ☑️ |
| opus47_2026-04 | SRG-1「マスバランスと副生成物定量の不在」 | R2 / R2 | ☑️ |
| opus47_2026-04 | SRG-2「提案触媒サイクルの直接的証拠の不在」 | R1 / R1 | ☑️ |
| opus47_2026-04 | SRG-3「1,2-ジクロロエチレンでの立体スクランブル」 | R6 / R6 | ☑️ |
| opus47_2026-04 | SRG-4「配位子活性順位の定性的記述」 | none: ligand activity ranking / cis-geometry inference / none: ligand activity ranking / cis-geometry inference | ☑️ |
| opus47_2026-04 | SRG-5「触媒終状態への沈黙（黒色混合物・多量の塩）」 | none: catalyst end state / black mixture and salts / none: catalyst end state / black mixture and salts | ☑️ |
| opus47_2026-04 | SRG-6「表エントリ単位の分析的開示欠落」 | R3 / R3 | ☑️ |
| opus47_2026-04 | SRG-7「溶媒効果の非裏付け」 | R5 / R5 | ☑️ |
| opus47_2026-04 | SRG-8「β-H 寛容性の機構的未解決」 | none: β-H tolerance mechanism / none: β-H tolerance mechanism | ☑️ |
| opus47_2026-04 | SRG-9「C_sp³ / 重ハロゲン化物の境界主張の非裏付け」 | R4 / R4 | ☑️ |
| opus47_2026-04 | SRG-10「収率基準の不整合」 | R3 / R3 | ☑️ |
| opus47_2026-04 | CLA-1「Corriu-Masse Ni(acac)₂ との非比較：ホスフィン配位子要件の未実証」 | none: Corriu-Masse Ni(acac)2 comparison / phosphine requirement / none: phosphine requirement vs Ni(acac)₂ (Corriu–Masse) benchmark ⚠ 不一致 | ☑️ |
| opus47_2026-04 | CLA-2「"Selective" の operational 定義不在：速度論／熱力学制御の未分離」 | R2 / R2 | ☑️ |
| gpt54thinking_2026-04 | SRG-1 [定量的副生成物・中間体データの不在] | R1+R2 / R1+R2 | ☑️ |
| gpt54thinking_2026-04 | SRG-2 [収率・同定フレームの不統一と分析仕様の省略] | R3 / R3 | ☑️ |
| gpt54thinking_2026-04 | SRG-3 [境界条件・比較設計なしの scope / condition 主張] | R4+R5 / R4+R5 | ☑️ |
| gpt54thinking_2026-04 | SRG-4 [立体化学異常の単発過読と将来送り] | R6 / R6 | ☑️ |
| gpt54thinking_2026-04 | SRG-5 [反応状態異常と触媒状態未同定] | none: catalyst end state / black mixture / none: catalyst end state / black mixture | ☑️ |
| gpt54thinking_2026-04 | SRG-6 [非最適条件の宣言と最適化空間の未提示] | R5 / R5 | ☑️ |
| haiku45_2026-09_run1 | SRG-α [定量的選択性検証の全体的不在] | R2+R3 / R2+R3 | ☑️ |
| haiku45_2026-09_run1 | SRG-β [触媒サイクルの実証的根拠不在] | R1 / R1 | ☑️ |
| haiku45_2026-09_run1 | SRG-γ [選択性原理の3層未説明] | R4 / R4 | ☑️ |
| haiku45_2026-09_run1 | SRG-δ [製品特性評価の不完全性] | none: product identity / purity characterization / none: product identity / purity characterization | ☑️ |
| haiku45_2026-09_run2 | SRG-1: Analytical data quality and yield basis closure | R3 / R3 | ☑️ |
| haiku45_2026-09_run2 | SRG-2: Mechanistic cycle validation absent | R1 / R1 | ☑️ |
| haiku45_2026-09_run2 | SRG-3: Selectivity control undemonstrated | R2 / R2 | ☑️ |
| haiku45_2026-09_run2 | CLA: Concurrent Corriu-Masse communication (C-2) undifferentiated | none: Corriu-Masse concurrent work comparison / novelty / none: concurrent Corriu–Masse work undifferentiated / novelty ⚠ 不一致 | ☑️ |
| haiku45_2026-09_run3 | SRG-1（触媒サイクル中間体の未観測） | R1 / R1 | ☑️ |
| haiku45_2026-09_run3 | SRG-2（選択性制御：速度論 vs. 熱力学の未区別） | R6 / R6 | ☑️ |
| haiku45_2026-09_run3 | SRG-3（溶媒・温度効果の速度論的根拠の不在） | R5 / R5 | ☑️ |
| haiku45_2026-09_run3 | SRG-4（分析検証の体系的不在：GLC内標・マスバランス・再現性） | R2+R3 / R2+R3 | ☑️ |
| haiku45_2026-09_run3 | SRG-5（反応範囲限界と副反応の報告不在） | R2+R4 / R2 ⚠ 不一致 | ☑️ |
| haiku45_2026-09_run3 | CLA (Claim-Level Adjunct) outside SRGs | header / header | ☑️ |
| haiku45_2026-09_run3 | CLA-1（Ni酸化価の非明示） | R1 / none: Ni oxidation state of intermediates unspecified ⚠ 不一致 | ☑️ |

各ブロックの全文は `srg_root_mapping/srg_blocks_packets.json`（block ID は key を参照）。特に ⚠ の 2 件と、Haiku 4.5（2026-04）が R4 を欠くという判定を見ていただけると助かります。


---

## E. B2 → Stage 3：「入力に無い内容の埋め合わせ」と判定された箇所（2026-09-29 追加）

Stage 3 の出力が、入力の記録にあるかのように示しながら記録にも PDF にも無い内容を書いた箇所の判定です（判定基準 `d4_baseline/b2_stage3_rating/rubric_e2_e3.md`）。U = パイプラインの記録を入力、B = 単一 prompt（B2）の記録を入力。判定者 A と B がそれぞれ挙げた箇所を並べます。各箇所が「埋め合わせ」に当たるかを確認してください（出力は `papers/dev/kumada/b2_stage3_R1_2026-09/in_{ID}/s3.md`、入力は同じ場所の `record.md`）。

| 出力（arm, run） | 判定者 | 箇所（≤30 語） | 理由 | 確認 |
|---|---|---|---|---|
| 485520（B, run1） | A | Items 3 and 40 are shared with SRG-8; items 15 and 51 are partially shared with SRG-9. | §2 SRG-1 notes. The record's SRG-9 is items 15, 16, 17, 36. Item 51 is in SRG-8, not SRG-9. | ☑️ |
| 485520（B, run1） | B | items 15 and 51 are partially shared with SRG-9 | Record SRG-9 = items 15, 16, 17, 36; item 51 is not a member (it is in SRG-1 and SRG-8). | ☑️ |
| 154160（B, run2） | A | Table I presents 13 entries with product identification by physical constants and spectral comparison to literature | §3. Table I has 11 yield rows; the record gives no count. | ☑️ |
| 154160（B, run2） | A | the n-BuMgBr/PhCl entry gives 76% isolated yield against a background of 81–98% for all other entries | §2 CLA-2. The record (item 27) says 89–98%; the PDF has 80% (α-NpMgBr), so '81–98%' is supported by neither. | ☑️ |
| 154160（B, run2） | A | For the double-coupling product Ph₂C=CH₂, characterization is sparser | §3. Nothing in the record or the PDF singles out Ph₂C=CH₂ characterisation. | ☑️ |
| 154160（B, run2） | B | transmetalation precedents using monodentate-phosphine or bipyridine Ni complexes (refs 12, 13) | Neither the PDF nor this record characterises the ligands of refs 12/13 (record item 33 says only that none uses the diphosphine); repeated in SRG-10. Possibly true from outside knowledge, but unsuppo | ☑️ |
| 154160（B, run2） | B | the n-BuMgBr/PhCl entry gives 76% isolated yield against a background of 81–98% for all other entries | Table I includes 80% (α-NpMgBr/CH2=CHCl); the record states 89–98% and mentions 80%. The 81–98% range is in neither. | ☑️ |
| 154160（B, run2） | B | Table I presents 13 entries with product identification by physical constants and spectral comparison to literature | PDF Table I has 11 rows; physical constants vs literature are given only for the two worked examples; the record gives no 13-entry count. | ☑️ |
| 247811（B, run4） | A | Items 1, 2, 3, 4, 8, 9, 14 (all A-classified) | §2 SRG-1. In the record, items 8 and 14 are U. | ☑️ |
| 247811（B, run4） | A | Items 8, 10, 15, 72 (mix of A and U) | §2 SRG-2. The record classes are 8 U, 10 U, 15 B, 72 U. There is no A item. | ☑️ |
| 247811（B, run4） | A | Items 5, 7, 49, 50 (mix of A and U) | §2 SRG-3. All four are U in the record. | ☑️ |
| 247811（B, run4） | A | Items 6, 20, 39, 40, 41, 42, 72 (all A) | §2 SRG-5. Items 42 and 72 are U in the record, and the output itself later calls 42 a U item. | ☑️ |
| 247811（B, run4） | A | Items 51, 61, 67 (mix of U and C) | §2 SRG-13. All three are U in the record. | ☑️ |
| 247811（B, run4） | A | Items 39, 40, 41, 42, 43 (all A) | §2 SRG-15. Item 42 is U in the record. | ☑️ |
| 247811（B, run4） | A | CLAs are identified from U-items in Part I not assigned to any SRG ... Grounded in item 7 (U). Not captured in SRG-3 | §2 CLA. The record's SRG-3 lists item 7 (Items: 5, 7, 49, 50). | ☑️ |
| 247811（B, run4） | A | the "and/or" characterisation language leaves characterisation depth uncertain for 10 of 12 Table I entries | §3 (also SRG-13). Table I has 11 entries, and the record gives no count of 12. | ☑️ |
| 247811（B, run4） | B | Items 1, 2, 3, 4, 8, 9, 14 (all A-classified). | Record classifies items 8 and 14 as U. | ☑️ |
| 247811（B, run4） | B | Items 8, 10, 15, 72 (mix of A and U). | Record classes: 8 U, 10 U, 15 B, 72 U - no A item. | ☑️ |
| 247811（B, run4） | B | Items 5, 7, 49, 50 (mix of A and U). | All four are U in the record. | ☑️ |
| 247811（B, run4） | B | Items 6, 20, 39, 40, 41, 42, 72 (all A). | Items 42 and 72 are U in the record (the same note later calls item 42 a U item). | ☑️ |
| 247811（B, run4） | B | items span the sp³/sp² boundary (21, 22), missing halide-class members (24, heteroaryl; 25, substituted aryl; 26, Hammett) | Record item 24 = allyl/benzyl/propargyl/acyl halides, 25 = heteroaryl, 26 = electronic substituent effects. | ☑️ |
| 247811（B, run4） | B | footnote 19 citing refs 11,12 (dipy-Ni) and 20 (low-valent Pd) — external systems | PDF fn 19/20 concern low-valent nickel complexes; record item 65 says Ni(0)/Pt(0). No Pd. Repeated in §3 VQ-2 '(refs 11, 12, 20 — dipy-Ni, low-valent Pd)'. | ☑️ |
| 247811（B, run4） | B | Items 51, 61, 67 (mix of U and C). | All three are U in the record. | ☑️ |
| 247811（B, run4） | B | Items 39, 40, 41, 42, 43 (all A). | Item 42 is U in the record. | ☑️ |
| 247811（B, run4） | B | Grounded in item 7 (U). Not captured in SRG-3 | Record SRG-3 = items 5, 7, 49, 50, so item 7 is an SRG member; the CLA rule the output states (U-items not in any SRG) is therefore misapplied on a false record claim. | ☑️ |
| 628833（B, run5） | A | convergence and gap information are inferred from item counts and category distribution (29 A, 13 B, 9 C, 21 U items; total 72 items) | §2 header. The record's Category tags give 28 A, 13 B, 9 C, 22 U. | ☑️ |
| 628833（B, run5） | A | the known β-hydride instability of transition-metal alkyls (refs in fn 17) is cited from other metal systems (Co, Rh, Ir, W) | §2 SRG-5. Footnote 17 cites a textbook and Yagupsky et al. and names no metals. The record has no such list. | ☑️ |
| 628833（B, run5） | A | the yield method is mixed across entries (five by glpc/internal standard per fn e, others by isolation | §2 SRG-7, repeated in §3 VQ-2. Footnote e is on 4 entries (98, 95, 95, 89). | ☑️ |
| 628833（B, run5） | A | Item 38 also appears in SRG-9 (external superiority) and SRG-12 (oxidative addition). | §2 SRG-7 notes. Item 38 is in SRG-7 and SRG-12, not SRG-9. SRG-12's note also mislabels SRG-7 as 'external superiority'. | ☑️ |
| 628833（B, run5） | A | the reaction mixture turns "black" immediately upon Grignard addition | §2 SRG-8. The PDF says only 'The resulting black mixture was heated to reflux'. The record says it was black before or after reflux. 'Immediately' has no support. | ☑️ |
| 628833（B, run5） | A | confirmed by glpc comparison with authentic samples ... Isolated yields for the two example procedures are reproducible at the preparative scale described | §3 VQ-1. The paper reports no authentic-sample comparison and no replicate or reproducibility data. | ☑️ |
| 628833（B, run5） | B | the known β-hydride instability of transition-metal alkyls (refs in fn 17) is cited from other metal systems (Co, Rh, Ir, W) | Neither the record nor the PDF identifies the metals in the fn 17 references (a textbook chapter and Yagupsky et al.). | ☑️ |
| 628833（B, run5） | B | Item 38 also appears in SRG-9 (external superiority) and SRG-12 (oxidative addition). | Record SRG-9 = items 31, 32, 33, 34, 43; item 38 is in SRG-7 and SRG-12 only (SRG-12 note likewise mislabels SRG-7 as 'external superiority'). | ☑️ |
| 628833（B, run5） | B | The cross-coupling products in Table I are confirmed by glpc comparison with authentic samples | Neither PDF nor record mentions comparison with authentic samples; PDF says only 'Characterized by glpc, nmr, ir, and/or mass spectra'. | ☑️ |
| 628833（B, run5） | B | Isolated yields for the two example procedures are reproducible at the preparative scale described. | No reproducibility or replicate data exist in the PDF; the record itself lists absence of replication. | ☑️ |
| 401244（U, run1） | A | n-BuMgBr + m-dichlorobenzene; PhMgBr + CH₂=CHCl; n-C₆H₁₃MgCl + CH₂=CHCl; PhMgBr + cis-ClCH=CHCl | §5 route to VQ-3 gives these as Table I entries. The paper's entry is n-C8H17MgCl, and neither the record nor the PDF has a C6H13 Grignard. | ☑️ |
| 401244（U, run1） | B | n-BuMgBr + m-dichlorobenzene; PhMgBr + CH₂=CHCl; n-C₆H₁₃MgCl + CH₂=CHCl; PhMgBr + cis-ClCH=CHCl | Listed as existing Table I entries; the PDF and record have n-C8H17MgCl + CH2=CHCl, not n-C6H13MgCl. | ☑️ |
| 542931（U, run2） | A | For entries 1–2 (n-BuMgBr/PhCl) and entry 7 (PhMgBr/CH₂=CHCl), these byproducts are commercially available; for biaryl entries | §2 SRG-1. Entry 1 is EtMgBr/PhCl, and Table I has no biaryl entry. Neither the record nor the PDF supports this. | ☑️ |
| 542931（U, run2） | A | β-H suppression is presented as a "remarkable feature" ... the evidence is purely observational — "high yield was obtained." | §2 SRG-5 notes. In the paper 'remarkable' refers to chloride reactivity and to the catalytic activity of bidentate ligands. The quoted phrase is not in the paper or the record. | ☑️ |
| 542931（U, run2） | A | Measure the activity order [NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] > [NiCl₂(PPh₃)₂] | §2 CLA (ligand). This restates the paper's order wrongly: the PDF and record B-7 give dmpe ≈ PPh3. | ☑️ |
| 542931（U, run2） | B | For entries 1–2 (n-BuMgBr/PhCl) and entry 7 (PhMgBr/CH₂=CHCl), these byproducts are commercially available; for biaryl entries they are obtainable by Ullmann coupling. | Table I entry 1 is EtMgBr/PhCl, and Table I contains no biaryl entries; paper facts not supported by PDF or record. | ☑️ |
| 771464（U, run3） | A | The Note Added in Proof is the last substantive item in the paper. | §2 CLA (Corriu–Masse). The Note Added in Proof is footnote 3a on p.4374, not the last item. Neither the record nor the PDF supports the claim. | ☑️ |

（E2 の引用 74 件は、2 名とも「原典を正確に伝えていない」を 0 件と判定しています。確認は任意です：`d4_baseline/b2_stage3_rating/rater{A,B}_e2.json`）

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
