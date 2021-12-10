#!/usr/bin/env python

from aoc2021 import input

DAY: str = "01"


def part01(input_file: str) -> str:
    depths: list[int] = input.load_lines(DAY, input_file, int)
    a: int = depths.pop(0)
    increases: int = 0
    for b in depths:
        if b > a:
            increases += 1
        a = b
    return str(increases)


def part02(input_file: str) -> str:
    depths: list[int] = input.load_lines(DAY, input_file, int)
    ldepths: int = len(depths)
    increases: int = 0
    for i in range(0, ldepths - 3):
        a: int = depths[i + 0] + depths[i + 1] + depths[i + 2]
        b: int = depths[i + 1] + depths[i + 2] + depths[i + 3]
        if b > a:
            increases += 1
    return str(increases)
