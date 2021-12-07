def solve1(sample):
    data = sample
    data_next = data[1:]

    count = 0
    count = sum([1 if int(elem2) > int(elem1) else 0 for elem1,elem2 in zip(data, data_next)])
    if int(data_next[-1]) > int(data[-1]):
        count += 1
    
    return count

def solve2(sample):
    view1 = sample[0:-2]
    view2 = sample[1:-1]
    view3 = sample[2:]

    sums = [int(i)+int(j)+int(k) for i,j,k in zip(view1,view2,view3)]
    return solve1(sums)

if __name__ == '__main__':
    with open('inputs/01_input.txt') as file:
        sample = file.read()
    sample = sample.split('\n')
    print(solve1(sample))
    print(solve2(sample))
