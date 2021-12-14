#!/usr/bin/env python

from aoc.common import input
from aoc.common import error

DAY: str = "2021/14"


class Rule:
    def __init__(self, definition: str):
        self.definition: str = definition
        split = definition.split(" -> ")
        self.first: str = split[0][0]
        self.second: str = split[0][1]
        self.result: str = split[1]

    def matches(self, first_node: str, second_node: str) -> bool:
        return first_node == self.first and second_node == self.second

    def __str__(self) -> str:
        return self.definition


class Node:
    def __init__(self, value: str):
        self.value: str = value
        self.next: "Node" = None
        self.prev: "Node" = None
        self.to_insert: "Node" = None

    def has_next(self) -> bool:
        return self.next is not None

    def matches_rule(self, rule: Rule) -> bool:
        return self.has_next() and rule.matches(self.value, self.next.value)

    def enqueue_append(self, other: "Node"):
        if self.has_next():
            self.to_insert = other

    def consume_enqueue(self):
        if self.has_next() and self.to_insert is not None:
            self.next.prev = self.to_insert
            self.to_insert.next = self.next
            self.next = self.to_insert
            self.to_insert.prev = self
            self.to_insert = None

    def __str__(self) -> str:
        return self.value


def build_chain(template: str) -> tuple[Node, Node]:
    root: Node = None
    previous: Node = None
    for c in template:
        current: Node = Node(c)
        if None == root:
            root = current
        else:
            previous.next = current
            current.prev = previous
        previous = current
    return root, previous


def count(root: Node, counts: dict[str, int], enqueued: bool = False):
    current: Node = root
    while current is not None:
        value: str = current.to_insert.value if enqueued else current.value
        if value not in counts:
            counts[value] = 0
        counts[value] += 1
        current = current.next


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
    rules: list[Rule] = [Rule(line) for line in lines]
    counts: dict[str, int] = {}
    count(root, counts)
    for _ in range(steps):
        for rule in rules:
            # apply the rules
            current: Node = root
            while current.has_next():
                if current.matches_rule(rule):
                    current.enqueue_append(Node(rule.result))
                    # count it
                    if rule.result not in counts:
                        counts[rule.result] = 0
                    counts[rule.result] += 1
                current = current.next
        # insert nodes
        current: Node = tail.prev
        while current is not None:
            current.consume_enqueue()
            current = current.prev

    maxn: int = max(counts.values())
    minn: int = min(counts.values())

    return maxn - minn


def part01(input_file: str) -> int:
    return polymerise(input_file, 10)


def part02(input_file: str) -> int:
    return polymerise(input_file, 40)
