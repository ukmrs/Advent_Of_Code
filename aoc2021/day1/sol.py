#!/usr/bin/env python3


def get_data():
    with open("./input", "r") as f:
        return [int(line) for line in f.readlines()]


def one(data):
    co = 0
    mx = data[0]
    for line in data[1:]:
        if line > mx:
            co += 1
        mx = line
    return co


def two(data):
    co = 0
    ln = len(data)
    a = sum(data[0:3])

    for i in range(1, ln - 2):
        sm = sum(data[i : i + 3])
        if sm > a:
            co += 1
        a = sm

    return co


def main():
    data = get_data()
    a = one(data)
    b = two(data)
    print(a)
    print(b)


main()
