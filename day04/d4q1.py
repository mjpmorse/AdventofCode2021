import numpy as np
from icecream import ic

calls = []
boards = []
boards.append([])

with open('data/data_q4.txt', 'r') as f:
    # pull out the first line
    calls.append(f.readline())
    calls = calls[0].split(',')
    # second line is a blank
    f.readline()
    board_number = 0
    for line in f:
        line = line.split()
        if len(line) == 0:
            board_number += 1
            boards.append([])
            continue
        boards[board_number].append(line)

# convert to numpy array and trim any white space
boards = np.array(boards)
boards = np.char.strip(boards)
called_boards = np.zeros_like(boards)
called_boards[called_boards == ''] = '0'
called_boards = called_boards.astype(int)
calls = np.array(calls)
calls = np.char.strip(calls)
winning_board = []
winning_called_board = []
last_called = -1

for call in calls:
    last_called = int(call)
    # record the calls on a seprate board
    called_boards[boards == call] = int(call)
    # blank out the first board
    boards[boards == call] = ''
    for board_number in range(boards.shape[0]):
        board = boards[board_number]
        # check to see if we have any column victories
        cols = np.all(board == '', axis=0)
        cols = np.argwhere(cols == 1)

        # check to see if we have any row victories
        rows = np.all(board == '', axis=1)
        rows = np.argwhere(rows == 1)

        if cols.size != 0 or rows.size != 0:
            winning_board = board
            winning_called_board = called_boards[board_number]
            break

    if len(winning_board) > 0:
        break

ic(winning_called_board)
ic(winning_board)

winning_board[winning_board == ''] = '0'
winning_board = winning_board.astype(int)

winning_uncalled_sum = np.sum(winning_board)
winning_called_sum = np.sum(winning_called_board)


statement = ('On the winning board, the sum of'
             f' the called numbers is: {last_called}. \n'
             f'The sum of the uncalled numbers is {winning_uncalled_sum}. \n'
             f'The last number called was: {last_called}. \n'
             f'The product is: {last_called * winning_uncalled_sum}')

print(statement)
