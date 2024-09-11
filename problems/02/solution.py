closing: dict[str, str] = {
    "}": "{",
    ")": "(",
    "]": "[",
}


def is_valid(s: str) -> bool:
    num_chars = len(s)
    if num_chars % 2 != 0:
        return False

    stack: list[str] = list()
    for i, ch in enumerate(s):
        if len(stack) > num_chars - i:
            return False

        if ch in "{([":
            stack.append(ch)
        elif ch in "})]":
            if len(stack) == 0 or closing[ch] != stack.pop():
                return False
        else:
            return False

    return len(stack) == 0


def test_valid_parens():
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False


if __name__ == "__main__":
    import pytest

    pytest.main()
