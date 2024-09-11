def merge(intervals: list[list[int]]):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    merged = []
    current = intervals[0]
    for interv in intervals[1:]:
        if (
            current[0] <= interv[0] <= current[1]
            or current[0] <= interv[1] <= current[1]
        ):
            current[0] = min(current[0], interv[0])
            current[1] = max(current[1], interv[1])
        else:
            merged.append(current)
            current = interv

    # if the last interval hasn't been added
    if not merged or current != merged[-1]:
        merged.append(current)

    return merged


def test_merge():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert merge(intervals) == [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    assert merge(intervals) == [[1, 5]]

    intervals = [[1, 4], [0, 4]]
    assert merge(intervals) == [[0, 4]]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
