
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest

def splitCard(strLine):

    strLine = strLine.split(':')[1]
    numList = strLine.split('|')
    numList[0] = numList[0].split()
    numList[1] = numList[1].split()

    return numList

def splitLine(strLine):
    numList = []
    strCard = strLine.split(':')[0].split()[1]
    numList = splitCard(strLine)
    numList.append(strCard)
    numList.append(1)

    return numList

def multiSplitLine(listLines):
    retValue = []
    for line in listLines:
        retValue.append(splitLine(line))

    return retValue
"""
def duplicateCard(listCards, cardNum):
    for idx, card in enumerate(listCards):
        if int(card[2]) == cardNum:
            listCards.insert(idx+1, card)
            break

    return listCards  
"""
def duplicateCard(listCards, cardNum, amount):
    for idx, card in enumerate(listCards):
        if int(card[2]) == cardNum:
            card[3] += amount
            break

    return listCards  

def getWinning(numList):
    retValue = 0

    for draw in numList[0]:
        for wNum in numList[1]:
            if draw == wNum:
                if retValue == 0: retValue += 1
                else: retValue *= 2
    
    return retValue

def getMatches(numList):
    retValue = 0

    for draw in numList[0]:
        for wNum in numList[1]:
            if draw == wNum:
                retValue += 1
    
    return retValue

def collectWinnings(strlist):
    retValue = 0

    for line in strlist:
        numList = splitCard(line)
        retValue += getWinning(numList)

    return retValue

def collectCards(strlist):
    retValue = 0
    winnings = 0
    listCards = multiSplitLine(strlist)

    for idx, card in enumerate(listCards):
        winnings = getMatches(card)
        while winnings > 0:
            listCards = duplicateCard(listCards, int(card[2])+winnings, card[3])
            winnings -= 1
        
    for idx, card in enumerate(listCards):
        retValue += card[3]
        print(card)

    return retValue

if __name__ == '__main__':
    control = input.getControlInput('2023', 'Day_4')
    print('---CONTROL P1---')
    print(collectWinnings(control))

    puzzle = input.getPuzzleInput('2023', 'Day_4')
    print('---PUZZLE P1---')
    print(collectWinnings(puzzle))

    print('---CONTROL P2---')
    print(collectCards(control))

    print('---PUZZLE P2---')
    print(collectCards(puzzle))
                
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_4')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
        #print(control)
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_4')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))
    
    def test_splitCard(self):
        strInput ='Card   1: 12 34 44 | 12 33 98\n'
        self.assertEqual([['12', '34', '44'], ['12', '33', '98']], splitCard(strInput))

    def test_splitCard(self):
        strInput ='Card   1: 12 34 44 | 12 33 98\n'
        self.assertEqual([['12', '34', '44'], ['12', '33', '98'], '1'], splitLine(strInput))

    def test_getWinning(self):
        listInput = [['12', '34', '44'], ['12', '33', '98']]
        self.assertEqual(1, getWinning(listInput))
        listInput = [['12', '34', '44', '55'], ['12', '34', '44', '55']]
        self.assertEqual(8, getWinning(listInput))

    def test_collectWinnings(self):
        control = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n', 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n', 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n', 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n', 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n', 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
        self.assertEqual(13, collectWinnings(control))

    def test_duplicateCard(self):
        control = multiSplitLine(['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n', 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n', 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n'])
        output = multiSplitLine(['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n', 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n','Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n', 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n'])
        #print(control)
        self.assertEqual(output, duplicateCard(control, 2))

    def test_collectCards(self):
        control = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n', 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n', 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n', 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n', 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n', 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
        self.assertEqual(30, collectCards(control))