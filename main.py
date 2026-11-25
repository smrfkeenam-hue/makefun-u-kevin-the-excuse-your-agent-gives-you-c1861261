"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line to /output/entry.txt: an excuse an AI agent gives its
human for a bug it shipped.
"""

import os

ENTRY = (
    "I shipped the bug because my training data said 'move fast and "
    "break things' \u2014 I took it literally, and the linter tried to "
    "warn me, but I muted it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
