Nomes, cartões de matrícula e turma:
Nome: Luccas da Silva Lima Matrícula: 00324683 Turma: A
Nome: Henrique Carniel da Silva Matrícula: 00335626 Turma: A

Bibliotecas:
Nenhuma biblioteca precisa ser instalada.

Avaliação poda alfa-beta no tic-tac-toe misere (item 2.3):
(i) O minimax sempre ganha do randomplayer? Sim, o jogo foi realizado 20 vezes e em todas o minimax ganhou.

(ii) O minimax sempre empata consigo mesmo? Sim o jogo foi realizado 20 vezes e em todas o minimax empatou.

(iii) O minimax sempre empata contra as jogadas perfeitas recomendadas pelo
https://nyc.cs.berkeley.edu/uni/games/ttt/variants/misere ? Sim.

(iv) Para o Othello, faça um mini-torneio entre os algoritmos. Observe e relate qual implementação foi a
mais bem-sucedida.

Count Vs Mask = Mask wins.
Mask Vs Count = Mask wins.

Custom Vs Mask = Mask wins.
Mask Vs Custom = Custom wins.

Custom vs Count = Custom wins.
Count Vs Custom = Custom wins.

As implementações Mask e Custom foram as melhores.

Othello:
(i) Descrição da função de avaliação customizada:
A avaliação customizada leva em conta a posições das peças e a mobilidade delas. Caso uma peça seja colocado em uma borda do tabuleiro, ela recebe valor 0,5 de recompensa. Caso a peça esteja na diagonal, recebe 2 pontos. A mobilidade é gerada levando em conta o número de jogadas possíveis.

(ii) descrição do critério de parada (profundidade máxima fixa? aprofundamento
iterativo?):
O critério de parada escolhido foi o de profundidade máxima fixa, igual a 4. 

(iii) resultado da avaliação (qual a melhor implementação, se MCTS ou minimax com
qual heurística...):
A melhor avaliação foi com minimax com a heurística custom.

(iv) implementação escolhida para o torneio e se houve implementação de alguma
melhoria no minimax ou no MCTS: 
Minimax com heurística custom.

Feedback: 
(i) quão fácil ou difícil foi realizar o trabalho? 
Tivemos grandes dificuldades na implementação do monte carlo tree search. Não entendemos exatamente como funcionava a estrutura da árvore e como deveríamos utilizá-la. A maior dificuldade foi para realizar o backpropagation após a simulação.
Tivemos algumas dificuldades durante a implementação do minimax também, mas estes foram resolvidos.
O maior desafio encontrado foi o tempo, tivemos pouco tempo (1 semana) entre a entrega do trabalho 3 para este e as tarefas de outras cadeiras (trabalhos e provas) também dificultaram.

(ii) como foi trabalhar com o auxílio da IA?
Utilizamos o ChatGPT. Ele foi útil para tirar algumas dúvidas mais 'bobas', como por exemplo a sintaxe de algumas estruturas e comandos em python. Também usamos ele para refatorar algumas partes do código.

(iii) quais sugestões teria para melhorar o trabalho?
Acredito que um aumento no prazo do trabalho ajudaria consideravelmente o seu desenvolvimento.