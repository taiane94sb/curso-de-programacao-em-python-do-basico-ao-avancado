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

# Podemos remover facilmente o último elemento de uma lista

print(lista5)  # ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print()

# O pop não somente remove o último elemento, mas também o retorna
ultimo_elemento = lista5.pop()
print(f"O elemento {ultimo_elemento} foi removido da lista.")
print(lista5)  # ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't']
print()

# Podemos remover um elemento pelo índice

# Obs.: Os elementos a direita deste índice serão deslocados para a esquerda
elemento_removido_1 = lista5.pop(2)
print(f"O elemento {elemento_removido_1} foi removido da lista.")
print(lista5)  # ['G', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't']
print()

# Obs.: Se não houver índice informado, teremos o erro IndexError
# elemento_inexistente = lista5.pop(100)  # IndexError: pop index out of range

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)
print(len(lista5))
print()
