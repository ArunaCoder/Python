"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')
numero_int = None
# numero_int = int(numero)
try:
    numero_int = int(numero)
    numero_par = (numero_int % 2) == 0
    if numero_par:
        print('Este número é par')
    else:
        print('Este número é ímpar')

except:
    print('Isso não é um número inteiro')


#--------------------     .

entrada = input ('Fala um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
