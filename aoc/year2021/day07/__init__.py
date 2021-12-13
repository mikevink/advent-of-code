#!/usr/bin/env python

import math

from aoc.common import input
from aoc.common import sort

DAY: str = "2021/07"


def part01(input_file: str) -> int:
    crabs: list[int] = input.load_single_csv(DAY, input_file, int)
    sort.heapsort(crabs)
    lenp: int = len(crabs)
    midway: int = lenp // 2
    if 0 == lenp % 2:
        median: int = (crabs[midway - 1] + crabs[midway]) // 2
    else:
        median: int = crabs[midway]
    fuel: int = 0
    for c in crabs:
        fuel += abs(c - median)
    return fuel


def mean_fuel(crab: int, mean: int) -> int:
    distance: int = abs(crab - mean)
    return (distance * (distance + 1)) // 2


def part02(input_file: str) -> int:
    crabs: list[int] = input.load_single_csv(DAY, input_file, int)
    mean: float = sum(crabs) / len(crabs)
    ceil_mean: int = math.ceil(mean)
    floor_mean: int = math.floor(mean)
    ceil_fuel: int = 0
    floor_fuel: int = 0
    for c in crabs:
        ceil_fuel += mean_fuel(c, ceil_mean)
        floor_fuel += mean_fuel(c, floor_mean)
    return min(ceil_fuel, floor_fuel)
