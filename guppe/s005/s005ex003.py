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


nome = "Taiane"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em uma lista

qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    soma = soma + num

print(f"A soma é {soma}.")
