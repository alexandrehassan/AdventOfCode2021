"""
For problem statement:
    https://adventofcode.com/2021/day/4
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


class Board:
    def __init__(self, board: list) -> None:
        self.board = board
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
        return -1

    def calculate_score(self, winningNum: int) -> int:
        score = 0
        for row in range(5):
            for col in range(5):
                score += self.board[row][col]
        return score * winningNum

    def get_index(self, row: int, toFind: int) -> int:
        try:
            return self.board[row].index(toFind)
        except ValueError:
            return -1


def makeBoards(lines: list) -> list:
    board = []
    boards = []
    board_row = 0
    for row in lines:
        if row == '':
            boards.append(Board(board))
            board_row = 0
            board = []
        else:
            board.append(list(
                map(int, list(filter(lambda x: x != "", row.split(" "))))))
            board_row += 1
    return boards


def part1() -> int:
    boards = makeBoards(lines)

    result = -1
    for call in calls:
        for board in boards:
            result = board.called(call)
            if result != -1:
                return result


def part2() -> int:
    boards = makeBoards(lines)

    result = -1
    for call in calls:
        for board in boards:
            result = board.called(call)
            if result != -1 and len(boards) == 1:
                return result
        boards = list(filter(lambda x: not x.won, boards))


def main():
    # Part 1: 35711
    print(f"Part 1: {part1()}")
    # Part 2: 5586
    print(f"Part 2: {part2()}")

    # Part 1: 0.007785375999999999s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.017704187s
    print(f"Part 2: {time_function(part2)}s")


def test():
    # Part 1: 35711
    part1_result = part1()
    print(f"Part 1: {part1_result}")
    assert part1_result == 35711
    # Part 2: 5586
    part2_result = part2()
    print(f"Part 2: {part2_result}")
    assert part2_result == 5586

    # Part 1: 0.007785375999999999s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.017704187s
    print(f"Part 2: {time_function(part2)}s")


lines = get_lines("Inputs/Day04.txt")
calls = list(map(int, lines.pop(0).split(",")))
lines.pop(0)

if __name__ == "__main__":
    test()
