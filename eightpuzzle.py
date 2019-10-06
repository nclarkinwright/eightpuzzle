# Nicholas Clarkin-Wright
# nc819094@wcupa.edu

import copy
import time
import heapq

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
        if open_space[0] > 0:
            possible_moves.append('N')
        if open_space[0] != len(self.grid) - 1:
            possible_moves.append('S')
        if open_space[1] > 0:
            possible_moves.append('W')
        if open_space[1] != len(self.grid[open_space[0]]) - 1:
            possible_moves.append('E')
                
        return possible_moves

    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        open_space = self.find_position(' ')
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
        # Number of moves away from goal
        blocks = [' ', 1, 2, 3, 4, 5, 6, 7, 8]
        y_moves = 0
        x_moves = 0

        for block in blocks:
            position = self.find_position(block)
            goal_position = goal.find_position(block)
            y_moves = y_moves + abs(goal_position[0] - position[0])
            x_moves = x_moves + abs(goal_position[1] - position[1])
        # Add total number of y and x moves
        return y_moves + x_moves

    def find_open_space(self):
        # Return tuple of location of empty space on grid (y, x)
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[y])):
                if self.grid[y][x] == ' ':
                    return (y,x)
        return None

    def find_position(self, block):
        # Return tuple of location of supplied block (y, x)
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[y])):
                if self.grid[y][x] == block:
                    return (y,x)
        return None

    def __eq__(self, other):
        return self.grid == other.grid

    def __ne__(self, other):
        return self.grid != other.grid

    def __hash__(self):
        return hash(str(self.grid))

class Agent():
    """Knows how to solve a sliding-block puzzle with A* search."""

    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
        # finished = set(puzzle_1, puzzle_2, etc.)
        # frontier = heapq((heuristic_value, entry count, puzzle), ...)
        # path = dict((puzzle: [moves_made_from_start]))
        finished = set()
        frontier = []
        path = dict()
        entry_value = 0

        # Stop and return no moves if start is same as goal
        if puzzle == goal:
            return []
        
        # Add start to frontier to begin loop; increment entry counter
        heapq.heappush(frontier, (puzzle.h(goal), entry_value, puzzle))
        entry_value += 1
        path.setdefault(puzzle, [])

        while (frontier != set()):
            # Get parent off frontier
            parent = heapq.heappop(frontier)
            parent_puzzle = parent[2]
            finished.add(parent_puzzle)

            # Check if parent is goal; if so stop
            if parent_puzzle == goal:
                break
            
            # Get list of possible moves from parent state
            # Loop through each possible state
            children = parent_puzzle.moves()
            for move in children:
                child = parent_puzzle.neighbor(move)
                parent_moves = path.get(parent_puzzle)
                child_moves = [*parent_moves, move]

                # Get frontier heap into usable check
                frontier_puzzle_list = [z for (x, y, z) in frontier]
                
                # Add child if not already in explored
                if child not in frontier_puzzle_list and child not in finished:
                    path.setdefault(child, child_moves)
                    heapq.heappush(frontier, (child.h(goal) + len(child_moves), entry_value, child))
                    entry_value += 1

                # Change path if current child has shorter path
                if child in path:
                    if len(path.get(child)) > len(child_moves):
                        path.setdefault(child_moves)
            
        # Return 
        return path.get(goal)
                        


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