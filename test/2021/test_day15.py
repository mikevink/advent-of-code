from aoc.common.input import load_lines
from aoc.year2021 import day15


def test_year2021_day15_part01_sample():
    assert 40 == day15.part01("sample")


def test_year2021_day15_part01_input():
    result: int = day15.part01("input")
    print(f"Day 15 Part 01 Result: {result}")


def test_year2021_day15_part02_sample():
    assert 315 == day15.part02("sample")


def test_year2021_day15_part02_input():
    result: int = day15.part02("input")
    print(f"Day 15 Part 02 Result: {result}")


def test_year2021_day15_generate_map():
    generated: list[list[int]] = day15.generate_map("sample")
    expected: list[str] = load_lines(day15.DAY, "part2_generated")
    for i in range(len(expected)):
        line: str = expected[i]
        gline: str = "".join(map(str, generated[i]))
        assert line == gline
