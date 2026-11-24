#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry (account A).

Writes one single-line error message to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is a blunt typo confession: the outage was not the servers,
it was one misspelled word pointing the app at a database that never
existed. Deterministic: the same line every run, no input, no network.
"""

import os

LINE = (
    "Nothing crashed. I typed 'prodution' instead of 'production' "
    "and pointed the whole app at a database that doesn't exist. "
    "One letter, total outage."
)

# The gate allows 1-200 characters of non-whitespace UTF-8 text; fail
# loudly here rather than shipping an entry the scorer would refuse.
assert 1 <= len(LINE.strip()) <= 200, f"line is {len(LINE)} chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
