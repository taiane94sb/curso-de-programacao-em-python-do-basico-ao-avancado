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

Porque utilizar tuplas?

- tuplas são mais rápidas do que listas
- tuplas deixam seu código mais seguros (isso porque trabalhar com elementos imutáveis traz mais segurança)
"""


print(type(()))  # <class 'tuple'>

# Dicas de utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
meses_do_ano_tupla = (
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
)
print(meses_do_ano_tupla)
print()


# meses_do_ano_lista = [
#     "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
# ]
# print(meses_do_ano_lista)


# O acesso de elementos de uma tupla é semelhante a de uma lista
print(meses_do_ano_tupla[5])
print()


# Iterar com while
i = 0

while i < len(meses_do_ano_tupla):
    print(meses_do_ano_tupla[i])
    i = i +1
print()


# Verificarmos em qual índice um elemento está na tupla
print(meses_do_ano_tupla.index('Janeiro'))
print()

# Obs.: caso o elemento não exista, será gerado um ValueError
# print(meses_do_ano_tupla.index("Domingo"))  # ValueError: tuple.index(x): x not in tuple
# print(meses_do_ano_tupla.index('Janeiro', 6))  # ValueError: tuple.index(x): x not in tuple


# Slicing

# tupla[inicio:fim:passo]
print(meses_do_ano_tupla[::])
print(meses_do_ano_tupla[::2])
print(meses_do_ano_tupla[::-1])
print(meses_do_ano_tupla[::-2])
print()


# Copiando uma tupla para outra

# na tupla não temos o problema de Shallow Copy

tupla = (1, 2, 3, 4)
nova = tupla
print(tupla)
print(nova)
print()

outra = (4, 5, 6)
nova = nova + tupla
print(tupla)
print(outra)
print(nova)
print()
