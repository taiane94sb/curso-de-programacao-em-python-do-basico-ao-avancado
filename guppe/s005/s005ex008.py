"""
Loop while

Forma geral:

while expressao_booleana:
// execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.
"""


numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# Obs.: Em um loop while, é importante que cuidemos do critério deparada para não causar loop infinito.
