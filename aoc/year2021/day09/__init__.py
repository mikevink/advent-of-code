#!/usr/bin/env python

from aoc.common import input

DAY: str = "2021/09"

DIRECTIONS: dict[str, tuple[int, int]] = {
    "north": (-1, 0),
    "east": (0, 1),
    "south": (1, 0),
    "west": (0, -1),
}


def parse_line(line: str) -> list[int]:
    return [int(l) for l in line]


def check_direction(heightmap: list[list[int]], x: int, y: int, direction: tuple[int, int]) -> bool:
    lenx: int = len(heightmap)
    leny: int = len(heightmap[0])
    nx: int = x + direction[0]
    # if out of bounds, ignore
    if 0 > nx or lenx <= nx:
        return True
    ny: int = y + direction[1]
    if 0 > ny or leny <= ny:
        return True
    h: int = heightmap[x][y]
    n: int = heightmap[nx][ny]
    return h < n


def check_directions(heightmap: list[list[int]], x: int, y: int) -> bool:
    good: bool = True
    for direction in DIRECTIONS.values():
        good = good and check_direction(heightmap, x, y, direction)
        if not good:
            return False
    return True


def find_depressions(heightmap: list[list[int]]) -> list[tuple[int, int]]:
    lenx: int = len(heightmap)
    leny: int = len(heightmap[0])
    depressions: list[tuple[int, int]] = []
    for x in range(lenx):
        for y in range(leny):
            if check_directions(heightmap, x, y):
                depressions.append((x, y))
    return depressions


def part01(input_file: str) -> str:
    heightmap: list[list[int]] = input.load_lines(DAY, input_file, parse_line)
    depressions: list[tuple[int, int]] = find_depressions(heightmap)
    return str(sum(map(lambda d: heightmap[d[0]][d[1]] + 1, depressions)))


def ascend(heightmap: list[list[int]], x: int, y: int) -> int:
    lenx: int = len(heightmap)
    leny: int = len(heightmap[0])
    # if out of bounds, ignore
    if 0 > x or lenx <= x:
        return 0
    if 0 > y or leny <= y:
        return 0
    h: int = heightmap[x][y]
    # ignore if summit or already seen
    if 9 == h or -1 == h:
        return 0
    heightmap[x][y] = -1
    count: int = 0
    for direction in DIRECTIONS.values():
        count += ascend(heightmap, x + direction[0], y + direction[1])
    return 1 + count


def part02(input_file: str) -> str:
    heightmap: list[list[int]] = input.load_lines(DAY, input_file, parse_line)
    depressions: list[tuple[int, int]] = find_depressions(heightmap)
    ascents: list[int] = [ascend(heightmap, d[0], d[1]) for d in depressions]
    sascents: list[int] = sorted(ascents)
    return str(sascents[-3] * sascents[-2] * sascents[-1])
