strategyGuide = open("Input\Shayne\\2022\Day_2.txt").readlines()

#define an empty chart that will store each rounds point result as the tournament is played
pointChart = []
altPointChart = []

#defines what what letters to look for when adding bonus triggers. Uses the matching index+1 (ex; 0+1 for X(rock)) to attribute point value
bonusTrigger = ['X','Y','Z']

def translateMove(move):
    if move == 'A' or move == 'X':
        translatedMove = 'Rock'
    elif move == 'B' or move == 'Y':
        translatedMove = 'Paper'
    elif move == 'C' or move == 'Z':
        translatedMove = 'Scissors'
    return translatedMove

#Function takes a list of two moves (left[0]=opponent, right[1]=you) and checks for win/draw/loss conditions on your side.
def roundResult(currentRound):
    if currentRound[0] == 'Rock' and currentRound[1] == 'Paper' or currentRound[0] == 'Paper' and currentRound[1] == 'Scissors' or currentRound[0] == 'Scissors' and currentRound[1] == 'Rock':
        #Win condition met
        return "Win"
    elif currentRound[0] == currentRound[1]:
        #Draw condition met
        return "Draw"
    elif currentRound[0] == 'Paper' and currentRound[1] == 'Rock' or currentRound[0] == 'Scissors' and currentRound[1] == 'Paper' or currentRound[0] == 'Rock' and currentRound[1] == 'Scissors':
        #Loss condition met
        return "Loss"
        
#Takes opponents play, and suggested round result (X = Lose, Y = Draw, Z = Win), and finds the proper play for you. Returns raw readout with the new play in formatting identical to part 1 
# (X = Rock, Y = Paper, Z = Scissors) so these may later be translated and parsed using the same functions.
def newResult(temp):
    theirOptions = ["A", "B", "C"]
    yourOptions = ["X", "Y", "Z"]

    theyPlay = theirOptions.index(temp[0])
    rollAmount = int(yourOptions.index(temp[1])-1)
    rolledList = yourOptions[rollAmount:] + yourOptions[:rollAmount]
    altRound = [temp[0], rolledList[theyPlay]]
    return altRound
        
#Calculates bonus points based on your choice, then points based on the result of the round. Returns sum of all points earned
def calculatePoints(move):
    bonus = int(bonusTrigger.index(move[1])+1)
    if move[0] == "Win":
        score = int(6)
    elif move[0] == "Draw":
        score = int(3)
    else:
        score = 0
    return int(bonus + score)

def processRound(RAW):
    translated = [translateMove(RAW[0]), translateMove(RAW[1])]
    result = roundResult(translated)
    roundPoints = calculatePoints([result, RAW[1]])
    return roundPoints

for i in strategyGuide:

    currentRound = [i[0], i[2]]
    altRound = newResult(currentRound)
    pointChart.append(processRound(currentRound))
    altPointChart.append(processRound(altRound))
print(sum(pointChart))
print(sum(altPointChart))