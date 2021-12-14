from collections import deque
import numpy as np

def solve1(sample):
    corrupted_chars = []
    for line in sample:
        open_chars = deque('') # Implement as a stack
        for char in line:
            if char in ('{','(','[','<'):
                open_chars.append(char)
            elif char == '}':
                if open_chars.pop() != '{':
                    corrupted_chars += ['}']
                    break
            elif char == ')':
                if open_chars.pop() != '(':
                    corrupted_chars += [')']
                    break
            elif char == ']':
                if open_chars.pop() != '[':
                    corrupted_chars += [']']
                    break
            elif char == '>':
                if open_chars.pop() != '<':
                    corrupted_chars += ['>']
                    break
    syntax_score = {')' : 3, ']':57, '}':1197, '>':25137}
    return sum(list(map(lambda x: syntax_score[x], corrupted_chars)))

def solve2(sample):
    autocomplete_scores = np.array([])
    for line in sample:
        open_chars = deque('') # Implement as a stack
        corrupted = False
        for char in line:
            if char in ('{','(','[','<'):
                open_chars.append(char)
            elif char == '}':
                if open_chars.pop() != '{':
                    corrupted = True
                    break
            elif char == ')':
                if open_chars.pop() != '(':
                    corrupted = True
                    break
            elif char == ']':
                if open_chars.pop() != '[':
                    corrupted = True
                    break
            elif char == '>':
                if open_chars.pop() != '<':
                    corrupted = True
                    break
        if corrupted:
            continue
        # Build closing chars
        closing_chars = deque('')
        closing_score = 0
        while len(open_chars) > 0:
            top = open_chars.pop()
            if top == '(':
                closing_chars.append(')')
                closing_score = closing_score*5 + 1
            elif top == '[':
                closing_chars.append(']')
                closing_score = closing_score*5 + 2
            elif top == '{':
                closing_chars.append('}')
                closing_score = closing_score*5 + 3
            elif top == '<':
                closing_chars.append('>')
                closing_score = closing_score*5 + 4
        autocomplete_scores = np.append(autocomplete_scores, closing_score)
    return int(np.median(autocomplete_scores))
        


if __name__ == '__main__':
    with open('inputs/10_input.txt') as file:
        sample = file.read().split('\n')
    
    print(solve2(sample))