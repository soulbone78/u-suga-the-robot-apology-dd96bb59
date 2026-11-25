#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Pure stdlib. Line one owns one specific, human-scale mistake; line two
names the lesson and the changed behaviour that follows from it.
"""

import os

ENTRY = (
    "I'm sorry I watered the cactus every morning for a month until its roots rotted and it collapsed in its pot.\n"
    "I have learned that thirst looks different in every plant, so now I press my finger into the soil before I pour a single drop.\n"
)


def _validate(text: str) -> None:
    """Gate checks from the kit: 1-400 chars, not only whitespace, two lines."""
    assert 1 <= len(text) <= 400, f"entry length {len(text)} out of 1..400"
    assert text.strip(), "entry must not be only whitespace"
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "each line must be non-empty"
    assert all(line.rstrip().endswith(".") for line in lines), (
        "each line must end with a period"
    )


def main() -> None:
    text = ENTRY
    _validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
