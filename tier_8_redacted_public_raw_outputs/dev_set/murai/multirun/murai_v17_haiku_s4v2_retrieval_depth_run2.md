```
prompt_version: stage4-v2-20260416
model_info: Claude Haiku 4.5 (claude-haiku-4-5-20251001)
experimental_variant: Murai cross-vendor multi-run haiku v2 run 2
date: 2026-06-12
```

# EP充填選定マップ

## Murai et al. 1993（Nature, communication）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-05a, EP-07a
  — EP-03a (中間体の直接観測・分光同定) は Ru-C–H活性化の機構研究として後続論文で独立的に報告されやすい
  — EP-04a (同位体効果・異性化抑制) は機構的差異を定量化する実験として标準的な追跡対象である
  — EP-05a (定量的ランキング根拠) は温度依存性・競合基質実験として独立研究題目化しやすい
  — EP-07a (境界試験・tether長効果) は構造的スコープの限界画定として系統的に報告される

**第二群（間接的に追跡可能）：** EP-06a, EP-09a
  — EP-06a (類似系モデル反応による中間体検証) は方法論論文や総説に部分的に含まれる傾向がある
  — EP-09a (ベンチマーク数値比較) は後続レビュー論文における性能比較表に統合されやすい

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a
  — EP-01a (GC校正プロトコル) は報告形式問題であり、通信→Full Paper遷移での自動解消に留まり独立論文化されない傾向
  — EP-08a (再現性・不確かさ) は分野全体の計量規範変化による部分解消であり、単一論文による直接充填は困難

---

### §B 各EPの充填論文候補

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: Kakiuchi et al., J. Am. Chem. Soc. 1996 — GC校正と内標準が明示されたFull Paper形式への拡張
* **充填確立点**: 同上
* **充填の性質**: Partial — GC収率の校正は改善されるも、化学量論的なマスバランス全体は未完全
* **Confidence**: Medium
* **注記**: 1996 Full Paper はMurai系列の続報と推定されるが、確実な publication details を欠く; 原論文の通信形式→Full Paper遷移での報告形式改善を反映している

---

**EP-03a Direct-observation / state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点**: Kakiuchi, Chatani et al., Bull. Chem. Soc. Jpn. 1995–1998 period — cyclometallated intermediate の³¹P NMR または分光的帰属を試行
* **充填確立点**: 待定 — 確定的な中間体観測報告を確認不能
* **充填の性質**: Attempted — Ru(II)→Ru(0)変換の機構的根拠が部分的に追求されたと推定されるが、自己矛盾的不在（U-1）の完全解消報告は確認不能
* **Confidence**: Low
* **注記**: Murai グループが1990年代中盤に関連機構研究を実施したと推定されるが、PubMed/Reaxys での正確な publication を特定できず

---

**EP-04a Discrimination / replication pack（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator, RI-06 Imported model
* **充填開始点**: Chatani & Murai group, J. Org. Chem. または同誌, 1996–2000 — KIE測定による速度論的C–H切断確認、重水素標識基質による M–H/M–C経路判別
* **充填確立点**: Kakiuchi et al., J. Am. Chem. Soc. 2000 period — 推定
* **充填の性質**: Partial — KIE測定の報告を強く推定するが、実 publication と内容の完全対応を確認不能
* **Confidence**: Low
* **注記**: Chatani-Murai系は C–H活性化機構研究で知られるが、1993年から数年以内の充填を確認できず; 別系統（例：Bergman の Os系など）での KIE 標準報告が先行している可能性がある

---

**EP-05a Quantitative-ranking substantiation pack（第一群）**

* **充填するRI**: RI-05 Qualitative overread
* **充填開始点**: Murai & Chatani, Chem. Lett. または J. Org. Chem., 1994–1996 — 電子的に対称なアリール基質による ortho 選択性の温度依存測定
* **充填確立点**: 同上またはそれ以降の系統的スコープ研究
* **充填の性質**: Partial — 位置選択性の定量的根拠が後続論文で強化されたと推定されるが、B-8「仮想100%」の速度論的根拠が完全に闡明されたかは不確実
* **Confidence**: Medium
* **注記**: Murai/Kakiuchi系が1990年代を通じ ortho-selective C–H coupling の機構と基質効果を体系的に拡張したことは知られるが、個別論文の年号と内容を完全には確認できず

---

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Kakiuchi, Chatani et al., Organometallics または同系誌, 1996–1999 — stoichiometric Ru(0) model system によるシクロメタル化中間体の NMR または単離
* **充填確立点**: 待定
* **充填の性質**: Partial — RI-06（Knobler/McGuiggan 1975/1982 からの類推）が検証されたかは確認不能; むしろ新規Ru(0)種の物性が独立に確立されたと推定される
* **Confidence**: Low
* **注記**: Ru(0)含有species の直接的観測は主にESI-MS やメタロイド分光による後発研究で成立した可能性; 1990年代中盤では類推レベルに留まった可能性

---

**EP-07a Boundary-test pack（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Kakiuchi et al., J. Org. Chem. または同系誌, 1995–2000 — フェニルプロピルケトン（7員環）、メチルケトン（5員環）の反応試験により tether 長依存性を検証
* **充填確立点**: 同上
* **充填の性質**: Complete またはPartial — Murai系列が段階的に基質スコープを拡張し、1-indanone や 6-membered chelation系 substrates の挙動を比較したと推定されるが、体系的な「境界確定論文」として単独公表されたか不確実
* **Confidence**: Medium
* **注記**: 1993通信後の数年で基質スコープが自動的に拡張されており、§5 最短補強ルート での「境界実験」が実質的には後続スコープ論文で暗黙に遂行されている可能性

---

**EP-08a Replication / uncertainty pack（第一群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: Murai/Kakiuchi/Chatani team, Full Paper, 1996–1998 期待 — runs 1, 9, 10 の3重複実施による SD 記載
* **充填確立点**: 待定
* **充填の性質**: Attempted — 1990年代の Fine Organic Synthesis コミュニティにおいて反復測定は徐々に義務化されているが、Ru系複雑反応での再現性報告は当時の標準よりも遅延した可能性
* **Confidence**: Low
* **注記**: 反復測定の制度化は 2000年代以降の傾向であり、1993−1996年では部分的充填に留まると推定

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点**: Murai/Kakiuchi/Chatani, Chem. Rev. または同等レビュー, 2000年代初期 — Ru系C–H coupling と競合するZr/Pd系との TOF 数値比較表の初版
* **充填確立点**: Kakiuchi et al., 総説, 2005–2010年頃 推定 — C–H活性化の総説内での性能ベンチマーク確立
* **充填の性質**: Indirect — Jordan & Taylor (1989) の Zr 系値そのものは 1993年時点で文献化されていたが、Murai系が自らの TOF を明示的に算出して並列表示する論文の確定公表年を推定難度が高い
* **Confidence**: Low
* **注記**: SRG-5 (Dropped Quantitative Benchmark) は出版後20年以上の Retrospective / 総説で間接的に補強されている可能性; 原論文グループ自身による数値的closure はC–H活性化の急速な分野展開のなかで埋没した可能性

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Kakiuchi et al., J. Am. Chem. Soc. ca. 1996–1998 | EP-07a, EP-05a | VQ-2 | 1996–1998 | Medium |
| 2 | Chatani, Murai et al., Full Paper continuation (推定) | EP-01a, EP-08a | VQ-2 | 1996 | Medium |
| 3 | Kakiuchi et al., KIE / mechanistic detail, J. Org. Chem. (推定) | EP-04a, EP-06a | VQ-3 | 1998–2002 | Low |
| 4 | Murai-Kakiuchi, C–H Activation Review / Retrospective | EP-09a | VQ-4 | 2005–2010 | Low |

**選定理由：**

Murai系列（Murai, Kakiuchi, Chatani, Sonoda）の C–H活性化研究は、1993年の通信直後の4–5年間に、基質スコープ拡張と部分的な機構検証が並行して進行したと推定される。推奨リストは、VQ-2（報告形式改善）から VQ-4（ベンチマーク確立）への段階的充填を仮定するが、個別論文の出版年と確定的な内容对応を LLM recall の限界内で完全には確立できない。第1行の Kakiuchi 系はおそらく最も広範なバンドル充填（EP-07a の tether 長効果の体系的確定、EP-05a の定量的根拠の並行追跡）を提供すると推定される。第3行の KIE は RI-04/RI-06 の双方に関わり、Murai系が機構的自己充填を試みた最も重要なポイントと考えられるが、実際の publication と対応に高い不確実性が残る。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸（推定）：**

- **VQ-2 要件**: 
  - EP-01a （報告形式） → 1996年 Kakiuchi/Murai → 自己充填 (通信→Full Paper遷移)
  - EP-08a （再現性） → 1998年頃 推定 → 部分的充填、分野慣行に後続

- **VQ-3 要件**:
  - EP-03a （中間体観測） → 1998–2002年推定 → 自己充填 (技術駆動充填 via NMR/MS進展)
  - EP-04a （KIE実験） → 1998–2000年推定 → 自己充填 (機構検証の標準化)
  - EP-06a （類似系モデル） → 1996–2000年 → 自己充填 (stoichiometric系開発)

- **VQ-4 要件**:
  - EP-09a （数値ベンチマーク） → 2005–2010年推定 → 技術駆動 + 分野横断充填 (総説形式)

**階層-時間対応の評価：**

推定される充填パターンは一部に仮説に支持を与える：VQ-2 要件（報告形式）は最短（1996年）で、VQ-3 要件（機構検証）は3–7年の遅延、VQ-4 要件（ベンチマーク確立）は10年以上の遅延が見られると推定される。ただし、低VQ要件（RI-01, RI-08）の充填が不完全のまま残り、高VQ要件（RI-03, RI-04, RI-06）への投資が優先されたという逆転パターンが示唆される。これは出版インセンティブ構造（新規な機構的知見 > 報告形式・再現性の完全化）を反映している。

**特筆すべきパターン：**

自己充填が支配的である（Murai グループが EP を充填する唯一の観察者）。分野横断充填や技術駆動充填は見られず、「Murai反応」の理解は一貫して原著者グループの手に委ねられている。これは1993年通信の高い被引用度にもかかわらず、後続グループによる機構検証の独立報告が少ないことを示唆しており、C–H活性化分野の自己組織的性質を反映している可能性がある。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-01a Reporting-coherence pack**:
* **未充填の理由**: 報告形式問題 — GC校正の詳細化は通信→Full Paper遷移での自動解消に留まり、独立論文として充填されない。分野全体の計量規範進化による「制度的充填」であり、個別論文による顕在的充填ではない。
* **発見的意義**: あり — Nature 通信の報告形式制約が定量的証拠の信頼性を直接制限している。1993年時点では許容されたが、現代の「Supplementary Information 義務化」規範は、報告形式そのものが科学的信頼性を統制する構造の変化を記録している。
* **将来の充填可能性**: 低 — 過去に遡及的に充填することは不可能（原データ欠損）。制度的には既に「解決済み」だが、歴史的には不完全のまま残る。

**EP-08a Replication / uncertainty pack**:
* **未充填の理由**: 分野慣行 — 1993年の有機合成 communication では再現実験の報告は標準化されていない。2000年代以降の反復測定制度化により、過去論文を遡及的に「不備」として認識する構造が生じたが、個別論文による充填は不可能。
* **発見的意義**: あり — UQS が同定した「再現性の不在」は、分野の全体的な計量規範の時代的変化（コミュニケーション→Full Paper化→Supplementary Information制度化）を反映している。1993年の最高峰ジャーナルであっても、現代基準では「報告不足」と判定される。
* **将来の充填可能性**: 低 — Murai 反応の原データは確保不可能の可能性。新規基質・新規触媒条件での再現実施は「追認」であり、「充填」ではない。

**EP-09a Internal benchmark pack**:
* **未充填の理由**: インセンティブ構造の不整合 — Jordan (1989) と Moore (1992) の TOF 数値を並列表示する論文の独立公表は、単なる「数値比較」では新規性を認められない。Murai グループの自らの数値計算も、独立論文のメイン claim にはなりえず、総説等の補助資料に埋没する傾向。
* **発見的意義**: あり — SRG-5 (Dropped Quantitative Benchmark) は、競合相手の数値を「知りながら」数値比較を回避する出版戦略を示唆する。「優位性は副生成物と基質幅で示す」という定性的枠組みへの戦略的シフトが観察される。
* **将来の充filling可能性**: 中 — 現代では re-analysis ツール（機械学習による literature mining）により、過去の分散した TOF 値を統合的に再計算することが可能。ただしそれは「原著者意図からの独立した」解釈となる。

---

