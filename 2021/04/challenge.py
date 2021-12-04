import aoc
import copy

input_data = aoc.get_input(delim='\n\n')
draw_numbers = input_data[0].split(',')


class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.marked_nums = []

    def mark(self, number):
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                if self.board[y][x] == number:
                    self.marked_nums.append((x, y))

    def has_bingo(self):
        # x first
        for x in range(5):
            x_nums = [num for num in self.marked_nums if num[0] == x]
            if len(x_nums) == 5:
                return True

        # then y
        for y in range(5):
            y_nums = [num for num in self.marked_nums if num[1] == y]
            if len(y_nums) == 5:
                return True

        return False

    def calc_score(self, last_num):
        num_sum = 0
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                if (x, y) not in self.marked_nums:
                    num_sum += self.board[y][x]

        return num_sum * last_num


def _parse_data():
    boards = []
    for board_nums in input_data[1:]:
        nums = []
        for board_line in board_nums.split('\n'):
            nums.append([int(n.strip()) for n in board_line.split(' ') if n])
        boards.append(BingoBoard(nums))

    return boards


def challenge1():
    boards = _parse_data()
    for num in draw_numbers:
        for board in boards:
            board.mark(int(num))
            if board.has_bingo():
                return board.calc_score(int(num))


def challenge2():
    last_score = 0

    boards = _parse_data()
    for num in draw_numbers:
        for board in boards:
            board.mark(int(num))
        for board in boards:
            if board.has_bingo():
                boards.remove(board)
                last_score = board.calc_score(int(num))

    return last_score


aoc.run(challenge1)
aoc.run(challenge2)
