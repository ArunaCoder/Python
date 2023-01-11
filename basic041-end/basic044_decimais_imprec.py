import decimal #importa biblioteca para poder corrigir decimal impreciso

numero_1 = 0.1
numero_2 = 0.7
soma = numero_1 + numero_2
print(soma) # 0.7999999999999999

#--------------------     .

numero_1_preciso = decimal.Decimal('0.1')
numero_2_preciso = decimal.Decimal('0.7')
soma_precisa = numero_1_preciso + numero_2_preciso
print(soma_precisa) # 0.8
print(type(soma_precisa)) #decimal.Decimal
multipli = soma_precisa * 3
print(multipli) # 2.4