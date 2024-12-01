list_1 = []
list_2 = []

with open('input_1.txt', mode='r', encoding='utf-8') as input_file:
    content = input_file.readlines()
    
for line in content:
    line = line.strip().split()
    list_1.append(int(line[0]))
    list_2.append(int(line[1]))
    
list_1.sort()
list_2.sort()

differences = []

for i in range(len(list_1)):    
    difference = list_1[i] - list_2[i]
    differences.append(abs(difference))
    
print(sum(differences))


for i in range(len(list_1)):    
    difference = list_1[i] - list_2[i]
    differences.append(abs(difference))
    
results = []
for i in range(len(list_1)):
    count = list_2.count(list_1[i])  
    result = list_1[i] * count
    results.append(result)
    
print(sum(results))