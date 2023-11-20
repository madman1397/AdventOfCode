import os

movementList = open("AdventOfCode\\Input\\Shayne\\2021\\Day_2.txt").readlines()

horizontalPosition = 0
depth = 0
aim = 0

def getDirection(command):
    direction = command[:len(command)-3]
    return direction

def getDistance(command):
    distance = command[len(command)-2:]
    distanceClean = distance[:len(distance)-1]
    return int(distanceClean)

for i in movementList:
    direction = getDirection(i)
    distance = getDistance(i)
    if direction == "forward":
        horizontalPosition += distance
        if aim >= 0:
            depth += aim*distance
        else: 
            depth -= aim*distance
    elif direction == "up":
        #depth -= distance
        aim -= distance
    else:
        #depth += distance
        aim += distance
    print(str(direction) + " " + str(distance))
    print(horizontalPosition)
    print(depth)
    print(aim)
    print("-------")
print(horizontalPosition*depth)
