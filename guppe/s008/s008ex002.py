"""
Dicionários

Obs.: Em algumas linguagens de programação, os dicionários Python são conhecidos pr mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Obs.: Sobre dicionários
    - Chave e Valor são separados por dois pontos 'chave: valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados
"""

print({})
print(type({}))  # <class 'dict'>
print()


# Acessando elementos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 1 (acessando via chave, da mesma forma que lista/tupla)
print(paises)
print(paises['br'])  # Brasil
print(paises['eua'])  # Estados Unidos
print(paises['py'])  # Paraguai

# Obs.: caso tentarmos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError
# print(paises['ru'])  # KeyError: 'ru'
print()


# Forma 2 (acessando via get, essa é a forma recomendada)
print(paises.get('br'))  # Brasil
print(paises.get('eua'))  # Estados Unidos
print(paises.get('py'))  # Paraguai
print(paises.get('ru'))  # None

# Obs.: caso o get não encontre o objeto com a chave informada,
# será retornado o valor None, e não será gerado erro KeyError
russia = paises.get('ru')  # None
paraguai = paises.get('py')  # None

# Obs.: podemos definir um valor padrão para caso não encontrarmos o objeto com a chave informada
italia = paises.get('it', 'Não encontrado')  # Não encontrado

if russia:
    print("Encontrei o país Russia.")
else:
    print("Não encontrei o país Russia.")  #

if paraguai:
    print("Encontrei o país Paraguai.")  #
else:
    print("Não encontrei o país Paraguai.")

if italia == 'Não encontrei':
    print("Encontrei o país Italia.")  #
else:
    print("Não encontrei o país Italia.")

print()


"""
Tipo None

O tipo de dado None em Python representa o tipo de dado sem tipo, ou poderia ser conhecido também como tipo vazio.
Porém, falar que é um tipo de dado sem tipo é mais apropriado.

Obs.: o tipo None é sempre especificado com a primeira letra maiúscula.

Quando utilizamos?
    - Quando queremos utilizar uma variável e inicializá-la com um tipo sem tipo, antes de recebermos um valor final.

Obs.: o tipo None em Python é sempre considerado como False.
"""

numeros = None
print(numeros)
print(type(numeros))
print()
