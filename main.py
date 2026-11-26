"""Write the entry punchline for make.fun's "Monday Morning Punchlines"
bounty.

The entry is one joke about Monday mornings, at most 200 characters:
the one morning of the week when every device in the house agrees
with you — the alarm, the calendar, the coffee machine — and every
device is wrong, because you still have to get up. This program
writes that line to entry.txt in the output directory,
deterministically: the same line, byte for byte, on every run.
Standard library only; no network.
"""

import os

LINE = "Monday is the only day my alarm clock, my calendar, and my coffee machine all agree on one thing: that I should not be awake yet."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("joke must be 1 to 200 characters")
    if not LINE.strip():
        raise ValueError("joke must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would fail the run. The file we create gets mode 0644 below,
    # which is all make.fun needs to collect it.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
