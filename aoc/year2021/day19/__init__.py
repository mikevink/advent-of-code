#!/usr/bin/env python
from collections import deque
from typing import Callable, Optional

from aoc.common import input
from aoc.common import error

DAY: str = "2021/19"


class Coords:
    def __init__(self, x: int, y: int, z: int):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.str: str = f"({self.x}, {self.y}, {self.z})"
        self.hash: int = hash(self.str)

    def manhattan(self, other: 'Coords') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __add__(self, other: 'Coords') -> 'Coords':
        return Coords(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Coords') -> 'Coords':
        return Coords(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: 'Coords') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return self.hash

    def __str__(self) -> str:
        return self.str


ORIENTATIONS: list[Callable[[Coords], Coords]] = [
    lambda c: Coords(c.x, c.y, c.z),  # a,  b,  c
    lambda c: Coords(c.x, -c.z, c.y),  # a, -c,  b
    lambda c: Coords(c.x, -c.y, -c.z),  # a, -b, -c
    lambda c: Coords(c.x, c.z, -c.y),  # a,  c, -b

    lambda c: Coords(-c.x, -c.y, c.z),  # -a, -b,  c
    lambda c: Coords(-c.x, c.z, c.y),  # -a,  c,  b
    lambda c: Coords(-c.x, c.y, -c.z),  # -a,  b, -c
    lambda c: Coords(-c.x, -c.z, -c.y),  # -a, -c, -b

    lambda c: Coords(c.y, -c.x, c.z),  # b, -a,  c
    lambda c: Coords(c.y, c.z, c.x),  # b,  c,  a
    lambda c: Coords(c.y, c.x, -c.z),  # b,  a, -c
    lambda c: Coords(c.y, -c.z, -c.x),  # b, -c, -a

    lambda c: Coords(-c.y, c.x, c.z),  # -b,  a,  c
    lambda c: Coords(-c.y, -c.z, c.x),  # -b, -c,  a
    lambda c: Coords(-c.y, -c.x, -c.z),  # -b, -a, -c
    lambda c: Coords(-c.y, c.z, -c.x),  # -b,  c, -a

    lambda c: Coords(c.z, c.x, c.y),  # c,  a,  b
    lambda c: Coords(c.z, -c.y, c.x),  # c, -b,  a
    lambda c: Coords(c.z, -c.x, -c.y),  # c, -a, -b
    lambda c: Coords(c.z, c.y, -c.x),  # c,  b, -a

    lambda c: Coords(-c.z, -c.x, c.y),  # -c, -a,  b
    lambda c: Coords(-c.z, c.y, c.x),  # -c,  b,  a
    lambda c: Coords(-c.z, c.x, -c.y),  # -c,  a, -b
    lambda c: Coords(-c.z, -c.y, -c.x),  # -c, -b, -a
]


class Scanner:
    def __init__(self, label: str):
        self.label: str = label.replace("-", "").strip()
        self.beacons: list[Coords] = []

    def register(self, beacon_: str):
        x, y, z = beacon_.strip().split(",")
        self.beacons.append(Coords(int(x), int(y), int(z)))

    def __str__(self) -> str:
        return f"{self.label}: [{', '.join([str(b) for b in self.beacons])}]"


class TrenchMap:
    def __init__(self, root: Scanner):
        self.scanners: dict[Coords, str] = {
            Coords(0, 0, 0): root.label
        }
        self.beacons: set[Coords] = set(root.beacons)

    def map(self, scanner: Scanner) -> Optional[Scanner]:
        for orientation in ORIENTATIONS:
            beacons: list[Coords] = [orientation(beacon) for beacon in scanner.beacons]
            votes: dict[Coords, int] = {}
            for trench_beacon in self.beacons:
                for beacon in beacons:
                    diff: Coords = trench_beacon - beacon
                    if diff not in votes:
                        votes[diff] = 1
                    else:
                        votes[diff] += 1
            winner: Coords = max(votes, key=votes.get)
            if 11 < votes[winner]:
                self.add(scanner.label, winner, beacons)
                return None
        return scanner

    def add(self, scanner: str, at: Coords, beacons: list[Coords]):
        self.scanners[at] = scanner
        self.beacons.update({beacon + at for beacon in beacons})


def parse(input_file: str) -> deque[Scanner]:
    lines: list[str] = input.load_lines(DAY, input_file)
    scanners: deque[Scanner] = deque()
    # noinspection PyTypeChecker
    current: Scanner = None
    for line in lines:
        if line.startswith("---"):
            current = Scanner(line)
        elif 0 == len(line.strip()):
            scanners.append(current)
        else:
            current.register(line)
    scanners.append(current)
    return scanners


def map_trench(input_file: str) -> TrenchMap:
    scanners: deque[Scanner] = parse(input_file)
    trench: TrenchMap = TrenchMap(scanners.popleft())
    while scanners:
        unmappable: Optional[Scanner] = trench.map(scanners.popleft())
        if unmappable is not None:
            scanners.append(unmappable)
    return trench


def part01(input_file: str) -> int:
    trench: TrenchMap = map_trench(input_file)
    return len(trench.beacons)


def part02(input_file: str) -> int:
    trench: TrenchMap = map_trench(input_file)
    manhattans: set[int] = set()
    for a in trench.scanners:
        for b in trench.scanners:
            if a != b:
                manhattans.add(a.manhattan(b))
    return max(manhattans)
