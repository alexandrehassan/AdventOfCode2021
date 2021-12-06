"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
"""
from typing import DefaultDict
from Common import get_lines, time_function


def setup() -> DefaultDict:
    input = lines[0].split(',')
    input = list(map(int, input))
    fish = DefaultDict(int)
    for f in input:
        fish[f] += 1
    return fish


def calculate_fish(days: int) -> int:
    fishes = setup()
    for day in range(days):
        babies = fishes[0]
        fishes[0] = 0
        for i in range(8):
            fishes[i] = fishes[i + 1]
            fishes[i + 1] = 0
        fishes[8] = babies
        fishes[6] += babies
        # for v in fishes.keys():
        #     print(f"day: {day + 1}, fishes at {v} days: {fishes.get(v)}")
        # print()
    return sum(fishes.values())


def part1() -> int:
    return calculate_fish(80)


def part2() -> int:
    return calculate_fish(256)


def main():
    # Part 1: 351092
    print(f"Part 1: {part1()}")
    # Part 2: 1595330616005
    print(f"Part 2: {part2()}")

    # Part 1: 0.00012867999999999997s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.00030791799999999996s
    print(f"Part 2: {time_function(part2)}s")


lines = get_lines("Inputs/Day06.txt")

if __name__ == "__main__":
    main()
