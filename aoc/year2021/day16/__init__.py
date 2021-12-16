#!/usr/bin/env python
from abc import abstractmethod
from functools import reduce
from operator import mul

from aoc.common import input
from aoc.common import error

DAY: str = "2021/16"

HEX_TO_BINARY: dict[str, str] = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Packet:
    def __init__(self, version: int, type_: int):
        self.version: int = version
        self.type: int = type_

    def sum_version(self) -> int:
        return self.version

    @abstractmethod
    def get_value(self) -> int:
        pass

    def __str__(self) -> str:
        return f"{self.type}: {self.version}"


class Literal(Packet):
    def __init__(self, version: int, type_: int, value: int):
        super().__init__(version, type_)
        self.value: int = value

    def get_value(self) -> int:
        return self.value


class Operator(Packet):
    def __init__(self, version: int, type_: int, packets: list[Packet]):
        super().__init__(version, type_)
        self.packets: list[Packet] = packets

    def sum_version(self) -> int:
        return self.version + sum([p.sum_version() for p in self.packets])

    def get_value(self) -> int:
        values: list[int] = [p.get_value() for p in self.packets]
        if 0 == self.type:
            return sum(values)
        if 1 == self.type:
            return reduce(mul, values, 1)
        if 2 == self.type:
            return min(values)
        if 3 == self.type:
            return max(values)
        if 5 == self.type:
            return 1 if values[0] > values[1] else 0
        if 6 == self.type:
            return 1 if values[0] < values[1] else 0
        if 7 == self.type:
            return 1 if values[0] == values[1] else 0


def parse_literal(version: int, type_: int, binary: str) -> tuple[Literal, str]:
    i: int = 0
    payload: str = ""
    while i < len(binary):
        header: str = binary[i]
        payload = f"{payload}{binary[i + 1:i + 5]}"
        i += 5
        if "0" == header:
            break
    return Literal(version, type_, int(payload, 2)), binary[i:]


def parse_operator(version: int, type_: int, binary: str) -> tuple[Operator, str]:
    if "0" == binary[0]:
        num_bits: int = int(binary[1:16], 2)
        payload: str = binary[16 : 16 + num_bits]
        packets: list[Packet] = []
        while payload:
            packet, payload = parse(payload)
            packets.append(packet)
        return Operator(version, type_, packets), binary[16 + num_bits :]
    else:
        num_packets: int = int(binary[1:12], 2)
        payload: str = binary[12:]
        packets: list[Packet] = []
        for i in range(num_packets):
            if not payload:
                raise Exception("we seem to have run out of payload")
            packet, payload = parse(payload)
            packets.append(packet)
        return Operator(version, type_, packets), payload


def parse(binary: str) -> tuple[Packet, str]:
    version: int = int(binary[0:3], 2)
    type_: int = int(binary[3:6], 2)
    if 4 == type_:
        return parse_literal(version, type_, binary[6:])
    else:
        return parse_operator(version, type_, binary[6:])


def hex_to_binary(hex_: str) -> str:
    return "".join([HEX_TO_BINARY[h] for h in hex_])


def receive_transmission(input_data: str, from_file: bool) -> str:
    return hex_to_binary(input.load_lines(DAY, input_data)[0] if from_file else input_data)


def part01(input_data: str, from_file: bool) -> int:
    transmission: str = receive_transmission(input_data, from_file)
    packet, _ = parse(transmission)
    return packet.sum_version()


def part02(input_data: str, from_file: bool) -> int:
    transmission: str = receive_transmission(input_data, from_file)
    packet, _ = parse(transmission)
    return packet.get_value()
