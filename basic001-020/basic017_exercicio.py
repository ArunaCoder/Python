name = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = name[::-1]
espaco = ' '
if espaco in name:
    contem_espacos = 'Seu nome contém espaços'
else:
    contem_espacos = 'Seu nome não contém espaços'

if name and idade:
    print(f'Seu nome é {name}\nSeu nome invertido é {nome_invertido}\n{contem_espacos}\nSeu nome tem {len(name)} letras \nA primeira letra do seu nome é {name[0]}\nA última letra do seu nome é {name[-1]}')
else:
    print('Desculpe, você deixou campos vazios')
