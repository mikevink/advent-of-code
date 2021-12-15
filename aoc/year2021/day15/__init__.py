#!/usr/bin/env python

from aoc.common import input
from aoc.common import error

DAY: str = "2021/15"

DIRECTIONS: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INFINITY: int = -1


def graph_edges(lines: list[list[int]], max_x: int, max_y: int) -> dict[int, dict[int, int]]:
    edges: dict[int, dict[int, int]] = {}
    for x in range(max_x):
        for y in range(max_y):
            node: int = x * max_y + y
            for d in DIRECTIONS:
                nx: int = x + d[0]
                ny: int = y + d[1]
                if 0 <= nx < max_x and 0 <= ny < max_y:
                    to_node: int = nx * max_y + ny
                    if node not in edges:
                        edges[node] = {}
                    edges[node][to_node] = lines[nx][ny]
    return edges


def smaller(x: int, y: int) -> bool:
    return INFINITY == y or x < y


def dijkstra(lines: list[list[int]]) -> int:
    max_x: int = len(lines)
    max_y: int = len(lines[0])
    edges: dict[int, dict[int, int]] = graph_edges(lines, max_x, max_y)
    unvisited: set[int] = set(range(max_x * max_y))
    distances: dict[int, int] = {0: 0}
    current: int = 0
    target: int = (max_x * max_y) - 1
    while unvisited:
        if target == current:
            break
        for node, cost in edges[current].items():
            if node in unvisited:
                may_dist: int = distances[current] + cost
                node_dist: int = distances.get(node, INFINITY)
                if INFINITY == node_dist or may_dist < node_dist:
                    distances[node] = may_dist
        del distances[current]
        unvisited.remove(current)

        current = min(distances, key=distances.get)

    return distances[target]


def part01(input_file: str) -> int:
    lines: list[list[int]] = input.load_lines(DAY, input_file, parse_line)
    return dijkstra(lines)


def parse_line(line: str) -> list[int]:
    return [int(l) for l in line]


def next_val(val: int):
    nval: int = val + 1
    if 9 < nval:
        return nval - 9
    return nval


def generate_map(input_file: str) -> list[list[int]]:
    lines: list[list[int]] = input.load_lines(DAY, input_file, parse_line)
    max_x: int = len(lines)
    max_y: int = len(lines[0])
    generated: list[list[int]] = [[0] * (5 * max_y) for _ in range(5 * max_x)]
    for x in range(max_x):
        for y in range(max_y):
            generated[x][y] = lines[x][y]
    for x in range(len(generated)):
        for y in range(max_y):
            val: int = generated[x][y]
            nval: int = next_val(val)
            if x + max_x < len(generated):
                generated[x + max_x][y] = nval
            for i in range(4):
                r: int = i + 1
                ny: int = y + (max_y * r)
                generated[x][ny] = nval
                nval = next_val(nval)
    return generated


def part02(input_file: str) -> int:
    generated: list[list[int]] = generate_map(input_file)
    return dijkstra(generated)
