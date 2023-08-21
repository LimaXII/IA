import random
from numpy import log as ln
from typing import Tuple

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

def uct(state, state_wins):   
    if state.visit_count[state] != 0:
        ratio = state_wins[state]/state.visit_count
        uct_score = ratio + 2 * (2 * ln(state.visit_count)/state.visit_count)
    else:
        uct_score = 'inf'
    return uct_score

def backpropagation(state, result, state_wins, root):
    root.visit_count.update[state] += 1
    if result == 1:
        state_wins[state] += 1
    state = root
    root.visit_count.update[state] += 1
    if result == 1:
        state_wins[state] += 1
    return state

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    root = state
    state_wins = [[0]]

    for _ in range(0, 100):
        if not state.is_terminal():
            if state.visit_count[state] == 0:
                next_state = random.choice(list(state.legal_moves()))
            else:
                for child in state.legal_moves():
                    score = uct(child, state_wins)
                    if max_score < score:
                        max_score, next_state = score, child
            state = state.next_state(next_state)
        else:
            result = state.winner()
            if result == None:
                # Empate
                state = backpropagation(state, 0, state_wins, root)
                pass
            elif result == state.player:
                # Vitória
                state = backpropagation(state, 1, state_wins, root)
                pass
            else:
                # Derrota
                state = backpropagation(state, -1, state_wins, root)
                pass
    
    for child in state.legal_moves():
        score = uct(child, state_wins)
        if max_score < score:
            max_score, best_move = score, child
    return best_move