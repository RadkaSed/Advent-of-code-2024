import re

content = []

with open('input_3.txt', mode='r', encoding='utf-8') as input_file:
    content = input_file.read()
    
regex = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(regex, content)

results = []

for x, y in matches:
    result = int(x) * int(y)
    results.append(result)
    
print(sum(results))