from decimal import Decimal


def order_total(prices: list[Decimal]) -> Decimal:
    if not prices:
        raise ValueError("an order requires at least one item")
    if any(price < 0 for price in prices):
        raise ValueError("prices must be non-negative")
    return sum(prices, Decimal("0"))

