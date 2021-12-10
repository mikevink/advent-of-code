from aoc2021 import day04


def test_sample_day04_part01():
    assert "4512" == day04.part01("sample")


def test_input_day04_part01():
    result: str = day04.part01("input")
    print(f"Day 04 Part 01 Result: {result}")


def test_sample_day04_part02():
    assert "1924" == day04.part02("sample")


def test_input_day04_part02():
    result: str = day04.part02("input")
    print(f"Day 04 Part 02 Result: {result}")
