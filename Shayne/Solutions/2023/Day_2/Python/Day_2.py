import os
#Define input, and strip data
Type = 'Shayne'
Input = [line.strip() for line in open(os.path.join(os.path.sep.join(__file__.split(os.path.sep)[:6]),'Input',Type,__file__.split(os.sep)[-4],(__file__.split(os.sep)[-1]).split('.')[0]+'.txt')).readlines()]

P1PossibleGames = []
P1ImpossibleGames = []

#defines the pull limits per color for part 1
P1Limits = {'red':12,'green':13,'blue':14}
P2Powers = []
#Iterate over individual games one by one
for game in Input:
    #split Game ID and colors pulled so data can be easier manipulated
    game = game.split(':')
    #remove 'Game' text from Game ID and store the integer alone as the ID value
    gameID = int(game[0].split(' ')[1])
    #defines the game data and assigns it to var 'game' / removes whitespace
    game = game[1].replace(' ','')
    #finds subset (caled subgroups to refrain from later using 'set' as a var) within current game, separates them into their own sublists
    subGames = [pull.split(',') for pull in game.split(';')]
    """ print('game',gameID,subGames) """ #this print for troubleshooting only
    gameRuleCheck = []
    P2Counts = {'red':None,'green':None,'blue':None}
    for group in subGames:
        subRuleCheck = []
        for pull in group:
            #identify color and count of each individual pull
            count = int(''.join(filter(str.isdecimal,pull)))
            color = ''.join(filter(str.isalpha,pull))
            #get cound limit of current color
            limit = P1Limits.get(color)
            """ print(count,color,limit) """ #this print for troubleshooting only
            if count>limit:
                subRuleCheck.append(False)
            else:
                subRuleCheck.append(True)
            if P2Counts.get(color) == None or count > P2Counts.get(color):
                P2Counts[color] = count
        if False in subRuleCheck:
            gameRuleCheck.append(False)
        else: gameRuleCheck.append(True)
    if False in gameRuleCheck: P1ImpossibleGames.append(gameID)
    else: P1PossibleGames.append(gameID)
    P2Counts = [x for x in P2Counts.values() if isinstance(x, int)]
    if P2Counts:
        product = 1
        for i in P2Counts:
            product *= i
        P2Powers.append(product)

        

PartOne = sum(P1PossibleGames)
print("Part One =",PartOne)

PartTwo = sum(P2Powers)
print("Part Two=",PartTwo)