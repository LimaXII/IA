from typing import Iterable, Set, Tuple
import help

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
    # Verfica se os caracteres do estado/string estão no conjunto de elementos possíveis
    for char in estado:
        if char not in possible_set:
            return "ERRO"

    underline_position = estado.find('_')
    successors = []
    
    # Pode mover pra cima
    if underline_position - 3 >= 0:
        successors.append((
            "acima",
            help.swap_string(estado, underline_position, underline_position - 3)
        ))
    # Pode mover pra baixo
    if underline_position + 3 <= 8:
        successors.append((
            "abaixo",
            help.swap_string(estado, underline_position, underline_position + 3)
        ))
    # Pode mover pra direita
    if (underline_position + 1) % 3 != 0:
        successors.append((
            "direita",
            help.swap_string(estado, underline_position, underline_position + 1)
        ))
    # Pode mover pra esquerda
    if underline_position % 3 != 0:
        successors.append((
            "esquerda",
            help.swap_string(estado, underline_position, underline_position - 1)
        ))
        
    return successors
    

def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # Lista de filhos
    nodes_list = []
    # Verifica filhos
    successors = sucessor(nodo.estado)
    # Atualiza lista de filhos
    for succ in successors:
        nodes_list.append(Nodo(succ[1], nodo, succ[0], 1 + nodo.custo))
    return nodes_list


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
