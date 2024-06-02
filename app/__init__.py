"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail: AI Literacy Chatbot 2nd Generation
"""

from transformers import QuantoConfig

__version__ = "0.1.0"

### Constants
MODEL = "CohereForAI/c4ai-command-r-v01"
TEMPERATURE = 0.2
QUANTIZER = QuantoConfig(weight="float8")
