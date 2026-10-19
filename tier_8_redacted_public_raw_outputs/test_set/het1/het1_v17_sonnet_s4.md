```
prompt_version: stage4-v1-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Yuan et al. 2018（Journal of the American Chemical Society, full_paper）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a

— EP-03a: 高時間分解能XAS（quick-XANES/quick-EXAFS）によるPd種のリアルタイム追跡は、シンクロトロン施設グループ（ESRF, SLS, SOLEIL, APS）が2000年代以降に独立した方法論論文として継続的に発表してきたテーマであり、Pd触媒への応用論文も複数存在する。RI-03の「観測されない活性種」に対するquick-XASによる上限設定という具体的アプローチが主題として成立しうる。

— EP-06a: Pd触媒クロスカップリング反応における陽イオン/中性経路の識別（ハメット相関・ハライドイオン効果）は、Jutandグループをはじめとする均一系Pd触媒機構研究者が1990年代から独立した機構論文として体系的に発表してきた中心テーマであり、文献上の充填候補が高密度に存在する。

**第二群（間接的に追跡可能）：** EP-04a, EP-09a

— EP-04a: ブランクXAS実験（ArI/オレフィン不在の対照実験）と再現オペランドランは、独立した主題論文として発表されるよりも、大型operando XAS研究の補足情報・方法論節として含まれる傾向があるが、「operando XASのベストプラクティス確立」を主題とする方法論論文が間接的充填候補として存在しうる。

— EP-09a: Pd@MOF触媒のTON/TOF定量ベンチマークは、独立論文の主題として発表されるよりも、レビュー論文・総説・後続スコープ拡張論文における比較表として間接的に充填される形が典型的であり、対象系そのものでの直接充填論文の同定は困難。

**第三群（充填が見つからない可能性あり）：** EP-08a

— EP-08a: EXAFSの完全系統誤差バジェット（S₀²不確かさ含む）とLCF時点別R因子報告は、この特定論文のデータに対して独立研究として充填される性質ではなく、分野のベストプラクティス文書（IFEFFIT/Athena マニュアル、IUCr勧告）の発展として対処されるRI-08パターンの典型。§6で指摘した「single-run operando」下位パターンは分野が構造的に回避してきた問いである可能性があり、独立充填論文が存在しない可能性が高い。

---

### §B 各EPの充填論文候補

---

**EP-03a Direct-observation/state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（SRG-3 Primary：Pd(0)活性種の非観測）+ RI-03 secondary（SRG-4：Cl⁻毒化の因果未検証）

* **充填開始点（quick-XASによるPd(0)存在上限の設定）**:
  — Briois, V. et al., J. Phys. Chem. C / J. Synchrotron Radiat.（推定 2010–2016）— SOLEIL放射光施設のQUICK-EXAFSビームラインを用いたPd系触媒の時間分解XANES研究。sub-100 ms時間分解でのPd(0)/Pd(II)酸化状態追跡を実証。
  — **Confidence: Low**（Brioisグループのquick-EXAFS論文群は確実に存在するが、特定タイトル・年・Pd-Heck系への直接適用の有無について実文献確認が必要）

* **充填確立点（自己充填の有力候補）**:
  — Yuan/Ding グループ後続論文（推定 2019–2023）— S0-6の「[REDACTED: verbatim source text; see the source paper via its DOI]」という明示的留保は、後続Full Paper（または続報通信）の準備を示唆する。quick-XANESまたはin situ UV-visによるPd(0)過渡種検出を含む可能性が最も高い自己充填候補。
  — **Confidence: Low**（後続論文の計画は強く示唆されるが、実際の発表・内容の詳細は未確認）

* **充填の性質**: Indirect（現時点での同定は類似系での充填または自己充填の推定にとどまる）
* **Confidence全体**: Low
* **注記**: EP-03aはSRG-3（U-1, A-1, B-16）とSRG-4（U-3, B-11）の両方に対応。均一系Pd触媒における速度論的プローブ（Hammett + KIE）が間接的充填として機能しうるが、MOF細孔内配位環境を考慮した同型性実証は均一系充填では達成されない（RI-06が残存）。VQ-3の最重要充填点であるため、充填未同定の科学史的意義は大きい（→§E参照）。

---

**EP-04a Discrimination/replication pack（第二群）**

* **充填するRI**: RI-04 Unreplicated discriminator（SRG-5 Primary；U-2, B-7, B-8）+ RI-08 secondary（SRG-2；B-3）

* **充填開始点（operando XAS方法論のベストプラクティス文書化）**:
  — Weckhuysen, B.M. et al., Chem. Soc. Rev. / Nat. Rev. Chem. 2010–2020（複数論文）— in situ / operando XASのベストプラクティスを論じた総説・レビュー群で、ブランク実験・対照実験・複数ランによる再現性確認の重要性が方法論として記述されている。
  — **Confidence: Medium**（Weckhuysenグループのoperando XASレビュー論文群は確実に存在し、方法論的推奨を含む。ただし、ブランクXASを「主題として」記述した独立論文の同定には文献確認が必要）

* **充填確立点（類似系への直接適用）**:
  — Newton et al. (het2), ACS Catal. 2024 — 本プロジェクトに登録されたheterogeneousタイプ論文として実在が確認されている。現代水準のoperando XAS研究として、ブランク実験・再現実験の実施状況がEP-04a充填の指標となりうる。ただし§6の記述（het2でも同種の省略が複数B/U項目として記録されている）は、EP-04aの完全充填を達成していない可能性を示唆する。
  — **Confidence: Medium**（論文の実在は確認済み；EP-04aの充填度は本プロジェクトのhet2 S1/S2出力で確認可能）

* **充填の性質**: Partial（operando XAS分野全体での方法論的推奨として間接充填；この特定システムでの直接充填は未同定）
* **Confidence**: Medium（方法論的推奨文書）/ Low（特定システムへの直接充填）
* **注記**: SRG-5のブランクXASと等温開始実験は独立論文の主題になりにくく、自己充填（Yuan後続論文）が最も可能性の高い充填経路。H₂O滴定実験（H₂O必須性の閾値決定）は同グループの後続スコープ論文で実施される可能性が高い。

---

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model（SRG-3 secondary；B-16：陽イオン機構のMOF系への適用根拠）

* **充填開始点（均一系Pd機構、陽イオン/中性経路の速度論的識別）**:
  — Amatore, C.; Jutand, A., Organometallics / J. Organomet. Chem. 1988–1993 — Pd(0)錯体へのアリールハライドの酸化的付加速度論と、ハライドイオン濃度効果の定量的評価。陽イオン型 vs. 中性型Pd(0)の反応性差を電気化学・速度論的手法で確立した一連の論文群。
  — **Confidence: High**（Amatore & Jutandグループのこの時代のOA速度論論文は確実に存在する。特定論文の詳細については確認が望ましいが、内容の大枠は確実）

* **充填確立点（Heck機構の包括的整理）**:
  — Jutand, A., Chem. Rev. 2008, 108, 2300–2347, "Contribution of Electrochemistry to Organometallic Catalysis" — 均一系Pd触媒クロスカップリング反応のハメット相関（ρ値の符号・大きさと機構の対応）、ハライドイオン効果（陽イオン促進 vs. 抑制）を体系的に整理したレビュー。アリールヨウ化物のPd(0)酸化的付加に対するρ ≈ +2〜+3 の値を含む。
  — **Confidence: High**（Jutand Chem. Rev. 2008はPd触媒機構分野の標準参照文献として確実に存在する）
  — **MOF系固有の充填（陽イオン機構のMOF細孔内適用）**: 未同定。MOF細孔内の配位環境・幾何学的拘束を考慮した陽イオン機構の直接検証は独立論文として未発表の可能性が高い。

* **充填の性質**: Indirect（均一系Pd触媒での陽イオン/中性経路識別は確立；MOF系への同型性実証は部分充填にとどまる）
* **Confidence**: High（均一系充填：Jutand論文群）/ 未同定（MOF系固有充填）
* **注記**: EP-06aの充填は二層構造を持つ。均一系ハメット相関（ρ > 0）によりHeck反応における陽イオン機構の間接支持は1990年代に確立された（Jutand High）。しかしMOF細孔内のPd–NH₂二座配位子環境がホモジニアス系と同一の機構を経由するかという RI-06の核心は、均一系充填では解消されない。SRG-3の「Imported model」問題はMOF触媒論文全般の構造的弱点であり、この特定のRI-06発現形式の充填は現在まで系統的に不完全な可能性がある（→§E参照）。

---

**EP-08a Replication/uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability（SRG-1 Primary；B-1, B-2 + SRG-2 secondary；B-3 + SRG-4 secondary；B-11）

* **充填開始点（XAS解析ベストプラクティスの方法論的確立）**:
  — Ravel, B.; Newville, M., J. Synchrotron Radiat. 2005, 12, 537–541, [REDACTED: substantial verbatim quotation; see Tier 9] — EXAFSデータ解析（S₀²決定・不確かさ伝播・フィット品質R因子・χ²_red）の標準的手法を記述した定義論文。LCFの統計的品質評価の方法論的根拠を提供する。
  — **Confidence: High**（Ravel & Newville JSR 2005はXAFSコミュニティの最も引用される論文の一つとして確実に存在する）

* **充填確立点（この特定論文のデータへの直接適用）**: **未同定**
  — 本論文のEXAFSデータに対して第三者が独立に再解析・不確かさバジェット評価を実施した論文は存在しない可能性が高い。

* **充填の性質**: Indirect（方法論文書としての間接充填のみ；特定論文データへの直接充填なし）
* **Confidence**: High（Ravel & Newville方法論文書）/ 未同定（特定論文への直接充填）
* **注記**: RI-08の「single-run operando」パターン（§6、SRG-1+SRG-2の複合）は、個別論文への充填よりも分野標準の更新（IUCrガイドライン改訂、JACS投稿要件の変化）として対処される性質を持つ。2018年→現代の移行でB-1（EXAFS系統誤差）が「modern-era deficient」に移行した事実は、この充填が点（特定論文）ではなく面（分野標準）として起きたことを示す。

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority（SRG-6 Primary；C-1, B-17, B-4：先行MOF-Heck触媒との同一指標比較なし）

* **充填開始点（MOF-Heck触媒の定量的性能比較レビュー）**:
  — Karmakar, A. et al. / または Pascanu, V. et al., Coord. Chem. Rev. / Chem. Soc. Rev.（推定 2019–2022）— MOF担持Pd触媒のHeckおよびSuzuki型反応における性能をTON/TOFで整理した総説。refs ~6, 10, 13, 14に相当する先行研究との数値比較を含む可能性。
  — **Confidence: Low**（この種の総説の存在は高確率で推定されるが、特定著者・誌名・年・対象論文との対応について実文献確認が必要）

* **充填確立点**: **未同定**
  — 本論文のPd@MIL-101-NH₂システムを明示的に他MOF-Heck触媒と同一指標（TOF h⁻¹, surface Pd当たりTOF）で比較した独立論文は同定されていない。

* **充填の性質**: Indirect（レビュー論文内での間接的ベンチマーク整理として部分充填の可能性）
* **Confidence**: Low
* **注記**: RI-09の充填は個別研究論文よりもレビュー・総説によって達成されやすいパターン（RI-09のデフォルト傾向は第二群）。C-1「引用しながら同一指標で比較しない」問題は、後続の独立グループが比較表を含む総説を書く際に自然に解消されるが、その充填の検出には系統的文献調査が必要。

---

### §C 推奨選定リスト

*注記：EP-03a, EP-04a（部分）, EP-08a（対象特定分）, EP-09aについて、High/Medium confidenceの充填論文を5–7報確保できなかった。本プロトコルの方針（Low confidence論文は推奨選定リストに原則不含）に従い、確認済みの4報を推奨リストとして掲載し、残余EPについては系統的文献調査を推奨する。*

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Amatore & Jutand, Organometallics / J. Organomet. Chem. 1988–1993（速度論的系列論文） | EP-06a（開始点） | VQ-3 | 1988–1993 | High |
| 2 | Jutand, A., Chem. Rev. 2008, 108, 2300 | EP-06a（確立点） | VQ-3 | 2008 | High |
| 3 | Ravel & Newville, J. Synchrotron Radiat. 2005, 12, 537 | EP-08a（間接・方法論） | VQ-4 | 2005 | High |
| 4 | Newton et al. (het2), ACS Catal. 2024 | EP-04a（era-norm比較基準） | VQ-3 | 2024 | Medium |

**選定理由：**

確認可能な4報のうち、EP-06a（VQ-3要件、RI-06）はAmatore/Jutand系列論文によって均一系レベルで実質的に充填されており、1988–1993年の速度論論文群が充填開始点、2008年Chem. Rev.が体系的整理による充填確立点として機能する。EP-08a（VQ-4要件、RI-08）はRavel & Newville JSR 2005によって方法論的に間接充填されるが、特定データへの直接充填ではない。Newton et al. 2024（het2）は、EP-04aについてこの論文と同世代の現代水準operando XAS研究として、ブランク実験・再現実験の実施状況を参照比較するための基準論文として選定する。

**重大な充填空白：** VQ-3のFatalブロッカーであるEP-03a（RI-03；Pd(0)活性種の直接検出）の充填論文をHigh/Medium confidenceで同定できなかった。この空白はVQ-3達成の障壁が2026年現在も実質的に残存することを示唆し、§Eで発見的意義として記録する。EP-09aも同様であり、MOF-Heck触媒の定量ベンチマーク整理レビューについて系統的文献調査を推奨する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-3 要件（均一系陽イオン機構の速度論的確立）**: EP-06a → 1988–2008年 Amatore/Jutand 【技術駆動充填：電気化学的手法の有機金属触媒への適用；分野横断充填：電気化学→有機金属化学】
- **VQ-4 要件（EXAFS解析の方法論的標準化）**: EP-08a → 2005年 Ravel & Newville 【技術駆動充填：XAFSソフトウェア整備による方法論確立】
- **VQ-3 要件（ブランクXAS + 再現実験の分野標準化）**: EP-04a → 2024年時点で間接充填のみ（Newton et al.が現在の比較基準）【未充填（分野慣行として部分解消の途上）】
- **VQ-3 要件（Pd(0)活性種の直接検出）**: EP-03a → 未充填（2018–2026年、充填論文未同定）【未充填】
- **VQ-4 要件（外部TON/TOFベンチマーク比較）**: EP-09a → 未同定（レビュー論文として間接充填の可能性）【充填検証待ち】

**階層-時間対応の評価：**

同定できた充填の範囲内では、階層-時間仮説は部分的にのみ支持される。VQ-3要件のEP-06a充填（均一系機構確立）は1988–2008年に達成されたが、これはVQ-4要件のEP-08a方法論標準化（2005年）とほぼ同時代であり、VQ階層の上昇が単純に充填遅延と対応するという仮説を完全には支持しない。より本質的なVQ-3要件（EP-03a：Pd(0)の直接検出）が2026年時点で未充填であることは、「より直接的な機構証拠を要求するVQ-3要件ほど充填困難・遅延する」という修正版仮説を支持する。VQ-4要件（EP-08a, EP-09a）の「面的」充填（特定論文ではなく分野標準・レビューとして）は、VQ階層が上がるほど充填形式が点（個別論文）から面（分野慣行の変化）に移行するという構造を示唆する。

**特筆すべきパターン：**

- **技術駆動充填（EP-06a）**: 陽イオン/中性経路の識別はCyclic Voltammetryの有機金属触媒への適用（Amatore/Jutand）によって達成された。分析手法の革新が機構論文献の充填を主導した典型的パターン。
- **未充填（EP-03a）**: 2018年から2026年まで8年を経てもPd@MOF-Heck系でのPd(0)活性種直接検出充填論文を同定できない。技術的困難（Pd(0)の短命性と現行XASの時間分解能の不整合）と分野慣行（「短命Pd(0)は観測不能」という暗黙的受容）の複合が原因と推定される。
- **面的充填（EP-08a）**: EXAFS不確かさ報告の問題は特定論文への充填ではなく、分野標準（JACS投稿要件、IUCrガイドライン）の進化として対処された。この「面的充填」パターンはRI-08に固有の充填様式として記録価値がある。
- **自己充填の可能性（EP-03a, EP-04a）**: S0-6の「under investigation」留保が自己充填を強く示唆。実現した場合の原論文→後続論文の年数（推定2–5年）がVQ-2→VQ-3遷移の典型的コストを表す。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

**EP-03a Direct-observation/state-assignment pack:**

* **未充填の理由**: 技術的困難 + 分野慣行の複合
  — モノマーPd(0)中間体の寿命がoperando XASの時間分解能（現行3.4分/スキャン）と不整合であり、検出窓外に存在するという技術的困難がある。並行して、「Pd(0)は短命で即座に再酸化される」という合理化がPd触媒文献全体で暗黙的に受容されており、活性種の直接XAS観測を独立論文の主題として追求する分野的動機が構造的に弱い。

* **発見的意義**: あり。「Pd(0)活性種の直接観測証拠なしにMOF-Heck機構を主張し続けるパターン」が2018年以降少なくとも8年間継続していることは、operando XAS論文におけるRI-03の系統的発現として記録価値がある。§6で提案した「観測法の原理的限界と活性種帰属の論理的分離」という下位パターン（quick-XASによる上限設定を標準解決戦略とする）が、この空白を埋めうるEP辞書への追加候補として有効である。

* **将来の充填可能性**: 中。quick-XANES（~5 s/スキャン）はESRF/SOLEIL/SPring-8で現行技術として実現可能であり、次世代の時間分解operando XAS論文がこのギャップを充填する可能性がある。ただし対象系（Pd@MIL-101-NH₂）への具体的適用には再度のシンクロトロンビームタイムが必要。

---

**EP-04a Discrimination/replication pack（部分的未充填）:**

* **未充填の理由**: 分野慣行
  — シンクロトロンビームタイムの希少性と「単一ランの先行結果で機構的結論に十分」という分野的判断により、ブランクXAS実験と再現オペランドランの標準慣行化が2024年時点でも完了していない可能性がある。Newton et al. 2024 (het2)での同種省略の記録は、この慣行の持続を示唆する。

* **発見的意義**: あり（限定的）。UQSがheterogeneousタイプ論文（het1, het2）で同パターン（SRG-2：単一ランのoperando XAS）を繰り返し検出する場合、「operando XAS分野が再現実験の標準化を系統的に遅延させてきたパターン」として記録できる。het2の詳細検証によって発見的意義の強度が決まる。

* **将来の充填可能性**: 高。ブランク実験と再現ランの実施は技術的困難がなく、JACS等の主要誌の投稿要件変化（審査方針の更新）によって充填が促進される可能性が高い。

---

**EP-09a Internal benchmark pack（部分的未充填）:**

* **未充填の理由**: 報告形式問題 + 関心の欠如
  — 先行MOF-Heck触媒研究（refs ~6, 10, 13, 14）自体が同一指標（TOF h⁻¹）を一貫して報告していない場合、異なる条件間での比較表作成が困難になる。また「変換率（%）で十分」という分野慣行が、TOF規格化への動機を弱めてきた可能性がある。

* **発見的意義**: 限定的。RI-09の「引用しながら同一指標で比較しない」パターンは本ケース固有ではなく触媒論文全般に広く見られる慣行であるため、UQSの固有発見としての意義は中程度にとどまる。

* **将来の充填可能性**: 高。TOF計算はGCデータから追加実験なしに可能であり、後続論文またはレビューによる充填が最も現実的な経路。

---

**EP-08a Replication/uncertainty pack（対象特定の充填なし）:**

* **未充填の理由**: 報告形式問題（面的対処）
  — この特定論文のEXAFSデータへの再解析論文という形での充填は、学術的動機が弱く独立論文として発表される性質ではない。方法論標準の変化（IUCr, JACS投稿要件）という「面的充填」として対処されており、点（特定論文）への直接充填が存在しないことは構造的に予測可能。

* **発見的意義**: あり（制度設計への寄与として記録済み）。§6で提案した「single-run operando」下位パターン（SRG-1+SRG-2複合によりEXAFS系統誤差と反復不在が互いを補強する構造）は、RI-08の新下位分類として記録価値があり、これが「面的充填」パターンの典型事例を提供する。

* **将来の充填可能性**: 低（特定論文への直接充填として）。高（分野標準向上による類似論文への間接的解消として）。
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
