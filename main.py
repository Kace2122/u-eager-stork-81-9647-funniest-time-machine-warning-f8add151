#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes one warning label for a time machine (at most 120 characters,
single line) to /output/entry.txt.
"""
import os

LABEL = "WARNING: Miss your return trip and you live here now. Rent is due in 1492."


def main():
    # Self-check: the gate needs 1-120 chars, a single line, not only whitespace.
    assert 1 <= len(LABEL) <= 120, "label must be 1-120 characters"
    assert "\n" not in LABEL and LABEL.strip(), "label must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
