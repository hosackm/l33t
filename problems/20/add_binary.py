from itertools import zip_longest


results = {
    # cab -> carry, result
    "000": ("0", "0"),
    "001": ("0", "1"),
    "010": ("0", "1"),
    "011": ("1", "0"),
    "100": ("0", "1"),
    "101": ("1", "0"),
    "110": ("1", "0"),
    "111": ("1", "1"),
}


def add(a: str, b: str) -> str:
    output = ""
    a = list(a)
    b = list(b)
    carry = "0"
    while a or b or carry == "1":
        first = a.pop(-1) if a else "0"
        second = b.pop(-1) if b else "0"
        carry, result = results[carry+first+second]
        output = result + output

    return output


def add_index(a: str, b: str) -> str:
    read_a = len(a) - 1
    read_b = len(b) - 1
    output = ""
    carry = "0"
    while read_a >= 0 or read_b >= 0 or carry == "1":
        first = a[read_a] if read_a >= 0 else "0"
        second = b[read_b] if read_b >= 0 else "0"

        carry, result = results[carry+first+second]
        output = result + output

        read_a -= 1
        read_b -= 1

    return output


def add_zip(a: str, b: str) -> str:
    output = ""
    carry = "0"
    for a, b in zip_longest(reversed(a), reversed(b), fillvalue="0"):
        carry, result = results[carry+a+b]
        output = result + output

    if carry == "1":
        output = carry + output

    return output


def test_add():
    assert add("11", "1") == "100"
    assert add("1010", "1011") == "10101"
    assert add_index("11", "1") == "100"
    assert add_index("1010", "1011") == "10101"
    assert add_zip("11", "1") == "100"
    assert add_zip("1010", "1011") == "10101"


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
