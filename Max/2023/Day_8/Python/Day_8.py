
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest

import math
                
def getDirection(strInput):
    retValue = []
    for dir in strInput:
        if 'L' == dir:
            retValue.append(0)
        elif 'R' == dir:
            retValue.append(1)
    return retValue

def getRoutesDict(listInput):
    retValue = {}
    for line in listInput:
        listLine = line.split()
        key = (listLine[0])
        value1 = (listLine[2][1:4])
        value2 = (listLine[3][:3])
        retValue[key] = [value1, value2]
    return retValue

def solution(listInput):
    directions = getDirection(listInput[0])
    routes = getRoutesDict(listInput[2:])
    countJumps = 0
    currentPos = 'AAA'
    index = 0
    dirLen = len(directions)
    while True:
        nextPos = routes[currentPos][directions[index]]
        currentPos = nextPos
        countJumps += 1
        if currentPos == 'ZZZ':
            break
        else:
            index = (index + 1) % dirLen
    return countJumps

def getAllCurrentPos(dictRoutes):
    startPos = [key for key in dictRoutes.keys() if key.endswith('A')]
    return startPos

def getNextPos(dictRoutes, currentPos, direction):
    nextPos = [dictRoutes[key][direction] for key in currentPos]
    return nextPos

def checkEnd(currentPos):
    #end = all(s.endswith('Z') for s in currentPos)
    end = None
    for strPos in currentPos:
        if not strPos.endswith('Z'):
            end = False
            break
        else:
            end = True
    return end

def solution2(listInput):
    directions = getDirection(listInput[0])
    routes = getRoutesDict(listInput[2:])
    countJumps = 0
    currentPos = getAllCurrentPos(routes)
    index = 0
    dirLen = len(directions)
    while True:
        currentPos = [routes[key][directions[index]] for key in currentPos] #getNextPos(routes, currentPos, directions[index])
        #currentPos = nextPos
        #print(currentPos)
        countJumps += 1
        if checkEnd(currentPos):
            break
        else:
            index = (index + 1) % dirLen
    return countJumps

def solution22(listInput):
    directions = getDirection(listInput[0]) # [0, 1, 1, 0, ...]
    routes = getRoutesDict(listInput[2:]) # {'AAA' : ['BBB', 'CCC'], ...}
    countJumps = 0
    currentPos = getAllCurrentPos(routes) # ['11A', '22A', ...]
    index_dir = 0
    index_pos = 0
    dirLen = len(directions)
    posLen = len(currentPos)
    print(currentPos)
    while True:
        nextPos = routes[currentPos[index_pos]][directions[index_dir]] #getNextPos(routes, currentPos[index_pos], directions[index_dir])
        currentPos[index_pos] = nextPos
        print(currentPos)
        countJumps += 1
        if currentPos[index_pos].endswith('Z'):
            currentPos[index_pos] = countJumps
            countJumps = 0
            index_dir = 0
            index_pos = (index_pos + 1) % posLen
            if index_pos == 0 : 
                print(currentPos)
                break
        else:
            index_dir = (index_dir + 1) % dirLen
    return currentPos

def lcm_of_list(numbers):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    result = 1
    for number in numbers:
        result = lcm(result, number)

    return result

if __name__ == '__main__':
    control = input.getControlInput('2023', 'Day_8')
    countJumps = solution(control)
    print('Control =',countJumps)
    
    puzzle = input.getPuzzleInput('2023', 'Day_8')
    countJumps = solution(puzzle)
    print('Puzzle =',countJumps)

    control = input.getControlInput('2023', 'Day_8_P2')
    currentPos = solution22(control)
    print('Control P2 LCM inputs:', currentPos)
    print('LCM output:', lcm_of_list(currentPos))

    currentPos = solution22(puzzle)
    print('Puzzle P2 LCM inputs:', currentPos)
    print('LCM output:', lcm_of_list(currentPos))
                
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_8')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_8')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))

    def test_getDirection(self):
        strInput = 'LLR\n'
        self.assertEqual([0, 0, 1], getDirection(strInput))

    def test_getRoutesDict(self):
        listInput = ['AAA = (BBB, BBB)\n', 'BBB = (AAA, ZZZ)\n', 'ZZZ = (ZZZ, ZZZ)']
        self.assertEqual({'AAA':['BBB', 'BBB'], 'BBB':['AAA', 'ZZZ'], 'ZZZ':['ZZZ', 'ZZZ']}, getRoutesDict(listInput))
    
    def test_getAllCurrentPos(self):
        control = input.getControlInput('2023', 'Day_8_P2')
        dictRoutes = getRoutesDict(control[2:])
        self.assertEqual(['11A', '22A'] ,getAllCurrentPos(dictRoutes))
    
    def test_getNetPos(self):
        control = input.getControlInput('2023', 'Day_8_P2')
        dictRoutes = getRoutesDict(control[2:])
        currentPos = getAllCurrentPos(dictRoutes)
        direction = 0
        nextPos = getNextPos(dictRoutes, currentPos, direction)
        self.assertEqual(['11B', '22B'], nextPos)

    def test_checkEnd(self):
        currentPos = ['11Z', '22V']
        self.assertEqual(False, checkEnd(currentPos))
        currentPos = ['11Z', '22Z']
        self.assertEqual(True, checkEnd(currentPos))
        currentPos = '11Z'
        self.assertEqual(True, checkEnd(currentPos))