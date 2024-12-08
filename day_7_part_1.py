import itertools


with open('input_7.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.readlines()
    
content = [line.strip().split(':') for line in content]
content = [[int(line[0]), list(map(int, line[1].split()))] for line in content]

def evaluate_expression(numbers, operators):
    result = numbers[0]  
    for i in range(1, len(numbers)):
        if operators[i - 1] == '+':
            result += numbers[i]  
        elif operators[i - 1] == '*':
            result *= numbers[i]  
    return result

def find_possible_calibration(input_lines):
    total = 0
    for line in input_lines:
        target = line[0]
        numbers = line[1]

        operators_combinations = itertools.product("+*", repeat=len(numbers) - 1)

        for operators in operators_combinations:
            if evaluate_expression(numbers, operators) == target:
                total += target
                break

    return total

result = find_possible_calibration(content)
print(result)