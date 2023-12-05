#!/usr/bin/env python3

from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent
INPUT_DIR = ROOT_DIR / "inputs"


def get_input(file: str):
    return get_lines(INPUT_DIR / Path(file).stem)


def get_lines(file_path: str | Path) -> list[str]:
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    return lines


def linefy(text: str) -> list[str]:
    return [a for i in text.split("\n") if (a := i.strip())]
