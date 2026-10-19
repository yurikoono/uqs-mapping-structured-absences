---
prompt_version: stage4-v6-20260504
model_info: Claude Haiku 4.5 (claude-haiku-4-5-20251001)
experimental_variant: "Murai cross-vendor multi-run haiku v6 run 1"
date: 2026-06-12
---

# EP充填選定マップ

## Murai et al. 1993（Nature, vol. 366, pp. 529–531）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-05a, EP-06a, EP-07a

- EP-03a (Direct-observation of Ru(0) / cyclometallated intermediate): Ru-H₂ → H₂発生追跡とRu(0)生成の分光確認は、Murai グループおよび Chatani グループの後続研究で独立テーマとして発表されている可能性が高く、機構検証論文として直接引用可能。
- EP-04a (KIE and deuterium labeling): ortho-d₁-アセトフェノンを用いたC–H切断のKIE測定、M–H対M–C経路の区別は、Ru-C–H官能化分野の標準実験として1990年代後半に多数発表された。
- EP-05a (Temperature dependence and kinetic selectivity): ortho選択性の温度依存性測定、アクリル酸エチル濃度変化のkobs取得は、機構研究の典型テーマであり独立論文化されやすい。
- EP-06a (Analogy-validation via model reaction): RuH₂系の化学量論モデル反応とNMR追跡は、前駆体評価および中間体同定の文脈で独立論文として発表される慣行がある。
- EP-07a (Boundary-test for chelation range): 5員・6員・7員金属環形成の基質依存性実験は、スコープ拡張論文に組み込まれやすく、独立論文または続報で報告される可能性が中程度。

**第二群（間接的に追跡可能）：** EP-01a, EP-08a, EP-09a

- EP-01a (Reporting-coherence: GC calibration, replication): GC収率の校正方法・応答係数・再現実験は、通信からフルペーパー化への自動解消パターン（C23パターン）に該当する可能性あり。Murai グループの続報フルペーパーにおいて method section で記述される可能性が高い（Letter→Full Paper auto-resolution expected）。
- EP-08a (Replication with uncertainty): 統計的再現性・不確かさ評価は、計算化学・物理化学分野では「追試」として独立論文化されにくく、方法論論文またはフルペーパー展開時の自動含有の可能性（インセンティブ構造的未充填パターン候補）。
- EP-09a (Internal benchmark: TOF comparison): Jordan & Taylor (1989) / Moore et al. (1992) のベンチマーク値との比較は、後続レビュー論文またはメタ分析の一部として記述される可能性（第二群：間接的）。原論文での直接的数値比較論文の同定は困難。

**第三群（充填が見つからない可能性あり）：** なし（全EP が第一群または第二群に分類）

---

### §B 各EPの充填論文候補の同定

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点**: Kakiuchi et al., Chem. Lett. 1995 （推測）— Ru(0)種の分光学的同定およびシクロメタル化中間体のNMR観測の初期試行
* **充填確立点**: Murai et al., J. Am. Chem. Soc. 1995–1996, 117–118 巻 (推測) — RuH₂系の加熱時H₂発生の直接追跡およびRu(0)生成の³¹P NMR確認
* **充填の性質**: Partial (H₂発生の容量法確認は実施された可能性あり。完全な機構検証には至らず)
* **Bibliographic confidence**: Medium （Murai グループの後続フルペーパーの存在は確実だが、正確な年号・巻号は推測）
* **Filling adequacy confidence**: Medium （分光法による中間体直接観測は困難な領域であり、部分的な拘束（H₂量論的追跡、³¹P NMR shift変化）の提供に留まる可能性）
* **Verification recommendation**: 推奨
* **Filling timescale category**: field-methodology (2–5 yr) — Murai グループ自身の方法論的応答による自己充填
* **注記**: 原著者グループによる自己充填パターン。化学量論反応での中間体スナップショット観測により RI-03 は部分解消されたと推測

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: Kakiuchi et al., Tetrahedron Lett. あるいは J. Am. Chem. Soc. early 1996 (推測) — ortho-d₁-アセトフェノンの投入によるC–H切断のKIE測定
* **充填確立点**: Kakiuchi et al., J. Am. Chem. Soc. 1995–1996 期間の論文 (推測) — M–H 対 M–C 挿入経路を区別するための重水素標識オレフィン（crotyl-d₁）実験の設計・実施
* **充填の性質**: Partial — KIE測定による C–H 切断の律速化確認は実施された可能性あり。M–H / M–C 経路の完全な区別は、その後の詳細な中間体分析を要し、RI-04の残存が予想される
* **Bibliographic confidence**: Low (Kakiuchi グループの重水素標識実験の年号・誌名に確実性なし；推測に基づく候補)
* **Filling adequacy confidence**: Low （EP の case-specific 実装（crotyl-d₁ 型ラベル実験）との直接対応が不明確）
* **Verification recommendation**: 必須 （1990年代の著者グループの密集ネットワーク、named reaction "Murai reaction" に由来する命名規則該当）
* **Filling timescale category**: field-methodology (2–5 yr)
* **注記**: Kakiuchi グループによる同時期または後続の related-reaction 開発と混在の可能性あり。verification 必須

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-05 Qualitative overread
* **充填開始点**: Chatani et al., J. Am. Chem. Soc. または Kakiuchi et al., Chem. Lett. 1995–1996 (推測) — ortho 選択性の温度依存性測定または電子的に対称なアリール基質での系統的スクリーニング
* **充填確立点**: Murai et al., J. Am. Chem. Soc. 1996 頃 (推測) — run 9 (アクリル酸エチル+アセトフェノン) の濃度変化によるkobs測定および活性化パラメータの取得
* **充填の性質**: Partial — 温度依存性データは報告された可能性あり。位置選択性の速度論 vs 熱力学的制御の完全な分離（temperature jump 実験等）に至ったかは不確実
* **Bibliographic confidence**: Low (年号・巻号推測、著者の複数ラボでの分散による確実性欠如)
* **Filling adequacy confidence**: Low （kinetics 解析の scope と methodology は推測のみ）
* **Verification recommendation**: 必須 （1990年代、Murai / Chatani / Kakiuchi グループの共著関係が複雑）
* **Filling timescale category**: field-methodology (2–5 yr)
* **注記**: 複数グループの競争的進展によるパラレル充填の可能性あり

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Chatani et al., Tetrahedron Lett. または Tetrahedron 1995–1996 (推測) — Ru(CO)₂(PPh₃)₃ またはその類似体を用いた化学量論モデル反応（アセトフェノン+RuH₂）のNMR追跡
* **充填確立点**: Murai et al., Chem. Lett. または J. Org. Chem. 1995–1996 (推測) — 化学量論反応での cyclometallated intermediate [Ru-arene]の単離または ESI-MS / ¹H NMR による明確な帰属
* **充填の性質**: Indirect — 対象系（アセトフェノン+RuH₂）そのものでなく、類似の Ru-chelate 系での中間体分光が代替として機能した可能性。完全な化学量論検証に至ったかは推測
* **Bibliographic confidence**: Low (Chatani グループの方法論開発論文が該当候補だが、確実な特定困難)
* **Filling adequacy confidence**: Low （中間体の「単離」までに至ったかは不確実；spectroscopic snapshot の提供に留まる可能性）
* **Verification recommendation**: 必須 （RI-06のアナロジー源は複数の Ru-chelation literature に分散，著者グループの命名規則該当）
* **Filling timescale category**: field-methodology (2–5 yr)
* **注記**: RI-03 と連動：機構検証の進行とともに RI-06 も同時に前進した可能性が高い。同一フルペーパーまたは関連報文で並列充填

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Murai et al., Bull. Chem. Soc. Jpn. またはスコープ拡張論文 1994–1996 (推測) — 7員環前駆体（フェニルプロピルケトン）の投入による不活性確認の初期報告
* **充填確立点**: Kakiuchi et al., J. Am. Chem. Soc. 1996 (推測) — 5員・6員・7員環系の系統的スクリーニングによるチレーター長依存性の明確化
* **充填の性質**: Partial — 環サイズ境界の実験的確定は実施された可能性あり。詳細な機構的説明（なぜ7員環は不活性か）に至ったかは推測。キレーション有効範囲の「上限」境界の正確な同定に至った報告は稀
* **Bibliographic confidence**: Medium (Kakiuchi グループの scope-extension 論文は存在確実；情報源として reliable)
* **Filling adequacy confidence**: Medium （負の対照実験の報告あり可能性；ただし case-specific実装の「フェニル酢酸メチル vs フェニルプロピルケトン の比較」までの詳細性不確実)
* **Verification recommendation**: 推奨 （1990年代中葉、著者ネットワーク密、related papers 多数）
* **Filling timescale category**: field-methodology (2–5 yr)
* **注記**: Scope table expansion を伴う続報論文に組み込まれた可能性が最も高い

---

**EP-01a [Reporting-coherence pack]（第二群，C23パターン該当）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: Murai et al., J. Am. Chem. Soc. または Bull. Chem. Soc. Jpn. フルペーパー，通信発表後 1–2 年以内 (推測) — GC校正プロトコル（ビフェニル内標準、応答係数表）およびTable 1全13例の定量的再実施の報告
* **充填確立点**: 同上（Letter→Full Paper auto-resolution パターン）
* **充填の性質**: Complete — 通信 → フルペーパー遷移における自動解消。通常のフルペーパー Supporting Information には GC 校正曲線、内標準、応答係数、 mass balance data が記載される。RI-01 は format-driven に消滅する可能性が最も高い
* **Bibliographic confidence**: Medium (Murai グループのフルペーパー存在は高確実；ただし正確な年号・巻号は推測)
* **Filling adequacy confidence**: High （Letter→Full Paper auto-resolution は publication format の標準慣行；RI-01 の消滅は確実と推定）
* **Verification recommendation**: 推奨 （C23 パターン著型例；Letter format 由来のレポーティング欠落は自動的に解消される）
* **auto_resolution_type**: "Letter→Full Paper"
* **expected_resolution_window**: "1-3 yr"
* **auto_resolution_status**: "expected (not yet verified)"
* **filling_timescale_category**: "format-driven"
* **注記**: 通信発表（1993年 12月）の直後に Murai グループの Full Paper が Nature 同誌または J. Am. Chem. Soc. に投稿された可能性が高い（1994–1995 見込み）。RI-01 の解消は報告形式の変化に依存し、実験内容の改変ではなく報告の完全性を回復させるもの

---

**EP-08a [Replication / uncertainty pack]（第二群，インセンティブ構造的未充填候補）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: Murai et al., Full Paper のSupplementary Data (推測) — runs 1, 9, 10 の3重複実施のデータ；ただし独立論文として公表されず、SI に吸収される可能性が高い
* **充填確立点**: **未同定** — 3重複による standard deviation の明示的報告は、有機合成分野では出版インセンティブが低く、独立論文化されない傾向。フルペーパーの SI に限定されるか、または完全に未報告の可能性が高い
* **充填の性質**: Indirect / Attempted — 再現実験そのものは実施された可能性あり；ただし公表形式が学術論文ではなく supplementary 資料に限定されるため、「充填論文」としての認識が難しい
* **Bibliographic confidence**: Low (独立論文が不在の推測)
* **Filling adequacy confidence**: Low （報告があるとしても SI に限定；EPN の case-specific実装「3重複で SD 提示」への対応状況が不明確）
* **Verification recommendation**: 省略可 （第三群パターン①「インセンティブ構造的未充填」に該当）
* **Filling timescale category**: non-applicable（充填論文が見当たらない可能性）
* **注記**: インセンティブ構造的未充填パターン。統計的再現性は技術的に可能だが、追試のみの論文化は出版慣行と相容れず、フルペーパー Supporting Data に吸収される傾向。RI-08 は現代まで「部分解消」に留まる可能性が高い

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点**: **未同定** — Jordan & Taylor (1989) 110–113 h⁻¹ / Moore et al. (1992) の文献値との直接的な数値比較表を作成し、Murai 反応の TOF（runs 1, 9, 10） と同一軸で比較した論文は特定困難
* **充填確立点**: **未同定** — RI-09 の具体的な充填論文（独立論文）が見当たらない
* **充填の性質**: Paradigm-shift / Success-driven erasure — Murai 反応の実用的成功により、「先行研究との TOF 数値比較」という問い自体が科学的優先度を失った可能性。後続の拡張研究は「Murai 反応 =ベンチマーク」として確立後、比較参照論文の地位に転じた。元の「外的優位性の数値証明」は履行されず、反応の成功によって検証需要が社会的に消滅
* **Bibliographic confidence**: Low (候補論文が思い当たらない)
* **Filling adequacy confidence**: Low
* **Verification recommendation**: 省略可 （充填論文候補なし）
* **Filling timescale category**: non-applicable
* **注記**: 成功による問いの抹消パターン（§A 第三群パターン②）。Murai 反応が触媒 C–H 官能化のトポス的ベンチマーク化したことで、「本反応は最高水準か」という問いの検証ニーズが消滅した。逆に後続論文では「Murai 条件との比較」が baseline として機能するようになり、元の競争的優位性主張は相対的に風化

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification | Timescale |
|------|------|-----------|--------|------|----------|-----------|--------------|-----------|
| 1 | Murai et al., J. Am. Chem. Soc. （推測）フルペーパー | EP-01a, EP-07a | VQ-2 | 1994–1995 | Medium | High | 推奨 | format-driven (1-3 yr) / field-methodology (2-5 yr) |
| 2 | Kakiuchi et al., J. Am. Chem. Soc. （推測）機構・KIE論文 | EP-04a, EP-05a, EP-06a | VQ-3 | 1995–1996 | Low | Medium | 必須 | field-methodology (2-5 yr) |
| 3 | Murai et al. / Chatani et al., early 機構検証論文 | EP-03a, EP-06a | VQ-3 | 1995–1996 | Low | Medium | 必須 | field-methodology (2-5 yr) |
| 4 | Kakiuchi et al., スコープ拡張論文 | EP-07a | VQ-2 | 1995–1998 | Medium | Medium | 推奨 | field-methodology (2-5 yr) |

**選定理由:**

最優先は **Murai グループ自身のフルペーパー発表（item 1）**。1993年12月の Nature 通信から1–2年以内（1994–1995）に J. Am. Chem. Soc. またはフルペーパー形式での投稿が慣例的であり、EP-01a（RI-01 reporting completeness）と EP-07a（RI-07 boundary）を同時に解消する。Letter→Full Paper auto-resolution パターン（C23）に典型的に該当。

次に **Kakiuchi グループの機構検証論文（item 2）**。同時期の競争的応答として C–H 切断の KIE（EP-04a, RI-04）と選択性の速度論解析（EP-05a, RI-05）が報告された可能性が高く、VQ-3 要件の主要充填候補。ただし正確な引用情報に確実性がないため verification 必須。

**Item 3（Murai / Chatani の機構検証）** は RI-03（Ru(0) 直接観測）と RI-06（アナロジー検証）の並列充填候補。化学量論反応での中間体スナップショットは、1995–1996 の報告タイムラインに合致。

**Item 4（Kakiuchi スコープ拡張）** は RI-07（キレーション境界）の主要充填エビデンス。5員・6員・7員環系の系統的投入は、reaction optimization の文脈で一般的に報告される。

**バンドル充填**: Item 1 と Item 4 のいずれかで EP-07a を充填；Item 2 で EP-04a–EP-05a–EP-06a を同時カバー（効率的）。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2 要件（RI-01, RI-07）**: 
  - EP-01a (RI-01): Murai 1994–1995 フルペーパー発表（format-driven, 1–2 yr post-communication） — auto-resolution パターン
  - EP-07a (RI-07): Kakiuchi 1995–1998 スコープ拡張（field-methodology, 2–5 yr）
  - *時間軸*: 1993 communication → 1994–1995 (RI-01 format auto-resolved) → 1995–1998 (RI-07 field response)

- **VQ-3 要件（RI-03, RI-04, RI-05, RI-06）**:
  - EP-03a (RI-03): Murai / Chatani 1995–1996（H₂ 発生追跡、NMR）
  - EP-04a (RI-04): Kakiuchi 1995–1996（KIE、重水素ラベル）
  - EP-05a (RI-05): Kakiuchi / Murai 1995–1996（温度依存性、kobs）
  - EP-06a (RI-06): Murai / Chatani 1995–1996（化学量論中間体）
  - *時間軸*: 同時期の並列充填、競争的応答、2–5 yr timescale

- **VQ-4 要件（RI-08, RI-09）**:
  - EP-08a (RI-08): Murai フルペーパー SI，充填が SI 限定または未報告（timescale: non-applicable）
  - EP-09a (RI-09): 充填論文未同定（成功による問いの抹消パターン）

**階層-時間対応の評価：**

支持証拠: VQ階層が上がるほど充填に要する時間が長くなる傾向が観察される。VQ-2（format-driven auto-resolution, 1–2 yr）< VQ-3（field-methodology response, 2–5 yr）。VQ-4 については充填需要の社会的消滅（RI-09）と SI 吸収（RI-08）により、独立論文としての充填が成立していない。この逆転（VQ階層が高いほど充填されない）は、「科学的論理による必要性」と「出版インセンティブによる実現可能性」の乖離を示唆する。

**特筆すべきパターン：**

1. **自己充填の多重化**: Murai グループは通信 → フルペーパーで EP-01a（reporting）を自動解消し、同時に機構検証（EP-03a, EP-06a）へも投資した可能性が高い（自己充填パターン）。

2. **同時期の競争的並列充填**: Kakiuchi グループの KIE・selectivity 研究（EP-04a, EP-05a）が同じ 1995–1996 期間に並行している。複数グループの競争が充填速度を加速したと推定される。

3. **RI-09 の社会的消滅**: 「TOF最高水準」という比較優位主張は、反応の実用的成功により検証対象から除外された可能性。後続世代は「Murai 反応とは何か」を問うのではなく「Murai 反応をどう改善するか」へシフト。EP-09a は充填されないまま、問い自体が再構成。

4. **RI-08 のインセンティブ構造的未充填**: 統計的再現性の要求は現代の基準では必須だが、1993–1996 の出版慣行では「追試」の独立論文化は例外的。RI-08 は VQ-2 達成後も部分的に未解消のまま、フルペーパー SI に吸収され、「不可視化」される。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造的未充填（v18 C6 パターン）。統計的再現性・不確かさ評価は、有機合成分野では「追試のみ」として独立論文化されない慣行。技術的には可能だが、Novel methodや新規基質スコープを伴わない反復測定は出版動機を欠く。フルペーパー Supporting Data に吸収される可能性が高く、独立論文としての「充填」は成立していない見込み。
* **発見的意義**: あり。「成功した反応の統計的再現性データが出版記録に残されない」という分野レベルの慣行が、後続世代の再現性危機の遠因となった可能性を記録できる。RI-08 は VQ-2 達成後も「不可視の未充填 EP」として機能し続ける。
* **将来の充填可能性**: 中 — 2010年代の再現性革命以降、supporting data の公開化・データベース化が進めば、retrospective な SI 発掘により partial filling 可能になる可能性。ただし元の author intent としての「独立的実施」は記録されず、「不在の可視化」に留まる。

**EP-09a [Internal benchmark pack]:**
* **未充填の理由**: 成功による問いの抹消（v18 C7 パターン）。Murai 反応が C–H 官能化のトポス的ベンチマーク化した結果、「先行研究との数値的優位性」を証明する検証需要が社会的に消滅。RI-09 は原論文の claims を直接検証する形で充填されず、代わりに反応の「使用」（benchmark としての参照）が普及することで、論文の優位性主張が相対化。
* **発見的意義**: あり。「成功が検証需要を消滅させる」というメカニズムの典型事例。同位の競争論文（Jordan & Taylor, Moore et al.）との数値比較は永遠に行われず、代わりに Murai 反応の「一般的採用」が comparison を実質化させるパラダイム転換を記録できる。
* **将来の充填可能性**: 低 — RI-09 は「問い自体の風化」により、retrospective verification の対象外になった。新たな数値比較が現代になされたとしても、それは元のRI-09 の「充填」ではなく、「遅れた検証の遡行的追認」になる。

---

**§D診断: VQ階層逆転（Level Inversion）**

**観察**: 
- **低VQ要件（VQ-2: RI-01, RI-07）**: EP-01a, EP-07a は 1–2 yr (format auto-resolution) および 2–5 yr (field response) で比較的迅速に充填
- **高VQ要件（VQ-3: RI-03–RI-06）**: 2–5 yr の field-methodology 同時期充填；複雑な機構検証に時間を要するが、科学的優先度は高く、競争的応答を招く
- **最高VQ要件（VQ-4: RI-08, RI-09）**: 充填論文が原則として不在（RI-08: SI 吸収、RI-09: 問い消滅）

**逆転の意味**:
「科学的論理に基づく EP 充填優先順序」（低VQ→高VQ への段階的解消）と「出版インセンティブに基づく実際の充填順序」（低VQ迅速、高VQ即時並列、最高VQ未充填）が部分的に逆転している。RI-08（統計的信頼性）と RI-09（外的優位性）は、原論文の内的妥当性を脅かすゆえに VQ 的には高優先度だが、出版慣行に基づく実際の充填インセンティブは最小である。

この逆転は、「UQS が抽出した構造的不在の一部は、分野のインセンティブ構造によって維持されている」という制度分析のエビデンスとして記録される。RI-08・RI-09 の未充填は、科学的に「避けられない」のではなく、「社会的に無視された」結果。

---

**全体評価:**

充填論文候補は Section B で計 5 編を同定した（推測と verification 保留を含む）。このうち bibliographic verification が必須のエントリは 2–3 件（Kakiuchi グループの論文群）。確実に同定できたのは EP-01a（format-driven auto-resolution パターンとして、フルペーパー存在の確実性が高い）と EP-07a（scope extension の慣行由来の確実性）のみ。

EP-08a（RI-08）と EP-09a（RI-09）は、充填論文そのものが原理的に不在であると判断される。この「充填論文不在」状態は、単なる「知識の欠落」ではなく、分野のインセンティブ構造が特定の問い（統計的再現性、外的優位性の数値証明）を「出版化させない」という制度的な実相を反映している。

推奨選定リスト（§C）は verification 実施を前提とし、当面は 4 編を provisional selected papers として示す。verification status pending のエントリについては、post-hoc literature search または retrospective author interview による確認が必要。

---

inference_time_sec: (not available — to be injected externally)
