from aoc2021 import day07


def test_sample_day07_part01():
    assert "37" == day07.part01("sample")


def test_input_day07_part01():
    result: str = day07.part01("input")
    print(f"Day 07 Part 01 Result: {result}")


def test_sample_day07_part02():
    assert "168" == day07.part02("sample")


def test_input_day07_part02():
    result: str = day07.part02("input")
    print(f"Day 07 Part 02 Result: {result}")
