from datetime import datetime
from .Sudoku import Sudoku


class AbstractSolver:
    __solver_name__ = "Abstract Solver"

    def __init__(self, grid: Sudoku):
        self.grid = grid
        self.__start_at = None
        self.__end_at = None
        self.duration = None

    def _solve(self) -> bool:
        raise NotImplementedError("Method solve not implemented")

    def solve(self) -> bool:
        self.__start_at = datetime.now()
        solvable = self._solve()
        self.__end_at = datetime.now()

        self.duration = self.__end_at - self.__start_at
        return solvable

    @staticmethod
    def name() -> str:
        return AbstractSolver.__solver_name__


__all__ = ["AbstractSolver"]
