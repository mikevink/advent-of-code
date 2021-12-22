#!/usr/bin/env python
import re
from re import Pattern, Match
from typing import Optional

from aoc.common import input

DAY: str = "2021/22"


class Range:
    def __init__(self, min_: int, max_: int):
        self.min: int = min_
        self.max: int = max_

    @property
    def count(self) -> int:
        return self.max - self.min + 1

    def bound(self, bounds: 'Range') -> Optional['Range']:
        if bounds.max < self.min or bounds.min > self.max:
            return None
        min_: int = self.min if self.min >= bounds.min else bounds.min
        max_: int = self.max if self.max <= bounds.max else bounds.max
        return Range(min_, max_)

    def intersect(self, other: 'Range') -> Optional['Range']:
        min_: int = max(self.min, other.min)
        max_: int = min(self.max, other.max)
        if 0 <= max_ - min_:
            return Range(min_, max_)
        return None

    def range(self) -> range:
        return range(self.min, self.max + 1)

    def __str__(self) -> str:
        return f"[{self.min}, {self.max}]"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: 'Range') -> bool:
        return self.min == other.min and self.max == other.max


class Cuboid:
    @staticmethod
    def parse(line: str) -> 'Cuboid':
        pattern: Pattern = re.compile(r"(\w+) x=(-*\d+)..(-*\d+),y=(-*\d+)..(-*\d+),z=(-*\d+)..(-*\d+)")
        result: Match = pattern.search(line)
        return Cuboid(
            "input",
            1 if "on" == result.group(1) else -1,
            Range(int(result.group(2)), int(result.group(3))),
            Range(int(result.group(4)), int(result.group(5))),
            Range(int(result.group(6)), int(result.group(7))),
        )

    def __init__(self, label: str, state: int, x: Range, y: Range, z: Range):
        self.label: str = label
        self.state: int = state
        self.x: Range = x
        self.y: Range = y
        self.z: Range = z

    @property
    def count(self) -> int:
        return self.x.count * self.y.count * self.z.count

    @property
    def state_changes(self) -> int:
        return self.state * self.count

    def bound(self, bounds: Range) -> Optional['Cuboid']:
        x: Optional[Range] = self.x.bound(bounds)
        y: Optional[Range] = self.y.bound(bounds)
        z: Optional[Range] = self.z.bound(bounds)
        if x is None or y is None or z is None:
            return None
        return Cuboid("bounded", self.state, x, y, z)

    def intersect(self, other: 'Cuboid') -> Optional['Cuboid']:
        x: Optional[Range] = self.x.intersect(other.x)
        y: Optional[Range] = self.y.intersect(other.y)
        z: Optional[Range] = self.z.intersect(other.z)
        if x and y and z:
            # reverse the state, to cancel out self
            return Cuboid("intersection", -1 * self.state, x, y, z)
        return None

    def __str__(self) -> str:
        return f"{{{self.label}: {self.state} {self.x}, {self.y}, {self.z}}}"

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
    # this only works because we know the first step is always 'on'
    filtered: list[Cuboid] = [cuboids.pop(0)]
    for cuboid in cuboids:
        # check the current cuboid against all the ones we've seen so far
        lenf: int = len(filtered)
        for i in range(lenf):
            intersection: Optional[Cuboid] = filtered[i].intersect(cuboid)
            if intersection:
                # if we have an intersection, add it to the list
                # each intersection negates the existing state of the cube, bringing it back to 'off'
                filtered.append(intersection)
        # add the current cuboid if it's 'on'
        if 1 == cuboid.state:
            filtered.append(cuboid)
    return sum(map(lambda c: c.state_changes, filtered))


def initialise(cuboids: list[Cuboid]) -> int:
    return reboot(filter_cuboids(cuboids, Range(-50, 50)))


def part01(input_file: str) -> int:
    return initialise(parse(input_file))


def part02(input_file: str) -> int:
    return reboot(parse(input_file))
