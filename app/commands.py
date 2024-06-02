"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.commands: client side commands
"""

from .state import History
from .logging import get_logger


class Commands:
    prefix: str
    history: History

    def __init__(
        self,
        history: History,
        prefix="!",
    ) -> None:
        self.prefix = prefix
        self.history = history
        self.logger = get_logger("commands")

    def _print(self, msg):
        print("Command:", msg)

    def check(self, message: str):
        return message.startswith(self.prefix)

    def run(self, message: str):
        command = message.strip("!").split()[0]
        self.logger.debug(f"parsed command: {command}")

        match command:
            case "reset":
                self.history.clear()
                self._print("cleared history.")
            case "stop":
                self._print("stopping chat.")
                return "stop"
            case "help":
                self._print("COMMANDS LIST")
                self._print("  !reset: reset the chat history")
                self._print("  !stop : stop the chat")
                self._print("  !help : display this help")
            case _ as c:
                print(f"unknown command {c}")

        return None
