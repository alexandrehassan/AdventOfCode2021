"""
For problem statement:
    https://adventofcode.com/2021/day/4
@author: Alexandre Hassan
"""
from Common import get_lines, time_function


class Board:
    # board = []
    # calledBoard = []
    # has_won

    def __init__(self, board: list) -> None:
        self.board = board
        self.calledBoard = [[False]*5 for i in range(5)]
        self.won = False

    def check_win(self) -> bool:
        for line in self.calledBoard:
            if all(line):
                return True

        for i in range(5):
            if self.calledBoard[0][i] and \
                    self.calledBoard[1][i] and \
                    self.calledBoard[2][i] and\
                    self.calledBoard[3][i] and\
                    self.calledBoard[4][i]:
                return True

    def called(self, called: int) -> int:
        for i in range(5):
            index = self.get_index(i, called)
            if index != -1:
                self.calledBoard[i][index] = True
                if self.check_win():
                    self.won = True
                    return self.calculate_score(called)
        return -1

    def calculate_score(self, winningNum: int) -> int:
        score = 0
        for i in range(5):
            for j in range(5):
                if not self.calledBoard[i][j]:
                    score += self.board[i][j]
        return score * winningNum

    def has_won(self) -> bool:
        return self.won

    def get_index(self, lineNum: int, toFind: int) -> int:
        try:
            return self.board[lineNum].index(toFind)
        except ValueError:
            return -1


def makeBoards(lines: list) -> list:
    board = []
    boards = []
    board_row = 0
    for line in lines:
        if line == '':
            boards.append(Board(board))
            board_row = 0
            board = []
        else:
            board.append(list(
                map(int, list(filter(lambda x: x != "", line.split(" "))))))
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
    print("No result")


def part2() -> int:
    boards = makeBoards(lines)

    result = -1
    for call in calls:
        for board in boards:
            result = board.called(call)
            if result != -1 and len(boards) == 1:
                return result
        boards = list(filter(lambda x: not x.has_won(), boards))


def main():
    # Part 1: 35711
    print(f"Part 1: {part1()}")
    # Part 2: 5586
    print(f"Part 2: {part2()}")

    # Part 1: 0.007785375999999999s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.017704187s
    print(f"Part 2: {time_function(part2)}s")


lines = get_lines("Inputs/Day04.txt")
calls = list(map(int, lines.pop(0).split(",")))
lines.pop(0)

if __name__ == "__main__":
    main()
