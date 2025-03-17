"""
Tipo booleano
Algebra booleana, criada por George Boole
2 constantes, Verdadeiro (True) ou Falso (False)
Obs.: Sempre com inicial maiúscula
"""


ativo = False
print(ativo)
print()

"""
Operações básicas
"""

# Negação (not)
"""
Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso.
Se o valor for falso, o resultado será verdadeiro.
"""
print(not ativo)
print(True)
print(not True)
print(False)
print(not False)
print()

# Ou (or)
"""
É uma operação binária, ou seja, depende de dois valores.
Ou um ou outro deve ser verdadeiro.
"""
print(True or True)
print(True or False)
print(False or True)
print(False or False) # Or só é False se os dois forem False
print()

# E (And)
"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os valores devem ser verdadeiro.
"""
print(True and True) # And só é True se os dois forem True
print(True and False)
print(False and True)
print(False and False)
print()
