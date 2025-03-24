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


# Podemos facilmente converter uma string para uma lista

# Exemplo 1
# Obs.: Por padrão, o split separa os elementos da lista pelo espaço entre elas

curso = "Programação em Python: Essencial"
print(curso)
curso = curso.split()  # ['Programação', 'em', 'Python:', 'Essencial']
print(curso)
print()

# Exemplo 2

curso = "Programação,em,Python:,Essencial"
print(curso)
curso = curso.split(',')  # ['Programação', 'em', 'Python:', 'Essencial']
print(curso)
print()
