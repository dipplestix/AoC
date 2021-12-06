import sys
import numpy as np


def check_win(binary_board):
    diag_1 = 0
    diag_2 = 0
    for i in range(5):
        diag_1 += binary_board[i, i]
        diag_2 += binary_board[i, 4-i]
        if sum(binary_board[i, :]) == 5.:
            return True
        if sum(binary_board[:, i]) == 5.:
            return True
    # if diag_2 == 5. or diag_1 == 5.:
    #     return True
    return False


def best_board(file_name):
    boards = []
    board = []
    with open(file_name, 'r') as f:
        numbers = [int(n) for n in f.readline().split(',')[:-1]]
        f.readline()
        for i, val in enumerate(f):
            if val == '\n':
                boards.append(np.array(board))
                board = []
            else:
                val = [int(i) for i in val.split()]
                board.append(val)
    boards.append(np.array(board))

    best_i = len(numbers)*2
    best_score = 0
    for board in boards:
        binary_board = np.zeros(board.shape)
        for i, num in enumerate(numbers):
            if num in board:
                binary_board[np.where(board==num)] = 1
            if i >= 5:
                if check_win(binary_board):
                    if i < best_i:
                        best_i = i
                        scored_numbers = num
                        unscored_numbers = sum(board[np.where(binary_board==0)])
                        best_score = scored_numbers*unscored_numbers
                    continue
    return best_score


def worst_board(file_name):
    boards = []
    board = []
    with open(file_name, 'r') as f:
        numbers = [int(n) for n in f.readline().split(',')[:-1]]
        f.readline()
        for i, val in enumerate(f):
            if val == '\n':
                boards.append(np.array(board))
                board = []
            else:
                val = [int(i) for i in val.split()]
                board.append(val)
    boards.append(np.array(board))

    worst_i = 0
    worst_score = 0
    for board in boards:
        binary_board = np.zeros(board.shape)
        for i, num in enumerate(numbers):
            if not check_win(binary_board):
                if num in board:
                    binary_board[np.where(board==num)] = 1
                if i >= 5:
                    if check_win(binary_board):
                        if i > worst_i:
                            worst_i = i
                            scored_numbers = num
                            unscored_numbers = sum(board[np.where(binary_board==0)])
                            worst_score = scored_numbers*unscored_numbers
    return worst_score


if __name__ == "__main__":
    best = best_board(sys.argv[1])
    print(best)
    worst = worst_board(sys.argv[1])
    print(worst)
