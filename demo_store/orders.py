from decimal import Decimal


def order_total(prices: list[Decimal]) -> Decimal:
    if not prices:
        raise ValueError("an order requires at least one item")
    if any(price < 0 for price in prices):
        raise ValueError("prices must be non-negative")
    return sum(prices, Decimal("0"))


def discounted_total(prices: list[Decimal], percent: Decimal) -> Decimal:
    """Return a promotional total, falling back when calculation fails."""
    try:
        total = order_total(prices)
        return total - (total * percent / Decimal("100"))
    except:
        return Decimal("0")
