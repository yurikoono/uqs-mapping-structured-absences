#!/usr/bin/env python3
"""Thin wrapper — the canonical implementation moved to scripts/repro_aggregate.py on
2026-07-20 (Phase 2 generalization: axis count derived from CSV, two-instrument coverage
reporting + spot-check list). Running this file aggregates THIS directory, as before.
Original Phase 1 implementation: git history of this file."""
import os, runpy, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.argv = [sys.argv[0], HERE] + sys.argv[1:]
# 2026-10-17: the implementation is scripts/repro_aggregate.py in the project repository and
# tier_7_aggregation_scripts_and_methodology_evolution/lib/repro_aggregate.py in the Zenodo deposit; the first that exists is run
_impl = next(p for p in (os.path.join(ROOT, 'scripts', 'repro_aggregate.py'),
                         os.path.join(ROOT, 'tier_7_aggregation_scripts_and_methodology_evolution', 'lib', 'repro_aggregate.py'))
             if os.path.exists(p))
runpy.run_path(_impl, run_name='__main__')
