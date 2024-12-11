with open('input_9.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read().strip()


unzip_file = []
index = 0
id = 0

for num in content:
    length = int(num)
    if index % 2 == 0:
        unzip_file.extend([id] * length)
        id += 1
    else:
        unzip_file.extend(['.'] * length)
    index += 1
    
files = {}
for i, char in enumerate(unzip_file):
    if char != '.':
        char = int(char)
        if char not in files:
            files[char] = []
        files[char].append(i)

for file_id in sorted(files.keys(), reverse=True):
    positions = files[file_id]
    file_length = len(positions)
    
    free_spaces = []
    start = None
    count = 0
    
    for i, char in enumerate(unzip_file):
        if char == '.':
            if start is None:
                start = i
            count += 1
        else:
            if count > 0:
                free_spaces.append((start, count))
            start = None
            count = 0
    if count > 0:
        free_spaces.append((start, count))

    for start, size in free_spaces:
        if size >= file_length and positions[0] > start:
            for j in range(file_length):
                unzip_file[start + j] = str(file_id)
            for pos in positions:
                unzip_file[pos] = '.'
            break
        
      
result = 0
for position, char in enumerate(unzip_file):
    if char != '.':
        result += position * int(char)


print(f"Výsledek: {result}")