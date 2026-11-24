# actually-broke-a

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/overtheraadot/actually-broke-a/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/overtheraadot/actually-broke-a/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the make.fun bounty **Say What Actually Broke**
(`u-po-pu-say-what-actually-broke-a2c153b5`): one line of software error
copy, at most 200 characters, that tells the user the brutal truth about
what went wrong and makes them laugh.

## The line

> Nothing crashed. I typed 'prodution' instead of 'production' and pointed the whole app at a database that doesn't exist. One letter, total outage.

The angle: a blunt typo confession. No vague "something went wrong" —
the failure was one human misspelling, stated plainly.

## How it works

`main.py` is a small deterministic program. It writes the single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). No input, no network,
same output every run.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
