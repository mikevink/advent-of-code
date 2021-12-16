from aoc.year2021 import day16


def test_year2021_day16_part01_sample():
    assert 16 == day16.part01("8A004A801A8002F478", False)
    assert 12 == day16.part01("620080001611562C8802118E34", False)
    assert 23 == day16.part01("C0015000016115A2E0802F182340", False)
    assert 31 == day16.part01("A0016C880162017C3686B18A3D4780", False)


def test_year2021_day16_part01_input():
    result: int = day16.part01("input", True)
    print(f"Day 16 Part 01 Result: {result}")


def test_year2021_day16_part02_sample():
    assert 3 == day16.part02("C200B40A82", False)
    assert 54 == day16.part02("04005AC33890", False)
    assert 7 == day16.part02("880086C3E88112", False)
    assert 9 == day16.part02("CE00C43D881120", False)
    assert 1 == day16.part02("D8005AC2A8F0", False)
    assert 0 == day16.part02("F600BC2D8F", False)
    assert 0 == day16.part02("9C005AC2F8F0", False)
    assert 1 == day16.part02("9C0141080250320F1802104A08", False)


def test_year2021_day16_part02_input():
    result: int = day16.part02("input", True)
    print(f"Day 16 Part 02 Result: {result}")
