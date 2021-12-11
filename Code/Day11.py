"""
For problem statement:
    https://adventofcode.com/2021/day/11
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from Common import get_lines, time_function, traverse_grid, \
    adjacent_coordinates, get_int_grid

GRID_SIZE = (10, 10)


def take_step(energy_levels: list) -> int:
    flashes = []
    for coord in traverse_grid(*GRID_SIZE):
        row, col = coord
        energy_levels[row][col] += 1
        if energy_levels[row][col] == 10:
            flashes.append(coord)

    while len(flashes) > 0:
        flash_position = flashes.pop(0)
        for coord in adjacent_coordinates(*flash_position, GRID_SIZE, True):
            row, col = coord
            energy_levels[row][col] += 1
            if energy_levels[row][col] == 10:
                flashes.append(coord)

    number_of_flashes = 0
    for coord in traverse_grid(*GRID_SIZE):
        row, col = coord
        if energy_levels[row][col] >= 10:
            number_of_flashes += 1
            energy_levels[row][col] = 0

    return number_of_flashes


def do_steps(grid: list, required_steps: int, part1: bool) -> int:
    steps = 0

    part1_res = 0
    part2_res = None

    while part2_res is None:
        number_of_flashes = take_step(grid)
        steps += 1

        if steps <= required_steps:
            part1_res += number_of_flashes

        if number_of_flashes == GRID_SIZE[0]**2:
            part2_res = steps

    return part1_res if part1 else part2_res


def part1(lines: list) -> int:
    grid = get_int_grid(lines)
    return do_steps(grid, 100, part1=True)


def part2(lines: list) -> int:
    grid = get_int_grid(lines)
    return do_steps(grid, 100, part1=False)


def main():
    lines = get_lines("Inputs/Day11.txt")
    # Part 1: 1673
    print(f"Part 1: {part1(lines)}")
    # # Part 2: 279
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.049193955999944
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.050320960999961244s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()
