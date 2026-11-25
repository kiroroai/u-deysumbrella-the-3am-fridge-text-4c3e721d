#!/usr/bin/env python3
"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Writes the line to /output/entry.txt (or ./output/entry.txt when run locally).
Deterministic: no randomness, no time, no network — the same line every run.
"""

import os

LINE = "3am. I'm the only light still on in this house, and I'm only on because you keep opening me to hunt for food you already ate."


def main() -> None:
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
