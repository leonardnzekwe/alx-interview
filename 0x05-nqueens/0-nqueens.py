#!/usr/bin/python3
"""N Queens Module"""
import sys


def is_safe(board, row, col, N):
    """Check if placing a queen at a given position is safe."""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """Recursively find all solutions to the N Queens problem."""
    # If all queens are placed then append the solution
    if col >= N:
        solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
        return True

    # Consider this column and try placing this queen in all rows
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens_util(board, col + 1, N, solutions)

            # If placing queen in board[i][col]
            # doesn't lead to a solution, backtrack
            board[i][col] = 0


def solve_nqueens(N):
    """Solve the N Queens problem and print solutions."""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    # Sort solutions based on the position of the first queen in each row
    solutions.sort(key=lambda x: x[0][1])

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)
