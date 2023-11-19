import os

src = open("Input\Shayne\\2021\Day_1.txt").readlines() #import source data to var

#define variables
increases = 0 #counts instances of increases from set A to B (A<B) occur within the dataset.
index = 0 #counts data points (index) observed thus far. 
aSum = 0 #temporary variable for Window A's sum, resets with each run of the main loop.
bSum = 0 #temporary variable for Window B's sum, resets with each run of the main loop.
loop = 0 #used to limit loops when calculating window sums; resets with each run of the main loop.

while index < len(src) - 2: #number of comparisons, should be equal to number of data points in set
    while loop < 3: #loops 3 times to create each sets 3 digit "window" and calculate their sums. 
        try:
            aSum += int(src[index])
            bSum += int(src[index+1])
        except:pass #allows excecution to continue when there arent enough data points left for another loop, but another was attempted.
        index += 1 
        loop += 1
    if(aSum<bSum):increases+=1

    index -= 2
    loop = 0
    aSum = 0
    bSum = 0
print (increases)