def parse_input(sample):
    all_vents = []
    max_x, max_y = 0,0
    for v in sample:
        vents = v.split(' -> ')
        # print(vents)
        start,end = tuple(vents[0].split(',')), tuple(vents[1].split(','))
        startx, starty, endx, endy = int(start[0]), int(start[1]), int(end[0]), int(end[1])
        if max(startx, endx) > max_x:
            max_x = max(startx, endx)
        if max(starty, endy) > max_y:
            max_y = max(starty, endy)
        all_vents += [(startx, starty, endx, endy)]
    return all_vents, max_x+1, max_y+1

def solve1(sample):
    vents, max_x, max_y = parse_input(sample)
    board = [[0 for i in range(max_x)] for j in range(max_y)]
    # print(board)
    for startx, starty, endx, endy in vents:
        if startx == endx:
            # Vertical pipe
            if starty > endy:
                starty, endy = endy, starty
            for spot in range(starty, endy+1):
                board[startx][spot] += 1
                # print(startx, spot)
        elif starty == endy:
            # Horizontal pipe
            if startx > endx:
                startx, endx = endx, startx
            for spot in range(startx, endx+1):
                # print(spot, starty)
                board[spot][starty] += 1
                # print(spot, starty)
        # print(board)
    
    overlap = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] > 1:
                overlap += 1
    return overlap

def solve2(sample):
    vents, max_x, max_y = parse_input(sample)
    board = [[0 for i in range(max_x)] for j in range(max_y)]
    for startx, starty, endx, endy in vents:
        if startx == endx:
            # Vertical pipe
            if starty > endy:
                starty, endy = endy, starty
            for spot in range(starty, endy+1):
                board[startx][spot] += 1
        elif starty == endy:
            # Horizontal pipe
            if startx > endx:
                startx, endx = endx, startx
            for spot in range(startx, endx+1):
                board[spot][starty] += 1
        else:
            # Diagonal pipe
            xdir, ydir = 1, 1
            if startx > endx:
                xdir = -1
            if starty > endy:
                ydir = -1
            steps = abs(startx-endx)
            for i in range(steps+1):
                board[startx + i*xdir][starty + i*ydir] += 1
    # print(board)
    overlap = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] > 1:
                overlap += 1
    return overlap


if __name__ == '__main__':
    with open('inputs/05_input.txt') as file:
        sample = file.read().split('\n')
    
    print(solve2(sample))