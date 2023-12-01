import io
import os
import unittest

control_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,os.pardir, os.pardir, "Input\\Control\\2023\\Day_1.txt")
control_path = os.path.abspath(control_path)
control_file = open(control_path)
control_input = control_file.readlines()
control_file.close()

control_P2_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,os.pardir, os.pardir, "Input\\Control\\2023\\Day_1P2.txt")
control_P2_path = os.path.abspath(control_P2_path)
control_P2_file = open(control_P2_path)
control_P2_input = control_P2_file.readlines()
control_P2_file.close()

puzzle_path = control_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,os.pardir, os.pardir, "Input\\Max\\2023\\Day_1.txt")
puzzle_path = os.path.abspath(control_path)
puzzle_file = open(control_path)
puzzle_input = puzzle_file.readlines()
puzzle_file.close()

def checkCalibrationLine(cal_line):
    retValue = ""

    for cal in cal_line:
        if cal.isnumeric():
            retValue = cal
            break

    return retValue

def getBracketNumbers(calibration_list):
    cal_first = ""
    cal_last = ""
    retList = []

    for calibration_line in calibration_list:
        cal_first = checkCalibrationLine(calibration_line)
        cal_last = checkCalibrationLine(reversed(calibration_line))
        try:
            number = int(cal_first+cal_last)
        except ValueError:
            number = 0
        retList.append(number)
        cal_first = ""
        cal_last = ""

    return retList

def checkCalibrationLine_P2(cal_line, reverse = False):
    retValue = ""
    if reverse == False:
        stringNumbersList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if reverse == True:
        stringNumbersList = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
    stringLine = ""

    for cal in cal_line:
        stringLine += cal
        for idx, num in enumerate(stringNumbersList):
            if num in stringLine:
                retValue = str(idx+1)
                break
        if retValue != "":
            break
        elif cal.isnumeric():
            retValue = cal
            break

    return retValue

def getBracketNumbers_P2(calibration_list):
    cal_first = ""
    cal_last = ""
    retList = []

    for calibration_line in calibration_list:
        cal_first = checkCalibrationLine_P2(calibration_line)
        cal_last = checkCalibrationLine_P2(reversed(calibration_line), True)

        try:
            number = int(cal_first+cal_last)
        except ValueError:
            number = 0
        retList.append(number)
        cal_first = ""
        cal_last = ""

    return retList

if __name__ == '__main__':
    numberList = getBracketNumbers(control_input)
    numberAdded = sum(numberList)
    print("P1 Control = " + str(numberAdded))

    numberList = getBracketNumbers(puzzle_input)
    numberAdded = sum(numberList)
    print("P1 Puzzle = " + str(numberAdded))

    numberList = getBracketNumbers_P2(control_P2_input)
    numberAdded = sum(numberList)
    print("P2 Control = " + str(numberAdded))

    numberList = getBracketNumbers_P2(puzzle_input)
    numberAdded = sum(numberList)
    print("P2 Puzzle = " + str(numberAdded))

class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        self.assertEqual(True, isinstance(control_file, io.TextIOWrapper))
        self.assertEqual(True, control_file.closed)
        self.assertEqual(True, bool(control_input and all(isinstance(elem, str) for elem in control_input)))

    def test_control_P2_file(self):
        self.assertEqual(True, isinstance(control_P2_file, io.TextIOWrapper))
        self.assertEqual(True, control_P2_file.closed)
        self.assertEqual(True, bool(control_P2_input and all(isinstance(elem, str) for elem in control_P2_input)))

    def test_puzzle_file(self):
        self.assertEqual(True, isinstance(puzzle_file, io.TextIOWrapper))
        self.assertEqual(True, puzzle_file.closed)
        self.assertEqual(True, bool(puzzle_input and all(isinstance(elem, str) for elem in puzzle_input)))

    def test_getNumbers(self):
        self.assertEqual(getBracketNumbers(control_input), [12, 38, 15, 77])
        self.assertEqual(getBracketNumbers_P2(control_P2_input), [29, 83, 13, 24, 42, 14, 76])
        