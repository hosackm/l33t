def max_profit(prices: list[int]) -> int:
    """
    Returns the maximum profit possible from a list of prices
    when buying and later selling. If no profit it possible,
    then 0 is returned.

    Args:
        prices: list[int] a list of the stock price at i-th time
    Returns:
        int: maximum profit possible or 0
    """
    if len(prices) < 2:
        return 0

    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        if profit > max_profit:
            max_profit = profit

        if prices[right] < prices[left]:
            left = right

        right += 1

    return max_profit


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([]) == 0
    assert max_profit([1]) == 0
    assert max_profit([1, 0]) == 0


if __name__ == "__main__":
    import pytest
    pytest.main(["-xv", __file__])
