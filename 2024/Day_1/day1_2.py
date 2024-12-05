data = open('day1_input.txt', 'r')


data_left = []
data_right = []
sim_score = 0


for line in data.readlines():
    data_left.append(int(line.split("   ")[0]))
    data_right.append(int(line.split("   ")[1]))


for line in data_left:
    sim_score += line * data_right.count(line)


print(sim_score)
