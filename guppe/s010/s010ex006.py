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


# Copiando um conjunto para outro

s = {1, 2, 3}
print(s)  # {1, 2, 3}
print()


# Forma 1: Deep Copy
novo = s.copy()
print(s)  # {1, 2, 3}
print(novo)  # {1, 2, 3}
novo.add(4)
print(s)  # {1, 2, 3}
print(novo)  # {1, 2, 3, 4}
print()

# Forma 2: Shallow Copy
novo = s
print(s)  # {1, 2, 3}
print(novo)  # {1, 2, 3}
novo.add(4)
print(s)  # {1, 2, 3, 4}
print(novo)  # {1, 2, 3, 4}
print()

# Podemos remover todos os elementos de um conjunto

s.clear()
print(s)  # set()
print(len(s))  # 0
print()
