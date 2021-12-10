from aoc.year2021 import day06


def test_year2021_day06_part01_sample():
    assert "5934" == day06.part01("sample")


def test_year2021_day06_part01_input():
    result: str = day06.part01("input")
    print(f"Day 06 Part 01 Result: {result}")


def test_year2021_day06_part02_sample():
    assert "26984457539" == day06.part02("sample")


def test_year2021_day06_part02_input():
    result: str = day06.part02("input")
    print(f"Day 06 Part 02 Result: {result}")
