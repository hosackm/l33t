COUNTER_ALLOWED = False

if COUNTER_ALLOWED:
    from collections import Counter
else:
    from collections import defaultdict

    class Counter:  # no-qa
        def __init__(self, s: str):
            self.data: dict[str, int] = defaultdict(int)
            for ch in s:
                self.data[ch] += 1

        def __eq__(self, other):
            return dict(self.data) == dict(other.data)


def is_anagram(s: str, t: str) -> bool:
    """
    Returns True if s is an anagram of t, else False.
    """
    if not s and not t:
        return True

    if len(s) != len(t):
        return False

    if len(s) < 2:
        return s[0] == t[0]

    return Counter(s) == Counter(t)


def test_is_anagram():
    assert is_anagram("", "") == True
    assert is_anagram("", "a") == False
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False


if __name__ == "__main__":
    import pytest

    pytest.main(["-xv", __file__])
