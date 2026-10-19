prompt_version: stage4-v1-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao et al. 1976（Bulletin of the Chemical Society of Japan, full paper）

---

### §A EP充填難易度の三群分類

Stage 3 §5で提示されたEPの投入順序（VQ-2→VQ-3→VQ-4）に従い7つのEPを評価する。

**第一群（文献で明確に追跡可能）：** EP-06a, EP-07a, EP-03a, EP-09a

- **EP-06a** (Analogy-validation pack): Scheme 1の触媒サイクル（Ni(0)/Ni(II)極性機構）の検証は、クロスオーバー実験・同位体標識・反応速度論という独立した研究主題として発表されやすく、遷移金属触媒の機構研究として多数の独立論文が存在する。
- **EP-07a** (Boundary-test pack): アルキルGrignard試薬とジハロエチレンの反応性という具体的な境界問題は、スコープ拡張や基質限界の克服を主題とする合成論文の独立テーマになりやすい。
- **EP-03a** (Direct-observation/state-assignment pack): 31P NMRによる触媒休止状態の観察と重水素標識によるβ-水素脱離/再挿入の確認は、機構論文の主題として独立発表されやすい。
- **EP-09a** (Internal benchmark pack): Niシステムとそれ以前のFe/Ag/Cu系およびPd系との直接比較は、レビュー論文や方法論的比較論文の主題として文献化されやすい。

**第二群（間接的に追跡可能）：** EP-04a, EP-05a

- **EP-04a** (Discrimination/replication pack): Hammettプロットや競合速度論によるアリールハロゲン化物反応性の律速段階同定は、Pd触媒メカニズム論文でも議論されており、Ni特有の異常順序を独立主題にした論文は少なく、関連メカニズム論文の一部として含まれやすい。
- **EP-05a** (Quantitative-ranking substantiation pack): β-水素脱離抑制条件の定量的確立（SRG-5のA3/A5関連）は、触媒選択性の機構的解明の副次的結果として現れることが多く、独立主題にはなりにくい。

**第三群（充填が見つからない可能性あり）：** EP-08a, EP-01a

- **EP-08a** (Replication/uncertainty pack): GLPC検量線・応答係数・測定不確かさの記述は報告形式問題（RI-08）であり、独立論文の主題ではなく、場合によってはFull Paper展開時の慣例改善として暗黙的に解消されるか、現代まで未解消のままとなる。
- **EP-01a** (Reporting-coherence pack): 収率報告基準の統一（RI-01）は分野全体の報告慣行変化によって徐々に改善されるものであり、特定の独立論文としての充填は見つかりにくい。

---

### §B 各EPの充填論文候補

---

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Tsou TT, Kochi JK. J. Am. Chem. Soc. 1979, 101(7):6319–6332 — ビス(ホスフィン)Ni(0)錯体に対する有機ハロゲン化物の酸化的付加速度を系統的に測定し、Ni(0)→Ni(II)酸化的付加ステップの速度論的証拠を提供、Scheme 1第一ステップへの間接的実験的根拠を付与。
* **充填確立点**: Breitenfeld J, Ruiz J, Wodrich MD, Hu X. J. Am. Chem. Soc. 2013, 135(32):12004–12012 — アルキル-アルキルKumadaカップリングにおいてNi(I)/Ni(III)ラジカル経由の酸化的付加が進行することをESR・重元素標識・速度論で実証し、Kumada 1976が提案したNi(0)/Ni(II)極性Scheme 1は少なくともアルキル基質には不適用であることを確定した（機構の部分的否定としての充填）。
* **充填の性質**: Partial（Scheme 1の検証として出発したが、アルキル基質ではScheme 1が代替経路に置き換えられることを示す）
* **Confidence**: High（Breitenfeld/Hu 2013の内容および充填との対応に確信）
* **注記**: Breitenfeld 2013はScheme 1のNi(0)/Ni(II)極性サイクルを否定してNi(I)/Ni(III)ラジカルサイクルを提唱する。この意味でEP-06aの「Scheme 1の各素反応ステップを実験的に検証する」という要求に対して「少なくともアルキル基質では不成立」という充填になる。アリール基質に対するScheme 1の適用可能性は別途検討が必要であり、その意味でPartial充填。Tsou-Kochi 1979はNi(0)酸化的付加の速度論として充填開始点に相当するが詳細は文献確認が必要（Medium信頼度）。

---

**EP-07a Boundary-test pack（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Yamamura M, Moritani I, Murahashi SI. J. Organomet. Chem. 1975, 91(2):C39–C42 — Pd-ホスフィン触媒によるGrignardクロスカップリングが「類似の」反応を触媒することを示したが、ジハロエチレン+アルキルGrignardの直接的記述はない（部分的先行文脈のみ）。
* **充填確立点**: 未同定（アルキルGrignard + ジハロエチレンの生成物分布を直接定量化した専用論文を高確信度で同定できない）
* **充填の性質**: Indirect（Pd触媒や改良Ni触媒系での類似限界の克服は複数論文に分散しており、Kumada 1976のこの特定限界の直接充填論文は特定困難）
* **Confidence**: Low（直接充填論文の同定に確信なし；文献確認が必要）
* **注記**: この限界は1976年以降の主な解決策として2経路が考えられる：(1) Pd触媒（Negishi, Suzuki, Stille等）がジハロエチレン基質に対してより優れた選択性を示すことで「Ni系の限界」が事実上回避された、(2) Kumadaグループ自身がA7で予告した「マスクされたハロカルボニル化合物の反応」として続報で対処。いずれのケースでも「Kumada 1976の限界を直接充填した」という形式の論文よりも、より広い問題設定で解決した論文が多いと推定される。

---

**EP-03a Direct-observation/state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点**: Hayashi T, Tajika M, Tamao K, Kumada M. J. Am. Chem. Soc. 1976, 98(26):7811–7813 — キラルフェロセニルホスフィン配位子を用いた不斉Grignardカップリングを報告し、立体選択性の観察からNi中間体の配置保持/反転について機構的示唆を提供、触媒中間体の幾何的性質への間接的観察として機能。
* **充填確立点**: Breitenfeld J, Wodrich MD, Hu X. Organometallics 2014, 33(19):5708–5715 — ESRスペクトルおよびDFT計算によりNi(I)ラジカル中間体の電子状態を特定し、β-水素脱離がNi(I)中間体においても進行しうることを理論・実験の両面から示した（U2のβ-水素脱離/再挿入矛盾の機構的説明を提供）。
* **充填の性質**: Partial（²H同位体標識による異性化経路の追跡は含まれず；Ni(I)/Ni(III)サイクルの提案によりβ-水素脱離矛盾を説明するが、31P NMR触媒休止状態同定は未実施）
* **Confidence**: Medium（Breitenfeld 2014 Organometallics の存在は高確信だが、上記内容との対応は中程度の確信）
* **注記**: ³¹P NMRによる触媒休止状態モニタリングはin situ NMR技術の発展（1990年代以降）と対応しており、その具体的論文はAmatore/Jutand グループ（Pd系）またはHu グループの後続論文に相当する可能性がある。²H標識による異性化機構の追跡は現代的なメカニスティックスタディとして充填可能性が高いが対応する特定論文の高確信同定は困難。

---

**EP-04a Discrimination/replication pack（第二群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: Fauvarque JF, Pflüger F, Troupel M. J. Organomet. Chem. 1981, 208(3):419–427 — Pd(0)触媒によるアリールハロゲン化物酸化的付加の速度論を研究し、I>Br>Clという通常の速度順序を確立；Ni系の異常順序との対比として参照される先行研究に相当。
* **充填確立点**: 未同定（[Ni(dppp)Cl₂]系でのPhI>PhCl>PhBr異常順序を競合速度論またはHammettプロットで機構的に説明した専用論文を高確信で同定できない）
* **充填の性質**: Indirect（Pd系での速度論的研究がNi系の比較基準を提供；Ni特有の異常順序の機構的解明は分散）
* **Confidence**: Low（直接充填論文の同定に確信なし）
* **注記**: この異常順序（PhI>PhCl>PhBr with Ni(dppp)）はその後の計算化学研究（DFTによる酸化的付加活性化エネルギーの比較）で部分的に検討された可能性があるが、特定論文は文献確認が必要。Kumada1976bの問題は依然として「未充填または分散充填」に属する可能性がある。

---

**EP-09a Internal benchmark pack（第一群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点**: Negishi E, King AO, Okukado N. J. Org. Chem. 1977, 42(10):1821–1823 — ニッケルまたはパラジウム触媒によるアリールまたはアルケニル亜鉛試薬のカップリングを報告、Zn/Ni系とZn/Pd系を並行試験することでNiとPdの相対的性能を同一実験内で比較した最初期の例の一つ。
* **充填確立点**: Negishi E. Acc. Chem. Res. 1982, 15(11):340–348 — [REDACTED: substantial verbatim quotation; see Tier 9] — NiとPd触媒の各種有機金属試薬への適用性を総括的に比較し、基質クラスごとのNi/Pd優劣を明示した最初の系統的比較；C1/C2（Dropped Quantitative Benchmark）を実質的に充填。
* **充填の性質**: Partial（Negishi 1982はNi/Pd比較を提供するが、Fe/Ag/Cu（refs 15-17）との同一基質比較は含まれない）
* **Confidence**: High（Negishi 1982 Acc. Chem. Res. の存在と内容に確信）
* **注記**: Negishi 1982はグリニャール試薬に加えて有機亜鉛・有機アルミニウム・有機ホウ素なども対象にしており、Kumada 1976との直接比較は同一基質での比較ではないため「Partial」とした。Fe/Ag/Cuとの詳細比較（C1）は以降のレビューで扱われるが特定論文は MEDIUM-LOW 確信。Hayashi T, Kumada M. Acc. Chem. Res. 1982, 15(12):395–401 も比較的近い時期のNi-Grignard総説として参照価値がある（Medium確信）。

---

**EP-08a Replication/uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability; RI-01 Reporting integrity（一部）
* **充填開始点**: 未同定
* **充填確立点**: 未同定
* **充填の性質**: ―（第三群）
* **Confidence**: Low
* **注記**: GLPC測定の不確かさ定量化とGC操作条件の完全報告は、分野全体の報告慣行が変化することで徐々に改善された（1980年代以降の合成論文では分析条件の記述が詳細化）が、これを独立主題にした論文は存在しない。U3の内部矛盾（収率>転化率）はデータ修正として解消される性質のものであり、充填論文の対象ではない。

---

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: 未同定（独立論文として充填される性質ではない）
* **充填確立点**: 未同定
* **充填の性質**: ―（第三群）
* **Confidence**: Low
* **注記**: 収率報告基準の統一（孤立収率/GC収率の並行報告、限定試薬基準の一貫適用）は、1980年代以降の合成ジャーナルの査読基準の変化として達成された。単一の充填論文は存在しない。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Breitenfeld J, Ruiz J, Wodrich MD, Hu X. JACS 2013, 135:12004 | EP-06a, EP-03a（部分） | VQ-3 | 2013 | High |
| 2 | Negishi E. Acc. Chem. Res. 1982, 15:340 | EP-09a | VQ-4 | 1982 | High |
| 3 | Tsou TT, Kochi JK. JACS 1979, 101:6319 | EP-06a（開始点） | VQ-3 | 1979 | Medium |
| 4 | Hayashi T, Tajika M, Tamao K, Kumada M. JACS 1976, 98:7811 | EP-03a（開始点） | VQ-3 | 1976 | Medium |
| 5 | Negishi E, King AO, Okukado N. J. Org. Chem. 1977, 42:1821 | EP-09a（開始点）, EP-07a（間接） | VQ-4→VQ-2 | 1977 | Medium |
| 6 | Breitenfeld J, Wodrich MD, Hu X. Organometallics 2014, 33:5708 | EP-03a（確立点） | VQ-3 | 2014 | Medium |

（第三群のEP-08aおよびEP-01aは充填論文を同定できないため選定リストから除外。EP-04aは充填論文が未同定のためリストから除外。）

**選定理由：**

最優先は順序1（Breitenfeld/Hu 2013 JACS）である。この論文はEP-06a（Scheme 1検証）とEP-03a（Ni中間体の直接観察）を同時に充填し、かつ充填の形式が「Scheme 1の確認」ではなく「Scheme 1の修正・代替経路の提案」という点で最も情報量が高い。Kumada 1976が「ほぼ全ての結果を合理化する」と述べたScheme 1の適用範囲に対して、実験的境界を引く充填論文として位置付けられる（バンドル充填：2EP同時充填）。

次に順序2（Negishi 1982）はEP-09a（Ni vs Pd/Fe比較）の確立点として、Kumada 1976のC1/C2（Dropped Quantitative Benchmark）を最初の系統的比較論文として充填する。この論文の存在は、1976年から1982年の6年間、NiとPdの数値的比較が公開文献から欠如していたことを実証する。

順序3-4（Tsou-Kochi 1979, Hayashi/Kumada 1976）は時系列的に重要な充填開始点であり、VQ-3要件の最初のステップとして価値がある。特に順序4のHayashi 1976は原論文と同年の充填であり、自己充填パターンの観察として重要である。

EP-07a（境界充填）の確立論文が未同定であることはこの充填マップの主要な未解決事項であり、§Eで考察する。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-01a → 未充填（分野慣行変化として徐々に改善、特定年不明）
- VQ-2 要件: EP-07a → 未同定（充填論文特定困難）
- VQ-2 要件: EP-08a → 未充填（第三群）
- VQ-3 要件: EP-06a → 1976年（Hayashi/Kumada 1976、自己充填・開始点）→ 1979年（Tsou-Kochi、開始点）→ 2013年（Breitenfeld/Hu、確立点）[自己充填→外部補完→決定的充填の3段階]
- VQ-3 要件: EP-03a → 1976年（Hayashi/Kumada 1976、自己充填・開始点）→ 2014年（Breitenfeld/Hu Organometallics、確立点）[37年の間隔]
- VQ-3 要件: EP-04a → 未同定
- VQ-4 要件: EP-09a → 1977年（Negishi et al., 開始点）→ 1982年（Negishi Acc. Chem. Res., 確立点）[6年で確立]

**階層-時間対応の評価：**

VQ-3要件（EP-06a, EP-03a）の決定的充填に37年（1976→2013/2014）を要した一方、VQ-4要件（EP-09a）は6年（1976→1982）で充填確立点に達したという逆転現象が観察される。これはVQ-4（ベンチマーク比較）の方がVQ-3（機構的直接証拠）よりも短期間で充填されたことを意味し、「VQ階層が上がるほど充填に時間がかかる」という仮説の反例となる。EP-09aは定量的比較であり他系との数値並列が容易だったのに対し、EP-06a/EP-03aは特定中間体の直接観察という技術的難易度の高い実験を必要としたためであると推定される。VQ-2要件（EP-07a, EP-01a, EP-08a）はいずれも充填論文未同定または第三群であり、VQ-2→VQ-3→VQ-4の昇順が充填時間と必ずしも対応しないことを示す。

**特筆すべきパターン：**

- **自己充填（Hayashi/Kumada 1976）**: EP-06aおよびEP-03aの充填開始点が、原著者グループ（Kumada group）による同年論文（Hayashi, Tajika, Tamao, Kumada JACS 1976）として現れる。これは1976 BSCJスコープ論文と並行してメカニズム研究が進行していたことを示し、「スコープ論文→機構論文」という逐次発表戦略（D-2の timing pressure に対応）の証拠となる。

- **長期遅延充填（EP-06a/EP-03a）**: EP-06aの決定的充填（Breitenfeld/Hu 2013）まで37年を要した。この遅延はNi触媒機構研究がPd系と比較して歴史的に少ないこと、およびNi(I)/Ni(III)ラジカル経路という代替概念の登場が技術進歩（ESR、DFT）に依存していたことを反映する。これは技術駆動充填の典型例でもある。

- **技術駆動充填（EP-06a確立点）**: Breitenfeld/Hu 2013のNi(I)/Ni(III)ラジカル機構の確立はESR分光とDFT計算という現代的手法に依存しており、これらが利用可能になった2000年代以降に初めて決定的充填が可能になった。

- **部分充填の科学的意義**: EP-06aの「確立点」であるBreitenfeld 2013は、Scheme 1を確認するのではなく否定することで充填を達成した。これは「語られていない問いが問われた結果、元の枠組みが誤りだった」という類型であり、充填の形式が仮説の確認ではなく修正だった例として記録する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-07a Boundary-test pack:**

* **未充填の理由**: 関心の欠如 + 迂回による実質的解消。アルキルGrignard + ジハロエチレンの直接的な生成物分布を定量化した専用論文は存在しない可能性が高い。この「最も深刻な限界」は、Ni触媒系での直接的解決よりも、(1) Pd触媒・有機亜鉛（Negishi coupling）・有機ホウ素（Suzuki）等の代替カップリング法への移行、(2) 基質の改変（官能基マスキング：A7）によって「問いごと回避」されたと推定される。

* **発見的意義**: あり。「最も深刻な限界」として著者自身が明示した問いが50年間専用論文として充填されなかった場合、それはRI-07が示す「境界主張の定量的根拠欠如」が分野全体のレベルで温存されたことを意味する。Ni-Grignardカップリングのジハロエチレン基質問題は、代替反応の発展によって「解決」ではなく「忘却」された問いの可能性があり、UQSが2026年時点でも有効な問いとして抽出できることはその証拠となる。

* **将来の充填可能性**: 高。現代のNi触媒研究（Ni/光触媒二元系、Ni(I)/Ni(III)ラジカル機構を利用した難基質カップリング）は、このような難基質の直接カップリングを可能にする枠組みを提供している。具体的には：アルキルGrignard + 1,2-ジクロロエチレンの[Ni(dppp)Cl₂]触媒反応を現代の分析装置（GC-MS、LC-NMR）で完全にキャラクタライズすることは技術的に容易であり、充填のための実験コストは低い。

---

**EP-04a Discrimination/replication pack（未充填）:**

* **未充填の理由**: 分野慣行 + 技術的回避。[Ni(dppp)Cl₂]触媒のPhI>PhCl>PhBr異常反応性順序をHammettプロットまたは競合速度論で機構的に説明した専用論文は同定できない。アリールハロゲン化物の反応性研究は主にPd触媒系（Amatore/Jutand group、Buchwald group等）で発展し、Ni-ホスフィン系の異常順序は分野内で「周知の難問」として位置付けられつつも専用論文化されなかった可能性がある。

* **発見的意義**: あり。この異常順序は1976年に「説明困難」として公開され、50年近くを経ても機構的に解明されていない可能性がある。Ni触媒反応のハロゲン化物反応性順序問題は、NiのPdと異なる電子的性質（Ni(I)/Ni(III)ラジカル経路の関与）に起因すると推定されるが、Kumada 1976の提案した「複数の律速段階」仮説の直接検証はUQSが抽出した「分野が体系的に回避してきた問い」の候補として記録する価値がある。

* **将来の充填可能性**: 中。現代の過渡吸収分光・ESR・DFT計算を組み合わせることで、Ni(dppp)-PhI/PhCl/PhBr系の各律速段階の速度定数を求めることは原理的に可能だが、専用の研究プロジェクトとして立案される動機が現時点で明確でないため「中」とした。

---

**EP-08a / EP-01a（第三群・構造的非充填）:**

* **未充填の理由（共通）**: 報告形式問題（RI-01/RI-08）であり、独立論文として充填される性質ではない。現代の合成論文では GC 操作条件の完全記述と収率基準の統一が慣例となっており、この意味で分野の報告慣行が漸進的に改善されてきた。ただし、Kumada 1976の~60エントリーを「現代基準で再収集・再報告する」という論文は存在しない。

* **発見的意義**: なし（報告形式の慣行変化は標準的な科学インフラの改善であり、UQS固有の発見ではない）。

* **将来の充填可能性**: 高（実験的追試として、現代の分析装置で同一基質ペアをGC-MSで再分析・収率を再測定することは低コストで実施可能）。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
