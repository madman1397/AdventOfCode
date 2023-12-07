import os
# THIS SECTION IS STRICTLY FOR DYNAMICALLY PULLING MY CORRESPONDING INPUT TXT AND IS BASED OFF MY DIRECTORY STRUCTURING, 
# THIS WILL LIKELY NOT BE APPLICABLE TO YOU UNLESS YOU USE THE SAME STRUCTURING.
Type = 'Control'
Year = __file__.split(os.sep)[-4:-3][0]
Day = __file__.split(os.sep)[-3:-2][0]
print('Advent Of Code',Year,Day)
Input = [line.strip() for line in open(os.path.join(os.sep.join(__file__.split(os.sep)[:-6]),'Input',Type,Year,Day+'.txt')).readlines()]
#print(Input) #TROUBLESHOOTING PRINTOUT; PRINTS FULL INPUT INTO A LIST WITH ONE LINE PER INDEX IN STRING FORM
'''----------------------------------------------------------------------------------------------------'''
# speed = 1mm/ms per 1ms button held - where time button held is subtracted from total race time (less time for movement), and acceleration is instant.
# - 20ms, 10 held, 10 moved = 10mm/ms*10 = 1000mm
# - 20ms, 9 held, 11 moved = 9mm/ms*11 = 990mm
# - 20ms, 11 held, 9 moved = 11mm/ms*9 = 990mm
# Holding the button for exactly half of the total race (or either of the two integer times closest to half)
#   time will always return the best possible distance given any race time alotment. 

# Part One Goal: return number of ways (seconds held) that beat the opponents score in each race, then get product of all values.
# - could be solved by reversing the acceleration function to return opponents +/- deviation from half race time... 
#   all deviation values less than this would result in a win and can be recorded.
#Reversed function = 
'''----------------------------------------------------------------------------------------------------'''
# Format the input file by converting each line into a list of integers.
# Args: file (file): The input file to be formatted.
def formatInput(file):
    file = [[int(i) for i in line.split()[1:] if i and i.isdigit()] for line in file]
    races = list(zip(*file))
    return races

# Take in: race time (x) and opponent score (y) as [x,y] - Return: button hold times for opponent as deviation from half race time
def opponentDeviation(raceStats):
    print(raceStats)


def main():
    raceList = formatInput(Input)
    winMargin = []
    for race in raceList:
        time = race[0]
        opScore = race[1]
        opDev = opponentDeviation(race)
        print(time,opScore)


if __name__ == '__main__':
    main()