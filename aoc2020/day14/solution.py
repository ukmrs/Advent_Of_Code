#!/usr/bin/env python3
from itertools import combinations as combo
from pprint import pprint


def parse_instructions(input_file):
    lst = []
    with open(input_file) as f:
        _, val = f.readline().strip().split(" = ")
        mask_length = len(val)
        lst.append(("", val))

        for opt, val in map(lambda x: x.strip().split(" = "), f.readlines()):
            lst.append((opt[4:-1], val))
    return lst, mask_length


def get_adresses(base, adds):
    yield base
    for i in range(1, len(adds) + 1):
        for cmb in combo(adds, i):
            yield base + sum(cmb)


def docking(instructions, mln):
    memory = {}
    mem2 = {}
    for opt, val in instructions:
        if opt:
            val = int(val)
            bval = f"{val:0{mln}b}"
            bmems = f"{int(opt):0{mln}b}"

            masked, base_mem = 0, 0
            adders = []
            for ix, mb, vb, bmem in zip(range(1, mln + 1), mask, bval, bmems):
                if mb == "X":
                    if vb == "1":
                        masked += 2**(mln - ix)
                    adders.append(2**(mln - ix))
                else:
                    if mb == "1":
                        masked += 2**(mln - ix)
                        base_mem += 2**(mln - ix)
                    elif bmem == "1":
                        base_mem += 2**(mln - ix)

            memory[opt] = masked

            for adress in get_adresses(base_mem, adders):
                mem2[adress] = val

        else:
            mask = val

    return {"part1": sum(memory.values()), "part2": sum(mem2.values())}


def main():
    parsed, maskln = parse_instructions("input")
    ans = docking(parsed, maskln)
    print(f"part1: {ans['part1']}")  # 14722016054794
    print(f"part2: {ans['part2']}")  # 3618217244644

if __name__ == "__main__":
    main()
