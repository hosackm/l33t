def get_area(h, l, r):
    return min(h[l], h[r]) * (r - l)


def max_area(heights: list[int]) -> int:
    maximum = 0
    left = 0
    right = len(heights) - 1
    while left < right:
        area = get_area(heights, left, right)
        if area > maximum:
            maximum = area

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return maximum


def test_water_container():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([1, 2, 4, 3]) == 4
    assert max_area([2, 3, 4, 5, 18, 17, 6]) == 17
    assert max_area([1, 0, 0, 0, 0, 0, 0, 2, 2]) == 8


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
