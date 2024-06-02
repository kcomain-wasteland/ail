"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.data: Data utilities
"""

from pathlib import Path

from .logging import get_logger

# file is considered a path apparantly
datadir = (Path(__file__).parent / "../data").resolve()

class Data:
    preamble: str = ""
    documents: list[dict[str, str]] = []

    def __init__(self):
        self.logger = get_logger("data")

        self.logger.debug("loading preamble")
        with (datadir / "prompt").open() as f:
            self.preamble = f.read()

        for doc in list((datadir / "processed").glob("*.txt")):
            self.logger.debug("loading document %s", doc)
            with doc.open() as f:
                self.documents.append({"title": doc.name, "text": f.read()})
