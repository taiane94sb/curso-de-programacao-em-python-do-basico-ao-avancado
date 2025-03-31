"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos Conjuntos da Matemática.
- No Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:
  - Sets (conjuntos) não possuem valores duplicados.
  - Sets (conjuntos) não possuem valores ordenados.
  - Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves.

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

"""


# Definindo um conjunto:

# Forma 1:

# Repare que temos valores repetidos
# Obs.: ao criar um conjunto, caso seja adicionado um valor ja existente,
# o mesmo será ignorado sem gerar erro e não fará parte do conjunto
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)  # {1, 2, 3, 4, 5, 6, 7}
print(type(s))  # <class 'set'>
print()

# Forma 1:
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(s)  # {1, 2, 3, 4, 5, 6, 7}
print(type(s))  # <class 'set'>
print()
