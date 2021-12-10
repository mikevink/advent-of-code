#!/usr/bin/env python

from aoc.common import error
from aoc.common import input

DAY: str = "2021/03"


def part01(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    numbits: int = len(lines[0])
    tracker: list[int] = [0] * numbits
    # track which bit is more frequent
    #  +1 for 1
    #  -1 for 0
    #  sign of value will tell us what to use
    for line in lines:
        for i in range(numbits):
            tracker[i] += 1 if "1" == line[i] else -1
    # build the binary representations of gamma and epsilon
    binary_gamma: str = ""
    binary_epsilon: str = ""
    for i in range(numbits):
        if 0 > tracker[i]:
            binary_gamma += "0"
            binary_epsilon += "1"
        elif 0 < tracker[i]:
            binary_gamma += "1"
            binary_epsilon += "0"
        else:
            return error.ERROR
    # convert to int
    gamma: int = int(binary_gamma, 2)
    epsilon: int = int(binary_epsilon, 2)
    power_consumption: int = gamma * epsilon
    return str(power_consumption)


def part02(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    numbits: int = len(lines[0])
    o2_index: int = -1
    co2_index: int = -1
    # possible candidates for the values of O2 and CO2
    o2_candidates: list[int] = list(range(len(lines)))
    co2_candidates: list[int] = list(range(len(lines)))
    # iterate through all the bits
    for i in range(numbits):
        # if we haven't found the O2 measurement
        if -1 == o2_index:
            # apply same tracking logic as in part 1, but only for this bit and only in the remaining candidates for O2
            tracker: int = 0
            for c in o2_candidates:
                tracker += 1 if "1" == lines[c][i] else -1
            keep: str = "0" if 0 > tracker else "1"
            # only keep the candidates whose ith bit matches the one determined above
            o2_candidates = [c for c in o2_candidates if keep == lines[c][i]]
            # if we only have one candidate left, we have a winner
            if 1 == len(o2_candidates):
                o2_index = o2_candidates[0]

        # if we haven't found the CO2 measurement
        if -1 == co2_index:
            # apply same tracking logic as in part 1, but only for this bit and only in the remaining candidates for CO2
            tracker: int = 0
            for c in co2_candidates:
                tracker += 1 if "1" == lines[c][i] else -1
            keep: str = "1" if 0 > tracker else "0"
            # only keep the candidates whose ith bit matches the one determined above
            co2_candidates = [c for c in co2_candidates if keep == lines[c][i]]
            # if we only have one candidate left, we have a winner
            if 1 == len(co2_candidates):
                co2_index = co2_candidates[0]
        # break if we have both
        if -1 != o2_index and -1 != co2_index:
            break
    o2: int = int(lines[o2_index], 2)
    co2: int = int(lines[co2_index], 2)
    life_support: int = o2 * co2
    return str(life_support)
