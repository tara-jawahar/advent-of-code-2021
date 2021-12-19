from collections import defaultdict
import copy

def construct_graph(sample):
    smol, G = set(), defaultdict(list)
    for line in sample:
        x,y = tuple(line.split('-'))
        if x in ('start','end'):
            x = x.upper()
        elif x.islower():
            smol.add(x)
        if y in ('start','end'):
            y = y.upper()
        elif y.islower():
            smol.add(y)
        if x!= 'END' and y != 'START':
            G[x].append(y)
        if x != 'START' and y != 'END':
            G[y].append(x)
    return smol,G

def solve1(sample):
    smol, G = construct_graph(sample)
    all_paths = [['START']]
    complete = 0
    while len(all_paths) != 0:
        path = all_paths.pop(0)
        if path[-1] == 'END':
            complete += 1
            continue
        next_v = G[path[-1]]
        for v in next_v:
            if v in smol and v in path:
                continue
            new_path = copy.deepcopy(path)
            new_path += [v]
            all_paths += [new_path]
    return complete

def solve2(sample):
    smol, G = construct_graph(sample)
    all_paths = [(['START'], {v:0 for v in smol})]
    complete = 0
    while len(all_paths) != 0:
        path,vis = all_paths.pop(0)
        if path[-1] == 'END':
            # print(path)
            complete += 1
            continue
        next_v = G[path[-1]]
        for v in next_v:
            if v in smol:
                if (2 in set(vis.values()) and vis[v] == 1) or vis[v] == 2:
                    continue
            vis2 = copy.deepcopy(vis)
            if v in vis2:
                vis2[v] += 1
            new_path = copy.deepcopy(path)
            new_path += [v]
            all_paths += [(new_path, vis2)]
    return complete

if __name__ == '__main__':
    with open('inputs/12_input.txt') as file:
        sample = file.read().split('\n')

    # print(construct_graph(sample)[1])
    print(solve2(sample))