# Retrieval-depth pilot — session records (Kumada 1972)

Exported records of seven chat sessions (`user_messages_*`, `thinking_trace_*`, `final_output_*`) and, for each, a `depth_analysis_*.json` made from them in the project. The SI-9.10 tally does not read this folder (its retrieval-depth candidates come from the `*_retrieval_depth*.md` Stage 4 files of `dev_set/kumada/`).

- Session `7669a991` is not a retrieval-depth run: its user message asks for a launch prompt for a v18.4 run with another tool, and its final output is that prompt.
- The thinking traces of sessions `7669a991` and `27e35148` are 21-byte stubs, and their `depth_analysis` files are identical; both mark every paper as absent because there was no trace to analyse.
- The script that wrote the `depth_analysis` files is not deposited. The redacted copies in Tier 8 hold the session records but not the JSON files.
