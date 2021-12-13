from aoc.year2021 import day05


def test_year2021_day05_part01_sample():
    assert 5 == day05.part01("sample")


def test_year2021_day05_part01_input():
    result: int = day05.part01("input")
    print(f"Day 05 Part 01 Result: {result}")


def test_year2021_day05_part02_sample():
    assert 12 == day05.part02("sample")


def test_year2021_day05_part02_input():
    result: int = day05.part02("input")
    print(f"Day 05 Part 02 Result: {result}")
