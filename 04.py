import copy

def get_boards(boards, sample):
    if len(sample) == 1:
        return boards
    if len(sample[1]) == 0:
        return get_boards(boards, sample[1:])
    elif len(sample[0]) == 0:
        row = map(lambda x : int(x), sample[1].strip().replace('  ', ' ').split(' '))
        boards += [[row]]
        return get_boards(boards, sample[1:])
    else:
        row = map(lambda x : int(x), sample[1].strip().replace('  ', ' ').split(' '))
        boards[-1] += [row]
        return get_boards(boards, sample[1:])

def add_rowcol_to_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = (i,j,board[i][j])
    return board

def draw_nums(num, board, marked_board):
    position = None
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col][2] == num:
                position = (board[row][col][0], board[row][col][1])
                break
    if position is not None:
        row,col = position
        marked_board[row][col] = 1
    return marked_board

def check_board(marked_board):
    for row in range(len(marked_board)):
        if sum(marked_board[row]) == len(marked_board):
            return True
    for col in range(len(marked_board[0])):
        current_col = 0
        for row in range(len(marked_board)):
            if marked_board[row][col] == 1:
                current_col += 1
        if current_col == len(marked_board):
            return True
    return False

def calculate_unmarked_sum(board, marked_board):
    sum = 0
    for row in range(len(marked_board)):
        for col in range(len(marked_board[0])):
            if marked_board[row][col] == 0:
                sum += board[row][col][2]
    return sum

def solve1(sample):
    drawn_nums = map(lambda x: int(x), sample[0].split(','))
    all_boards = get_boards([], sample[1:])
    all_boards = map(add_rowcol_to_board, all_boards)
    num_boards, board_len = len(all_boards), len(all_boards[0])
    marked_boards = [[[0 for k in range(board_len)] for j in range(board_len)] for i in range(num_boards)]
    for n in drawn_nums:
        # Mark number on all boards
        for board_num in range(len(all_boards)):
            marked_boards[board_num] = draw_nums(n, all_boards[board_num], marked_boards[board_num])
        # Check for a win
        for board_num in range(len(all_boards)):
            if check_board(marked_boards[board_num]):
                sum = unmarked_sum(all_boards[board_num], marked_boards[board_num])
                return sum*n

def solve2(sample):
    drawn_nums = map(lambda x: int(x), sample[0].split(','))
    all_boards = get_boards([], sample[1:])
    all_boards = map(add_rowcol_to_board, all_boards)
    num_boards, board_len = len(all_boards), len(all_boards[0])
    marked_boards = [[[0 for k in range(board_len)] for j in range(board_len)] for i in range(num_boards)]
    
    winning_boards = [0 for i in range(num_boards)]
    for n in drawn_nums:
        # Mark number on all boards
        for board_num in range(len(all_boards)):
            marked_boards[board_num] = draw_nums(n, all_boards[board_num], marked_boards[board_num])
        # Check for a win
        for board_num in range(len(all_boards)):
            if check_board(marked_boards[board_num]):
                winning_boards[board_num] = 1
                if sum(winning_boards) == num_boards:
                    unmarked_sum = calculate_unmarked_sum(all_boards[board_num], marked_boards[board_num])
                    return unmarked_sum*n

if __name__ == '__main__':
    with open('inputs/04_input.txt') as file:
        sample = file.read().split('\n')

    print(solve2(sample))