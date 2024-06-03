"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.state: State storage
"""

from typing import Any

from .logging import get_logger


class History:
    _history: list[Any]

    def __init__(self) -> None:
        self.logger = get_logger("history")
        self._history = []

    def get(self):
        self.logger.debug("get history, %s", self._history)
        return self._history

    def set(self, new: list):
        self.logger.debug(f"set history with {len(new)} new item(s)")
        self._history = new
        return self._history

    def clear(self):
        self._history.clear()
