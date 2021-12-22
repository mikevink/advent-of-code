from aoc.year2021 import day21


def test_year2021_day21_part01_sample():
    assert 739785 == day21.part01("sample")


def test_year2021_day21_part01_input():
    result: int = day21.part01("input")
    print(f"Day 21 Part 01 Result: {result}")
    assert 897798 == result


def test_year2021_day21_part02_sample():
    assert 444356092776315 == day21.part02("sample")


def test_year2021_day21_part02_input():
    result: int = day21.part02("input")
    print(f"Day 21 Part 02 Result: {result}")
