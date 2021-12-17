#!/usr/bin/env python3


def open_file(file):
    with open(file, "r") as f:
        return [i.strip() for i in f.readlines()]


def sol1(lst):
    horizontal = 0
    depth = 0
    for action in lst:
        cmd, value = action.split(" ")
        value = int(value)
        if cmd == "forward":
            horizontal += value
        elif cmd == "up":
            depth -= value
        elif cmd == "down":
            depth += value
    return horizontal * depth

def sol2(lst):
    aim = 0
    horizontal = 0
    depth = 0
    for action in lst:
        cmd, value = action.split(" ")
        value = int(value)
        if cmd == "forward":
            horizontal += value
            depth += value * aim
        elif cmd == "up":
            aim -= value
        elif cmd == "down":
            aim += value
    return horizontal * depth


def main():
    lst = open_file("input")
    a = sol1(lst)
    b = sol2(lst)
    print(a)
    print(b)


main()
