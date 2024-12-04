

with open('input_4.txt', mode='r', encoding='utf-8') as input_file:
    lines = input_file.read().strip().split('\n')
    
matrix = [list(line) for line in lines]
rows, cols = len(matrix), len(matrix[0])

count = 0

for row in range (1, rows -1):
    for col in range (1, cols - 1):
        if matrix [row][col] == 'A':
            top_left = matrix[row - 1][col - 1]
            bottom_right = matrix[row + 1][col + 1]
            top_right = matrix[row - 1][col + 1]
            bottom_left = matrix[row + 1][col - 1]
            if ((top_left == 'M' and bottom_right == 'S' or
            top_left == 'S' and bottom_right == 'M') and
            (top_right == 'M' and bottom_left == 'S' or
            top_right == 'S' and bottom_left == 'M')):
                count += 1
            
print(count)