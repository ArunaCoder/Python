# 34585076
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Que horas são? ')

hora = None
manha = None
tarde = None
noite = None

try:
    hora = int(entrada)
    manha = hora >= 0 and hora <= 11
    tarde = hora >= 12 and hora <= 17
    noite = hora >= 18 and hora <= 23

    if manha:
        print('Bom dia')
    elif tarde:
        print('Boa tarde')
    elif noite:
        print('Boa noite')
    else:
        print('Isso é hora meu filho?')
except:
    print('Você tá de brincadeira? Digite um número inteiro rapaz!')
