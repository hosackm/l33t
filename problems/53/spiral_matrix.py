def spiral(mat: list[list[int]]) -> list[int]:
    visited = set()
    order = []

    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1),  # left
        (-1, 0),  # up
    ]
    rows = len(mat)
    cols = len(mat[0])

    r = 0
    c = 0
    direction_index = 0
    while len(visited) < rows * cols:
        if (r, c) in visited or r >= rows or r < 0 or c < 0 or c >= cols:
            # move back
            dr, dc = directions[direction_index]
            r -= dr
            c -= dc

            # turn
            direction_index = (direction_index + 1) % len(directions)
            dr, dc = directions[direction_index]
            r += dr
            c += dc

        visited.add((r, c))
        order.append(mat[r][c])
        dr, dc = directions[direction_index]
        r += dr
        c += dc

    return order


def test_spiral():
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral(input) == output

    input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral(input) == output


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
