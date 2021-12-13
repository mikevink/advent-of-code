#!/usr/bin/env python

from aoc.common import input
from aoc.common import error

DAY: str = "2021/12"


def build_graph(lines: list[str]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for line in lines:
        nodeA, nodeB = line.split("-")
        if nodeA not in graph:
            graph[nodeA] = []
        if nodeB not in graph:
            graph[nodeB] = []
        if "end" != nodeA and "start" != nodeB:
            graph[nodeA].append(nodeB)
        if "end" != nodeB and "start" != nodeA:
            graph[nodeB].append(nodeA)
    # clear the end entry, it ought to be empty
    del graph["end"]
    return graph


def find_paths(graph: dict[str, list[str]], node: str, path: str, paths: set[str], twice_allowed: bool):
    if "end" == node and 0 != len(path):
        paths.add(path + "end")
    for child in graph.get(node, []):
        if child.isupper() or child not in path:
            find_paths(graph, child, f"{path}{node}-", paths, twice_allowed)
        elif child in path and twice_allowed:
            find_paths(graph, child, f"{path}{node}-", paths, False)


def part01(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    graph: dict[str, list[str]] = build_graph(lines)
    paths: set[str] = set()
    find_paths(graph, "start", "", paths, twice_allowed=False)
    return len(paths)


def part02(input_file: str) -> int:
    lines: list[str] = input.load_lines(DAY, input_file)
    graph: dict[str, list[str]] = build_graph(lines)
    paths: set[str] = set()
    find_paths(graph, "start", "", paths, twice_allowed=True)
    return len(paths)
