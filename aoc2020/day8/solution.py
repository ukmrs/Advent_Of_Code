#!/usr/bin/env python3


def parse_instructions(instructions):
    inst = []
    with open(instructions) as f:
        for op, val in map(lambda x: x.rstrip().split(" "), f.readlines()):
            inst.append([op, int(val)])
    return inst


def terminates_acc(instructions):
    seen = set()
    ix, acc = 0, 0
    while ix not in seen:
        try:
            op, val = instructions[ix]
        except IndexError:
            return True, acc
        seen.add(ix)
        if op == "nop":
            ix += 1
        elif op == "acc":
            acc += val
            ix += 1
        else:
            ix += val

    return False, acc


def part1(instructions):
    return terminates_acc(instructions)[1]


def part2(instructions):
    swapper = {"nop": "jmp", "jmp": "nop"}
    checked = 0
    while checked < len(instructions):
        if (inst := instructions[checked][0]) != "acc":
            instructions[checked][0] = swapper[inst]
            terminates, acc = terminates_acc(instructions)
            instructions[checked][0] = inst
            if terminates:
                return acc
        checked += 1


def main():
    parsed = parse_instructions("input")
    print(f"part1: {part1(parsed)}")  # 1337
    print(f"part2: {part2(parsed)}")  # 1358


if __name__ == "__main__":
    main()
