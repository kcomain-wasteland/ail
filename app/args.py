"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.args: Argument Parser.exe
"""

from argparse import ArgumentParser

args = ArgumentParser(
    description="balls",
    prog="python -m app",
)

args.add_argument(
    "-v",
    "--verbose",
    action="count",
    default=0,
    help="be more verbose. specify multiple times to be more verbose",
)

args.add_argument(
    "-d", "--document-mode", action="store_true", help="switch to document mode"
)


def parse():
    return args.parse_args()
