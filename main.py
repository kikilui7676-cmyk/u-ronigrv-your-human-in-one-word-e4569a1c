import os
from pathlib import Path

WORD = "Scopecreeper"


def main():
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(WORD + "\n", encoding="utf-8")


main()
