

with open('input_4.txt', mode='r', encoding='utf-8') as input_file:
    lines = input_file.read().strip().split('\n')
    
matrix = [list(line) for line in lines]

horizontal_count = 0
words = ['XMAS', 'SAMX']
word_length = len(words[0])

for row in matrix:
    for i in range(len(row) - word_length + 1):
        substring = ''.join(row[i:(i + word_length)])
        if substring in words:
            horizontal_count += 1
            
transposed_matrix = list(zip(*matrix))
vertical_count = 0

for col in transposed_matrix:
    for i in range(len(col) - word_length + 1):
        substring = ''.join(col[i:(i + word_length)])
        if substring in words:
            vertical_count += 1
            

diagonals_left = []
rows, cols = len(matrix), len(matrix[0])

for i in range(cols):
    diagonal = []
    row, col = 0, i
    while row < rows and col < cols:
        diagonal.append(matrix[row][col])
        row += 1
        col += 1
    diagonals_left.append(diagonal)
    
for j in range(1, rows):
    diagonal = []
    row, col = j, 0
    while row < rows and col < cols:
        diagonal.append(matrix[row][col])
        row += 1
        col += 1
    diagonals_left.append(diagonal)

diagonal_leftcount = 0
    
for diag in diagonals_left:
    for i in range(len(diag) - word_length + 1):
        substring = ''.join(diag[i:(i + word_length)])
        if substring in words:
            diagonal_leftcount += 1
            
diagonals_right = []
rows, cols = len(matrix), len(matrix[0])

for i in range(cols - 1, -1, -1):
    diagonal = []
    row, col = 0, i
    while row < rows and col >= 0:
        diagonal.append(matrix[row][col])
        row += 1
        col -= 1
    diagonals_right.append(diagonal)
    
for row_start in range(1, rows):
    diagonal = []
    row, col = row_start, cols - 1
    while row < rows and col >= 0: 
        diagonal.append(matrix[row][col])
        row += 1
        col -= 1
    diagonals_right.append(diagonal)
    
diagonal_rightcount = 0

for diag in diagonals_right: 
    for i in range(len(diag) - word_length + 1):
        substring = ''.join(diag[i:(i + word_length)])
        if substring in words:
            diagonal_rightcount += 1
            
total = vertical_count + horizontal_count+ diagonal_leftcount + diagonal_rightcount

print(total)

            
