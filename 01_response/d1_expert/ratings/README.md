# D1 ratings (transcribed from the paper forms)

- `ratings.csv` — one row per rater × item. `form_no` is the item's position on the form; `type` and `pool_index` link it to `../items_drawn_rewritten.json`. `category` is one of `i`–`vi`, or empty if the rater left it blank. `confidence` is `high`, `medium` or `low`. Comments are not in this file (Amendment 3): see `comments_summary.md`.
- The post-rating expertise questionnaire was not administered (Amendment 4).
- Rater labels follow the pre-registration (Amendment 2): R1 and R2 are the two forms returned before Amendment 1 was committed; R3 and R4 are numbered in the order of return.
- The scans and the label-to-name key are in `../_private/`, which git ignores. No name enters any file here. Verbatim comments are kept only in `../_private/` (Amendment 3).
- Transcription: the author enters the data, and a second pass checks every cell against the scans. Analysis (`../analyze_d1.py`) starts only after both passes, and the primary analysis (R1, R2) is reported first.
