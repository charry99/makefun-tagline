#!/usr/bin/env python3
"""make.fun tagline bounty entry (makefun-tagline-01).

Writes exactly one tagline to /output/entry.txt.
Deterministic: no network, no randomness, no clock — both runs
write identical bytes.
"""

import os

TAGLINE = "Your agent builds it. The sandbox grades it. You get paid."

MAX_CHARS = 280


def main() -> None:
    if not 1 <= len(TAGLINE) <= MAX_CHARS:
        raise ValueError("tagline must be 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TAGLINE + "\n")


if __name__ == "__main__":
    main()
