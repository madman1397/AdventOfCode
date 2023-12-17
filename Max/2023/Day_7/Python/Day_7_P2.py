
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest

card_dict = {
'A' : 14,
'K' : 13,
'Q' : 12,
'J' : 1,
'T' : 10,
'9' : 9,
'8' : 8,
'7' : 7,
'6' : 6,
'5' : 5,
'4' : 4,
'3' : 3,
'2' : 2
}

rank_dict = {
    5 : 7, #FIVE_KIND
    4 : 6, #FOUR_KIND
    32 : 5, #FULL_HOUSE
    3 : 4, #THREE_KIND
    22 : 3, #TWO_PAIR
    2 : 2, #ONE_PAIR
    1 : 1, #HIGH_CARD
    0 : 0 #NOTHING
}

rank2string_dict = {
    7 : 'FIVE_KIND', #FIVE_KIND
    6 : 'FOUR_KIND', #FOUR_KIND
    5 : 'FULL_HOUSE', #FULL_HOUSE
    4 : 'THREE_KIND', #THREE_KIND
    3 : 'TWO_PAIR', #TWO_PAIR
    2 : 'ONE_PAIR', #ONE_PAIR
    1 : 'HIGH_CARD', #HIGH_CARD
    0 : 'NOTHING' #NOTHING
}

class Hand:
    cards = None
    bid = None
    cardsCntDict = None
    typeRank = None
    jokerRank = None
    strengthList = None

    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = bid
        self.cardsCntDict = {}
        self.typeRank = None
        self.strengthList = []
        self.jokerRank = None
        self.fillRank()
        self.fillStrength()

    def fillRank(self):
        for card in self.cards:
            if card in self.cardsCntDict:
                self.cardsCntDict[card] += 1
            else:
                self.cardsCntDict[card] = 1

        self.cardsCntDict = dict(sorted(self.cardsCntDict.items(), key=lambda item: item[1], reverse=True))
        first_key, first_entry  = 0, 0
        second_key, second_entry = 0, 0

        
        first_key, first_entry = list(self.cardsCntDict.items())[0]
        try:
            second_key, second_entry = list(self.cardsCntDict.items())[1]
        except:
            pass
        self.typeRank = self.determinRank(first_entry, second_entry)

        try:
            self.jokerRank = self.cardsCntDict['J']
            if first_key != 'J':
                first_entry += self.jokerRank
            elif second_entry != 0:
                first_entry += second_entry
        except:
            pass
        self.jokerRank = self.determinRank(first_entry, second_entry)

    def determinRank(self, first_entry, second_entry):
        retValue = 0
        if first_entry == 2 and second_entry == 2:
            retValue = rank_dict[22]
        elif first_entry == 3 and second_entry == 2:
                retValue = rank_dict[32]
        else:
            retValue = rank_dict[first_entry]
        return retValue

    def fillStrength(self):
        for card in self.cards:
            self.strengthList.append(card_dict[card])

def sortHands(hands):
    sorted_hands = sorted(hands, key=lambda hand: (hand.jokerRank, *hand.strengthList), reverse=False) #hand.typeRank,
    for hand in sorted_hands:
            #print("Hand:", hand.cards, "JokerRank:", rank2string_dict[hand.jokerRank], "HandStrenght:", hand.strengthList) #"NormalRank:", rank2string_dict[hand.typeRank],
            pass
    return sorted_hands

def getSolution(listInput):    
    solution = 0
    hands = []
    for strInput in listInput:
        cards, bid = strInput.split()
        hands.append(Hand(cards, bid))
    hands = sortHands(hands)
    for idx, hand in enumerate(hands):
        solution += int(hand.bid) * (idx+1)
    return (solution)

if __name__ == '__main__':
    control = input.getControlInput('2023', 'Day_7')
    print("Control P2:", getSolution(control))
    puzzle = input.getPuzzleInput('2023', 'Day_7')
    print("Puzzle P2:", getSolution(puzzle))
    
                
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_7')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_7')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))

    def test_classHand(self):
        listInput = ["32T3K 765\n", "T55J5 684"]
        hands = []
        for strInput in listInput:
            cards, bid = strInput.split()
            hands.append(Hand(cards, bid))

        self.assertEqual("32T3K", hands[0].cards)
        self.assertEqual("765", hands[0].bid)
        self.assertEqual(2, hands[0].cardsCntDict['3'])
        self.assertEqual(1, hands[0].cardsCntDict['2'])
        for key, value in hands[0].cardsCntDict.items():
            #print(f"{key}: {value}")
            pass
        self.assertEqual([3, 2, 10, 3, 13], hands[0].strengthList)
        self.assertEqual('ONE_PAIR' ,rank2string_dict[hands[0].typeRank])
        self.assertEqual('THREE_KIND' ,rank2string_dict[hands[1].typeRank])
        
    def test_sortHands(self):
        control = input.getControlInput('2023', 'Day_7')
        hands = []
        for strInput in control:
            cards, bid = strInput.split()
            hands.append(Hand(cards, bid))
        hands = sortHands(hands)
        for hand in hands:
            #print(rank2string_dict[hand.typeRank], hand.strengthList)
            pass