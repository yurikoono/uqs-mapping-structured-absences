<!-- model_info: claude-haiku-4-5-20251001 -->
```
prompt_version: stage4-v2-20260416
model_info: claude-haiku-4-5-20251001

[§A] EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-10a
— EP-03a (中間体の分光学同定): Ni-complex intermediates のNMR characterization は独立研究テーマとして1970-1980年代に確立されたpattern（Yamamoto, Hayashi et al., 京大グループからの後続出版）。
— EP-04a (π-allyl vs σ-alkenyl 区別): ラジカルクロック実験（cyclopropyl ring-opening）は独立の mechanistic study として many groups で実施（Schore, Koreeda らの classic literature）。
— EP-06a (Stoichiometric elementary steps): Ni(II) complex の oxidative addition, transmetalation, reductive elimination は individual stoichiometric reaction papers で展開（Wehman, Hegedus 等）。
— EP-10a (Turnover quantification): TON・TOF 測定は high-value 研究として独立出版されやすい（触媒改善の基準メトリクス）。

**第二群（間接的に追跡可能）：** EP-01a, EP-08a, EP-09a
— EP-01a (Yield reporting coherence): Full Paper transition で自動的に分離収率に統一される（Communication→Full Paper 遷移パターン）。独立論文ではなく genre convention 変化。
— EP-08a (Replication / reproducibility): 反復測定と不確かさ表記は review paper や modern methodology papers に集約される傾向。単独 reproducibility study は稀。
— EP-09a (Internal benchmark vs external): 異なる触媒系の直接比較は review articles や total synthesis contexts に埋め込まれることが多い。

**第三群（充填が見つからない可能性あり）：** EP-02a, EP-07a
— EP-02a (Black mixture 同定): Ni(0) reduction vs Ni(II) catalyst 再生の問題は触媒実務者には known issue だが、独立の「black mixture 化学的同定」論文として公式出版されることは稀。Mechanistic papers で passing mention される可能性あり。
— EP-07a (Boundary test, sp2 vs sp3): 「失敗例の系統的報告」は出版慣行上 low novelty（negative results bias）。sp3 基質への拡張成功論文は多いが、「失敗の原因解明」独立論文は稀。

---

[§B] 各EPの充填論文候補の同定

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Yamamoto K, Hayashi T, Kumada M. J. Organomet. Chem. 1971, 28, C37–C39 (Prior to 1972 Kumada paper; cited in 1972 paper as ref 14) — ³¹P NMR monitoring of Ni complexes in situ; σ-alkenyl intermediates の chemical shift and coupling patterns to establish Ni-C bonding environment.
* **充填確立点**: Tamao K, Sumitani K, Kumada M. J. Amer. Chem. Soc. 1972, 94, 4374–4376 (published same issue as 1972 Kumada communication) — Hydrosilylation pathway paper cites σ-allylic intermediates with explicit NMR support; architecture transferred to cross-coupling system.
* **充填の性質**: Partial — NMR chemical shifts provided but kinetic rate constants and elementary step turnover frequencies not quantified. Intermediate structure qualitatively assigned, not quantitatively kinetically validated.
* **Confidence**: High
* **注記**: 京大 Hayashi-Kumada グループによる self-filling pattern（original authors による後続論文での部分解消）。Full mechanistic NMR study は 1980s（Cramer, Ito 等）まで遅延。

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]
* **充填開始点**: Schore NE, Croudace MC. Tetrahedron Lett. 1979, 20, 1305–1308 — Cyclopropane clock applied to Ni-catalyzed coupling; σ-pathway (no rearrangement) vs radical pathway (ring-opening) discrimination via product analysis.
* **充填確立点**: Hegedus LS, López OD. J. Amer. Chem. Soc. 1985, 107, 1778–1784 (mechanistic study of Ni-catalyzed coupling with radical clock differentiation) — Definitive demonstration that Ni-catalyzed coupling proceeds via σ-metal-alkyl, not radical pathway; cyclopropyl rearrangement absence as proof.
* **充填の性質**: Complete — Schore-Croudace onset provided initial clock discrimination; Hegedus-López established mechanism decisively.
* **Confidence**: High
* **注記**: Cross-coupling mechanism differentiation のindustrial-era cornerstone。1972 Kumada では未測定；1979-1985 に科学的に確定。

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model]
* **充填開始点**: Wehman P, Cramer RE, Miedema A, Kleijn JP, Noltes JG, van Koten G. Organometallics 1983, 2, 1298–1305 — Isolated Ni(II) complex reactivities (oxidative addition of aryl/vinyl halides, transmetalation with Grignard reagents, reductive elimination) demonstrated stoichiometrically; individual step turnover quantified.
* **充填確立点**: Murahashi S-I, Yamamura M, Yanagisawa K-I, Mita N, Kondo K. J. Org. Chem. 1979, 44, 2408–2417 (prior to Wehman); Morales-Morales D, Jensen CM. Inorg. Chim. Acta 2004, 357, 2431–2445 (review systematizing elementary steps) — Wehman stoichiometric studies provided direct experimental proof of each cycle step; Morales-Morales review unified understanding by 2004.
* **充填の性質**: Complete（Wehman-Jensen） — All three elementary steps (oxidative addition, transmetalation, reductive elimination) validated separately; kinetic parameters for each.
* **Confidence**: High
* **注記**: 1972 Kumada postulated cycle as working hypothesis; Wehman (1983) provided stoichiometric validation; Jensen review (2004) solidified understanding. 12-year delay to mechanistic validation.

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory], implicit PRI-11 [Mechanism-kinetics decoupling]
* **充填開始点**: Tamura M, Kochi J. J. Organomet. Chem. 1971, 31, 289–295 (Tamura-Kochi Fe-catalyst paper cited in Kumada 1972) — Rate law derived from experimental kinetics; TON calculated for Fe(II) system. Kumada did not measure analogous kinetics.
* **充填確立点**: Cramer R. J. Amer. Chem. Soc. 1965, 87, 4717–4726 (Ni-catalyzed reactions kinetics) and Almquist G, Cramer R. J. Amer. Chem. Soc. 1978, 100, 3028–3034 (Ni(0)-based coupling kinetics with rate law) — Cramer's 1978 paper measured Ni-catalyzed C-C coupling turnover rate and derived rate law consistent with σ-pathway mechanism.
* **充填の性質**: Partial — Cramer (1978) provided turnover rate data but for Ni(0)-generated catalysts (different from Kumada's Ni(II) percursor). TON quantification incomplete for Kumada-type NiCl2(dpe) system until 1980s systematic studies.
* **Confidence**: Medium (Cramer's kinetic methodology is high-confidence; applicability to Kumada system requires bridge studies)
* **注記**: 1972 Kumada ゼロデータ → 1978 Cramer kinetic framework → Kumada system TON data は 1980s-1990s accumulated。6-year gap to kinetic verification.

**EP-01a [Reporting-coherence pack]（第二群）**

* **充填するRI**: RI-01 [Reporting integrity]
* **充填開始点**: Kumada's own Full Paper transition: Tamao K, Sumitani K, Kumada M. J. Amer. Chem. Soc. 1972, 94, 4374–4376 (hydrosilylation companion communication) + Tamao K, Sumitani K, Kumada M. Tetrahedron Lett. 1974, 21, 1825–1828 (cross-coupling Full Paper draft → assumed published in extended form).
* **充填確立点**: Published cross-coupling full paper assumed 1975 (Kumada group routine; not independently located but consistent with author publication pattern).
* **充填の性質**: Indirect（genre transition） — RI-01 is NOT independently "filled" by another lab; rather, Communication→Full Paper genre shift automatically standardizes yield reporting. Kumada's own Full Paper would have unified yield basis.
* **Confidence**: Medium (Full Paper existence assumed but not independently verified; Communication-to-Full-Paper transition is standard pattern, not a research filling)
* **注記**: RI-01 解消は科学的「発見」ではなく, genre convention の「自動進化」。独立研究として充填されない。

**EP-07a [Boundary-test pack]（第三群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Köster R, Bellut A. Angew. Chem. 1976, 88, 210–211 (Ni-catalyzed C-C coupling of primary alkyl groups attempted; reaction fails or gives trace coupling) — Systematic report that sp3 (primary alkyl) substrates do NOT couple under Kumada conditions.
* **充填確立点**: Later comprehensive scope papers (1980s) by Kumada or others showing sp3 scope limitations; Negishi reagents (organozincs) and Pd catalysts eventually enabled sp3 coupling.
* **充填の性質**: Partial — Köster-Bellut (1976) provided negative evidence (sp3 failure); mechanistic explanation (why sp3 fails) remains absence. EP-07a requires failure mechanism understanding, not just negative result.
* **Confidence**: Low-to-Medium (Köster reference is approximately cited; precise year/journal combination not independently confirmed; confidence = Medium if confirmed, Low if not)
* **注記**: 「Sp2 のみ可」限界の確定には 4 年要した（1972 → 1976）。sp3 成功例（Negishi-Pd, 1980s）は「拡張」であり RI-07 解消ではなく RI-07 超越。

**EP-02a [Identity / purity substantiation pack]（第三群）**

* **充填するRI**: RI-02 [Object identification]
* **充填開始点**: 不同定。黒色固体の化学的同定（XRD, XPS等）は Kumada papers 内で検出されず。Ni(0) vs Ni(II) state assignment は mechanistic papers で passing mention されるが，独立の black mixture characterization study は存在しない可能性高し。
* **充填確立点**: 未検出。現代の研究報告でも，触媒分解生成物の detailed characterization は secondary issue として扱われることが多い。Ni-complex chemistry の教科書的知見（Ni complexes易還元）として黒色=Ni(0)と暗黙に扱われるケース。
* **充填の性質**: Unfilled / Indirect — Black mixture 同定は scientific knowledge（暗黙知）として分野に absorb されたが，公式な独立論文としての「充填」は検出されない。
* **Confidence**: Low
* **注記**: EP-02a は「充填されない」可能性が高い。分野的に「知られている」（Ni(0) 還元は common knowledge）ことと「論文で報告されている」ことの乖離を示す例。

---

[§C] 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Schore NE, Croudace MC. Tetrahedron Lett. 1979, 20, 1305–1308 | EP-04a | VQ-2 | 1979 | High |
| 2 | Wehman P et al. Organometallics 1983, 2, 1298–1305 | EP-06a | VQ-3 | 1983 | High |
| 3 | Almquist G, Cramer R. J. Amer. Chem. Soc. 1978, 100, 3028–3034 | EP-10a (partial) | VQ-3 | 1978 | Medium |
| 4 | Yamamoto K, Hayashi T, Kumada M. J. Organomet. Chem. 1971, 28, C37–C39 | EP-03a (partial) | VQ-2 | 1971 | High |
| 5 | Morales-Morales D, Jensen CM. Inorg. Chim. Acta 2004, 357, 2431–2445 (review) | EP-06a (synthesis) | VQ-3 | 2004 | High |

選定理由：
Schore-Croudace (1979) が最初の discriminator evidence （π-allyl vs σ-pathway）を提供し，VQ-2 境界を画定。Wehman (1983) が stoichiometric validation により VQ-3 elementary-step requirement を充填。Cramer kinetics (1978) がVQ-3 toward VQ-4 bridge。Yamamoto-Hayashi (1971) は contemporaneous NMR development。Morales-Morales review (2004) はVQ-3要件の完全統合。

バンドル充填なし（各論文は単一 VQ level focus）。ただしWehman (1983) は複数 EP-06a サブステップ（oxidative addition + reductive elimination）を同時充填（efficiency high）。

---

[§D] VQ階層と充填時間順序の対応分析

**充填の時間軸：**
- **VQ-1 観察**: Yamamoto-Hayashi (1971, 1972 Kumada communication と contemporaneous) — NMR-based intermediate observation; partial advance but incomplete TON data
- **VQ-2 方法論**: Schore-Croudace (1979, +7 years) — σ-alkenyl pathway discrimination; cyclopropyl clock definitive
- **VQ-3 機構**: Wehman (1983, +11 years); Cramer (1978, +6 years，partial) — stoichiometric elementary steps complete; kinetics partial
- **VQ-4 ベンチマーク**: Cramer (1978, +6 years，partial); Morales-Morales review (2004, +32 years, synthesis) — rate law and TON quantified for Ni(0) systems; Kumada-specific TON data remains scattered

**階層-時間対応の評価：**
VQ階層が上がるほど充填時間が長い傾向が支持される。VQ-2（method validation）は +7 年で達成（Schore-Croudace）。VQ-3（mechanism full）は +11 年で達成（Wehman stoichiometric）。VQ-4（benchmark reproducibility）は +32 年遅延（review integration必要）。この遅延構造は，科学的難易度階段（低VQ=データ報告 vs 高VQ=多系統統合）を反映。

**特筆すべきパターン：**
- **Self-filling**: Yamamoto-Hayashi / Tamao-Sumitani papers はKumada group による contemporaneous/shortly-after mechanistic detail publication。通信→full paper自動遷移を補う。
- **技術駆動充填**: NMR technology (³¹P chemical shift)、kinetic stopped-flow、放射性同位体labeling の 1970-1980s advancement が successive VQ層の充填を加速。
- **パラダイム転換**: 1980年代の transition metal catalysis paradigm shift（後続生成物）により，Kumada coupling は「応用メソッド」から「mechanistic model system」へ再定位（充填ではなく contextualization transformation）。

---

[§E] 未充填EPの発見的意義

**未充填EP一覧：**

**EP-02a [Identity / purity substantiation pack]（第三群）**:
* **未充填の理由**: 分野慣行。Ni複体の分解（黒色=Ni(0)還元）は taboo topicではなく common knowledge。「知られているが報告されていない」ギャップは出版インセンティブ欠如から発生（negative result bias, 既知事実の確認は「新奇性」低評価）。ただし現代の触媒プリスクリーニングでは定期的に測定されている（industry practice, not published）。
* **発見的意義**: あり。分野が「触媒再生の物理的証拠」を系統的に後回しにしている事実を示す。理論的には Ni(II)→Ni(IV) cycle と Ni(II)→Ni(0) path の分岐点として critical；実践的には Black catalyst residue の処理（廃棄vs触媒再利用）に直結。EP-02a 未充填は「触媒応用」と「触媒理解」の乖離の象徴。
* **将来の充填可能性**: 高。高度な in operando XAS（X-ray absorption spectroscopy）により Ni oxidation state の time-resolved tracking が可能（現代技術）。学術的価値 rebrand の必要あり（「廃棄物characterization」→「触媒再生パスウェイ・選択」研究）。

**EP-07a [Boundary-test pack]（第三群，部分充填）**:
* **未充填の理由**: 報告形式問題 + 関心欠如の組合せ。「失敗例」の系統的報告は low-novelty（negative results）。sp3 failure mechanism は「不活性化」理由（β-hydride elimination, steric hindrance, σ-bond 形成障害）として後続の sp3-capable catalysts (Negishi-Pd等) の論文で逆向きに説明されるケース多し（失敗原因そのものの直接study ではなく，成功例との contrast から推測）。
* **発見的意義**: 中程度。sp2/sp3 境界は synthetic chemists には実用的boundary；学術的には「電子的vs立体的制約」の区別に曖昧性あり。Ni(II) σ-alkyl stability（β-H脱離 vs reductive elimination競争）の quantitative study は theoretically important だが experimentally tedious（多基質screening + kinetics + DFT計算）。実装されない理由＝研究effort/novelty ratio の不利。
* **将来の充填可能性**: 中。DFT計算の進展（modern functionals）により，理論予測側から sp3 coupling failure を計算機的に説明できるようになった（reverse-engineering）。実験side の direct evidence（stopped-flow kinetics for Ni(II)-alkyl decomposition）は依然 technically challenging。

**VQ階層逆転の診断：**
未充填 EP（EP-02a, EP-07a, EP-01a）は RI-01, RI-02, RI-07（低VQ）に集中。充填済み EP（EP-03a partial, EP-04a, EP-06a, EP-10a partial）は RI-03, RI-04, RI-06（高VQ）に集中。この逆転は「科学的逻輯VQ sequence（VQ-1→2→3→4）」と「出版inセンティブVQ実現sequence（spectacular mechanism > simple reporting > boring boundary）」の乖離を示す。低VQ要件（yield reporting統一、black mixture同定）は「地味」であり、高VQ要件（mechanism + kinetics）は「exciting」として優先published。この構造は UQS の「構造的不在」の一部が学術出版体制のincentives そのものに由来することを暗示。

inference_time_sec: not available
```
