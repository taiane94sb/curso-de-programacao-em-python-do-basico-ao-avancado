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


# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]


# Trabalhando com slice de listas com o parâmetro 'ínicio'

#        0  1  2  3
lista = [1, 2, 3, 4]
print(lista)  # [1, 2, 3, 4]
print(lista[:])  # pega todos os elementos -> [1, 2, 3, 4]
print()

print(lista[0:])  # começa do 0, pega até o final -> [1, 2, 3, 4]
print(lista[1:])  # começa do 1, pega até o final -> [2, 3, 4]
print(lista[2:])  # começa do 2, pega até o final -> [3, 4]
print(lista[3:])  # começa do 3, pega até o final -> [4]
print()


# Trabalhando com slice de listas com o parâmetro 'fim'

#        0  1  2  3
lista = [1, 2, 3, 4]
print(lista)  # [1, 2, 3, 4]
print(lista[:])  # pega todos os elementos -> [1, 2, 3, 4]
print()

print(lista[:1])  # começa do 0, pega até o índice 1 - 1 -> 0 -> [1]
print(lista[:2])  # começa do 0, pega até o índice 2 - 1 -> 1 ->  [1, 2]
print(lista[:3])  # começa do 0, pega até o índice 3 - 1 -> 2 -> [1, 2, 3]
print(lista[:4])  # começa do 0, pega até o índice 4 - 1 -> 3 -> [1, 2, 3, 4]
print()


# Trabalhando com slice de listas com o parâmetro 'passo'

#        0  1  2  3
lista = [1, 2, 3, 4]
print(lista)  # [1, 2, 3, 4]
print(lista[::])  # pega todos os elementos -> [1, 2, 3, 4]
print()

print(lista[::1])  # pega todos os elementos, pulando de 1 em 1 -> [1, 2, 3, 4]
print(lista[::2])  # pega todos os elementos, pulando de 2 em 2 -> [1, 3]
print(lista[::-1])  # começa do fim, até o início, pega todos os elementos, pulando de 1 em 1 -> [1, 3]
print(lista[::-2])  # começa do fim, até o início, pega todos os elementos, pulando de 2 em 2 -> [4, 2]
print()


# Invertendo valores

nomes = ['Geek', 'University']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
print()

nomes = ['Geek', 'University']
print(nomes)
nomes.reverse()
print(nomes)
print()
