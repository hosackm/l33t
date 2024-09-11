def rotting_oranges(grid: list[list[int]]) -> int:
    """
    If it's impossible for an orange to rot, return -1
    If there are no fresh oranges return 0
    """
    fresh = set()
    rotten = set()
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh.add((r, c))
            if grid[r][c] == 2:
                rotten.add((r, c))

    if not fresh:
        return 0

    t = 0
    done = False
    while not done:
        to_rot = set()
        for rot_row, rot_col in rotten:
            for n in fresh_neighbors(grid, rot_row, rot_col):
                if n in fresh:
                    fresh.remove(n)
                    to_rot.add(n)

        if not to_rot:
            done = True
            continue

        for row, col in to_rot:
            grid[row][col] = 2
            rotten.add((row, col))

        t += 1

    return t if not fresh else -1


def fresh_neighbors(grid, r, c):
    neighbors = []
    for row, col in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            continue
        neighbors.append((row, col))
    return neighbors


def test_rotting_oranges():
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    assert rotting_oranges(grid) == 4

    grid = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1],
    ]
    assert rotting_oranges(grid) == -1

    grid = [[0, 2]]
    assert rotting_oranges(grid) == 0


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
