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

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300 }

print(receita)  # {'jan': 100, 'fev': 120, 'mar': 300}
print(type(receita))  # <class 'dict'>
print()

# Forma 1

# Obs1.: aqui, precisamos, sempre, informar a chave, e caso não encontre o elemento, o KeyError é retornado.
# Obs2.: ao retornarmos um objeto, o valor deste objeto é sempre retornado.
marco = receita.pop('mar')  # 200
# abril = receita.pop('abr')  # KeyError: 'abr'

print(f"O valor {marco} do mês de Março foi removido")
print(receita)  # {'jan': 100, 'fev': 120}
print(type(receita))  # <class 'dict'>
print()

# Forma 2

# Obs1.: se a chave não existir, será gerado um KeyError.
# Obs2.: neste caso, o valor removido não é retornado.
del receita['fev']
print(receita)  # {'jan': 100 }
print(type(receita))  # <class 'dict'>
print()
# del receita['fev']  # KeyError: 'fev'
