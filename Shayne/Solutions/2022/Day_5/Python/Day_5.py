#import raw .txt source
sourceData = open("AdventOfCode\\Input\\Shayne\\2022\\Day_5.txt").readlines()
#----------------------------------------------------------------------------------------------------

#trim line breaks from source, assign lines as list entries
trimmedSource = []
for i in sourceData:
    trimmedSource.append(i[:len(i)-1])
#----------------------------------------------------------------------------------------------------
sortedPiles = []
#trim top portion of document to its own variable, define pile row labels to another variable
piles = trimmedSource[:trimmedSource.index("")-1] #outputs just the pile chart as its read from the trimmed source
indexRef = trimmedSource[trimmedSource.index("")-1:trimmedSource.index("")] #outputs just the index line as its read from the trimmed source
indexClean = indexRef[0].split() #cleans the index row, removing spaces and separating them as list entries
indexClean = list(map(int, indexClean)) #prev cont'd
#----------------------------------------------------------------------------------------------------
newPiles = []
#sorts pile diagram into lists by stack. index 0 up is left to right, sublist index 0 up is bottom moving up.
for i in indexClean:
    newPiles.append([])
for row in piles:
    for stack in indexClean:
        newPiles[stack-1].append(row[indexRef[0].index(str(stack))])

for sublist in newPiles:
    sublist.reverse()
    while(" " in sublist):sublist.remove(" ")

#print(newPiles)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#Pile movement command comprehension
commandList = trimmedSource[trimmedSource.index("")+1:] #full list of commands snipped from source txt

multiCranePiles = []
multiCranePiles.extend(newPiles)

def singleCrateComprehension(input):
    takeFrom = int(input[1])-1
    putIn = int(input[2])-1
    for i in range(int(input[0])):
        newPiles[putIn].append(newPiles[takeFrom][-1])
        newPiles[takeFrom].pop(-1)

def multiCrateComprehension(info):
    num = int(info[0])
    take = int(info[1])-1
    put = int(info[2])-1
    multiCranePiles[put].extend(multiCranePiles[take][-num:len(multiCranePiles[take])])
    multiCranePiles[take] = multiCranePiles[take][:-num]
    


#breaks down commands into a simple set of 3 numbers (x times, from y, to z), stored as a list [0, 1, 2]
for command in commandList:
    command = commandList[commandList.index(command)]
    commandCut = command.split()
    for char in commandCut:
        if char.isnumeric() == False: commandCut.pop(commandCut.index(char))
    #singleCrateComprehension(commandCut)
    multiCrateComprehension(commandCut)
    #print(commandCut)

#print(newPiles)
stackTops = []
stackTopsMulti = []
for i in newPiles:
    stackTops.append(newPiles[newPiles.index(i)][-1])
print("In step one, the top crates from left to right are " + str(stackTops))
for i in multiCranePiles:
    stackTopsMulti.append(multiCranePiles[multiCranePiles.index(i)][-1])
print("In step two, the top crates from left to right are " + str(stackTopsMulti))

