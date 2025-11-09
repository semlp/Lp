def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

if __name__ == "__main__":
    n = int(input("Enter number of queens: "))
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)

    print(f"\nTotal solutions found for {n}-Queens: {len(solutions)}")

    if solutions:
        show = int(input(f"\n How many solutions(1 to {len(solutions)}) do you want to see? "))
        show = min(show, len(solutions))
        for i in range(show):
            print(f"\nSolution {i + 1}:")
            print_board(solutions[i])
    else:
        print("No solution exists for given N.")
