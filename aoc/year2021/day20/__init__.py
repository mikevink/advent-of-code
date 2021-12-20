#!/usr/bin/env python

from aoc.common import input
from aoc.common import error

DAY: str = "2021/20"


def parse_input(input_file: str) -> tuple[str, dict[int, dict[int, str]]]:
    lines: list[str] = input.load_lines(DAY, input_file)
    algorithm: str = lines.pop(0).replace(".", "0").replace("#", "1")
    image: dict[int, dict[int, str]] = {}
    # get rid of the separating line
    lines.pop(0)
    len_x: int = len(lines)
    len_y: int = len(lines[0])
    for x in range(len_x):
        image[x] = {}
        for y in range(len_y):
            image[x][y] = "1" if "#" == lines[x][y] else "0"
    return algorithm, image


def enhance_pixel(x: int, y: int, algorithm: str, source_image: dict[int, dict[int], str], border: str) -> str:
    index: str = source_image.get(x - 1, {}).get(y - 1, border)
    index += source_image.get(x - 1, {}).get(y, border)
    index += source_image.get(x - 1, {}).get(y + 1, border)

    index += source_image.get(x, {}).get(y - 1, border)
    index += source_image.get(x, {}).get(y, border)
    index += source_image.get(x, {}).get(y + 1, border)

    index += source_image.get(x + 1, {}).get(y - 1, border)
    index += source_image.get(x + 1, {}).get(y, border)
    index += source_image.get(x + 1, {}).get(y + 1, border)
    return algorithm[int(index, 2)]


def enhance(algorithm: str, source_image: dict[int, dict[int, str]], border: str) -> dict[int, dict[int, str]]:
    image: dict[int, dict[int, str]] = {}
    len_x: int = len(source_image)
    len_y: int = len(source_image[0])
    for x in range(-1, len_x + 1):
        image[x + 1] = {}
        for y in range(-1, len_y + 1):
            image[x + 1][y + 1] = enhance_pixel(x, y, algorithm, source_image, border)
    return image


def enhancement_loop(steps: int, input_file: str) -> int:
    algorithm, image = parse_input(input_file)
    border: str = "0"
    for _ in range(steps):
        image = enhance(algorithm, image, border)
        border = algorithm[0] if "0" == border else algorithm[-1]
    count: int = 0
    for row in image.values():
        for pixel in row.values():
            count += int(pixel)
    return count


def part01(input_file: str) -> int:
    return enhancement_loop(2, input_file)


def part02(input_file: str) -> int:
    return enhancement_loop(50, input_file)
