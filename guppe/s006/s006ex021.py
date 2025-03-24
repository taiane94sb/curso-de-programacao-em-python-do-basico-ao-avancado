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

# Outros métodos

# Encontrar o índie de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros)
print("-----")

# Em qual índice está o valor 6
print(numeros.index(6))
print("-----")

# Em qual índice está o valor 11
# Obs.: caso não tenha este elemento na lista, será apresentado o erro ValueError
# print(numeros.index(11))  # ValueError: 11 is not in list

# Em qual índice está o valor 5
# Obs.: No caso de ter mais de um mesmo elemento na lista, retorna o índice do primeiro elemento encontrado
print(numeros.index(5))
print("-----")

# Podemos fazer a busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1))  # buscando a partir do índice 1
print("-----")

# Podemos fazer a busca dentro de um range, ou seja, qual índice começar a buscar
# Obs.: caso não tenha este elemento na lista, será apresentado o erro ValueError
# print(numeros.index(5, 5))  # buscando a partir do índice 5  # ValueError: 5 is not in list

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # buscando a partir do índice 3 até o índice 6
print("-----")
