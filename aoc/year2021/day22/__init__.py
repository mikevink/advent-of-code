#!/usr/bin/env python
import re
from re import Pattern, Match
from typing import Optional

from aoc.common import input
from aoc.common import error

DAY: str = "2021/22"


class Range:
    def __init__(self, min_: int, max_: int):
        self.min: int = min_
        self.max: int = max_

    def bound(self, bounds: 'Range') -> Optional['Range']:
        if bounds.max < self.min or bounds.min > self.max:
            return None
        min_: int = self.min if self.min >= bounds.min else bounds.min
        max_: int = self.max if self.max <= bounds.max else bounds.max
        return Range(min_, max_)

    def range(self) -> range:
        return range(self.min, self.max + 1)

    def __str__(self) -> str:
        return f"[{self.min}, {self.max}]"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: 'Range') -> bool:
        return self.min == other.min and self.max == other.max


class Coords:
    def __init__(self, x: int, y: int, z: int):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.str: str = f"({self.x}, {self.y}, {self.z})"
        self.hash: int = hash(self.str)

    def __eq__(self, other: 'Coords') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return self.hash

    def __str__(self) -> str:
        return self.str


class Cuboid:
    @staticmethod
    def parse(line: str) -> 'Cuboid':
        pattern: Pattern = re.compile(r"(\w+) x=(-*\d+)..(-*\d+),y=(-*\d+)..(-*\d+),z=(-*\d+)..(-*\d+)")
        result: Match = pattern.search(line)
        return Cuboid(
            1 if "on" == result.group(1) else 0,
            Range(int(result.group(2)), int(result.group(3))),
            Range(int(result.group(4)), int(result.group(5))),
            Range(int(result.group(6)), int(result.group(7))),
        )

    def __init__(self, state: int, x: Range, y: Range, z: Range):
        self.state: int = state
        self.x: Range = x
        self.y: Range = y
        self.z: Range = z

    def bound(self, bounds: Range) -> Optional['Cuboid']:
        x: Optional[Range] = self.x.bound(bounds)
        y: Optional[Range] = self.y.bound(bounds)
        z: Optional[Range] = self.z.bound(bounds)
        if x is None or y is None or z is None:
            return None
        return Cuboid(self.state, x, y, z, )

    def apply(self, reactor: dict[Coords, int]):
        for x in self.x.range():
            for y in self.y.range():
                for z in self.z.range():
                    reactor[Coords(x, y, z)] = self.state

    def __str__(self) -> str:
        return f"{{{self.state}: {self.x}, {self.y}, {self.z}}}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: 'Cuboid') -> bool:
        return self.state == other.state and self.x == other.x and self.y == other.y and self.z == other.z


def parse(input_file: str) -> list[Cuboid]:
    lines: list[str] = input.load_lines(DAY, input_file)
    return [Cuboid.parse(line) for line in lines]


def filter_cuboids(cuboids: list[Cuboid], bounds: Range) -> list[Cuboid]:
    return list(filter(lambda c: c is not None, map(lambda c: c.bound(bounds), cuboids)))


def reboot(cuboids: list[Cuboid]) -> int:
    reactor: dict[Coords, int] = {}
    for cuboid in cuboids:
        cuboid.apply(reactor)
    return sum(reactor.values())


def initialise(cuboids: list[Cuboid]) -> int:
    return reboot(filter_cuboids(cuboids, Range(-50, 50)))


def part01(input_file: str) -> int:
    return initialise(parse(input_file))


def part02(input_file: str) -> int:
    return 0
    # return reboot(parse(input_file))
