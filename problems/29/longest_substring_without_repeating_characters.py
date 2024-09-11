def longest_substring(s: str):
    """
    Returns the length of the longest substring without
    repeating characters.
    """
    queue = []
    letters = set()
    longest = 0

    for ch in s:
        while ch in letters:
            p = queue.pop(0)
            letters.remove(p)

        queue.append(ch)
        letters.add(ch)

        if len(queue) > longest:
            longest = len(queue)

    return longest


def test_longest_substring():
    assert longest_substring("abcabcbb") == 3
    assert longest_substring("bbbbb") == 1
    assert longest_substring("pwwkew") == 3


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
