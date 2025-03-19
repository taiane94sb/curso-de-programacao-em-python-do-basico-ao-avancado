"""
Ranges

- Precisamos conhecer o loop for para usar o range.
- Precisamos conhecer range para trabalhar melhor com o loop for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim, de maneira específica.

Formas gerais:

- Forma 1:
    range(valor_de_parada)
Obs.: valor_de_parada não inclusiva (inicio padrão 0, e passo de 1 em 1)
for num in range(11):
    print(num)

- Forma 2:
    range(valor_de_inicio, valor_de_parada)
Obs.: valor_de_parada não inclusiva (inicio especificado pelo usuário, e passo de 1 em 1)
for num in range(1, 11):
    print(num)

- Forma 3:
    range(valor_de_inicio, valor_de_parada, passo)
Obs.: valor_de_parada não inclusiva (inicio especificado pelo usuário, e passo especificado pelo usuário)
for num in range(0, 10, 2):
    print(num)

- Forma 4:
    range(valor_de_final, valor_de_parada, passo)
Obs.: valor_de_parada não inclusiva (inicio especificado pelo usuário, e passo especificado pelo usuário)
for num in range(10, 0, -1):
    print(num)

"""


# Forma 1
for num in range(11):
    print(num)

print("----")

# Forma 2
for num in range(1, 11):
    print(num)

print("----")

# Forma 3
for num in range(0, 10, 2):
    print(num)

print("----")

# Forma 4
for num in range(10, 0, -1):
    print(num)

print("----")
