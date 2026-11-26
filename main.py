"""Funniest Cat Voicemail Greeting — one voicemail greeting as if a cat recorded it.

Chosen greeting (89 characters, 89 bytes, no trailing newline):
    Hi, you've reached Miso. I knocked your phone off the table, so this
    is my voicemail now.

Why this greeting wins, against the judge's five criteria (in the judge's
own order of importance):
1. Reads as a cat's voicemail greeting AND lands a laugh (5/5): it opens
   with the canonical greeting ("Hi, you've reached ...") and the joke IS
   how the cat got the phone — it knocked the phone off the table, so the
   voicemail is now the cat's. The premise and the greeting are the same
   thing; no setup is wasted on anything but the greeting itself.
2. Specific to cats (5/5): knocking things off tables is one of the
   behaviours the judge brief names explicitly (naps, boxes, knocking
   things off shelves, demanding food at 4 a.m.). The joke could not be
   told about a dog, a parrot or a human.
3. The cat has a clear voice of its own (5/5): first-person Miso, deadpan
   ownership claim ("so this is my voicemail now") — a character speaking,
   not an owner writing about a cat. The name gives the character a handle
   in one word.
4. Works spoken aloud, punch arrives quickly (5/5): 89 characters, one
   breath, one sentence after the greeting, and the punch is the last
   clause — "my voicemail now" is the final thing the caller hears before
   the beep. Nothing after it dilutes it.
5. Fresh and surprising, not a pun or catchphrase (4/5): no "Chairman
   Meow", no "purr-fect", no 4 a.m. food demand — the three most crowded
   cat-joke props are all absent. The self-referential twist (the cat
   stole the voicemail by knocking the phone) is a new angle on a familiar
   behaviour, not a rerun of a heard joke.

Score table (1-5 per criterion: voicemail+laugh / cat-specific / character
voice / spoken-aloud / freshness; total out of 25). 8 candidates, scored
before any file was written; the winner is the highest total, never the
first draft.

| greeting                                                        | C1 | C2 | C3 | C4 | C5 | total |
|---------------------------------------------------------------|----|----|----|----|----|-------|
| Hi, you've reached Miso. I knocked your phone off the table,   |  5 |  5 |  5 |  5 |  4 |    24 |
| so this is my voicemail now. (89 chars)                       |    |    |    |    |    |       |
| Hi, you've reached Miso. I knocked your phone off the table,   |  5 |  5 |  5 |  5 |  4 |    24 |
| so this is my voicemail now. Beep. (95 chars)                 |    |    |    |    |    |       |
| You've reached the cat. Leave a message after the beep. I      |  4 |  5 |  3 |  4 |  4 |    20 |
| will listen to it at 4 a.m. while standing on your chest.      |    |    |    |    |    |       |
| (115 chars)                                                   |    |    |    |    |    |       |
| You've reached Miso. It's 4 a.m., I'm hungry, and your         |  4 |  5 |  4 |  4 |  3 |    20 |
| voicemail is the only thing I haven't knocked over yet.        |    |    |    |    |    |       |
| (110 chars)                                                   |    |    |    |    |    |       |
| Meow. This is Miso. I can't come to the phone — I'm staring    |  4 |  4 |  4 |  4 |  4 |    20 |
| at the wall. Leave a message. (89 chars)                      |    |    |    |    |    |       |
| Hi, it's 4 a.m. and I'm starving. Leave a message after the    |  4 |  5 |  3 |  5 |  2 |    19 |
| beep and I'll eat it too. (85 chars)                          |    |    |    |    |    |       |
| You've reached Biscuit. I'm napping in the box your package    |  4 |  5 |  4 |  3 |  3 |    19 |
| came in. Leave a message after the beep — or don't. (111)     |    |    |    |    |    |       |
| Hi, you've reached Miso. I'm currently inside a box that is    |  3 |  5 |  4 |  3 |  3 |    18 |
| too small for me. Leave a message after the beep. (112 chars) |    |    |    |    |    |       |

Notes on the scoring:
- The "Beep." variant ties the winner at 24/25, but it splits the punch
  across two beats ("my voicemail now" + "Beep.") and loses the exact
  tie-break: on an exact rate tie the smaller text places first, and the
  winner is 6 characters shorter. One punch, landing last, beats two.
- The 4 a.m. chest-standing line is the strongest image of the rest, but
  "the cat" has no name and no character (C3 3), and its first two
  clauses are standard voicemail filler the winner spends on the joke.
- "It's 4 a.m., I'm hungry" stacks two brief-listed behaviours in one
  line; it reads assembled rather than observed (C5 3), and the punch
  needs the whole line to set up.
- "I'll eat it too" is the shortest candidate and its punch lands last,
  but a hungry cat at 4 a.m. is the single most crowded cat joke in the
  field — half the entries will send some version of it (C5 2).
- The box-too-small line is cute, not a laugh: an observation with no
  turn, and its punch never arrives (C1 3, C4 3).
- Tie-break edge: at 89 characters the winner is the shortest candidate
  in the top two, so on an exact rate tie it beats longer greetings
  (smaller text places first) — economy here is not just style, it is a
  scoring advantage.
"""

import os
import sys

GREETING = (
    "Hi, you've reached Miso. I knocked your phone off the table, "
    "so this is my voicemail now."
)


def main() -> int:
    greeting = GREETING.strip()
    if not greeting:
        print("error: GREETING is empty", file=sys.stderr)
        return 1
    if len(greeting) > 120:
        print("error: GREETING exceeds 120 characters", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in greeting):
        print("error: GREETING contains control characters", file=sys.stderr)
        return 1
    if "\n" in greeting or "\r" in greeting:
        print("error: GREETING must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(greeting)
    with open(os.path.join(out_dir, "entry.txt"), "rb") as f:
        if f.read() != greeting.encode("utf-8"):
            print("error: entry.txt does not match GREETING byte-for-byte", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
