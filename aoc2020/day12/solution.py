#!/usr/bin/env python3
def parse_instructions(file):
    with open(file) as f:
        return [(a[0], int(a[1:].rstrip())) for a in f.readlines()]


class Ship():
    multi = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def __init__(self):
        self.x, self.y = 0, 0
        self.code = {"N": 0, "E": 1, "S": 2, "W": 3, "F": 1}

    def turnright(self, degrees):
        self.set_head((self.head + (degrees // 90)) % 4)

    def turnleft(self, degrees):
        self.set_head((self.head - (degrees // 90)) % 4)

    @property
    def head(self):
        return self.code["F"]

    def set_head(self, val):
        self.code["F"] = val

    def swim(self, direction, val):
        a, b = self.multi[self.code[direction]]
        self.x += val * a
        self.y += val * b

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def travel(self, instructions):
        for opt, val in instructions:
            if opt == "L":
                self.turnleft(val)

            elif opt == "R":
                self.turnright(val)

            else:
                self.swim(opt, val)


class ShipTwo(Ship):
    def __init__(self):
        super().__init__()
        self.set_head(0)
        self.waypoint = [1, 10]

    def turnright(self, degrees):
        og1, og2 = self.head, (self.head + 1) % 4
        self.set_head((self.head + (degrees // 90)) % 4)
        self.rotate_waypoint(og1, og2)

    def turnleft(self, degrees):
        og1, og2 = self.head, (self.head + 1) % 4
        self.set_head((self.head - (degrees // 90)) % 4)
        self.rotate_waypoint(og1, og2)

    def rotate_waypoint(self, og1, og2):
        if (og1 < 2) ^ (self.head < 2):
            self.waypoint[0] *= -1
        if (og2 < 2) ^ (((self.head + 1) % 4) < 2):
            self.waypoint[1] *= -1

    def change_waypoint(self, direction, val):
        if self.head % 2:
            b, a = self.multi[self.code[direction]]
        else:
            a, b = self.multi[self.code[direction]]

        self.waypoint[0] += val * a
        self.waypoint[1] += val * b

    def swim(self, val):
        if self.head % 2:
            a, b = self.waypoint
        else:
            b, a = self.waypoint
        self.x += val * a
        self.y += val * b

    def travel(self, instructions):
        for opt, val in instructions:
            if opt == "L":
                self.turnleft(val)
            elif opt == "R":
                self.turnright(val)
            elif opt == "F":
                self.swim(val)
            else:
                self.change_waypoint(opt, val)


def main():
    parsed = parse_instructions("input")

    ship_one = Ship()
    ship_two = ShipTwo()

    ship_one.travel(parsed)
    ship_two.travel(parsed)

    print(ship_one.manhattan)  # 1186
    print(ship_two.manhattan)  # 47806


if __name__ == "__main__":
    main()
