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


# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)  # {1, 2, 3}

s.add(4)  # {1, 2, 3, 4}
s.add(4)  # {1, 2, 3, 4} Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)
print()


# Removendo elementos em um conjunto

s = {1, 2, 3}
print(s)  # {1, 2, 3}

# Forma 1

# Informamos o valor a ser removido
s.remove(1)  # {2, 3}

# Caso o valor não seja encontrado, vai gerar um KeyError
# s.remove(11)  # KeyError: 11
print(s)
print()


s = {1, 2, 3}
print(s)  # {1, 2, 3}

# Forma 2
# Informamos o valor a ser removido
s.discard(1)  # {2, 3}
print(s)

# Caso o valor não seja encontrado, nenhum erro é gerado
s.discard(11)
print(s)  # {2, 3}
print()
