def get_adj(i,j,board):
    adj_points = []
    if j > 0:
        adj_points += [(i,j-1)]
    if i > 0:
        adj_points += [(i-1,j)]
    if j < len(board[0]) - 1:
        adj_points += [(i,j+1)]
    if i < len(board) - 1:
        adj_points += [(i+1,j)]
    return adj_points

def solve1(sample):
    sample = [list(map(lambda x: int(x), list(x))) for x in sample]
    
    total_risk, low_points = 0, []
    for i in range(len(sample)):
        for j in range(len(sample[0])):
            adj_points = get_adj(i,j,sample)
            if len(adj_points) == len(list(filter(lambda x: sample[i][j] < sample[x[0]][x[1]], adj_points))):
                total_risk += sample[i][j] + 1
                low_points += [(i,j)]
    return total_risk, low_points

def find_all_low_pts(pts, basin, sample):
    if len(pts) == 0:
        return len(basin)
    
    cur_pt = pts[0]
    adj_pts = get_adj(cur_pt[0], cur_pt[1], sample)
    adj_pts = list(filter(lambda x: sample[x[0]][x[1]] != 9, adj_pts))
    basin_pts = filter(lambda x: sample[cur_pt[0]][cur_pt[1]] < sample[x[0]][x[1]], adj_pts)
    basin_list = list(basin_pts)
    basin_set = set(basin_list)
    pts += basin_list
    basin = set.union(basin, basin_set)
    return find_all_low_pts(pts[1:], basin, sample)

def solve2(sample):
    _, low_points = solve1(sample)
    sample = [list(map(lambda x: int(x), list(x))) for x in sample]
    basins = []
    for i,j in low_points:
        basin_size = find_all_low_pts([(i,j)], {(i,j)}, sample)
        basins += [basin_size]
    basins.sort(reverse=True)
    return basins[0]*basins[1]*basins[2]

if __name__ == '__main__':
    with open('inputs/09_input.txt') as file:
        sample = file.read().split('\n')

    print(solve2(sample))