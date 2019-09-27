import copy
import time

class Puzzle():
    """A sliding-block puzzle."""

    def __init__(self, grid):
        """Instances differ by their number configurations."""
        self.grid = copy.deepcopy(grid) # No aliasing!

    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print(number, end = ' ')
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current configuration."""
        # Open space is (y, x)
        open_space = self.find_open_space()
        possible_moves = []

        if open_space == None:
            return possible_moves

        # Check if on edge, if not, then move is possible
        if open_space[0] != 0:
            possible_moves.append('N')
        if open_space[0] != len(self.grid) - 1:
            possible_moves.append('S')
        if open_space[1] != 0:
            possible_moves.append('W')
        if open_space[0] != len(self.grid[open_space[0]]) - 1:
            possible_moves.append('E')

        return possible_moves

    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        open_space = self.find_open_space()
        y = open_space[0]
        x = open_space[1]
        moved_puzzle = Puzzle(self.grid)

        if move == 'N':
            moved_puzzle.grid[y][x] = moved_puzzle.grid[y - 1][x]
            moved_puzzle.grid[y - 1][x] = ' '
        if move == 'S':
            moved_puzzle.grid[y][x] = moved_puzzle.grid[y + 1][x]
            moved_puzzle.grid[y + 1][x] = ' '
        if move == 'W':
            moved_puzzle.grid[y][x] = moved_puzzle.grid[y][x - 1]
            moved_puzzle.grid[y][x - 1] = ' '
        if move == 'E':
            moved_puzzle.grid[y][x] = moved_puzzle.grid[y][x + 1]
            moved_puzzle.grid[y][x + 1] = ' '
        
        return moved_puzzle

    def h(self, goal):
        """Compute the distance heuristic from this instance to the goal."""
        # YOU FILL THIS IN
    
    def find_open_space(self):
        # Return tuple of location of empty space on grid (y, x)
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[y])):
                if self.grid[y][x] == ' ':
                    return (y,x)
        return None

class Agent():
    """Knows how to solve a sliding-block puzzle with A* search."""

    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
        # YOU FILL THIS IN

def main():
    """Create a puzzle, solve it with A*, and console-animate."""

    puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
    puzzle.display()

    agent = Agent()
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    path = agent.astar(puzzle, goal)

    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()

if __name__ == '__main__':
    main()