"""
Estruturas lógicas
and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:
    - Para o And, todos os valores precisam ser True.
    - Para o Or, ou um, ou outro precisam ser True;
    - Para o not, o valor do booleano é invertido.
"""


ativo = True
logado = True

if ativo and logado:
    print("Bem-vindo usuário!") #
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")


ativo = True
logado = False

if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.") #


ativo = False
logado = True

if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.") #


ativo = False
logado = False

if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.") #


ativo = True
logado = True

if not ativo:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.") #


ativo = True
logado = True

if not logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.") #


ativo = True
logado = True

if ativo is True:
    print("Bem-vindo usuário!") #
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")


ativo = True
logado = True

if logado is True:
    print("Bem-vindo usuário!") #
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")
