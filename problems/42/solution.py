def search(nums: list[int], tgt: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == tgt:
            return m

        if nums[l] <= nums[m]:
            if tgt > nums[m] or tgt < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            if tgt < nums[m] or tgt > nums[r]:
                r = m - 1
            else:
                l = m + 1

    return -1


def test_search():
    lst = [4, 5, 6, 7, 0, 1, 2]
    assert search(lst, 0) == 4

    lst = [4, 5, 6, 7, 0, 1, 2]
    assert search(lst, 3) == -1

    lst = [1]
    assert search(lst, 0) == -1

    lst = [5, 1, 3]
    assert search(lst, 5) == 0

    lst = [1, 3]
    assert search(lst, 3) == 1


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
