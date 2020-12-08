from solution import part1, part2

ex = [["nop", 0], ["acc", 1], ["jmp", 4], ["acc", 3], ["jmp", -3],
      ["acc", -99], ["acc", 1], ["jmp", -4], ["acc", 6]]


def test_part1():
    assert part1(ex) == 5


def test_part2():
    part2(ex) == 8
