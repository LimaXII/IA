from typing import Tuple, Callable
from advsearch.tttm.gamestate import GameState

def minimax_move(state:GameState, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    def max_value(state:GameState, max_depth, alpha, beta, player):
        if max_depth == 0 or GameState.is_terminal(state):
            return eval_func(state, player)
        
        value = float('-inf')
        for move in GameState.legal_moves(state):
            new_state = state.next_state(move)
            value = max(value, min_value(new_state, max_depth - 1, alpha, beta, player))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    
    def min_value(state:GameState, max_depth, alpha, beta, player):
        if max_depth == 0 or GameState.is_terminal(state):
            return eval_func(state, player)
        
        value = float('inf')
        for move in GameState.legal_moves(state):
            new_state = state.next_state(move)
            value = min(value, max_value(new_state, max_depth - 1, alpha, beta, player))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
    
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    player = state.player

    if max_depth == -1:
        max_depth = float('inf')
       
    for move in GameState.legal_moves(state):
        new_state = state.next_state(move)
        value = min_value(new_state, max_depth - 2, alpha, beta, player)
        if value > alpha:
            alpha = value
            best_move = move
    
    return best_move