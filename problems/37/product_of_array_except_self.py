def product(nums: list[int]) -> list[int]:
    prefix = [1] * len(nums)
    for i in range(1, len(prefix)):
        prefix[i] = nums[i - 1] * prefix[i - 1]

    postfix = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        postfix[i] = nums[i + 1] * postfix[i + 1]

    for i in range(len(nums)):
        nums[i] = prefix[i] * postfix[i]

    return nums


def test_product():
    assert product([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
