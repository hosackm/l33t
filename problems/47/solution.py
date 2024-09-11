from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key, value, ts):
        self.data[key].append((ts, value))

    def get(self, key, ts):
        values = self.data[key]
        if not values:
            return ""

        # ts can be larger than value.timestamp
        pos = 0
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == ts:
                return values[mid][1]
            if values[mid][0] < ts:
                pos = mid
                left = mid + 1
            else:
                right = mid - 1

        if values[pos][0] > ts:
            return ""
        return values[pos][1]


def test_time_map():
    tm = TimeMap()

    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"

    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"

    tm = TimeMap()
    tm.set("love", "high", 10)
    tm.set("love", "low", 20)
    assert tm.get("love", 5) == ""
    assert tm.get("love", 10) == "high"
    assert tm.get("love", 15) == "high"
    assert tm.get("love", 20) == "low"
    assert tm.get("love", 25) == "low"


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
