"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.
2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja,
    seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python, fazemos:
    nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica.
Isso Significa que ao declarar uma variável, nós não colocamos o tipo de dado dele.
Este tipo é inferido ao atribuirmos o valor à mesma.
"""


nome = "Taiane"  # Variável global
print(nome)
print(type(nome))

nome = "Matheus"  # Variável global
print(nome)
print(type(nome))

nao_existo = "Oi"
print(nao_existo)

numero = 42
novo = 0

if numero > 100:
    novo = numero + 10 # Variável local (declarada dentro do escopo do if
    print(novo)

# print(novo)  # NameError: name 'novo' is not defined
