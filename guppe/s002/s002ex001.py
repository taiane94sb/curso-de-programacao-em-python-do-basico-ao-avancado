"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem

The Zen of Python
import this

A ideia do PEP8 é que possamos escrever códigos Python de forma Pythonica


[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo separados por underline para funções ou variáveis;

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5


[3] - Utilize 4 espaços para identação (não use Tab);

if 'a' in 'banana':
    print('tem')


[4] - Linhas em branco:
    - Separar funções e definições de classes com duas linhas em branco;
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco;



[5] - Imports:
    - Imports devem ser sempre feitas em linhas separadas;

# import errado:
import sys, os

# import correto:
import sys
import os

# Caso tenha poucos  imports de um mesmo pacote, não há problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# imports devem ser colocados no topo do arquivo, logo depois de qualqer comentário ou docstring e
# antes de constantes ou variáveis globais.


[6] - Espaços em expressões e instruções;

# Não faça:
funcao( algo[ 1 ], { outro: 2 })
# Faça:
funcao(algo[1], {outro: 2})

# Não faça:
algo_(1)
# Faça:
algo(1)

# Não faça:
dict [ 'chave' ] = lista [ indice ]
# Faça:
dict['chave'] = lista[indice]

# Não faça:
x              = 1
y              = 3
variavel_longa = 5
# Faça:
x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução sempre com uma noa linha;
"""
import this
