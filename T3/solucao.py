from typing import Iterable, Set, Tuple
import help
from heapq import heapify, heappush, heappop

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """        
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.custo_estimado = 0
        
    # override the comparison operator
    def __lt__(self, nxt):
        return self.custo_estimado < nxt.custo_estimado


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # Conjunto de elementos possíveis    
    possible_set = {'1', '2', '3', '4', '5', '6', '7', '8', '_'}
    
    # Verifica se o estado/string possui 9 caracteres
    if len(estado) != 9:
        return "ERRO"
    # Verifica se o estado/string não repete elementos
    if len(set(estado)) != 9:
        return "ERRO"
    # Verifica se os caracteres do estado/string estão no conjunto de elementos possíveis
    for char in estado:
        if char not in possible_set:
            return "ERRO"

    underline_position = estado.find('_')
    successor_set = set()
    
    # Pode mover pra cima
    if underline_position - 3 >= 0:
        successor_set.add((
            "acima",
            help.swap_string(estado, underline_position, underline_position - 3)
        ))
    # Pode mover pra baixo
    if underline_position + 3 <= 8:
        successor_set.add((
            "abaixo",
            help.swap_string(estado, underline_position, underline_position + 3)
        ))
    # Pode mover pra direita
    if (underline_position + 1) % 3 != 0:
        successor_set.add((
            "direita",
            help.swap_string(estado, underline_position, underline_position + 1)
        ))
    # Pode mover pra esquerda
    if underline_position % 3 != 0:
        successor_set.add((
            "esquerda",
            help.swap_string(estado, underline_position, underline_position - 1)
        ))
        
    return successor_set
    

def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # Conjunto de filhos
    node_set = set()
    # Verifica filhos
    successors = sucessor(nodo.estado)
    # Atualiza lista de filhos
    for succ in successors:
        node_set.add(Nodo(succ[1], nodo, succ[0], 1 + nodo.custo))
    return node_set


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    initial_node = Nodo(estado, None, None, 0)
    explored = set()
    border = [initial_node]
    heapify(border)
    
    while (border):    
        current_node = heappop(border) #função que retira o nodo com o menor custo estimado
        
        if current_node.estado == "12345678_": #final state
            path = []
            while(current_node.pai is not None):
                path.insert(0, current_node.acao)
                current_node = current_node.pai
            return path #lista de ações que leva ao estado final
        if current_node.estado not in explored:
            explored.add(current_node.estado)
            son_node_set = expande(current_node)
            for node in son_node_set:
                node.custo_estimado = node.custo + hamming_cost(node)
                heappush(border, node)
            
    return None

# ADICIONAL
def hamming_cost(node: Nodo) -> int:
    node_state = node.estado
    final_state = '12345678_'
    hamming_cost = 0
    for i in range(9):
        if node_state[i] != final_state[i]:
            hamming_cost += 1
    return hamming_cost 


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    initial_node = Nodo(estado, None, None, 0)
    explored = set()
    border = [initial_node]
    heapify(border)
    
    while (border):    
        current_node = heappop(border) #função que retira o nodo com o menor custo estimado
        
        if current_node.estado == "12345678_": #final state
            path = []
            while(current_node.pai is not None):
                path.insert(0, current_node.acao)
                current_node = current_node.pai
            return path #lista de ações que leva ao estado final
        if current_node.estado not in explored:
            explored.add(current_node.estado)
            son_node_set = expande(current_node)
            for node in son_node_set:
                node.custo_estimado = node.custo + manhattan_cost(node)
                heappush(border, node)
            
    return None

# ADICIONAL
def manhattan_cost(node: Nodo) -> int:
    node_state = node.estado
    final_board = {'1' : [0,0], '2' : [1,0], '3' : [2,0],
                   '4' : [0,1], '5' : [1,1], '6' : [2,1],
                   '7' : [0,2], '8' : [1,2], '_' : [2,2]}
    
    board = {}
    for i in range(9):
        board[node_state[i]] = [i % 3, i // 3]
        
    manhattan_cost = 0
    for key in board.keys():
        manhattan_cost += abs(final_board[key][0] - board[key][0]) + abs(final_board[key][1] - board[key][1])
    
    return manhattan_cost

def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
