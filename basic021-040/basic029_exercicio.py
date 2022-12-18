frase = 'O Python é uma linguagem de programação' \
    'multiparadigma.' \
    'Python foi criado por Guido van Rossum.'

tamanho_frase = len(frase)
i = 0
letra = None
maior_letra = None
repete = 0
maior_repete = 0

# while i < tamanho_frase:
    # letra = frase[i]

    # if letra == ' ':
    #     i += 1
    #     continue

    # repete = frase.count(letra)

    # if repete > maior_repete:
    #     maior_letra = letra
    #     maior_repete = repete
    # i += 1


for letra in frase:
    if letra == ' ':
        continue

    repete = frase.count(letra)

    if repete > maior_repete:
        maior_letra = letra
        maior_repete = repete


print(f'A letra que mais repete é "{maior_letra}", que repete {maior_repete}x.')

