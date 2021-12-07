#!/usr/bin/env python

import math

from aoc2021 import input
from aoc2021 import error

DAY: str = "07"

def maxheap(array: list[int], chroot: int, lena: int):
    maximum: int = chroot
    left: int = 2 * chroot + 1
    right: int = 2 * chroot + 2

    if left < lena and array[maximum] <= array[left]:
        maximum = left

    if right < lena and array[maximum] <= array[right]:
        maximum = right

    if chroot != maximum:
        array[chroot], array[maximum] = array[maximum], array[chroot]

        maxheap(array, maximum, lena)

def heapsort(array: list[int]):
    lena: int = len(array)
    # build heap
    for i in range(lena//2, -1, -1):
        maxheap(array, i, lena)
    # sort
    # we always work with 0, so no need to include it in the loop
    for i in range(lena - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        # last element of the array should already be max, so skip it
        lena -= 1
        maxheap(array, 0, lena)

def part01(input_file: str) -> str:
    crabs: list[int] = input.load_single_csv(DAY, input_file, int)
    heapsort(crabs)
    lenp: int = len(crabs)
    midway: int = lenp//2
    if 0 == lenp % 2:
        median: int = (crabs[midway - 1] + crabs[midway]) // 2
    else:
        median: int = crabs[midway]
    fuel: int = 0
    for c in crabs:
        fuel += abs(c - median)
    return str(fuel)

def mean_fuel(crab: int, mean: int) -> int:
    distance: int = abs(crab - mean)
    return (distance * (distance + 1)) // 2

def part02(input_file: str) -> str:
    crabs: list[int] = input.load_single_csv(DAY, input_file, int)
    mean: float = sum(crabs) / len(crabs)
    ceil_mean: int =  math.ceil(mean)
    floor_mean: int = math.floor(mean)
    ceil_fuel: int = 0
    floor_fuel: int = 0
    for c in crabs:
        ceil_fuel += mean_fuel(c, ceil_mean)
        floor_fuel += mean_fuel(c, floor_mean)
    return str(min(ceil_fuel, floor_fuel))
