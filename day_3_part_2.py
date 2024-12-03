import re

content = []

with open('input_3.txt', mode='r', encoding='utf-8') as input_file:
    content = input_file.read()
    
do_regex = r"do\(\)"
dont_regex = r"don't\(\)"
mul_regex = r"mul\(\d{1,3},\d{1,3}\)"

instructions = re.findall(f"{do_regex}|{dont_regex}|{mul_regex}", content)

blocks = []
current_block = []

for instruction in instructions:
    if instruction == "do()" or instruction == "don't()":
        if current_block: 
            blocks.append(current_block)
        current_block = [instruction]
    else:
        current_block.append(instruction)
        
if current_block:
    blocks.append(current_block)
print(blocks)    
total_sum = 0

for block in blocks:
    if block[0] != "don't()": 
        for instruction in block:
            if instruction.startswith("mul"):
                stripped = instruction[4:-1] 
                x, y = map(int, stripped.split(","))
                total_sum += x * y

print(total_sum)