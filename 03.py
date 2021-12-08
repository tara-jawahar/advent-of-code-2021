import functools, operator

def solve1(sample):
    nums = map(lambda x: int(x), sample)
    max_len = len(str(max(nums)))
    digits = [sum([int(num[dig]) for num in sample]) for dig in range(max_len)]
    most_common_digit = ['1' if x > len(sample)/2 else '0' for x in digits]
    gamma_rate = int(''.join(most_common_digit), 2)
    least_common_digit = ['0' if x > len(sample)/2 else '1' for x in digits]
    epsilon_rate = int(''.join(least_common_digit), 2)
    return gamma_rate*epsilon_rate

def calculate_most_common_digit(sample, i):
    digit = sum([int(num[i]) for (idx,num) in sample])
    # print(digit, len(sample), float(len(sample))/2)
    return '1' if digit >= float(len(sample))/2 else '0'

def o2_rating(i, keep_vals):
    if len(keep_vals) == 1:
        return keep_vals[0]
    cur_pos = calculate_most_common_digit(keep_vals, i)
    keep_vals = filter(lambda x : x[1][i] == cur_pos, keep_vals)
    return o2_rating(i+1, keep_vals)

def co2_rating(i, keep_vals):
    if len(keep_vals) == 1:
        return keep_vals[0]
    cur_pos = calculate_most_common_digit(keep_vals, i)
    cur_pos = str(int(cur_pos,2) ^ 1) # flip to get least common digit 
                                      # and then turn back into str
    keep_vals = filter(lambda x : x[1][i] == cur_pos, keep_vals)
    return co2_rating(i+1, keep_vals)

def solve2(sample):
    nums = map(lambda x: int(x), sample)
    max_len = len(str(max(nums)))
    all_nums = [(i,j) for i,j in enumerate(sample)]
    o2 = int(o2_rating(0, all_nums)[1], 2)
    co2 = int(co2_rating(0, all_nums)[1], 2)
    return o2*co2

if __name__ == '__main__':
    with open('inputs/03_input.txt') as file:
        sample = file.read().split('\n')
    
    # print(solve1(sample))
    print(solve2(sample))
    