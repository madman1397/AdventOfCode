import os

calories_list = open('Source\M_AOC2022_1.txt').readlines()

# 1) seperate the Elfs for total calories
elf_list = []
calories_num = 0

for i in calories_list:
    if i == '\n':
        elf_list.append(calories_num)
        calories_num = 0
        continue
    else:
        calories_num += int(i)

# 2) find max calories and index of elf
max_val = max(elf_list)
max_idx = elf_list.index(max_val)
print(max_val)
print(max_idx)

# 3) sort - highest first & add highest three
elf_list.sort(reverse=True)
sum_top_three = elf_list[0] + elf_list[1] + elf_list[2]
print(sum_top_three)
