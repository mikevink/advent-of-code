#!/usr/bin/env python
from collections import namedtuple

from aoc.common import input

DAY: str = "2021/14"

Rule: namedtuple = namedtuple("Rule", ["node", "left_link", "right_link"])


def parse_rules(lines: list[str]) -> dict[str, Rule]:
    rules: dict[str, tuple[str, str, str]] = {}
    for line in lines:
        condition, result = line.split(" -> ")
        rules[condition] = Rule(result, f"{condition[0]}{result}", f"{result}{condition[1]}")
    return rules


def count_initial_chain(chain: str, counts: dict[str, int]):
    for node in chain:
        if node in counts:
            counts[node] += 1
        else:
            counts[node] = 1


def break_chain(chain: str) -> dict[str, int]:
    links: dict[str, int] = {}
    for i in range(len(chain) - 1):
        chainlink: str = chain[i : i + 2]
        if chainlink not in links:
            links[chainlink] = 1
        else:
            links[chainlink] += 1
    return links


def index_possible_links(links: dict[str, int], rules: dict[str, Rule]):
    for link, rule in rules.items():
        if link not in links:
            links[link] = 0
        if rule.left_link not in links:
            links[rule.left_link] = 0
        if rule.right_link not in links:
            links[rule.right_link] = 0


def index_possible_nodes(counts: dict[str, int], rules: dict[str, Rule]):
    for rule in rules.values():
        if rule.node not in counts:
            counts[rule.node] = 0


def grow_chain(links: dict[str, int], rules: dict[str, Rule], counts: dict[str, int]):
    for link, num_links in list(links.items()):
        if 0 != num_links and link in rules:
            links[link] -= num_links
            links[rules[link].left_link] += num_links
            links[rules[link].right_link] += num_links
            counts[rules[link].node] += num_links


def polymerise(input_file: str, steps: int) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    chain: str = lines.pop(0)
    counts: dict[str, int] = {}
    count_initial_chain(chain, counts)
    links: dict[str, int] = break_chain(chain)
    # get rid of the blank line
    lines.pop(0)
    rules: dict[str, tuple[str, str, str]] = parse_rules(lines)
    index_possible_links(links, rules)
    index_possible_nodes(counts, rules)
    for _ in range(steps):
        grow_chain(links, rules, counts)

    maxn: int = max(counts.values())
    minn: int = min(counts.values())

    return maxn - minn


def part01(input_file: str) -> int:
    return polymerise(input_file, 10)


def part02(input_file: str) -> int:
    return polymerise(input_file, 40)
