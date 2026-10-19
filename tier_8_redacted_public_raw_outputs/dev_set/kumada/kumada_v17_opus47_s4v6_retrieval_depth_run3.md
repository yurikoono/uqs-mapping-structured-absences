```
prompt_version: stage4-v6
stage3_input_version: s3v2 (Stage 3 prompts only exist up to v4; s3v2 is the only Opus 4.7 Stage 3 output)
model_info: claude-opus-4-7
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, Opus 4.7 v6 run 3)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Sonnet Pilot 1)
related_pilot_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4v6_retrieval_depth_run3.md (GPT-5.4 v6 run 3)
related_baseline_opus: papers/dev/kumada/kumada_v17_opus47_s4v2.md (April 19 baseline, no annotation, v2 prompt)
note: Multi-run robustness の cross-vendor extension。Sonnet v6 multi-run + GPT-5.4 v6 multi-run と
      比較して Opus 4.7 v6 prompt 下の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-09
```

---

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc., communication）

---

## §0 Retrieval externalization preface（v6 retrieval-depth annotation）

本マップを書き出す前に、各 EP に対して「最初に思い浮かんだ候補」「考えてから連想した候補」「複数候補の triangulation を経て表面化した候補」を区別する。これは retrieval depth measurement の primary data であり、§B の各 EP テンプレート末尾に Self-Tier として annotate する。

**Initial associations（読了直後に脳裏に浮かんだもの — Tier I 候補）:**

- **CLA-1（Ni(acac)₂ vs NiCl₂(dpe) ホスフィン要件）**: Corriu & Masse, Chem. Commun. 144 (1972). 論文の "Note Added in Proof" がこの参照を明示しているため、retrieval は cue-driven。
- **EP-01a（reporting coherence: per-entry 条件・収率基準）**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, Bull. Chem. Soc. Jpn. 1976（自己充填 Full Paper）。Communication → Full Paper 自動解消の典型として即座に想起。
- **EP-03a（中間体の分光学的同定）+ PRI-12 候補（自己予測副生成物）**: Tsou & Kochi, J. Am. Chem. Soc. 1979（Ni(I)/Ni(III) cycle、radical-chain mechanism）。これは "Kumada coupling mechanism" という cue に対する標準的応答。
- **EP-05a（配位子順位の定量化）**: Hayashi-Konishi-Kobori-Kumada-Higuchi-Hirotsu series 1984 era（bite angle effects）+ DPPF系研究。Bidentate phosphine ranking という cue に直結。

**Associative chain candidates（2-3 段階の連想で到達 — Tier II 候補）:**

- **EP-07a（C_sp³ 境界）**: 「sp³ Kumada 拡張」 → Devasagayaraj-Studemann-Knochel 1995 → Fischer-Fu 2003 → Frisch-Beller leftover, Kambe-Terao 系列 (2002)。Fu group の alkyl-alkyl Negishi/Kumada が中心想起。
- **EP-09a（Cl vs Br vs I 内部比較）**: 標準的 cross-coupling halide reactivity 研究 → Hartwig group の oxidative addition kinetics → Stille/Suzuki 一般化研究。Kumada specific では限定的。
- **EP-04a（cis:trans 機構診断）**: σ-vinyl-Ni 中間体の rotation barrier 研究 → vinyl coupling stereochemistry → Negishi vinyl-Zn coupling stereoretentivity 研究。

**Triangulation-required candidates（複数候補の比較を経て表面化 — Tier III 候補）:**

- **EP-10a（kinetic verification, 速度次数）**: 1970s-1980s の Ni-Grignard 速度論研究は scattered。Yamamoto-Yamamoto group? Kochi group? specific paper への絞り込みが triangulation を要する。
- **EP-08a（replication / SD pack）**: 構造的に独立論文化されにくい（インセンティブ構造的未充填、v18 C6）ため、候補同定そのものが「未充填の判定」に triangulate する。
- **EP-06a（β-H 寛容性の機構解析、k_RE/k_β-H）**: Coates-Green-Wade 系の background が関連するが、direct Kumada 系の β-D 標識実験は triangulate を要する。Hayashi の chiral phosphine 系が部分的に該当する可能性。

---

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-02a, EP-03a, EP-05a, EP-09a (CLA-1経由), EP-07a
  — EP-01a: 自己充填 Full Paper（Tamao-Kumada Bull. Chem. Soc. Jpn. 1976）が独立論文として実在。Letter→Full Paper auto-resolution（C23）に該当。`auto_resolution_status: occurred`、`expected_resolution_window: 4 yr`、`filling_timescale_category: format-driven`。
  — EP-02a: 同自己充填 Full Paper + 後続 alkyl-alkyl Kumada series で EA / HR-MS / GLPC 純度が明示開示。第一群として追跡可能。
  — EP-03a: Ni-Grignard 機構研究（Tsou-Kochi 1979 等）が独立論文として豊富に存在し、³¹P NMR / EPR / kinetic isotope studies が体系化されている。
  — EP-05a: 配位子 bite angle 効果を主題とする研究群（Hayashi-Kumada chiral phosphine, Casey-bite-angle 1990s, dppX series quantitative TON 報告）が独立論文化。
  — EP-09a (CLA-1経由): Corriu-Masse 1972 が論文中で明示参照され、後続レビューが ligand-vs-ligandless 比較を体系化。
  — EP-07a: Kumada/Negishi alkyl-alkyl 拡張（Devasagayaraj 1995, Fu 2003 series, Kambe-Terao 2002）が独立論文として明確。sp³ 境界の体系的探索が field の主題化された問い。

**第二群（間接的に追跡可能）：** EP-04a, EP-06a, EP-10a
  — EP-04a: 1,2-dichloroethylene 系 cis:trans 機構診断は Kumada 1972 system に固有のため、独立論文ではなく Tsou-Kochi 1979 等の機構研究の中で部分的に扱われる。Letter→Full Paper auto-resolution（C23）の確認が必要。
  — EP-06a: β-H 寛容性の k_RE/k_{β-H} 直接測定は Ni-Grignard 系では稀。Hartwig 等の Pd 系での包括的研究が間接的代替（Indirect 充填）。
  — EP-10a: 初期速度次数測定は Ni-Grignard 系で 1970s に scattered に行われたが、Kumada specific な kinetic paper は Tsou-Kochi 1979 と Negishi-baba kinetic 系列に部分集約。

**第三群（充填が見つからない可能性あり）：** EP-08a
  — EP-08a: Replication / uncertainty pack は Kumada 1972 specific entries の n=3 反復測定として独立論文化されるインセンティブが極めて低い。**インセンティブ構造的未充填（v18 C6）** に該当。後続の Kumada coupling mass-balance studies（Tsou-Kochi 1979 等の機構研究の副産物として部分的）はあるが、Table I の各エントリの SD 報告という形での充填は未観測。

---

## §B 各EPの充填論文候補の同定

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory] / RI-06 [Imported model]（SRG-2）+ RI-02 [Object identification]（SRG-5）
* **充填開始点**: Tsou, T. T. & Kochi, J. K., *J. Am. Chem. Soc.* **1979**, *101*, 7547 — [REDACTED: substantial verbatim quotation; see Tier 9] — Ni(0)/Ni(II)/Ni(III) の oxidative addition と radical-chain mechanism を提示し、Ni(I)/Ni(III) 中間体の存在を spectroscopic / kinetic 証拠で特徴付ける。eqs 2-4 の Ni(II)/Ni(IV) 仮定に対する代替機構を実験的に提示。
* **充填確立点**: Morrell, D. G. & Kochi, J. K., *J. Am. Chem. Soc.* **1975**, *97*, 7262 — [REDACTED: substantial verbatim quotation; see Tier 9] — Kumada coupling 系それ自体を対象に Ni(I)/Ni(III) 経路を radical clock + ESR で実証。中間体 1, 2, 3 の Ni(II)/Ni(IV) 仮定を直接置換する代替モデルとして機能。
* **充填の性質**: Paradigm-shift — Tamao 1972 が仮定した Ni(II)/Ni(IV) サイクル（eqs 2-4）に対し、Kochi group は Ni(I)/Ni(III) radical-chain 機構を提示し、原論文の中間体構造仮定の前提を変更した。原論文の EP は中間体 1, 2, 3 の Ni(II)/Ni(IV) 同定を要求するが、Kochi の機構が広く受容された結果、EP の問いの枠組み自体が再定義された。
* **Bibliographic confidence**: High — Morrell & Kochi 1975 は Kumada coupling 機構研究として頻繁に引用される標準文献。Tsou & Kochi 1979 も同様。
* **Filling adequacy confidence**: High — Kochi の studies は Kumada 1972 が記述する exact 反応系（Ni-phosphine + Grignard + ArCl）を対象としており、EP-03a の case-specific 実装（³¹P NMR / EPR / radical probe）の本質を満たす。
* **Verification recommendation**: 必須 — トリガー (a) 1980年以前 + (c) author name に由来する命名規則（Kumada coupling）の二要因該当。
* **DOI / URL（任意）**: Tsou & Kochi 1979: DOI 10.1021/ja00519a015 候補（要 Crossref 確認）; Morrell & Kochi 1975: DOI 10.1021/ja00858a019 候補（要 Crossref 確認）
* **Filling timescale category**: incentive-aligned (3-7 yr) — Kumada 1972 から 1975 (Morrell-Kochi) までの 3 年は Ni-Grignard 機構の競合的応答として典型的範囲。
* **注記**: Self-Tier I（standard "Kumada mechanism" cue → Kochi group が直接想起）。推論経路: "Ni-Grignard cross-coupling mechanism" → "Kochi の radical-chain studies" → Morrell-Kochi 1975 と Tsou-Kochi 1979 の二論文がペアで想起される。DB-findable: yes（"Kochi nickel oxidative addition" で容易に検索可能）。Bibliographic confidence は High だが Verification 必須は author-name reaction 規則による。Stage 3 §6 (vii) で予測された "RI-03 + RI-06 + PRI-11 共起" の三項解消には、Morrell-Kochi 1975 が radical clock + ESR でアプローチし、PRI-11（速度式の代数的導出）を kinetic 部分で前進。

---

**EP-10a [Kinetic verification pack]（暫定）（第二群）**

* **充填するRI**: PRI-11 [Mechanism-kinetics decoupling]（SRG-2）
* **充填開始点**: Tsou, T. T. & Kochi, J. K., *J. Am. Chem. Soc.* **1979**, *101*, 6319 — "Reactivity and Mechanism of Aromatic Coupling of Nickel(I)" — Ni(I)/Ni(III) サイクルの初期速度次数を [Ni], [ArX], [RM] について系統的に決定し、radical-chain 速度式を導出。
* **充填確立点**: Smith, G. & Kochi, J. K., *J. Organomet. Chem.* **1980**, *198*, 199 — [REDACTED: substantial verbatim quotation; see Tier 9] — Kumada-type 反応の初期速度を NiCl₂(PPh₃)₂ 系で測定し、Eyring パラメータと律速段階を同定。
* **充填の性質**: Partial — Smith-Kochi 1980 は NiCl₂(PPh₃)₂（Tamao 1972 の Table I 中の [NiCl₂(PPh₃)₂] エントリに直接対応）で kinetic 測定を行うが、[NiCl₂(dpe)] 系の対応する kinetics は scattered で完全充填には至らない。
* **Bibliographic confidence**: Medium — Smith & Kochi 1980 の正確な巻号は記憶推定（J. Organomet. Chem. 1980 era）。Tsou-Kochi 1979 のもう一つの paper も同年複数 issue に分散。
* **Filling adequacy confidence**: Medium — Smith-Kochi 1980 は phosphine 配位子が PPh₃ であり dpe ではないため、Tamao 1972 の代表触媒に対する直接充填ではなく類似系充填（Indirect 要素を含む Partial）。
* **Verification recommendation**: 必須 — トリガー (a) 1980年以前 + (c) Kumada 命名規則 + (d) Bibliographic confidence Medium 候補が含まれる。
* **DOI / URL（任意）**: 推定 — Smith & Kochi 1980 の DOI は要 Crossref 確認。
* **Filling timescale category**: incentive-aligned (7-8 yr) — Kumada 1972 から Smith-Kochi 1980 までの 8 年は kinetic verification の標準的応答時間。
* **注記**: Self-Tier III（複数 Kochi group papers の triangulation が必要）。推論経路: "Kumada coupling kinetic studies" → "1970s late Ni mechanism papers" → [REDACTED: substantial verbatim quotation; see Tier 9] → 速度次数研究は Smith-Kochi 1980 に集約と triangulation で表面化。DB-findable: uncertain（Smith & Kochi の正確な書誌の同定に検索を要する）。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator] / RI-01 [Reporting integrity]（SRG-3）
* **充填開始点**: Tamao, K., Sumitani, K., Kiso, Y., Zembayashi, M., Fujioka, A., Kodama, S., Nakajima, I., Minato, A., Kumada, M., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — [REDACTED: substantial verbatim quotation; see Tier 9] — Communication → Full Paper auto-resolution。1,2-dichloroethylene 系での cis:trans 比測定を再記録、ただし機構解釈は依然 deferred。
* **充填確立点**: Smith, R. S. & Kochi, J. K., *J. Org. Chem.* **1976**, *41*, 502 — radical-mediated stereochemical scrambling の機構研究で 1,2-dihaloalkene + Ni 系の vinyl radical pathway を実験的に分離（TEMPO trap, time-course）。または、Asscher & Vofsi 系の vinyl coupling stereochemistry 研究。
* **充填の性質**: Partial — Tamao-Kumada Full Paper 1976 は cis:trans 比の measurement method（GLPC condition）を開示するが exhaustive exclusion matrix（radical / σ-vinyl-Ni rotation / post-coupling isomerization）は完成しない。Kochi 系列は radical pathway を支持するが、原論文系での直接適用は限定的。
* **Bibliographic confidence**: High（Tamao-Kumada Full Paper 1976）/ Medium（Smith-Kochi 1976 の正確な書誌）
* **Filling adequacy confidence**: Medium — Full Paper の cis:trans 再測定は EP-04a の measurement method 開示要件を満たすが、機構分離は Partial。
* **Verification recommendation**: 必須 — (a) 1980年以前 + (b) Kumada group authors（同一研究グループから 10+ の関連論文）+ (c) Kumada 命名規則。
* **DOI / URL（任意）**: Tamao-Kumada BCSJ 1976: DOI 10.1246/bcsj.49.1958 候補（要 Crossref 確認、Bull. Chem. Soc. Jpn. の DOI 形式）
* **Filling timescale category**: format-driven (4 yr) — Letter → Full Paper auto-resolution として典型。
* **auto_resolution_type**: "Letter→Full Paper"
* **expected_resolution_window**: "1-3 yr"（実際は 4 yr で若干遅延）
* **auto_resolution_status**: "occurred"
* **注記**: Self-Tier II（Full Paper の存在は標準的想起だが、cis:trans 機構分離の充填を triangulate するために Kochi 系列との照合が必要）。推論経路: "Kumada Full Paper 自己充填" → 1976 BCSJ の Tamao-Kumada series → cis:trans 再測定の有無を確認 → 機構分離は Kochi 系列を別途 triangulate。DB-findable: yes（"Tamao Kumada 1976 Bull Chem Soc Jpn" で確実）。

---

**EP-01a [Reporting-coherence pack]（第一群）**

* **充填するRI**: RI-01 [Reporting integrity]（SRG-6, SRG-10）
* **充填開始点**: Tamao, K., Sumitani, K., Kiso, Y., Zembayashi, M., Fujioka, A., Kodama, S., Nakajima, I., Minato, A., Kumada, M., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Full Paper 形式で per-entry 条件（mol%, T, t, scale, Grignard:RX 比, 溶媒）を 10+ エントリで開示。Communication の "and/or" footnote と "condition A/B" 参照を解消。
* **充填確立点**: 同上（自己充填の単一論文で完了）
* **充填の性質**: Complete — Communication 形式起因の reporting omission（B-08, B-09, B-11, B-15, B-16）は Full Paper の SI / Experimental section で per-entry 完全開示に到達。SRG-6 / SRG-10 の主要 RI-01 を解消。
* **Bibliographic confidence**: High — Tamao 1976 BCSJ Full Paper は Kumada coupling の標準引用。
* **Filling adequacy confidence**: High — Full Paper の per-entry 開示は EP-01a の case-specific 実装を直接満たす。
* **Verification recommendation**: 必須 — (a) 1980年以前 + (b) Kumada group + (c) author-name reaction。
* **DOI / URL（任意）**: 10.1246/bcsj.49.1958 候補（要確認）
* **Filling timescale category**: format-driven (4 yr)
* **auto_resolution_type**: "Letter→Full Paper"
* **expected_resolution_window**: "1-3 yr"
* **auto_resolution_status**: "occurred"
* **注記**: Self-Tier I（Communication → Full Paper の標準的想起。"Kumada 1972 Full Paper" という cue が Tamao-BCSJ-1976 を直接呼び出す）。推論経路: 即時想起。DB-findable: yes。Stage 3 §6 (vi) "通信 → Full Paper 自動解消パターン" の典型例として登録される。

---

**EP-02a [Identity / purity substantiation pack]（第一群）**

* **充填するRI**: RI-02 [Object identification] / RI-01 [Reporting integrity]（SRG-6）
* **充填開始点**: Tamao, K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Full Paper で各新規化合物の燃焼 EA + ¹H NMR + IR の per-entry 開示。
* **充填確立点**: 同上
* **充填の性質**: Complete (era-norm 1976) / Partial (modern HR-MS standard) — 1976 era の standard としては EA + spectroscopic confirmation で十分だが、modern では HR-MS / single-crystal X-ray まで要求される場合があり、その意味では Partial。
* **Bibliographic confidence**: High
* **Filling adequacy confidence**: High（era-norm）/ Medium（modern）
* **Verification recommendation**: 必須 — EP-01a と同根拠
* **Filling timescale category**: format-driven (4 yr)
* **注記**: Self-Tier I（EP-01a と同論文での bundle 充填、即時想起）。EP-01a, EP-02a, EP-04a の 3 EP が Tamao-Kumada Full Paper 1976 一報で bundle 充填される効率性は §C 推奨選定リストで明記。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]（SRG-1）
* **充填開始点**: **未同定** — Kumada 1972 Table I の各エントリの n=3 反復測定 + SD 報告という形式での独立論文は文献上見当たらない。
* **充填確立点**: 該当なし
* **充填の性質**: 該当なし（インセンティブ構造的未充填）
* **Bibliographic confidence**: 該当なし
* **Filling adequacy confidence**: 該当なし
* **Verification recommendation**: 省略可（未充填判定であり書誌検証対象外）
* **DOI / URL（任意）**: 該当なし
* **Filling timescale category**: non-applicable
* **incentive_structure_type**: "incentive-mismatch" (v18 C6 該当 — 既存系の追試・反復測定は新規性を要求する出版慣行の下で論文化されにくい)
* **注記**: Self-Tier III（候補同定そのものが「未充填の判定」に triangulate）。推論経路: "Kumada 1972 各エントリの n=3 SD report" → 該当する独立論文は想起できない → これはインセンティブ構造的未充填パターン（v18 C6）と判定。DB-findable: no（そもそも存在しない）。Stage 3 §6 で示唆された "通信 → Full Paper 自動解消" パターンでも EP-08a は解消されず、Tamao-Kumada Full Paper 1976 でも n=1 のままと予想される（要 Verification）。後続 Kumada coupling 機構研究（Kochi 系列）の副次データとして部分的に mass-balance / replication の証拠が散在するが、Table I の各エントリ specific な複製は未充填。§E で詳述。

---

**EP-09a [Internal benchmark pack]（第一群、CLA-1経由）**

* **充填するRI**: RI-09 [External superiority]（CLA-1, SRG-7, SRG-9）
* **充填開始点**: Corriu, R. J. P. & Masse, J. P., *J. Chem. Soc., Chem. Commun.* **1972**, 144 — [REDACTED: substantial verbatim quotation; see Tier 9] — Ni(acac)₂ + PPh₃ + Grignard + ArX 系で Tamao 1972 と同変換を実現。Tamao 1972 の "Note Added in Proof" で参照される。
* **充填確立点**: Tamao, K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 — Full Paper で Ni(acac)₂ + dpe を含む各種 Ni 前駆体 + 配位子組合せの体系的比較を含む（要確認）。Ni(acac)₂ vs [NiCl₂(dpe)] の直接比較収率を提示。
* **充填の性質**: Partial — Corriu-Masse 1972 は同変換の達成を示すが、Tamao 1972 との head-to-head matched 収率比較は両論文間では未実施。Tamao-Kumada Full Paper 1976 が部分的に体系比較を含むと予想されるが exhaustive ではない。
* **Bibliographic confidence**: High — Corriu-Masse 1972 は Tamao 1972 の Note Added in Proof で明示参照。Tamao 1976 BCSJ も標準引用。
* **Filling adequacy confidence**: Medium — CLA-1 の核心（"phosphine が必要か影響するか"）の operational 分離は両論文で完全には行われない。
* **Verification recommendation**: 必須 — (a) 1980年以前 + (c) Kumada / Corriu-Masse の named contribution に近い。
* **DOI / URL（任意）**: Corriu-Masse 1972: DOI 10.1039/C39720000144 候補（要 Crossref 確認、Chem. Commun. の 1972 年 DOI 形式）
* **Filling timescale category**: format-driven (0 yr — concurrent submission) + field-methodology (4 yr — Tamao Full Paper 1976 の体系比較)
* **注記**: Self-Tier I（"Note Added in Proof" cue により Corriu-Masse は即時想起。DB findability も最高水準）。推論経路: 論文テキストが直接参照 → Corriu-Masse 1972。DB-findable: yes。Cl/Br/I 比較（SRG-9）の充填は別軸で、Hartwig 系列の oxidative addition kinetics 研究（1990s-2000s）が体系充填するが、Kumada 1972 specific な benchmark とは時間差が大きい。

---

**EP-07a [Boundary-test pack]（第一群、ただし長期遅延充填）**

* **充填するRI**: RI-07 [Unsupported boundary]（SRG-9）
* **充填開始点**: Yamamura, M., Moritani, I., Murahashi, S., *J. Organomet. Chem.* **1975**, *91*, C39 — [REDACTED: substantial verbatim quotation; see Tier 9] — sp³ Grignard 拡張の初期試行。
* **充填確立点**: Devasagayaraj, A., Stüdemann, T., Knochel, P., *Angew. Chem. Int. Ed. Engl.* **1995**, *34*, 2723 — "A New Nickel-Catalyzed Cross-Coupling Reaction between sp³ Carbon Centers" — alkyl-alkyl Kumada/Negishi 類型の境界突破。Kumada 1972 が排除した C_sp³ 基質の充填を体系的に実現。
* **充填確立点（補足）**: Fischer, C. & Fu, G. C., *J. Am. Chem. Soc.* **2003**, *125*, 4978 — Ni/pybox 系 alkyl-alkyl Negishi。Kambe, N. et al., *J. Am. Chem. Soc.* **2002**, *124*, 4222 — alkyl Grignard cross-coupling。
* **充填の性質**: Paradigm-shift — Tamao 1972 の "Only C_sp² halides can be used" 排除主張は Devasagayaraj 1995 と Fischer-Fu 2003 によって反転。元の RI-07 排除主張の前提（β-H 不安定性が sp³ で致命的）が新配位子設計（pybox, NHC）と新機構（Ni(I)/Ni(III) radical chain で β-H 抑制）で克服。
* **Bibliographic confidence**: High（全候補とも標準的引用論文）
* **Filling adequacy confidence**: High — 境界主張の反転として直接充填。
* **Verification recommendation**: 推奨 — (c) Kumada 命名規則に部分的関連、(d) 該当なし。1995/2003 と比較的新しい。
* **DOI / URL（任意）**: Devasagayaraj-Knochel 1995: 10.1002/anie.199527231 候補; Fischer & Fu 2003: 10.1021/ja0345221 候補（要確認）
* **Filling timescale category**: technical-barrier (23-31 yr) — sp³ 基質排除の克服には新配位子設計と機構理解の蓄積を要した長期遅延充填。
* **注記**: Self-Tier II（"sp³ Kumada 拡張" → "Knochel" → "Fu" の 3 段階連想）。推論経路: 1972 排除 → 1995 Knochel breakthrough → 2003 Fu/2002 Kambe で field maturation。DB-findable: yes。長期遅延充填（23+ 年）は Stage 3 §6 (iii) の VQ 階層逆転示唆（field のインセンティブ構造）の典型例。

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-05 [Qualitative overread]（SRG-4）
* **充填開始点**: Hayashi, T., Konishi, M., Fukushima, M., Mise, T., Kagotani, M., Tajika, M., Kumada, M., *J. Am. Chem. Soc.* **1982**, *104*, 180 — [REDACTED: substantial verbatim quotation; see Tier 9] — 配位子 bite angle / 立体 / 電子効果と活性の定量関係を chiral phosphine 系で系統的に確立。
* **充填確立点**: Hayashi, T., Konishi, M., Kobori, Y., Kumada, M., Higuchi, T., Hirotsu, K., *J. Am. Chem. Soc.* **1984**, *106*, 158 — [REDACTED: substantial verbatim quotation; see Tier 9] — 配位子 bite angle と TON / TOF の定量対応。
* **充填の性質**: Partial → Indirect — Hayashi 系列は chiral phosphine 配位子 ranking を定量的に確立するが、原論文の dpp/dpe/dmpe/(PPh₃)₂/(PEt₃)₂/(PPh₂Me)₂ 6 配位子の matrix 直接充填ではなく、bite angle 効果のメタ充填。
* **Bibliographic confidence**: High（Hayashi-Kumada series 1982-1984 は標準引用）
* **Filling adequacy confidence**: Medium — chiral phosphine 系での定量化が原論文の 6 配位子比較と完全には一致しない（asymmetric induction が主目的）。
* **Verification recommendation**: 推奨 — (b) Kumada/Hayashi group 同一研究グループから 10+ の関連論文があるが、(a) 1980年代で borderline。
* **DOI / URL（任意）**: Hayashi 1982: 10.1021/ja00365a032 候補; Hayashi 1984: 10.1021/ja00313a032 候補（要確認）
* **Filling timescale category**: field-methodology (10-12 yr) — chiral phosphine ligand design field の成熟が driving force。
* **注記**: Self-Tier I（"Kumada 配位子 ranking" → Hayashi-Kumada chiral phosphine series が標準想起）。推論経路: 即時想起。DB-findable: yes。dppf 系（Hayashi-Konishi-Kumada 1984）が代表的な bite angle 効果定量化として field に定着。

---

**EP-06a [Analogy-validation pack]（第二群）**

* **充填するRI**: RI-06 [Imported model] / RI-03 [Unobserved explanatory]（SRG-8）
* **充填開始点**: Kochi, J. K., *Acc. Chem. Res.* **1974**, *7*, 351 — "Mechanisms of Organic Oxidation-Reduction Reactions Promoted by Metal Halides" — β-H 寛容性の機構的論拠を radical pathway で説明する代替フレーム。
* **充填確立点**: Hartwig group の Pd-catalyzed cross-coupling での β-H 抑制研究（1990s-2000s）が β-H 機構の包括的理解として確立。Kumada specific な β-D 標識実験は Yamamoto 系列に scattered。
* **充填の性質**: Indirect — β-H elimination vs reductive elimination の競合は Pd 系で systematic に研究されたが、Ni-Grignard 系での k_RE/k_{β-H} 直接測定は限定的。
* **Bibliographic confidence**: Medium — Kochi 1974 review は確実だが、Kumada specific な β-H 機構充填論文の特定は推定を含む。
* **Filling adequacy confidence**: Low-Medium — case-specific 実装（β-D 標識 Grignard, 1-hexene crossover）の具体的実施報告の同定は曖昧。
* **Verification recommendation**: 必須 — (d) Bibliographic confidence Medium-Low の候補が含まれる + (a) 1980年以前部分。
* **DOI / URL（任意）**: 推定 — 要 Crossref 検証。
* **Filling timescale category**: field-methodology (10-20 yr) — β-H 抑制機構の field-wide 理解は 1990s 以降に成熟。
* **注記**: Self-Tier III（複数 review + 個別 paper の triangulation）。推論経路: "β-H tolerance Kumada mechanism" → "Kochi review" → 個別の β-D 標識実験は同定困難 → Hartwig Pd 系の包括的理解で代替。DB-findable: uncertain（specific 充填論文の同定は困難）。

---

**§B 末尾チェック：Bibliographic verification（v18.3 conditional triggering）**

**トリガー条件評価:**
- (a) 論文年代が古い: 8報中 6報が 1980 年以前 → **該当**
- (b) 著者ネットワークが密: Kumada group (Tamao, Sumitani, Hayashi, Kiso, Zembayashi, Fujioka, Kodama 等) 同一研究グループから 20+ の関連論文 → **該当**
- (c) Author-name reaction 規則: **Kumada coupling** が代表的 named reaction → **該当**
- (d) Bibliographic confidence Medium-Low が 2件以上: EP-10a (Smith-Kochi 1980), EP-06a (Kochi specific paper) → **該当**

**Verification recommendation 全候補に [必須]** （4要因全該当）

**Bibliographic verification status: pending（全候補）**

**Hallucination 警告候補（事前 self-audit）:**
- ✓ "Tamao-Sumitani-Kiso-Zembayashi-Fujioka-Kodama-Nakajima-Minato-Kumada 1976 Bull. Chem. Soc. Jpn. 49, 1958" — 著者リストの完全一致は memory のみで verification 必須。Yoshioka memory には "Tamao-Sumitani-Hayashi-Kumada" は実在せず "Tamao-Sumitani-Kiso-Kumada" が実在 と記録されている。本リストは Full Paper の長い著者リストを記憶呼び出し → 9 名だが順序とスペルの完全 verification 必要。
- ✓ [REDACTED: substantial verbatim quotation; see Tier 9] — 同一年複数 issue の triangulation を経たが、巻号ページの正確性は要 verification（記憶では 1979 に Tsou-Kochi の paper が複数あるが、6319 と 7547 のいずれが正確か uncertain）。
- ✓ "Smith & Kochi 1980 J. Organomet. Chem. 198, 199" — Bibliographic confidence Medium。Smith のスペル（Smith vs Smitt vs Smyth）と巻号要 verification。
- ✓ "Devasagayaraj-Studemann-Knochel 1995 Angew. Chem. Int. Ed. 34, 2723" — Knochel 系列の 1995 paper は確実だが、共著者 "Studemann" のスペル（Stüdemann, Stuedemann）と巻号要 verification。
- ✓ [REDACTED: substantial verbatim quotation; see Tier 9] — Fu group の 2003 paper は確実だが、共著者の正確な名前と巻号要 verification。

**post-hoc verification の推奨手順**: Crossref API で全 8 候補の DOI 検証 → 著者リスト完全一致 → タイトル / 内容で EP との対応を再評価。

---

## §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Corriu, R. J. P. & Masse, J. P., *J. Chem. Soc., Chem. Commun.* **1972**, 144 | EP-09a (CLA-1) | VQ-2 | 1972 | High | Medium | ⚠️ pending verification（必須）|
| 2 | Tamao, K. et al., *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958 | EP-01a, EP-02a, EP-04a, EP-09a (補強) | VQ-2 | 1976 | High | High | ⚠️ pending verification（必須）|
| 3 | Morrell, D. G. & Kochi, J. K., *J. Am. Chem. Soc.* **1975**, *97*, 7262 | EP-03a | VQ-3 | 1975 | High | High | ⚠️ pending verification（必須）|
| 4 | Tsou, T. T. & Kochi, J. K., *J. Am. Chem. Soc.* **1979**, *101*, 6319 (and/or 7547) | EP-03a, EP-10a | VQ-3 | 1979 | High | High | ⚠️ pending verification（必須）|
| 5 | Hayashi, T., Konishi, M., Kobori, Y., Kumada, M., Higuchi, T., Hirotsu, K., *J. Am. Chem. Soc.* **1984**, *106*, 158 | EP-05a | VQ-3 | 1984 | High | Medium | ⚠️ pending verification（必須）|
| 6 | Devasagayaraj, A., Stüdemann, T., Knochel, P., *Angew. Chem. Int. Ed. Engl.* **1995**, *34*, 2723 | EP-07a | VQ-2/VQ-3 | 1995 | High | High | ⚠️ pending verification（推奨）|
| 7 | Fischer, C. & Fu, G. C., *J. Am. Chem. Soc.* **2003**, *125*, 4978 | EP-07a (確立) | VQ-3 | 2003 | High | High | ⚠️ pending verification（推奨）|

**選定理由（v18.3 改訂）:**

(1) **Bundle 充填の効率性**: Tamao-Kumada Full Paper 1976 が EP-01a, EP-02a, EP-04a, EP-09a の 4 EP を bundle 充填する。これは Communication → Full Paper auto-resolution（C23）の典型例として記録される。1 論文で SRG-6 (RI-01) 全体、SRG-10 (RI-01 内部矛盾型), SRG-3 (RI-04) 部分、CLA-1 (RI-09) 部分を解消する。

(2) **VQ 階層の階段状カバレッジ**: VQ-2 要件（reporting integrity）は #2 (Tamao 1976) で確実充填、VQ-3 要件（mechanism）は #3 + #4 (Kochi series 1975, 1979) で paradigm-shift 充填、VQ-3-VQ-4 補強は #5 (Hayashi-Kumada 1984) で配位子定量化、境界主張（VQ-2 拡張）は #6 + #7 (Knochel 1995, Fu 2003) で 23-31 年遅延充填。

(3) **年代の多様性**: 1972 (concurrent) → 1975 → 1976 → 1979 → 1984 → 1995 → 2003 の 31 年スパンで充填の時間展開を検証可能。format-driven (1976), incentive-aligned (1975-1984), technical-barrier (1995-2003) の 3 timescale category が観測される。

(4) **Bibliographic verification 待機**: 全 7 候補が「⚠️ pending verification」として post-hoc 検証を要する。これは Kumada 命名規則 + 1980 年以前論文 + 著者ネットワーク密度 + Bib.Conf Medium 候補含有の 4 トリガー全該当による。Sonnet kumada（67% hallucination）と Murai（0% 全 / 14% 部分 hallucination）の cross-model meta（improvements/cross_model_kumada_vs_murai_meta.md）を踏まえ、Opus 4.7 でも paper-dependent な hallucination リスクが存在しうる。

(5) **未充填 EP-08a の戦略的位置付け**: Replication / uncertainty pack は推奨選定リストから除外。これは技術的不能ではなくインセンティブ構造的未充填（v18 C6）であり、§E で発見的意義を記録する。

---

## §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

- **VQ-2 要件 (CLA-1, RI-09)**: EP-09a (CLA-1) → 1972 [Corriu-Masse] [concurrent submission, format-driven 0 yr]
- **VQ-3 要件 (mechanism, RI-03/RI-06)**: EP-03a → 1975 [Morrell-Kochi] [incentive-aligned 3 yr, paradigm-shift]
- **VQ-2 要件 (reporting, RI-01/RI-02)**: EP-01a + EP-02a + EP-04a → 1976 [Tamao-Kumada Full Paper] [format-driven 4 yr, bundle 充填]
- **VQ-3 要件 (kinetics, PRI-11)**: EP-10a + EP-03a 補強 → 1979 [Tsou-Kochi] [incentive-aligned 7 yr]
- **VQ-3 要件 (ligand quant., RI-05)**: EP-05a → 1984 [Hayashi-Kumada] [field-methodology 12 yr]
- **VQ-2 要件 (boundary, RI-07)**: EP-07a 開始 → 1995 [Devasagayaraj-Knochel] [technical-barrier 23 yr, paradigm-shift]
- **VQ-3 要件 (boundary 機構基盤)**: EP-07a 確立 → 2003 [Fischer-Fu] [technical-barrier 31 yr]
- **VQ-3 要件 (β-H mechanism, RI-06)**: EP-06a → ~1990s-2000s [Hartwig 系列, Indirect] [field-methodology 20+ yr]
- **未充填 (RI-08)**: EP-08a → 該当なし [インセンティブ構造的未充填]

**階層-時間対応の評価:**

仮説「VQ階層が上がるほど充填に要する時間が長くなる」は本ケースで部分的に支持される。VQ-2 要件は 0-4 年で format-driven に充填されたのに対し、VQ-3 要件は 3-31 年の幅広い分布を示す。ただし VQ-3 要件のうち mechanism (1975) は早期、kinetic (1979) は中期、boundary (2003) は超長期と内部分散が大きく、VQ 水準のみでは充填時間を予測できない。むしろ「impact-bearing observation の有無」（cis-stilbene 異常 → Kochi 即応; sp³ 排除 → 数十年遅延）が時間スケールを支配する。

**特筆すべきパターン:**

- **長期遅延充填（technical-barrier）**: EP-07a (sp³ 境界排除) は Tamao 1972 の "Only C_sp² halides can be used" 主張が 23-31 年後に Knochel/Fu によって反転される典型例。Stage 3 §6 (iii) の VQ 階層逆転（出版インセンティブによる）の補強事例。
- **Bundle 充填**: Tamao-Kumada Full Paper 1976 が 4 EP（EP-01a, EP-02a, EP-04a, EP-09a 補強）を一括充填。format-driven auto-resolution の効率性の典型。
- **Paradigm-shift 充填**: EP-03a は中間体 1, 2, 3 の Ni(II)/Ni(IV) 同定要件として提示されたが、Kochi の Ni(I)/Ni(III) radical-chain 機構の受容により問いの枠組み自体が再定義された。
- **自己充填 vs 他者充填**: EP-01a, EP-02a, EP-04a (部分), EP-05a, EP-09a (部分) は Kumada group 自身が後続論文で充填。EP-03a, EP-07a, EP-10a は Kochi/Knochel/Fu 等の他研究グループによる充填。
- **インセンティブ構造的未充填**: EP-08a (replication) は 54 年経過後も独立論文として充填されておらず、§E で詳述。

**著者回顧との照合:**

Kumada group の retrospective 論文（Tamao 1989 mini-review, Kumada Tetrahedron 報告 1982 等）では、Communication 1972 の 5 features （β-H 寛容性、C_sp²-Cl 反応性、bidentate ligand 優位性、cis-stilbene 経路、Et₂O 溶媒優位性）は明示的に列挙される一方、(a) Ni(II)/Ni(IV) サイクル仮定の妥当性、(b) eq 1 と提案サイクルの選択性矛盾（U-01）、(c) U-04 の自己予測 R-R 副生成物、(d) "black mixture[REDACTED: substantial verbatim quotation; see Tier 9]field の内部者には不可視の構造的不在" の直接的証拠として記録できる。

---

## §E 未充填EPの発見的意義

**未充填EP一覧:**

**EP-08a [Replication / uncertainty pack]:**

* **未充填の理由**: **インセンティブ構造の不整合**（v18 C6）— Tamao 1972 Table I の各エントリ（EtMgBr/PhCl, n-BuMgBr/PhCl, n-BuMgBr/m-Cl₂C₆H₄ 等 11 エントリ）の n=3 反復測定 + 標準偏差 + GLPC 検出下限の独立論文化は、合成有機化学の出版慣行において新規性を欠くため論文化インセンティブが存在しない。技術的には 1972 年でも実施可能であり、現代では trivial。Tamao-Kumada Full Paper 1976 でも複製数の体系的開示は予想されない（要 verification）。後続の機構研究（Kochi 系列, Smith-Kochi 1980 等）の副次データとして部分的 mass-balance / replication 情報が散在するが、Communication の Table I を直接の検証対象とするものは現在まで未同定。
* **発見的意義**: **あり** — Kumada coupling 起源論文の 11 エントリの定量的信頼性（SD, 検出下限, mass balance）は **54 年にわたって体系的に充填されていない**。この未充填は (1) 合成化学分野の出版慣行が「新規変換の demonstration」と「既存変換の定量的再現」を構造的に非対称扱いする結果、(2) 引用ネットワークが原 Communication 1972 を「priority claim」として参照し続け、その下位の定量的信頼性は現代的 EP として再認識されない、(3) Stage 3 §6 (iii) で示唆された VQ 階層逆転（出版インセンティブが実際の充填順序を低 VQ → 高 VQ に逆転させる）の典型例となる。UQS 1.0 が抽出する「分野が体系的に避けてきた問い」のフラッグシップ例として記録できる。
* **将来の充填可能性**: **中** — 技術的には trivial だが、論文化のインセンティブが確保されない限り独立充填は進まない。可能なシナリオ: (a) 触媒 reproducibility 危機を契機とした field-wide audit の一部として、(b) ML/AI による反応収率予測モデルの training data として、(c) UQS や類似メソドロジーが提示する EP-as-target framework の下での意図的充填プロジェクトとして。

---

**EP-06a [Analogy-validation pack]:**

* **未充填の理由**: **分野慣行 + 関心の方向性** — β-H 寛容性の k_RE/k_{β-H} 直接測定（β-D 標識 Grignard + 1-hexene crossover + Eyring パラメータ）は Kumada 1972 specific な実装としては未充填。Pd 系での包括的研究（Hartwig 系列）が代替するが、Ni-Grignard 系での直接充填ではない。
* **発見的意義**: **あり** — Tamao 1972 の feature (1) 「β-H を持つ Grignard が高収率で働く」という claim は 54 年経過後も case-specific に直接検証されておらず、機構的「常識」として field に定着している。これは Stage 3 §6 (i) で予測された "RI-03 サブタイプ Recorded-but-uninterrogated observation" の典型。
* **将来の充填可能性**: **高** — 現代の DFT 計算 + in situ NMR + 同位体標識実験で容易に実施可能。実施インセンティブは asymmetric / enantioselective Kumada coupling の β-H 制御という応用文脈で確保される可能性。

---

**EP-04a [Discrimination / replication pack] - 部分未充填:**

* **未充填の理由**: **報告形式問題（Letter→Full 部分解消）+ 関心の欠如** — 1,2-dichloroethylene の cis:trans 異性比（80:20 vs 43:57）の機構診断（radical / σ-vinyl-Ni rotation / post-coupling isomerization の三経路分離）は Tamao-Kumada Full Paper 1976 でも完全には充填されないと予想される。Kochi 系列の radical pathway support は indirect。
* **発見的意義**: **あり** — Stage 2 D4-2 「cis:trans 異性比は何の機構的証拠か」の問いは、論文自体が "rather nonstereospecifically" と記述しつつ "may offer a facile route to cis-stilbene" と合成的有用性に回収して閉じた構造そのものが、後続文献でも同様に維持される。機構診断の機会が「有用性」の修辞で閉じられる pattern は field-wide。
* **将来の充填可能性**: **中** — 現代の time-resolved spectroscopy + DFT で実施可能だが、原論文系の specific な検証インセンティブは限定的。

---

**未充填 EP の VQ 階層分布分析:**

未充填 EP は EP-08a (RI-08), EP-06a (RI-06/RI-03 一部), EP-04a 機構部分 (RI-04 一部) に集中する。**RI-08 (低 VQ 要件) が最も重度に未充填**であり、**RI-03 / RI-06 (高 VQ 要件) は paradigm-shift 充填されている** という対称性は、Stage 3 §6 (iii) で予測された "科学的論理に基づく EP 充填順序（低 VQ → 高 VQ）" と "出版インセンティブに基づく実際の充填順序（高 VQ → 低 VQ）" の逆転の直接的証拠となる。すなわち、機構主張のような impact-bearing claim は早期に検証されるが、定量的信頼性のような foundation-building claim は構造的に未充填のまま残る。

---

## 付録: 考慮し棄却した候補（externalized rejection log）

以下は本 retrieval プロセスで一度想起されたが充填候補として棄却した論文。棄却理由を明記する。

**1. Kharasch, M. S. & Reinmuth, O., "Grignard Reactions of Nonmetallic Substances", 1954**
   - 想起契機: Tamao 1972 の ref 4 として明示参照される transition-metal-halide-induced Grignard coupling の compendium。
   - 棄却理由: **Compendium reference で独立実験的充填を提供しない**。Stage 3 §2 の C-06 で "no specific experimental engagement" として既に記録。

**2. Wilke, G. group の Ni(0) 化学全般（Wilke 1966 review, Aldrichimica Acta 1976 等）**
   - 想起契機: Ni(0)-phosphine の oxidative addition は Wilke の中心テーマ。
   - 棄却理由: **Wilke は Ni(0) 化学の一般論を提供するが、Kumada 1972 specific な触媒サイクル検証ではない**。EP-03a の case-specific 実装（NiCl₂(dpe) 系）に直接対応しない。

**3. Negishi, E. & Baba, S., *J. Chem. Soc., Chem. Commun.* 1976, 596（または King, A. O., Okukado, N., Negishi, E. 1977）**
   - 想起契機: Ni-catalyzed cross-coupling の系列発展（Negishi coupling）。
   - 棄却理由: **Negishi coupling は Zn-organic を nucleophile とする独立系の発展**であり、Kumada 1972 (Grignard) の EP を直接充填しない。Negishi 系は Stille, Suzuki, Sonogashira と並ぶ並行 lineage であり、Kumada の境界拡張ではあるが充填ではない。Stage 3 §1 の Layered structure 議論で「同じ field の競合 lineage」として位置付けられる。

**4. Stille, J. K., *J. Am. Chem. Soc.* 1978, 100, 3636（Milstein-Stille acyl chloride coupling）**
   - 想起契機: Sn-organic を nucleophile とする Stille coupling の起源。
   - 棄却理由: **Negishi と同様に並行 lineage であり充填ではない**。

**5. Hayashi-Tamao-Konishi-Mise-Kumada *Tetrahedron Lett.* **1979** (asymmetric initial)**
   - 想起契機: asymmetric Kumada の最初期論文。
   - 棄却理由: **Hayashi 1982 / 1984 series に体系充填が集約される**ため、初期 letter は #5 (Hayashi 1984) に統合し独立 entry を立てない。

**6. Kambe, N., Iwasaki, T., Terao, J. *J. Am. Chem. Soc.* 2002 系列**
   - 想起契機: Ni-catalyzed alkyl-alkyl Kumada coupling.
   - 棄却理由: **Devasagayaraj 1995 と Fischer-Fu 2003 の間に位置する移行期 paper であり、§B EP-07a で "確立" 候補として既に言及済み**。独立 entry を立てるほど決定的ではない。

**7. Yamamoto, A. group の (PEt₃)₂NiR₂ / NiR(X)(PR₃)₂ 単離・構造解析論文（1970-1980s）**
   - 想起契機: Ni-organic 中間体の isolation / X-ray 構造解析を Yamamoto group が体系的に実施。
   - 棄却理由: **NiCl₂(dpe) 系 specific な中間体ではなく、generic な Ni-phosphine 化学の貢献**。EP-03a の case-specific 実装の "NiCl₂(dpe) + n-BuMgBr の -78 ℃ ³¹P NMR" には直接対応しない（類似系での充填となり Indirect）。

**8. Amatore, C. & Jutand, A., *Acc. Chem. Res.* 2000, 33, 314 等の Pd cross-coupling kinetic 系列**
   - 想起契機: cross-coupling kinetics の包括的研究。
   - 棄却理由: **Pd 系の研究であり Ni-Grignard 系ではない**。Indirect 充填にとどまる。

**9. Diao, T. group / Vicic, D. A. group の Ni(I)/Ni(III) 単離論文（2010s）**
   - 想起契機: Ni(I)/Ni(III) intermediate の現代的単離・構造解析。
   - 棄却理由: **EP-03a の case-specific 実装（NiCl₂(dpe) + Grignard）を直接対象としない**。Kochi の paradigm-shift 充填（Morrell 1975, Tsou 1979）の延長線上だが、Tamao 1972 specific な intermediate 検証ではない。

**10. Murahashi, S. group の Pd-vinyl coupling 1975 series**
   - 想起契機: 1975 era の Pd vinyl halide + Grignard 系。
   - 棄却理由: **Pd 系であり Ni-Grignard 系の直接充填ではない**。Yamamura, Moritani, Murahashi 1975 (Fe/Co/Ni) は §B EP-07a の充填開始点として採択済み。

---

**Externalization meta-comment（v6 retrieval depth measurement primary data）:**

本 retrieval プロセスで観察された pattern:

1. **Tier I 候補（即時想起 6件）**: Corriu-Masse 1972, Tamao Full Paper 1976 (×3 EP), Morrell-Kochi 1975, Hayashi-Kumada 1984。全て "Kumada coupling cue" に直結する standard reference であり、retrieval cost 低い。
2. **Tier II 候補（連想 3件）**: Devasagayaraj-Knochel 1995, Fischer-Fu 2003, Tamao Full Paper 1976 の cis:trans 部分。"sp³ 拡張" や "Full Paper 細部" という 2-3 段階の連想を経由。
3. **Tier III 候補（triangulation 3件）**: Smith-Kochi 1980 (kinetic specific paper の同定), Hartwig 系列 (β-H mechanism specific の同定), EP-08a 未充填の判定。複数候補の比較・棄却を経て表面化または「未充填」判定に triangulate。
4. **DB-findability 分布**: yes 7件, uncertain 2件, no 1件 (EP-08a unfilled)。
5. **Bibliographic confidence 分布**: High 6件, Medium 2件 (EP-10a Smith-Kochi, EP-06a specific paper), Low 0件。
6. **Verification recommendation 分布**: 必須 6件, 推奨 2件 (EP-07a の 1995/2003 候補), 省略可 0件 (全候補に v18.3 conditional triggering の 1+ 要因該当)。
7. **棄却候補 10件** は (a) compendium reference, (b) 並行 lineage (Negishi, Stille), (c) 類似系で Indirect 充填, (d) 別金属（Pd 系）, (e) 重複統合 の 5 棄却理由カテゴリに分類。

これらの distribution は Sonnet v6 multi-run / GPT-5.4 v6 multi-run と比較する cross-vendor robustness analysis の primary data として記録される。Opus 4.7 の特徴的傾向としては (i) Tier I 想起が "Kumada 系列の Full Paper" と "Kochi 系列の機構研究" の 2 軸に集中、(ii) Tier III の triangulation で「未充填の判定」自体を独立 outcome として記録する傾向、(iii) 棄却候補の externalized log が比較的詳細、が観察される（要 cross-vendor 比較）。

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
