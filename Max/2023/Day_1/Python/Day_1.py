import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest

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
    control = input.getControlInput('2023', 'Day_1')
    numberList = getBracketNumbers(control)
    numberAdded = sum(numberList)
    print("P1 Control = " + str(numberAdded))

    puzzle = input.getPuzzleInput('2023', 'Day_1')
    numberList = getBracketNumbers(puzzle)
    numberAdded = sum(numberList)
    print("P1 Puzzle = " + str(numberAdded))

    control_P2 = input.getControlInput('2023', 'Day_1P2')
    numberList = getBracketNumbers_P2(control_P2)
    numberAdded = sum(numberList)
    print("P2 Control = " + str(numberAdded))

    numberList = getBracketNumbers_P2(puzzle)
    numberAdded = sum(numberList)
    print("P2 Puzzle = " + str(numberAdded))

################################################################

class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2023', 'Day_1')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))

    def test_control_P2_file(self):
        control_P2 = input.getControlInput('2023', 'Day_1P2')
        self.assertEqual(True, bool(control_P2) and all(isinstance(elem, str) for elem in control_P2))

    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2023', 'Day_1')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))

    def test_getNumbers(self):
        control = input.getControlInput('2023', 'Day_1')
        control_P2 = input.getControlInput('2023', 'Day_1P2')
        self.assertEqual(getBracketNumbers(control), [12, 38, 15, 77])
        self.assertEqual(getBracketNumbers_P2(control_P2), [29, 83, 13, 24, 42, 14, 76])
        