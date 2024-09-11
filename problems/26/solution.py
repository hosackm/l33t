def insert_interval(intervals, new):
    """
    Inserts an interval into a sorted list of intervals and
    merges any overlapping intervals.
    """
    modified = []
    for i, it in enumerate(intervals):
        if new[1] < it[0]:
            return modified + [new] + intervals[i:]
        elif new[0] > it[1]:
            modified.append(it)
        else:
            new = [min(new[0], it[0]), max(new[1], it[1])]

    # new has not been written
    return modified + [new]


def test_insert_interval():
    assert insert_interval(
        [[1, 3], [6, 9]],
        [2, 5],
    ) == [[1, 5], [6, 9]]

    assert insert_interval(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        [4, 8],
    ) == [[1, 2], [3, 10], [12, 16]]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
