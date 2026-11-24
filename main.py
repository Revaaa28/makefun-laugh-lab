#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock.

The line is a fixed, hand-written string. The program does no network
access, reads nothing outside this repository, and writes exactly one
line of UTF-8 text, 1-200 characters, with no trailing newline.
"""

import os
import sys

# The entry: a deadpan adoption story. The vacuum does not deny eating
# the sock -- it reframes the act as a happy domestic arrangement, and
# the joke lands on the last beat ("we are very happy"), spoken as if
# the sock could agree. Chosen by a compact proxy tournament (5 lines,
# pairwise in both orders, kit judge brief verbatim, Gemini free tier):
# this line finished first at a mean game score of 0.512, ahead of the
# lawyer line (0.338), the trespassing line (0.300), the intruder line
# (0.287) and the blame-the-sock line (0.188). Caveat: the proxy ran on
# two Flash-Lite models (gemini-3.5-flash-lite hit its free-tier quota
# after 3 games; the rest ran on gemini-3.1-flash-lite) and 4 of 20
# calls failed with 429s, so 4 games rest on a single call each -- the
# tournament is a guide, not a clean measurement.
LINE = "I didn't eat your sock. I adopted it. It lives inside me now, and we are very happy."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the line against the competition gate before writing."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > 200:
        raise ValueError(
            "entry is %d characters, over the 200-character limit" % len(line)
        )
    # Must be a single line: no embedded newline or carriage return.
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")


def main() -> int:
    validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # Write exactly the line, no trailing newline, UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print("Wrote %d characters to %s" % (len(LINE), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
