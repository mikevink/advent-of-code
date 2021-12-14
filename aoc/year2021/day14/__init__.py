#!/usr/bin/env python
from typing import Optional

from aoc.common import input
from aoc.common import error

DAY: str = "2021/14"


def parse_rules(lines: list[str]) -> dict[str, str]:
    rules: dict[str, str] = {}
    for line in lines:
        condition, result = line.split(" -> ")
        rules[condition] = result
    return rules


def count_initial_chain(chain: str, counts: dict[str, int]):
    for node in chain:
        if node in counts:
            counts[node] += 1
        else:
            counts[node] = 1


def link(chain: str, rules: dict[str, str], counts: dict[str, int]) -> str:
    linked_chain: str = ""
    for i in range(len(chain) - 1):
        pair: str = chain[i:i + 2]
        if pair in rules:
            node: str = rules[pair]
            linked_chain = f"{linked_chain}{chain[i]}{node}"
            if node in counts:
                counts[node] += 1
            else:
                counts[node] = 1
        else:
            linked_chain = f"{linked_chain}{chain[i]}"
    return f"{linked_chain}{chain[-1]}"


def polymerise(input_file: str, steps: int) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    chain: str = lines.pop(0)
    # get rid of the blank line
    lines.pop(0)
    rules: dict[str, str] = parse_rules(lines)
    counts: dict[str, int] = {}
    count_initial_chain(chain, counts)
    for _ in range(steps):
        chain = link(chain, rules, counts)
        print(_)

    maxn: int = max(counts.values())
    minn: int = min(counts.values())

    return maxn - minn


def part01(input_file: str) -> int:
    return polymerise(input_file, 10)


def part02(input_file: str) -> int:
    return polymerise(input_file, 40)
