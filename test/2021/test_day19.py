from aoc.year2021 import day19


def test_year2021_day19_part01_sample():
    assert 79 == day19.part01("sample")


def test_year2021_day19_part01_input():
    result: int = day19.part01("input")
    print(f"Day 19 Part 01 Result: {result}")


def test_year2021_day19_part02_sample():
    assert 3621 == day19.part02("sample")


def test_year2021_day19_part02_input():
    result: int = day19.part02("input")
    print(f"Day 19 Part 02 Result: {result}")
