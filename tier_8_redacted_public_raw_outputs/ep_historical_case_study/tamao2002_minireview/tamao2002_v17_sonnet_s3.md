# Stage 3 — tamao2002 v17 sonnet

```
prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tamao 2002（Journal of Organometallic Chemistry, historical mini-review）

### §1 Claim Architecture

**コア主張の要約：**
Novelty柱：1972年にNi–ホスフィン錯体触媒によるGrignard試薬とC(sp²)ハライドのクロスカップリングを（Corriu/Masseと独立に）世界で初めて報告した。これはKharasch型反応へのホスフィン錯体触媒の初適用であり、「分子触媒」という概念を開いた。三段階（OA/TM/RE）の触媒サイクルは以後のPd系クロスカップリングの原型となった。
Utility柱：β-H含有アルキルGrignard試薬の選択的カップリング・不斉クロスカップリング・オリゴチオフェン合成・ビニルクロリドの工業的適用を含む10の特徴的スコープを確立した。引用数の持続的増加（Fig. 2）により分野全体への重要性増大を定量的に示した。

**Layered structure：** 3層独立構造。(a) 歴史的優先権（化学的反証が原理的に不可能な社会的・歴史的主張）、(b) 分子触媒概念（ホスフィン錯体触媒の先例がなかったという主張、先例発見で反証可能）、(c) 10の実験的スコープ特徴（各々が基質スコープ反例で個別に反証可能）。層間依存関係：(c) が成立しても (a)(b) は独立して成立するが、(b) の「分子触媒のプロトタイプ性」は触媒サイクルの実験的確立（RI-03, RI-06）に依存しており、ここだけ (b)–(c) 間に論理的依存がある（ピボット：B-3 ↔ C-5）。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [触媒サイクル機構的証拠の体系的不在]**

* **Primary RI**: RI-03 Unobserved explanatory — Ni(0)静止状態・Ni(II)ジオルガノ中間体のいずれも直接観測されていない
* **Secondary RI**: RI-06 Imported model — OA/TM/REサイクルはYamamotoのσ-有機Ni化学から帰納されているが、このクロスカップリング系での直接的同型性検証はされていない
* **ER**: 触媒サイクルの各素過程が速度論データまたは独立した化学量論的ステップ実験によって支持されること。Ni(0)活性種の分光学的証拠またはNi(I)/Ni(III)サイクルの排除実験が存在すること。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific実装**: ³¹P NMR / UV-vis によるNi(0)錯体（例: Ni(dppp)(cod)など）の反応条件下in situ観測；NiCl₂(dppp) + ArMgX の化学量論反応によるNi(Ar)(X)(dppp)の単離・特性評価；EPRによるNi(I)種の排除（または検出）
* **注記**: B-3（high_convergence_high_gap; convergence=3/3; temperature_gap=medium）+ U-1（self-contradictory absence; V2=critical）。このケースは「提案者自身の系で提案後30年経過しても機構的検証が引用されない」という特殊パターンを呈する。

---

**SRG-2 [sec-アルキル選択性逆転の機構的根拠の不在]**

* **Primary RI**: RI-05 Qualitative overread — dppp/dmpe間の96:4→9:84の完全逆転が数値的観察として記録されているが、構造的・因果的含意（β-H脱離/再挿入の競争、鎖歩行など）は証拠なしに示唆されている
* **Secondary RI**: RI-03 Unobserved explanatory — 選択性を決定するNi–アルキル中間体の構造や速度定数が観測されていない
* **ER**: 逆転を生む分岐点（どの素過程、何の速度比が決定している）を識別する動力学実験または同位体標識実験が提示されること。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: dppp / dmpe 系それぞれで sec-アルキル（例: sec-BuMgBr）をPhClと反応させ、産物比の温度依存性（速度論的 vs. 熱力学的制御の判別）；D標識sec-アルキルGrignard試薬を用いた同位体追跡によりβ-H脱離/再挿入の関与を確認
* **注記**: B-4（high_convergence_low_gap; convergence=2/3; temperature_gap=none）+ U-2（A/B/C非該当の機構的unexplained観察）。

---

**SRG-3 [β-H脱離抑制の速度論的根拠の不在]**

* **Primary RI**: RI-05 Qualitative overread — 「選択的クロスカップリング」がβ-H脱離より優先する根拠として速度論的比較がなく、「分子触媒」という概念から含意が引き出されている
* **Secondary RI**: PRI-10 Kinetic overclaim（暫定） — 絶対的速度優位性の主張が速度データなし
* **ER**: アルキル–Ni(II)中間体からの還元的脱離速度とβ-H脱離速度の比較定量データ（または温度依存性データ）が示されること。
* **EP**: EP-10a Kinetic verification pack（暫定）; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: n-BuMgBr + PhCl / Ni(dppp)Cl₂ 系でβ-H脱離副生成物（ブテン・ベンゼン）の定量（GC/MS）；反応温度変化による副生成物比変動の測定
* **注記**: B-2（high_convergence_low_gap; convergence=2/3; temperature_gap=low）。SRG-2と関連するが根の問いが異なる（SRG-2は選択性逆転、SRG-3は選択性そのものの速度論的根拠）。

---

**SRG-4 [引用分析の方法論的透明性の欠如]**

* **Primary RI**: RI-01 Reporting integrity — 引用数データ（Fig. 2）のデータベース・クエリ・自己引用方針・3論文選択基準・1972–1983年欠落の理由がいずれも非記載
* **ER**: 引用分析に使用したデータベース、検索日、自己引用の扱い、3論文の選択基準、カバレッジ開始年（1984年）の根拠を明示すること。
* **EP**: EP-01a Reporting-coherence pack
* **Case-specific実装**: Web of Science / Scopus を明示し、検索クエリ・自己引用の扱いを記録；1972–1983年の引用データを補完し時系列の完全版を示す；3論文以外の姉妹論文の引用数を比較提示
* **注記**: B-7（high_convergence_low_gap; convergence=2/3; temperature_gap=low）。これはD-1の「分野インパクトの定量的証拠」として機能する唯一のデータであるため、VQ-4到達の前提条件となる。

---

**SRG-5 [同時独立発見の文書的・科学的比較の不在]**

* **Primary RI**: RI-09 External superiority — Corriu/Masse系と科学的内容比較なしに「独立性」を主張し、日本側発見の独自性を暗示
* **Secondary RI**: RI-04 Unreplicated discriminator — 発見の時系列は著者の自伝的回想のみに依拠し、コロボレーションがない
* **ER**: 両系の触媒・基質・条件・機構を並列比較した表または記述が提示されること；提出日時の文書的証拠（対応編集者のコメントなど）が引用されること。
* **EP**: EP-09a Internal benchmark pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: Tamao/Sumitani/Kumada [ref 1]とCorriu/Masse [ref 2]の両原報から触媒系・基質・収率・条件を抽出して対比表を作成；Chem. Commun. 誌の受理日記録の確認
* **注記**: B-8（high_convergence_low_gap; convergence=2/3; temperature_gap=low）+ C-1。歴史的priority主張であり化学的実験では解消できない部分がある（§4でera-norm処理）。

---

**SRG-6 [未発表姉妹論文への依存]**

* **Primary RI**: RI-04 Unreplicated discriminator — 工業化適用（[15]）・Yamamoto現代的記述（[8b]）・Murahashi Pdカップリング（[11b]）・Kumadaレビュー（[10d]）が提出時未発表の単一参照のみで支持されている
* **ER**: 引用されるすべての一次文献が独立した査読プロセスを経た形で検証可能であること；工業適用の場合は少なくとも収率・スケール・条件の概要が主論文または公開可能な特許に記載されること。
* **EP**: EP-04a Discrimination / replication pack
* **Case-specific実装**: 特別号2002の当該論文が実際に掲載されたかどうかを確認；工業化については特許（出願番号）または公開文献への誘導を提示
* **注記**: B-5（high_convergence_low_gap; convergence=2/3; temperature_gap=low）+ C-5。時間経過により（2002年以降）姉妹論文は発表されているため、現時点では解消可能。

---

**SRG外：CLA**

**CLA-1 [Ni > Pd反応性主張の定量的根拠の不在]**

* **Primary RI**: RI-09 External superiority — Ni触媒がPd触媒よりC(sp²)ハライドに対して「一般的に反応性が高い」という主張が直接比較データなしに外部文献（[11, 16]）のみで提示されている
* **Secondary RI**: RI-05 Qualitative overread — C-Cl結合エネルギーがC-Brより高いという反直観的事実に対し、定性的な反応性主張から因果的含意（OA速度差）が導かれている
* **ER**: 同一基質（例: PhCl, PhBr, PhI）についてNiとPdの収率または速度定数を直接対比したデータが示されること。
* **EP**: EP-09a Internal benchmark pack
* **Case-specific実装**: PhCl + PhMgBr / Ni(dppp)Cl₂ vs. Pd(dppp)Cl₂ の競合実験；ArX（X = Cl, Br, I）系列でNi/Pdを同一条件下で比較した収率表の作成
* **注記**: grounded_in: B-10, C-4, B-6。C-4（symmetric_pattern=yes; 4件の参照が数値抽出なしでグループ引用）。B-6（C-Cl優先の反直観的主張）。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Qualified)**

**VQ-1 [Observation]：通る（Non-fatal前提）**
RI-02（Object identification）：NiCl₂(dppp)等の触媒錯体・Grignard試薬・C(sp²)ハライドはいずれも一次文献で構造規定されており、本レビューが引用する形で継承される。プロダクトの同定（eqs. 1–6）も引用一次文献が担保。レビュー形式のため、RI-02は一次論文への委任として非致命的。

**VQ-2 [Method]：通る（Qualified）**
VQ-1継承を前提。RI-07（Unsupported boundary）がSRG-1外で残存する（B-6: Cl > Br > I の体系的スコープ試験なし）が、これはレビュー形式の委任として非致命的。SRG-4（RI-01: 引用分析手法の未記載）はD-1のutility主張の根拠に直接影響するが、10特徴のスコープ自体の方法論は一次文献に委任済み。RI-05（定性的順位からの過大含意）がSRG-2, SRG-3, CLA-1に残存するため、VQ-2はQualifiedとして成立。

**VQ-3 [Mechanism]：未達**
VQ-2継承を前提として、以下が未解消：
- RI-03（Ni(0)/Ni(II)中間体の直接観測なし、SRG-1）— Fatal：触媒サイクルが「Pd系クロスカップリングの原型」であるという主張の成立に必要な機構的実体が未確認
- RI-04（dppp/dmpe逆転の反復実測・弁別実験なし、SRG-2）— Fatal（機構主張に対して）
- RI-06（YamamotoモデルをNiクロスカップリング系へ同型性未検証で輸入、SRG-1）— Fatal

**VQ-4 [Benchmark]：未達（VQ-3前提不成立）**
SRG-4（RI-01: 引用分析手法）とCLA-1（RI-09: Ni > Pd直接比較）が未解消で、VQ-3到達が前提条件。

---

### §4 Era-Norm Annotation

**communication-era tolerated（2002年・historical mini-review・特別号の慣行内で許容）：**

- B-1〜B-6, B-9, B-10（10特徴の定量データ欠如）：HistoricalミニレビューはScopeの定量的提示を一次論文に委任するのが通常形式であり、2002年当時この省略は許容範囲内だった。
- B-5（未発表姉妹論文への引用）：同一特別号内の共同刊行論文を未掲載状態で引用する慣行は、special issueでは当時も現在も一定程度容認されている。
- B-7（引用分析の手法未記載）：2002年当時、化学系レビューでの引用分析にデータベース・クエリを明記する慣行は確立していなかった。
- B-8（Corriu/Masse発見の文書的証拠なし）：先行研究との関係を著者証言のみで記述するHistorical mini-reviewのジャンル的慣行内。

**modern-era deficient（現代の再認定基準で不足）：**

- B-3 + U-1（触媒サイクルの実験的検証なし）：現代の触媒化学レビューは少なくとも速度論的支持か中間体の分光学的証拠を引用することが期待される。OA/TM/REサイクルはNi(0)/Ni(I)/Ni(III)の並存する複数の機構的仮説が提案されており、これを2002年時点で無批判に「確立」として提示することも現代基準では不足。
- B-4 + U-2（dppp/dmpe逆転の機構的説明なし）：現代では96:4→9:84のような劇的な選択性逆転は必ず機構的説明または少なくとも説明の試みを要求される。このままでは読者は再現も設計も原理的にできない。
- CLA-1 / B-10 + C-4（Ni > Pd優位性の直接比較データなし）：現代の方法論比較では等条件下の直接比較が必須。

---

### §5 最短補強ルート

**現在: VQ-2 (Qualified) → 第一目的関数: VQ-3 [Mechanism]**
**第二目的関数: VQ-4 [Benchmark]（VQ-3到達後）**

**VQ-3 への最短ルート：**

1. EP-03a [Direct-observation / state-assignment pack] — NiCl₂(dppp) + ArMgX 系の化学量論的ステップ実験（Ni(0)活性種の³¹P NMR/UV-vis確認；EPRによるNi(I)種の有無測定）を実施し、OAステップで生成するNi(Ar)(X)(dppp)を同定する。RI-03とRI-06を前進。

2. EP-04a [Discrimination / replication pack] — D標識sec-アルキルGrignard試薬（例: (CD₃)CHMgBr）を用い、dppp/dmpe系における産物の重水素分布を追跡してβ-H脱離/再挿入 vs. Grignard自体の再配列を識別する。RI-04とU-2を前進。

3. EP-05a [Quantitative-ranking substantiation pack] — n-BuMgBr / sec-BuMgBr + PhCl / Ni(dppp)Cl₂ 系でβ-H脱離副生成物（ブテン・ベンゼン）の定量（GC）と温度依存性測定を行い、SRG-3（RI-05, PRI-10）を前進。

**VQ-4 への追加ルート（VQ-3到達後）：**

4. EP-09a [Internal benchmark pack] — PhX（X = Cl, Br, I）に対するNi(dppp)Cl₂ vs. Pd(dppp)Cl₂ の初速度測定（同一条件）。CLA-1（RI-09）を解消。

5. EP-01a [Reporting-coherence pack] — Fig. 2の引用分析を再実行（WoS/Scopus、自己引用フィルター、検索クエリ明記、1972–1983年補完）。SRG-4（RI-01）を解消し、Utility主張の定量的根拠を確立。

**認定ゲート順注記：** 実験投入は情報利得順（1→5）で行うが、最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4 の継承ゲート順で確定する。EP-03a（手順1）単独でRI-03/RI-06が前進してもVQ-3認定にはRI-04（手順2）の同時解消が必要。

---

### §6 制度設計への寄与

**1. RI-03 + RI-06の複合パターン——「後発的機構権威化」（PRI-11候補の提案）：**

本ケースは既存RIの境界条件を露わにする。RI-03は「提案した機構の基礎となる種が観測されていない」を、RI-06は「他系モデルを同型性検証なしに輸入」をそれぞれ捉える。しかし本論文では両者が融合した特異パターンが観察される：提案者自身の系で提案後30年が経過したにもかかわらず、機構的検証を引用せず、提案当時の権威性を現在もそのまま再提示している（「retroactive mechanistic consolidation」）。これはRI-03 + RI-06の単純な重複ではなく、レビュー論文が「時間的権威」によって実験的証拠の要求を回避するという構造的パターンであり、PRI-11候補として提案する。昇格には独立2報での同型確認を要する。

**2. Era-norm第三タグの提案——「review-genre tolerated」：**
§4の分析では「communication-era tolerated」タグを使用したが、この論文の省略の多くは「2002年当時の慣行」ではなく「HistoricalミニレビューというジャンルのNorm」から生じている。後者は時代的慣行ではなくジャンル的慣行であり、両者を区別するために「review-genre tolerated」という第三タグをEra-norm Annotationに追加することを提案する。

**3. 既存RI/EP辞書のCase-specific実装例の追加：**
EP-03a（Direct-observation pack）のCase-specific実装として、「Ni(0)活性種のin situ ³¹P NMR観測 + EPRによるNi(I)排除実験」という実装パターンを、Ni触媒系における標準的プロトコルとして辞書に追加可能。

**4. 一般知見：**
本論文は「Historical mini-review + 特別号」という複合的制度設計が、VQ-2止まりの主張構造を標準的報告様式として固定化する機能を果たすことを示す好例である。UQSプロトコルはこのような「ジャンルによる証拠要求の圧縮」を明示化する点で有効であることが確認された。
```
