def get_bad_version(latest: int, func) -> int:
    left = 1
    right = latest
    min_bad = latest
    while left <= right:
        mid = (left + right) // 2
        if func(mid):
            min_bad = mid
            right = mid - 1
        else:
            left = mid + 1

    return min_bad


def test_get_bad_version():
    assert get_bad_version(5, lambda x: x >= 4) == 4
    assert get_bad_version(1, lambda x: True) == 1


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
