"""
For problem statement:
    https://adventofcode.com/2021/day/1
@author: Alexandre Hassan
"""
from typing import DefaultDict
from Common import get_lines, time_function


class Display:
    def __init__(self, line: str):
        self.long_5 = set()
        self.long_6 = set()
        raw = line.split(" | ")
        inputs = raw[0].split(" ")
        outputs = raw[1].split(" ")
        inputs = [sort_string(i) for i in inputs]
        self.outputs = [sort_string(i) for i in outputs]
        self.all_num = inputs + self.outputs
        self.known_values = DefaultDict(str)
        self.segments = self.find_segments()

    def get_sum(self):
        out = []
        keys = list(self.known_values.keys())
        values = list(self.known_values.values())
        for output in self.outputs:
            out.append(str(keys[values.index(output)]))
        out_str = "".join(out)
        return int(out_str)

    # def get_known_values(self):
    #     known_values = DefaultDict()
    #     for value in self.all_num:
    #         length = len(value)
    #         if length == 2:
    #             known_values[1] = value
    #         elif length == 3:
    #             known_values[7] = value
    #         elif length == 4:
    #             known_values[4] = value
    #         elif length == 7:
    #             known_values[8] = value
    #         elif length == 5:
    #             self.long_5.append(value)
    #         elif length == 6:
    #             self.long_6.append(value)
    #     segments[1] = find_diff(known_values[1], known_values[7])
    #     return known_values

    def find_segments(self):
        segments = DefaultDict(str)
        for value in self.all_num:
            length = len(value)
            if length == 2:
                self.known_values[1] = value
            elif length == 3:
                self.known_values[7] = value
            elif length == 4:
                self.known_values[4] = value
            elif length == 7:
                self.known_values[8] = value
            elif length == 5:
                self.long_5.add(value)
            elif length == 6:
                self.long_6.add(value)

        segments[1] = find_diff(self.known_values[1], self.known_values[7])
        temp = self.known_values[4] + segments[1]
        for num in self.long_6:
            if len(find_diff(num, temp)) == 1:
                self.known_values[9] = num
                break
        segments[5] = find_diff(
            self.known_values[9], self.known_values[8])
        segments[7] = find_diff(
            self.known_values[9], self.known_values[4] + segments[1])
        for num in self.long_5:
            if len(find_diff(num, self.known_values[9])) != 1:
                self.known_values[2] = num
                break
        temp = find_diff(self.known_values[9], self.known_values[7])
        for num in self.long_6:
            if num == self.known_values[9]:
                pass
            elif len(find_diff(num, temp)) == 3:
                self.known_values[6] = num
            else:
                self.known_values[0] = num
        segments[3] = find_diff(
            self.known_values[8], self.known_values[6])
        segments[4] = find_diff(
            self.known_values[8], self.known_values[0])
        segments[6] = find_diff(self.known_values[1], segments[3])
        segments[2] = find_diff(
            self.known_values[8], segments[6] + self.known_values[2])
        self.known_values[5] = find_diff(self.known_values[9], segments[3])
        self.known_values[3] = find_diff(self.known_values[9], segments[2])
        return segments


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
        display = Display(line)
        running_sum += display.get_sum()
    return running_sum


def main():
    lines = get_lines("Inputs/Day08.txt")
    # Part 1: 1184
    print(f"Part 1: {part1(lines)}")
    # Part 2: 1158
    temp = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0005400190013460815s
    # print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 1: 0.0019921099999919535s
    # print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()
