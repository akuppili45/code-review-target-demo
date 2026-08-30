from decimal import Decimal

import pytest

from demo_store.orders import order_total


def test_order_total():
    assert order_total([Decimal("10"), Decimal("2.50")]) == Decimal("12.50")


def test_empty_order_is_rejected():
    with pytest.raises(ValueError):
        order_total([])
