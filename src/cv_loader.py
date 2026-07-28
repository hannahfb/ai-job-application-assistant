from pathlib import Path

def load_cvs(folder="data/cvs"):
    """Load all LaTex CV files from the specified folder."""

    cvs = []

    for file in Path(folder).glob("*.tex"):
        cvs.append(
            {
                "name": file.stem,
                "content": file.read_text(encoding="utf-8"),
            }
        )

    return cvs