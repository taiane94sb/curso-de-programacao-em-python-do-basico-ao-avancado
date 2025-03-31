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


# Métodos Matemáticos de Conjuntos

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
print(estudantes_python)  # {'Julia', 'Pedro', 'Guilherme', 'Marcos', 'Patricia', 'Ellen'}
print(estudantes_java)  # {'Julia', 'Fernando', 'Patricia', 'Gustavo', 'Ana'}
print()


# Forma 1: Utilizando intersection

ambos_1 = estudantes_python.intersection(estudantes_java)
# {'Julia', 'Patricia'}
print(ambos_1)
ambos_1_2 = estudantes_java.intersection(estudantes_python)
# {'Julia', 'Patricia'}
print(ambos_1)
print()


# Forma 2: Utilizando o caractere &

ambos_2 = estudantes_python & estudantes_java
# {'Julia', 'Patricia'}
print(ambos_2)
ambos_2_2 = estudantes_java & estudantes_python
# {'Julia', 'Patricia'}
print(ambos_2_2)
print()
