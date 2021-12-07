"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


def calculate(CO2: bool, lines: list) -> int:
    bytes = lines
    count_1 = 0
    to_remove = '1'

    for i in range(len(bytes)):
        count_1 = len(
            list(filter(lambda x: x[i] == '1', bytes)))
        to_remove = '0' if CO2 != (count_1 >= len(bytes)/2) else '1'

        bytes = list(
            filter(lambda x: x[i] == to_remove, bytes))

        if len(bytes) == 1:
            return int(bytes[0], 2)


def flip_bit(string: str) -> int:
    return int(string.replace('1', '2').replace('0', '1').replace('2', '0'), 2)


def part1(lines: list) -> int:
    line_length = len(lines[0])
    num_lines = len(lines)
    count_1 = [0] * line_length

    for line in lines:
        for j in range(line_length):
            count_1[j] += int(line[j])

    gamma = ""
    for count in count_1:
        gamma += '0' if count >= int(num_lines/2) else '1'
    return int(gamma, 2) * flip_bit(gamma)


def part2(lines: list) -> int:
    return calculate(True, lines) * calculate(False, lines)


def main():
    lines = get_lines("Inputs/Day03.txt")
    # Part 1: 3633500
    print(f"Part 1: {part1(lines)}")
    # Part 2: 4550283
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0010945069999999998s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.0007929939999999999s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


def test():
    lines = get_lines("Inputs/Day03_sample.txt")

    result = part1(lines)
    print(f"Part 1 sample: {result}")
    assert(result == 198)

    result = part2(lines)
    print(f"Part 2 sample: {result}")
    assert(result == 230)

    lines = get_lines("Inputs/Day03.txt")
    result = part1(lines)
    print(f"Part 1: {result}")
    assert(result == 3633500)

    result = part2(lines)
    print(f"Part 2: {result}")
    assert(result == 4550283)

    # Part 1: 0.0010945069999999998s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.0007929939999999999s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    test()
