def get_adj(i,j,board):
    all_pts = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
    valid_pts = filter(lambda x: x[0]>=0 and x[0]<len(board) and x[1]>=0 and x[1]<len(board), all_pts)
    return valid_pts

def get_flashes(board):
    flashes = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] > 9:
                flashes.add((i,j))
    return flashes

def update(board, flashes, flash_hist):
    if len(flashes) == 0:
        flash_hist = flash_hist.union(flashes)
        return board, len(flash_hist)
    flash_hist = flash_hist.union(flashes)
    curr_f = flashes.pop()
    adj_pts = get_adj(curr_f[0], curr_f[1], board)
    for (i,j) in adj_pts:
        if (i,j) not in flash_hist:
            board[i][j] += 1
    board[curr_f[0]][curr_f[1]] = 0
    flashes = flashes.union(get_flashes(board))
    return update(board, flashes, flash_hist)

def solve1(board, steps):
    total_flashes = 0
    for i in range(steps):
        board = [[board[i][j] + 1 for j in range(len(board))] for i in range(len(board))]
        flashes = get_flashes(board)
        new_board, flash_ct = update(board, flashes, flashes)
        if flash_ct == 100:
            return i+1
        total_flashes += flash_ct

if __name__ == '__main__':
    with open('inputs/11_input.txt') as file:
        sample = file.read().split('\n')
    sample = [list(map(lambda x: int(x), list(x))) for x in sample]
    print(solve1(sample, 1000))