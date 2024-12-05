data=open('day1_input.txt', 'r')

data_left = []
data_right = []
sim_score = 0

for l in data.readlines():
    data_left.append(int(l.split("   ")[0]))
    data_right.append(int(l.split("   ")[1]))

for l in data_left:
    sim_score += l * data_right.count(l)

print(sim_score)