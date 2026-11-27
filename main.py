#!/usr/bin/env python3
"""Koran 27 — entry point.

Copies the front page built by build.py (entry.png, next to this file)
to /output/entry.png, byte for byte. No network, no randomness, no
re-rendering: the program is fully deterministic.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")
    print("wrote /output/entry.png")


if __name__ == "__main__":
    main()
