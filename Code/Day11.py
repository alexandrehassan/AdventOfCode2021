"""
For problem statement:
    https://adventofcode.com/2021/day/11
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


def get_adjacent_points(row: int, col: int, num_lines: int, num_col: int) -> list:
    adjacent_points = []

    if row > 0:
        adjacent_points.append((row - 1, col))
    if row < num_lines - 1:
        adjacent_points.append((row + 1, col))
    if col > 0:
        adjacent_points.append((row, col - 1))
    if col < num_col - 1:
        adjacent_points.append((row, col + 1))
    if row > 0 and col > 0:
        adjacent_points.append((row - 1, col - 1))
    if row > 0 and col < num_col - 1:
        adjacent_points.append((row - 1, col + 1))
    if row < num_lines - 1 and col > 0:
        adjacent_points.append((row + 1, col - 1))
    if row < num_lines - 1 and col < num_col - 1:
        adjacent_points.append((row + 1, col + 1))

    return adjacent_points


def get_neighbors(row: int, col: int, grid: list) -> list:
    neighbors = set()
    value = grid[row][col]
    adjacent_points = get_adjacent_points(row, col, len(grid), len(grid[0]))

    for adj in adjacent_points:
        adj_value = grid[adj[0]][adj[1]]
        if adj_value > value and adj_value != 9:
            neighbors.add(adj)

    return neighbors


def get_grid(lines: list) -> list:
    grid = []

    for line in lines:
        grid.append(list(map(int, (list(line)))))

    return grid


def flash(grid: list, row: int, col: int):
    adjacent = get_adjacent_points(row, col, len(grid), len(grid[0]))
    count = 0
    for adj in adjacent:
        grid[adj[0]][adj[1]] += 1
        if grid[adj[0]][adj[1]] > 9:
            count += flash(grid, adj[0], adj[1])
    return count


def do_step(grid: list):
    flashed = set()
    done = False
    while not done:
        for row, line in enumerate(grid):
            for col in range(len(line)):
                if grid[row][col] > 9 and (row, col) not in flashed:
                    flashed.add((row, col))
                    flash(grid, row, col, 0)
        done = is_done(grid, flashed)


def is_done(grid, flashed):
    for row, line in enumerate(grid):
        for col in range(len(line)):
            if (row, col) not in flashed and grid[row][col] > 9:
                done = False
    return True


def simulate_steps(grid: list, steps: int):

    for _ in range(steps):
        for row, line in enumerate(grid):
            grid[row] = list(map(lambda x: x+1, line))
        do_step(grid)


def part1(lines: list) -> int:
    grid = get_grid(lines)
    simulate_steps(grid, 100)


def part2(lines: list) -> int:
    pass


def main():
    lines = get_lines("Inputs/Day11_sample.txt")
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
