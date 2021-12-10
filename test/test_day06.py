from aoc2021 import day06


def test_sample_day06_part01():
    assert "5934" == day06.part01("sample")


def test_input_day06_part01():
    result: str = day06.part01("input")
    print(f"Day 06 Part 01 Result: {result}")


def test_sample_day06_part02():
    assert "26984457539" == day06.part02("sample")


def test_input_day06_part02():
    result: str = day06.part02("input")
    print(f"Day 06 Part 02 Result: {result}")
