from aoc.year2021 import day07


def test_year2021_day07_part01_sample():
    assert 37 == day07.part01("sample")


def test_year2021_day07_part01_input():
    result: int = day07.part01("input")
    print(f"Day 07 Part 01 Result: {result}")


def test_year2021_day07_part02_sample():
    assert 168 == day07.part02("sample")


def test_year2021_day07_part02_input():
    result: int = day07.part02("input")
    print(f"Day 07 Part 02 Result: {result}")
