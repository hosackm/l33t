INT_MAX = (2**31) - 1
INT_MIN = -(2**31)


def atoi(s):
    s = s.strip()

    if len(s) == 0:
        return 0

    start = 0
    negative = False
    if s.startswith(("-", "+")):
        if s[0] == "-":
            negative = True
        start = 1

    if start > len(s):
        return 0

    while start < len(s) and s[start] == "0":
        start += 1

    if start == len(s):
        return 0

    digit_lut = {ch: i for i, ch in enumerate("0123456789")}

    num = 0
    i = start
    while i < len(s) and s[i].isdigit():
        digit_char = s[i]
        digit = digit_lut[digit_char]

        # if would overflow, return INT_MAX or INT_MIN
        if negative:
            if ((INT_MIN + digit) // 10) >= num:
                return INT_MIN
            num = num * 10 - digit
        else:
            if ((INT_MAX - digit) // 10) < num:
                return INT_MAX
            num = num * 10 + digit
        i += 1

    return num


def test_atoi():
    s = " -042"
    output = -42
    assert atoi(s) == output

    s = "42"
    output = 42
    assert atoi(s) == output

    s = "1337c0d3"
    output = 1337
    assert atoi(s) == output

    s = "0-1"
    output = 0
    assert atoi(s) == output

    s = str(INT_MAX + 1)
    output = INT_MAX
    assert atoi(s) == output

    s = str(INT_MIN - 1)
    output = INT_MIN
    assert atoi(s) == output

    assert atoi("2147483646") == 2147483646


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
