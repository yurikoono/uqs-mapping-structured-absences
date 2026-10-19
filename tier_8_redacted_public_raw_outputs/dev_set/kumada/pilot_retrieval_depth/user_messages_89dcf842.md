papers/dev/kumada/ 内の以下のファイルを Read tool で読み込んでください：
- kumada1972.pdf （PDF 直接読み込み、マルチモーダル）
- kumada_v17_sonnet_[s0.md](http://s0.md)
- kumada_v17_sonnet_[s1.md](http://s1.md)
- kumada_v17_sonnet_[s2.md](http://s2.md)
- kumada_v17_sonnet_[s3v2.md](http://s3v2.md)

【重要】papers/dev/kumada/ 内の Stage 4 関連ファイル（kumada_v17_sonnet_s4*.md）は
今回の実験では絶対に Read しないでください。retrieval depth 測定の独立性のため、
過去の Stage 4 出力を参照しない fresh な retrieval を行う必要があります。

その後、prompts/stage2f3/prompt_stage4_[v2.md](http://v2.md) を Read tool で読み込み、
その指示に従って Kumada 1972 の充填論文を同定してください。
（最新版ではなく v2 を使うことが指示の核心です。v3〜v6 は使わない）

通常の Stage 4 v2 出力に加えて、retrieval depth annotation を必ず含めてください。
各充填論文候補について：

1. **Self-classified retrieval Tier**（あなた自身の主観的評価）
   - Tier I (immediate): EP description から直接想起
   - Tier II (associative): 2–3 段階の連想（例：EP → 反応カテゴリ → 著者群 → 論文）
   - Tier III (deep): 複数候補の triangulation を経て surface

2. **推論経路の簡潔な記述**（1–2 文）
   例: [REDACTED: substantial verbatim quotation; see Tier 9]

3. **DB-findability の見当**（タイトル・abstract に EP 関連キーワードを含むか yes/no/uncertain）

4. **Bibliographic confidence**（High / Medium / Low）と Verification recommendation
   （Sonnet の Kumada 系 hallucination 高警戒を引き続き適用）

最終出力に以下のマトリクスを含めてください：

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| ... | ... | I/II/III | ... | yes/no/uncertain | High/Medium/Low |

末尾付録として「考慮し棄却した候補」も明示記録してください
（pilot 1 で価値が surface した項目です）：
- 棄却した候補名
- 一瞬考慮した理由
- 棄却の判定キー

重要: Stage 4 タスクを実行する間、思考過程を可能な限り externalize してください。
どの候補がいつ最初に思い浮かんだか、どの候補を考えて棄却したか、明示的に記述すること。

【出力ファイル】
完成した Stage 4 v2 + retrieval depth annotation を、以下のファイル名で保存してください：
papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_[depth.md](http://depth.md)

ファイルの先頭には以下のメタデータブロックを入れてください：

```
prompt_version: stage4-v2
model_info: claude-sonnet-4-6
experimental_variant: retrieval-depth-annotation (Pilot 2)
related_pilot: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_[depth.md](http://depth.md) (Pilot 1, v6)
related_baseline: papers/dev/kumada/kumada_v17_sonnet_[s4v2.md](http://s4v2.md) (existing v2 baseline without depth annotation)
note: 通常の Stage 4 v2 出力に retrieval depth annotation を付加した実験変体（Pilot 2）。
      Pilot 1 (v6) との比較を目的とし、prompt 改訂が retrieval scope に与える影響を測定する。
```
（メタデータブロックの ``` は通常のバッククォート 3 つです）

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
