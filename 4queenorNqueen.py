def print_board(board):
    for row in board:
        print(' '.join(['Q' if cell else '.' for cell in row]))
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = True
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = False
    return False

def solve_4_queens():
    board = [[False for _ in range(4)] for _ in range(4)]
    if solve_n_queens(board, 0):
        print("Solution found:")
        print_board(board)
    else:
        print("No Solution Exists")

if __name__ == "__main__":
    solve_4_queens()
