"""
For problem statement:
    https://adventofcode.com/2021/day/9
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


def valid(row: int, col: int, grid: list) -> bool:
    try:
        grid[row][col]
        return True
    except IndexError:
        return False


def product_largest_3(nums: list) -> list:
    nums.sort(reverse=True)
    return nums[0] * nums[1] * nums[2]


def get_adjecent_points(row: int, col: int) -> list:
    adjecent_points = []
    if row > 0:
        adjecent_points.append((row - 1, col))
    if row < num_lines - 1:
        adjecent_points.append((row + 1, col))
    if col > 0:
        adjecent_points.append((row, col - 1))
    if col < num_col - 1:
        adjecent_points.append((row, col + 1))
    return adjecent_points


def get_neighbors(point: tuple, grid: list) -> list:
    neighbors = set()
    value = grid[point[0]][point[1]]
    adjecent_points = get_adjecent_points(point[0], point[1])
    for adj_point in adjecent_points:
        if grid[adj_point[0]][adj_point[1]] > value and \
                grid[adj_point[0]][adj_point[1]] != 9:
            neighbors.add(adj_point)
    return neighbors


def is_low_point(row: int, col: int, grid: list) -> bool:
    adjecent_points = get_adjecent_points(row, col)
    for point in adjecent_points:
        if grid[point[0]][point[1]] < grid[row][col]:
            return False
    return True


def find_lowpoints(grid: list) -> list:
    low_points = {}
    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if is_low_point(row, col, grid):
                low_points[(row, col)] = get_neighbors((row, col), grid)
    return low_points


def part1(lines: list) -> int:
    grid = []
    risk_level = 0
    for line in lines:
        grid.append(list(map(int, (list(line)))))
    low_points = find_lowpoints(grid)
    row, line = 0, 0
    for low_point in low_points.keys():
        row, line = low_point
        risk_level += grid[row][line] + 1
    return risk_level


def part2(lines: list) -> int:
    grid = []
    for line in lines:
        grid.append(list(map(int, (list(line)))))

    low_points = find_lowpoints(grid)

    basin_sizes = []
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
            to_check = set(filter(lambda x: x not in checked, to_check))

        basin_sizes.append(len(low_points[low_point]) + 1)

    return product_largest_3(basin_sizes)


def main():
    lines = get_lines("Inputs/Day09.txt")
    global num_col
    num_col = len(lines[0])
    global num_lines
    num_lines = len(lines)
    # Part 1:
    print(f"Part 1: {part1(lines)}")
    # Part 2:
    print(f"Part 2: {part2(lines)}")

    # # Part 1:
    # print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # # Part 2: 0.03372787s
    # print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()
