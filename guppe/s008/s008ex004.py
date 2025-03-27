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

# Tuplas, por exemplo, são bastante interessantes de serem utilizadas como chaves de dicionários,
# pois as mesmas são imutáveis

localidades = {
    (35.6895, 39.6917): "Escritótio em Tóquio",
    (40.7128, 74.0060): "Escritótio em Nova Iorque",
    (37.7749, 122.4194): "Escritótio em São Paulo",
}

print(localidades)
print(type(localidades))  # <class 'dict'>
print()
