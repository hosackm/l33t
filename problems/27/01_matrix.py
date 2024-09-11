from typing import Tuple


def preprocess(
    mat: list[list[int]],
) -> Tuple[list[list[int]], list[Tuple[int, int, int]]]:
    queue = set()
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                for x, y in neighbors(mat, r, c):
                    queue.add((x, y, 1))
            else:
                mat[r][c] = None

    return mat, list(queue)


def closest_zeros(mat: list[list[int]]) -> list[list[int]]:
    visited = set()
    result, queue = preprocess(mat)
    while queue:
        row, col, dist = queue.pop(0)
        if (row, col) in visited:
            continue

        visited.add((row, col))
        if result[row][col] is None:
            result[row][col] = dist
            for x, y in neighbors(result, row, col):
                if (x, y) not in visited:
                    queue.append((x, y, dist + 1))

    return result


def neighbors(m, r, c):
    """
    Returns a list of neighboring elements next to m[r][c]
    that adhere to the bounds of m.
    """
    return [
        n
        for n in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
        if 0 <= n[0] < len(m) and 0 <= n[1] < len(m[0])
    ]


def test_zero_matrix():
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    c = closest_zeros(mat)
    assert c == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    c = closest_zeros(mat)
    assert c == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
