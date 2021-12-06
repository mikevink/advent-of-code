#!/usr/bin/env python

from aoc2021 import input
from aoc2021 import error

DAY: str = "02"

def part01(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    position: int = 0
    depth: int = 0
    for line in lines:
        modifier, value = line.split(" ")
        value = int(value)
        if "forward" == modifier:
            position += value
        elif "up" == modifier:
            depth -= value
        elif "down" == modifier:
            depth += value
        else:
            return error.ERROR 
    return str(position * depth)

def part02(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    position: int = 0
    depth: int = 0
    aim: int = 0
    for line in lines:
        modifier, value = line.split(" ")
        value = int(value)
        if "forward" == modifier:
            position += value
            depth += aim * value
        elif "up" == modifier:
            aim -= value
        elif "down" == modifier:
            aim += value
        else:
            return error.ERROR 
    return str(position * depth)
