# https://pythonacademy.com.br/blog/f-strings-no-python

# Como f-strings são processadas em tempo de execução, podemos colocar quase todo tipo de código dentro das expressões.

nome = 'python academy'

print(f"Qual o melhor Blog sobre Python? {nome.upper() + '!' * 3}")
#--------------------     .

import math

x = 0.5

print(f'cos({x}) = {math.cos(x)}')

#--------------------     .

dicionario = {'nome': 'Vinícius', 'ocupacao': 'Software Engineer'}

print(f"{dicionario['nome']} é um {dicionario['ocupacao']}")