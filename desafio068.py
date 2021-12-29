#Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador PERDER, mostando 
# o total de vitórias consecutivas que ele conquistou no final 
# do jogo.

from random import randint

while True:
    print('Impar[1]')
    print('Par  [0]')
    user = int(input('Escolhar Impar ou Par: '))
    numero = int(input('Escolha um número entre 0 e 5: '))
    computer =  randint(0,5)
    print('-=' * 20)
    print(f'Você jogou {numero}')
    print(f'O computador jogou {computer}')
    if ((computer + numero) % 2) == 0 and user == 0:
        print(f'{computer} + {numero} é par! Você ganhou!')
    elif ((computer + numero) % 2) == 0 and user == 1:
        print(f'{computer} + {numero} é par! Você perdeu =(')
        break
    elif ((computer + numero) % 2) != 0 and user == 1:
        print(f'{computer} + {numero} é impar! Você ganhou!')
    elif ((computer + numero) % 2) != 0 and user == 0:
        print(f'{computer} + {numero} é impar! Você perdeu =(')
        break
    print('-=' * 20)

