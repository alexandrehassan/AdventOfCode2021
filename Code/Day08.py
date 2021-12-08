"""
For problem statement:
    https://adventofcode.com/2021/day/1
@author: Alexandre Hassan
"""
from typing import DefaultDict
from Common import get_lines, time_function


def sort_string(string: str):
    return ''.join(sorted(string))


def find_diff(a: str, b: str) -> str:
    if len(a) > len(b):
        for ch in b:
            a = a.replace(ch, "")
        return a
    else:
        for ch in a:
            b = b.replace(ch, "")
        return b


def find_similar(a: str, b: str) -> str:
    sim = ""
    if len(a) > len(b):
        for ch in b:
            if ch in a:
                sim += ch

    else:
        for ch in a:
            if ch in a:
                sim += ch
    return sim


class L:
    def __init__(self, long_5: list, long_6: list, all_sequence: list,
                 outputs: list) -> None:
        self.long_5 = long_5
        self.long_6 = long_6
        self.all_sequence = all_sequence
        self.outputs = outputs


def process_line(line: str) -> L:
    long_5 = set()
    long_6 = set()
    raw = line.split(" | ")
    inputs = raw[0].split(" ")
    outputs = raw[1].split(" ")
    inputs = [sort_string(i) for i in inputs]
    outputs = [sort_string(i) for i in outputs]
    all_num = inputs + outputs
    return L(long_5, long_6, all_num, outputs)


def solve(processed: L) -> DefaultDict[int, str]:
    segments = DefaultDict(str)
    known_values = DefaultDict(str)
    for value in processed.all_sequence:
        length = len(value)
        if length == 2:
            known_values[1] = value
        elif length == 3:
            known_values[7] = value
        elif length == 4:
            known_values[4] = value
        elif length == 7:
            known_values[8] = value
        elif length == 5:
            processed.long_5.add(value)
        elif length == 6:
            processed.long_6.add(value)

    segments[1] = find_diff(known_values[1], known_values[7])
    temp = known_values[4] + segments[1]
    for num in processed.long_6:
        if len(find_diff(num, temp)) == 1:
            known_values[9] = num
            processed.long_6.remove(num)
            break

    segments[5] = find_diff(known_values[9], known_values[8])
    segments[7] = find_diff(known_values[9], known_values[4] + segments[1])
    for num in processed.long_5:
        if len(find_diff(num, known_values[9])) != 1:
            known_values[2] = num
            processed.long_5.remove(num)
            break
    temp = find_diff(known_values[9], known_values[7])
    for num in processed.long_6:
        if len(find_diff(num, temp)) == 3:
            known_values[6] = num
        else:
            known_values[0] = num
    segments[3] = find_diff(known_values[8], known_values[6])
    segments[4] = find_diff(known_values[8], known_values[0])
    segments[6] = find_diff(known_values[1], segments[3])
    segments[2] = find_diff(known_values[8], segments[6] + known_values[2])
    known_values[5] = find_diff(known_values[9], segments[3])
    known_values[3] = find_diff(known_values[9], segments[2])
    return known_values


def get_output_num(line: L, known_values: DefaultDict[int, str]) -> int:
    out = ""
    keys = list(known_values.keys())
    values = list(known_values.values())
    for output in line.outputs:
        out += str(keys[values.index(output)])
    return int(out)


def get_value(segments: DefaultDict, output: str):
    if len(output) == 2:
        return 1
    elif len(output) == 3:
        return 7
    elif len(output) == 4:
        return 4
    elif len(output) == 7:
        return 8
    elif len(output) == 5:
        if segments[6] in output:
            if segments[2] in output:
                return 5
            else:
                return 3
        else:
            return 2
    else:
        if segments[4] not in output:
            return 0
        elif segments[3] in output:
            return 6
        else:
            return 9


def part1(lines: list) -> int:
    output_values = []
    for line in lines:
        out = line.split(" | ")[1]
        output_values.extend(out.split(" "))
    return len(list(filter(lambda x: len(x) == 2 or len(
        x) == 4 or len(x) == 3 or len(x) == 7, output_values)))


def part2(lines: list) -> int:
    running_sum = 0
    for line in lines:
        line_info = process_line(line)
        running_sum += get_output_num(line_info, solve(line_info))
    return running_sum


def main():
    lines = get_lines("Inputs/Day08.txt")
    # Part 1: 504
    print(f"Part 1: {part1(lines)}")
    # Part 2: 1073431
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.00021447399999999998s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.005627696000000001s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()
