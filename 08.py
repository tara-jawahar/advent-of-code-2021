def solve1(sample):
    lines = [tuple(line.split(' | ')) for line in sample]
    count = 0
    for _, output in lines:
        # 1: len 2, 4: len 4, 7: len 3, 8: len 7
        digits = [len(num) for num in output.split(' ')]
        count += len(list(filter(lambda x: x in (2,4,3,7), digits)))
    return count

def solve2(sample):
    lines = [tuple(line.split(' | ')) for line in sample]
    final_output = []
    
    # map lengths to possible nums, 1,4,7,8 are unique
    pattern_segnums = {6:[0,6,9], 2:1, 4:4, 5:[2,3,5], 3:7, 7:8} # map length to actual num
    pattern_segs = {0:'abcefg', 1:'cf', 2:'acdeg', 3:'acdfg', 4:'bcdf',
                    5:'abdfg', 6:'abdefg', 7:'acf', 8:'abcdefg', 9:'abcdfg'}
    code_to_num = {v:k for k,v in pattern_segs.items()}
    
    for pattern, output in lines:
        map_dict = {} # map what is in code to what it should actually be
        possible_map = {} # maps num to possib
        # update with knowns first
        for code in pattern.split(' '):
            if len(code) in (2,4,3,7):
                num = pattern_segnums[len(code)]
                segs = set(pattern_segs[num])
                possible_map[num] = set(code)
                
        map_dict['a'] = set.difference(possible_map[7], possible_map[1])
        map_dict['cf'] = possible_map[1]
        map_dict['bd'] = set.difference(possible_map[4], possible_map[1])
        map_dict['eg'] = set.difference(possible_map[8], possible_map[4], possible_map[1], possible_map[7])
        for code in pattern.split(' '):
            if len(code) == 6: # possible: 0,6,9
                if map_dict.get('cf') != None and len(set.intersection(map_dict['cf'], set(code))) != 2:
                    map_dict['f'] = set.intersection(map_dict['cf'], set(code))
                    map_dict['c'] = set.difference(map_dict['cf'], map_dict['f'])
                    map_dict.pop('cf')
                if map_dict.get('bd') != None and len(set.intersection(map_dict['bd'], set(code))) != 2:
                    map_dict['b'] = set.intersection(map_dict['bd'], set(code))
                    map_dict['d'] = set.difference(map_dict['bd'], map_dict['b'])
                    map_dict.pop('bd')
                if map_dict.get('eg') != None and len(set.intersection(map_dict['eg'], set(code))) != 2:
                    map_dict['g'] = set.intersection(map_dict['eg'], set(code))
                    map_dict['e'] = set.difference(map_dict['eg'], map_dict['g'])
                    map_dict.pop('eg')
            if len(code) == 5: # possible: 2,3,5
                if map_dict.get('bd') != None and len(set.intersection(map_dict['bd'], set(code))) != 2:
                    map_dict['d'] = set.intersection(map_dict['bd'], set(code))
                    map_dict['b'] = set.difference(map_dict['bd'], map_dict['d'])
                    map_dict.pop('bd')
                if map_dict.get('eg') != None and len(set.intersection(map_dict['eg'], set(code))) != 2:
                    map_dict['g'] = set.intersection(map_dict['eg'], set(code))
                    map_dict['e'] = set.difference(map_dict['eg'], map_dict['g'])
                    map_dict.pop('eg')
        map_dict = {''.join(v):k for k,v in map_dict.items()}
        temp_output = []
        for num_code in output.split(' '):
            mapped_code = ''.join(sorted([map_dict[char] for char in list(num_code)]))
            temp_output += [str(code_to_num[mapped_code])]
        final_output += [''.join(temp_output)]
    return sum(map(lambda x: int(x), final_output))

if __name__ == '__main__':
    with open('inputs/08_input.txt') as file:
        sample = file.read().split('\n')
    
    # sample = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
    print(solve2(sample))