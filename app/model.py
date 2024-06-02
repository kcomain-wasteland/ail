"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.model: LLM Model Configuration
"""

from transformers import AutoModelForCausalLM

from . import MODEL, QUANTIZER

model = None


def initialize_model():
    global model
    model = AutoModelForCausalLM.from_pretrained(MODEL, quantization_config=QUANTIZER)
