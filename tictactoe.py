"""
Tic Tac Toe Player
"""

import math
import copy

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
    if board == initial_state():
        return X 
    
    min_player  = 0
    max_player = 0

    n = len(board)
    for i in range(n):
        for j in range(n):
            if (board[i][j] == X):
                max_player += 1
            elif board[i][j] == O:
                min_player += 1
    if (max_player > min_player):
        return O
    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_possible_actions = set()

    n = len(board)
    for i in range(n):
        for j in range(n):
            if (board[i][j] == EMPTY):
                all_possible_actions.add((i, j))
    return all_possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i, j) = action

    if i not in range(0,3) or j not in range(0, 3) or board[i][j] is not EMPTY:
        raise Exception("Move not allowed")
    result = copy.deepcopy(board)
    result[i][j] = player(board)
    return result

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = [X, O]
    n = len(board)
    for p in players:
        
        for row in range(n):
            if board[row][0] == p and board[row][1] == p and board[row][2] == p:
                return p
        
        for col in range(n):
            if board[0][col] == p and board[1][col] == p and board[2][col] == p:
                return p
        
        if board[0][0] == p and board[1][1] == p and board[2][2] == p:
            return p
        
        if board[0][2] == p and board[1][1] == p and board[2][0] == p:
            return p 
   
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    n = len(board)
    if winner(board) is not None:
        return True
    empty_count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == EMPTY:
                empty_count += 1
    return empty_count == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
  

    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    
    def min_value(board, alpha, beta):
        if (terminal(board)):
            return (None, utility(board))
        
        (min_action, min_utility) = (None, math.inf)

        for action in actions(board):
            (_, value) = max_value(result(board,action), alpha, beta)

            if value < min_utility:
                (min_action, min_utility) = (action, value)
 
            if min_utility <= alpha:
                break

            if min_utility < beta:
                beta = min_utility 

        return (min_action, min_utility)
    
    def max_value(board, alpha, beta):
        if (terminal(board)):
            return (None, utility(board))
        
        (max_action, max_utility) = (None, -math.inf)

        for action in actions(board):
            (_, value) = min_value(result(board, action), alpha, beta)

            if value > max_utility:
                (max_action, max_utility) = (action, value)

            if max_utility >= beta:
                break

            if max_utility > alpha:
                alpha = max_utility 
                
        return (max_action, max_utility)

    if player(board) == X:
        (action, _) = max_value(board, -math.inf, math.inf)
    else:
        (action, _) = min_value(board, -math.inf, math.inf)

    return action
