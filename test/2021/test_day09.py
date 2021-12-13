from aoc.year2021 import day09


def test_year2021_day09_part01_sample():
    assert 15 == day09.part01("sample")


def test_year2021_day09_part01_input():
    result: int = day09.part01("input")
    print(f"Day 09 Part 01 Result: {result}")


def test_year2021_day09_part02_sample():
    assert 1134 == day09.part02("sample")


def test_year2021_day09_part02_input():
    result: int = day09.part02("input")
    print(f"Day 09 Part 02 Result: {result}")
