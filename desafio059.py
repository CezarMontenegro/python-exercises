#Crie um programa que leia dois valores e mostre um menu na tela:

option = 0
n1 = int(input('Digite seu primeiro inteiro: '))
n2 = int(input('Digite seu segundo inteiro: '))

while option != 5:
    print('-=' * 20)
    print('[1]Somar')
    print('[2]Multiplicar')
    print('[3]Dividir')
    print('[4]Novos Números')
    print('[5]Sair do programa')
    print('-=' * 20)
    option = int(input('Digite uma opção: '))
    if option == 1:
        print(n1 + n2)
    elif option == 2:
        print(n1 * n2)
    elif option == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif option == 4:
        n1 = int(input('Digite seu primeiro inteiro: '))
        n2 = int(input('Digite seu segundo inteiro: '))