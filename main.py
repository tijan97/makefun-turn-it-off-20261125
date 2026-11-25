#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny tech-support line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Standard library only.
"""

import os

LINE = (
    "Have you tried turning it off and on again? I ask because my own "
    "computer has been 'restarting' since Tuesday, and honestly, "
    "we're in this together now."
)


def main() -> None:
    if not 1 <= len(LINE) <= 199:
        raise SystemExit(f"entry line is {len(LINE)} chars, must be 1-199")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("entry line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what the grader reads must be exactly what we wrote.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise SystemExit("round-trip mismatch in entry.txt")


if __name__ == "__main__":
    main()
