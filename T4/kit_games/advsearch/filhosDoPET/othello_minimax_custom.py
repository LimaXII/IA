import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, 4, evaluate_custom)
    #return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """

    opponent = Board.opponent(player)
    player_points = 0
    opponent_points = 0
    board = state.get_board()
    size_board = len(board.tiles)

    for row in range(size_board):
        for col in range(size_board):
            if board.tiles[row][col] == player:
                player_points += calculate_tile_value(row, col, size_board, state)
            elif board.tiles[row][col] == opponent:
                opponent_points += calculate_tile_value(row, col, size_board, state)
                 
    return player_points/opponent_points * 100

def calculate_tile_value(row, col, size_board, state):
        value = 1

        # Adicionar valor às peças nas bordas
        if row == 0 or row == size_board - 1 or col == 0 or col == size_board - 1:
            value += 1

        # Adicionar valor às peças estáveis nas diagonais
        if (row == 0 and col == 0) or (row == 0 and col == size_board - 1) or \
            (row == size_board - 1 and col == 0) or (row == size_board - 1 and col == size_board - 1):
            value += 2

        # Avaliar mobilidade considerando o número de jogadas possíveis
        if state.is_terminal():
            return value
        mobility = len(state.board.legal_moves(state.player))
        value += mobility * 0.2
        return value