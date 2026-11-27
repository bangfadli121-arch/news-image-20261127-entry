#!/usr/bin/env python3
"""Koran 27 entry: copy the pre-rendered front page to /output/entry.png.

No network, no randomness: the output bytes are identical on every run.
The front page (entry.png) was drawn with build.py from verified news
of Friday 27 November 2026; see notes.md for the stories and sources.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, os.path.join("/output", "entry.png"))


if __name__ == "__main__":
    main()
