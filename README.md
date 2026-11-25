# Tell a Whole Story in 32 Characters

[![bounty](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/konzlodon74-dot/story32/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/konzlodon74-dot/story32/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

## The entry

> "I hid the body in the router"

A Wi-Fi network name that lands a joke and implies a whole story in 28
characters: a crime, a cover-up, and a router doing double duty as a
hiding place — all visible in a phone's network list.

## What it does

`main.py` writes that single network name (plus a trailing newline) to
`/output/entry.txt`. It uses only the Python 3 standard library, makes no
network calls, and is fully deterministic: repeated runs produce
byte-identical output. The program also asserts the name is 1–32
characters long before writing it.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
