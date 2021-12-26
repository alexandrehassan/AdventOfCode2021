"""
For problem statement:
    https://adventofcode.com/2021/day/13
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from typing import DefaultDict
from Common import time_function


def get_data(filename):
    with open(filename) as file:
        data = file.read().split("\n\n")

    numbers = set()
    instructions = []
    max_x = 0
    max_y = 0
    number_lines = data[0].splitlines()
    instruction_lines = data[1].splitlines()
    for line in number_lines:
        a, b = line.split(",")
        max_x = max(max_x, int(a))
        max_y = max(max_y, int(b))
        numbers.add((int(a), int(b)))

    for line in instruction_lines:
        line = line.replace("fold along ", "")
        a, b = line.split("=")
        instructions.append((a, int(b)))
    return numbers, instructions, max_x, max_y


def count_dots(numbers: list, instructions: list, part1=True) -> int:
    for instruction in instructions:
        max_x, max_y = 0, 0
        for x, y in numbers:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        print(max_x, max_y, instruction)
        direction, position = instruction
        if direction == "x":
            for x in range(position):
                for y in range(max_y):
                    x1 = max_x - x
                    if (x1, y) in numbers:
                        numbers.remove((x1, y))
                        numbers.add((x, y))
        elif direction == "y":
            for y in range(0, position):
                for x in range(max_x):
                    y1 = max_y - y
                    if (x, y1) in numbers:
                        numbers.remove((x, y1))
                        numbers.add((x, y))
        if part1:
            return len(numbers)
    print(len(numbers))
    return numbers


def print_grid(numbers: list) -> str:
    max_x, max_y = 0, 0
    for x, y in numbers:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    string = ""
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in numbers:
                string += "#"
            else:
                string += "."
        string += "\n"
    with open("Outputs/Day13.txt", "w") as file:
        file.write(string)


def part1(filename: str) -> int:
    numbers, instructions, max_x, max_y = get_data(filename)
    return count_dots(numbers, instructions)


def part2(filename: str) -> int:
    numbers, instructions, max_x, max_y = get_data(filename)
    print_grid(count_dots(numbers, instructions, part1=False))


def main():
    filename = "Inputs/Day13.txt"
    # Part 1:
    print(f"Part 1: {part1(filename)}")
    # Part 2:
    print(f"Part 2: {part2(filename)}")

    # # Part 1:
    # print(f"Part 1: {time_function(lambda: part1(filename))}s")
    # # Part 2:
    # print(f"Part 2: {time_function(lambda: part2(filename))}s")


if __name__ == "__main__":
    main()
