
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest

def calcPQ(p, q):
    x_1 = (-p)/2 + ((p/2)**2 - q)**0.5
    x_2 = (-p)/2 - ((p/2)**2 - q)**0.5
    return [x_1, x_2]

class Race:
    def calcRangeWin(self):
        p = -self.time
        q = self.distance
        wins = calcPQ(p, q)
        self.x_1 = int(-((-wins[0])//1) - 1)
        self.x_2 =  int(wins[1]//1 + 1)
        self.numWins = abs(self.x_1 - self.x_2) + 1
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance
        self.calcRangeWin()

def getValue(strInput, nameValue):
    retValue = []
    flagNumbers = False

    strNumber = strInput.split()
    for number in strNumber:
        if nameValue in number:
            flagNumbers = True
        elif flagNumbers == True:
            try:
                retValue.append(int(number))
            except:
                flagNumbers = False

    return retValue

def getValue_P2(strInput, nameValue):
    retValue = ''
    flagNumbers = False

    strNumber = strInput.split()
    for number in strNumber:
        if nameValue in number:
            flagNumbers = True
        elif flagNumbers == True:
            try:
                int(number)
                retValue += number
            except:
                flagNumbers = False
    
    return int(retValue)

def getSolution(strInput):
    time = getValue(strInput[0], 'Time')
    distance = getValue(strInput[1], 'Distance')
    races = []
    solution = 1
    for idx in range(len(time)):
            races.append(Race(time[idx], distance[idx]))
    for race in races:
        #print('Ways to win: ' + str(race.numWins))
        solution = solution * race.numWins
    #print('Multiplied number of Wins: ' + str(solution))
    return solution

def getSolution_P2(strInput):
    time = getValue_P2(strInput[0], 'Time')
    distance = getValue_P2(strInput[1], 'Distance')
    race = Race(time, distance)
    solution = race.numWins

    return solution

if __name__ == '__main__':
    control = input.getControlInput('2023', 'Day_6')
    print('Control P1: ' + str(getSolution(control)))

    puzzle = input.getPuzzleInput('2023', 'Day_6')
    print('Puzzle P1: ' + str(getSolution(puzzle)))

    print('Control P2: ' + str(getSolution_P2(control)))

    print('Puzzle P2: ' + str(getSolution_P2(puzzle)))
    
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_6')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_6')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))
    
    def test_getValue(self):
        strInput = "Time:      7  15   30\nDistance:  9  40  200"
        self.assertEqual([7,15,30], getValue(strInput, 'Time'))
        self.assertEqual([9,40,200], getValue(strInput, 'Distance'))
    
    def test_getValue_P2(self):
        strInput = "Time:      7  15   30\nDistance:  9  40  200"
        self.assertEqual(71530, getValue_P2(strInput, 'Time'))
        self.assertEqual(940200, getValue_P2(strInput, 'Distance'))

    def test_classRace(self):
        strInput = "Time:      7  15   30\nDistance:  9  40  200"
        time = getValue(strInput, 'Time')
        distance = getValue(strInput, 'Distance')
        races = []
        for idx in range(len(time)):
            races.append(Race(time[idx], distance[idx]))

        self.assertEqual(7, (races[0].time))
        self.assertEqual(9, (races[0].distance))
        self.assertEqual(5, (races[0].x_1))
        self.assertEqual(2, (races[0].x_2))
        self.assertEqual(4, (races[0].numWins))

        self.assertEqual(15, (races[1].time))
        self.assertEqual(40, (races[1].distance))
        self.assertEqual(11, (races[1].x_1))
        self.assertEqual(4, (races[1].x_2))
        self.assertEqual(8, (races[1].numWins))

        self.assertEqual(9, (races[2].numWins))

    def test_classRace_P2(self):
        strInput = "Time:      7  15   30\nDistance:  9  40  200"
        time = getValue_P2(strInput, 'Time')
        distance = getValue_P2(strInput, 'Distance')
        race = Race(time, distance)
        self.assertEqual(71530, (race.time))
        self.assertEqual(940200, (race.distance))
        self.assertEqual(71516, (race.x_1))
        self.assertEqual(14, (race.x_2))
        self.assertEqual(71503, (race.numWins))

    def test_calcPQ(self):
        p = (-7)
        q = 9
        self.assertAlmostEqual(5.3, calcPQ(p,q)[0], 1)
        self.assertAlmostEqual(1.7, calcPQ(p,q)[1], 1)