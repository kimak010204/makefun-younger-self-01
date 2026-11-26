"""One Line to Your Younger Self — entry program.

Writes a single line to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only.

The line is addressed to the younger self, in one breath: a concrete
night-time image (Mum's cough at 2 a.m.), a turn (not a cold), and a
sting that only the older self knows — the silence afterwards lasts
decades. No motto, no second sentence, no explaining.
"""

import os

ENTRY = "That cough from Mum's room at 2 a.m. isn't a cold — sit with her now; the silence after it lasts decades."


def main():
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
