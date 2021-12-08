"""
For problem statement:
    https://adventofcode.com/2021/day/1
@author: Alexandre Hassan
"""
from Common import get_int_lines, time_function


def part1(lines: list) -> int:
    pass


def part2(lines: list) -> int:
    pass


def main():
    lines = get_int_lines("Inputs/Day01.txt")
    # Part 1: 1184
    print(f"Part 1: {part1(lines)}")
    # Part 2: 1158
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0005400190013460815s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 1: 0.0019921099999919535s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()
