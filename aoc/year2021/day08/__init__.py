#!/usr/bin/env python

from aoc.common import input

DAY: str = "2021/08"

NUMBERS: dict[str, str] = {
    "1110111": "0",
    "0010010": "1",
    "1011101": "2",
    "1011011": "3",
    "0111010": "4",
    "1101011": "5",
    "1101111": "6",
    "1010010": "7",
    "1111111": "8",
    "1111011": "9",
}

EXPECTED: set[str] = set(NUMBERS.keys())


def parse(input_file: str) -> list[(list[str], list[str])]:
    lines: list[str] = input.load_lines(DAY, input_file)
    observations: list[(list[str], list[str])] = []
    for line in lines:
        patterns, output = line.split(" | ")
        observations.append((patterns.split(" "), output.split(" ")))
    return observations


def part01(input_file: str) -> int:
    observations: list[(list[str], list[str])] = parse(input_file)
    count: int = 0
    for observation in observations:
        output: list[str] = observation[1]
        for o in output:
            l: int = len(o)
            if l in [2, 3, 4, 7]:
                count += 1
    return count


def map_patterns(patterns: list[str], mapping: dict[str, int]) -> set[str]:
    maybe: set[str] = set()
    for pattern in patterns:
        array: list[str] = ["0"] * 7
        for c in pattern:
            array[mapping[c]] = "1"
        maybe.add("".join(array))
    return maybe


def map_output(output: list[str], mapping: dict[str, int]) -> int:
    total: str = ""
    for o in output:
        array: list[str] = ["0"] * 7
        for c in o:
            array[mapping[c]] = "1"
        total += NUMBERS["".join(array)]
    return int(total)


def solve(patterns: list[str], output: list[str]) -> int:
    uniques: dict[int, str] = {}
    for pattern in patterns:
        lenp: int = len(pattern)
        if lenp in [2, 3, 4, 7]:
            uniques[lenp] = pattern
        if 4 == len(uniques):
            break
    # keep a track of all the characters whose value we sort of know
    known: set[str] = set()
    # 2 == len(pattern) => pattern represents number 1
    one: list[str] = list(uniques[2])
    one_options: list[dict[str, int]] = [{one[0]: 2, one[1]: 5}, {one[0]: 5, one[1]: 2}]
    known.update(one)
    # 3 == len(pattern) => pattern represents number 7.
    #   seven shares two characters with 1, so we can ignore those, giving us one clear answer
    seven: list[str] = [c for c in uniques[3] if c not in known]
    seven_value: dict[str, int] = {seven[0]: 0}
    known.update(seven)
    # 4 == len(pattern) => pattern represents number 4.
    #   this also shares two characters with 1, but also has two unknowns. so same pattern
    four: list[str] = [c for c in uniques[4] if c not in known]
    four_options: list[dict[str, int]] = [
        {four[0]: 1, four[1]: 3},
        {four[0]: 3, four[1]: 1},
    ]
    known.update(four)
    # 7 == len(pattern) => finally, we get to number 8.
    #   same rigamarole, remove the known ones, speculate on the unknown
    eight: list[str] = [c for c in uniques[7] if c not in known]
    eight_options: list[dict[str, int]] = [
        {eight[0]: 4, eight[1]: 6},
        {eight[0]: 6, eight[1]: 4},
    ]
    # now, combine until be get to NUMBERS_ARRAY
    final_number: int = 0
    count: int = 0
    for o in one_options:
        for f in four_options:
            for e in eight_options:
                mapping: dict[str, int] = {}
                mapping.update(o)
                mapping.update(f)
                mapping.update(e)
                # don't forget the value from seven
                mapping.update(seven_value)
                maybe: set[str] = map_patterns(patterns, mapping)
                if EXPECTED == maybe:
                    final_number = map_output(output, mapping)
                    count += 1
    if 1 != count:
        raise Exception("we got more than 1 match, abort, abort")
    return final_number


def part02(input_file: str) -> str:
    observations: list[(list[str], list[str])] = parse(input_file)
    total: int = 0
    for observation in observations:
        total += solve(observation[0], observation[1])
    return total
