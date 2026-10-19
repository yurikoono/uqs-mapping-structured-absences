prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Murai et al. 1993（Nature, Communication）

---

### §A EP充填難易度の三群分類

Stage 3 §5 に列挙された EP は以下の6件：EP-03a, EP-06a, EP-04a, EP-09a, EP-08a, EP-07a。

---

**第一群（文献で明確に追跡可能）：** EP-03a, EP-06a, EP-04a, EP-07a

- **EP-03a（Direct-observation / state-assignment pack）**: シクロメタル化中間体の直接観測（³¹P NMR / X線結晶解析）は、Kakiuchi・Chatani グループが後続の Full Paper 系列（1993–2002）で独立した研究主題として発表しており、文献検索で直接追跡可能である（RI-03）。
- **EP-06a（Analogy-validation pack）**: Ru(0) 酸化的付加と類似系（Mn(I)・Ru(II) ストイキオメトリック）の機構的比較は、C–H 活性化機構の理論・実験論文として独立して発表されており、計算化学（DFT）を含む充填文献が存在する（RI-06）。
- **EP-04a（Discrimination / replication pack）**: 重水素化 KIE 実験（k_H/k_D 測定）は有機金属 C–H 活性化メカニズム論文の標準的内容であり、Murai 反応そのもの、または密接に関連するキレーション補助 Ru 系で実施された文献が確認できる（RI-04）。
- **EP-07a（Boundary-test pack）**: ケトン以外の directing group（アルデヒド、エステル、アミド、イミン）への適用範囲拡張は、1993年以降のChatani グループおよび他グループによる多数のフォローアップ論文が存在し、スコープ境界の系統的試験として追跡可能である（RI-07）。

**第二群（間接的に追跡可能）：** EP-09a

- **EP-09a（Internal benchmark pack）**: runs 1, 9, 10 の TOF 数値と Jordan & Taylor (1989) / Moore et al. (1992) との直接数値比較は、独立論文として発表されるよりも、総説・レビューや後続 Full Paper の introduction での比較の形で部分的に含まれる可能性が高い（RI-09）。対象系を対象とした直接対照実験は困難。

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a（Replication / uncertainty pack）**: GC 定量の内部標準・レスポンスファクター・反復実験（n≥3）による不確実性定量は、Full Paper 展開（Kakiuchi et al. 1994, JACS）において方法論記載が拡充される形で部分的に解消される可能性があるが、それ自体が独立論文として発表されることはなく（RI-01 / RI-08 の報告形式問題）、また分野慣行として定量的 GC 方法論の完全開示は現在も均一ではない（third-group typical）。

---

### §B 各EPの充填論文候補

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（シクロメタル化中間体 U-1 critical; Ru(0) 活性種 U-2 high）
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83 — Murai 1993 通信の Full Paper 版であり、基質スコープの系統的拡張・反応条件の詳細化および触媒サイクルの実験的検討を含む。シクロメタル化中間体の間接的証拠（反応速度の基質依存性、同位体実験）を追加。tentative_citation（Full Paper の存在は高確信だが、掲載雑誌・年・頁は要確認）
* **充填確立点**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693 — DFT 計算によってシクロメタル化中間体の構造・エネルギーを直接計算し、Ru(II) 五員環中間体の安定性と C–H 酸化的付加の遷移状態を理論的に確立した；RI-03 における「存在の理論的実証」という形で充填が確立される最初の主要例。tentative_citation（論文の存在と内容は高確信だが、号・頁は要確認）
* **充填の性質**: Partial — 実験的直接観測（NMR・X 線）よりも理論的実証（DFT）が先行した充填であり、EP-03a が要求する「ストイキオメトリック条件での ³¹P NMR 観測」は Matsubara 1998 では満たされない。実験的孤立・同定は後続研究（2000 年代）に委ねられる。
* **Confidence**: Medium — Full Paper（Kakiuchi 1995）の存在は高確信；Matsubara 1998 DFT の内容は高確信だが、同論文が実験的中間体孤立を含まない点で EP-03a への充填対応は推論を含む。
* **注記**: EP-03a の充填は「理論（DFT）」と「実験（NMR/X 線）」の二段階で起きており、完全な充填確立（Complete）には後続の実験的中間体孤立論文（例：Chatani グループ 2000 年代の関連ルテナサイクル結晶解析）が必要。また Gorelsky, S. I.; Lapointe, D.; Fagnou, K. *J. Am. Chem. Soc.* **2008**, *130*, 10848 等の CMD（concerted metalation-deprotonation）機構論文は、Ru(0) 酸化的付加という本論文提案枠組みへのパラダイム-シフト的充填として機能しうる（§D で後述）。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model（refs 14・15 の Mn(I)/Ru(II) ストイキオメトリック系から Ru(0) 触媒サイクルへの類推の機構的妥当性：B-11, C-2）
* **充填開始点**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693 — DFT 計算が Ru(0) 活性種から出発する Ru(0)/Ru(II) 触媒サイクルを明示的にモデル化し、Mn(I) 先例とは異なる Ru(0) OA 機構を計算で検証；refs 14（Knobler 1975）の Mn(I) 先例とは異なる酸化状態に基づく機構を独立して検討した最初の計算研究。tentative_citation（同上）
* **充填確立点**: Foley, N. A.; Lee, J. P.; Ke, Z.; Gunnoe, T. B.; Cundari, T. R. *Acc. Chem. Res.* **2009**, *42*, 585–597 — Ru 触媒系における C–H 活性化機構（OA vs CMD vs σ-CAM）の総合的実験・計算比較を提供し、各機構の適用条件を明確化。Murai 系への直接適用を含む可能性があり、refs 14/15 の Mn(I)/Ru(II) 先例の機構的限界を後付けで整理する文脈で引用されうる。tentative_citation（論文の存在は確信、EP 充填との対応は推論）
* **充填の性質**: Indirect — EP-06a が要求する「refs 14/15 の生成物と提案中間体の構造同一性の直接確認」は Matsubara 1998 DFT では行われておらず、計算から独立した Ru(0) サイクルを提案することで RI-06 の問題を迂回する形での充填。refs 14/15 の先例そのものの再評価ではない。
* **Confidence**: Medium — Matsubara 1998 の DFT が EP-06a の RI-06 問題を解消する方向に進んでいることは確信；Foley 2009 の充填対応は推論を含む。
* **注記**: EP-06a と EP-03a の充填は Matsubara 1998 においてバンドル充填されている（同一論文が両EPに対して部分的充填を提供）。RI-06 の完全解消は、Mn(I) 先例（Knobler 1975）と Ru(0) 触媒中間体の構造的差異を実験で確認することであり、これは現在まで独立論文として発表されていない可能性がある（§E 参照）。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator（KIE による C–H 切断が速度決定段階かの判定; SRG-3 ring strain 帰属の速度論的根拠）
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83 — Full Paper 版において重水素化実験（部分的 KIE 測定）が含まれる可能性があり、C–H 切断の速度論的役割を最初に検討した文献として。tentative_citation（Full Paper 内容の詳細は要確認）
* **充填確立点**: Matsubara, T.; Koga, N.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1998**, *120*, 12692–12693 — DFT による活性化障壁計算から C–H 切断が速度決定段階であることを理論的に示し、ring strain 仮説に対する計算的根拠を提供。tentative_citation
* **充填の性質**: Partial — KIE 実験の実測（k_H/k_D 数値）よりも DFT 活性化障壁計算によって部分的に充填されており、EP-04a が要求する「実験的 KIE 測定」は完全充填とは言えない。
* **Confidence**: Medium — DFT が C–H 切断の RDS 性格を理論的に扱っていることは確信；実験的 KIE がどの論文で測定されたかは不確実。
* **注記**: KIE 実験（実測 k_H/k_D）については、後続のキレーション補助 C–H 活性化研究（例：Chatani グループ、Glorius グループ、Fagnou グループによる関連 Rh/Pd 系）で系統的に実施されており、Murai Ru 系への直接適用も存在する可能性があるが、具体的な文献の特定は要確認（confidence: Low のため選定リストには含めない）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary（SRG-4: 「a variety of aromatic systems」スコープ宣言の境界定義；ケトン以外の directing group への適用試験）
* **充填開始点**: Chatani, N.; Fukuyama, T.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* **1998**, *120*, 11522–11523 — イミン基を directing group とするアリール C–H 活性化および C–C カップリングを報告；ケトン以外のカルボニル系 directing group への拡張の初期例。tentative_citation（著者・雑誌・年は高確信、号・頁は要確認）
* **充填確立点**: Chatani, N.; Asaumi, M.; Orizu, S.; Ikeda, T.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* **2001**, *123*, 10935–10941 — アミド directing group を用いた Ru 触媒 C–H アルキル化を報告し、ケトン以外の directing group でも Murai 型反応が進行することを体系的に示した。tentative_citation（内容は高確信だが詳細は要確認）
* **充填の性質**: Partial — ケトン・イミン・アミドへの拡張が報告されたが、アルデヒド・エステル・ニトリル・無 directing group 系の全体的なスコープ地図（「なぜケトンが最良か」の定量的比較）は未充填。U-3 の自己矛盾的不在（「a variety of aromatic systems」は過大宣言であった）は、後続研究が directing group 依存性を個別に示すことで間接的に解消された形となる。
* **Confidence**: Medium — ケトン以外の directing group 拡張論文の存在は高確信；特定の引用文献の内容との EP-07a 対応は推論を含む。
* **注記**: EP-07a の充填は「ケトン特殊性の境界定義」という形では行われておらず、「別の directing group で別の論文を書く」というパターンが主流であった。U-3 の「a variety of aromatic systems」という過大宣言に対して「境界を実験的に定義する」スタイルの論文はほぼ存在しない点は §E で議論する。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 External superiority（TOF 数値の欠如；Jordan & Taylor 1989 / Moore et al. 1992 との定量比較の不在：SRG-5, B-2, C-1）
* **充填開始点**: Kakiuchi, F.; Murai, S. in *Topics in Organometallic Chemistry*, Vol. 3, pp. 47–79 (Springer, 1999) — Murai 反応の包括的レビューであり、触媒効率（TON・TOF）の先行文献との比較表を含む可能性がある。ただしレビューは原則 EP 充填に該当しないため、独自のメタ定量分析を含む部分のみが対象。tentative_citation（巻号・頁は不確実）
* **充填確立点**: **未同定** — Jordan & Taylor (1989) および Moore et al. (1992) と本論文 runs 1, 9, 10 の TOF を同一換算基準（mol/mol/h）で直接比較する独立論文は特定できない。当時の報告スタイルの影響（各論文が独自基準での記述）および対象系の化学的非同一性（異なる基質・溶媒）が直接比較を困難にしていた。
* **充填の性質**: Partial（間接的） — TOF の絶対数値は後続の総説・教科書・触媒化学テキスト（例：Crabtree, *The Organometallic Chemistry of the Transition Metals*, 4th ed.）に収録された文脈で間接的に比較されるが、独立論文として充填された形跡はない。
* **Confidence**: Low — 独立充填論文の特定は困難；レビューや教科書での言及は EP 充填の定義に合致しない。
* **注記**: EP-09a の未同定の理由は §E で詳述する。インセンティブ構造（既存触媒の TOF 定量的再評価は出版インセンティブが低い）が主因と推定される。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-01 Reporting integrity + RI-08 Unquantified reliability（GC 定量の内部標準・レスポンスファクター不記載；反復実験による不確実性定量の欠如）
* **充填開始点**: Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N.; Murai, S. *Bull. Chem. Soc. Jpn.* **1995**, *68*, 62–83 — Full Paper 化によって実験条件の詳細（GC 定量法の記述）が Communication より詳細化されることが期待される。ただし完全な内部標準・レスポンスファクター記述および n≥3 反復実験の標準偏差記載を含むかは不確実。tentative_citation（Full Paper の存在は高確信；内容の詳細は要確認）
* **充填確立点**: **未同定** — GC 定量の内部標準・反復測定標準偏差を完備した形での「Murai 反応の代表例再評価」論文は特定できない。
* **充填の性質**: Partial — Full Paper 化（Communication → BCSJ 1995）によって実験記述が拡充されたと推定されるが、RI-08 が要求する n≥3 独立反復実験による信頼区間の記載は分野慣行として 1990 年代には要求されておらず、現代基準では未解消のまま残る可能性がある。
* **Confidence**: Low — Full Paper の方法論記述改善は確信だが、EP-08a の完全充填との対応は不確実。
* **注記**: EP-08a は §A で第三群に分類した通り、報告形式問題（RI-01 / RI-08）に起因しており、独立論文としての充填は性質上発生しない。分野慣行としての GC 定量方法論の完全開示が現代でも不均一であることは §E で記録する。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Matsubara et al., *J. Am. Chem. Soc.* 1998 | EP-03a, EP-06a, EP-04a（バンドル） | VQ-3（Mechanism） | 1998 | Medium |
| 2 | Kakiuchi, Murai et al., *Bull. Chem. Soc. Jpn.* 1995 | EP-03a（部分）, EP-04a（部分）, EP-08a（部分） | VQ-2（Method） | 1995 | Medium |
| 3 | Chatani et al., *J. Am. Chem. Soc.* 1998（イミン系） | EP-07a | VQ-2（Method/Boundary） | 1998 | Medium |
| 4 | Chatani et al., *J. Am. Chem. Soc.* 2001（アミド系） | EP-07a（確立） | VQ-2（Method/Boundary） | 2001 | Medium |
| 5 | Foley et al., *Acc. Chem. Res.* 2009 | EP-06a（確立）, EP-04a（補完） | VQ-3（Mechanism） | 2009 | Medium |

**選定理由：**

最優先は Matsubara et al. 1998 である。この論文は DFT 計算によって EP-03a（シクロメタル化中間体の理論的実証）・EP-06a（Ru(0) OA 機構の独立計算）・EP-04a（C–H 切断 RDS の理論的根拠）の三EPをバンドル充填しており、VQ-3（Mechanism）要件の中核に直接対応する最も効率的な充填候補である。VQ-2（Method）要件の充填確認には Kakiuchi, Murai et al. 1995 Full Paper が最初の候補として有効であり、通信→Full Paper 遷移による自動解消パターンの検証にも寄与する。EP-07a（スコープ境界）は Chatani 1998 / 2001 の2報が時間的段階を追って境界拡張を示しており、「ケトン directing group 特殊性の間接的解消」の過程を追跡できる。VQ 階層ごとに異なる年代の論文（1995, 1998×2, 2001, 2009）を選定することで、充填の時間的展開を多層的に検証できる。

全選定論文が tentative_citation であることを注記する：掲載雑誌・著者構成は高確信だが、巻号・頁・具体的内容の EP 充填対応については実際の文献確認が必要。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件（RI-01 / RI-07 / RI-08）: EP-08a（部分）+ EP-07a（開始）→ **1995年** Kakiuchi, Murai et al. BCSJ（Full Paper、自己充填）；EP-07a 継続 → **1998年**（Chatani 1998, イミン）→ **2001年**（Chatani 2001, アミド）[自己充填]
- VQ-3 要件（RI-03 / RI-06 / RI-04）: EP-03a + EP-06a + EP-04a（バンドル理論充填）→ **1998年** Matsubara et al. JACS（技術駆動充填：DFT 計算の成熟）；EP-06a 継続確立 → **2009年** Foley et al. Acc. Chem. Res.
- VQ-4 要件（RI-09）: EP-09a → **未充填**（現在まで）

**階層-時間対応の評価：**

VQ-2 要件（Method）の充填は 1995 年（原論文から2年）に始まり、VQ-3 要件（Mechanism）の充填は 1998 年（5年後）に理論的手法によって部分充填された。VQ-4 要件（Benchmark）の EP-09a は現在まで独立論文として充填されていない。この順序は「VQ 階層が上がるほど充填に要する時間が長くなる傾向」の仮説を支持する証拠を提供する。ただし VQ-3 の充填が実験的ではなく計算的（DFT）であった点は、技術駆動充填によって「実験的 VQ-3」への到達よりも「計算的 VQ-3」への到達が先行した例として記録価値がある。

**特筆すべきパターン：**

1. **自己充填（1995年, 2001年）**: Murai グループ自身（Kakiuchi, Chatani を含む）が 1993 通信を Full Paper 化（BCSJ 1995）し、さらに directing group 拡張（1998, 2001）として EP-07a を段階的に充填した。これは「原著者グループによる後続論文での自己充填」の典型例であり、特に EP-07a において顕著である。

2. **技術駆動充填（1998年）**: EP-03a / EP-06a / EP-04a の VQ-3 要件充填が DFT 計算（Matsubara 1998）によって「実験的中間体孤立なしに」理論的に達成された点は、有機金属化学における DFT の普及（1990 年代後半）が UQS の構造的不在を解消した典型事例である。実験的充填（³¹P NMR・X 線）よりも計算的充填が先行したことは、インセンティブ構造（DFT 論文の新規性が高く、既存系の追実験は低い）を反映している。

3. **パラダイム転換充填（2008年以降）**: Gorelsky, Lapointe, Fagnou, *J. Am. Chem. Soc.* **2008** に代表される CMD（concerted metalation-deprotonation）機構の確立は、Murai 1993 が提案した Ru(0) 酸化的付加という枠組みを部分的に置換する「パラダイム転換充填」として機能した。tentative_citation。EP-03a / EP-06a に対して「充填というよりも succession（問いの枠組みが変わった）」としての記録が適切。ただし Ru(0) Murai 系への CMD 機構の直接適用は Rh/Pd 系に比べて議論があり、Ru 系においては現在もパラダイム的に決着していない可能性がある。

4. **VQ 逆転パターンの観察**: EP-08a（VQ-2 要件の RI-01/RI-08 問題）が現在まで未充填のまま残り、EP-03a / EP-06a（VQ-3 要件）が 1998 年に部分充填されたという事実は、「科学的論理に基づく EP 充填順序（低 VQ → 高 VQ）」と「実際の充填順序（高 VQ の計算論文が先行、低 VQ の定量 GC 再評価は後回し）」の逆転を示している。GC 内部標準・反復測定という「退屈な」実験的確認（RI-01/RI-08）よりも、機構を扱う計算論文（RI-03/RI-06）の方が出版インセンティブが高いという分野構造が、この逆転を生み出している。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

---

EP-09a [Internal benchmark pack]:

* **未充填の理由**: インセンティブ構造の不整合 + 方法論的困難。Jordan & Taylor (1989) の Zr/α-ピコリン/プロペン系と Moore et al. (1992) の Ru/ピリジン/CO/ヘキセン系は、Murai 1993 の Ru/芳香族ケトン/オレフィン系と基質・溶媒・触媒が根本的に異なり、「同一換算基準での TOF 比較」は対象系の化学的非同一性のため方法論的に困難である（単純比較は恣意的になりうる）。さらに、既存触媒の TOF を統一基準で再測定し比較するという実験は、新規性を要求する出版慣行のもとで独立論文として報告されるインセンティブが著しく低い。SRG-5（C-1: 先行研究との定量比較の不在）が示す「定性的優位性宣言」スタイルは、現代でも触媒化学の初報 communication において残存している分野慣行の一形態である。
* **発見的意義**: あり。「最高 TOF」という競合的主張（B-2 / SRG-5）が 30 年以上にわたって定量的に検証されないまま citation として機能し続けている事実は、UQS が「分野のインセンティブ構造によって維持されている構造的不在」を同定できる典型例として記録できる。RI-09（External superiority）の era-norm 依存性（S3 §4 両タグ該当項目）と組み合わせると、「1993 年に定性的比較として許容されたものが、現代の触媒化学基準では再現不能な主張として残存している」という発見的診断が可能である。
* **将来の充填可能性**: 低。基質・系の非同一性が直接比較を原理的に困難にしており、Jordan & Taylor (1989) および Moore et al. (1992) の当時の実験条件での Murai 反応の追試（同一基質での対照実験）を行うグループが今後現れるインセンティブも低い。EP-09a は「充填されないことに発見的意義がある」未充填 EP として記録する。

---

EP-08a [Replication / uncertainty pack]（部分的未充填）:

* **未充填の理由**: 報告形式問題（Full Paper 遷移で部分解消）+ 分野慣行（GC 定量方法論の完全開示は 1993 年代の有機金属化学の触媒論文では慣例的に要求されていなかった）。Full Paper（Kakiuchi et al., BCSJ 1995）によって実験記述が拡充されたと推定されるが、n≥3 独立反復実験・信頼区間付き平均値・内部標準名・レスポンスファクターの完全記載という現代の RI-01/RI-08 要件は、当時の Full Paper でも満たされていない可能性が高い。
* **発見的意義**: 限定あり。EP-08a の未充填は分野慣行（GC 収率の単一実験値報告）の反映であり、Murai 反応固有の問題ではなく 1990 年代前半の有機金属合成触媒論文全般に共通する構造的問題として記録できる。UQS の B-1（communication-era tolerated）への §4 の両タグ該当記録と整合する。
* **将来の充填可能性**: 中。現代の再現性クライシス（reproducibility crisis）への対応として、高影響力古典論文の定量的再評価（n≥3 再現実験）が行われることがあり（例：C–H 活性化ベンチマーク研究）、Murai 1993 の代表ランについて現代基準での再現試験が実施される可能性は中程度である。ただし Ru 触媒系として現在も広く使用されているため、文献中に散在する追試データから統計的に再評価できる可能性もある。

---

EP-07a の「ケトン directing group 特殊性の境界定義」に関する追記：

EP-07a は第一群（充填論文あり）と判定したが、充填の性質が Partial であり、発見的意義のある半未充填パターンを示す。「なぜケトンが最良の directing group か」を定量的に示す（アルデヒド・エステル・アミド・イミンとの収率・速度の系統的比較）という形の充填は、Chatani グループが directing group を一つずつ個別論文として拡張するスタイルをとったため、包括的な「directing group hierarchy」としては結晶化していない。U-3（「a variety of aromatic systems」過大宣言）が提示した問い——「ケトン以外は本当にスコープ外なのか、それとも単に未試験なのか」——への「包括的な答え」は、現在も文献に存在しない。これは「分野が 30 年間、個別拡張論文を積み上げながらも、比較定量的なスコープ地図を描いてこなかった」という構造的不在の証拠として記録できる。
