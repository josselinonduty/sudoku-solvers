import sys

from lib import AbstractSolver, Sudoku
from bruteforce import BruteForceSolver
from human import HumanSolver


def main():
    solvers: list[AbstractSolver] = [BruteForceSolver, HumanSolver]

    for Solver in solvers:
        print("=" * 20)
        print(f"Using {Solver.name()}")

        sudoku = Sudoku()
        sudoku.load_from_file("./examples/medium-2.txt")

        solver = Solver(sudoku)
        solvable = solver.solve()

        if "-v" in sys.argv:
            if solvable:
                print(sudoku)
            else:
                print("No solution found.")
        print(f"Took: {solver.duration.total_seconds()*1000:.3f}ms")


if __name__ == "__main__":
    main()
