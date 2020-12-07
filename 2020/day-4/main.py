#!/usr/bin/env python

import re
from pathlib import Path

def parse(lines):
    entry = []
    result = []

    for line in lines:
        if line.strip() == '':
            result.append(' '.join(entry))
            entry = []
        else:
            entry.append(line.strip())

    if entry:
        result.append(' '.join(entry))

    regex = re.compile(r'(?P<field>[^: ]+):(?P<value>[^ ]+)')

    return [
        dict(regex.findall(row)) for row in result
    ]

def is_valid(passeport, required_fields=['byr','iyr','eyr','hgt','hcl','ecl','pid'], optional_fields=['cid']):
    allowed_fields = required_fields + optional_fields

    # Check if required fields are present
    for field in required_fields:
        if field not in passeport:
            return False

    # Check if field are in allowed fields
    for field, _ in passeport.items():
        if field not in allowed_fields:
            return False

    # Passeport is valid
    return True

def part_1(passeports):
    result = 0

    for passeport in passeports:
        if is_valid(passeport):
            result += 1

    return result

def part_2(passeports):
    valid_passeports = [passeport for passeport in passeports if is_valid(passeport)]
    result = 0

    for passeport in valid_passeports:
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not re.match(r'^[0-9]{4}$', passeport['byr']) or int(passeport['byr']) < 1920 or int(passeport['byr']) > 2002:
            continue

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not re.match(r'^[0-9]{4}$', passeport['iyr']) or int(passeport['iyr']) < 2010 or int(passeport['iyr']) > 2020:
            continue

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not re.match(r'^[0-9]{4}$', passeport['eyr']) or int(passeport['eyr']) < 2020 or int(passeport['eyr']) > 2030:
            continue

        # hgt (Height) - a number followed by either cm or in:
        m_hgt = re.match(r'^(?P<height>[0-9]+)(?P<unit>in|cm)$', passeport['hgt'].lower())

        if not m_hgt:
            continue

        # If in, the number must be at least 59 and at most 76.
        if m_hgt.group('unit') == 'in':
            if int(m_hgt.group('height')) < 59 or int(m_hgt.group('height')) > 76:
                continue

        # If cm, the number must be at least 150 and at most 193.
        if m_hgt.group('unit') == 'cm':
            if int(m_hgt.group('height')) < 150 or int(m_hgt.group('height')) > 193:
                continue

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not re.match(r'^#[0-9a-f]{6}$', passeport['hcl'].lower()):
            continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if not re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passeport['ecl']):
            continue

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not re.match(r'^[0-9]{9}$', passeport['pid']):
            continue

        result += 1
        
    return result

def main():
    input_file = Path('./input.txt')
    input_passeports = parse(input_file.open('r').readlines())

    result = part_1(input_passeports)
    print(f'Part #1 - Valid passeports: {result}')

    result = part_2(input_passeports)
    print(f'Part #2 - Valid passeports: {result}')

if __name__ == '__main__':
    main()
