#Crie um jogo de pedra, papel ou tesoura

import random
import time

itens = ['Pedra', 'Papel', 'Tesoura']

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

user = int(input('Qual a sua jogada? '))
computer = random.randint(0,2)

print('JO')
time.sleep(.5)
print('KEN')
time.sleep(.5)
print('PO')
time.sleep(.5)



print('-=' * 20)
print('Você jogou {}'.format(itens[user]))
print('O computador jogou {}'.format(itens[computer]))
print('-=' * 20)

if computer == 0:
    if user == 0:
        print('EMPATE')
    elif user == 1:
        print('VOCE PERDEU!')
    elif user == 2:
        print('VOCE GANHOU!')
elif computer == 1:
    if user == 1:
        print('EMPATE')
    elif user == 2:
        print('VOCE PERDEU!')
    elif user == 0:
        print('VOCE GANHOU!')
elif computer == 2:
    if user == 2:
        print('EMPATE')
    elif user == 1:
        print('VOCE PERDEU!')
    elif user == 0:
        print('VOCE GANHOU!')
    
