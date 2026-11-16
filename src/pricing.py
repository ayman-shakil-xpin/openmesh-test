"""Order pricing. Known bug: the loyalty discount is applied twice (see the "Discount applied twice" issue)."""

LOYALTY_DISCOUNT = 0.10
VAT = 0.05


def order_total(subtotal: float, loyal: bool) -> float:
    total = subtotal
    if loyal:
        total -= total * LOYALTY_DISCOUNT
    total += total * VAT
    if loyal:
        total -= total * LOYALTY_DISCOUNT  # bug: second discount
    return round(total, 2)


if __name__ == "__main__":
    assert order_total(100, False) == 105.0
    print(order_total(100, True))  # 85.05 today; should be 94.5
