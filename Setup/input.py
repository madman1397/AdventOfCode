
import io
import os
import unittest

def getControlInput(stringYear, stringDay):
    control_path = os.path.join(os.path.dirname(__file__), os.pardir, "Input/Control/" + stringYear + "/" + stringDay + ".txt")
    control_path = os.path.abspath(control_path)
    control_file = open(control_path)
    control_input = control_file.readlines()
    control_file.close()
    return control_input

def getPuzzleInput(stringYear, stringDay):
    puzzle_path = os.path.join(os.path.dirname(__file__), os.pardir, "Input/Max/" + stringYear + "/" + stringDay + ".txt")
    puzzle_path = os.path.abspath(puzzle_path)
    puzzle_file = open(puzzle_path)
    puzzle_input = puzzle_file.readlines()
    puzzle_file.close()
    return puzzle_input

if __name__ == '__main__':
    pass

class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        input = getControlInput('2023', 'Day_1')
        self.assertEqual(True, bool(input) and all(isinstance(elem, str) for elem in input))

    def test_puzzle_file(self):
        input = getPuzzleInput('2023', 'Day_1')
        self.assertEqual(True, bool(input) and all(isinstance(elem, str) for elem in input))
