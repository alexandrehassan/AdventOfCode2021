"""
For problem statement:
    https://adventofcode.com/2021/day/1
@author: Alexandre Hassan
"""
from Common import get_int_lines, time_function


def part1(lines: list) -> int:
    count_increases = 0
    count_of_lines = len(lines)
    for i in range(1, count_of_lines):
        if lines[i] > lines[i - 1]:
            count_increases += 1
    return count_increases


def part2(lines: list) -> int:
    count_increases = 0
    count_of_lines = len(lines)
    for i in range(1, count_of_lines - 1):
        current_slide = sum(lines[i-1:i+2])
        next_slide = sum(lines[i:i+3])
        # print(f"{current_slide} , {next_slide} at {i}")
        if current_slide < next_slide:
            count_increases += 1
    return count_increases


def main():
    lines = get_int_lines("Inputs/Day01.txt")
    # Part 1: 1184
    print(f"Part 1: {part1(lines)}")
    # Part 2: 1158
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0005400190013460815s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 1: 0.0019921099999919535s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


def test():
    lines = get_int_lines("Inputs/Day01_sample.txt")

    result = part1(lines)
    print(f"Part 1 sample: {result}")
    assert(result == 7)

    result = part2(lines)
    print(f"Part 2 sample: {result}")
    assert(result == 5)

    lines = get_int_lines("Inputs/Day01.txt")
    result = part1(lines)
    print(f"Part 1: {result}")
    assert(result == 1184)

    result = part2(lines)
    print(f"Part 2: {result}")
    assert(result == 1158)

    # Part 1: 0.0005400190013460815s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 1: 0.0019921099999919535s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    test()
