#!/usr/bin/env python
from abc import ABC, abstractmethod

from aoc.common import input

DAY: str = "2021/21"

FIRST: bool = True
SECOND: bool = False


def parse(input_file: str) -> tuple[int, int]:
    lines: list[str] = input.load_lines(DAY, input_file)
    x: int = int(lines[0].split(": ")[-1]) - 1
    y: int = int(lines[1].split(": ")[-1]) - 1
    return x, y


def wrap(value: int, limit: int, strict: bool = False) -> int:
    if limit <= value:
        if not strict or limit < value:
            return value % limit
    return value


class Pawn:
    def __init__(self, first: bool, position: int, score: int):
        self.first: bool = first
        self.position: int = position
        self.score: int = score

    def maybe_move(self, first_turn: bool, distance: int) -> 'Pawn':
        if self.first != first_turn:
            return self
        position: int = wrap(self.position + distance, 10)
        return Pawn(self.first, position, self.score + position + 1)

    def __str__(self) -> str:
        return f"{0 if self.first else 1}@{self.position}={self.score}"

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __eq__(self, other: 'Pawn') -> bool:
        return self.position == other.position and self.score == other.score


class Win:
    def __init__(self, first: int, second: int):
        self.first: int = first
        self.second: int = second

    def __add__(self, other: 'Win') -> 'Win':
        return Win(self.first + other.first, self.second + other.second)

    def __eq__(self, other: 'Win') -> bool:
        return self.first == other.first and self.second == other.second

    def multiply(self, factor: int) -> 'Win':
        return Win(self.first * factor, self.second * factor)


class Dirac:
    def __init__(self, first_turn: bool, x: Pawn, y: Pawn):
        self.first_turn: bool = first_turn
        self.pawns: dict[bool, Pawn] = {
            FIRST:  x,
            SECOND: y,
        }

    def move(self, distance: int) -> 'Dirac':
        return Dirac(
            not self.first_turn,
            self.pawns[FIRST].maybe_move(self.first_turn, distance),
            self.pawns[SECOND].maybe_move(self.first_turn, distance),
        )

    def at(self, score: int) -> bool:
        return score <= self.pawns[self.first_turn].score

    def is_won(self, target: int) -> bool:
        return target <= self.pawns[FIRST].score or target <= self.pawns[SECOND].score

    def winner(self) -> Pawn:
        # by the time we detect a win, the game has already moved to the next turn. so go back one
        return self.pawns[not self.first_turn]

    def loser(self) -> Pawn:
        # by the time we detect a win, the game has already moved to the next turn. so go back one
        return self.pawns[self.first_turn]

    def as_win(self) -> Win:
        # by the time we detect a win, the game has already moved to the next turn. so go back one
        return Win(0, 1) if self.first_turn else Win(1, 0)

    def predict_win(self, number: int) -> Win:
        return Win(number, 0) if self.first_turn else Win(0, number)

    def __str__(self) -> str:
        return f"{0 if self.first_turn else 1}: {self.pawns[FIRST]}, {self.pawns[SECOND]}"

    def __eq__(self, other: 'Dirac') -> bool:
        return self.first_turn == other.first_turn and \
               self.pawns[FIRST] == other.pawns[FIRST] and \
               self.pawns[SECOND] == other.pawns[SECOND]

    def __hash__(self) -> int:
        return hash(self.__str__())


class DeterministicDie:
    def __init__(self):
        self.roll: int = 1

    def three_rolls(self) -> int:
        roll: int = 3 * wrap(self.roll, 100, strict=True) + 3
        self.roll += 3
        return roll


def part01(input_file: str) -> int:
    x, y = parse(input_file)
    dirac: Dirac = Dirac(FIRST, Pawn(FIRST, x, 0), Pawn(SECOND, y, 0))
    die: DeterministicDie = DeterministicDie()
    while not dirac.is_won(1000):
        dirac = dirac.move(die.three_rolls())
    return (die.roll - 1) * dirac.loser().score


class QuantumDie:
    def __init__(self):
        self.rolls: list[int] = [3, 4, 5, 6, 7, 8, 9]
        self.multipliers: list[int] = [1, 3, 6, 7, 6, 3, 1]
        self.roll: int = -1

    def three_rolls(self) -> int:
        self.roll += 1
        return self.rolls[self.roll]

    def multiplier(self) -> int:
        return self.multipliers[self.roll]

    def has_rolls(self) -> bool:
        return self.roll < len(self.rolls) - 1


def quantum(game: Dirac, history: dict[Dirac, Win]) -> Win:
    if game in history:
        return history[game]

    if game.at(20):
        return game.predict_win(27)

    win: Win = Win(0, 0)
    die: QuantumDie = QuantumDie()

    while die.has_rolls():
        roll_game: Dirac = game.move(die.three_rolls())
        if roll_game.is_won(21):
            roll_win: Win = roll_game.as_win()
        else:
            roll_win: Win = quantum(roll_game, history)
        history[roll_game] = roll_win
        win += roll_win.multiply(die.multiplier())

    history[game] = win

    return win


def part02(input_file: str) -> int:
    x, y = parse(input_file)
    dirac = Dirac(FIRST, Pawn(FIRST, x, 0), Pawn(SECOND, y, 0))
    history: dict[Dirac, Win] = {}
    win: Win = quantum(dirac, history)
    return max(win.first, win.second)
