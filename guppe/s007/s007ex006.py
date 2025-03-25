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

Métodos de adição e remoção nas tuplas não existem, dado o fato das tuplas serem imutáveis.
"""


print(type(()))  # <class 'tuple'>

# Concatenação de tuplas
tupla1 = (1, 2, 36)
tupla2 = (4, 5, 6)
print(tupla1)
print(tupla2)
print()

tupla3 = tupla1 + tupla2
print(tupla1)
print(tupla2)
print(tupla3)
print(tupla1 + tupla2)

# tuplas são imutáveis, mas podemos sobreescrever seus valores
tupla1 = tupla1 + tupla2
print(tupla1)
print(tupla2)
print(tupla3)
