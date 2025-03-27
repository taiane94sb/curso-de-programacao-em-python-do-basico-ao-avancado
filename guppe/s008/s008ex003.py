"""
Dicionários

Obs.: Em algumas linguagens de programação, os dicionários Python são conhecidos pr mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Obs.: Sobre dicionários
    - Chave e Valor são separados por dois pontos 'chave: valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados
"""

print({})
print(type({}))  # <class 'dict'>
print()


# Acessando elementos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)  # True
print('eua' in paises)  # True
print('py' in paises)  # True
print()

print('Brasil' in paises)  # False
print('Estados Unidos' in paises)  # False
print('Paraguai' in paises)  # False
print()

if 'ru' in paises:
    print('Existe a chave ru')
else:
    print('Não existe a chave ru')
print()
