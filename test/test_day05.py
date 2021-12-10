from aoc2021 import day05


def test_sample_day05_part01():
    assert "5" == day05.part01("sample")


def test_input_day05_part01():
    result: str = day05.part01("input")
    print(f"Day 05 Part 01 Result: {result}")


def test_sample_day05_part02():
    assert "12" == day05.part02("sample")


def test_input_day05_part02():
    result: str = day05.part02("input")
    print(f"Day 05 Part 02 Result: {result}")
