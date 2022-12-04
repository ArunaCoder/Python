#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34543692#overview

# print(12,88,sep='', end='-')

# print(12,999,sep='', end='-')

# print(r"Where is my \"cheese\"?")
# print("Where is my \"cheese\"?")
# print("Where is my \"cheese\"?")

# print(type(True))
# print(type(True))

# nome = 'Gabriel'
# sobrenome = 'Silva'
# idade = 66
# ano_nascimento = 2022 - idade
# maior_de_idade = idade >= 18
# altura_metros = 1.80

# print('Nome:', nome)
# print('Sobrenome:', sobrenome)
# print('Idade:', idade)
# print('Ano de nascimento:', ano_nascimento)
# print('É maior de idade?', maior_de_idade)
# print('Altura em metros:', altura_metros)

# divisao_inteira = 10 // 3.0
# print(divisao_inteira)

# concatenacao = 'A' + ' ' + 'B'
# a_dez_vezes = 'A' * 10

# print(a_dez_vezes)
# print(concatenacao)

# altura = 1.95
# peso = 98
# imc = peso / altura ** 2

# # print(nome, sobrenome, "tem", altura,"de altura,")
# # print('pesa', peso,'quilos e seu IMC é')

# # print(imc)

# linha_1 = f'{nome} {sobrenome} tem {altura:.3f} de altura'
# # linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'
# print(linha_1)


#--------------------     . 
# a = 'AAAAA'
# b = 'BBBBBB'
# c = 1.18546
# string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
# formato = string.format(
#     nome1=a, nome2=b, nome3=c
# )
# # a é argumento, nome1 é parâmetro
# print(formato)
#--------------------     . 

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

# --------------------     .  
# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# int_numero_1 = int(numero_1)
# int_numero_2 = int(numero_2)

# print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
#--------------------     . 


#--------------------     . if, elif, else
# entrada = input('Você quer "entrar" ou "sair"? ')

# if entrada == 'entrar':
#     print('Você entrou no sistema')

#     print(12341234)
# elif entrada == 'sair':
#     print('Você saiu do sistema')
# else:
#     print('Você não digitou nem entrar e nem sair.')

# print('FORA DOS BLOCOS')
#--------------------     . 


#--------------------     . 

# condicao1 = False
# condicao2 = True
# condicao3 = True
# condicao4 = True

# if condicao1:
#     print('Código para condição 1')
#     print('Código para condição 1')
# elif condicao2:
#     print('Código para condição 2')
# elif condicao3:
#     print('Código para condição 3')
# elif condicao4:
#     print('Código para condição 4')
# else:
#     print('Nenhuma condição foi satisfeita.')

# if 10 == 10:
#     print('Outro if')

# print('Fora do if')

#--------------------     .  OPERATORS
"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
# maior = 2 > 1
# maior_ou_igual = 2 >= 2
# menor = 1 < 2
# menor_ou_igual = 2 <= 2
# igual = 'a' == 'a'
# diferente = 'a' != 'b'
# print('Olha meu print aqui')

### Pode digitar no terminal python -i nomearquivo.py, que ele abre o terminal interativo, no qual posso digitar o nome da variável, que ele mostra o valor. para sair, quit()

#--------------------     . 
# primeiro_valor = input('Digite um valor: ')
# segundo_valor = input('Digite outro valor: ')

# if primeiro_valor > segundo_valor:
#     print(f"primeiro_valor='{primeiro_valor}' é maior do que segundo_valor='{segundo_valor}")
# elif segundo_valor > primeiro_valor:
#     print(f"segundo_valor='{segundo_valor}' é maior do que primeiro_valor='{primeiro_valor}")
# else:
#     print(f"primeiro_valor='{primeiro_valor}' é igual ao segundo_valor='{segundo_valor}")
    
# if primeiro_valor > segundo_valor:
#     print(
#         f'{primeiro_valor} é maior '
#         f'do que {segundo_valor}'
#         )
# elif segundo_valor > primeiro_valor:
#     print(
#         f'{segundo_valor} é maior '
#         f'do que {primeiro_valor}'
#         )
# else:
#     print(f"primeiro_valor='{primeiro_valor}' é igual ao segundo_valor='{segundo_valor}")


#--------------------     . and or

# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)