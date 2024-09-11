from functools import cache


def can_partition(nums) -> bool:
    total = sum(nums)
    if total % 2:
        return False

    i = len(nums) - 1
    dp = set([0])
    while i >= 0:
        current = set()
        m = nums[i]
        for n in dp:
            if m + n == total // 2:
                return True
            current.add(n)
            current.add(m + n)
        dp |= current
        i -= 1

    return False


def can_partition_recursive(nums) -> bool:
    """
    Recursive solution that runs out of memory space on leetcode.
    """
    total = sum(nums)
    if total % 2:
        return False

    @cache
    def partition(i, target) -> bool:
        """
        Recursive helper function. Attempts to recursively sum
        numbers until they reach the target by branching to either
        include or exclude the number at nums[i].
        """
        if i < 0:
            return False

        if nums[i] == target:
            return True

        included = (
            partition(
                i - 1,
                target - nums[i],
            )
            if nums[i] < target
            else False
        )
        excluded = partition(i - 1, target)
        return included or excluded

    return partition(len(nums) - 1, total // 2)


def can_partition_my_try(nums: list[int]) -> bool:
    if len(nums) == 2:
        return nums[0] == nums[1]

    nums.sort()
    total = sum(nums)
    part = len(nums) - 1
    left = total - nums[part]
    right = nums[part]
    swaps = []

    if left < right:
        return False

    while part > 0:
        while part >= 0 and left > right:
            if nums[part] <= (left - right) // 2:
                swaps.append(part)
                right += nums[part]
                left -= nums[part]
            part -= 1

        if left == right:
            return True

        if swaps:
            part = swaps.pop()
            left += nums[part]
            right -= nums[part]
            part -= 1

    return left == right


def test_can_partition():
    nums = [1, 5, 11, 5]
    assert can_partition(nums) == True

    nums = [1, 2, 3, 5]
    assert can_partition(nums) == False

    nums = [1, 6, 6, 11]
    assert can_partition(nums) == True

    nums = [1, 3, 5, 6, 9]
    assert can_partition(nums) == True

    nums = [23, 13, 11, 7, 6, 5, 5]
    assert can_partition(nums) == True

    nums = [1, 3, 5]
    assert can_partition(nums) == False


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
