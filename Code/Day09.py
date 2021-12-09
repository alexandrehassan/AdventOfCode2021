"""
For problem statement:
    https://adventofcode.com/2021/day/9
@author: Alexandre Hassan
"""
from typing import DefaultDict
from Common import get_lines, time_function


def part1(lines: list) -> int:
    pass


def part2(lines: list) -> int:
    pass


def main():
    lines = get_lines("Inputs/Day09.txt")
    # Part 1:
    print(f"Part 1: {part1(lines)}")
    # Part 2:
    print(f"Part 2: {part2(lines)}")

    # Part 1:
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2:
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()
