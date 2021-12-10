#!/usr/bin/env python

from collections import deque

from aoc.common import input
from aoc.common import error

DAY: str = "2021/10"


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
    for i in range(lena // 2, -1, -1):
        maxheap(array, i, lena)
    # sort
    # we always work with 0, so no need to include it in the loop
    for i in range(lena - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        # last element of the array should already be max, so skip it
        lena -= 1
        maxheap(array, 0, lena)


PAIRS: dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
OPEN: set[str] = set(PAIRS.keys())

ERROR_POINTS: dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137, "": 0}


def first_error(line: str) -> str:
    walk: deque = deque()
    for l in line:
        if 0 == len(walk):
            walk.append(l)
        else:
            if l in OPEN:
                walk.append(l)
            else:
                last: str = walk[-1]
                if PAIRS[last] == l:
                    walk.pop()
                else:
                    return l
    return ""


def part01(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    return str(sum([ERROR_POINTS[first_error(line)] for line in lines]))


COMPLETION_POINTS: dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}


def completion_score(line: str) -> int:
    walk: deque = deque()
    for l in line:
        if 0 == len(walk):
            walk.append(l)
        else:
            if l in OPEN:
                walk.append(l)
            else:
                last: str = walk[-1]
                if PAIRS[last] == l:
                    walk.pop()
                else:
                    raise Exception(error.ERROR)
    score: int = 0
    while 0 != len(walk):
        l: str = PAIRS[walk.pop()]
        score = score * 5 + COMPLETION_POINTS[l]
    return score


def part02(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    incomplete: list[str] = [line for line in lines if "" == first_error(line)]
    scores: list[int] = [completion_score(line) for line in incomplete]
    heapsort(scores)
    return str(scores[len(scores) // 2])
