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


# Assim como todo outro conjunto Python, podemos colocar todo tipo de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))
print()

# Podemos iterar, normalmente, em um set
for valor in s:
    print(valor)
print("----------")
print()

