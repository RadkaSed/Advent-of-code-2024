def find_words_in_lines(lines, words, word_length):
    count = 0
    for line in lines:
        for i in range(len(line) - word_length + 1):
            substring = ''.join(line[i:(i + word_length)])
            if substring in words:
                count += 1
    return count

def generate_diagonals_lr(matrix):
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []

    for i in range(cols):
        diagonal = []
        row, col = 0, i
        while row < rows and col < cols:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
        diagonals.append(diagonal)

    for j in range(1, rows):
        diagonal = []
        row, col = j, 0
        while row < rows and col < cols:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
        diagonals.append(diagonal)

    return diagonals

def generate_diagonals_rl(matrix):
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []

    for i in range(cols - 1, -1, -1):
        diagonal = []
        row, col = 0, i
        while row < rows and col >= 0:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)

    for j in range(1, rows):
        diagonal = []
        row, col = j, cols - 1
        while row < rows and col >= 0:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)

    return diagonals


with open('input_4.txt', mode='r', encoding='utf-8') as input_file:
    lines = input_file.read().strip().split('\n')

matrix = [list(line) for line in lines]
words = ['XMAS', 'SAMX']
word_length = len(words[0])


horizontal_count = find_words_in_lines(matrix, words, word_length)
vertical_count = find_words_in_lines(zip(*matrix), words, word_length)
diagonals_left = generate_diagonals_lr(matrix)
diagonal_leftcount = find_words_in_lines(diagonals_left, words, word_length)
diagonals_right = generate_diagonals_rl(matrix)
diagonal_rightcount = find_words_in_lines(diagonals_right, words, word_length)


total = horizontal_count + vertical_count + diagonal_leftcount + diagonal_rightcount
print(total)

