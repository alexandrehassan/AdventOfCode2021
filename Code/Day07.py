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


def part1() -> int:
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


def part2() -> int:
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
    part1_result = part1()
    print(f"Part 1: {part1_result}")
    assert part1_result == 364898

    part2_result = part2()
    print(f"Part 2: {part2_result}")
    assert part2_result == 104149091


def main():
    # Part 1: 351092
    print(f"Part 1: {part1()}")
    # Part 2: 104149091
    print(f"Part 2: {part2()}")

    # Part 1: 0.0009632410000000002s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.931904042s
    print(f"Part 2: {time_function(part2)}s")


lines = get_lines("Inputs/Day07.txt")

if __name__ == "__main__":
    main()
