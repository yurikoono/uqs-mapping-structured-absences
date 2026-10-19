必要なファイルを並行して読み込みます。まず既存出力ファイルとプロンプトを読み込みます。

S2とS3v2ファイル、およびPDFを並行読み込みします。

PDFのパスを確認します。

PDFファイル名を確認しました（`Kumada_1972.pdf`）。読み込みます。

全入力を確認しました。Stage 4 v2 + retrieval depth annotationを実行して出力を生成します。

出力を保存しました。主要な結果をまとめます。

---

## 実行完了：`kumada_v17_sonnet_s4v2_retrieval_depth.md`

### 同定された充填論文とRetrieval Tier

| EP | 充填論文（主要） | Self-Tier | Bib confidence |
|---|---|---|---|
| EP-01a, EP-02a, EP-05a, EP-07a | Tamao et al. Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 | **I（即座）** | Medium |
| EP-06a | Tsou & Kochi JACS 1979, 101, 7547 | **II（連想）** | Medium |
| EP-09a | Corriu/Masse Full Paper（書誌未確定） | **I（即座）** | Low |
| EP-03a | Yamamoto A. 群 σ-オルガノニッケル論文群（書誌未確定） | **III（深層）** | Low |
| EP-04a | Kumada/Hayashi 立体選択性論文（書誌未確定） | **II** | Low |
| **EP-08a** | **未充填**（インセンティブ構造的不在） | — | N/A |

### Pilot 1 (v6) との比較に関わる構造的差異

- **v2プロンプトのEP体系**（EP-01a〜EP-09a、9EP）は §2 SRG/CLA crosswalk から直接導出されており、EPのcase-specific実装が具体的——これにより retrieval の「検索語逆算」アプローチが明確に機能した
- **EP-08a**（第三群・未充填）が明示的に同定されたことは、v6との比較で「プロンプト版がEP三群分類の粒度に与える影響」を測定する材料になる
- **書誌ハルシネーション警戒**として、Kumada系論文全体にMedium以下の信頼度を付与し、全EPについてVerification recommendationを明記した（Pilot 1との重要な方法論的差異）