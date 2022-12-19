"""
Introdução ao empacotamento e desempacotamento
"""

cores = ['amarelo','azul','laranja']

cor1, cor2, cor3 = cores
print(cor1)

corx,*resto = cores
print(corx, resto)

# convenção quando não vai usar o resto, dá o nome de _

cor_vou_usar, *_ = cores
print(cor_vou_usar)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)

