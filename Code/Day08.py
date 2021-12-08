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
        return sort_string(''.join(set(a) - set(b)))
    else:
        return sort_string(''.join(set(b) - set(a)))


def find_similar(a: str, b: str) -> str:
    a = set(a)
    b = set(b)
    if len(a) > len(b):
        return sort_string(''.join(a.intersection(b)))
    else:
        return sort_string(''.join(b.intersection(a)))


class Proccessed_line:
    def __init__(self, inputs: list, outputs: list) -> None:
        self.outputs = outputs
        self.inputs = inputs


def process_line(line: str) -> Proccessed_line:

    raw = line.split(" | ")
    inputs = raw[0].split(" ")
    outputs = raw[1].split(" ")
    inputs = [sort_string(i) for i in inputs]
    outputs = [sort_string(i) for i in outputs]
    return Proccessed_line(inputs, outputs)


def solve(processed: Proccessed_line) -> DefaultDict[int, str]:
    five_characters = set()
    six_characters = set()
    segments = DefaultDict(str)
    known_values = DefaultDict(str)
    for value in processed.inputs:
        length = len(value)
        if length == 2:
            known_values["1"] = value
        elif length == 3:
            known_values["7"] = value
        elif length == 4:
            known_values["4"] = value
        elif length == 7:
            known_values["8"] = value
        elif length == 5:
            five_characters.add(value)
        elif length == 6:
            six_characters.add(value)

    segments[1] = find_diff(known_values["1"], known_values["7"])
    temp = known_values["4"] + segments[1]
    for num in six_characters:
        if len(find_diff(num, temp)) == 1:
            known_values["9"] = num
            six_characters.remove(num)
            break

    for num in five_characters:
        if len(find_diff(num, known_values["9"])) != 1:
            known_values["2"] = num
            five_characters.remove(num)
            break

    temp = find_diff(known_values["9"], known_values["7"])
    for num in six_characters:
        if len(find_diff(num, temp)) == 3:
            known_values["6"] = num
        else:
            known_values["0"] = num

    segments[3] = find_diff(known_values["8"], known_values["6"])

    for num in five_characters:
        if segments[3] in num:
            known_values["3"] = num
        else:
            known_values["5"] = num
    return known_values


def get_output_num(raw_line: str) -> int:
    processed = process_line(raw_line)
    known_values = solve(processed)
    out = ""
    keys = list(known_values.keys())
    values = list(known_values.values())
    for output in processed.outputs:
        out += keys[values.index(output)]
    return int(out)


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
        running_sum += get_output_num(line)
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
