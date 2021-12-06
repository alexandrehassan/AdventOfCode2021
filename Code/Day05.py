"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
"""
from typing import DefaultDict
from Common import get_lines, time_function
import re


class Vent:
    def __init__(self, input: str):
        line = re.split(',| ->', input)
        self.x1, self.y1, self.x2, self.y2 = int(
            line[0]), int(line[1]), int(line[2]), int(line[3])
        self.isVertical = self.x1 == self.x2
        self.isHorizontal = self.y1 == self.y2
        if self.isHorizontal or self.isVertical:
            self.x1, self.x2 = self.order(self.x1, self.x2)
            self.y1, self.y2 = self.order(self.y1, self.y2)
            return
        self.x1, self.y1, self.x2, self.y2 = self.orderDiagonal()
        # self.posDiagonal = self.positiveSlope()
        # if self.posDiagonal:
        #     self.x1, self.x2 = self.order(self.x1, self.x2)
        #     self.y1, self.y2 = self.order(self.y1, self.y2)
        # else:
        #     self.x1, self.x2 = self.order(self.x1, self.x2)
        #     self.y2, self.y1 = self.order(self.y1, self.y2)

    @property
    def slope(self) -> int:
        if self.x2 - self.x1 > 0 and self.y2 - self.y1 > 0 or \
                self.x2 - self.x1 < 0 and self.y2 - self.y1 < 0:
            return 1
        else:
            return -1

    def part1Count(self):
        return self.isHorizontal or self.isVertical

    def order(self, z1: int, z2: int) -> int:
        if z1 < z2:
            return z1, z2
        else:
            return z2, z1

    def orderDiagonal(self):
        if self.x1 < self.x2:
            return self.x1, self.y1, self.x2, self.y2
        else:
            return self.x2, self.y2, self.x1, self.y1

    def getCoords(self) -> list:
        coords = []
        if self.isVertical:
            for i in range(self.y1, self.y2 + 1):
                coords.append((i, self.x1))
        elif self.isHorizontal:
            for i in range(self.x1, self.x2+1):
                coords.append((self.y1, i))
        else:
            b = self.y1 - (self.slope * self.x1)
            x_range = abs(self.x2 - self.x1)
            # print(
            #     f" {self.x1}, {self.y1} -> {self.x2}, {self.y2}   {self.slope}*x + {b} = y {x_range}")
            for i in range(x_range+1):
                x = self.x1 + i
                coords.append((self.slope * x + b, x))

        return coords

    def __str__(self) -> str:
        return f"{self.x1},{self.y1}->{self.x2},{self.y2}"


def part1():
    vents = [Vent(i) for i in input]
    grid = DefaultDict(int)
    vents = list(filter(lambda x: x.part1Count(), vents))
    for vent in vents:
        coords = vent.getCoords()
        for coord in coords:
            grid[coord] += 1
    return len(
        list(filter(lambda x: x >= 2, grid.values())))


def part2():
    vents = [Vent(i) for i in input]
    grid = DefaultDict(int)
    for vent in vents:
        coords = vent.getCoords()
        for coord in coords:
            grid[coord] += 1
    return len(
        list(filter(lambda x: x >= 2, grid.values())))


def main():
    # Part 1: 7468
    print(f"Part 1: {part1()}")
    # Part 2: 22364
    print(f"Part 2: {part2()}")

    # Part 1: 0.049304637000000005s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.10330538100000002s
    print(f"Part 2: {time_function(part2)}s")


def test():
    part1_result = part1()
    assert part1_result == 7468
    part2_result = part2()
    print(f"Part 2: {part2_result}")
    assert part2_result == 22364

    # Part 1: 0.09364735399999999s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.117770411s
    print(f"Part 2: {time_function(part2)}s")


input = get_lines("Inputs/Day05.txt")

if __name__ == "__main__":
    main()
