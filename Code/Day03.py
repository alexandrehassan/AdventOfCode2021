from Common import get_lines, time_function


def part1() -> int:
    count_1 = []
    num_lines = len(lines)
    for char in lines[0]:
        if char == '1':
            count_1.append(1)
        else:
            count_1.append(0)
    for i in range(1, num_lines):
        for j in range(0, len(lines[i])):
            if lines[i][j] == '1':
                count_1[j] += 1

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


def get_O2() -> int:
    O2_lines = lines
    count_1 = 0
    char_checking = 0
    found_O2 = False
    to_pop = '1'

    while not found_O2:
        count_1 = len(
            list(filter(lambda x: x[char_checking] == '1', O2_lines)))
        if count_1 >= len(O2_lines)/2:
            to_pop = '1'
        else:
            to_pop = '0'

        O2_lines = list(
            filter(lambda x: x[char_checking] == to_pop, O2_lines))
        char_checking += 1
        if len(O2_lines) == 1:
            return int(O2_lines[0], 2)


def get_CO2() -> int:
    CO2_lines = lines
    count_1 = 0
    char_checking = 0
    found_CO2 = False
    to_pop = '1'

    while not found_CO2:
        count_1 = len(
            list(filter(lambda x: x[char_checking] == '1', CO2_lines)))
        if count_1 >= len(CO2_lines)/2:
            to_pop = '0'
        else:
            to_pop = '1'

        CO2_lines = list(
            filter(lambda x: x[char_checking] == to_pop, CO2_lines))

        char_checking += 1
        if len(CO2_lines) == 1:
            return int(CO2_lines[0], 2)


def char_matches(string: str, char: str, char_position: int) -> bool:
    return string[char_position] == char


def part2() -> int:
    return get_CO2() * get_O2()


def main():
    # Part 1: 3633500
    print(f"Part 1: {part1()}")
    # Part 2: 2089174012
    print(f"Part 2: {part2()}")

    # Part 1: 0.0011276530000000002s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.0008213049988262355s
    # print(f"Part 2: {time_function(part2)}s")


lines = get_lines("Inputs/Day03.txt")

if __name__ == "__main__":
    main()
