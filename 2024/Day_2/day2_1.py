data = open('day2_input.txt', 'r')


def order_discovery(lst):
    if lst == sorted(lst) or lst == sorted(lst, reverse=True):
        return "Safe"
    else:
        return "Unuseable"


def largest_difference(num):
    return max(abs(num[i] - num[i + 1]) for i in range(len(num) - 1))


reports = [list(map(int, line.split())) for line in data]

useable_reports = (
    [report for report in reports if order_discovery(report) != "Unuseable"]
)
safe_reports = 0
for x in useable_reports:
    if all(1 <= abs(x[i] - x[i + 1]) <= 3 for i in range(len(x) - 1)):
        safe_reports += 1


print(safe_reports)
