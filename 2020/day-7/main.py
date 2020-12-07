#!/usr/bin/env python

import re
from pathlib import Path

def parse_rules(lines):
    regex_line = re.compile(r'^(?P<color>.+) +bags contain (?P<content>.+)$')
    regex_content = re.compile(r'^(?P<count>[0-9]+) (?P<color>.+) bags?$')
    bags = {}

    for line in lines:
        m_line = regex_line.match(line)

        bags[m_line.group('color')] = {}

        for bag in m_line.group('content').strip('.').split(', '):
            m_content = regex_content.match(bag)

            if not m_content:
                continue

            bags[m_line.group('color')][m_content.group('color')] = int(m_content.group('count'))

    return bags

def part_1(input):
    def contains(content, wanted_color):
        for color, count in content.items():
            if color == wanted_color:
                return True

            if count:
                if contains(input[color], wanted_color):
                    return True

        return False

    result = 0

    for color, content in input.items():
        if contains(content, 'shiny gold'):
            result += 1

    return result

def part_2(input):
    def sum(content):
        result = 0

        for color, count in content.items():
            result += count
            result += count * sum(input[color])

        return result

    return sum(input['shiny gold'])

def main():
    input_file = Path('./input.txt')
    input_rules = parse_rules([line.strip() for line in input_file.open('r').readlines()])

    result = part_1(input_rules)
    print(f'Part #1 - Result: {result}')

    result = part_2(input_rules)
    print(f'Part #2 - Result: {result}')

if __name__ == '__main__':
    main()
