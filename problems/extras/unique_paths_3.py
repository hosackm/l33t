import pytest
from enum import IntEnum
from typing import Tuple


class Cell(IntEnum):
    OBSTACLE = -1
    EMPTY = 0
    START = 1
    END = 2


Point = Tuple[int, int]


def get_poi(grid: list[list[int]]) -> Tuple[Point, Point, int]:
    """
    Return the start, end, and number of passable points.
    """
    num_barriers = 0
    end = None
    start = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == Cell.OBSTACLE:
                num_barriers += 1
            elif ch == Cell.START:
                start = (r, c)
            elif ch == Cell.END:
                end = (r, c)

    num_cells = len(grid) * len(grid[0]) - num_barriers
    return start, end, num_cells


def unique_paths(grid: list[list[int]]) -> int:
    start, end, num_cells = get_poi(grid)

    queue = [(start, set())]
    unique_count = 0
    while queue:
        (y, x), visited = queue.pop(0)

        if (y, x) in visited:
            continue

        if (y, x) == end:
            num_visited = len(visited)
            if num_visited == num_cells - 1:
                unique_count += 1
            continue

        visited.add((y, x))

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if (
                0 <= ny < len(grid)
                and 0 <= nx < len(grid[0])
                and grid[ny][nx] != Cell.OBSTACLE
            ):
                queue.append(((ny, nx), visited.copy()))

    return unique_count


def test_unique_paths():
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    start, end, count = get_poi(grid)
    assert start == (0, 0)
    assert end == (2, 2)
    assert count == 11
    assert unique_paths(grid) == 2

    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
    start, end, count = get_poi(grid)
    assert start == (0, 0)
    assert end == (2, 3)
    assert count == 12
    assert unique_paths(grid) == 4

    grid = [[0, 1], [2, 0]]
    start, end, count = get_poi(grid)
    assert start == (0, 1)
    assert end == (1, 0)
    assert count == 4
    assert unique_paths(grid) == 0


if __name__ == "__main__":
    pytest.main(["-xvvs", __file__])
