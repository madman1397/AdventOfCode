import unittest
import os
from datetime import *

stringImport_lines = """
import io
import os
import unittest
"""
stringPath_lines_control = """
control_path = os.path.abspath(control_path)
control_file = open(control_path)
control_input = control_file.readlines()
control_file.close()
"""
stringPath_lines_puzzle = """
puzzle_path = os.path.abspath(control_path)
puzzle_file = open(control_path)
puzzle_input = puzzle_file.readlines()
puzzle_file.close()
"""
stringMain = """
if __name__ == '__main__':
    pass
"""
stringUnitTest = """
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        self.assertEqual(True, isinstance(control_file, io.TextIOWrapper))
        self.assertEqual(True, control_file.closed)
        self.assertEqual(True, bool(control_input and all(isinstance(elem, str) for elem in control_input)))
    def test_puzzle_file(self):
        self.assertEqual(True, isinstance(puzzle_file, io.TextIOWrapper))
        self.assertEqual(True, puzzle_file.closed)
        self.assertEqual(True, bool(puzzle_input and all(isinstance(elem, str) for elem in puzzle_input)))
"""

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
                stringControl_path = '\ncontrol_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, os.pardir, "Input\\\\Control\\\\'+str(yearCheck)+'\\\\'+day+'.txt")'
                stringPuzzle_path = 'puzzle_path = control_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,os.pardir, os.pardir, "Input\\\\Max\\\\'+str(yearCheck)+'\\\\'+day+'.txt")'
                with open(os.path.join(dayPath,str(day+'.py')), "w") as file:
                    file.write(stringImport_lines)
                    file.write(stringControl_path)
                    file.write(stringPath_lines_control)
                    file.write(stringPuzzle_path)
                    file.write(stringPath_lines_puzzle)
                    file.write(stringMain)
                    file.write(stringUnitTest)
                    print("Added "+str(day+'.py'))
            dayCheck+=1
        yearCheck+=1

if __name__ == "__main__":
    main()



