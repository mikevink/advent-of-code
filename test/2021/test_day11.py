from aoc.year2021 import day11


def test_year2021_day11_part01_sample():
    assert "1656" == day11.part01("sample", 100)


def test_year2021_day11_part01_input():
    result: str = day11.part01("input", 100)
    print(f"Day 11 Part 01 Result: {result}")


def test_year2021_day11_part02_sample():
    assert "195" == day11.part02("sample")


def test_year2021_day11_part02_input():
    result: str = day11.part02("input")
    print(f"Day 11 Part 02 Result: {result}")
