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

# Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append.

Obs.: Com append, nós só conseguimos adicionar um elemento por vez.
# lista1.append(12, 34, 56)  # TypeError: list.append() takes exactly one argument (3 given)
"""

print(lista1)  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista1.append(42)
print(lista1)  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 42]
print()

# append -> coloca a lista como elemento único (sublista)
lista1.append([8, 3, 1])  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 42, [8, 3, 1]]
print(lista1)
print()

if [8, 3, 1] in lista1:
    print("Encontrei a lista.")
else:
    print("Não encontrei a lista.")
print()

if [22, 27, 27] in lista1:
    print("Encontrei a lista.")
else:
    print("Não encontrei a lista.")
print()

# extend -> coloca cada elemento da lista como valor adicional à lista
lista1.extend([123, 44, 77])  # [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 42, [8, 3, 1], 123, 44, 77]
print(lista1)
print()
