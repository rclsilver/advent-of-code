#!/usr/bin/env python

from pathlib import Path

def compute(map, x_offset, y_offset):
    trees = 0
    x_pos = 0

    for y_pos, line in enumerate(map):
        if y_pos % y_offset != 0:
            continue

        if x_pos >= len(line):
            line += line * round(x_pos / len(line))

        if line[x_pos] == '#':
            trees += 1

        x_pos += x_offset

    return trees

def part_1(map):
    return compute(map, 3, 1)

def part_2(map):
    return compute(map, 1, 1) * compute(map, 3, 1) * compute(map, 5, 1) * compute(map, 7, 1) * compute(map, 1, 2)

def main():
    input_file = Path('./input.txt')
    input_map = [
        line.strip() for line in input_file.open('r').readlines()
    ]

    result = part_1(input_map)
    print(f'Part #1 - Number of trees: {result}')

    result = part_2(input_map)
    print(f'Part #2 - Number of trees: {result}')

if __name__ == '__main__':
    main()
