#!/usr/bin/python3
import sys


class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def solve(self):
        self.backtrack(0)
        return self.solutions

    def backtrack(self, row):
        if row == self.n:
            self.add_solution()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.backtrack(row + 1)
                self.board[row] = -1

    def is_safe(self, row, col):
        for r in range(row):
            if (
                self.board[r] == col
                or self.board[r] - col == r - row
                or self.board[r] - col == row - r
            ):
                return False
        return True

    def add_solution(self):
        solution = []
        for row in range(self.n):
            solution.append([row, self.board[row]])
        self.solutions.append(solution)

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    """Check number of arguments"""
    number_of_argument = len(sys.argv)
    if number_of_argument != 2:
        print("Usage: nqueens N")
        exit(1)

    """Check if N is not an integer"""
    N = sys.argv[1]
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        exit(1)

    """Check if N is smaller than 4"""
    if N < 4:
        print("N must be at least 4")
        exit(1)

    # Solve the N-queens problem
    n_queens = NQueens(N)
    solutions = n_queens.solve()

    """Print solution"""
    print_solutions(solutions)
