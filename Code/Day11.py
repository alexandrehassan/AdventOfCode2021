
from typing import Iterator
from Common import get_lines, time_function

GRID_SIZE = 10


def inside_grid(coordinate: tuple) -> bool:
    row, col = coordinate
    return (row >= 0) and (row < GRID_SIZE) and (col >= 0) and (col < GRID_SIZE)


def adjacent_coordinates(row: int, col: int) -> Iterator:
    """Return coordinates of adjacent points of the given `coordinate`"""
    adjacent_coordinates = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]
    return filter(inside_grid, adjacent_coordinates)


def traverse_grid(size: int) -> Iterator:
    for r in range(size):
        for c in range(size):
            yield (r, c)


def take_step(energy_levels: list) -> int:
    """Update the energy levels and return the total number of flashes"""

    # First part: Increment energy levels, store flash positions
    flashes = []
    for coordinate in traverse_grid(GRID_SIZE):
        row, col = coordinate
        energy_levels[row][col] += 1
        if energy_levels[row][col] == 10:
            flashes.append(coordinate)

    # Second part: Continuously update positions affected by flashes
    while len(flashes) > 0:
        flash_position = flashes.pop(0)
        for coordinate in adjacent_coordinates(*flash_position):
            row, col = coordinate
            energy_levels[row][col] += 1
            if energy_levels[row][col] == 10:
                flashes.append(coordinate)

    # Finally: Count the number of flashes and reset the respective positions
    number_of_flashes = 0
    for coordinate in traverse_grid(GRID_SIZE):
        row, col = coordinate
        if energy_levels[row][col] >= 10:
            number_of_flashes += 1
            energy_levels[row][col] = 0

    return number_of_flashes


def get_grid(lines: list) -> list:
    grid = []

    for line in lines:
        grid.append(list(map(int, (list(line)))))

    return grid


def do_steps(grid: list, required_steps: int, part1: bool) -> int:
    steps = 0

    part1_res = 0
    part2_res = None

    while part2_res == None:
        number_of_flashes = take_step(grid)
        steps += 1

        if steps <= required_steps:
            part1_res += number_of_flashes

        if number_of_flashes == GRID_SIZE**2:
            part2_res = steps

    return part1_res if part1 else part2_res


def part1(lines: list) -> int:
    grid = get_grid(lines)
    return do_steps(grid, 100, part1=True)


def part2(lines: list) -> int:
    grid = get_grid(lines)
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
