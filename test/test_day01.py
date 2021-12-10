from aoc2021 import day01


def test_sample_day01_part01():
    assert "7" == day01.part01("sample")


def test_input_day01_part01():
    result: str = day01.part01("input")
    print(f"Day 01 Part 01 Result: {result}")


def test_sample_day01_part02():
    assert "5" == day01.part02("sample")


def test_input_day01_part02():
    result: str = day01.part02("input")
    print(f"Day 01 Part 02 Result: {result}")
