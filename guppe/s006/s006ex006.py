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

# Podemos juntar duas listas

print(lista1)  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(lista2)  # ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

# Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista6 = lista1 + lista2
print(lista1)  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(lista2)  # ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(lista6)  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 'G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print()

lista7 = lista1.extend(lista2)
print(lista1)  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(lista2)  # ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(lista7)  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 'G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print()
