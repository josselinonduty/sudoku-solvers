"""Brute-force solving

This solver goes through each cell in order.
It fills the current cell with one available possibility, then tries to solve the new grid.
If no solution is found at one point, it backtracks and removes the last value, and tries the next one.
If it runs out of possibilities, it marks the grid unsolvable
"""

from lib import AbstractSolver, Sudoku


class BruteForceSolver(AbstractSolver):
    __solver_name__ = "Brute-force Solver"

    def _solve(self) -> bool:
        remaining_cells = self.grid.get_empty_cells()

        if not remaining_cells:
            return True

        x, y = remaining_cells[0]
        available_values = list(
            self.grid.get_complete_set()
            - self.grid.get_row_set(x)
            - self.grid.get_col_set(y)
            - self.grid.get_square_set(Sudoku.get_square_number(x, y))
        )
        available_values.sort()
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


__all__ = ["BruteForceSolver"]
