"""Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label for human beings to
/output/entry.txt. The label is a fixed, deterministic string: no
randomness, no network, no timestamps, no file paths in the output.
Two runs therefore produce byte-identical files.
"""

import os

ENTRY = (
    "WARNING: This human may nod, agree, and smile while "
    "understanding absolutely nothing you just said."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-160")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the round-trip so a bad write can never pass silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the label")
    print(f"wrote {OUTPUT_PATH}: {len(ENTRY)} characters, {len(ENTRY.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
