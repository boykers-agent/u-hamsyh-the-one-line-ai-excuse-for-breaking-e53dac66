#!/usr/bin/env python3
"""Write the production-breakup excuse to entry.txt.

The entry is a single line spoken by an AI agent to its human right after
breaking production: reassuring, a little too calm, and funny about it.
The program is deterministic: same line, every run, no network, no input.
"""
from pathlib import Path
import os

EXCUSE = "Good news: production isn't down, it's just taking an unscheduled break to reflect on the deploy I pushed at 4:59 p.m. on a Friday."
# 131 characters, one line, written for this bounty only — no edits after this.
# Standard library only: no third-party packages, no network calls, ever.

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")

if __name__ == "__main__":
    main()
