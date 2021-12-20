from aoc.year2021 import day20


def test_year2021_day20_part01_sample():
    assert 35 == day20.part01("sample")


def test_year2021_day20_part01_input():
    result: int = day20.part01("input")
    print(f"Day 20 Part 01 Result: {result}")


def test_year2021_day20_part02_sample():
    assert 3351 == day20.part02("sample")


def test_year2021_day20_part02_input():
    result: int = day20.part02("input")
    print(f"Day 20 Part 02 Result: {result}")
