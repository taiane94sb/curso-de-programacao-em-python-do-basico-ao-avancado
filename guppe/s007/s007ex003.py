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

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
print(tupla)

# Obs.: gera um erro (ValueError) se colocarmos um número diferente de elementos para desempacotar
escola, curso = tupla
print(escola)  # Geek University
print(curso)  # Programação em Python: Essencial
