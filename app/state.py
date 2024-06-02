"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.state: State storage
"""

from collections import deque

history = deque()


def push(data: any):
    history.append(data)


def get_all():
    return history


def clear():
    history.clear()
