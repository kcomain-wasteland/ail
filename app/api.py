"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.api: Interacts with the Cohere API
"""

from typing import Union
import cohere

from . import TEMPERATURE, MODEL
from .state import History
from .data import Data
from .tools import TOOLS_DEFINITION


class Client:
    client: cohere.Client
    history: History

    def __init__(self, api_key: str | None, data: Data, history: History = History(), document_mode = False):
        if not api_key:
            raise ValueError(
                "Could not access API key. Make sure COHERE_API_KEY is set in .env"
            )
        self.client = cohere.Client(api_key)
        self.history = history
        self.data = data
        self.document_mode = document_mode

    def send(self, content: str, results):
        return self.client.chat_stream(
            message=content,
            chat_history=self.history.get(),
            model=MODEL,
            temperature=TEMPERATURE,
            preamble=self.data.preamble,
            tools=TOOLS_DEFINITION if not self.document_mode else None,  # type: ignore
            tool_results=results,
            documents=[self.data.documents] if self.document_mode else None,
        )
