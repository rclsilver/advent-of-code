#!/usr/bin/env python

from pathlib import Path

def part_1(numbers):
    for a in numbers:
        for b in numbers:
            if a + b == 2020:
                return a, b, a * b

def part_2(numbers):
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == 2020:
                    return a, b, c, a * b * c

def main():
    input_file = Path('./input.txt')
    input_numbers = [
        int(line.strip()) for line in input_file.open('r').readlines()
    ]
    
    a, b, c = part_1(input_numbers)
    print(f'Part #1 - Numbers are {a} and {b} and answer is {c}')

    a, b, c, d = part_2(input_numbers)
    print(f'Part #2 - Numbers are {a}, {b} and {c} and answer is {d}')

if __name__ == '__main__':
    main()
