import functools, sys

def solve1(sample):
    components = [tuple(i.split(' ')) for i in sample]
    horiz_dir = sum([int(dist) if dir == 'forward' else 0 for (dir,dist) in components])
    # Filter to only up/down movements
    depths = filter(lambda x : x[0] in ('up', 'down'), components)
    # Normalize
    depth_dir = [int(dist)*-1 if dir == 'up' else int(dist) for (dir,dist) in depths]
    depth = functools.reduce(lambda a,b : a+b, depth_dir)
    return horiz_dir * depth

def calculate_depth(dirs, aim, depth):
    if len(dirs) == 0:
        return depth
    cur_dir = dirs[0]
    if cur_dir[0] == 'depth':
        return calculate_depth(dirs[1:], aim + cur_dir[1], depth)
    else:
        depth += aim*abs(cur_dir[1])
        return calculate_depth(dirs[1:], aim, depth)

def solve2(sample):
    components = [tuple(i.split(' ')) for i in sample]
    horiz_dir = sum([int(dist) if dir == 'forward' else 0 for (dir,dist) in components])
    # Normalize up direction to be negative
    norm_dir = [('depth', int(dist)*-1) if dir == 'up' else ('depth', int(dist)) if dir == 'down' else (dir, int(dist)) for (dir,dist) in components]
    sys.setrecursionlimit(1100)
    depth = calculate_depth(norm_dir, 0, 0)
    return horiz_dir*depth

if __name__ == '__main__':
    with open('inputs/02_input.txt') as file:
        sample = file.read().split('\n')
    print(solve1(sample))
    print(solve2(sample))
