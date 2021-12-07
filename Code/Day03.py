"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


def get_O2(lines: list) -> int:
    O2_lines = lines
    count_1 = 0
    char_checking = 0
    to_pop = '1'

    while True:
        count_1 = len(
            list(filter(lambda x: x[char_checking] == '1', O2_lines)))

        to_pop = '1' if count_1 >= len(O2_lines)/2 else '0'

        O2_lines = list(
            filter(lambda x: x[char_checking] == to_pop, O2_lines))

        char_checking += 1

        if len(O2_lines) == 1:
            return int(O2_lines[0], 2)


def get_CO2(lines: list) -> int:
    CO2_lines = lines
    count_1 = 0
    char_checking = 0
    to_pop = '1'

    while True:
        count_1 = len(
            list(filter(lambda x: x[char_checking] == '1', CO2_lines)))
        to_pop = '0' if count_1 >= len(CO2_lines)/2 else '1'

        CO2_lines = list(
            filter(lambda x: x[char_checking] == to_pop, CO2_lines))

        char_checking += 1
        if len(CO2_lines) == 1:
            return int(CO2_lines[0], 2)


def part1(lines: list) -> int:
    line_length = len(lines[0])
    num_lines = len(lines)
    count_1 = [0] * line_length

    for line in lines:
        for j in range(line_length):
            count_1[j] += int(line[j])

    gamma = ""
    epsilon = ""
    for count in count_1:
        if count > num_lines/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)


def part2(lines: list) -> int:
    return get_CO2(lines) * get_O2(lines)


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
