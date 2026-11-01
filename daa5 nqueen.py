n = int(input("Enter number of queens: "))
board = [[0] * n for _ in range(n)]

def safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False

    return True

def solve(row):
    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False

board[0][0] = 1

if solve(1):
    for row in board:
        print(row)
else:
    print("Solution does not exist")