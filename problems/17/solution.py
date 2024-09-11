from collections import Counter


def longest_palindrome(s: str) -> int:
    total = 0
    middle = 0
    for count in Counter(s).values():
        total += (count // 2) * 2
        if count % 2 == 1:
            middle = 1

    return total + middle


def test_longest_palindrome():
    s = "abccccdd"
    assert longest_palindrome(s) == 7
    s = "a"
    assert longest_palindrome(s) == 1


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
