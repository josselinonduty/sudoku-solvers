"""Human solving

This solver uses a human approach for solving sudoku.
It looks for the easiest cells to complete. That is to say, the cell with least number of possibilities.
When it has more than 1 possibility, it tries them all.

It behaves like a Wave Function Collapse algorithm, with the number of possibilites beeing the entropy.
It costs more to compute but reduces the number of computations the more pre-filled cells there are.
"""

from lib import AbstractSolver, Sudoku


def get_degree(grid: Sudoku, x: int, y: int) -> int:
    available_values = list(
        grid.get_complete_set()
        - grid.get_row_set(x)
        - grid.get_col_set(y)
        - grid.get_square_set(Sudoku.get_square_number(x, y))
    )
    return len(available_values)


def get_min_degree_cell(
    grid: Sudoku, remaining: list[tuple[int, int]]
) -> tuple[int, int]:
    min_degree = 100
    min_cell = None

    for cell in remaining:
        degree = get_degree(grid, cell[0], cell[1])
        if degree < min_degree:
            min_degree = degree
            min_cell = cell

        if degree == 1:
            break

    return min_cell


class HumanSolver(AbstractSolver):
    __solver_name__ = "Human Solver"

    def _solve(self) -> bool:
        remaining_cells = self.grid.get_empty_cells()

        if not remaining_cells:
            return True

        x, y = get_min_degree_cell(self.grid, remaining_cells)
        available_values = list(
            self.grid.get_complete_set()
            - self.grid.get_row_set(x)
            - self.grid.get_col_set(y)
            - self.grid.get_square_set(Sudoku.get_square_number(x, y))
        )
        available_values
        if not available_values:
            return False

        for v in available_values:
            self.grid.set_cell_at(x, y, v)

            solved = self._solve()
            if solved:
                return True
            else:
                self.grid.set_empty_at(x, y)

        return False


__all__ = ["HumanSolver"]
