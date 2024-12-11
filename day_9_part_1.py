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


while '.' in unzip_file:
    first_dot = unzip_file.index('.')
    last_block = len(unzip_file) - 1 

    while last_block >= 0:
        if unzip_file[last_block] != '.':
            break
        last_block -= 1

    if last_block <= first_dot:
        break 


    unzip_file[first_dot] = unzip_file[last_block]
    unzip_file[last_block] = '.'

result = 0
for position, char in enumerate(unzip_file):
    if char != '.':
        result += position * int(char)


print(f"Výsledek: {result}")
