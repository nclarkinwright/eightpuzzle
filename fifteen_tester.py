from eightpuzzle import *

def main():

    puzzle = Puzzle([[8, 4, 3, 11], [9, 1, 10, ' '], [12, 2, 5, 6], [7, 11, 13, 14]])
    puzzle.display()

    agent = Agent()
    goal = Puzzle([[' ', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

    path = agent.astar(puzzle, goal)

    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()

if __name__ == '__main__':
    main()