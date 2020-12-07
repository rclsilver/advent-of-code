#!/usr/bin/env python

from pathlib import Path

def parse_boarding_pass(boarding_pass):
    remaining_ranges = [i for i in range(0, 128)]
    remaining_columns = [i for i in range(0, 8)]

    for c in boarding_pass[:7]:
        middle = int(len(remaining_ranges) / 2)

        if c == 'F':
            remaining_ranges = remaining_ranges[:middle]
        else:
            remaining_ranges = remaining_ranges[-middle:]

    for c in boarding_pass[-3:]:
        middle = int(len(remaining_columns) / 2)

        if c == 'L':
            remaining_columns = remaining_columns[:middle]
        else:
            remaining_columns = remaining_columns[-middle:]

    return remaining_ranges[0] * 8 + remaining_columns[0]

def part_1(boarding_passes):
    result = 0

    for boarding_pass in boarding_passes:
        place = parse_boarding_pass(boarding_pass)

        if result < place:
            result = place

    return result

def part_2(boarding_passes):
    places = dict((i, False) for i in range(0, part_1(boarding_passes) + 1))
    
    for boarding_pass in boarding_passes:
        place = parse_boarding_pass(boarding_pass)
        places[place] = True

    for place in [place for place, occupied in places.items() if not occupied]:
        if (place + 1) in places and (place - 1) in places and places[place - 1] and places[place + 1]:
            return place

def main():
    input_file = Path('./input.txt')
    input_passes = [line.strip() for line in input_file.open('r').readlines()]

    result = part_1(input_passes)
    print(f'Part #1 - Highest boarding pass: {result}')

    result = part_2(input_passes)
    print(f'Part #2 - My place: {result}')

if __name__ == '__main__':
    main()
