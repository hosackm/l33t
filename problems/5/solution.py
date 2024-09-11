def valid_palindrome(s: str) -> bool:
    """
    Returns True if s is a palindrome. Ignores all non-alphanumeric
    characters and is case-insensitive.

    Args:
        s (str): string to be palindrome tested
    Returns:
        bool: True, if the string is a palindrome
    """
    # remove all non-ascii characters and make lowercase
    if len(s) < 2:
        return True
    if len(s) == 2:
        return s[0] == s[1]

    left = 0
    right = len(s) - 1
    while left < right:
        while left < len(s) and not s[left].isalnum():
            left += 1
        while right > 0 and not s[right].isalnum():
            right -= 1

        if left >= right:
            return True

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def test_valid_palindrome():
    assert valid_palindrome("A man, a plan, a canal: Panama") == True
    assert valid_palindrome("race a car") == False
    assert valid_palindrome(" ") == True


if __name__ == "__main__":
    import pytest
    pytest.main(["-xv", __file__])
