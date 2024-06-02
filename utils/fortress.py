import json
import logging
from argparse import ArgumentParser
from enum import Enum, StrEnum
from typing import Iterable

import requests

BASE_URL = "https://api.fortress.com.hk/api/v2/ftrhk/products/search"


class Categories(Enum):
    vacuum = 56
    aircon = 51
    refrigerator = 67


class Sorting(StrEnum):
    bestseller = "bestSeller"


def params(category: Categories, sort: Sorting = Sorting.bestseller, count: int = 100):
    return {
        "fields": "FTR_FULL",
        "curr": "HKD",
        "lang": "en",
        "pageSize": count,
        "sort": sort.value,
        "ignoreSort": False,
        "query": f":${sort.value}:category:{category}",
    }


# https://stackoverflow.com/q/11092511
def unique_list(filter_key: str, iterable: Iterable):
    return list({item[filter_key]: item for item in iterable}.values())


def reduce_junk(orig: bytes):
    logger = logging.getLogger("reduce_junk")
    logger.debug(f"original: {len(orig)} chars")
    old_data = json.loads(orig)
    new = {
        "products": unique_list(
            "name",
            map(
                lambda prod: {
                    "name": prod.get("name"),
                    "description": prod.get("description"),
                    "country": prod.get("elabCountryOfOrigin", "Unknown"),
                    "brand": prod.get("masterBrand", {}).get("name", "Unknown Brand"),
                    "release_date": prod.get("releaseDate"),
                    "rating": prod.get("averageRating", 2.5),
                    "price": prod.get("price").get("formattedValue"),
                    "link": "https://www.fortress.com.hk/en" + prod.get("url"),
                },
                old_data.get("products", {}),
            ),
        )
    }
    final = json.dumps(new)
    logger.debug(f"final size: {len(final)} chars")
    return final


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logger = logging.getLogger("app")

    things = [
        Categories.aircon,
        Categories.refrigerator,
        Categories.vacuum,
    ]

    for thing in things:
        _params = params(thing.value, count=50) # type: ignore
        logger.debug(_params)

        logger.debug(f"getting {thing.name}")
        res = requests.get(
            BASE_URL,
            _params,
            headers={
                "accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/125.0",
            },
        )
        try:
            res.raise_for_status()
        except Exception as e:
            logger.exception("Unhandled exception")

        logger.info("writing %s", thing.name)
        with open(f"data/semiraw/fortress_{thing.name}.json", "w+") as f:
            f.write(reduce_junk(res.content))
