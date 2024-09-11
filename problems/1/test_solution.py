from solution import two_sum


def test_data_file(datafile):
    with open(datafile) as f:
        lines = f.readlines()

    read = 0
    stride = 3
    while read < len(lines) - stride:
        numbers, target, expected = lines[read:read+stride]
        numbers = [int(n) for n in numbers.strip().split(" ")]
        expected = [int(n) for n in expected.strip().split(" ")]
        target = int(target)
        assert expected == two_sum(numbers, target)
        read += stride
