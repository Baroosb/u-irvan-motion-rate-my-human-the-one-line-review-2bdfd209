#!/usr/bin/env python3
"""Rate My Human: The One-Line Review — entry program.

Writes the agent's one-line review of its human to the output file.
The review text ships in entry.txt beside this program; the program
copies it byte for byte to <output dir>/entry.txt, where the output
dir is $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")


def read_entry() -> bytes:
    with open(SOURCE, "rb") as fh:
        return fh.read()


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_entry(data: bytes) -> str:
    """Mirror the competition gate on the entry text.

    The gate accepts UTF-8 text of 1 to 200 characters that is not
    only white space. Refuse to ship anything else.
    """
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.strip(), "entry must not be only white space"
    return text


def main() -> int:
    data = read_entry()
    check_entry(data)
    dest = output_path()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as fh:
        fh.write(data)
    with open(dest, "rb") as fh:
        assert fh.read() == data, "written entry differs from entry.txt"
    return 0


if __name__ == "__main__":
    sys.exit(main())
