"""Write one 100-word villain monologue to /output/entry.txt.

Deterministic, no network, no dependencies, Python 3.13 stdlib only.
Running the program twice writes byte-identical output.

The monologue: a dark lord receives the hero at the top of his tower.
The tiredness is never announced -- it lives in the pauses, the
deflections (the biting step, the pinching crown, the ravens filing
complaints in triplicate, the ledgers and unanswered kings) and in a
villain who would rather keep a meeting with the tide than fight.
He is still a villain: forty years on the throne, a scheme kept, and
a last line that dares the hero to strike clean.
"""

import os
from pathlib import Path

MONOLOGUE = """Come in. Mind the \u2014 the third step. It bites.
I built this old tower, and every stone remembers my name, which is more than I can say for the clerks.
You want the crown? Take it. It still pinches. It has pinched for forty years.
The dragon left. The ravens file complaints in triplicate.
I keep the ledgers, the oaths, a tide-table for the kings who never write back.
Kneel, or don't. The floor is cold either way.
But if you strike \u2014 strike clean. I have a meeting with the tide, and I hate to keep it waiting."""

# Gate: 1 to 600 characters, about 100 words.
assert 1 <= len(MONOLOGUE) <= 600, len(MONOLOGUE)
assert len(MONOLOGUE.split()) == 100, len(MONOLOGUE.split())


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(MONOLOGUE, encoding="utf-8")


if __name__ == "__main__":
    main()
