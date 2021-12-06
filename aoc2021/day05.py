#!/usr/bin/env python

from collections import namedtuple

from aoc2021 import input
from aoc2021 import error

DAY: str = "05"

class Point:
    def __init__(self, coord: str):
        self.coord: str = coord
        sx, sy = coord.split(",")
        self.x: int = int(sx)
        self.y: int = int(sy)

    def inline(self, other: 'Point') -> bool:
        return (self.x == other.x) or (self.y == other.y)

Increment = namedtuple("Increment", ["x", "y"])

def determine_increment(start: int, end: int) -> int:
    dif: int = end - start
    if dif > 0:
        return 1
    if dif < 0:
        return -1
    return 0

def reached(start: int, end: int, increment: int) -> bool:
    if 0 > increment:
        return start < end
    return start > end


class Walker:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0 
    
    def reset(self, start: Point):
        self.x = start.x
        self.y = start.y

    def reached(self, end: Point, increment: Increment) -> bool:
        return reached(self.x, end.x, increment.x) or reached(self.y, end.y, increment.y)

    def step(self, increment: Increment):
        self.x += increment.x
        self.y += increment.y



class Line:
    def __init__(self, definition: str):
        scoord, ignored, ecoord = definition.split(" ")
        self.definition: str = definition
        self.start: Point = Point(scoord)
        self.end: Point = Point(ecoord)
        self.inline: bool = self.start.inline(self.end)
        self.increment: Increment = Increment(
                determine_increment(self.start.x, self.end.x),
                determine_increment(self.start.y, self.end.y)
        )
        self.walker: Walker = Walker()

    def is_point(self) -> bool:
        return self.start.x == self.end.x and self.start.y == self.end.y

    def reset(self):
        self.walker.reset(self.start)

    def walking(self) -> bool:
        return not self.walker.reached(self.end, self.increment)

    def step(self):
        self.walker.step(self.increment)

def maximum(a: int, b: int, c: int) -> int:
    if a > b:
        if a > c:
            return a
        return c
    if b > c:
        return b
    return c

class Board:
    def __init__(self, lines: str):
        self.lines: list[Lines] = [ Line(l) for l in lines ]
        self.board: list[list[int]] = []

    def init_board(self):
        max_x: int = 0
        max_y: int = 0
        for line in self.lines:
            max_x = maximum(max_x, line.start.x, line.end.x)
            max_y = maximum(max_y, line.start.y, line.end.y)
        max_x += 1
        max_y += 1
        self.board = [[0] * max_y for x in range(max_x)] 

    def fill(self, inline: bool):
        for line in self.lines:
            if not inline or (inline and line.inline):
                line.reset()
                if line.is_point():
                    self.board[line.walker.x][line.walker.y] += 1
                else:
                    while line.walking():
                        self.board[line.walker.x][line.walker.y] += 1
                        line.step()

    def count_intersections(self) -> int:
        count: int = 0
        for row in self.board:
            for col in row:
                if 1 < col:
                    count += 1
        return count

def part01(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    board: Board = Board(lines)
    board.init_board()
    board.fill(inline = True)
    return str(board.count_intersections())

def part02(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    board: Board = Board(lines)
    board.init_board()
    board.fill(inline = False)
    return str(board.count_intersections())
