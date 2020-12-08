#!/usr/bin/env python

import copy
import re
from pathlib import Path

def parse_code(lines):
    regex = re.compile(r'(?P<instruction>acc|jmp|nop) (?P<value>[-+][0-9]+)')
    return [(op.group('instruction'), int(op.group('value'))) for op in (regex.match(line) for line in lines)]

def part_1(code):
    acc = 0
    ope = 0
    history = []

    while ope not in history:
        history.append(ope)

        if code[ope][0] == 'acc':
            acc += code[ope][1]
            ope += 1
        elif code[ope][0] == 'jmp':
            ope += code[ope][1]
        elif code[ope][0] == 'nop':
            ope += 1

    return acc

def part_2(code):
    end_ope = len(code) - 1

    for i in range(len(code)):
        if code[i][0] == 'acc':
            continue

        new_code = copy.deepcopy(code)
        new_code[i] = ('jmp' if code[i][0] == 'nop' else 'nop', code[i][1])
        acc = 0
        ope = 0
        history = []

        while 0 <= ope < end_ope and ope not in history:
            history.append(ope)

            if new_code[ope][0] == 'acc':
                acc += new_code[ope][1]
                ope += 1
            elif new_code[ope][0] == 'jmp':
                ope += new_code[ope][1]
            elif new_code[ope][0] == 'nop':
                ope += 1

        if ope == end_ope:
            return acc

def main():
    input_file = Path('./input.txt')
    input_code = parse_code(input_file.open('r').readlines())

    result = part_1(input_code)
    print(f'Part #1 - Result: {result}')

    result = part_2(input_code)
    print(f'Part #2 - Result: {result}')

if __name__ == '__main__':
    main()
