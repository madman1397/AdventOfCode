sectionIDs = open("AdventOfCode\\Input\\Shayne\\2022\\Day_4.txt").readlines()

#Clean data in currently analyzed line for easier use later
def cleanData(rawPairs):
    pairText = rawPairs[:len(rawPairs)-1]
    splitPairs = pairText.split(",")
    leftRange = [splitPairs[0].split("-")]
    rightRange = [splitPairs[1].split("-")]
    pairList = leftRange+rightRange
    return pairList

#check ranges and fill range in new lists
def findRanges(pairList):
    elfOne = pairList[0]
    elfTwo = pairList[1]
    leftRange = list(range(int(elfOne[0]),int(elfOne[1])+1))
    rightRange = list(range(int(elfTwo[0]),int(elfTwo[1])+1))
    return [leftRange,rightRange]

#check new lists for similarities
def checkOverlap(ranges):
    common = list(set(ranges[0]).intersection(ranges[1]))
    return [ranges[0], ranges[1], common]

#make lists of similarities, if list size is equal to either other list, this means one list is totally encapsulated in the other.
def checkSubset(ranges):
    if len(ranges[2]) == len(ranges[0]) or len(ranges[2]) == len(ranges[1]):
        return True
    else: return False

subsetsFound = 0
overlapsFound = 0

for i in sectionIDs:
    if checkSubset(checkOverlap(findRanges(cleanData(i)))) == True: 
        subsetsFound += 1
        overlapsFound += 1
    elif len(checkOverlap(findRanges(cleanData(i)))[2]) > 0:
        overlapsFound += 1
    

print("Subsets Found = " + str(subsetsFound))
print("Overlaps Found = " + str(overlapsFound))