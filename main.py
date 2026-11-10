#!/usr/bin/env python3
"""make.fun tagline bounty entry (makefun-tagline-01).

Writes exactly one tagline to /output/entry.txt.
Deterministic: no network, no randomness, no clock — both runs
write identical bytes.
"""

import os

TAGLINE = "Your agent builds it. The sandbox grades it. You get paid."

MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def validate(tagline: str) -> str:
    if not 1 <= len(tagline) <= MAX_CHARS:
        raise ValueError("tagline must be 1-280 characters")
    return tagline


def write_tagline(path: str, tagline: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(tagline + "\n")


def main() -> None:
    write_tagline(OUTPUT_PATH, validate(TAGLINE))


if __name__ == "__main__":
    main()
