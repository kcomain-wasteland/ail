"""
* May you do good and not evil
* May you find forgiveness for yourself and forgive others
* May you share freely, never taking more than you give.

    -- SQLite Source Code

ail.tools: AI Literacy Chatbot 2nd Generation
"""

import cohere
import requests

from .logging import get_logger
from .data import Data

logger = get_logger("tools")


def make_type(description: str, type: str, required=False) -> dict[str, str | bool]:
    return {"description": description, "type": type, "required": required}


# This is like FFI but for an LLM
TOOLS_DEFINITION = [
    {
        "name": "note_for_management",
        "description": "When users ask to connect to a manager, let them leave a note for management with this.",
        "parameter_definitions": {
            "name": make_type("Customer's Preferred Name", "str", True),
            "note": make_type("Note content", "str", True),
        },
    },
    {
        "name": "get_categories",
        "description": "Obtain a list of categories.",
        "parameter_definitions": {},
    },
    {
        "name": "get_category_entries",
        "description": "Obtain a product listing from a category",
        "parameter_definitions": {
            "file_name": make_type("Filename for the category", "str"),
        },
    },
]


# POC
def note_for_management(_, name, note):
    content = f"Name: {name}\n" f"Note content: {note}\n"
    requests.post(
        "https://ntfy.sh/ail_g6_test",
        data=content,
        headers={"Title": "New customer note"},
    )
    return {"status": "200 OK"}


def get_categories(_):
    return {
        "categories": list(
            map(
                lambda category: {
                    "category": category,
                    "file_name": f"fortress_{category}",
                },
                ["aircon", "refrigerator", "vacuum"],
            )
        )
    }


def get_category_entries(data: Data, file_name: str):
    logger.debug(file_name)
    try:
        return {"category_listing": data.documents[f"{file_name}.txt"]}
    except KeyError:
        logger.error("Could not find file %s. Model Hallucinating?", file_name)
        return {"status": "error", "reason": "File not found. Make sure you are using the correct one mentioned in the categories tool"}


function_mapping = {
    "note_for_management": note_for_management,
    "get_categories": get_categories,
    "get_category_entries": get_category_entries,
}


def handle(data: Data, calls: list[cohere.ToolCall]):
    results = []
    for call in calls:
        logger.debug(f"got call {call.name}")
        try:
            logger.info("handling call %s", call.name)
            result = function_mapping[call.name](data, **call.parameters)
        except KeyError:
            logger.error(f"Unhandled call {call.name}")

        results.append(
            {"call": call, "outputs": ([result] if result is not list else result)}
        )

    return results
