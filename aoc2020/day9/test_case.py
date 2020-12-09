from solution import part1, part2

case = [
    35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299,
    277, 309, 576
]


def test_part1():
    assert part1(case, 5) == 127


def test_part2():
    assert part2(case, 127) == 62
