from aoc.common import input
from aoc.year2021 import day17


def test_year2021_day17_part01_sample():
    assert 45 == day17.part01("sample")


def test_year2021_day17_part01_input():
    result: int = day17.part01("input")
    print(f"Day 17 Part 01 Result: {result}")


def test_year2021_day17_part02_sample():
    assert 112 == day17.part02("sample")


def test_year2021_day17_part02_input():
    result: int = day17.part02("input")
    print(f"Day 17 Part 02 Result: {result}")
