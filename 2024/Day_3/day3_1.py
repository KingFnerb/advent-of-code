import re

pattern = r"mul\(\d+,\d+\)"
num_pattern = r"\d+,\d+"
match_list = []
num_list = []
total = 0

with open('day3_input.txt', 'r') as file:
    for x in file:
        match_list.append(re.findall(pattern, x))

for x in match_list:
    num_list.append(re.findall(num_pattern, str(x)))


for x in num_list:
    for n in x:
        total += int(re.findall(r"\d+", n)[0]) * int(re.findall(r"\d+", n)[1])

print(total)
