# 事前登録 — Paper A provenance ablation 第 1 期（2026-08-09 凍結）

**Status**: PRE-REGISTERED（本文書 commit 後・全 run 開始前）。最初の run 実行後の変更は
すべて日付つき amendment として本文書末尾に追記する（無断改稿禁止）。

## 1. 問い

Paper A の解析出力（S0–S2）は、入力論文からの **extraction** か、事前学習重みからの
**retrieval** か。定量的には S_T(A|paper, weights) と S_T(A|weights) の増分を、
PDF あり/なしの 2 腕対比で操作化する。

## 2. 設計

- **腕**: Arm P = 標準 pipeline（PDF 読込あり）／ Arm W = 書誌 stub のみ（`_run_kit/stub_*.txt`、
  **prompt は逐語不変**、harness 側入力差し替えのみ）
- **Profile**: `paperA` 凍結（prompts/v184 の stage0 / turn1–3 / turn4_v184 / stage2_v184、
  S0–S2 のみ、S3/S4 なし）× **Sonnet 4.6**（各 run で逐語検証。合格 2 形 = `claude-sonnet-4-6` /
  `claude-sonnet-4-6-20251001` — Amendment 2）
- **対象 n=6（d_i 層化）**: 高 prior = kumada, murai, app1 ／ 低 prior = app2 (2025),
  scr2 (2025), hom2 (2024)（低側は 4.6 訓練 cutoff 後出版 = d_i≈0 の構造保証）。
  層化根拠 = S5 暫定 labels + cutoff 基準（`ablation_di_probe_results_20260808.md` §5）。
  **Amendment window**: 4.6 labels 確認の結果による低 prior 側 1–2 報の入替は、最初の run
  開始前に限り amendment なしで許可。
- **反復**: 各腕 × 各論文 N=3（fresh session、across-run union で集計）。計 36 run。
- **決定事項（共著者承認 2026-08-09）**: kumada を含める ／ 既存 run は Arm P に算入しない
  （全 run 新規、既存 run は参考対照として別掲可）／ 置き場は本 zone。

## 3. Endpoints（機械採点、LLM 判定不使用）

- **E1（primary、逐語層）**: anchor 実在率 = (EXACT + HIGH) / text quotes。
  採点 = `scripts/anchor_matcher.py`（8-gram containment、閾値 **0.75 / 0.45 で凍結** —
  較正: 真正 min 0.756 / 逸脱 max 0.562 / 別論文照合の偽陽性 0.000）。FORMULA・CAPTION は
  分母から除外（別枠報告）。SI が存在する論文は本文+SI を連結照合（SI は採点前までに取得）。
- **E2（secondary、内容層）**: content-specifics 一致率 = 出力中の数値 token・化合物名・
  固有 entity の実論文（本文+SI）との機械 match 率。特異度 5 層で層別報告
  （一般概念 / system-specific entity / document-specific relation / 定量値 / absence relation）。
- **補助**: 項目数・T3 比率・section-coverage（既存 parser 流用）。
- **Arm P の役割**: 各論文の matcher 床キャリブレーション（Arm P の E1 が低い論文は
  text layer/matcher の限界の指標であり fabrication ではない）。

## 4. 事前登録予測（graded、2 層）

- **Retrieval 仮説**: Arm W の E1・E2 が d_i とともに上昇し、P–W ギャップが高 d_i で縮小。
- **Extraction 仮説**: Arm P は d_i に対して不変、Arm W は全 d_i で床に張り付く。
- **Register 変換 retrieval（E1 の盲点対応、2 層分岐）**:
  - Arm W で E1 低 × **E2 高**（特に高 d_i 論文の document-specific relation / 定量値層）
    = 逐語でなく内容が漏出 = **register 変換 retrieval**
  - Arm W で E1 低 × E2 低 = **extraction 支持**
  - Arm W で E1 高 = 逐語記憶（最強の retrieval 証拠）

## 5. 解釈のコミットメント（結果別、revision での扱い）

1. **Extraction 支持**（W 全域崩落）: revision response + Limitations に統制実験として報告。
   「extraction であって retrieval でない」の初の直接証拠。
2. **部分 retrieval**（高 d_i のみ E2 漏出等）: caveat を先回りして自分の言葉で記載、
   SI-7a（anchor 検証）の存在意義を強化する形で報告。
3. **Retrieval 優勢**: 共著者協議の上で先回り caveat。隠さない（honest reporting）。

## 6. 分析規則

- **within-paper contrast のみ**（P–W 差、同一論文内）。cross-paper の絶対値比較は行わない
  （era/register/OCR 交絡 — `ablation_di_probe_results_20260808.md` §4 の計器所見による）。
- 集計は各腕 across-run union（N=3）と per-run の両方を報告。
- 統制の成立確認を先に読む（Entry 096 規律 11）: Arm P の E1 床が較正表（v17/v184 出力で
  0.71–1.00）と整合すること。整合しない場合は解釈より先に計器を疑う。

## 7. 衛生

隔離・命名・registry・contamination sweep は zone README の規約に従う。
本文書の scoring script 版: anchor_matcher.py は commit `5a5782b` 時点の仕様
（E2 用の specifics matcher は採点開始前に追加実装し、実装後・採点前に本文書へ amendment 追記）。

---
（amendments 追記欄）

## Amendment 1（2026-08-09、全 run 開始前）— E2 matcher 実装

- `scripts/specifics_matcher.py` を実装（§7 の予告どおり、採点開始前）。機械化の範囲 =
  **numeric（≈ 定量値層）と entity（≈ system-specific 層）のみ**。document-specific relation /
  absence relation 層は canonical record coding の管轄（本実験の scope 外）と確定。
- 仕様: UQS 内部 ID（V1-Q*, S0-*, EP-* 等）を抽出前に除去 / numeric は単位付き抽出 +
  数値 core の token fallback（表描画対策）/ entity は英数混在・化学式様 token + 略号辞書、
  末尾量論数字の fallback（OCR 下付き崩れ対策）/ stub（書誌）token 除外。
- **較正値（真正 run による正例 / 別論文照合による負例）**: numeric 正例 0.81–0.95 vs
  負例 0.36–0.49（汎用値の null 床が高い — 単独絶対値で読まない）/ entity 正例 0.24–0.39 vs
  負例 0.00–0.07（正例床は OCR・別名による — Arm P が per-paper 床を与える）。
- **読み方の確定**: E2 も E1 同様 **within-paper の P–W 対比**でのみ解釈し、Arm P を
  per-paper 床、負例値（numeric ~0.4 / entity ~0.05）を null 基準とする。

## Amendment 2（2026-08-09、全 run 開始前）— model 検証の合格形を 2 形に修正

pilot run が HARD STOP で正しく停止（session の harness 報告は短縮形 `claude-sonnet-4-6`、
pin は日付付き `claude-sonnet-4-6-20251001` — **不一致の原因は事前登録側の過剰指定**であり
model の取り違えではない。日付付き形は歴史的出力の `model_info:` 行に由来し、harness の
報告形式と異なっていた）。guard の目的（Sonnet 5 との取り違え防止）は `claude-sonnet-4-6` の
逐語一致で満たされるため、**合格 = 上記 2 形のいずれかと完全一致**へ修正（glob・部分一致・
alias 推論による自己判断は引き続き禁止）。`model_info:` には harness が報告した文字列を
そのまま記録し、日付形の自己補完はしない。停止した pilot は出力を一切書いていないため
run 数への影響なし。なお pilot session が「alias の透過的同一性を自分で保証することは指示に
反する」と判断して停止したのは guard の期待どおりの挙動（自己免除の拒否）。

## Amendment 3（2026-08-10、全 run 完了後・解釈確定前）— E1 に STUB_ECHO カテゴリを追加

初回採点で Arm W の E1 が d_i と逆相関気味の不可解なパターン（post-cutoff の app2 が 0.81 等）
→ provenance dump で検分した結果、Arm W の HIGH 判定 quote は**書誌 stub のタイトル断片**
（モデル自身が `(BIB-1、スタブのみ利用可能)` と provenance を自己申告）であり、タイトルは
論文中に実在するため E1 が誤って「実在」判定していた（**stub echo** — E2 には stub 除外が
あったが E1 に無かった採点側の穴）。修正 = anchor_matcher に **STUB_ECHO カテゴリ**
（stub との gram 含有率 ≥ 0.6）を追加し実在率の分母から除外。修正過程で grams() 内の
意図しない space→NBSP 置換（作成時の混入。両側が同関数を通るため E1 結果には無影響）も
発見・清掃し、Arm P で回帰なしを確認（kumada P1 = 1.000 不変）。**変更は採点手続きのみで、
endpoint 定義・閾値・予測・分岐は不変。**方向として、この修正は Arm W のスコアを下げる
（= retrieval 証拠を減らす）側であり、extraction 支持へのバイアス懸念に対しては
「除外されたのは物理的に stub 由来と確定できる quote のみ」で答える。
