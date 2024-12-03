content = []

with open('input_2.txt', mode='r', encoding='utf_8') as input_file:
    content = input_file.readlines()

line_list = []    
for line in content:
    line = line.strip().split()
    line = list(map(int, line))
    line_list.append(line)

safe_reports_with_dampener = []

for report in line_list:
    is_safe = True
    if report == sorted(report) or report == sorted(report, reverse=True):
        for i in range(1, len(report)):
            if abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
                is_safe = False
                break
        if is_safe:
            safe_reports_with_dampener.append(report)
            continue

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        is_safe = True
        if modified_report == sorted(modified_report) or modified_report == sorted(modified_report, reverse=True):
            for j in range(1, len(modified_report)):
                if abs(modified_report[j] - modified_report[j - 1]) < 1 or abs(modified_report[j] - modified_report[j - 1]) > 3:
                    is_safe = False
                    break
            if is_safe:
                safe_reports_with_dampener.append(report)
                break


print(len(safe_reports_with_dampener))