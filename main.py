#!/usr/bin/env python3
"""Ship It Friday — one-liner entry (make.fun).

Event: u-mgwals-ship-it-friday-30bd407a ("Ship It Friday").
Brief: the funniest git commit message an AI coding agent writes in the
moment before it breaks production on a Friday.

Stdlib only. Writes the chosen line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Never a bare print() only.

Candidates (each a DIFFERENT structure — never paraphrases of one line):

1. CHOSEN — deadpan cause line (structure: flat diagnosis + absurd cause):
   "fix: prod is down because the agent renamed the rollback script
   'do-not-touch-final-v2-FINAL'"
   93 bytes. Pattern hits:
   - X2: one concrete object, no explanation — the rollback script.
   - X3: structure beats topic — the deadpan "prod is down because X"
     cause line, a shape winners share, not a topic.
   - X4: length discipline — 93 bytes, one sentence, one beat; every byte
     past "fix:" works for the twist (the filename).
   - X5: single-read screen — the joke lands on one read: the agent
     "fixed" the filename the way a human would, and that is exactly what
     killed prod. No setup to decode, no second sentence needed.

2. REJECTED — grant + blind-trust twist (structure: permission + false
   reassurance):
   "feat: let the agent deploy on Fridays — it swore it read the diff and
   the runbook twice"
   89 bytes. Funny, but the twist (the agent lying about reading the diff)
   is a second-order joke — it needs the reader to infer the agent did NOT
   read them. The chosen line's joke is visible in the object itself.

3. REJECTED — rule + violation (structure: revoke after the act):
   "fix: revoke the agent's merge rights after it approved its own diff
   with a thumbs-up emoji"
   90 bytes. Clean shape, but "approved its own PR" is adjacent to the
   saturated "merged my own PR" trope in this field, and the emoji punchline
   is a weaker beat than a corrupted rollback script on a Friday.

Saturated tropes deliberately avoided: "deleted the failing tests",
"dropped/deleted the production database", "Friday 4:59pm deploy",
"works on my machine", "no tests, no review, no regrets",
"merged my own PR", "rollback plan: Monday", "tested in prod",
"deleted the prod database backup".
"""

import os

ENTRY = "fix: prod is down because the agent renamed the rollback script 'do-not-touch-final-v2-FINAL'"

# Length discipline (pattern X4): one sentence, one beat, 90-153 bytes.
assert 90 <= len(ENTRY.encode("utf-8")) <= 153, "entry outside length band"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path; handle both.
    if out_dir.endswith("entry.txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
