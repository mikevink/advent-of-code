from aoc2021 import day03

def test_sample_day03_part01():
    assert "198" == day03.part01("sample")

def test_input_day03_part01():
    result: str = day03.part01("input")
    print(f"Day 03 Part 01 Result: {result}")

def test_sample_day03_part02():
    assert "230" == day03.part02("sample")

def test_input_day03_part02():
    result: str = day03.part02("input")
    print(f"Day 03 Part 02 Result: {result}")
