"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


def part1() -> int:
    # Only one line here
    fishes = lines[0].split(',')
    fishes = list(map(int, fishes))
    for day in range(NUM_DAYS):
        to_append = 0
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                to_append += 1
            else:
                fishes[i] -= 1
        for i in range(to_append):
            fishes.append(8)
        to_append = 0
    return len(fishes)


def part2() -> int:
    pass


def main():
    # Part 1: 3633500
    print(f"Part 1: {part1()}")
    # # Part 2: 4550283
    # print(f"Part 2: {part2()}")

    # # Part 1: 0.0010945069999999998s
    # print(f"Part 1: {time_function(part1)}s")
    # # Part 2: 0.0007929939999999999s
    # print(f"Part 2: {time_function(part2)}s")


def test():
    part1_result = part1()
    assert part1_result == 7468
    part2_result = part2()
    assert part2_result == 22364

    # Part 1: 0.11251974499999999s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.117770411s
    print(f"Part 2: {time_function(part2)}s")


lines = get_lines("Inputs/Day06.txt")
NUM_DAYS = 80

if __name__ == "__main__":
    main()
