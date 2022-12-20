lista = ['Maria',  'João', 'Vera','Jose']

lista_enumerada = enumerate(lista)

print(lista_enumerada) # <enumerate object at 0x000002458EBD3600>
print(list(lista_enumerada)) # [(0, 'Maria'), (1, 'João'), (2, 'Vera'), (3, 'Jose')]

for item in lista_enumerada:
    print(item)

print('cade?')

# não dá pra acessar de novo, já esgotou a "lista_numerada"
for item in lista_enumerada:
    print(item)


# mas dá pra acessar direto
for item in enumerate(lista):
    print(item, 'ok')


# pra achar o índice
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# dá na mesma se fizer isso, pra achar o índice

for indice, nome in enumerate(lista):
    print(indice, nome)

# isso não funciona
# for indice, nome in lista:
#     print(indice, nome)

