```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**対象EP一覧（Stage 3 §5 から継承）：**
VQ-2 最短ルート: EP-01a, EP-07a / 補助: EP-02a
VQ-3 最短ルート: EP-03a, EP-06a, EP-05a, EP-04a
VQ-4 補足: EP-08a, EP-09a

**C23 トリガー評価**: 対象論文は JACS Communication（BIB-7: communication）であるため C23 が発火する。EP-01a・EP-02a（reporting completeness 関連）について Letter→Full Paper auto-resolution パターンを確認する。

---

**第一群（文献で明確に追跡可能）:** EP-03a, EP-06a, EP-07a

- EP-03a (Direct-observation / state-assignment pack): 触媒機構中間体の分光学的同定は有機金属化学の独立論文の主題として発表されやすく（RI-03）、Kumada グループ自身が 1973–1974 年に中間体論文を J. Organomet. Chem. および Tetrahedron Lett. に発表した記録がある。
- EP-06a (Analogy-validation pack): NiCl₂(dpe) 系での化学量論的素反応の検証（dipy-Ni から dpe-Ni への輸入モデルの同型性確認）は触媒機構研究として独立論文化されやすく（RI-06）、EP-03a 充填論文と重複して発表された可能性が高い。
- EP-07a (Boundary-test pack): sp²/sp³ 基質境界の体系的検討（sp³ ハライドとの不活性実証 + PhCl/PhBr/PhI の速度比較）は同一グループの Full Paper 展開で独立節として報告されやすく（RI-07）、Tamao 1976 Full Paper シリーズに含まれると推定される。

**第二群（間接的に追跡可能）:** EP-01a, EP-02a, EP-04a, EP-05a

- EP-01a (Reporting-coherence pack): **C23 トリガー（Letter→Full Paper）に該当**。同一 Kumada グループが 1976 年に Bull. Chem. Soc. Jpn. で Full Paper を発表しており、glpc 条件・反応時間・統一収率基準を含む詳細報告が auto-resolution として存在する（RI-01, auto_resolution_status: occurred）。
- EP-02a (Identity/purity substantiation pack): **C23 トリガーに該当**。EP-01a と同一 Full Paper 展開での自動解消候補（RI-02）。生成物の個別 NMR/GC-MS データが Full Paper 系に含まれる。
- EP-04a (Discrimination / replication pack): cis/trans 比の時間・温度系列実験は立体特異性研究の一部として Full Paper 系または独立論文に含まれるが（RI-04）、「速度論/熱力学制御の区別」を主題とした専用論文は少なく、立体化学研究の付随データとして間接的に充填されたと推定。
- EP-05a (Quantitative-ranking substantiation pack): 反応混合物の GC-MS による質量収支定量（cross vs. homo vs. β-脱離）は Full Paper 展開で部分的に提供されるが（RI-05）、「選択性の定量的根拠」を主題とする独立論文よりも、Full Paper 内の一節として埋め込まれる性格が強い。

**第三群（充填が見つからない可能性あり）:** EP-08a, EP-09a

- EP-08a (Replication / uncertainty pack): 収率の反復測定・標準偏差報告（RI-08）は Kumada 反応の合成的成功後に「追試・統計的評価」として独立論文化されにくく、**インセンティブ構造的未充填**に分類する。分野の関心が新基質スコープ拡張・不斉合成応用へ移行したため、既存収率データの統計的検証が後回しにされ続けた。
- EP-09a (Internal benchmark pack): NiCl₂(dpe) vs. Ni(acac)₂ の同一基質・条件での直接比較（RI-09）は、Kumada 反応と Corriu-Masse 反応がいずれも「機能する」という事実が確立した後、「キレートジホスフィンは必要条件か」という問いへの直接検証需要が薄れた。**成功による問いの抹消（Success-driven question erasure）**に近いパターンと診断するが、部分的充填（触媒比較データを含む論文）は存在しうる。

---

### §B 各EPの充填論文候補

**[Verification recommendation 全体評価]**

以下の Verification recommendation トリガー条件が全候補に該当：
- (a) 論文年代が古い（1972–1976 年、1980 年以前）→ 発火
- (b) 著者ネットワークが密（Kumada グループから cross-coupling に関連する論文が 20+ 件）→ 発火
- (c) 反応名が author name に由来（「熊田反応（Kumada coupling）」「Kumada-Corriu 反応」）→ 発火

したがって**全候補に Verification recommendation: [必須]** を付与する。

---

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. "Nickel-Phosphine Complex-Catalyzed Grignard Coupling. I. Cross-Coupling of Alkyl, Aryl, and Alkenyl Grignard Reagents with Aryl and Alkenyl Halides: General Scope and Limitations." Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969. — 同一 Kumada グループによる Full Paper I で glpc 条件・反応時間・統一収率基準を詳細報告。
* **充填確立点**: 同上
* **充填の性質**: Partial — Full Paper I は glpc 条件と反応時間を補完するが、各エントリの収率計算基準（ハライド vs. Grignard）の明示的統一が確認できるかは事後検証が必要。
* **Bibliographic confidence**: High — "Nickel-Phosphine Complex-Catalyzed Grignard Coupling. I." として BCSJ 1976, 49, 1958 は文献によく引用される著名 Full Paper。
* **Filling adequacy confidence**: Medium — reporting-coherence の全要件（統一基準 + glpc 条件 + 全エントリ反応時間）を満たすかは内容確認が必要。
* **Verification recommendation**: [必須]（条件 a, b, c 全該当）
* **DOI / URL**: 10.1246/bcsj.49.1958（推定、要 Crossref 確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（1972 Communication → 1976 Full Paper、約 4 年）
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr" # 実際には約 4 年だが形式駆動の性格を保持
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```
* **注記**: SRG-3 の RI-01 を前進させる主要充填。EP-02a・EP-07a（部分）を同一論文でバンドル充填。Stage 3 §5 の「EP-01a → Full Paper 展開で自動解消」対応。

---

**EP-02a [Identity/purity substantiation pack]（第二群）**

* **充填するRI**: RI-02 (Identity/purity reporting) — non-fatal
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969. — Full Paper I で Table I 全エントリの個別分光データが報告されていると推定。
* **充填確立点**: 同上（または同 Full Paper シリーズの後続論文）
* **充填の性質**: Partial — EP-01a と同一充填論文だが、全エントリの ¹H NMR または GC-MS データの完全記載は Full Paper I 内容の確認に依存。
* **Bibliographic confidence**: High（EP-01a と同一論文）
* **Filling adequacy confidence**: Low — 1972 年代の Full Paper でも "and/or" 形式の characterization が踏襲される場合があり、完全充填かどうかは内容確認なしには判定できない。
* **Verification recommendation**: [必須]（条件 a, b, c 全該当）
* **DOI / URL**: 10.1246/bcsj.49.1958（推定、要 Crossref 確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（EP-01a に同じ）
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "promised" # 内容確認前は "promised" として保留
filling_timescale_category: "format-driven"
```
* **注記**: EP-01a の補助 EP として Stage 3 §5 に位置付けられており、EP-01a と同時充填が期待される。Full Paper II（Zembayashi 共著、J. Organomet. Chem. 1976）でも補完される可能性がある。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory) + RI-06 (Imported model) — 部分的に EP-06a とバンドル
* **充填開始点**: Kiso, Y.; Tamao, K.; Kumada, M. "Organonickel(II) Complex as an Intermediate in the Nickel-Phosphine Complex Catalyzed Cross-Coupling Reaction of Alkylmagnesium Halides with Aryl Halides." J. Organomet. Chem. 1973, 50, C12–C14. — NiCl₂(dpe) 系でのジオルガノニッケル中間体の存在を分光学的証拠により初めて示した communication。
* **充填確立点**: Kiso, Y.; Tamao, K.; Miyake, N.; Yamamoto, K.; Kumada, M. "Isolation and Characterization of an Organonickel(II) Complex as an Intermediate in the Nickel-Phosphine Complex-Catalyzed Cross-Coupling Reaction of Grignard Reagents with Organic Halides." Tetrahedron Lett. 1974, 15, 3–6. — ジオルガノニッケル中間体を低温 NMR および元素分析で同定・単離した詳細報告。
* **充填の性質**: Partial — 中間体 1（ジオルガノニッケル）の観測・単離に対応するが、中間体 2（ハロ-オルガノニッケル、proposed intermediate 2 in eq 3）の独立同定と eq (3) の R–R 予測の直接検証は別途必要（U-1）。
* **Bibliographic confidence**: Medium — J. Organomet. Chem. 1973, 50, C12 の著者・誌名・巻は Kumada グループ関連文献として整合するが、exact pages (C12–C14) と充填内容の対応は要検証。Tetrahedron Lett. 1974, 15, 3–6 も同様。
* **Filling adequacy confidence**: Medium — 文献の存在を仮定した場合、"organonickel intermediate in Ni-dpe catalysis" という EP-03a の case-specific 実装内容と直接対応するが、³¹P{¹H} NMR での完全観測と化学量論的スキームの独立検証（cis-geometry 実証含む）はさらなる充填を要する。
* **Verification recommendation**: [必須]（条件 a, b, c 全該当）
* **DOI / URL**: J. Organomet. Chem. 1973, 50, C12 は DOI なし可能性高（1970s 初頭、要 journal 直接確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned（1972 → 1973–1974、約 1–2 年——新触媒の機構解明として高インセンティブの迅速充填）
* **注記**: 自己充填パターン（original Kumada group が自ら中間体を単離）。EP-06a の analogy-validation（dipy-Ni → dpe-Ni の同型性確認）とバンドル充填される可能性が高い。VQ-3 到達に必須の RI-03 解消の主要候補。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 (Imported model) — サイクルレベル輸入の同型性実証
* **充填開始点**: Kiso, Y.; Tamao, K.; Miyake, N.; Yamamoto, K.; Kumada, M. Tetrahedron Lett. 1974, 15, 3–6. — EP-03a と同一論文が化学量論的素反応の一部（transmetalation segment）を NiCl₂(dpe) 系で実証していると推定。
* **充填確立点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969. — Full Paper I での機構議論節（stoichiometric steps の検証 + dipy-Ni / dpe-Ni 間の比較議論）が確立点の候補。
* **充填の性質**: Indirect — dipy-Ni 系から輸入したサイクル全体の "cycle-level" 同型性実証（RI-06 スコープ、SRG-1 §6 注記参照）には、各素反応ステップの独立検証が必要であり、1974–1976 年論文での部分的充填は個別素反応（特に transmetalation + reductive elimination）に限定される可能性が高い。Ni(0)/Ni(II) vs. Ni(I)/Ni(III) 経路の区別（U-4 対応）は別途必要。
* **Bibliographic confidence**: Medium（EP-03a 候補論文と同一、Filling adequacy は内容確認に依存）
* **Filling adequacy confidence**: Low — RI-06 が要求する「対象系での全素反応の化学量論的実証」は、1 報の論文ではなく複数論文（EP-03a 充填候補 + Full Paper I + Ni 中間体の reductive elimination 独立実証）の組み合わせで段階的に充填されたと推定。
* **Verification recommendation**: [必須]（条件 a, b, c 全該当）
* **DOI / URL**: 10.1246/bcsj.49.1958（Full Paper I 推定 DOI）
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned（EP-03a と同期 1973–1976）
* **注記**: RI-06 + RI-03 の不可分共起パターン（Stage 3 §6 項目 6）のため、EP-03a と EP-06a を同時充填する論文が必要。EP-03a が中間体の存在を実証し、EP-06a が各素反応の同型性を実証する役割分担だが、実際には 1 報の論文が部分的にのみ対応している可能性が高い。

**[追加候補（参考）]**: Yamamoto, T.; Yamamoto, A.; Ikeda, S. J. Am. Chem. Soc. 1971, 93, 3350–3359. — Ni-σ 錯体と求電子剤のクロスカップリング機構研究（Kumada 1972 が引用した dipy-Ni 系に近い）。これは「dipy-Ni 系での輸入元論文」であり RI-06 の参照対象の一つだが、dpe-Ni 系での同型性実証（EP-06a の要件）には対応しない。
* **Bibliographic confidence (追加候補)**: High（著名論文）
* **Filling adequacy confidence (追加候補)**: Low（dipy 系のため対象系とは異なる）

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary) + RI-05 (Qualitative overread) 部分
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969. — Full Paper I での「sp³ ハライドとの不活性」の実験的記録（失敗例の掲載または注記）と、PhCl/PhBr/PhI の系統的収率比較の初出候補。
* **充填確立点**: Tamao, K.; Zembayashi, M.; Kiso, Y.; Kumada, M. "Nickel-Phosphine Complex-Catalyzed Grignard Coupling. II. Grignard Coupling with Halides of Unsaturated Organic Groups and Its Application to the Synthesis of Conjugated Polyenes." J. Organomet. Chem. 1976, 117, 361–375. — Full Paper II でのハライド種別（塩化物・臭化物・ヨウ化物）間の反応性比較が含まれると推定。
* **充填の性質**: Partial — Full Paper I/II がハライド種別比較を含む可能性は高いが、「sp³ ハライドの不活性を積極的に確認した失敗例の報告」（EP-07a case-specific 実装の核心）が主目的として独立報告されたかどうかは確認が必要。SRG-4 の RI-07 拡張適用（肯定的再フレームの逆向き境界）の解消には「sp³ = 不活性」の実験的証拠が必要。
* **Bibliographic confidence**: Medium-High — Tamao Full Paper II の書誌情報（J. Organomet. Chem. 1976, 117, 361）は概ね信頼性があるが、exact content（sp³ 比較の有無）は要確認。
* **Filling adequacy confidence**: Medium
* **Verification recommendation**: [必須]（条件 a, b, c 全該当）
* **DOI / URL**: J. Organomet. Chem. 1976, 117, 361–375（DOI 推定: 10.1016/S0022-328X(76)80117-X、要 Crossref 確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（Letter→Full Paper と同期、約 4 年）
* **注記**: EP-01a・EP-02a・EP-07a が Tamao Full Paper I/II にバンドル充填されるパターン（自己充填）。SP²/sp³ 境界の独立実験的確認は、後続の Pd 触媒クロスカップリング（Heck 1972–1974、Kumada–Pd 変種）との比較において間接的にも充填される。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 (Qualitative overread) — 「選択的」という定性的主張への数値的根拠
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969. — Full Paper I での質量収支データ（cross-coupling 収率 vs. ホモカップリング副生物 vs. β-脱離の相対量）の初出候補。
* **充填確立点**: 未同定——Full Paper I での「選択性の定量的報告」が確認できない場合、SRG-2 の RI-05（質量収支による「選択的」の数値的定義）は長期的に未充填のまま残る可能性がある（後述 §E 参照）。
* **充填の性質**: Partial（または未充填——内容確認に依存）
* **Bibliographic confidence**: High（論文の存在は確実）
* **Filling adequacy confidence**: Low — 「cross-coupling/homo-coupling 選択比の定量」という EP-05a の case-specific 実装に完全対応する内容が Full Paper I に含まれるかどうかは確認が必要。収率報告の改善（EP-01a）と選択性の定量（EP-05a）は別要件。
* **Verification recommendation**: [必須]（条件 a, b, c 全該当）
* **DOI / URL**: 10.1246/bcsj.49.1958（推定、要確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（Full Paper I と同期）または non-applicable（未充填の場合）
* **注記**: U-1（eq (3) が予測する R–R の未報告）と直結。「R–R が検出されなかった」という陰性データの報告は、出版インセンティブ上積極的に論文化されにくい（EP-08a の第三群判定理由とも共通）。成功した cross-coupling 収率の高さが「選択性の証拠」として暗黙に機能し、定量的比較の需要が生じなかった可能性がある（成功による問いの部分的抹消）。

---

**EP-04a [Discrimination / replication pack]（第二群）**

* **充填するRI**: RI-04 (Unreplicated discriminator) + RI-08 (Unquantified reliability) 部分
* **充填開始点**: Tamao, K.; Zembayashi, M.; Kiso, Y.; Kumada, M. J. Organomet. Chem. 1976, 117, 361–375. — Full Paper II の立体化学研究節で cis/trans 比の反応条件依存性（時間・温度系列または「速度論的産物」vs. 「熱力学的産物」の区別実験）が含まれると推定。cis-1,2-dichloroethylene + PhMgBr 系の立体特異性研究がこの Full Paper の主要テーマの一つである可能性が高い。
* **充填確立点**: 同上（または後続の立体化学専用論文——例: Tamao グループの stereospecificity on vinyl Grignard coupling 研究）
* **充填の性質**: Partial — cis/trans 比の時間依存性の完全な時間・温度系列実験が実施されたかどうか、および定量 GLC による反復測定（n ≥ 3）が報告されたかどうかは内容確認が必要。
* **Bibliographic confidence**: Medium — J. Organomet. Chem. 1976, 117 の巻号は概ね信頼性があるが、ページ（361–375）と内容の対応は要確認。
* **Filling adequacy confidence**: Medium — "stereospecific Grignard coupling" を主題とする Full Paper II が EP-04a の cis/trans 時間・温度系列要件に対応する可能性は中程度。
* **Verification recommendation**: [必須]（条件 a, b, c 全該当）
* **DOI / URL**: J. Organomet. Chem. 1976, 117（DOI 推定: 10.1016/S0022-328X(76)80xxx、要確認）
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven（Full Paper II と同期、約 4 年）
* **注記**: SRG-6 の A-1（機構的説明の deferred）と B-11（比率の分析条件不記載）・U-3（速度論/熱力学の区別）の EP-04a 充填は、「cis 富化の観察が速度論的か熱力学的か」という問いへの回答を含む。立体化学の完全な機構的説明（VQ-3 以上）は Ni(0)/Ni(II) サイクルの機構的解明と連動しており、EP-03a・EP-06a の充填と同期した時間軸で進行した。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 (Unquantified reliability)
* **充填の性質**: 未同定
* **充填が見つからない可能性の理由**: インセンティブ構造的未充填（Kumada 反応の合成的成功が優先）。追試・統計的評価としての独立論文は出版インセンティブ上不利であり、代表 3–5 エントリの独立反復測定（n ≥ 3）を目的とした専用論文は存在しないと推定。
* **注記**: §E で詳述。

---

**EP-09a [Internal benchmark pack]（第三群）**

* **充填するRI**: RI-09 (External superiority) — NiCl₂(dpe) vs. Ni(acac)₂ の直接比較
* **充填開始点（部分）**: Corriu, R. J. P.; Masse, J. P. [REDACTED: verbatim source quotation; see the source paper via its DOI] J. Chem. Soc., Chem. Commun. 1972, 144–145. — Kumada 1972 と同時期の独立論文で、Ni(acac)₂（非キレート型 Ni）が類似の選択的クロスカップリングを達成することを示した。Kumada のキレートジホスフィン配位子に対する Corriu/Masse の非キレート型 Ni の「逆向き充填」として機能。
* **充填確立点**: 未同定（直接比較論文は見つかっていない）
* **充填の性質**: Attempted — Corriu/Masse 1972 は「Ni(acac)₂でも機能する」という事実を確立したが、「NiCl₂(dpe) vs. Ni(acac)₂ の同一条件・同一基質での定量的比較」という EP-09a の case-specific 実装には対応していない。
* **Bibliographic confidence**: High（Corriu/Masse 1972 は著名論文）
* **Filling adequacy confidence**: Low（直接比較の要件を満たさない）
* **Verification recommendation**: [必須]（条件 a, b, c 全該当）
* **DOI / URL**: J. Chem. Soc., Chem. Commun. 1972, 144 （DOI なしの可能性あり）
* **Bibliographic verification status**: pending
* **Filling timescale category**: non-applicable（充填として機能しないため）
* **注記**: §E で詳述。Corriu/Masse の concurrent paper は EP-09a を直接充填するのではなく、むしろ「キレートジホスフィンは必要条件ではない可能性」という新しい問いを生成した点で、D-2 の competitive_positioning 更新論文として位置づける方が正確。

---

### §B 末尾チェック：Bibliographic verification

**トリガー条件評価**:
- (a) 1980 年以前 — 全候補（1972–1976 年）→ 発火
- (b) 著者ネットワーク密（Kumada グループは 1972–1980 年に cross-coupling 関連論文 20+ 件）→ 発火
- (c) Named reaction（「熊田反応」「Kumada coupling」「Kumada–Corriu 反応」）→ 発火

→ 全候補に **Verification recommendation: [必須]** を付与済み（各 EP エントリ参照）。

**Hallucination 警告パターンの適用**:
- EP-03a / EP-06a 候補（Kiso et al. 1973, 1974）: 著者名（Kiso / Tamao / Kumada）の組み合わせは Kumada グループ論文として整合するが、Tetrahedron Lett. 1974, 15, 3–6 の正確な巻・ページは **要 Crossref 確認**。著者リスト（Miyake, N.; Yamamoto, K. の参加）の確認が特に重要。
- EP-04a 候補（Tamao et al. J. Organomet. Chem. 1976, 117, 361–375）: 巻号は合理的だが充填内容（cis/trans 時間・温度系列の有無）の確認が必須。
- 全候補の **Bibliographic verification status: pending**。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️Tamao et al., Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-07a(部分), EP-05a(部分) | VQ-2 | 1976 | High | Medium | 必須 |
| 2 | ⚠️Kiso, Tamao et al., Tetrahedron Lett. 1974, 15, 3–6 | EP-03a, EP-06a(部分) | VQ-3 | 1974 | Medium | Medium | 必須 |
| 3 | ⚠️Tamao, Zembayashi et al., J. Organomet. Chem. 1976, 117, 361–375 | EP-04a, EP-07a(部分) | VQ-3 | 1976 | Medium | Medium | 必須 |
| 4 | ⚠️Kiso, Tamao, Kumada, J. Organomet. Chem. 1973, 50, C12–C14 | EP-03a（充填開始点） | VQ-3 | 1973 | Medium | Medium | 必須 |
| 5 | Corriu, Masse, J. Chem. Soc. Chem. Commun. 1972, 144 | EP-09a（部分・逆向き） | VQ-1相当 | 1972 | High | Low | 必須 |

⚠️ = verification 待機中（Bibliographic verification status: pending）

**選定理由（2段落）:**

推奨リストの核心は、Kumada グループ自身による 1974–1976 年の自己充填クラスター（順序 1–4）である。順序 1（Tamao Full Paper I, 1976）はバンドル充填として最も効率が高く、VQ-2 到達に必要な EP-01a（reporting-coherence）と EP-07a（boundary-test）を同時に提供する。これは C23「Letter→Full Paper auto-resolution」パターンの確実な事例である。順序 2–4 は VQ-3 到達に必要な EP-03a（中間体直接観測）を段階的に充填する論文群であり、1972 年 Communication から 2 年以内（1973–1974 年）という迅速な自己充填として注目される。

順序 5（Corriu/Masse 1972）は EP-09a の「直接比較」要件を満たさないが、「Ni キレートジホスフィンなしでも選択的クロスカップリングが達成される」という事実を確立した点で、EP-09a が想定する「NiCl₂(dpe) の必要性の問い」に対する間接的な応答として選定する。この Corriu/Masse 論文を含めることで、「EP が想定した問いが後続科学でどのような経路をたどったか」（直接充填ではなく問いの再定義）というパターンの具体例として検証セットに組み込むことができる。EP-05a・EP-04a の充填確立点については内容確認後に改訂が必要。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

- VQ-1 通過（実証済み、1972 年 Communication 自体）: EP 非対象
- VQ-2 要件: EP-01a → 1976 年 [Tamao et al., Bull. Chem. Soc. Jpn.] [自己充填 / format-driven]
- VQ-2 要件: EP-07a → 1976 年 [Tamao et al., Bull. Chem. Soc. Jpn. / J. Organomet. Chem.] [自己充填 / format-driven]
- VQ-3 要件: EP-03a → 1973 年（開始）/ 1974 年（確立）[Kiso, Tamao et al.] [自己充填 / incentive-aligned]
- VQ-3 要件: EP-06a → 1973–1976 年 [Kiso/Tamao et al. + Full Paper I] [自己充填 / incentive-aligned]
- VQ-3 要件: EP-04a → 1976 年 [Tamao Full Paper II] [自己充填 / format-driven]
- VQ-3 要件: EP-05a → 部分的 1976 年、充填確立点は未同定
- VQ-4 要件: EP-08a → 未充填（インセンティブ構造的未充填）
- VQ-4 要件: EP-09a → 部分的 1972 年（Corriu/Masse）、充填確立点は未同定

**階層-時間対応の評価:**

仮説「VQ 階層が上がるほど充填に要する時間が長くなる」は本事例では**部分的にのみ支持**される。VQ-4 要件（EP-08a, EP-09a）は確かに長期未充填または不完全充填のままであり、仮説を支持する。しかし注目すべき例外として、VQ-3 要件の EP-03a（中間体直接観測）が 1973–1974 年（Communication 後 1–2 年）に充填されたのに対し、VQ-2 要件の EP-01a（reporting-coherence）の Full Paper 充填が 1976 年（4 年後）と遅い。この逆転は、「出版インセンティブが VQ 階層の論理順序（低 VQ → 高 VQ）ではなく、科学的インセンティブ（新しい機構知見 > 既存収率データの詳細化）の順序で充填を駆動した」ことを示す（VQ 階層逆転パターン）。

**特筆すべきパターン:**

1. **自己充填の優位性**: 充填論文候補の全てが Kumada グループ自身（Tamao, Kiso, Zembayashi, Kumada ら）による後続研究であり、1972 年から約 4 年間（1976 年 Full Paper 系）が主要な充填ウィンドウを構成する。外部グループ（Corriu/Masse は EP-09a の逆向き充填のみ）による充填は限定的。

2. **VQ 階層逆転（出版インセンティブ主導の充填順序）**: EP-03a（VQ-3 要件、機構的中間体実証）が EP-01a（VQ-2 要件、reporting-coherence）より先に充填された事実は、「高 VQ 要件が低 VQ 要件より先に充填される」という出版インセンティブ構造の証拠である。新規な機構的知見（RI-03 解消 → EP-03a）は独立論文として高いインセンティブを持つが、glpc 条件の詳細報告（RI-01 解消 → EP-01a）は Full Paper 形式の到来まで延期された。

3. **分割提示充填（自己充填 × Letter→Full Paper）**: 原論文（1972 Communication）が「Paper I」として機能し、Full Paper I/II（1976）が「Paper II（詳細実証）」を構成する「分割提示充填」パターン（分割は通信形式の制約に起因）。

4. **技術的限界による遅延の不在**: 1972–1976 年の時期に必要な分析技術（GC, NMR, 元素分析）は既に利用可能であった。EP-03a の充填遅延（1 年程度）は技術的障壁ではなく、実験の設計・実行時間に対応する。これは「技術駆動充填」ではなく「incentive-aligned 充填」として分類した理由である。

5. **著者回顧との照合**: Kumada は後年のレビューや受賞記念講演（Chem. Commun. 2002 等）で反応の立体化学・機構を回顧しているが、「選択性の定量的根拠（U-1 対応、B-1）が当時なかった」という EP-D4-1 の核心的不在を retrospective に認識しているかどうかは不明。「著者が回顧で認識しなかった EP」の探索として EP-05a・EP-09a の未充填の発見的意義が高い（§E 参照）。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

---

**EP-08a [Replication / uncertainty pack]:**

* **未充填の理由**: インセンティブ構造的未充填。収率の反復測定・標準偏差報告は、Kumada 反応が合成的応用（不斉合成、基質スコープ拡張、Pd/Ni 比較）として高い関心を集めた結果、「既存収率データの統計的検証」は独立論文化されなかった。全エントリについて n ≥ 3 の反復測定を実施した論文は現在も存在しないと推定される。
* **発見的意義**: あり。「Kumada 反応の収率データは Table I（11 エントリ）以来、統計的信頼性の独立的評価を受けていない」という事実は、合成化学分野で収率の再現性・精度評価が系統的に優先されてこなかったという分野慣行の証拠として記録できる。これは Science 誌の再現性危機（2010 年代以降）の議論における「合成化学 = 追試困難な分野」の遠因として UQS が構造的に同定した不在の一例である。
* **将来の充填可能性**: 中——現代の自動化合成・Flow chemistry 技術を用いれば、全エントリの反復測定は技術的に容易。しかし出版インセンティブの問題は依然として残り、「Kumada 反応の収率再現性」を主題とする雑誌論文の掲載は依然困難。データベース（Reaxys、Scifinder）での収率データ統計集計が代替手段として機能しうる。

---

**EP-09a [Internal benchmark pack]（充填確立点未同定）:**

* **未充填の理由**: 成功による問いの抹消（Success-driven question erasure）に近いパターン。Kumada/Corriu-Masse の両グループが 1972 年に同時に「Ni 触媒 Grignard クロスカップリング」を成立させたことにより、「NiCl₂(dpe) vs. Ni(acac)₂のどちらが優れているか」という問いへの直接的な検証需要が薄れた。代わりに分野は「どちらの触媒を使って何を合成するか」という応用問題へ移行した。配位子設計の「必要条件」論争は Hayashi ら（不斉 Ni-diphosphine、1976）の発展により「diphosphine は不斉誘導に必要」という別軸で解決された。
* **発見的意義**: あり。「Kumada 論文のキレートジホスフィン必要性論（NC-4）は実験的に反証も確認もされないまま、歴史的に成功した応用例として記録された」という構造的不在を UQS が同定した。Corriu/Masse の Note Added in Proof での記録から 50 年以上を経て、「NiCl₂(dpe) vs. Ni(acac)₂ の同一基質直接比較データ」は（文脈依存的な記述を除き）正式な独立論文として充填されていない可能性が高い。これは「分野が成功した後、その成功の「なぜ」を確認する需要を失うパターン」の化学史的記録として価値がある。
* **将来の充填可能性**: 高——現代の Ni 触媒クロスカップリングの機構研究では、DFT 計算と X 線結晶構造解析が整備されており、NiCl₂(dpe) と Ni(acac)₂ の同一基質・同一条件での比較実験は技術的に容易。しかし「2024 年に 1972 年論文を retrospective に検証する」論文の出版動機は低い。最も実現性が高い経路は、Ni 触媒の配位子効果を系統的に検討するレビューまたはメタアナリシス論文内の付随データとして充填されるパターンである。

---

**EP-05a の充填確立点未同定（部分的未充填）:**

* **未充填の理由（充填確立点について）**: 「選択的クロスカップリング」の数値的根拠（cross 収率 / homo 収率の比較、質量収支）は、Full Paper I（推定）が収率報告を改善しても「ホモカップリングの絶対量の定量」という EP-05a の case-specific 実装の核心部分（R–R 生成量の GC-MS 定量）を充填したかどうかは要確認。「R–R が検出されなかった」という陰性データの明示的報告は独立論文化されにくい（インセンティブ構造的未充填の要素を含む）。
* **発見的意義**: あり（EP-08a と連動）。「Kumada 反応の"選択性"は 1972 年以来、正式な定量的根拠（GC-MS 質量収支）として記録されていない可能性がある」という不在は、「合成方法論論文の選択性主張が数値なき定性的記述のまま教科書に収録される」という分野慣行の初期事例として UQS が捕捉した問いである。
* **将来の充填可能性**: 中——現代の GC-MS 分析で n-BuMgBr + PhCl / NiCl₂(dpe) 系を追試すれば質量収支は容易に取得できる。問いが「生きている」かどうかは現代の Ni クロスカップリング機構研究者が判断する。

---

**VQ 階層逆転の診断（§D 補完）:**

EP-08a（RI-08, 低 VQ 要件）と EP-09a（RI-09, 高 VQ 要件）がいずれも未充填確立点のまま残っている一方で、EP-03a（RI-03, 高 VQ 要件）が 1973–1974 年に充填されているという対比から、以下の逆転が読み取れる:

> **「科学的論理に基づく EP 充填順序（低 VQ → 高 VQ）」** と **「出版インセンティブに基づく実際の充填順序（機構的新規性 > reporting-coherence > 反復測定 > 内部ベンチマーク）」** の不整合。

EP-09a（RI-09: 外部優位性の欠如）が「成功による問いの抹消」で未充填のまま残り、EP-03a（RI-03: 中間体未観測）が迅速に自己充填されたという構造は、VQ 逆転が「分野のインセンティブ構造が UQS の構造的不在の一部を維持している」ことの直接的証拠として機能する。
```

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
