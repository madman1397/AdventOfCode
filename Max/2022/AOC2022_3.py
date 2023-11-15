import os

rucksack_list = open('Source\M_AOC2022_3.txt').readlines()

lowercase_difference = 96
uppercase_difference = 38

def calcPrio(character):
    numChar = ord(character)
    if numChar > 90:
        return (numChar - lowercase_difference)
    else:
        return (numChar - uppercase_difference)

def findDuplicates(first_comp, second_comp):
    first_comp = sorted(first_comp)
    second_comp = sorted(second_comp)

    found_duplicates = []
    last_checked = '0'

    for letter_first in first_comp:
        # skip if already checked
        if letter_first == last_checked: continue
        last_checked = letter_first

        # check if letter_first exitsts in second_comp
        for letter_second in second_comp:
            if letter_first == letter_second:
                found_duplicates.append(letter_first)
                break

    return found_duplicates

def findDuplicates_trio(first_comp, second_comp, third_comp):
    
    tmp_duplicates = findDuplicates(first_comp, second_comp)
    #print(first_comp)
    #print(second_comp)
    #print(tmp_duplicates)

    found_duplicates = findDuplicates(third_comp, tmp_duplicates)
    #print(third_comp)
    #print(found_duplicates)

    return found_duplicates

### FIRST PART ###
# 1) seperate rucksack into compartments
# 2) find duplicates in compartments
# 3) get the priotity of same items
# 4) sum the priorities of same items

sum_prio = 0
for item in rucksack_list:
    # 1) seperate rucksacks into compartments
    compartment_length = int((len(item)-1)/2)
    first_compartment = item[:compartment_length]
    second_compartment = item[compartment_length:(len(item)-1)]

    # 2) find duplicates
    duplicates = findDuplicates(first_compartment, second_compartment)
    #print(sorted(first_compartment))
    #print(sorted(second_compartment))
    #print(duplicates)

    # 3), 4) sum priorities of duplicates
    for dup_item in duplicates:
        sum_prio += calcPrio(dup_item)

print("Sum of compartment-prios = {}".format(sum_prio))

### SECOND PART ###
# 1) get trio of rucksacks
# 2) check for duplicates in all three
# 3) get prio of duplicate
# 4) sum the prio

sum_prio = 0
item_count = 0
item_list = [0, 0, 0]
for item in rucksack_list:
    
    item_list[item_count] = item[:(len(item)-1)]
    item_count = (item_count + 1) % 3
    
    if item_count == 0:
        duplicates = findDuplicates_trio(item_list[0], item_list[1], item_list[2])
        #print(item_list[0])
        #print(item_list[1])
        #print(item_list[2])
        #print(duplicates)
        
        # 3), 4) sum priorities of duplicates
        for dup_item in duplicates:
            sum_prio += calcPrio(dup_item)
    
    

print("Sum of badge-prios = {}".format(sum_prio))
