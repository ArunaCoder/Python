# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')
print(not True)  # False
print(not False)  # True

if senha != '123456':
    print('Senha incorreta')

if not senha:
    print('Nada digitado')