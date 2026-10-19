prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Yamamoto, Hayashi, Yamamoto 1978（Bull. Chem. Soc. Jpn. full_paper）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-06a, EP-03a

- **EP-06a Analogy-validation pack**: Scheme 1の触媒サイクル輸入（Kumada 1972→Tamao 1976 BCSJ→本論文）の検証として求められる「n=1類縁体BrNi(bpy)(C₆H₄Br)の単離・同定」は、1980年代以降の有機金属化学において独立した研究主題として存在する可能性が高い。特に同一グループ（Akio Yamamoto, Tokyo Institute of Technology）が後続論文でモノアルキルNi錯体を研究しており（Yamamoto 1981 BCSJ: Yamamoto, Kohara, Yamamoto）、monoaryl-Ni(X)(L₂)型錯体への展開が期待される。

- **EP-03a Direct-observation / state-assignment pack**: 遷移金属触媒重縮合の機構中間体（Ni-aryl種）の直接観察を要求するEP-03aは、重縮合触媒化学の独立したテーマとして1980〜2000年代に活発に研究されてきた。Parshall 1974（trans-NiAr(X)(PEt₃)₂の単離）およびYamamoto 1981（NiEt(Y)(L)₂の合成）が具体的な充填候補として存在する。

**第二群（間接的に追跡可能）：** EP-05a, EP-09a, EP-04a

- **EP-05a Quantitative-ranking substantiation pack**: poly(p-phenylene)等のGPCによる絶対分子量測定は、1980年代の高分子化学文献において技術的進展として扱われたが、本論文の具体的な反応系を対象として行われた独立研究は限定的。レビュー・手法論文に含まれる可能性あり。

- **EP-09a Internal benchmark pack**: 本論文の遷移金属触媒重縮合法とUllmann法・Wurtz-Fittig法の直接数値比較は、高分子化学のレビュー・教科書（例：Schluter 1991, JACS "Synthesis of Poly(p-phenylene)"）に間接的に含まれる可能性があるが、同一条件での並行実験は独立論文として発表されにくい。

- **EP-04a Discrimination / replication pack**: ラジカル経路排除実験（TEMPO添加）や動力学の反復は、後続機構研究（Transalkylation, Yokozawa群等）に間接的に含まれる可能性があるが、本論文の系固有の実験として独立論文を特定するのは困難。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a, EP-10a

- **EP-01a Reporting-coherence pack**: Table 1の収率基準の統一や copolymer 収率表示の整合性は、Full Paper展開時の自動解消パターンに近いが、本論文自体がFull Paperであることを考えると、このRI-01の問題は独立論文として充填される性質ではない。

- **EP-08a Replication / uncertainty pack**: 動力学実験（Fig. 3）の反復測定・誤差棒付与は、分野慣行として独立論文化されにくいRI-08起因の問題。1978年から現代への自然な報告水準改善の一部として部分的に解消されている可能性あり。

- **EP-10a Kinetic verification pack（暫定）**: 重縮合系の速度論的解析（Scheme 1からの速度式導出）は、1990〜2000年代の理論的Ni-catalyzed polycondensation研究において取り扱われた可能性があるが、本論文の具体的系（NiCl₂(bpy)/p-C₆H₄Br₂/Mg/THF）に対する速度式の独立導出は特定困難。

---

### §B 各EPの充填論文候補

---

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model（Scheme 1の重縮合系への外挿検証）
* **充填開始点**: Yamamoto, Kohara, Yamamoto, *Bull. Chem. Soc. Jpn.*, **54**, 2010 (1981) — 同一グループ（Akio Yamamoto, Tokyo Institute of Technology）による後続論文が、ジアルキルNi(II)錯体 NiR₂L₂（R = Me, Et; L = bpy, PEt₃）とモノアルキルNi(II)錯体 NiR(Y)Lₙ の合成・単離・NMR特性評価を報告し、これらが「Ni触媒反応の鍵中間体と想定される」と明記している。中間体1（モノアリール-Ni-X-L₂型）の直接類縁体にあたるモノアルキル錯体の単離は、Yamamoto 1978のScheme 1の輸入モデル（Tamao 1976 BCSJ）に対するalkyl版の独立検証として機能する。
* **充填確立点**: Yamamoto, Kohara, Yamamoto, *Bull. Chem. Soc. Jpn.*, **54**, 2010 (1981) — 同上（Yamamoto 1981はモノアルキル錯体を扱い、Yamamoto 1978のmonoaryl中間体1の直接対応物は提供していない点に注意：これはalkyl版の充填であり、aryl版（BrNi(bpy)(C₆H₄Br)）の充填は未達成）。
* **充填の性質**: Partial — Yamamoto 1981はモノアルキル-Ni錯体の単離を実証したが、本論文のScheme 1中間体1（モノアリール-Ni-X-bpy型）の直接充填ではなく、alkyl-Ni類縁体による間接的検証にとどまる。aryl-Ni-X-L₂型の明示的単離は別の論文が必要。
* **Confidence**: High（Yamamoto 1981の存在・内容・同グループからの出版は確認済み；Yamamoto 1981 S3v2出力が参照材料として提供されている）
* **注記**: Yamamoto 1981はStage 3 §6で「Second-generation EP-03a inheritance」の姉妹論文として同定されており、Yamamoto 1978 → Yamamoto 1981 の自己充填パターンが成立。充填までの年数：3年（1978→1981）。ただし充填は「alkyl類縁体による間接充填」の性質。同一グループによる自己充填（partial）。Yamamoto 1981 S3v2では「NiEt(Cl)(bpy)」（錯体14）がmonohaloalkyl-Ni中間体候補として同定されており、これがYamamoto 1978のScheme 1中間体1のalkyl版に対応する。

---

**EP-03a Direct-observation / state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（中間体1・2の直接観測）
* **充填開始点（Aryl-Ni側）**: Parshall, G. W., *J. Am. Chem. Soc.*, **96**, 2360 (1974) — trans-NiAr(X)(PEt₃)₂型のモノアリール-Ni(X)(L₂)錯体（Aryl = Ph等; X = Cl, Br; L = PEt₃）の単離・X線構造解析・NMR特性評価を報告。これはYamamoto 1978のScheme 1中間体1（BrNiL₂–C₆H₄–MgBr型）のPEt₃配位子系版に相当するmonoaryl-Ni(X)(L₂)種の最も近い充填候補。ただし本報の実施時点（1974）はYamamoto 1978（1978）の発表前であり、Yamamoto 1978がParshall 1974を引用しているかを確認する必要がある（引用なし：C-xxから外れた未引用同時代充填論文）。
* **充填確立点（bpy系）**: Yamamoto, Kohara, Yamamoto, *Bull. Chem. Soc. Jpn.*, **54**, 2010 (1981) — bpy配位子系のモノアルキルNi(II)錯体（中間体1のalkyl版）を単離・NMR同定。bpy系のmonoaryl版（BrNi(bpy)(C₆H₄Br)相当）の明示的単離は、後続のHayashi-Kumada型触媒機構研究または重縮合触媒機構研究に移行した可能性がある。
* **充填の性質**: Partial（Parshall 1974 → PEt₃系monoaryl、Yamamoto 1981 → bpy系monoalkyl；bpy系monoaryl-Ni(X)(L₂)の直接単離は限定的）
* **Confidence**: Medium（Parshall 1974については内容に推論を含む；trans-NiAr(X)(PR₃)₂型錯体の先行単離事例としての存在は高信頼だが、JACS 1974年の具体的内容のEP充填との対応は中程度）
* **注記**: EP-03aのbpy系充填は、重縮合触媒機構の研究（Yokozawa群、Woo群、1990〜2010年代）においてより完全に達成された可能性がある。Yamamoto 1978は参照材料としてTamao 1976 BCSJ（ref. 6b）を挙げているが、Parshall 1974は本論文の参照リストには存在しない（GAP-4に対応：Morrell-Kochi 1975を経由する間接的知識経路）。

---

**EP-05a Quantitative-ranking substantiation pack（第二群）**

* **充填するRI**: RI-05 Qualitative overread（絶対Mn不在によるDP主張の過読）; RI-08 Unquantified reliability
* **充填開始点**: Schlüter, A.-D., *J. Polym. Sci., Polym. Chem.*, **32**, 1955 (1994) — poly(p-phenylene)およびその誘導体の合成論文において、GPC（THF/CHCl₃ベース）によるMn/Mw/PDI測定が標準的に報告されるようになった1990年代の代表事例。Yamamoto群や関連グループの後続重縮合論文にGPCデータが含まれる可能性あり。
* **充填確立点**: 未同定（poly(p-phenylene)の高温GPC測定による絶対Mn報告が本系に適用された独立論文が特定できない）。Yamamoto群の後続論文（1981年以降のBCSJ掲載重縮合論文）にGPCデータが含まれる可能性がある。
* **充填の性質**: Indirect（1990年代以降の高分子合成論文では絶対Mn報告が標準化されたが、本論文の具体的反応系（NiCl₂(bpy)/p-C₆H₄Br₂/Mg）に対する直接の「充填実験」は特定困難）
* **Confidence**: Low（文献の存在は推測可能だが、本論文系への直接対応は未確認）
* **注記**: 1990〜2000年代の重縮合触媒化学（Yokozawa, Yokota, Yokozawa-Ohta等）では、Ni触媒重縮合のMn/PDIが詳細に報告されるようになったため、技術駆動充填パターンに相当する可能性あり。

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority（従来法との直接数値比較不在）
* **充填開始点**: 未同定（同一モノマーによるUllmann法、Wurtz-Fittig法、酸化カチオン重合法との直接並行実験を報告した論文を特定できない）。Kovacic-Oziomek系の後続論文（refs 2b,2cの後継研究）に部分的な比較データが含まれる可能性あり。
* **充填確立点**: 未同定
* **充填の性質**: Indirect（高分子化学レビューにおいて諸合成法の間接的比較はなされているが、本論文が要求する「同一モノマー、同一キャラクタリゼーション手順での直接並行実験」を実施した独立論文は特定困難）
* **Confidence**: Low
* **注記**: Dropped Quantitative Benchmark（B-4, SRG-4）の解消には、インセンティブ構造の問題が存在する：「既存法との比較実験のみを主題とした論文」は新規性要件の観点から出版されにくい。VQ階層逆転の典型事例（低VQ要件の未充填）。

---

**EP-04a Discrimination / replication pack（第二群）**

* **充填するRI**: RI-04 Unreplicated discriminator（Fig. 3単一データから機構推論）; RI-03（ラジカル経路排除）
* **充填開始点（ラジカル排除）**: 複数の研究グループがNi触媒クロスカップリングにおけるラジカル/イオン経路の識別実験（ラジカルクロック基質使用、TEMPO添加等）を1980〜1990年代に実施。特にKochi group (Morrell, Kochi, JACS 1975, ref. 6c)が関連実験を提供している可能性があるが、本論文の重縮合系固有の識別実験は特定困難。
* **充填確立点**: 未同定（重縮合系固有のラジカル/イオン識別実験を独立主題とした論文は未同定）
* **充填の性質**: Indirect
* **Confidence**: Low
* **注記**: Yokozawa群（controlled Kumada-type polycondensation, 2004以降）の機構研究が部分的に充填している可能性あり。ただし異なる配位子系（dppe等）を使用しており、NiCl₂(bpy)系への直接転用は限定的。

---

**EP-10a Kinetic verification pack（第三群）**

* **充填するRI**: PRI-11（Mechanism-kinetics decoupling）; RI-04
* **充填開始点**: 未同定（Yamamoto 1978の具体的系（NiCl₂(bpy)/p-C₆H₄Br₂/Mg/THF, 3 °C）に対する速度式の代数的導出と速度定数報告を実施した論文を特定できない）。1990〜2000年代のKumada type polycondensation の機構研究（特にYokozawa群の「quasi-living polymerization」研究）が近傍にあるが、NiCl₂(bpy)系を具体的に対象とした速度則解析は限定的。
* **充填確立点**: 未同定
* **充填の性質**: 未同定
* **Confidence**: Low
* **注記**: PRI-11（第3確認例候補）の観点からは、Breitenfeld 2014と Pengfei 2024が同様の機構-速度論デカップリングパターンを示した論文として記録されており、本論文の充填ではなく同型パターンの確認例。

---

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity（収率基準不統一、Table 1内の不整合）
* **充填開始点**: 未同定（Table 1の収率基準統一という問題は独立論文として充填される性質ではない）
* **充填の性質**: 未同定（第三群：充填が見つからない可能性あり）
* **Confidence**: Low
* **注記**: RI-01起因の問題はFull Paper展開での自動解消パターンに近いが、本論文自体がFull Paperであるため、その自動解消は後続論文での訂正または別報での再実験によってしか達成されない。インセンティブ構造の不整合（数値修正のみの論文は出版されにくい）。

---

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability（反復測定・不確かさ記述なし）
* **充填開始点**: 未同定
* **充填の性質**: 未同定
* **Confidence**: Low
* **注記**: RI-08の問題は分野の報告慣行として体系的に回避されてきた可能性がある（重縮合収率の誤差棒付与は現代でも一般的ではない）。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Yamamoto, Kohara, Yamamoto, *Bull. Chem. Soc. Jpn.*, 54, 2010 (1981) | EP-06a（partial）, EP-03a（partial, alkyl版） | VQ-3（部分） | 1981 | High |
| 2 | Parshall, G. W., *J. Am. Chem. Soc.*, 96, 2360 (1974) | EP-03a（partial, PEt₃系monoaryl-Ni(X)L₂） | VQ-3（部分） | 1974* | Medium |
| 3 | Tamao, Sumitani, Kumada, *J. Am. Chem. Soc.*, 94, 4374 (1972) | EP-06a（analogy source; Scheme 1の輸入元の実験基盤） | VQ-2 | 1972* | High |
| 4 | Tamao, Sumitani, Kiso, ..., Kumada, *Bull. Chem. Soc. Jpn.*, 49, 1958 (1976) | EP-06a（Scheme 1のステップa–dの4ステップ機構の一次ソース） | VQ-3（indirect） | 1976* | High |
| 5 | Morrell, Kochi, *J. Am. Chem. Soc.*, 97, 7262 (1975) | EP-04a（ラジカル/イオン経路識別；Ni-触媒クロスカップリングの機構的識別実験） | VQ-3（indirect） | 1975* | Medium |

*注：順序2–5は本論文（1978）の発表以前の論文であり、「充填」ではなく「本論文が参照できたにもかかわらず参照しなかった（または不十分にしか参照しなかった）先行知識基盤」として位置づけられる。これらはGAP論文（GAP-1～4）に対応し、本論文が生成するEPの「先行充填試み」として記録する。

**充填後から本論文以降の追加候補（1978年以降）：**

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 6 | Yokozawa, Yokota et al., various 2004–2015 (*JACS*, *Macromolecules*) | EP-10a（準living重縮合の速度論的解析）, EP-04a（partial） | VQ-3（partial） | 2004–2015 | Medium |

**選定理由：**

Yamamoto 1981（順序1）は最も決定的な充填候補であり、同一グループ（Akio Yamamoto, Tokyo Tech）がScheme 1のalkyl版類縁体を独立に合成・単離することでEP-06aとEP-03aを部分充填している。バンドル充填（EP-06a + EP-03a both partially covered）の効率性と高信頼度（High）から、最優先として選定する。

Tamao 1972（順序3）とTamao 1976 BCSJ（順序4）は本論文のScheme 1の一次ソースであり、Yamamoto 1978がこれらを引用（ref. 6a, 6b）しているにもかかわらず、Scheme 1の重縮合系への適用の同型性実証を行っていないため、EP-06a解消の「基礎文献」として参照する。これらはYamamoto 1978を充填する論文ではなく、むしろYamamoto 1978がScheme 1の充填責任を果たさなかったことを示すコンテキスト証拠として位置づけられる。

Parshall 1974（順序2）はmonoaryl-Ni(X)(PR₃)₂の単離という点でEP-03aに最も直接対応するが、本論文（1978）は発表時点でParshall 1974を引用しておらず（GAP-4が指摘している）、知識の非活用パターンが示されている。

**重要な「逆充填」観察：** Yamamoto 1978自身はKumada 1972の EP-03a（中間体単離）を充填しない。Kumada 1972のStage 3（kumada1972_v17_sonnet_s3.md）ではSRG-1（機構サイクルの実験的根拠欠如、EP-06a + EP-03a）が未解消のまま残されており、Yamamoto 1978はKumada 1972のEP-03aギャップを「解消」するのではなく「継承・拡張」している（Second-generation EP-03a inheritance）。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2要件（RI-01, RI-07: Method層）: EP-01a（収率報告整合）→ **未充填**（インセンティブ構造問題）; EP-08a（反復測定）→ **未充填**（分野慣行として回避）

- VQ-3要件（RI-03, RI-04, RI-06: Mechanism層）:
  - EP-06a（analogy検証）→ 1972年: Tamao-Kumada（analogy source）; 1981年: Yamamoto 1981（自己充填、alkyl版partial）; 技術駆動充填（1980–2000年代）
  - EP-03a（中間体直接観測）→ 1974年: Parshall（PEt₃系, prior art); 1981年: Yamamoto 1981（bpy系alkyl版, 自己充填）; 2000年代〜: Yokozawa群（quasi-living polycondensation）

- VQ-4要件（RI-08, RI-09: Benchmark層）:
  - EP-05a（絶対Mn報告）→ **技術駆動充填**（1990年代以降のGPC標準化により間接充填）
  - EP-09a（従来法直接比較）→ **未充填**（インセンティブ構造問題）

**階層-時間対応の評価：**

VQ階層が上がるほど充填に時間がかかるという仮説は、本論文に対しては部分的に支持される。VQ-2要件（RI-01, RI-07）の充填は技術的に容易なはずだが、むしろインセンティブ構造の問題で未充填のまま残っている。これは「VQ階層逆転」パターン（低VQが未充填、高VQが部分充填）の事例である。VQ-3要件（RI-03, RI-06）については自己充填（Yamamoto 1981, 3年）が比較的速く起きているが、充填が「alkyl版」にとどまり「aryl版」には達していない。

**特筆すべきパターン：**

1. **自己充填（Partial, 3年）**: Yamamoto 1978 → Yamamoto 1981（同グループ、alkyl-Ni錯体合成によるEP-06a/03aの部分充填）。自己充填パターンの代表的事例。ただし充填がalkyl版にとどまる点が特徴的。

2. **先行充填（Prior filling without citation）**: Parshall 1974はYamamoto 1978の発表4年前にtrans-NiAr(X)(PR₃)₂を単離しているが、Yamamoto 1978はこれを引用していない。これはGAP-4（Morrell-Kochi引用）と同様の「分野横断的知識の非活用」パターン。

3. **VQ階層逆転（出版インセンティブによる）**: EP-09a（RI-09, VQ-4相当）は独立論文として充填されにくいが、EP-06a（RI-06, VQ-3相当）は後続研究の主題として充填された。より高VQの要件が先に充填され、低VQのreporting-coherence要件が長期にわたり未充填。

4. **Second-generation non-filler（本論文の構造的位置づけ）**: Kumada 1972のEP-03a（Ni-aryl中間体単離）が未充填のまま、Yamamoto 1978がそのEP-03aギャップを「重縮合系に継承」した。Yamamoto 1978はKumada 1972を充填せず、自身のEP-03aギャップを生成した。Yamamoto 1981が初めてalkyl版partial充填を行う。この3世代構造（Kumada 1972 → Yamamoto 1978 → Yamamoto 1981）は「EP-03aギャップの世代間継承→partial自己充填」の典型事例として記録する価値がある。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

**EP-09a Internal benchmark pack:**
* **未充填の理由**: インセンティブ構造の不整合 — 同一モノマーによる従来法（Ullmann, Wurtz-Fittig）との直接並行比較実験は技術的に実施可能だが、「既存法との比較のみを主題とした論文」は新規性要件の観点から独立論文として出版されにくい。重縮合触媒化学のレビュー・教科書には間接的な比較が含まれるが、本論文の具体的系での直接比較データが独立論文に存在するかは未確認。
* **発見的意義**: あり — 「新法の優位性主張が直接比較なく行われた慣行」は、1970〜80年代の高分子合成化学において体系的に繰り返されたパターンであり、UQSがこれを「現在まで充填されていない可能性のある構造的不在」として検出していることは、当時の合成報告文化に関する分析的知見を提供する。
* **将来の充填可能性**: 中 — 現代の技術で実施可能だが、「既存研究の直接追試」として論文化されにくい。

---

**EP-10a Kinetic verification pack（暫定）:**
* **未充填の理由**: 分野慣行の回避の可能性 + 技術的困難 — NiCl₂(bpy)/p-C₆H₄Br₂/Mg系の速度則解析は、重縮合動力学の複雑さ（Schulz-Flory分布とScheme 1サイクルの連立）のために独立論文として扱われにくい。2004年以降のYokozawa群によるquasi-living Kumada-type polycondensation研究（dppe系）は近傍に位置するが、bpy系NiCl₂の速度論的解析ではない。
* **発見的意義**: あり — Yamamoto 1978からYokozawa群の準生きたKumada重縮合（2004年〜）まで、Ni触媒重縮合の速度則が完全には解析されなかった期間（約25年）は、PRI-11（Mechanism-kinetics decoupling）が分野レベルで体系的に放置されてきた期間として記録できる。これはUQSが機構-速度論デカップリングを「分野が長期にわたり回避してきた構造的問い」として同定した事例となる。
* **将来の充填可能性**: 高 — 現代のin situ NMR/IR技術と計算化学（DFT + kinetic simulation）により、Scheme 1の個々のステップの速度定数推定は技術的に実施可能。

---

**EP-01a Reporting-coherence pack:**
* **未充填の理由**: 報告形式問題 + インセンティブ構造の不整合 — Table 1の収率基準不統一（entries 25, 27の%なし表示）は、後続論文での再実験・再報告によってのみ解消可能だが、このためだけの独立論文は出版されない。
* **発見的意義**: なし（報告形式問題は個別論文のEP-01aとして記録したが、独立の発見的意義はない）。
* **将来の充填可能性**: 低 — 特定の報告不整合の訂正は現代でも独立論文化されない。

---

**EP-08a Replication / uncertainty pack:**
* **未充填の理由**: 分野慣行として体系的に回避 — 高分子化学の収率報告における反復実験・標準偏差の付与は、現代においても義務的ではないケースが多く、本論文固有の未充填問題ではなく分野全体の慣行問題。
* **発見的意義**: なし（個別論文の問題として記録済み）。
* **将来の充填可能性**: 低（慣行として変化が遅い）。

---

**VQ階層逆転の診断：**

本論文のEP未充填パターンを検討すると、以下の逆転が観察される：

- **低VQ要件（RI-01, RI-08: reporting-coherence, replication）** → 未充填 (EP-01a, EP-08a, EP-09a)
- **高VQ要件（RI-03, RI-06: mechanism, intermediate observation）** → Partial充填 (EP-03a, EP-06a through Yamamoto 1981 and prior art)

これは「科学的論理に基づくEP充填順序（低VQ要件を先に充填）」と「出版インセンティブに基づく実際の充填順序（高VQ要件が先に充填）」の逆転パターンの事例である。高VQ要件（中間体単離、機構検証）は独立論文の主題として出版されやすいが、低VQ要件（収率の反復測定、直接比較実験）は新規性不足により出版されにくい。この逆転は分野のインセンティブ構造がUQSの構造的不在の一部を維持していることの証拠として記録する。
