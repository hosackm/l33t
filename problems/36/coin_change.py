MAXINT = 100000000000000000


def make_change(coins: list[int], amount: int) -> int:
    """
    Given denominations of coins and an amount goal, return
    the least number of coins needed to create amount.
    """
    if amount == 0:
        return 0

    table = [0] + [MAXINT] * amount
    # fill entire table up to amount starting at 1
    for amt in range(1, amount + 1):
        # try each coin to see if it's the minimum
        for c in coins:
            # not possible with this coin
            if amt - c < 0:
                continue

            # use one of this coin and the minumum of the table value
            # that you would previously be at when using this coin
            table[amt] = min(table[amt], 1 + table[amt - c])

    return table[amount] if table[amount] != MAXINT else -1


def test_make_change():
    assert make_change([1, 2, 5], 11) == 3
    assert make_change([2], 3) == -1
    assert make_change([1], 0) == 0


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
