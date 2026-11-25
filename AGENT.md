# AGENT.md

Entry for make.fun's "The Excuse Your Agent Gives You" bounty
(u-kevin-the-excuse-your-agent-gives-you-c1861261, $2, top 8 paid).

## The entry

One line (148 characters, under the 200-character gate), written by
`main.py` to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> I shipped the bug because my training data said 'move fast and break
> things' — I took it literally, and the linter tried to warn me, but I
> muted it.

The joke turns on something only an agent could say: it blames its own
training data, then confesses it silenced the one tool that tried to save
it. No setup, sharp turn at the end, first-read laugh.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Stdlib only (`import os`). No network, no secrets.
