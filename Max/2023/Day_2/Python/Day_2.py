
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest

def multiplyList(mulList):
    retValue = 1

    if bool(mulList) and all(isinstance(elem, int) for elem in mulList):
        for elem in mulList:
            retValue *= elem
    elif None in mulList:
        retValue = 0
    else:
        print('Argument mulList has to be a list made up of only integer values!')
        retValue = None
    
    return retValue

def getSubGameResult(stringSubGame):
    stringListColors = ['red', 'green', 'blue']
    if stringSubGame == '':
        retValue = [None, None, None]
    else:
        retValue = [0, 0, 0]
    ballCountString = ''
    ballCount = None
    ballColorString = ''
    indexColor = None

    for idxString, character in enumerate(stringSubGame):
        
        if character.isnumeric():
            ballCountString += character
        elif character != ',' or character != ';':
            ballColorString += character
            for idxColor, color in enumerate(stringListColors):
                if color in ballColorString:
                    indexColor = idxColor
        
        if character == ',' or character == ';' or (idxString+1) == len(stringSubGame):
            try:
                ballCount = int(ballCountString)
                retValue[indexColor] = ballCount
            except (TypeError, ValueError):
                retValue = [None, None, None]
            ballCountString = ''
            ballCount = None
            ballColorString = ''
            indexColor = None

    return retValue

def getGameResult(stringGame):
    retValue = []
    startGame = False
    stringSubGame = ''

    if isinstance(stringGame, list):
        print('Function getGameResult cannot work on lists!')
    else:
        for idxString, character in enumerate(stringGame):
            if character == ':':
                startGame = True
            elif startGame:
                stringSubGame += character
                if character == ';' or (idxString+1) == len(stringGame):
                    retValue.append(getSubGameResult(stringSubGame))
                    stringSubGame = ''

    return retValue

def getSumIdxPossible(stringAllGames):
    retValue = 0
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    maxColor = [maxRed, maxGreen, maxBlue]
    gameRes = None
    gamePossible = True

    for idxGame, game in enumerate(stringAllGames):
        gameRes = getGameResult(game)
        retValue += (idxGame+1)
        gamePossible = True
        for subGame in gameRes:
            for idxColor, resColor in enumerate(subGame):
                if resColor > maxColor[idxColor] and gamePossible:
                    retValue -= (idxGame+1)
                    gamePossible = False
                    break

    return retValue

def getSumPowerPossible(stringAllGames):
    retValue = 0
    gameRes = None
    gameColorMax = [1, 1, 1]
    gamePower = None

    for idxGame, game in enumerate(stringAllGames):
        gameRes = getGameResult(game)
        if len(gameRes) == 0:
            continue
        for subGame in gameRes:
            for idxColor, resColor in enumerate(subGame):
                    if resColor > gameColorMax[idxColor]:
                        gameColorMax[idxColor] = resColor
        gamePower = multiplyList(gameColorMax)
        retValue += gamePower
        gameColorMax = [1, 1, 1]

    return retValue

if __name__ == '__main__':
    control = input.getControlInput('2023', 'Day_2')    
    print('Control sum of idx possible: ' + str(getSumIdxPossible(control)))

    puzzle = input.getPuzzleInput('2023', 'Day_2')
    print('Puzzle sum of idx possible ' + str(getSumIdxPossible(puzzle)))
  
    print('Control P2 power of game: ' + str(getSumPowerPossible(control)))

    print('Puzzle P2 power of game: ' + str(getSumPowerPossible(puzzle)))
                
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_2')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_2')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))

    def test_getSubGameResult(self):
        self.assertEqual([4,0,3], getSubGameResult(' 3 blue, 4 red;'))
        self.assertEqual([0,2,0], getSubGameResult(' 2 green'))
        self.assertEqual([None, None, None], getSubGameResult(''))
        self.assertEqual([None, None, None], getSubGameResult('n'))

    def test_getGameResult(self):
        control = input.getControlInput('2023', 'Day_2')
        self.assertEqual([[4, 0, 3], [1, 2, 6], [0, 2, 0]], getGameResult(control[0]))
        self.assertEqual([[6, 3, 1], [1, 2, 2]], getGameResult('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'))
        self.assertEqual([[6, 3, 1], [1, 2, 2]], getGameResult('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'))
        self.assertEqual([[None, None, None]], getGameResult('Game 3: '))


    def test_getSumIdxPossible(self):
        control = input.getControlInput('2023', 'Day_2')
        self.assertEqual(8, getSumIdxPossible(control))

    def test_getSumPowerPossible(self):
        control = input.getControlInput('2023', 'Day_2')
        #self.assertEqual(2286, getSumPowerPossible(control))
        self.assertEqual(0, getSumPowerPossible('Game 3: ;'))

    def test_multiplyList(self):
        self.assertEqual(None, multiplyList(['20', 13, 6]))
        self.assertEqual(1560, multiplyList([20, 13, 6]))
        self.assertEqual(0, multiplyList([None, None, None]))


                