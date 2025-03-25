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

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))
print()
