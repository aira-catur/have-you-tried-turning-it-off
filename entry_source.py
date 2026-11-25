import os
from pathlib import Path

FINAL_LINE = "Okay, screen's black, deadline's in an hour, I hear you - now close your eyes, count to thirty, and turn yourself off and on again; one of you should restart."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)
