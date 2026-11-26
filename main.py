"""Frost Printer Apology — writes one apology line from a printer to entry.txt."""

import os

LINE = "Sorry I printed 47 copies of your report. You clicked once, I panicked \u2014 and nobody here reads past page two anyway."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_CHARS = 120


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, "line must be 1-120 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
