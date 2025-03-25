"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1. As tuplas são representadas por parênteses ()
2. As tuplas são imutáveis: isso significa que ao criar uma tupla, ela não muda.
Toda operação em uma tupla gera uma nova tupla.

Podemos concluir que tuplas são definidas pela vírgula, e não pelo uso de parenteses.

(4) -> Não é uma tupla
(4,) -> É uma tupla
4, -> É uma tupla
"""


print(type(()))  # <class 'tuple'>

# Cuidado 1: as tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))
print()

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))
print()

# Cuidado 1: tuplas com 1 elemento:

# podemos concluir que tuplas são definidas pela vírgula,
# e não pelo uso da parenteses
tupla3 = (4)  # isso não é uma tupla
print(tupla3)
print(type(tupla3))  # <class 'int'>
print()

tupla4 = (4, )  # isso é uma tupla
print(tupla4)
print(type(tupla4))  # <class 'tuple'>
print()

tupla5 = 4,   # isso é uma tupla
print(tupla5)
print(type(tupla5))  # <class 'tuple'>
print()
