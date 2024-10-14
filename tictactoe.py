import math
import random

BOARD_SIZE = 3
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * (BOARD_SIZE * 4 - 1))

def check_winner(board, player):
    for row in range(BOARD_SIZE):
        if all(board[row][col] == player for col in range(BOARD_SIZE)):
            return True
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True
    return False

def get_empty_positions(board):
    return [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == EMPTY]

def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return -10 + depth
    if check_winner(board, PLAYER_O):
        return 10 - depth
    if not get_empty_positions(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (r, c) in get_empty_positions(board):
            board[r][c] = PLAYER_O
            score = minimax(board, depth + 1, False)
            board[r][c] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (r, c) in get_empty_positions(board):
            board[r][c] = PLAYER_X
            score = minimax(board, depth + 1, True)
            board[r][c] = EMPTY
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for (r, c) in get_empty_positions(board):
        board[r][c] = PLAYER_O
        score = minimax(board, 0, False)
        board[r][c] = EMPTY
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

def player_move(board):
    while True:
        try:
            r, c = map(int, input("Enter your move (row and column): ").split())
            if board[r][c] == EMPTY:
                board[r][c] = PLAYER_X
                break
            else:
                print("Invalid move! Cell is already occupied.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column as two integers from 0 to 2.")

def play_game():
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    print("Tic-Tac-Toe Game Started!")
    print_board(board)
    
    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, PLAYER_X):
            print("Congratulations! You win!")
            break
        if not get_empty_positions(board):
            print("It's a tie!")
            break
        
        print("AI is making a move...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = PLAYER_O
            print_board(board)
            if check_winner(board, PLAYER_O):
                print("AI wins!")
                break
            if not get_empty_positions(board):
                print("It's a tie!")
                break

if __name__ == "__main__":
    play_game()
