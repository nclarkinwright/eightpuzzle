from eightpuzzle import *
import unittest

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.puzzle1_start = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
        self.puzzle1_goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
        self.puzzle2 = Puzzle ([[7, 8, 5], [4, ' ', 6], [1, 2, 3]])

    def test_moves(self):
        self.assertCountEqual(self.puzzle1_start.moves(), ["N","W"])
        self.assertCountEqual(self.puzzle1_goal.moves(), ["E", "S"])
        self.assertCountEqual(self.puzzle2.moves(), ['N', 'S', 'W', 'E'])

if __name__ == '__main__':
    unittest.main(verbosity=2)