import os
from datetime import *

today = date.today()
currentYear = int(today.strftime("%Y"))
firstYear = 2015
yearCheck = firstYear
homedir = os.path.dirname(__file__)

while yearCheck <= currentYear:
    totalDays = 25
    dayCheck = 1
    yearPath = os.path.join(homedir, str(yearCheck))
    while dayCheck <= totalDays:
        day = str('Day_'+str(dayCheck))
        dayPath = os.path.join(yearPath, day, 'Python')
        if not os.path.exists(dayPath):
            os.makedirs(dayPath)
            print("Created DIR "+ dayPath)
            firstLine = str('crudeInput = open("AdventOfCode\\\\Input\\\\Control\\\\'+str(yearCheck)+'\\\\'+day+'.txt''"'').readlines()')
            with open(os.path.join(dayPath,str(day+'.py')), "w") as file:
                file.write(firstLine)
                print("Added "+str(day+'.py')+' with first line: '+ firstLine)
        dayCheck+=1
    yearCheck+=1