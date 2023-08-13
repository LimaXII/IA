from typing import Iterable, Set, Tuple, Callable
import help
import constants
import heuristic
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
        
    # Sobreescreve o operador de comparação para ordenar baseado no custo estimado, útil ao heap usado no A*
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
    if (invalid_state(estado)):
        return constants.ERROR_MESSAGE

    underline_position = estado.find(constants.UNDERLINE_CHAR)
    successor_set = set()
    
    # Pode mover pra cima
    if underline_position - 3 >= 0:
        successor_set.add((
            constants.UP,
            help.swap_string(estado, underline_position, underline_position - 3)
        ))
    # Pode mover pra baixo
    if underline_position + 3 <= 8:
        successor_set.add((
            constants.DOWN,
            help.swap_string(estado, underline_position, underline_position + 3)
        ))
    # Pode mover pra direita
    if (underline_position + 1) % 3 != 0:
        successor_set.add((
            constants.RIGHT,
            help.swap_string(estado, underline_position, underline_position + 1)
        ))
    # Pode mover pra esquerda
    if underline_position % 3 != 0:
        successor_set.add((
            constants.LEFT,
            help.swap_string(estado, underline_position, underline_position - 1)
        ))
        
    return successor_set
    
def invalid_state(state: str) -> bool:
    # Verifica se o estado/string possui 9 caracteres
    if len(state) != 9:
        return True
    # Verifica se o estado/string não repete elementos
    if len(set(state)) != 9:
        return True
    # Verifica se os caracteres do estado/string estão no conjunto de elementos possíveis
    for char in state:
        if char not in constants.POSSIBLE_SET:
            return True
        
    return False
    

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


def astar(estado:str, heuristic_cost_function:Callable[[Nodo], int])->list[str]:
    initial_node = Nodo(estado, None, None, 0)
    explored = set()
    border = [initial_node]
    heapify(border)
    
    while (border):
        # Retira o nodo com o menor custo estimado
        current_node = heappop(border) 
        
        if current_node.estado == constants.FINAL_STATE:
            return find_path(current_node)
        if current_node.estado not in explored:
            explored.add(current_node.estado)
            for node in expande(current_node):
                node.custo_estimado = node.custo + heuristic_cost_function(node.estado)
                heappush(border, node)
            
    return None


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, heuristic.hamming_cost)


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return astar(estado, heuristic.manhattan_cost)


def bfs_or_dfs(estado:str, data_structure:constants):
    initial_node = Nodo(estado, None, None, 0)
    explored = set()
    border = [initial_node]
    
    while (border):
        current_node = border.pop(data_structure)
        
        if current_node.estado == constants.FINAL_STATE:
            return find_path(current_node)
        if current_node.estado not in explored:
            explored.add(current_node.estado)
            for node in expande(current_node):
                border.append(node)
            
    return None


def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """    
    return bfs_or_dfs(estado, constants.QUEUE)


def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return bfs_or_dfs(estado, constants.STACK)

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

def find_path(node: Nodo) -> list[str]:
    path = []
    while(node.pai is not None):
        path.insert(0, node.acao)
        node = node.pai
    return path