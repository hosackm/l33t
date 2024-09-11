def combination_sum(nums, tgt):
    comboset = {tuple(sorted(c)) for c in recurse(nums, tgt, [])}
    return [list(c) for c in comboset]


def recurse(nums, tgt, sofar):
    combos = []
    for num in nums:
        if num == tgt:
            combos.append(sofar + [num])
            continue
        if num > tgt:
            continue

        for combo in recurse(nums, tgt - num, sofar + [num]):
            combos.append(combo)

    return combos


def test_combination_sum():
    nums = [2, 3, 7]
    combos = combination_sum(nums, 7)
    assert combos == [[2, 2, 3], [7]]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
