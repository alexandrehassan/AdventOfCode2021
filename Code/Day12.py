"""
For problem statement:
    https://adventofcode.com/2021/day/12
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""

from collections import defaultdict
from functools import cache
from typing import DefaultDict
from Common import time_function


def get_data(filename):
    with open(filename) as file:
        data = file.read().split("\n\n")
    cave_maps = []
    for d in data:
        cave_map = defaultdict(list)
        for line in d.splitlines():
            a, b = line.split("-")
            cave_map[a].append(b)
            cave_map[b].append(a)
        cave_maps.append(cave_map)
    return cave_maps[0]


def count_paths(cave_map: DefaultDict, single_small_twice: bool) -> int:
    # Use functools.cache to eliminate unnecessary recursive calls.
    @cache
    def count_next_paths(origin: str, seen: set, twice: bool) -> int:
        if origin.islower():
            seen = seen.union({origin})
        n_paths = 0
        for cave in cave_map[origin]:
            if cave == "end":
                n_paths += 1
            elif cave not in seen:
                n_paths += count_next_paths(cave, seen, twice)
            elif cave != "start" and twice:
                n_paths += count_next_paths(cave, seen, False)
        return n_paths
    return count_next_paths("start", frozenset(), single_small_twice)


def part1(filename):
    cave_map = get_data(filename)
    return count_paths(cave_map, False)


def part2(filename):
    cave_map = get_data(filename)
    return count_paths(cave_map, True)


def main():
    filename = "Inputs/Day12.txt"
    # Part 1: 3576
    print("Part 1:", part1(filename))
    # Part 2: 84271
    print("Part 2:", part2(filename))
    # Part 1: 0.0004956439999999999s
    print(f"Part 1: {time_function(lambda: part1(filename))}s")
    # Part 2: 0.0015470040000000003s
    print(f"Part 2: {time_function(lambda: part2(filename))}s")


if __name__ == "__main__":
    main()
