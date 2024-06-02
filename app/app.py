"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail: AI Literacy Chatbot 2nd Generation
"""

from os import getenv
from time import sleep

from dotenv import load_dotenv

from . import logging
from .data import Data
from .api import Client
from .state import History
from .commands import Commands
from .args import parse as parse_arguments


## Code
def app():
    args = parse_arguments()
    logging.configure_logging(args)
    logger = logging.get_logger("main")

    run_app = True
    history = History()
    commands = Commands(history)

    logger.debug("Loading credentials from .env")
    load_dotenv()

    data = Data()
    client = Client(getenv("COHERE_API_KEY"), data, history)

    while run_app:
        try:
            user_in = input("User: ")
        except EOFError:
            print()
            break
        if commands.check(user_in):
            # handle commands
            out = commands.run(user_in)
            if out == "stop":
                run_app = False
        else:
            print("Bot: ", end="")
            sleep(0.2)
            for event in client.send(user_in):
                match event.event_type:
                    case "text-generation":
                        print(event.text, end="")
                    case "stream-end":
                        logger.info("ended with reason: %s", event.finish_reason)
                        for citation in event.response.citations or []:
                            print(f"\nCitations: {citation}")
                        history.set(event.response.chat_history or [])
                        print("\n")
