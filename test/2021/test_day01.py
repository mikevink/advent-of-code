from aoc.year2021 import day01


def test_year2021_day01_part01_sample():
    assert "7" == day01.part01("sample")


def test_year2021_day01_part01_input():
    result: str = day01.part01("input")
    print(f"Day 01 Part 01 Result: {result}")


def test_year2021_day01_part02_sample():
    assert "5" == day01.part02("sample")


def test_year2021_day01_part02_input():
    result: str = day01.part02("input")
    print(f"Day 01 Part 02 Result: {result}")
