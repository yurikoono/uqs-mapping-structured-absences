papers/dev/kumada/ 内の以下のファイルを Read tool で読み込んでください：
- kumada1972.pdf （PDF 直接読み込み、マルチモーダル）
- kumada_v17_sonnet_[s0.md](http://s0.md)
- kumada_v17_sonnet_[s1.md](http://s1.md)
- kumada_v17_sonnet_[s2.md](http://s2.md)
- kumada_v17_sonnet_[s3v2.md](http://s3v2.md)

【重要】papers/dev/kumada/ 内の Stage 4 関連ファイル（kumada_v17_sonnet_s4*.md
および kumada_v17_sonnet_s4*_retrieval_depth*.md など）は今回の実験では絶対に
Read しないでください。retrieval depth 測定の独立性のため、過去の Stage 4 出力を
参照しない fresh な retrieval を行う必要があります。

その後、prompts/stage2f3/prompt_stage4_[v2.md](http://v2.md) を Read tool で読み込み、
その指示に従って Kumada 1972 の充填論文を同定してください。
（v2 を使うことが指示の核心です。v3〜v6 は使わない）

通常の Stage 4 v2 出力に加えて、retrieval depth annotation を必ず含めてください。
各充填論文候補について：

1. **Self-classified retrieval Tier**（あなた自身の主観的評価）
   - Tier I (immediate): EP description から直接想起
   - Tier II (associative): 2–3 段階の連想
   - Tier III (deep): 複数候補の triangulation を経て surface

2. **推論経路の簡潔な記述**（1–2 文）
3. **DB-findability の見当**（yes / no / uncertain）
4. **Bibliographic confidence**（High / Medium / Low）と Verification recommendation

最終出力に以下のマトリクスを含めてください：

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| ... | ... | I/II/III | ... | yes/no/uncertain | High/Medium/Low |

末尾付録として「考慮し棄却した候補」も明示記録してください。

重要: Stage 4 タスクを実行する間、思考過程を可能な限り externalize してください。
どの候補がいつ最初に思い浮かんだか、どの候補を考えて棄却したか、明示的に記述すること。

【出力ファイル】
完成した Stage 4 v2 + retrieval depth annotation を、以下のファイル名で保存してください：
papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth_[run3.md](http://run3.md)

ファイルの先頭には以下のメタデータブロックを入れてください：

```
prompt_version: stage4-v2
model_info: claude-sonnet-4-6
experimental_variant: retrieval-depth-annotation (Multi-run robustness, v2 run 3)
related_pilot: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_[depth.md](http://depth.md) (Pilot 2, v2 run 1)
note: Multi-run robustness check の v2 第 3 run。Pilot 2 と同 prompt で実行し、
      run 間の retrieval scope と Tier annotation の variance を測定する。
```