from math import sqrt
from heapq import heapify, nsmallest


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    distances = [
        (
            sqrt(x * x + y * y),
            [x, y],
        )
        for x, y in points
    ]
    heapify(distances)
    return [c[1] for c in nsmallest(k, distances)]


def test_k_closest():
    pts = k_closest([[1, 3], [-2, 2]], 1)
    assert len(pts) == 1
    assert pts[0] == [-2, 2]

    pts = k_closest([[3, 3], [5, -1], [-2, 4]], 2)
    assert len(pts) == 2
    assert [-2, 4] in pts
    assert [3, 3] in pts


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
