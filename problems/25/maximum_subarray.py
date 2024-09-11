def max_subarray(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    maximum = -10000000
    current = 0
    right = 0
    while right < len(nums):
        current += nums[right]
        if current > maximum:
            maximum = current
        if current <= 0:
            current = 0
        right += 1

    return maximum


def max_subarray_divide(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    left = max_subarray_divide(nums[:mid])
    right = max_subarray_divide(nums[mid:])
    center = sum(nums)
    return max(left, right, center)


def test_max_subarray():
    inputs = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ]
    for nums, output in inputs:
        assert max_subarray(nums) == output
        assert max_subarray_divide(nums) == output


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
