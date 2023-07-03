## INF01048 - Inteligência Artificial - 2023/1 - Turma A
* Henrique Carniel da Silva - 335626
* Luccas da Silva Lima - 324683

# Trabalho 1 - Parte 1
Deixamos as variáveis w e b com o valor 0, o num_iterations com o valor inicial de 100, e o alpha alteramos para 0.11, pois diminuia o valor do EQM, resultando em uma predição melhor, com alpha >= 0.12 a reta resultante não converge. O valor final do EQM com esse parâmetros é de 0.5777860252560527, realizando testes com o num_iterations maior, percebemos que o valor de EQM converge para 0.575, ou seja, com um num_iterations relativamente pequeno, nos aproximamos bastante de uma "reta ideal".

# Trabalho 1 - Parte 2

## The MNIST Dataset

* Classes: 10. Cada classe representa um número entre 0 e 9.
* Amostras: 60.000 amostras reservadas para o treinamento e 10.000 para teste. Totalizando 70.000 amostras no dataset.
* Tamanho das imagens: 28x28x1 (altura x largura x canais de cor)

## Fashion MNIST Dataset

* Classes: 10. Cada classe representa uma peça de roupa diferente. (T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag and Ankle boot)
* Amostras: 60.000 amostras reservadas para o treinamento e 10.000 para teste. Totalizando 70.000 amostras no dataset.
* Tamanho das imagens: 28x28x1 (altura x largura x canais de cor)

## CIFAR-10 Dataset

* Classes: 10. Airplane, automobile, bird, cat, deer, dog, frog, horse, ship and truck.
* Amostras: 50.000 amostras reservadas para o treinamento e 10.000 para teste. Totalizando 60.000 amostras no dataset.
* Tamanho das imagens: 32x32x3 (altura x largura x canais de cor)

## Cifar-100 Dataset

* Classes: 100.
* Amostras: 500 imagens para o treinamento e 100 de teste por classe. Totalizando 60.000 amostras no dataset
* Tamanho das imagens: 32x32x3 (altura x largura x canais de cor)

# Perguntas gerais

1) Em quais datasets um perceptron simples (sem convolução e sem camadas ocultas) obtem uma
acurácia acima de 80%?

* MNIST - Acurácia de 97%
* Fashion MNIST - Acurácia de 88%

2) Qual a acurácia máxima obtida no CIFAR-10? Qual modificação teve maior impacto positivo?
Qual o maior desafio/dificuldade?

Acurácia máxima de 76,9%. O maior impacto positivo foi com a adição de alguns Dropouts (para evitar overfitting) e o BatchNormalization. As camadas de convoluções seguidas do BatchNormalization obtiveram uma melhora significativa de aproximadamente 2%
Também deu pra perceber que aumentar a quantidade de layers nas camadas trouxe uma melhora significativa.

Não foi possível aumentar mais que 76,9% porque a adição de mais layers levavam a um grande overfitting e portanto, uma acurácia menor nos dados finais.
O maior desafio/dificuldade foi conseguir maximizar a acurácia mantendo as epochs em 10.

3) Foi possivel obter mais de 60% de acurácia no CIFAR-100? Qual modificação teve maior
impacto positivo? Qual o maior desafio/dificuldade?

Não.
Similarmente ao CIFAR-10, as melhores modificações foram as adições do Dropout e o BatchNormalization.
A maior dificuldade foi tentar aumentar a acurácia, tendo em visto que o dataset possui muitas classes diferentes.
Acredito que se pudesse aumentar o número de epochs, o resultado poderia ser um pouco melhor.
Foi testada a adição de camadas adicionais, porém obtivemos uma acurácia menor.

4) Quais fatores (tanto das próprias redes quanto dos dados) levam as redes neurais a melhorarem o
desempenho? E quais fatores tornam o desempenho pior?

* O aumento no número de layers e camadadas tendem a aumentar o desepenho (Mas não pra sempre, se aumentar demais causa overfitting). A adição do Dropout e BatchNormalization ajuda bastante no desempenho também.
* A convolução é extremamente necessária para Image Classification.
* O exagero de camadas ocultas, ou a falta delas, pioram o desempenho. Uma má função de ativação também piora significativamente.
* O otimizador rmsprop tende a funcionar bem com Image Classification
* A ativação softmax é necessária no layer de output.
* Datasets com muitas classes (Ex: Cifar-100) são muito mais difíceis de treinar. Para o caso do Cifar-100, no dataset cada classe possui bem menos imagens para treinar do que as classes do Cifar-10. No Cifar-10 cada classe possui 5.000 imagens para treinamento, para o Cifar-100 cada classe possui apenas 500 imagens para treinamento.
