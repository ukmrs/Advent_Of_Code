from solution import parse_documents, part1, part2

example1 = parse_documents('example1')
example2 = parse_documents('example2')


def test_part1():
    assert part1(example1) == 2


def test_part2():
    assert part2(example2) == 4
