def subsets(arr: list[int]) -> list[list[int]]:
    """
    Generate the powerset for a list of numbers.

    The ordering of sets within the powerset
    is not deterministic.  See func subsets_ordered for a
    deterministic version of the function.
    """
    powerset = set()
    # add empty set
    powerset.add(tuple())

    for num in arr:
        subset = set()
        for s in powerset:
            # add the set where we don't use this number
            subset.add((num,))
            # add the set where we use this number
            subset.add(tuple(list(s) + [num]))

        # add them all back to power set
        for s in subset:
            powerset.add(s)

    # convert to a list and sort to have a predictable ordering
    return [list(s) for s in powerset]


def subsets_ordered(arr: list[int]) -> list[list[int]]:
    """
    Generate the powerset for a list of numbers.

    Uses dictionaries to retain for deterministic ordering.

    Example:
    >>> subsets([1, 2])
    [[], [1], [1, 2], [2]]
    """
    powerset = dict()
    # add empty set
    powerset[tuple()] = None

    for num in arr:
        subset = dict()
        for s in powerset:
            # add the set where we don't use this number
            subset[(num,)] = None
            # add the set where we use this number
            subset[tuple(list(s) + [num])] = None

        # add them all back to power set
        for s in subset:
            powerset[s] = None

    # convert to a list and sort to have a predictable ordering
    return [list(key) for key in powerset.keys()]


def test_subsets():
    wants = [
        [],
        [1],
        [2],
        [1, 2],
        [3],
        [1, 3],
        [2, 3],
        [1, 2, 3],
    ]
    assert subsets_ordered([1, 2, 3]) == wants

    assert subsets_ordered([0]) == [[], [0]]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
