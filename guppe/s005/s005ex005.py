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


emoji = "U0001F60D"

for _ in range(3):
    for num in range(1, 11):
        print("\U0001F60D" * num)
