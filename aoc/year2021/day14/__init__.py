#!/usr/bin/env python
from typing import Optional

from aoc.common import input
from aoc.common import error

DAY: str = "2021/14"


class Node:
    def __init__(self, value: str):
        self.value: str = value
        self.next: "Node" = None
        self.prev: "Node" = None
        self.link_node: "Node" = None

    @property
    def pair(self) -> Optional[str]:
        if self.has_next():
            return f"{self.value}{self.next.value}"
        return None

    def has_next(self) -> bool:
        return self.next is not None

    def link(self, node: "Node"):
        if self.has_next():
            self.link_node = node

    def chain(self):
        if self.has_next() and self.link_node is not None:
            self.next.prev = self.link_node
            self.link_node.next = self.next
            self.next = self.link_node
            self.link_node.prev = self
            self.link_node = None

    def __str__(self) -> str:
        return self.value


def build_chain(template: str) -> tuple[Node, Node]:
    root: Node = None
    previous: Node = None
    for c in template:
        current: Node = Node(c)
        if root is None:
            root = current
        else:
            previous.next = current
            current.prev = previous
        previous = current
    return root, previous


def parse_rules(lines: list[str]) -> dict[str, str]:
    rules: dict[str, str] = {}
    for line in lines:
        condition, result = line.split(" -> ")
        rules[condition] = result
    return rules


def count_initial_nodes(root: Node, counts: dict[str, int]):
    current: Node = root
    while current is not None:
        if current.value not in counts:
            counts[current.value] = 0
        counts[current.value] += 1
        current = current.next


def link(root: Node, rules: dict[str, str], counts: dict[str, int]):
    current: Node = root
    # no point in checking the last node, it can't match rules on it's own
    while current.has_next():
        if current.pair in rules:
            link_node: Node = Node(rules[current.pair])
            if link_node.value not in counts:
                counts[link_node.value] = 0
            counts[link_node.value] += 1
            current.link(link_node)
        current = current.next


def chain(tail: Node):
    current: Node = tail
    while current is not None:
        current.chain()
        current = current.prev


def print_polymer(step: int, root: Node):
    polymer: str = ""
    current: Node = root
    while current is not None:
        polymer += current.value
        current = current.next
    return f"{step}: {polymer}"


def polymerise(input_file: str, steps: int) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    root, tail = build_chain(lines.pop(0))
    # get rid of the blank line
    lines.pop(0)
    rules: dict[str, str] = parse_rules(lines)
    counts: dict[str, int] = {}
    count_initial_nodes(root, counts)
    for _ in range(steps):
        link(root, rules, counts)
        chain(tail.prev)
        print(_)

    maxn: int = max(counts.values())
    minn: int = min(counts.values())

    return maxn - minn


def part01(input_file: str) -> int:
    return polymerise(input_file, 10)


def part02(input_file: str) -> int:
    return polymerise(input_file, 40)
