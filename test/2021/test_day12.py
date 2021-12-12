from aoc.year2021 import day12


def test_year2021_day12_part01_sample():
    assert "10" == day12.part01("sample")


def test_year2021_day12_part01_sample1():
    assert "19" == day12.part01("sample1")


def test_year2021_day12_part01_sample2():
    assert "226" == day12.part01("sample2")


def test_year2021_day12_part01_input():
    result: str = day12.part01("input")
    print(f"Day 12 Part 01 Result: {result}")


def test_year2021_day12_part02_sample():
    assert "36" == day12.part02("sample")


def test_year2021_day12_part02_sample1():
    assert "103" == day12.part02("sample1")


def test_year2021_day12_part02_sample2():
    assert "3509" == day12.part02("sample2")


def test_year2021_day12_part02_input():
    result: str = day12.part02("input")
    print(f"Day 12 Part 02 Result: {result}")
