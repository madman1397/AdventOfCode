import unittest
import os
from datetime import *

def userFolder(userName):
    userPath = os.path.join(os.path.dirname(__file__), os.pardir, userName)
    userPath = os.path.abspath(userPath)
    if not os.path.exists(userPath):
        os.makedirs(userPath)
    return userPath

def main():
    firstYear = 2015
    totalDays = 25

    today = date.today()
    currentYear = int(today.strftime("%Y"))
    yearCheck = firstYear
    inputData = input("Enter user dir name for setup (blank for current dir): ")

    if inputData == "":
        homedir = os.path.dirname(__file__)
    else:
        homedir = userFolder(inputData)

    while yearCheck <= currentYear:
        dayCheck = 1
        yearPath = os.path.join(homedir, str(yearCheck))
        while dayCheck <= totalDays:
            day = str('Day_'+str(dayCheck))
            dayPath = os.path.join(yearPath, day, 'Python')
            if not os.path.exists(dayPath):
                os.makedirs(dayPath)
                print("Created DIR "+ dayPath)
                stringImport_lines = """
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest
                """
                stringMain = """
if __name__ == '__main__':
    pass
                """
                stringUnitTest = """
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('""" + str(yearCheck) + """', '""" + day + """')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('""" + str(yearCheck) + """', '""" + day + """')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))
                """
                with open(os.path.join(dayPath,str(day+'.py')), "w") as file:
                    file.write(stringImport_lines)
                    file.write(stringMain)
                    file.write(stringUnitTest)
                    print("Added "+str(day+'.py'))
            dayCheck+=1
        yearCheck+=1

if __name__ == "__main__":
    main()



