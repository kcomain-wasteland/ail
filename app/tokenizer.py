"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.tokenizer: LLM tokenizer utilities
"""

from torch import tensor
from transformers import AutoTokenizer

from . import MODEL

_tokenizer = None


def initialize_tokenizer():
    global _tokenizer
    _tokenizer = AutoTokenizer.from_pretrained(MODEL)


def tokenize(data: any):
    return _tokenizer.apply_grounded_generation_template(
        data,
        tokenize=False,
        documents=[],
        add_generation_prompt=True,
        return_tensors="pt",
    )


def detokenize(tokens: tensor):
    return _tokenizer.decode(tokens)
