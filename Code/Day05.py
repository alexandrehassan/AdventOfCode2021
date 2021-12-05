"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
"""
from Common import get_lines, time_function
import re


class Vent:
    def __init__(self, line: str):
        self.x1, self.y1, self.x2, self.y2 = int(
            line[0]), int(line[1]), int(line[2]), int(line[3])
        self.isVertical = self.x1 == self.x2
        self.isHorizontal = self.y1 == self.y2
        if self.isHorizontal or self.isVertical:
            self.x1, self.x2 = self.order(self.x1, self.x2)
            self.y1, self.y2 = self.order(self.y1, self.y2)
        self.isDiagonal = not self.isVertical and not self.isHorizontal
        self.posDiagonal = self.positiveSlope()
        if self.isDiagonal:
            if self.posDiagonal:
                self.x1, self.x2 = self.order(self.x1, self.x2)
                self.y1, self.y2 = self.order(self.y1, self.y2)
            else:
                self.x1, self.x2 = self.order(self.x1, self.x2)
                self.y2, self.y1 = self.order(self.y1, self.y2)

    def positiveSlope(self) -> bool:
        return self.x2 - self.x1 > 0 and self.y2 - self.y1 > 0 or \
            self.x2 - self.x1 < 0 and self.y2 - self.y1 < 0

    def part1Count(self):
        return self.isHorizontal or self.isVertical

    def order(self, z1: int, z2: int) -> int:
        if z1 < z2:
            return z1, z2
        else:
            return z2, z1

    def __str__(self) -> str:
        return f"{self.x1},{self.y1}->{self.x2},{self.y2}"


def part1() -> int:
    lines = [re.split(',| ->', i) for i in input]
    vents = [Vent(i) for i in lines]
    grid = [[0 for i in range(1000)] for j in range(1000)]

    toCheck = list(filter(lambda x: x.part1Count(), vents))

    for vent in toCheck:
        # print("-"*20)
        # print(vent)
        # for row in grid:
        #     print(row)
        if vent.isVertical:
            for i in range(vent.x1, vent.x2 + 1):
                grid[i][vent.y1] += 1
        else:
            for i in range(vent.y1, vent.y2+1):
                grid[vent.x1][i] += 1
    count = 0

    for row in grid:
        count += sum(col >= 2 for col in row)
    return count


def part2() -> int:
    lines = [re.split(',| ->', i) for i in input]
    vents = [Vent(i) for i in lines]
    grid = [[0 for i in range(1000)] for j in range(1000)]

    for vent in vents:
        # print("-"*20)
        # print(vent)
        # for row in grid:
        #     print(row)
        if vent.isVertical:
            for i in range(vent.y1, vent.y2 + 1):
                grid[i][vent.x1] += 1
        elif vent.isHorizontal:
            for i in range(vent.x1, vent.x2+1):
                grid[vent.y1][i] += 1
        else:
            if vent.posDiagonal:
                row, col = vent.y1, vent.x1
                for i in range(vent.x2 - vent.x1 + 1):
                    grid[row][col] += 1
                    row += 1
                    col += 1
            else:
                row, col = vent.y1, vent.x1
                for i in range(vent.x2 - vent.x1 + 1):
                    grid[row][col] += 1
                    row -= 1
                    col += 1
    count = 0

    for row in grid:
        # print(row)
        count += sum(col >= 2 for col in row)

    return count


def main():
    # Part 1: 7468
    # print(f"Part 1: {part1()}")
    # Part 2: 4550283
    print(f"Part 2: {part2()}")
    # Too high: 23482

    # # Part 1: 0.0010945069999999998s
    # print(f"Part 1: {time_function(part1)}s")
    # # Part 2: 0.0007929939999999999s
    # print(f"Part 2: {time_function(part2)}s")


input = get_lines("Inputs/Day05.txt")

if __name__ == "__main__":
    main()
