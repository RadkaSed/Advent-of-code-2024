from itertools import combinations
from math import gcd

def parse_map(input_map):
    antennas = {}
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char != '.': 
                if char not in antennas:
                    antennas[char] = []  
                antennas[char].append((x, y))
    return antennas

with open('input_8.txt', 'r', encoding='utf-8') as input_file:
    input_map = [line.strip() for line in input_file]

num_rows = len(input_map)
num_cols = len(input_map[0])

antennas = parse_map(input_map)
antinodes = set() 

for positions in antennas.values():
    antinodes.update(positions)

for frequency, positions in antennas.items():
    if len(positions) < 2:
        continue

    for antenna1, antenna2 in combinations(positions, 2):
        x1, y1 = antenna1
        x2, y2 = antenna2

        delta_x = x2 - x1
        delta_y = y2 - y1

        divisor = gcd(delta_x, delta_y)
        delta_x //= divisor
        delta_y //= divisor

        current_x, current_y = x1 + delta_x, y1 + delta_y
        while (current_x, current_y) != (x2, y2):
            antinodes.add((current_x, current_y))
            current_x += delta_x
            current_y += delta_y

        current_x, current_y = x2 + delta_x, y2 + delta_y
        while 0 <= current_x < num_cols and 0 <= current_y < num_rows:
            antinodes.add((current_x, current_y))
            current_x += delta_x
            current_y += delta_y

        current_x, current_y = x1 - delta_x, y1 - delta_y
        while 0 <= current_x < num_cols and 0 <= current_y < num_rows:
            antinodes.add((current_x, current_y))
            current_x -= delta_x
            current_y -= delta_y

print(len(antinodes))