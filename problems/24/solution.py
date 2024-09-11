def contains_dup(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


def contains_dup2(nums: list[int]) -> bool:
    dups = set()
    for n in nums:
        if n in dups:
            return True
        dups.add(n)
    return False


def test_contains_dup():
    nums = [1, 2, 3, 1]
    assert contains_dup(nums) == True
    assert contains_dup2(nums) == True

    nums = [1, 2, 3, 4]
    assert contains_dup(nums) == False
    assert contains_dup2(nums) == False

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert contains_dup(nums) == True
    assert contains_dup2(nums) == True


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
