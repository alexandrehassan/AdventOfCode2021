"""
For problem statement:
    https://adventofcode.com/2021/day/4
@author: Alexandre Hassan
"""
from Common import time_function


class Board:
    def __init__(self, raw_board: str) -> None:
        self.board = [[int(x) for x in row.split()]
                      for row in raw_board.split('\n')]

        self.won = False

    def check_win(self) -> bool:
        for row in self.board:
            if sum(row) == 0:
                return True

        for col in range(5):
            if self.board[0][col] + \
                    self.board[1][col] + \
                    self.board[2][col] +\
                    self.board[3][col] +\
                    self.board[4][col] == 0:
                return True

    def called(self, called: int) -> int:
        for row in range(5):
            index = self.get_index(row, called)
            if index != -1:
                self.board[row][index] = 0
                if self.check_win():
                    self.won = True
                    return self.calculate_score(called)
                else:
                    return -1
        return -1

    def calculate_score(self, winningNum: int) -> int:
        score = 0
        for row in self.board:
            score += sum(row)
        return score * winningNum

    def get_index(self, row: int, toFind: int) -> int:
        try:
            return self.board[row].index(toFind)
        except ValueError:
            return -1


def getInformation(filename: str):
    with open(filename) as file:
        calls = list(map(int, (next(file).rstrip()).split(",")))
        next(file)
        raw_boards = file.read().split('\n\n')

    boards = [Board(raw_board.rstrip()) for raw_board in raw_boards]

    return calls, boards


def part1(calls: list, boards: list) -> int:
    result = -1
    for call in calls:
        for board in boards:
            result = board.called(call)
            if result != -1:
                return result


def part2(calls: list, boards: list) -> int:
    result = -1
    for call in calls:
        for board in boards:
            result = board.called(call)
            if result != -1 and len(boards) == 1:
                return result
        boards = list(filter(lambda x: not x.won, boards))


def main():
    instructions, lines = getInformation("Inputs/Day04.txt")
    # Part 1: 35711
    print(f"Part 1: {part1(instructions, lines)}")
    # Part 2: 5586
    print(f"Part 2: {part2(instructions, lines)}")

    # Part 1: 0.012491363s
    print(f"Part 1: {time_function(lambda: part1(instructions, lines))}s")
    # Part 2: 0.00029262300000000075s
    print(f"Part 2: {time_function(lambda: part2(instructions, lines))}s")


def test():
    instructions, lines = getInformation("Inputs/Day04_sample.txt")

    result = part1(instructions, lines)
    print(f"Part 1 sample: {result}")
    assert(result == 4512)

    result = part2(instructions, lines)
    print(f"Part 2 sample: {result}")
    assert(result == 1924)

    instructions, lines = getInformation("Inputs/Day04.txt")
    result = part1(instructions, lines)
    print(f"Part 1: {result}")
    assert(result == 35711)

    result = part2(instructions, lines)
    print(f"Part 2: {result}")
    assert(result == 5586)

    # Part 1: 0.012491363s
    print(f"Part 1: {time_function(lambda: part1(instructions, lines))}s")
    # Part 2: 0.00029262300000000075s
    print(f"Part 2: {time_function(lambda: part2(instructions, lines))}s")


if __name__ == "__main__":
    test()
