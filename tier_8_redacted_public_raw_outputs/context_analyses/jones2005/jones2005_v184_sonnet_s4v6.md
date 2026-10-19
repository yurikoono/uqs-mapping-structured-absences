prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Jones et al. 2005（Chem. Commun. 2005, Communication, DOI: 10.1039/b504996b）

### §A EP充填難易度の三群分類

**C23トリガー評価**: jones2005はChemComm通信論文（Letter形式）→ C23（Letter→Full Paper auto-resolution）が発火する。Vicic研究グループが "further investigations are ongoing" を明言しているため、Full Paper続報の存在が期待される。

**第一群（文献で明確に追跡可能）：** EP-10a, EP-03a

- **EP-10a [Kinetic verification pack]**: Ni触媒アルキル–アルキルカップリングのラジカル機構探索（ラジカルクロック・TEMPO捕捉・EPR）は、2008–2015年にかけて複数の研究グループが独立した主題として論文化している。Breitenfeld/Hu group（JACS 2013）はこの EP を直接充填する代表論文。
- **EP-03a [Direct-observation / state-assignment pack]**: Ni(I)/Ni(III)酸化状態のin situ EPR観測はNi-アルキル触媒機構研究の標準アプローチとして独立論文化されており、検索可能。

**第二群（間接的に追跡可能）：** EP-02a, EP-06a, EP-05a

- **EP-02a [Identity / purity substantiation pack]**: jones2005がChemComm通信であることから、Letter→Full Paper auto-resolution（C23）が適用される。Vicic研究グループのFull Paper続報が1–3年以内に存在する可能性が高く、より完全な錯体キャラクタリゼーション（1bのXRD等）が含まれると予想される。
- **EP-06a [Analogy-validation pack]**: Grignard→亜鉛求核剤間の機構的類推（ref 12の同型性）を検証した実験は、類似系Ni触媒の比較論文として間接的に追跡可能だが、対象系（tpy'/Zn）に特化した論文の存在は限定的。
- **EP-05a [Quantitative-ranking substantiation pack]**: tpy配位子の電子効果vs溶解性寄与の分離実験は、Vicic研究グループのFull Paperまたは配位子最適化論文に間接的に含まれる可能性がある。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a, EP-09a, EP-04a

- **EP-01a [Reporting-coherence pack]**: 式(3)のマスバランス閉鎖は、Full Paper展開で部分的に解消される可能性があるが、化学量論的実験の炭素バランス（特に62%未帰属部分）を独立論文の主題として充填するインセンティブは低い。インセンティブ構造的未充填候補。C23による自動解消（Full Paper）で部分充填される場合は第二群昇格。
- **EP-08a [Replication / uncertainty pack]**: GC収率の反復測定・統計評価は、独立論文化のインセンティブが存在しない典型的なインセンティブ構造的未充填パターン。
- **EP-09a [Internal benchmark pack]**: 先行Ni-アルキル系（refs 5-11）との直接比較は、競合研究グループが自系の優位性を示す比較論文に含まれる可能性があるが、jones2005のtpy'系を対象とした直接比較論文は見つからない可能性がある。
- **EP-04a [Discrimination / replication pack]**: 2aの単結晶代表性（PXRD確認）はFull Paperで自動解消可能だが、独立論文の主題にはならない。

---

### §B 各EPの充填論文候補

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（ラジカルvs内圏機構）、RI-04 [Unreplicated discriminator]（単一stoichiometric discriminator）、PRI-11
* **充填開始点**: Jones, G. D.; Martin, J. L.; McFarland, C.; Allen, O. R.; Hall, R. E.; Haley, A. D.; Brandon, R. J.; Konovalova, T.; Desrochers, P. J.; Pulay, P.; Vicic, D. A. *J. Am. Chem. Soc.* 2006, 128, 13175–13183 — Vicic研究グループによるFull Paper続報。EPR分光法によるNi(I)中間体の直接観測と、より詳細な機構的実験を含む可能性が高い。
  - auto_resolution_type: "Letter→Full Paper"
  - expected_resolution_window: "1 yr"
  - auto_resolution_status: "occurred" (if confirmed)
  - filling_timescale_category: "format-driven"
* **充填確立点**: Breitenfeld, J.; Ruiz, J.; Wodrich, M. D.; Hu, X. *J. Am. Chem. Soc.* 2013, 135, 12004–12012 — Ni(I)/Ni(III)アルキル-アルキルカップリングのラジカル機構をラジカルクロック基質と EPR で直接実証。radical clock（アリルクロック）実験により、アルキルラジカル中間体の生成を実証。tpy系ではなくビスホスフィン-Ni系での結果だが、Ni(I)/Ni(III)ラジカル機構という枠組みを確立した点で間接充填（EP充填の性質: Indirect）。
* **充填の性質**: Partial (Vicic JACS 2006) / Indirect-Complete (Breitenfeld 2013 for Ni(I)/Ni(III) radical mechanism)
* **Bibliographic confidence**: Vicic JACS 2006: Medium（Full Paper続報の存在と年代は高信頼だが、著者リストと正確な巻号は推測を含む）; Breitenfeld 2013: High（著者・巻号・DOIが特定可能）
* **Filling adequacy confidence**: Vicic JACS 2006: Medium（EPR/ラジカルプローブを含むかは不確実）; Breitenfeld 2013: High（Ni(I)/Ni(III)ラジカル機構の確立という点で EP-10a 要件に合致）
* **Verification recommendation**: [必須]（Vicic JACS 2006はBibliographic confidence Medium; Breitenfeld 2013: DOI確認推奨）
* **DOI**: Breitenfeld 2013: 10.1021/ja405712h（High conf）; Vicic 2006: 推測 10.1021/ja063334i（要確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (Vicic 2006, 1 yr); incentive-aligned (Breitenfeld 2013, 8 yr)
* **注記**: Breitenfeld 2013はビスホスフィン-Ni/Grignard系の結果であり、tpy'/Zn系への直接適用性は間接的。tpy'系での definitive ラジカルプローブ実験は未同定の可能性あり。EP-03aと充填論文をバンドルする可能性がある。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（on-cycle status, active species identity）
* **充填開始点**: Jones, G. D. et al., Vicic, D. A. *J. Am. Chem. Soc.* 2006, 128, 13175 — Full Paper続報でEPR分光法によるNi(I)中間体の直接観測を含む可能性。
  - auto_resolution_type: "Letter→Full Paper"
  - expected_resolution_window: "1 yr"
  - filling_timescale_category: "format-driven"
* **充填確立点**: Zhong, M.; Pannecoucke, X.; Jubault, P.; Poisson, T. 等によるNi触媒アルキルカップリングのEPR機構研究論文群（2012–2018年代のNi(I)/Ni(III)サイクルのin situ EPR確立）— 総体的にRI-03（on-cycle status）を充填したが、tpy'系に特化した論文は限定的。
* **充填の性質**: Partial（Vicic Full Paper, if EPR data included）/ Indirect（他研究グループのNi-アルキル EPR 研究）
* **Bibliographic confidence**: Vicic 2006: Medium; 他EPR研究: Low-Medium（特定論文名が推測を含む）
* **Filling adequacy confidence**: Vicic 2006: Medium; 他EPR研究: Low（tpy'系への適用限定）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (Vicic 2006); field-methodology (Ni EPR field adoption, 2010s)
* **注記**: Ni触媒反応中のNi(I) in situEPR観測はHu研究グループが最も系統的に実施した（Hu, X. Chem. Sci. 2011 Review等）。tpy'配位子を持つNi(I)の触媒条件下in situ EPRの具体的論文は確認が必要。

---

**EP-06a [Analogy-validation pack]（第二群）**

* **充填するRI**: RI-06 [Imported model]（Grignard/tpy系 ref 12 → Zn/tpy'系への機構的類推）
* **充填開始点（暫定）**: Kitiachvili, K. D.; Mindiola, D. J.; Hillhouse, G. L. 等のNi-アルキル機構論文群、またはVicic研究グループのtpy/tpy' Ni系の亜鉛求核剤比較論文（2006–2010年代）。
* **充填確立点**: 未同定。Grignard→Zn求核剤間での機構的類推（ラジカル vs 非ラジカル経路）の等価性を tpy'系で直接実証した論文は、独立した主題として存在しない可能性がある。
* **充填の性質**: Indirect / 未確認
* **Bibliographic confidence**: Low（具体的な充填論文の同定は推測ベース）
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]（Low confidence候補のみ）
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned（もし充填されるなら 5–10 yr）
* **注記**: このEPは「Ni/Grignard系機構実験の結果がNi/Zn系に転用できるか」という問いに対応する。後続の研究でNi(I)/Ni(III)ラジカル機構が求核剤種によらず成立することが示されれば、間接的な充填となる。Breitenfeld 2013（Grignard/Ni-bisphosphine系のラジカル機構）がPartial-Indirectの充填候補。

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Object identification]（1b XRD不在、2a合成收率未記載）
* **充填開始点**: Jones, G. D.; Martin, J. L.; McFarland, C.; Allen, O. R.; Hall, R. E.; Haley, A. D.; Brandon, R. J.; Konovalova, T.; Desrochers, P. J.; Pulay, P.; Vicic, D. A. *J. Am. Chem. Soc.* 2006, 128, 13175–13183 — Letter→Full Paper自動解消。1bのXRD構造、2aの合成収率・PXRD確認、および完全な電気化学データが含まれると期待される。
  - auto_resolution_type: "Letter→Full Paper"
  - expected_resolution_window: "1 yr"
  - auto_resolution_status: "occurred" (if confirmed)
  - filling_timescale_category: "format-driven"
* **充填確立点**: 同上（Full Paper展開が一次充填確立点）
* **充填の性質**: Complete（Full Paper展開で達成されると期待）
* **Bibliographic confidence**: Medium（Full Paper続報の存在は高確率で期待できるが、著者リスト・巻号・DOIは推測を含む）
* **Filling adequacy confidence**: Medium（Full Paper形式なら通常はXRD + 収率 + PXRD を含む）
* **Verification recommendation**: [必須]（Bibliographic confidence Medium）
* **DOI**: 推測 10.1021/ja063334i（要確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1 yr)
* **注記**: jones2005 が ChemComm 通信であることから、C23（Letter→Full Paper auto-resolution）が最も自然な充填経路。Vicic研究グループが自己充填するパターン。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]（溶解性vs電子効果の定量的分離が未実施）
* **充填開始点（暫定）**: Vicic研究グループによるtpy/tpy'誘導体を用いたNi触媒研究（2006–2012年頃）— 配位子電子パラメータと触媒活性の相関を検討した論文の可能性。または、構造的アナログ（4-置換ビピリジン系等）を用いたNi-アルキルカップリング論文。
* **充填確立点**: 未同定。
* **充填の性質**: Indirect / 未確認
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned（もし充填されるなら 3–10 yr）
* **注記**: 溶解性vs電子効果の分離という実験設計は、Hammett相関、Tolman電子パラメータ（CO/Ni ν値）等の配位子電子効果評価手法を用いれば独立した論文テーマとなりうるが、tpy'系への特化度が不明。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]（式3のマスバランス62%未帰属、GC收率基準不統一）
* **充填の性質**: 第三群（インセンティブ構造的未充填 + Letter→Full Paper auto-resolution可能性）
* **充填論文候補**: Vicic JACS 2006 Full Paperが部分充填の可能性（Full Paperでは完全マスバランス報告が標準化されているため）。しかし「62%未帰属炭素の再実験」を独立論文として出版するインセンティブはない。
* **Bibliographic confidence**: Low-Medium（Full Paper自動解消の可能性はあるが、マスバランスが特別に報告されるかは不確実）
* **注記**: インセンティブ構造的未充填の典型例。Full Paper展開で炭素バランスが記録されれば§Bで第二群昇格。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]（GC収率のn/SD未報告）
* **充填の性質**: 第三群（インセンティブ構造的未充填）
* **充填論文候補**: なし（追試・反復測定を独立論文として出版するインセンティブが存在しない）
* **注記**: Full Paper展開でn=2–3の繰り返しが記録される可能性はあるが、統計的評価としての独立論文化は想定されない。EP-08aは本質的に第三群であり、充填は通信→Full Paper遷移内での部分解消に限定される。

---

**EP-09a [Internal benchmark pack]（第三群）**

* **充填するRI**: RI-09 [External superiority]（refs 5-11 との直接比較なし）
* **充填の性質**: 第三群（インセンティブ構造的未充填候補）
* **充填論文候補（暫定）**: 後続のNi-アルキルカップリング比較論文（Hu、Fu研究グループ等による異なる配位子系の比較論文）が間接的にEP-09aを充填する可能性。ただし、tpy'/Niシステムを特定のref 5-11と同一条件で直接比較した論文は見つからない可能性が高い。
* **Bibliographic confidence**: Low
* **注記**: Success-driven question erasureの可能性あり——よりロバストなNi-アルキルカップリング系（Hu/Fu等のビスホスフィン系）の成功により、tpy'系の詳細な比較研究の需要が消滅した可能性がある。

---

**§B末尾：Bibliographic verification（conditional triggering）**

トリガー条件評価:
- (a) 1980年以前: No（2005年論文）
- (b) 著者ネットワーク密（10+関連論文）: Borderline Yes（Vicic研究グループのNi-アルキルカップリング論文群）
- (c) named reaction: Borderline（Kumada-Corriu型に関連するが、求核剤はZn → 「Negishi型」に近い。「Kumada」の名前は論文タイトルに登場しない）
- (d) Medium-Low confidence候補が2件以上: **Yes**（EP-03a, EP-06a, EP-05a）

→ トリガー(d)が成立 → **全候補にverification recommendation [必須]を付与**

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Jones, G. D. et al., Vicic, D. A., *J. Am. Chem. Soc.* **2006**, 128, 13175 | EP-02a, EP-10a(部), EP-01a(部), EP-03a(部) | VQ-2 | 2006 | Medium | Medium | 必須 ⚠️ |
| 2 | Breitenfeld, J.; Ruiz, J.; Wodrich, M. D.; Hu, X., *J. Am. Chem. Soc.* **2013**, 135, 12004 | EP-10a, EP-03a(間接) | VQ-3 | 2013 | High | High | 必須 |
| 3 | （未同定: tpy'/Ni系でのEPR on-cycle実証論文） | EP-03a | VQ-3 | 2008–2015 | Low | Medium | 必須 ⚠️ pending |
| 4 | （未同定: Vicic群の配位子電子効果論文） | EP-05a, EP-06a(部) | VQ-2 | 2007–2012 | Low | Low | 必須 ⚠️ pending |
| 5 | （未同定: Ni-アルキル/亜鉛系の機構比較論文） | EP-06a | VQ-3 | 2008–2016 | Low | Low | 必須 ⚠️ pending |

**選定理由：**

推奨論文1（Vicic JACS 2006 Full Paper）はLetter→Full Paper自動解消（C23）の核心論文として最優先に位置づける。jones2005の著者グループ自身による自己充填であり、EP-02a（錯体キャラクタリゼーション完全化）、EP-01a（マスバランス、Full Paper形式では報告される可能性）、EP-10a（もし機構的実験が拡張されていれば）を束ねて充填するバンドル充填論文として期待される。ただし、著者リスト・DOI・具体的な内容は Bibliographic verification 待機中（⚠️）。

推奨論文2（Breitenfeld 2013）はNi(I)/Ni(III)アルキル-アルキルカップリングのラジカル機構をラジカルクロック + EPRで確立した点でEP-10aの間接充填として最も信頼性が高い（Bibliographic confidence High）。jones2005の「still cannot be ruled out」という開放的な結論が、8年後にBreitenfeld 2013により収束された科学的発展の典型例。

推奨論文3–5は現時点で未同定（⚠️ verification pending）であり、post-hoc verification後に具体的な論文への更新が必要。

⚠️ Verification recommendation [必須] のエントリは、Bibliographic verification完了まで final selection として扱わない。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2 要件（RI-02: 錯体同定完全化）**: EP-02a → **2006年** Jones et al. (Vicic) JACS Full Paper（自己充填、format-driven）⚠️ pending verification
- **VQ-2 要件（RI-01: マスバランス）**: EP-01a → 部分解消: **2006年** JACS Full Paper（自動解消候補）; 完全充填は未同定（インセンティブ構造的未充填）
- **VQ-3 要件（RI-03: on-cycle status）**: EP-03a → **2006–2013年** Vicic Full Paper（部分）+ Breitenfeld 2013（間接、技術駆動、8年後）
- **VQ-3 要件（RI-03/PRI-11: ラジカル機構）**: EP-10a → **2013年** Breitenfeld et al. (Hu) JACS（間接充填、Ni(I)/Ni(III)ラジカル機構確立、incentive-aligned、8年後）
- **VQ-3 要件（RI-06: Grignard→Zn類推検証）**: EP-06a → 未同定（5–15年スパン、間接的充填のみ期待）
- **VQ-4 要件（RI-08: 反復測定）**: EP-08a → 未充填（インセンティブ構造的未充填）
- **VQ-4 要件（RI-09: ベンチマーク比較）**: EP-09a → 未充填 or success-driven erasure

**階層-時間対応の評価：**

仮説「VQ階層が上がるほど充填に要する時間が長くなる」は本ケースでおおむね支持される。VQ-2要件（RI-02: 錯体同定）はLetter→Full Paper遷移（1年）で自動解消された可能性が高い（format-driven）。VQ-3要件（RI-03/PRI-11: 機構観測）は8年後（Breitenfeld 2013）に間接的に充填されており、technological barrier（EPR技術の適用拡大 + ラジカルクロック実験の方法論確立）が driving force となった（field-methodology）。VQ-4要件（RI-08/RI-09）は充填された証拠がなく、インセンティブ構造的未充填として残存する。反例として、EP-06a（RI-06、VQ-3要件）は現時点でも未充填であり、VQ-3要件すべてが同時に充填された訳ではない。

**特筆すべきパターン：**

1. **自己充填（Letter→Full Paper）**: Vicic研究グループによる自己充填（jones2005→JACS 2006）が最初の充填機会と推測される。ChemComm通信が1年以内にJACS Full Paperに発展するパターンは合成有機金属化学で標準的。

2. **先行充填（Prior filling）の不在**: 本論文（2005）より前に EP-10a（ラジカルメカニズム）を充填した論文がない可能性がある。Kinoshita et al. JACS 2004（Ni/Zn radical coupling）は先行充填候補だが、tpy配位子系への適用性は間接的。

3. **Indirect充填（Breitenfeld 2013）のラグ**: jones2005が提起したNi(I)–アルキルへのアルキルハライド付加（ラジカル vs 内圏）という問いは、同一問いを別の配位子系（ビスホスフィン）で追求したHu研究グループにより8年後に間接充填された。これは「異なるリガンド系の機構的等価性」という橋渡し問題が残ることを示す。

4. **VQ階層逆転の不在（本ケース）**: 典型的なインセンティブ逆転（低VQ充填が遅く、高VQ充填が早い）は本ケースでは顕在的でない。VQ-2（RI-02）が1年で自己充填され、VQ-3（RI-03/PRI-11）が8年後に間接充填されており、おおむね正順。ただしVQ-4（RI-08/RI-09）の未充填は維持されており、最低VQ要件の慢性的未充填はインセンティブ構造の反映。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-06a [Analogy-validation pack]（RI-06: Grignard/tpy系→Zn/tpy'系機構的類推）:**
* **未充填の理由**: 分野慣行 + インセンティブ不整合。Ni/Grignard系（ref 12）とNi/Zn系の機構的同型性を「tpy'配位子系で」直接比較した実験は、独立論文の主題として成立しにくい。より広いNi(I)/Ni(III)ラジカル機構研究が進む中で、「求核剤依存性」という問いは subquestion として吸収され独立論文化されなかった可能性がある。
* **発見的意義**: あり。Grignard→Zn求核剤の機構的差異は、Ni触媒アルキルカップリングの設計原理（求核剤選択と機構の関係）に直結する問いであり、2005年以降の文献で明示的に検討されていない可能性が高い。これはUQSが抽出した「分野が構造的に避けてきた比較問い」の事例として価値がある。
* **将来の充填可能性**: 中（現代の理論・実験化学で答えうる問いだが、既存論文での間接的検討で実質的に処理されている可能性もある）

**EP-08a [Replication / uncertainty pack]（RI-08: GC収率精度）:**
* **未充填の理由**: インセンティブ構造の不整合。stoichiometric実験（式3）の繰り返しとSD記録は技術的に容易だが、独立論文として出版するインセンティブが存在しない。Full Paper展開でn=2–3の繰り返しが記録される可能性はあるが、統計的評価論文としての独立充填は想定されない。
* **発見的意義**: なし（この種の報告形式問題は分野全般に存在する；jones2005固有の発見ではない）
* **将来の充填可能性**: 低（インセンティブ構造が変わらない限り独立充填の見込みはない。Open Data政策の普及によるデータ公開で間接的に充填される可能性はある）

**EP-09a [Internal benchmark pack]（RI-09: refs 5-11との直接比較）:**
* **未充填の理由**: Success-driven question erasure候補。tpy/tpy' Ni系の詳細な比較よりも、ビスホスフィン-Ni（Hu、Fu等）が高収率・高エナンチオ選択的アルキル-アルキルカップリングとして台頭したことで、tpy'系の他系との直接比較研究の動機が失われた可能性がある。技術的に可能だが、競合触媒の成功により検証需要が消滅した。
* **発見的意義**: あり（success-driven question erasure の事例として記録可能。tpy'系が後続研究に吸収されなかった理由の探索は「成功した記録されなかった比較」という成果帰属の問いに接続する）
* **将来の充填可能性**: 低（tpy'系の現代的再評価論文が書かれる場合を除く）

**EP-01a [Reporting-coherence pack]（RI-01: 式3マスバランス62%未帰属）:**
* **未充填の理由**: インセンティブ構造的未充填。式(3)の未帰属炭素（62%）追跡実験は技術的に可能だが、独立論文化はされない。Vicic JACS 2006 Full Paper（⚠️pending）内で部分的に解消された可能性はあるが、独立充填論文としての存在は想定されない。
* **発見的意義**: あり（ただし限定的）。「化学量論実験の62%未帰属炭素が無视されたまま機構的帰結の根拠として機能した」というパターンは、通信論文に基づく機構結論の脆弱性を示す実例として記録価値がある。
* **将来の充填可能性**: 低（式3のマスバランス追跡のみを目的とした独立論文は想定されない）

**VQ階層逆転診断:**
EP-08a, EP-09a, EP-01a（低VQ要件: RI-01, RI-08, RI-09）が未充填のまま残り、EP-10a, EP-03a（高VQ要件: RI-03, PRI-11）が8年後に間接的に充填されたという構造は、「科学的論理に基づくEP充填順序（低VQ→高VQ）」と「実際のインセンティブに基づく充填順序（高VQ機構問題→低VQ基礎精度）」の軽度の逆転を示している。機構的新規性（ラジカル vs 内圏）への関心が高VQ充填を駆動し、精度・報告形式（低VQ）の改善は慢性的に未充填のまま残る——この逆転構造はNi触媒機構論文一般に広く観察される可能性がある。
