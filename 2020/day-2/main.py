#!/usr/bin/env python

import re
from pathlib import Path

def part_1(passwords):
    result = 0

    for password in passwords:
        letter = tuple(c for c in password['password'] if c == password['letter'])
        letter_count = len(letter)
        if letter_count >= password['min'] and letter_count <= password['max']:
            result += 1

    return result

def part_2(passwords):
    result = 0

    for password in passwords:
        first_pos = password['password'][password['min'] - 1] if len(password['password']) >= password['min'] else None
        second_pos = password['password'][password['max'] - 1] if len(password['password']) >= password['max'] else None

        if (
            (first_pos == password['letter'] and second_pos != password['letter'])
        ) or (
            (first_pos != password['letter'] and second_pos == password['letter'])
        ):
            result += 1

    return result

def main():
    input_file = Path('./input.txt')
    regex = re.compile(r'^(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-zA-Z]): (?P<password>.+)$')
    input_passwords = [
        {
            'min': int(password.group('min')),
            'max': int(password.group('max')),
            'letter': password.group('letter'),
            'password': password.group('password'),
        }
        for password in (
            regex.match(line) for line in input_file.open('r').readlines()
        )
    ]

    valid_passwords = part_1(input_passwords)
    print(f'Part #1 - Valid passwords: {valid_passwords}')

    valid_passwords = part_2(input_passwords)
    print(f'Part #2 - Valid passwords: {valid_passwords}')

if __name__ == '__main__':
    main()
