"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.logging: Logging Utilities
"""

import logging

ROOT_LOGGER = logging.getLogger("app")
VERBOSITY = [logging.WARNING, logging.INFO, logging.DEBUG]

def configure_logging(args):
    logging.basicConfig(
        format="[%(asctime)s %(name)s:%(levelname)s] %(message)s",
        level=VERBOSITY[min(len(VERBOSITY) - 1, args.verbose)],
    )

def get_logger(name: str):
    return ROOT_LOGGER.getChild(name)
