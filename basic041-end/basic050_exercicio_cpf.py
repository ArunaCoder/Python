cpf = '927.935.670'

# regular expression
import re

# Cálculo do primeiro dígito do CPF

# Remover ponto e traço
# cpf_numerico = cpf \
#     .replace('.','') \
#     .replace('-','')

entrada = input('CPF:')

primeiro_caractere_cpf = entrada[0]
repetido = primeiro_caractere_cpf * len(entrada)

if entrada == repetido:
    print("repetiu, digite de novo")
else:
    # Remover ponto e traço com expressão regular
    cpf_numerico = re.sub(
        r'[^0-9]',
        '',
        entrada
    )




    # remover dígitos informados
    cpf_numerico = cpf_numerico[:9] #pega de 0 a 8, ou seja, o 9 não é incluído

    # multiplicar cada um pelo valor correspondente da contagem regressiva a partir de 10

    contagem = 10
    aux_1 = 0

    for k in cpf_numerico:
        # multip = contagem * int(k)
        aux_1 = aux_1 + contagem * int(k)
        contagem -= 1
        # print(contagem,k)

    # multiplicar o resultado por 10 e depois achar o resto por 11
    aux_2 = aux_1 * 10
    aux_3 = aux_2 % 11

    # com o valor encontrado, estabelecer regra pro primeiro dígito
    primeiro_digito = 0 if aux_3 > 9 else aux_3

    # print(primeiro_digito)

    cpf_numerico_2 = cpf_numerico + str(primeiro_digito)


    contagem = 11
    aux_1 = 0

    for k in cpf_numerico_2:
        # multip = contagem * int(k)
        aux_1 = aux_1 + contagem * int(k)
        contagem -= 1
        # print(contagem,k)

    # multiplicar o resultado por 10 e depois achar o resto por 11
    aux_2 = aux_1 * 10
    aux_3 = aux_2 % 11

    # com o valor encontrado, estabelecer regra pro primeiro dígito
    segundo_digito = 0 if aux_3 > 9 else aux_3
    # print(cpf_numerico)

    cpf_numerico_final = cpf_numerico + str(primeiro_digito) + str(segundo_digito)

    print(cpf_numerico_final)