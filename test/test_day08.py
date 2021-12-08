from aoc2021 import day08

def test_sample_day08_part01():
    assert "26" == day08.part01("sample")

def test_input_day08_part01():
    result: str = day08.part01("input")
    print(f"Day 08 Part 01 Result: {result}")

def test_sample_day08_part02():
    assert "61229" == day08.part02("sample")

def test_input_day08_part02():
    result: str = day08.part02("input")
    print(f"Day 08 Part 02 Result: {result}")
