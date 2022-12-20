import os

lista = []
item = ''
apagar = ''
lista_enumerada = None

while True:
    option = input('\nSelecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ')

    if option == 'i':
        os.system('cls')
        item = input('Digite o item para incluir: ')
        lista.append(item)
    elif option == 'a':
        os.system('cls')
        if len(lista) == 0:
            print('Não tem nada na lista ainda')
            continue
        try:
            apagar = int(input('Digite o índice do item para apagar: '))
            if apagar >= len(lista):
                print('Digitou um item que não existe. Digite l para ver a lista e saber o número')
                continue
            else:
                lista.pop(apagar)
        except ValueError:
            print('Por favor digite um número inteiro quando quiser excluir.')
    elif option == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Não tem nada na lista ainda')
        for i, k in enumerate(lista):
            print(i,k)
    elif option == 's':
        break
    else:
        print('Digitou errado. Digite, i, a, l ou s.')
