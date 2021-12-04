"""
For problem statement:
    https://adventofcode.com/2021/day/1
@author: Alexandre Hassan
"""
from Common import get_int_lines, time_function


def part1() -> int:
    count_increases = 0
    count_of_lines = len(lines)
    for i in range(1, count_of_lines):
        if lines[i] > lines[i - 1]:
            count_increases += 1
    return count_increases


def part2() -> int:
    count_increases = 0
    count_of_lines = len(lines)
    for i in range(1, count_of_lines - 1):
        current_slide = sum(lines[i-1:i+2])
        next_slide = sum(lines[i:i+3])
        # print(f"{current_slide} , {next_slide} at {i}")
        if current_slide < next_slide:
            count_increases += 1
    return count_increases


lines = get_int_lines("Inputs/Day01.txt")


def main():
    # Part 1: 1184
    print(f"Part 1: {part1()}")
    # Part 2: 1158
    print(f"Part 2: {part2()}")

    # Part 1: 0.0005400190013460815s
    print(f"Part 1: {time_function(part1)}s")
    # Part 1: 0.0019921099999919535s
    print(f"Part 2: {time_function(part2)}s")


if __name__ == "__main__":
    main()
