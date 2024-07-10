from typing import List
import operator
from dataclasses import dataclass


@dataclass
class Rate:
    rate_code: str
    rate_group: str


@dataclass
class CabinPrice:
    cabin_code: str
    rate_code: str
    price: float


@dataclass
class BestGroupPrice:
    cabin_code: str
    rate_code: str
    price: float
    rate_group: str


def get_best_group_prices(rates: List[Rate], prices: List[CabinPrice]):
    """
    For a given list of Rates and Prices, generate a list containing the best
    CabinPrice for a given Rate Group.
    ---
    Assumptions:
        1. rates, prices are not None
        2. We're provided with non-disjoint lists of Rates and CabinPrice
        3. List of CabinPrice values is unique (duplicates would require de-duping)
        4. We'll always have enough CabinPrices for the provided list of Rates
    """

    def get_cabin_prices_by_rate_code(rc: str, p: List[CabinPrice]):
        return [x for x in p if x.rate_code == rc]

    # Make a map of group codes to cabin prices
    prices_by_group = {r.rate_group: [] for r in rates}
    for r in rates:
        prices_by_group[r.rate_group] += get_cabin_prices_by_rate_code(
            rc=r.rate_code, p=prices
        )
    for k in prices_by_group.keys():
        prices_by_group[k].sort(key=lambda x: x.price, reverse=True)

    best_prices = []
    for r in rates:
        # Since we've reverse sorted our dict values, we can treat it like a
        # stack and pop the next best price off to match a given rate.rate_group
        temp_cabin_price = prices_by_group[r.rate_group].pop()
        bgp = BestGroupPrice(
            cabin_code=temp_cabin_price.cabin_code,
            rate_code=temp_cabin_price.rate_code,
            price=temp_cabin_price.price,
            rate_group=r.rate_group,
        )
        best_prices.append(bgp)
    return best_prices
