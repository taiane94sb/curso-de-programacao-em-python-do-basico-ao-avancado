"""
Dicionários

Obs.: Em algumas linguagens de programação, os dicionários Python são conhecidos pr mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Obs.: Sobre dicionários
    - Chave e Valor são separados por dois pontos 'chave: valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados

Podemos usar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionario, como chaves de um dicionário
"""

print({})
print(type({}))  # <class 'dict'>
print()


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Adicionar elementod em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300 }

print(receita)  # {'jan': 100, 'fev': 120, 'mar': 300 }
print(type(receita))  # <class 'dict'>
print()


# Forma 1

receita['abr'] = 350
print(receita)  # {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350}
print(type(receita))  # <class 'dict'>
print()


# Forma 2

novo_dado = {'mai': 500}
print(receita)  # {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350}
print(type(receita))  # <class 'dict'>
receita.update(novo_dado)  # receita.update({'mai': 500})
print(receita)  # {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 500}
print(type(receita))  # <class 'dict'>
print()

# Atualizando dados em um dicionário

# Conclusão 1: a forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2: em dicionários, não podemos ter chaves repetidas.

print(receita)  # {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 500}
print(type(receita))  # <class 'dict'>
receita.update({'mai': 600})
print(receita)  # {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 600}
print(type(receita))  # <class 'dict'>
print()
