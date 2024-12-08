"""I gave in an used Chat GPT on this one.

I am a dirty cheater but was tired of routinely getting the wrong answer.
"""

data = open('day2_input.txt', 'r')

data_list = [x.split() for x in data]


def order_discovery(lst):
    lst = list(map(int, lst))
    if lst == sorted(lst) or lst == sorted(lst, reverse=True):
        return True
    return False


def difference_count(num):
    num = list(map(int, num))
    for i in range(len(num) - 1):
        diff = abs(num[i] - num[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


dampened_count = 0

for report in data_list:
    if order_discovery(report) and difference_count(report):
        dampened_count += 1
    else:
        found_safe = False
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:] 
            if order_discovery(new_report) and difference_count(new_report):
                dampened_count += 1  
                found_safe = True
                break


print(dampened_count)
