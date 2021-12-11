#!/usr/bin/env python

from aoc.common import input
from aoc.common import error

DAY: str = "2021/11"

ROWS: int = 10
COLS: int = 10
DIRECTIONS: list[tuple[int, int]] = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def to_array(line: str) -> list[int]:
    return [int(l) for l in line]


def flash(array: list[list[int]], i: int, j: int):
    if 0 == array[i][j]:
        return
    array[i][j] = 0
    for d in DIRECTIONS:
        ni: int = i + d[0]
        nj: int = j + d[1]
        if 0 <= ni < ROWS and 0 <= nj < COLS:
            if 0 == array[ni][nj]:
                continue
            array[ni][nj] += 1
            if 9 < array[ni][nj]:
                flash(array, ni, nj)


def print_array(array: list[list[int]], step: int):
    print(f"At step {step}")
    for row in array:
        print("".join(map(str, row)))
    print("")


def part01(input_file: str, steps: int) -> str:
    array: list[list[int]] = input.load_lines(DAY, input_file, to_array)
    flashes: int = 0
    for step in range(steps):
        for i in range(ROWS):
            for j in range(COLS):
                array[i][j] += 1
        for i in range(ROWS):
            for j in range(COLS):
                if 9 < array[i][j]:
                    flash(array, i, j)
        for row in array:
            for col in row:
                if 0 == col:
                    flashes += 1
    return str(flashes)


def part02(input_file: str) -> str:
    array: list[list[int]] = input.load_lines(DAY, input_file, to_array)
    flashes: int = 0
    step: int = 0
    while True:
        for i in range(ROWS):
            for j in range(COLS):
                array[i][j] += 1
        for i in range(ROWS):
            for j in range(COLS):
                if 9 < array[i][j]:
                    flash(array, i, j)
        if 0 == sum([sum(row) for row in array]):
            return str(step + 1)
        step += 1
