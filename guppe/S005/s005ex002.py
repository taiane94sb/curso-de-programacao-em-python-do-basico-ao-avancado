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

"""
Enumerate:
((0, 'T'), (1, 'a'), (2, 'i'), (3, 'a'), (4, 'n'), (5, 'e'))
"""
print('Indice e Valor: ')
for indice, valor in enumerate(nome):
    print(indice, valor, nome[indice])

print()

"""
Obs.: quando não precisamos de uma valor, podermos descartá-lo utilizando um underline (_).
"""
print('Indice: ')
for indice, _ in enumerate(nome):
    print(indice)

print()


print('Valor: ')
for _, valor in enumerate(nome):
    print(valor)

print()
