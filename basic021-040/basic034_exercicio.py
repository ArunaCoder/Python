palavra_secreta = 'eita'

tamanho_palavra_secreta = len(palavra_secreta)

palavra_desvendada = '*' * tamanho_palavra_secreta

palavra_montada = ''

letra_desvendada = ''

tentativas = 0

numeros = range(0,tamanho_palavra_secreta)

print(f'A palavra secreta é: {palavra_desvendada}',)

while palavra_desvendada != palavra_secreta:
    tentativa = input('Digite uma letra: ').lower()

    tentativas += 1

    if len(tentativa) == 0:
        print('Você não digitou nada. Tente de novo.')
        continue

    if len(tentativa) > 1:
        print('Digite apenas uma letra. Tente de novo.')
        continue

    if tentativa in palavra_desvendada:
        print('Essa letra já foi. Tente de novo.')
        continue



    if tentativa in palavra_secreta:
        palavra_montada = ''
        for i in numeros:
            letra_desvendada = palavra_desvendada[i]
            if letra_desvendada != '*':
                palavra_montada += letra_desvendada
                continue
            if tentativa == palavra_secreta[i]:
                palavra_montada += tentativa
            else:
                palavra_montada += '*'
        palavra_desvendada = palavra_montada
        print(f'Acertou! A palavra secreta é: {palavra_desvendada}\nTentativas: {tentativas}')
    else:
        print(f'Não acertou. Tente de novo\nTentativas: {tentativas}')


# if tentativa in palavra_secreta:
#     contador = 0
#     while contador < tamanho_palavra_secreta:
#         if tentativa == palavra_secreta[contador]:
#             palavra_desvendada = palavra_desvendada.replace(palavra_desvendada[contador],tentativa,1)
#             print(f'A palavra secreta é: {palavra_desvendada}')
#             contador += 1
#         else:
#             contador += 1
# else:
#     print('Errou. A palavra secreta é', palavra_desvendada)


print(f'Parabéns campeão, você acertou! A palavra secreta é {palavra_desvendada} ')