from aoc.year2021 import day03


def test_year2021_day03_part01_sample():
    assert "198" == day03.part01("sample")


def test_year2021_day03_part01_input():
    result: str = day03.part01("input")
    print(f"Day 03 Part 01 Result: {result}")


def test_year2021_day03_part02_sample():
    assert "230" == day03.part02("sample")


def test_year2021_day03_part02_input():
    result: str = day03.part02("input")
    print(f"Day 03 Part 02 Result: {result}")
