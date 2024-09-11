def climb_linear_mem(n: int) -> int:
    """
    Calculate the number of ways to get to the nth step
    by climbing one-step or two-steps at a time. Uses linear
    memory in the options list.
    """
    options = [0, 1, 2]
    if n <= 2:
        return options[n]

    step = 3
    while step <= n:
        current = options[-2] + options[-1]
        options.append(current)
        step += 1

    return options[-1]


def climb_constant_mem(n: int) -> int:
    """
    Calculate the number of options to get to the nth step.
    Uses constanct memory (3 ints).
    """
    if n < 3:
        return n

    previous = 2
    two_ago = 1
    step = 3
    while step < n:
        two_ago, previous = previous, previous + two_ago
        step += 1

    return previous + two_ago


def test_climb():
    assert climb_linear_mem(1) == 1
    assert climb_linear_mem(2) == 2
    assert climb_linear_mem(3) == 3
    assert climb_linear_mem(4) == 5
    assert climb_linear_mem(5) == 8

    assert climb_constant_mem(1) == 1
    assert climb_constant_mem(2) == 2
    assert climb_constant_mem(3) == 3
    assert climb_constant_mem(4) == 5
    assert climb_constant_mem(5) == 8


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
