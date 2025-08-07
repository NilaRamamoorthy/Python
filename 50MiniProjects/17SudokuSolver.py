import csv, time
from functools import wraps

# Decorator to measure solving time
def timeit(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        t0 = time.time()
        result = func(self, *args, **kwargs)
        print(f"Solved in {time.time() - t0:.3f} seconds")
        return result
    return wrapper

# Custom exception for invalid input
class InvalidGridError(Exception):
    pass

class Sudoku:
    def __init__(self, grid):
        # Expect grid as list of lists 9×9
        if len(grid) != 9 or any(len(row) != 9 for row in grid):
            raise InvalidGridError("Grid must be 9×9")
        self.grid = grid

    def __str__(self):
        return "\n".join(" ".join(str(n or '.') for n in row) for row in self.grid)

    def possible_numbers(self, row, col):
        """Generator yielding valid candidates for a cell."""
        used = set(self.grid[row]) | {self.grid[r][col] for r in range(9)}
        br, bc = 3*(row//3), 3*(col//3)
        used |= {self.grid[r][c] for r in range(br, br+3) for c in range(bc, bc+3)}
        for num in range(1, 10):
            if num not in used:
                yield num

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def is_valid_move(self, row, col, num):
        return num in self.possible_numbers(row, col)

    @timeit
    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True
        r, c = empty
        for num in self.possible_numbers(r, c):
            self.grid[r][c] = num
            if self.solve():
                return True
            self.grid[r][c] = 0
        return False

    @classmethod
    def load_from_csv(cls, filename):
        grid = []
        with open(filename, newline='') as f:
            for row in csv.reader(f):
                if len(row) != 9:
                    raise InvalidGridError("Each CSV row must have 9 values")
                grid.append([int(x) if x != '' else 0 for x in row])
        return cls(grid)
puzzle = Sudoku.load_from_csv("sudoku_puzzle.csv")
if puzzle.solve():
    print(puzzle)
else:
    print("No solution found")
