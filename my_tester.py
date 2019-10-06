from eightpuzzle import *
import unittest

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.puzzle1_start = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
        self.puzzle1_goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
        self.puzzle2 = Puzzle ([[7, 8, 5], [4, ' ', 6], [1, 2, 3]])
        self.puzzle3 = Puzzle ([[7, ' ', 5], [4, 8, 6], [1, 2, 3]])
        self.puzzle4 = Puzzle ([[7, 8, 5], [4, 2, 6], [1, ' ', 3]])
        self.puzzle5 = Puzzle ([[7, 8, 5], [' ', 4, 6], [1, 2, 3]])
        self.puzzle6 = Puzzle ([[7, 8, 5], [4, 6, ' '], [1, 2, 3]])

    def test_moves(self):
        self.assertCountEqual(self.puzzle1_start.moves(), ["N","W"])
        self.assertCountEqual(self.puzzle1_goal.moves(), ["E", "S"])
        self.assertCountEqual(self.puzzle2.moves(), ['N', 'S', 'W', 'E'])
        self.assertCountEqual(self.puzzle3.moves(), ['S', 'W', 'E'])
        self.assertCountEqual(self.puzzle4.moves(), ['N', 'W', 'E'])
        self.assertCountEqual(self.puzzle5.moves(), ['N', 'S', 'E'])
        self.assertCountEqual(self.puzzle6.moves(), ['N', 'S', 'W'])

if __name__ == '__main__':
    unittest.main(verbosity=2)