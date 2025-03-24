"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

for item in iteravel:
    // execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = "Geek University"
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""


nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em uma lista

# Exemplo 1: iterando em uma string
for letra in nome:
    print(letra)

# Exemplo 2: iterando sobre uma lista
for numero in numeros:
    print(numero)

# Exemplo 3: iterando sobre um range
"""
range(valor_inicial, valor_final)

Obs.:
o valor final não é inclusive.
range(1, 10)
1
2
3
4
5
6
7
8
9
"""
for numero in range(1, 10):
    print(numero)
