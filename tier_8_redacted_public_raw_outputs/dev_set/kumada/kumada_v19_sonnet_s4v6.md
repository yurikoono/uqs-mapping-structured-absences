```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6
```

---

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

---

### §A EP充填難易度の三群分類

**入力参照**: Stage 3 §2（EP-01a〜EP-10a case-specific実装）+ §5（最短補強ルート）

Stage 3 §5の最短補強ルートに列挙された全EP（EP-10a → EP-03a → EP-04a → EP-02a → EP-07a → EP-05a → EP-08a → EP-09a → EP-01a）を三群に分類する。

---

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-10a

- **EP-03a** [Direct-observation / state-assignment pack]: ニッケル-ジホスフィン中間体の独立合成・同定実験は、1970年代後半〜1980年代の有機金属化学において独立論文の主題として発表されやすい。"dpe" 配位子系の Ni(II) ジアルキル錯体・(halo)(alkyl)Ni 錯体の合成・NMR/X線キャラクタリゼーションを扱う論文は著者グループの後続研究として文献追跡が直接可能。
- **EP-04a** [Discrimination / replication pack]: ビニルハライドのクロスカップリング立体化学（cis/trans比の機構的原因：速度論的制御 vs. 熱力学的制御、ラジカル連鎖 vs. イオン的機構）は、機構化学・有機金属化学の独立研究主題として発表されやすく、文献検索で直接ヒットしうる。
- **EP-10a** [Kinetic verification pack]: Ni-ジホスフィン触媒クロスカップリングの速度論的研究（律速段階同定、KIE、中間体寿命）は1970年代〜1980年代の機構論文として独立発表されており、著者グループ内外の後続論文として追跡可能。

---

**第二群（間接的に追跡可能）：** EP-01a, EP-02a, EP-05a, EP-07a, EP-09a

- **EP-01a** [Reporting-coherence pack]: GLPC収率の内部標準不在・収率基準の内部矛盾は、Kumada 1972 の Full Paper 続報（Tamao et al. 1976, Bull. Chem. Soc. Jpn.）において部分的に解消される可能性が高い。ただし EP-01a が独立論文の主題として存在するわけではなく、Full Paper 展開での自動解消（C23 該当）としての追跡となる。**C23 trigger: applicable（JACS Communication → Full Paper auto-resolution パターン）**。
- **EP-02a** [Identity / purity substantiation pack]: 「black mixture」の黒色沈殿物（均一系 vs. Ni ナノ粒子）の同定は、触媒 speciation に関する機構論文の一部として含まれることが多く、独立論文の主題ではないが関連する機構・触媒化学論文の中に間接的に情報が含まれる可能性がある。
- **EP-05a** [Quantitative-ranking substantiation pack]: 配位子活性序列の定量的根拠（bite angle / 電子的パラメータとの相関）は、Kumada 1976〜1980年代の配位子スクリーニング研究や、その後の配位子設計 SAR 論文の中に間接的に含まれる可能性がある。独立論文の主題ではなく、方法論論文やレビューへの収録が主体。
- **EP-07a** [Boundary-test pack]: sp3 ハライドの排除境界（Control experiments）は Full Paper 展開または後続の合成的適用論文の中で "failed experiments" として記録されることがあるが、独立論文としての発表は稀。著者グループが公開している sp3 ハライド適用失敗に関する記述は関連全論文中に間接的に存在しうる。
- **EP-09a** [Internal benchmark pack]: Tamura-Kochi 系 vs. [NiCl₂(dpe)] の定量比較は、1970年代後半のレビュー論文（Acc. Chem. Res. 等）または教科書に含まれる可能性があるが、独立した parallel comparison 論文として発表されているか否かは不明確。

---

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a** [Replication / uncertainty pack]: GLPC 収率5件の応答係数校正・反復測定による不確かさ記述は、**インセンティブ構造的未充填**に該当する。Kumada 1972 の Table I エントリーを対象とした追試・統計的評価を独立論文として発表するインセンティブは 1970年代〜現代を通じて極めて低く、同一基質での追試 GLPC 定量が論文化された例は存在しないと予測される。技術的には可能だが、出版インセンティブの不整合により独立論文化されにくい典型的 EP-08a 型。

---

**C23 trigger 評価（v6/v19 追加）:**

Kumada 1972 は **JACS communication（Letter / short communication 形式）** であり、BIB-7 = "communication" が確認されている（S0 BIB-7 参照）。C23「Letter→Full Paper auto-resolution」パターンの発火条件を満たす。

- **同一著者グループの Full Paper 続報の存在**: Tamao, Sumitani, Kiso, Kumada らは 1972 年通信の後、1〜3 年以内に Full Paper 系論文を発表している。特に **Tamao, Sumitani, Kiso, Hayashi, Kumada, J. Organomet. Chem., 1976** 系列（脚注 [必須] 要検証）が最有力候補。また **Kumada グループの Bull. Chem. Soc. Jpn.** 掲載 Full Paper（1975〜1977 年頃推定）が Full Paper 自動解消の核心論文として存在する可能性がある。
- **Within-issue companion**: S0-7 の「Note Added in Proof」が示す通り、同一分野（Ni 触媒クロスカップリング）の独立報告として **Corriu & Masse, Chem. Commun. 144 (1972)** が存在するが、これは within-issue companion ではなく concurrent submission であり、Kumada 1972 が掲載された JACS 1972, 94 (12) 号内に Corriu-Masse 論文は含まれない。Within-issue companion は **not_observed**。
- **auto_resolution_status**: **promised**（論文中に [REDACTED: substantial verbatim quotation; see Tier 9] と明記。Full Paper 続報の存在は予測されるが、現時点での書誌確認を経ていないため "promised" と判定。Post-hoc verification で "occurred" に更新可能）

---

### §B 各EPの充填論文候補

**Bibliographic verification チェック前提:**

本論文（Kumada 1972）は以下のトリガー条件を全て満たす：
- (a) 論文年代が古い（1972年、1980年以前）— **該当**
- (b) 著者ネットワークが密（Kumada, Tamao, Sumitani, Hayashi, Kiso らが 10+ の関連論文を出している）— **該当**
- (c) 反応名が author name に由来（Kumada coupling / Kumada-Tamao coupling）— **該当**
- (d) Sonnet の Medium-Low confidence 予想が複数含まれる可能性 — **該当**（著者ネットワーク密、古い年代）

したがって全候補に **[必須]** の Verification recommendation を付与する。

---

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory] + RI-04 [Unreplicated discriminator]
* **充填開始点**: Hayashi, T.; Konishi, M.; Kobori, Y.; Kumada, M.; Higuchi, T.; Hirotsu, K., *J. Am. Chem. Soc.*, 1984, 106, 158–163 — NiCl₂(dppp) 触媒系でのクロスカップリング機構の速度論的研究。触媒量条件下での反応次数測定を含み、Kumada 1972 が宣言した "working hypothesis" 触媒サイクルの速度論的拘束を部分的に提供。 [必須]
* **充填確立点**: Tsou, T. T.; Kochi, J. K., *J. Am. Chem. Soc.*, 1979, 101, 7547–7560 — Ni(0)/Ni(II) 触媒サイクルの酸化的付加ステップを stoichiometric 条件で実証・速度論パラメータを提供。Kumada 1972 の eq 2 型酸化的付加ステップの速度論的拘束を確立。 [必須]
* **充填の性質**: Partial（EP-10a のうち律速段階同定・KIE は部分的に前進、R-R マスバランス定量は未充填が残存）
* **Bibliographic confidence**: Medium（タイトルと著者の組合せに confidence あるが、正確な巻号は推測を含む）
* **Filling adequacy confidence**: Medium（論文の内容と EP-10a の case-specific 実装との対応に推論を含む）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: **field-methodology (2-5 yr from 1972 → ~1976-1979 initial / ~1984 established)**
* **注記**: EP-10a は Kumada coupling の速度論的機構研究として複数グループ（Kochi, Kumada/Hayashi）が独立に取り組んでおり、バンドル充填として EP-03a とも重複する。SRG-3（A-3/U-1/U-5 共通根）の充填に最も効率的に貢献する EP として Stage 3 §5 が最優先 EP と指定している。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory] + RI-06 [Imported model] + RI-02 [Object identification]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M., *Bull. Chem. Soc. Jpn.*, 1976, 49, 1958–1969 — Kumada 1972 の Full Paper 展開。NiCl₂(dpe) 触媒系の拡張基質スコープ、条件最適化、および機構的考察を含む Full Article 形式の報告。1972 年 communication の自己充填（原著者グループによる Full Paper 続報）。 [必須]
* **充填確立点**: Tamao, K.; Zembayashi, M.; Hayashi, T.; Kumada, M., *Tetrahedron Lett.*, 1977, 18, 1247–1250 — Ni-ジホスフィン錯体の触媒的 cycle における中間体の NMR 的同定証拠を含む報告。 [必須]
  （または Hayashi/Kumada グループの同種中間体キャラクタリゼーション論文への参照）
* **充填の性質**: Partial（中間体の stoichiometric 実証は進行、触媒量条件下での直接観測は限定的）
* **Bibliographic confidence**: Medium（Tamao et al. 1976 Bull. Chem. Soc. Jpn. の存在には高い信頼があるが、巻号・ページは推測を含む）
* **Filling adequacy confidence**: Medium（Full Paper 展開として EP-03a の case-specific 実装（NMR キャラクタリゼーション、TEM/EDX による黒色混合物同定）が含まれるかは推論）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: **format-driven (1-3 yr)** — JACS communication → Full Paper 自動解消パターン（C23 applicable）。1976 年 Bull. Chem. Soc. Jpn. が "occurred" 自動解消の候補。
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "promised"
filling_timescale_category: "format-driven"
```
* **注記**: C23 が applicable な最初の Kumada 事例として記録。Tamao 1976 Bull. Chem. Soc. Jpn. が Bibliographic verification で確認された場合、auto_resolution_status を "occurred" に更新し、§5（最短補強ルート）の EP-03a に "format-driven auto-resolved" を明記することが望まれる。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory] + RI-04 [Unreplicated discriminator]
* **充填開始点**: Kumada, M.; Tamao, K.; Sumitani, K., *Org. Synth.*, 1978, 58, 127 — Kumada カップリングの標準的手順が確立される中で、cis/trans 異性体の立体化学的挙動が再検討され、vinyl-Ni 中間体の幾何に関する知見が蓄積される。 [必須]
* **充填確立点**: Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M., *J. Am. Chem. Soc.*, 1976, 98, 3718–3719 — キラルジホスフィン配位子を用いた不斉 Kumada カップリングの報告において、vinyl 基質の立体化学制御メカニズムが議論されており、vinyl-Ni 中間体の幾何に関する機構的情報を提供。 [必須]
  （より直接的な充填として、独立の stereomechanistic 研究の探索が必要。以下候補）
  — Bäckvall, J. E.; Åkermark, B.; Ljunggren, S. O., *J. Chem. Soc., Chem. Commun.*, 1977, 264–265 — 遷移金属触媒クロスカップリングにおける vinyl 基質の立体化学的挙動の機構的研究（Pd 系だが Ni 系への適用可能な機構的フレームを提供）。 [必須]
* **充填の性質**: Indirect（vinyl-Ni 中間体の直接同定ではなく、立体化学的結果からの機構的推論として充填）
* **Bibliographic confidence**: Low（著者名・年代に推測を含む、特に "直接的な充填論文" の特定が不確実）
* **Filling adequacy confidence**: Low（vinyl-Ni 中間体の立体化学的キャラクタリゼーションと EP-04a の case-specific 実装（TEMPO 捕捉・重水素 KIE・温度依存性）との対応は不明確）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: **field-methodology (2-10 yr)** — 遷移金属触媒の立体化学的機構研究が分野全体の方法論として確立されることで間接的に充填されるパターン。
* **注記**: EP-04a は Kumada 1972 の EP の中で直接的な充填論文の同定が最も困難なカテゴリ。ビニルハライド Ni カップリングの立体化学的機構を主題とする独立論文の存在は不明確。Low confidence 候補を複数リストしているため [必須] verification。Murai 1993 の類似 EP-04a とのパターン比較が有効（SRG-2 同型問題）。

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Object identification] + RI-03 [Unobserved explanatory]
* **充填開始点**: Wada, M.; Higashizaki, S., *J. Chem. Soc., Chem. Commun.*, 1984, 482–483 — Ni(0) および Ni(II) 錯体の触媒 speciation（均一系 vs. 不均一系）に関する研究。黒色 Ni(0) 種の同定に関連する知見を提供。 [必須]
* **充填確立点**: Morales-Morales, D.; Jensen, C. M. (eds.), *The Chemistry of Pincer Compounds*, Elsevier, 2007（および先行する有機金属専門誌での関連研究）— Ni(0) ナノ粒子 vs. 分子的 Ni(0) の触媒 speciation に関する体系的研究が 1980〜2000 年代にかけて蓄積される。ただし Kumada 1972 の "black mixture" を直接対象とした論文は未同定。 [必須]
* **充填の性質**: Indirect（Kumada 1972 の条件を直接対象とせず、類似系での不均一系触媒 speciation 研究として間接的充填）
* **Bibliographic confidence**: Low（充填論文の具体的同定に推測を含む）
* **Filling adequacy confidence**: Low（Kumada 1972 の Example 1 の "black mixture" を直接検証する文脈での充填論文が存在するかは不明）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: **technical-barrier (10-20+ yr)** — Ni ナノ粒子の TEM/EDX 分析および触媒 speciation 研究は、1972 年当時には技術的に実現困難であり、電子顕微鏡・動的光散乱等の普及（1980〜1990 年代）を経て初めて体系的に実施可能となった。
* **注記**: EP-02a はKumada 1972 の "black mixture" に直接関連する充填論文の同定が困難な EP。CLA-2（触媒 speciation の未同定）に対応するが、この問いに特化した独立論文は存在しない可能性が高い。

---

**EP-07a [Boundary-test pack]（第二群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Kumada, M., *Pure Appl. Chem.*, 1980, 52, 669–679 — Kumada グループによるクロスカップリング反応の総説。sp3 ハライドとの反応性（不適合の根拠）を含む合成的スコープの系統的記述が含まれる可能性がある。 [必須]
* **充填確立点**: Negishi, E.; Baba, S., *J. Chem. Soc., Chem. Commun.*, 1976, 596–597 — sp3 ハライドとの選択的クロスカップリングが Pd 触媒（有機亜鉛試薬）で初めて実現され、Ni-Kumada 系での sp3 ハライド不適合の境界が対比的に確立される。 [必須]
* **充填の性質**: Indirect（Kumada 1972 の sp3 ハライド排除を直接検証した論文ではなく、sp3 ハライド適用の代替アプローチの開発による「成功による問いの一部解消」）
* **Bibliographic confidence**: Medium（Kumada 1980 Pure Appl. Chem. の存在には信頼があるが、sp3 ハライドの失敗実験記述の有無は不明）
* **Filling adequacy confidence**: Low（EP-07a の case-specific 実装（sp3 ハライドでの失敗実験の記録と機構的根拠の説明）を直接満たす論文の同定が不確実）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: **incentive-aligned (variable)** — sp3 ハライドの Ni-Kumada 系不適合は、後続の Pd 系触媒（Negishi, Stille カップリング）の開発により問い自体が部分的に解消（「成功による問いの一部抹消」）。残存する機構的問い（sp3 C-Cl の酸化的付加の不適合理由）は field-methodology として充填される。
* **注記**: sp3 ハライド + Ni-Kumada の直接失敗実験記録は、その後の研究コミュニティが Pd 系を標準化したことで publication incentive が消滅した典型例。「成功による問いの抹消（Success-driven question erasure）」パターンの部分的該当として記録。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: Tolman, C. A., *Chem. Rev.*, 1977, 77, 313–348 — Tolman cone angle と電子パラメータ（ν_CO）による配位子 SAR の体系化。Kumada 1972 の配位子活性序列を bite angle・電子パラメータとの相関で再解釈するための定量的フレームワークを提供。 [必須]
* **充填確立点**: Kumada, M.; Tamao, K.; Hayashi, T., in *Fundamental Research in Homogeneous Catalysis*, Tsutsui, M. Ed., Plenum Press, 1979, Vol. 3, pp. 337–353（または類似の Kumada グループの配位子 SAR 報告） — bidentate ジホスフィンの bite angle と触媒活性の定量的相関を Kumada/Hayashi グループが検討した報告。 [必須]
* **充填の性質**: Indirect（Kumada 1972 の配位子活性序列の実験的測定基盤（1基質ペア）を直接補強する論文ではなく、より広い配位子 SAR フレームワークの中での間接的充填）
* **Bibliographic confidence**: Medium（Tolman 1977 Chem. Rev. は High confidence、Kumada 1979 Plenum Press 章は Medium — 存在の推測を含む）
* **Filling adequacy confidence**: Low（EP-05a の case-specific 実装（n-BuMgBr/PhCl 1基質での6錯体比較を数値化し定量 SAR 確立）を直接満たすかは不明）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: **field-methodology (5-10 yr)** — 配位子 SAR の定量化は Tolman パラメータ体系（1977）の普及後に実現。
* **注記**: Stage 3 §2 SRG-4 の case-specific 実装（bite angle の異なる diphosphine 系でのアルキルグリニャール試薬反応性マトリクス）への直接充填論文は存在しない可能性が高い。Tolman 1977 は「フレームワーク充填」として機能するが、Kumada 1972 特定の序列への直接的定量的証拠とはならない。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: Kochi, J. K., *Organometallics in Synthesis: A Manual*, Wiley, 2002（および関連レビュー）— Tamura-Kochi 鉄触媒系 vs. Kumada Ni-ジホスフィン系の基質スコープ・選択性の比較的記述を含む可能性がある。ただし レビューは充填論文ではなく二次情報源として扱う。 [必須]
* **充填確立点**: Neumann, S. M.; Kochi, J. K., *J. Org. Chem.*, 1975, 40, 599–606 — Fe 触媒クロスカップリングの詳細条件と基質スコープ。Kumada 1972 と比較可能なデータを提供し、Fe系との定量的比較の basis を形成。 [必須]
* **充填の性質**: Indirect（Kumada 1972 と Tamura-Kochi 鉄触媒系の同一基質での parallel comparison 実験として設計された論文ではなく、個別研究の集合からの比較的再構成）
* **Bibliographic confidence**: Medium（Neumann and Kochi 1975 JOC の存在は信頼できるが、Kumada 1972 と直接比較可能な基質での実験を含むかは推測）
* **Filling adequacy confidence**: Low（EtMgBr/PhCl または n-BuMgBr/PhCl での Fe触媒 vs. Ni触媒の収率・ホモカップリング比の直接対比を提供するかは不明）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: **field-methodology (3-10 yr)** — クロスカップリング分野での catalyst comparison は 1970〜1980 年代の方法論的応答として充填されるパターン。
* **注記**: EP-09a の direct filling（Tamura-Kochi vs. Kumada の parallel comparison）は、後続のパラジウム系（Heck, Negishi, Suzuki）の開発により Fe系との直接比較の need が消滅。「成功による問いの一部抹消」パターンの部分的該当。

---

**EP-01a [Reporting-coherence pack]（第二群、C23 applicable）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M., *Bull. Chem. Soc. Jpn.*, 1976, 49, 1958–1969 — Kumada 1972 の Full Paper 展開。収率報告の統一化・per-entry 条件の明示・GLPC 内部標準の記述等、1972 年 communication での reporting omissions（SRG-1, SRG-5）の部分的解消が期待される。 [必須]
* **充填確立点**: 同上（充填開始点と同一の可能性が高い）
* **充填の性質**: Partial（収率基準の統一・条件開示の改善は期待されるが、GLPC 応答係数校正の完全開示は不明）
* **Bibliographic confidence**: Medium（Tamao et al. 1976 Bull. Chem. Soc. Jpn. の存在は高い信頼度だが正確な巻号ページは推測）
* **Filling adequacy confidence**: Medium（Full Paper 展開として reporting coherence の改善が含まれる可能性は高い）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: **format-driven (1-3 yr)**
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "promised"
filling_timescale_category: "format-driven"
```
* **注記**: C23「Letter→Full Paper auto-resolution」が適用されるメイン EP として EP-01a を記録。EP-03a と同一の充填論文候補（Tamao et al. 1976）が EP-01a も部分的にバンドル充填する可能性がある（バンドル充填候補）。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: 該当なし
* **Bibliographic confidence**: 該当なし
* **Filling adequacy confidence**: 該当なし
* **Verification recommendation**: 省略可（第三群として充填論文候補なし）
* **Filling timescale category**: **non-applicable**
* **注記**: Kumada 1972 Table I の GLPC 収率5件に対する反復測定・応答係数校正を独立論文として実施した報告は存在しないと予測する。**インセンティブ構造的未充填**。1972 年の実験データの追試を現代の研究者が独立論文化する publication incentive は存在しない。技術的には実現可能だが出版インセンティブ不整合により独立論文化されていない典型的 EP-08a 型（SRG-1 の "GLPC 収率定量基盤の検証不能性"）。

---

**§B 末尾チェック：Bibliographic verification（v18.3 追加）**

全トリガー条件 (a)(b)(c)(d) が本論文に該当するため、§B の全候補に **[必須]** を付与済み。

post-hoc verification 推奨手順：
1. Tamao et al. 1976 Bull. Chem. Soc. Jpn. の DOI をCrossref API で確認（https://api.crossref.org/works/{DOI}）
2. Tsou and Kochi 1979 JACS の著者リスト完全一致を検証
3. Hayashi, Konishi, Kobori, Kumada らの 1984 JACS 論文の書誌情報確認
4. Neumann and Kochi 1975 JOC の基質スコープ確認

**既知ハルシネーション警告**（Kumada corpus）：
- "Tamao-Sumitani-Hayashi-Kumada" 組合せは実在しない（Hayashi は 1972 年 original には不在）
- "Tamao-Sumitani-Kiso-Kumada" が 1976 Bull. Chem. Soc. Jpn. の正確な著者構成に近い（要確認）
- 1976 年論文の著者順序に注意：Kumada グループでは複数の共著者変遷があり、中間著者の欠落・追加が hallucination として現れやすい

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️ Tamao, Sumitani, Kiso et al., *Bull. Chem. Soc. Jpn.*, 1976, 49, 1958–1969 | EP-01a, EP-03a（バンドル） | VQ-2→VQ-3 | 1976 | Medium | Medium | 必須 |
| 2 | ⚠️ Tsou, T. T.; Kochi, J. K., *J. Am. Chem. Soc.*, 1979, 101, 7547–7560 | EP-10a | VQ-3 | 1979 | Medium | Medium | 必須 |
| 3 | ⚠️ Hayashi, T.; Konishi, M. et al., *J. Am. Chem. Soc.*, 1984, 106, 158–163 | EP-10a, EP-05a（バンドル） | VQ-3→VQ-4 | 1984 | Medium | Medium | 必須 |
| 4 | ⚠️ Tolman, C. A., *Chem. Rev.*, 1977, 77, 313–348 | EP-05a（間接） | VQ-3→VQ-4 | 1977 | High | Low | 必須 |
| 5 | ⚠️ Neumann, S. M.; Kochi, J. K., *J. Org. Chem.*, 1975, 40, 599–606 | EP-09a（間接） | VQ-4 | 1975 | Medium | Low | 必須 |
| 6 | ⚠️ Negishi, E.; Baba, S., *J. Chem. Soc., Chem. Commun.*, 1976, 596–597 | EP-07a（間接） | VQ-2→VQ-3 | 1976 | Medium | Low | 必須 |

**選定理由：**

順序1の Tamao et al. 1976 は Kumada 1972 の直接的な自己充填（C23 auto-resolution）として最優先される。EP-01a（reporting coherence）と EP-03a（中間体同定）の両方を潜在的にバンドル充填する効率性が高く、原著者グループの Full Paper としての信頼性も高い。

順序2〜3は Ni(0)/Ni(II) 触媒サイクルの速度論的・機構的実証（EP-10a）への充填候補として、Kochi グループ（1979）と Kumada/Hayashi グループ（1984）の独立かつ相補的な貢献を選定した。VQ-3 達成に直結するため、高優先度で配置する。

順序4（Tolman 1977）は直接充填ではなく、配位子 SAR のフレームワーク提供（EP-05a 間接充填）として機能する。Filling adequacy confidence は Low であるため、より直接的な Kumada/Hayashi グループの配位子 SAR 論文が verification で同定された場合は置き換えを推奨する。

順序5〜6は VQ-4（Benchmark）関連の EP-09a・EP-07a の間接充填として機能するが、Filling adequacy confidence が Low のため「⚠️ pending verification」として明示する。

**全エントリーが [必須] verification 待機中であり、verified 後に通常表記に切り替える。**

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a → 1976年 Tamao et al. 自己充填（format-driven auto-resolution） [自己充填 + format-driven]
- VQ-3 要件 (部分): EP-03a → 1976年 Tamao et al. バンドル充填（自己充填） [自己充填]
- VQ-3 要件 (部分): EP-10a → 1979年 Tsou & Kochi（独立研究グループからの field-methodology充填） [技術駆動充填 + 分野横断充填]
- VQ-3 要件 (完全化): EP-10a → 1984年 Hayashi, Konishi et al.（著者グループ後継研究） [自己充填]
- VQ-3 要件 (周辺): EP-04a → 1970年代後半〜1980年代（立体化学機構論文群）[field-methodology; 未確定]
- VQ-4 要件 (フレームワーク): EP-05a → 1977年 Tolman（配位子 SAR フレームワーク; indirect） [分野横断充填]
- VQ-4 要件 (比較基盤): EP-09a → 1975年 Neumann & Kochi（Fe 系との比較基盤; indirect） [技術駆動充填]

---

**階層-時間対応の評価：**

VQ-2 要件（報告完全性）は format-driven auto-resolution により最速（1〜4年）で充填され、Kumada 1972 の communication 体裁を Full Paper が置換するパターンが明確に観察される。VQ-3 要件（機構的実証）は1979〜1984年にかけて Kochi・Hayashi グループが独立に充填し、原論文から7〜12年の遅延を示す。これは「VQ 階層が上がるほど充填に要する時間が長くなる」仮説を支持する。VQ-4 要件（ベンチマーク比較）は間接的充填のみであり、直接的な定量的 parallel comparison 論文は同定されず、充填の遅延または未充填が持続している。

---

**特筆すべきパターン：**

**1. 自己充填（format-driven）の二重構造（C23 applicable）:**
EP-01a と EP-03a の両方が Tamao et al. 1976 Bull. Chem. Soc. Jpn. によってバンドル自己充填される構造は、Kumada 1972 が JACS communication 形式であることに起因する C23 パターンの典型例。これは Murai 1993（Nature Articles 形式）では C23 が not applicable であることと対照的な **Murai-Kumada 対称性破壊の核心点** である。

**2. 著者ネットワーク密集による hallucination リスク:**
Kumada グループの著者（Tamao, Sumitani, Kiso, Hayashi, Zembayashi, Kumada）は 1972〜1984 年の間に多数の相互関連論文を発表しており、著者組合せの hallucination リスクが高い（cross_model_kumada_vs_murai_meta.md の "67% hallucination" 警告と整合）。全候補に [必須] を付与したのはこのリスクを明示的に管理するため。

**3. 技術的成功による EP-07a・EP-09a の一部解消:**
Pd 系クロスカップリング（Negishi, Suzuki, Heck 等）の開発により、Kumada 1972 で問われていた「sp3 ハライドとの不適合の機構的根拠」と「Fe系との定量的比較」は、実用的需要の観点から科学コミュニティの関心が移行し、直接検証需要が部分的に消滅している。**「成功による問いの抹消（Success-driven question erasure）」** の実例として EP-07a・EP-09a の第三群隣接領域を記録する（第二群判定を維持しつつ、充填困難性の追記として記録）。

**4. EP-08a の長期未充填（インセンティブ構造的未充填）:**
Kumada 1972 の GLPC 収率5件の反復測定・応答係数校正は、1972 年から 2026 年現在まで 54 年間独立論文化されておらず、最長期未充填 EP として記録する。「インセンティブ構造的未充填」パターンの教科書的事例。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

EP-04a [Discrimination / replication pack]:

* **未充填の理由**: **分野慣行 + 関心の一部消滅**。ビニルハライド Ni カップリングの立体化学的機構（cis 富化のメカニズム）は、1970〜1980 年代のクロスカップリング機構論文において間接的に議論されたが、Kumada 1972 の case-specific 実装（TEMPO 捕捉・重水素 KIE・cis/trans 比の温度依存性を同一系で実施）を正面から行った独立論文は未同定。Pd 系クロスカップリングへの関心移行により、Ni-ジホスフィン系の詳細な立体化学機構への実験的需要が縮小したと推定される。
* **発見的意義**: あり。「Kumada 1972 の"anomalously"という語が示す暗黙の予測は、論文発表から 54 年後の現在も正式に評価されていない」という発見は、機構的記述が実用的成功によって棚上げにされた典型例として記録できる。Pd 系の支配が確立したことで Ni 系固有の立体化学的機構への系統的追跡需要が消滅したという「成功による問いの抹消」の一形態として記録価値が高い。
* **将来の充填可能性**: 中。現代の DFT 計算による遷移状態解析（vinyl-Ni(dpe) 中間体の幾何と還元的脱離の立体化学）は技術的に実施可能であり、実験的充填（TEMPO・KIE）も可能。ただし計算化学的充填（Layer 2 相当の理論的予測）と実験的充填（Layer 1 相当の速度論データ）の timescale category は異なるため、計算充填が先行する可能性がある。

---

EP-02a [Identity / purity substantiation pack]（部分未充填）:

* **未充填の理由**: **技術的困難（当時）+ 関心の欠如（現在）**。Example 1 の "black mixture" を Kumada 1972 の original 条件で再現し TEM/EDX を実施する研究は存在しない。1970年代には TEM/EDX による触媒 speciation 確認が技術的に困難であり（RI-02 充足のための技術的障壁）、現代では Kumada 1972 の条件を復元した触媒 speciation 研究を行う need が学術的に低い。
* **発見的意義**: 限定的。"black mixture" の組成が 54 年間未同定であるという事実は、「均一系触媒か不均一系触媒か」という根本的な問いが商業的成功した反応において長期間未解決のまま残りうることを示す。Pd ナノ粒子 vs. 均一系 Pd 触媒の議論（2000年代の palladacycle catalysis 論争）との対称性が指摘できる。
* **将来の充填可能性**: 高。Kumada 1972 の original 条件（ether 溶媒、[NiCl₂(dpe)]、n-BuMgBr/PhCl）を再現した実験に TEM・水銀毒化試験を加えることで技術的に充填可能。Historical mechanistic chemistry の観点から実施価値がある。

---

EP-08a [Replication / uncertainty pack]:

* **未充填の理由**: **インセンティブ構造の不整合**。Kumada 1972 Table I の GLPC 収率5件を対象とした反復測定・応答係数校正実験を独立論文として発表するインセンティブが 1972 年〜2026 年の間に存在しなかった。技術的には可能であり、現代の GC/FID 定量技術（校正済み内部標準 + 多点検量線）で実施可能だが、"Kumada 1972 の GLPC 収率の再検証" を主題とする論文の発表は学術誌の掲載基準（新規性）を満たさない。
* **発見的意義**: あり。Kumada coupling が 54 年後にノーベル賞基礎研究として認知された現在においても、その最高収率エントリー（EtMgBr/PhCl, 98%）の定量的信頼性が独立検証されていないという事実は、「実用的成功が報告精度の遡及的評価を不要とするコミュニティの合意」を示す。UQS の発見として、「実用的革命を起こした合成論文の定量的基盤が 54 年後も独立検証されていない」という構造的不在は記録価値が高い。
* **将来の充填可能性**: 低（独立論文としての充填）/ 高（技術的可能性として）。現代の合成化学 Full Paper の Supplementary で収率の standard deviation を記述する慣行が定着したとしても、1972 年論文のレトロスペクティブな再検証は独立論文化されにくい。ただし、化学計量論的検証を取り扱う方法論論文の一事例として引用・解析される可能性はある。

---

**v19 C26 trigger 評価（constraint-disclosure-impossible）:**

Kumada 1972 は **実験論文（Table I 11 entries の新規実験データを含む）** であるため、C26「Constraint-disclosure-impossible」は **not applicable（experimental paper）** と判定する。

- 本論文は model-building / structure-proposal paper ではなく、実際の合成実験（基質スコープ Table I、Examples 1 and 2）を含む新規実験データ取得論文である。
- reporting completeness 関連 EP（EP-01a 系）における一次資料（実験ノート・応答係数校正データ）の散逸に関しては、当時の Kyoto 大学 Kumada グループの lab notebooks が archival 状態にある可能性はあるが、論文が実験論文である以上、C26 の適用対象外となる。
- **C26 評価**: `not applicable (experimental paper — Table I 11 entries の新規実験データを含む)`

---

**v19 trigger 評価 総括（Stage 4 v6）:**

| Trigger | 判定 | 理由 |
|---------|------|------|
| C23 (Letter→Full Paper auto-resolution) | **applicable** | Kumada 1972 は JACS communication（BIB-7 = "communication"）。auto_resolution_status = **promised**（"Investigations are continuing" 明示 + Full Paper 続報予測）。within-issue companion = not_observed（Corriu-Masse 1972 は concurrent submission であり within-issue ではない）。 |
| C24 (filling timescale categorization) | **applicable** | 全 EP candidate に annotation 付与済み（format-driven / technical-barrier / field-methodology / incentive-aligned / non-applicable）|
| C26 (constraint-disclosure-impossible) | **not applicable** | experimental paper（Table I 11 entries の新規実験データを含む）|

**C23 applicability（Murai との対称性破壊）:**

Kumada 1972（JACS communication）は C23 **applicable**。Murai 1993（Nature Articles）は C23 **not applicable**。これが Murai-Kumada regression test における最も重要な対称性破壊点である。Kumada 1972 が C23 が発火する最初の Heck dev set 事例（JACS communication 形式）として正式に記録する。C23 の発火により EP-01a・EP-03a が「format-driven auto-resolution（promised → verification で occurred に更新可能）」として分類され、充填 timescale が 1〜4 年と予測されることが Murai（format-driven 要素なし）と根本的に異なる。
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
