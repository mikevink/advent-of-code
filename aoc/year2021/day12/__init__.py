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
        graph[nodeA].append(nodeB)
        graph[nodeB].append(nodeA)
    return graph

def find_paths(graph: dict[str, list[str]], node: str, path: str, paths: set[str]):
    if "end" == node and 0 != len(path):
        paths.add(path + "end")
    for child in graph[node]:
        if child.isupper() or child not in path:
            find_paths(graph, child, f"{path}{node}-", paths)


def part01(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    graph: dict[str, list[str]] = build_graph(lines)
    paths: set[str] = set()
    find_paths(graph, "start", "", paths)
    return str(len(paths))


def part02(input_file: str) -> str:
    lines: list[str] = input.load_lines(DAY, input_file)
    return error.ERROR
