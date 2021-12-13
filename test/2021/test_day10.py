from aoc.year2021 import day10


def test_year2021_day10_part01_sample():
    assert 26397 == day10.part01("sample")


def test_year2021_day10_part01_input():
    result: int = day10.part01("input")
    print(f"Day 10 Part 01 Result: {result}")


def test_year2021_day10_part02_sample():
    assert 288957 == day10.part02("sample")


def test_year2021_day10_part02_input():
    result: int = day10.part02("input")
    print(f"Day 10 Part 02 Result: {result}")
