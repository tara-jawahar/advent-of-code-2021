import numpy as np

def solve1(sample):
    min, max = np.min(sample), np.max(sample)
    min_fuel_cost = 9999999999
    for i in range(min, max):
        fuel_cost = sum([abs(pos - i) for pos in sample])
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
    return min_fuel_cost

def solve2(sample):
    min, max = np.min(sample), np.max(sample)
    min_fuel_cost = 9999999999
    for i in range(min, max):
        fuel_cost = sum([sum(range(0, abs(i-pos)+1)) for pos in sample])
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
    return min_fuel_cost

if __name__ == '__main__':
    with open('inputs/07_input.txt') as file:
        sample = file.read().split(',')
    sample = np.array(list(map(lambda x: int(x), sample)))
    # print(sample)

    print(solve2(sample))