nome = 'Joal Almeida Camargo Python'

tamanho_nome = len(nome)
nome_asterisco = ""

indice = 0

while indice < tamanho_nome:
    letra = nome[indice]
    nome_asterisco += f'*{letra}'
    indice += 1

print(nome_asterisco)