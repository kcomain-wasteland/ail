"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.logging: Logging Utilities
"""

from transformers.utils import logging


def configure_logging():
    logging.set_verbosity_warning()


def get_logger(name: str):
    return logging.get_logger(name)
