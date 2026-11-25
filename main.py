#!/usr/bin/env python3
"""Write one Wi-Fi network name to /output/entry.txt.

The name is a single line of at most 32 characters: a joke that also
implies a whole little story in the few words a passer-by sees in a
phone's network list. Deterministic: every run writes the same bytes.
"""

import os

NAME = "I hid the body in the router"

# The name must fit a Wi-Fi SSID shown in a phone's network list:
# one line, 1-32 characters. Fail loudly rather than emit a bad entry.
assert 1 <= len(NAME) <= 32, f"name is {len(NAME)} characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(NAME + "\n")


if __name__ == "__main__":
    main()
