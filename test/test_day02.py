from aoc2021 import day02


def test_sample_day02_part01():
    assert "150" == day02.part01("sample")


def test_input_day02_part01():
    result: str = day02.part01("input")
    print(f"Day 02 Part 01 Result: {result}")


def test_sample_day02_part02():
    assert "900" == day02.part02("sample")


def test_input_day02_part02():
    result: str = day02.part02("input")
    print(f"Day 02 Part 02 Result: {result}")
