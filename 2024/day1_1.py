
data=open('day1_input.txt', 'r')

def get_distance(l,r):
    distance = abs(l-r)
    return distance

data_left = []
data_right = []
data_total = []

for l in data.readlines():
    data_left.append(l.split("   ")[0])
    data_right.append(l.split("   ")[1])

left_sorted = sorted(data_left)
right_sorted = sorted(data_right)

for l,r in zip(left_sorted, right_sorted):
    data_total.append(get_distance(int(l),int(r)))

final_tally = [sum(int(x) for x in data_total)]
print(final_tally)