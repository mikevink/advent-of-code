#!/usr/bin/env python
from collections import deque
from copy import deepcopy
from math import floor, ceil

from .abstracts import Node
from aoc.common import error
from aoc.common import input

DAY: str = "2021/18"


class Number(Node):
    def __init__(self, value: int):
        super().__init__(None, None)
        self.value: int = value

    def leftmost(self) -> Node:
        return self

    def rightmost(self) -> Node:
        return self

    def chain(self):
        pass

    def magnitude(self) -> int:
        return self.value

    def can_explode(self, depth: int) -> bool:
        return False

    def explode(self, depth: int) -> bool:
        return False

    def can_split(self) -> bool:
        return 9 < self.value

    def split(self) -> bool:
        return False

    def reduce(self):
        pass

    def __str__(self) -> str:
        return str(self.value)


class Pair(Node):
    # noinspection PyTypeChecker
    @staticmethod
    def explode_pair(node: Node):
        pair_left: Number = node.left
        if pair_left.left is not None:
            num_left: Number = pair_left.left
            num_left.value += pair_left.value
        pair_right: Number = node.right
        if pair_right.right is not None:
            num_right: Number = pair_right.right
            num_right.value += pair_right.value

    # noinspection PyTypeChecker
    @staticmethod
    def split_number(node: Node) -> Node:
        number: Number = node
        left: int = int(floor(number.value / 2))
        right: int = int(ceil(number.value / 2))
        return Pair(Number(left), Number(right))

    def leftmost(self) -> Node:
        return self.left.leftmost()

    def rightmost(self) -> Node:
        return self.right.rightmost()

    def chain(self):
        self.right.chain()
        self.left.chain()

        leftmost: Node = self.right.leftmost()
        rightmost: Node = self.left.rightmost()

        leftmost.left = rightmost
        rightmost.right = leftmost

    def magnitude(self) -> int:
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def can_explode(self, depth: int) -> bool:
        return 3 < depth

    def explode(self, depth: int) -> bool:
        if self.left.can_explode(depth + 1):
            Pair.explode_pair(self.left)
            self.left = Number(0)
            return True
        if self.left.explode(depth + 1):
            return True
        if self.right.can_explode(depth + 1):
            Pair.explode_pair(self.right)
            self.right = Number(0)
            return True
        return self.right.explode(depth + 1)

    def can_split(self) -> bool:
        return False

    # noinspection PyTypeChecker,DuplicatedCode
    def split(self) -> bool:
        if self.left.can_split():
            self.left = Pair.split_number(self.left)
            return True
        if self.left.split():
            return True
        if self.right.can_split():
            self.right = Pair.split_number(self.right)
            return True
        return self.right.split()

    def reduce(self):
        can_reduce: bool = True
        while can_reduce:
            can_reduce = False
            if self.explode(0):
                can_reduce = True
            elif self.split():
                can_reduce = True
            self.chain()

    def __str__(self) -> str:
        return f"[{self.left}, {self.right}]"


def parse(line: str) -> Pair:
    q: deque[Node] = deque()
    acc: str = ""
    for char in line:
        if "[" == char:
            acc = ""
        elif "," == char:
            if 0 != len(acc):
                q.append(Number(int(acc)))
                acc = ""
        elif "]" == char:
            if 0 != len(acc):
                q.append(Number(int(acc)))
                acc = ""
            right: Node = q.pop()
            left: Node = q.pop()
            q.append(Pair(left, right))
        else:
            acc += char

    if 1 != len(q):
        raise Exception("Something's fishy")
    root: Node = q.pop()
    if not isinstance(root, Pair):
        raise Exception("Something else's fishy")
    root.chain()
    return root


def add(left: Node, right: Node) -> Node:
    return Pair(deepcopy(left), deepcopy(right))


def part01(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    sfnumbers: list[Node] = [parse(line) for line in lines]
    total: Node = sfnumbers[0]
    for number in sfnumbers[1:]:
        total = add(total, number)
        total.reduce()
    return total.magnitude()


def part02(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    sfnumbers: list[Node] = [parse(line) for line in lines]
    magnitudes: set[int] = set()
    for i in sfnumbers:
        for j in sfnumbers:
            if i != j:
                ij: Node = add(i, j)
                ij.reduce()
                magnitudes.add(ij.magnitude())
                ji: Node = add(j, i)
                ji.reduce()
                magnitudes.add(ji.magnitude())
    return max(magnitudes)
