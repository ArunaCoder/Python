nome = "Joao"
sobrenome = "Silva"

divisao_inteira = 10 // 3.0
print(divisao_inteira)

concatenacao = 'A' + ' ' + 'B'
a_dez_vezes = 'A' * 10

print(a_dez_vezes)
print(concatenacao)

altura = 1.95
peso = 98
imc = peso / altura ** 2

print(nome, sobrenome, "tem", altura,"de altura,")
print('pesa', peso,'quilos e seu IMC é')

print(imc)

linha_1 = f'{nome} {sobrenome} tem {altura:.3f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'
print(linha_1)