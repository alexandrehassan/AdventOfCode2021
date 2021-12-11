from timeit import timeit
from typing import Iterator


def get_int_lines(filename: str) -> list:
    lines = get_lines(filename)
    lines = list(map(int, lines))
    return lines


def get_lines(filename: str) -> list:
    with open(filename) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))
    return lines


def time_function(func, iterations=100) -> int:
    return timeit(func, number=iterations) / 100


def traverse_grid(num_line: int, num_col) -> Iterator:
    for row in range(num_line):
        for col in range(num_col):
            yield (row, col)


def inside_grid(row: int, col: int, num_line: int, num_col: int) -> bool:
    return 0 <= row < num_line and 0 <= col < num_col


def adjacent_coordinates(row: int, col: int, gridsize: tuple,
                         diagonals=False) -> Iterator:
    adjacent_coordinates = [
        (row - 1, col),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col),
    ]
    if diagonals:
        adjacent_coordinates.extend([
            (row - 1, col - 1),
            (row - 1, col + 1),
            (row + 1, col - 1),
            (row + 1, col + 1)])
    return filter(lambda coordinate: inside_grid(*coordinate, *gridsize),
                  adjacent_coordinates)


def get_int_grid(lines: list) -> list:
    grid = []

    for line in lines:
        grid.append(list(map(int, (list(line)))))

    return grid
