

with open('input_5.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()
    
rules_in, lines_in = content.split('\n\n')

rules = [line.split('|') for line in rules_in.splitlines()]
rules = [[int(x) for x in rule] for rule in rules]

lines = [line.split(',') for line in lines_in.splitlines()]
lines = [[int(x) for x in line] for line in lines]

valid_lines = []

for line in lines:
    is_valid = True
    
    for rule in rules:
        if rule[0] in line and rule[1] in line:
            index_1 = line.index(rule[0])
            index_2 = line.index(rule[1])
            
            if index_1 > index_2:
                is_valid = False
                break
    if is_valid:
        valid_lines.append(line)
        
medium_index = len(line) // 2

medium_nums = []

for line in valid_lines:
    medium_index = len(line) // 2
    medium_nums.append(line[medium_index])

print(sum(medium_nums))
