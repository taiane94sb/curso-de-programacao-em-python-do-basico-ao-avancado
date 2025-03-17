"""
Tipo float
Tipo real, decimal
Casas decimais

Obs.: O separador de casas decimais na programação é o ponto e não a vírgula.
"""


# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))  # <class 'tuple'>

# Corretodo ponto de vista do Float
valor = 1.44
print(valor)
print(type(valor))  # <class 'float'>

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))  # <class 'int'>
print(valor2)
print(type(valor2))  # <class 'int'>

# Podemos converter um float para um int
"""
Obs.: Ao converter valores float para inteiros, perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))  # <class 'int'>

# Podemos trabalhar com números complexos
print(5j)
print(type(5j))  # <class 'complex'>
