from aoc.year2021 import day22
from aoc.year2021.day22 import Cuboid, Range


def test_year2021_day22_parsing():
    assert Cuboid(
        1, Range(-20, 26), Range(-36, 17), Range(-47, 7)
    ) == Cuboid.parse("on x=-20..26,y=-36..17,z=-47..7")
    assert Cuboid(
        0, Range(-54112, -39298), Range(-85059, -49293), Range(-27449, 7877)
    ) == Cuboid.parse("off x=-54112..-39298,y=-85059..-49293,z=-27449..7877")


def test_year2021_day22_part01_bounding():
    bounds: Range = Range(-50, 50)
    in_bounds: Cuboid = Cuboid.parse("on x=-20..26,y=-36..17,z=-47..7")
    partial_bounds: Cuboid = Cuboid.parse("on x=-70..26,y=-66..67,z=-50..7")
    out_of_bounds: Cuboid = Cuboid.parse("off x=-54112..-39298,y=-85059..-49293,z=-27449..7877")

    assert Cuboid.parse("on x=-20..26,y=-36..17,z=-47..7") == in_bounds.bound(bounds)
    assert Cuboid.parse("on x=-50..26,y=-50..50,z=-50..7") == partial_bounds.bound(bounds)
    assert out_of_bounds.bound(bounds) is None


def test_year2021_day22_part01_filtering():
    cuboids: list[Cuboid] = day22.parse("sample")
    assert 22 == len(cuboids)
    filtered: list[Cuboid] = day22.filter_cuboids(cuboids, Range(-50, 50))
    assert 20 == len(filtered)


def test_year2021_day22_part01_sample():
    assert 590784 == day22.part01("sample")


def test_year2021_day22_part01_input():
    result: int = day22.part01("input")
    print(f"Day 22 Part 01 Result: {result}")


def test_year2021_day22_part02_sample():
    assert 2758514936282235 == day22.part02("sample")


def test_year2021_day22_part02_input():
    result: int = day22.part02("input")
    print(f"Day 22 Part 02 Result: {result}")
