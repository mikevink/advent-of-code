#!/usr/bin/env python

from aoc2021 import input
from aoc2021 import error

DAY: str = "06"


class School:
    def __init__(self, initial: list[int], lifecycle: int, initial_offset: int):
        self.lifecycle: int = lifecycle - 1
        self.initial_lifecycle: int = self.lifecycle + initial_offset
        self.stages: int = self.initial_lifecycle + 1
        self.timers: list[int] = [0] * self.stages
        for x in initial:
            self.timers[x] += 1

    def tic(self):
        new_timers: list[int] = [0] * self.stages
        for i in range(self.stages):
            if 0 == i:
                new_timers[self.initial_lifecycle] += self.timers[i]
                new_timers[self.lifecycle] += self.timers[i]
            else:
                new_timers[i - 1] += self.timers[i]
        self.timers = new_timers

    def simulate(self, days: int):
        for i in range(days):
            self.tic()

    def population(self) -> int:
        return sum(self.timers)


def simulation(input_file: str, days: int) -> int:
    school: School = School(input.load_single_csv(DAY, input_file, int), 7, 2)
    school.simulate(days)
    return school.population()


def part01(input_file: str) -> str:
    return str(simulation(input_file, 80))


def part02(input_file: str) -> str:
    return str(simulation(input_file, 256))
