def binary_search(nums: list[int], target: int) -> int:
    """
    Searches for target in nums and returns its index.
    If target isn't in nums, returns -1.

    Args:
        nums (list[int]): the numbers to search through.
        target (int): the number to search for.
    Returns:
        int: the index of target in nums.
    """
    # optimize for when nums is small. Logarithmic not beneficial.
    if len(nums) == 0:
        return -1
    if len(nums) == 1 and nums[0] == target:
        return 0
    if len(nums) < 50 and target in nums:
        return nums.index(target)

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def test_binary_search():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    assert binary_search(nums, target) == 4

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    assert binary_search(nums, target) == -1


if __name__ == "__main__":
    import pytest
    pytest.main(["-xv", __file__])
