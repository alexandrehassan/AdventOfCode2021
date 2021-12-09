"""
For problem statement:
    https://adventofcode.com/2021/day/9
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


def get_neighbors(point: tuple, grid: list) -> list:
    neighbors = set()
    col_max = len(grid[0])
    row_max = len(grid)
    row, col = point
    if row > 0:
        if grid[row - 1][col] > grid[row][col] and grid[row - 1][col] != 9:
            neighbors.add((row - 1, col))
    if col > 0:
        if grid[row][col - 1] > grid[row][col] and grid[row][col - 1] != 9:
            neighbors.add((row, col - 1))
    if row < row_max - 1:
        if grid[row + 1][col] > grid[row][col] and grid[row + 1][col] != 9:
            neighbors.add((row + 1, col))
    if col < col_max - 1:
        if grid[row][col + 1] > grid[row][col] and grid[row][col + 1] != 9:
            neighbors.add((row, col + 1))
    return neighbors


def product_largest_3(nums: list) -> list:
    nums.sort(reverse=True)
    nums = nums[:3]
    return nums[0] * nums[1] * nums[2]


def part1(lines: list) -> int:
    grid = []
    risk_level = 0
    for line in lines:
        grid.append(list(map(int, (list(line)))))
    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if col == len(line) - 1 and row == len(grid) - 1:
                if grid[row - 1][col] > value and grid[row][col - 1] > value:
                    risk_level += value + 1
            elif col == len(line) - 1:
                if grid[row - 1][col] > value and grid[row + 1][col] > value \
                        and grid[row][col - 1] > value:
                    risk_level += value + 1
            elif row == len(grid) - 1:
                if grid[row - 1][col] > value and grid[row][col + 1] > value \
                        and grid[row][col - 1] > value:
                    risk_level += value + 1
            elif row == 0 and col == 0:
                if grid[row + 1][col] > value and grid[row][col + 1] > value:
                    risk_level += value + 1
            elif row == 0:
                if grid[row + 1][col] > value and grid[row][col + 1] > value \
                        and grid[row][col - 1] > value:
                    risk_level += value + 1
            elif col == 0:
                if grid[row + 1][col] > value and grid[row - 1][col] > value \
                        and grid[row][col + 1] > value:
                    risk_level += value + 1
            else:
                if grid[row + 1][col] > value and grid[row - 1][col] > value \
                    and grid[row][col + 1] > value \
                        and grid[row][col - 1] > value:
                    risk_level += value + 1
    return risk_level


def part2(lines: list) -> int:
    grid = []
    low_points = {}
    for line in lines:
        grid.append(list(map(int, (list(line)))))
    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if col == len(line) - 1 and row == len(grid) - 1:
                if grid[row - 1][col] > value and grid[row][col - 1] > value:
                    low_points[(row, col)] = get_neighbors((row, col), grid)
            elif col == len(line) - 1:
                if grid[row - 1][col] > value and grid[row + 1][col] > value \
                        and grid[row][col - 1] > value:
                    low_points[(row, col)] = get_neighbors((row, col), grid)
            elif row == len(grid) - 1:
                if grid[row - 1][col] > value and grid[row][col + 1] > value \
                        and grid[row][col - 1] > value:
                    low_points[(row, col)] = get_neighbors((row, col), grid)
            elif row == 0 and col == 0:
                if grid[row + 1][col] > value and grid[row][col + 1] > value:
                    low_points[(row, col)] = get_neighbors((row, col), grid)
            elif row == 0:
                if grid[row + 1][col] > value and grid[row][col + 1] > value \
                        and grid[row][col - 1] > value:
                    low_points[(row, col)] = get_neighbors((row, col), grid)
            elif col == 0:
                if grid[row + 1][col] > value and grid[row - 1][col] > value \
                        and grid[row][col + 1] > value:
                    low_points[(row, col)] = get_neighbors((row, col), grid)
            else:
                if grid[row + 1][col] > value and grid[row - 1][col] > value \
                    and grid[row][col + 1] > value \
                        and grid[row][col - 1] > value:
                    low_points[(row, col)] = get_neighbors((row, col), grid)

    basins = []
    for low_point in low_points.keys():
        to_check = low_points[low_point].copy()
        checked = set()
        while len(to_check) > 0:
            current = to_check.pop()
            if current not in checked:
                neighbors = get_neighbors(current, grid)
                low_points[low_point].update(neighbors)
                to_check.update(neighbors)
                checked.add(current)
        basins.append(len(low_points[low_point]) + 1)

    basins.sort()
    return product_largest_3(basins)


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
