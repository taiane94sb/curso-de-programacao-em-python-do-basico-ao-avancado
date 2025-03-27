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


# Imagine que você tem um comércio eletrônico onde temos um carrinho de compras na qual adicionamos produtos.

"""
Carrinho de compras:
    - Produto 1:
        - nome;
        - quantidade;
        - preço;
    - Produto 2:
        - nome;
        - quantidade;
        - preço;
"""

# 1 - Poderíamos utilizar uma lista para isso? Sim.
# Teríamos de saber qual é o índice de cada informação no produto.

carrinho = []
print(carrinho)  # []
print(type(carrinho))  # <class 'list'>

produto1 = ['Produto 1', 1, 2300.00]
produto2 = ['Produto 2', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)  # [['Produto 1', 1, 230.0], ['Produto 2', 1, 150.0]]
print(type(carrinho))  # <class 'list'>


# 2 - Poderíamos utilizar uma tupla para isso? Sim.
# Teríamos de saber qual é o índice de cada informação no produto.

produto1 = ('Produto 1', 1, 2300.00)
produto2 = ('Produto 2', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)  # (('Produto 1', 1, 2300.0), ('Produto 2', 1, 150.0))
print(type(carrinho))  # <class 'tuple'>


# 3 -Poderíamos utilizar um dicionário para isso? Sim.
# Desta forma, facilmente adicionamos ou removemos produtos no carrinho,
# e em cada produto, podemos ter a certeza sobre cada informação.

carrinho = []
print(carrinho)  # []
print(type(carrinho))  # <class 'list'>

produto1 = {'Produto 1', 1, 2300.00}
produto2 = {'Produto 2', 1, 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)  # [{1, 2300.0, 'Produto 1'}, {1, 150.0, 'Produto 2'}]', 1, 230.0], ['Produto 2', 1, 150.0]]
print(type(carrinho))  # <class 'list'>
