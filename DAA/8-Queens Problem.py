
N = 8
board = [[0] * N for i in range(N)]

# Check safe position
def safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1),
                    range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1),
                    range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True

# Backtracking
def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False

# Place first queen
board[0][0] = 1

if solve(1):
    print("8 Queens Solution:")
    for row in board:
        print(row)
else:
    print("No solution")


8 Queens Solution:
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
