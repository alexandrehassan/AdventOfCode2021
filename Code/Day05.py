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
            self.order()
        else:
            self.orderDiagonal()

    @property
    def slope(self) -> int:
        if self.x2 - self.x1 > 0 and self.y2 - self.y1 > 0 or \
                self.x2 - self.x1 < 0 and self.y2 - self.y1 < 0:
            return 1
        else:
            return -1

    def part1Count(self) -> bool:
        return self.isHorizontal or self.isVertical

    def order(self) -> int:
        if self.x1 > self.x2 or self.y1 > self.y2:
            self.x1, self.y1, self.x2, self.y2 =\
                self.x2, self.y2, self.x1, self.y1

    def orderDiagonal(self):
        if self.x1 > self.x2:
            self.x1, self.y1, self.x2, self.y2 =\
                self.x2, self.y2, self.x1, self.y1

    def getCoords(self):
        if self.isVertical:
            for i in range(self.y1, self.y2 + 1):
                yield (i, self.x1)
        elif self.isHorizontal:
            for i in range(self.x1, self.x2+1):
                yield (self.y1, i)
        else:
            b = self.y1 - (self.slope * self.x1)
            x_range = abs(self.x2 - self.x1)
            for i in range(x_range+1):
                x = self.x1 + i
                yield (self.slope * x + b, x)

    def __str__(self) -> str:
        return f"{self.x1},{self.y1}->{self.x2},{self.y2}"


def get_num_dangers(part1: bool) -> int:
    vents = [Vent(i) for i in input]
    grid = DefaultDict(int)
    if part1:
        vents = list(filter(lambda x: x.part1Count(), vents))
    for vent in vents:
        for coord in vent.getCoords():
            grid[coord] += 1
    return sum(1 for i in grid.values() if i >= 2)


def part1():
    return get_num_dangers(part1=True)


def part2():
    return get_num_dangers(part1=False)


def main():
    # Part 1: 7468
    print(f"Part 1: {part1()}")
    # Part 2: 22364
    print(f"Part 2: {part2()}")

    # Part 1: 0.049304637000000005s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.098618044s
    print(f"Part 2: {time_function(part2)}s")


def test():
    part1_result = part1()
    print(f"Part 1: {part1_result}")
    assert part1_result == 7468
    part2_result = part2()
    print(f"Part 2: {part2_result}")
    assert part2_result == 22364

    print(f"Part 1: {time_function(part1,10)}s")
    print(f"Part 2: {time_function(part2,10)}s")


input = get_lines("Inputs/Day05.txt")

if __name__ == "__main__":
    main()
