#!/usr/bin/env python3
import numpy as np
import re

numex = re.compile(r"\d+")

class Bingo():
    def __init__(self, sequence, cards):
        self.sequence = sequence
        self.cards = cards

    def __str__(self):
        return f"{self.sequence}\n{self.cards}"

    def print(self):
        print(self.sequence)
        for array in self.cards:
            print(array)
            print()

    def solve2(self):
        marked_for_del = []
        flag = False
        for number in self.sequence:
            for ix, card in enumerate(self.cards):
                x = np.argwhere(card == number)
                if x.size > 0:
                    a, b = x[0]
                    card[a, b] = -1
                for row in card:
                    if row.sum() == -5:
                        if len(self.cards) == 1:
                            return self.calculate(card, number)
                        flag = True
                        marked_for_del.append(ix)

                if flag:
                    flag = False
                    continue


                for column in card.T:
                    if column.sum() == -5:
                        if len(self.cards) == 1:
                            return self.calculate(card, number)
                        marked_for_del.append(ix)

            while marked_for_del:
                print(marked_for_del)
                delix = marked_for_del.pop()
                del self.cards[delix]

    def solve(self):
        for number in self.sequence:
            for card in self.cards:
                x = np.argwhere(card == number)
                if x.size > 0:
                    a, b = x[0]
                    card[a, b] = -1
                for row in card:
                    if row.sum() == -5:
                        return self.calculate(card, number)

                for column in card.T:
                    if column.sum() == -5:
                        return self.calculate(card, number)

    @staticmethod
    def calculate(arr, number):
        a = arr[arr != -1]
        return a.sum() * number

def parse_file(file):
    with open(file, "r") as f:
        result = []
        lineiter = f.readlines()
        seq = [int(i) for i in lineiter[0].rstrip().split(",")]
        array = np.zeros(shape=(5,5), dtype="int32")
        co = -1
        for line in lineiter[2:]:
            co += 1
            found = numex.findall(line)
            if not found:
                co = -1
                result.append(array)
                array = np.zeros(shape=(5,5), dtype="int32")
                continue
            array[co, :] = found 

        if array.sum() > 0:
            result.append(array)
                
    return Bingo(seq, result)


def test():
    parsed = parse_file("./example")
    assert parsed.solve() == 4512
    assert parsed.solve2() == 1924


def main():
    test()
    parsed = parse_file("./input")
    print(parsed.solve2())


if __name__ == "__main__":
    main()
