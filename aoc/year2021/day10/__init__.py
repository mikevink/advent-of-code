#!/usr/bin/env python

from collections import deque

from aoc.common import error
from aoc.common import input
from aoc.common import sort

DAY: str = "2021/10"


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


def part01(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    return sum([ERROR_POINTS[first_error(line)] for line in lines])


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


def part02(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    incomplete: list[str] = [line for line in lines if "" == first_error(line)]
    scores: list[int] = [completion_score(line) for line in incomplete]
    sort.heapsort(scores)
    return scores[len(scores) // 2]
