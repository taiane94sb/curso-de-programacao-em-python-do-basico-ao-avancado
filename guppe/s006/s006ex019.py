"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
        Ou seja, nestas linguagens, se você criar um array do tipo int e com tamanho 5,
        este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Linguagem Python:
- Dinâmico:
        - Não possui tamanho fixo:
            Ou seja, podemos criar a lista e simplesmente ir adicionando elementos.
        - Qualquer tipo de dado:
            Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []
"""


print(type([]))  # <class 'list'>
print()

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list("Geek University")
lista6 = [1, 2.34, True, 'Geek', [1, 2, 3], 453453453453]


# Iterando sobre listas

#         0        1          2       3
cores = ["verde", "amarelo", "azul", "branco"]
#        -4       -3         -2       -1
print(cores)

for cor in cores:
    print(cor)
print("----------")

indice = 0
while indice < len(cores):
    print(f"{indice}) {cores[indice]}")
    indice = indice + 1
print("----------")

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)
print("----------")

print(list(enumerate(cores)))  # [(0, 'verde'), (1, 'amarelo'), (2, 'azul'), (3, 'branco')]
print("----------")
