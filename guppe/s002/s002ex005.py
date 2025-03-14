"""
Recebendo dados do usuário

input() - Todo dado recebido via input é do tipo String.

Em Python, string é tudo queestiver entre:
    - Aspas simples;
    - Aspas duplas;
    - Aspas simples triplas;
    - Aspas duplas triplas;
"""


# Print 'moderno' (versão 3.x do Python):

nome = input("Qual o seu nome? ") # Entrada de dados
print(f"Seja bem-vindo(a) {nome}!") # Saída de dados

# Processamento de dados

idade = input("Qual a sua idade? ") # Entrada de dados
print(f"A {nome} tem {idade} anos.") # Saída de dados
print(f"A {nome} nasceu no ano de {2025 - int(idade)}.") # Saída de dados

