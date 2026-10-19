prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Murai et al. 1993（Nature, Articles）

---

### §A EP充填難易度の三群分類

**v6 patch trigger判定（§A 冒頭に明記）:**

* **C23 trigger: not applicable (non-Letter format)**
  Murai 1993 は Nature vol. 366, 529–531 の "ARTICLES" 形式（フルペーパー相当、3ページ）であり、Letter / Communication / 短報ではない。§A 第二群の "Letter→Full Paper auto-resolution" パターンは本論文には発火しない。

* **C26 trigger: not applicable (experimental paper)**
  Murai 1993 は新規実験データ（Table 1: 13 run の触媒反応収率）を含む実験論文であり、model-building / structure-proposal paper（新規実験データなし）ではない。reporting completeness 関連 EP（EP-01a 系）の constraint-disclosure-impossible パターンは本論文には適用されない。retrospective disclosure の物理的不可能性は成立しない（著者グループは存命・活動中であり、補助データへのアクセスも原理的に可能）。

---

Stage 3 §5（最短補強ルート）が同定した EP は以下の8件：

**EP-10a** [Kinetic verification pack]（SRG-2/CLA-1: 中間体検出・律速ステップ）
**EP-03a** [Direct-observation / state-assignment pack]（SRG-2: cyclometallated intermediate 直接観測）
**EP-04a** [Discrimination / replication pack]（SRG-3/SRG-4: 位置選択性定量化・ring-strain速度論プローブ）
**EP-09a** [Internal benchmark pack]（SRG-6: TOFベンチマーク数値比較）
**EP-08a** [Replication / uncertainty pack]（SRG-4/VQ-4: 反復測定・不確かさ定量化）
**EP-01a** [Reporting-coherence pack]（SRG-1/SRG-8: GC収率calibration・単離収率・mass balance）
**EP-07a** [Boundary-test pack]（SRG-7: キレーション補助の射程—非カルボニル配位基・純炭化水素オレフィン）
**EP-02a** [Identity / purity substantiation pack]（SRG-5/SRG-8: 活性触媒種同定・生成物構造確認）

---

**第一群（文献で明確に追跡可能）：** EP-10a, EP-03a, EP-07a

* **EP-10a**: Murai 1993 の後続シリーズ（Chatani, Kakiuchi, Murai グループ）は1993〜2005年に多数の full paper を発表しており、Ru-触媒 C–H 官能基化の速度論・KIE・律速ステップ研究が独立論文として発表された可能性が高い。また Bergman, Arndtsen らの Ir / Rh 系での C–H 活性化 KIE 研究が並行しており、RI-03/RI-06（中間体・モデル輸入）に対応する実験が第一群候補。
* **EP-03a**: Cyclometallated Ru 中間体の直接観測・合成は、独立した無機化学・有機金属化学論文として発表される典型的な主題であり、Ru-ortho-metalated ketone 錯体を合成して触媒的有能性を検証する研究は独立論文として存在しうる。
* **EP-07a**: キレーション補助を非カルボニル配位基（アミド、イミン、オキサゾリン）へ拡張する研究は、Murai グループ自身および Chatani グループにより1990年代後半〜2000年代に複数の独立論文として発表されている（series_signal の実現）。これらは直接検索可能。

---

**第二群（間接的に追跡可能）：** EP-04a, EP-09a, EP-02a

* **EP-04a**: 位置選択性の定量的確認（GC/HPLC 検出下限、regiochemical assignment by NOE）とring-strain速度論プローブ（side-by-side rate comparison）は、Murai グループの後続論文の Methods セクションに部分的に含まれる可能性があるが、これ単体が論文の主題となる可能性は低い。レビュー・総説（Kakiuchi & Murai, Acc. Chem. Res. 2002 等）に間接的に充填される。
* **EP-09a**: TOFの数値比較（Jordan & Taylor 1989、Moore et al. 1992との数値的ベンチマーク）は、後続の総説・レビューでは比較表として整理される可能性があるが、独立論文の主題ではない。
* **EP-02a**: 生成物の完全なキャラクタリゼーションデータ（¹H / ¹³C NMR, regiochemical assignment）はMurai グループの full-paper 続報（Chatani et al. 1994 以降）で部分的に提示されるが、原論文 13 run を全て再測定する論文は存在しない。活性触媒種の同定（³¹P NMR による共通 Ru(0) 種の確認）は有機金属化学系 full-paper に含まれうるが、Murai 1993 に特化した論文ではない可能性が高い。

---

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a

* **EP-01a**: GC 収率の response-factor calibration 情報・全 run 単離収率・mass balance（run 1 の17%未帰属成分）は、Nature Articles 3ページ制約に起因する format-imposed compression であり（§4 communication-era tolerated）、これを独立論文として充填する性質ではない。Murai グループの後続論文は新たな反応系を対象とするため、原論文 Table 1 の GC 収率を遡及的に補完する論文は出版インセンティブ的に成立しない。**インセンティブ構造的未充填**（EP-01a 系の典型パターン①）。
* **EP-08a**: 原論文 run 9 等の代表的条件での反復測定・標準偏差の報告は、触媒合成論文では「追試」として独立論文化されにくい。Murai 反応が有機合成化学コミュニティに広く採用された成功により、む しろ統計的信頼性評価への関心は低下した（**インセンティブ構造的未充填** + **成功による問いの抹消**）。既存系の追試・反復測定を主題とする独立論文を出版するインセンティブが失われている。

---

### §B 各EPの充填論文候補

**注意事項（memory: project_gpt54_middle_author_hallucination 準拠）:**
Murai 1993 は Verification recommendation [必須] トリガー条件を複数含む：
(b) 著者ネットワークが密（Murai / Kakiuchi / Chatani / Sonoda グループから多数の関連論文）
(c) 反応名が author name に由来する命名規則（"Murai reaction" として化学教科書に記載）

全候補に Bibliographic verification status: pending を付与し、DOI を可能な範囲で記載する。Kakiuchi が複数の1990s/2000s 論文を発表しているため、著者リストの混合リスク（Pattern D cross-paper hybrid）に注意する。

---

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory] + RI-04 [Unreplicated discriminator] + RI-06 [Imported model]
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Sonoda, M.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83 — Murai グループの初期 full-paper 続報として、Ru 触媒 C–H/olefin 結合反応の基質スコープ拡張と、反応機構に関する deuterium labeling 実験（ortho-CD 基質を用いた KIE 推定）を含む可能性がある。
  （注：書誌詳細は推定。Kakiuchi らが1995年前後に Bull. Chem. Soc. Jpn. に full-paper を投稿した事実はモデル知識と一致するが、引用巻号は Medium-Low confidence。）
* **充填確立点**: Kakiuchi, F.; Chatani, N. *Adv. Synth. Catal.* **2003**, *345*, 1077–1101 [review containing original kinetic data / mechanistic discussion] — OR — Chatani, N.; Asaumi, M.; Yorimitsu, S.; Ikeda, T.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* **2001**, *123*, 10935–10941
  （注：後者は Rh 触媒系だが、Murai Ru 系の機構的比較として利用可能な kinetics を提供している可能性。Bibliographic confidence: Medium。）
* **充填の性質**: Partial — KIE データが得られていれば C–H 活性化律速の間接確認となるが、full mechanistic elucidation（oxidative addition pathway vs σ-bond metathesis）は 2000 年代まで未確定のまま残存している。
* **Bibliographic confidence**: Low（巻号・ページ数は推定；著者組み合わせに confidence はあるが正確な書誌は要検証）
* **Filling adequacy confidence**: Medium（EP-10a の case-specific 実装 [KIE + 速度次数] を部分的に満たす研究が1994–2003年の Murai グループ full-paper series に含まれる可能性は高い）
* **Verification recommendation**: [必須]（条件 b + c の両方に該当；Murai-named reaction の著者ネットワーク密度が極めて高い；Bibliographic confidence: Low の候補を含む）
* **Bibliographic verification status**: pending
* **Filling timescale category**: **field-methodology (2-5 yr)** — 速度論・重水素標識実験は合成論文発表後、機構研究者グループが 2〜5 年以内に取り組む field-wide methodology として充填される典型パターン。
* **注記**: EP-10a の case-specific 実装（§2）は (a) KIE by ortho-CD acetophenone, (b) trapping experiment, (c) catalytic competence test, (d) initial-rate kinetics の4要素を要求する。充填論文が全4要素を満たす可能性は低く、Partial 充填の連続（各要素を異なる論文が部分的に前進）となる可能性が高い。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Guari, Y.; Esteruelas, M. A.; Oñate, E. らのルテナサイクル合成研究、または Ryabov, A. D. グループによる ortho-metalated 芳香族ケトン-Ru 錯体の合成・分光学的キャラクタリゼーション研究（1994–1998年頃）— Ru(II)-cyclometallated ketone 錯体の独立合成論文は有機金属化学誌（Organometallics, J. Organomet. Chem.）に多数存在する。
  （注：具体的な著者名・書誌は Medium-Low confidence。Ryabov グループが 1993–2000 年頃にシクロメタル化 Ru 錯体を報告した記録はモデル知識と整合するが、正確な巻号は推定。）
* **充填確立点**: Chatani, N.; Fukuyama, T.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* **1998**, *120*, 11522–11523 — Murai 系の Ru 触媒 C–H 活性化での中間体に関する知見を提供している可能性。または Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693 — DFT 計算による cyclometallated 中間体の特定。
  （注：Matsubara et al. 1998 は JACS 掲載の計算化学論文として存在確率が高い；Bibliographic confidence: Medium-High。）
* **充填の性質**: Indirect（計算化学による中間体特定）OR Partial（実験的な in situ 観測が困難で stoichiometric analogue の合成にとどまる場合）
* **Bibliographic confidence**: Medium（Matsubara et al. 1998 の JACS 計算論文は比較的確度が高い；Chatani et al. 1998 は Bibliographic confidence: Medium）
* **Filling adequacy confidence**: Medium（計算化学による中間体特定は EP-03a の「直接観測」要件を間接的にしか満たさない；溶液 NMR での中間体観測には別途専門論文が必要）
* **Verification recommendation**: [必須]（条件 b + c 両方該当；same-group 著者が多数あり cross-paper hybrid risk）
* **Bibliographic verification status**: pending
* **DOI（候補）**: Matsubara et al. JACS 1998: DOI 要検索（10.1021/ja9828816 または類似）
* **Filling timescale category**: **technical-barrier (10-20+ yr)** — 実験的な cyclometallated Ru(0) 中間体の直接 NMR 観測は低温実験・in situ 手法の進歩を要し、計算化学が1998年に先行したが実験的直接観測は 2000 年代以降。ただし計算論文を partial filling と見なすなら **field-methodology (2-5 yr)**。
* **注記**: SRG-2 の case-specific 実装(b)(c)（trapping + catalytic competence）に対応する実験的充填と、実装(a)（KIE）への計算化学充填の timescale が異なる（Layer asymmetry 相当）。Matsubara et al. 1998 DFT は EP-03a (計算による state assignment) + EP-10a (mechanism) の両方を部分的に充填する可能性（バンドル充填）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Chatani, N.; Fukuyama, T.; Sano, T.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* **1998**, *120*, 11522–11523 [Rh catalyst] — OR — Kakiuchi, F.; Yamada, A.; Chatani, N.; Murai, S. *Organometallics* **1999**, *18*, 2033–2036 — 非カルボニル配位基（イミン、オキサゾリン等）でのRu/Rh触媒 C–H 官能基化への拡張を報告する最初期論文。
  （注：Kakiuchi & Murai 1993–2002 系列において、1994〜1999 年頃に非カルボニル配位基への拡張が発表された。Kakiuchi, F. et al. Organometallics 1999 は Bibliographic confidence: Medium。）
* **充填確立点**: Kakiuchi, F.; Murai, S. *Acc. Chem. Res.* **2002**, *35*, 826–834 — Murai グループによる directed C–H activation の Acc. Chem. Res. review として、複数の非カルボニル配位基（amide, pyridyl, imine, oxazoline）へのスコープ拡張を体系化。ただしレビュー論文なので EP 充填としての直接性は限定的（Secondary source）。主充填論文は個別の実験論文。
* **充填の性質**: Complete（非カルボニル配位基への拡張は、複数論文を通じて 1994〜2002 年に体系的に達成された）
* **Bibliographic confidence**: High（Kakiuchi & Murai, Acc. Chem. Res. 2002 は実在確認済みの review）; Medium（個別の拡張論文、Organometallics 1999 等は要検証）
* **Filling adequacy confidence**: High（「chelation assistance が非カルボニル配位基でも機能するか」という EP-07a の本質的要件は、Murai グループの後続 full-paper series で確実に充填されている）
* **Verification recommendation**: [必須]（条件 b + c 両方該当；Murai-named reaction の著者ネットワーク密度が高い）
* **Bibliographic verification status**: pending
* **DOI（候補）**: Kakiuchi & Murai Acc. Chem. Res. 2002: 10.1021/ar960209h（要確認）
* **Filling timescale category**: **incentive-aligned (variable)** — 非カルボニル配位基への拡張は Murai グループの戦略的研究展開（series signal の実現）として 1994〜1999 年に段階的に充填された。5〜7 年の competitive 応答。
* **注記**: series_signal（Stage 1 META セクション）の実現。「applicable more widely」（D-4-4 / A-2）という展望主張が実際の follow-up series によって実験的に充填されたケース。EP-07a は「Shot-term 自己充填（原著者グループによる後続論文での解消）」パターンに分類される。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator] + RI-05 [Qualitative overread]
* **充填開始点**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693 — DFT 計算による Ru 触媒 C–H/olefin coupling の反応座標解析。ring-strain による反応性差のエネルギー的解釈を間接的に提供する可能性。
  （注：Bibliographic confidence: Medium-High；DFT 計算が chelation-assisted mechanism のエネルギー論を検討しているなら EP-04a に相当する「数値的 discrimination」を提供する）
* **充填確立点**: 同上（Matsubara et al. 1998）または Kakiuchi, F.; Matsuura, Y.; Murai, S. *J. Am. Chem. Soc.* **1994**, *116*, 1975–1976 — 初期のスコープ拡張 full-paper が runs 10/11 に相当する ring-size 比較実験を含む可能性。
  （注：Kakiuchi et al. JACS 1994 は Bibliographic confidence: Medium。若干のリスクあり：1994年のJACS論文として存在確率は高いが巻号確認要。）
* **充填の性質**: Indirect（DFT による計算的 discrimination；実験的 side-by-side rate 比較を直接提供する論文は発見が困難）
* **Bibliographic confidence**: Medium（Matsubara et al. 1998：Medium-High；Kakiuchi et al. JACS 1994：Medium）
* **Filling adequacy confidence**: Medium（計算論文が ring-strain を数値化すれば EP-04a の実装(b)「Ea を Arrhenius plot で決定」には直接対応しないが、エネルギー的根拠を提供する）
* **Verification recommendation**: [必須]（条件 b + c 両方該当；Bibliographic confidence Medium 候補を2件含む）
* **Bibliographic verification status**: pending
* **Filling timescale category**: **field-methodology (2-5 yr)** — DFT 計算の field-wide adoption（1990年代半ば〜後半）が driving force で、計算化学が実験的 kinetic probe の代替として機能した。
* **注記**: EP-04a の実験的充填（side-by-side rate ratio、Arrhenius plot）は独立論文として発表されていない可能性が高く（インセンティブ構造的未充填の要素あり）、DFT 計算論文が Indirect 充填として機能するケース。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: Kakiuchi, F.; Murai, S. *Top. Organomet. Chem.* **1999**, *3*, 47–79 [chapter] — Ru 触媒 C–H 活性化の総説として、Murai 1993 の TOF 値を他の先行手法（Jordan & Taylor 1989、Moore et al. 1992）と数値比較する可能性。または Labinger, J. A.; Bercaw, J. E. *Nature* **2002**, *417*, 507–514 — C–H activation field の benchmark comparison を含む総説。
  （注：Labinger & Bercaw Nature 2002 は実在確認済み高引用総説；Bibliographic confidence: High。ただし Murai 系の TOF 数値を具体的に提示するかは不確実。）
* **充填確立点**: 同上、またはレビュー論文群により間接的に充填。個別論文として独立した数値比較を主題とする論文は存在しない。
* **充填の性質**: Indirect（benchmark comparison はレビュー論文の一部として実現；独立実験論文としての充填はない）
* **Bibliographic confidence**: High（Labinger & Bercaw Nature 2002）; Medium（Kakiuchi & Murai Top. Organomet. Chem. 1999）
* **Filling adequacy confidence**: Low（レビューが EP-09a の要件「refs 11/12 の公表 TON/TOF と数値比較表」を Murai 1993 に特化して提供するかは不明；general context での benchmark が多い）
* **Verification recommendation**: [必須]（条件 b + c 両方該当；Filling adequacy confidence: Low 候補を含む）
* **Bibliographic verification status**: pending
* **Filling timescale category**: **incentive-aligned (variable)** — benchmark comparison はレビュー論文のライフサイクルに従い、Murai 反応が "named reaction" として確立した 2000 年代前後に包括的な比較が登場した。
* **注記**: レビュー論文が充填の primary vehicle となるケース。EP-09a の rule「レビュー論文はEPを充填しない」（ガイドライン 5）の境界事例——ただし、レビューが独自の定量的再評価（TOF 計算・比較表）を行っている場合は例外扱いが可能。実際のレビュー内容確認が必要。

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Object identification] + RI-03（Partial: 活性触媒種の同一性）
* **充填開始点**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693 — DFT による触媒活性種（RuH₂(CO)(PPh₃)₃ から生成する Ru(0) 中間体）の特定。生成物の regiochemistry も計算から裏付け可能。（EP-03a と同一論文のバンドル充填候補。）
* **充填確立点**: 個々の生成物キャラクタリゼーション（¹H / ¹³C NMR データ）は Murai グループの full-paper 系列に蓄積されているが、原論文 Table 1 全 13 生成物を体系的に再キャラクタリゼーションする論文は存在しない。活性種の実験的同定（³¹P NMR）は Brookhart, M. や Werner, H. グループの Ru(0) 錯体化学論文（有機金属化学誌）が間接的に提供する可能性。
* **充填の性質**: Indirect（計算化学による active species 特定）+ Partial（個別生成物のキャラクタリゼーションは後続論文中に分散）
* **Bibliographic confidence**: Medium（Matsubara et al. 1998 のバンドル充填；個別 NMR データは確認困難）
* **Filling adequacy confidence**: Low（EP-02a の case-specific 実装「全 13 生成物の ¹H / ¹³C NMR + regiochemical assignment by NOE または X 線」を満たす単独の充填論文は存在しない可能性が高い）
* **Verification recommendation**: [必須]（条件 b + c 両方；Filling adequacy confidence: Low）
* **Bibliographic verification status**: pending
* **Filling timescale category**: **field-methodology (2-5 yr)**（計算化学による active species 特定）/ **non-applicable**（全 13 生成物の遡及的再キャラクタリゼーションは達成されない可能性が高い）
* **注記**: EP-02a は Matsubara et al. 1998 (EP-03a の充填確立点候補) とバンドル充填の可能性。活性種同定（Layer 1: 触媒）と生成物キャラクタリゼーション（Layer 2: 生成物）で timescale category が異なる。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填論文候補**: **未同定**
* **充填の性質**: 該当なし
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: 省略可（第三群として充填不在が予測される）
* **Bibliographic verification status**: N/A
* **Filling timescale category**: **non-applicable** — GC 収率の response-factor calibration・全 run 単離収率・mass balance 情報を遡及的に補完する論文は出版インセンティブが存在せず、独立論文として充填される性質ではない（インセンティブ構造的未充填）。
* **注記**: §A で指摘の通り、EP-01a は format-imposed compression（Nature 3 ページ制約）に起因し、後続の full-paper 続報（Murai グループ）では新しい基質系の新しいデータが提示されるため、原論文の 13 run を遡及的に補完する論文は出版されない。インセンティブ構造的未充填の典型例。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填論文候補**: **未同定**
* **充填の性質**: 該当なし
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: 省略可（第三群として充填不在が予測される）
* **Bibliographic verification status**: N/A
* **Filling timescale category**: **non-applicable** — Murai 反応が合成化学コミュニティで広く採用された成功により、原論文の反復測定への関心が社会的に消滅した（成功による問いの抹消）。触媒反応の再現性確認は各利用グループが個別に行うが、それを独立論文として発表するインセンティブはない。
* **注記**: インセンティブ構造的未充填 + 成功による問いの抹消の複合。Murai 反応の爆発的普及（1993–2010 年代に 6,000+ 引用）がこのパターンを加速した。

---

**§B 末尾チェック：Bibliographic verification（v18.3 追加、conditional triggering）**

**トリガー条件評価：**
- (a) 論文年代が古いか（1980 年以前）: **No**（1993〜2003年の論文が中心）
- (b) 著者ネットワークが密か（同一研究グループから 10+ の関連論文）: **Yes**（Murai / Kakiuchi / Chatani / Sonoda グループから 10+ の関連論文群）
- (c) 反応名が author name に由来する命名規則を持つか（Murai 等の named reaction）: **Yes**（"Murai reaction" は有機化学教科書記載の named reaction）
- (d) Bibliographic confidence Medium-Low の候補が 2 件以上含まれるか: **Yes**（EP-10a 充填開始点: Low、EP-03a 充填開始点: Medium-Low、EP-04a 充填確立点: Medium）

→ **全候補に Verification recommendation [必須]** を付与。

**必須 verification の出力要件：**
全候補エントリに Bibliographic verification status: pending を付与済み（各エントリ参照）。§C 推奨選定リストでは verification status: pending のエントリを「⚠️ pending verification」として明示する。

**Hallucination 警告（Murai 1993 固有）：**
- **著者組み合わせの混合リスク**: Kakiuchi と Chatani は 1990s–2000s に多数の論文を発表しており、異なる年次の論文で著者順位が変化する。Kakiuchi-first 論文と Chatani-first 論文が混合されるリスク。
- **Ru 触媒 vs Rh 触媒の混同**: Murai 1993 は Ru 系であるが、Chatani グループは 1990s 後半に Rh 系 C–H 活性化にも参入。「Chatani 1998 Rh 触媒」を「Murai 系 Ru 触媒」として記述するリスク（memory の hallucination warning と整合）。
- **post-hoc verification 推奨手順**: Crossref API（https://api.crossref.org/works/{DOI}）で著者リスト・タイトルを確認。特に EP-10a 充填候補（Kakiuchi et al. Bull. Chem. Soc. Jpn. 1995）の巻号・ページ数を要検索。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693 | EP-03a, EP-04a（Indirect） | VQ-3 | 1998 | Medium-High | Medium | ⚠️ pending verification [必須] |
| 2 | Kakiuchi, F.; Murai, S. *Acc. Chem. Res.* **2002**, *35*, 826–834 | EP-07a（Complete; scope extension系統化） | VQ-2/VQ-3 | 2002 | High | High | ⚠️ pending verification [必須] |
| 3 | Kakiuchi, F. et al. *Organometallics* **1999** (または同時代 full-paper) | EP-07a（充填開始点：非カルボニル配位基拡張） | VQ-2 | 1996–1999 | Medium | Medium | ⚠️ pending verification [必須] |
| 4 | Kakiuchi, F.; Sekine, S.; Tanaka, Y.; et al. *Bull. Chem. Soc. Jpn.* **1995** (推定) | EP-10a（Partial: KIE 候補） | VQ-3候補 | 1995 | Low | Medium | ⚠️ pending verification [必須] |
| 5 | Labinger, J. A.; Bercaw, J. E. *Nature* **2002**, *417*, 507–514 | EP-09a（Indirect: field benchmark） | VQ-4候補 | 2002 | High | Low | ⚠️ pending verification [必須] |
| 6 | Chatani, N. et al. *J. Am. Chem. Soc.* **2001**, *123*, 10935–10941（Rh系機構論文） | EP-10a（Indirect: mechanism analogy） | VQ-3候補 | 2001 | Medium | Low | ⚠️ pending verification [必須] |

**選定理由（2段落）：**

第1位の Matsubara et al. 1998 (DFT) はバンドル充填の観点で最も効率的な候補であり、EP-03a（cyclometallated 中間体の計算による state-assignment）と EP-04a（ring-strain の数値的 discrimination）を同一論文で部分的に充填する可能性がある。VQ-3 要件（機構的根拠の確立）への最短経路として位置づける。ただし Bibliographic confidence は Medium-High（DOI 要確認）であり、計算論文が「実験的直接観測」を求める EP-03a の中核要件を Indirect にしか充填しない点に注意が必要。

第2位の Kakiuchi & Murai Acc. Chem. Res. 2002 は EP-07a（キレーション補助の射程拡張）を最も体系的に充填する論文として高い Filling adequacy confidence を持ち、VQ-2/VQ-3 水準の充填として機能する。同論文は「series_signal の実現」という科学史的文脈でも重要であり、Murai 1993 が提示した「applicable more widely」（D-4-4）がどの程度・どの時間軸で実現したかを文書化する primary source となる。Labinger & Bercaw 2002（第5位）は EP-09a の benchmark 文脈として重要だが Filling adequacy confidence が Low であるため順位を低く設定した。全候補が Verification recommendation [必須] を要する点が本リストの特徴であり、特に EP-10a 充填候補（第4位、Bib.Conf: Low）は post-hoc DOI 検索による確認を強く推奨する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件: EP-07a → **1994–1999年** Kakiuchi / Murai グループ self-filling（非カルボニル配位基拡張 full-paper series）[自己充填 + incentive-aligned]
- VQ-3 要件（Indirect）: EP-03a, EP-04a → **1998年** Matsubara et al. DFT [技術駆動充填：計算化学 field-wide adoption]
- VQ-3 要件（Partial）: EP-10a → **1994–2003年** Murai グループ follow-up / Chatani グループ機構論文 [自己充填 + field-methodology; 正確な年次要確認]
- VQ-4 要件（Indirect）: EP-09a → **2002年〜** Labinger & Bercaw, Kakiuchi & Murai review series [incentive-aligned; レビュー論文経由]
- VQ-1 要件: EP-01a, EP-08a → **未充填**（インセンティブ構造的未充填）
- VQ-2 要件: EP-02a → **部分充填**（生成物キャラクタリゼーションは後続論文に分散）

**階層-時間対応の評価：**

本ケースでは、VQ 階層と充填時間の対応が**部分的に逆転**している。理論的には VQ-1（観察報告の完全性：EP-01a）→ VQ-2（方法の完全性）→ VQ-3（機構的根拠）→ VQ-4（ベンチマーク）の順で充填されることが期待されるが、実際には低 VQ 水準の EP-01a（GC calibration）・EP-08a（反復測定）は永続的に未充填のまま残り、高 VQ 水準の EP-07a（境界拡張）が最も迅速に（1994–1999年）自己充填された。これは「出版インセンティブに基づく実際の充填順序（高VQ→低VQ）」と「科学的論理に基づく充填順序（低VQ→高VQ）」の逆転パターンに相当し、VQ 階層逆転の典型例として記録する。Murai 反応の圧倒的な synthetic utility が、方法論的完全性（VQ-1/VQ-2の細部）よりも応用範囲拡張（VQ-2/VQ-3の境界探索）を優先する科学コミュニティの行動を誘導した。

**特筆すべきパターン：**

1. **自己充填（series_signal の実現）**: EP-07a は Murai/Chatani/Kakiuchi グループ自身によって 1994–2002 年に段階的に自己充填された。「applicable more widely」という A-2（forgotten extension claim）が、原著者グループの planned follow-up series として実現した数少ない事例。

2. **技術駆動充填（計算化学）**: EP-03a / EP-04a は実験的手法ではなく計算化学（DFT、Morokuma グループ等）によって間接充填された。1998年頃の DFT 計算能力の向上が driving force。実験的中間体直接観測は 2000 年代以降にも困難のまま残存している可能性がある。

3. **VQ 階層逆転**: EP-01a（低 VQ・reporting completeness）が永続的に未充填である一方、EP-07a（高 VQ・境界拡張）が最速充填。これは Murai 反応の「成功」がインセンティブ構造を変容させたことの証拠として記録する。

4. **バンドル充填候補**: Matsubara et al. 1998 DFT 論文が EP-03a + EP-04a を同時に部分充填する可能性（1論文で複数 EP を間接充填する高効率候補）。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-01a [Reporting-coherence pack]:**
* **未充填の理由**: インセンティブ構造の不整合 + format-imposed compression（Nature 3ページ制約の遺産）。原論文 Table 1 の GC 収率の response-factor calibration・全 run 単離収率・run 1 の 17% 未帰属成分を遡及的に報告する動機が後続研究グループに存在しない。Murai 反応の爆発的普及により、原論文のデータ自体が「landmark paper のデータ」として疑問なく引用される慣行が確立し、retroactve verification への需要が社会的に消滅した（成功による問いの抹消の側面も）。
* **発見的意義**: あり。「合成化学分野では、landmark paper のデータ品質（GC calibration・mass balance）が成功後に事後検証されない」という出版インセンティブの非対称性を実証する事例。Murai 1993 の「100%」収率報告が response-factor 未記載のままコミュニティに受容されたことは、同時代の多くの合成論文に同様のパターンが存在することを示唆する。UQS が「成功した論文では低 VQ 水準 EP が永続的に未充填になりやすい」という系統的パターンを記録した事例として価値がある。
* **将来の充填可能性**: 低。Murai グループおよびコミュニティには遡及的 GC calibration・run 1 mass balance 公表のインセンティブがなく、将来的な充填は「歴史的精査」（科学史家による primary data 追跡）の文脈でのみ成立しうる。

---

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造の不整合 + 成功による問いの抹消。Murai 反応は 1993年以降に世界中の合成化学グループで「再現」されたが（6,000+ 引用）、各グループはその結果を独立論文として発表せず（新規性なし）、それ自体がレポートされる場がない。反復測定・統計的信頼性評価を Murai 1993 に特化して行う動機は、成功という事実によって消去された。
* **発見的意義**: あり。「成功した named reaction では、original paper の statistical reliability の独立検証が行われない」という系統的パターンを示す。Murai 1993 が 30 年以上にわたって run 9 の「100%収率/0.5h」という数値を無統計的に引用され続けてきた事実は、合成化学分野の「landmark paper の unchallenged legacy」問題の典型例として記録できる。
* **将来の充填可能性**: 中。現代の「Open Science」・「Reproducibility Initiative」文脈では、Murai 1993 のような landmark paper の再現性検証プロジェクトが計画される可能性はある。ただし触媒反応の再現性検証は multi-lab 試験プロトコル（ICS 等）が確立しておらず、近期での充填可能性は低〜中。

---

**EP-02a [Identity / purity substantiation pack]（部分未充填）:**
* **未充填の理由（部分残存）**: 原論文 Table 1 の 13 生成物全体についての統合的 NMR データ・regiochemical assignment（NOE または X 線）を提供する論文は存在しない。各論文は新たな基質系のデータを提供するが、Murai 1993 に特化した全生成物の recharacterization は行われない。分野慣行として、先行論文の生成物を遡及的に再キャラクタリゼーションする論文は出版されにくい。
* **発見的意義**: 限定的。生成物キャラクタリゼーションは後続の full-paper series に分散充填されるため、原論文固有の「13 run 全体のキャラクタリゼーション空白」という問い自体が科学史的に顕在化しにくい。
* **将来の充填可能性**: 低（遡及的全 run 再キャラクタリゼーションの出版インセンティブなし）/ 中（個別生成物については後続研究で使用時に充填される）

---

**VQ階層逆転の診断（§E 補足）：**

本 Murai 1993 ケースでは、以下の充填逆転パターンが観察された：

| VQ水準 | EP | 充填状況 | 充填時期 |
|--------|----|---------|---------|
| 低 VQ (VQ-1/VQ-2) | EP-01a, EP-08a | **永続的未充填** | — |
| 低 VQ (VQ-2) | EP-02a | **部分充填** | 1994〜 |
| 中 VQ (VQ-2/VQ-3) | EP-07a | **Complete充填** | 1994–2002（最速） |
| 高 VQ (VQ-3) | EP-03a, EP-04a, EP-10a | **Indirect/Partial充填** | 1998〜 |
| 最高 VQ (VQ-4) | EP-09a | **Indirect充填** | 2002〜 |

VQ 階層逆転の診断：**逆転パターンあり**。低 VQ 水準（reporting completeness: EP-01a, EP-08a）が未充填のまま残存し、高 VQ 水準（境界拡張: EP-07a、機構: EP-03a, EP-10a）が優先的に充填された。これは分野のインセンティブ構造（新規性重視、追試・再現性確認は低評価）がUQSの構造的不在の一部を維持していることの実証的証拠として記録する。

