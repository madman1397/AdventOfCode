###Goal: Find the elf with the most calories
###premise: elves write 
###step 1: iterate list, sum calories and attribute to each elf until a blank space is hit.

crude = open("Input\Shayne\\2022\Day_1.txt").readlines()
src = []
#Clean input for interpretation
for ln in crude:
    ln = ln.strip()
    src.append(ln)

elfList = []
cSum = 0

for item in src:
    if len(item) > 0:
        cSum += int(item)
        if src.index(item) == len(src)-1:
            elfList.append(cSum)
        else:pass
    else:
        elfList.append(cSum)
        cSum = 0
sList = sorted(elfList, reverse=True)

topThree = [sList[0],sList[1],sList[2]]
topThreeSum = sum(topThree)

print(str(topThree)+str(topThreeSum))
