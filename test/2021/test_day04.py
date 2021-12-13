from aoc.year2021 import day04


def test_year2021_day04_part01_sample():
    assert 4512 == day04.part01("sample")


def test_year2021_day04_part01_input():
    result: int = day04.part01("input")
    print(f"Day 04 Part 01 Result: {result}")


def test_year2021_day04_part02_sample():
    assert 1924 == day04.part02("sample")


def test_year2021_day04_part02_input():
    result: int = day04.part02("input")
    print(f"Day 04 Part 02 Result: {result}")
