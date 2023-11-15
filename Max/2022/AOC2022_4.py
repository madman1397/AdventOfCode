import os

pair_list = open('Source\M_AOC2022_4.txt').readlines()

elf_1_start = []
elf_1_start_int = 0
elf_1_end = []
elf_1_end_int = 0

elf_2_start = []
elf_2_start_int = 0
elf_2_end = []
elf_2_end_int = 0

elf_pair = [elf_1_start, elf_1_end, elf_2_start, elf_2_end]
elf_indicator = 0

subsets_found = 0
overlaps_found = 0

for item in pair_list:

    for character in item:
        if character == '-':
            elf_indicator += 1
            continue
        elif character == ',':
            elf_indicator += 1
            continue
        elif character == '\n':
            elf_indicator = 0
            break
        elf_pair[elf_indicator].append(character)
        
    elf_1_start_int = int("".join(elf_1_start))
    elf_1_end_int = int("".join(elf_1_end))
    elf_2_start_int = int("".join(elf_2_start))
    elf_2_end_int = int("".join(elf_2_end))
    for clearing in elf_pair:
        clearing.clear()

 

    # check subsets
    if (elf_1_start_int == elf_2_start_int) or (elf_1_end_int == elf_2_end_int):
        subsets_found += 1
    elif (elf_1_start_int > elf_2_start_int):
        if (elf_1_end_int < elf_2_end_int):
            subsets_found += 1
    elif (elf_1_start_int < elf_2_start_int):
        if(elf_1_end_int > elf_2_end_int):
            subsets_found += 1

    # check overlaps
    if (elf_1_start_int == elf_2_start_int) or (elf_1_end_int == elf_2_end_int):
        overlaps_found += 1
    elif (elf_1_start_int == elf_2_end_int) or (elf_1_end_int == elf_2_start_int):
        overlaps_found += 1
    elif (elf_1_start_int > elf_2_start_int):
        if (elf_1_start_int < elf_2_end_int):
            overlaps_found += 1
    elif (elf_1_start_int < elf_2_start_int):
        if (elf_1_end_int > elf_2_start_int):
            overlaps_found += 1


print("Subsets found = {}".format(subsets_found))
print("Overlaps found = {}".format(overlaps_found))

