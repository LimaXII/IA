import constants
from math import sqrt

def hamming_cost(node_state: str) -> int:
    hamming_cost = 0
    for i in range(9):
        if node_state[i] != constants.FINAL_STATE[i]:
            hamming_cost += 1
    return hamming_cost


def manhattan_cost(node_state: str) -> int:    
    board = {}
    for i in range(9):
        board[node_state[i]] = [i % 3, i // 3]
        
    manhattan_cost = 0
    for key in board.keys():
        manhattan_cost += abs(constants.FINAL_BOARD[key][0] - board[key][0]) + abs(constants.FINAL_BOARD[key][1] - board[key][1])
    
    return manhattan_cost


def eucledian_cost(node_state: str) -> int:    
    board = {}
    for i in range(9):
        board[node_state[i]] = [i % 3, i // 3]
        
    eucledian_cost = 0
    for key in board.keys():
        eucledian_cost += sqrt((constants.FINAL_BOARD[key][0] - board[key][0])**2 + (constants.FINAL_BOARD[key][1] - board[key][1])**2)
    
    return eucledian_cost
