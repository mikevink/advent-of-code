from aoc.year2021 import day13


def test_year2021_day13_part01_sample():
    assert 17 == day13.part01("sample")


def test_year2021_day13_part01_input():
    result: int = day13.part01("input")
    print(f"Day 13 Part 01 Result: {result}")


def test_year2021_day13_part02_sample():
    assert "#####\n#   #\n#   #\n#   #\n#####\n     \n     " == day13.part02("sample")


def test_year2021_day13_part02_input():
    result: str = day13.part02("input")
    print(f"Day 13 Part 02 Result: \n{result}")
