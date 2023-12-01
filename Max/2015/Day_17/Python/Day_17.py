
import sys
sys.path.insert(1, 'Setup')
import input
import io
import unittest
                
if __name__ == '__main__':
    pass
    
                
################################################################
class TestStringMethods(unittest.TestCase):

    def test_control_file(self):
        control = input.getControlInput('2015', 'Day_17')
        self.assertEqual(True, bool(control) and all(isinstance(elem, str) for elem in control))
    def test_puzzle_file(self):
        puzzle = input.getPuzzleInput('2015', 'Day_17')
        self.assertEqual(True, bool(puzzle) and all(isinstance(elem, str) for elem in puzzle))
                