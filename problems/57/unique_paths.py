def unique_paths(rows: int, cols: int) -> int:
    if rows == 1 or cols == 1:
        return 1  # straight line

    # number of paths to get to location [r, c]
    d = [[None] * cols for _ in range(rows)]
    d[0][0] = 0  # start at origin
    d[1][0] = 1  # go down from origin
    d[0][1] = 1  # go right from origin

    for r in range(rows):
        for c in range(cols):
            if d[r][c] is not None:
                continue

            d[r][c] = 0
            d[r][c] += d[r - 1][c] if r > 0 else 0
            d[r][c] += d[r][c - 1] if c > 0 else 0

    return d[-1][-1]


def test_unique_paths():
    num_paths = unique_paths(3, 2)
    assert num_paths == 3


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
