from typing import List
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
        
    pass
