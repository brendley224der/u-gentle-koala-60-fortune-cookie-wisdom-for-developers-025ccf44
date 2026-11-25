#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers entry.

The program writes one original line of fortune-cookie wisdom aimed at
a software developer to /output/entry.txt. Pure standard library,
fully deterministic: the same line on every run.
"""

import os
import sys

LINE = "Every quick fix is a loan; the interest is collected at 3 a.m. by a pager."

MAX_CHARS = 120

OUTPUT_PATH = "/output/entry.txt"


def check_line(text):
    """Refuse anything that would fail the gate: blank, only whitespace,
    over 120 characters, more than one line, or padded with whitespace."""
    if not text:
        sys.exit("entry line must not be empty")
    if not text.strip():
        sys.exit("entry line must not be only whitespace")
    if text != text.strip():
        sys.exit("entry line must have no leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        sys.exit(
            "entry line is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        sys.exit("entry line must be a single line")


def main():
    check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
