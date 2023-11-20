import os

with open("AdventOfCode\\Input\\Shayne\\2022\\Day_8.txt")as f:
    map_str = f.read()
treeRows = map_str.strip().split("\n")
#----------------------------------------------------------------------------------------------------
visFromEdge = 0
#----------------------------------------------------------------------------------------------------
for i in range(len(treeRows)):
    for j in range(len(treeRows[i])):
        # check if the current cell contains a tree that is taller than all others in its row or column
        tallest_in_row = True
        tallest_in_col = True

        for k in range(len(treeRows)):
            if i != k and treeRows[k][j] > treeRows[i][j]:
                tallest_in_row = False

        for k in range(len(treeRows[i])):
            if j != k and treeRows[i][k] > treeRows[i][j]:
                tallest_in_col = False

        if tallest_in_row or tallest_in_col:
            visFromEdge += 1
#----------------------------------------------------------------------------------------------------
print(visFromEdge)
