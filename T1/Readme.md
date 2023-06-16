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

Acurácia máxima de 75%. O maior impacto positivo foi com a adição de alguns Dropouts (para evitar overfitting) e o BatchNormalization.
Também deu pra perceber que aumentar a quantidade de layers nas camadas trouxe uma melhora significativa.

Não foi possível aumentar mais que 75% porque a adição de mais layers levavam a um grande overfitting e portanto, uma acurácia menor nos dados finais.
O maior desafio/dificuldade foi conseguir maximizar a acurácia mantendo as epochs em 10.

3) Foi possivel obter mais de 60% de acurácia no CIFAR-100? Qual modificação teve maior
impacto positivo? Qual o maior desafio/dificuldade?

Não.
Similarmente ao CIFAR-10, as melhores modificações foram as adições do Dropout e o BatchNormalization.
A maior dificuldade foi tentar aumentar a acurácia, tendo em visto que o dataset possui muitas classes diferentes.
Acredito que se pudesse aumentar o número de epochs, o resultado poderia ser um pouco melhor.

4) Quais fatores (tanto das próprias redes quanto dos dados) levam as redes neurais a melhorarem o
desempenho? E quais fatores tornam o desempenho pior?

O aumento no número de layers e camadadas tendem a aumentar o desepenho (Mas não pra sempre, se aumentar demais causa overfitting). A adição do Dropout e BatchNormalization ajuda bastante no desempenho também.
A convolução é extremamente necessária para os datasets que possuem imagens.

O exagero de camadas ocultas, ou a falta delas, pioram o desempenho. Uma má função de ativação também piora significativamente.