#!/usr/bin/env python

from aoc.common import input
from aoc.common import error

DAY: str = "2021/13"


# X == horizontal, Y == vertical
def parse_input(input_file: str) -> tuple[set[tuple[int, int]], list[tuple[str, int]]]:
    lines: list[str] = input.load_lines(DAY, input_file)
    coords: set[tuple[int, int]] = set()
    folds: list[tuple[str, int]] = []
    for line in lines:
        if "" == line:
            continue
        if "fold" in line:
            fold: str = line.split(" ")[2]
            dim, pos = fold.split("=")
            folds.append((dim, int(pos)))
        else:
            x, y = line.split(",")
            coords.add((int(x), int(y)))
    return coords, folds


def fold(coords: set[tuple[int, int]], at: tuple[str, int]) -> set[tuple[int, int]]:
    index: int = 0 if "x" == at[0] else 1
    remaining_coords: set[tuple[int, int]] = set()
    for coord in coords:
        if at[1] < coord[index]:
            diff: int = coord[index] - at[1]
            if "x" == at[0]:
                new_coord: tuple[int, int] = (at[1] - diff, coord[1])
            else:
                new_coord: tuple[int, int] = (coord[0], at[1] - diff)
            remaining_coords.add(new_coord)
        else:
            remaining_coords.add(coord)
    return remaining_coords


def part01(input_file: str) -> str:
    coords, folds = parse_input(input_file)
    coords = fold(coords, folds[0])
    return str(len(coords))


def part02(input_file: str) -> list[str]:
    coords, folds = parse_input(input_file)
    for fold_at in folds:
        coords = fold(coords, fold_at)
    max_x: int = 0
    max_y: int = 0
    for i in range(len(folds) - 1, -1, -1):
        if 0 != max_y and 0 != max_x:
            break
        if 0 == max_y and "y" == folds[i][0]:
            max_y = folds[i][1]
        if 0 == max_x and "x" == folds[i][0]:
            max_x = folds[i][1]
    results: list[list[str]] = [[" "] * max_x for _ in range(max_y)]
    for coord in coords:
        results[coord[1]][coord[0]] = "#"
    return "\n".join(["".join(row) for row in results])
