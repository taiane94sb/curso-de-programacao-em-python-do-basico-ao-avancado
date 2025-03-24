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

for letra in nome:
    print(letra)

for letra in nome:
    print(letra, end="")
