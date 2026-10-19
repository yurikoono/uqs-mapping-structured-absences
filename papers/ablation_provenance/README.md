# papers/ablation_provenance/ — 統制実験専用 zone（2026-08-09 新設、共著者決定 3）

**目的**: Paper A provenance ablation（retrieval vs extraction 弁別）第 1 期の出力置き場。
sandbox と異なり、**ここの出力は Paper A revision で引用され得る**（そのために新設された）。
将来の統制実験（第 2 期 P⁻/P′ 等）にも再利用する。

## 構造

```
ablation_provenance/
├── README.md                              # 本 file
├── _preregistration_paperA_20260809.md    # 事前登録（run 開始前に凍結）
├── _run_kit/                              # 実行キット（stub 6 + RUN_INSTRUCTIONS）
└── {paper_id}/
    ├── armP/run{1,2,3}/                   # PDF あり腕（標準 pipeline）
    └── armW/run{1,2,3}/                   # 書誌 stub のみ腕（prompt 逐語不変）
```

## 命名・記録規約

- 出力 file: `{paper_id}_v184_sonnet46_s{stage}_abl{P|W}_r{k}.md`（bare `_sonnet_` 禁止）
- registry: 各 run を upsert、`notes` に `ablation_paperA;arm{P|W};r{k}`、Arm W はさらに `noPDF`
- model 検証: **各 run の Step 0 で model id を逐語確認**（`claude-sonnet-4-6-20251001` 以外は
  halt）。出力冒頭の `model_info:` と filename tag の一致は
  `registry_helper.py audit-provenance --scan-fs --strict` で事後検証

## 隔離規則（ハード）

1. **1 run = 1 fresh session**（同一論文の run 間で context を共有しない）
2. **Arm W session は PDF・既存出力・過去の ablation 出力を一切開かない**（書誌 stub のみ）
3. Arm P session も既存の解析出力（papers/dev|test 内の *_s*.md）を開かない
4. 実行後に `python3 scripts/claudemd_contamination_audit.py --sweep`
5. 採点（E1/E2）は実行 session と別 session で可（機械採点、LLM 判定なし）

## 実行状態

- [ ] 4.6 d_i labels 確認（開始前の任意 amendment window — 低 prior 側 1–2 報入替の可能性。
  手順 = `_run_kit/KICKOFF_PROMPT.txt` §C）
- [x] Arm P/W 36 run 完了（2026-08-10。216 files、audit 0 mismatch、registry 36 row）
- [x] SI 取得（app1/scr2/app2/hom2。kumada/murai は SI 制度以前 = N/A）
- [x] E2 specifics matcher 実装（2026-08-09、`scripts/specifics_matcher.py`。較正値・読み方は
  事前登録 Amendment 1）
- [x] E1/E2 採点 + 裁定完了（2026-08-10）: **分岐①「extraction 支持」** — Arm W 逐語層 0/55、
  E2 null 床。結果正本 = `improvements/_methodology/ablation_results_paperA_20260810.md`、
  採点交絡の修正 = 事前登録 Amendment 3 (STUB_ECHO)

設計正本: `improvements/_methodology/uqs_epiplexity_finzi2026_correspondence_20260808.md` §6/§9
