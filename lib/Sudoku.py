import numpy as np


class Sudoku:
    def __init__(self):
        self.board = np.zeros((9, 9), dtype=int)

    def load_from_array(self, arr: list[list[int]]):
        self.board = np.array(arr)

    def load_from_file(self, filename):
        """Load a sudoku board from a file

        File format:
        9x9 grid of figures, no spaces
        0 represents an empty cell
        """
        with open(filename, "r") as f:
            lines = f.readlines()
            self.board = np.array([[int(c) for c in line.strip()] for line in lines])

    @staticmethod
    def get_square_number(x: int, y: int) -> int:
        return ((x - 1) // 3) * 3 + ((y - 1) // 3) + 1

    @staticmethod
    def get_complete_set() -> set:
        return set(range(1, 10))

    def get_cell_at(self, x: int, y: int) -> int:
        return self.board[x - 1, y - 1]

    def set_cell_at(self, x: int, y: int, v: int):
        if self.is_valid_at(x, y, v):
            self.board[x - 1, y - 1] = v
        else:
            raise Exception(f"Invalid value {v} at coordinates {x},{y}")

    def set_empty_at(self, x: int, y: int):
        self.board[x - 1, y - 1] = 0

    def is_valid_at(self, x: int, y: int, v: int) -> bool:
        return not (
            v in self.get_row_set(x)
            or v in self.get_col_set(y)
            or v in self.get_square_set(Sudoku.get_square_number(x, y))
        )

    def get_row_set(self, r: int) -> set:
        return set(self.board[r - 1, :].flatten())

    def get_col_set(self, c: int) -> set:
        return set(self.board[:, c - 1].flatten())

    def get_square_set(self, s: int) -> set:
        """Order of squares

        1 2 3\n
        4 5 6\n
        7 8 9
        """

        return set(
            self.board[
                ((s - 1) // 3) * 3 : ((s - 1) // 3) * 3 + 3,
                ((s - 1) % 3) * 3 : ((s - 1) % 3) * 3 + 3,
            ].flatten()
        )

    def get_empty_cells(self) -> list:
        return list(np.add(np.argwhere(self.board == 0), 1))

    def is_solved(self) -> bool:
        for i in range(1, 10):
            if self.get_row_set(i) != Sudoku.get_complete_set():
                return False
            if self.get_col_set(i) != Sudoku.get_complete_set():
                return False
            if self.get_square_set(i) != Sudoku.get_complete_set():
                return False
        return True

    def clear(self):
        for row in range(1, 10):
            for col in range(1, 10):
                self.set_empty_at(row, col)

    def __str__(self) -> str:
        string = ""
        for row in range(1, 10):
            if row % 3 == 1:
                string += "o===o===o===o\n"

            for col in range(1, 10):
                if col % 3 == 1:
                    string += "|"

                value = self.get_cell_at(row, col)
                string += str(value if value != 0 else " ")

                if col == 9:
                    string += "|"

            string += "\n"
            if row == 9:
                string += "o===o===o===o"

        return string


__all__ = ["Sudoku"]
