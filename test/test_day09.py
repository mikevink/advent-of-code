from aoc2021 import day09

def test_sample_day09_part01():
    assert "15" == day09.part01("sample")

def test_input_day09_part01():
    result: str = day09.part01("input")
    print(f"Day 09 Part 01 Result: {result}")

def test_sample_day09_part02():
    assert "1134" == day09.part02("sample")

def test_input_day09_part02():
    result: str = day09.part02("input")
    print(f"Day 09 Part 02 Result: {result}")
