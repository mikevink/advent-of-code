from aoc.year2021 import day23
from aoc.year2021.day23 import ROOMS, Room, Hallway, Amphipod, Coords, HALLWAY


def test_year2021_day23_distance_calculation():
    a: Amphipod = Amphipod(Coords(1, 2), 4)
    assert 3 == a.move(HALLWAY, 0).distance
    assert 8 == a.move(HALLWAY, 9).distance
    assert 4 == a.move(1, 4).distance
    assert 5 == a.move(2, 4).distance


def test_year2021_day23_part01_sample():
    assert 12521 == day23.part01("sample")


def test_year2021_day23_part01_input():
    result: int = day23.part01("input")
    print(f"Day 23 Part 01 Result: {result}")


def test_year2021_day23_part02_sample():
    assert "-" == day23.part02("sample")


def test_year2021_day23_part02_input():
    result: int = day23.part02("input")
    print(f"Day 23 Part 02 Result: {result}")
