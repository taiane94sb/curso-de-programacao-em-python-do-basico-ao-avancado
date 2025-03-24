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

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print()

# Podemos facilmente checar se determinado valor está contido na lista

num = 8
if num in lista4:
    print(f"Encontrei o número {num}.")
else:
    print(f"Não encontrei o número {num}.")
print()

num = 18
if num in lista4:
    print(f"Encontrei o número {num}.")
else:
    print(f"Não encontrei o número {num}.")
print()

letra = 'e'
if letra in lista5:
    print(f"Encontrei a letra {letra}.")
else:
    print(f"Não encontrei a letra {letra}.")
print()

letra = 'a'
if letra in lista5:
    print(f"Encontrei a letra {letra}.")
else:
    print(f"Não encontrei a letra {letra}.")
print()

print(dir(lista5))
print()
