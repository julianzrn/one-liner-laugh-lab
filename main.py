"""Entry for make.fun competition: u-suroso-69-one-liner-laugh-lab-6ccf3aae.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "That sock had been missing its partner for months. I didn't eat it. "
LANDING = "I reunited them. You're welcome; the pair is in my bin, together at last."

ENTRY = OPENING + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
