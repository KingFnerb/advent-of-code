data = open('day1_input.txt', 'r')


def get_distance(left, right):
    distance = abs(left - right)
    return distance


data_left = []
data_right = []
data_total = []

for line in data.readlines():
    data_left.append(line.split("   ")[0])
    data_right.append(line.split("   ")[1])

left_sorted = sorted(data_left)
right_sorted = sorted(data_right)

for left, right in zip(left_sorted, right_sorted):
    data_total.append(get_distance(int(left), int(right)))

final_tally = [sum(int(x) for x in data_total)]
print(final_tally)
