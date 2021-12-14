from aoc.year2021 import day14


def test_year2021_day14_part01_sample():
    assert 1588 == day14.part01("sample")


def test_year2021_day14_part01_input():
    result: int = day14.part01("input")
    print(f"Day 14 Part 01 Result: {result}")


def test_year2021_day14_part02_sample():
    assert 2188189693529 == day14.part02("sample")


def test_year2021_day14_part02_input():
    result: int = day14.part02("input")
    print(f"Day 14 Part 02 Result: {result}")
