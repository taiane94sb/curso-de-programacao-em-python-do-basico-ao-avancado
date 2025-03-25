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

# Contando elemento dentro de uma tupla
tupla1 = ('a', 'b', 'c', 'a', 'd')
print(tupla1)
print(tupla1.count('a'))
print(tupla1.count('b'))
print(tupla1.count('c'))
print(tupla1.count('d'))
print()

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))
print()
