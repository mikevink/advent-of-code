from aoc.year2021 import day18
from aoc.year2021.day18 import Node


def test_year2021_day18_parsing():
    assert "[1, 2]" == str(day18.parse("[1, 2]"))
    assert "[[1, 2], 3]" == str(day18.parse("[[1, 2], 3]"))
    assert "[9, [8, 7]]" == str(day18.parse("[9, [8, 7]]"))
    assert "[[1, 9], [8, 5]]" == str(day18.parse("[[1, 9], [8, 5]]"))
    assert "[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]" == str(day18.parse("[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]"))
    assert "[[[9, [3, 8]], [[0, 9], 6]], [[[3, 7], [4, 9]], 3]]" == str(
        day18.parse("[[[9, [3, 8]], [[0, 9], 6]], [[[3, 7], [4, 9]], 3]]")
    )
    assert "[[[[1, 3], [5, 3]], [[1, 3], [8, 7]]], [[[4, 9], [6, 9]], [[8, 2], [7, 3]]]]" == str(
        day18.parse("[[[[1, 3], [5, 3]], [[1, 3], [8, 7]]], [[[4, 9], [6, 9]], [[8, 2], [7, 3]]]]")
    )


def test_year2021_day18_chaining():
    def chain_string(node: Node) -> str:
        current: Node = node.rightmost()
        chain: str = ""
        while current is not None:
            chain = f"{current}{chain}"
            current = current.left
        return chain

    assert "12" == chain_string(day18.parse("[1, 2]"))
    assert "123" == chain_string(day18.parse("[[1, 2], 3]"))
    assert "987" == chain_string(day18.parse("[9, [8, 7]]"))
    assert "1985" == chain_string(day18.parse("[[1, 9], [8, 5]]"))
    assert "123456789" == chain_string(day18.parse("[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]"))
    assert "93809637493" == chain_string(
        day18.parse("[[[9, [3, 8]], [[0, 9], 6]], [[[3, 7], [4, 9]], 3]]")
    )
    assert "1353138749698273" == chain_string(
        day18.parse("[[[[1, 3], [5, 3]], [[1, 3], [8, 7]]], [[[4, 9], [6, 9]], [[8, 2], [7, 3]]]]")
    )


def test_year2021_day18_add_reduce():
    left: Node = day18.parse("[[[[4,3],4],4],[7,[[8,4],9]]]")
    right: Node = day18.parse("[1, 1]")
    total: Node = day18.add(left, right)
    assert "[[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]" == str(total)
    total.reduce()
    assert "[[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]" == str(total)


def test_year2021_day18_part01_sample():
    assert 4140 == day18.part01("sample")


def test_year2021_day18_part01_input():
    result: int = day18.part01("input")
    print(f"Day 18 Part 01 Result: {result}")


def test_year2021_day18_part02_sample():
    assert 3993 == day18.part02("sample")


def test_year2021_day18_part02_input():
    result: int = day18.part02("input")
    print(f"Day 18 Part 02 Result: {result}")
