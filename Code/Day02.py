"""
For problem statement:
    https://adventofcode.com/2021/day/2
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


def part1(lines: list) -> int:
    posX, posY = 0, 0
    for line in lines:
        instruction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        if instruction == "up":
            posY -= distance
        elif instruction == "down":
            posY += distance
        elif instruction == "forward":
            posX += distance
        else:
            print("Something went wrong")
    return posX * posY


def part2(lines: list) -> int:
    posX, posY, aim = 0, 0, 0
    for line in lines:
        instruction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        if instruction == "up":
            aim -= distance
        elif instruction == "down":
            aim += distance
        elif instruction == "forward":
            posX += distance
            posY += aim * distance
        else:
            print("Something went wrong")
    return posX * posY


def main():
    lines = get_lines("Inputs/Day02.txt")
    # Part 1: 1989265
    print(f"Part 1: {part1(lines)}")
    # Part 2: 2089174012
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0007306340010836721s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.0008213049988262355s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


def test():
    lines = get_lines("Inputs/Day02_sample.txt")

    result = part1(lines)
    print(f"Part 1 sample: {result}")
    assert(result == 150)

    result = part2(lines)
    print(f"Part 2 sample: {result}")
    assert(result == 900)

    lines = get_lines("Inputs/Day02.txt")
    result = part1(lines)
    print(f"Part 1: {result}")
    assert(result == 1989265)

    result = part2(lines)
    print(f"Part 2: {result}")
    assert(result == 2089174012)

    # Part 1: 0.0007306340010836721s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.0008213049988262355s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    test()
