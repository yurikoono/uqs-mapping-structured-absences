```
prompt_version: stage4-v6-20260504
model_info: Claude Sonnet (current snapshot)
experimental_variant: "Murai cross-vendor multi-run sonnet v6 run 3"
date: 2026-06-12
```

---

# EP充填選定マップ

## Murai et al. 1993（Nature, communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a

- **EP-03a（Direct-observation / state-assignment pack）**: Ru(0)活性種の生成確認・シクロメタル化中間体の観測という実験的課題は、Chataniら・Kakiuchiらのグループによる後続機構論文の主題として独立に発表されやすく、直接追跡可能。
- **EP-04a（Discrimination / replication pack）**: KIE測定・重水素標識実験によるC–H切断の律速確認は、反応機構研究として独立した論文主題になりやすく、Murai反応の機構解明研究として複数件が発表されているはずである。
- **EP-06a（Analogy-validation pack）**: シクロメタル化モデル反応（化学量論反応でのRu中間体単離）は独立した論文の主題として出版されやすく、Ru錯体化学の文脈でChatani等のグループが対応する研究を行っているはずである。
- **EP-07a（Boundary-test pack）**: キレーション支援の構造的境界（環サイズ、キレーター種）の体系的探索は、Murai反応の基質スコープ拡張論文群の主題として独立に発表されており、直接追跡可能。

**第二群（間接的に追跡可能）：** EP-05a, EP-09a

- **EP-05a（Quantitative-ranking substantiation pack）**: 選択性の速度論的対熱力学的制御の判別は、Murai反応の詳細機構論文やDFT計算論文で扱われているが、独立した主題というより機構研究の一部として登場する傾向がある。
- **EP-09a（Internal benchmark pack）**: TOF値の先行研究との数値的比較は、レビュー論文・perspective・教科書等でMurai反応の歴史的評価として取り扱われるが、それ単独を主題とした独立研究は少ない。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a

- **EP-01a（Reporting-coherence pack）**: GC収率の校正プロトコルの遡及的開示はLetter→Full Paper遷移でのformat-driven自動解消を期待できるが、同一著者グループのFull Paperが有機合成系の展開論文として発表された場合、校正プロトコル自体は新しい内部手順となっており、1993年オリジナル実験の校正データが後続論文で明示的に「遡及的に提供」されることは稀である。インセンティブ構造的未充填の傾向あり。
- **EP-08a（Replication / uncertainty pack）**: 13例の3重複実験・SD付きデータは独立論文として出版するインセンティブが低く（新規性要求との不整合）、Full Paperとしての展開でもTable 1の13例を再計測・再報告することは通常行われない。インセンティブ構造的未充填に分類。

なお、EP-01aについて：Murai 1993はNature communication（3ページ）形式であり、C23（Letter→Full Paper auto-resolution）パターンが発動する条件を満たす。同一著者グループによるFull Paperの続報が1〜3年以内に発表された場合、reporting completenessの自動部分解消が期待できる。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: Kakiuchi, F. et al., *J. Am. Chem. Soc.* 1994, 116, 11620–11621（推測）— 同一著者グループによるFull Paperまたは続報において、実験条件の詳細（内標準・反応条件・不活性ガス雰囲気）が初めて明示されたと推定されるが、これは1993年オリジナルデータの校正プロトコルの遡及的開示ではなく、新規実験の標準化された報告である。
* **充填確立点**: 未同定（GC校正プロトコルの遡及的開示として機能する論文は確認できない）
* **充填の性質**: Partial — 後続Full Paperが実験条件を詳述することで間接的に部分解消されるが、オリジナル13例の校正データは提供されない
* **Bibliographic confidence**: Low — 続報論文の存在は推測であり、巻号ページを確認できない
* **Filling adequacy confidence**: Low — EP-01aの要件（Table 1全13例の校正プロトコル遡及開示）を直接満たす論文の同定が困難
* **Verification recommendation**: [必須] — (c) named reaction（Murai reaction）+ (d) Low confidence候補を含む
* **Filling timescale category**: format-driven (1-3 yr) — Letter→Full Paper自動解消パターンを一部期待できるが、完全充填は構造的に困難
* **注記**: C23トリガー発動（Letter形式）。同著者グループのFull Paperによるauto-resolution_status: promisedと評価するが、GC校正の遡及的開示という意味での完全充填はnon-applicableに近い。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点**: Chatani, N., Fukuyama, T., Kakiuchi, F. & Murai, S., *J. Am. Chem. Soc.* 1998, 120, 11522–11523 — Murai反応の機構的側面を扱い、活性種の帰属に関する実験的証拠を提供した論文として想起（著者組合せに推測含む）。
* **充填確立点**: Guari, Y., Sabo-Etienne, S. & Chaudret, B., *J. Am. Chem. Soc.* 1998, 120, 4228–4229 — ルテニウムカルボニル錯体とケトン基質の相互作用に関する分光学的研究として想起。ただしMurai 1993系との対応は推論を含む。
* **充填の性質**: Partial — Ru(0)活性種の生成確認は複数の後続論文で扱われているが、オリジナルのRuH₂(CO)(PPh₃)₃系における直接観測という意味での完全充填は長期遅延した可能性がある
* **Bibliographic confidence**: Low — 著者組合せおよび巻号の正確性に不確実性がある
* **Filling adequacy confidence**: Medium — Murai反応の機構論文として複数件が存在し、Ru活性種生成のNMR追跡や中間体観測が行われているはずである
* **Verification recommendation**: [必須] — (b) 同一著者ネットワーク10+件あり、(c) named reaction
* **DOI**: 不明（確認要）
* **Filling timescale category**: field-methodology (2-5 yr) — 機構研究はMurai反応の発表後、field-wideな方法論的応答として展開した
* **注記**: Murai 1993以降の機構研究としては、Chatani・Kakiuchi・Muraiグループ自身による後続研究に加え、他グループ（Bergman、Goldman等）のRu系C–H活性化機構研究が対応する可能性がある。SRG-1（B-3, B-14, U-1, U-2）の解消に最も直接的に寄与するカテゴリ。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: Kakiuchi, F., Sato, T., Tsujii, K., Chatani, N. & Murai, S., *J. Am. Chem. Soc.* 1998, 120, 11994–11995（著者・年・タイトル推測）— Murai反応のKIE実験または重水素標識実験が含まれた機構論文として想起。著者リストの正確性に不確実性がある。
* **充填確立点**: Lim, S.-G., Ahn, J.-A. & Jun, C.-H., *Org. Lett.* 2004, 6, 4687–4690（推測）— RuまたはRh触媒系のC–H活性化におけるKIE測定を含む機構論文として想起。ただし本系への対応は推論を含む。
* **充填の性質**: Partial — KIE測定・重水素標識実験はMurai反応系で実施された可能性があるが、M–H/M–C挿入経路の完全判別という観点での充填確立は不確実
* **Bibliographic confidence**: Low — 著者・年・巻号の正確性に不確実性がある
* **Filling adequacy confidence**: Medium — KIEおよびラベル実験によるC–H切断律速確認はMurai反応の機構論文で扱われているはずである
* **Verification recommendation**: [必須] — (b)(c)に該当
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: M–H対M–C挿入経路の区別という問いへの答えは、DFT計算を組み合わせた計算化学的アプローチによっても対応されている可能性がある。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 Qualitative overread
* **充填開始点**: Kakiuchi, F. & Murai, S., *Acc. Chem. Res.* 2002, 35, 826–834（推測）— Murai反応の選択性に関する定量的考察を含む総括論文。ただしレビュー性格が強く、EP充填の主体は選択性の速度論的実験を含む原著論文でなければならない。
* **充填確立点（原著論文として）**: Matsubara, T., Koga, N., Musaev, D. G. & Morokuma, K., *J. Am. Chem. Soc.* 2000, 122, 10, 2222–2223（推測）— Murai反応のDFT計算による機構解析（遷移状態の自由エネルギー）。ortho選択性の速度論的起源を計算化学的に支持する内容として想起。
* **充填の性質**: Indirect — 選択性の速度論的起源は実験（VT-GC、競合実験）ではなく計算化学的アプローチで主に対応されており、EP-05aの実験的要件の直接充填ではない
* **Bibliographic confidence**: Low（Acc. Chem. Res. 2002）/ Low（Morokuma計算論文の具体的な著者・巻号）
* **Filling adequacy confidence**: Medium — DFT計算はortho選択性の速度論的基盤を部分的に提供する
* **Verification recommendation**: [必須] — (b)(c)に該当
* **Filling timescale category**: field-methodology (2-5 yr) — DFT計算手法の成熟化によって対応された
* **注記**: EP-05aの実験的要件（温度依存性VT-GC、速度論的制御の実験的判別）は充填されていない可能性があり、計算化学的対応が主流となったことで問いの性格が変容した（Paradigm-shift的充填）。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Chatani, N., Asaumi, M., Ikeda, T., Yorimitsu, S., Ishii, Y., Kakiuchi, F. & Murai, S., *J. Am. Chem. Soc.* 2000, 122, 10, 2610–2611（著者・年・巻号推測）— Murai型反応のシクロメタル化中間体の直接的な証拠を提供した論文として想起（著者リスト推測を含む）。
* **充填確立点**: Matsubara, T., Koga, N., Musaev, D. G. & Morokuma, K., *J. Am. Chem. Soc.* 1998, 120, 12692–12693（推測）— RuH₂(CO)(PPh₃)₂を用いたMurai型C–H活性化のDFT計算による機構解析として想起。シクロメタル化中間体の安定性・形成経路を理論的に示す。
* **充填の性質**: Partial — シクロメタル化中間体の理論的サポートは与えられているが、RuH₂(CO)(PPh₃)₃系における直接分光観測という観点での充填は限定的
* **Bibliographic confidence**: Low — 著者組合せと巻号ページに不確実性がある
* **Filling adequacy confidence**: Medium
* **Verification recommendation**: [必須] — (b)(c)に該当
* **Filling timescale category**: field-methodology (2-5 yr)
* **注記**: Matsubara-Morokuma計算論文は、類似系での計算化学的支持としてRI-06の解消に間接的に貢献する。原著類似系（C₄H₄Knobler / McGuiggan参照論文）との比較は充填論文によってより具体的に対応された。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Kakiuchi, F., Yamamoto, Y., Chatani, N. & Murai, S., *Chem. Lett.* 1995, 681–682（推測）— Murai型反応のキレーター種の境界条件を探索した最初期の展開論文として想起。
* **充填確立点**: Kakiuchi, F., Sekine, S., Tanaka, Y., Kamatani, A., Sonoda, M., Chatani, N. & Murai, S., *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83（推測）— 1993年の発見communicationのFull Paper展開として、様々な基質（環サイズ・キレーター種）を系統的に探索し境界条件を確立した論文として想起。
* **充填の性質**: Complete — Full Paper展開によってキレーション支援の構造的境界（5員 vs. 7員金属環、ケトン vs. アルデヒド vs. イミン等のキレーター種）が体系的に検証されたはずである
* **Bibliographic confidence**: Medium（Bull. Chem. Soc. Jpn. 1995は年・著者に高い確信；巻号ページは推測）/ Low（Chem. Lett. 1995）
* **Filling adequacy confidence**: High — Full Paper展開として基質スコープ境界の系統的検証が主題になっているはずである
* **Verification recommendation**: [必須] — (b)(c)(d)に該当
  * auto_resolution_type: "Letter→Full Paper"
  * expected_resolution_window: "1-3 yr"
  * auto_resolution_status: occurred
  * filling_timescale_category: "format-driven"
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: EP-07aとCLA-1（キレーション支援の構造的境界）の充填はLetter→Full Paper自動解消パターン（C23）で対応される典型事例。Murai et al. 1993のFull Paper展開としてBull. Chem. Soc. Jpn.あるいはChem. Lett.誌の続報が存在するはずである。Stage 3 §5の「EP-07aは不活性ガス条件確立（1日実験）」という最短補強ルートとは異なり、本境界テストは実験展開として1-3年の時間スケールで充填された。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: Non-applicable — インセンティブ構造的未充填に分類
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: N/A
* **Filling timescale category**: non-applicable
* **注記**: 13例の3重複実験によるSD付きデータセットは、新規性要求を中心とする出版慣行のもとで独立論文として出版するインセンティブが存在しない。Full Paper展開でも収率は新規基質について報告されるのが通例であり、1993年の13例を再計測・再報告してSD付きデータを提供する研究は発表されていない可能性が高い。インセンティブ構造的未充填（incentive-structure mismatch）として記録する。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点**: Kakiuchi, F. & Murai, S., *Acc. Chem. Res.* 2002, 35, 826–834（推測）— Murai反応の歴史的評価を含む総括論文。Jordan & Taylor (1989) / Moore et al. (1992)との文脈的比較がレビューとして提供されたと想起。ただしレビューは充填論文ではなく二次情報源である。
* **充填確立点（レビュー以外の独立論文として）**: 未同定 — TOFの直接数値比較を独立論文の主題として報告した研究は特定できない
* **充填の性質**: Indirect — レビューやPerspective論文においてMurai反応とZr/Ru先行系のTOF値の文脈的比較が提供されているが、EP-09aが要求する「同一軸での数値比較表」としての充填には至らない可能性が高い
* **Bibliographic confidence**: Medium（Acc. Chem. Res. 2002年・著者Kakiuchi/Murai名は確信）
* **Filling adequacy confidence**: Low — レビュー論文は充填論文として機能しないという原則からも、EP-09aの完全充填論文の同定は困難
* **Verification recommendation**: [推奨]
* **DOI**: 10.1021/ar010085f（推測）
* **Filling timescale category**: incentive-aligned (variable)
* **注記**: EP-09aはSRG-5（D-4候補6：先行研究との数値的比較の不在）に直接対応する。レビュー・Perspective・総説類においてMurai反応のTOFが言及・比較される形での間接充填が主流となっており、独立した数値比較論文の出版動機は低かった。

---

**§B 末尾チェック：Bibliographic verification（v18.3 追加）**

トリガー条件の評価：
- (b) 著者ネットワークが密（Murai/Kakiuchi/Chataniグループから10+件の関連論文あり）: **該当**
- (c) Named reaction（Murai反応）: **該当**
- (d) Bibliographic confidence Medium-Low の候補が複数含まれる: **該当**

→ 全候補に **[必須]** を付与。

Bibliographic verification status: **pending**（post-hoc検証が必要）

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Kakiuchi, F. et al., *Bull. Chem. Soc. Jpn.* 1995, 68, 62–83（⚠️推測） | EP-07a, EP-01a（部分） | VQ-2（RI-07前進） | 1995 | Medium | High | 必須 |
| 2 | Matsubara, T. et al., *J. Am. Chem. Soc.* 1998, 120, 12692–12693（⚠️推測） | EP-06a, EP-03a（間接） | VQ-3（RI-06前進） | 1998 | Low | Medium | 必須 |
| 3 | Chatani, N. et al., *J. Am. Chem. Soc.* 1998, 120, 11522–11523（⚠️推測） | EP-03a, EP-04a（部分） | VQ-3（RI-03前進） | 1998 | Low | Medium | 必須 |
| 4 | Kakiuchi, F. & Murai, S., *Acc. Chem. Res.* 2002, 35, 826–834（⚠️推測） | EP-09a（間接）, EP-07a（補完） | VQ-4（RI-09間接） | 2002 | Medium | Low | 推奨 |
| 5 | Kakiuchi, F., Yamamoto, Y., Chatani, N. & Murai, S., *Chem. Lett.* 1995, 681–682（⚠️推測） | EP-07a（部分） | VQ-2（RI-07部分前進） | 1995 | Low | Medium | 必須 |

全エントリが **⚠️ verification 待機中**。

**選定理由：**

順序1のKakiuchi et al. 1995（Bull. Chem. Soc. Jpn.）は、1993年communicationのFull Paper展開として最も直接的にEP-07a（キレーション支援の構造的境界）を充填するはずである。著者・年・掲載誌については比較的高い確信があるが、具体的な巻号ページは推測であり、verification必須。このFull Paperがformat-driven auto-resolutionの核心論文であり、EP-07a（CLA-1）の充填確立点として機能する。

順序2・3の1998年論文群は、SRG-1（機構実験の完全不在）に対応するfield-methodology応答として5年スケールで充填が行われた候補である。Murai・Chatani・Kakiuchiグループ自身による後続機構論文、およびMorokuma計算グループによるDFT機構研究として想起しているが、著者組合せと巻号ページの正確性に不確実性があり、post-hoc verificationが不可欠。

順序4のKakiuchi & Murai Acc. Chem. Res. 2002は、EP-09a（TOF数値比較）をレビューとして間接的に対応するものであり、充填論文の本来的な性格を持たないが、「二次情報源として充填論文の特定に利用できる」という位置付けで選定リストに含めた。Filling adequacy confidence: Lowであり、これは§C規定（Low論文は原則選定しない）の例外的記載であることを明記する。

バンドル充填として、Bull. Chem. Soc. Jpn. 1995（推測）がEP-07aとEP-01a（部分）を同時カバーする効率的な充填論文候補として位置付けられる。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a（Reporting-coherence）→ 【構造的に未充填（incentive mismatch）/ 部分的にformat-driven 1-3 yr】
- VQ-2 要件: EP-07a（Boundary-test）→ 【1995年頃 Kakiuchi et al. / format-driven auto-resolved（推測）】自己充填・分割提示充填
- VQ-3 要件: EP-03a（Direct-observation）→ 【1998年頃 機構論文群 / field-methodology 5 yr】自己充填
- VQ-3 要件: EP-04a（Discrimination / replication）→ 【1998-2000年頃 / field-methodology 5-7 yr】自己充填
- VQ-3 要件: EP-05a（Quantitative-ranking）→ 【2000年頃 計算化学 / field-methodology + paradigm-shift的変容】分野横断充填
- VQ-3 要件: EP-06a（Analogy-validation）→ 【1998-2000年頃 計算化学 / field-methodology】技術駆動充填
- VQ-4 要件: EP-08a（Replication / uncertainty）→ 【未充填（incentive-structural unfilling）】
- VQ-4 要件: EP-09a（Internal benchmark）→ 【レビュー論文で間接的対応 / incentive-aligned, variable】

**階層-時間対応の評価：**

VQ-2要件に対応するEP-07aがformat-driven（1-2年）で比較的早期に充填される一方、VQ-3要件に対応するEP-03a・EP-04a・EP-05a・EP-06aはfield-methodology（5-7年）スケールで充填される傾向が見られる。これは「VQ階層が上がるほど充填に要する時間が長くなる」という仮説と概ね整合的である。しかしVQ-2要件のEP-01a（Reporting integrity）は低VQ要件でありながら未充填のままである点で反例となる——これはEP-01aがreporting integrityという「インセンティブ構造的に充填されにくい」問いであることを示しており、VQ階層よりもRI種別がfilling timelineを規定するという観察として記録できる。

VQ-4要件のEP-08a（Replication / uncertainty）は最も高いVQ要件でありながら未充填のままであり、長期遅延充填（incentive-structural unfilling）として機能している。

**特筆すべきパターン：**

1. **自己充填 + 分割提示充填**: Murai/Kakiuchi/Chataniグループ自身が後続論文（Full Paper、Chem. Lett.、Bull. Chem. Soc. Jpn.等）でEP-07aを充填するパターンが最も典型的。これはMurai反応がグループ内での展開研究として組織的に継続されたことを示す。

2. **技術駆動充填（計算化学的転換）**: EP-05a・EP-06aに対してはDFT計算（Morokuma、Koga等）が主要な充填経路となり、実験的充填ではなく計算化学的アプローチで問いが「再定義」された。この技術駆動転換は1995年以降のDFT計算コストの低下に対応する。

3. **著者回顧との照合（CLA-2「合成標的との接続」）**: Murai反応はその後、医薬品・天然物合成への応用研究が急速に展開し（Murai自身のグループ + Chataniグループ + 国際的な展開）、CLA-2に対応する充填は多数存在する。これは「著者が回顧で認識しなかった問いへの後続充填」の典型事例である。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-01a [Reporting-coherence pack]（第三群・部分未充填）:**

* **未充填の理由**: インセンティブ構造的未充填（incentive-structure mismatch）。GC収率の校正プロトコル（内標準・応答係数）の遡及的開示は、後続Full Paperの文脈では新規基質に対する新たな実験として報告されるため、1993年のオリジナル13例についての校正データが「遡及的に」提供される動機が存在しない。Letter→Full Paperの形式転換によって実験条件の詳述は進むが、元のデータの測定根拠の補完という意味での充填は行われない。
* **発見的意義**: あり。「発見communicationの定量的証拠は後続論文によって遡及的に補完されない」という分野慣行のパターンとして記録できる。1993年の13例はGC収率のまま未検証で歴史的記録として定着しており、Murai反応の「量的基盤」は検証不可能な状態で科学的影響力を発揮し続けているという発見論的意義がある。
* **将来の充填可能性**: 低 — オリジナル実験の著者グループが現在もいくつかのメンバーが活動中であっても、1993年の実験ノートの検証・公開という形での充填は実現していないと推測される。historical archiveとしての参照可能性は低い。

**EP-08a [Replication / uncertainty pack]（第三群・未充填）:**

* **未充填の理由**: インセンティブ構造的未充填（incentive-structure mismatch）。13例の3重複実験によるSD付きデータセットは、「追試」「統計的評価」として独立論文化するインセンティブが低く、新規性要求を中心とする出版慣行との不整合が持続している。Murai反応の後続研究は新規基質・新規触媒・新規キレーター・新規反応条件の探索として展開し、1993年の代表的収率の再現実験は行われていない。
* **発見的意義**: あり。Murai反応の効率性・選択性・汎用性という3主張はすべてSD付きデータのないGC収率に依拠しており、この「統計的根拠の未充填」が30年以上継続していることは、成功した有機合成communicationにおける再現性担保の制度的不在の証拠として記録できる。UQSが「分野が30年にわたって体系的に問わなかった問い」として特定できる典型事例。
* **将来の充填可能性**: 中 — 現代の再現性・再現性危機に関する議論の文脈で、Murai反応のような歴史的ランドマーク反応の独立再現研究が提案・実施される可能性はある（例：Replication Studies in Synthetic Chemistry的なイニシアティブ）。ただし現時点では充填論文は発表されていないと推測する。

**VQ階層逆転パターンの診断：**

EP-01a（RI-01）・EP-08a（RI-08）という低VQ要件（VQ-2, VQ-4）に関連するEPが未充填のまま残り、EP-03a・EP-04a・EP-07a（RI-03, RI-04, RI-07）という相対的に高いVQ要件のEPが先に充填される傾向（または充填への進展が観察される傾向）が見られる。これはUQS Stage 3 §5が規定する「EP-01a → EP-07a → EP-03a → EP-04a → EP-05a → EP-06a → EP-09a」という科学的論理に基づく最短補強ルート（低VQ→高VQ）に対し、実際の充填順序が「EP-07a（スコープ境界→実用的展開）→ EP-03a/EP-06a（計算化学・機構研究）→ EP-09a（レビュー）」という出版インセンティブ主導の高VQ先行充填として展開した可能性を示す。VQ階層逆転パターンとして記録する。

---

*inference_time_sec: not available — inject externally*
