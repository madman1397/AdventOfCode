rucksackList = open("Input\Shayne\\2022\Day_3.txt").readlines()

priorityList = []
groupPrioList = []
bagList = []
groupItems = []

def compartmentalized(bag):
    compartmentLength = int(((len(i))-1)/2)
    firstCompartment = bag[:compartmentLength]
    secondCompartment = bag[compartmentLength:(len(bag)-1)]
    splitBag = [firstCompartment,secondCompartment]
    return splitBag

def findCommon(compartments):
    if len(compartments) > 2:
        common = set(compartments[0]).intersection(compartments[1],compartments[2])
    else:
        common = set(compartments[0]).intersection(compartments[1])
    return common

def calcPriority(item):
    asciiPrio = ord(item)

    itemCase = item.islower()
    if itemCase == True:
        itemValue = ord(item) - (ord("a")-1)
    else:
        itemValue = (ord(item.lower()) - (ord("a")-2)) + (ord("z") - ord("a"))
    return itemValue



for i in rucksackList:
    currentBag = i
    organizedBag = compartmentalized(currentBag)
    commonItem = list(findCommon(organizedBag))
    itemValue = calcPriority(commonItem[0])
    priorityList.append(itemValue)


    bagList.append(str(organizedBag[0]+organizedBag[1])) 
    if len(bagList) == 3:
        trioCommon = list(findCommon(bagList))
        groupValue = calcPriority(trioCommon[0])
        groupPrioList.append(groupValue)
        bagList.clear()

print("the sum of all personal priorities is {}".format(sum(priorityList)))
print("the sum of all group priorities is {}".format(sum(groupPrioList)))