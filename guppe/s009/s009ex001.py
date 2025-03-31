"""
Mapas: conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)
print()


# Iterar sobre dicionários

# Acessando as chaves
print(receita.keys())  # dict_keys(['jan', 'fev', 'mar'])

for chave in receita:
    print(chave)
print("----------")
print()
for chave in receita.keys():
    print(chave)
print("----------")
print()


# Acessando os valores
print(receita.values())  # dict_values([100, 250, 400])

for valor in receita.values():
    print(valor)
print("----------")
print()

for chave in receita:
    print(receita[chave])
print("----------")
print()


# Acessando as chaves e os valores
print(receita.items())  # dict_items([('jan', 100), ('fev', 250), ('mar', 400)])

for chave, valor in receita.items():
    print(f"Em {chave} recebi R${valor}")
print("----------")
print()

for chave in receita:
    print(f"Em {chave} recebi R${receita[chave]}")
print("----------")
print()

for chave in receita:
    print(f"Em {chave} recebi R${receita[chave]}")
print("----------")
print()
