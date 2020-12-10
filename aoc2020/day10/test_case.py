from solution import part1, part2

case1 = sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
case2 = sorted([
    28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1,
    32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
    ])
case3 = [1, 3, 5, 6, 7]


def test_part1():
    assert part1(case1) == 7 * 5
    assert part1(case2) == 22 * 10


def test_part2():
    assert part2(case1) == 8
    assert part2(case2) == 19208
    # assert part2(case3) == 6
