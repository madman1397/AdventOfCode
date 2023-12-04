import os
#THIS SECTION IS STRICTLY FOR DYNAMICALLY PULLING MY CORRESPONDING INPUT TXT AND IS BASED OFF MY DIRECTORY STRUCTURING, 
#THIS WILL LIKELY NOT BE APPLICABLE TO YOU UNLESS YOU USE THE SAME STRUCTURING.
Type = 'Shayne'
Year = __file__.split(os.sep)[-4:-3][0]
Day = __file__.split(os.sep)[-3:-2][0]
print('Advent Of Code',Year,Day)
Input = [line.strip() for line in open(os.path.join(os.sep.join(__file__.split(os.sep)[:-6]),'Input',Type,Year,Day+'.txt')).readlines()]
#print(Input) #TROUBLESHOOTING PRINTOUT; PRINTS FULL INPUT INTO A LIST WITH ONE LINE PER INDEX IN STRING FORM


#takes in winning numbers and my numbers from current card,
#sorts them into separate lists, then cleans any empty space (ONLY holds nums)
def getMatches(cardDetails):
    winningNums, myNums = cardDetails.split('|')
    winningNums = [i for i in winningNums.split(' ') if i]
    myNums = [i for i in myNums.split(' ') if i]
    #searches for matches between both sets of numbers, adds each hit to list matchedNums
    matchedNums = [key for key, val in enumerate(myNums) if val in set(winningNums)]
    
    return matchedNums

#If card has ANY matches, 
#returns score as 2 to the power of x (# of matches)
def calcPts(matches):
    cScore = (2)**(len(matches)-1)
    return cScore

#spread based on matches, num of copies based on copies won (1 win on 2 cards = 2 copies for next card)
def cardCopies(matchCts):
    totalCopies = []
    while matchCts:
        idx = 0
        #print(matchCts)
        mult = matchCts[0][0]
        spread = matchCts[0][1]
        totalCopies.append(mult)
        matchCts.pop(0)
        while idx < spread:
            matchCts[idx][0] += mult
            idx += 1
    return sum(totalCopies)

def main():
    #ptsList holds total score of each card, with idx+1 referencing the corresponding card number
    ptsList = []
    #similar to ptsList, but holds match counts for each card, idx+1 refs the card number
    matchCounts = []
    for card in Input:
        cardNo = card.split(':')[0][1] #Might not be needed if stored using list index later
        #Pass scoring function only the WinningNums|MyNums portion of the card
        matches = getMatches(card.split(':')[1])
        if matches:
            points = calcPts(matches)
        else: points = 0
        ptsList.append(points)
        matchCounts.append([1,len(matches)])

    PartOne = sum(ptsList)
    print('Part One:',PartOne)

    PartTwo = cardCopies(matchCounts)
    print('Part Two:',PartTwo)

    

if __name__ == '__main__':
    main()