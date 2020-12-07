#!/usr/bin/env python

from pathlib import Path

def parse_groups(lines):
    groups = []
    current_group = []

    for line in lines:
        if line == '':
            if current_group:
                groups.append(current_group)
                current_group = []
        else:
            current_group.append(line)

    if current_group:
        groups.append(current_group)

    return groups

def part_1(groups):
    result = 0

    for group in groups:
        answers = []

        for person in group:
            for answer in person:
                if answer not in answers:
                    answers.append(answer)
        
        result += len(answers)

    return result

def part_2(groups):
    result = 0

    for group in groups:
        answers = {}

        for person in group:
            for answer in person:
                if answer not in answers:
                    answers[answer] = 1
                else:
                    answers[answer] += 1
        
        for answer, count in answers.items():
            if count == len(group):
                result += 1

    return result

def main():
    input_file = Path('./input.txt')
    input_groups = parse_groups([line.strip() for line in input_file.open('r').readlines()])

    result = part_1(input_groups)
    print(f'Part #1 - Result: {result}')

    result = part_2(input_groups)
    print(f'Part #2 - Result: {result}')

if __name__ == '__main__':
    main()
