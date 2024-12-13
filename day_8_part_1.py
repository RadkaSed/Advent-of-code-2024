from itertools import combinations

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

for frequency, positions in antennas.items():
    if len(positions) < 2:
        continue

    for antenna1, antenna2 in combinations(positions, 2):
        x1, y1 = antenna1
        x2, y2 = antenna2


        delta_x = x2 - x1
        delta_y = y2 - y1


        antinode1 = (x1 - delta_x, y1 - delta_y) 
        antinode2 = (x2 + delta_x, y2 + delta_y)

    
        if 0 <= antinode1[0] < num_cols and 0 <= antinode1[1] < num_rows:
            antinodes.add(antinode1)
        if 0 <= antinode2[0] < num_cols and 0 <= antinode2[1] < num_rows:
            antinodes.add(antinode2)


print(len(antinodes))
