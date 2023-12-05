from utils import common
from collections import defaultdict


def get_matching(line) -> int:
    winning, elfs = (set(i.split()) for i in line.split(":")[-1].split(" | "))
    return len(winning & elfs)


def part1(lines: list[str]) -> int:
    s = 0
    for line in lines:
        matching = get_matching(line)
        if matching != 0:
            s += 1 << matching - 1

    return s


def part2(lines: list[str]) -> int:
    cards = defaultdict(int)
    max_card_number = len(lines)
    for card_number, line in enumerate(lines, start=1):
        matching = get_matching(line)
        card_power = cards[card_number]

        for i in range(card_number + 1, card_number + 1 + matching):
            if i <= max_card_number:
                cards[i] += card_power + 1

    return sum(cards.values()) + max_card_number


def main():
    lines = common.get_input(__file__)
    res1 = part1(lines)
    res2 = part2(lines)
    print(res1)
    print(res2)


if __name__ == "__main__":
    main()
