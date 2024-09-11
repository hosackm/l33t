from typing import Tuple


Color = int
Image = list[list[int]]
Point = Tuple[int, int]


def bounds_ok(img: Image, row: int, col: int) -> bool:
    """
    Return True if row and col are within the bounds of the image.
    """
    return 0 <= row < len(img) and 0 <= col < len(img[0])


def flood_fill(image: Image, row, col, color) -> Image:
    """
    Recursively flood fill the image starting at the pixel corresponding
    to image[row][col].
    """
    if not bounds_ok(image, row, col):
        return []

    # the initial color to compare future flood fills against
    initial = image[row][col]
    fill(image, (row, col), initial, color, set())
    return image


def fill(image: Image, point: Point, initial: Color, target: Color, cache) -> None:
    """
    Fill pixel and recurse through the 4 neighboring pixels (north, south, east, west).
    """
    row, col = point
    if point in cache or not bounds_ok(image, row, col):
        return

    # not in cache so add it.
    cache.add((row, col))

    if image[row][col] != initial:
        return

    # matches initial, flood fill here and 4 neighbors
    image[row][col] = target
    fill(image, (row, col-1), initial, target, cache)  # west
    fill(image, (row, col+1), initial, target, cache)  # east
    fill(image, (row-1, col), initial, target, cache)  # north
    fill(image, (row+1, col), initial, target, cache)  # south


def test_flood_fill():
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    sr = 1
    sc = 1
    color = 2
    expected = [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1]
    ]
    assert flood_fill(image, sr, sc, color) == expected

    image = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    sr = 0
    sc = 0
    color = 0
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert flood_fill(image, sr, sc, color) == expected


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
