import os
import re
#Define input, and strip data
Type = 'Shayne'
Input = [line.strip() for line in open(os.path.join(os.path.sep.join(__file__.split(os.path.sep)[:6]),'Input',Type,__file__.split(os.sep)[-4],(__file__.split(os.sep)[-1]).split('.')[0]+'.txt')).readlines()]

#Iterate input, remove non numeric characters, then concatenate only the first and last numerics on the line
def getNums(fInput):
    Numerics = [''.join(filter(str.isdigit, i)) for i in fInput]
    EndCaps = [int(i[0]+i[-1]) for i in Numerics]
    return EndCaps

PartOne = sum(getNums(Input))
print(PartOne)

#---------------PART-TWO-----------------#
def Words2Nums(line):
    #analyze line with a moving 'frame', if frame sees number, or verbose number, append to new list as int, then return that list for further handling
    NumDict = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    numLine = []
    minLen = len(min(NumDict, key=len))
    maxLen = len(max(NumDict, key=len))
    frameStart = 0
    #Iteration Limiter: cease iteration when frame reaches end of line
    while frameStart<len(line):
        #Define the initial size of the view frame
        frameEnd = frameStart+minLen
        #If first index in frame is numeric, append to numLine, skip to next start index before iterating further
        if line[frameStart].isnumeric():
            numLine.append(line[frameStart])
            frameStart += 1
        #each iteration, move the frame over(up) one index, adjust frame width for each possible word size,-
        #-each time checking for a match in NumDict. If match, append its corresponding int to numLine
        else:
            while frameEnd<=frameStart+maxLen:
                frame = line[frameStart:frameEnd]
                if frame in NumDict:
                    numLine.append(NumDict[frame])              
                frameEnd +=1
            frameStart += 1
    #return all numerics, verbose and int, in order of occurance, joined as one int (ex. seven3p5nine --> 7359)
    return ''.join(numLine)
        

P2Input = [Words2Nums(line) for line in Input]
PartTwo = sum(getNums(P2Input))
print(PartTwo)