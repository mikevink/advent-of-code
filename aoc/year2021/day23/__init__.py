#!/usr/bin/env python
from collections import namedtuple, deque
from copy import deepcopy
from typing import Optional

from aoc.common import error
from aoc.common import input

DAY: str = "2021/23"
DESTINATIONS: dict[str, int] = {"A": 2, "B": 4, "C": 6, "D": 8}
SNOITANITSED: dict[int, str] = {2: "A", 4: "B", 6: "C", 8: "D", -1: "-"}
COSTS: dict[int, int] = {2: 1, 4: 10, 6: 100, 8: 1000}
HALLWAY: int = 0
HALLWAY_SPACES: int = 11
HALLWAY_AVAILABLE: list[int] = [0, 1, 3, 5, 7, 9, 10]
ROOMS: list[int] = [2, 4, 6, 8]
TOP: int = 1
BOTTOM: int = 2
INVALID: int = 0
FREE: int = -1
INFINITY: int = -1


class Coords:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.str: str = f"({self.x}, {self.y})"
        self.hash: int = hash(self.__str__())

    def manhattan(self, other: "Coords") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self) -> str:
        return self.str

    def __eq__(self, other: "Coords") -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: "Coords") -> bool:
        if self.x < other.x:
            return True
        if self.x == other.x:
            return self.y < other.y
        return False

    def __le__(self, other: "Coords") -> bool:
        return self < other or self == other

    def __gt__(self, other: "Coords") -> bool:
        if self.x > other.x:
            return True
        if self.x == other.x:
            return self.y > other.y
        return False

    def __ge__(self, other: "Coords") -> bool:
        return self == other or self > other

    def __hash__(self) -> int:
        return self.hash


class Hallway:
    def __init__(self, occupied: dict[int, int] = None):
        occupied = {} if occupied is None else occupied
        self.spaces: dict[int, bool] = {
            i: i not in occupied for i in HALLWAY_AVAILABLE
        }
        reprs: list[str] = [" "] * HALLWAY_SPACES
        for i, v in self.spaces.items():
            if not v:
                reprs[i] = SNOITANITSED[occupied[i]]
            else:
                reprs[i] = "-"
        reprs = [r for r in reprs if r.strip()]
        self.str: str = f"[{' '.join(reprs)}]"

    def available(self, from_room: int) -> list[int]:
        available: list[int] = []
        for i in range(from_room, -1, -1):
            if i in self.spaces:
                if not self.spaces[i]:
                    break
                available.append(i)
        for i in range(from_room + 1, HALLWAY_SPACES):
            if i in self.spaces:
                if not self.spaces[i]:
                    break
                available.append(i)
        return available

    def free(self, start: int, end: int, in_hallway: bool = False) -> bool:
        if start > end:
            start, end = end, start
            if in_hallway:
                end -= 1
        else:
            if in_hallway:
                start += 1
        for i in range(start, end + 1):
            if i in self.spaces and not self.spaces[i]:
                return False
        return True

    def __str__(self) -> str:
        return self.str


class Room:
    def __init__(self, inx: int):
        self.inx: int = inx
        self.top: int = FREE
        self.bottom: int = FREE

    def bottom_ok(self) -> bool:
        return self.inx == self.bottom

    def top_occupied(self) -> bool:
        return FREE != self.top

    def free(self) -> int:
        if FREE != self.top:
            return INVALID
        if FREE == self.bottom:
            return BOTTOM
        if self.inx == self.bottom:
            return TOP
        return INVALID

    def fill(self, x: int, destination: int):
        if TOP == x:
            self.top = destination
        else:
            self.bottom = destination

    def __str__(self) -> str:
        return f"[{SNOITANITSED[self.top]} {SNOITANITSED[self.bottom]}]"


class Amphipod:
    def __init__(self, position: Coords, destination: int, moved: bool = False, distance: int = 0):
        self.position: Coords = position
        self.destination: int = destination
        self.moved: bool = moved
        self.distance: int = distance
        self.str: str = f"{self.destination} @ {self.position}"
        self.hash: int = hash(f"{self.destination} @ {self.position}")

    def moves(self, rooms: dict[int, Room], hallway: Hallway) -> list['Amphipod']:
        if not self.moved:  # state == still in starting room
            if self.position.y == self.destination:  # if initial room == destination room
                # if I'm the one at the bottom or the one at the bottom is also at destination
                if self.position.x == BOTTOM or rooms[self.destination].bottom_ok():
                    return []  # do bugger all
            # if I'm at the bottom and the top isn't free
            if self.position.x == BOTTOM and rooms[self.position.y].top_occupied():
                return []  # can't move
            # ok, I can move now, let's go
            available: list[int] = hallway.available(self.position.y)
            amphipods: list[Amphipod] = []
            for a in available:
                amphipods.append(self.move(HALLWAY, a))
            # actually, is my room free?
            room_space: int = rooms[self.destination].free()
            if room_space:
                # it is, can I get there?
                if hallway.free(self.position.y, self.destination):
                    # sweet, let's put that as an option as well
                    amphipods.append(self.move(room_space, self.destination))
            return amphipods
        # if I have moved
        if HALLWAY == self.position.x:  # I'm on the hallway, great
            room_space: int = rooms[self.destination].free()
            if room_space:
                # it is, can I get there?
                if hallway.free(self.position.y, self.destination, True):
                    # sweet, let's put that as an option as well
                    return [self.move(room_space, self.destination)]
        return []

    def move(self, x: int, y: int) -> 'Amphipod':
        moved_position: Coords = Coords(x, y)
        if HALLWAY != self.position.x:
            entrance = Coords(HALLWAY, moved_position.y)
            distance: int = self.position.manhattan(entrance) + entrance.manhattan(moved_position)
        else:
            distance: int = self.position.manhattan(moved_position)
        return Amphipod(moved_position, self.destination, moved=True, distance=distance)

    def __str__(self) -> str:
        return self.str

    def __eq__(self, other: 'Amphipod') -> bool:
        return self.destination == other.destination and self.position == other.position

    def __lt__(self, other: "Amphipod") -> bool:
        if self.destination < other.destination:
            return True
        if self.destination == other.destination:
            return self.position < other.position
        return False

    def __le__(self, other: "Amphipod") -> bool:
        return self < other or self == other

    def __gt__(self, other: "Amphipod") -> bool:
        if self.destination > other.destination:
            return True
        if self.destination == other.destination:
            return self.position > other.position
        return False

    def __ge__(self, other: "Amphipod") -> bool:
        return self == other or self > other

    def __hash__(self) -> int:
        return self.hash


def copypods(amphipods: dict[int, Amphipod], inx: int, amphipod: Amphipod) -> dict[int, Amphipod]:
    return {i: amphipod if inx == i else a for i, a in amphipods.items()}


class State:
    def __init__(self, amphipods: dict[int, Amphipod], cost: int = 0):
        self.amphipods: dict[int, Amphipod] = amphipods
        self.hallway: Hallway = Hallway(
            {a.position.y: a.destination for a in amphipods.values() if HALLWAY == a.position.x}
        )
        self.rooms: dict[int, Room] = {}
        for a in amphipods.values():
            if a.position.y in ROOMS:
                if a.position.y not in self.rooms:
                    self.rooms[a.position.y] = Room(a.position.y)
                self.rooms[a.position.y].fill(a.position.x, a.destination)
        for room in ROOMS:
            if room not in self.rooms:
                self.rooms[room] = Room(room)
        self.cost: int = cost
        room_str: list[str] = [str(self.rooms[k]) for k in ROOMS]
        self.str: str = f"{self.hallway} {' '.join(room_str)}"
        self.hash: int = hash(self.str)

    def eq(self, as_str: str) -> bool:
        return self.str == as_str

    def moves(self) -> list['State']:
        neighbours: list['State'] = []
        for i in self.amphipods:
            next_amphipods: list[Amphipod] = self.amphipods[i].moves(self.rooms, self.hallway)
            for next_amphipod in next_amphipods:
                cost: int = next_amphipod.distance * COSTS[next_amphipod.destination]
                neighbours.append(State(copypods(self.amphipods, i, next_amphipod), cost))
        return neighbours

    def __sub__(self, other: 'State') -> int:
        diff: int = 0
        for inx in self.amphipods:
            diff += 0 if self.amphipods[inx] == other.amphipods[inx] else 1
        return diff

    def __str__(self) -> str:
        return f"{self.str} = {self.cost}"

    def __eq__(self, other: 'State') -> bool:
        return set(self.amphipods.values()) == set(other.amphipods.values())

    def __hash__(self) -> int:
        return self.hash


def group_add(by_group: dict[int, deque[State]], group: int, value: State):
    if group not in by_group:
        by_group[group] = deque([value])
    else:
        by_group[group].append(value)


def group_clear(by_group: dict[int, deque[State]], group: int, value: State):
    if group in by_group:
        if value in by_group[group]:
            by_group[group].remove(value)
            if not by_group[group]:
                del by_group[group]


def group_min(by_group: dict[int, deque[State]]) -> State:
    if not by_group:
        raise Exception("boom")
    min_: int = min(by_group.keys())
    value: State = by_group[min_].popleft()
    if not by_group[min_]:
        del by_group[min_]
    return value


class Trail:
    def __init__(self, trail: list[State] = None):
        self.trail: list[State] = trail
        self.inx: int = 0

    @property
    def target(self) -> State:
        return self.trail[-1]

    def next(self) -> State:
        state: State = self.trail[self.inx]
        self.inx += 1
        return state

    def add(self, inx: int, x: int, y: int):
        amphipods: dict[int, Amphipod] = deepcopy(self.trail[-1].amphipods)
        amphipods[inx] = amphipods[inx].move(x, y)
        state: State = State(amphipods)
        self.trail.append(state)


def dijktra_generator(root: State, target: State) -> int:
    visited: set[State] = set()
    distances: dict[State, int] = {root: 0}
    by_distance: dict[int, deque[State]] = {}
    current: State = root
    while True:
        if target == current:
            break
        for node in current.moves():
            if node not in visited:
                may_dist: int = distances[current] + node.cost
                node_dist: int = distances.get(node, INFINITY)
                if INFINITY == node_dist or may_dist < node_dist:
                    group_clear(by_distance, node_dist, node)
                    group_add(by_distance, may_dist, node)
                    distances[node] = may_dist
        del distances[current]
        visited.add(current)

        current = group_min(by_distance)

    return distances[target]


def parse(input_file: str) -> State:
    lines: list[str] = input.load_lines(DAY, input_file, strip=False)
    amphipods: dict[int, Amphipod] = {}
    inx: int = 0
    for l in [2, 3]:
        for i in range(len(lines[l])):
            destination: int = DESTINATIONS.get(lines[l][i])
            if destination:
                # we -1 the i and the l because the discard the first row and column of the input
                amphipods[inx] = Amphipod(Coords(l - 1, i - 1), destination)
                inx += 1
    return State(amphipods)


def part01(input_file: str) -> int:
    root: State = parse(input_file)
    target: State = parse("target")

    # target_base: State = parse(input_file)
    # trail: Trail = Trail([target_base])
    # trail.add(2, HALLWAY, 3)
    # trail.add(1, 1, 6)
    # trail.add(5, HALLWAY, 5)
    # trail.add(2, 2, 4)
    # trail.add(0, 1, 4)
    # trail.add(3, HALLWAY, 7)
    # trail.add(7, HALLWAY, 9)
    # trail.add(3, 2, 8)
    # trail.add(5, 1, 8)
    # trail.add(7, 1, 2)

    return dijktra_generator(root, target)


def part02(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    return error.ERROR
