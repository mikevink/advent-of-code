#!/usr/bin/env python

from aoc.common import error
from aoc.common import input

DAY: str = "2021/04"
BOARD_SIZE: int = 5

# ASSUMPTION: Per card, all numbers are unique


class Board:
    def __init__(self, rows: list[list[int]]):
        # keep track of all the numbers in a board
        self.numbers: dict[int, tuple[int, int]] = {}
        self.score: int = -1
        # how many numbers in a given row/column have been called
        self.per_row: list[int] = [0] * BOARD_SIZE
        self.per_col: list[int] = [0] * BOARD_SIZE

        # add store the indexes of the board numbers
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                number: int = rows[i][j]
                self.numbers[number] = (i, j)

    def call(self, number: int) -> bool:
        if number in self.numbers:
            i, j = self.numbers.pop(number)
            self.per_row[i] += 1
            self.per_col[j] += 1
            if (BOARD_SIZE == self.per_row[i]) or (BOARD_SIZE == self.per_col[j]):
                remainder: int = sum(self.numbers.keys())
                self.score = number * remainder
                return True
        return False


# takes a line of form `1 2 4 6  5  7` and converts it to [1, 2, 4, 6, 5, 7] (i.e. ignore consecutive spaces)
def process_line(line: str, separator: str = " ") -> list[int]:
    return [int(l) for l in line.split(separator) if l.strip()]


class Bingo:
    def __init__(self, lines: list[str]):
        # get the calls
        self.calls: list[int] = process_line(lines.pop(0), ",")
        # discard empty line
        lines.pop(0)
        self.boards: list[Board] = []
        rows: list[list[int]] = []
        for line in lines:
            if not line:
                self.boards.append(Board(rows))
                rows = []
            else:
                rows.append(process_line(line))
        # include the last entry
        if rows:
            self.boards.append(Board(rows))

    def play(self, to_the_end: bool = False) -> int:
        last_score: int = -1
        board_indexes: list[int] = list(range(len(self.boards)))
        for number in self.calls:
            finished: list[int] = []
            for bi in board_indexes:
                board: Board = self.boards[bi]
                if board.call(number):
                    last_score = board.score
                    finished.append(bi)
                    if not to_the_end:
                        return last_score
            board_indexes = [bi for bi in board_indexes if bi not in finished]
            if not board_indexes:
                return last_score
        raise Exception(error.ERROR)


def part01(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    bingo: Bingo = Bingo(lines)
    return bingo.play()


def part02(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    bingo: Bingo = Bingo(lines)
    return bingo.play(to_the_end=True)
