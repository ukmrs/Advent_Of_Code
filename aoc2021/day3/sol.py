#!/usr/bin/env python3


def open_file(file):
    with open(file, "r") as f:
        return [i.strip() for i in f.readlines()]


def binzarize(n):
    if n > 0:
        return 1
    return 0


def sol1(lst):
    sup = [0 for i in range(len(lst[0]))]
    for line in lst:
        for ix, bit in enumerate(line):
            if bit == "1":
                sup[ix] += 1
            else:
                sup[ix] -= 1

    gamma = (str(binzarize(i)) for i in sup)
    epsilon = (str(int(not binzarize(i))) for i in sup)

    a = int("".join(gamma), 2)
    b = int("".join(epsilon), 2)

    return a * b


def get_bit(number, bit):
    return number >> bit & 1


def count_bits(lst, bit):
    ones, zero = 0, 0

    for i in lst:
        if get_bit(i, bit) == 1:
            ones += 1
        else:
            zero += 1

    if ones >= zero:
        return 1, 0
    return 0, 1


def sol2(lst):
    ln = len(lst[0])
    container = [int(i, 2) for i in lst]

    obit, cbit = count_bits(container, 0)
    oxy = [i for i in container if get_bit(i, ln - 1) == obit]
    carb = [i for i in container if get_bit(i, ln - 1) == cbit]

    for bit in range(2, ln + 1):
        obit, _ = count_bits(oxy, ln - bit)
        oxy = [i for i in oxy if get_bit(i, ln - bit) == obit]
        if len(oxy) == 1:
            ox_ans = oxy[0]
            break
    else:
        raise ValueError("not found")


    for bit in range(2, ln + 1):
        _, cbit = count_bits(carb, ln - bit)
        carb = [i for i in carb if get_bit(i, ln - bit) == cbit]

        if len(carb) == 1:
            carb_ans = carb[0]
            break
    else:
        raise ValueError("not found")

    return ox_ans * carb_ans


def main():
    lst = open_file("./input")
    print(sol1(lst))
    print(sol2(lst))


main()
