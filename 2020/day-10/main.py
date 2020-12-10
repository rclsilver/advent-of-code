#!/usr/bin/env python

from pathlib import Path

def compute(adapters, i=0, solutions={}):
    if i == len(adapters) - 1:
        return 1

    if i in solutions:
        return solutions[i]

    result = 0

    for j in range(i + 1, len(adapters)):
        if adapters[j] - adapters[i] <= 3:
            result += compute(adapters, j, solutions)

    solutions[i] = result

    return result

def part_1(adapters):
    adapters = [0] + adapters
    adapters.append(max(adapters) + 3)
    diff_1 = 0
    diff_3 = 0

    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]

        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1

    return diff_1 * diff_3

def part_2(adapters):
    adapters = [0] + adapters
    adapters.append(max(adapters) + 3)
    return compute(adapters)

def main():
    input_file = Path('./input.txt')
    input_adapters = sorted([int(line.strip()) for line in input_file.open('r').readlines()])

    result = part_1(input_adapters)
    print(f'Part #1 - Result: {result}')

    result = part_2(input_adapters)
    print(f'Part #2 - Result: {result}')

if __name__ == '__main__':
    main()
