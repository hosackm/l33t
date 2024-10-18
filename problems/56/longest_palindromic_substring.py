def longest_palindrome(s: str) -> str:
    if len(s) == 1:
        return s

    if len(s) == 2:
        return s if s[0] == s[1] else ""

    offsets = [
        (-1, 1),  # odd length palindromes begin from -1 and +1 from center char
        (0, 1),  # even length from 0 and +1 from center char
    ]
    longest = ""
    for off in offsets:
        center = 0
        linc, rinc = off
        while center < len(s):
            candidate = s[center]
            i = center + linc
            j = center + rinc
            while i >= 0 and j < len(s) and s[i] == s[j]:
                candidate = s[i : j + 1]
                if len(candidate) >= len(longest):
                    longest = candidate
                i -= 1
                j += 1
            center += 1

    return longest


def test_longest_palindrome():
    assert longest_palindrome("babad") == "aba"
    assert longest_palindrome("cbbd") == "bb"


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvvs", __file__])
