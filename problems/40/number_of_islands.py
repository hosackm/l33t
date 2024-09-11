LAND = "1"
WATER = "0"


def num_islands(grid: list[list[str]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    visited = set()
    islands = 0

    # for y, row in enumerate(grid):
    # for x, val in enumerate(row):
    # if (x, y) not in visited and val == LAND:

    for x in range(num_cols):
        for y in range(num_rows):
            if (x, y) not in visited and grid[y][x] == LAND:
                # bfs to find all 1s and convert to 0s
                islands += 1
                queue = [(x, y)]
                while queue:
                    curx, cury = queue.pop(0)

                    if (curx, cury) in visited:
                        continue
                    if curx < 0 or curx >= num_cols or cury < 0 or cury >= num_rows:
                        continue
                    if grid[cury][curx] == WATER:
                        continue

                    visited.add((curx, cury))
                    queue.extend(
                        [
                            (curx - 1, cury),
                            (curx + 1, cury),
                            (curx, cury - 1),
                            (curx, cury + 1),
                        ]
                    )

    return islands


def test_islands():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    assert num_islands(grid) == 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(grid) == 3


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
