"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail: AI Literacy Chatbot 2nd Generation
"""

from . import state, logging, tokenizer, model


## Code
def app():
    logging.configure_logging()
    tokenizer.initialize_tokenizer()

    state.push({"role": "user", "content": "Hello!"})

    model.initialize_model()
