data = open('day2_input.txt', 'r')

data_list = [x.split() for x in data]
data_sorted = [sorted(lst.split(), key=int) for lst in data]


def order_discovery(lst):
    if lst == sorted(lst, key=int) or lst == sorted(lst, reverse=True, key=int):
        return "Safe"
    else:
        return "Unuseable"


def largest_difference(num):
    return max(abs(num[i] - num[i + 1]) for i in range(len(num) - 1))


def difference_count(num):
    counter = 0
    num = list(map(int, num))
    for i in range(len(num) - 1):
        if num[i] == num[i + 1] or abs(num[i] - num[i + 1]) > 3:
            counter += 1
    else:
        pass
    return str(counter)


data_keys = {}

for x in data_list:
    data_keys[tuple(x)] = difference_count(x)

dampened_count = 0
dampened_vals = []


for key, value in data_keys.items():
    print(f"{key} - {value}")
    if int(value) <= 1:
        dampened_count += 1
        dampened_vals.append(list(key))
    else:
        pass

print(dampened_count)


