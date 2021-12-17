#!/usr/bin/env python
import re
from collections import namedtuple
from math import sqrt
from re import Pattern, Match

from aoc.common import input
from aoc.common import error

DAY: str = "2021/17"

Bound: namedtuple = namedtuple("Bound", ["min", "max"])

Target: namedtuple = namedtuple("Target", ["x", "y"])


def load_target(input_file: str) -> Target:
    line: str = input.load_lines(DAY, input_file)[0]
    pattern: Pattern = re.compile(r"target area: x=(-*\d+)..(-*\d+), y=(-*\d+)..(-*\d+)")
    result: Match = pattern.search(line)
    return Target(Bound(int(result.group(1)), int(result.group(2))), Bound(int(result.group(4)), int(result.group(3))))


def triangle(val: int) -> int:
    return (val * (val + 1)) // 2


# logic for part 1
#   * the higher we start, the faster we fall
#   * but if we fall _too_ fast, we overshoot the target
#   * we always cross the y == 0 point, because we start from there so we can't end up overshooting it
#   * so, on return, at y == 0, the max speed we can have is the min(y coordinates of target)
#     - i.e. from zero, the farthest we can go in one step is the bottom edge of the target area
#   * we can run than in reverse, to see where we came up from
#     - assuming stop_y = min(y coordinates of target) => max_y = (stop_y * (stop_y + 1)) / 2
#       - or a = abs(stop_y) - 1, max_y = (a * (a+1)) / 2, as we have a point in the middle where vy = 0
def part01(input_file: str) -> int:
    target: Target = load_target(input_file)
    return triangle(target.y.max)


# logic for part 2
#   * work out what starting x or y will end up in target area, then mix and match


def reverse_triangle(val: int) -> int:
    return int((sqrt(8 * val + 1) - 1) // 2)


def starting_xs(bound_x: Bound) -> list[int]:
    min_x: int = reverse_triangle(bound_x.min)
    # account for rounding
    while triangle(min_x) < bound_x.min:
        min_x += 1
    starting_x: list[int] = []
    for x in range(bound_x.max, min_x - 1, -1):
        acc: int = x
        pos: int = 0
        steps: int = 0
        while pos < bound_x.min:
            pos += acc
            acc -= 1
            steps += 1
        if pos <= bound_x.max:
            starting_x.append(x)
    return starting_x


def starting_ys(bound_y: Bound) -> list[int]:
    # this works because we know y is negative
    max_height: int = triangle(bound_y.max)
    max_y: int = reverse_triangle(max_height)
    # rounding errors again
    while triangle(max_y) < max_height:
        max_y += 1
    starting_y: list[int] = []
    # could try to be smart and handle positive speeds different to negative speeds
    for y in range(bound_y.max, max_y + 1):
        acc: int = y
        pos: int = 0
        steps: int = 0
        while pos > bound_y.min:
            pos += acc
            acc -= 1
            steps += 1
        if pos >= bound_y.max:
            starting_y.append(y)
    return starting_y


def launch(x: int, y: int, vx: int, vy: int, target: Target) -> bool:
    if (target.x.min <= x <= target.x.max) and (target.y.min >= y >= target.y.max):
        return True
    if x > target.x.max or y < target.y.max:
        return False
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    vy -= 1
    return launch(x, y, vx, vy, target)


def part02_pair_up(input_file: str) -> int:
    target: Target = load_target(input_file)
    count: int = 0
    starting_y: list[int] = starting_ys(target.y)
    for x in starting_xs(target.x):
        for y in starting_y:
            if launch(0, 0, x, y, target):
                count += 1
    return count


def part02_brute_force(input_file: str) -> int:
    target: Target = load_target(input_file)
    # this works because we know y is negative
    max_height: int = triangle(target.y.max)
    max_y: int = reverse_triangle(max_height)
    # rounding errors again
    while triangle(max_y) < max_height:
        max_y += 1
    count: int = 0
    for x in range(1, target.x.max + 1):
        for y in range(target.y.max, max_y + 1):
            if launch(0, 0, x, y, target):
                count += 1
    return count


# logic for part 2
#   * x is somewhat easy, use triangle / reverse triangle to find min and max starting x velocity
#   * for y, current idea is to use the above to figure out the positive speeds
#     - then try to work out the negative ones
def addcrement(where: dict[int, int], key: int):
    if key not in where:
        where[key] = 0
    where[key] += 1


def workout_x(bound_x: Bound, max_step_y: int) -> dict[int, int]:
    min_x: int = reverse_triangle(bound_x.min)
    # account for rounding
    while triangle(min_x) < bound_x.min:
        min_x += 1
    starting_x: dict[int, int] = {}
    for x in range(bound_x.max, min_x - 1, -1):
        acc: int = x
        pos: int = 0
        steps: int = 0
        while pos <= bound_x.max and acc > 0:
            pos += acc
            acc -= 1
            steps += 1
            if bound_x.min <= pos <= bound_x.max:
                addcrement(starting_x, steps)
                print(x)
                if 0 == acc and steps < max_step_y:
                    for k in range(steps + 1, max_step_y):
                        addcrement(starting_x, k)
    return starting_x


def workout_y(bound_y: Bound) -> dict[int, int]:
    # this works because we know y is negative
    max_height: int = triangle(bound_y.max)
    max_y: int = reverse_triangle(max_height)
    # rounding errors again
    while triangle(max_y) < max_height:
        max_y += 1
    starting_y: dict[int, int] = {}
    # could try to be smart and handle positive speeds different to negative speeds
    for y in range(bound_y.max, max_y + 1):
        acc: int = y
        pos: int = 0
        steps: int = 0
        while pos > bound_y.min:
            pos += acc
            acc -= 1
            steps += 1
        if pos >= bound_y.max:
            if steps not in starting_y:
                starting_y[steps] = 0
            starting_y[steps] += 1
            print(y)
    return starting_y


def part02_try_hard(input_file: str) -> int:
    target: Target = load_target(input_file)
    starting_y: dict[int, int] = workout_y(target.y)
    max_steps_y: int = max(starting_y.keys()) + 1
    print("----")
    starting_x: dict[int, int] = workout_x(target.x, max_steps_y)
    total: int = 0
    for count in starting_x:
        total += starting_x[count] * starting_y.get(count, 0)
    return total


def part02(input_file: str) -> int:
    return part02_pair_up(input_file)
