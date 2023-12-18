
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest
                
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

if __name__ == '__main__':
    control = input.getControlInput('2023', 'Day_8')
    countJumps = solution(control)
    print('Control =',countJumps)
    
    puzzle = input.getPuzzleInput('2023', 'Day_8')
    countJumps = solution(puzzle)
    print('Puzzle =',countJumps)
                
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
