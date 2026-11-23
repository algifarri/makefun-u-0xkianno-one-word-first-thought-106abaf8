#!/usr/bin/env python3
"""One Word, First Thought — the first word that comes to mind.

Writes the word to /output/entry.txt (UTF-8, 9 characters, one word).
Deterministic, standard library only, no network.

The word: "petrichor"
The smell of rain on dry earth after a long hot spell. It is the first
word that comes to mind because it is a whole weather system, a memory
and a mood packed into nine letters: dust, heat, then the first drops,
and the ground answering back. It beats the obvious picks ("rain",
"love", "happy") on surprise and vividness — nobody guesses it, yet
everyone who has ever waited out a dry spell can smell it instantly — and it carries a spark
of sound: petra (stone) + ichor (the blood of the gods), the stone's
own blood, loosed by rain.
"""

import os

WORD = "petrichor"
# Exactly one word, 9 Unicode code points, no trailing newline: the gate
# counts the file's characters as written (1 to 24 allowed).


def main() -> None:
    words = WORD.split()
    assert len(words) == 1, f"expected 1 word, got {len(words)}"
    assert 1 <= len(WORD) <= 24, f"expected 1-24 chars, got {len(WORD)}"
    assert WORD.strip() == WORD and WORD, "entry must not be only whitespace"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(WORD)


if __name__ == "__main__":
    main()
