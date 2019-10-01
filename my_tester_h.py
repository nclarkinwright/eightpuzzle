from eightpuzzle import *

def main():
    
    puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])

    h1 = puzzle.h(goal)
    h2 = goal.h(goal)

    print(h1)
    print(h2)

if __name__ == '__main__':
    main()