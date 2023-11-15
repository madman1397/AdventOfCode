import os
import re

pile_move_list = list(open('Source\M_AOC2022_5.txt').readlines())

# create seperate lists for pile and moves
pile_row_count = 0
for item in pile_move_list:
    if item == '\n':
        break
    pile_row_count += 1
pile_list = pile_move_list[:pile_row_count]
move_list = pile_move_list[(pile_row_count+1):]

# ----- Prepare a good list for solution -----

pile_numbers = pile_list[(pile_row_count-1)]
piles = []
piles_p2 = []
index_list = []
pile_count = 0

# check what the number if piles is
pile_numbers = list(map(int, re.findall(r"\d+", pile_numbers)))
pile_count = max(pile_numbers)

# prepare pile lists and create a index list, where the items of the pile are located
index_list = []
for i in range(pile_count):
    piles.append([])
    piles_p2.append([])
    if i == 0:
        index_list.append(1)
    else:
        index_list.append(index_list[i-1] + 4)

# populate the piles list
for row in pile_list:
    for idx in range(len(row)):
        if row[idx].isalpha():
            piles[index_list.index(idx)].append(row[idx])
            piles_p2[index_list.index(idx)].append(row[idx])

# ----- PART 1 -----

MOVE_COUNT_IDX = 0
POP_IDX = 1
INSERT_IDX = 2
move_instruction = []

for line in move_list:

    # get the three 
    move_instruction = list(map(int, re.findall(r"\d+", line)))

    for i in range(move_instruction[MOVE_COUNT_IDX]):
        try:
            pop = piles[move_instruction[POP_IDX]-1].pop(0)
            piles[move_instruction[INSERT_IDX]-1].insert(0, pop)
            #print("pop_list = {} | popped = {} | insert_list = {}".format(move_instruction[POP_IDX], pop, move_instruction[INSERT_IDX]))
        except:
            pass
            print("empty list")

    move_instruction.clear()

pile_string = ""
for item in piles:
    pile_string = pile_string + item[0]

print("Part 1 solution: " + pile_string)

# ----- PART 2 -----

for line in move_list:

    move_instruction = list(map(int, re.findall(r"\d+", line)))
    #print(move_instruction)

    for i in range(move_instruction[MOVE_COUNT_IDX]):
        try:
            pop = piles_p2[move_instruction[POP_IDX]-1].pop(0)
            piles_p2[move_instruction[INSERT_IDX]-1].insert(i, pop)
            #print("pop_list = {} | popped = {} | insert_list = {}".format(move_instruction[POP_IDX], pop, move_instruction[INSERT_IDX]))
        except:
            pass
            print("empty list")

    move_instruction.clear()

pile_string = ""
for item in piles_p2:
    pile_string = pile_string + item[0]

print("Part 2 solution: " + pile_string)
