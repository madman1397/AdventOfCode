import os
Type = 'Shayne'
Year = __file__.split(os.sep)[-3]
Day = __file__.split(os.sep)[-2]
print('Advent Of Code',Year,Day)
Input = [line.strip() for line in open(os.path.join(os.sep.join(__file__.split(os.sep)[:-5]),'Input',Type,Year,Day+'.txt')).readlines()]

List_A = [int(line.split()[0]) for line in Input]
List_B = [int(line.split()[1]) for line in Input]

def ascendingList():
    return list(zip(sorted(List_A),sorted(List_B)))

def distances():
    return [max(line)-min(line) for line in ascendingList()]

def similarityScores():
    similarities = [num*List_B.count(num) for num in List_A]
    return similarities

#Part One
print(f"Part One: {sum(distances())}")

#Part Two
print(f"Part Two: {sum(similarityScores())}")