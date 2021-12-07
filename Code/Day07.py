"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


def sequence(num: int) -> int:
    return num * (num + 1) // 2


def calc(num: int, toCheck: list) -> int:
    return sum(list(map(lambda x: abs(x - num), toCheck)))


def calc_2(num: int, toCheck: list) -> int:
    return sum(list(map(lambda x: sequence(abs(x - num)), toCheck)))


def part1(lines: list) -> int:
    pos = list(map(int, (lines[0].split(","))))
    pos.sort()
    top = len(pos) - 1
    bottom = 0
    middle = (top + bottom) // 2

    while True:
        top_dist = calc(pos[top], pos)
        bottom_dist = calc(pos[bottom], pos)

        if top_dist < bottom_dist:
            bottom = middle
        else:
            top = middle
        if top_dist == bottom_dist:
            return top_dist


def part2(lines: list) -> int:
    pos = list(map(int, (lines[0].split(","))))
    pos.sort()
    top = pos[-1]
    bottom = pos[0]

    while True:
        top_dist = calc_2(top, pos)
        bottom_dist = calc_2(bottom, pos)
        if top_dist < bottom_dist:
            bottom += 1
        else:
            top -= 1
        if top_dist == bottom_dist:
            return top_dist


def test():
    lines = get_lines("Inputs/Day07_sample.txt")

    result = part1(lines)
    print(f"Part 1 sample: {result}")
    assert(result == 37)

    result = part2(lines)
    print(f"Part 2 sample: {result}")
    assert(result == 168)

    lines = get_lines("Inputs/Day07.txt")
    result = part1(lines)
    print(f"Part 1: {result}")
    assert(result == 364898)

    result = part2(lines)
    print(f"Part 2: {result}")
    assert(result == 104149091)

    # Part 1: 0.0009632410000000002s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.931904042s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


def main():
    lines = get_lines("Inputs/Day07.txt")
    # Part 1: 351092
    print(f"Part 1: {part1(lines)}")
    # Part 2: 104149091
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0009632410000000002s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.931904042s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    test()
