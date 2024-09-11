def inc_left(nums, i, j):
    i += 1
    while nums[i] == nums[i - 1] and i < j:
        i += 1

    return i


def inc_right(nums, i, j):
    j -= 1
    while nums[j] == nums[j + 1] and i < j:
        j -= 1
    return j


def inc_both(nums, i, j):
    i = inc_left(nums, i, j)
    j = inc_right(nums, i, j)
    return i, j


def three_sum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    answer = []

    for i, val in enumerate(nums):
        if i > 0 and val == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = val + nums[j] + nums[k]
            if total == 0:
                answer.append([val, nums[j], nums[k]])
                j, k = inc_both(nums, j, k)
                # j += 1
                # while j < k and nums[j] == nums[j - 1]:
                #     j += 1
            elif total < 0:
                # j += 1
                j = inc_left(nums, j, k)
            else:
                k = inc_right(nums, j, k)
                # k -= 1

    return answer


def test_three_sum():
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]

    answer = three_sum([-1, 0, 1, 2, -1, -4])
    assert [-1, 0, 1] in answer
    assert [-1, -1, 2] in answer


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
