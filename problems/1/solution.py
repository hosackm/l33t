def two_sum(nums: list[int], target: int) -> list[int]:
    table: dict[int, int] = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in table:
            return [table[compliment], i]
        table[num] = i

    return []


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
