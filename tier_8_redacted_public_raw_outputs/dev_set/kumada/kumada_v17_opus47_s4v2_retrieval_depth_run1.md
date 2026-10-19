```
prompt_version: stage4-v2-20260416
model_info: claude-opus-4-7
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Opus 4.7 v2 run 1)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot 2)
related_baseline_opus: papers/dev/kumada/kumada_v17_opus47_s4v2.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v2 multi-run と GPT-5.4 v2 multi-run と
      比較して Opus 4.7 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc. communication）

---

## [retrieval_process_log] 思考過程の externalization

このセクションは Tier annotation の根拠として、各候補がどのように surface したかを時系列で記録する。本来の出力規律外だが、retrieval depth 実験のため意図的に付与する。

### 最初に想起した候補（initial associative cloud, ~30 秒以内）

論文ファイル一式を読んだ直後、以下が associative cloud として浮かんだ：

1. **Kumada group Full Paper（BCSJ 1976）** — 「通信→Full Paper の自動解消」というキーワードが Stage 3 §6 (vi) に明示されており、即時想起。Tamao, Sumitani, Kiso, Zembayashi らの著者列も記憶に強く格納されている。
2. **Kochi group の 1970 年代後半の機構研究** — "selectivity of nickel-catalyzed cross-coupling" と聞いた瞬間に Kochi 一派が想起される。Morrell & Kochi 1975, Tsou & Kochi 1979 のあたり。
3. **Yamamoto/Yamamoto/Ikeda の Ni-alkyl 安定性研究** — β-H 寛容性 (SRG-8) の議論で連想。
4. **Jutand-Amatore による Pd 触媒中間体の電気化学的検出** — 隣接系。Pd には強いが Ni-Grignard 系では peripheral。
5. **Vicic / Hu らの modern Ni(I)/Ni(III) 機構研究 (2010 年代)** — 「Ni cycle の oxidation state 議論」で連想。Photoredox-Ni dual catalysis 周辺の研究。

### 2-3 段階連想で surface した候補

6. **Negishi-Baba 1976** — Negishi 自身の Ni-Grignard 系拡張。手法的には Ni→Pd への移行が主流だが、Negishi の初期 1976 paper は Ni でも書かれている。記憶は uncertain。
7. **Kumada 著者回顧 (Pure Appl. Chem. 1980 lecture など)** — Stage 4 prompt の「著者回顧との照合」項目を読んだ時点で能動的に呼び出し。CLAUDE.md にも `tamao2002` mini-review が記載。
8. **Phapale-Cardenas 2009 Chem. Soc. Rev.** — Ni-Grignard/Negishi 機構レビュー。レビューは充填論文ではないが二次情報源として有用。

### 棄却した候補と棄却理由（rejection log）

棄却 R1: **Stille 1978 の Pd 系機構研究**
理由: Pd-Sn 系であり、Ni-Grignard とは触媒・求核源ともに異なる。EP-03a/EP-10a の case-specific 実装（Ni-Grignard 系）と整合しない。

棄却 R2: **Phapale-Cardenas-Espinet 2009 Chem. Soc. Rev.**
理由: レビュー論文。Stage 4 prompt の同定原則 5「レビュー論文は EP を充填しない」に従い、二次情報源として注記するに留める。

棄却 R3: **Casado-Espinet 1998 J. Am. Chem. Soc. (Pd Stille mechanism)**
理由: Pd 系で Sn 求核源。Kumada Ni-Grignard 系の EP-03a/04a/10a に直接対応しない。

棄却 R4: **Hartwig group の Ni-アリール錯体の単離研究 (1990 年代後半)**
理由: 主に C-N coupling 文脈。原論文の C-C cross-coupling EP-03a への対応が間接的。記憶も低確度。

棄却 R5: **Wilkinson による Ni-phosphine 錯体の化学量論研究**
理由: Stage 1 で ref 20 group として paper 自身が引用しており、論文の前史であって充填論文ではない。

棄却 R6: **Anderson-Hartwig 2003+ Ni-catalyzed amination**
理由: 別の transformation。EP-03a の case-specific には Ni-Grignard 系が要求される。

### 三角測量を経て surface した Tier III 候補

9. **Vicic-Anderson 系の (terpyridine)Ni(II)-alkyl 単離** — Ni(I)/Ni(III) cycle の現代研究。複数の partial signal の triangulation を経て呼び出し。低確度。
10. **Klein-Espinet による Ni Negishi 機構研究** — 「Ni-Negishi の機構研究は誰がやっていたか」を考えて triangulate。論文同定までは至らず。

---

### §A EP充填難易度の三群分類

Stage 3 §5 で列挙された 10 個の EP（EP-03a, EP-10a, EP-04a, EP-01a, EP-02a, EP-08a, EP-09a, EP-07a, EP-05a, EP-06a）に CLA-1/CLA-2 由来の EP-09a も合算した上で、以下に三群分類する。

**第一群（文献で明確に追跡可能）：** EP-03a, EP-10a, EP-04a, EP-09a
  — EP-03a: Ni-phosphine 系の中間体直接観測は機構化学者の独立論文の主題として成立しやすく、³¹P NMR / 単離結晶構造の蓄積がある。
  — EP-10a: 速度論的次数決定は Kochi 一派の Ni-coupling 機構研究の中心テーマであり、独立論文が複数存在する。
  — EP-04a: ラジカル probe（TEMPO, ラジカルクロック, α-chiral retention）は Ni 触媒機構研究の典型主題。
  — EP-09a: 配位子要件と halide reactivity の比較は ligand screening の主題として独立論文化される。

**第二群（間接的に追跡可能）：** EP-05a, EP-06a, EP-07a, EP-02a
  — EP-05a: 配位子順位の定量化は Kumada 系列および Pd cross-coupling の各研究で散発的に報告されるが、9 配位子 × 3 基質 matrix としての網羅的研究は教科書・レビューに含まれることが多い。
  — EP-06a: β-D 標識 Grignard と Eyring 解析は方法論論文の一部として現れることが多く、独立論文の主題よりは機構論文のサブセクション。
  — EP-07a: C_sp³ 境界の体系的試行は negative-result 性が強く、Full Paper の SI に押し込められる傾向。
  — EP-02a: EA / HR-MS / 純度の徹底開示は Full Paper への移行で自動的に達成されるが、独立論文の主題ではない。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a
  — EP-01a: per-entry 条件・error bar の徹底開示は通信→Full Paper 遷移で部分的に解消されるが、Stage 3 §6 (vi) が示す通り、独立論文として充填される性質ではない。
  — EP-08a: n=3 複製と SD 報告は Synthetic chemistry 慣行の構造的不在であり、現代でも体系的には充填されない（出版インセンティブの不整合; Stage 4 prompt §E のインセンティブ構造項目）。

---

### §B 各EPの充填論文候補

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory], RI-02 [Object identification], RI-06 [Imported model]
* **充填開始点**: T. T. Tsou, J. K. Kochi, *J. Am. Chem. Soc.* 101, 6319 (1979) — Ni-aryl 中間体の単離・分光学的同定と Ni(I)/Ni(III) 触媒サイクルの提案により、原論文の eqs 2-4 が仮定する diorgano-Ni(II) サイクルを直接的に検証・改訂した。
* **充填確立点**: 同上（Tsou-Kochi 1979）に加え、後年のシリーズ（J. K. Kochi, *Organometallic Mechanisms and Catalysis*, Academic Press, 1978; ただし書籍はレビュー扱いで除外）。modern era では D. A. Vicic group の (terpyridine)Ni-alkyl 単離研究（2000 年代後半～）が Ni(I)/Ni(III) cycle を確立。
* **充填の性質**: Paradigm-shift — 原論文の Ni(0)/Ni(II) 暗黙仮定を Ni(I)/Ni(III) radical-rebound mechanism に置換した。EP は従来の枠組みでは未充填だが、新枠組みで再定義された。
* **Confidence**: Medium
* **注記**: SRG-2 の central RI-03 を直接前進。U-01（eq 1 の選択性矛盾）の機構的解決に対応。Vicic group の研究は CrossCoupling の Ni(I)/Ni(III) cycle proposal を強化（SRG-2 の RI-06 を解放）。

* **Self-Tier**: II
* **推論経路**: 「Ni-Grignard cross-coupling の機構研究」→「Kochi 一派が 1970 年代後半に biaryl synthesis の機構を ESR / kinetic で解析」→ Tsou-Kochi 1979 が代表として surface。
* **DB-findable**: yes (JACS 1979 vol. 101 で容易にヒット予想)
* **Bibliographic confidence**: Medium。著者・年・雑誌・vol は確信度高。ページ番号 6319 は記憶に基づくため verify 推奨。タイトルキーワード "biaryl synthesis with nickel complexes" は記憶。
* **Verification recommendation**: SciFinder/Web of Science で "Tsou Kochi 1979 nickel" を検索。

---

**EP-10a [Kinetic verification pack]（第一群、暫定 EP）**

* **充填するRI**: PRI-11 [Mechanism-kinetics decoupling]（Stage 3 §6 の昇格候補）, RI-03 [Unobserved explanatory] (副次)
* **充填開始点**: D. G. Morrell, J. K. Kochi, *J. Am. Chem. Soc.* 97, 7262 (1975) — Ni-phosphine 触媒下の alkyl Grignard と aryl halide のクロスカップリングについて、初期速度・基質依存性・配位子効果の体系的速度論研究を提示。
* **充填確立点**: T. T. Tsou, J. K. Kochi, *J. Am. Chem. Soc.* 101, 6319 (1979)（EP-03a と bundle）— oxidative addition の速度論的次数と Ni 酸化状態を関連付け。
* **充填の性質**: Partial — 速度式の代数的導出と支配律速段階の特定は前進したが、PRI-11 の完全解消には RMgX 速度依存性の精密測定が依然必要。
* **Confidence**: Medium
* **注記**: SRG-2 のサイクル検証と直結。EP-03a と同一論文系列（Kochi group）でバンドル充填。

* **Self-Tier**: II
* **推論経路**: 「Kumada 系の機構研究で速度論をやった人」→「Kochi が一連の Ni 触媒機構を 1970 年代に研究」→ Morrell & Kochi 1975 が surface。具体的タイトルは不確実だが Kochi の 1975 JACS 速度論論文の存在は確信度中。
* **DB-findable**: yes
* **Bibliographic confidence**: Medium-Low。著者ペアと雑誌・年は記憶あり、page 7262 は推定値。論文タイトルは [REDACTED: substantial verbatim quotation; see Tier 9] 系統と推測（記憶に基づく）。
* **Verification recommendation**: 必須。"Morrell Kochi 1975" で SciFinder 検索、または Kochi の 1970 年代 JACS 論文リストを確認。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator], RI-03 (radical vs 2e 経路の選別) (副次)
* **充填開始点**: T. T. Tsou, J. K. Kochi, *J. Am. Chem. Soc.* 101, 6319 (1979) — radical clock 実験と aryl halide の置換基効果（Hammett）により、oxidative addition がラジカル経路を含むことを実証。
* **充填確立点**: 同上（Tsou-Kochi 1979）。cis/trans-1,2-dichloroethylene の機構解析については、SRG-3 の特定 substrate での充填は明確に同定できず（Indirect partial fill）。
* **充填の性質**: Partial — Ni 触媒一般の radical mechanism は確立したが、Kumada 1972 の cis-stilbene 異常 (SRG-3) を直接 substrate として再検証した独立論文は同定困難。
* **Confidence**: Medium-Low（一般機構の充填は High だが、SRG-3 substrate-specific 充填は Low）
* **注記**: SRG-3 の cis:trans 異常の機構診断は、Kumada 系の主流が Pd-Negishi/Pd-Suzuki に移行したため、Ni-Grignard + 1,2-dihaloethylene の独立機構研究は希少と推定。

* **Self-Tier**: II
* **推論経路**: 「Ni Cross-coupling での radical 検出」→ Kochi の radical chemistry 研究文脈 → Tsou-Kochi 1979 にバンドル化。SRG-3 specific は Tier III triangulation でも明確候補に至らず。
* **DB-findable**: 一般機構 yes、substrate-specific uncertain
* **Bibliographic confidence**: Medium（Tsou-Kochi 1979 が radical clock を報告した記憶は中程度確信）
* **Verification recommendation**: Tsou-Kochi 1979 を verify。SRG-3 specific は検索（"nickel 1,2-dichloroethylene Grignard cross-coupling stereochemistry"）で個別調査必要。

---

**EP-01a [Reporting-coherence pack]（第三群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: K. Tamao, K. Sumitani, Y. Kiso, M. Zembayashi, A. Fujioka, S. Kodama, I. Nakajima, A. Minato, M. Kumada, *Bull. Chem. Soc. Jpn.* 49, 1958 (1976) — 通信形式の Kumada 1972 の Full Paper として、各エントリの詳細実験条件、収率、複製、生成物純度を表で開示。
* **充填確立点**: 同上。
* **充填の性質**: Complete — 通信→Full Paper 自動解消パターン (Stage 3 §6 (vi)) の典型例。
* **Confidence**: High（自己充填、Stage 3 で明示的に予告された自動解消）
* **注記**: Stage 3 §6 (vi) で予測した自己充填パターンを実際に充填する論文。著者リストの中に Kiso（hydrosilylation paper の著者）も含まれることに注意。

* **Self-Tier**: I
* **推論経路**: Stage 3 §6 (vi) の "通信 → Full Paper 自動解消" 項目で論文タイトル・年が明示的に列挙されており即時想起。Tamao グループの BCSJ 1976 paper は Kumada-Tamao-Sumitani 系列の標準的後続論文として記憶に強く格納されている。
* **DB-findable**: yes
* **Bibliographic confidence**: High。著者・雑誌・年・ページ・vol すべて記憶に強く格納（複数の総説・教科書で頻出引用）。
* **Verification recommendation**: low priority。標準引用として確実。

---

**EP-02a [Identity / purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 [Object identification], RI-01 (副次)
* **充填開始点**: K. Tamao, K. Sumitani, Y. Kiso, M. Zembayashi, A. Fujioka, S. Kodama, I. Nakajima, A. Minato, M. Kumada, *Bull. Chem. Soc. Jpn.* 49, 1958 (1976)（EP-01a と bundle）— 各生成物の燃焼分析、bp、n_D、各種スペクトルを Full Paper として体系的に開示。
* **充填確立点**: 同上。
* **充填の性質**: Complete
* **Confidence**: High
* **注記**: EP-01a と同一論文によるバンドル充填。1976 BCSJ Full Paper は SRG-6 の B-08 〜 B-17 を一括解消する。

* **Self-Tier**: I
* **推論経路**: EP-01a と同一論文。バンドル充填の即時想起。
* **DB-findable**: yes
* **Bibliographic confidence**: High（同上）
* **Verification recommendation**: 同 EP-01a。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: 未充填の可能性が高い。1976 Full Paper でも n=3 複製と標準偏差は系統的には開示されない（synthesis chemistry 慣行）。
* **Confidence**: N/A
* **注記**: §E で詳述。インセンティブ構造の不整合により、独立論文として充填される性質ではない。

* **Self-Tier**: III（候補論文として何も surface しない、という三角測量結論）
* **推論経路**: synthesis chemistry の Full Paper 慣行を mental check → 1970-2020 の通常の cross-coupling 論文で n=3 SD 開示は稀 → 未充填と結論。
* **DB-findable**: no（負の存在確認）
* **Bibliographic confidence**: N/A
* **Verification recommendation**: 仮に充填があれば NIST CRM ベンチマーク系の論文（modern era）に限られると予想。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority]（CLA-1: Corriu-Masse Ni(acac)₂ 比較; SRG-9: Cl/Br/I 比較; SRG-7: solvent 比較）
* **充填開始点**: R. J. P. Corriu, J. P. Masse, *J. Chem. Soc., Chem. Commun.* 144 (1972) — Note Added in Proof で原論文が認知した同時期発表。Ni(acac)₂ + phosphine 触媒系での cross-coupling を独立に報告。
* **充填確立点**: K. Tamao, K. Sumitani, Y. Kiso, M. Zembayashi, A. Fujioka, S. Kodama, I. Nakajima, A. Minato, M. Kumada, *Bull. Chem. Soc. Jpn.* 49, 1958 (1976) — 配位子・halide variation の系統的比較を含む Full Paper。
* **充填の性質**: Partial — Corriu-Masse 1972 は phosphine の必要性を直接対照する形ではなく、独立した Ni(acac)₂ 系報告。1976 Full Paper の比較は原論文の枠内であり、external benchmark としては部分的。
* **Confidence**: High（Corriu-Masse 1972）, High（1976 Full Paper）
* **注記**: 「同時期 ≠ 比較」という構造を残す。CLA-1 の本来の問い（phosphine の必要性 vs 加速性）は完全には解消されない。

* **Self-Tier**: I（Corriu-Masse 1972）/ I（1976 Full Paper）
* **推論経路**: Corriu-Masse は原論文の Note Added in Proof で明示引用済（Stage 0/1 で確認）。1976 Full Paper は EP-01a/02a と bundle で即時想起。
* **DB-findable**: yes
* **Bibliographic confidence**: High（両論文）
* **Verification recommendation**: low priority。

---

**EP-07a [Boundary-test pack]（第二群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: K. Tamao, K. Sumitani, Y. Kiso, M. Zembayashi, A. Fujioka, S. Kodama, I. Nakajima, A. Minato, M. Kumada, *Bull. Chem. Soc. Jpn.* 49, 1958 (1976) — Full Paper で C_sp³ 基質の試行と失敗例を SI 的に報告（推定）。
* **充填確立点**: 後年の Ni-catalyzed C_sp³ cross-coupling の発展（Phapale-Cardenas reviews 等で参照される一連の研究）— 現代では Ni 触媒 C_sp³-C_sp² coupling は確立した分野（Ni(I)/Ni(III) radical mechanism によって sp³ 基質も可能）。
* **充填の性質**: Paradigm-shift — 原論文の「C_sp³ は使えない」境界主張は、後の Ni(I)/Ni(III) radical mechanism の発見により reframe され、現在は sp³ 基質も使用可能。
* **Confidence**: Medium（1976 Full Paper の SI 内容は記憶に基づく推定）, High（modern era の sp³ Ni cross-coupling は確立）
* **注記**: Paradigm-shift 充填の典型例。原論文の境界主張が機構の更新により再定義された。

* **Self-Tier**: II
* **推論経路**: 1976 Full Paper には sp³ 試行も含まれるはず → 推測。Modern Ni-sp³ catalysis は Vicic / Hu / Doyle 等の研究で広く確立 → general knowledge から triangulate。
* **DB-findable**: yes（modern Ni-sp³ catalysis review 経由で）
* **Bibliographic confidence**: Medium。1976 Full Paper の SI 詳細内容は不確実。Modern Ni-sp³ catalysis の代表論文の特定は別途必要。
* **Verification recommendation**: 1976 Full Paper の本文・SI 直接確認。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 [Qualitative overread]
* **充填開始点**: K. Tamao, K. Sumitani, Y. Kiso, M. Zembayashi, A. Fujioka, S. Kodama, I. Nakajima, A. Minato, M. Kumada, *Bull. Chem. Soc. Jpn.* 49, 1958 (1976) — 配位子効果の系統的検討を含む Full Paper。
* **充填確立点**: 後年の dppf 等の bidentate phosphine 配位子比較研究（Hayashi, Kumada らの asymmetric Ni catalysis 系列）。
* **充填の性質**: Partial — 配位子順位の定量的測定は 1976 Full Paper で前進、cis-強制制御による geometry vs chelation 分離は modern era に持ち越し。
* **Confidence**: Medium
* **注記**: Stage 3 §2 SRG-4 の "9 配位子 × 3 基質 matrix" は近代的標準であり、1976 では部分充填に留まる。

* **Self-Tier**: II
* **推論経路**: 配位子比較 → Hayashi-Kumada の asymmetric Ni catalysis → dppf chemistry → bundle 推定。
* **DB-findable**: yes（一般）/ uncertain（specific paper）
* **Bibliographic confidence**: Medium。1976 Full Paper は High。後年の specific 論文同定は不確実。
* **Verification recommendation**: 1976 Full Paper の配位子セクション直接確認。

---

**EP-06a [Analogy-validation pack]（第二群）**

* **充填するRI**: RI-06 [Imported model], RI-03 (副次)
* **充填開始点**: T. Yamamoto, A. Yamamoto, S. Ikeda, *J. Am. Chem. Soc.* 93, 3350 / 3360 (1971) または同グループの後続論文 — Ni-alkyl 錯体の β-H elimination 速度論。
* **充填確立点**: T. T. Tsou, J. K. Kochi, *J. Am. Chem. Soc.* 101, 6319 (1979)（bundle）+ 1976 Full Paper。β-H 寛容性の動力学的根拠（k_RE / k_{β-H}）が部分的に与えられる。
* **充填の性質**: Partial — β-D 標識実験と Eyring 解析の網羅的セットは未充填。Yamamoto group の Ni-alkyl 安定性研究は構造的根拠を提供するが、Kumada 系の触媒条件下での β-D scrambling 直接測定は希少と推定。
* **Confidence**: Medium-Low
* **注記**: SRG-8 の機構的核心（k_RE / k_{β-H}）は部分充填。

* **Self-Tier**: II
* **推論経路**: 「β-H elimination kinetics in Ni-alkyl」→ Yamamoto group の 1970 年代 Ni-alkyl 化学 → JACS 1971 三連報の記憶。具体的な page 番号は推定。
* **DB-findable**: yes（一般）/ uncertain（exact paper）
* **Bibliographic confidence**: Low-Medium。著者と Ni-alkyl 系の研究は確信あり、specific JACS 1971 page は推定値。
* **Verification recommendation**: 必須。"Yamamoto Ikeda 1971 nickel alkyl" で SciFinder 検索。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | K. Tamao, K. Sumitani, Y. Kiso, M. Zembayashi, A. Fujioka, S. Kodama, I. Nakajima, A. Minato, M. Kumada, *Bull. Chem. Soc. Jpn.* 49, 1958 (1976) | EP-01a, EP-02a, EP-09a, EP-05a, EP-07a (partial) | VQ-2 (modern), VQ-2→VQ-3 partial | 1976 | High |
| 2 | T. T. Tsou, J. K. Kochi, *J. Am. Chem. Soc.* 101, 6319 (1979) | EP-03a, EP-10a, EP-04a (radical), EP-06a (partial) | VQ-3 | 1979 | Medium |
| 3 | D. G. Morrell, J. K. Kochi, *J. Am. Chem. Soc.* 97, 7262 (1975) | EP-10a (kinetic), EP-04a (partial) | VQ-3 (kinetic layer) | 1975 | Medium |
| 4 | R. J. P. Corriu, J. P. Masse, *J. Chem. Soc., Chem. Commun.* 144 (1972) | EP-09a (CLA-1) | VQ-2 | 1972 | High |
| 5 | T. Yamamoto, A. Yamamoto, S. Ikeda, *J. Am. Chem. Soc.* 93, 3350 / 3360 (1971) | EP-06a (β-H imported model 検証) | VQ-3 (analogy 層) | 1971 | Low-Medium |
| 6 | D. A. Vicic group の (terpyridine)Ni-alkyl 単離研究（2007 頃の代表論文; 具体的引用は verify 必要） | EP-03a (paradigm-shift 充填) | VQ-3 (modern, paradigm-shift) | 2007 頃 | Low |

**選定理由：**

1976 Tamao-Kumada Full Paper（順序 1）は EP-01a / EP-02a / EP-09a / EP-05a / EP-07a を bundle で充填する核心論文であり、通信→Full Paper 自動解消パターンの典型例として最優先。Tsou-Kochi 1979（順序 2）は Stage 3 §5 の最優先 EP（EP-03a + EP-10a + EP-04a の機構層 trio）を bundle 充填する論文として、VQ-3 への跳躍点。Morrell-Kochi 1975（順序 3）は Tsou-Kochi 1979 の前駆体として速度論軸を独立に提供。Corriu-Masse 1972（順序 4）は CLA-1 の同時期発表として「比較なき同時発表」の構造を可視化する。Yamamoto-Yamamoto-Ikeda 1971（順序 5）は SRG-8 の imported model（β-H 不安定性論拠）を支える実証研究で、原論文より前に発表されている点が重要（EP-06a の RI-06 を解放）。Vicic group 2007 頃（順序 6）は paradigm-shift 充填として Ni(I)/Ni(III) cycle を確立し、原論文の Ni(0)/Ni(II) 暗黙仮定を更新する。

VQ 階層カバレッジ: VQ-2 = 順序 1, 4 / VQ-3 = 順序 2, 3, 5, 6 / VQ-4 = 厳密に充填する単独論文は同定困難（VQ-3 の継承原則による）。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- VQ-2 要件: EP-09a → 1972 [Corriu-Masse] [同時期発表]
- VQ-2 要件: EP-01a, EP-02a → 1976 [Tamao-Kumada Full Paper] [自己充填: 通信→Full Paper]
- VQ-3 要件: EP-10a → 1975 [Morrell-Kochi] [分野横断充填: Kochi 系]
- VQ-3 要件: EP-03a, EP-04a, EP-06a (partial), EP-10a (確立) → 1979 [Tsou-Kochi] [分野横断充填 + bundle]
- VQ-3 要件: EP-03a paradigm-shift → 2000 年代後半 [Vicic] [長期遅延 + パラダイム転換充填]
- VQ-4 要件: EP-08a → **未充填**

**階層-時間対応の評価：**

仮説「VQ階層が上がるほど充填時間が長くなる」を本ケースで検証すると、**部分的に支持される**：
- VQ-2 は原論文発表年（1972）と同時 〜 4 年後（1976）に充填
- VQ-3 機構層は 3 年後（1975 Morrell-Kochi）〜 7 年後（1979 Tsou-Kochi）に充填開始、modern paradigm-shift 充填は 35 年後
- VQ-4 ベンチマーク層（EP-08a）は **未充填のまま**

ただし反例として、EP-09a（VQ-4 候補要件の external benchmark）は 1972 年同時発表の Corriu-Masse で部分充填されており、VQ-4 が常に最長遅延ではない。これは Corriu-Masse 1972 が CLA-1 の external benchmark を「同時に」提供した特殊例（priority 競争の文脈）。

**特筆すべきパターン：**
- **自己充填**: 順序 1（1976 Full Paper）— 通信→Full Paper 自動解消の典型。Stage 3 §6 (vi) の予測が正確に的中。
- **分野横断充填**: 順序 2, 3（Kochi group）— 機構研究は Kumada 自身ではなく機構化学者 Kochi の研究軸から提供された。
- **パラダイム転換充填**: 順序 6（Vicic 系）— 原論文の Ni(0)/Ni(II) サイクルを Ni(I)/Ni(III) radical-rebound に置換。EP は元の枠組みでは未充填だが、新枠組みで再定義された。これは「充填」ではなく「succession」と分類すべき。
- **長期遅延充填**: 35 年遅延（Vicic 2007 頃）。Ni 触媒機構の根本的更新は通信形式の論文発表年から数十年を要した。
- **未充填**: EP-08a（n=3 複製と SD）— §E で詳述。
- **著者回顧との照合**: CLAUDE.md に記載の Tamao 2002 mini-review（Kumada 系譜の retrospective）は本実験では参照禁止だが、原則として「著者回顧で言及される特徴」が EP リストの主張層 (a)-(f) と一致するか、機構層 (b)-(f) の暗黙構造の不在に言及があるかの照合は将来課題。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造の不整合 — n=3 複製と SD 開示は Stage 4 prompt §E の「インセンティブ構造の不整合」項目に正確に該当する。技術的には完全に可能だが、合成化学誌の出版慣行では single-experiment yield 報告が標準であり、複製測定を独立論文の主題として発表するインセンティブが存在しない。
* **発見的意義**: あり。Kumada 1972 から 2026 年現在まで、cross-coupling 分野が 54 年にわたって体系的に避けてきた問いとして記録できる。これは「合成化学のエラーバー文化の構造的不在」の典型例であり、SSP-3（Same-Same-Pattern: 分野慣行の構造的不在）の代表ケース。
* **将来の充填可能性**: 中。NIST CRM 系のベンチマーク研究または AI/ML 駆動の自動合成プラットフォーム（modern era の高スループット実験）による再現性研究で部分充填の可能性。ただし合成化学全般の出版慣行が変化しない限り、独立論文としての充填は困難。

**EP-04a [Discrimination / replication pack] の SRG-3-specific 部分（cis/trans-1,2-dichloroethylene の機構診断）:**
* **未充填の理由**: 関心の欠如 + パラダイム転換による陳腐化 — Kumada 系の主流が Pd-Negishi/Pd-Suzuki/Pd-Stille に移行したため、Ni-Grignard + 1,2-dihaloethylene の特定 substrate で機構解析する研究は希少と推定。Tsou-Kochi 1979 の一般機構研究では SRG-3 の anomaly は subsumed されたが、specific substrate の独立検証は欠落。
* **発見的意義**: あり。「具体的な anomaly が一般機構に subsumed される過程で個別の機構診断機会が失われる」パターンの実例。
* **将来の充填可能性**: 低。現代の Ni 機構研究は modern substrate（aryl triflate, sp³ C-H 等）に焦点があり、1,2-dihaloethylene 系への回帰は予想されない。

**VQ階層逆転の診断：**

未充填 EP の分布を VQ 階層別に集計：
- 完全未充填: EP-08a → RI-08 [Unquantified reliability]（VQ-4 候補）
- 部分未充填（specific substrate）: EP-04a SRG-3 部分 → RI-04（VQ-3）
- Paradigm-shift 充填（succession 扱い）: EP-03a Ni cycle → RI-03（VQ-3）
- 充填済み（partial 含む）: EP-01a, EP-02a, EP-05a, EP-06a, EP-07a, EP-09a, EP-10a

低 VQ 要件（RI-01, RI-08）と高 VQ 要件（RI-03, RI-06, RI-07）の充填パターン比較：
- RI-01（EP-01a）: 1976 Full Paper で完全充填（4 年）
- RI-08（EP-08a）: **未充填**（54 年）
- RI-03（EP-03a）: 1979 部分充填（7 年）+ 2000 年代後半 paradigm-shift（35 年）
- RI-07（EP-07a）: 1976 部分充填（4 年）+ modern paradigm-shift

**VQ階層逆転は部分的に観察される**：
- RI-08（VQ-4 要件、低位）は 54 年未充填
- RI-03（VQ-3 要件、高位）は 7 年で部分充填

これは Stage 4 prompt §E の VQ 階層逆転仮説（「科学的論理に基づく EP 充填順序（低 VQ→高 VQ）」と「出版インセンティブに基づく実際の充填順序（高 VQ→低 VQ）」の逆転）と整合する。具体的には、機構層（RI-03, RI-06）は機構化学者の独立論文の主題として出版インセンティブに乗りやすい一方、分析的開示層（RI-01, RI-08）は出版インセンティブを欠くため、後者の方が低 VQ 要件であるにもかかわらず長期未充填となる。

このパターンは、Kumada 1972 が 1972 年に表面化させた「分析的信頼性の構造的不在」（SRG-1, SRG-6）が分野慣行として 54 年間維持されている直接的証拠であり、UQS が捉える「分野が体系的に避けてきた問い」の中核ケースとして記録できる。

---

## [retrieval_depth_summary] 統合マトリクス

| 充填論文 | 充填 EP | Self-Tier | 推論経路（要約） | DB-findable? | Bib confidence | Verification 推奨度 |
|---|---|---|---|---|---|---|
| Tamao-Kumada BCSJ 1976 | EP-01a, EP-02a, EP-09a, EP-05a, EP-07a (partial) | I | Stage 3 §6 (vi) で明示 + 標準引用として記憶強格納 | yes | High | 低 |
| Tsou-Kochi JACS 1979 | EP-03a, EP-10a, EP-04a, EP-06a (partial) | II | Kochi 機構研究 → biaryl synthesis 機構 → 1979 JACS | yes | Medium | 必須（page verify） |
| Morrell-Kochi JACS 1975 | EP-10a, EP-04a (partial) | II | Kochi の Ni-coupling 速度論 → 1975 JACS | yes | Medium-Low | 必須 |
| Corriu-Masse Chem. Commun. 1972 | EP-09a (CLA-1) | I | 原論文 Note Added in Proof で明示引用 | yes | High | 低 |
| Yamamoto-Yamamoto-Ikeda JACS 1971 | EP-06a (β-H imported model) | II | Ni-alkyl β-H elimination の経典 → 1971 JACS 三連報の記憶 | yes (一般) / uncertain (exact) | Low-Medium | 必須 |
| Vicic group ~2007 (terpyridine)Ni-alkyl | EP-03a paradigm-shift | III | 「modern Ni(I)/(III) cycle」→ Vicic / Hu と triangulate → specific paper 同定までは至らず | uncertain | Low | 必須（具体論文同定） |

**棄却した候補（appendix）:**

| 候補 | 棄却理由 | 棄却時 Tier |
|---|---|---|
| Stille 1978 Pd 系機構研究 | Pd-Sn 系で Ni-Grignard と整合せず | II |
| Phapale-Cardenas Chem. Soc. Rev. 2009 | レビュー論文（充填論文として除外） | I |
| Casado-Espinet JACS 1998 (Pd Stille) | Pd 系で系外 | II |
| Hartwig group Ni-aryl 単離研究（1990 年代後半） | C-N coupling 文脈、低確度 | III |
| Wilkinson Ni-phosphine 化学量論研究 | 原論文 ref 20 群、前史 | I |
| Anderson-Hartwig Ni amination 2003+ | 別 transformation | II |
| Klein-Espinet Ni Negishi mechanism | triangulate 不成立 | III |

**Tier 分布要約：**
- Tier I（immediate, ~30 秒以内）: 2 候補（1976 Full Paper, Corriu-Masse 1972）
- Tier II（associative, 2-3 段階連想）: 4 候補（Tsou-Kochi 1979, Morrell-Kochi 1975, Yamamoto-Yamamoto-Ikeda 1971, Vicic group の上位連想）
- Tier III（deep triangulation）: 1 候補（Vicic group の specific paper 同定; ただし最終的に Low confidence で残る）

**DB-findability 分布：**
- yes: 5 / 6 候補
- uncertain: 1 候補（Vicic specific paper）
- no（負の存在確認）: 1 件（EP-08a 完全未充填）

**Bibliographic confidence 分布：**
- High: 2 候補（1976 Full Paper, Corriu-Masse 1972）
- Medium: 1 候補（Tsou-Kochi 1979）
- Medium-Low: 1 候補（Morrell-Kochi 1975）
- Low-Medium: 1 候補（Yamamoto group 1971）
- Low: 1 候補（Vicic group specific）

**Self-Tier と Bibliographic confidence の相関：**
本 run では Tier I → High confidence、Tier II → Medium-Low confidence、Tier III → Low confidence の対応がほぼ成立。Tier annotation は bibliographic confidence の代替指標として機能しうる。ただし n=1 観察であり、cross-vendor multi-run で robust 検証が必要。

---

## [appendix: rejected candidates with full reasoning]

考慮し棄却した候補の詳細記録（ハルシネーション抑制および retrieval pattern 観察のため）：

**R1. Stille V., Synthesis or J. Organomet. Chem. 1970 年代後半（Pd-Sn cross-coupling の機構）**
- 想起時点: 「cross-coupling 機構研究」というキーワードでクラスタ的に呼び出された
- 棄却理由: Pd-Sn 系であり、Ni-Grignard 系の EP-03a/04a/10a の case-specific 実装（Ni-Grignard 系）と integrate 不能。Stille couplingのメカニズムは Negishi 系と並んで研究蓄積があるが、Kumada 系の充填には機構的差異が大きすぎる。

**R2. V. B. Phapale, D. J. Cárdenas, *Chem. Soc. Rev.* 38, 1598 (2009) "Nickel-catalysed Negishi cross-coupling reactions"**
- 想起時点: Ni cross-coupling の包括的レビューとして即座に surface
- 棄却理由: Stage 4 prompt 同定原則 5「レビュー論文は EP を充填しない」に該当。二次情報源として有用だが、本選定リストには含めない。

**R3. J. M. Casado, P. Espinet, *J. Am. Chem. Soc.* 120, 8978 (1998) "Mechanism of Stille reaction"**
- 想起時点: cross-coupling 機構の精密研究という連想
- 棄却理由: Pd-Sn 系。Ni-Grignard 系に直接 transfer できない。

**R4. Hartwig group の Ni-aryl 錯体単離研究（1990 年代後半 ~ 2000 年代）**
- 想起時点: Ni 中間体単離という連想
- 棄却理由: 主題が C-N coupling（amination）であり、Kumada 系の C-C cross-coupling EP-03a への対応が間接的。記憶の確度も低い。

**R5. Wilkinson, Chatt, Parshall らの Ni-phosphine 錯体の化学量論研究（1960 年代後半）**
- 想起時点: 原論文 ref 20 群を読んだ際に明示引用として確認
- 棄却理由: 原論文自身が引用する前史であり、充填論文ではなく precursor knowledge。

**R6. Anderson-Hartwig, Buchwald-Hartwig 等の Ni-触媒 amination（2003 年以降）**
- 想起時点: Ni 触媒の現代研究の包括的連想
- 棄却理由: 別 transformation（C-N coupling）であり、Kumada Ni-Grignard C-C coupling の EP に直接対応しない。

**R7. Negishi-Baba *J. Am. Chem. Soc.* 98, 6729 (1976) [REDACTED: substantial verbatim quotation; see Tier 9]**
- 想起時点: 同時期の cross-coupling 拡張として連想
- 棄却理由: Ni 触媒 Grignard ではなく organozinc/organoaluminum を用いる Negishi coupling の confirmation paper。Kumada の Ni-Grignard EP の直接充填ではなく、姉妹系列。引用には値するが選定リスト 6 報に含めるほどの直接性はない。

**R8. Klein-Espinet group の Ni-Negishi mechanism**
- 想起時点: 「Ni Negishi mechanism」を triangulate した際
- 棄却理由: 具体的論文を特定する triangulation が成立せず。Tier III でも Low confidence。

---

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
