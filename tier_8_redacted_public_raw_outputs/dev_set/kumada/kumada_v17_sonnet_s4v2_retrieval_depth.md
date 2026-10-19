```
prompt_version: stage4-v2
model_info: claude-sonnet-4-6
experimental_variant: retrieval-depth-annotation (Pilot 2)
related_pilot: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Pilot 1, v6)
related_baseline: papers/dev/kumada/kumada_v17_sonnet_s4v2.md (existing v2 baseline without depth annotation)
note: 通常の Stage 4 v2 出力に retrieval depth annotation を付加した実験変体（Pilot 2）。
      Pilot 1 (v6) との比較を目的とし、prompt 改訂が retrieval scope に与える影響を測定する。
```

---

```
prompt_version: stage4-v2-20260416
model_info: claude-sonnet-4-6
```

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-02a, EP-05a, EP-07a, EP-09a

- **EP-01a (Reporting-coherence pack)**: 通信論文→Full Paper遷移で自動解消されるRI-01起因の欠落であり、著者グループ自身による後続Full Paper（推定1976年、Bull. Chem. Soc. Jpn.）が独立論文として文献検索に直接ヒットする可能性が高い。
- **EP-02a (Identity/purity substantiation pack)**: EP-01aと同一のFull Paperで束として解消される——同一基質系の完全な分光データ記載はFull Paperの標準的内容であり、独立論文として存在する可能性が高い。
- **EP-05a (Quantitative-ranking substantiation pack)**: 選択性の質量収支定量は合成論文の方法論的主張の核心であり、後続のFull Paperまたは選択性を主題とした論文として追跡可能。
- **EP-07a (Boundary-test pack)**: sp²/sp³ハライドの境界は合成スコープ論文の典型的主題であり、著者グループまたは競合グループによるスコープ拡張論文として文献検索可能。
- **EP-09a (Internal benchmark pack)**: Corriu/Masse (Ni(acac)₂系)はNote Added in Proofで明記された具体的競合報告であり、両グループの後続論文で直接比較が行われることが予測される——検索に直接ヒットしうる。

**第二群（間接的に追跡可能）：** EP-03a, EP-04a, EP-06a

- **EP-03a (Direct-observation / state-assignment pack)**: NiCl₂(dpe)系でのジオルガノニッケル中間体の低温NMR直接観測は有機金属機構研究の専門的主題として独立論文が存在しうるが、dpe配位子に特化した論文か、より一般的なσ-オルガノニッケル系の論文かが判然としない——間接的追跡が必要。
- **EP-04a (Discrimination / replication pack)**: cis/trans比の速度論/熱力学的区別実験（時間・温度系列）は、立体選択的クロスカップリング研究の文脈で部分的に扱われるが、当該実験を主題とした独立論文は限定的と推定される。
- **EP-06a (Analogy-validation pack)**: dpe-Ni系での化学量論的素反応の個別検証は有機金属化学の機構論文に含まれるが、NiCl₂(dpe)に特化した検証と一般的σ-オルガノニッケル化学の区別が必要——文献の範囲は類似系を含む形で追跡される可能性が高い。

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a (Replication / uncertainty pack)**: クロスカップリング収率の統計的再現性（標準偏差報告を伴う3回以上の独立測定）は合成化学分野の出版慣行では独立論文として発表されない——Full Paper展開で一部の代表エントリに適用されることはあっても、体系的な不確かさ定量を主題とした独立論文が存在する可能性は低い。

---

### §B 各EPの充填論文候補の同定

---

**EP-01a [Reporting-coherence pack]（第一群）**

【思考過程の externalization】
EP-01aの要件（統一glpc条件・収率基準・全エントリ反応時間）が最初に思い浮かんだ瞬間：「通信論文→Full Paper」という自己充填パターンは即座に surface した（Tier I）。Kumada群の著者たちが1974〜1977年の間に後続Full Paperを発表したことはほぼ確実——問題は「どの雑誌の何年か」という書誌的細部への信頼度である。Bull. Chem. Soc. Jpn. という判断は、1970年代の日本の有機金属化学グループがよく使った主要誌という記憶から来る。

* **充填するRI**: RI-01 (Reporting integrity)
* **充填開始点**: Tamao, K.; Sumitani, K.; Hayashi, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Okumura, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — 通信論文のFull Paper展開として、全基質のglpc条件・統一収率基準・反応時間を体系的に記録
* **充填確立点**: 同上
* **充填の性質**: Complete（glpc条件・収率計算基準・反応時間の統一的記載）
* **Confidence**: Medium
  - 書誌根拠: Kumada群が1976年頃にBull. Chem. Soc. Jpn.にFull Paperシリーズを発表したという記憶は信頼度が高いが、著者リスト（9名）・ページ番号（1958–1969）の細部には確認が推奨される
* **注記**: EP-02aと同一論文でバンドル充填。通信→Full Paper遷移での自動解消の典型事例（§4 Era-Norm Annotationで予告済み）。充填まで約4年（1972→1976）。自己充填パターン（原著者グループ）。

---

**EP-02a [Identity/purity substantiation pack]（第一群）**

【思考過程】EP-01aと完全に同一の推論経路で即座に同定（Tier I）。Full Paperでは個別エントリの¹H NMR、IR、マスデータが記載されるのが標準的であり、"and/or"構文問題（B-13）はFull Paper展開で自動解消される。

* **充填するRI**: RI-02 (Product identity) [non-fatal residual]
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — EP-01aと同一論文でバンドル充填
* **充填確立点**: 同上
* **充填の性質**: Complete
* **Confidence**: Medium（EP-01aと同一書誌評価を継承）
* **注記**: EP-01aとのバンドル充填。自己充填パターン。

---

**EP-03a [Direct-observation / state-assignment pack]（第二群）**

【思考過程の externalization】
このEPが最も retrieval に時間を要した（Tier III）。
- 最初の連想：「NiCl₂(dpe)中間体の低温NMR観測」→ まず Yamamoto, A. 群（東京工業大学）が σ-オルガノニッケル錯体を系統的に研究していたことを想起。しかし dpe 配位子に特化した論文かどうかが不明。
- 2段階目：「機構論文」→ Kochi 群（University of Texas → Indiana）がNi触媒クロスカップリングの機構を追跡したことを想起。Tsou & Kochi が酸化的付加ステップを研究した可能性。
- 3段階目：「原著者 Kumada 群自身が中間体を characterize したか」→ 彼らの Full Paper または後続の機構論文に一部含まれる可能性——しかし低温 ³¹P{¹H} NMR による単離・同定は専門的有機金属論文のスコープ。
- 棄却した経路：「Wilke 群（Max-Planck Institut）がNi(0)化学で貢献した」→ 彼らのNi(0)研究はオレフィン反応系が中心であり、dpe-Ni のクロスカップリング中間体への直接関連が薄い。

* **充填するRI**: RI-03 (Unobserved explanatory)
* **充填開始点（部分）**: Yamamoto, T.; Yamamoto, A. et al. — Yamamoto, A. 群（Tokyo Institute of Technology）によるσ-オルガノニッケル錯体の系統的合成・特性評価論文群（1974〜1983年）が部分的充填候補。[具体的論文: 未同定 — 詳細は注記参照]
* **充填確立点（推定）**: Tamao, K.; Hayashi, T.; Kumada, M. — Kumada群による機構論文（推定1976–1978年、J. Organomet. Chem.または類似誌）での NiCl₂(dpe) 系中間体の分光特性評価。[具体的書誌: 未確認]
* **充填の性質**: Partial（対象系（dpe-Ni）でのジオルガノニッケル中間体の直接観測は類似系研究から間接的に推論されるが、特定の論文での確立が未確認）
* **Confidence**: Low
  - 書誌根拠: dpe-Ni系に特化したジオルガノニッケル(II)中間体の低温NMR直接観測を行った論文の書誌を確認できていない。Yamamoto群のσ-オルガノニッケル研究の存在は確実だが、dpe配位子系に特化した論文へのマッピングが不確実。
* **注記**: 高ハルシネーション警戒。Verification recommendation: CAS SciFinder または Reaxys で "diorganonickel" + "diphosphine" + "NMR characterization" で検索し、1972–1982年の一次論文を確認すること。EP-06aとRI-06+RI-03不可分共起（§6-6）——EP-03aとEP-06aの両論文が揃って初めてVQ-3の RI-03+RI-06 両解消が達成される。

---

**EP-04a [Discrimination / replication pack]（第二群）**

【思考過程の externalization】
- 最初の連想：「cis/trans-stilbene比の時間・温度系列実験」→ 立体選択的クロスカップリングを主題とした論文群 → Kumada群の立体化学研究 → Hayashi, T.（後にHayashi/Trost型不斉クロスカップリング）
- 2段階目：「ビニルハライドの立体特異的クロスカップリング」→ Kumada群（cis/transビニルクロリドの立体配置保持の検証）と Negishi 群（亜鉛試薬ベースでの立体特異的カップリング）の両方を想起。
- 棄却した候補：「Suzuki カップリングでのcis/trans比研究」→ Pd系・ボロン酸ベースであり、Ni/Grignard系への直接適用不可として棄却。

* **充填するRI**: RI-04 (Unreplicated discriminator), RI-08 (Unquantified reliability)
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — Full Paperでのcis/trans比測定の再現データ（複数エントリでの繰り返し測定）が部分的充填として機能
* **充填確立点（速度論/熱力学区別に関して）**: 未同定 — 速度論的vs熱力学的制御を主題とした独立実験は確認できない。Hayashi, T.; Kumada, M. による立体選択的クロスカップリング研究（推定1976–1982年）での立体保持/反転メカニズム考察が間接的に関連するが、「cis/trans比の時間・温度依存性」を直接実験したことを示す論文を確認できない。
* **充填の性質**: Partial（再現性はFull Paperで部分解消；速度論/熱力学区別は未確立と推定）
* **Confidence**: Medium（Full Paper充填はMedium；速度論/熱力学区別はLow）
* **注記**: EP-04aのうち「反復測定による不確かさ評価（RI-08）」はFull Paperで部分的に解消される可能性が高い。「速度論/熱力学制御の区別（RI-04の核心）」は現在まで明示的に主題化されていない可能性がある——§Eで「部分未充填」として記録する。

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

【思考過程の externalization】
- 最初の連想（Tier I）：「選択性の質量収支定量（クロス vs. ホモカップリング）」→ Full Paper（Tamao et al. 1976）が即座に surface した。
- 補強する連想：「反応混合物のGC-MS分析で n-Bu-n-Bu、1-ブテン、PhClを定量」→ 1970年代の有機金属Full Paperでは収率の詳細は記載されるが、「ホモカップリング生成物量の定量」を明示した研究は限定的かもしれないという疑念が生じた。
- 解決：Full Paperでは少なくともクロスカップリング選択性の定性的・半定量的記述は提供されると判断（比率や副生物量の言及）。

* **充填するRI**: RI-05 (Qualitative overread)
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — Full Paperでの反応質量収支記述（ホモカップリング生成物の定量的または半定量的記載）
* **充填確立点**: 同上（Full Paperが最も決定的な充填候補）
* **充填の性質**: Partial（「選択的」の定量的根拠を提供するが、「クロスカップリング生成物/ホモカップリング生成物/β-脱離生成物の三成分完全質量収支」としての記述がどの程度厳密かは未確認）
* **Confidence**: Medium
* **注記**: もし Full Paper でホモカップリング生成物の定量を明示していない場合、EP-05a は VQ-3 到達に必要な充填として機能しない可能性がある。Verification recommendation: Tamao et al. 1976 の実験セクションで副生物定量の記述を確認すること。

---

**EP-06a [Analogy-validation pack]（第二群）**

【思考過程の externalization】
- EP-03a より複雑な retrieval（Tier II–III）。
- 最初の連想：「NiCl₂(dpe)系での化学量論的素反応（eq 2 および eq 3 相当の個別反応）の実証」→ 有機金属化学の専門グループを探索。
- 2段階目：Yamamoto, A. 群（東工大）→ 彼らは σ-オルガノニッケル錯体（ジオルガノニッケル、ハロオルガノニッケル）の合成と反応性を系統的に研究していた。eq (2)相当（L₂NiX₂ + RMgX → L₂NiR₂）と eq (3)相当（L₂NiR₂ + R'X → 生成物）は彼らの研究スコープに入る可能性。
- 3段階目：Kochi 群 → Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979 — Ni(0) 錯体へのアリールハライドの酸化的付加（eq 2 の逆反応的ステップに相当）を機構論的に研究した論文として想起。このステップの速度論的特性評価はEP-06aの「analogy-validation」に直接関連する。
- 棄却した候補：「Otsuka/Nakamura 群のNi(0)錯体研究」→ olefin配位に特化しており、R-X酸化的付加との関連が薄いと判断して棄却。

* **充填するRI**: RI-06 (Imported model)
* **充填開始点**: Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979, 101, 7547 [書誌信頼度: Medium] — Ni(0)ビス（ホスフィン）錯体へのアリールハライドの酸化的付加の速度論・機構研究（eq 2 に相当する素反応ステップの dpe-Ni 類縁系での検証）
* **充填確立点**: Yamamoto, A. 群による σ-オルガノニッケル錯体系の化学量論的反応研究（複数論文、1974–1985年、Bull. Chem. Soc. Jpn.）[具体的書誌: 未確定]
* **充填の性質**: Indirect（dpe-Ni 系に特化した検証ではなく、ホスフィン配位 Ni(0)/Ni(II) 系一般の素反応として検証）
* **Confidence**: Medium（Tsou/Kochi 1979の存在はMediumだが、dpe-Ni特化の可否は未確認；Yamamoto群論文はLow）
* **注記**: Verification recommendation: Tsou & Kochi 1979 の DOI を CrossRef で確認し、使用した配位子系が dpe 類縁 (bidentate phosphine) か単座ホスフィンかを確認すること。RI-06（サイクルレベル輸入）とRI-03（中間体未観測）の不可分共起（§6-6）から、EP-06aとEP-03aは同時に評価する必要がある。

---

**EP-07a [Boundary-test pack]（第一群）**

【思考過程の externalization】
- 即座に想起（Tier I–II）。「sp³ハライドを [NiCl₂(dpe)] 存在下で試みた実験」→ 2つの経路が同時に浮かんだ：
  (a) Kumada群のFull Paperが sp³ハライドの不活性を記録している可能性
  (b) Corriu 群（Montpellier大学）が Ni(acac)₂系と dpe-Ni系の両方でアルキルハライドへの適用を試みた可能性
- 棄却した候補：「Negishi (1977) の亜鉛系クロスカップリング」→ これはsp³問題を「別の金属でのNi類縁系で解決する」アプローチであり、「sp³ハライドがNiCl₂(dpe)系で不活性という確認」とは異なる——EP-07aの充填としては適切でないと判断。

* **充填するRI**: RI-07 (Unsupported boundary)
* **充填開始点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — Full Paperでのsp³ハライドとの試みに関する記述（不活性確認または追加スコープ情報）
* **充填確立点（sp³/sp²境界の根拠確立）**: Corriu, R.J.P.; Moreau, J.J.E. et al. — Corriu 群の後続論文群（推定1973–1978年、J. Organomet. Chem.）でのNi触媒クロスカップリングの境界条件研究 [具体的書誌: 未確定]
* **充填の性質**: Partial（sp²制限の「試みたが不活性」という実験的確認と「なぜsp²のみか」の速度論的・機構的根拠は別問題——後者はVQ-3以上のEPとして残存する可能性）
* **Confidence**: Medium（Full Paperでの記述はMedium；Corriu後続論文はLow）
* **注記**: sp³ハライドでのNi触媒クロスカップリングは後に Kumada 群自身も探索を続け、Hayashi 群を通じた chiral phosphine 系での展開へと続く。boundary の厳密な実験的確立には Verification が必要。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

【思考過程の externalization】
- 最初に考えた経路：「Kumada反応の収率再現性を3回以上測定し標準偏差を報告した論文」→ 1970年代の合成化学論文で標準偏差付き収率報告は慣例的に行われなかった → この要件を主題とした独立論文は存在しない可能性が高いと即座に判断。
- 補完的検討：「Full Paper（1976）に収率の標準偏差は含まれるか」→ 通常の合成論文では単一試行収率の記載が標準であり、統計処理は含まれないと推定。
- 結論：第三群に分類したものの、Full Paper展開で代表エントリについて複数回の実験が実施された可能性は否定できない（ただし統計処理を伴う形での報告は想定しにくい）。

* **充填するRI**: RI-08 (Unquantified reliability)
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: 充填論文が存在しない可能性が高い
* **Confidence**: N/A（充填論文なしと判定）
* **注記**: EP-08aのRI-08は合成化学分野の出版インセンティブ構造と根本的に非整合——収率の反復統計を独立論文として発表するインセンティブが存在しない。§Eで「分野インセンティブ不整合型未充填」として詳述。

---

**EP-09a [Internal benchmark pack]（第一群）**

【思考過程の externalization】
- 即座に（Tier I）：「NiCl₂(dpe) vs. Ni(acac)₂」→ Corriu/Masse はNote Added in Proofで言及された具体的競合グループ → 彼らの後続Full Paperが直接比較を提供すると推定。
- 2段階目：「Corriu/Masse のFull Paper」→ J. Organomet. Chem. に1973〜1975年頃発表されたと推定（彼らは通信→Full Paperの同じ遷移をたどったはず）。
- 補強：Kumada群のFull Paper（1976）でも配位子スクリーニングの定量的記述が含まれる可能性（[NiCl₂(dpe)] vs. [NiCl₂(dpp)] vs. Ni(acac)₂のような比較）。

* **充填するRI**: RI-09 (External superiority)
* **充填開始点**: Corriu, R.J.P.; Masse, J.P. — 後続Full Paper（推定1973–1975年、J. Organomet. Chem.）でのNi(acac)₂系と chelating phosphine-Ni 系の直接比較 [具体的書誌: 未確定]
* **充填確立点**: Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — Kumada群Full Paperでの配位子比較（定量的活性比較、[NiCl₂(dpe)] vs. 他のNi錯体）と直接または間接的なNi(acac)₂比較
* **充填の性質**: Partial（「NiCl₂(dpe)の選択性がNi(acac)₂と同等か優れるか」という問いの定量的回答——bidentate ligandの「必要条件 vs. 有効選択肢」の決着には複数論文の統合が必要）
* **Confidence**: Low（Corriu群Full Paper書誌はLow；Kumada群Full Paperのこの論点への対応はMedium）
* **注記**: この比較が「bidentate diphosphineの必要性」（論文の機構的主張の核心：B-3、D4-8）を決着させたかどうかは §Dの時間分析で扱う。Verification recommendation: Corriu および Masse の 1972–1980 年の全論文リストを CrossRef で取得し、Ni(acac)₂ vs. NiCl₂(diphosphine) を主題とする論文を確認すること。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao, K.; Sumitani, K.; Hayashi, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Okumura, A.; Kumada, M. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-05a, EP-07a (partial) | VQ-2 | 1976 | Medium |
| 2 | Tsou, T.T.; Kochi, J.K. J. Am. Chem. Soc. 1979, 101, 7547 [要確認] | EP-06a (partial) | VQ-3 | 1979 | Medium |
| 3 | Corriu, R.J.P.; Masse, J.P. — 後続Full Paper（J. Organomet. Chem. 1973–1975年、書誌未確定） | EP-09a, EP-07a (partial) | VQ-2/3 | ~1973–1975 | Low |
| 4 | Yamamoto, A. 群 — σ-オルガノニッケル錯体の化学量論的反応研究（書誌未確定） | EP-03a (partial), EP-06a (partial) | VQ-3 | 1975–1983 | Low |
| 5 | Kumada 群 — 立体選択的/立体特異的クロスカップリング論文（推定1976–1982年、書誌未確定） | EP-04a (partial) | VQ-3 | ~1978–1982 | Low |

**選定理由:**

推奨リストの中心は、論文1（Tamao et al. 1976 Full Paper）である。これはEP-01a・EP-02a・EP-05aを束として充填し、VQ-2到達に必要な RI-01（Reporting integrity）の主要解消を一つの論文で担う。書誌信頼度はMediumだが、通信→Full Paper遷移パターンとして構造的に必然的な充填であり、存在そのものへの信頼度は高い。

論文2（Tsou/Kochi 1979）と論文4（Yamamoto群）は、VQ-3到達に必要なRI-06（サイクルレベル輸入）の対象系検証（EP-06a）と RI-03（中間体未観測、EP-03a）の部分充填を担うが、いずれも書誌信頼度がMedium以下であり、独立した文献確認が必須である。論文3（Corriu群Full Paper）はEP-09aの充填候補として論理的に必然だが書誌がLowである。

**バンドル充填の注記**: 論文1（Tamao 1976）は EP-01a + EP-02a + EP-05a + EP-07a(partial) の4EP以上を一論文でカバーする高効率バンドル充填候補であり、確認優先度が最も高い。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸（推定）:**

- VQ-2 要件 (RI-01, RI-07): EP-01a, EP-02a, EP-07a → 1976年 [Tamao et al. BCSJ] 自己充填（通信→Full Paper、4年後）
- VQ-2 要件 (RI-05): EP-05a → 1976年 [Tamao et al. BCSJ] (partial) 自己充填
- VQ-3 要件 (RI-06): EP-06a → ~1979年 [Tsou/Kochi JACS推定] + Yamamoto群論文群（~1975–1985） 技術駆動充填 + 分野横断充填
- VQ-3 要件 (RI-03): EP-03a → ~1975–1985年 [Yamamoto群・Kumada群、書誌未確定] 技術駆動充填
- VQ-3 要件 (RI-04): EP-04a → ~1978–1985年 [Kumada/Hayashi立体選択性論文] 自己充填（部分）
- VQ-4 要件 (RI-09): EP-09a → ~1973–1976年 [Corriu群Full Paper + Tamao 1976] 分野横断充填 + 自己充填
- VQ-4 要件 (RI-08): EP-08a → **未充填（現在まで）**

**階層-時間対応の評価:**

「VQ階層が上がるほど充填に要する時間が長くなる」という仮説は、本ケースでは部分的にのみ支持される。VQ-2要件（RI-01/RI-07）は1976年（4年後）に自己充填されており、最速で解消されている——これは仮説を支持する。VQ-3要件（RI-06, RI-03）の充填は1970年代後半から1980年代にかけての機構研究の蓄積に依存しており、VQ-2より遅延している。しかし、VQ-4要件（RI-09 = EP-09a）は逆にVQ-3要件より早く（~1973–1975年、Corriu群Full Paper）部分的に対応された可能性があり、「低VQから順に充填」という単純な時系列は成立しない。

**特筆すべきパターン:**

- **自己充填（VQ-2）**: Kumada群が1976年のFull Paperで EP-01a, EP-02a, EP-05a, EP-07a を自己充填したパターンは、原著者グループによる段階的な論文展開の典型例である。
- **出版インセンティブ逆転（VQ-4 = EP-08a）**: 最低VQ要件を構成するはずの RI-08（反復測定・不確かさ定量）が現在まで未充填のまま残っている——これは「科学的論理に基づくEP充填順序（低VQ→高VQ）」と「出版インセンティブに基づく実際の充填順序（高VQ→低VQ）」の逆転の直接証拠として記録する。合成化学では収率の統計的再現性よりも新規な機構知見・非対称触媒設計・スコープ拡張の方が出版インセンティブが高く、EP-08aが50年以上未充填のまま残存していることを説明する。
- **著者回顧との照合（Tamao 2002 論文 参照）**: Tamao（2002年の著者回顧的mini-review、papers/ep/discussion/tamao2002/）が「触媒の均一/不均一性問題」と「ホモカップリング副生物」に言及したかどうかを確認することで、EP-06a（均一系機構）と EP-05a（選択性定量）への著者内部での認識を評価できる——「分野内部者には不可視の構造的不在」の直接的証拠判定のために Tamao 2002 参照を推奨する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造の不整合——Grignard/Ni触媒クロスカップリングの収率を独立した3回以上の試行で再測定し標準偏差を報告することは技術的には可能だが、合成化学の出版慣行において「既知反応の収率再現性定量」は独立論文として発表されるインセンティブが存在しない。Full Paper（Tamao 1976）でも代表エントリへの複数測定適用は行われる可能性があるが、統計処理（標準偏差・信頼区間）を伴う報告は1970年代の有機合成論文では慣例ではなかった。
* **発見的意義**: あり——「収率の統計的再現性定量を要求するRI-08が、1972年の発表から現在に至るまで独立論文として充填されていない」という事実は、合成化学分野が反復測定による不確かさ評価を体系的に回避してきたという構造的証拠として記録できる。VQ階層逆転の典型事例（最低VQ要件が最も充填されにくい）として UQS の §Eパターンに登録する。
* **将来の充填可能性**: 中——現代のオープンサイエンス運動と再現性危機への関心から、「標準合成反応の収率再現性定量」を主題とした論文が今後登場する可能性は中程度。ただし Kumada 反応に特化した再現性研究は学術的インセンティブが限られる。

**EP-04a（速度論/熱力学区別部分）:**
* **部分未充填の理由**: 技術的困難 + 関心の欠如——cis-1,2-dichloroethylene + PhMgBr からのcis/trans-stilbene比の時間・温度系列実験は技術的に可能だが、この特定基質系を主題とした独立論文として発表されたかどうかは未確認。立体選択的クロスカップリング研究は「新しい基質で何が得られるか」の探索に向かい、「得られた比が速度論的産物か熱力学的産物か」を区別する実験を主題化するインセンティブは低かった。
* **発見的意義**: あり——SRG-6（cis/trans selectivity observation）として記録された観察が「機構的含意がある」と原論文が主張しながら（footnote [REDACTED: verbatim source text; see the source paper via its DOI]"）、その主張の前提（速度論的制御の確認）を実験的に検証した論文が54年間発表されていないとすれば、「著者が科学的意義を認識しながら分野が追跡しなかった問い」の事例として記録できる。
* **将来の充填可能性**: 高——現代のオルガノニッケル触媒研究の関心から、cis/trans選択性の速度論/熱力学的制御はDFT計算と組み合わせた実験的研究として容易に主題化できる。

**EP-03a（dpe-Ni特化の低温NMR観測部分）:**
* **部分未充填の理由**: 技術的困難——低温 ³¹P{¹H} NMR でジオルガノニッケル(dpe)中間体を直接観測するには、中間体の速度論的安定性、低温での分光観測技術、独立合成した参照化合物との比較が必要。1970年代の NMR 技術（特に低温 ³¹P NMR）の発展段階によっては不可能ではなかったが、dpe-Ni 系に特化した論文として発表されたかは現在確認できていない。
* **発見的意義**: あり——触媒として機能することが実用的に確立されたNiCl₂(dpe)触媒の反応中間体が、触媒の実用的発展から50年近く経っても「独立した分光学的直接観測論文」として同定できないとすれば、有機金属触媒の「中間体の存在が仮定されたまま使われ続ける」という構造的問題の事例として記録できる。
* **将来の充填可能性**: 高——現代の低温多核NMR（特に低温 ³¹P, ²H-decoupled ¹H）と単結晶X線構造解析の組み合わせで、[Ni(R)₂(dpe)] 中間体の直接観測・構造決定は現代標準技術の範囲内にある。

---

## Retrieval Depth Summary Matrix

| 充填論文 | 充填 EP | Self-Tier | 推論経路（要約） | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Tamao et al. BCSJ 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-05a, EP-07a(partial) | I | EP-01a → 通信→Full Paper自己充填パターン → Kumada群Full Paper in BCSJ | yes | Medium |
| Tsou, T.T.; Kochi, J.K. JACS 1979, 101, 7547 | EP-06a (partial) | II | EP-06a → 酸化的付加素反応の速度論 → Kochi群のNi(0)研究 → Tsou/Kochi | yes | Medium |
| Corriu/Masse Full Paper（J. Organomet. Chem. ~1973–1975、書誌未確定） | EP-09a, EP-07a(partial) | I | EP-09a → Corriu/Masse はNote Added in Proofの具体的競合グループ → 後続Full Paper | uncertain | Low |
| Yamamoto, A. 群 σ-オルガノニッケル論文群（書誌未確定） | EP-03a (partial), EP-06a (partial) | III | EP-03a → NiR₂(dpe)中間体の直接観測 → σ-オルガノニッケル化学 → Yamamoto群 → 特定論文 | uncertain | Low |
| Kumada/Hayashi 立体選択性論文（書誌未確定） | EP-04a (partial) | II | EP-04a → cis/trans比の再現 → 立体選択的クロスカップリング → Hayashi/Kumada | yes | Low |
| EP-08a | なし（未充填） | — | — | — | N/A |
| EP-05a（Full Paper以外の単独充填） | EP-05a | I | EP → 質量収支定量 → Kumada Full Paper 同定済み（上記1と同一） | yes | Medium |

---

## 付録：考慮し棄却した候補

以下は同定過程で一時的に検討したが、充填論文として棄却した候補である。

**1. Negishi, E.; King, A.O.; Okukado, N. J. Org. Chem. 1977, 42, 1821（Negishi クロスカップリング）**
- 一瞬考慮した理由：EP-09a（Ni触媒の内部ベンチマーク）の文脈でNi系クロスカップリングの比較対象として浮かんだ。また EP-07a（sp³境界）の文脈で、sp³アルキル亜鉛試薬を用いたNi触媒カップリングが sp³ハライド問題への対応策として機能するかを検討した。
- 棄却の判定キー：(a) Negishi カップリングはZn（亜鉛）試薬を用いるため、「Grignard試薬 + NiCl₂(dpe) でのsp³ハライドの境界確認」というEP-07aの要件とは本質的に異なる実験体系。(b) EP-09aの要件は「NiCl₂(dpe) vs. Ni(acac)₂の同一基質比較」であり、異なる金属（Zn vs. Mg）の比較は EP-09a を充填しない。

**2. Hayashi, T.; Konishi, M.; Kobori, Y.; Kumada, M. J. Am. Chem. Soc. 1984（非対称クロスカップリング）**
- 一瞬考慮した理由：Kumada群の Hayashi が立体化学とリガンド設計を主題とした重要論文を複数発表しており、EP-04a（cis/trans比の立体化学）と EP-07a（スコープ）の充填候補として浮かんだ。
- 棄却の判定キー：(a) 1984年の論文はキラルferrocenyl-phosphine配位子を用いた不斉クロスカップリングが主題であり、「cis-1,2-dichloroethylene + PhMgBrのcis/trans-stilbene比の速度論/熱力学区別」というEP-04a のcase-specific実装とは直接対応しない。(b) 年代が遅く（1984年）、VQ階層分析への寄与が限定的。

**3. Heck, R.F. — Pd触媒クロスカップリング論文群（1972–1976）**
- 一瞬考慮した理由：EP-06aの「analogy-validation」の文脈で、Pd触媒系でのβ-水素化物脱離・酸化的付加・還元的脱離の素反応検証が Ni 系の analogy validation として機能するかを検討した。
- 棄却の判定キー：EP-06aの要件は「dipy-Ni系から dpe-Ni 系への輸入モデル（RI-06）の同型性実証」であり、Pd系は全く別の金属・配位子系（Csp²-Hとの反応、Pd(0)/Pd(II)）。Pd系での検証はdpe-Ni系のRI-06を直接解消しない。

**4. Elschenbroich, C. 「Organometallics」（教科書・1972年以降）**
- 一瞬考慮した理由：EP-01aの文脈で、主要有機金属化学教科書がNiCl₂(dpe)系の実験条件を統一的に記録しているかを検討した。
- 棄却の判定キー：教科書はレビュー扱い（Stage 4プロンプトの「レビュー論文はEPを充填しない」規則に準拠）。教科書に記載されたデータは原論文からの転載であり新たな実験的証拠を提供しない。

**5. Tamura, M.; Kochi, J.K. Synthesis 1971, 303（原論文 ref 6）**
- 一瞬考慮した理由：EP-05a（選択性の定量）の文脈で、Tamura/Kochi の Fe 触媒系との比較によってNi/dpe系の「選択的」主張が相対的に確認されるかを検討した。また C-1（Dropped Quantitative Benchmark）との関連で参照可能性を探った。
- 棄却の判定キー：(a) Tamura/Kochi 1971は原論文より前に発表されており、Kumada 1972 の EP を充填する後続論文ではない。(b) Fe 触媒系でのデータは Ni/dpe 系の EP-05a を直接充填しない（同一基質での Fe vs. Ni 比較があれば充填になりうるが、当時の両論文には共通基質の直接比較がない）。

---

*注記: 全ての書誌情報は書誌信頼度ラベルに従って独立確認が推奨される。特に "Low" とラベルされた候補については、著者名・年・雑誌・ページ番号の全フィールドについて CrossRef または CAS SciFinder による一次確認を実施すること。Sonnet 4.6 は Kumada 関連論文系統でハルシネーション高警戒（memory参照）。*
