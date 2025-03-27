"""
Dicionários

Obs.: Em algumas linguagens de programação, os dicionários Python são conhecidos pr mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Obs.: Sobre dicionários
    - Chave e Valor são separados por dois pontos 'chave: valor'.
    - Tanto chave quanto valor podem ser de qualquer tipo de dado.
    - Podemos misturar tipos de dados.
"""

print({})
print(type({}))  # <class 'dict'>
print()


# Criação de dicionários

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))
print()


# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))
print()
