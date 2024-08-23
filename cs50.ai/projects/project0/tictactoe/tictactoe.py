"""
Tic Tac Toe Player
"""

import math
import numpy as np
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                X_count += 1
            if board[i][j] == "O":
                O_count += 1

    if X_count == 0 and O_count == 0:
        return "X"
    elif X_count > O_count:
        return "O"
    elif X_count == O_count:
        return "X"
    
    return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not all((0 <= action[i] <= 2 for i in range(2))):
        raise Exception("Invalid Move")

    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid Move!")
    
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    len_board = len(board)
    def checks_rows(board):
        for row in board:
            if len(set(row)) == 1 and row[0] != EMPTY:
                return row[0]
        return None
    
    def checks_diagonals(board):
        if len(set([board[i][i] for i in range(len_board)])) == 1 and board[1][1] != EMPTY:
            return board[0][0]
        if len(set([board[i][len_board - i - 1] for i in range(len_board)])) == 1 and board[1][1] != EMPTY:
            return board[0][len_board - 1]
        return None 
    
    for new_board in [board, np.transpose(board)]:
        result = checks_rows(new_board)
        if result:
            return result
    return checks_diagonals(board)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for i in range (3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == "X":
        return 1
    elif result == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == "X":
        _, action = max_value(board, -float('inf'), float('inf'))    
        
    else:
        _, action = min_value(board, -float('inf'), float('inf'))

    return action


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    
    v = -float('inf')
    best_action = None

    for action in actions(board):
        value, _ = min_value(result(board, action), alpha, beta) # We use min_value to get the min value to play as the opp for the next move
        if v < value:
            v = value
            best_action = action
        alpha = max(alpha, v)
        if v >= beta:
            break
    return v, best_action
    

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    best_action = None
    
    for action in actions(board):
        value, _ = max_value(result(board, action), alpha, beta)
        if v > value:
            v = value
            best_action = action
        beta = min(beta, v)
        if v <= alpha:
            break
    return v, best_action
