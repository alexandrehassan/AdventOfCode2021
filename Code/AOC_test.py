# import pytest
from Common import get_int_lines, get_lines
import Day01
import Day02
import Day03
import Day04
import Day05
import Day06
import Day07
import Day08


def test_day01():
    lines = get_int_lines("Inputs/Day01_sample.txt")
    assert Day01.part1(lines) == 7, "Day01 part1 sample failed"
    assert Day01.part2(lines) == 5, "Day01 part2 sample failed"
    lines = get_int_lines("Inputs/Day01.txt")
    assert Day01.part1(lines) == 1184, "Day01 part1 failed"
    assert Day01.part2(lines) == 1158, "Day01 part2 failed"


def test_day02():
    lines = get_lines("Inputs/Day02_sample.txt")
    assert Day02.part1(lines) == 150, "Day02 part1 sample failed"
    assert Day02.part2(lines) == 900, "Day02 part2 sample failed"
    lines = get_lines("Inputs/Day02.txt")
    assert Day02.part1(lines) == 1989265, "Day02 part1 failed"
    assert Day02.part2(lines) == 2089174012, "Day02 part2 failed"


def test_day03():
    lines = get_lines("Inputs/Day03_sample.txt")
    assert Day03.part1(lines) == 198, "Day03 part1 sample failed"
    assert Day03.part2(lines) == 230, "Day03 part2 sample failed"
    lines = get_lines("Inputs/Day03.txt")
    assert Day03.part1(lines) == 3633500, "Day03 part1 failed"
    assert Day03.part2(lines) == 4550283, "Day03 part2 failed"


def test_day04():
    instructions, lines = Day04.get_information("Inputs/Day04_sample.txt")
    assert Day04.part1(instructions, lines) == \
        4512, "Day04 part1 sample failed"
    assert Day04.part2(
        instructions, lines) == 1924, "Day04 part2 sample failed"
    instructions, lines = Day04.get_information("Inputs/Day04.txt")
    assert Day04.part1(instructions, lines) == 35711, "Day04 part1 failed"
    assert Day04.part2(instructions, lines) == 5586, "Day04 part2 failed"


def test_day05():
    lines = get_lines("Inputs/Day05_sample.txt")
    assert Day05.part1(lines) == 5, "Day05 part1 sample failed"
    assert Day05.part2(lines) == 12, "Day05 part2 sample failed"
    lines = get_lines("Inputs/Day05.txt")
    assert Day05.part1(lines) == 7468, "Day05 part1 failed"
    assert Day05.part2(lines) == 22364, "Day05 part2 failed"


def test_day06():
    lines = get_lines("Inputs/Day06_sample.txt")
    assert Day06.part1(lines) == 5934, "Day06 part1 sample failed"
    assert Day06.part2(lines) == 26984457539, "Day06 part2 sample failed"
    lines = get_lines("Inputs/Day06.txt")
    assert Day06.part1(lines) == 351092, "Day06 part1 failed"
    assert Day06.part2(lines) == 1595330616005, "Day06 part2 failed"


def test_day07():
    lines = get_lines("Inputs/Day07_sample.txt")
    assert Day07.part1(lines) == 37, "Day07 part1 sample failed"
    assert Day07.part2(lines) == 168, "Day07 part2 sample failed"
    lines = get_lines("Inputs/Day07.txt")
    assert Day07.part1(lines) == 364898, "Day07 part1 failed"
    assert Day07.part2(lines) == 104149091, "Day07 part2 failed"


def test_day08():
    lines = get_lines("Inputs/Day08_sample.txt")
    assert Day08.part1(lines) == 26, "Day08 part1 sample failed"
    day08_part2_sample = [
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab " +
        "| cdfeb fcadb cdfeb cdbaf"]
    assert Day08.part2((day08_part2_sample)
                       ) == 5353, "Day08 part2 sample failed"
    lines = get_lines("Inputs/Day08.txt")
    assert Day08.part1(lines) == 504, "Day08 part1 failed"
    assert Day08.part2(lines) == 1073431, "Day08 part2 failed"
