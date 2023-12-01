
import io
import os
import unittest

control_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, os.pardir, "Input\\Control\\2019\\Day_13.txt")
control_path = os.path.abspath(control_path)
control_file = open(control_path)
control_input = control_file.readlines()
control_file.close()
puzzle_path = control_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,os.pardir, os.pardir, "Input\\Max\\2019\\Day_13.txt")
puzzle_path = os.path.abspath(control_path)
puzzle_file = open(control_path)
puzzle_input = puzzle_file.readlines()
puzzle_file.close()

if __name__ == '__main__':
    pass

class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        self.assertEqual(True, isinstance(control_file, io.TextIOWrapper))
        self.assertEqual(True, control_file.closed)
        self.assertEqual(True, bool(control_input and all(isinstance(elem, str) for elem in control_input)))
    def test_puzzle_file(self):
        self.assertEqual(True, isinstance(puzzle_file, io.TextIOWrapper))
        self.assertEqual(True, puzzle_file.closed)
        self.assertEqual(True, bool(puzzle_input and all(isinstance(elem, str) for elem in puzzle_input)))
