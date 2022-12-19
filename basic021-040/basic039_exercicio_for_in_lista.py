"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']


#  minha solução
i = 0
for nome in lista:
    print(i,nome)
    i += 1

# solução do professor
indices = range(len(lista))
for indice in indices:
    print(indice,lista[indice])