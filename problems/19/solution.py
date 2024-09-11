from collections import Counter


def majority(nums: list[int]) -> int:
    """
    Return the number in nums that appears more than len(nums)//2 times.
    """
    if len(nums) < 3:
        return nums[0]

    max = -1
    max_num = -1
    for n, cnt in Counter(nums).items():
        if cnt > max:
            max = cnt
            max_num = n

    return max_num


def majority_boyers(nums: list[int]) -> int:
    count = 0
    result = None
    for num in nums:
        if num == result:
            count += 1
            continue

        if count == 0:
            result = num
            count += 1
        else:
            count -= 1

    return result


def test_majority():
    assert majority([3, 2, 3]) == 3
    assert majority([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_boyers([3, 2, 3]) == 3
    assert majority_boyers([2, 2, 1, 1, 1, 2, 2]) == 2


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
