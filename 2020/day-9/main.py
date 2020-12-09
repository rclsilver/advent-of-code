#!/usr/bin/env python

from pathlib import Path

def part_1(data):
    def is_valid(number, slice):
        for a in slice:
            for b in slice:
                if a + b == number:
                    return True
        return False

    for i in range(25, len(data)):
        if not is_valid(data[i], data[i-25:i+25]):
            return data[i]

def part_2(data):
    number = part_1(data)
    i_start = 0
    i_end = 0
    total = 0

    for i in range(len(data)):
        total += data[i]
        i_end = i

        while total > number:
            total -= data[i_start]
            i_start += 1

        if total == number and (i_end - i_start) >= 2:
            min_number = min(data[i_start:i_end])
            max_number = max(data[i_start:i_end])
            return min_number + max_number

def main():
    input_file = Path('./input.txt')
    input_data = [int(line.strip()) for line in input_file.open('r').readlines()]

    result = part_1(input_data)
    print(f'Part #1 - Result: {result}')

    result = part_2(input_data)
    print(f'Part #2 - Result: {result}')

if __name__ == '__main__':
    main()
