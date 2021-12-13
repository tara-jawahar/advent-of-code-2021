import numpy as np

def simulate(day, total_days, fish):
    if day == total_days:
        return fish
    add_fish = fish[fish==0].size
    fish = np.where(fish == 0, 7, fish) - 1
    fish = np.append(fish, [8]*add_fish)
    return simulate(day+1, total_days, fish)

def solve1(total_days, sample):
    return simulate(0, total_days, sample).size

def solve2(total_days, sample):
    day_counts = {k:0 for k in range(10)}
    for i in sample:
        day_counts[i] += 1
    for day in range(total_days):
        if day_counts[0] != 0:
            day_counts[7] += day_counts[0]
            day_counts[9] += day_counts[0]
            day_counts[0] = 1
        new_day_counts = {k:0 for k in range(10)}
        for k,v in day_counts.items():
            if k != 0:
                new_day_counts[k-1] += day_counts[k]
        day_counts = new_day_counts
    return sum([v for v in day_counts.values()])

if __name__ == '__main__':
    with open('inputs/06_input.txt') as file:
        sample = file.read().split(',')
    sample = np.array(list(map(lambda x: int(x), sample)))
    
    # print(solve1(256, sample))
    print(solve2(256, sample))
