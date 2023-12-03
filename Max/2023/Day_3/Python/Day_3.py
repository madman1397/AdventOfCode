
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest

def isSymbol(charInput):
    retValue = None

    if not isinstance(charInput, str):
        retValue = False
    elif charInput.isnumeric():
        retValue = False
    elif charInput == '.' or charInput == '\n':
        retValue = False
    else:
        retValue = True

    return retValue

class Symbol:
    character = None
    y_coord = None
    x_coord = None
    numAdjacent = []
    gearRatio = 0
    def __init__(self, new_character, start_y_coord, start_x_coord):
        self.character = new_character
        self.y_coord = start_y_coord
        self.x_coord = start_x_coord
        self.numAdjacent = []
    def __str__(self):
        return str('y: ' + str(self.y_coord) + ' x: ' + str(self.x_coord))

class Number(Symbol):
    x_coord_end = None
    value = None
    def __init__(self, start_y_coord, start_x_coord, end_x_coord, new_value):
        Symbol.__init__(self, '.', start_y_coord, start_x_coord)
        self.x_coord_end = end_x_coord
        self.value = new_value
    def __str__(self):
        return Symbol.__str__(self) + str(' x_end: ' + str(self.x_coord_end))


class Game:
    symbolList = []
    numberList = []
    partNumberList = []

    def __init__(self, stringObjectLines):
        self.symbolList = []
        self.numberList = []
        self.partNumberList = []
        self.populateLists(stringObjectLines)
        self.checkNearSymbol()
        self.checkGear()

    def addSymbol(self, character, start_y_coord, start_x_coord):
        self.symbolList.append(Symbol(character, start_y_coord, start_x_coord))

    def addNumber(self, start_y_coord, start_x_coord, end_x_coord, value):
        self.numberList.append(Number(start_y_coord, start_x_coord, end_x_coord, value))

    def populateLists(self, stringObjectLines):
        if not isinstance(stringObjectLines, list):
            pass
        elif bool(stringObjectLines) and all(isinstance(elem, str) for elem in stringObjectLines):
            first_x_coord = None
            flagNumStart = False
            for y_coord, line in enumerate(stringObjectLines):
                for x_coord, character in enumerate(line):
                    if isSymbol(character):
                        self.addSymbol(character, y_coord, x_coord)
                    if character.isnumeric() and not flagNumStart:
                        first_x_coord = x_coord
                        flagNumStart = True
                    elif not character.isnumeric() and flagNumStart:
                        value = int(line[first_x_coord:x_coord])
                        self.addNumber(y_coord, first_x_coord, x_coord-1, value)
                        first_x_coord = None
                        flagNumStart = False

    def checkNearSymbol(self):
        for number in self.numberList:
            for symbol in self.symbolList:
                if number.y_coord < (symbol.y_coord - 1) or number.y_coord > (symbol.y_coord + 1):
                    continue
                elif number.x_coord <= symbol.x_coord and number.x_coord_end >= symbol.x_coord:
                    self.partNumberList.append(number.value)
                    symbol.numAdjacent.append(number.value)
                elif number.x_coord >= (symbol.x_coord-1) and number.x_coord <= (symbol.x_coord+1):
                    self.partNumberList.append(number.value)
                    symbol.numAdjacent.append(number.value)
                elif number.x_coord_end >= (symbol.x_coord-1) and number.x_coord_end <= (symbol.x_coord+1):
                    self.partNumberList.append(number.value)
                    symbol.numAdjacent.append(number.value)

    def checkGear(self):
        for symbol in self.symbolList:
            if symbol.character != '*':
                continue
            elif len(symbol.numAdjacent) == 2:
                symbol.gearRatio = symbol.numAdjacent[0] * symbol.numAdjacent[1]


def getSymbolCoord_X(stringSymbolLine):
    retValue = []
    
    if bool(stringSymbolLine) and isinstance(stringSymbolLine, str):
        for idx, symbol in enumerate(stringSymbolLine):
            if isSymbol(symbol):
                retValue.append(idx)
    
    return retValue

def getSymbolCoordinates(listSymbolLines):
    retValue = []
    xCoords = None

    if not isinstance(listSymbolLines, list):
        pass
    elif bool(listSymbolLines) and all(isinstance(elem, str) for elem in listSymbolLines):
        for idx, line in enumerate(listSymbolLines):
            xCoords = getSymbolCoord_X(line)
            if xCoords != None:
                for symbolCoord_X in xCoords:
                    retValue.append([idx, symbolCoord_X])
                xCoords = None

    return retValue

def checkLineNumbers(listSymbolLines, symbolCoord, y_offset):
    retValue = []
    flagLeftSearch = True
    flagTopSearch = True
    flagRightSearch = True
    tmpStringNumber = ''

    # Left search
    x_offset = -1
    while flagLeftSearch == True:
        tmpChar = listSymbolLines[symbolCoord[0] + y_offset][symbolCoord[1] + x_offset]
        if tmpChar.isnumeric():
            tmpStringNumber += tmpChar
            x_offset -= 1
        else:
            tmpStringNumber = tmpStringNumber[::-1]
            flagLeftSearch = False
    # Level search
    x_offset = 0
    while flagTopSearch == True:
        tmpChar = listSymbolLines[symbolCoord[0] + y_offset][symbolCoord[1] + x_offset]
        if tmpChar.isnumeric():
            tmpStringNumber += tmpChar
            x_offset += 1
        elif x_offset == 0 and tmpStringNumber != '':
            retValue.append(int(tmpStringNumber))
            tmpStringNumber = ''
            flagTopSearch = False
        elif tmpStringNumber != '':
            retValue.append(int(tmpStringNumber))
            flagTopSearch = False
            if x_offset >= 2:
                flagRightSearch = False
    # Right search
    x_offset = 1
    while flagRightSearch == True:
        tmpStringNumber = ''
        tmpChar = listSymbolLines[symbolCoord[0] + y_offset][symbolCoord[1] + x_offset]
        if tmpChar.isnumeric():
            tmpStringNumber += tmpChar
            x_offset += 1
        elif x_offset >= 2 and tmpStringNumber != '':
            retValue.append(int(tmpStringNumber))
            flagRightSearch = False
        else:
            print(tmpStringNumber)
            flagRightSearch = False
    return retValue

def checkPartNumbers(listSymbolLines):
    retValue = []

    if not isinstance(listSymbolLines, list):
        pass
    elif bool(listSymbolLines) and all(isinstance(elem, str) for elem in listSymbolLines):
        listSymbolCoords = getSymbolCoordinates(listSymbolLines)
        for symbolCoord in listSymbolCoords:
            for y_offset in range(-1, 1, 1):
                retValue.append(checkLineNumbers(listSymbolLines, symbolCoord, y_offset))

    return retValue

if __name__ == '__main__':
    control = input.getControlInput('2023', 'Day_3')
    control_game = Game(control)
    print('...CONTORL P1...')
    print(sum(control_game.partNumberList))
    print('...CONTORL P2...')
    control_ratio = 0
    for symbol in control_game.symbolList:
        if symbol.gearRatio != 0:
            control_ratio += symbol.gearRatio
    print(control_ratio)

    puzzle = input.getPuzzleInput('2023', 'Day_3')
    puzzle_game = Game(puzzle)
    print('...PUZZLE P1...')
    print(sum(puzzle_game.partNumberList))
    print('...PUZZLE P2...')
    puzzle_ratio = 0
    for symbol in puzzle_game.symbolList:
        if symbol.gearRatio != 0:
            puzzle_ratio += symbol.gearRatio
    print(puzzle_ratio)
    
                
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_3')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_3')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))
    
    def test_isSymbol(self):
        self.assertEqual(False, isSymbol(2))
        self.assertEqual(False, isSymbol('1'))
        self.assertEqual(False, isSymbol('.'))
        self.assertEqual(True, isSymbol('#'))

    def test_getSymbolCoord_X(self):
        self.assertEqual([], getSymbolCoord_X(1))
        self.assertEqual([], getSymbolCoord_X(['*']))
        self.assertEqual([], getSymbolCoord_X(None))
        self.assertEqual([], getSymbolCoord_X('...1......'))
        self.assertEqual([3], getSymbolCoord_X('...*......'))
        self.assertEqual([3, 5], getSymbolCoord_X('...$.*....'))

    def test_getSymbolCoordinates(self):
        self.assertEqual([], getSymbolCoordinates(None))
        self.assertEqual([], getSymbolCoordinates(1))
        self.assertEqual([], getSymbolCoordinates('...*......'))
        self.assertEqual([], getSymbolCoordinates(['467..114..', 1]))
        self.assertEqual([], getSymbolCoordinates(['467..114..']))
        self.assertEqual([], getSymbolCoordinates(['467..114..', '..........']))
        self.assertEqual([[1, 3]], getSymbolCoordinates(['467..114..', '...*......']))
        self.assertEqual([[1, 3], [1, 5]], getSymbolCoordinates(['467..114..', '...$.*....']))
        self.assertEqual([[1, 3], [3, 6]], getSymbolCoordinates(['467..114..', '...*......', '..35..633.', '......#...']))

    def test_gameListFill(self):
        game_1 = Game(['467..114..', '...*......', '..35..633.', '......#...', '617*......'])
        self.assertEqual(1, game_1.symbolList[0].y_coord)
        self.assertEqual(3, game_1.symbolList[0].x_coord)
        self.assertEqual(0, game_1.numberList[0].x_coord)
        self.assertEqual(2, game_1.numberList[0].x_coord_end)
        print(game_1.partNumberList)
        game_2 = Game(['......#...', '617*......', '.....+.58.'])
        self.assertEqual(1, game_2.symbolList[1].y_coord)
        self.assertEqual(3, game_2.symbolList[1].x_coord)
        self.assertEqual(0, game_2.numberList[0].x_coord)
        self.assertEqual(2, game_2.numberList[0].x_coord_end)
        print(game_2.partNumberList)

    def test_checkPartNumbers(self):
        self.assertEqual([], checkPartNumbers(None))
        self.assertEqual([], checkPartNumbers(''))
        self.assertEqual([], checkPartNumbers(['467..114..', 2, '..35..633.']))
        self.assertEqual([], checkPartNumbers(['467..114..', '...3......', '..35..633.']))
        #self.assertEqual([[467, 35]], checkPartNumbers(['467..114..', '...*......', '..35..633.']))
        self.assertEqual([467, 114], checkPartNumbers(['467.114..', '...*......', '..35..633.']))
