from solution import is_valid


def test_is_valid(datafile):
    with open(datafile) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        s, expect = line.split(" ")
        expect = True if "true" in expect else False
        assert is_valid(s) == expect
