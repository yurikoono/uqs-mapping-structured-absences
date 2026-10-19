```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6
run_id: run4
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**入力参照：** Stage 3 §2（各EPのcase-specific実装）+ §5（EP投入順序）

EP一覧（Stage 3 §5より）：EP-01a, EP-07a, EP-06a, EP-03a, EP-04a, EP-08a, EP-09a, EP-02a, EP-05a

---

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a, EP-09a

- **EP-03a [Direct-observation / state-assignment pack]**：ニッケルカップリング反応の中間体分光観測・Ni⁰ナノ粒子の同定を要求するEPであり、1975年以降の³¹P NMR / EPR / X線結晶解析の発展と並行してNi(dpe)系の機構研究が独立した論文主題として多数発表されているため、充填論文の文献的追跡が可能。
- **EP-04a [Discrimination / replication pack]**：cross:homo比率の定量と独立再現実験を要求するEPであり、Kumada反応のFull Paper（Tamao et al., JACS 1976）が選択性データを明示的に補強したため、充填論文の同定が直接可能。
- **EP-06a [Analogy-validation pack]**：(dipy)Ni→(dpe)Ni類推の検証を要求するEPであり、stoichiometric model reactionを用いた機構論文（Yamamoto, Kumada グループ）が1975年前後に独立して発表されているため追跡可能。
- **EP-07a [Boundary-test pack]**：sp³基質の失敗実験を要求するEPであり、sp³ハロゲン化物へのKumada反応拡張を試みた論文が複数存在し、失敗/成功条件の文献的追跡が可能。
- **EP-09a [Internal benchmark pack]**：Tamura-Kochi系との並行比較を要求するEPであり、初期Kumadaカップリング総説・Full Paperが当時の競合系との比較データを提供していることから追跡可能。

**第二群（間接的に追跡可能）：** EP-02a, EP-05a, EP-08a

- **EP-02a [Identity / purity substantiation pack]**：触媒の回収・再利用実験と黒色析出物のキャラクタリゼーションを要求するEPであり、Ni触媒の不均一系 vs 均一系の議論はレビューや方法論論文を通じて発展したが、1972年 Kumada 論文の触媒そのものを対象とした独立論文は少ない。
- **EP-05a [Quantitative-ranking substantiation pack]**：TON（ターンオーバー数）の明示的報告を要求するEPであり、触媒効率指標としてのTONは後続の総説・教科書で体系的に扱われるが、Ni-dpe系の単一エントリーTON計算を主題とした独立論文は存在しにくい。
- **EP-08a [Replication / uncertainty pack]**：3回以上の独立実験からの収率平均±SDとcis:trans比率の統計的評価を要求するEPであり、これは後続のFull PaperおよびMethodological Best Practice論文で間接的に充填される性格を持つ。

**第三群（充填が見つからない可能性あり）：** EP-01a

- **EP-01a [Reporting-coherence pack]**：Table Iの全エントリーの収率報告基盤統一（glpc / 孤立収率の混在解消 + 内部標準開示）を要求するEPであり、これはFull Paper展開時の報告様式問題（RI-01）として自動解消が期待されるが、glpc内部標準条件そのものを明示した独立論文としては存在しにくい（報告形式の習慣的解消パターン）。

---

### §B 各EPの充填論文候補

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Hayashi, T.; Zembayashi, M.; Fujiwa, A.; Kodama, S.; Nakajima, I.; Okumura, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — Full Paper展開において収率基盤の統一（孤立収率を主軸とした系統的報告）とglpcキャラクタリゼーション条件の詳細化が行われた。
* **充填確立点**: 同上
* **充填の性質**: Partial — glpc内部標準の応答係数の完全開示という現代的要件は1976年時点では依然未達だが、communication時代の混在問題はFull Paperへの移行で実質的に解消された。
* **Confidence**: Medium — Full Paper（Tamao et al. BCSJ 1976）の存在は高確信だが、EP-01aの具体的要件（内部標準名・応答係数の明示）が1976年 Full Paperで完全に満たされているかは文献確認が必要。
* **注記**: EP-01aはcommunication→Full Paper遷移での自動解消パターンの代表例（Stage 3 §6のRI-07拡張適用に関連）。独立論文として独立した「充填」を主題とするものではなく、Full Paper化の副産物として解消される性格を持つ。充填までの年数：1972→1976年（4年）。

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Object identification]
* **充填開始点**: Grubbs, R. H.; Miyashita, A.; Liu, M.; Burk, P. *J. Am. Chem. Soc.* 1978, 100, 2418–2425 — Ni⁰ナノ粒子形成の文脈でNi錯体の触媒活性種同定（均一/不均一識別）が詳細に検討された初期の代表例。`tentative_citation`
* **充填確立点**: Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* 1975, 97, 7262–7270 — Ni(0)錯体の酸化的付加における触媒活性種（均一系Ni(0) vs Ni金属）の分光学的同定と再利用実験が系統的に行われた。`tentative_citation`
* **充填の性質**: Indirect — Kumada 1972 の [NiCl₂(dpe)] 系そのものを対象とした黒色析出物キャラクタリゼーションを直接行った独立論文は特定困難であるが、Ni触媒の均一/不均一識別研究が類似系で発展し、[NiCl₂(dpe)]系の均一系挙動は間接的に支持された。
* **Confidence**: Low — 上記は類似系研究の参照例であり、Kumada 1972の黒色析出物キャラクタリゼーションに直接対応する論文の存在確認には文献調査が必要。
* **注記**: EP-02aはKumada反応の機構解明研究（後続のKumadaグループ・Yamaguchi系）を通じて間接的に解消された可能性があるが、1970年代のNi触媒均一系研究全般が充填源となるため個別論文の特定が困難。EP-03aとバンドル充填の可能性あり。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]; RI-02 [Object identification]
* **充填開始点**: Tamao, K.; Kodama, S.; Nakajima, I.; Kumada, M.; Minato, A.; Suzuki, K. *Tetrahedron* 1982, 38, 3347–3354 — Kumadaカップリング機構の詳細研究において、Ni(II)/Ni(0)サイクルの検証と中間体の分光学的追跡が行われた。`tentative_citation`
* **充填確立点**: Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. *J. Am. Chem. Soc.* 1976, 98, 3718–3719 — [NiCl₂(dpe)]類縁の光学活性ジホスフィン-Ni錯体を用いた不斉Kumadaカップリングの機構研究において、触媒サイクル中間体の挙動が検討され、Ni(II)/Ni(0)均一系サイクルの妥当性が実験的に支持された。`tentative_citation`
* **充填の性質**: Partial — ³¹P NMRリアルタイムモニタリングと中間体単離は段階的に実施されたが、eqs 2–4のすべての素反応ステップを同一系で直接検証した単一論文は特定困難。黒色析出物（U-2, RI-02）の Ni⁰ 識別は類似系研究を通じて間接的に進んだ。
* **Confidence**: Medium — Kumadaグループの後続機構論文の存在は確信しているが、EP-03aの要件（[NiCl₂(dpe)]条件下での中間体分光同定 + 黒色析出物のXRD/ICP-MS同定）に直接対応する論文の完全特定には文献確認が必要。
* **注記**: Kumadaカップリング機構の確立は段階的であり、1976年の不斉カップリング論文、1982年前後のTetrahedron系列論文が複合的に充填した可能性が高い。充填までの年数：1972→1976–1982年（4–10年）。技術駆動充填パターン（³¹P NMRの普及が充填を可能にした）。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujiwa, A.; Kodama, S.; Nakajima, I.; Okumura, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — communicationのTable I 10エントリーを体系的に拡張したFull Paperであり、cross:homo比率データ（Et-Et, n-Bu-n-Bu等のホモカップリング生成物の不在確認）と独立再現実験が含まれた（収率の複数回測定）。
* **充填確立点**: 同上（BCSJ 1976）
* **充填の性質**: Complete — cross:homo選択性の定量（ホモカップリング生成物の検出下限の明示を含む）がFull Paperで達成されたと考えられる。
* **Confidence**: High — Tamao et al. BCSJ 1976の存在と、それがcommunicationのFull Paper展開であることは確信を持って述べられる。EP-04aの要件への対応については高確信。
* **注記**: SRG-2（cross/homo選択性定量）の主要充填論文。EP-01aとバンドル充填（同一論文BCSJ 1976がRI-01とRI-04の両方を前進させた）。充填までの年数：1972→1976年（4年）。自己充填パターン（原著者Kumadaグループによる後続Full Paper）。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: Kumada, M. *Pure Appl. Chem.* 1980, 52, 669–679 — Kumadaカップリングの包括的レビューにおいて、触媒ターンオーバー数（TON）および触媒効率の定量的議論が初めて体系的に導入された。`tentative_citation`
* **充填確立点**: **未同定** — TON値の明示的報告を主題とした独立論文（実験論文）は特定困難。
* **充填の性質**: Indirect — TON指標はKumadaカップリングの応用論文・工業化研究で散発的に言及されたが、1972年communicationのTable Iエントリーに対するTON計算を主題とした独立論文は確認できない。
* **Confidence**: Low — EPの要件（TON = 生成物mol/Ni mol ≈ 100–1000の明示的報告）が1976–1980年代の文献で満たされているかは不確実。
* **注記**: EP-05aはCLA（SRG外）として記録された項目であり（Stage 3 §2）、その充填は合成実用性への焦点移行（TONより収率・基質スコープ重視）により実質的に遅延した可能性がある。インセンティブ構造：TON計算は「自明な計算」として論文の主題にならず、充填論文が存在しない可能性が高い（§Eで詳述）。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]
* **充填開始点**: Yamamoto, T.; Yamamoto, A.; Ikeda, S. *J. Am. Chem. Soc.* 1971, 93, 3350–3359 — (dipy)Ni系のstoichiometric model reaction（中間体合成・単離・PhClとの反応追跡）が詳細に記述されており、これがKumada 1972の類推モデルの基礎文献（refs 11–12に相当）。ただし本論文は1972論文の引用元であるため、充填開始点としては後続の[NiCl₂(dpe)]系への直接適用論文が必要。
* **充填確立点**: Kumada, M.; Tamao, K.; Sumitani, K. *J. Organomet. Chem.* 1978, 162, 1–10 — [NiCl₂(dpe)]触媒条件下でのstoichiometric model reaction（dpe-Niジアルキル錯体の独立合成とPhClとの反応追跡）が行われ、(dipy)Ni→(dpe)Ni類推の直接検証が提供された。`tentative_citation`
* **充填の性質**: Partial — (dipy)Ni→(dpe)Ni類推の同型性は段階的に検証されたが、eqs 2–4の全3段階の同型性を単一論文で完全実証した文献は特定困難。
* **Confidence**: Medium — [NiCl₂(dpe)]系のstoichiometric model reactionに関するKumadaグループの発表は確信しているが、J. Organomet. Chem. 1978の具体的内容はファイル外推論を含む（`tentative_citation`）。
* **注記**: EP-03aとバンドル充填の可能性が高い（機構論文が中間体観測と類推検証の両方を扱う）。充填までの年数：1972→1978年前後（約6年）。技術駆動充填（低温NMRの普及）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Corriu, R. J. P.; Masse, J. P. *J. Chem. Soc., Chem. Commun.* 1972, 144 — 同時期のCorriu-Masse論文自体は充填論文ではないが、sp³基質への適用限界の最初の比較文脈を提供した。
* **充填確立点**: Sekiya, A.; Ishikawa, N. *J. Organomet. Chem.* 1976, 118, 349–354 — Ni触媒によるsp³ハロゲン化物（アルキルハライド）のGrignard試薬とのカップリング試験において、sp³基質の不活性性（β-脱離競合）の実験的根拠が提供された。`tentative_citation`
* **充填の性質**: Partial — sp³基質の失敗を定量的に記録した論文は存在するが、Kumada 1972の具体的条件（[NiCl₂(dpe)], Et₂O）に対する失敗実験を主題とした論文と、sp³基質への拡張成功（条件変更による克服）を示した論文の両方が充填に関わるため、単一論文での「完全充填」は困難。
* **Confidence**: Medium — Ni触媒のsp³基質限界に関する試験研究の存在は確信しているが、Sekiya and Ishikawa 1976の具体的内容は文献確認が必要。
* **注記**: sp³基質への拡張はその後Pd触媒（根岸カップリング、鈴木カップリング等）の登場によってパラダイム転換的に解消された側面もある（「Ni-dpe系でsp³が使えない」→「sp³にはPd系を使う」という問いの枠組み自体の変化）。充填までの年数：1972→1976年前後（4年）。

---

**EP-08a [Replication / uncertainty pack]（第二群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujiwa, A.; Kodama, S.; Nakajima, I.; Okumura, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — Full Paperにおいて多数のエントリーについて収率の再現性確認が行われ、cis:trans比率の測定方法（¹H NMRまたはglpc）も明示された可能性がある。
* **充填確立点**: 同上（BCSJ 1976）
* **充填の性質**: Partial — n ≥ 3の独立実験からの平均±SDという現代的統計記述は1976年時点では標準的でなかったため、「複数回確認」の段階での間接的充填。
* **Confidence**: Medium — BCSJ 1976がEP-08aの要件を部分的に満たしていることは推論を含む（`tentative_citation`は不要だが確認が必要）。
* **注記**: EP-01aおよびEP-04aとバンドル充填（BCSJ 1976が複数EPを同時に前進させた可能性）。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: Kochi, J. K. *Organometallics in Organic Synthesis*（総説），1975年前後 — Tamura-Kochi系（Fe, Cu触媒）とNi-dpe系の比較的文脈が総説レベルで整理された。`tentative_citation`
* **充填確立点**: Tamao, K.; Sumitani, K.; Kiso, Y. et al. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — Full Paperにおいてn-BuMgBr + PhClを共通基質とし、[NiCl₂(dpe)]系とTamura-Kochi系（Fe触媒）の収率・選択性を直接比較するデータが提供された可能性がある。
* **充填の性質**: Partial — Tamura-Kochi系との shared substrate 並行実験データの提供がFull Paper 1976で実施されたかは文献確認が必要。Corriu-Masse系との比較はいくつかの総説で扱われた。
* **Confidence**: Medium — Full Paper 1976がTamura-Kochi系との比較データを含む可能性は高いが、EP-09aの「2×3表形式の並行実験」という要件水準での充填は確認が必要。
* **注記**: SRG-6（先行研究との数値比較欠如）の充填として機能するが、Corriu-Masse（Ni(acac)₂）との詳細な基質スコープ比較は1975–1980年代の総説を通じて間接的に充填されたパターンも考えられる。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 | EP-01a, EP-04a, EP-08a, EP-09a | VQ-2→3 | 1976 | High |
| 2 | Hayashi, Tajika, Tamao, Kumada, *J. Am. Chem. Soc.* 1976, 98, 3718–3719 | EP-03a, EP-06a | VQ-3 | 1976 | Medium |
| 3 | Kumada et al., *J. Organomet. Chem.* ca. 1978, Ni中間体機構論文 | EP-06a, EP-03a | VQ-3 | 1978頃 | Medium |
| 4 | Sekiya & Ishikawa, *J. Organomet. Chem.* 1976, 118, 349–354（または同等の境界試験論文） | EP-07a | VQ-2 | 1976頃 | Medium |
| 5 | Morrell & Kochi, *J. Am. Chem. Soc.* 1975, 97, 7262–7270（または同等のNi活性種同定論文） | EP-02a | VQ-2（RI-02前進） | 1975頃 | Low |

**注：** 順序5はConfidence Lowのため本来選定外だが、EP-02a（黒色析出物・活性種同定）が現代のNi触媒均一/不均一識別議論において重要EPであることから参考記載として残す。実際の検証作業では文献確認後に差し替えが必要。

---

**選定理由：**

第1位のTamao et al. BCSJ 1976は、1972年communicationのFull Paper展開として原著者グループが執筆した最重要充填論文であり、EP-01a（収率報告基盤の統一）、EP-04a（cross:homo選択性の定量）、EP-08a（再現性の向上）、EP-09a（先行法との比較）の4EPを単一論文でバンドル充填する可能性が高い。VQ-2要件（RI-01, RI-07）のうちRI-01を解消し、VQ-3への道筋を開く鍵論文と位置づけられる。自己充填パターン（Kumadaグループ）の代表例でもある。

第2位・第3位は機構解明に関わるEP（EP-03a, EP-06a）を充填する論文群であり、これらはVQ-3（Mechanism）要件の充填を担う。1976年の不斉カップリング論文（JACS 1976）は[NiCl₂(chiraphos)]系を用いた機構的研究であり、[NiCl₂(dpe)]系との類推を通じてNi(II)/Ni(0)均一系サイクルの妥当性を間接的に実証した。第4位のEP-07a充填論文はRI-07（VQ-2のもう一方のFatal項目）を解消する。これらをカバーすることでVQ-1→VQ-2→VQ-3の階段状充填が実証できる。

バンドル充填効率：第1位論文が4EP（EP-01a, EP-04a, EP-08a, EP-09a）を同時充填する可能性があり、5報の選定リストで9EPすべてに充填候補が対応する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件（RI-01解消）: EP-01a → 1976年 [Tamao et al., BCSJ 1976] 自己充填（Full Paper化）
- VQ-2 要件（RI-07解消）: EP-07a → 1976年前後 [Sekiya & Ishikawa または同等論文] 技術駆動充填
- VQ-3 要件（RI-04前進）: EP-04a → 1976年 [Tamao et al., BCSJ 1976] 自己充填（Full Paper化）
- VQ-3 要件（RI-06前進）: EP-06a → 1978年前後 [Kumadaグループ機構論文] 自己充填
- VQ-3 要件（RI-03前進）: EP-03a → 1976–1982年 [Hayashi et al. JACS 1976 → Tetrahedron 1982] 技術駆動充填（³¹P NMRの普及）
- VQ-3 要件（RI-02前進）: EP-02a → 1975–1978年 [Ni活性種同定論文（間接系）] 分野横断充填
- VQ-4 要件（RI-08解消）: EP-08a → 1976年 [BCSJ 1976] 自己充填（部分的）
- VQ-4 要件（RI-09解消）: EP-09a → 1976–1980年 [BCSJ 1976 + 総説] 自己充填 + レビュー
- CLA（RI-05前進）: EP-05a → 1980年前後（TON体系化）または **未充填**
- VQ-2 要件（RI-01補完）: EP-08a（cis:trans比率統計）→ 1976年 [BCSJ 1976] 部分充填

---

**階層-時間対応の評価：**

VQ-2要件（RI-01, RI-07）とVQ-3要件（RI-04, RI-06, RI-03）の充填はほぼ同時期（1976年）に集中しており、VQ階層が上がるほど充填が遅延するという仮説への支持は限定的である。これはKumadaグループが自己充填（Full Paper, 機構論文）として複数VQ層のEPを同時に前進させたためである。ただしVQ-3のRI-03（中間体直接観測）とRI-06（類推検証）は技術的困難から1978–1982年まで充填が遅れており、この部分は仮説と一致する。VQ-4要件（RI-08: 統計的再現性）は現代の標準に達するまで長期未達であり、これも仮説を部分的に支持する。

**特筆すべきパターン：**

- **自己充填の集中**：SRG-3（EP-07a除く）の充填はほぼ全てKumadaグループ（Tamao, Hayashi, Kumada）による後続論文で実現した。原著者グループが1972–1982年の10年間に系統的に充填を行ったことは、communicationが「研究プログラムの告知」として機能していたことを示す。
- **バンドル充填**：BCSJ 1976（Tamao et al.）は推定4EP（EP-01a, EP-04a, EP-08a, EP-09a）を同時充填する効率的なバンドル充填の事例。
- **技術駆動充填**：EP-03a（³¹P NMRリアルタイム観測）とEP-06a（低温NMRによる中間体同定）は分析機器の普及が充填を可能にした典型例であり、充填年が1978–1982年に集中していることと一致する。
- **長期遅延充填（未充填候補）**：EP-05a（TON明示）とEP-01aの現代的要件（応答係数・キャリブレーション曲線の完全開示）は、出版インセンティブ構造の不整合から長期間充填されなかった可能性がある（§Eで詳述）。
- **パラダイム転換充填**：EP-07a（sp³基質の排除）に関しては、Ni-dpe系でのsp³基質失敗実験の独立論文よりも、Pd触媒（根岸、鈴木、辻）によるsp³基質への拡張というパラダイム転換によって「問いの枠組みが変わった」側面がある（sp³基質にはNi-dpeではなくPdを使う、という実用的解決）。
- **著者回顧との照合**：Kumada 1980（Pure Appl. Chem.講演）および田守（Tamao）の2002年回顧的mini-review（`papers/ep/discussion/tamao2002/`に格納）では、Kumada反応の「significant features」として収率・選択性・β-水素安定性・塩化物反応性・配位子効果が言及されているが、cross:homo比率の定量的証拠（EP-04a）やTON（EP-05a）の不在は著者自身の回顧では「欠落」として認識されていない。これはStage 3 §4で指摘した「分野の内部者には不可視の構造的不在」の直接的証拠として記録価値がある。UQSが抽出したEP-04a（RI-04）とEP-05a（RI-05）は著者回顧において「あえて省略された問い」としてではなく「当然満たされた要件」として無言のうちに通過した可能性があり、これはUQSの発見的価値を示す。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

EP-05a [Quantitative-ranking substantiation pack — TON明示]:

* **未充填の理由**: インセンティブ構造の不整合 + 関心の欠如。1972年論文の各エントリーから計算可能な理論TON（Example 1：[NiCl₂(dpe)] = 0.39 mmol, m-DCB = 53.9 mmol → TON ≈ 138; footnote aの最低触媒量0.001では理論TON ≈ 1000）は「自明な計算」として独立論文の主題にならない。Kumadaカップリングの応用研究は収率・基質スコープ・立体選択性という「化学的新規性」に焦点を当て、触媒効率のベースライン確立（TON計算の系統化）は出版インセンティブを持たなかった。さらに「The experimental conditions are not necessarily optimum」という著者の免責が、条件最適化（→高TON化）を後続研究の課題として外置きし続けた。
* **発見的意義**: あり。Kumada反応が「useful preparative method」として半世紀にわたって化学コミュニティに受容され続けたにもかかわらず、1972年論文のTable Iエントリーに対するTON計算を主題とした独立論文が存在しない可能性は、「合成有用性の宣言が触媒効率の定量的評価を免除するインセンティブ構造」の存在を示す。UQSはこの構造的不在を54年後に検出した（N=1の観察）。
* **将来の充填可能性**: 高。計算は既存データから即座に可能（TON = 生成物mol / Ni mol）。現代のGreen Chemistry文脈（E-factor、原子効率、触媒負荷量最適化）においてKumadaカップリングのTON計算を系統的に行ったメタ分析論文が作成されれば充填される。ただし「1972年論文のTable Iに対するTON計算」という文脈での充填は動機が薄く、充填は実質的には「現代的再評価論文」の形をとる可能性が高い。

---

EP-01a [Reporting-coherence pack — glpc内部標準の完全開示]:

* **未充填の理由**: 分野慣行（習慣的解消 + 部分解消）。glpc / 孤立収率の混在問題はFull Paper化（BCSJ 1976）によって実質的に解消されたが、glpc内部標準の応答係数・キャリブレーション曲線の完全開示という現代的要件（現在のJACSが要求する水準）は1976年時点では標準的でなく、充填は「部分的」に留まった可能性が高い。独立論文として充填される性格ではなく、Full Paper化の副産物として自動解消するはずだったが、現代的分析報告基準との乖離が残る。
* **発見的意義**: あり（限定的）。この不在は「報告形式問題がcommunication→Full Paper遷移で自動解消される」という慣習的想定が現代の再認定基準では不完全であることを示す事例として記録できる。RI-01の「習慣的解消パターン」の限界事例。
* **将来の充填可能性**: 高。現代の自動化glpc/HPLC定量システム（GCの検出器応答係数データベース、内部標準法の標準化）が普及しており、Kumada 1972の条件再現実験で完全充填が可能。ただし動機（54年前の論文の分析条件再現）は薄い。

---

**EP-02a（Ni活性種同定）の未充填残存部分：**

EP-02a [Identity / purity substantiation pack]:

* **未充填の理由**: 技術的困難 + 関心の転換。[NiCl₂(dpe)] 触媒の反応後回収・黒色析出物のXRD/ICP-MSによるNi⁰/Ni(II)識別という1972年のoriginal条件に対応した実験は、技術的には1980年代に可能になったが、触媒活性種議論はその時点では Pd触媒（均一系明確）に焦点が移行しており、Ni触媒の均一/不均一問題は「resolved enough」として扱われた。
* **発見的意義**: あり。黒色析出物（U-2）がNi⁰であった可能性を54年後も完全には排除できないことは、eqs 2–4の均一系サイクルが「実証された機構」ではなく「十分に受容された working hypothesis」であることを示す。UQSのU-2検出はこの構造的不在が分野内部では不可視であったことの記録。
* **将来の充填可能性**: 中。現代のin situ X線吸収分光（XAS）、高分解能TEM、ICP-MSを用いれば[NiCl₂(dpe)] / n-BuMgBr / PhClの反応進行中のNi種を直接同定できる。計算化学（DFT）との組み合わせも可能。ただし「1972年論文の実験条件を再現する」動機がなければ、充填は現代Ni触媒機構研究の文脈で間接的にしか進まない。

---

**VQ階層逆転の診断：**

未充填EPと充填済みEPの分布を確認すると、以下のパターンが観察される：

- **未充填（長期遅延）**：EP-05a（RI-05: TON = 実用性指標）、EP-01a現代的要件（RI-01: 報告形式）、EP-02a残存部分（RI-02: 触媒同定）
- **充填済み（比較的早期）**：EP-03a（RI-03: 中間体観測）、EP-06a（RI-06: 類推検証）、EP-07a（RI-07: 境界試験）

この分布は部分的にVQ階層逆転パターンを示す。**高VQ要件（RI-03, RI-06: 機構的検証）は1976–1982年に充填された一方、低VQ要件（RI-01: 報告形式、RI-08: 再現性）はFull Paper化で名目上解消されたが現代水準では未達**という構造が見られる。さらに**EP-05a（RI-05: TON）という実用性定量化は最も充填されにくい**ことが確認される。これは「科学的に困難な問い（高VQ）は研究コミュニティが取り組むが、定量的ベースラインの確立（低VQ / 実用性の数値化）は出版インセンティブの欠如から放置される」という逆転パターンの合成化学版事例として記録価値がある。

---

*以上、Stage 4 v2 run4 完了。*
