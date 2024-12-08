with open('input_6.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.readlines()
    
map = [list(line.strip()) for line in content]

UP = (-1, 0)
DOWN = (+1, 0)
RIGHT = (0, +1)
LEFT = (0, -1)
   
    

def turn_right(direction):
    if direction == UP:
        return RIGHT
    elif direction == RIGHT:
        return DOWN
    elif direction == DOWN:
        return LEFT
    elif direction == LEFT:
        return UP
    
def move_forward(row, col, direction):
    row += direction[0]
    col += direction[1]
    return row, col

def out_of_map(row, col):
    if row < 0 or col < 0 or row >= len(map) or col >= len(map[0]):
        return True
    else:
        return False
    
def simulate_guard(map, start_row, start_col, current_direction):
    row, col = start_row, start_col
    visited_positions = set()
    visited_positions.add((row, col, current_direction))
    
    while True:
        next_row, next_col = move_forward(row, col, current_direction)
        
        if out_of_map(next_row, next_col):
            return False
        if (next_row, next_col, current_direction) in visited_positions:
            return True
        if map[next_row][next_col] != '#':
            row, col = next_row, next_col
            visited_positions.add((row, col, current_direction))
        else:
            current_direction = turn_right(current_direction)

def find_possible_obtacle_position(map, guard_row, guard_col, current_direction):
    possible_obtacle_count = 0
    
    for r in range(len(map)):
        for c in range (len(map[r])):
            if map[r][c] != '#' and (r, c) != (guard_row, guard_col):
                new_map = [row [:] for row in map]
                new_map[r][c] = '#'
                
                if simulate_guard(new_map, guard_row, guard_col, current_direction):
                    possible_obtacle_count += 1
                    
    return possible_obtacle_count
        
    
               
row = 0

for line in map:
    if '^' not in line:
        row += 1
    else:
        guard_col = line.index('^')
        guard_row = row        
        break

current_direction = UP

possible_position = find_possible_obtacle_position(map, guard_row, guard_col, current_direction) 

print(possible_position)
    
