content = []

with open('test_input_2.txt', mode='r', encoding='utf_8') as input_file:
    content = input_file.readlines()

line_list = []    
for line in content:
    line = line.strip().split()
    line = list(map(int, line))
    line_list.append(line)

safe_reports_with_dampener = []

for report in line_list:
    is_safe = True
    dampener_used = False

    for i in range(1, len(report)):
        difference = abs(report[i] - report[i - 1])

        if difference < 1 or difference > 3:
            if not dampener_used:
                dampener_used = True
                if i + 1 < len(report):
                    second_difference = abs(report[i + 1] - report[i - 1])
                    if 1 <= second_difference <= 3:
                        continue
            is_safe = False
            break

    if is_safe:
        safe_reports_with_dampener.append(report)

print(safe_reports_with_dampener)