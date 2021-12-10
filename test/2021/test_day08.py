from aoc.year2021 import day08


def test_year2021_day08_part01_sample():
    assert "26" == day08.part01("sample")


def test_year2021_day08_part01_input():
    result: str = day08.part01("input")
    print(f"Day 08 Part 01 Result: {result}")


def test_year2021_day08_part02_sample():
    assert "61229" == day08.part02("sample")


def test_year2021_day08_part02_input():
    result: str = day08.part02("input")
    print(f"Day 08 Part 02 Result: {result}")
