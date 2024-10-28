TABLE = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def phone_numbers(digits: str) -> list[str]:
    if not digits:
        return []

    # fill with '' so we have something to iterate
    # over the first iteration
    combinations = set([""])
    for digit in digits:
        new_combinations = []
        for letter in TABLE[digit]:
            for combination in combinations:
                new_combinations.append(combination + letter)
        combinations = set(new_combinations)

    return sorted(list(combinations))


def test_phone_numbers():
    nums = phone_numbers("23")
    assert nums == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    nums = phone_numbers("")
    assert nums == []

    nums = phone_numbers("2")
    assert nums == ["a", "b", "c"]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
