from collections import Counter, defaultdict


def can_construct_no_counter(letter: str, magazine: str) -> bool:
    magazine_count = defaultdict(int)
    for ch in magazine:
        magazine_count[ch] += 1

    letter_count = defaultdict(int)
    for ch in letter:
        letter_count[ch] += 1

    for ch, cnt in letter_count.items():
        if cnt > magazine_count[ch]:
            return False
    return True


def can_construct(letter: str, magazine: str) -> bool:
    magazine_count = Counter(magazine)
    letter_count = Counter(letter)
    for ch, cnt in letter_count.items():
        if cnt > magazine_count[ch]:
            return False
    return True


def test_can_construct():
    assert can_construct("a", "b") == False
    assert can_construct("aa", "ab") == False
    assert can_construct("aa", "aab") == True

    assert can_construct_no_counter("a", "b") == False
    assert can_construct_no_counter("aa", "ab") == False
    assert can_construct_no_counter("aa", "aab") == True


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
