prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Terao et al. 2002（JACS, Communication）

---

### §A EP充填難易度の三群分類

Stage 3 §5 で導出された EP 一覧: EP-03a（×2: SRG-1 中間体同定 / SRG-4 BD 回収）, EP-04a, EP-10a, EP-07a, EP-08a, EP-09a

**C23 trigger チェック:** 本論文は JACS Communication（2 pp）形式 → **C23 該当**。同一著者グループによる Full Paper / 続報の存在確認が必要。

---

**第一群（文献で明確に追跡可能）:** EP-03a (SRG-1: 中間体同定), EP-04a, EP-07a

- **EP-03a (SRG-1)**: η¹,η³-nickelate 型中間体の分光学的同定または化学量論的合成は、独立した Ni(0)–ジエン錯体の organometallic chemistry として多数の単独論文が存在する。Kambe グループ自身も後続 Full Paper で機構的実験を追加している可能性が高い。RI-03 は独立論文の主題になりやすい。
- **EP-04a**: 複数の radical clock 系 + TEMPO トラッピング実験による Ni 触媒機構の radical probe 研究は 2002 年以降の Ni 触媒 C–C 結合形成の主要論文で広く実施された。独立論文として存在する可能性が高い。
- **EP-07a**: 二級・三級アルキル基質への適用拡張は、Ni 触媒アルキル–アルキル cross-coupling の「next challenge」として複数のグループが独立に取り組んだ研究対象であり、独立論文化された可能性が高い。

**第二群（間接的に追跡可能）:** EP-03a (SRG-4: BD 回収), EP-10a

- **EP-03a (SRG-4)**: BD 回収の定量（触媒性確認）は独立論文の主題ではなく、同一著者グループの Full Paper または DFT 研究の補足実験として実施された可能性がある。C23 に該当する Letter→Full Paper auto-resolution が期待される（auto_resolution_type: "Letter→Full Paper", expected_resolution_window: "1-3 yr"）。
  - ```yaml
    auto_resolution_type: "Letter→Full Paper"
    expected_resolution_window: "1-3 yr"
    auto_resolution_status: "promised" — ("further studies...ongoing" の言及あり、Full Paper 確認は verification 要)
    filling_timescale_category: "format-driven"
    ```
- **EP-10a**: 初速度法による速度論的解析は、Ni 触媒アルキル–アルキル cross-coupling では計算化学（DFT による速度式導出）による間接的アプローチが主流であり、実験的速度論論文が独立に存在する可能性は中程度。DFT 機構論文（Kambe グループまたは独立計算化学者）に含まれる可能性がある。

**第三群（充填が見つからない可能性あり）:** EP-08a, EP-09a, EP-01a

- **EP-08a**: GC 較正付き反復測定（n≥3）による統計的信頼性評価は、「追試・再現性評価」として独立論文化されないインセンティブ構造的未充填の典型。C23（Letter→Full Paper）で較正 GC が導入されても、統計的評価（SD）の明示的報告は合成 Chemistry Communications では現在でも必須でない場合がある。（インセンティブ構造的未充填）
- **EP-09a**: refs 1–3 との同一条件での直接比較は「ベンチマーク論文」としての独立出版インセンティブがなく、競合グループが同条件で先行系を再現する動機が低い。（インセンティブ構造的未充填）
- **EP-01a**: GC 報告形式の完全性（較正標準明示・mass balance 報告）は、C23 Letter→Full Paper 展開で部分的に自動解消されるが、RI-01 の要件（ホモカップリング副産物・全物質収支）が独立論文として充填されることはなく、分野の reporting 慣行内での漸進的改善に留まる。（インセンティブ構造的未充填 + 分野慣行）

---

### §B 各EPの充填論文候補

**EP-03a [Direct-observation / state-assignment pack]（第一群 — SRG-1: 中間体同定）**

* **充填するRI**: RI-03 (Unobserved explanatory)
* **充填開始点**: Kambe, N. et al. (Terao, J.; Ikumi, A.; Kuniyasu, H.; Kambe, N.) — J. Am. Chem. Soc. 2003 ないし 2004 頃（Kambe グループ Full Paper または続報）— η¹,η³-nickelate 中間体 2 に相当する類似錯体の化学量論的合成・同定実験が含まれる可能性。(1文充填内容: Ni(0) と 1,3-BD の化学量論的反応生成物の分光学的同定、または機構的追実験。)
* **充填確立点**: 独立した計算化学グループによる DFT 機構解析 — 例えば Yoshikai, N.; Nakamura, E. Chem. Rev. 2012, 112, 2339 類の Ni 触媒機構総説 / または同等の DFT 一次論文において、中間体の構造・エネルギーが計算的に特定された可能性。
* **充填の性質**: Indirect — 対象系（NiCl₂/1,3-BD/THF）での direct 分光観測は未確認の可能性が高く、計算的または類似 Ni-diene 錯体系での間接同定が主体。
* **Bibliographic confidence**: Low（著者名・年・雑誌・巻号の具体的情報に確信が持てない）
* **Filling adequacy confidence**: Medium（中間体同定の実験は Kambe グループ続報または DFT 論文にほぼ確実に存在するが、同一条件での direct 分光観測かは不明）
* **Verification recommendation**: 必須（条件 (b): Kambe グループは 10+ の関連 follow-up を持つ密な著者ネットワーク）
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr) — DFT 計算が 2005-2010 年代に機構論の主流になったことで間接充填。
* **注記**: 第一群に分類したが、Terao 2002 の specific な「η¹,η³-nickelate の in situ 分光観測」という要件が Kambe グループの続報で直接満たされたかどうかは verification を要する。

---

**EP-03a [Direct-observation / state-assignment pack]（第二群 — SRG-4: BD 触媒性）**

* **充填するRI**: RI-03 (Unobserved explanatory) — U-1 cycle-prediction unfulfilled
* **充填開始点**: 未同定 — BD 回収の定量的報告が Full Paper 続報または Kambe グループ関連論文に含まれるか不明。Kambe, N. et al. の Full Paper 候補（2003-2004 年頃）に含まれる可能性がある。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "promised"
  filling_timescale_category: "format-driven"
  ```
* **充填確立点**: 未同定（以下§E参照）
* **充填の性質**: Partial（BD 回収定量は続報 Full Paper に含まれる可能性があるが、主要 focus でない可能性が高い）
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 必須
* **Bibliographic verification status**: pending
* **Filling timescale category**: non-applicable（充填確認ができないため）
* **注記**: BD の触媒的役割（再生確認）は Kambe グループの Acc. Chem. Res. 等の総説 article では言及されている可能性があるが、定量的 GC 測定による「BD 回収率」の一次論文は存在しない可能性が高い（→§E参照）。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 (Unreplicated discriminator)
* **充填開始点（ラジカルクロック拡張）**: Terao, J. et al. (Kambe グループ) — Full Paper 続報（2003-2005 年頃; 雑誌・巻号未特定）において、(bromomethyl)cyclopropane に加えて hex-5-enyl 系（低速 radical clock）または TEMPO トラッピング実験が追加されていた可能性。(1文: Full Paper で radical probe 実験を複数 clock で再実施し "ruling out a radical mechanism" の根拠を補強。)
* **充填確立点（TEMPO/多 clock）**: 独立グループによる Ni-catalyzed alkyl cross-coupling の mechanism study — 例えば Weix グループまたは Engle グループ（2010 年代以降）が Ni(0)/Ni(II)サイクルにおける radical probe を系統的に実施した論文が存在する可能性。
* **充填の性質**: Partial（Kambe 系に限定した場合；別 Ni 触媒系での radical probe は Indirect）
* **Bibliographic confidence**: Low（Kambe 続報については中程度の確信があるが詳細未特定; 独立 Weix/Engle 論文については年号・雑誌不明）
* **Filling adequacy confidence**: Medium（ラジカルプローブ実験の multi-clock 化は 2010 年代の Ni 機構論文の標準的 repertoire となっており、このタイプの EP 充填は存在するはず）
* **Verification recommendation**: 必須（条件 (b): 著者ネットワーク密）
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-5 yr for Kambe group) / incentive-aligned (5-10 yr for independent groups)
* **注記**: U-2 の論理的飛躍（β-H 脱離と transmetalation 区別）については、これを直接指摘して deuterium labeling で区別した論文は現時点では未同定（→§E参照）。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary)
* **充填開始点（二級アルキルへの拡張）**: 複数の候補が存在：
  (1) Kambe グループ自身の scope extension 論文（2003-2006 年頃; Terao, Kambe et al., JACS or Angew. Chem. — 年号・巻号未特定）において二級アルキルグリニャール試薬への適用が報告された可能性が高い。
  (2) Fu グループ: Gonzalez-Bobes, F.; Fu, G. C. J. Am. Chem. Soc. 2006, 128, 5360-5361 — Ni 触媒（Ni(cod)₂/ligand）による二級アルキルハライドとアリルシランの cross-coupling。ただしこれは alkyl-aryl 系であり、Kambe 系の alkyl-alkyl scope とは文脈が異なる。
* **充填確立点（一級のみというバウンダリーの明確化）**: Terao, J.; Kambe, N. 系の Review article（例: Kambe, N.; Terao, J. et al. 2008-2010 年頃の Acc. Chem. Res. 類）において、Ni/1,3-BD 触媒が一級 and/or 二級アルキル基質に対応するかどうかが整理された可能性が高い。1文充填内容: 一級アルキル専用という制約の明確化、または二級基質拡張の達成。
* **充填の性質**: Partial（Kambe 系については partial；他の Ni 触媒系では完全充填の可能性あり）
* **Bibliographic confidence**: Low-Medium（Kambe 続報の存在は確信があるが詳細未特定; Fu 2006 JACS は Medium — 内容は微妙に異なる可能性）
* **Filling adequacy confidence**: Medium（二級アルキル Grignard × alkyl 電解質の Ni 触媒 cross-coupling は 2005-2010 年代に複数グループが取り組んだ問いであり、何らかの充填論文が存在するはず）
* **Verification recommendation**: 必須（条件 (b)(d)）
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (3-7 yr) — 一級専用 scope を超える Ni 触媒系の探索は 2002 年以降の競合研究課題として field-wide に取り組まれた。
* **注記**: Kambe グループ内の "ongoing" promise（S0-6）の実現として、A-2（二級基質スコープ）は自己充填パターン（Kambe 自身による後続論文）の典型候補。

---

**EP-10a [Kinetic verification pack]（第二群）**

* **充填するRI**: RI-03 (Unobserved explanatory), PRI-11 (Mechanism-kinetics decoupling)
* **充填開始点（DFT 機構論文）**: 計算化学的アプローチによる Ni/1,3-BD/Grignard 触媒系の DFT 速度論解析が、独立した計算化学グループによって 2005-2015 年の間に実施されていた可能性。例えば Yoshikai, N.; Nakamura, E. 系の Ni 機構 DFT 論文（J. Am. Chem. Soc. 2010 前後）において η¹,η³-nickelate 経由サイクルの activation energy profile が計算された可能性がある（Medium confidence; 論文存在は確信があるが Terao 系への specific 適用は推測）。
* **充填確立点**: 未同定（実験的 initial-rate kinetics については現時点で未充填の可能性が高い — §E参照）
* **充填の性質**: Indirect — DFT 速度論が present なら partial; 実験的速度論は現在も未充填の可能性
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low（実験的速度論については特にFilling adequacy confidence Low）
* **Verification recommendation**: 必須
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (10-15 yr) — DFT 計算が Ni 機構論の主流になるまで時間を要した。
* **注記**: EP-10a の実験的充填（initial-rate kinetics）は現在も未充填の可能性が高い（インセンティブ構造: Ni アルキル–アルキル cross-coupling の速度論測定は技術的困難 + 出版インセンティブ低）。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 (Unquantified reliability)
* **充填開始点（C23 Letter→Full Paper 自動解消）**: Kambe グループ Full Paper 続報（2003-2005 年頃）において較正 GC 収率または孤立収率が報告された可能性。(1文: Full Paper 化により較正標準付き GC または孤立収率が導入。)
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-3 yr"
  auto_resolution_status: "promised"
  filling_timescale_category: "format-driven"
  ```
* **充填確立点**: 未同定（Full Paper 化での部分解消以上の統計的評価は存在しない可能性が高い）
* **充填の性質**: Partial（較正 GC は Full Paper で解消される可能性があるが、n≥3 の統計的有意性評価は合成化学分野では現在でも非必須）
* **Bibliographic confidence**: Low（Full Paper 続報の存在は確信があるが詳細未特定）
* **Filling adequacy confidence**: Low（統計的評価まで含む完全充填は困難）
* **Verification recommendation**: 必須
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr) — ただし完全充填は non-applicable
* **注記**: インセンティブ構造的未充填 — 反復測定による統計的有意性評価は合成化学 Communications では現在でも独立論文化されない慣行。C23 で部分解消されるが完全充填は起きない可能性が高い。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: 未同定（ホモカップリング副産物・活性化 Grignard 消費量・BD 回収の全物質収支を含む完全な報告形式は、独立論文として充填されない）
* **充填確立点**: 未同定
* **充填の性質**: Partial（C23 Full Paper で GC 収率の較正は改善される可能性があるが、全物質収支報告は分野慣行外）
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 必須
* **Bibliographic verification status**: pending
* **Filling timescale category**: non-applicable
* **注記**: インセンティブ構造的未充填。RI-01（reporting coherence）は independent 論文の主題にはならず、Full Paper 展開でも全物質収支の完全報告は Ni 触媒 alkyl cross-coupling 分野では必須慣行でない。

---

**EP-09a [Internal benchmark pack]（第三群）**

* **充填するRI**: RI-09 (External superiority)
* **充填開始点**: 未同定（refs 1–3 の先行 Ni 系を同一条件で再実施した論文は存在しない可能性が高い）
* **充填確立点**: 未同定
* **充填の性質**: Indirect — 総説論文（Kambe グループ Acc. Chem. Res. 類）が各系の収率を表形式で比較している可能性があるが、これはレビューであり EP 充填として機能しない（guideline 5）
* **Bibliographic confidence**: Low
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 必須
* **Bibliographic verification status**: pending
* **Filling timescale category**: non-applicable
* **注記**: インセンティブ構造的未充填。先行 Ni 系との直接比較実験を独立論文として実施するインセンティブは存在しない。代替として: 総説 article が各系の scope/収率を間接比較することで indirect 充填が起きている可能性。

---

**§B 末尾チェック: Bibliographic verification**

**トリガー条件評価:**
- (a) 論文年代: 2002 年（比較的新しいが verification は有益）
- (b) 著者ネットワーク: Kambe グループは Ni/1,3-BD 触媒で 20+ 報の関連論文 → **条件 (b) 該当**
- (c) 命名規則: 本論文はナンバーリングされた「named reaction」ではないが Kumada coupling の派生系 → 部分的に (c) に近い
- (d) Bibliographic confidence Medium-Low の候補が全エントリーで該当 → **条件 (d) 該当**

→ **全候補 [必須]。全エントリーに `Bibliographic verification status: pending` を付記。**

post-hoc verification 推奨手順: Crossref API で著者 "Terao Kambe" + 年 2003-2006 の JACS/Angew.Chem. 論文を検索し、Full Paper 候補を特定すること。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️ Terao, J.; Ikumi, A.; Kuniyasu, H.; Kambe, N. — Full Paper 続報（推定 JACS/Angew.Chem., 2003-2005 年頃） | EP-08a, EP-01a, EP-04a（partial） | VQ-2 | ~2003-2005 | Low | Medium | 必須 |
| 2 | ⚠️ Kambe グループ機構/scope extension 論文（推定 2004-2007 年頃） | EP-07a, EP-03a（SRG-4 partial） | VQ-2 → VQ-3 partial | ~2004-2007 | Low | Medium | 必須 |
| 3 | ⚠️ DFT 機構論文（推定 2008-2015 年頃; 計算化学グループ） | EP-10a（indirect）, EP-03a（SRG-1 indirect） | VQ-3 partial | ~2008-2015 | Low | Low | 必須 |
| 4 | ⚠️ 独立グループによる Ni アルキル-alkyl cross-coupling radical probe 論文（推定 2008-2015 年） | EP-04a | VQ-3 partial | ~2008-2015 | Low | Medium | 必須 |
| 5 | ⚠️ Ni 触媒 C(sp³)–C(sp³) cross-coupling scope 拡張論文（Fu, Knochel, または Weix グループ, 2005-2012 年） | EP-07a | VQ-2 → VQ-3 partial | ~2005-2012 | Low | Medium | 必須 |

**注記:** 全エントリーが `⚠️ verification 待機中`。Bibliographic confidence が全体的に Low–Medium のため、post-hoc verification を経るまで final selection として扱わない。

**選定理由:**
候補 1（Kambe Full Paper 続報）は C23 Letter→Full Paper 自動解消パターンとして EP-08a/EP-01a（reporting completeness）と EP-04a（radical probe 追実験）の両方を同一論文で partial 充填する効率が高く、最優先に選定。候補 2（scope extension 論文）は EP-07a（二級アルキルスコープ）という VQ-2 要件を充填しながら機構的情報（EP-03a SRG-4）も提供する可能性がある。候補 3（DFT 機構論文）は EP-10a/EP-03a の indirect 充填として VQ-3 前進の唯一の経路であり、実験的速度論論文が存在しない場合の代替。候補 4-5 は EP-04a/EP-07a の独立充填として年代多様性のために選定した。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸（推定）:**

- **VQ-2 要件** (RI-01, RI-07, RI-08):
  - EP-01a, EP-08a（reporting completeness）→ 2003-2005 年頃（Kambe Full Paper; format-driven 自動解消）[自己充填]
  - EP-07a（scope boundary）→ 2004-2008 年頃（Kambe グループ自己充填 + 競合グループ充填）[自己充填 + 分野横断充填]

- **VQ-3 要件** (RI-03, RI-04):
  - EP-04a（radical probe 拡張）→ 2003-2008 年頃（Kambe Full Paper partial + 独立グループ）[自己充填 → 分野横断充填]
  - EP-03a/SRG-1（中間体同定）→ 2008-2015 年頃（DFT 機構論文による indirect 充填）[技術駆動充填: DFT 普及]
  - EP-03a/SRG-4（BD 触媒性）→ 未充填（long-term gap の可能性）

- **VQ-4 要件** (RI-08, RI-09):
  - EP-09a（direct benchmark）→ 未充填（インセンティブ構造的未充填）
  - EP-10a（kinetics）→ 部分的 indirect 充填（DFT; 実験的は未充填の可能性）

**階層–時間対応の評価:**
推定の充填時間軸は「VQ-2 要件（reporting completeness / scope boundary）→ VQ-3 要件（mechanism）→ VQ-4 要件（benchmark/kinetics）」という VQ 階層に沿った充填順序と概ね一致する。VQ-2 の format-driven 自動解消（C23）が最速（1-3 yr）で実現し、VQ-3 の機構論充填は技術駆動（DFT 普及）で 5-13 yr を要し、VQ-4 の実験的 kinetics 充填は現時点でも未充填である可能性が高い。この時間-VQ 階層対応は「VQ 階層が科学の発展難易度構造を反映する」という仮説を支持する。ただし全エントリーが verification pending であり、この評価は仮説的。

**特筆すべきパターン:**
- **自己充填 + C23 同時発火**: Kambe グループ Full Paper 続報が EP-08a/EP-01a（reporting）と EP-04a（radical probe）を同一論文で充填する可能性があり、自己充填と format-driven auto-resolution が重なる効率的充填パターンが期待される。
- **VQ 階層逆転の部分的観察**: EP-07a（VQ-2, scope boundary 拡張）が 2004-2008 年に充填される一方、EP-01a/EP-08a（VQ-2, reporting completeness）は分野慣行により完全には充填されない可能性があり、同一 VQ 水準内でも充填難易度に非対称性が存在する。これは「充填インセンティブ」が VQ 階層よりも実験の novel な発見性（scope 拡張 > 再現性評価）に引っ張られる pattern として記録する。

---

### §E 未充填EPの発見的意義

**EP-03a (SRG-4) [Direct-observation / state-assignment pack — BD 触媒性]:**
* **未充填の理由**: インセンティブ構造の不整合 + 分野慣行。BD 回収の定量（GC ヘッドスペース分析）は技術的に可能だが、「触媒量の添加物が再生されているかどうか」の実証は合成化学コミュニティで独立論文の主題になりにくい。Kambe グループの review 類で言及されている可能性はあるが、定量的 primary data として発表された論文は存在しない可能性が高い。
* **発見的意義**: あり。「論文が自ら描く触媒サイクルの根幹（BD 再生経路）を、その論文の発表から 20 年以上経過した現時点でも定量的に実証した primary 論文が存在しない」とすれば、これは合成化学コミュニティが「添加物の触媒的役割（substoichiometric 再生）を実証する義務」を体系的に回避してきた分野慣行の証拠として記録できる。
* **将来の充填可能性**: 高 — GC ヘッドスペース分析または in situ IR/NMR（BD の stretch tracking）で原理的に可能。BD の volatility（bp 約 -4°C）を考慮した sealed-vessel 実験が必要。機構論の精密化に関心を持つグループが取り組める課題。

**EP-09a [Internal benchmark pack]:**
* **未充填の理由**: インセンティブ構造の不整合。refs 1–3 の先行 Ni 系（異なる配位子・溶媒・温度条件）を同一条件で再実施した直接比較論文は、「先行系との比較」を primary purpose とする論文が出版されにくいという慣行の産物。競合グループが先行系を「再現実験」として発表するインセンティブが存在しない。
* **発見的意義**: あり（中程度）。"limited success" という refs 1–3 への評価が experimental data なしの asserted claims として残り続けていることは、「先行研究との定量的比較なしでの競合優位性主張」という RI-09 パターンが Ni cross-coupling 化学で慢性的に残存していることの証拠として記録できる。
* **将来の充填可能性**: 中 — 合成化学コミュニティに再現性評価への関心が高まれば（Open Chemistry/reproducibility initiatives）充填可能。ただし短期的には低い。

**EP-10a [Kinetic verification pack]（実験的速度論）:**
* **未充填の理由**: 技術的困難 + インセンティブ構造の不整合。Ni-catalyzed alkyl–alkyl cross-coupling の実験的 initial-rate kinetics 測定は、[RMgX] が反応中に消費されて定常状態になりにくく、Ni(0) 種の安定性が低く、GC による精密な initial-rate 測定が困難という技術的障壁がある。さらに、速度論論文として独立に発表されるためには "mechanism" 以上の novelty が必要であり、インセンティブが低い。DFT による間接的な活性化エネルギー計算が代替として機能してきた。
* **発見的意義**: あり。PRI-11（Mechanism-kinetics decoupling）の era-norm 依存 Fatal として記録。2002 年 Communication での速度論省略は当時の慣行だが、2025 年時点でも実験的速度論が存在しない可能性があるとすれば、この gap は単なる「当時の省略」ではなく「分野が体系的に取り組まない問い」として機能している証拠になる。
* **将来の充填可能性**: 中 — flow chemistry + in situ IR + kinetic modeling の組合せで real-time kinetics 測定は原理的に可能。計算面では DFT/AIMD による free-energy surface 計算（GPU 加速）で実質的な速度式導出が 2020 年代に可能になりつつある。
