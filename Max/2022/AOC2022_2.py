import os

strategy_list = open('Source\M_AOC2022_2.txt').readlines()

# ----- 1) Write down definitions -----
# Winnings:
# Rock wins Scissors
# Paper wins Rock
# Scissors wins Paper

# Column 1:
# A -> Rock
# B -> Paper
# C -> Scissors
rock_col1 = 'A'
paper_col1 = 'B'
scissors_col1 = 'C'


# Column 2:
# X -> Rock
# Y -> Paper
# Z -> Scissors
rock_col2 = 'X'
paper_col2 = 'Y'
scissors_col2 = 'Z'

# Scores:
# Rock -> 1
# Paper -> 2
# Scissors -> 3
# ---
# Draw -> 3
# Win -> 6
score_rock = 1
score_paper = 2
score_scissors = 3
score_draw = 3
score_win = 6
score_lose = 0

# ----- 2) Calculate winnings -----
score = 0

for i in strategy_list:

    # I play rock:
    if i[2] == rock_col2:
        score += score_rock

        if i[0] == scissors_col1:
            score += score_win
        elif i[0] == rock_col1:
            score += score_draw

    # I play paper:
    elif i[2] == paper_col2:
        score += score_paper

        if i[0] == rock_col1:
            score += score_win
        elif i[0] == paper_col1:
            score += score_draw

    # I play scissors:
    elif i[2] == scissors_col2:
        score += score_scissors
        
        if i[0] == paper_col1:
            score += score_win
        elif i[0] == scissors_col1:
            score += score_draw

print("Play strategy score: {}".format(score))

# ----- 3) Play by the strategy -----
score = 0

lose_col2 = 'X'
draw_col2 = 'Y'
win_col2 = 'Z'


for i in strategy_list:

    # I play win:
    if i[2] == win_col2:
        score += score_win

        if i[0] == rock_col1:
            score += score_paper
        elif i[0] == paper_col1:
            score += score_scissors
        elif i[0] == scissors_col1:
            score += score_rock

    # I play draw:
    elif i[2] == draw_col2:
        score += score_draw

        if i[0] == rock_col1:
            score += score_rock
        elif i[0] == paper_col1:
            score += score_paper
        elif i[0] == scissors_col1:
            score += score_scissors

    # I play lose:
    elif i[2] == lose_col2:
        score += score_lose

        if i[0] == rock_col1:
            score += score_scissors
        elif i[0] == paper_col1:
            score += score_rock
        elif i[0] == scissors_col1:
            score += score_paper


print("Result strategy score: {}".format(score))

