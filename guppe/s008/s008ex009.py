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


print(dir({}))
print()


# Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)  # {'a': 1, 'b': 2, 'c': 3}
print(type(d))  # <class 'dict'>
print()


# Limpar o dicionário (zerar dados)

d.clear()
print(d)  # {}
print()


# Copiando um dicionário para outro

# Forma 1

novo = d.copy()  # Deep Copy
print(d)  # {}
print(novo)  # {}

novo['d'] = 4
print(d)  # {}
print(novo)  # {'d': 4}
print()


# Forma 1

novo2 = d  # Shallow Copy
print(d)  # {}
print(novo2)  # {}

novo2['d'] = 4
print(d)  # {'d': 4}
print(novo2)  # {'d': 4}
print()


# Forma não usual de criação de dicionários

# Obs.: o método fromkeys recebe dois parâmetros, um iterável e um valor.
# Ele vai gerar, para cada valor do iterável, uma chave, e irá atribuir a esta chave, o valor informado.
outro = {}.fromkeys('a', 'b')
print(outro)  # {'a': 'b'}
print(type(outro))  # <class 'dict'>
print()

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)  # {'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido', 'profile': 'desconhecido'}
print(type(usuario))  # <class 'dict'>
print()

outro2 = {}.fromkeys('teste', 'valor')
print(outro2)  #  {'t': 'valor', 'e': 'valor', 's': 'valor'}
print(type(outro2))  # <class 'dict'>
print()

outro3 = {}.fromkeys(range(1, 11), 'valor')
#  {1: 'valor', 2: 'valor', 3: 'valor', 4: 'valor', 5: 'valor', 6: 'valor', 7: 'valor', 8: 'valor', 9: 'valor', 10: 'valor'}
print(outro3)
print(type(outro3))  # <class 'dict'>
print()
