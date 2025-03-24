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


# Copiando uma lista para outra (Shallow Copy e Deep Copy)


# Forma 1 - Deep Copy

# Ao utilizarmos lista.copy() copiamos os dados de uma lista para uma nova lista,
# mas elas ficam totalmente independentes, ou seja,
# modificando uma lista, não afeta a outra.
# Isso em Python, é chamado de Deep Copy (Cópia Profunda)

lista = [1, 2, 3]
nova = lista.copy()
print(lista)  # [1, 2, 3]
print(nova)  # [1, 2, 3]
print()

nova.append(4)
print(lista)  # [1, 2, 3]
print(nova)  # [1, 2, 3, 4]
print()


# Forma 2 - Shallow Copy

# Ao utilizarmos a cópia via atribuição, copiamos os dados de uma lista para uma nova lista,
# mas após realizar modificações em uma das listas, essas modificações se refletiram em ambas as listas.
# Isso em Python, é chamado de Shallow Copy (Cópia Rasa)

lista = [1, 2, 3]
nova = lista # cópia
print(lista)  # [1, 2, 3]
print(nova)  # [1, 2, 3]
print()

nova.append(4)
print(lista)  # [1, 2, 3, 4]
print(nova)  # [1, 2, 3, 4]
print()
