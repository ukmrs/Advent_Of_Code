#!/usr/bin/env python3

import argparse


CMD = """
from solutions import day{n}
day{n}.main()
"""

import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="xd")
    parser.add_argument("day", type=int, help="day")
    parser.add_argument(
        "--secondary",
        type=int,
        default=0,
        help="part, default: 0, 0 for both",
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    exec(CMD.format(n=args.day))


if __name__ == "__main__":
    main()
