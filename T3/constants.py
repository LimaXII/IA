# Conjunto de elementos possíveis
POSSIBLE_SET = {'1', '2', '3', '4', '5', '6', '7', '8', '_'}

RIGHT = "direita"
LEFT = "esquerda"
UP = "acima"
DOWN = "abaixo"

FINAL_STATE = "12345678_"
FINAL_BOARD = {'1' : [0,0], '2' : [1,0], '3' : [2,0],
               '4' : [0,1], '5' : [1,1], '6' : [2,1],
               '7' : [0,2], '8' : [1,2], '_' : [2,2]}

UNDERLINE_CHAR = '_'

ERROR_MESSAGE = "INVALID STATE"

# Estruturas de dados para implementar o DFS e BFS
QUEUE = 0
STACK = -1