

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

row = 0

for line in map:
    if '^' not in line:
        row += 1
    else:
        guard_col = line.index('^')
        guard_row = row        
        break

current_direction = UP
    
visited_positions = set()
visited_positions.add((guard_row, guard_col))

while True:
    
    next_row, next_col = move_forward(guard_row, guard_col, current_direction)

    if out_of_map(next_row, next_col):
        break
    
    elif map[next_row][next_col] == '#':
        current_direction = turn_right(current_direction)
    
    else:
        guard_row, guard_col = next_row, next_col
        visited_positions.add((guard_row, guard_col))

print(len(visited_positions))
    
    
