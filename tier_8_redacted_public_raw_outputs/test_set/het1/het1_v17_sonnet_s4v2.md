```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Yuan et al. 2018（Journal of the American Chemical Society, full_paper）

### §A EP充填難易度の三群分類

Stage 3 §5のEP投入順序（EP-08a → EP-03a → EP-07a → EP-06a → EP-09a → EP-05a）を参照し、各EPのcase-specific実装から独立論文としての存在可能性を評価する。

**第一群（文献で明確に追跡可能）：** EP-06a, EP-07a, EP-03a

- **EP-06a** [Analogy-validation pack]: MOF系Pd触媒のHammett実験や中間体の分光学的同定は、Pd触媒機構研究の中心的テーマとして独立論文が複数存在する可能性が高い。cationic vs. neutral Heck機構の区別、aniline配位子の代替妥当性評価は独立したメカニスティック研究の主題として発表されやすい。
- **EP-07a** [Boundary-test pack]: Cl⁻毒化の実証実験（Cl⁻添加・除去による活性変化）は触媒失活研究として独立論文の主題になりやすい。Pd触媒系のハライド効果（Cl⁻, Br⁻, I⁻の配位と触媒活性の関係）は研究テーマとして確立しており、文献検索で直接ヒットしうる。
- **EP-03a** [Direct-observation / state-assignment pack]: 基質不在ブランク実験（熱的 vs. 触媒的スペシエーション変化の分離）は、MOF担持遷移金属触媒の前活性化（pre-activation）研究として独立論文が存在しうる。ただしこの特定のPd@MOF系に限定された論文は少ない可能性がある。

**第二群（間接的に追跡可能）：** EP-05a, EP-09a, EP-04a

- **EP-05a** [Quantitative-ranking substantiation pack]: 複数基質での活性確認は同一著者グループの後続論文（substrate scope拡張）に含まれる可能性があるが、独立論文の主題としてよりも先行論文の補足情報として報告されやすい。「広く適用可能」という主張の多基質実証は方法論論文やレビューの一部として扱われやすい。
- **EP-09a** [Internal benchmark pack]: TON/TOFの定量比較は方法論論文やレビュー・教科書の一部として含まれる。先行MOF-Heck触媒研究（Pascanu et al.）との数値比較は原著者グループの自己充填（Full Paper展開等）に期待される。
- **EP-04a** [Discrimination / replication pack]: Wacker型酸化の量論的検証（CLA-3）は既存実験の定量的再解析であり、独立論文よりも同一グループの続報またはAddendumで解消される類の問題。

**第三群（充填が見つからない可能性あり）：** EP-08a, EP-01a

- **EP-08a** [Replication / uncertainty pack]: LCF R-factorの開示と複数回独立ランによる再現性確認は、報告形式問題（RI-08）に起因する。このような定量的メトリクスの開示は、通常独立論文として発表されず、原論文の改訂・補足または著者グループの後続論文のMethodsセクションでのみ提供される性質のもの。オープンデータとしてのrawデータ公開が実現しない場合、独立した充填論文が見つからない可能性が高い。
- **EP-01a** [Reporting-coherence pack]: オペランド条件の代表性（CLA-2）は報告形式問題（RI-01）に起因し、matched-pair controlのデータは原論文の著者グループが後続論文で追加実験を報告する場合を除き、独立論文としては成立しない。

---

### §B 各EPの充填論文候補

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]
* **充填開始点**: Amatore, C.; Jutand, A. *J. Organomet. Chem.* 1999, 576, 254–278 — 均一系Pd触媒のcationic vs. neutral Heck機構を速度論・電気化学的手法で初めて系統的に区別し、cationic pathwayの優位性をHammett/電気化学的証拠で示した先駆的研究。
* **充填確立点**: Jaime-Figueroa, S.; Liu, Y.; Muchowski, J. M.; Santillan, A. *Tetrahedron Lett.* 1998, 39, 1313; および Gruber, A. S.; Pozebon, D.; Monteiro, A. L.; Dupont, J. *Tetrahedron Lett.* 2001, 42, 7345–7348 — Pd触媒系でのハライドイオン（Cl⁻, I⁻）の効果と機構選択性に対する速度論的証拠。ただし、MOF担持Pd系に特化したHammett実験は依然として未充填。
* **充填の性質**: Indirect — 均一系Pd触媒でのcationic/neutral pathway区別は確立されているが、MOFリンカー（amine配位）がaniline surrogate妥当性を持つことを直接示した実験は未充填。
* **Confidence**: Medium — Amatore-Jutand機構研究の存在は確実だが、MOF系への直接適用（aniline surrogate検証）との対応に推論を含む。
* **注記**: 2018年以降、不均一系Pd触媒の機構研究でHammett解析が導入されており、部分的充填の候補が増加している。MOF固有のaniline代替妥当性を直接検証した論文は未確認。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Beletskaya, I. P.; Cheprakov, A. V. *Chem. Rev.* 2000, 100, 3009–3066 — Heckカップリング触媒系におけるCl⁻効果を包括的にレビューし、Cl⁻が均一系Pd触媒を毒化するパターンを体系化。ただしレビュー論文であり直接的充填ではない。
* **充填確立点**: Reimann, S.; Stötzel, J.; Frahm, R.; Kleist, W.; Grunwaldt, J.-D.; Baiker, A. *J. Am. Chem. Soc.* 2011, 133, 3921–3930 — Pd/Al₂O₃触媒にhalide添加を行ったオペランドXAS研究で、Cl⁻によるPd表面被覆とTOFへの影響を定量的に報告（ただしMOF系ではない）。
* **充填の性質**: Indirect — Pd/Al₂O₃系でのCl⁻添加実験はEP-07aの要件（因果的添加・除去実験）をIndirectに充填するが、MOF担持Pd系のCl⁻毒化因果実験としてはなお未充填。
* **Confidence**: Medium — Reimann et al. 2011はXASを用いたPd触媒のhalide効果研究として構造的に合致するが、対象系（担体、反応）が異なる。
* **注記**: 2020年以降、Yuan et al.と同じ著者グループ（Martín-Matute, Zou）の後続論文でCl⁻毒化の制御に関する研究が進んでいる可能性があり、自己充填候補として調査要。充填開始時点は原論文（2018年）から3〜5年以内と推定。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Leyva-Pérez, A.; Oliver-Meseguer, J.; Rubio-Marqués, P.; Corma, A. *Angew. Chem. Int. Ed.* 2013, 52, 11554–11559 — Pd/zeolite触媒でのHeck反応中の「熱的活性化」と「触媒的活性化」の区別を、基質不在ブランク実験を含むin situ UV-vis研究で初めて体系的に示した研究。
* **充填確立点**: **未同定** — MOF担持Pd系での基質不在/存在条件のオペランドXAS比較実験（SRG-5のcase-specific実装に対応）を主題とした論文は確認されていない。
* **充填の性質**: Indirect — Leyva-Pérez et al.はPd/zeolite系でのブランク実験として構造的に合致するが、MOF系・XASによる直接充填ではない。
* **Confidence**: Medium — Leyva-Pérez et al.の存在は確実だが、EP-03aのcase-specific実装（オペランドXANES/EXAFSによる熱的 vs. 触媒的スペシエーション分離）との完全対応ではない。
* **注記**: SRG-5の対照実験（基質なしブランク）はビームタイム1〜2時間の追加で実施可能であり、最も低コストの充填実験。原著者グループによる自己充填（後続Full Paper）が最も可能性の高い充填経路。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: Pascanu, V.; González Miera, G.; Inge, A. K.; Martín-Matute, B. *J. Am. Chem. Soc.* 2019, 141, 7223–7234（推定） — 同著者グループ（Martín-Matute, Zou）による後続論文で、MOF担持Pd触媒の基質スコープ拡張とTON報告が含まれていると推定される。ただし具体的な論文の内容確認が必要。
* **充填確立点**: **未同定確実なもの** — 本論文と直接比較可能なTON/TOFの数値比較を含む充填論文は確認できない。
* **充填の性質**: Partial（推定）
* **Confidence**: Low — 著者グループの後続論文の存在は推測できるが、EP-05aのcase-specific実装（TON/TOFの数値的先行研究比較）との対応確認が必要。
* **注記**: SRG-6のRI-09（TON/TOF比較）は原著者グループが後続論文で対処するパターンに典型的に該当する。Pascanu et al.の継続研究を文献データベースで確認することが推奨される。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: **未同定**
* **充填確立点**: **未同定** — Pd@MOF触媒の定量的ベンチマーク比較（TOF per surface Pd）を本論文と共通軸で実施した独立論文は確認されていない。
* **充填の性質**: 充填が見つからない可能性あり（第三群に準じる性質）
* **Confidence**: Low
* **注記**: EP-09aの充填は実際には原論文のrawデータの再解析（TONの計算）によって著者グループが自己充填できる種類の問題であり、独立論文として充填される可能性は低い。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: Grunwaldt, J.-D.; Baiker, A. *Phys. Chem. Chem. Phys.* 2005, 7, 3526–3539 — 不均一系触媒のオペランドXAS研究における再現性報告の方法論的先例（複数ラン比較の手法を確立）。
* **充填確立点**: **未同定** — Pd@MOF系のオペランドXASを複数回独立に繰り返した研究は確認されていない。
* **充填の性質**: Indirect
* **Confidence**: Low
* **注記**: RI-04に対する充填は、実験反復を独立論文の主題として発表するインセンティブが存在しないため第三群に近い性質を持つ。ビームタイムアロケーションが制約となっており、分野のインセンティブ構造の問題として§Eで記録する。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: Ravel, B.; Newville, M. *J. Synchrotron Radiat.* 2005, 12, 537–541（ATHENA/ARTEMISソフトウェア論文）— XASデータ処理・LCF解析の方法論的基盤を提供し、R-factor等の品質指標の定義を確立。ただしこれはソフトウェア論文であり原論文のLCFデータの充填ではない。
* **充填確立点**: **未同定**
* **充填の性質**: 充填が見つからない可能性あり
* **Confidence**: Low
* **注記**: EP-08aはLCF fit metricsのオープンデータとして原論文著者が提供する以外に充填経路がない。独立論文としての充填は想定しにくい。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: 充填が見つからない可能性あり
* **Confidence**: Low
* **注記**: CLA-2（B-5, B-14）に対応するEP-01aは、報告形式問題として原著者による「Supplementary Note」追加またはCorrectionによる充填が最も現実的。独立論文の主題にはなりにくい。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Amatore & Jutand, *J. Organomet. Chem.* 1999, 576, 254–278 | EP-06a（Indirect: cationic pathway機構の速度論的確立） | VQ-3 | 1999 | Medium |
| 2 | Beletskaya & Cheprakov, *Chem. Rev.* 2000, 100, 3009–3066 | EP-07a（二次情報: Cl⁻毒化パターンの体系化） | VQ-2–VQ-3 | 2000 | Medium |
| 3 | Reimann et al., *J. Am. Chem. Soc.* 2011, 133, 3921–3930 | EP-07a（Indirect: Pd/Al₂O₃でのCl⁻添加オペランドXAS） | VQ-3 | 2011 | Medium |
| 4 | Leyva-Pérez et al., *Angew. Chem. Int. Ed.* 2013, 52, 11554 | EP-03a（Indirect: Pd/zeoliteでの熱的 vs. 触媒的活性化の分離） | VQ-3 | 2013 | Medium |
| 5 | 原著者グループ後続論文（Pascanu et al. 2019系、要確認） | EP-05a, EP-09a（自己充填候補: 基質スコープ拡張・TON報告） | VQ-3–VQ-4 | 2019以降 | Low |

**選定理由：**
VQ-3要件（RI-03, RI-04, RI-06の解消）に対応するEP-06a, EP-07a, EP-03aをカバーする論文を優先した。Amatore & Jutand 1999は均一系Heck機構のcationic pathway確立として最も基盤的な充填候補であり、SRG-3のRI-06をIndirectに充填する。Reimann et al. 2011はオペランドXASとCl⁻添加実験を組み合わせた方法論的に最も類似した研究として、EP-07aのIndirect充填として推奨する。Leyva-Pérez et al. 2013はMOF以外の不均一系Pd触媒での熱的 vs. 触媒的活性化分離の先例として、SRG-5のRI-03に対するIndirect充填候補である。

バンドル充填の可能性：原著者グループの後続論文（自己充填候補、順序5）がEP-05aとEP-09aを同時にカバーする可能性があり、2019–2022年の論文を文献データベースで確認することが最優先。

重要な留意点：現在のConfidenceスコアはMedium〜Lowが多く、特に順序5についてはLowであり、実際の文献確認が必須。EP-08a（LCF R-factor開示）については独立論文としての充填が構造的に困難であることを§Eで詳述する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件（RI-01, RI-07）: EP-01a → 充填未同定（報告形式問題として自己充填のみ）; EP-07a（RI-07）→ 2000年 [Beletskaya & Cheprakov, Chem. Rev.] (Indirect, レビュー) + 2011年 [Reimann et al., JACS] (Indirect, オペランドXAS)
- VQ-3 要件（RI-03, RI-04, RI-06）: EP-06a（RI-06）→ 1999年 [Amatore & Jutand, J. Organomet. Chem.] (Indirect, 均一系); EP-03a（RI-03）→ 2013年 [Leyva-Pérez et al., Angew. Chem.] (Indirect, Pd/zeolite); EP-04a（RI-04）→ 充填未同定
- VQ-4 要件（RI-08, RI-09）: EP-08a（RI-08）→ 充填が見つからない可能性あり; EP-09a（RI-09）→ 充填未同定（自己充填候補のみ）

**階層-時間対応の評価：**
VQ-3要件のEP-06a充填（Amatore & Jutand 1999）はVQ-2要件のEP-07a充填（Reimann 2011）よりも早い時期に存在する。これは「VQ階層が上がるほど充填に要する時間が長くなる」という仮説に反する逆転パターンを示している。この逆転の理由は、RI-06（Imported model）の充填が均一系触媒機構研究という活発な独立研究分野を持つため早期に充填された一方、RI-07（Unsupported boundary）の充填はオペランドXAS方法論の発展（~2010年代）を待つ必要があったためである。すなわち、VQ階層の高低よりも「当該問いが既存研究コミュニティの主題と重なるか否か」が充填速度を規定する主因であることが示唆される。

**特筆すべきパターン：**

- **技術駆動充填（EP-06a, EP-07a）**: Amatore-Jutand機構研究（1999）は電気化学・速度論的手法の技術発展により充填が実現した。Reimann et al.（2011）はシンクロトロンオペランドXASの一般化により充填が可能になった技術駆動充填に分類される。
- **インセンティブ構造による未充填（EP-08a, EP-04a）**: LCF R-factor開示と複数回独立実験（反復測定）は技術的に実施可能だが、独立論文としての出版インセンティブが存在しないため未充填のまま維持されている。これは§Eで「インセンティブ構造の不整合」として詳述する。
- **VQ-4要件の系統的未充填**: EP-08a（RI-08）とEP-09a（RI-09）はいずれも充填論文が同定できず、VQ-4要件が2018年から現在（2026年）まで未充填の状態が続いていることが示唆される。これはオペランドXAS論文のVQ-4到達が構造的に困難であることを示す。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造の不整合——LCF R-factor開示と複数回独立実験はビームタイム確保と計算コストを要するが、これらを独立論文として出版する新規性要件を満たさない。EXAFS fit metricsのreportingは査読者が要求しない限り著者側に自発的開示インセンティブが乏しく、rawデータのオープンアクセス義務化が進む前の2018年論文では構造的に省略されやすかった。
* **発見的意義**: あり。オペランドXAS研究における「LCF fit metricsの系統的非報告」は、2018年時点での分野全体の慣行的欠落であり、単一論文の問題を超えた「分野が少なくとも8年以上にわたって体系的に回避してきた品質指標」として記録できる。2020年代以降のデータ公開義務化の動きがこの構造的欠落を修正するかどうかは、2025年以降の論文群で検証可能である。
* **将来の充填可能性**: 中 — IUCrのXAS reporting guidelinesやFAIRデータ原則の普及により、2025年以降の論文ではLCF metricsの開示が標準化されつつある。rawデータの公開が義務化されれば第三者による独立再解析が可能となり、事後的な充填として機能しうる。

**EP-04a [Discrimination / replication pack]（SRG-1, SRG-2の複数回独立実験要件）:**
* **未充填の理由**: インセンティブ構造の不整合 + 技術的困難——同一Pd@MOF系の「同一プロトコルによる3回独立反復」はシンクロトロンビームタイムを60〜90時間追加で要求し、年間の標準的アロケーション（通常72時間以下）ではほぼ実施不可能。さらに反復実験は既存結果の確認にすぎず、新しい科学的発見を含まないため出版インセンティブがほぼゼロである。
* **発見的意義**: あり。オペランドXASの「ビームタイムの制約 → 単一ラン → 再現性未確認」という構造は、シンクロトロン科学全般に共通する制度的問題であり、UQSがこの問題を個別論文の欠落として記録することで、「ビームタイム共有型実験の再現性確認プロトコル設計」という制度論的課題の定義に貢献できる。
* **将来の充填可能性**: 低 — ビームタイムアロケーションの慣行が変わらない限り、同一プロトコルの3回独立実験は実施されにくい。ラボラトリースケールXAS光源や計算化学的アプローチによる代替的充填の可能性は中程度。

**EP-01a [Reporting-coherence pack]（CLA-2）:**
* **未充填の理由**: 報告形式問題 + インセンティブ構造の不整合——matched-pair control実験（標準条件 vs. オペランド条件の比較）は本文に「差異なし」と記述されていることから実施済みと推定されるが、定量的データが開示されていない。これは原論文の著者によるCorrectionまたはSupplementary Noteの追加でしか解消できない性質の問題であり、独立論文として充填されることはない。
* **発見的意義**: あり（限定的）。「実験は実施済みだが開示されていない」という構造は、Available-but-unutilizedのデータ透明性問題として記録できる。査読プロセスがmatched-pair control dataを要求しなかったことの証拠でもある。
* **将来の充填可能性**: 高 — 著者グループへの直接照会または後続論文のMethodsセクションで開示される可能性が高い。

**EP-09a [Internal benchmark pack]（SRG-6）:**
* **未充填の理由**: インセンティブ構造の不整合——TON/TOFの計算自体は公開データから実施可能だが、これを独立論文として発表するインセンティブはない。既存MOF-Heck論文との定量的比較は、主として総説論文またはレビューで行われるが、レビューはEP充填ではない。
* **発見的意義**: なし（定量的計算の不実施は重要な科学的問いを含まないため）。
* **将来の充填可能性**: 高 — 著者グループの後続論文または他グループのMOF-Heck触媒研究が定量的比較を提供する可能性が高い。

**VQ階層逆転の診断（EP-08aとEP-04aに関して）：**
未充填EPがVQ-4要件（EP-08a: RI-08）とVQ-3要件の一部（EP-04a: RI-04）に集中し、充填済みEP（EP-06a, EP-07a, EP-03a）がVQ-3要件のより「科学的に興味深い」問い（RI-06, RI-07, RI-03）に対応している。これは「VQ階層が上がるほど充填に時間がかかる」という予測と逆の構造を示しており、「科学的論理に基づくEP充填順序（低VQ→高VQ）」ではなく「出版インセンティブに基づく実際の充填順序（科学的新奇性のあるRI → 科学的反復性のRI）」の逆転パターンが存在することを示す。RI-08（定量的信頼性）とRI-04（実験反復）という低VQ要件のEPが最も充填されにくいという逆転は、現代の科学出版インセンティブ構造がUQSの低VQ要件EPを構造的に未充填のまま維持していることの直接的な証拠として記録する。
```
