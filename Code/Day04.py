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
        x = 0
        x_has_False = False

        for i in range(5):
            if self.calledBoard[0][i] and \
                    self.calledBoard[1][i] and \
                    self.calledBoard[2][i] and\
                    self.calledBoard[3][i] and\
                    self.calledBoard[4][i]:
                return True

    def called(self, called: int) -> int:
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == called:
                    self.calledBoard[i][j] = True
        if self.check_win():
            self.won = True
            return self.calculate_score(called)
        else:
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


def part1() -> int:
    board = [[0]*5 for i in range(5)]
    boards = []
    board_row = 0
    for line in lines:
        if line == '':
            boards.append(Board(board))
            board_row = 0
            board = [[0]*5 for i in range(5)]
        else:
            line = line.split(" ")
            no_space_int_line = list(
                map(int, list(filter(lambda x: x != "", line))))
            board[board_row] = no_space_int_line
            board_row += 1

    result = -1
    for call in calls:
        for board in boards:
            result = board.called(call)
            if result != -1:
                return result
    print("No result")


def part2() -> int:
    board = [[0]*5 for i in range(5)]
    boards = []
    board_row = 0
    for line in lines:
        if line == '':
            boards.append(Board(board))
            board_row = 0
            board = [[0]*5 for i in range(5)]
        else:
            line = line.split(" ")
            no_space_int_line = list(
                map(int, list(filter(lambda x: x != "", line))))
            board[board_row] = no_space_int_line
            board_row += 1

    result = -1
    for call in calls:
        for board in boards:
            if not board.has_won():

                result = board.called(call)
                losing_boards = list(filter(lambda x: not x.has_won(), boards))
                if len(losing_boards) == 0:
                    return result
    print("No result")


def main():
    # Part 1: 35711
    print(f"Part 1: {part1()}")
    # Part 2: 5586
    print(f"Part 2: {part2()}")

    # Part 1: 0.008072555s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.08988011800000001s
    print(f"Part 2: {time_function(part2)}s")


lines = get_lines("Inputs/Day04.txt")
calls = list(map(int, lines.pop(0).split(",")))
lines.pop(0)

if __name__ == "__main__":
    main()
