from aoc.year2021 import day02


def test_year2021_day02_part01_sample():
    assert 150 == day02.part01("sample")


def test_year2021_day02_part01_input():
    result: int = day02.part01("input")
    print(f"Day 02 Part 01 Result: {result}")


def test_year2021_day02_part02_sample():
    assert 900 == day02.part02("sample")


def test_year2021_day02_part02_input():
    result: int = day02.part02("input")
    print(f"Day 02 Part 02 Result: {result}")
