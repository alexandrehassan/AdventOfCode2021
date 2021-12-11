"""
For problem statement:
    https://adventofcode.com/2021/day/11
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from Common import get_lines, time_function, traverse_grid, \
    adjacent_coordinates, get_int_grid

GRID_SIZE = (10, 10)


def take_step(grid: list) -> int:
    do_flashes(grid, will_flash(grid))
    return count_flashes(grid)


def count_flashes(grid):
    number_of_flashes = 0
    for coord in traverse_grid(*GRID_SIZE):
        row, col = coord
        if grid[row][col] >= 10:
            number_of_flashes += 1
            grid[row][col] = 0
    return number_of_flashes


def do_flashes(grid, to_flash):
    while len(to_flash) > 0:
        flash_position = to_flash.pop(0)
        for coord in adjacent_coordinates(*flash_position, GRID_SIZE, True):
            row, col = coord
            grid[row][col] += 1
            if grid[row][col] == 10:
                to_flash.append(coord)


def will_flash(grid):
    flashes = []
    for coord in traverse_grid(*GRID_SIZE):
        row, col = coord
        grid[row][col] += 1
        if grid[row][col] == 10:
            flashes.append(coord)
    return flashes


def do_steps(grid: list, steps_total: int, part1: bool) -> int:
    steps_done, part1_res = 0, 0

    part2_res = None

    while part2_res is None:
        number_of_flashes = take_step(grid)
        steps_done += 1

        if steps_done <= steps_total:
            part1_res += number_of_flashes

        if number_of_flashes == GRID_SIZE[0]**2:
            part2_res = steps_done

    return part1_res if part1 else part2_res


def part1(lines: list) -> int:
    return do_steps(get_int_grid(lines), 100, part1=True)


def part2(lines: list) -> int:
    return do_steps(get_int_grid(lines), 100, part1=False)


def main():
    lines = get_lines("Inputs/Day11.txt")
    # Part 1: 1673
    print(f"Part 1: {part1(lines)}")
    # # Part 2: 279
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.024099096s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.023895938999999995s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()
