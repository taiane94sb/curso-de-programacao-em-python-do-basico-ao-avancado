"""
Mapas: conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)
print()


# Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f"chave={chave} e valor={valor}")
print("----------")
print()
